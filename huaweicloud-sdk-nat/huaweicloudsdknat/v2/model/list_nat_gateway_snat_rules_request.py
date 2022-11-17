# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNatGatewaySnatRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'cidr': 'str',
        'limit': 'int',
        'floating_ip_address': 'str',
        'floating_ip_id': 'str',
        'id': 'str',
        'description': 'str',
        'created_at': 'str',
        'nat_gateway_id': 'list[str]',
        'network_id': 'str',
        'source_type': 'int',
        'status': 'str'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'cidr': 'cidr',
        'limit': 'limit',
        'floating_ip_address': 'floating_ip_address',
        'floating_ip_id': 'floating_ip_id',
        'id': 'id',
        'description': 'description',
        'created_at': 'created_at',
        'nat_gateway_id': 'nat_gateway_id',
        'network_id': 'network_id',
        'source_type': 'source_type',
        'status': 'status'
    }

    def __init__(self, admin_state_up=None, cidr=None, limit=None, floating_ip_address=None, floating_ip_id=None, id=None, description=None, created_at=None, nat_gateway_id=None, network_id=None, source_type=None, status=None):
        """ListNatGatewaySnatRulesRequest

        The model defined in huaweicloud sdk

        :param admin_state_up: 解冻/冻结状态。 取值范围： \&quot;true\&quot;：解冻 \&quot;false\&quot;：冻结
        :type admin_state_up: bool
        :param cidr: 可以是网段或者主机格式，与network_id参数二选一。 Source_type&#x3D;0时，cidr必须是vpc子网网段的子集(不能相等）; Source_type&#x3D;1时，cidr必须指定专线侧网段。
        :type cidr: str
        :param limit: 功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。
        :type limit: int
        :param floating_ip_address: 功能说明：弹性公网IP，多个弹性公网IP使用逗号分隔。 取值范围：最大长度1024字节。
        :type floating_ip_address: str
        :param floating_ip_id: 功能说明：弹性公网IP的id，多个弹性公网IP使用逗号分隔。 取值范围：最大长度4096字节。
        :type floating_ip_id: str
        :param id: SNAT规则的ID。
        :type id: str
        :param description: SNAT规则的描述，长度限制为255。
        :type description: str
        :param created_at: SNAT规则的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。
        :type created_at: str
        :param nat_gateway_id: 公网NAT网关实例的ID。
        :type nat_gateway_id: list[str]
        :param network_id: 规则使用的网络id。与cidr参数二选一。
        :type network_id: str
        :param source_type: 0：VPC侧，可以指定network_id 或者cidr 1：专线侧，只能指定cidr 不输入默认为0（VPC）
        :type source_type: int
        :param status: 功能说明：SNAT规则的状态。
        :type status: str
        """
        
        

        self._admin_state_up = None
        self._cidr = None
        self._limit = None
        self._floating_ip_address = None
        self._floating_ip_id = None
        self._id = None
        self._description = None
        self._created_at = None
        self._nat_gateway_id = None
        self._network_id = None
        self._source_type = None
        self._status = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if cidr is not None:
            self.cidr = cidr
        if limit is not None:
            self.limit = limit
        if floating_ip_address is not None:
            self.floating_ip_address = floating_ip_address
        if floating_ip_id is not None:
            self.floating_ip_id = floating_ip_id
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if nat_gateway_id is not None:
            self.nat_gateway_id = nat_gateway_id
        if network_id is not None:
            self.network_id = network_id
        if source_type is not None:
            self.source_type = source_type
        if status is not None:
            self.status = status

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListNatGatewaySnatRulesRequest.

        解冻/冻结状态。 取值范围： \"true\"：解冻 \"false\"：冻结

        :return: The admin_state_up of this ListNatGatewaySnatRulesRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListNatGatewaySnatRulesRequest.

        解冻/冻结状态。 取值范围： \"true\"：解冻 \"false\"：冻结

        :param admin_state_up: The admin_state_up of this ListNatGatewaySnatRulesRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def cidr(self):
        """Gets the cidr of this ListNatGatewaySnatRulesRequest.

        可以是网段或者主机格式，与network_id参数二选一。 Source_type=0时，cidr必须是vpc子网网段的子集(不能相等）; Source_type=1时，cidr必须指定专线侧网段。

        :return: The cidr of this ListNatGatewaySnatRulesRequest.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this ListNatGatewaySnatRulesRequest.

        可以是网段或者主机格式，与network_id参数二选一。 Source_type=0时，cidr必须是vpc子网网段的子集(不能相等）; Source_type=1时，cidr必须指定专线侧网段。

        :param cidr: The cidr of this ListNatGatewaySnatRulesRequest.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def limit(self):
        """Gets the limit of this ListNatGatewaySnatRulesRequest.

        功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。

        :return: The limit of this ListNatGatewaySnatRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListNatGatewaySnatRulesRequest.

        功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。

        :param limit: The limit of this ListNatGatewaySnatRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def floating_ip_address(self):
        """Gets the floating_ip_address of this ListNatGatewaySnatRulesRequest.

        功能说明：弹性公网IP，多个弹性公网IP使用逗号分隔。 取值范围：最大长度1024字节。

        :return: The floating_ip_address of this ListNatGatewaySnatRulesRequest.
        :rtype: str
        """
        return self._floating_ip_address

    @floating_ip_address.setter
    def floating_ip_address(self, floating_ip_address):
        """Sets the floating_ip_address of this ListNatGatewaySnatRulesRequest.

        功能说明：弹性公网IP，多个弹性公网IP使用逗号分隔。 取值范围：最大长度1024字节。

        :param floating_ip_address: The floating_ip_address of this ListNatGatewaySnatRulesRequest.
        :type floating_ip_address: str
        """
        self._floating_ip_address = floating_ip_address

    @property
    def floating_ip_id(self):
        """Gets the floating_ip_id of this ListNatGatewaySnatRulesRequest.

        功能说明：弹性公网IP的id，多个弹性公网IP使用逗号分隔。 取值范围：最大长度4096字节。

        :return: The floating_ip_id of this ListNatGatewaySnatRulesRequest.
        :rtype: str
        """
        return self._floating_ip_id

    @floating_ip_id.setter
    def floating_ip_id(self, floating_ip_id):
        """Sets the floating_ip_id of this ListNatGatewaySnatRulesRequest.

        功能说明：弹性公网IP的id，多个弹性公网IP使用逗号分隔。 取值范围：最大长度4096字节。

        :param floating_ip_id: The floating_ip_id of this ListNatGatewaySnatRulesRequest.
        :type floating_ip_id: str
        """
        self._floating_ip_id = floating_ip_id

    @property
    def id(self):
        """Gets the id of this ListNatGatewaySnatRulesRequest.

        SNAT规则的ID。

        :return: The id of this ListNatGatewaySnatRulesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListNatGatewaySnatRulesRequest.

        SNAT规则的ID。

        :param id: The id of this ListNatGatewaySnatRulesRequest.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        """Gets the description of this ListNatGatewaySnatRulesRequest.

        SNAT规则的描述，长度限制为255。

        :return: The description of this ListNatGatewaySnatRulesRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListNatGatewaySnatRulesRequest.

        SNAT规则的描述，长度限制为255。

        :param description: The description of this ListNatGatewaySnatRulesRequest.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this ListNatGatewaySnatRulesRequest.

        SNAT规则的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。

        :return: The created_at of this ListNatGatewaySnatRulesRequest.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ListNatGatewaySnatRulesRequest.

        SNAT规则的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。

        :param created_at: The created_at of this ListNatGatewaySnatRulesRequest.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def nat_gateway_id(self):
        """Gets the nat_gateway_id of this ListNatGatewaySnatRulesRequest.

        公网NAT网关实例的ID。

        :return: The nat_gateway_id of this ListNatGatewaySnatRulesRequest.
        :rtype: list[str]
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        """Sets the nat_gateway_id of this ListNatGatewaySnatRulesRequest.

        公网NAT网关实例的ID。

        :param nat_gateway_id: The nat_gateway_id of this ListNatGatewaySnatRulesRequest.
        :type nat_gateway_id: list[str]
        """
        self._nat_gateway_id = nat_gateway_id

    @property
    def network_id(self):
        """Gets the network_id of this ListNatGatewaySnatRulesRequest.

        规则使用的网络id。与cidr参数二选一。

        :return: The network_id of this ListNatGatewaySnatRulesRequest.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this ListNatGatewaySnatRulesRequest.

        规则使用的网络id。与cidr参数二选一。

        :param network_id: The network_id of this ListNatGatewaySnatRulesRequest.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def source_type(self):
        """Gets the source_type of this ListNatGatewaySnatRulesRequest.

        0：VPC侧，可以指定network_id 或者cidr 1：专线侧，只能指定cidr 不输入默认为0（VPC）

        :return: The source_type of this ListNatGatewaySnatRulesRequest.
        :rtype: int
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this ListNatGatewaySnatRulesRequest.

        0：VPC侧，可以指定network_id 或者cidr 1：专线侧，只能指定cidr 不输入默认为0（VPC）

        :param source_type: The source_type of this ListNatGatewaySnatRulesRequest.
        :type source_type: int
        """
        self._source_type = source_type

    @property
    def status(self):
        """Gets the status of this ListNatGatewaySnatRulesRequest.

        功能说明：SNAT规则的状态。

        :return: The status of this ListNatGatewaySnatRulesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListNatGatewaySnatRulesRequest.

        功能说明：SNAT规则的状态。

        :param status: The status of this ListNatGatewaySnatRulesRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListNatGatewaySnatRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
