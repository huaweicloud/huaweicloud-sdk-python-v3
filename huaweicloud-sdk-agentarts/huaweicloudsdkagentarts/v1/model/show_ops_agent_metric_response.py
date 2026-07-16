# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsAgentMetricResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_agent_list': 'list[MetricResponse]'
    }

    attribute_map = {
        'metric_agent_list': 'metric_agent_list'
    }

    def __init__(self, metric_agent_list=None):
        r"""ShowOpsAgentMetricResponse

        The model defined in huaweicloud sdk

        :param metric_agent_list: 指标响应体信息
        :type metric_agent_list: list[:class:`huaweicloudsdkagentarts.v1.MetricResponse`]
        """
        
        super().__init__()

        self._metric_agent_list = None
        self.discriminator = None

        if metric_agent_list is not None:
            self.metric_agent_list = metric_agent_list

    @property
    def metric_agent_list(self):
        r"""Gets the metric_agent_list of this ShowOpsAgentMetricResponse.

        指标响应体信息

        :return: The metric_agent_list of this ShowOpsAgentMetricResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.MetricResponse`]
        """
        return self._metric_agent_list

    @metric_agent_list.setter
    def metric_agent_list(self, metric_agent_list):
        r"""Sets the metric_agent_list of this ShowOpsAgentMetricResponse.

        指标响应体信息

        :param metric_agent_list: The metric_agent_list of this ShowOpsAgentMetricResponse.
        :type metric_agent_list: list[:class:`huaweicloudsdkagentarts.v1.MetricResponse`]
        """
        self._metric_agent_list = metric_agent_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsAgentMetricResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOpsAgentMetricResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
