# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNatGatewaysRequest:

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
        'enterprise_project_id': 'str',
        'description': 'str',
        'created_at': 'str',
        'name': 'str',
        'status': 'list[str]',
        'spec': 'list[str]',
        'admin_state_up': 'bool',
        'internal_network_id': 'str',
        'router_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'id': 'id',
        'enterprise_project_id': 'enterprise_project_id',
        'description': 'description',
        'created_at': 'created_at',
        'name': 'name',
        'status': 'status',
        'spec': 'spec',
        'admin_state_up': 'admin_state_up',
        'internal_network_id': 'internal_network_id',
        'router_id': 'router_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, id=None, enterprise_project_id=None, description=None, created_at=None, name=None, status=None, spec=None, admin_state_up=None, internal_network_id=None, router_id=None, limit=None, marker=None):
        r"""ListNatGatewaysRequest

        The model defined in huaweicloud sdk

        :param id: 公网NAT网关实例的ID。
        :type id: str
        :param enterprise_project_id: 企业项目ID。创建公网NAT网关实例时，关联的企业项目ID。
        :type enterprise_project_id: str
        :param description: 公网NAT网关实例的描述，长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param created_at: 公网NAT网关实例的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。
        :type created_at: str
        :param name: 公网NAT网关实例的名字，长度限制为64。 公网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文
        :type name: str
        :param status: 公网NAT网关实例的状态。 取值为： \&quot;ACTIVE\&quot;: 可用 \&quot;PENDING_CREATE\&quot;：创建中 \&quot;PENDING_UPDATE\&quot;：更新中 \&quot;PENDING_DELETE\&quot;：删除中 \&quot;INACTIVE\&quot;：不可用
        :type status: list[str]
        :param spec: 公网NAT网关实例的规格。 取值为： \&quot;1\&quot;：小型，SNAT最大连接数10000 \&quot;2\&quot;：中型，SNAT最大连接数50000 \&quot;3\&quot;：大型，SNAT最大连接数200000 \&quot;4\&quot;：超大型，SNAT最大连接数1000000 
        :type spec: list[str]
        :param admin_state_up: 解冻/冻结状态。 取值范围： \&quot;true\&quot;：解冻 \&quot;false\&quot;：冻结
        :type admin_state_up: bool
        :param internal_network_id: 公网NAT网关下行口（DVR的下一跳）所属的network id。
        :type internal_network_id: str
        :param router_id: VPC的id。
        :type router_id: str
        :param limit: 功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。
        :type limit: int
        :param marker: 分页查询的起始资源ID，表示从指定资源的下一条记录开始查询。 - 若不传入marker和limit参数，查询结果返回第一页全部资源记录（默认2000条）。 - 若不传入marker参数，limit为10，查询结果返回第1~10条资源记录。 - 若marker为第10条记录的资源ID，limit为10，查询结果返回第11~20条资源记录。 - 若marker为第10条记录的资源ID，不传入limit参数，查询结果返回第11条及之后的资源记录（默认2000条）。
        :type marker: str
        """
        
        

        self._id = None
        self._enterprise_project_id = None
        self._description = None
        self._created_at = None
        self._name = None
        self._status = None
        self._spec = None
        self._admin_state_up = None
        self._internal_network_id = None
        self._router_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if spec is not None:
            self.spec = spec
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if internal_network_id is not None:
            self.internal_network_id = internal_network_id
        if router_id is not None:
            self.router_id = router_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def id(self):
        r"""Gets the id of this ListNatGatewaysRequest.

        公网NAT网关实例的ID。

        :return: The id of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListNatGatewaysRequest.

        公网NAT网关实例的ID。

        :param id: The id of this ListNatGatewaysRequest.
        :type id: str
        """
        self._id = id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListNatGatewaysRequest.

        企业项目ID。创建公网NAT网关实例时，关联的企业项目ID。

        :return: The enterprise_project_id of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListNatGatewaysRequest.

        企业项目ID。创建公网NAT网关实例时，关联的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListNatGatewaysRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def description(self):
        r"""Gets the description of this ListNatGatewaysRequest.

        公网NAT网关实例的描述，长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListNatGatewaysRequest.

        公网NAT网关实例的描述，长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this ListNatGatewaysRequest.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this ListNatGatewaysRequest.

        公网NAT网关实例的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。

        :return: The created_at of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ListNatGatewaysRequest.

        公网NAT网关实例的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。

        :param created_at: The created_at of this ListNatGatewaysRequest.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def name(self):
        r"""Gets the name of this ListNatGatewaysRequest.

        公网NAT网关实例的名字，长度限制为64。 公网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文

        :return: The name of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListNatGatewaysRequest.

        公网NAT网关实例的名字，长度限制为64。 公网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文

        :param name: The name of this ListNatGatewaysRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListNatGatewaysRequest.

        公网NAT网关实例的状态。 取值为： \"ACTIVE\": 可用 \"PENDING_CREATE\"：创建中 \"PENDING_UPDATE\"：更新中 \"PENDING_DELETE\"：删除中 \"INACTIVE\"：不可用

        :return: The status of this ListNatGatewaysRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListNatGatewaysRequest.

        公网NAT网关实例的状态。 取值为： \"ACTIVE\": 可用 \"PENDING_CREATE\"：创建中 \"PENDING_UPDATE\"：更新中 \"PENDING_DELETE\"：删除中 \"INACTIVE\"：不可用

        :param status: The status of this ListNatGatewaysRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def spec(self):
        r"""Gets the spec of this ListNatGatewaysRequest.

        公网NAT网关实例的规格。 取值为： \"1\"：小型，SNAT最大连接数10000 \"2\"：中型，SNAT最大连接数50000 \"3\"：大型，SNAT最大连接数200000 \"4\"：超大型，SNAT最大连接数1000000 

        :return: The spec of this ListNatGatewaysRequest.
        :rtype: list[str]
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this ListNatGatewaysRequest.

        公网NAT网关实例的规格。 取值为： \"1\"：小型，SNAT最大连接数10000 \"2\"：中型，SNAT最大连接数50000 \"3\"：大型，SNAT最大连接数200000 \"4\"：超大型，SNAT最大连接数1000000 

        :param spec: The spec of this ListNatGatewaysRequest.
        :type spec: list[str]
        """
        self._spec = spec

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this ListNatGatewaysRequest.

        解冻/冻结状态。 取值范围： \"true\"：解冻 \"false\"：冻结

        :return: The admin_state_up of this ListNatGatewaysRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this ListNatGatewaysRequest.

        解冻/冻结状态。 取值范围： \"true\"：解冻 \"false\"：冻结

        :param admin_state_up: The admin_state_up of this ListNatGatewaysRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def internal_network_id(self):
        r"""Gets the internal_network_id of this ListNatGatewaysRequest.

        公网NAT网关下行口（DVR的下一跳）所属的network id。

        :return: The internal_network_id of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._internal_network_id

    @internal_network_id.setter
    def internal_network_id(self, internal_network_id):
        r"""Sets the internal_network_id of this ListNatGatewaysRequest.

        公网NAT网关下行口（DVR的下一跳）所属的network id。

        :param internal_network_id: The internal_network_id of this ListNatGatewaysRequest.
        :type internal_network_id: str
        """
        self._internal_network_id = internal_network_id

    @property
    def router_id(self):
        r"""Gets the router_id of this ListNatGatewaysRequest.

        VPC的id。

        :return: The router_id of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        r"""Sets the router_id of this ListNatGatewaysRequest.

        VPC的id。

        :param router_id: The router_id of this ListNatGatewaysRequest.
        :type router_id: str
        """
        self._router_id = router_id

    @property
    def limit(self):
        r"""Gets the limit of this ListNatGatewaysRequest.

        功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。

        :return: The limit of this ListNatGatewaysRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNatGatewaysRequest.

        功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。

        :param limit: The limit of this ListNatGatewaysRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListNatGatewaysRequest.

        分页查询的起始资源ID，表示从指定资源的下一条记录开始查询。 - 若不传入marker和limit参数，查询结果返回第一页全部资源记录（默认2000条）。 - 若不传入marker参数，limit为10，查询结果返回第1~10条资源记录。 - 若marker为第10条记录的资源ID，limit为10，查询结果返回第11~20条资源记录。 - 若marker为第10条记录的资源ID，不传入limit参数，查询结果返回第11条及之后的资源记录（默认2000条）。

        :return: The marker of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListNatGatewaysRequest.

        分页查询的起始资源ID，表示从指定资源的下一条记录开始查询。 - 若不传入marker和limit参数，查询结果返回第一页全部资源记录（默认2000条）。 - 若不传入marker参数，limit为10，查询结果返回第1~10条资源记录。 - 若marker为第10条记录的资源ID，limit为10，查询结果返回第11~20条资源记录。 - 若marker为第10条记录的资源ID，不传入limit参数，查询结果返回第11条及之后的资源记录（默认2000条）。

        :param marker: The marker of this ListNatGatewaysRequest.
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
        if not isinstance(other, ListNatGatewaysRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
