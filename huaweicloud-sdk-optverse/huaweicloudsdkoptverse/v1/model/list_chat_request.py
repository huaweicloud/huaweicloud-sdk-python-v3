# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListChatRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'sort_dir': 'str',
        'title': 'str',
        'agent_type': 'str',
        'domain_type': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'sort_dir': 'sort_dir',
        'title': 'title',
        'agent_type': 'agent_type',
        'domain_type': 'domain_type',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, limit=None, offset=None, sort_dir=None, title=None, agent_type=None, domain_type=None, start_time=None, end_time=None):
        r"""ListChatRequest

        The model defined in huaweicloud sdk

        :param limit: **参数解释**： 限制量，单次查询总量。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,1000]。 **默认取值**： 100 
        :type limit: int
        :param offset: **参数解释**： 偏移量，查询起始偏移。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,100000000]。 **默认取值**： 0 
        :type offset: int
        :param sort_dir: **参数解释**： 排序规则。 **约束限制**： 不涉及 **取值范围**： - DESC：降序。 - ASC：升序。 **默认取值**： DESC 
        :type sort_dir: str
        :param title: **参数解释**： 对话名称，支持模糊搜索。 **约束限制**： 不涉及 **取值范围**： 取值范围为[1-500]个字符。 **默认取值**： 不涉及 
        :type title: str
        :param agent_type: **参数解释**： 对话名称，支持模糊搜索。 **约束限制**： 不涉及 **取值范围**： * optverse：天筹工具链 * predict：预测工具链 * demand：需求助手 **默认取值**： 不涉及 
        :type agent_type: str
        :param domain_type: **参数解释**： 领域类型，仅agent_type为optverse时生效。 **约束限制**： 不涉及 **取值范围**： * production-planning：生产计划 * sequence-planning：生产排程 * vrp：运输计划 * optverse：通用数学规划 **默认取值**： optverse
        :type domain_type: str
        :param start_time: **参数解释**： 筛选起始时间，按对话创建时间（create_time）过滤，包含边界。 **约束限制**： 不涉及 **取值范围**： Unix时间戳（秒级），例如：1789991522。 **默认取值**： 不涉及 
        :type start_time: str
        :param end_time: **参数解释**： 筛选结束时间，按对话创建时间（create_time）过滤，包含边界。 **约束限制**： 不涉及 **取值范围**： Unix时间戳（秒级），例如：1789991522。 **默认取值**： 不涉及 
        :type end_time: str
        """
        
        

        self._limit = None
        self._offset = None
        self._sort_dir = None
        self._title = None
        self._agent_type = None
        self._domain_type = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if title is not None:
            self.title = title
        if agent_type is not None:
            self.agent_type = agent_type
        if domain_type is not None:
            self.domain_type = domain_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListChatRequest.

        **参数解释**： 限制量，单次查询总量。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,1000]。 **默认取值**： 100 

        :return: The limit of this ListChatRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListChatRequest.

        **参数解释**： 限制量，单次查询总量。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,1000]。 **默认取值**： 100 

        :param limit: The limit of this ListChatRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListChatRequest.

        **参数解释**： 偏移量，查询起始偏移。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,100000000]。 **默认取值**： 0 

        :return: The offset of this ListChatRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListChatRequest.

        **参数解释**： 偏移量，查询起始偏移。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,100000000]。 **默认取值**： 0 

        :param offset: The offset of this ListChatRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListChatRequest.

        **参数解释**： 排序规则。 **约束限制**： 不涉及 **取值范围**： - DESC：降序。 - ASC：升序。 **默认取值**： DESC 

        :return: The sort_dir of this ListChatRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListChatRequest.

        **参数解释**： 排序规则。 **约束限制**： 不涉及 **取值范围**： - DESC：降序。 - ASC：升序。 **默认取值**： DESC 

        :param sort_dir: The sort_dir of this ListChatRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def title(self):
        r"""Gets the title of this ListChatRequest.

        **参数解释**： 对话名称，支持模糊搜索。 **约束限制**： 不涉及 **取值范围**： 取值范围为[1-500]个字符。 **默认取值**： 不涉及 

        :return: The title of this ListChatRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ListChatRequest.

        **参数解释**： 对话名称，支持模糊搜索。 **约束限制**： 不涉及 **取值范围**： 取值范围为[1-500]个字符。 **默认取值**： 不涉及 

        :param title: The title of this ListChatRequest.
        :type title: str
        """
        self._title = title

    @property
    def agent_type(self):
        r"""Gets the agent_type of this ListChatRequest.

        **参数解释**： 对话名称，支持模糊搜索。 **约束限制**： 不涉及 **取值范围**： * optverse：天筹工具链 * predict：预测工具链 * demand：需求助手 **默认取值**： 不涉及 

        :return: The agent_type of this ListChatRequest.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        r"""Sets the agent_type of this ListChatRequest.

        **参数解释**： 对话名称，支持模糊搜索。 **约束限制**： 不涉及 **取值范围**： * optverse：天筹工具链 * predict：预测工具链 * demand：需求助手 **默认取值**： 不涉及 

        :param agent_type: The agent_type of this ListChatRequest.
        :type agent_type: str
        """
        self._agent_type = agent_type

    @property
    def domain_type(self):
        r"""Gets the domain_type of this ListChatRequest.

        **参数解释**： 领域类型，仅agent_type为optverse时生效。 **约束限制**： 不涉及 **取值范围**： * production-planning：生产计划 * sequence-planning：生产排程 * vrp：运输计划 * optverse：通用数学规划 **默认取值**： optverse

        :return: The domain_type of this ListChatRequest.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        r"""Sets the domain_type of this ListChatRequest.

        **参数解释**： 领域类型，仅agent_type为optverse时生效。 **约束限制**： 不涉及 **取值范围**： * production-planning：生产计划 * sequence-planning：生产排程 * vrp：运输计划 * optverse：通用数学规划 **默认取值**： optverse

        :param domain_type: The domain_type of this ListChatRequest.
        :type domain_type: str
        """
        self._domain_type = domain_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ListChatRequest.

        **参数解释**： 筛选起始时间，按对话创建时间（create_time）过滤，包含边界。 **约束限制**： 不涉及 **取值范围**： Unix时间戳（秒级），例如：1789991522。 **默认取值**： 不涉及 

        :return: The start_time of this ListChatRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListChatRequest.

        **参数解释**： 筛选起始时间，按对话创建时间（create_time）过滤，包含边界。 **约束限制**： 不涉及 **取值范围**： Unix时间戳（秒级），例如：1789991522。 **默认取值**： 不涉及 

        :param start_time: The start_time of this ListChatRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListChatRequest.

        **参数解释**： 筛选结束时间，按对话创建时间（create_time）过滤，包含边界。 **约束限制**： 不涉及 **取值范围**： Unix时间戳（秒级），例如：1789991522。 **默认取值**： 不涉及 

        :return: The end_time of this ListChatRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListChatRequest.

        **参数解释**： 筛选结束时间，按对话创建时间（create_time）过滤，包含边界。 **约束限制**： 不涉及 **取值范围**： Unix时间戳（秒级），例如：1789991522。 **默认取值**： 不涉及 

        :param end_time: The end_time of this ListChatRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListChatRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
