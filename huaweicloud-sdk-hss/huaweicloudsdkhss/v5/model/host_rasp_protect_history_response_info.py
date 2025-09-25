# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostRaspProtectHistoryResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_ip': 'str',
        'host_name': 'str',
        'alarm_time': 'int',
        'threat_type': 'str',
        'alarm_level': 'int',
        'source_ip': 'str',
        'attacked_url': 'str'
    }

    attribute_map = {
        'host_ip': 'host_ip',
        'host_name': 'host_name',
        'alarm_time': 'alarm_time',
        'threat_type': 'threat_type',
        'alarm_level': 'alarm_level',
        'source_ip': 'source_ip',
        'attacked_url': 'attacked_url'
    }

    def __init__(self, host_ip=None, host_name=None, alarm_time=None, threat_type=None, alarm_level=None, source_ip=None, attacked_url=None):
        r"""HostRaspProtectHistoryResponseInfo

        The model defined in huaweicloud sdk

        :param host_ip: **参数解释**: 服务器IP **取值范围**: 字符长度0-64位 
        :type host_ip: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param alarm_time: **参数解释**: 告警时间，单位毫秒。 **取值范围**: 最小值0，最大值4070880000000 
        :type alarm_time: int
        :param threat_type: **参数解释**： 威胁类型 **取值范围**： 字符长度0-128位 
        :type threat_type: str
        :param alarm_level: **参数解释**: 告警等级 **取值范围**: - 1 : 紧急。 - 2 : 重要。 - 3 : 次要。 - 4 : 提示。 
        :type alarm_level: int
        :param source_ip: **参数解释**： 攻击源IP **取值范围**： 字符长度0-128位 
        :type source_ip: str
        :param attacked_url: **参数解释**： 攻击源URL **取值范围**： 字符长度0-2000位 
        :type attacked_url: str
        """
        
        

        self._host_ip = None
        self._host_name = None
        self._alarm_time = None
        self._threat_type = None
        self._alarm_level = None
        self._source_ip = None
        self._attacked_url = None
        self.discriminator = None

        if host_ip is not None:
            self.host_ip = host_ip
        if host_name is not None:
            self.host_name = host_name
        if alarm_time is not None:
            self.alarm_time = alarm_time
        if threat_type is not None:
            self.threat_type = threat_type
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if source_ip is not None:
            self.source_ip = source_ip
        if attacked_url is not None:
            self.attacked_url = attacked_url

    @property
    def host_ip(self):
        r"""Gets the host_ip of this HostRaspProtectHistoryResponseInfo.

        **参数解释**: 服务器IP **取值范围**: 字符长度0-64位 

        :return: The host_ip of this HostRaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this HostRaspProtectHistoryResponseInfo.

        **参数解释**: 服务器IP **取值范围**: 字符长度0-64位 

        :param host_ip: The host_ip of this HostRaspProtectHistoryResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def host_name(self):
        r"""Gets the host_name of this HostRaspProtectHistoryResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this HostRaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this HostRaspProtectHistoryResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this HostRaspProtectHistoryResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def alarm_time(self):
        r"""Gets the alarm_time of this HostRaspProtectHistoryResponseInfo.

        **参数解释**: 告警时间，单位毫秒。 **取值范围**: 最小值0，最大值4070880000000 

        :return: The alarm_time of this HostRaspProtectHistoryResponseInfo.
        :rtype: int
        """
        return self._alarm_time

    @alarm_time.setter
    def alarm_time(self, alarm_time):
        r"""Sets the alarm_time of this HostRaspProtectHistoryResponseInfo.

        **参数解释**: 告警时间，单位毫秒。 **取值范围**: 最小值0，最大值4070880000000 

        :param alarm_time: The alarm_time of this HostRaspProtectHistoryResponseInfo.
        :type alarm_time: int
        """
        self._alarm_time = alarm_time

    @property
    def threat_type(self):
        r"""Gets the threat_type of this HostRaspProtectHistoryResponseInfo.

        **参数解释**： 威胁类型 **取值范围**： 字符长度0-128位 

        :return: The threat_type of this HostRaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._threat_type

    @threat_type.setter
    def threat_type(self, threat_type):
        r"""Sets the threat_type of this HostRaspProtectHistoryResponseInfo.

        **参数解释**： 威胁类型 **取值范围**： 字符长度0-128位 

        :param threat_type: The threat_type of this HostRaspProtectHistoryResponseInfo.
        :type threat_type: str
        """
        self._threat_type = threat_type

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this HostRaspProtectHistoryResponseInfo.

        **参数解释**: 告警等级 **取值范围**: - 1 : 紧急。 - 2 : 重要。 - 3 : 次要。 - 4 : 提示。 

        :return: The alarm_level of this HostRaspProtectHistoryResponseInfo.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this HostRaspProtectHistoryResponseInfo.

        **参数解释**: 告警等级 **取值范围**: - 1 : 紧急。 - 2 : 重要。 - 3 : 次要。 - 4 : 提示。 

        :param alarm_level: The alarm_level of this HostRaspProtectHistoryResponseInfo.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def source_ip(self):
        r"""Gets the source_ip of this HostRaspProtectHistoryResponseInfo.

        **参数解释**： 攻击源IP **取值范围**： 字符长度0-128位 

        :return: The source_ip of this HostRaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        r"""Sets the source_ip of this HostRaspProtectHistoryResponseInfo.

        **参数解释**： 攻击源IP **取值范围**： 字符长度0-128位 

        :param source_ip: The source_ip of this HostRaspProtectHistoryResponseInfo.
        :type source_ip: str
        """
        self._source_ip = source_ip

    @property
    def attacked_url(self):
        r"""Gets the attacked_url of this HostRaspProtectHistoryResponseInfo.

        **参数解释**： 攻击源URL **取值范围**： 字符长度0-2000位 

        :return: The attacked_url of this HostRaspProtectHistoryResponseInfo.
        :rtype: str
        """
        return self._attacked_url

    @attacked_url.setter
    def attacked_url(self, attacked_url):
        r"""Sets the attacked_url of this HostRaspProtectHistoryResponseInfo.

        **参数解释**： 攻击源URL **取值范围**： 字符长度0-2000位 

        :param attacked_url: The attacked_url of this HostRaspProtectHistoryResponseInfo.
        :type attacked_url: str
        """
        self._attacked_url = attacked_url

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
        if not isinstance(other, HostRaspProtectHistoryResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
