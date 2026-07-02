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
        'example_sql_text': 'str',
        'ids': 'list[int]',
        'count': 'int',
        'total_time': 'float',
        'avg_time': 'float',
        'max_time': 'float',
        'strategy': 'str'
    }

    attribute_map = {
        'keyword': 'keyword',
        'example_sql_text': 'example_sql_text',
        'ids': 'ids',
        'count': 'count',
        'total_time': 'total_time',
        'avg_time': 'avg_time',
        'max_time': 'max_time',
        'strategy': 'strategy'
    }

    def __init__(self, keyword=None, example_sql_text=None, ids=None, count=None, total_time=None, avg_time=None, max_time=None, strategy=None):
        r"""IntelligentKillSessionStatistic

        The model defined in huaweicloud sdk

        :param keyword: **参数解释**：  预览智能Kill会话SQL模板关键字。  **取值范围**：  不涉及。
        :type keyword: str
        :param example_sql_text: **参数解释**：  预览智能Kill会话中的SQL模板命中的首个会话正在执行的SQL语句。  **取值范围**：  不涉及。
        :type example_sql_text: str
        :param ids: **参数解释**：  预览智能Kill会话中的SQL模板命中的会话线程ID列表。
        :type ids: list[int]
        :param count: **参数解释**：  预览智能Kill会话中的SQL模板命中的会话个数。  **取值范围**：  &gt;&#x3D;0。
        :type count: int
        :param total_time: **参数解释**：  预览智能Kill会话中的SQL模板命中的会话总执行时间，单位为秒。  **取值范围**：  &gt;&#x3D;0。
        :type total_time: float
        :param avg_time: **参数解释**：  预览智能Kill会话中的SQL模板命中的会话平均执行时间，单位为秒。  **取值范围**：  &gt;&#x3D;0。
        :type avg_time: float
        :param max_time: **参数解释**：  预览智能Kill会话中的SQL模板命中的会话中最长会话执行时间，单位为秒。  **取值范围**：  &gt;&#x3D;0。
        :type max_time: float
        :param strategy: **参数解释**：  预览智能Kill会话中的SQL模板命中Kill会话策略。  **取值范围**：  - top3_time: 以每组内会话最长的执行时长排序，选择排名前三的组内会话进行Kill。 - top3_count: 以每组内会话数量排序，选择排名前三的组内会话进行Kill。 - top3_avg_time: 以每组内会话平均执行时长排序，选择排名前三的组内会话进行Kill。
        :type strategy: str
        """
        
        

        self._keyword = None
        self._example_sql_text = None
        self._ids = None
        self._count = None
        self._total_time = None
        self._avg_time = None
        self._max_time = None
        self._strategy = None
        self.discriminator = None

        if keyword is not None:
            self.keyword = keyword
        if example_sql_text is not None:
            self.example_sql_text = example_sql_text
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

    @property
    def keyword(self):
        r"""Gets the keyword of this IntelligentKillSessionStatistic.

        **参数解释**：  预览智能Kill会话SQL模板关键字。  **取值范围**：  不涉及。

        :return: The keyword of this IntelligentKillSessionStatistic.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this IntelligentKillSessionStatistic.

        **参数解释**：  预览智能Kill会话SQL模板关键字。  **取值范围**：  不涉及。

        :param keyword: The keyword of this IntelligentKillSessionStatistic.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def example_sql_text(self):
        r"""Gets the example_sql_text of this IntelligentKillSessionStatistic.

        **参数解释**：  预览智能Kill会话中的SQL模板命中的首个会话正在执行的SQL语句。  **取值范围**：  不涉及。

        :return: The example_sql_text of this IntelligentKillSessionStatistic.
        :rtype: str
        """
        return self._example_sql_text

    @example_sql_text.setter
    def example_sql_text(self, example_sql_text):
        r"""Sets the example_sql_text of this IntelligentKillSessionStatistic.

        **参数解释**：  预览智能Kill会话中的SQL模板命中的首个会话正在执行的SQL语句。  **取值范围**：  不涉及。

        :param example_sql_text: The example_sql_text of this IntelligentKillSessionStatistic.
        :type example_sql_text: str
        """
        self._example_sql_text = example_sql_text

    @property
    def ids(self):
        r"""Gets the ids of this IntelligentKillSessionStatistic.

        **参数解释**：  预览智能Kill会话中的SQL模板命中的会话线程ID列表。

        :return: The ids of this IntelligentKillSessionStatistic.
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this IntelligentKillSessionStatistic.

        **参数解释**：  预览智能Kill会话中的SQL模板命中的会话线程ID列表。

        :param ids: The ids of this IntelligentKillSessionStatistic.
        :type ids: list[int]
        """
        self._ids = ids

    @property
    def count(self):
        r"""Gets the count of this IntelligentKillSessionStatistic.

        **参数解释**：  预览智能Kill会话中的SQL模板命中的会话个数。  **取值范围**：  >=0。

        :return: The count of this IntelligentKillSessionStatistic.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this IntelligentKillSessionStatistic.

        **参数解释**：  预览智能Kill会话中的SQL模板命中的会话个数。  **取值范围**：  >=0。

        :param count: The count of this IntelligentKillSessionStatistic.
        :type count: int
        """
        self._count = count

    @property
    def total_time(self):
        r"""Gets the total_time of this IntelligentKillSessionStatistic.

        **参数解释**：  预览智能Kill会话中的SQL模板命中的会话总执行时间，单位为秒。  **取值范围**：  >=0。

        :return: The total_time of this IntelligentKillSessionStatistic.
        :rtype: float
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        r"""Sets the total_time of this IntelligentKillSessionStatistic.

        **参数解释**：  预览智能Kill会话中的SQL模板命中的会话总执行时间，单位为秒。  **取值范围**：  >=0。

        :param total_time: The total_time of this IntelligentKillSessionStatistic.
        :type total_time: float
        """
        self._total_time = total_time

    @property
    def avg_time(self):
        r"""Gets the avg_time of this IntelligentKillSessionStatistic.

        **参数解释**：  预览智能Kill会话中的SQL模板命中的会话平均执行时间，单位为秒。  **取值范围**：  >=0。

        :return: The avg_time of this IntelligentKillSessionStatistic.
        :rtype: float
        """
        return self._avg_time

    @avg_time.setter
    def avg_time(self, avg_time):
        r"""Sets the avg_time of this IntelligentKillSessionStatistic.

        **参数解释**：  预览智能Kill会话中的SQL模板命中的会话平均执行时间，单位为秒。  **取值范围**：  >=0。

        :param avg_time: The avg_time of this IntelligentKillSessionStatistic.
        :type avg_time: float
        """
        self._avg_time = avg_time

    @property
    def max_time(self):
        r"""Gets the max_time of this IntelligentKillSessionStatistic.

        **参数解释**：  预览智能Kill会话中的SQL模板命中的会话中最长会话执行时间，单位为秒。  **取值范围**：  >=0。

        :return: The max_time of this IntelligentKillSessionStatistic.
        :rtype: float
        """
        return self._max_time

    @max_time.setter
    def max_time(self, max_time):
        r"""Sets the max_time of this IntelligentKillSessionStatistic.

        **参数解释**：  预览智能Kill会话中的SQL模板命中的会话中最长会话执行时间，单位为秒。  **取值范围**：  >=0。

        :param max_time: The max_time of this IntelligentKillSessionStatistic.
        :type max_time: float
        """
        self._max_time = max_time

    @property
    def strategy(self):
        r"""Gets the strategy of this IntelligentKillSessionStatistic.

        **参数解释**：  预览智能Kill会话中的SQL模板命中Kill会话策略。  **取值范围**：  - top3_time: 以每组内会话最长的执行时长排序，选择排名前三的组内会话进行Kill。 - top3_count: 以每组内会话数量排序，选择排名前三的组内会话进行Kill。 - top3_avg_time: 以每组内会话平均执行时长排序，选择排名前三的组内会话进行Kill。

        :return: The strategy of this IntelligentKillSessionStatistic.
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        r"""Sets the strategy of this IntelligentKillSessionStatistic.

        **参数解释**：  预览智能Kill会话中的SQL模板命中Kill会话策略。  **取值范围**：  - top3_time: 以每组内会话最长的执行时长排序，选择排名前三的组内会话进行Kill。 - top3_count: 以每组内会话数量排序，选择排名前三的组内会话进行Kill。 - top3_avg_time: 以每组内会话平均执行时长排序，选择排名前三的组内会话进行Kill。

        :param strategy: The strategy of this IntelligentKillSessionStatistic.
        :type strategy: str
        """
        self._strategy = strategy

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
