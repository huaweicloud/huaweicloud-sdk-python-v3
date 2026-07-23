# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsAgentMetricTypeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_by': 'list[str]',
        'start_time': 'str',
        'end_time': 'str',
        'metric_name': 'str',
        'resource_id': 'str',
        'resource_type': 'str',
        'user_id': 'str',
        'filter': 'list[MetricFilterParam]'
    }

    attribute_map = {
        'group_by': 'group_by',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'metric_name': 'metric_name',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'user_id': 'user_id',
        'filter': 'filter'
    }

    def __init__(self, group_by=None, start_time=None, end_time=None, metric_name=None, resource_id=None, resource_type=None, user_id=None, filter=None):
        r"""ShowOpsAgentMetricTypeRequestBody

        The model defined in huaweicloud sdk

        :param group_by: 分组名
        :type group_by: list[str]
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param metric_name: 指标名
        :type metric_name: str
        :param resource_id: 智能体或工作流的id
        :type resource_id: str
        :param resource_type: 智能体类型,agent单智能体,multiagents多智能体,workflow工作流,office_ace
        :type resource_type: str
        :param user_id: 用户id
        :type user_id: str
        :param filter: 过滤条件
        :type filter: list[:class:`huaweicloudsdkagentarts.v1.MetricFilterParam`]
        """
        
        

        self._group_by = None
        self._start_time = None
        self._end_time = None
        self._metric_name = None
        self._resource_id = None
        self._resource_type = None
        self._user_id = None
        self._filter = None
        self.discriminator = None

        if group_by is not None:
            self.group_by = group_by
        self.start_time = start_time
        self.end_time = end_time
        self.metric_name = metric_name
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if user_id is not None:
            self.user_id = user_id
        if filter is not None:
            self.filter = filter

    @property
    def group_by(self):
        r"""Gets the group_by of this ShowOpsAgentMetricTypeRequestBody.

        分组名

        :return: The group_by of this ShowOpsAgentMetricTypeRequestBody.
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this ShowOpsAgentMetricTypeRequestBody.

        分组名

        :param group_by: The group_by of this ShowOpsAgentMetricTypeRequestBody.
        :type group_by: list[str]
        """
        self._group_by = group_by

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowOpsAgentMetricTypeRequestBody.

        开始时间

        :return: The start_time of this ShowOpsAgentMetricTypeRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowOpsAgentMetricTypeRequestBody.

        开始时间

        :param start_time: The start_time of this ShowOpsAgentMetricTypeRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowOpsAgentMetricTypeRequestBody.

        结束时间

        :return: The end_time of this ShowOpsAgentMetricTypeRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowOpsAgentMetricTypeRequestBody.

        结束时间

        :param end_time: The end_time of this ShowOpsAgentMetricTypeRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowOpsAgentMetricTypeRequestBody.

        指标名

        :return: The metric_name of this ShowOpsAgentMetricTypeRequestBody.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowOpsAgentMetricTypeRequestBody.

        指标名

        :param metric_name: The metric_name of this ShowOpsAgentMetricTypeRequestBody.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ShowOpsAgentMetricTypeRequestBody.

        智能体或工作流的id

        :return: The resource_id of this ShowOpsAgentMetricTypeRequestBody.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ShowOpsAgentMetricTypeRequestBody.

        智能体或工作流的id

        :param resource_id: The resource_id of this ShowOpsAgentMetricTypeRequestBody.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ShowOpsAgentMetricTypeRequestBody.

        智能体类型,agent单智能体,multiagents多智能体,workflow工作流,office_ace

        :return: The resource_type of this ShowOpsAgentMetricTypeRequestBody.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ShowOpsAgentMetricTypeRequestBody.

        智能体类型,agent单智能体,multiagents多智能体,workflow工作流,office_ace

        :param resource_type: The resource_type of this ShowOpsAgentMetricTypeRequestBody.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowOpsAgentMetricTypeRequestBody.

        用户id

        :return: The user_id of this ShowOpsAgentMetricTypeRequestBody.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowOpsAgentMetricTypeRequestBody.

        用户id

        :param user_id: The user_id of this ShowOpsAgentMetricTypeRequestBody.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def filter(self):
        r"""Gets the filter of this ShowOpsAgentMetricTypeRequestBody.

        过滤条件

        :return: The filter of this ShowOpsAgentMetricTypeRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.MetricFilterParam`]
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ShowOpsAgentMetricTypeRequestBody.

        过滤条件

        :param filter: The filter of this ShowOpsAgentMetricTypeRequestBody.
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
        if not isinstance(other, ShowOpsAgentMetricTypeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
