# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDomainConfigs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code_cache': 'list[ErrorCodeCache]',
        'ip_filter': 'IpFilter',
        'flow_limit_strategy': 'list[FlowLimitStrategy]',
        'bandwidth_alarm_strategy': 'BandwidthAlarmStrategy'
    }

    attribute_map = {
        'error_code_cache': 'error_code_cache',
        'ip_filter': 'ip_filter',
        'flow_limit_strategy': 'flow_limit_strategy',
        'bandwidth_alarm_strategy': 'bandwidth_alarm_strategy'
    }

    def __init__(self, error_code_cache=None, ip_filter=None, flow_limit_strategy=None, bandwidth_alarm_strategy=None):
        r"""CreateDomainConfigs

        The model defined in huaweicloud sdk

        :param error_code_cache: **参数解释：** 将源站返回的错误状态码缓存到CDN节点，用户再次请求时由CDN直接响应给用户错误码 **约束限制：** 不涉及
        :type error_code_cache: list[:class:`huaweicloudsdkcdn.v2.ErrorCodeCache`]
        :param ip_filter: 
        :type ip_filter: :class:`huaweicloudsdkcdn.v2.IpFilter`
        :param flow_limit_strategy: **参数解释：** 设置用量封顶阈值，当实际用量大于阈值时停用域名，有效预防流量盗刷或恶意攻击带来的高额账单。  &gt; 由于监控数据存在时延，域名将在用量达到阈值后的10分钟左右被停用  **约束限制：** 不涉及
        :type flow_limit_strategy: list[:class:`huaweicloudsdkcdn.v2.FlowLimitStrategy`]
        :param bandwidth_alarm_strategy: 
        :type bandwidth_alarm_strategy: :class:`huaweicloudsdkcdn.v2.BandwidthAlarmStrategy`
        """
        
        

        self._error_code_cache = None
        self._ip_filter = None
        self._flow_limit_strategy = None
        self._bandwidth_alarm_strategy = None
        self.discriminator = None

        if error_code_cache is not None:
            self.error_code_cache = error_code_cache
        if ip_filter is not None:
            self.ip_filter = ip_filter
        if flow_limit_strategy is not None:
            self.flow_limit_strategy = flow_limit_strategy
        if bandwidth_alarm_strategy is not None:
            self.bandwidth_alarm_strategy = bandwidth_alarm_strategy

    @property
    def error_code_cache(self):
        r"""Gets the error_code_cache of this CreateDomainConfigs.

        **参数解释：** 将源站返回的错误状态码缓存到CDN节点，用户再次请求时由CDN直接响应给用户错误码 **约束限制：** 不涉及

        :return: The error_code_cache of this CreateDomainConfigs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.ErrorCodeCache`]
        """
        return self._error_code_cache

    @error_code_cache.setter
    def error_code_cache(self, error_code_cache):
        r"""Sets the error_code_cache of this CreateDomainConfigs.

        **参数解释：** 将源站返回的错误状态码缓存到CDN节点，用户再次请求时由CDN直接响应给用户错误码 **约束限制：** 不涉及

        :param error_code_cache: The error_code_cache of this CreateDomainConfigs.
        :type error_code_cache: list[:class:`huaweicloudsdkcdn.v2.ErrorCodeCache`]
        """
        self._error_code_cache = error_code_cache

    @property
    def ip_filter(self):
        r"""Gets the ip_filter of this CreateDomainConfigs.

        :return: The ip_filter of this CreateDomainConfigs.
        :rtype: :class:`huaweicloudsdkcdn.v2.IpFilter`
        """
        return self._ip_filter

    @ip_filter.setter
    def ip_filter(self, ip_filter):
        r"""Sets the ip_filter of this CreateDomainConfigs.

        :param ip_filter: The ip_filter of this CreateDomainConfigs.
        :type ip_filter: :class:`huaweicloudsdkcdn.v2.IpFilter`
        """
        self._ip_filter = ip_filter

    @property
    def flow_limit_strategy(self):
        r"""Gets the flow_limit_strategy of this CreateDomainConfigs.

        **参数解释：** 设置用量封顶阈值，当实际用量大于阈值时停用域名，有效预防流量盗刷或恶意攻击带来的高额账单。  > 由于监控数据存在时延，域名将在用量达到阈值后的10分钟左右被停用  **约束限制：** 不涉及

        :return: The flow_limit_strategy of this CreateDomainConfigs.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.FlowLimitStrategy`]
        """
        return self._flow_limit_strategy

    @flow_limit_strategy.setter
    def flow_limit_strategy(self, flow_limit_strategy):
        r"""Sets the flow_limit_strategy of this CreateDomainConfigs.

        **参数解释：** 设置用量封顶阈值，当实际用量大于阈值时停用域名，有效预防流量盗刷或恶意攻击带来的高额账单。  > 由于监控数据存在时延，域名将在用量达到阈值后的10分钟左右被停用  **约束限制：** 不涉及

        :param flow_limit_strategy: The flow_limit_strategy of this CreateDomainConfigs.
        :type flow_limit_strategy: list[:class:`huaweicloudsdkcdn.v2.FlowLimitStrategy`]
        """
        self._flow_limit_strategy = flow_limit_strategy

    @property
    def bandwidth_alarm_strategy(self):
        r"""Gets the bandwidth_alarm_strategy of this CreateDomainConfigs.

        :return: The bandwidth_alarm_strategy of this CreateDomainConfigs.
        :rtype: :class:`huaweicloudsdkcdn.v2.BandwidthAlarmStrategy`
        """
        return self._bandwidth_alarm_strategy

    @bandwidth_alarm_strategy.setter
    def bandwidth_alarm_strategy(self, bandwidth_alarm_strategy):
        r"""Sets the bandwidth_alarm_strategy of this CreateDomainConfigs.

        :param bandwidth_alarm_strategy: The bandwidth_alarm_strategy of this CreateDomainConfigs.
        :type bandwidth_alarm_strategy: :class:`huaweicloudsdkcdn.v2.BandwidthAlarmStrategy`
        """
        self._bandwidth_alarm_strategy = bandwidth_alarm_strategy

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
        if not isinstance(other, CreateDomainConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
