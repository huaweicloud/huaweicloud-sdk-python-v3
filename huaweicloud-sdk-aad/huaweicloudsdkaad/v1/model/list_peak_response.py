# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPeakResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attack_kbps_peak': 'float',
        'in_kbps_peak': 'float',
        'ddos_count': 'float',
        'timestamp': 'float',
        'vip': 'str'
    }

    attribute_map = {
        'attack_kbps_peak': 'attack_kbps_peak',
        'in_kbps_peak': 'in_kbps_peak',
        'ddos_count': 'ddos_count',
        'timestamp': 'timestamp',
        'vip': 'vip'
    }

    def __init__(self, attack_kbps_peak=None, in_kbps_peak=None, ddos_count=None, timestamp=None, vip=None):
        r"""ListPeakResponse

        The model defined in huaweicloud sdk

        :param attack_kbps_peak: 攻击峰值
        :type attack_kbps_peak: float
        :param in_kbps_peak: 流量峰值
        :type in_kbps_peak: float
        :param ddos_count: 攻击次数
        :type ddos_count: float
        :param timestamp: 攻击峰值发生时间点
        :type timestamp: float
        :param vip: 高防IP
        :type vip: str
        """
        
        super(ListPeakResponse, self).__init__()

        self._attack_kbps_peak = None
        self._in_kbps_peak = None
        self._ddos_count = None
        self._timestamp = None
        self._vip = None
        self.discriminator = None

        if attack_kbps_peak is not None:
            self.attack_kbps_peak = attack_kbps_peak
        if in_kbps_peak is not None:
            self.in_kbps_peak = in_kbps_peak
        if ddos_count is not None:
            self.ddos_count = ddos_count
        if timestamp is not None:
            self.timestamp = timestamp
        if vip is not None:
            self.vip = vip

    @property
    def attack_kbps_peak(self):
        r"""Gets the attack_kbps_peak of this ListPeakResponse.

        攻击峰值

        :return: The attack_kbps_peak of this ListPeakResponse.
        :rtype: float
        """
        return self._attack_kbps_peak

    @attack_kbps_peak.setter
    def attack_kbps_peak(self, attack_kbps_peak):
        r"""Sets the attack_kbps_peak of this ListPeakResponse.

        攻击峰值

        :param attack_kbps_peak: The attack_kbps_peak of this ListPeakResponse.
        :type attack_kbps_peak: float
        """
        self._attack_kbps_peak = attack_kbps_peak

    @property
    def in_kbps_peak(self):
        r"""Gets the in_kbps_peak of this ListPeakResponse.

        流量峰值

        :return: The in_kbps_peak of this ListPeakResponse.
        :rtype: float
        """
        return self._in_kbps_peak

    @in_kbps_peak.setter
    def in_kbps_peak(self, in_kbps_peak):
        r"""Sets the in_kbps_peak of this ListPeakResponse.

        流量峰值

        :param in_kbps_peak: The in_kbps_peak of this ListPeakResponse.
        :type in_kbps_peak: float
        """
        self._in_kbps_peak = in_kbps_peak

    @property
    def ddos_count(self):
        r"""Gets the ddos_count of this ListPeakResponse.

        攻击次数

        :return: The ddos_count of this ListPeakResponse.
        :rtype: float
        """
        return self._ddos_count

    @ddos_count.setter
    def ddos_count(self, ddos_count):
        r"""Sets the ddos_count of this ListPeakResponse.

        攻击次数

        :param ddos_count: The ddos_count of this ListPeakResponse.
        :type ddos_count: float
        """
        self._ddos_count = ddos_count

    @property
    def timestamp(self):
        r"""Gets the timestamp of this ListPeakResponse.

        攻击峰值发生时间点

        :return: The timestamp of this ListPeakResponse.
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this ListPeakResponse.

        攻击峰值发生时间点

        :param timestamp: The timestamp of this ListPeakResponse.
        :type timestamp: float
        """
        self._timestamp = timestamp

    @property
    def vip(self):
        r"""Gets the vip of this ListPeakResponse.

        高防IP

        :return: The vip of this ListPeakResponse.
        :rtype: str
        """
        return self._vip

    @vip.setter
    def vip(self, vip):
        r"""Sets the vip of this ListPeakResponse.

        高防IP

        :param vip: The vip of this ListPeakResponse.
        :type vip: str
        """
        self._vip = vip

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
        if not isinstance(other, ListPeakResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
