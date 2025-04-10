# coding: utf-8

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
        'floating_ip_address': 'list[str]',
        'floating_ip_id': 'list[str]',
        'id': 'str',
        'description': 'str',
        'created_at': 'str',
        'nat_gateway_id': 'list[str]',
        'network_id': 'str',
        'source_type': 'int',
        'status': 'str',
        'marker': 'str'
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
        'status': 'status',
        'marker': 'marker'
    }

    def __init__(self, admin_state_up=None, cidr=None, limit=None, floating_ip_address=None, floating_ip_id=None, id=None, description=None, created_at=None, nat_gateway_id=None, network_id=None, source_type=None, status=None, marker=None):
        r"""ListNatGatewaySnatRulesRequest

        The model defined in huaweicloud sdk

        :param admin_state_up: 解冻/冻结状态。 取值范围： \&quot;true\&quot;：解冻 \&quot;false\&quot;：冻结
        :type admin_state_up: bool
        :param cidr: 可以是网段或者主机格式，与network_id参数二选一。 Source_type&#x3D;0时，cidr必须是vpc子网网段的子集(不能相等）; Source_type&#x3D;1时，cidr必须指定专线侧网段。
        :type cidr: str
        :param limit: 功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。
        :type limit: int
        :param floating_ip_address: 功能说明：弹性公网IP。
        :type floating_ip_address: list[str]
        :param floating_ip_id: 功能说明：弹性公网IP的id。
        :type floating_ip_id: list[str]
        :param id: SNAT规则的ID。
        :type id: str
        :param description: SNAT规则的描述，长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param created_at: SNAT规则的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。
        :type created_at: str
        :param nat_gateway_id: 公网NAT网关实例的ID。
        :type nat_gateway_id: list[str]
        :param network_id: 规则使用的网络id。与cidr参数二选一。
        :type network_id: str
        :param source_type: 0：VPC侧，可以指定network_id 或者cidr 1：专线侧，只能指定cidr 不输入默认为0（VPC）
        :type source_type: int
        :param status: SNAT规则的状态。 取值为： \&quot;ACTIVE\&quot;: 可用 \&quot;PENDING_CREATE\&quot;：创建中 \&quot;PENDING_UPDATE\&quot;：更新中 \&quot;PENDING_DELETE\&quot;：删除中 \&quot;EIP_FREEZED\&quot;：EIP冻结 \&quot;INACTIVE\&quot;：不可用
        :type status: str
        :param marker: 分页查询的起始资源ID，表示从指定资源的下一条记录开始查询。 - 若不传入marker和limit参数，查询结果返回第一页全部资源记录（默认2000条）。 - 若不传入marker参数，limit为10，查询结果返回第1~10条资源记录。 - 若marker为第10条记录的资源ID，limit为10，查询结果返回第11~20条资源记录。 - 若marker为第10条记录的资源ID，不传入limit参数，查询结果返回第11条及之后的资源记录（默认2000条）。
        :type marker: str
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
        self._marker = None
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
        if marker is not None:
            self.marker = marker

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this ListNatGatewaySnatRulesRequest.

        解冻/冻结状态。 取值范围： \"true\"：解冻 \"false\"：冻结

        :return: The admin_state_up of this ListNatGatewaySnatRulesRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this ListNatGatewaySnatRulesRequest.

        解冻/冻结状态。 取值范围： \"true\"：解冻 \"false\"：冻结

        :param admin_state_up: The admin_state_up of this ListNatGatewaySnatRulesRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def cidr(self):
        r"""Gets the cidr of this ListNatGatewaySnatRulesRequest.

        可以是网段或者主机格式，与network_id参数二选一。 Source_type=0时，cidr必须是vpc子网网段的子集(不能相等）; Source_type=1时，cidr必须指定专线侧网段。

        :return: The cidr of this ListNatGatewaySnatRulesRequest.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this ListNatGatewaySnatRulesRequest.

        可以是网段或者主机格式，与network_id参数二选一。 Source_type=0时，cidr必须是vpc子网网段的子集(不能相等）; Source_type=1时，cidr必须指定专线侧网段。

        :param cidr: The cidr of this ListNatGatewaySnatRulesRequest.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def limit(self):
        r"""Gets the limit of this ListNatGatewaySnatRulesRequest.

        功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。

        :return: The limit of this ListNatGatewaySnatRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNatGatewaySnatRulesRequest.

        功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。

        :param limit: The limit of this ListNatGatewaySnatRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def floating_ip_address(self):
        r"""Gets the floating_ip_address of this ListNatGatewaySnatRulesRequest.

        功能说明：弹性公网IP。

        :return: The floating_ip_address of this ListNatGatewaySnatRulesRequest.
        :rtype: list[str]
        """
        return self._floating_ip_address

    @floating_ip_address.setter
    def floating_ip_address(self, floating_ip_address):
        r"""Sets the floating_ip_address of this ListNatGatewaySnatRulesRequest.

        功能说明：弹性公网IP。

        :param floating_ip_address: The floating_ip_address of this ListNatGatewaySnatRulesRequest.
        :type floating_ip_address: list[str]
        """
        self._floating_ip_address = floating_ip_address

    @property
    def floating_ip_id(self):
        r"""Gets the floating_ip_id of this ListNatGatewaySnatRulesRequest.

        功能说明：弹性公网IP的id。

        :return: The floating_ip_id of this ListNatGatewaySnatRulesRequest.
        :rtype: list[str]
        """
        return self._floating_ip_id

    @floating_ip_id.setter
    def floating_ip_id(self, floating_ip_id):
        r"""Sets the floating_ip_id of this ListNatGatewaySnatRulesRequest.

        功能说明：弹性公网IP的id。

        :param floating_ip_id: The floating_ip_id of this ListNatGatewaySnatRulesRequest.
        :type floating_ip_id: list[str]
        """
        self._floating_ip_id = floating_ip_id

    @property
    def id(self):
        r"""Gets the id of this ListNatGatewaySnatRulesRequest.

        SNAT规则的ID。

        :return: The id of this ListNatGatewaySnatRulesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListNatGatewaySnatRulesRequest.

        SNAT规则的ID。

        :param id: The id of this ListNatGatewaySnatRulesRequest.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this ListNatGatewaySnatRulesRequest.

        SNAT规则的描述，长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this ListNatGatewaySnatRulesRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListNatGatewaySnatRulesRequest.

        SNAT规则的描述，长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this ListNatGatewaySnatRulesRequest.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this ListNatGatewaySnatRulesRequest.

        SNAT规则的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。

        :return: The created_at of this ListNatGatewaySnatRulesRequest.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ListNatGatewaySnatRulesRequest.

        SNAT规则的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。

        :param created_at: The created_at of this ListNatGatewaySnatRulesRequest.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def nat_gateway_id(self):
        r"""Gets the nat_gateway_id of this ListNatGatewaySnatRulesRequest.

        公网NAT网关实例的ID。

        :return: The nat_gateway_id of this ListNatGatewaySnatRulesRequest.
        :rtype: list[str]
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        r"""Sets the nat_gateway_id of this ListNatGatewaySnatRulesRequest.

        公网NAT网关实例的ID。

        :param nat_gateway_id: The nat_gateway_id of this ListNatGatewaySnatRulesRequest.
        :type nat_gateway_id: list[str]
        """
        self._nat_gateway_id = nat_gateway_id

    @property
    def network_id(self):
        r"""Gets the network_id of this ListNatGatewaySnatRulesRequest.

        规则使用的网络id。与cidr参数二选一。

        :return: The network_id of this ListNatGatewaySnatRulesRequest.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        r"""Sets the network_id of this ListNatGatewaySnatRulesRequest.

        规则使用的网络id。与cidr参数二选一。

        :param network_id: The network_id of this ListNatGatewaySnatRulesRequest.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def source_type(self):
        r"""Gets the source_type of this ListNatGatewaySnatRulesRequest.

        0：VPC侧，可以指定network_id 或者cidr 1：专线侧，只能指定cidr 不输入默认为0（VPC）

        :return: The source_type of this ListNatGatewaySnatRulesRequest.
        :rtype: int
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this ListNatGatewaySnatRulesRequest.

        0：VPC侧，可以指定network_id 或者cidr 1：专线侧，只能指定cidr 不输入默认为0（VPC）

        :param source_type: The source_type of this ListNatGatewaySnatRulesRequest.
        :type source_type: int
        """
        self._source_type = source_type

    @property
    def status(self):
        r"""Gets the status of this ListNatGatewaySnatRulesRequest.

        SNAT规则的状态。 取值为： \"ACTIVE\": 可用 \"PENDING_CREATE\"：创建中 \"PENDING_UPDATE\"：更新中 \"PENDING_DELETE\"：删除中 \"EIP_FREEZED\"：EIP冻结 \"INACTIVE\"：不可用

        :return: The status of this ListNatGatewaySnatRulesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListNatGatewaySnatRulesRequest.

        SNAT规则的状态。 取值为： \"ACTIVE\": 可用 \"PENDING_CREATE\"：创建中 \"PENDING_UPDATE\"：更新中 \"PENDING_DELETE\"：删除中 \"EIP_FREEZED\"：EIP冻结 \"INACTIVE\"：不可用

        :param status: The status of this ListNatGatewaySnatRulesRequest.
        :type status: str
        """
        self._status = status

    @property
    def marker(self):
        r"""Gets the marker of this ListNatGatewaySnatRulesRequest.

        分页查询的起始资源ID，表示从指定资源的下一条记录开始查询。 - 若不传入marker和limit参数，查询结果返回第一页全部资源记录（默认2000条）。 - 若不传入marker参数，limit为10，查询结果返回第1~10条资源记录。 - 若marker为第10条记录的资源ID，limit为10，查询结果返回第11~20条资源记录。 - 若marker为第10条记录的资源ID，不传入limit参数，查询结果返回第11条及之后的资源记录（默认2000条）。

        :return: The marker of this ListNatGatewaySnatRulesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListNatGatewaySnatRulesRequest.

        分页查询的起始资源ID，表示从指定资源的下一条记录开始查询。 - 若不传入marker和limit参数，查询结果返回第一页全部资源记录（默认2000条）。 - 若不传入marker参数，limit为10，查询结果返回第1~10条资源记录。 - 若marker为第10条记录的资源ID，limit为10，查询结果返回第11~20条资源记录。 - 若marker为第10条记录的资源ID，不传入limit参数，查询结果返回第11条及之后的资源记录（默认2000条）。

        :param marker: The marker of this ListNatGatewaySnatRulesRequest.
        :type marker: str
        """
        self._marker = marker

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
