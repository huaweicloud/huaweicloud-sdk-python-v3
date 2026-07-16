# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsAgentMetricLabelValuesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'resource_id': 'str',
        'resource_type': 'str',
        'metric_name': 'str',
        'label_name': 'str',
        'filter': 'list[MetricFilterParam]'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'metric_name': 'metric_name',
        'label_name': 'label_name',
        'filter': 'filter'
    }

    def __init__(self, start_time=None, end_time=None, resource_id=None, resource_type=None, metric_name=None, label_name=None, filter=None):
        r"""ListOpsAgentMetricLabelValuesRequestBody

        The model defined in huaweicloud sdk

        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param resource_id: 智能体或工作流的id
        :type resource_id: str
        :param resource_type: 智能体类型 multiagents多智能体 workflow工作流 agent单智能体 office_ace
        :type resource_type: str
        :param metric_name: 组件名
        :type metric_name: str
        :param label_name: 维度名称
        :type label_name: str
        :param filter: 过滤条件
        :type filter: list[:class:`huaweicloudsdkagentarts.v1.MetricFilterParam`]
        """
        
        

        self._start_time = None
        self._end_time = None
        self._resource_id = None
        self._resource_type = None
        self._metric_name = None
        self._label_name = None
        self._filter = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.resource_id = resource_id
        self.resource_type = resource_type
        if metric_name is not None:
            self.metric_name = metric_name
        if label_name is not None:
            self.label_name = label_name
        if filter is not None:
            self.filter = filter

    @property
    def start_time(self):
        r"""Gets the start_time of this ListOpsAgentMetricLabelValuesRequestBody.

        开始时间

        :return: The start_time of this ListOpsAgentMetricLabelValuesRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListOpsAgentMetricLabelValuesRequestBody.

        开始时间

        :param start_time: The start_time of this ListOpsAgentMetricLabelValuesRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListOpsAgentMetricLabelValuesRequestBody.

        结束时间

        :return: The end_time of this ListOpsAgentMetricLabelValuesRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListOpsAgentMetricLabelValuesRequestBody.

        结束时间

        :param end_time: The end_time of this ListOpsAgentMetricLabelValuesRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListOpsAgentMetricLabelValuesRequestBody.

        智能体或工作流的id

        :return: The resource_id of this ListOpsAgentMetricLabelValuesRequestBody.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListOpsAgentMetricLabelValuesRequestBody.

        智能体或工作流的id

        :param resource_id: The resource_id of this ListOpsAgentMetricLabelValuesRequestBody.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListOpsAgentMetricLabelValuesRequestBody.

        智能体类型 multiagents多智能体 workflow工作流 agent单智能体 office_ace

        :return: The resource_type of this ListOpsAgentMetricLabelValuesRequestBody.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListOpsAgentMetricLabelValuesRequestBody.

        智能体类型 multiagents多智能体 workflow工作流 agent单智能体 office_ace

        :param resource_type: The resource_type of this ListOpsAgentMetricLabelValuesRequestBody.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ListOpsAgentMetricLabelValuesRequestBody.

        组件名

        :return: The metric_name of this ListOpsAgentMetricLabelValuesRequestBody.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ListOpsAgentMetricLabelValuesRequestBody.

        组件名

        :param metric_name: The metric_name of this ListOpsAgentMetricLabelValuesRequestBody.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def label_name(self):
        r"""Gets the label_name of this ListOpsAgentMetricLabelValuesRequestBody.

        维度名称

        :return: The label_name of this ListOpsAgentMetricLabelValuesRequestBody.
        :rtype: str
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        r"""Sets the label_name of this ListOpsAgentMetricLabelValuesRequestBody.

        维度名称

        :param label_name: The label_name of this ListOpsAgentMetricLabelValuesRequestBody.
        :type label_name: str
        """
        self._label_name = label_name

    @property
    def filter(self):
        r"""Gets the filter of this ListOpsAgentMetricLabelValuesRequestBody.

        过滤条件

        :return: The filter of this ListOpsAgentMetricLabelValuesRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.MetricFilterParam`]
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ListOpsAgentMetricLabelValuesRequestBody.

        过滤条件

        :param filter: The filter of this ListOpsAgentMetricLabelValuesRequestBody.
        :type filter: list[:class:`huaweicloudsdkagentarts.v1.MetricFilterParam`]
        """
        self._filter = filter

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
        if not isinstance(other, ListOpsAgentMetricLabelValuesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
