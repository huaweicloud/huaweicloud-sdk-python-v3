# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TelemetryConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metrics': 'Metric',
        'access_logging': 'AccessLogging',
        'tracing': 'Tracing'
    }

    attribute_map = {
        'metrics': 'metrics',
        'access_logging': 'accessLogging',
        'tracing': 'tracing'
    }

    def __init__(self, metrics=None, access_logging=None, tracing=None):
        r"""TelemetryConfig

        The model defined in huaweicloud sdk

        :param metrics: 
        :type metrics: :class:`huaweicloudsdkasm.v1.Metric`
        :param access_logging: 
        :type access_logging: :class:`huaweicloudsdkasm.v1.AccessLogging`
        :param tracing: 
        :type tracing: :class:`huaweicloudsdkasm.v1.Tracing`
        """
        
        

        self._metrics = None
        self._access_logging = None
        self._tracing = None
        self.discriminator = None

        if metrics is not None:
            self.metrics = metrics
        if access_logging is not None:
            self.access_logging = access_logging
        if tracing is not None:
            self.tracing = tracing

    @property
    def metrics(self):
        r"""Gets the metrics of this TelemetryConfig.

        :return: The metrics of this TelemetryConfig.
        :rtype: :class:`huaweicloudsdkasm.v1.Metric`
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this TelemetryConfig.

        :param metrics: The metrics of this TelemetryConfig.
        :type metrics: :class:`huaweicloudsdkasm.v1.Metric`
        """
        self._metrics = metrics

    @property
    def access_logging(self):
        r"""Gets the access_logging of this TelemetryConfig.

        :return: The access_logging of this TelemetryConfig.
        :rtype: :class:`huaweicloudsdkasm.v1.AccessLogging`
        """
        return self._access_logging

    @access_logging.setter
    def access_logging(self, access_logging):
        r"""Sets the access_logging of this TelemetryConfig.

        :param access_logging: The access_logging of this TelemetryConfig.
        :type access_logging: :class:`huaweicloudsdkasm.v1.AccessLogging`
        """
        self._access_logging = access_logging

    @property
    def tracing(self):
        r"""Gets the tracing of this TelemetryConfig.

        :return: The tracing of this TelemetryConfig.
        :rtype: :class:`huaweicloudsdkasm.v1.Tracing`
        """
        return self._tracing

    @tracing.setter
    def tracing(self, tracing):
        r"""Sets the tracing of this TelemetryConfig.

        :param tracing: The tracing of this TelemetryConfig.
        :type tracing: :class:`huaweicloudsdkasm.v1.Tracing`
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
        if not isinstance(other, TelemetryConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
