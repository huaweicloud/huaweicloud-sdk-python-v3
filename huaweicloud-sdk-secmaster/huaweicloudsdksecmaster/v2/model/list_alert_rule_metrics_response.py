# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlertRuleMetricsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cu_usage': 'CuUsage',
        'alert_severities': 'AlertSeverities',
        'metrics_status': 'MetricsStatus'
    }

    attribute_map = {
        'cu_usage': 'cu_usage',
        'alert_severities': 'alert_severities',
        'metrics_status': 'metrics_status'
    }

    def __init__(self, cu_usage=None, alert_severities=None, metrics_status=None):
        r"""ListAlertRuleMetricsResponse

        The model defined in huaweicloud sdk

        :param cu_usage: 
        :type cu_usage: :class:`huaweicloudsdksecmaster.v2.CuUsage`
        :param alert_severities: 
        :type alert_severities: :class:`huaweicloudsdksecmaster.v2.AlertSeverities`
        :param metrics_status: 
        :type metrics_status: :class:`huaweicloudsdksecmaster.v2.MetricsStatus`
        """
        
        super().__init__()

        self._cu_usage = None
        self._alert_severities = None
        self._metrics_status = None
        self.discriminator = None

        if cu_usage is not None:
            self.cu_usage = cu_usage
        if alert_severities is not None:
            self.alert_severities = alert_severities
        if metrics_status is not None:
            self.metrics_status = metrics_status

    @property
    def cu_usage(self):
        r"""Gets the cu_usage of this ListAlertRuleMetricsResponse.

        :return: The cu_usage of this ListAlertRuleMetricsResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.CuUsage`
        """
        return self._cu_usage

    @cu_usage.setter
    def cu_usage(self, cu_usage):
        r"""Sets the cu_usage of this ListAlertRuleMetricsResponse.

        :param cu_usage: The cu_usage of this ListAlertRuleMetricsResponse.
        :type cu_usage: :class:`huaweicloudsdksecmaster.v2.CuUsage`
        """
        self._cu_usage = cu_usage

    @property
    def alert_severities(self):
        r"""Gets the alert_severities of this ListAlertRuleMetricsResponse.

        :return: The alert_severities of this ListAlertRuleMetricsResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.AlertSeverities`
        """
        return self._alert_severities

    @alert_severities.setter
    def alert_severities(self, alert_severities):
        r"""Sets the alert_severities of this ListAlertRuleMetricsResponse.

        :param alert_severities: The alert_severities of this ListAlertRuleMetricsResponse.
        :type alert_severities: :class:`huaweicloudsdksecmaster.v2.AlertSeverities`
        """
        self._alert_severities = alert_severities

    @property
    def metrics_status(self):
        r"""Gets the metrics_status of this ListAlertRuleMetricsResponse.

        :return: The metrics_status of this ListAlertRuleMetricsResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.MetricsStatus`
        """
        return self._metrics_status

    @metrics_status.setter
    def metrics_status(self, metrics_status):
        r"""Sets the metrics_status of this ListAlertRuleMetricsResponse.

        :param metrics_status: The metrics_status of this ListAlertRuleMetricsResponse.
        :type metrics_status: :class:`huaweicloudsdksecmaster.v2.MetricsStatus`
        """
        self._metrics_status = metrics_status

    def to_dict(self):
        import warnings
        warnings.warn("ListAlertRuleMetricsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListAlertRuleMetricsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
