# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Attribute:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'data_type': 'str',
        'other_uses': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'data_type': 'data_type',
        'other_uses': 'other_uses'
    }

    def __init__(self, name=None, data_type=None, other_uses=None):
        r"""Attribute

        The model defined in huaweicloud sdk

        :param name: 名称。
        :type name: str
        :param data_type: 数据类型。
        :type data_type: str
        :param other_uses: 其他用途。
        :type other_uses: list[str]
        """
        
        

        self._name = None
        self._data_type = None
        self._other_uses = None
        self.discriminator = None

        self.name = name
        if data_type is not None:
            self.data_type = data_type
        if other_uses is not None:
            self.other_uses = other_uses

    @property
    def name(self):
        r"""Gets the name of this Attribute.

        名称。

        :return: The name of this Attribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Attribute.

        名称。

        :param name: The name of this Attribute.
        :type name: str
        """
        self._name = name

    @property
    def data_type(self):
        r"""Gets the data_type of this Attribute.

        数据类型。

        :return: The data_type of this Attribute.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this Attribute.

        数据类型。

        :param data_type: The data_type of this Attribute.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def other_uses(self):
        r"""Gets the other_uses of this Attribute.

        其他用途。

        :return: The other_uses of this Attribute.
        :rtype: list[str]
        """
        return self._other_uses

    @other_uses.setter
    def other_uses(self, other_uses):
        r"""Sets the other_uses of this Attribute.

        其他用途。

        :param other_uses: The other_uses of this Attribute.
        :type other_uses: list[str]
        """
        self._other_uses = other_uses

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
        if not isinstance(other, Attribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
