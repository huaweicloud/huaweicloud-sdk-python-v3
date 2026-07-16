# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsAgentRuntLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_run_id': 'str',
        'log_type': 'str',
        'resource_type': 'str',
        'user_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'scroll_id': 'str',
        'keyword': 'str',
        'line_num': 'str',
        'is_desc': 'bool'
    }

    attribute_map = {
        'agent_run_id': 'agent_run_id',
        'log_type': 'log_type',
        'resource_type': 'resource_type',
        'user_id': 'user_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'scroll_id': 'scroll_id',
        'keyword': 'keyword',
        'line_num': 'line_num',
        'is_desc': 'is_desc'
    }

    def __init__(self, agent_run_id=None, log_type=None, resource_type=None, user_id=None, start_time=None, end_time=None, limit=None, scroll_id=None, keyword=None, line_num=None, is_desc=None):
        r"""ListOpsAgentRuntLogRequest

        The model defined in huaweicloud sdk

        :param agent_run_id: agent_run_id
        :type agent_run_id: str
        :param log_type: 开始时间戳
        :type log_type: str
        :param resource_type: 智能体类型,agent单智能体,multiagents,workflow工作流
        :type resource_type: str
        :param user_id: 用户id,兼容officeclaw场景传用户id
        :type user_id: str
        :param start_time: 开始时间戳
        :type start_time: str
        :param end_time: 结束时间戳
        :type end_time: str
        :param limit: 每次返回的数量
        :type limit: int
        :param scroll_id: 分页查询时，若上次查询的返回结果中包含字段scrollId，需要增加该字段参与分页查询
        :type scroll_id: str
        :param keyword: 关键字查询
        :type keyword: str
        :param line_num: 行数，首次为空，后面上一次的最后一个的line_num
        :type line_num: str
        :param is_desc: 参数解释：表示日志查询的顺序，当前支持顺序（false）或倒序查询（true）
        :type is_desc: bool
        """
        
        

        self._agent_run_id = None
        self._log_type = None
        self._resource_type = None
        self._user_id = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._scroll_id = None
        self._keyword = None
        self._line_num = None
        self._is_desc = None
        self.discriminator = None

        self.agent_run_id = agent_run_id
        if log_type is not None:
            self.log_type = log_type
        if resource_type is not None:
            self.resource_type = resource_type
        if user_id is not None:
            self.user_id = user_id
        self.start_time = start_time
        self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if scroll_id is not None:
            self.scroll_id = scroll_id
        if keyword is not None:
            self.keyword = keyword
        if line_num is not None:
            self.line_num = line_num
        if is_desc is not None:
            self.is_desc = is_desc

    @property
    def agent_run_id(self):
        r"""Gets the agent_run_id of this ListOpsAgentRuntLogRequest.

        agent_run_id

        :return: The agent_run_id of this ListOpsAgentRuntLogRequest.
        :rtype: str
        """
        return self._agent_run_id

    @agent_run_id.setter
    def agent_run_id(self, agent_run_id):
        r"""Sets the agent_run_id of this ListOpsAgentRuntLogRequest.

        agent_run_id

        :param agent_run_id: The agent_run_id of this ListOpsAgentRuntLogRequest.
        :type agent_run_id: str
        """
        self._agent_run_id = agent_run_id

    @property
    def log_type(self):
        r"""Gets the log_type of this ListOpsAgentRuntLogRequest.

        开始时间戳

        :return: The log_type of this ListOpsAgentRuntLogRequest.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        r"""Sets the log_type of this ListOpsAgentRuntLogRequest.

        开始时间戳

        :param log_type: The log_type of this ListOpsAgentRuntLogRequest.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListOpsAgentRuntLogRequest.

        智能体类型,agent单智能体,multiagents,workflow工作流

        :return: The resource_type of this ListOpsAgentRuntLogRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListOpsAgentRuntLogRequest.

        智能体类型,agent单智能体,multiagents,workflow工作流

        :param resource_type: The resource_type of this ListOpsAgentRuntLogRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def user_id(self):
        r"""Gets the user_id of this ListOpsAgentRuntLogRequest.

        用户id,兼容officeclaw场景传用户id

        :return: The user_id of this ListOpsAgentRuntLogRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ListOpsAgentRuntLogRequest.

        用户id,兼容officeclaw场景传用户id

        :param user_id: The user_id of this ListOpsAgentRuntLogRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListOpsAgentRuntLogRequest.

        开始时间戳

        :return: The start_time of this ListOpsAgentRuntLogRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListOpsAgentRuntLogRequest.

        开始时间戳

        :param start_time: The start_time of this ListOpsAgentRuntLogRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListOpsAgentRuntLogRequest.

        结束时间戳

        :return: The end_time of this ListOpsAgentRuntLogRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListOpsAgentRuntLogRequest.

        结束时间戳

        :param end_time: The end_time of this ListOpsAgentRuntLogRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListOpsAgentRuntLogRequest.

        每次返回的数量

        :return: The limit of this ListOpsAgentRuntLogRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOpsAgentRuntLogRequest.

        每次返回的数量

        :param limit: The limit of this ListOpsAgentRuntLogRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def scroll_id(self):
        r"""Gets the scroll_id of this ListOpsAgentRuntLogRequest.

        分页查询时，若上次查询的返回结果中包含字段scrollId，需要增加该字段参与分页查询

        :return: The scroll_id of this ListOpsAgentRuntLogRequest.
        :rtype: str
        """
        return self._scroll_id

    @scroll_id.setter
    def scroll_id(self, scroll_id):
        r"""Sets the scroll_id of this ListOpsAgentRuntLogRequest.

        分页查询时，若上次查询的返回结果中包含字段scrollId，需要增加该字段参与分页查询

        :param scroll_id: The scroll_id of this ListOpsAgentRuntLogRequest.
        :type scroll_id: str
        """
        self._scroll_id = scroll_id

    @property
    def keyword(self):
        r"""Gets the keyword of this ListOpsAgentRuntLogRequest.

        关键字查询

        :return: The keyword of this ListOpsAgentRuntLogRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ListOpsAgentRuntLogRequest.

        关键字查询

        :param keyword: The keyword of this ListOpsAgentRuntLogRequest.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def line_num(self):
        r"""Gets the line_num of this ListOpsAgentRuntLogRequest.

        行数，首次为空，后面上一次的最后一个的line_num

        :return: The line_num of this ListOpsAgentRuntLogRequest.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this ListOpsAgentRuntLogRequest.

        行数，首次为空，后面上一次的最后一个的line_num

        :param line_num: The line_num of this ListOpsAgentRuntLogRequest.
        :type line_num: str
        """
        self._line_num = line_num

    @property
    def is_desc(self):
        r"""Gets the is_desc of this ListOpsAgentRuntLogRequest.

        参数解释：表示日志查询的顺序，当前支持顺序（false）或倒序查询（true）

        :return: The is_desc of this ListOpsAgentRuntLogRequest.
        :rtype: bool
        """
        return self._is_desc

    @is_desc.setter
    def is_desc(self, is_desc):
        r"""Sets the is_desc of this ListOpsAgentRuntLogRequest.

        参数解释：表示日志查询的顺序，当前支持顺序（false）或倒序查询（true）

        :param is_desc: The is_desc of this ListOpsAgentRuntLogRequest.
        :type is_desc: bool
        """
        self._is_desc = is_desc

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
        if not isinstance(other, ListOpsAgentRuntLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
