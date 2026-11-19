# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OverviewSubscriptionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dashboard_status': 'bool',
        'risky_trend_status': 'bool',
        'risky_distribution_status': 'bool',
        'top_risky_host_status': 'bool',
        'top_account_crack_status': 'bool',
        'host_info_status': 'bool'
    }

    attribute_map = {
        'dashboard_status': 'dashboard_status',
        'risky_trend_status': 'risky_trend_status',
        'risky_distribution_status': 'risky_distribution_status',
        'top_risky_host_status': 'top_risky_host_status',
        'top_account_crack_status': 'top_account_crack_status',
        'host_info_status': 'host_info_status'
    }

    def __init__(self, dashboard_status=None, risky_trend_status=None, risky_distribution_status=None, top_risky_host_status=None, top_account_crack_status=None, host_info_status=None):
        r"""OverviewSubscriptionReq

        The model defined in huaweicloud sdk

        :param dashboard_status: **参数解释**： 安全总览是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 
        :type dashboard_status: bool
        :param risky_trend_status: **参数解释**： 风险趋势是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 
        :type risky_trend_status: bool
        :param risky_distribution_status: **参数解释**： 风险分布是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 
        :type risky_distribution_status: bool
        :param top_risky_host_status: **参数解释**： top5风险主机是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 
        :type top_risky_host_status: bool
        :param top_account_crack_status: **参数解释**： top5暴力破解来源是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 
        :type top_account_crack_status: bool
        :param host_info_status: **参数解释**： 服务器列表是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 
        :type host_info_status: bool
        """
        
        

        self._dashboard_status = None
        self._risky_trend_status = None
        self._risky_distribution_status = None
        self._top_risky_host_status = None
        self._top_account_crack_status = None
        self._host_info_status = None
        self.discriminator = None

        if dashboard_status is not None:
            self.dashboard_status = dashboard_status
        if risky_trend_status is not None:
            self.risky_trend_status = risky_trend_status
        if risky_distribution_status is not None:
            self.risky_distribution_status = risky_distribution_status
        if top_risky_host_status is not None:
            self.top_risky_host_status = top_risky_host_status
        if top_account_crack_status is not None:
            self.top_account_crack_status = top_account_crack_status
        if host_info_status is not None:
            self.host_info_status = host_info_status

    @property
    def dashboard_status(self):
        r"""Gets the dashboard_status of this OverviewSubscriptionReq.

        **参数解释**： 安全总览是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :return: The dashboard_status of this OverviewSubscriptionReq.
        :rtype: bool
        """
        return self._dashboard_status

    @dashboard_status.setter
    def dashboard_status(self, dashboard_status):
        r"""Sets the dashboard_status of this OverviewSubscriptionReq.

        **参数解释**： 安全总览是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :param dashboard_status: The dashboard_status of this OverviewSubscriptionReq.
        :type dashboard_status: bool
        """
        self._dashboard_status = dashboard_status

    @property
    def risky_trend_status(self):
        r"""Gets the risky_trend_status of this OverviewSubscriptionReq.

        **参数解释**： 风险趋势是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :return: The risky_trend_status of this OverviewSubscriptionReq.
        :rtype: bool
        """
        return self._risky_trend_status

    @risky_trend_status.setter
    def risky_trend_status(self, risky_trend_status):
        r"""Sets the risky_trend_status of this OverviewSubscriptionReq.

        **参数解释**： 风险趋势是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :param risky_trend_status: The risky_trend_status of this OverviewSubscriptionReq.
        :type risky_trend_status: bool
        """
        self._risky_trend_status = risky_trend_status

    @property
    def risky_distribution_status(self):
        r"""Gets the risky_distribution_status of this OverviewSubscriptionReq.

        **参数解释**： 风险分布是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :return: The risky_distribution_status of this OverviewSubscriptionReq.
        :rtype: bool
        """
        return self._risky_distribution_status

    @risky_distribution_status.setter
    def risky_distribution_status(self, risky_distribution_status):
        r"""Sets the risky_distribution_status of this OverviewSubscriptionReq.

        **参数解释**： 风险分布是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :param risky_distribution_status: The risky_distribution_status of this OverviewSubscriptionReq.
        :type risky_distribution_status: bool
        """
        self._risky_distribution_status = risky_distribution_status

    @property
    def top_risky_host_status(self):
        r"""Gets the top_risky_host_status of this OverviewSubscriptionReq.

        **参数解释**： top5风险主机是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :return: The top_risky_host_status of this OverviewSubscriptionReq.
        :rtype: bool
        """
        return self._top_risky_host_status

    @top_risky_host_status.setter
    def top_risky_host_status(self, top_risky_host_status):
        r"""Sets the top_risky_host_status of this OverviewSubscriptionReq.

        **参数解释**： top5风险主机是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :param top_risky_host_status: The top_risky_host_status of this OverviewSubscriptionReq.
        :type top_risky_host_status: bool
        """
        self._top_risky_host_status = top_risky_host_status

    @property
    def top_account_crack_status(self):
        r"""Gets the top_account_crack_status of this OverviewSubscriptionReq.

        **参数解释**： top5暴力破解来源是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :return: The top_account_crack_status of this OverviewSubscriptionReq.
        :rtype: bool
        """
        return self._top_account_crack_status

    @top_account_crack_status.setter
    def top_account_crack_status(self, top_account_crack_status):
        r"""Sets the top_account_crack_status of this OverviewSubscriptionReq.

        **参数解释**： top5暴力破解来源是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :param top_account_crack_status: The top_account_crack_status of this OverviewSubscriptionReq.
        :type top_account_crack_status: bool
        """
        self._top_account_crack_status = top_account_crack_status

    @property
    def host_info_status(self):
        r"""Gets the host_info_status of this OverviewSubscriptionReq.

        **参数解释**： 服务器列表是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :return: The host_info_status of this OverviewSubscriptionReq.
        :rtype: bool
        """
        return self._host_info_status

    @host_info_status.setter
    def host_info_status(self, host_info_status):
        r"""Sets the host_info_status of this OverviewSubscriptionReq.

        **参数解释**： 服务器列表是否订阅 **约束限制**： 不涉及 **取值范围**： - true：是 - false：否  **默认取值**： 不涉及 

        :param host_info_status: The host_info_status of this OverviewSubscriptionReq.
        :type host_info_status: bool
        """
        self._host_info_status = host_info_status

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
        if not isinstance(other, OverviewSubscriptionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
