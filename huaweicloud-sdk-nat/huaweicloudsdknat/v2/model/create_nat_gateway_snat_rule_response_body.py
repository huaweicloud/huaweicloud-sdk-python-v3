# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNatGatewaySnatRuleResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'tenant_id': 'str',
        'nat_gateway_id': 'str',
        'cidr': 'str',
        'source_type': 'int',
        'floating_ip_id': 'str',
        'description': 'str',
        'status': 'str',
        'created_at': 'str',
        'network_id': 'str',
        'admin_state_up': 'bool',
        'floating_ip_address': 'str',
        'global_eip_id': 'str',
        'global_eip_address': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'nat_gateway_id': 'nat_gateway_id',
        'cidr': 'cidr',
        'source_type': 'source_type',
        'floating_ip_id': 'floating_ip_id',
        'description': 'description',
        'status': 'status',
        'created_at': 'created_at',
        'network_id': 'network_id',
        'admin_state_up': 'admin_state_up',
        'floating_ip_address': 'floating_ip_address',
        'global_eip_id': 'global_eip_id',
        'global_eip_address': 'global_eip_address'
    }

    def __init__(self, id=None, tenant_id=None, nat_gateway_id=None, cidr=None, source_type=None, floating_ip_id=None, description=None, status=None, created_at=None, network_id=None, admin_state_up=None, floating_ip_address=None, global_eip_id=None, global_eip_address=None):
        """CreateNatGatewaySnatRuleResponseBody

        The model defined in huaweicloud sdk

        :param id: SNAT规则的ID。
        :type id: str
        :param tenant_id: 项目的ID。
        :type tenant_id: str
        :param nat_gateway_id: 公网NAT网关实例的ID。
        :type nat_gateway_id: str
        :param cidr: cidr，可以是网段或者主机格式，与network_id参数二选一。 Source_type&#x3D;0时，cidr必须是vpc 子网网段的子集(不能相等）; Source_type&#x3D;1时，cidr必须指定专线侧网段。
        :type cidr: str
        :param source_type: 0：VPC侧，可以指定network_id 或者cidr 1：专线侧，只能指定cidr 不输入默认为0（VPC）
        :type source_type: int
        :param floating_ip_id: 功能说明：弹性公网IP的id，多个弹性公网IP使用逗号分隔。 取值范围：最大长度4096字节。
        :type floating_ip_id: str
        :param description: SNAT规则的描述，长度限制为255。
        :type description: str
        :param status: SNAT规则的状态。 取值为： \&quot;ACTIVE\&quot;: 可用 \&quot;PENDING_CREATE\&quot;：创建中 \&quot;PENDING_UPDATE\&quot;：更新中 \&quot;PENDING_DELETE\&quot;：删除中 \&quot;EIP_FREEZED\&quot;：EIP冻结 \&quot;INACTIVE\&quot;：不可用
        :type status: str
        :param created_at: SNAT规则的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。
        :type created_at: str
        :param network_id: 规则使用的网络id。与cidr参数二选一。
        :type network_id: str
        :param admin_state_up: 解冻/冻结状态。 取值范围： - \&quot;true\&quot;：解冻 - \&quot;false\&quot;：冻结
        :type admin_state_up: bool
        :param floating_ip_address: 功能说明：弹性公网IP，多个弹性公网IP使用逗号分隔。
        :type floating_ip_address: str
        :param global_eip_id: 全域弹性公网IP的id。
        :type global_eip_id: str
        :param global_eip_address: 全域弹性公网IP的地址。
        :type global_eip_address: str
        """
        
        

        self._id = None
        self._tenant_id = None
        self._nat_gateway_id = None
        self._cidr = None
        self._source_type = None
        self._floating_ip_id = None
        self._description = None
        self._status = None
        self._created_at = None
        self._network_id = None
        self._admin_state_up = None
        self._floating_ip_address = None
        self._global_eip_id = None
        self._global_eip_address = None
        self.discriminator = None

        self.id = id
        self.tenant_id = tenant_id
        self.nat_gateway_id = nat_gateway_id
        self.cidr = cidr
        self.source_type = source_type
        self.floating_ip_id = floating_ip_id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.network_id = network_id
        self.admin_state_up = admin_state_up
        self.floating_ip_address = floating_ip_address
        self.global_eip_id = global_eip_id
        self.global_eip_address = global_eip_address

    @property
    def id(self):
        """Gets the id of this CreateNatGatewaySnatRuleResponseBody.

        SNAT规则的ID。

        :return: The id of this CreateNatGatewaySnatRuleResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateNatGatewaySnatRuleResponseBody.

        SNAT规则的ID。

        :param id: The id of this CreateNatGatewaySnatRuleResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CreateNatGatewaySnatRuleResponseBody.

        项目的ID。

        :return: The tenant_id of this CreateNatGatewaySnatRuleResponseBody.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CreateNatGatewaySnatRuleResponseBody.

        项目的ID。

        :param tenant_id: The tenant_id of this CreateNatGatewaySnatRuleResponseBody.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def nat_gateway_id(self):
        """Gets the nat_gateway_id of this CreateNatGatewaySnatRuleResponseBody.

        公网NAT网关实例的ID。

        :return: The nat_gateway_id of this CreateNatGatewaySnatRuleResponseBody.
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        """Sets the nat_gateway_id of this CreateNatGatewaySnatRuleResponseBody.

        公网NAT网关实例的ID。

        :param nat_gateway_id: The nat_gateway_id of this CreateNatGatewaySnatRuleResponseBody.
        :type nat_gateway_id: str
        """
        self._nat_gateway_id = nat_gateway_id

    @property
    def cidr(self):
        """Gets the cidr of this CreateNatGatewaySnatRuleResponseBody.

        cidr，可以是网段或者主机格式，与network_id参数二选一。 Source_type=0时，cidr必须是vpc 子网网段的子集(不能相等）; Source_type=1时，cidr必须指定专线侧网段。

        :return: The cidr of this CreateNatGatewaySnatRuleResponseBody.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this CreateNatGatewaySnatRuleResponseBody.

        cidr，可以是网段或者主机格式，与network_id参数二选一。 Source_type=0时，cidr必须是vpc 子网网段的子集(不能相等）; Source_type=1时，cidr必须指定专线侧网段。

        :param cidr: The cidr of this CreateNatGatewaySnatRuleResponseBody.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def source_type(self):
        """Gets the source_type of this CreateNatGatewaySnatRuleResponseBody.

        0：VPC侧，可以指定network_id 或者cidr 1：专线侧，只能指定cidr 不输入默认为0（VPC）

        :return: The source_type of this CreateNatGatewaySnatRuleResponseBody.
        :rtype: int
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this CreateNatGatewaySnatRuleResponseBody.

        0：VPC侧，可以指定network_id 或者cidr 1：专线侧，只能指定cidr 不输入默认为0（VPC）

        :param source_type: The source_type of this CreateNatGatewaySnatRuleResponseBody.
        :type source_type: int
        """
        self._source_type = source_type

    @property
    def floating_ip_id(self):
        """Gets the floating_ip_id of this CreateNatGatewaySnatRuleResponseBody.

        功能说明：弹性公网IP的id，多个弹性公网IP使用逗号分隔。 取值范围：最大长度4096字节。

        :return: The floating_ip_id of this CreateNatGatewaySnatRuleResponseBody.
        :rtype: str
        """
        return self._floating_ip_id

    @floating_ip_id.setter
    def floating_ip_id(self, floating_ip_id):
        """Sets the floating_ip_id of this CreateNatGatewaySnatRuleResponseBody.

        功能说明：弹性公网IP的id，多个弹性公网IP使用逗号分隔。 取值范围：最大长度4096字节。

        :param floating_ip_id: The floating_ip_id of this CreateNatGatewaySnatRuleResponseBody.
        :type floating_ip_id: str
        """
        self._floating_ip_id = floating_ip_id

    @property
    def description(self):
        """Gets the description of this CreateNatGatewaySnatRuleResponseBody.

        SNAT规则的描述，长度限制为255。

        :return: The description of this CreateNatGatewaySnatRuleResponseBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateNatGatewaySnatRuleResponseBody.

        SNAT规则的描述，长度限制为255。

        :param description: The description of this CreateNatGatewaySnatRuleResponseBody.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this CreateNatGatewaySnatRuleResponseBody.

        SNAT规则的状态。 取值为： \"ACTIVE\": 可用 \"PENDING_CREATE\"：创建中 \"PENDING_UPDATE\"：更新中 \"PENDING_DELETE\"：删除中 \"EIP_FREEZED\"：EIP冻结 \"INACTIVE\"：不可用

        :return: The status of this CreateNatGatewaySnatRuleResponseBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateNatGatewaySnatRuleResponseBody.

        SNAT规则的状态。 取值为： \"ACTIVE\": 可用 \"PENDING_CREATE\"：创建中 \"PENDING_UPDATE\"：更新中 \"PENDING_DELETE\"：删除中 \"EIP_FREEZED\"：EIP冻结 \"INACTIVE\"：不可用

        :param status: The status of this CreateNatGatewaySnatRuleResponseBody.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this CreateNatGatewaySnatRuleResponseBody.

        SNAT规则的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。

        :return: The created_at of this CreateNatGatewaySnatRuleResponseBody.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateNatGatewaySnatRuleResponseBody.

        SNAT规则的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。

        :param created_at: The created_at of this CreateNatGatewaySnatRuleResponseBody.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def network_id(self):
        """Gets the network_id of this CreateNatGatewaySnatRuleResponseBody.

        规则使用的网络id。与cidr参数二选一。

        :return: The network_id of this CreateNatGatewaySnatRuleResponseBody.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this CreateNatGatewaySnatRuleResponseBody.

        规则使用的网络id。与cidr参数二选一。

        :param network_id: The network_id of this CreateNatGatewaySnatRuleResponseBody.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateNatGatewaySnatRuleResponseBody.

        解冻/冻结状态。 取值范围： - \"true\"：解冻 - \"false\"：冻结

        :return: The admin_state_up of this CreateNatGatewaySnatRuleResponseBody.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateNatGatewaySnatRuleResponseBody.

        解冻/冻结状态。 取值范围： - \"true\"：解冻 - \"false\"：冻结

        :param admin_state_up: The admin_state_up of this CreateNatGatewaySnatRuleResponseBody.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def floating_ip_address(self):
        """Gets the floating_ip_address of this CreateNatGatewaySnatRuleResponseBody.

        功能说明：弹性公网IP，多个弹性公网IP使用逗号分隔。

        :return: The floating_ip_address of this CreateNatGatewaySnatRuleResponseBody.
        :rtype: str
        """
        return self._floating_ip_address

    @floating_ip_address.setter
    def floating_ip_address(self, floating_ip_address):
        """Sets the floating_ip_address of this CreateNatGatewaySnatRuleResponseBody.

        功能说明：弹性公网IP，多个弹性公网IP使用逗号分隔。

        :param floating_ip_address: The floating_ip_address of this CreateNatGatewaySnatRuleResponseBody.
        :type floating_ip_address: str
        """
        self._floating_ip_address = floating_ip_address

    @property
    def global_eip_id(self):
        """Gets the global_eip_id of this CreateNatGatewaySnatRuleResponseBody.

        全域弹性公网IP的id。

        :return: The global_eip_id of this CreateNatGatewaySnatRuleResponseBody.
        :rtype: str
        """
        return self._global_eip_id

    @global_eip_id.setter
    def global_eip_id(self, global_eip_id):
        """Sets the global_eip_id of this CreateNatGatewaySnatRuleResponseBody.

        全域弹性公网IP的id。

        :param global_eip_id: The global_eip_id of this CreateNatGatewaySnatRuleResponseBody.
        :type global_eip_id: str
        """
        self._global_eip_id = global_eip_id

    @property
    def global_eip_address(self):
        """Gets the global_eip_address of this CreateNatGatewaySnatRuleResponseBody.

        全域弹性公网IP的地址。

        :return: The global_eip_address of this CreateNatGatewaySnatRuleResponseBody.
        :rtype: str
        """
        return self._global_eip_address

    @global_eip_address.setter
    def global_eip_address(self, global_eip_address):
        """Sets the global_eip_address of this CreateNatGatewaySnatRuleResponseBody.

        全域弹性公网IP的地址。

        :param global_eip_address: The global_eip_address of this CreateNatGatewaySnatRuleResponseBody.
        :type global_eip_address: str
        """
        self._global_eip_address = global_eip_address

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
        if not isinstance(other, CreateNatGatewaySnatRuleResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
