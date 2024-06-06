# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProxyConfiguration:

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
        'elem_type': 'str',
        'value_range': 'str',
        'value': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'data_type': 'data_type',
        'elem_type': 'elem_type',
        'value_range': 'value_range',
        'value': 'value',
        'description': 'description'
    }

    def __init__(self, name=None, data_type=None, elem_type=None, value_range=None, value=None, description=None):
        """ProxyConfiguration

        The model defined in huaweicloud sdk

        :param name: 参数名称
        :type name: str
        :param data_type: 参数数据类型
        :type data_type: str
        :param elem_type: 参数父标签类型
        :type elem_type: str
        :param value_range: 取值范围
        :type value_range: str
        :param value: 参数默认值
        :type value: str
        :param description: 参数描述
        :type description: str
        """
        
        

        self._name = None
        self._data_type = None
        self._elem_type = None
        self._value_range = None
        self._value = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if data_type is not None:
            self.data_type = data_type
        if elem_type is not None:
            self.elem_type = elem_type
        if value_range is not None:
            self.value_range = value_range
        if value is not None:
            self.value = value
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this ProxyConfiguration.

        参数名称

        :return: The name of this ProxyConfiguration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProxyConfiguration.

        参数名称

        :param name: The name of this ProxyConfiguration.
        :type name: str
        """
        self._name = name

    @property
    def data_type(self):
        """Gets the data_type of this ProxyConfiguration.

        参数数据类型

        :return: The data_type of this ProxyConfiguration.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ProxyConfiguration.

        参数数据类型

        :param data_type: The data_type of this ProxyConfiguration.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def elem_type(self):
        """Gets the elem_type of this ProxyConfiguration.

        参数父标签类型

        :return: The elem_type of this ProxyConfiguration.
        :rtype: str
        """
        return self._elem_type

    @elem_type.setter
    def elem_type(self, elem_type):
        """Sets the elem_type of this ProxyConfiguration.

        参数父标签类型

        :param elem_type: The elem_type of this ProxyConfiguration.
        :type elem_type: str
        """
        self._elem_type = elem_type

    @property
    def value_range(self):
        """Gets the value_range of this ProxyConfiguration.

        取值范围

        :return: The value_range of this ProxyConfiguration.
        :rtype: str
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        """Sets the value_range of this ProxyConfiguration.

        取值范围

        :param value_range: The value_range of this ProxyConfiguration.
        :type value_range: str
        """
        self._value_range = value_range

    @property
    def value(self):
        """Gets the value of this ProxyConfiguration.

        参数默认值

        :return: The value of this ProxyConfiguration.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ProxyConfiguration.

        参数默认值

        :param value: The value of this ProxyConfiguration.
        :type value: str
        """
        self._value = value

    @property
    def description(self):
        """Gets the description of this ProxyConfiguration.

        参数描述

        :return: The description of this ProxyConfiguration.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProxyConfiguration.

        参数描述

        :param description: The description of this ProxyConfiguration.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ProxyConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
