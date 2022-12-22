# coding: utf-8

from xml.etree import ElementTree as ET
from decimal import Decimal
import six
import re


class XmlTransfer:

    def __init__(self, encoding="UTF-8", resolve_attr=False):
        """Dict to xml, or xml to dict

        :param encoding: Default is 'utf-8'
        :param resolve_attr: Parse the attributes of the label
        :param with_head: Add the xml head when calling the method to_bytes/to_string
        """
        self._encoding = encoding
        self._resolve_attr = resolve_attr

    def to_bytes(self, _dict, head=False):
        if not _dict:
            return b''

        result = ET.tostring(self._dict_to_xml_element(_dict))
        if head:
            head = six.ensure_binary('<?xml version="1.0" encoding="%s" standalone="yes"?>' % self._encoding,
                                     self._encoding)
            result = head + result
        return result

    def to_string(self, _dict, head=False):
        return six.ensure_str(self.to_bytes(_dict, head), encoding=self._encoding)

    def _dict_to_xml_element(self, _dict):
        self._check_invalid_dict(_dict)

        root_name = list(_dict.keys())[0]
        value = _dict.get(root_name)
        root = ET.Element(root_name)

        str_value = self._to_string(value)
        if str_value is not None:
            root.text = str_value
        elif isinstance(value, dict):
            for k, v in value.items():
                self._make_element(root, k, v)
        else:
            raise ValueError("parse error: type " + type(value))
        return root

    def _make_element(self, element, key, value):
        if self._fill_element_attr_and_text(element, key, value):
            return

        str_value = self._to_string(value)
        if str_value is not None:
            ET.SubElement(element, key).text = str_value
        elif isinstance(value, list):
            for item in value:
                self._make_element(element, key, item)
        elif isinstance(value, dict):
            sub = ET.SubElement(element, key)
            for k, v in value.items():
                self._make_element(sub, k, v)
        else:
            ET.SubElement(element, key)

    def to_dict(self, string, ignore_root=False):
        _dict = {}
        if not string:
            return _dict

        root = ET.fromstring(string)
        self._handle_xmlns(root)
        key = root.tag
        text = self._get_text(root)
        if text:
            _dict[key] = text
            return _dict
        else:
            _dict[key] = {}
            for child in root:
                self._resolve_element(child, _dict[key])

        self._resolve_attrs(root, _dict)

        if ignore_root and _dict:
            return next(iter(_dict.values()))
        return _dict

    @classmethod
    def _handle_xmlns(cls, root):
        result = re.findall("({.+}).+", root.tag)
        if len(result) != 1:
            return
        xmlns = result[0]
        temp_dict = {"xmlns": xmlns[1:-1]}
        temp_dict.update(root.attrib)
        root.attrib = temp_dict

        def _process_tag(element):
            element.tag = element.tag.replace(xmlns, "")
            for child in element:
                _process_tag(child)

        _process_tag(root)

    def _resolve_element(self, element, data):
        if element.tag in data:
            if not isinstance(data[element.tag], list):
                data[element.tag] = [data[element.tag]]
            temp_dict = {}
            self._resolve_element(element, temp_dict)
            data[element.tag].append(temp_dict[element.tag])
        else:
            text = self._get_text(element)
            if text:
                data[element.tag] = text
            elif list(element):
                data[element.tag] = {}
                for child in element:
                    self._resolve_element(child, data[element.tag])
            else:
                data[element.tag] = None

            self._resolve_attrs(element, data)

    @classmethod
    def _check_invalid_dict(cls, _dict):
        if not isinstance(_dict, dict):
            raise TypeError("transfer error, not a dict")
        length = len(_dict)
        if length != 1:
            raise ValueError("there can be only one root node, current root node count: " + str(length))

    def _resolve_attrs(self, element, data):
        if not self._resolve_attr:
            return
        for name, value in element.attrib.items():
            if data[element.tag] is None:
                data[element.tag] = {}
            elif isinstance(data[element.tag], str):
                data[element.tag] = {"#text": data[element.tag]}
            data.setdefault(element.tag, {})["@" + name] = value

    @classmethod
    def _get_text(cls, element):
        if not element.text:
            return ""
        return element.text.strip()

    def _to_string(self, data):
        if isinstance(data, bool):
            return str(data).lower()
        elif isinstance(data, six.text_type):
            return six.ensure_str(data)
        elif isinstance(data, six.binary_type):
            return data.decode(self._encoding)
        elif isinstance(data, (float, Decimal) + six.integer_types):
            return str(data)
        else:
            return None

    def _fill_element_attr_and_text(self, element, key, value):
        flag = False
        if not self._resolve_attr:
            return flag

        if key.startswith("@"):
            element.set(key[1:], value)
            flag = True
        elif key == "#text":
            element.text = value
            flag = True
        return flag
