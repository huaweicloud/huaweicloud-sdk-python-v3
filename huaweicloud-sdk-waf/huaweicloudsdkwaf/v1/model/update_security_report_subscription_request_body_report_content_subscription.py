# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'overview_statistics_enable': 'bool',
        'group_by_day_enable': 'bool',
        'request_statistics_enable': 'bool',
        'qps_statistics_enable': 'bool',
        'bandwidth_statistics_enable': 'bool',
        'response_code_statistics_enable': 'bool',
        'attack_type_distribution_enable': 'bool',
        'top_attacked_domains_enable': 'bool',
        'top_attack_source_ips_enable': 'bool',
        'top_attacked_urls_enable': 'bool',
        'top_attack_source_locations_enable': 'bool',
        'top_abnormal_urls_enable': 'bool'
    }

    attribute_map = {
        'overview_statistics_enable': 'overview_statistics_enable',
        'group_by_day_enable': 'group_by_day_enable',
        'request_statistics_enable': 'request_statistics_enable',
        'qps_statistics_enable': 'qps_statistics_enable',
        'bandwidth_statistics_enable': 'bandwidth_statistics_enable',
        'response_code_statistics_enable': 'response_code_statistics_enable',
        'attack_type_distribution_enable': 'attack_type_distribution_enable',
        'top_attacked_domains_enable': 'top_attacked_domains_enable',
        'top_attack_source_ips_enable': 'top_attack_source_ips_enable',
        'top_attacked_urls_enable': 'top_attacked_urls_enable',
        'top_attack_source_locations_enable': 'top_attack_source_locations_enable',
        'top_abnormal_urls_enable': 'top_abnormal_urls_enable'
    }

    def __init__(self, overview_statistics_enable=None, group_by_day_enable=None, request_statistics_enable=None, qps_statistics_enable=None, bandwidth_statistics_enable=None, response_code_statistics_enable=None, attack_type_distribution_enable=None, top_attacked_domains_enable=None, top_attack_source_ips_enable=None, top_attacked_urls_enable=None, top_attack_source_locations_enable=None, top_abnormal_urls_enable=None):
        r"""UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription

        The model defined in huaweicloud sdk

        :param overview_statistics_enable: 
        :type overview_statistics_enable: bool
        :param group_by_day_enable: 
        :type group_by_day_enable: bool
        :param request_statistics_enable: 
        :type request_statistics_enable: bool
        :param qps_statistics_enable: 
        :type qps_statistics_enable: bool
        :param bandwidth_statistics_enable: 
        :type bandwidth_statistics_enable: bool
        :param response_code_statistics_enable: 
        :type response_code_statistics_enable: bool
        :param attack_type_distribution_enable: 
        :type attack_type_distribution_enable: bool
        :param top_attacked_domains_enable: 
        :type top_attacked_domains_enable: bool
        :param top_attack_source_ips_enable: 
        :type top_attack_source_ips_enable: bool
        :param top_attacked_urls_enable: 
        :type top_attacked_urls_enable: bool
        :param top_attack_source_locations_enable: 
        :type top_attack_source_locations_enable: bool
        :param top_abnormal_urls_enable: 
        :type top_abnormal_urls_enable: bool
        """
        
        

        self._overview_statistics_enable = None
        self._group_by_day_enable = None
        self._request_statistics_enable = None
        self._qps_statistics_enable = None
        self._bandwidth_statistics_enable = None
        self._response_code_statistics_enable = None
        self._attack_type_distribution_enable = None
        self._top_attacked_domains_enable = None
        self._top_attack_source_ips_enable = None
        self._top_attacked_urls_enable = None
        self._top_attack_source_locations_enable = None
        self._top_abnormal_urls_enable = None
        self.discriminator = None

        if overview_statistics_enable is not None:
            self.overview_statistics_enable = overview_statistics_enable
        if group_by_day_enable is not None:
            self.group_by_day_enable = group_by_day_enable
        if request_statistics_enable is not None:
            self.request_statistics_enable = request_statistics_enable
        if qps_statistics_enable is not None:
            self.qps_statistics_enable = qps_statistics_enable
        if bandwidth_statistics_enable is not None:
            self.bandwidth_statistics_enable = bandwidth_statistics_enable
        if response_code_statistics_enable is not None:
            self.response_code_statistics_enable = response_code_statistics_enable
        if attack_type_distribution_enable is not None:
            self.attack_type_distribution_enable = attack_type_distribution_enable
        if top_attacked_domains_enable is not None:
            self.top_attacked_domains_enable = top_attacked_domains_enable
        if top_attack_source_ips_enable is not None:
            self.top_attack_source_ips_enable = top_attack_source_ips_enable
        if top_attacked_urls_enable is not None:
            self.top_attacked_urls_enable = top_attacked_urls_enable
        if top_attack_source_locations_enable is not None:
            self.top_attack_source_locations_enable = top_attack_source_locations_enable
        if top_abnormal_urls_enable is not None:
            self.top_abnormal_urls_enable = top_abnormal_urls_enable

    @property
    def overview_statistics_enable(self):
        r"""Gets the overview_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :return: The overview_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :rtype: bool
        """
        return self._overview_statistics_enable

    @overview_statistics_enable.setter
    def overview_statistics_enable(self, overview_statistics_enable):
        r"""Sets the overview_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :param overview_statistics_enable: The overview_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :type overview_statistics_enable: bool
        """
        self._overview_statistics_enable = overview_statistics_enable

    @property
    def group_by_day_enable(self):
        r"""Gets the group_by_day_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :return: The group_by_day_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :rtype: bool
        """
        return self._group_by_day_enable

    @group_by_day_enable.setter
    def group_by_day_enable(self, group_by_day_enable):
        r"""Sets the group_by_day_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :param group_by_day_enable: The group_by_day_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :type group_by_day_enable: bool
        """
        self._group_by_day_enable = group_by_day_enable

    @property
    def request_statistics_enable(self):
        r"""Gets the request_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :return: The request_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :rtype: bool
        """
        return self._request_statistics_enable

    @request_statistics_enable.setter
    def request_statistics_enable(self, request_statistics_enable):
        r"""Sets the request_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :param request_statistics_enable: The request_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :type request_statistics_enable: bool
        """
        self._request_statistics_enable = request_statistics_enable

    @property
    def qps_statistics_enable(self):
        r"""Gets the qps_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :return: The qps_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :rtype: bool
        """
        return self._qps_statistics_enable

    @qps_statistics_enable.setter
    def qps_statistics_enable(self, qps_statistics_enable):
        r"""Sets the qps_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :param qps_statistics_enable: The qps_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :type qps_statistics_enable: bool
        """
        self._qps_statistics_enable = qps_statistics_enable

    @property
    def bandwidth_statistics_enable(self):
        r"""Gets the bandwidth_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :return: The bandwidth_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :rtype: bool
        """
        return self._bandwidth_statistics_enable

    @bandwidth_statistics_enable.setter
    def bandwidth_statistics_enable(self, bandwidth_statistics_enable):
        r"""Sets the bandwidth_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :param bandwidth_statistics_enable: The bandwidth_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :type bandwidth_statistics_enable: bool
        """
        self._bandwidth_statistics_enable = bandwidth_statistics_enable

    @property
    def response_code_statistics_enable(self):
        r"""Gets the response_code_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :return: The response_code_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :rtype: bool
        """
        return self._response_code_statistics_enable

    @response_code_statistics_enable.setter
    def response_code_statistics_enable(self, response_code_statistics_enable):
        r"""Sets the response_code_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :param response_code_statistics_enable: The response_code_statistics_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :type response_code_statistics_enable: bool
        """
        self._response_code_statistics_enable = response_code_statistics_enable

    @property
    def attack_type_distribution_enable(self):
        r"""Gets the attack_type_distribution_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :return: The attack_type_distribution_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :rtype: bool
        """
        return self._attack_type_distribution_enable

    @attack_type_distribution_enable.setter
    def attack_type_distribution_enable(self, attack_type_distribution_enable):
        r"""Sets the attack_type_distribution_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :param attack_type_distribution_enable: The attack_type_distribution_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :type attack_type_distribution_enable: bool
        """
        self._attack_type_distribution_enable = attack_type_distribution_enable

    @property
    def top_attacked_domains_enable(self):
        r"""Gets the top_attacked_domains_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :return: The top_attacked_domains_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :rtype: bool
        """
        return self._top_attacked_domains_enable

    @top_attacked_domains_enable.setter
    def top_attacked_domains_enable(self, top_attacked_domains_enable):
        r"""Sets the top_attacked_domains_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :param top_attacked_domains_enable: The top_attacked_domains_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :type top_attacked_domains_enable: bool
        """
        self._top_attacked_domains_enable = top_attacked_domains_enable

    @property
    def top_attack_source_ips_enable(self):
        r"""Gets the top_attack_source_ips_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :return: The top_attack_source_ips_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :rtype: bool
        """
        return self._top_attack_source_ips_enable

    @top_attack_source_ips_enable.setter
    def top_attack_source_ips_enable(self, top_attack_source_ips_enable):
        r"""Sets the top_attack_source_ips_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :param top_attack_source_ips_enable: The top_attack_source_ips_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :type top_attack_source_ips_enable: bool
        """
        self._top_attack_source_ips_enable = top_attack_source_ips_enable

    @property
    def top_attacked_urls_enable(self):
        r"""Gets the top_attacked_urls_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :return: The top_attacked_urls_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :rtype: bool
        """
        return self._top_attacked_urls_enable

    @top_attacked_urls_enable.setter
    def top_attacked_urls_enable(self, top_attacked_urls_enable):
        r"""Sets the top_attacked_urls_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :param top_attacked_urls_enable: The top_attacked_urls_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :type top_attacked_urls_enable: bool
        """
        self._top_attacked_urls_enable = top_attacked_urls_enable

    @property
    def top_attack_source_locations_enable(self):
        r"""Gets the top_attack_source_locations_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :return: The top_attack_source_locations_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :rtype: bool
        """
        return self._top_attack_source_locations_enable

    @top_attack_source_locations_enable.setter
    def top_attack_source_locations_enable(self, top_attack_source_locations_enable):
        r"""Sets the top_attack_source_locations_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :param top_attack_source_locations_enable: The top_attack_source_locations_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :type top_attack_source_locations_enable: bool
        """
        self._top_attack_source_locations_enable = top_attack_source_locations_enable

    @property
    def top_abnormal_urls_enable(self):
        r"""Gets the top_abnormal_urls_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :return: The top_abnormal_urls_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :rtype: bool
        """
        return self._top_abnormal_urls_enable

    @top_abnormal_urls_enable.setter
    def top_abnormal_urls_enable(self, top_abnormal_urls_enable):
        r"""Sets the top_abnormal_urls_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.

        :param top_abnormal_urls_enable: The top_abnormal_urls_enable of this UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription.
        :type top_abnormal_urls_enable: bool
        """
        self._top_abnormal_urls_enable = top_abnormal_urls_enable

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
        if not isinstance(other, UpdateSecurityReportSubscriptionRequestBodyReportContentSubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
