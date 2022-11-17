# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterServerMonitorRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'monitor_metrics': 'str'
    }

    attribute_map = {
        'monitor_metrics': 'monitorMetrics'
    }

    def __init__(self, monitor_metrics=None):
        """RegisterServerMonitorRequestBody

        The model defined in huaweicloud sdk

        :param monitor_metrics: 注册云服务器监控。
        :type monitor_metrics: str
        """
        
        

        self._monitor_metrics = None
        self.discriminator = None

        self.monitor_metrics = monitor_metrics

    @property
    def monitor_metrics(self):
        """Gets the monitor_metrics of this RegisterServerMonitorRequestBody.

        注册云服务器监控。

        :return: The monitor_metrics of this RegisterServerMonitorRequestBody.
        :rtype: str
        """
        return self._monitor_metrics

    @monitor_metrics.setter
    def monitor_metrics(self, monitor_metrics):
        """Sets the monitor_metrics of this RegisterServerMonitorRequestBody.

        注册云服务器监控。

        :param monitor_metrics: The monitor_metrics of this RegisterServerMonitorRequestBody.
        :type monitor_metrics: str
        """
        self._monitor_metrics = monitor_metrics

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
        if not isinstance(other, RegisterServerMonitorRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
