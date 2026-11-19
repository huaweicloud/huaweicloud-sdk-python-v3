# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OverviewInfoRes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dashboard_info_list': 'list[object]',
        'risky_trend_info_list': 'list[object]',
        'risky_distribution_info_list': 'list[object]',
        'top_risky_host_info_list': 'list[object]',
        'top_account_crack_info_list': 'list[object]',
        'host_info_list': 'list[object]',
        'overall_situation_info_list': 'list[object]'
    }

    attribute_map = {
        'dashboard_info_list': 'dashboard_info_list',
        'risky_trend_info_list': 'risky_trend_info_list',
        'risky_distribution_info_list': 'risky_distribution_info_list',
        'top_risky_host_info_list': 'top_risky_host_info_list',
        'top_account_crack_info_list': 'top_account_crack_info_list',
        'host_info_list': 'host_info_list',
        'overall_situation_info_list': 'overall_situation_info_list'
    }

    def __init__(self, dashboard_info_list=None, risky_trend_info_list=None, risky_distribution_info_list=None, top_risky_host_info_list=None, top_account_crack_info_list=None, host_info_list=None, overall_situation_info_list=None):
        r"""OverviewInfoRes

        The model defined in huaweicloud sdk

        :param dashboard_info_list: **参数解释**： 安全总览内容列表 **取值范围**： 0-100个DashboardInfo对象 
        :type dashboard_info_list: list[object]
        :param risky_trend_info_list: **参数解释**： 风险趋势内容列表 **取值范围**： 0-100个RiskyTrendInfo对象 
        :type risky_trend_info_list: list[object]
        :param risky_distribution_info_list: **参数解释**： 风险分布内容列表 **取值范围**： 0-100个RiskyDistributionInfo对象 
        :type risky_distribution_info_list: list[object]
        :param top_risky_host_info_list: **参数解释**： top5风险主机列表 **取值范围**： 0-5个TopRiskyHostInfo对象 
        :type top_risky_host_info_list: list[object]
        :param top_account_crack_info_list: **参数解释**： top5暴力破解来源列表 **取值范围**： 0-5个TopAccountCrackInfo对象 
        :type top_account_crack_info_list: list[object]
        :param host_info_list: **参数解释**： 服务器列表 **取值范围**： 0-200个HostInfo对象 
        :type host_info_list: list[object]
        :param overall_situation_info_list: **参数解释**： 总体情况列表 **取值范围**： 0-100个OverallSituationInfo对象 
        :type overall_situation_info_list: list[object]
        """
        
        

        self._dashboard_info_list = None
        self._risky_trend_info_list = None
        self._risky_distribution_info_list = None
        self._top_risky_host_info_list = None
        self._top_account_crack_info_list = None
        self._host_info_list = None
        self._overall_situation_info_list = None
        self.discriminator = None

        if dashboard_info_list is not None:
            self.dashboard_info_list = dashboard_info_list
        if risky_trend_info_list is not None:
            self.risky_trend_info_list = risky_trend_info_list
        if risky_distribution_info_list is not None:
            self.risky_distribution_info_list = risky_distribution_info_list
        if top_risky_host_info_list is not None:
            self.top_risky_host_info_list = top_risky_host_info_list
        if top_account_crack_info_list is not None:
            self.top_account_crack_info_list = top_account_crack_info_list
        if host_info_list is not None:
            self.host_info_list = host_info_list
        if overall_situation_info_list is not None:
            self.overall_situation_info_list = overall_situation_info_list

    @property
    def dashboard_info_list(self):
        r"""Gets the dashboard_info_list of this OverviewInfoRes.

        **参数解释**： 安全总览内容列表 **取值范围**： 0-100个DashboardInfo对象 

        :return: The dashboard_info_list of this OverviewInfoRes.
        :rtype: list[object]
        """
        return self._dashboard_info_list

    @dashboard_info_list.setter
    def dashboard_info_list(self, dashboard_info_list):
        r"""Sets the dashboard_info_list of this OverviewInfoRes.

        **参数解释**： 安全总览内容列表 **取值范围**： 0-100个DashboardInfo对象 

        :param dashboard_info_list: The dashboard_info_list of this OverviewInfoRes.
        :type dashboard_info_list: list[object]
        """
        self._dashboard_info_list = dashboard_info_list

    @property
    def risky_trend_info_list(self):
        r"""Gets the risky_trend_info_list of this OverviewInfoRes.

        **参数解释**： 风险趋势内容列表 **取值范围**： 0-100个RiskyTrendInfo对象 

        :return: The risky_trend_info_list of this OverviewInfoRes.
        :rtype: list[object]
        """
        return self._risky_trend_info_list

    @risky_trend_info_list.setter
    def risky_trend_info_list(self, risky_trend_info_list):
        r"""Sets the risky_trend_info_list of this OverviewInfoRes.

        **参数解释**： 风险趋势内容列表 **取值范围**： 0-100个RiskyTrendInfo对象 

        :param risky_trend_info_list: The risky_trend_info_list of this OverviewInfoRes.
        :type risky_trend_info_list: list[object]
        """
        self._risky_trend_info_list = risky_trend_info_list

    @property
    def risky_distribution_info_list(self):
        r"""Gets the risky_distribution_info_list of this OverviewInfoRes.

        **参数解释**： 风险分布内容列表 **取值范围**： 0-100个RiskyDistributionInfo对象 

        :return: The risky_distribution_info_list of this OverviewInfoRes.
        :rtype: list[object]
        """
        return self._risky_distribution_info_list

    @risky_distribution_info_list.setter
    def risky_distribution_info_list(self, risky_distribution_info_list):
        r"""Sets the risky_distribution_info_list of this OverviewInfoRes.

        **参数解释**： 风险分布内容列表 **取值范围**： 0-100个RiskyDistributionInfo对象 

        :param risky_distribution_info_list: The risky_distribution_info_list of this OverviewInfoRes.
        :type risky_distribution_info_list: list[object]
        """
        self._risky_distribution_info_list = risky_distribution_info_list

    @property
    def top_risky_host_info_list(self):
        r"""Gets the top_risky_host_info_list of this OverviewInfoRes.

        **参数解释**： top5风险主机列表 **取值范围**： 0-5个TopRiskyHostInfo对象 

        :return: The top_risky_host_info_list of this OverviewInfoRes.
        :rtype: list[object]
        """
        return self._top_risky_host_info_list

    @top_risky_host_info_list.setter
    def top_risky_host_info_list(self, top_risky_host_info_list):
        r"""Sets the top_risky_host_info_list of this OverviewInfoRes.

        **参数解释**： top5风险主机列表 **取值范围**： 0-5个TopRiskyHostInfo对象 

        :param top_risky_host_info_list: The top_risky_host_info_list of this OverviewInfoRes.
        :type top_risky_host_info_list: list[object]
        """
        self._top_risky_host_info_list = top_risky_host_info_list

    @property
    def top_account_crack_info_list(self):
        r"""Gets the top_account_crack_info_list of this OverviewInfoRes.

        **参数解释**： top5暴力破解来源列表 **取值范围**： 0-5个TopAccountCrackInfo对象 

        :return: The top_account_crack_info_list of this OverviewInfoRes.
        :rtype: list[object]
        """
        return self._top_account_crack_info_list

    @top_account_crack_info_list.setter
    def top_account_crack_info_list(self, top_account_crack_info_list):
        r"""Sets the top_account_crack_info_list of this OverviewInfoRes.

        **参数解释**： top5暴力破解来源列表 **取值范围**： 0-5个TopAccountCrackInfo对象 

        :param top_account_crack_info_list: The top_account_crack_info_list of this OverviewInfoRes.
        :type top_account_crack_info_list: list[object]
        """
        self._top_account_crack_info_list = top_account_crack_info_list

    @property
    def host_info_list(self):
        r"""Gets the host_info_list of this OverviewInfoRes.

        **参数解释**： 服务器列表 **取值范围**： 0-200个HostInfo对象 

        :return: The host_info_list of this OverviewInfoRes.
        :rtype: list[object]
        """
        return self._host_info_list

    @host_info_list.setter
    def host_info_list(self, host_info_list):
        r"""Sets the host_info_list of this OverviewInfoRes.

        **参数解释**： 服务器列表 **取值范围**： 0-200个HostInfo对象 

        :param host_info_list: The host_info_list of this OverviewInfoRes.
        :type host_info_list: list[object]
        """
        self._host_info_list = host_info_list

    @property
    def overall_situation_info_list(self):
        r"""Gets the overall_situation_info_list of this OverviewInfoRes.

        **参数解释**： 总体情况列表 **取值范围**： 0-100个OverallSituationInfo对象 

        :return: The overall_situation_info_list of this OverviewInfoRes.
        :rtype: list[object]
        """
        return self._overall_situation_info_list

    @overall_situation_info_list.setter
    def overall_situation_info_list(self, overall_situation_info_list):
        r"""Sets the overall_situation_info_list of this OverviewInfoRes.

        **参数解释**： 总体情况列表 **取值范围**： 0-100个OverallSituationInfo对象 

        :param overall_situation_info_list: The overall_situation_info_list of this OverviewInfoRes.
        :type overall_situation_info_list: list[object]
        """
        self._overall_situation_info_list = overall_situation_info_list

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
        if not isinstance(other, OverviewInfoRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
