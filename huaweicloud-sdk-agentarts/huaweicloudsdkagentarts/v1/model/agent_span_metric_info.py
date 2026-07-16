# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentSpanMetricInfo:

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
        'metric_total_value': 'int',
        'agent_metric_value_list': 'list[AgentSpanMetricValueInfo]'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'metric_total_value': 'metric_total_value',
        'agent_metric_value_list': 'agent_metric_value_list'
    }

    def __init__(self, metric_name=None, metric_total_value=None, agent_metric_value_list=None):
        r"""AgentSpanMetricInfo

        The model defined in huaweicloud sdk

        :param metric_name: 指标名称
        :type metric_name: str
        :param metric_total_value: 总数
        :type metric_total_value: int
        :param agent_metric_value_list: span列表
        :type agent_metric_value_list: list[:class:`huaweicloudsdkagentarts.v1.AgentSpanMetricValueInfo`]
        """
        
        

        self._metric_name = None
        self._metric_total_value = None
        self._agent_metric_value_list = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if metric_total_value is not None:
            self.metric_total_value = metric_total_value
        if agent_metric_value_list is not None:
            self.agent_metric_value_list = agent_metric_value_list

    @property
    def metric_name(self):
        r"""Gets the metric_name of this AgentSpanMetricInfo.

        指标名称

        :return: The metric_name of this AgentSpanMetricInfo.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this AgentSpanMetricInfo.

        指标名称

        :param metric_name: The metric_name of this AgentSpanMetricInfo.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def metric_total_value(self):
        r"""Gets the metric_total_value of this AgentSpanMetricInfo.

        总数

        :return: The metric_total_value of this AgentSpanMetricInfo.
        :rtype: int
        """
        return self._metric_total_value

    @metric_total_value.setter
    def metric_total_value(self, metric_total_value):
        r"""Sets the metric_total_value of this AgentSpanMetricInfo.

        总数

        :param metric_total_value: The metric_total_value of this AgentSpanMetricInfo.
        :type metric_total_value: int
        """
        self._metric_total_value = metric_total_value

    @property
    def agent_metric_value_list(self):
        r"""Gets the agent_metric_value_list of this AgentSpanMetricInfo.

        span列表

        :return: The agent_metric_value_list of this AgentSpanMetricInfo.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.AgentSpanMetricValueInfo`]
        """
        return self._agent_metric_value_list

    @agent_metric_value_list.setter
    def agent_metric_value_list(self, agent_metric_value_list):
        r"""Sets the agent_metric_value_list of this AgentSpanMetricInfo.

        span列表

        :param agent_metric_value_list: The agent_metric_value_list of this AgentSpanMetricInfo.
        :type agent_metric_value_list: list[:class:`huaweicloudsdkagentarts.v1.AgentSpanMetricValueInfo`]
        """
        self._agent_metric_value_list = agent_metric_value_list

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
        if not isinstance(other, AgentSpanMetricInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
