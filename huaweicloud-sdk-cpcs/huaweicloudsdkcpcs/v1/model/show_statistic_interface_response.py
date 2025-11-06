# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatisticInterfaceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_name': 'str',
        'metrics': 'list[ShowStatisticInterfaceResponseBodyMetrics]'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'metrics': 'metrics'
    }

    def __init__(self, metric_name=None, metrics=None):
        r"""ShowStatisticInterfaceResponse

        The model defined in huaweicloud sdk

        :param metric_name: 资源名称
        :type metric_name: str
        :param metrics: 接口统计列表
        :type metrics: list[:class:`huaweicloudsdkcpcs.v1.ShowStatisticInterfaceResponseBodyMetrics`]
        """
        
        super().__init__()

        self._metric_name = None
        self._metrics = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if metrics is not None:
            self.metrics = metrics

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowStatisticInterfaceResponse.

        资源名称

        :return: The metric_name of this ShowStatisticInterfaceResponse.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowStatisticInterfaceResponse.

        资源名称

        :param metric_name: The metric_name of this ShowStatisticInterfaceResponse.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def metrics(self):
        r"""Gets the metrics of this ShowStatisticInterfaceResponse.

        接口统计列表

        :return: The metrics of this ShowStatisticInterfaceResponse.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.ShowStatisticInterfaceResponseBodyMetrics`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this ShowStatisticInterfaceResponse.

        接口统计列表

        :param metrics: The metrics of this ShowStatisticInterfaceResponse.
        :type metrics: list[:class:`huaweicloudsdkcpcs.v1.ShowStatisticInterfaceResponseBodyMetrics`]
        """
        self._metrics = metrics

    def to_dict(self):
        import warnings
        warnings.warn("ShowStatisticInterfaceResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowStatisticInterfaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
