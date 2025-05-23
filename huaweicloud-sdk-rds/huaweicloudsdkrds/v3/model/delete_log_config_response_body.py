# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteLogConfigResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_configs': 'list[DeleteLogConfigs]'
    }

    attribute_map = {
        'log_configs': 'log_configs'
    }

    def __init__(self, log_configs=None):
        r"""DeleteLogConfigResponseBody

        The model defined in huaweicloud sdk

        :param log_configs: 实例日志配置信息。
        :type log_configs: list[:class:`huaweicloudsdkrds.v3.DeleteLogConfigs`]
        """
        
        

        self._log_configs = None
        self.discriminator = None

        self.log_configs = log_configs

    @property
    def log_configs(self):
        r"""Gets the log_configs of this DeleteLogConfigResponseBody.

        实例日志配置信息。

        :return: The log_configs of this DeleteLogConfigResponseBody.
        :rtype: list[:class:`huaweicloudsdkrds.v3.DeleteLogConfigs`]
        """
        return self._log_configs

    @log_configs.setter
    def log_configs(self, log_configs):
        r"""Sets the log_configs of this DeleteLogConfigResponseBody.

        实例日志配置信息。

        :param log_configs: The log_configs of this DeleteLogConfigResponseBody.
        :type log_configs: list[:class:`huaweicloudsdkrds.v3.DeleteLogConfigs`]
        """
        self._log_configs = log_configs

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
        if not isinstance(other, DeleteLogConfigResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
