# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNatGatewaySnatRuleOption:

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
        'cidr': 'str',
        'network_id': 'str',
        'description': 'str',
        'source_type': 'int',
        'floating_ip_id': 'str'
    }

    attribute_map = {
        'nat_gateway_id': 'nat_gateway_id',
        'cidr': 'cidr',
        'network_id': 'network_id',
        'description': 'description',
        'source_type': 'source_type',
        'floating_ip_id': 'floating_ip_id'
    }

    def __init__(self, nat_gateway_id=None, cidr=None, network_id=None, description=None, source_type=None, floating_ip_id=None):
        """CreateNatGatewaySnatRuleOption

        The model defined in huaweicloud sdk

        :param nat_gateway_id: 公网NAT网关实例的ID。
        :type nat_gateway_id: str
        :param cidr: cidr，可以是网段或者主机格式，与network_id参数二选一。 Source_type&#x3D;0时，cidr必须是vpc 子网网段的子集(不能相等）; Source_type&#x3D;1时，cidr必须指定专线侧网段。 
        :type cidr: str
        :param network_id: 规则使用的网络id。与cidr参数二选一。
        :type network_id: str
        :param description: SNAT规则的描述，长度限制为255。
        :type description: str
        :param source_type: 0：VPC侧，可以指定network_id 或者cidr 1：专线侧，只能指定cidr 不输入默认为0（VPC） 
        :type source_type: int
        :param floating_ip_id: 功能说明：弹性公网IP的id，多个弹性公网IP使用逗号分隔。 取值范围：最大长度4096字节。 约束：弹性公网IP的id个数不能超过20个。 
        :type floating_ip_id: str
        """
        
        

        self._nat_gateway_id = None
        self._cidr = None
        self._network_id = None
        self._description = None
        self._source_type = None
        self._floating_ip_id = None
        self.discriminator = None

        self.nat_gateway_id = nat_gateway_id
        if cidr is not None:
            self.cidr = cidr
        if network_id is not None:
            self.network_id = network_id
        if description is not None:
            self.description = description
        if source_type is not None:
            self.source_type = source_type
        self.floating_ip_id = floating_ip_id

    @property
    def nat_gateway_id(self):
        """Gets the nat_gateway_id of this CreateNatGatewaySnatRuleOption.

        公网NAT网关实例的ID。

        :return: The nat_gateway_id of this CreateNatGatewaySnatRuleOption.
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        """Sets the nat_gateway_id of this CreateNatGatewaySnatRuleOption.

        公网NAT网关实例的ID。

        :param nat_gateway_id: The nat_gateway_id of this CreateNatGatewaySnatRuleOption.
        :type nat_gateway_id: str
        """
        self._nat_gateway_id = nat_gateway_id

    @property
    def cidr(self):
        """Gets the cidr of this CreateNatGatewaySnatRuleOption.

        cidr，可以是网段或者主机格式，与network_id参数二选一。 Source_type=0时，cidr必须是vpc 子网网段的子集(不能相等）; Source_type=1时，cidr必须指定专线侧网段。 

        :return: The cidr of this CreateNatGatewaySnatRuleOption.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this CreateNatGatewaySnatRuleOption.

        cidr，可以是网段或者主机格式，与network_id参数二选一。 Source_type=0时，cidr必须是vpc 子网网段的子集(不能相等）; Source_type=1时，cidr必须指定专线侧网段。 

        :param cidr: The cidr of this CreateNatGatewaySnatRuleOption.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def network_id(self):
        """Gets the network_id of this CreateNatGatewaySnatRuleOption.

        规则使用的网络id。与cidr参数二选一。

        :return: The network_id of this CreateNatGatewaySnatRuleOption.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this CreateNatGatewaySnatRuleOption.

        规则使用的网络id。与cidr参数二选一。

        :param network_id: The network_id of this CreateNatGatewaySnatRuleOption.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def description(self):
        """Gets the description of this CreateNatGatewaySnatRuleOption.

        SNAT规则的描述，长度限制为255。

        :return: The description of this CreateNatGatewaySnatRuleOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateNatGatewaySnatRuleOption.

        SNAT规则的描述，长度限制为255。

        :param description: The description of this CreateNatGatewaySnatRuleOption.
        :type description: str
        """
        self._description = description

    @property
    def source_type(self):
        """Gets the source_type of this CreateNatGatewaySnatRuleOption.

        0：VPC侧，可以指定network_id 或者cidr 1：专线侧，只能指定cidr 不输入默认为0（VPC） 

        :return: The source_type of this CreateNatGatewaySnatRuleOption.
        :rtype: int
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this CreateNatGatewaySnatRuleOption.

        0：VPC侧，可以指定network_id 或者cidr 1：专线侧，只能指定cidr 不输入默认为0（VPC） 

        :param source_type: The source_type of this CreateNatGatewaySnatRuleOption.
        :type source_type: int
        """
        self._source_type = source_type

    @property
    def floating_ip_id(self):
        """Gets the floating_ip_id of this CreateNatGatewaySnatRuleOption.

        功能说明：弹性公网IP的id，多个弹性公网IP使用逗号分隔。 取值范围：最大长度4096字节。 约束：弹性公网IP的id个数不能超过20个。 

        :return: The floating_ip_id of this CreateNatGatewaySnatRuleOption.
        :rtype: str
        """
        return self._floating_ip_id

    @floating_ip_id.setter
    def floating_ip_id(self, floating_ip_id):
        """Sets the floating_ip_id of this CreateNatGatewaySnatRuleOption.

        功能说明：弹性公网IP的id，多个弹性公网IP使用逗号分隔。 取值范围：最大长度4096字节。 约束：弹性公网IP的id个数不能超过20个。 

        :param floating_ip_id: The floating_ip_id of this CreateNatGatewaySnatRuleOption.
        :type floating_ip_id: str
        """
        self._floating_ip_id = floating_ip_id

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
        if not isinstance(other, CreateNatGatewaySnatRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
