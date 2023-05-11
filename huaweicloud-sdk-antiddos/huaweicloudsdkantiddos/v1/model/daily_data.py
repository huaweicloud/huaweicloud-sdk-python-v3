# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DailyData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period_start': 'int',
        'bps_in': 'int',
        'bps_attack': 'int',
        'total_bps': 'int',
        'pps_in': 'int',
        'pps_attack': 'int',
        'total_pps': 'int'
    }

    attribute_map = {
        'period_start': 'period_start',
        'bps_in': 'bps_in',
        'bps_attack': 'bps_attack',
        'total_bps': 'total_bps',
        'pps_in': 'pps_in',
        'pps_attack': 'pps_attack',
        'total_pps': 'total_pps'
    }

    def __init__(self, period_start=None, bps_in=None, bps_attack=None, total_bps=None, pps_in=None, pps_attack=None, total_pps=None):
        """DailyData

        The model defined in huaweicloud sdk

        :param period_start: 开始时间
        :type period_start: int
        :param bps_in: 入流量（bit/s）
        :type bps_in: int
        :param bps_attack: 攻击流量（bit/s）
        :type bps_attack: int
        :param total_bps: 总流量
        :type total_bps: int
        :param pps_in: 入报文速率（个/s）
        :type pps_in: int
        :param pps_attack: 攻击文速率（个/s）
        :type pps_attack: int
        :param total_pps: 总报文速率
        :type total_pps: int
        """
        
        

        self._period_start = None
        self._bps_in = None
        self._bps_attack = None
        self._total_bps = None
        self._pps_in = None
        self._pps_attack = None
        self._total_pps = None
        self.discriminator = None

        self.period_start = period_start
        self.bps_in = bps_in
        self.bps_attack = bps_attack
        self.total_bps = total_bps
        self.pps_in = pps_in
        self.pps_attack = pps_attack
        self.total_pps = total_pps

    @property
    def period_start(self):
        """Gets the period_start of this DailyData.

        开始时间

        :return: The period_start of this DailyData.
        :rtype: int
        """
        return self._period_start

    @period_start.setter
    def period_start(self, period_start):
        """Sets the period_start of this DailyData.

        开始时间

        :param period_start: The period_start of this DailyData.
        :type period_start: int
        """
        self._period_start = period_start

    @property
    def bps_in(self):
        """Gets the bps_in of this DailyData.

        入流量（bit/s）

        :return: The bps_in of this DailyData.
        :rtype: int
        """
        return self._bps_in

    @bps_in.setter
    def bps_in(self, bps_in):
        """Sets the bps_in of this DailyData.

        入流量（bit/s）

        :param bps_in: The bps_in of this DailyData.
        :type bps_in: int
        """
        self._bps_in = bps_in

    @property
    def bps_attack(self):
        """Gets the bps_attack of this DailyData.

        攻击流量（bit/s）

        :return: The bps_attack of this DailyData.
        :rtype: int
        """
        return self._bps_attack

    @bps_attack.setter
    def bps_attack(self, bps_attack):
        """Sets the bps_attack of this DailyData.

        攻击流量（bit/s）

        :param bps_attack: The bps_attack of this DailyData.
        :type bps_attack: int
        """
        self._bps_attack = bps_attack

    @property
    def total_bps(self):
        """Gets the total_bps of this DailyData.

        总流量

        :return: The total_bps of this DailyData.
        :rtype: int
        """
        return self._total_bps

    @total_bps.setter
    def total_bps(self, total_bps):
        """Sets the total_bps of this DailyData.

        总流量

        :param total_bps: The total_bps of this DailyData.
        :type total_bps: int
        """
        self._total_bps = total_bps

    @property
    def pps_in(self):
        """Gets the pps_in of this DailyData.

        入报文速率（个/s）

        :return: The pps_in of this DailyData.
        :rtype: int
        """
        return self._pps_in

    @pps_in.setter
    def pps_in(self, pps_in):
        """Sets the pps_in of this DailyData.

        入报文速率（个/s）

        :param pps_in: The pps_in of this DailyData.
        :type pps_in: int
        """
        self._pps_in = pps_in

    @property
    def pps_attack(self):
        """Gets the pps_attack of this DailyData.

        攻击文速率（个/s）

        :return: The pps_attack of this DailyData.
        :rtype: int
        """
        return self._pps_attack

    @pps_attack.setter
    def pps_attack(self, pps_attack):
        """Sets the pps_attack of this DailyData.

        攻击文速率（个/s）

        :param pps_attack: The pps_attack of this DailyData.
        :type pps_attack: int
        """
        self._pps_attack = pps_attack

    @property
    def total_pps(self):
        """Gets the total_pps of this DailyData.

        总报文速率

        :return: The total_pps of this DailyData.
        :rtype: int
        """
        return self._total_pps

    @total_pps.setter
    def total_pps(self, total_pps):
        """Sets the total_pps of this DailyData.

        总报文速率

        :param total_pps: The total_pps of this DailyData.
        :type total_pps: int
        """
        self._total_pps = total_pps

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
        if not isinstance(other, DailyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
