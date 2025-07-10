# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NatGateway:

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
        'name': 'str',
        'description': 'str',
        'spec': 'str',
        'status': 'str',
        'admin_state_up': 'str',
        'created_at': 'str',
        'router_id': 'str',
        'internal_network_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'name': 'name',
        'description': 'description',
        'spec': 'spec',
        'status': 'status',
        'admin_state_up': 'admin_state_up',
        'created_at': 'created_at',
        'router_id': 'router_id',
        'internal_network_id': 'internal_network_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, tenant_id=None, name=None, description=None, spec=None, status=None, admin_state_up=None, created_at=None, router_id=None, internal_network_id=None, enterprise_project_id=None):
        r"""NatGateway

        The model defined in huaweicloud sdk

        :param id: 网关实例的ID。
        :type id: str
        :param tenant_id: 项目的ID。
        :type tenant_id: str
        :param name: 公网NAT网关实例的名字，长度限制为64。
        :type name: str
        :param description: 公网NAT网关实例的描述，长度限制为255。
        :type description: str
        :param spec: 公网NAT网关的规格。取值为：“1”：小型，SNAT最大连接数10000；“2”：中型，SNAT最大连接数50000；“3”：大型，SNAT最大连接数200000；“4”：超大型，SNAT最大连接数1000000。
        :type spec: str
        :param status: 公网NAT网关实例的状态。 枚举值： ACTIVE PENDING_CREATE PENDING_UPDATE PENDING_DELETE INACTIVE
        :type status: str
        :param admin_state_up: 公网NAT网关实例的名字，长度限制为64。 解冻/冻结状态。取值范围： \&quot;true\&quot;：解冻 \&quot;false\&quot;：冻结
        :type admin_state_up: str
        :param created_at: 公网NAT网关实例的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。
        :type created_at: str
        :param router_id: VPC的id。
        :type router_id: str
        :param internal_network_id: 公网NAT网关下行口（DVR的下一跳）所属的network id。
        :type internal_network_id: str
        :param enterprise_project_id: 企业项目ID。创建公网NAT网关实例时，关联的企业项目ID。
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._tenant_id = None
        self._name = None
        self._description = None
        self._spec = None
        self._status = None
        self._admin_state_up = None
        self._created_at = None
        self._router_id = None
        self._internal_network_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if created_at is not None:
            self.created_at = created_at
        if router_id is not None:
            self.router_id = router_id
        if internal_network_id is not None:
            self.internal_network_id = internal_network_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this NatGateway.

        网关实例的ID。

        :return: The id of this NatGateway.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NatGateway.

        网关实例的ID。

        :param id: The id of this NatGateway.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this NatGateway.

        项目的ID。

        :return: The tenant_id of this NatGateway.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this NatGateway.

        项目的ID。

        :param tenant_id: The tenant_id of this NatGateway.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        r"""Gets the name of this NatGateway.

        公网NAT网关实例的名字，长度限制为64。

        :return: The name of this NatGateway.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NatGateway.

        公网NAT网关实例的名字，长度限制为64。

        :param name: The name of this NatGateway.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this NatGateway.

        公网NAT网关实例的描述，长度限制为255。

        :return: The description of this NatGateway.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this NatGateway.

        公网NAT网关实例的描述，长度限制为255。

        :param description: The description of this NatGateway.
        :type description: str
        """
        self._description = description

    @property
    def spec(self):
        r"""Gets the spec of this NatGateway.

        公网NAT网关的规格。取值为：“1”：小型，SNAT最大连接数10000；“2”：中型，SNAT最大连接数50000；“3”：大型，SNAT最大连接数200000；“4”：超大型，SNAT最大连接数1000000。

        :return: The spec of this NatGateway.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this NatGateway.

        公网NAT网关的规格。取值为：“1”：小型，SNAT最大连接数10000；“2”：中型，SNAT最大连接数50000；“3”：大型，SNAT最大连接数200000；“4”：超大型，SNAT最大连接数1000000。

        :param spec: The spec of this NatGateway.
        :type spec: str
        """
        self._spec = spec

    @property
    def status(self):
        r"""Gets the status of this NatGateway.

        公网NAT网关实例的状态。 枚举值： ACTIVE PENDING_CREATE PENDING_UPDATE PENDING_DELETE INACTIVE

        :return: The status of this NatGateway.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NatGateway.

        公网NAT网关实例的状态。 枚举值： ACTIVE PENDING_CREATE PENDING_UPDATE PENDING_DELETE INACTIVE

        :param status: The status of this NatGateway.
        :type status: str
        """
        self._status = status

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this NatGateway.

        公网NAT网关实例的名字，长度限制为64。 解冻/冻结状态。取值范围： \"true\"：解冻 \"false\"：冻结

        :return: The admin_state_up of this NatGateway.
        :rtype: str
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this NatGateway.

        公网NAT网关实例的名字，长度限制为64。 解冻/冻结状态。取值范围： \"true\"：解冻 \"false\"：冻结

        :param admin_state_up: The admin_state_up of this NatGateway.
        :type admin_state_up: str
        """
        self._admin_state_up = admin_state_up

    @property
    def created_at(self):
        r"""Gets the created_at of this NatGateway.

        公网NAT网关实例的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :return: The created_at of this NatGateway.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this NatGateway.

        公网NAT网关实例的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ。

        :param created_at: The created_at of this NatGateway.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def router_id(self):
        r"""Gets the router_id of this NatGateway.

        VPC的id。

        :return: The router_id of this NatGateway.
        :rtype: str
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        r"""Sets the router_id of this NatGateway.

        VPC的id。

        :param router_id: The router_id of this NatGateway.
        :type router_id: str
        """
        self._router_id = router_id

    @property
    def internal_network_id(self):
        r"""Gets the internal_network_id of this NatGateway.

        公网NAT网关下行口（DVR的下一跳）所属的network id。

        :return: The internal_network_id of this NatGateway.
        :rtype: str
        """
        return self._internal_network_id

    @internal_network_id.setter
    def internal_network_id(self, internal_network_id):
        r"""Sets the internal_network_id of this NatGateway.

        公网NAT网关下行口（DVR的下一跳）所属的network id。

        :param internal_network_id: The internal_network_id of this NatGateway.
        :type internal_network_id: str
        """
        self._internal_network_id = internal_network_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this NatGateway.

        企业项目ID。创建公网NAT网关实例时，关联的企业项目ID。

        :return: The enterprise_project_id of this NatGateway.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this NatGateway.

        企业项目ID。创建公网NAT网关实例时，关联的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this NatGateway.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, NatGateway):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
