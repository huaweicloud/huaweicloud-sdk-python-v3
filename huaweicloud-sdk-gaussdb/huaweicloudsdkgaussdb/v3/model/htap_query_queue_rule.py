# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HtapQueryQueueRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query_queue_max_queued_queries': 'int',
        'query_queue_pending_timeout_second': 'int',
        'query_queue_concurrency_limit': 'int',
        'query_queue_mem_used_pct_limit': 'int',
        'query_queue_cpu_used_pct_limit': 'int',
        'enable_query_queue_select': 'str'
    }

    attribute_map = {
        'query_queue_max_queued_queries': 'query_queue_max_queued_queries',
        'query_queue_pending_timeout_second': 'query_queue_pending_timeout_second',
        'query_queue_concurrency_limit': 'query_queue_concurrency_limit',
        'query_queue_mem_used_pct_limit': 'query_queue_mem_used_pct_limit',
        'query_queue_cpu_used_pct_limit': 'query_queue_cpu_used_pct_limit',
        'enable_query_queue_select': 'enable_query_queue_select'
    }

    def __init__(self, query_queue_max_queued_queries=None, query_queue_pending_timeout_second=None, query_queue_concurrency_limit=None, query_queue_mem_used_pct_limit=None, query_queue_cpu_used_pct_limit=None, enable_query_queue_select=None):
        r"""HtapQueryQueueRule

        The model defined in huaweicloud sdk

        :param query_queue_max_queued_queries: **参数解释**：  查询队列中的查询数量上限。  **约束限制**：  不涉及。  **取值范围**：  非负整数。  **默认值**：  1024。
        :type query_queue_max_queued_queries: int
        :param query_queue_pending_timeout_second: **参数解释**：  查询阻塞时间上限。  **约束限制**：  不涉及。  **取值范围**：  非负整数。  **默认值**：  300。
        :type query_queue_pending_timeout_second: int
        :param query_queue_concurrency_limit: **参数解释**：  查询队列并发值。  **约束限制**：  不涉及。  **取值范围**：  0~100的整数，0表示没有限制。  **默认值**：  0。
        :type query_queue_concurrency_limit: int
        :param query_queue_mem_used_pct_limit: **参数解释**：  内存使用百分比。  **约束限制**：  不涉及。  **取值范围**：  0~100的整数，0表示没有限制。  **默认值**：  0。
        :type query_queue_mem_used_pct_limit: int
        :param query_queue_cpu_used_pct_limit: **参数解释**：  CPU使用百分比。  **约束限制**：  不涉及。  **取值范围**：  0~100的整数，0表示没有限制。  **默认值**：  0。
        :type query_queue_cpu_used_pct_limit: int
        :param enable_query_queue_select: **参数解释**：  查询队列开关状态。  **约束限制**：  不涉及。  **取值范围**：  - true：表示开启。 - false：表示关闭。  **默认值**：  false。
        :type enable_query_queue_select: str
        """
        
        

        self._query_queue_max_queued_queries = None
        self._query_queue_pending_timeout_second = None
        self._query_queue_concurrency_limit = None
        self._query_queue_mem_used_pct_limit = None
        self._query_queue_cpu_used_pct_limit = None
        self._enable_query_queue_select = None
        self.discriminator = None

        self.query_queue_max_queued_queries = query_queue_max_queued_queries
        self.query_queue_pending_timeout_second = query_queue_pending_timeout_second
        self.query_queue_concurrency_limit = query_queue_concurrency_limit
        self.query_queue_mem_used_pct_limit = query_queue_mem_used_pct_limit
        self.query_queue_cpu_used_pct_limit = query_queue_cpu_used_pct_limit
        if enable_query_queue_select is not None:
            self.enable_query_queue_select = enable_query_queue_select

    @property
    def query_queue_max_queued_queries(self):
        r"""Gets the query_queue_max_queued_queries of this HtapQueryQueueRule.

        **参数解释**：  查询队列中的查询数量上限。  **约束限制**：  不涉及。  **取值范围**：  非负整数。  **默认值**：  1024。

        :return: The query_queue_max_queued_queries of this HtapQueryQueueRule.
        :rtype: int
        """
        return self._query_queue_max_queued_queries

    @query_queue_max_queued_queries.setter
    def query_queue_max_queued_queries(self, query_queue_max_queued_queries):
        r"""Sets the query_queue_max_queued_queries of this HtapQueryQueueRule.

        **参数解释**：  查询队列中的查询数量上限。  **约束限制**：  不涉及。  **取值范围**：  非负整数。  **默认值**：  1024。

        :param query_queue_max_queued_queries: The query_queue_max_queued_queries of this HtapQueryQueueRule.
        :type query_queue_max_queued_queries: int
        """
        self._query_queue_max_queued_queries = query_queue_max_queued_queries

    @property
    def query_queue_pending_timeout_second(self):
        r"""Gets the query_queue_pending_timeout_second of this HtapQueryQueueRule.

        **参数解释**：  查询阻塞时间上限。  **约束限制**：  不涉及。  **取值范围**：  非负整数。  **默认值**：  300。

        :return: The query_queue_pending_timeout_second of this HtapQueryQueueRule.
        :rtype: int
        """
        return self._query_queue_pending_timeout_second

    @query_queue_pending_timeout_second.setter
    def query_queue_pending_timeout_second(self, query_queue_pending_timeout_second):
        r"""Sets the query_queue_pending_timeout_second of this HtapQueryQueueRule.

        **参数解释**：  查询阻塞时间上限。  **约束限制**：  不涉及。  **取值范围**：  非负整数。  **默认值**：  300。

        :param query_queue_pending_timeout_second: The query_queue_pending_timeout_second of this HtapQueryQueueRule.
        :type query_queue_pending_timeout_second: int
        """
        self._query_queue_pending_timeout_second = query_queue_pending_timeout_second

    @property
    def query_queue_concurrency_limit(self):
        r"""Gets the query_queue_concurrency_limit of this HtapQueryQueueRule.

        **参数解释**：  查询队列并发值。  **约束限制**：  不涉及。  **取值范围**：  0~100的整数，0表示没有限制。  **默认值**：  0。

        :return: The query_queue_concurrency_limit of this HtapQueryQueueRule.
        :rtype: int
        """
        return self._query_queue_concurrency_limit

    @query_queue_concurrency_limit.setter
    def query_queue_concurrency_limit(self, query_queue_concurrency_limit):
        r"""Sets the query_queue_concurrency_limit of this HtapQueryQueueRule.

        **参数解释**：  查询队列并发值。  **约束限制**：  不涉及。  **取值范围**：  0~100的整数，0表示没有限制。  **默认值**：  0。

        :param query_queue_concurrency_limit: The query_queue_concurrency_limit of this HtapQueryQueueRule.
        :type query_queue_concurrency_limit: int
        """
        self._query_queue_concurrency_limit = query_queue_concurrency_limit

    @property
    def query_queue_mem_used_pct_limit(self):
        r"""Gets the query_queue_mem_used_pct_limit of this HtapQueryQueueRule.

        **参数解释**：  内存使用百分比。  **约束限制**：  不涉及。  **取值范围**：  0~100的整数，0表示没有限制。  **默认值**：  0。

        :return: The query_queue_mem_used_pct_limit of this HtapQueryQueueRule.
        :rtype: int
        """
        return self._query_queue_mem_used_pct_limit

    @query_queue_mem_used_pct_limit.setter
    def query_queue_mem_used_pct_limit(self, query_queue_mem_used_pct_limit):
        r"""Sets the query_queue_mem_used_pct_limit of this HtapQueryQueueRule.

        **参数解释**：  内存使用百分比。  **约束限制**：  不涉及。  **取值范围**：  0~100的整数，0表示没有限制。  **默认值**：  0。

        :param query_queue_mem_used_pct_limit: The query_queue_mem_used_pct_limit of this HtapQueryQueueRule.
        :type query_queue_mem_used_pct_limit: int
        """
        self._query_queue_mem_used_pct_limit = query_queue_mem_used_pct_limit

    @property
    def query_queue_cpu_used_pct_limit(self):
        r"""Gets the query_queue_cpu_used_pct_limit of this HtapQueryQueueRule.

        **参数解释**：  CPU使用百分比。  **约束限制**：  不涉及。  **取值范围**：  0~100的整数，0表示没有限制。  **默认值**：  0。

        :return: The query_queue_cpu_used_pct_limit of this HtapQueryQueueRule.
        :rtype: int
        """
        return self._query_queue_cpu_used_pct_limit

    @query_queue_cpu_used_pct_limit.setter
    def query_queue_cpu_used_pct_limit(self, query_queue_cpu_used_pct_limit):
        r"""Sets the query_queue_cpu_used_pct_limit of this HtapQueryQueueRule.

        **参数解释**：  CPU使用百分比。  **约束限制**：  不涉及。  **取值范围**：  0~100的整数，0表示没有限制。  **默认值**：  0。

        :param query_queue_cpu_used_pct_limit: The query_queue_cpu_used_pct_limit of this HtapQueryQueueRule.
        :type query_queue_cpu_used_pct_limit: int
        """
        self._query_queue_cpu_used_pct_limit = query_queue_cpu_used_pct_limit

    @property
    def enable_query_queue_select(self):
        r"""Gets the enable_query_queue_select of this HtapQueryQueueRule.

        **参数解释**：  查询队列开关状态。  **约束限制**：  不涉及。  **取值范围**：  - true：表示开启。 - false：表示关闭。  **默认值**：  false。

        :return: The enable_query_queue_select of this HtapQueryQueueRule.
        :rtype: str
        """
        return self._enable_query_queue_select

    @enable_query_queue_select.setter
    def enable_query_queue_select(self, enable_query_queue_select):
        r"""Sets the enable_query_queue_select of this HtapQueryQueueRule.

        **参数解释**：  查询队列开关状态。  **约束限制**：  不涉及。  **取值范围**：  - true：表示开启。 - false：表示关闭。  **默认值**：  false。

        :param enable_query_queue_select: The enable_query_queue_select of this HtapQueryQueueRule.
        :type enable_query_queue_select: str
        """
        self._enable_query_queue_select = enable_query_queue_select

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
        if not isinstance(other, HtapQueryQueueRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
