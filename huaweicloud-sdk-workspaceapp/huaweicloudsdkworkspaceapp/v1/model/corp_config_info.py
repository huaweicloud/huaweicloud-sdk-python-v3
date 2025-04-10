# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CorpConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_key': 'str',
        'config_value': 'str'
    }

    attribute_map = {
        'config_key': 'config_key',
        'config_value': 'config_value'
    }

    def __init__(self, config_key=None, config_value=None):
        r"""CorpConfigInfo

        The model defined in huaweicloud sdk

        :param config_key: 查询的配置configKey。
        :type config_key: str
        :param config_value: 根据configKey查到的configValue。
        :type config_value: str
        """
        
        

        self._config_key = None
        self._config_value = None
        self.discriminator = None

        if config_key is not None:
            self.config_key = config_key
        if config_value is not None:
            self.config_value = config_value

    @property
    def config_key(self):
        r"""Gets the config_key of this CorpConfigInfo.

        查询的配置configKey。

        :return: The config_key of this CorpConfigInfo.
        :rtype: str
        """
        return self._config_key

    @config_key.setter
    def config_key(self, config_key):
        r"""Sets the config_key of this CorpConfigInfo.

        查询的配置configKey。

        :param config_key: The config_key of this CorpConfigInfo.
        :type config_key: str
        """
        self._config_key = config_key

    @property
    def config_value(self):
        r"""Gets the config_value of this CorpConfigInfo.

        根据configKey查到的configValue。

        :return: The config_value of this CorpConfigInfo.
        :rtype: str
        """
        return self._config_value

    @config_value.setter
    def config_value(self, config_value):
        r"""Sets the config_value of this CorpConfigInfo.

        根据configKey查到的configValue。

        :param config_value: The config_value of this CorpConfigInfo.
        :type config_value: str
        """
        self._config_value = config_value

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
        if not isinstance(other, CorpConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
