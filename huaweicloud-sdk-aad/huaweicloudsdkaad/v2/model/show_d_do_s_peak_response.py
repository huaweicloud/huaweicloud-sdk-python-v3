# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDDoSPeakResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attack_kbytes_total': 'int',
        'attack_pps_peak': 'int',
        'in_pps_peak': 'int',
        'attack_bps_peak': 'int',
        'in_bps_peak': 'int',
        'ddos_count': 'int',
        'utime': 'int'
    }

    attribute_map = {
        'attack_kbytes_total': 'attack_kbytes_total',
        'attack_pps_peak': 'attack_pps_peak',
        'in_pps_peak': 'in_pps_peak',
        'attack_bps_peak': 'attack_bps_peak',
        'in_bps_peak': 'in_bps_peak',
        'ddos_count': 'ddos_count',
        'utime': 'utime'
    }

    def __init__(self, attack_kbytes_total=None, attack_pps_peak=None, in_pps_peak=None, attack_bps_peak=None, in_bps_peak=None, ddos_count=None, utime=None):
        r"""ShowDDoSPeakResponse

        The model defined in huaweicloud sdk

        :param attack_kbytes_total: 攻击流量
        :type attack_kbytes_total: int
        :param attack_pps_peak: 攻击流量峰值包速率
        :type attack_pps_peak: int
        :param in_pps_peak: 入流量峰值包速率
        :type in_pps_peak: int
        :param attack_bps_peak: 攻击流量峰值
        :type attack_bps_peak: int
        :param in_bps_peak: 入流量峰值
        :type in_bps_peak: int
        :param ddos_count: 攻击数量
        :type ddos_count: int
        :param utime: 峰值时间
        :type utime: int
        """
        
        super().__init__()

        self._attack_kbytes_total = None
        self._attack_pps_peak = None
        self._in_pps_peak = None
        self._attack_bps_peak = None
        self._in_bps_peak = None
        self._ddos_count = None
        self._utime = None
        self.discriminator = None

        if attack_kbytes_total is not None:
            self.attack_kbytes_total = attack_kbytes_total
        if attack_pps_peak is not None:
            self.attack_pps_peak = attack_pps_peak
        if in_pps_peak is not None:
            self.in_pps_peak = in_pps_peak
        if attack_bps_peak is not None:
            self.attack_bps_peak = attack_bps_peak
        if in_bps_peak is not None:
            self.in_bps_peak = in_bps_peak
        if ddos_count is not None:
            self.ddos_count = ddos_count
        if utime is not None:
            self.utime = utime

    @property
    def attack_kbytes_total(self):
        r"""Gets the attack_kbytes_total of this ShowDDoSPeakResponse.

        攻击流量

        :return: The attack_kbytes_total of this ShowDDoSPeakResponse.
        :rtype: int
        """
        return self._attack_kbytes_total

    @attack_kbytes_total.setter
    def attack_kbytes_total(self, attack_kbytes_total):
        r"""Sets the attack_kbytes_total of this ShowDDoSPeakResponse.

        攻击流量

        :param attack_kbytes_total: The attack_kbytes_total of this ShowDDoSPeakResponse.
        :type attack_kbytes_total: int
        """
        self._attack_kbytes_total = attack_kbytes_total

    @property
    def attack_pps_peak(self):
        r"""Gets the attack_pps_peak of this ShowDDoSPeakResponse.

        攻击流量峰值包速率

        :return: The attack_pps_peak of this ShowDDoSPeakResponse.
        :rtype: int
        """
        return self._attack_pps_peak

    @attack_pps_peak.setter
    def attack_pps_peak(self, attack_pps_peak):
        r"""Sets the attack_pps_peak of this ShowDDoSPeakResponse.

        攻击流量峰值包速率

        :param attack_pps_peak: The attack_pps_peak of this ShowDDoSPeakResponse.
        :type attack_pps_peak: int
        """
        self._attack_pps_peak = attack_pps_peak

    @property
    def in_pps_peak(self):
        r"""Gets the in_pps_peak of this ShowDDoSPeakResponse.

        入流量峰值包速率

        :return: The in_pps_peak of this ShowDDoSPeakResponse.
        :rtype: int
        """
        return self._in_pps_peak

    @in_pps_peak.setter
    def in_pps_peak(self, in_pps_peak):
        r"""Sets the in_pps_peak of this ShowDDoSPeakResponse.

        入流量峰值包速率

        :param in_pps_peak: The in_pps_peak of this ShowDDoSPeakResponse.
        :type in_pps_peak: int
        """
        self._in_pps_peak = in_pps_peak

    @property
    def attack_bps_peak(self):
        r"""Gets the attack_bps_peak of this ShowDDoSPeakResponse.

        攻击流量峰值

        :return: The attack_bps_peak of this ShowDDoSPeakResponse.
        :rtype: int
        """
        return self._attack_bps_peak

    @attack_bps_peak.setter
    def attack_bps_peak(self, attack_bps_peak):
        r"""Sets the attack_bps_peak of this ShowDDoSPeakResponse.

        攻击流量峰值

        :param attack_bps_peak: The attack_bps_peak of this ShowDDoSPeakResponse.
        :type attack_bps_peak: int
        """
        self._attack_bps_peak = attack_bps_peak

    @property
    def in_bps_peak(self):
        r"""Gets the in_bps_peak of this ShowDDoSPeakResponse.

        入流量峰值

        :return: The in_bps_peak of this ShowDDoSPeakResponse.
        :rtype: int
        """
        return self._in_bps_peak

    @in_bps_peak.setter
    def in_bps_peak(self, in_bps_peak):
        r"""Sets the in_bps_peak of this ShowDDoSPeakResponse.

        入流量峰值

        :param in_bps_peak: The in_bps_peak of this ShowDDoSPeakResponse.
        :type in_bps_peak: int
        """
        self._in_bps_peak = in_bps_peak

    @property
    def ddos_count(self):
        r"""Gets the ddos_count of this ShowDDoSPeakResponse.

        攻击数量

        :return: The ddos_count of this ShowDDoSPeakResponse.
        :rtype: int
        """
        return self._ddos_count

    @ddos_count.setter
    def ddos_count(self, ddos_count):
        r"""Sets the ddos_count of this ShowDDoSPeakResponse.

        攻击数量

        :param ddos_count: The ddos_count of this ShowDDoSPeakResponse.
        :type ddos_count: int
        """
        self._ddos_count = ddos_count

    @property
    def utime(self):
        r"""Gets the utime of this ShowDDoSPeakResponse.

        峰值时间

        :return: The utime of this ShowDDoSPeakResponse.
        :rtype: int
        """
        return self._utime

    @utime.setter
    def utime(self, utime):
        r"""Sets the utime of this ShowDDoSPeakResponse.

        峰值时间

        :param utime: The utime of this ShowDDoSPeakResponse.
        :type utime: int
        """
        self._utime = utime

    def to_dict(self):
        import warnings
        warnings.warn("ShowDDoSPeakResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowDDoSPeakResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
