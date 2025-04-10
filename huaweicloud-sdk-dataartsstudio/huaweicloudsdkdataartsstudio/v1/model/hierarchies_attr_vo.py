# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HierarchiesAttrVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'hierarchies_id': 'str',
        'attr_id': 'str',
        'level': 'int',
        'attr_name_en': 'str',
        'attr_name_ch': 'str',
        'detail_attr_ids': 'list[str]',
        'detail_attr_name_ens': 'list[str]',
        'detail_attr_name_chs': 'list[str]',
        'attr': 'DimensionAttributeVO',
        'detail_attrs': 'list[DimensionAttributeVO]'
    }

    attribute_map = {
        'id': 'id',
        'hierarchies_id': 'hierarchies_id',
        'attr_id': 'attr_id',
        'level': 'level',
        'attr_name_en': 'attr_name_en',
        'attr_name_ch': 'attr_name_ch',
        'detail_attr_ids': 'detail_attr_ids',
        'detail_attr_name_ens': 'detail_attr_name_ens',
        'detail_attr_name_chs': 'detail_attr_name_chs',
        'attr': 'attr',
        'detail_attrs': 'detail_attrs'
    }

    def __init__(self, id=None, hierarchies_id=None, attr_id=None, level=None, attr_name_en=None, attr_name_ch=None, detail_attr_ids=None, detail_attr_name_ens=None, detail_attr_name_chs=None, attr=None, detail_attrs=None):
        r"""HierarchiesAttrVO

        The model defined in huaweicloud sdk

        :param id: 编码，ID字符串。
        :type id: str
        :param hierarchies_id: 层级ID，ID字符串。
        :type hierarchies_id: str
        :param attr_id: 属性ID，ID字符串。
        :type attr_id: str
        :param level: 层次。
        :type level: int
        :param attr_name_en: 引用属性编码。
        :type attr_name_en: str
        :param attr_name_ch: 引用属性名称，只读。
        :type attr_name_ch: str
        :param detail_attr_ids: 详情属性ID，ID字符串。
        :type detail_attr_ids: list[str]
        :param detail_attr_name_ens: 详情属性英文。
        :type detail_attr_name_ens: list[str]
        :param detail_attr_name_chs: 详情属性中文，只读。
        :type detail_attr_name_chs: list[str]
        :param attr: 
        :type attr: :class:`huaweicloudsdkdataartsstudio.v1.DimensionAttributeVO`
        :param detail_attrs: 详情字段，只读。
        :type detail_attrs: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionAttributeVO`]
        """
        
        

        self._id = None
        self._hierarchies_id = None
        self._attr_id = None
        self._level = None
        self._attr_name_en = None
        self._attr_name_ch = None
        self._detail_attr_ids = None
        self._detail_attr_name_ens = None
        self._detail_attr_name_chs = None
        self._attr = None
        self._detail_attrs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if hierarchies_id is not None:
            self.hierarchies_id = hierarchies_id
        if attr_id is not None:
            self.attr_id = attr_id
        if level is not None:
            self.level = level
        if attr_name_en is not None:
            self.attr_name_en = attr_name_en
        if attr_name_ch is not None:
            self.attr_name_ch = attr_name_ch
        if detail_attr_ids is not None:
            self.detail_attr_ids = detail_attr_ids
        if detail_attr_name_ens is not None:
            self.detail_attr_name_ens = detail_attr_name_ens
        if detail_attr_name_chs is not None:
            self.detail_attr_name_chs = detail_attr_name_chs
        if attr is not None:
            self.attr = attr
        if detail_attrs is not None:
            self.detail_attrs = detail_attrs

    @property
    def id(self):
        r"""Gets the id of this HierarchiesAttrVO.

        编码，ID字符串。

        :return: The id of this HierarchiesAttrVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HierarchiesAttrVO.

        编码，ID字符串。

        :param id: The id of this HierarchiesAttrVO.
        :type id: str
        """
        self._id = id

    @property
    def hierarchies_id(self):
        r"""Gets the hierarchies_id of this HierarchiesAttrVO.

        层级ID，ID字符串。

        :return: The hierarchies_id of this HierarchiesAttrVO.
        :rtype: str
        """
        return self._hierarchies_id

    @hierarchies_id.setter
    def hierarchies_id(self, hierarchies_id):
        r"""Sets the hierarchies_id of this HierarchiesAttrVO.

        层级ID，ID字符串。

        :param hierarchies_id: The hierarchies_id of this HierarchiesAttrVO.
        :type hierarchies_id: str
        """
        self._hierarchies_id = hierarchies_id

    @property
    def attr_id(self):
        r"""Gets the attr_id of this HierarchiesAttrVO.

        属性ID，ID字符串。

        :return: The attr_id of this HierarchiesAttrVO.
        :rtype: str
        """
        return self._attr_id

    @attr_id.setter
    def attr_id(self, attr_id):
        r"""Sets the attr_id of this HierarchiesAttrVO.

        属性ID，ID字符串。

        :param attr_id: The attr_id of this HierarchiesAttrVO.
        :type attr_id: str
        """
        self._attr_id = attr_id

    @property
    def level(self):
        r"""Gets the level of this HierarchiesAttrVO.

        层次。

        :return: The level of this HierarchiesAttrVO.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this HierarchiesAttrVO.

        层次。

        :param level: The level of this HierarchiesAttrVO.
        :type level: int
        """
        self._level = level

    @property
    def attr_name_en(self):
        r"""Gets the attr_name_en of this HierarchiesAttrVO.

        引用属性编码。

        :return: The attr_name_en of this HierarchiesAttrVO.
        :rtype: str
        """
        return self._attr_name_en

    @attr_name_en.setter
    def attr_name_en(self, attr_name_en):
        r"""Sets the attr_name_en of this HierarchiesAttrVO.

        引用属性编码。

        :param attr_name_en: The attr_name_en of this HierarchiesAttrVO.
        :type attr_name_en: str
        """
        self._attr_name_en = attr_name_en

    @property
    def attr_name_ch(self):
        r"""Gets the attr_name_ch of this HierarchiesAttrVO.

        引用属性名称，只读。

        :return: The attr_name_ch of this HierarchiesAttrVO.
        :rtype: str
        """
        return self._attr_name_ch

    @attr_name_ch.setter
    def attr_name_ch(self, attr_name_ch):
        r"""Sets the attr_name_ch of this HierarchiesAttrVO.

        引用属性名称，只读。

        :param attr_name_ch: The attr_name_ch of this HierarchiesAttrVO.
        :type attr_name_ch: str
        """
        self._attr_name_ch = attr_name_ch

    @property
    def detail_attr_ids(self):
        r"""Gets the detail_attr_ids of this HierarchiesAttrVO.

        详情属性ID，ID字符串。

        :return: The detail_attr_ids of this HierarchiesAttrVO.
        :rtype: list[str]
        """
        return self._detail_attr_ids

    @detail_attr_ids.setter
    def detail_attr_ids(self, detail_attr_ids):
        r"""Sets the detail_attr_ids of this HierarchiesAttrVO.

        详情属性ID，ID字符串。

        :param detail_attr_ids: The detail_attr_ids of this HierarchiesAttrVO.
        :type detail_attr_ids: list[str]
        """
        self._detail_attr_ids = detail_attr_ids

    @property
    def detail_attr_name_ens(self):
        r"""Gets the detail_attr_name_ens of this HierarchiesAttrVO.

        详情属性英文。

        :return: The detail_attr_name_ens of this HierarchiesAttrVO.
        :rtype: list[str]
        """
        return self._detail_attr_name_ens

    @detail_attr_name_ens.setter
    def detail_attr_name_ens(self, detail_attr_name_ens):
        r"""Sets the detail_attr_name_ens of this HierarchiesAttrVO.

        详情属性英文。

        :param detail_attr_name_ens: The detail_attr_name_ens of this HierarchiesAttrVO.
        :type detail_attr_name_ens: list[str]
        """
        self._detail_attr_name_ens = detail_attr_name_ens

    @property
    def detail_attr_name_chs(self):
        r"""Gets the detail_attr_name_chs of this HierarchiesAttrVO.

        详情属性中文，只读。

        :return: The detail_attr_name_chs of this HierarchiesAttrVO.
        :rtype: list[str]
        """
        return self._detail_attr_name_chs

    @detail_attr_name_chs.setter
    def detail_attr_name_chs(self, detail_attr_name_chs):
        r"""Sets the detail_attr_name_chs of this HierarchiesAttrVO.

        详情属性中文，只读。

        :param detail_attr_name_chs: The detail_attr_name_chs of this HierarchiesAttrVO.
        :type detail_attr_name_chs: list[str]
        """
        self._detail_attr_name_chs = detail_attr_name_chs

    @property
    def attr(self):
        r"""Gets the attr of this HierarchiesAttrVO.

        :return: The attr of this HierarchiesAttrVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DimensionAttributeVO`
        """
        return self._attr

    @attr.setter
    def attr(self, attr):
        r"""Sets the attr of this HierarchiesAttrVO.

        :param attr: The attr of this HierarchiesAttrVO.
        :type attr: :class:`huaweicloudsdkdataartsstudio.v1.DimensionAttributeVO`
        """
        self._attr = attr

    @property
    def detail_attrs(self):
        r"""Gets the detail_attrs of this HierarchiesAttrVO.

        详情字段，只读。

        :return: The detail_attrs of this HierarchiesAttrVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionAttributeVO`]
        """
        return self._detail_attrs

    @detail_attrs.setter
    def detail_attrs(self, detail_attrs):
        r"""Sets the detail_attrs of this HierarchiesAttrVO.

        详情字段，只读。

        :param detail_attrs: The detail_attrs of this HierarchiesAttrVO.
        :type detail_attrs: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionAttributeVO`]
        """
        self._detail_attrs = detail_attrs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HierarchiesAttrVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
