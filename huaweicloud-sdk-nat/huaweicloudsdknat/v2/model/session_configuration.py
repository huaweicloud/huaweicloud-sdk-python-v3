# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SessionConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tcp_session_expire_time': 'int',
        'udp_session_expire_time': 'int',
        'icmp_session_expire_time': 'int',
        'tcp_time_wait_time': 'int'
    }

    attribute_map = {
        'tcp_session_expire_time': 'tcp_session_expire_time',
        'udp_session_expire_time': 'udp_session_expire_time',
        'icmp_session_expire_time': 'icmp_session_expire_time',
        'tcp_time_wait_time': 'tcp_time_wait_time'
    }

    def __init__(self, tcp_session_expire_time=None, udp_session_expire_time=None, icmp_session_expire_time=None, tcp_time_wait_time=None):
        r"""SessionConfiguration

        The model defined in huaweicloud sdk

        :param tcp_session_expire_time: TCP会话过期时间。
        :type tcp_session_expire_time: int
        :param udp_session_expire_time: UDP会话过期时间。
        :type udp_session_expire_time: int
        :param icmp_session_expire_time: ICMP会话过期时间。
        :type icmp_session_expire_time: int
        :param tcp_time_wait_time: TCP连接关闭时TIME_WAIT状态持续时间。
        :type tcp_time_wait_time: int
        """
        
        

        self._tcp_session_expire_time = None
        self._udp_session_expire_time = None
        self._icmp_session_expire_time = None
        self._tcp_time_wait_time = None
        self.discriminator = None

        if tcp_session_expire_time is not None:
            self.tcp_session_expire_time = tcp_session_expire_time
        if udp_session_expire_time is not None:
            self.udp_session_expire_time = udp_session_expire_time
        if icmp_session_expire_time is not None:
            self.icmp_session_expire_time = icmp_session_expire_time
        if tcp_time_wait_time is not None:
            self.tcp_time_wait_time = tcp_time_wait_time

    @property
    def tcp_session_expire_time(self):
        r"""Gets the tcp_session_expire_time of this SessionConfiguration.

        TCP会话过期时间。

        :return: The tcp_session_expire_time of this SessionConfiguration.
        :rtype: int
        """
        return self._tcp_session_expire_time

    @tcp_session_expire_time.setter
    def tcp_session_expire_time(self, tcp_session_expire_time):
        r"""Sets the tcp_session_expire_time of this SessionConfiguration.

        TCP会话过期时间。

        :param tcp_session_expire_time: The tcp_session_expire_time of this SessionConfiguration.
        :type tcp_session_expire_time: int
        """
        self._tcp_session_expire_time = tcp_session_expire_time

    @property
    def udp_session_expire_time(self):
        r"""Gets the udp_session_expire_time of this SessionConfiguration.

        UDP会话过期时间。

        :return: The udp_session_expire_time of this SessionConfiguration.
        :rtype: int
        """
        return self._udp_session_expire_time

    @udp_session_expire_time.setter
    def udp_session_expire_time(self, udp_session_expire_time):
        r"""Sets the udp_session_expire_time of this SessionConfiguration.

        UDP会话过期时间。

        :param udp_session_expire_time: The udp_session_expire_time of this SessionConfiguration.
        :type udp_session_expire_time: int
        """
        self._udp_session_expire_time = udp_session_expire_time

    @property
    def icmp_session_expire_time(self):
        r"""Gets the icmp_session_expire_time of this SessionConfiguration.

        ICMP会话过期时间。

        :return: The icmp_session_expire_time of this SessionConfiguration.
        :rtype: int
        """
        return self._icmp_session_expire_time

    @icmp_session_expire_time.setter
    def icmp_session_expire_time(self, icmp_session_expire_time):
        r"""Sets the icmp_session_expire_time of this SessionConfiguration.

        ICMP会话过期时间。

        :param icmp_session_expire_time: The icmp_session_expire_time of this SessionConfiguration.
        :type icmp_session_expire_time: int
        """
        self._icmp_session_expire_time = icmp_session_expire_time

    @property
    def tcp_time_wait_time(self):
        r"""Gets the tcp_time_wait_time of this SessionConfiguration.

        TCP连接关闭时TIME_WAIT状态持续时间。

        :return: The tcp_time_wait_time of this SessionConfiguration.
        :rtype: int
        """
        return self._tcp_time_wait_time

    @tcp_time_wait_time.setter
    def tcp_time_wait_time(self, tcp_time_wait_time):
        r"""Sets the tcp_time_wait_time of this SessionConfiguration.

        TCP连接关闭时TIME_WAIT状态持续时间。

        :param tcp_time_wait_time: The tcp_time_wait_time of this SessionConfiguration.
        :type tcp_time_wait_time: int
        """
        self._tcp_time_wait_time = tcp_time_wait_time

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
        if not isinstance(other, SessionConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
