# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMySqlProxySlowLogListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'slow_log_list': 'list[ProxySlowLogDetail]',
        'slow_log_column': 'list[str]',
        'slow_log_query_time': 'str',
        'lts_slow_log_enabled': 'str',
        'support_switch_lts_slow_log': 'bool',
        'total_count': 'str'
    }

    attribute_map = {
        'slow_log_list': 'slow_log_list',
        'slow_log_column': 'slow_log_column',
        'slow_log_query_time': 'slow_log_query_time',
        'lts_slow_log_enabled': 'lts_slow_log_enabled',
        'support_switch_lts_slow_log': 'support_switch_lts_slow_log',
        'total_count': 'total_count'
    }

    def __init__(self, slow_log_list=None, slow_log_column=None, slow_log_query_time=None, lts_slow_log_enabled=None, support_switch_lts_slow_log=None, total_count=None):
        r"""ShowMySqlProxySlowLogListResponse

        The model defined in huaweicloud sdk

        :param slow_log_list: **参数解释**：  数据库代理慢日志信息列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type slow_log_list: list[:class:`huaweicloudsdkrds.v3.ProxySlowLogDetail`]
        :param slow_log_column: **参数解释**：  慢日志展示列表，该字段定义slow_log_list返回哪些字段信息，line_num字段一定返回。  **约束限制**：  不涉及。  **取值范围**：  - source_ip：客户端IP。 - desc_ip：后端数据库IP回。 - user：数据库用户。 - reaction_time：响应时长，单位ms。 - trace_id：SQL执行跟踪ID。 - sql：执行语句。 - start_time：SQL语句执行开始时间，毫秒级时间戳。 - end_time：SQL语句执行结束时间，毫秒级时间戳。 - database：数据库名称，默认不返回。 - log_time：日志上报时间，毫秒级时间戳，默认不返回。  **默认取值**：  不涉及。
        :type slow_log_column: list[str]
        :param slow_log_query_time: **参数解释**：  慢日志阈值，单位ms。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type slow_log_query_time: str
        :param lts_slow_log_enabled: **参数解释**：  慢日志上报开关状态。  **约束限制**：  不涉及。  **取值范围**：  - on：开启。 - off：关闭。  **默认取值**：  不涉及。
        :type lts_slow_log_enabled: str
        :param support_switch_lts_slow_log: **参数解释**：  数据库代理版本是否支持慢日志上报。  **约束限制**：  不涉及。  **取值范围**：  - true：支持。 - false：不支持。  **默认取值**：  不涉及。
        :type support_switch_lts_slow_log: bool
        :param total_count: **参数解释**：  每次查询到的慢日志数量。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type total_count: str
        """
        
        super().__init__()

        self._slow_log_list = None
        self._slow_log_column = None
        self._slow_log_query_time = None
        self._lts_slow_log_enabled = None
        self._support_switch_lts_slow_log = None
        self._total_count = None
        self.discriminator = None

        if slow_log_list is not None:
            self.slow_log_list = slow_log_list
        if slow_log_column is not None:
            self.slow_log_column = slow_log_column
        if slow_log_query_time is not None:
            self.slow_log_query_time = slow_log_query_time
        if lts_slow_log_enabled is not None:
            self.lts_slow_log_enabled = lts_slow_log_enabled
        if support_switch_lts_slow_log is not None:
            self.support_switch_lts_slow_log = support_switch_lts_slow_log
        if total_count is not None:
            self.total_count = total_count

    @property
    def slow_log_list(self):
        r"""Gets the slow_log_list of this ShowMySqlProxySlowLogListResponse.

        **参数解释**：  数据库代理慢日志信息列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The slow_log_list of this ShowMySqlProxySlowLogListResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ProxySlowLogDetail`]
        """
        return self._slow_log_list

    @slow_log_list.setter
    def slow_log_list(self, slow_log_list):
        r"""Sets the slow_log_list of this ShowMySqlProxySlowLogListResponse.

        **参数解释**：  数据库代理慢日志信息列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param slow_log_list: The slow_log_list of this ShowMySqlProxySlowLogListResponse.
        :type slow_log_list: list[:class:`huaweicloudsdkrds.v3.ProxySlowLogDetail`]
        """
        self._slow_log_list = slow_log_list

    @property
    def slow_log_column(self):
        r"""Gets the slow_log_column of this ShowMySqlProxySlowLogListResponse.

        **参数解释**：  慢日志展示列表，该字段定义slow_log_list返回哪些字段信息，line_num字段一定返回。  **约束限制**：  不涉及。  **取值范围**：  - source_ip：客户端IP。 - desc_ip：后端数据库IP回。 - user：数据库用户。 - reaction_time：响应时长，单位ms。 - trace_id：SQL执行跟踪ID。 - sql：执行语句。 - start_time：SQL语句执行开始时间，毫秒级时间戳。 - end_time：SQL语句执行结束时间，毫秒级时间戳。 - database：数据库名称，默认不返回。 - log_time：日志上报时间，毫秒级时间戳，默认不返回。  **默认取值**：  不涉及。

        :return: The slow_log_column of this ShowMySqlProxySlowLogListResponse.
        :rtype: list[str]
        """
        return self._slow_log_column

    @slow_log_column.setter
    def slow_log_column(self, slow_log_column):
        r"""Sets the slow_log_column of this ShowMySqlProxySlowLogListResponse.

        **参数解释**：  慢日志展示列表，该字段定义slow_log_list返回哪些字段信息，line_num字段一定返回。  **约束限制**：  不涉及。  **取值范围**：  - source_ip：客户端IP。 - desc_ip：后端数据库IP回。 - user：数据库用户。 - reaction_time：响应时长，单位ms。 - trace_id：SQL执行跟踪ID。 - sql：执行语句。 - start_time：SQL语句执行开始时间，毫秒级时间戳。 - end_time：SQL语句执行结束时间，毫秒级时间戳。 - database：数据库名称，默认不返回。 - log_time：日志上报时间，毫秒级时间戳，默认不返回。  **默认取值**：  不涉及。

        :param slow_log_column: The slow_log_column of this ShowMySqlProxySlowLogListResponse.
        :type slow_log_column: list[str]
        """
        self._slow_log_column = slow_log_column

    @property
    def slow_log_query_time(self):
        r"""Gets the slow_log_query_time of this ShowMySqlProxySlowLogListResponse.

        **参数解释**：  慢日志阈值，单位ms。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The slow_log_query_time of this ShowMySqlProxySlowLogListResponse.
        :rtype: str
        """
        return self._slow_log_query_time

    @slow_log_query_time.setter
    def slow_log_query_time(self, slow_log_query_time):
        r"""Sets the slow_log_query_time of this ShowMySqlProxySlowLogListResponse.

        **参数解释**：  慢日志阈值，单位ms。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param slow_log_query_time: The slow_log_query_time of this ShowMySqlProxySlowLogListResponse.
        :type slow_log_query_time: str
        """
        self._slow_log_query_time = slow_log_query_time

    @property
    def lts_slow_log_enabled(self):
        r"""Gets the lts_slow_log_enabled of this ShowMySqlProxySlowLogListResponse.

        **参数解释**：  慢日志上报开关状态。  **约束限制**：  不涉及。  **取值范围**：  - on：开启。 - off：关闭。  **默认取值**：  不涉及。

        :return: The lts_slow_log_enabled of this ShowMySqlProxySlowLogListResponse.
        :rtype: str
        """
        return self._lts_slow_log_enabled

    @lts_slow_log_enabled.setter
    def lts_slow_log_enabled(self, lts_slow_log_enabled):
        r"""Sets the lts_slow_log_enabled of this ShowMySqlProxySlowLogListResponse.

        **参数解释**：  慢日志上报开关状态。  **约束限制**：  不涉及。  **取值范围**：  - on：开启。 - off：关闭。  **默认取值**：  不涉及。

        :param lts_slow_log_enabled: The lts_slow_log_enabled of this ShowMySqlProxySlowLogListResponse.
        :type lts_slow_log_enabled: str
        """
        self._lts_slow_log_enabled = lts_slow_log_enabled

    @property
    def support_switch_lts_slow_log(self):
        r"""Gets the support_switch_lts_slow_log of this ShowMySqlProxySlowLogListResponse.

        **参数解释**：  数据库代理版本是否支持慢日志上报。  **约束限制**：  不涉及。  **取值范围**：  - true：支持。 - false：不支持。  **默认取值**：  不涉及。

        :return: The support_switch_lts_slow_log of this ShowMySqlProxySlowLogListResponse.
        :rtype: bool
        """
        return self._support_switch_lts_slow_log

    @support_switch_lts_slow_log.setter
    def support_switch_lts_slow_log(self, support_switch_lts_slow_log):
        r"""Sets the support_switch_lts_slow_log of this ShowMySqlProxySlowLogListResponse.

        **参数解释**：  数据库代理版本是否支持慢日志上报。  **约束限制**：  不涉及。  **取值范围**：  - true：支持。 - false：不支持。  **默认取值**：  不涉及。

        :param support_switch_lts_slow_log: The support_switch_lts_slow_log of this ShowMySqlProxySlowLogListResponse.
        :type support_switch_lts_slow_log: bool
        """
        self._support_switch_lts_slow_log = support_switch_lts_slow_log

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowMySqlProxySlowLogListResponse.

        **参数解释**：  每次查询到的慢日志数量。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The total_count of this ShowMySqlProxySlowLogListResponse.
        :rtype: str
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowMySqlProxySlowLogListResponse.

        **参数解释**：  每次查询到的慢日志数量。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param total_count: The total_count of this ShowMySqlProxySlowLogListResponse.
        :type total_count: str
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ShowMySqlProxySlowLogListResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowMySqlProxySlowLogListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
