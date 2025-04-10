# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RocketMQConfigResp:

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
        'config_type': 'str',
        'default_value': 'str',
        'valid_values': 'str',
        'value_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'config_type': 'config_type',
        'default_value': 'default_value',
        'valid_values': 'valid_values',
        'value_type': 'value_type'
    }

    def __init__(self, name=None, value=None, config_type=None, default_value=None, valid_values=None, value_type=None):
        r"""RocketMQConfigResp

        The model defined in huaweicloud sdk

        :param name: RocketMQ配置名称。
        :type name: str
        :param value: RocketMQ配置当前值。
        :type value: str
        :param config_type: RocketMQ配置的类型。
        :type config_type: str
        :param default_value: RocketMQ配置的默认值。
        :type default_value: str
        :param valid_values: RocketMQ配置取值的范围。
        :type valid_values: str
        :param value_type: RocketMQ配置值的类型。
        :type value_type: str
        """
        
        

        self._name = None
        self._value = None
        self._config_type = None
        self._default_value = None
        self._valid_values = None
        self._value_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if config_type is not None:
            self.config_type = config_type
        if default_value is not None:
            self.default_value = default_value
        if valid_values is not None:
            self.valid_values = valid_values
        if value_type is not None:
            self.value_type = value_type

    @property
    def name(self):
        r"""Gets the name of this RocketMQConfigResp.

        RocketMQ配置名称。

        :return: The name of this RocketMQConfigResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RocketMQConfigResp.

        RocketMQ配置名称。

        :param name: The name of this RocketMQConfigResp.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this RocketMQConfigResp.

        RocketMQ配置当前值。

        :return: The value of this RocketMQConfigResp.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this RocketMQConfigResp.

        RocketMQ配置当前值。

        :param value: The value of this RocketMQConfigResp.
        :type value: str
        """
        self._value = value

    @property
    def config_type(self):
        r"""Gets the config_type of this RocketMQConfigResp.

        RocketMQ配置的类型。

        :return: The config_type of this RocketMQConfigResp.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        r"""Sets the config_type of this RocketMQConfigResp.

        RocketMQ配置的类型。

        :param config_type: The config_type of this RocketMQConfigResp.
        :type config_type: str
        """
        self._config_type = config_type

    @property
    def default_value(self):
        r"""Gets the default_value of this RocketMQConfigResp.

        RocketMQ配置的默认值。

        :return: The default_value of this RocketMQConfigResp.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this RocketMQConfigResp.

        RocketMQ配置的默认值。

        :param default_value: The default_value of this RocketMQConfigResp.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def valid_values(self):
        r"""Gets the valid_values of this RocketMQConfigResp.

        RocketMQ配置取值的范围。

        :return: The valid_values of this RocketMQConfigResp.
        :rtype: str
        """
        return self._valid_values

    @valid_values.setter
    def valid_values(self, valid_values):
        r"""Sets the valid_values of this RocketMQConfigResp.

        RocketMQ配置取值的范围。

        :param valid_values: The valid_values of this RocketMQConfigResp.
        :type valid_values: str
        """
        self._valid_values = valid_values

    @property
    def value_type(self):
        r"""Gets the value_type of this RocketMQConfigResp.

        RocketMQ配置值的类型。

        :return: The value_type of this RocketMQConfigResp.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        r"""Sets the value_type of this RocketMQConfigResp.

        RocketMQ配置值的类型。

        :param value_type: The value_type of this RocketMQConfigResp.
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
        if not isinstance(other, RocketMQConfigResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
