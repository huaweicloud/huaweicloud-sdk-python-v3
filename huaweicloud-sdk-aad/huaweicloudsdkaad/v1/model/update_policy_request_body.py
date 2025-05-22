# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'threshold': 'int',
        'description': 'str',
        'udp': 'str',
        'tcp': 'str',
        'icmp': 'str',
        'other': 'str',
        'icmp_traffic_limiting': 'int',
        'udp_traffic_limiting': 'int',
        'udp_fragment_rate_limiting': 'int',
        'other_traffic_limiting': 'int',
        'tcp_traffic_limiting': 'int',
        'tcp_fragment_rate_limiting': 'int'
    }

    attribute_map = {
        'name': 'name',
        'threshold': 'threshold',
        'description': 'description',
        'udp': 'udp',
        'tcp': 'tcp',
        'icmp': 'icmp',
        'other': 'other',
        'icmp_traffic_limiting': 'icmp_traffic_limiting',
        'udp_traffic_limiting': 'udp_traffic_limiting',
        'udp_fragment_rate_limiting': 'udp_fragment_rate_limiting',
        'other_traffic_limiting': 'other_traffic_limiting',
        'tcp_traffic_limiting': 'tcp_traffic_limiting',
        'tcp_fragment_rate_limiting': 'tcp_fragment_rate_limiting'
    }

    def __init__(self, name=None, threshold=None, description=None, udp=None, tcp=None, icmp=None, other=None, icmp_traffic_limiting=None, udp_traffic_limiting=None, udp_fragment_rate_limiting=None, other_traffic_limiting=None, tcp_traffic_limiting=None, tcp_fragment_rate_limiting=None):
        r"""UpdatePolicyRequestBody

        The model defined in huaweicloud sdk

        :param name: 策略名
        :type name: str
        :param threshold: 清洗阈值
        :type threshold: int
        :param description: 描述
        :type description: str
        :param udp: udp协议设置。block：封禁，unblock：不封禁，limiting：限速
        :type udp: str
        :param tcp: tcp协议设置。block：封禁，unblock：不封禁，limiting：限速
        :type tcp: str
        :param icmp: icmp协议设置。block：封禁，unblock：不封禁，limiting：限速
        :type icmp: str
        :param other: other协议设置。block：封禁，unblock：不封禁，limiting：限速
        :type other: str
        :param icmp_traffic_limiting: icmp自定义限速值，icmp取值limiting情况下，如果该值为空表示不限速
        :type icmp_traffic_limiting: int
        :param udp_traffic_limiting: udp自定义限速值，udp取值limiting情况下，如果该值为空表示不限速
        :type udp_traffic_limiting: int
        :param udp_fragment_rate_limiting: udp分片自定义限速值，udp取值limiting情况下，如果该值为空表示不限速
        :type udp_fragment_rate_limiting: int
        :param other_traffic_limiting: other自定义限速值，other取值limiting情况下，如果该值为空表示不限速
        :type other_traffic_limiting: int
        :param tcp_traffic_limiting: tcp自定义限速值，tcp取值limiting情况下，如果该值为空表示不限速
        :type tcp_traffic_limiting: int
        :param tcp_fragment_rate_limiting: tcp分片自定义限速值，tcp取值limiting情况下，如果该值为空表示不限速
        :type tcp_fragment_rate_limiting: int
        """
        
        

        self._name = None
        self._threshold = None
        self._description = None
        self._udp = None
        self._tcp = None
        self._icmp = None
        self._other = None
        self._icmp_traffic_limiting = None
        self._udp_traffic_limiting = None
        self._udp_fragment_rate_limiting = None
        self._other_traffic_limiting = None
        self._tcp_traffic_limiting = None
        self._tcp_fragment_rate_limiting = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if threshold is not None:
            self.threshold = threshold
        if description is not None:
            self.description = description
        if udp is not None:
            self.udp = udp
        if tcp is not None:
            self.tcp = tcp
        if icmp is not None:
            self.icmp = icmp
        if other is not None:
            self.other = other
        if icmp_traffic_limiting is not None:
            self.icmp_traffic_limiting = icmp_traffic_limiting
        if udp_traffic_limiting is not None:
            self.udp_traffic_limiting = udp_traffic_limiting
        if udp_fragment_rate_limiting is not None:
            self.udp_fragment_rate_limiting = udp_fragment_rate_limiting
        if other_traffic_limiting is not None:
            self.other_traffic_limiting = other_traffic_limiting
        if tcp_traffic_limiting is not None:
            self.tcp_traffic_limiting = tcp_traffic_limiting
        if tcp_fragment_rate_limiting is not None:
            self.tcp_fragment_rate_limiting = tcp_fragment_rate_limiting

    @property
    def name(self):
        r"""Gets the name of this UpdatePolicyRequestBody.

        策略名

        :return: The name of this UpdatePolicyRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdatePolicyRequestBody.

        策略名

        :param name: The name of this UpdatePolicyRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def threshold(self):
        r"""Gets the threshold of this UpdatePolicyRequestBody.

        清洗阈值

        :return: The threshold of this UpdatePolicyRequestBody.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this UpdatePolicyRequestBody.

        清洗阈值

        :param threshold: The threshold of this UpdatePolicyRequestBody.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def description(self):
        r"""Gets the description of this UpdatePolicyRequestBody.

        描述

        :return: The description of this UpdatePolicyRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdatePolicyRequestBody.

        描述

        :param description: The description of this UpdatePolicyRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def udp(self):
        r"""Gets the udp of this UpdatePolicyRequestBody.

        udp协议设置。block：封禁，unblock：不封禁，limiting：限速

        :return: The udp of this UpdatePolicyRequestBody.
        :rtype: str
        """
        return self._udp

    @udp.setter
    def udp(self, udp):
        r"""Sets the udp of this UpdatePolicyRequestBody.

        udp协议设置。block：封禁，unblock：不封禁，limiting：限速

        :param udp: The udp of this UpdatePolicyRequestBody.
        :type udp: str
        """
        self._udp = udp

    @property
    def tcp(self):
        r"""Gets the tcp of this UpdatePolicyRequestBody.

        tcp协议设置。block：封禁，unblock：不封禁，limiting：限速

        :return: The tcp of this UpdatePolicyRequestBody.
        :rtype: str
        """
        return self._tcp

    @tcp.setter
    def tcp(self, tcp):
        r"""Sets the tcp of this UpdatePolicyRequestBody.

        tcp协议设置。block：封禁，unblock：不封禁，limiting：限速

        :param tcp: The tcp of this UpdatePolicyRequestBody.
        :type tcp: str
        """
        self._tcp = tcp

    @property
    def icmp(self):
        r"""Gets the icmp of this UpdatePolicyRequestBody.

        icmp协议设置。block：封禁，unblock：不封禁，limiting：限速

        :return: The icmp of this UpdatePolicyRequestBody.
        :rtype: str
        """
        return self._icmp

    @icmp.setter
    def icmp(self, icmp):
        r"""Sets the icmp of this UpdatePolicyRequestBody.

        icmp协议设置。block：封禁，unblock：不封禁，limiting：限速

        :param icmp: The icmp of this UpdatePolicyRequestBody.
        :type icmp: str
        """
        self._icmp = icmp

    @property
    def other(self):
        r"""Gets the other of this UpdatePolicyRequestBody.

        other协议设置。block：封禁，unblock：不封禁，limiting：限速

        :return: The other of this UpdatePolicyRequestBody.
        :rtype: str
        """
        return self._other

    @other.setter
    def other(self, other):
        r"""Sets the other of this UpdatePolicyRequestBody.

        other协议设置。block：封禁，unblock：不封禁，limiting：限速

        :param other: The other of this UpdatePolicyRequestBody.
        :type other: str
        """
        self._other = other

    @property
    def icmp_traffic_limiting(self):
        r"""Gets the icmp_traffic_limiting of this UpdatePolicyRequestBody.

        icmp自定义限速值，icmp取值limiting情况下，如果该值为空表示不限速

        :return: The icmp_traffic_limiting of this UpdatePolicyRequestBody.
        :rtype: int
        """
        return self._icmp_traffic_limiting

    @icmp_traffic_limiting.setter
    def icmp_traffic_limiting(self, icmp_traffic_limiting):
        r"""Sets the icmp_traffic_limiting of this UpdatePolicyRequestBody.

        icmp自定义限速值，icmp取值limiting情况下，如果该值为空表示不限速

        :param icmp_traffic_limiting: The icmp_traffic_limiting of this UpdatePolicyRequestBody.
        :type icmp_traffic_limiting: int
        """
        self._icmp_traffic_limiting = icmp_traffic_limiting

    @property
    def udp_traffic_limiting(self):
        r"""Gets the udp_traffic_limiting of this UpdatePolicyRequestBody.

        udp自定义限速值，udp取值limiting情况下，如果该值为空表示不限速

        :return: The udp_traffic_limiting of this UpdatePolicyRequestBody.
        :rtype: int
        """
        return self._udp_traffic_limiting

    @udp_traffic_limiting.setter
    def udp_traffic_limiting(self, udp_traffic_limiting):
        r"""Sets the udp_traffic_limiting of this UpdatePolicyRequestBody.

        udp自定义限速值，udp取值limiting情况下，如果该值为空表示不限速

        :param udp_traffic_limiting: The udp_traffic_limiting of this UpdatePolicyRequestBody.
        :type udp_traffic_limiting: int
        """
        self._udp_traffic_limiting = udp_traffic_limiting

    @property
    def udp_fragment_rate_limiting(self):
        r"""Gets the udp_fragment_rate_limiting of this UpdatePolicyRequestBody.

        udp分片自定义限速值，udp取值limiting情况下，如果该值为空表示不限速

        :return: The udp_fragment_rate_limiting of this UpdatePolicyRequestBody.
        :rtype: int
        """
        return self._udp_fragment_rate_limiting

    @udp_fragment_rate_limiting.setter
    def udp_fragment_rate_limiting(self, udp_fragment_rate_limiting):
        r"""Sets the udp_fragment_rate_limiting of this UpdatePolicyRequestBody.

        udp分片自定义限速值，udp取值limiting情况下，如果该值为空表示不限速

        :param udp_fragment_rate_limiting: The udp_fragment_rate_limiting of this UpdatePolicyRequestBody.
        :type udp_fragment_rate_limiting: int
        """
        self._udp_fragment_rate_limiting = udp_fragment_rate_limiting

    @property
    def other_traffic_limiting(self):
        r"""Gets the other_traffic_limiting of this UpdatePolicyRequestBody.

        other自定义限速值，other取值limiting情况下，如果该值为空表示不限速

        :return: The other_traffic_limiting of this UpdatePolicyRequestBody.
        :rtype: int
        """
        return self._other_traffic_limiting

    @other_traffic_limiting.setter
    def other_traffic_limiting(self, other_traffic_limiting):
        r"""Sets the other_traffic_limiting of this UpdatePolicyRequestBody.

        other自定义限速值，other取值limiting情况下，如果该值为空表示不限速

        :param other_traffic_limiting: The other_traffic_limiting of this UpdatePolicyRequestBody.
        :type other_traffic_limiting: int
        """
        self._other_traffic_limiting = other_traffic_limiting

    @property
    def tcp_traffic_limiting(self):
        r"""Gets the tcp_traffic_limiting of this UpdatePolicyRequestBody.

        tcp自定义限速值，tcp取值limiting情况下，如果该值为空表示不限速

        :return: The tcp_traffic_limiting of this UpdatePolicyRequestBody.
        :rtype: int
        """
        return self._tcp_traffic_limiting

    @tcp_traffic_limiting.setter
    def tcp_traffic_limiting(self, tcp_traffic_limiting):
        r"""Sets the tcp_traffic_limiting of this UpdatePolicyRequestBody.

        tcp自定义限速值，tcp取值limiting情况下，如果该值为空表示不限速

        :param tcp_traffic_limiting: The tcp_traffic_limiting of this UpdatePolicyRequestBody.
        :type tcp_traffic_limiting: int
        """
        self._tcp_traffic_limiting = tcp_traffic_limiting

    @property
    def tcp_fragment_rate_limiting(self):
        r"""Gets the tcp_fragment_rate_limiting of this UpdatePolicyRequestBody.

        tcp分片自定义限速值，tcp取值limiting情况下，如果该值为空表示不限速

        :return: The tcp_fragment_rate_limiting of this UpdatePolicyRequestBody.
        :rtype: int
        """
        return self._tcp_fragment_rate_limiting

    @tcp_fragment_rate_limiting.setter
    def tcp_fragment_rate_limiting(self, tcp_fragment_rate_limiting):
        r"""Sets the tcp_fragment_rate_limiting of this UpdatePolicyRequestBody.

        tcp分片自定义限速值，tcp取值limiting情况下，如果该值为空表示不限速

        :param tcp_fragment_rate_limiting: The tcp_fragment_rate_limiting of this UpdatePolicyRequestBody.
        :type tcp_fragment_rate_limiting: int
        """
        self._tcp_fragment_rate_limiting = tcp_fragment_rate_limiting

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
        if not isinstance(other, UpdatePolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
