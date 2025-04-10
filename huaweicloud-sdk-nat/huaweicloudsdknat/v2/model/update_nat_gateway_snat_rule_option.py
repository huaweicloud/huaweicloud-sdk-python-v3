# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNatGatewaySnatRuleOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nat_gateway_id': 'str',
        'public_ip_address': 'str',
        'global_eip_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'nat_gateway_id': 'nat_gateway_id',
        'public_ip_address': 'public_ip_address',
        'global_eip_id': 'global_eip_id',
        'description': 'description'
    }

    def __init__(self, nat_gateway_id=None, public_ip_address=None, global_eip_id=None, description=None):
        r"""UpdateNatGatewaySnatRuleOption

        The model defined in huaweicloud sdk

        :param nat_gateway_id: 公网NAT网关的id。
        :type nat_gateway_id: str
        :param public_ip_address: 功能说明：弹性公网IP，多个弹性公网IP使用逗号分隔。 约束：弹性公网IP的id个数不能超过20个 
        :type public_ip_address: str
        :param global_eip_id: 全域弹性公网IP的id。
        :type global_eip_id: str
        :param description: SNAT规则的描述，长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        """
        
        

        self._nat_gateway_id = None
        self._public_ip_address = None
        self._global_eip_id = None
        self._description = None
        self.discriminator = None

        self.nat_gateway_id = nat_gateway_id
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if global_eip_id is not None:
            self.global_eip_id = global_eip_id
        if description is not None:
            self.description = description

    @property
    def nat_gateway_id(self):
        r"""Gets the nat_gateway_id of this UpdateNatGatewaySnatRuleOption.

        公网NAT网关的id。

        :return: The nat_gateway_id of this UpdateNatGatewaySnatRuleOption.
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        r"""Sets the nat_gateway_id of this UpdateNatGatewaySnatRuleOption.

        公网NAT网关的id。

        :param nat_gateway_id: The nat_gateway_id of this UpdateNatGatewaySnatRuleOption.
        :type nat_gateway_id: str
        """
        self._nat_gateway_id = nat_gateway_id

    @property
    def public_ip_address(self):
        r"""Gets the public_ip_address of this UpdateNatGatewaySnatRuleOption.

        功能说明：弹性公网IP，多个弹性公网IP使用逗号分隔。 约束：弹性公网IP的id个数不能超过20个 

        :return: The public_ip_address of this UpdateNatGatewaySnatRuleOption.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        r"""Sets the public_ip_address of this UpdateNatGatewaySnatRuleOption.

        功能说明：弹性公网IP，多个弹性公网IP使用逗号分隔。 约束：弹性公网IP的id个数不能超过20个 

        :param public_ip_address: The public_ip_address of this UpdateNatGatewaySnatRuleOption.
        :type public_ip_address: str
        """
        self._public_ip_address = public_ip_address

    @property
    def global_eip_id(self):
        r"""Gets the global_eip_id of this UpdateNatGatewaySnatRuleOption.

        全域弹性公网IP的id。

        :return: The global_eip_id of this UpdateNatGatewaySnatRuleOption.
        :rtype: str
        """
        return self._global_eip_id

    @global_eip_id.setter
    def global_eip_id(self, global_eip_id):
        r"""Sets the global_eip_id of this UpdateNatGatewaySnatRuleOption.

        全域弹性公网IP的id。

        :param global_eip_id: The global_eip_id of this UpdateNatGatewaySnatRuleOption.
        :type global_eip_id: str
        """
        self._global_eip_id = global_eip_id

    @property
    def description(self):
        r"""Gets the description of this UpdateNatGatewaySnatRuleOption.

        SNAT规则的描述，长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this UpdateNatGatewaySnatRuleOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateNatGatewaySnatRuleOption.

        SNAT规则的描述，长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this UpdateNatGatewaySnatRuleOption.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpdateNatGatewaySnatRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
