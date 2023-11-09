# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceConfig:

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
        'valid_values': 'str',
        'default_value': 'str',
        'config_type': 'str',
        'value': 'str',
        'value_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'valid_values': 'valid_values',
        'default_value': 'default_value',
        'config_type': 'config_type',
        'value': 'value',
        'value_type': 'value_type'
    }

    def __init__(self, name=None, valid_values=None, default_value=None, config_type=None, value=None, value_type=None):
        """InstanceConfig

        The model defined in huaweicloud sdk

        :param name: 配置名称。
        :type name: str
        :param valid_values: 有效值。
        :type valid_values: str
        :param default_value: 默认值。
        :type default_value: str
        :param config_type: 配置类型：static/dynamic。
        :type config_type: str
        :param value: 配置当前值。
        :type value: str
        :param value_type: 值类型。
        :type value_type: str
        """
        
        

        self._name = None
        self._valid_values = None
        self._default_value = None
        self._config_type = None
        self._value = None
        self._value_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if valid_values is not None:
            self.valid_values = valid_values
        if default_value is not None:
            self.default_value = default_value
        if config_type is not None:
            self.config_type = config_type
        if value is not None:
            self.value = value
        if value_type is not None:
            self.value_type = value_type

    @property
    def name(self):
        """Gets the name of this InstanceConfig.

        配置名称。

        :return: The name of this InstanceConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceConfig.

        配置名称。

        :param name: The name of this InstanceConfig.
        :type name: str
        """
        self._name = name

    @property
    def valid_values(self):
        """Gets the valid_values of this InstanceConfig.

        有效值。

        :return: The valid_values of this InstanceConfig.
        :rtype: str
        """
        return self._valid_values

    @valid_values.setter
    def valid_values(self, valid_values):
        """Sets the valid_values of this InstanceConfig.

        有效值。

        :param valid_values: The valid_values of this InstanceConfig.
        :type valid_values: str
        """
        self._valid_values = valid_values

    @property
    def default_value(self):
        """Gets the default_value of this InstanceConfig.

        默认值。

        :return: The default_value of this InstanceConfig.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this InstanceConfig.

        默认值。

        :param default_value: The default_value of this InstanceConfig.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def config_type(self):
        """Gets the config_type of this InstanceConfig.

        配置类型：static/dynamic。

        :return: The config_type of this InstanceConfig.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """Sets the config_type of this InstanceConfig.

        配置类型：static/dynamic。

        :param config_type: The config_type of this InstanceConfig.
        :type config_type: str
        """
        self._config_type = config_type

    @property
    def value(self):
        """Gets the value of this InstanceConfig.

        配置当前值。

        :return: The value of this InstanceConfig.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InstanceConfig.

        配置当前值。

        :param value: The value of this InstanceConfig.
        :type value: str
        """
        self._value = value

    @property
    def value_type(self):
        """Gets the value_type of this InstanceConfig.

        值类型。

        :return: The value_type of this InstanceConfig.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this InstanceConfig.

        值类型。

        :param value_type: The value_type of this InstanceConfig.
        :type value_type: str
        """
        self._value_type = value_type

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
        if not isinstance(other, InstanceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
