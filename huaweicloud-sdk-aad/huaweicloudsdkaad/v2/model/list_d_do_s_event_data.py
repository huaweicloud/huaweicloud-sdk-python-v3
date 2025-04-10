# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDDoSEventData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_ip': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'max_drop_kbps': 'str',
        'max_drop_pps': 'str',
        'max_in_kbps': 'str',
        'max_in_pps': 'str',
        'attack_types': 'str',
        'attack_ips': 'str',
        'attack_ips_desc': 'str',
        'attack_status': 'str'
    }

    attribute_map = {
        'zone_ip': 'zone_ip',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'max_drop_kbps': 'max_drop_kbps',
        'max_drop_pps': 'max_drop_pps',
        'max_in_kbps': 'max_in_kbps',
        'max_in_pps': 'max_in_pps',
        'attack_types': 'attack_types',
        'attack_ips': 'attack_ips',
        'attack_ips_desc': 'attack_ips_desc',
        'attack_status': 'attack_status'
    }

    def __init__(self, zone_ip=None, start_time=None, end_time=None, max_drop_kbps=None, max_drop_pps=None, max_in_kbps=None, max_in_pps=None, attack_types=None, attack_ips=None, attack_ips_desc=None, attack_status=None):
        r"""ListDDoSEventData

        The model defined in huaweicloud sdk

        :param zone_ip: 防护IP
        :type zone_ip: str
        :param start_time: 开始时间（毫秒时间戳）
        :type start_time: str
        :param end_time: 结束时间（毫秒时间戳）
        :type end_time: str
        :param max_drop_kbps: 攻击流量峰值，单位“kbps”
        :type max_drop_kbps: str
        :param max_drop_pps: 攻击报文数峰值，单位“pps”
        :type max_drop_pps: str
        :param max_in_kbps: 入流量峰值，单位“kbps”
        :type max_in_kbps: str
        :param max_in_pps: 入报文数峰值，单位“pps”
        :type max_in_pps: str
        :param attack_types: 攻击类型
        :type attack_types: str
        :param attack_ips: 攻击源IP
        :type attack_ips: str
        :param attack_ips_desc: 攻击IP描述
        :type attack_ips_desc: str
        :param attack_status: 攻击状态
        :type attack_status: str
        """
        
        

        self._zone_ip = None
        self._start_time = None
        self._end_time = None
        self._max_drop_kbps = None
        self._max_drop_pps = None
        self._max_in_kbps = None
        self._max_in_pps = None
        self._attack_types = None
        self._attack_ips = None
        self._attack_ips_desc = None
        self._attack_status = None
        self.discriminator = None

        if zone_ip is not None:
            self.zone_ip = zone_ip
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if max_drop_kbps is not None:
            self.max_drop_kbps = max_drop_kbps
        if max_drop_pps is not None:
            self.max_drop_pps = max_drop_pps
        if max_in_kbps is not None:
            self.max_in_kbps = max_in_kbps
        if max_in_pps is not None:
            self.max_in_pps = max_in_pps
        if attack_types is not None:
            self.attack_types = attack_types
        if attack_ips is not None:
            self.attack_ips = attack_ips
        if attack_ips_desc is not None:
            self.attack_ips_desc = attack_ips_desc
        if attack_status is not None:
            self.attack_status = attack_status

    @property
    def zone_ip(self):
        r"""Gets the zone_ip of this ListDDoSEventData.

        防护IP

        :return: The zone_ip of this ListDDoSEventData.
        :rtype: str
        """
        return self._zone_ip

    @zone_ip.setter
    def zone_ip(self, zone_ip):
        r"""Sets the zone_ip of this ListDDoSEventData.

        防护IP

        :param zone_ip: The zone_ip of this ListDDoSEventData.
        :type zone_ip: str
        """
        self._zone_ip = zone_ip

    @property
    def start_time(self):
        r"""Gets the start_time of this ListDDoSEventData.

        开始时间（毫秒时间戳）

        :return: The start_time of this ListDDoSEventData.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListDDoSEventData.

        开始时间（毫秒时间戳）

        :param start_time: The start_time of this ListDDoSEventData.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListDDoSEventData.

        结束时间（毫秒时间戳）

        :return: The end_time of this ListDDoSEventData.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListDDoSEventData.

        结束时间（毫秒时间戳）

        :param end_time: The end_time of this ListDDoSEventData.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def max_drop_kbps(self):
        r"""Gets the max_drop_kbps of this ListDDoSEventData.

        攻击流量峰值，单位“kbps”

        :return: The max_drop_kbps of this ListDDoSEventData.
        :rtype: str
        """
        return self._max_drop_kbps

    @max_drop_kbps.setter
    def max_drop_kbps(self, max_drop_kbps):
        r"""Sets the max_drop_kbps of this ListDDoSEventData.

        攻击流量峰值，单位“kbps”

        :param max_drop_kbps: The max_drop_kbps of this ListDDoSEventData.
        :type max_drop_kbps: str
        """
        self._max_drop_kbps = max_drop_kbps

    @property
    def max_drop_pps(self):
        r"""Gets the max_drop_pps of this ListDDoSEventData.

        攻击报文数峰值，单位“pps”

        :return: The max_drop_pps of this ListDDoSEventData.
        :rtype: str
        """
        return self._max_drop_pps

    @max_drop_pps.setter
    def max_drop_pps(self, max_drop_pps):
        r"""Sets the max_drop_pps of this ListDDoSEventData.

        攻击报文数峰值，单位“pps”

        :param max_drop_pps: The max_drop_pps of this ListDDoSEventData.
        :type max_drop_pps: str
        """
        self._max_drop_pps = max_drop_pps

    @property
    def max_in_kbps(self):
        r"""Gets the max_in_kbps of this ListDDoSEventData.

        入流量峰值，单位“kbps”

        :return: The max_in_kbps of this ListDDoSEventData.
        :rtype: str
        """
        return self._max_in_kbps

    @max_in_kbps.setter
    def max_in_kbps(self, max_in_kbps):
        r"""Sets the max_in_kbps of this ListDDoSEventData.

        入流量峰值，单位“kbps”

        :param max_in_kbps: The max_in_kbps of this ListDDoSEventData.
        :type max_in_kbps: str
        """
        self._max_in_kbps = max_in_kbps

    @property
    def max_in_pps(self):
        r"""Gets the max_in_pps of this ListDDoSEventData.

        入报文数峰值，单位“pps”

        :return: The max_in_pps of this ListDDoSEventData.
        :rtype: str
        """
        return self._max_in_pps

    @max_in_pps.setter
    def max_in_pps(self, max_in_pps):
        r"""Sets the max_in_pps of this ListDDoSEventData.

        入报文数峰值，单位“pps”

        :param max_in_pps: The max_in_pps of this ListDDoSEventData.
        :type max_in_pps: str
        """
        self._max_in_pps = max_in_pps

    @property
    def attack_types(self):
        r"""Gets the attack_types of this ListDDoSEventData.

        攻击类型

        :return: The attack_types of this ListDDoSEventData.
        :rtype: str
        """
        return self._attack_types

    @attack_types.setter
    def attack_types(self, attack_types):
        r"""Sets the attack_types of this ListDDoSEventData.

        攻击类型

        :param attack_types: The attack_types of this ListDDoSEventData.
        :type attack_types: str
        """
        self._attack_types = attack_types

    @property
    def attack_ips(self):
        r"""Gets the attack_ips of this ListDDoSEventData.

        攻击源IP

        :return: The attack_ips of this ListDDoSEventData.
        :rtype: str
        """
        return self._attack_ips

    @attack_ips.setter
    def attack_ips(self, attack_ips):
        r"""Sets the attack_ips of this ListDDoSEventData.

        攻击源IP

        :param attack_ips: The attack_ips of this ListDDoSEventData.
        :type attack_ips: str
        """
        self._attack_ips = attack_ips

    @property
    def attack_ips_desc(self):
        r"""Gets the attack_ips_desc of this ListDDoSEventData.

        攻击IP描述

        :return: The attack_ips_desc of this ListDDoSEventData.
        :rtype: str
        """
        return self._attack_ips_desc

    @attack_ips_desc.setter
    def attack_ips_desc(self, attack_ips_desc):
        r"""Sets the attack_ips_desc of this ListDDoSEventData.

        攻击IP描述

        :param attack_ips_desc: The attack_ips_desc of this ListDDoSEventData.
        :type attack_ips_desc: str
        """
        self._attack_ips_desc = attack_ips_desc

    @property
    def attack_status(self):
        r"""Gets the attack_status of this ListDDoSEventData.

        攻击状态

        :return: The attack_status of this ListDDoSEventData.
        :rtype: str
        """
        return self._attack_status

    @attack_status.setter
    def attack_status(self, attack_status):
        r"""Sets the attack_status of this ListDDoSEventData.

        攻击状态

        :param attack_status: The attack_status of this ListDDoSEventData.
        :type attack_status: str
        """
        self._attack_status = attack_status

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
        if not isinstance(other, ListDDoSEventData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
