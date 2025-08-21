# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FirewallReport:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attack_info': 'AttackReport',
        'category': 'str',
        'internet_firewall': 'InternetReport',
        'send_time': 'int',
        'statistic_period': 'StatisticPeriod',
        'vpc_firewall': 'VpcReport'
    }

    attribute_map = {
        'attack_info': 'attack_info',
        'category': 'category',
        'internet_firewall': 'internet_firewall',
        'send_time': 'send_time',
        'statistic_period': 'statistic_period',
        'vpc_firewall': 'vpc_firewall'
    }

    def __init__(self, attack_info=None, category=None, internet_firewall=None, send_time=None, statistic_period=None, vpc_firewall=None):
        r"""FirewallReport

        The model defined in huaweicloud sdk

        :param attack_info: 
        :type attack_info: :class:`huaweicloudsdkcfw.v1.AttackReport`
        :param category: **参数解释**： 报告类型 **取值范围**： 不涉及
        :type category: str
        :param internet_firewall: 
        :type internet_firewall: :class:`huaweicloudsdkcfw.v1.InternetReport`
        :param send_time: **参数解释**： 发送时间 **取值范围**： 不涉及
        :type send_time: int
        :param statistic_period: 
        :type statistic_period: :class:`huaweicloudsdkcfw.v1.StatisticPeriod`
        :param vpc_firewall: 
        :type vpc_firewall: :class:`huaweicloudsdkcfw.v1.VpcReport`
        """
        
        

        self._attack_info = None
        self._category = None
        self._internet_firewall = None
        self._send_time = None
        self._statistic_period = None
        self._vpc_firewall = None
        self.discriminator = None

        if attack_info is not None:
            self.attack_info = attack_info
        if category is not None:
            self.category = category
        if internet_firewall is not None:
            self.internet_firewall = internet_firewall
        if send_time is not None:
            self.send_time = send_time
        if statistic_period is not None:
            self.statistic_period = statistic_period
        if vpc_firewall is not None:
            self.vpc_firewall = vpc_firewall

    @property
    def attack_info(self):
        r"""Gets the attack_info of this FirewallReport.

        :return: The attack_info of this FirewallReport.
        :rtype: :class:`huaweicloudsdkcfw.v1.AttackReport`
        """
        return self._attack_info

    @attack_info.setter
    def attack_info(self, attack_info):
        r"""Sets the attack_info of this FirewallReport.

        :param attack_info: The attack_info of this FirewallReport.
        :type attack_info: :class:`huaweicloudsdkcfw.v1.AttackReport`
        """
        self._attack_info = attack_info

    @property
    def category(self):
        r"""Gets the category of this FirewallReport.

        **参数解释**： 报告类型 **取值范围**： 不涉及

        :return: The category of this FirewallReport.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this FirewallReport.

        **参数解释**： 报告类型 **取值范围**： 不涉及

        :param category: The category of this FirewallReport.
        :type category: str
        """
        self._category = category

    @property
    def internet_firewall(self):
        r"""Gets the internet_firewall of this FirewallReport.

        :return: The internet_firewall of this FirewallReport.
        :rtype: :class:`huaweicloudsdkcfw.v1.InternetReport`
        """
        return self._internet_firewall

    @internet_firewall.setter
    def internet_firewall(self, internet_firewall):
        r"""Sets the internet_firewall of this FirewallReport.

        :param internet_firewall: The internet_firewall of this FirewallReport.
        :type internet_firewall: :class:`huaweicloudsdkcfw.v1.InternetReport`
        """
        self._internet_firewall = internet_firewall

    @property
    def send_time(self):
        r"""Gets the send_time of this FirewallReport.

        **参数解释**： 发送时间 **取值范围**： 不涉及

        :return: The send_time of this FirewallReport.
        :rtype: int
        """
        return self._send_time

    @send_time.setter
    def send_time(self, send_time):
        r"""Sets the send_time of this FirewallReport.

        **参数解释**： 发送时间 **取值范围**： 不涉及

        :param send_time: The send_time of this FirewallReport.
        :type send_time: int
        """
        self._send_time = send_time

    @property
    def statistic_period(self):
        r"""Gets the statistic_period of this FirewallReport.

        :return: The statistic_period of this FirewallReport.
        :rtype: :class:`huaweicloudsdkcfw.v1.StatisticPeriod`
        """
        return self._statistic_period

    @statistic_period.setter
    def statistic_period(self, statistic_period):
        r"""Sets the statistic_period of this FirewallReport.

        :param statistic_period: The statistic_period of this FirewallReport.
        :type statistic_period: :class:`huaweicloudsdkcfw.v1.StatisticPeriod`
        """
        self._statistic_period = statistic_period

    @property
    def vpc_firewall(self):
        r"""Gets the vpc_firewall of this FirewallReport.

        :return: The vpc_firewall of this FirewallReport.
        :rtype: :class:`huaweicloudsdkcfw.v1.VpcReport`
        """
        return self._vpc_firewall

    @vpc_firewall.setter
    def vpc_firewall(self, vpc_firewall):
        r"""Sets the vpc_firewall of this FirewallReport.

        :param vpc_firewall: The vpc_firewall of this FirewallReport.
        :type vpc_firewall: :class:`huaweicloudsdkcfw.v1.VpcReport`
        """
        self._vpc_firewall = vpc_firewall

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
        if not isinstance(other, FirewallReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
