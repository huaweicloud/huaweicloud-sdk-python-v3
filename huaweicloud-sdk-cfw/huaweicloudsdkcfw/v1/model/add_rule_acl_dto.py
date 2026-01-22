# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddRuleAclDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'type': 'int',
        'rules': 'list[AddRuleAclDtoRules]'
    }

    attribute_map = {
        'object_id': 'object_id',
        'type': 'type',
        'rules': 'rules'
    }

    def __init__(self, object_id=None, type=None, rules=None):
        r"""AddRuleAclDto

        The model defined in huaweicloud sdk

        :param object_id: **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志ID，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得 **约束限制**： type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type object_id: str
        :param type: **参数解释**： 规则类型，用于区分不同防护对象设置规则类型。 **约束限制**： 不涉及 **取值范围**：  0：互联网边界规则，源（source）和目的（destination）地址需要为公网IP或域名； 1：VPC间规则，源（source）和目的（destination）地址需要为私有ip； 2：NAT规则，源（source）地址需要为私网IP，目的地址为公网IP或域名。 **默认取值**： 不涉及
        :type type: int
        :param rules: **参数解释**： 添加规则请求规则列表 **约束限制**： 不涉及
        :type rules: list[:class:`huaweicloudsdkcfw.v1.AddRuleAclDtoRules`]
        """
        
        

        self._object_id = None
        self._type = None
        self._rules = None
        self.discriminator = None

        self.object_id = object_id
        self.type = type
        self.rules = rules

    @property
    def object_id(self):
        r"""Gets the object_id of this AddRuleAclDto.

        **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志ID，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得 **约束限制**： type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The object_id of this AddRuleAclDto.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this AddRuleAclDto.

        **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志ID，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得 **约束限制**： type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param object_id: The object_id of this AddRuleAclDto.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def type(self):
        r"""Gets the type of this AddRuleAclDto.

        **参数解释**： 规则类型，用于区分不同防护对象设置规则类型。 **约束限制**： 不涉及 **取值范围**：  0：互联网边界规则，源（source）和目的（destination）地址需要为公网IP或域名； 1：VPC间规则，源（source）和目的（destination）地址需要为私有ip； 2：NAT规则，源（source）地址需要为私网IP，目的地址为公网IP或域名。 **默认取值**： 不涉及

        :return: The type of this AddRuleAclDto.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AddRuleAclDto.

        **参数解释**： 规则类型，用于区分不同防护对象设置规则类型。 **约束限制**： 不涉及 **取值范围**：  0：互联网边界规则，源（source）和目的（destination）地址需要为公网IP或域名； 1：VPC间规则，源（source）和目的（destination）地址需要为私有ip； 2：NAT规则，源（source）地址需要为私网IP，目的地址为公网IP或域名。 **默认取值**： 不涉及

        :param type: The type of this AddRuleAclDto.
        :type type: int
        """
        self._type = type

    @property
    def rules(self):
        r"""Gets the rules of this AddRuleAclDto.

        **参数解释**： 添加规则请求规则列表 **约束限制**： 不涉及

        :return: The rules of this AddRuleAclDto.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AddRuleAclDtoRules`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this AddRuleAclDto.

        **参数解释**： 添加规则请求规则列表 **约束限制**： 不涉及

        :param rules: The rules of this AddRuleAclDto.
        :type rules: list[:class:`huaweicloudsdkcfw.v1.AddRuleAclDtoRules`]
        """
        self._rules = rules

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
        if not isinstance(other, AddRuleAclDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
