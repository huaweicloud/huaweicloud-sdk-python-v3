# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterLogConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ttl_in_days': 'int',
        'log_configs': 'list[ClusterLogConfigLogConfigs]'
    }

    attribute_map = {
        'ttl_in_days': 'ttl_in_days',
        'log_configs': 'log_configs'
    }

    def __init__(self, ttl_in_days=None, log_configs=None):
        """ClusterLogConfig

        The model defined in huaweicloud sdk

        :param ttl_in_days: 存储时长
        :type ttl_in_days: int
        :param log_configs: 日志配置项
        :type log_configs: list[:class:`huaweicloudsdkcce.v3.ClusterLogConfigLogConfigs`]
        """
        
        

        self._ttl_in_days = None
        self._log_configs = None
        self.discriminator = None

        if ttl_in_days is not None:
            self.ttl_in_days = ttl_in_days
        if log_configs is not None:
            self.log_configs = log_configs

    @property
    def ttl_in_days(self):
        """Gets the ttl_in_days of this ClusterLogConfig.

        存储时长

        :return: The ttl_in_days of this ClusterLogConfig.
        :rtype: int
        """
        return self._ttl_in_days

    @ttl_in_days.setter
    def ttl_in_days(self, ttl_in_days):
        """Sets the ttl_in_days of this ClusterLogConfig.

        存储时长

        :param ttl_in_days: The ttl_in_days of this ClusterLogConfig.
        :type ttl_in_days: int
        """
        self._ttl_in_days = ttl_in_days

    @property
    def log_configs(self):
        """Gets the log_configs of this ClusterLogConfig.

        日志配置项

        :return: The log_configs of this ClusterLogConfig.
        :rtype: list[:class:`huaweicloudsdkcce.v3.ClusterLogConfigLogConfigs`]
        """
        return self._log_configs

    @log_configs.setter
    def log_configs(self, log_configs):
        """Sets the log_configs of this ClusterLogConfig.

        日志配置项

        :param log_configs: The log_configs of this ClusterLogConfig.
        :type log_configs: list[:class:`huaweicloudsdkcce.v3.ClusterLogConfigLogConfigs`]
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
        if not isinstance(other, ClusterLogConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
