# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunObservabilityResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logs': 'CoreRunLogsConfigResp',
        'metrics': 'CoreRunMetricsObservabilityConfigResp',
        'tracing': 'CoreRunTracingObservabilityConfigResp'
    }

    attribute_map = {
        'logs': 'logs',
        'metrics': 'metrics',
        'tracing': 'tracing'
    }

    def __init__(self, logs=None, metrics=None, tracing=None):
        r"""CoreRunObservabilityResp

        The model defined in huaweicloud sdk

        :param logs: 
        :type logs: :class:`huaweicloudsdkagentarts.v1.CoreRunLogsConfigResp`
        :param metrics: 
        :type metrics: :class:`huaweicloudsdkagentarts.v1.CoreRunMetricsObservabilityConfigResp`
        :param tracing: 
        :type tracing: :class:`huaweicloudsdkagentarts.v1.CoreRunTracingObservabilityConfigResp`
        """
        
        

        self._logs = None
        self._metrics = None
        self._tracing = None
        self.discriminator = None

        if logs is not None:
            self.logs = logs
        if metrics is not None:
            self.metrics = metrics
        if tracing is not None:
            self.tracing = tracing

    @property
    def logs(self):
        r"""Gets the logs of this CoreRunObservabilityResp.

        :return: The logs of this CoreRunObservabilityResp.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunLogsConfigResp`
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        r"""Sets the logs of this CoreRunObservabilityResp.

        :param logs: The logs of this CoreRunObservabilityResp.
        :type logs: :class:`huaweicloudsdkagentarts.v1.CoreRunLogsConfigResp`
        """
        self._logs = logs

    @property
    def metrics(self):
        r"""Gets the metrics of this CoreRunObservabilityResp.

        :return: The metrics of this CoreRunObservabilityResp.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunMetricsObservabilityConfigResp`
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this CoreRunObservabilityResp.

        :param metrics: The metrics of this CoreRunObservabilityResp.
        :type metrics: :class:`huaweicloudsdkagentarts.v1.CoreRunMetricsObservabilityConfigResp`
        """
        self._metrics = metrics

    @property
    def tracing(self):
        r"""Gets the tracing of this CoreRunObservabilityResp.

        :return: The tracing of this CoreRunObservabilityResp.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunTracingObservabilityConfigResp`
        """
        return self._tracing

    @tracing.setter
    def tracing(self, tracing):
        r"""Sets the tracing of this CoreRunObservabilityResp.

        :param tracing: The tracing of this CoreRunObservabilityResp.
        :type tracing: :class:`huaweicloudsdkagentarts.v1.CoreRunTracingObservabilityConfigResp`
        """
        self._tracing = tracing

    def to_dict(self):
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
        if not isinstance(other, CoreRunObservabilityResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
