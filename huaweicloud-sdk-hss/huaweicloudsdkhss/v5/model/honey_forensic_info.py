# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HoneyForensicInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attack_ip': 'str',
        'sandbox_name': 'str',
        'service_name': 'str',
        'attack_type': 'str',
        'attack_method_desc': 'str',
        'attack_desc': 'str'
    }

    attribute_map = {
        'attack_ip': 'attack_ip',
        'sandbox_name': 'sandbox_name',
        'service_name': 'service_name',
        'attack_type': 'attack_type',
        'attack_method_desc': 'attack_method_desc',
        'attack_desc': 'attack_desc'
    }

    def __init__(self, attack_ip=None, sandbox_name=None, service_name=None, attack_type=None, attack_method_desc=None, attack_desc=None):
        r"""HoneyForensicInfo

        The model defined in huaweicloud sdk

        :param attack_ip: **参数解释**： 攻击源 IP **取值范围**： 不涉及
        :type attack_ip: str
        :param sandbox_name: **参数解释**： 隔离沙箱名称 **取值范围**： 不涉及
        :type sandbox_name: str
        :param service_name: **参数解释**： 欺骗服务 **取值范围**： 不涉及
        :type service_name: str
        :param attack_type: **参数解释**： 攻击类型 **取值范围**： - probe：探测 - invade：入侵
        :type attack_type: str
        :param attack_method_desc: **参数解释**： 攻击手法 **取值范围**： 不涉及
        :type attack_method_desc: str
        :param attack_desc: **参数解释**： 攻击行为 **取值范围**： 不涉及
        :type attack_desc: str
        """
        
        

        self._attack_ip = None
        self._sandbox_name = None
        self._service_name = None
        self._attack_type = None
        self._attack_method_desc = None
        self._attack_desc = None
        self.discriminator = None

        if attack_ip is not None:
            self.attack_ip = attack_ip
        if sandbox_name is not None:
            self.sandbox_name = sandbox_name
        if service_name is not None:
            self.service_name = service_name
        if attack_type is not None:
            self.attack_type = attack_type
        if attack_method_desc is not None:
            self.attack_method_desc = attack_method_desc
        if attack_desc is not None:
            self.attack_desc = attack_desc

    @property
    def attack_ip(self):
        r"""Gets the attack_ip of this HoneyForensicInfo.

        **参数解释**： 攻击源 IP **取值范围**： 不涉及

        :return: The attack_ip of this HoneyForensicInfo.
        :rtype: str
        """
        return self._attack_ip

    @attack_ip.setter
    def attack_ip(self, attack_ip):
        r"""Sets the attack_ip of this HoneyForensicInfo.

        **参数解释**： 攻击源 IP **取值范围**： 不涉及

        :param attack_ip: The attack_ip of this HoneyForensicInfo.
        :type attack_ip: str
        """
        self._attack_ip = attack_ip

    @property
    def sandbox_name(self):
        r"""Gets the sandbox_name of this HoneyForensicInfo.

        **参数解释**： 隔离沙箱名称 **取值范围**： 不涉及

        :return: The sandbox_name of this HoneyForensicInfo.
        :rtype: str
        """
        return self._sandbox_name

    @sandbox_name.setter
    def sandbox_name(self, sandbox_name):
        r"""Sets the sandbox_name of this HoneyForensicInfo.

        **参数解释**： 隔离沙箱名称 **取值范围**： 不涉及

        :param sandbox_name: The sandbox_name of this HoneyForensicInfo.
        :type sandbox_name: str
        """
        self._sandbox_name = sandbox_name

    @property
    def service_name(self):
        r"""Gets the service_name of this HoneyForensicInfo.

        **参数解释**： 欺骗服务 **取值范围**： 不涉及

        :return: The service_name of this HoneyForensicInfo.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this HoneyForensicInfo.

        **参数解释**： 欺骗服务 **取值范围**： 不涉及

        :param service_name: The service_name of this HoneyForensicInfo.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def attack_type(self):
        r"""Gets the attack_type of this HoneyForensicInfo.

        **参数解释**： 攻击类型 **取值范围**： - probe：探测 - invade：入侵

        :return: The attack_type of this HoneyForensicInfo.
        :rtype: str
        """
        return self._attack_type

    @attack_type.setter
    def attack_type(self, attack_type):
        r"""Sets the attack_type of this HoneyForensicInfo.

        **参数解释**： 攻击类型 **取值范围**： - probe：探测 - invade：入侵

        :param attack_type: The attack_type of this HoneyForensicInfo.
        :type attack_type: str
        """
        self._attack_type = attack_type

    @property
    def attack_method_desc(self):
        r"""Gets the attack_method_desc of this HoneyForensicInfo.

        **参数解释**： 攻击手法 **取值范围**： 不涉及

        :return: The attack_method_desc of this HoneyForensicInfo.
        :rtype: str
        """
        return self._attack_method_desc

    @attack_method_desc.setter
    def attack_method_desc(self, attack_method_desc):
        r"""Sets the attack_method_desc of this HoneyForensicInfo.

        **参数解释**： 攻击手法 **取值范围**： 不涉及

        :param attack_method_desc: The attack_method_desc of this HoneyForensicInfo.
        :type attack_method_desc: str
        """
        self._attack_method_desc = attack_method_desc

    @property
    def attack_desc(self):
        r"""Gets the attack_desc of this HoneyForensicInfo.

        **参数解释**： 攻击行为 **取值范围**： 不涉及

        :return: The attack_desc of this HoneyForensicInfo.
        :rtype: str
        """
        return self._attack_desc

    @attack_desc.setter
    def attack_desc(self, attack_desc):
        r"""Sets the attack_desc of this HoneyForensicInfo.

        **参数解释**： 攻击行为 **取值范围**： 不涉及

        :param attack_desc: The attack_desc of this HoneyForensicInfo.
        :type attack_desc: str
        """
        self._attack_desc = attack_desc

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
        if not isinstance(other, HoneyForensicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
