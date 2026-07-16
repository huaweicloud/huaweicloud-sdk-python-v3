# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsAgentSpanMetricResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_span_metric_list': 'list[AgentSpanMetricInfo]'
    }

    attribute_map = {
        'agent_span_metric_list': 'agent_span_metric_list'
    }

    def __init__(self, agent_span_metric_list=None):
        r"""ListOpsAgentSpanMetricResponse

        The model defined in huaweicloud sdk

        :param agent_span_metric_list: span列表
        :type agent_span_metric_list: list[:class:`huaweicloudsdkagentarts.v1.AgentSpanMetricInfo`]
        """
        
        super().__init__()

        self._agent_span_metric_list = None
        self.discriminator = None

        if agent_span_metric_list is not None:
            self.agent_span_metric_list = agent_span_metric_list

    @property
    def agent_span_metric_list(self):
        r"""Gets the agent_span_metric_list of this ListOpsAgentSpanMetricResponse.

        span列表

        :return: The agent_span_metric_list of this ListOpsAgentSpanMetricResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.AgentSpanMetricInfo`]
        """
        return self._agent_span_metric_list

    @agent_span_metric_list.setter
    def agent_span_metric_list(self, agent_span_metric_list):
        r"""Sets the agent_span_metric_list of this ListOpsAgentSpanMetricResponse.

        span列表

        :param agent_span_metric_list: The agent_span_metric_list of this ListOpsAgentSpanMetricResponse.
        :type agent_span_metric_list: list[:class:`huaweicloudsdkagentarts.v1.AgentSpanMetricInfo`]
        """
        self._agent_span_metric_list = agent_span_metric_list

    def to_dict(self):
        import warnings
        warnings.warn("ListOpsAgentSpanMetricResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOpsAgentSpanMetricResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
