# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePasswordlessConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_ips': 'list[str]'
    }

    attribute_map = {
        'config_ips': 'config_ips'
    }

    def __init__(self, config_ips=None):
        """UpdatePasswordlessConfigRequestBody

        The model defined in huaweicloud sdk

        :param config_ips: 要设置的免密配置,ip与网段的列表,空列表表示清空免密配置。
        :type config_ips: list[str]
        """
        
        

        self._config_ips = None
        self.discriminator = None

        self.config_ips = config_ips

    @property
    def config_ips(self):
        """Gets the config_ips of this UpdatePasswordlessConfigRequestBody.

        要设置的免密配置,ip与网段的列表,空列表表示清空免密配置。

        :return: The config_ips of this UpdatePasswordlessConfigRequestBody.
        :rtype: list[str]
        """
        return self._config_ips

    @config_ips.setter
    def config_ips(self, config_ips):
        """Sets the config_ips of this UpdatePasswordlessConfigRequestBody.

        要设置的免密配置,ip与网段的列表,空列表表示清空免密配置。

        :param config_ips: The config_ips of this UpdatePasswordlessConfigRequestBody.
        :type config_ips: list[str]
        """
        self._config_ips = config_ips

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
        if not isinstance(other, UpdatePasswordlessConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
