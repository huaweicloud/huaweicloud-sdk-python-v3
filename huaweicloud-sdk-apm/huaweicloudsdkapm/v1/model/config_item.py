# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_name': 'str',
        'config_value': 'str',
        'should_override': 'bool'
    }

    attribute_map = {
        'config_name': 'config_name',
        'config_value': 'config_value',
        'should_override': 'should_override'
    }

    def __init__(self, config_name=None, config_value=None, should_override=None):
        r"""ConfigItem

        The model defined in huaweicloud sdk

        :param config_name: 配置项名称。
        :type config_name: str
        :param config_value: 配置项值。
        :type config_value: str
        :param should_override: 是否重写。
        :type should_override: bool
        """
        
        

        self._config_name = None
        self._config_value = None
        self._should_override = None
        self.discriminator = None

        if config_name is not None:
            self.config_name = config_name
        if config_value is not None:
            self.config_value = config_value
        if should_override is not None:
            self.should_override = should_override

    @property
    def config_name(self):
        r"""Gets the config_name of this ConfigItem.

        配置项名称。

        :return: The config_name of this ConfigItem.
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        r"""Sets the config_name of this ConfigItem.

        配置项名称。

        :param config_name: The config_name of this ConfigItem.
        :type config_name: str
        """
        self._config_name = config_name

    @property
    def config_value(self):
        r"""Gets the config_value of this ConfigItem.

        配置项值。

        :return: The config_value of this ConfigItem.
        :rtype: str
        """
        return self._config_value

    @config_value.setter
    def config_value(self, config_value):
        r"""Sets the config_value of this ConfigItem.

        配置项值。

        :param config_value: The config_value of this ConfigItem.
        :type config_value: str
        """
        self._config_value = config_value

    @property
    def should_override(self):
        r"""Gets the should_override of this ConfigItem.

        是否重写。

        :return: The should_override of this ConfigItem.
        :rtype: bool
        """
        return self._should_override

    @should_override.setter
    def should_override(self, should_override):
        r"""Sets the should_override of this ConfigItem.

        是否重写。

        :param should_override: The should_override of this ConfigItem.
        :type should_override: bool
        """
        self._should_override = should_override

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
        if not isinstance(other, ConfigItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
