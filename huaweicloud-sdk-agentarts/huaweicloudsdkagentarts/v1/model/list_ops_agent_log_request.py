# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsAgentLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'trace_id': 'str',
        'span_id': 'str',
        'limit': 'int',
        'scroll_id': 'str',
        'keyword': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'trace_id': 'trace_id',
        'span_id': 'span_id',
        'limit': 'limit',
        'scroll_id': 'scroll_id',
        'keyword': 'keyword'
    }

    def __init__(self, agent_id=None, start_time=None, end_time=None, trace_id=None, span_id=None, limit=None, scroll_id=None, keyword=None):
        r"""ListOpsAgentLogRequest

        The model defined in huaweicloud sdk

        :param agent_id: agentId
        :type agent_id: str
        :param start_time: 开始时间戳
        :type start_time: str
        :param end_time: 结束时间戳
        :type end_time: str
        :param trace_id: 调用链id
        :type trace_id: str
        :param span_id: span id
        :type span_id: str
        :param limit: 每次返回的数量
        :type limit: int
        :param scroll_id: 分页查询时，若上次查询的返回结果中包含字段scrollId，需要增加该字段参与分页查询
        :type scroll_id: str
        :param keyword: 关键字查询
        :type keyword: str
        """
        
        

        self._agent_id = None
        self._start_time = None
        self._end_time = None
        self._trace_id = None
        self._span_id = None
        self._limit = None
        self._scroll_id = None
        self._keyword = None
        self.discriminator = None

        self.agent_id = agent_id
        self.start_time = start_time
        self.end_time = end_time
        if trace_id is not None:
            self.trace_id = trace_id
        if span_id is not None:
            self.span_id = span_id
        if limit is not None:
            self.limit = limit
        if scroll_id is not None:
            self.scroll_id = scroll_id
        if keyword is not None:
            self.keyword = keyword

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ListOpsAgentLogRequest.

        agentId

        :return: The agent_id of this ListOpsAgentLogRequest.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ListOpsAgentLogRequest.

        agentId

        :param agent_id: The agent_id of this ListOpsAgentLogRequest.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListOpsAgentLogRequest.

        开始时间戳

        :return: The start_time of this ListOpsAgentLogRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListOpsAgentLogRequest.

        开始时间戳

        :param start_time: The start_time of this ListOpsAgentLogRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListOpsAgentLogRequest.

        结束时间戳

        :return: The end_time of this ListOpsAgentLogRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListOpsAgentLogRequest.

        结束时间戳

        :param end_time: The end_time of this ListOpsAgentLogRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def trace_id(self):
        r"""Gets the trace_id of this ListOpsAgentLogRequest.

        调用链id

        :return: The trace_id of this ListOpsAgentLogRequest.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this ListOpsAgentLogRequest.

        调用链id

        :param trace_id: The trace_id of this ListOpsAgentLogRequest.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def span_id(self):
        r"""Gets the span_id of this ListOpsAgentLogRequest.

        span id

        :return: The span_id of this ListOpsAgentLogRequest.
        :rtype: str
        """
        return self._span_id

    @span_id.setter
    def span_id(self, span_id):
        r"""Sets the span_id of this ListOpsAgentLogRequest.

        span id

        :param span_id: The span_id of this ListOpsAgentLogRequest.
        :type span_id: str
        """
        self._span_id = span_id

    @property
    def limit(self):
        r"""Gets the limit of this ListOpsAgentLogRequest.

        每次返回的数量

        :return: The limit of this ListOpsAgentLogRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOpsAgentLogRequest.

        每次返回的数量

        :param limit: The limit of this ListOpsAgentLogRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def scroll_id(self):
        r"""Gets the scroll_id of this ListOpsAgentLogRequest.

        分页查询时，若上次查询的返回结果中包含字段scrollId，需要增加该字段参与分页查询

        :return: The scroll_id of this ListOpsAgentLogRequest.
        :rtype: str
        """
        return self._scroll_id

    @scroll_id.setter
    def scroll_id(self, scroll_id):
        r"""Sets the scroll_id of this ListOpsAgentLogRequest.

        分页查询时，若上次查询的返回结果中包含字段scrollId，需要增加该字段参与分页查询

        :param scroll_id: The scroll_id of this ListOpsAgentLogRequest.
        :type scroll_id: str
        """
        self._scroll_id = scroll_id

    @property
    def keyword(self):
        r"""Gets the keyword of this ListOpsAgentLogRequest.

        关键字查询

        :return: The keyword of this ListOpsAgentLogRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ListOpsAgentLogRequest.

        关键字查询

        :param keyword: The keyword of this ListOpsAgentLogRequest.
        :type keyword: str
        """
        self._keyword = keyword

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
        if not isinstance(other, ListOpsAgentLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
