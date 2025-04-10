# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProxyConfigurationItem:

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
        'value': 'str',
        'elem_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'elem_type': 'elem_type'
    }

    def __init__(self, name=None, value=None, elem_type=None):
        r"""UpdateProxyConfigurationItem

        The model defined in huaweicloud sdk

        :param name: 参数名。
        :type name: str
        :param value: 参数值。
        :type value: str
        :param elem_type: 父标签类型。
        :type elem_type: str
        """
        
        

        self._name = None
        self._value = None
        self._elem_type = None
        self.discriminator = None

        self.name = name
        self.value = value
        self.elem_type = elem_type

    @property
    def name(self):
        r"""Gets the name of this UpdateProxyConfigurationItem.

        参数名。

        :return: The name of this UpdateProxyConfigurationItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateProxyConfigurationItem.

        参数名。

        :param name: The name of this UpdateProxyConfigurationItem.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this UpdateProxyConfigurationItem.

        参数值。

        :return: The value of this UpdateProxyConfigurationItem.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this UpdateProxyConfigurationItem.

        参数值。

        :param value: The value of this UpdateProxyConfigurationItem.
        :type value: str
        """
        self._value = value

    @property
    def elem_type(self):
        r"""Gets the elem_type of this UpdateProxyConfigurationItem.

        父标签类型。

        :return: The elem_type of this UpdateProxyConfigurationItem.
        :rtype: str
        """
        return self._elem_type

    @elem_type.setter
    def elem_type(self, elem_type):
        r"""Sets the elem_type of this UpdateProxyConfigurationItem.

        父标签类型。

        :param elem_type: The elem_type of this UpdateProxyConfigurationItem.
        :type elem_type: str
        """
        self._elem_type = elem_type

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
        if not isinstance(other, UpdateProxyConfigurationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
