# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityReportContentResponseReportContentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'overview_statistics_list_info': 'list[SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo]',
        'request_statistics_info_list': 'list[SecurityReportContentResponseReportContentInfoRequestStatisticsInfoList]',
        'qps_statistics_info': 'SecurityReportContentResponseReportContentInfoQpsStatisticsInfo',
        'bandwidth_statistics_info': 'SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfo',
        'response_code_statistics_info': 'SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfo',
        'attack_type_distribution_info_list': 'list[SecurityReportContentResponseReportContentInfoAttackTypeDistributionInfoList]',
        'top_attacked_domains_info_list': 'list[SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList]',
        'top_attack_source_ips_info_list': 'list[SecurityReportContentResponseReportContentInfoTopAttackSourceIpsInfoList]',
        'top_attacked_urls_info_list': 'list[SecurityReportContentResponseReportContentInfoTopAttackedUrlsInfoList]',
        'top_attack_source_locations_info_list': 'list[SecurityReportContentResponseReportContentInfoTopAttackSourceLocationsInfoList]',
        'top_abnormal_urls_info': 'SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo'
    }

    attribute_map = {
        'overview_statistics_list_info': 'overview_statistics_list_info',
        'request_statistics_info_list': 'request_statistics_info_list',
        'qps_statistics_info': 'qps_statistics_info',
        'bandwidth_statistics_info': 'bandwidth_statistics_info',
        'response_code_statistics_info': 'response_code_statistics_info',
        'attack_type_distribution_info_list': 'attack_type_distribution_info_list',
        'top_attacked_domains_info_list': 'top_attacked_domains_info_list',
        'top_attack_source_ips_info_list': 'top_attack_source_ips_info_list',
        'top_attacked_urls_info_list': 'top_attacked_urls_info_list',
        'top_attack_source_locations_info_list': 'top_attack_source_locations_info_list',
        'top_abnormal_urls_info': 'top_abnormal_urls_info'
    }

    def __init__(self, overview_statistics_list_info=None, request_statistics_info_list=None, qps_statistics_info=None, bandwidth_statistics_info=None, response_code_statistics_info=None, attack_type_distribution_info_list=None, top_attacked_domains_info_list=None, top_attack_source_ips_info_list=None, top_attacked_urls_info_list=None, top_attack_source_locations_info_list=None, top_abnormal_urls_info=None):
        r"""SecurityReportContentResponseReportContentInfo

        The model defined in huaweicloud sdk

        :param overview_statistics_list_info: **参数解释：** 总览统计信息，包含各维度的汇总统计数据及TOP域名详情。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type overview_statistics_list_info: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo`]
        :param request_statistics_info_list: **参数解释：** 请求次数统计信息，包含各维度按时间线的请求数量统计。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type request_statistics_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoRequestStatisticsInfoList`]
        :param qps_statistics_info: 
        :type qps_statistics_info: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoQpsStatisticsInfo`
        :param bandwidth_statistics_info: 
        :type bandwidth_statistics_info: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfo`
        :param response_code_statistics_info: 
        :type response_code_statistics_info: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfo`
        :param attack_type_distribution_info_list: **参数解释：** 攻击类型分布统计信息，包含各攻击类型的数量分布。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type attack_type_distribution_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoAttackTypeDistributionInfoList`]
        :param top_attacked_domains_info_list: **参数解释：** TOP被攻击的域名信息，按被攻击次数排序的域名列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type top_attacked_domains_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList`]
        :param top_attack_source_ips_info_list: **参数解释：** TOP攻击的源IP信息，按攻击次数排序的攻击源IP列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type top_attack_source_ips_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAttackSourceIpsInfoList`]
        :param top_attacked_urls_info_list: **参数解释：** TOP被攻击的URL信息，按被攻击次数排序的URL列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type top_attacked_urls_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAttackedUrlsInfoList`]
        :param top_attack_source_locations_info_list: **参数解释：** TOP攻击的源地理位置信息，按攻击次数排序的地理位置列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type top_attack_source_locations_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAttackSourceLocationsInfoList`]
        :param top_abnormal_urls_info: 
        :type top_abnormal_urls_info: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo`
        """
        
        

        self._overview_statistics_list_info = None
        self._request_statistics_info_list = None
        self._qps_statistics_info = None
        self._bandwidth_statistics_info = None
        self._response_code_statistics_info = None
        self._attack_type_distribution_info_list = None
        self._top_attacked_domains_info_list = None
        self._top_attack_source_ips_info_list = None
        self._top_attacked_urls_info_list = None
        self._top_attack_source_locations_info_list = None
        self._top_abnormal_urls_info = None
        self.discriminator = None

        if overview_statistics_list_info is not None:
            self.overview_statistics_list_info = overview_statistics_list_info
        if request_statistics_info_list is not None:
            self.request_statistics_info_list = request_statistics_info_list
        if qps_statistics_info is not None:
            self.qps_statistics_info = qps_statistics_info
        if bandwidth_statistics_info is not None:
            self.bandwidth_statistics_info = bandwidth_statistics_info
        if response_code_statistics_info is not None:
            self.response_code_statistics_info = response_code_statistics_info
        if attack_type_distribution_info_list is not None:
            self.attack_type_distribution_info_list = attack_type_distribution_info_list
        if top_attacked_domains_info_list is not None:
            self.top_attacked_domains_info_list = top_attacked_domains_info_list
        if top_attack_source_ips_info_list is not None:
            self.top_attack_source_ips_info_list = top_attack_source_ips_info_list
        if top_attacked_urls_info_list is not None:
            self.top_attacked_urls_info_list = top_attacked_urls_info_list
        if top_attack_source_locations_info_list is not None:
            self.top_attack_source_locations_info_list = top_attack_source_locations_info_list
        if top_abnormal_urls_info is not None:
            self.top_abnormal_urls_info = top_abnormal_urls_info

    @property
    def overview_statistics_list_info(self):
        r"""Gets the overview_statistics_list_info of this SecurityReportContentResponseReportContentInfo.

        **参数解释：** 总览统计信息，包含各维度的汇总统计数据及TOP域名详情。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The overview_statistics_list_info of this SecurityReportContentResponseReportContentInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo`]
        """
        return self._overview_statistics_list_info

    @overview_statistics_list_info.setter
    def overview_statistics_list_info(self, overview_statistics_list_info):
        r"""Sets the overview_statistics_list_info of this SecurityReportContentResponseReportContentInfo.

        **参数解释：** 总览统计信息，包含各维度的汇总统计数据及TOP域名详情。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param overview_statistics_list_info: The overview_statistics_list_info of this SecurityReportContentResponseReportContentInfo.
        :type overview_statistics_list_info: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoOverviewStatisticsListInfo`]
        """
        self._overview_statistics_list_info = overview_statistics_list_info

    @property
    def request_statistics_info_list(self):
        r"""Gets the request_statistics_info_list of this SecurityReportContentResponseReportContentInfo.

        **参数解释：** 请求次数统计信息，包含各维度按时间线的请求数量统计。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The request_statistics_info_list of this SecurityReportContentResponseReportContentInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoRequestStatisticsInfoList`]
        """
        return self._request_statistics_info_list

    @request_statistics_info_list.setter
    def request_statistics_info_list(self, request_statistics_info_list):
        r"""Sets the request_statistics_info_list of this SecurityReportContentResponseReportContentInfo.

        **参数解释：** 请求次数统计信息，包含各维度按时间线的请求数量统计。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param request_statistics_info_list: The request_statistics_info_list of this SecurityReportContentResponseReportContentInfo.
        :type request_statistics_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoRequestStatisticsInfoList`]
        """
        self._request_statistics_info_list = request_statistics_info_list

    @property
    def qps_statistics_info(self):
        r"""Gets the qps_statistics_info of this SecurityReportContentResponseReportContentInfo.

        :return: The qps_statistics_info of this SecurityReportContentResponseReportContentInfo.
        :rtype: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoQpsStatisticsInfo`
        """
        return self._qps_statistics_info

    @qps_statistics_info.setter
    def qps_statistics_info(self, qps_statistics_info):
        r"""Sets the qps_statistics_info of this SecurityReportContentResponseReportContentInfo.

        :param qps_statistics_info: The qps_statistics_info of this SecurityReportContentResponseReportContentInfo.
        :type qps_statistics_info: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoQpsStatisticsInfo`
        """
        self._qps_statistics_info = qps_statistics_info

    @property
    def bandwidth_statistics_info(self):
        r"""Gets the bandwidth_statistics_info of this SecurityReportContentResponseReportContentInfo.

        :return: The bandwidth_statistics_info of this SecurityReportContentResponseReportContentInfo.
        :rtype: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfo`
        """
        return self._bandwidth_statistics_info

    @bandwidth_statistics_info.setter
    def bandwidth_statistics_info(self, bandwidth_statistics_info):
        r"""Sets the bandwidth_statistics_info of this SecurityReportContentResponseReportContentInfo.

        :param bandwidth_statistics_info: The bandwidth_statistics_info of this SecurityReportContentResponseReportContentInfo.
        :type bandwidth_statistics_info: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoBandwidthStatisticsInfo`
        """
        self._bandwidth_statistics_info = bandwidth_statistics_info

    @property
    def response_code_statistics_info(self):
        r"""Gets the response_code_statistics_info of this SecurityReportContentResponseReportContentInfo.

        :return: The response_code_statistics_info of this SecurityReportContentResponseReportContentInfo.
        :rtype: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfo`
        """
        return self._response_code_statistics_info

    @response_code_statistics_info.setter
    def response_code_statistics_info(self, response_code_statistics_info):
        r"""Sets the response_code_statistics_info of this SecurityReportContentResponseReportContentInfo.

        :param response_code_statistics_info: The response_code_statistics_info of this SecurityReportContentResponseReportContentInfo.
        :type response_code_statistics_info: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoResponseCodeStatisticsInfo`
        """
        self._response_code_statistics_info = response_code_statistics_info

    @property
    def attack_type_distribution_info_list(self):
        r"""Gets the attack_type_distribution_info_list of this SecurityReportContentResponseReportContentInfo.

        **参数解释：** 攻击类型分布统计信息，包含各攻击类型的数量分布。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The attack_type_distribution_info_list of this SecurityReportContentResponseReportContentInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoAttackTypeDistributionInfoList`]
        """
        return self._attack_type_distribution_info_list

    @attack_type_distribution_info_list.setter
    def attack_type_distribution_info_list(self, attack_type_distribution_info_list):
        r"""Sets the attack_type_distribution_info_list of this SecurityReportContentResponseReportContentInfo.

        **参数解释：** 攻击类型分布统计信息，包含各攻击类型的数量分布。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param attack_type_distribution_info_list: The attack_type_distribution_info_list of this SecurityReportContentResponseReportContentInfo.
        :type attack_type_distribution_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoAttackTypeDistributionInfoList`]
        """
        self._attack_type_distribution_info_list = attack_type_distribution_info_list

    @property
    def top_attacked_domains_info_list(self):
        r"""Gets the top_attacked_domains_info_list of this SecurityReportContentResponseReportContentInfo.

        **参数解释：** TOP被攻击的域名信息，按被攻击次数排序的域名列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The top_attacked_domains_info_list of this SecurityReportContentResponseReportContentInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList`]
        """
        return self._top_attacked_domains_info_list

    @top_attacked_domains_info_list.setter
    def top_attacked_domains_info_list(self, top_attacked_domains_info_list):
        r"""Sets the top_attacked_domains_info_list of this SecurityReportContentResponseReportContentInfo.

        **参数解释：** TOP被攻击的域名信息，按被攻击次数排序的域名列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param top_attacked_domains_info_list: The top_attacked_domains_info_list of this SecurityReportContentResponseReportContentInfo.
        :type top_attacked_domains_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAttackedDomainsInfoList`]
        """
        self._top_attacked_domains_info_list = top_attacked_domains_info_list

    @property
    def top_attack_source_ips_info_list(self):
        r"""Gets the top_attack_source_ips_info_list of this SecurityReportContentResponseReportContentInfo.

        **参数解释：** TOP攻击的源IP信息，按攻击次数排序的攻击源IP列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The top_attack_source_ips_info_list of this SecurityReportContentResponseReportContentInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAttackSourceIpsInfoList`]
        """
        return self._top_attack_source_ips_info_list

    @top_attack_source_ips_info_list.setter
    def top_attack_source_ips_info_list(self, top_attack_source_ips_info_list):
        r"""Sets the top_attack_source_ips_info_list of this SecurityReportContentResponseReportContentInfo.

        **参数解释：** TOP攻击的源IP信息，按攻击次数排序的攻击源IP列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param top_attack_source_ips_info_list: The top_attack_source_ips_info_list of this SecurityReportContentResponseReportContentInfo.
        :type top_attack_source_ips_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAttackSourceIpsInfoList`]
        """
        self._top_attack_source_ips_info_list = top_attack_source_ips_info_list

    @property
    def top_attacked_urls_info_list(self):
        r"""Gets the top_attacked_urls_info_list of this SecurityReportContentResponseReportContentInfo.

        **参数解释：** TOP被攻击的URL信息，按被攻击次数排序的URL列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The top_attacked_urls_info_list of this SecurityReportContentResponseReportContentInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAttackedUrlsInfoList`]
        """
        return self._top_attacked_urls_info_list

    @top_attacked_urls_info_list.setter
    def top_attacked_urls_info_list(self, top_attacked_urls_info_list):
        r"""Sets the top_attacked_urls_info_list of this SecurityReportContentResponseReportContentInfo.

        **参数解释：** TOP被攻击的URL信息，按被攻击次数排序的URL列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param top_attacked_urls_info_list: The top_attacked_urls_info_list of this SecurityReportContentResponseReportContentInfo.
        :type top_attacked_urls_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAttackedUrlsInfoList`]
        """
        self._top_attacked_urls_info_list = top_attacked_urls_info_list

    @property
    def top_attack_source_locations_info_list(self):
        r"""Gets the top_attack_source_locations_info_list of this SecurityReportContentResponseReportContentInfo.

        **参数解释：** TOP攻击的源地理位置信息，按攻击次数排序的地理位置列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The top_attack_source_locations_info_list of this SecurityReportContentResponseReportContentInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAttackSourceLocationsInfoList`]
        """
        return self._top_attack_source_locations_info_list

    @top_attack_source_locations_info_list.setter
    def top_attack_source_locations_info_list(self, top_attack_source_locations_info_list):
        r"""Sets the top_attack_source_locations_info_list of this SecurityReportContentResponseReportContentInfo.

        **参数解释：** TOP攻击的源地理位置信息，按攻击次数排序的地理位置列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param top_attack_source_locations_info_list: The top_attack_source_locations_info_list of this SecurityReportContentResponseReportContentInfo.
        :type top_attack_source_locations_info_list: list[:class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAttackSourceLocationsInfoList`]
        """
        self._top_attack_source_locations_info_list = top_attack_source_locations_info_list

    @property
    def top_abnormal_urls_info(self):
        r"""Gets the top_abnormal_urls_info of this SecurityReportContentResponseReportContentInfo.

        :return: The top_abnormal_urls_info of this SecurityReportContentResponseReportContentInfo.
        :rtype: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo`
        """
        return self._top_abnormal_urls_info

    @top_abnormal_urls_info.setter
    def top_abnormal_urls_info(self, top_abnormal_urls_info):
        r"""Sets the top_abnormal_urls_info of this SecurityReportContentResponseReportContentInfo.

        :param top_abnormal_urls_info: The top_abnormal_urls_info of this SecurityReportContentResponseReportContentInfo.
        :type top_abnormal_urls_info: :class:`huaweicloudsdkwaf.v1.SecurityReportContentResponseReportContentInfoTopAbnormalUrlsInfo`
        """
        self._top_abnormal_urls_info = top_abnormal_urls_info

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SecurityReportContentResponseReportContentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
