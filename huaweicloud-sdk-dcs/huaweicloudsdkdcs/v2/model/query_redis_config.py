# coding: utf-8

import pprint
import re

import six





class QueryRedisConfig:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'param_value': 'str',
        'value_type': 'str',
        'value_range': 'str',
        'description': 'str',
        'default_value': 'str',
        'param_name': 'str',
        'param_id': 'int'
    }

    attribute_map = {
        'param_value': 'param_value',
        'value_type': 'value_type',
        'value_range': 'value_range',
        'description': 'description',
        'default_value': 'default_value',
        'param_name': 'param_name',
        'param_id': 'param_id'
    }

    def __init__(self, param_value=None, value_type=None, value_range=None, description=None, default_value=None, param_name=None, param_id=None):
        """QueryRedisConfig - a model defined in huaweicloud sdk"""
        
        

        self._param_value = None
        self._value_type = None
        self._value_range = None
        self._description = None
        self._default_value = None
        self._param_name = None
        self._param_id = None
        self.discriminator = None

        if param_value is not None:
            self.param_value = param_value
        if value_type is not None:
            self.value_type = value_type
        if value_range is not None:
            self.value_range = value_range
        if description is not None:
            self.description = description
        if default_value is not None:
            self.default_value = default_value
        if param_name is not None:
            self.param_name = param_name
        if param_id is not None:
            self.param_id = param_id

    @property
    def param_value(self):
        """Gets the param_value of this QueryRedisConfig.

        配置参数值。

        :return: The param_value of this QueryRedisConfig.
        :rtype: str
        """
        return self._param_value

    @param_value.setter
    def param_value(self, param_value):
        """Sets the param_value of this QueryRedisConfig.

        配置参数值。

        :param param_value: The param_value of this QueryRedisConfig.
        :type: str
        """
        self._param_value = param_value

    @property
    def value_type(self):
        """Gets the value_type of this QueryRedisConfig.

        配置参数的值类型。

        :return: The value_type of this QueryRedisConfig.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this QueryRedisConfig.

        配置参数的值类型。

        :param value_type: The value_type of this QueryRedisConfig.
        :type: str
        """
        self._value_type = value_type

    @property
    def value_range(self):
        """Gets the value_range of this QueryRedisConfig.

        配置参数的取值范围。

        :return: The value_range of this QueryRedisConfig.
        :rtype: str
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        """Sets the value_range of this QueryRedisConfig.

        配置参数的取值范围。

        :param value_range: The value_range of this QueryRedisConfig.
        :type: str
        """
        self._value_range = value_range

    @property
    def description(self):
        """Gets the description of this QueryRedisConfig.

        配置项的描述。

        :return: The description of this QueryRedisConfig.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueryRedisConfig.

        配置项的描述。

        :param description: The description of this QueryRedisConfig.
        :type: str
        """
        self._description = description

    @property
    def default_value(self):
        """Gets the default_value of this QueryRedisConfig.

        配置参数的默认值。

        :return: The default_value of this QueryRedisConfig.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this QueryRedisConfig.

        配置参数的默认值。

        :param default_value: The default_value of this QueryRedisConfig.
        :type: str
        """
        self._default_value = default_value

    @property
    def param_name(self):
        """Gets the param_name of this QueryRedisConfig.

        配置参数名称。

        :return: The param_name of this QueryRedisConfig.
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        """Sets the param_name of this QueryRedisConfig.

        配置参数名称。

        :param param_name: The param_name of this QueryRedisConfig.
        :type: str
        """
        self._param_name = param_name

    @property
    def param_id(self):
        """Gets the param_id of this QueryRedisConfig.

        配置参数ID。

        :return: The param_id of this QueryRedisConfig.
        :rtype: int
        """
        return self._param_id

    @param_id.setter
    def param_id(self, param_id):
        """Sets the param_id of this QueryRedisConfig.

        配置参数ID。

        :param param_id: The param_id of this QueryRedisConfig.
        :type: int
        """
        self._param_id = param_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QueryRedisConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
