# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSessionSummaryUseOpsTunnelResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'active_count': 'int',
        'total_count': 'int',
        'max_query_time_cost': 'int',
        'max_transaction_time_cost': 'int'
    }

    attribute_map = {
        'active_count': 'active_count',
        'total_count': 'total_count',
        'max_query_time_cost': 'max_query_time_cost',
        'max_transaction_time_cost': 'max_transaction_time_cost'
    }

    def __init__(self, active_count=None, total_count=None, max_query_time_cost=None, max_transaction_time_cost=None):
        r"""ShowSessionSummaryUseOpsTunnelResponse

        The model defined in huaweicloud sdk

        :param active_count: **参数解释**: 活跃会话数量。 **取值范围**: 不涉及。
        :type active_count: int
        :param total_count: **参数解释**: 会话总数量。 **取值范围**: 不涉及。
        :type total_count: int
        :param max_query_time_cost: **参数解释**: 最大SQL执行时间。单位：秒。 **取值范围**: 不涉及。
        :type max_query_time_cost: int
        :param max_transaction_time_cost: **参数解释**: 最大事务执行时间。单位：秒。 **取值范围**: 不涉及。
        :type max_transaction_time_cost: int
        """
        
        super().__init__()

        self._active_count = None
        self._total_count = None
        self._max_query_time_cost = None
        self._max_transaction_time_cost = None
        self.discriminator = None

        if active_count is not None:
            self.active_count = active_count
        if total_count is not None:
            self.total_count = total_count
        if max_query_time_cost is not None:
            self.max_query_time_cost = max_query_time_cost
        if max_transaction_time_cost is not None:
            self.max_transaction_time_cost = max_transaction_time_cost

    @property
    def active_count(self):
        r"""Gets the active_count of this ShowSessionSummaryUseOpsTunnelResponse.

        **参数解释**: 活跃会话数量。 **取值范围**: 不涉及。

        :return: The active_count of this ShowSessionSummaryUseOpsTunnelResponse.
        :rtype: int
        """
        return self._active_count

    @active_count.setter
    def active_count(self, active_count):
        r"""Sets the active_count of this ShowSessionSummaryUseOpsTunnelResponse.

        **参数解释**: 活跃会话数量。 **取值范围**: 不涉及。

        :param active_count: The active_count of this ShowSessionSummaryUseOpsTunnelResponse.
        :type active_count: int
        """
        self._active_count = active_count

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowSessionSummaryUseOpsTunnelResponse.

        **参数解释**: 会话总数量。 **取值范围**: 不涉及。

        :return: The total_count of this ShowSessionSummaryUseOpsTunnelResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowSessionSummaryUseOpsTunnelResponse.

        **参数解释**: 会话总数量。 **取值范围**: 不涉及。

        :param total_count: The total_count of this ShowSessionSummaryUseOpsTunnelResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def max_query_time_cost(self):
        r"""Gets the max_query_time_cost of this ShowSessionSummaryUseOpsTunnelResponse.

        **参数解释**: 最大SQL执行时间。单位：秒。 **取值范围**: 不涉及。

        :return: The max_query_time_cost of this ShowSessionSummaryUseOpsTunnelResponse.
        :rtype: int
        """
        return self._max_query_time_cost

    @max_query_time_cost.setter
    def max_query_time_cost(self, max_query_time_cost):
        r"""Sets the max_query_time_cost of this ShowSessionSummaryUseOpsTunnelResponse.

        **参数解释**: 最大SQL执行时间。单位：秒。 **取值范围**: 不涉及。

        :param max_query_time_cost: The max_query_time_cost of this ShowSessionSummaryUseOpsTunnelResponse.
        :type max_query_time_cost: int
        """
        self._max_query_time_cost = max_query_time_cost

    @property
    def max_transaction_time_cost(self):
        r"""Gets the max_transaction_time_cost of this ShowSessionSummaryUseOpsTunnelResponse.

        **参数解释**: 最大事务执行时间。单位：秒。 **取值范围**: 不涉及。

        :return: The max_transaction_time_cost of this ShowSessionSummaryUseOpsTunnelResponse.
        :rtype: int
        """
        return self._max_transaction_time_cost

    @max_transaction_time_cost.setter
    def max_transaction_time_cost(self, max_transaction_time_cost):
        r"""Sets the max_transaction_time_cost of this ShowSessionSummaryUseOpsTunnelResponse.

        **参数解释**: 最大事务执行时间。单位：秒。 **取值范围**: 不涉及。

        :param max_transaction_time_cost: The max_transaction_time_cost of this ShowSessionSummaryUseOpsTunnelResponse.
        :type max_transaction_time_cost: int
        """
        self._max_transaction_time_cost = max_transaction_time_cost

    def to_dict(self):
        import warnings
        warnings.warn("ShowSessionSummaryUseOpsTunnelResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSessionSummaryUseOpsTunnelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
