# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Config:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'value': 'str',
        'config_file_name': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'config_file_name': 'config_file_name'
    }

    def __init__(self, key=None, value=None, config_file_name=None):
        """Config

        The model defined in huaweicloud sdk

        :param key: 配置名，仅支持MRS组件配置页面上所展示的配置名。
        :type key: str
        :param value: 配置值
        :type value: str
        :param config_file_name: 配置文件名，仅支持MRS组件配置页面上所展示的文件名。
        :type config_file_name: str
        """
        
        

        self._key = None
        self._value = None
        self._config_file_name = None
        self.discriminator = None

        self.key = key
        self.value = value
        self.config_file_name = config_file_name

    @property
    def key(self):
        """Gets the key of this Config.

        配置名，仅支持MRS组件配置页面上所展示的配置名。

        :return: The key of this Config.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Config.

        配置名，仅支持MRS组件配置页面上所展示的配置名。

        :param key: The key of this Config.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this Config.

        配置值

        :return: The value of this Config.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Config.

        配置值

        :param value: The value of this Config.
        :type value: str
        """
        self._value = value

    @property
    def config_file_name(self):
        """Gets the config_file_name of this Config.

        配置文件名，仅支持MRS组件配置页面上所展示的文件名。

        :return: The config_file_name of this Config.
        :rtype: str
        """
        return self._config_file_name

    @config_file_name.setter
    def config_file_name(self, config_file_name):
        """Sets the config_file_name of this Config.

        配置文件名，仅支持MRS组件配置页面上所展示的文件名。

        :param config_file_name: The config_file_name of this Config.
        :type config_file_name: str
        """
        self._config_file_name = config_file_name

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
        if not isinstance(other, Config):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
