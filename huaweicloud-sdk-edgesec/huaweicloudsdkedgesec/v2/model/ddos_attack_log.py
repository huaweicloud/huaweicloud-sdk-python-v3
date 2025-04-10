# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DdosAttackLog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attack_time': 'int',
        'avg_bps': 'int',
        'avg_pps': 'int',
        'max_bps': 'int',
        'max_pps': 'int'
    }

    attribute_map = {
        'attack_time': 'attack_time',
        'avg_bps': 'avg_bps',
        'avg_pps': 'avg_pps',
        'max_bps': 'max_bps',
        'max_pps': 'max_pps'
    }

    def __init__(self, attack_time=None, avg_bps=None, avg_pps=None, max_bps=None, max_pps=None):
        r"""DdosAttackLog

        The model defined in huaweicloud sdk

        :param attack_time: ddos攻击时间
        :type attack_time: int
        :param avg_bps: 攻击流量带宽平均值
        :type avg_bps: int
        :param avg_pps: 攻击流量带宽峰值
        :type avg_pps: int
        :param max_bps: 包转发率平均值
        :type max_bps: int
        :param max_pps: 包转发率峰值
        :type max_pps: int
        """
        
        

        self._attack_time = None
        self._avg_bps = None
        self._avg_pps = None
        self._max_bps = None
        self._max_pps = None
        self.discriminator = None

        if attack_time is not None:
            self.attack_time = attack_time
        if avg_bps is not None:
            self.avg_bps = avg_bps
        if avg_pps is not None:
            self.avg_pps = avg_pps
        if max_bps is not None:
            self.max_bps = max_bps
        if max_pps is not None:
            self.max_pps = max_pps

    @property
    def attack_time(self):
        r"""Gets the attack_time of this DdosAttackLog.

        ddos攻击时间

        :return: The attack_time of this DdosAttackLog.
        :rtype: int
        """
        return self._attack_time

    @attack_time.setter
    def attack_time(self, attack_time):
        r"""Sets the attack_time of this DdosAttackLog.

        ddos攻击时间

        :param attack_time: The attack_time of this DdosAttackLog.
        :type attack_time: int
        """
        self._attack_time = attack_time

    @property
    def avg_bps(self):
        r"""Gets the avg_bps of this DdosAttackLog.

        攻击流量带宽平均值

        :return: The avg_bps of this DdosAttackLog.
        :rtype: int
        """
        return self._avg_bps

    @avg_bps.setter
    def avg_bps(self, avg_bps):
        r"""Sets the avg_bps of this DdosAttackLog.

        攻击流量带宽平均值

        :param avg_bps: The avg_bps of this DdosAttackLog.
        :type avg_bps: int
        """
        self._avg_bps = avg_bps

    @property
    def avg_pps(self):
        r"""Gets the avg_pps of this DdosAttackLog.

        攻击流量带宽峰值

        :return: The avg_pps of this DdosAttackLog.
        :rtype: int
        """
        return self._avg_pps

    @avg_pps.setter
    def avg_pps(self, avg_pps):
        r"""Sets the avg_pps of this DdosAttackLog.

        攻击流量带宽峰值

        :param avg_pps: The avg_pps of this DdosAttackLog.
        :type avg_pps: int
        """
        self._avg_pps = avg_pps

    @property
    def max_bps(self):
        r"""Gets the max_bps of this DdosAttackLog.

        包转发率平均值

        :return: The max_bps of this DdosAttackLog.
        :rtype: int
        """
        return self._max_bps

    @max_bps.setter
    def max_bps(self, max_bps):
        r"""Sets the max_bps of this DdosAttackLog.

        包转发率平均值

        :param max_bps: The max_bps of this DdosAttackLog.
        :type max_bps: int
        """
        self._max_bps = max_bps

    @property
    def max_pps(self):
        r"""Gets the max_pps of this DdosAttackLog.

        包转发率峰值

        :return: The max_pps of this DdosAttackLog.
        :rtype: int
        """
        return self._max_pps

    @max_pps.setter
    def max_pps(self, max_pps):
        r"""Sets the max_pps of this DdosAttackLog.

        包转发率峰值

        :param max_pps: The max_pps of this DdosAttackLog.
        :type max_pps: int
        """
        self._max_pps = max_pps

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
        if not isinstance(other, DdosAttackLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
