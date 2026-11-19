# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HoneypotEventResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_name': 'str',
        'host_id': 'str',
        'agent_id': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'severity': 'str',
        'attack_ip': 'str',
        'attack_num': 'int',
        'attack_last_time': 'int',
        'attack_start_time': 'int',
        'device_fingerprint': 'str'
    }

    attribute_map = {
        'host_name': 'host_name',
        'host_id': 'host_id',
        'agent_id': 'agent_id',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'severity': 'severity',
        'attack_ip': 'attack_ip',
        'attack_num': 'attack_num',
        'attack_last_time': 'attack_last_time',
        'attack_start_time': 'attack_start_time',
        'device_fingerprint': 'device_fingerprint'
    }

    def __init__(self, host_name=None, host_id=None, agent_id=None, private_ip=None, public_ip=None, severity=None, attack_ip=None, attack_num=None, attack_last_time=None, attack_start_time=None, device_fingerprint=None):
        r"""HoneypotEventResponseInfo

        The model defined in huaweicloud sdk

        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param host_id: **参数解释**: 服务器的唯一标识ID **取值范围**: 字符长度1-64位 
        :type host_id: str
        :param agent_id: **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **取值范围**: 字符长度1-64位 
        :type agent_id: str
        :param private_ip: **参数解释**: 服务器私有IP **取值范围**: 字符长度1-128位 
        :type private_ip: str
        :param public_ip: **参数解释**: 服务器弹性IP地址 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） 
        :type public_ip: str
        :param severity: **参数解释**： 威胁等级 **取值范围**： - Security：安全 - Low: 低危 - Medium: 中危 - High: 高危 - Critical: 危急 
        :type severity: str
        :param attack_ip: **参数解释**: 攻击源IP **取值范围**: 字符长度1-128位 
        :type attack_ip: str
        :param attack_num: **参数解释**: 攻击次数 **取值范围**: 最小值0，最大值2147483547 
        :type attack_num: int
        :param attack_last_time: **参数解释**: 最近攻击时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807 
        :type attack_last_time: int
        :param attack_start_time: **参数解释**: 攻击开始时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807 
        :type attack_start_time: int
        :param device_fingerprint: **参数解释**: 设备指纹 **取值范围**: 字符长度1-512位 
        :type device_fingerprint: str
        """
        
        

        self._host_name = None
        self._host_id = None
        self._agent_id = None
        self._private_ip = None
        self._public_ip = None
        self._severity = None
        self._attack_ip = None
        self._attack_num = None
        self._attack_last_time = None
        self._attack_start_time = None
        self._device_fingerprint = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if agent_id is not None:
            self.agent_id = agent_id
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if severity is not None:
            self.severity = severity
        if attack_ip is not None:
            self.attack_ip = attack_ip
        if attack_num is not None:
            self.attack_num = attack_num
        if attack_last_time is not None:
            self.attack_last_time = attack_last_time
        if attack_start_time is not None:
            self.attack_start_time = attack_start_time
        if device_fingerprint is not None:
            self.device_fingerprint = device_fingerprint

    @property
    def host_name(self):
        r"""Gets the host_name of this HoneypotEventResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this HoneypotEventResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this HoneypotEventResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this HoneypotEventResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this HoneypotEventResponseInfo.

        **参数解释**: 服务器的唯一标识ID **取值范围**: 字符长度1-64位 

        :return: The host_id of this HoneypotEventResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this HoneypotEventResponseInfo.

        **参数解释**: 服务器的唯一标识ID **取值范围**: 字符长度1-64位 

        :param host_id: The host_id of this HoneypotEventResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def agent_id(self):
        r"""Gets the agent_id of this HoneypotEventResponseInfo.

        **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **取值范围**: 字符长度1-64位 

        :return: The agent_id of this HoneypotEventResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this HoneypotEventResponseInfo.

        **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **取值范围**: 字符长度1-64位 

        :param agent_id: The agent_id of this HoneypotEventResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this HoneypotEventResponseInfo.

        **参数解释**: 服务器私有IP **取值范围**: 字符长度1-128位 

        :return: The private_ip of this HoneypotEventResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this HoneypotEventResponseInfo.

        **参数解释**: 服务器私有IP **取值范围**: 字符长度1-128位 

        :param private_ip: The private_ip of this HoneypotEventResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this HoneypotEventResponseInfo.

        **参数解释**: 服务器弹性IP地址 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） 

        :return: The public_ip of this HoneypotEventResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this HoneypotEventResponseInfo.

        **参数解释**: 服务器弹性IP地址 **取值范围**: IPv4格式（长度7-15位）、IPv6格式（长度15-39位） 

        :param public_ip: The public_ip of this HoneypotEventResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def severity(self):
        r"""Gets the severity of this HoneypotEventResponseInfo.

        **参数解释**： 威胁等级 **取值范围**： - Security：安全 - Low: 低危 - Medium: 中危 - High: 高危 - Critical: 危急 

        :return: The severity of this HoneypotEventResponseInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this HoneypotEventResponseInfo.

        **参数解释**： 威胁等级 **取值范围**： - Security：安全 - Low: 低危 - Medium: 中危 - High: 高危 - Critical: 危急 

        :param severity: The severity of this HoneypotEventResponseInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def attack_ip(self):
        r"""Gets the attack_ip of this HoneypotEventResponseInfo.

        **参数解释**: 攻击源IP **取值范围**: 字符长度1-128位 

        :return: The attack_ip of this HoneypotEventResponseInfo.
        :rtype: str
        """
        return self._attack_ip

    @attack_ip.setter
    def attack_ip(self, attack_ip):
        r"""Sets the attack_ip of this HoneypotEventResponseInfo.

        **参数解释**: 攻击源IP **取值范围**: 字符长度1-128位 

        :param attack_ip: The attack_ip of this HoneypotEventResponseInfo.
        :type attack_ip: str
        """
        self._attack_ip = attack_ip

    @property
    def attack_num(self):
        r"""Gets the attack_num of this HoneypotEventResponseInfo.

        **参数解释**: 攻击次数 **取值范围**: 最小值0，最大值2147483547 

        :return: The attack_num of this HoneypotEventResponseInfo.
        :rtype: int
        """
        return self._attack_num

    @attack_num.setter
    def attack_num(self, attack_num):
        r"""Sets the attack_num of this HoneypotEventResponseInfo.

        **参数解释**: 攻击次数 **取值范围**: 最小值0，最大值2147483547 

        :param attack_num: The attack_num of this HoneypotEventResponseInfo.
        :type attack_num: int
        """
        self._attack_num = attack_num

    @property
    def attack_last_time(self):
        r"""Gets the attack_last_time of this HoneypotEventResponseInfo.

        **参数解释**: 最近攻击时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The attack_last_time of this HoneypotEventResponseInfo.
        :rtype: int
        """
        return self._attack_last_time

    @attack_last_time.setter
    def attack_last_time(self, attack_last_time):
        r"""Sets the attack_last_time of this HoneypotEventResponseInfo.

        **参数解释**: 最近攻击时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807 

        :param attack_last_time: The attack_last_time of this HoneypotEventResponseInfo.
        :type attack_last_time: int
        """
        self._attack_last_time = attack_last_time

    @property
    def attack_start_time(self):
        r"""Gets the attack_start_time of this HoneypotEventResponseInfo.

        **参数解释**: 攻击开始时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The attack_start_time of this HoneypotEventResponseInfo.
        :rtype: int
        """
        return self._attack_start_time

    @attack_start_time.setter
    def attack_start_time(self, attack_start_time):
        r"""Sets the attack_start_time of this HoneypotEventResponseInfo.

        **参数解释**: 攻击开始时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807 

        :param attack_start_time: The attack_start_time of this HoneypotEventResponseInfo.
        :type attack_start_time: int
        """
        self._attack_start_time = attack_start_time

    @property
    def device_fingerprint(self):
        r"""Gets the device_fingerprint of this HoneypotEventResponseInfo.

        **参数解释**: 设备指纹 **取值范围**: 字符长度1-512位 

        :return: The device_fingerprint of this HoneypotEventResponseInfo.
        :rtype: str
        """
        return self._device_fingerprint

    @device_fingerprint.setter
    def device_fingerprint(self, device_fingerprint):
        r"""Sets the device_fingerprint of this HoneypotEventResponseInfo.

        **参数解释**: 设备指纹 **取值范围**: 字符长度1-512位 

        :param device_fingerprint: The device_fingerprint of this HoneypotEventResponseInfo.
        :type device_fingerprint: str
        """
        self._device_fingerprint = device_fingerprint

    def to_dict(self):
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
        if not isinstance(other, HoneypotEventResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
