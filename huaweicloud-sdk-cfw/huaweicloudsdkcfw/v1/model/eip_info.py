# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EipInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip_id': 'str',
        'fw_instance_id': 'str',
        'object_id': 'str',
        'public_ip': 'str',
        'public_ipv6': 'str',
        'type': 'int'
    }

    attribute_map = {
        'eip_id': 'eip_id',
        'fw_instance_id': 'fw_instance_id',
        'object_id': 'object_id',
        'public_ip': 'public_ip',
        'public_ipv6': 'public_ipv6',
        'type': 'type'
    }

    def __init__(self, eip_id=None, fw_instance_id=None, object_id=None, public_ip=None, public_ipv6=None, type=None):
        r"""EipInfo

        The model defined in huaweicloud sdk

        :param eip_id: **参数解释**： 弹性公网ID，可通过调用弹性IP列表查询获取，通过返回值中的data.records.id（.表示各对象之间层级的区分）获得 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type eip_id: str
        :param fw_instance_id: **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type fw_instance_id: str
        :param object_id: **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志ID，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象ID，type为1的为VPC边界防护对象ID。 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type object_id: str
        :param public_ip: **参数解释**： IPV4地址  **约束限制**： 不涉及 **取值范围**： 不涉及   **默认取值**： 不涉及
        :type public_ip: str
        :param public_ipv6: **参数解释**： IPV6地址  **约束限制**： 不涉及 **取值范围**： 不涉及   **默认取值**： 不涉及
        :type public_ipv6: str
        :param type: **参数解释**： EIP白名单标志 **约束限制**： 不涉及 **取值范围**： 0表示是EIP白名单，1表示不是EIP白名单 **默认取值**： 不涉及
        :type type: int
        """
        
        

        self._eip_id = None
        self._fw_instance_id = None
        self._object_id = None
        self._public_ip = None
        self._public_ipv6 = None
        self._type = None
        self.discriminator = None

        if eip_id is not None:
            self.eip_id = eip_id
        if fw_instance_id is not None:
            self.fw_instance_id = fw_instance_id
        if object_id is not None:
            self.object_id = object_id
        if public_ip is not None:
            self.public_ip = public_ip
        if public_ipv6 is not None:
            self.public_ipv6 = public_ipv6
        if type is not None:
            self.type = type

    @property
    def eip_id(self):
        r"""Gets the eip_id of this EipInfo.

        **参数解释**： 弹性公网ID，可通过调用弹性IP列表查询获取，通过返回值中的data.records.id（.表示各对象之间层级的区分）获得 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The eip_id of this EipInfo.
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        r"""Sets the eip_id of this EipInfo.

        **参数解释**： 弹性公网ID，可通过调用弹性IP列表查询获取，通过返回值中的data.records.id（.表示各对象之间层级的区分）获得 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param eip_id: The eip_id of this EipInfo.
        :type eip_id: str
        """
        self._eip_id = eip_id

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this EipInfo.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The fw_instance_id of this EipInfo.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this EipInfo.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param fw_instance_id: The fw_instance_id of this EipInfo.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def object_id(self):
        r"""Gets the object_id of this EipInfo.

        **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志ID，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象ID，type为1的为VPC边界防护对象ID。 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The object_id of this EipInfo.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this EipInfo.

        **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志ID，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象ID，type为1的为VPC边界防护对象ID。 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param object_id: The object_id of this EipInfo.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this EipInfo.

        **参数解释**： IPV4地址  **约束限制**： 不涉及 **取值范围**： 不涉及   **默认取值**： 不涉及

        :return: The public_ip of this EipInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this EipInfo.

        **参数解释**： IPV4地址  **约束限制**： 不涉及 **取值范围**： 不涉及   **默认取值**： 不涉及

        :param public_ip: The public_ip of this EipInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def public_ipv6(self):
        r"""Gets the public_ipv6 of this EipInfo.

        **参数解释**： IPV6地址  **约束限制**： 不涉及 **取值范围**： 不涉及   **默认取值**： 不涉及

        :return: The public_ipv6 of this EipInfo.
        :rtype: str
        """
        return self._public_ipv6

    @public_ipv6.setter
    def public_ipv6(self, public_ipv6):
        r"""Sets the public_ipv6 of this EipInfo.

        **参数解释**： IPV6地址  **约束限制**： 不涉及 **取值范围**： 不涉及   **默认取值**： 不涉及

        :param public_ipv6: The public_ipv6 of this EipInfo.
        :type public_ipv6: str
        """
        self._public_ipv6 = public_ipv6

    @property
    def type(self):
        r"""Gets the type of this EipInfo.

        **参数解释**： EIP白名单标志 **约束限制**： 不涉及 **取值范围**： 0表示是EIP白名单，1表示不是EIP白名单 **默认取值**： 不涉及

        :return: The type of this EipInfo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EipInfo.

        **参数解释**： EIP白名单标志 **约束限制**： 不涉及 **取值范围**： 0表示是EIP白名单，1表示不是EIP白名单 **默认取值**： 不涉及

        :param type: The type of this EipInfo.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, EipInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
