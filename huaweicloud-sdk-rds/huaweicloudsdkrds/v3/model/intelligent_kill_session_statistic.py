# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IntelligentKillSessionStatistic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keyword': 'str',
        'raw_sql_text': 'str',
        'ids': 'list[int]',
        'count': 'int',
        'total_time': 'float',
        'avg_time': 'float',
        'max_time': 'float',
        'strategy': 'str',
        'advice_concurrency': 'int',
        'type': 'str'
    }

    attribute_map = {
        'keyword': 'keyword',
        'raw_sql_text': 'raw_sql_text',
        'ids': 'ids',
        'count': 'count',
        'total_time': 'total_time',
        'avg_time': 'avg_time',
        'max_time': 'max_time',
        'strategy': 'strategy',
        'advice_concurrency': 'advice_concurrency',
        'type': 'type'
    }

    def __init__(self, keyword=None, raw_sql_text=None, ids=None, count=None, total_time=None, avg_time=None, max_time=None, strategy=None, advice_concurrency=None, type=None):
        r"""IntelligentKillSessionStatistic

        The model defined in huaweicloud sdk

        :param keyword: **参数解释**：  该类统计维度下提取到的限流关键字。  **约束限制**：  不涉及。
        :type keyword: str
        :param raw_sql_text: **参数解释**：  随机选取符合sql限流关键字的用户某条sql样例。  **约束限制**：  不涉及。
        :type raw_sql_text: str
        :param ids: **参数解释**：  符合该统计维度的线程id。  **约束限制**：  不涉及。
        :type ids: list[int]
        :param count: **参数解释**：  符合该统计维度的线程id总数量。  **约束限制**：  不涉及。
        :type count: int
        :param total_time: **参数解释**：  符合该统计维度的线程总执行时间。  **约束限制**：  不涉及。
        :type total_time: float
        :param avg_time: **参数解释**：  符合该统计维度的线程平均执行时间。  **约束限制**：  不涉及。
        :type avg_time: float
        :param max_time: **参数解释**：  符合该统计维度的线程最大执行时间。  **约束限制**：  不涉及。
        :type max_time: float
        :param strategy: **参数解释**：  统计维度。  **约束限制**：  不涉及。
        :type strategy: str
        :param advice_concurrency: **参数解释**：  推荐最大并发数。type为\&quot;kill\&quot;时该参数没有返回值。  **约束限制**：  不涉及。
        :type advice_concurrency: int
        :param type: **参数解释**：  该条维度数据的类型。\&quot;kill\&quot;表示当前统计时刻下一键kill会话下发后会kill该类会话；\&quot;limit\&quot;表示当前统计时刻下勾选\&quot;同步开启sql限流和添加规则\&quot;时会添加的规则。  **约束限制**：  不涉及。
        :type type: str
        """
        
        

        self._keyword = None
        self._raw_sql_text = None
        self._ids = None
        self._count = None
        self._total_time = None
        self._avg_time = None
        self._max_time = None
        self._strategy = None
        self._advice_concurrency = None
        self._type = None
        self.discriminator = None

        if keyword is not None:
            self.keyword = keyword
        if raw_sql_text is not None:
            self.raw_sql_text = raw_sql_text
        if ids is not None:
            self.ids = ids
        if count is not None:
            self.count = count
        if total_time is not None:
            self.total_time = total_time
        if avg_time is not None:
            self.avg_time = avg_time
        if max_time is not None:
            self.max_time = max_time
        if strategy is not None:
            self.strategy = strategy
        if advice_concurrency is not None:
            self.advice_concurrency = advice_concurrency
        if type is not None:
            self.type = type

    @property
    def keyword(self):
        r"""Gets the keyword of this IntelligentKillSessionStatistic.

        **参数解释**：  该类统计维度下提取到的限流关键字。  **约束限制**：  不涉及。

        :return: The keyword of this IntelligentKillSessionStatistic.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this IntelligentKillSessionStatistic.

        **参数解释**：  该类统计维度下提取到的限流关键字。  **约束限制**：  不涉及。

        :param keyword: The keyword of this IntelligentKillSessionStatistic.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def raw_sql_text(self):
        r"""Gets the raw_sql_text of this IntelligentKillSessionStatistic.

        **参数解释**：  随机选取符合sql限流关键字的用户某条sql样例。  **约束限制**：  不涉及。

        :return: The raw_sql_text of this IntelligentKillSessionStatistic.
        :rtype: str
        """
        return self._raw_sql_text

    @raw_sql_text.setter
    def raw_sql_text(self, raw_sql_text):
        r"""Sets the raw_sql_text of this IntelligentKillSessionStatistic.

        **参数解释**：  随机选取符合sql限流关键字的用户某条sql样例。  **约束限制**：  不涉及。

        :param raw_sql_text: The raw_sql_text of this IntelligentKillSessionStatistic.
        :type raw_sql_text: str
        """
        self._raw_sql_text = raw_sql_text

    @property
    def ids(self):
        r"""Gets the ids of this IntelligentKillSessionStatistic.

        **参数解释**：  符合该统计维度的线程id。  **约束限制**：  不涉及。

        :return: The ids of this IntelligentKillSessionStatistic.
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this IntelligentKillSessionStatistic.

        **参数解释**：  符合该统计维度的线程id。  **约束限制**：  不涉及。

        :param ids: The ids of this IntelligentKillSessionStatistic.
        :type ids: list[int]
        """
        self._ids = ids

    @property
    def count(self):
        r"""Gets the count of this IntelligentKillSessionStatistic.

        **参数解释**：  符合该统计维度的线程id总数量。  **约束限制**：  不涉及。

        :return: The count of this IntelligentKillSessionStatistic.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this IntelligentKillSessionStatistic.

        **参数解释**：  符合该统计维度的线程id总数量。  **约束限制**：  不涉及。

        :param count: The count of this IntelligentKillSessionStatistic.
        :type count: int
        """
        self._count = count

    @property
    def total_time(self):
        r"""Gets the total_time of this IntelligentKillSessionStatistic.

        **参数解释**：  符合该统计维度的线程总执行时间。  **约束限制**：  不涉及。

        :return: The total_time of this IntelligentKillSessionStatistic.
        :rtype: float
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        r"""Sets the total_time of this IntelligentKillSessionStatistic.

        **参数解释**：  符合该统计维度的线程总执行时间。  **约束限制**：  不涉及。

        :param total_time: The total_time of this IntelligentKillSessionStatistic.
        :type total_time: float
        """
        self._total_time = total_time

    @property
    def avg_time(self):
        r"""Gets the avg_time of this IntelligentKillSessionStatistic.

        **参数解释**：  符合该统计维度的线程平均执行时间。  **约束限制**：  不涉及。

        :return: The avg_time of this IntelligentKillSessionStatistic.
        :rtype: float
        """
        return self._avg_time

    @avg_time.setter
    def avg_time(self, avg_time):
        r"""Sets the avg_time of this IntelligentKillSessionStatistic.

        **参数解释**：  符合该统计维度的线程平均执行时间。  **约束限制**：  不涉及。

        :param avg_time: The avg_time of this IntelligentKillSessionStatistic.
        :type avg_time: float
        """
        self._avg_time = avg_time

    @property
    def max_time(self):
        r"""Gets the max_time of this IntelligentKillSessionStatistic.

        **参数解释**：  符合该统计维度的线程最大执行时间。  **约束限制**：  不涉及。

        :return: The max_time of this IntelligentKillSessionStatistic.
        :rtype: float
        """
        return self._max_time

    @max_time.setter
    def max_time(self, max_time):
        r"""Sets the max_time of this IntelligentKillSessionStatistic.

        **参数解释**：  符合该统计维度的线程最大执行时间。  **约束限制**：  不涉及。

        :param max_time: The max_time of this IntelligentKillSessionStatistic.
        :type max_time: float
        """
        self._max_time = max_time

    @property
    def strategy(self):
        r"""Gets the strategy of this IntelligentKillSessionStatistic.

        **参数解释**：  统计维度。  **约束限制**：  不涉及。

        :return: The strategy of this IntelligentKillSessionStatistic.
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        r"""Sets the strategy of this IntelligentKillSessionStatistic.

        **参数解释**：  统计维度。  **约束限制**：  不涉及。

        :param strategy: The strategy of this IntelligentKillSessionStatistic.
        :type strategy: str
        """
        self._strategy = strategy

    @property
    def advice_concurrency(self):
        r"""Gets the advice_concurrency of this IntelligentKillSessionStatistic.

        **参数解释**：  推荐最大并发数。type为\"kill\"时该参数没有返回值。  **约束限制**：  不涉及。

        :return: The advice_concurrency of this IntelligentKillSessionStatistic.
        :rtype: int
        """
        return self._advice_concurrency

    @advice_concurrency.setter
    def advice_concurrency(self, advice_concurrency):
        r"""Sets the advice_concurrency of this IntelligentKillSessionStatistic.

        **参数解释**：  推荐最大并发数。type为\"kill\"时该参数没有返回值。  **约束限制**：  不涉及。

        :param advice_concurrency: The advice_concurrency of this IntelligentKillSessionStatistic.
        :type advice_concurrency: int
        """
        self._advice_concurrency = advice_concurrency

    @property
    def type(self):
        r"""Gets the type of this IntelligentKillSessionStatistic.

        **参数解释**：  该条维度数据的类型。\"kill\"表示当前统计时刻下一键kill会话下发后会kill该类会话；\"limit\"表示当前统计时刻下勾选\"同步开启sql限流和添加规则\"时会添加的规则。  **约束限制**：  不涉及。

        :return: The type of this IntelligentKillSessionStatistic.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IntelligentKillSessionStatistic.

        **参数解释**：  该条维度数据的类型。\"kill\"表示当前统计时刻下一键kill会话下发后会kill该类会话；\"limit\"表示当前统计时刻下勾选\"同步开启sql限流和添加规则\"时会添加的规则。  **约束限制**：  不涉及。

        :param type: The type of this IntelligentKillSessionStatistic.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, IntelligentKillSessionStatistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
