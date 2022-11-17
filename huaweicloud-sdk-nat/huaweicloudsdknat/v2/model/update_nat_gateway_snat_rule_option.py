# coding: utf-8

import re
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
        'description': 'str'
    }

    attribute_map = {
        'nat_gateway_id': 'nat_gateway_id',
        'public_ip_address': 'public_ip_address',
        'description': 'description'
    }

    def __init__(self, nat_gateway_id=None, public_ip_address=None, description=None):
        """UpdateNatGatewaySnatRuleOption

        The model defined in huaweicloud sdk

        :param nat_gateway_id: 公网NAT网关的id。
        :type nat_gateway_id: str
        :param public_ip_address: 功能说明：弹性公网IP，多个弹性公网IP使用逗号分隔。 取值范围：最大长度1024字节。 约束：弹性公网IP的id个数不能超过20个 
        :type public_ip_address: str
        :param description: SNAT规则的描述，长度限制为255。
        :type description: str
        """
        
        

        self._nat_gateway_id = None
        self._public_ip_address = None
        self._description = None
        self.discriminator = None

        self.nat_gateway_id = nat_gateway_id
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if description is not None:
            self.description = description

    @property
    def nat_gateway_id(self):
        """Gets the nat_gateway_id of this UpdateNatGatewaySnatRuleOption.

        公网NAT网关的id。

        :return: The nat_gateway_id of this UpdateNatGatewaySnatRuleOption.
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        """Sets the nat_gateway_id of this UpdateNatGatewaySnatRuleOption.

        公网NAT网关的id。

        :param nat_gateway_id: The nat_gateway_id of this UpdateNatGatewaySnatRuleOption.
        :type nat_gateway_id: str
        """
        self._nat_gateway_id = nat_gateway_id

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this UpdateNatGatewaySnatRuleOption.

        功能说明：弹性公网IP，多个弹性公网IP使用逗号分隔。 取值范围：最大长度1024字节。 约束：弹性公网IP的id个数不能超过20个 

        :return: The public_ip_address of this UpdateNatGatewaySnatRuleOption.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this UpdateNatGatewaySnatRuleOption.

        功能说明：弹性公网IP，多个弹性公网IP使用逗号分隔。 取值范围：最大长度1024字节。 约束：弹性公网IP的id个数不能超过20个 

        :param public_ip_address: The public_ip_address of this UpdateNatGatewaySnatRuleOption.
        :type public_ip_address: str
        """
        self._public_ip_address = public_ip_address

    @property
    def description(self):
        """Gets the description of this UpdateNatGatewaySnatRuleOption.

        SNAT规则的描述，长度限制为255。

        :return: The description of this UpdateNatGatewaySnatRuleOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateNatGatewaySnatRuleOption.

        SNAT规则的描述，长度限制为255。

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
