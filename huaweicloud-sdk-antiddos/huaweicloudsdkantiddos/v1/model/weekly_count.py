# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WeeklyCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ddos_intercept_times': 'int',
        'ddos_blackhole_times': 'int',
        'max_attack_bps': 'int',
        'max_attack_conns': 'int',
        'period_start_date': 'int'
    }

    attribute_map = {
        'ddos_intercept_times': 'ddos_intercept_times',
        'ddos_blackhole_times': 'ddos_blackhole_times',
        'max_attack_bps': 'max_attack_bps',
        'max_attack_conns': 'max_attack_conns',
        'period_start_date': 'period_start_date'
    }

    def __init__(self, ddos_intercept_times=None, ddos_blackhole_times=None, max_attack_bps=None, max_attack_conns=None, period_start_date=None):
        """WeeklyCount

        The model defined in huaweicloud sdk

        :param ddos_intercept_times: DDoS拦截次数
        :type ddos_intercept_times: int
        :param ddos_blackhole_times: DDoS黑洞次数
        :type ddos_blackhole_times: int
        :param max_attack_bps: 最大攻击流量
        :type max_attack_bps: int
        :param max_attack_conns: 最大攻击连接数
        :type max_attack_conns: int
        :param period_start_date: 开始时间
        :type period_start_date: int
        """
        
        

        self._ddos_intercept_times = None
        self._ddos_blackhole_times = None
        self._max_attack_bps = None
        self._max_attack_conns = None
        self._period_start_date = None
        self.discriminator = None

        self.ddos_intercept_times = ddos_intercept_times
        self.ddos_blackhole_times = ddos_blackhole_times
        self.max_attack_bps = max_attack_bps
        self.max_attack_conns = max_attack_conns
        self.period_start_date = period_start_date

    @property
    def ddos_intercept_times(self):
        """Gets the ddos_intercept_times of this WeeklyCount.

        DDoS拦截次数

        :return: The ddos_intercept_times of this WeeklyCount.
        :rtype: int
        """
        return self._ddos_intercept_times

    @ddos_intercept_times.setter
    def ddos_intercept_times(self, ddos_intercept_times):
        """Sets the ddos_intercept_times of this WeeklyCount.

        DDoS拦截次数

        :param ddos_intercept_times: The ddos_intercept_times of this WeeklyCount.
        :type ddos_intercept_times: int
        """
        self._ddos_intercept_times = ddos_intercept_times

    @property
    def ddos_blackhole_times(self):
        """Gets the ddos_blackhole_times of this WeeklyCount.

        DDoS黑洞次数

        :return: The ddos_blackhole_times of this WeeklyCount.
        :rtype: int
        """
        return self._ddos_blackhole_times

    @ddos_blackhole_times.setter
    def ddos_blackhole_times(self, ddos_blackhole_times):
        """Sets the ddos_blackhole_times of this WeeklyCount.

        DDoS黑洞次数

        :param ddos_blackhole_times: The ddos_blackhole_times of this WeeklyCount.
        :type ddos_blackhole_times: int
        """
        self._ddos_blackhole_times = ddos_blackhole_times

    @property
    def max_attack_bps(self):
        """Gets the max_attack_bps of this WeeklyCount.

        最大攻击流量

        :return: The max_attack_bps of this WeeklyCount.
        :rtype: int
        """
        return self._max_attack_bps

    @max_attack_bps.setter
    def max_attack_bps(self, max_attack_bps):
        """Sets the max_attack_bps of this WeeklyCount.

        最大攻击流量

        :param max_attack_bps: The max_attack_bps of this WeeklyCount.
        :type max_attack_bps: int
        """
        self._max_attack_bps = max_attack_bps

    @property
    def max_attack_conns(self):
        """Gets the max_attack_conns of this WeeklyCount.

        最大攻击连接数

        :return: The max_attack_conns of this WeeklyCount.
        :rtype: int
        """
        return self._max_attack_conns

    @max_attack_conns.setter
    def max_attack_conns(self, max_attack_conns):
        """Sets the max_attack_conns of this WeeklyCount.

        最大攻击连接数

        :param max_attack_conns: The max_attack_conns of this WeeklyCount.
        :type max_attack_conns: int
        """
        self._max_attack_conns = max_attack_conns

    @property
    def period_start_date(self):
        """Gets the period_start_date of this WeeklyCount.

        开始时间

        :return: The period_start_date of this WeeklyCount.
        :rtype: int
        """
        return self._period_start_date

    @period_start_date.setter
    def period_start_date(self, period_start_date):
        """Sets the period_start_date of this WeeklyCount.

        开始时间

        :param period_start_date: The period_start_date of this WeeklyCount.
        :type period_start_date: int
        """
        self._period_start_date = period_start_date

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
        if not isinstance(other, WeeklyCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
