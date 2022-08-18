# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TacticsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cron_configs': 'list[CronConfig]',
        'metric_configs': 'list[MetricConfig]'
    }

    attribute_map = {
        'cron_configs': 'cron_configs',
        'metric_configs': 'metric_configs'
    }

    def __init__(self, cron_configs=None, metric_configs=None):
        """TacticsConfig

        The model defined in huaweicloud sdk

        :param cron_configs: 定时配置列表
        :type cron_configs: list[:class:`huaweicloudsdkfunctiongraph.v2.CronConfig`]
        :param metric_configs: 流量配置列表
        :type metric_configs: list[:class:`huaweicloudsdkfunctiongraph.v2.MetricConfig`]
        """
        
        

        self._cron_configs = None
        self._metric_configs = None
        self.discriminator = None

        if cron_configs is not None:
            self.cron_configs = cron_configs
        if metric_configs is not None:
            self.metric_configs = metric_configs

    @property
    def cron_configs(self):
        """Gets the cron_configs of this TacticsConfig.

        定时配置列表

        :return: The cron_configs of this TacticsConfig.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.CronConfig`]
        """
        return self._cron_configs

    @cron_configs.setter
    def cron_configs(self, cron_configs):
        """Sets the cron_configs of this TacticsConfig.

        定时配置列表

        :param cron_configs: The cron_configs of this TacticsConfig.
        :type cron_configs: list[:class:`huaweicloudsdkfunctiongraph.v2.CronConfig`]
        """
        self._cron_configs = cron_configs

    @property
    def metric_configs(self):
        """Gets the metric_configs of this TacticsConfig.

        流量配置列表

        :return: The metric_configs of this TacticsConfig.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.MetricConfig`]
        """
        return self._metric_configs

    @metric_configs.setter
    def metric_configs(self, metric_configs):
        """Sets the metric_configs of this TacticsConfig.

        流量配置列表

        :param metric_configs: The metric_configs of this TacticsConfig.
        :type metric_configs: list[:class:`huaweicloudsdkfunctiongraph.v2.MetricConfig`]
        """
        self._metric_configs = metric_configs

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
        if not isinstance(other, TacticsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
