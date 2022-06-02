# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NatGatewayResponseBody:

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
        'admin_state_up': 'bool',
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
        """NatGatewayResponseBody

        The model defined in huaweicloud sdk

        :param id: 公网NAT网关实例的ID。
        :type id: str
        :param tenant_id: 项目的ID。
        :type tenant_id: str
        :param name: 公网NAT网关实例的名字，长度限制为64。
        :type name: str
        :param description: 公网NAT网关实例的描述，长度限制为255。
        :type description: str
        :param spec: 公网NAT网关的规格。 取值为： “1”：小型，SNAT最大连接数10000 “2”：中型，SNAT最大连接数50000 “3”：大型，SNAT最大连接数200000 “4”：超大型，SNAT最大连接数1000000 
        :type spec: str
        :param status: 公网NAT网关实例的状态。
        :type status: str
        :param admin_state_up: 解冻/冻结状态。 取值范围： - \&quot;true\&quot;：解冻 - \&quot;false\&quot;：冻结
        :type admin_state_up: bool
        :param created_at: 公网NAT网关实例的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。
        :type created_at: str
        :param router_id: VPC的id。
        :type router_id: str
        :param internal_network_id: 公网NAT网关下行口（DVR的下一跳）所属的network id。
        :type internal_network_id: str
        :param enterprise_project_id: 企业项目ID。 创建公网NAT网关实例时，关联的企业项目ID。
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

        self.id = id
        self.tenant_id = tenant_id
        self.name = name
        self.description = description
        self.spec = spec
        self.status = status
        self.admin_state_up = admin_state_up
        self.created_at = created_at
        self.router_id = router_id
        self.internal_network_id = internal_network_id
        self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this NatGatewayResponseBody.

        公网NAT网关实例的ID。

        :return: The id of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NatGatewayResponseBody.

        公网NAT网关实例的ID。

        :param id: The id of this NatGatewayResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NatGatewayResponseBody.

        项目的ID。

        :return: The tenant_id of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NatGatewayResponseBody.

        项目的ID。

        :param tenant_id: The tenant_id of this NatGatewayResponseBody.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this NatGatewayResponseBody.

        公网NAT网关实例的名字，长度限制为64。

        :return: The name of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NatGatewayResponseBody.

        公网NAT网关实例的名字，长度限制为64。

        :param name: The name of this NatGatewayResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this NatGatewayResponseBody.

        公网NAT网关实例的描述，长度限制为255。

        :return: The description of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NatGatewayResponseBody.

        公网NAT网关实例的描述，长度限制为255。

        :param description: The description of this NatGatewayResponseBody.
        :type description: str
        """
        self._description = description

    @property
    def spec(self):
        """Gets the spec of this NatGatewayResponseBody.

        公网NAT网关的规格。 取值为： “1”：小型，SNAT最大连接数10000 “2”：中型，SNAT最大连接数50000 “3”：大型，SNAT最大连接数200000 “4”：超大型，SNAT最大连接数1000000 

        :return: The spec of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this NatGatewayResponseBody.

        公网NAT网关的规格。 取值为： “1”：小型，SNAT最大连接数10000 “2”：中型，SNAT最大连接数50000 “3”：大型，SNAT最大连接数200000 “4”：超大型，SNAT最大连接数1000000 

        :param spec: The spec of this NatGatewayResponseBody.
        :type spec: str
        """
        self._spec = spec

    @property
    def status(self):
        """Gets the status of this NatGatewayResponseBody.

        公网NAT网关实例的状态。

        :return: The status of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NatGatewayResponseBody.

        公网NAT网关实例的状态。

        :param status: The status of this NatGatewayResponseBody.
        :type status: str
        """
        self._status = status

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this NatGatewayResponseBody.

        解冻/冻结状态。 取值范围： - \"true\"：解冻 - \"false\"：冻结

        :return: The admin_state_up of this NatGatewayResponseBody.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this NatGatewayResponseBody.

        解冻/冻结状态。 取值范围： - \"true\"：解冻 - \"false\"：冻结

        :param admin_state_up: The admin_state_up of this NatGatewayResponseBody.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def created_at(self):
        """Gets the created_at of this NatGatewayResponseBody.

        公网NAT网关实例的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。

        :return: The created_at of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NatGatewayResponseBody.

        公网NAT网关实例的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。

        :param created_at: The created_at of this NatGatewayResponseBody.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def router_id(self):
        """Gets the router_id of this NatGatewayResponseBody.

        VPC的id。

        :return: The router_id of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        """Sets the router_id of this NatGatewayResponseBody.

        VPC的id。

        :param router_id: The router_id of this NatGatewayResponseBody.
        :type router_id: str
        """
        self._router_id = router_id

    @property
    def internal_network_id(self):
        """Gets the internal_network_id of this NatGatewayResponseBody.

        公网NAT网关下行口（DVR的下一跳）所属的network id。

        :return: The internal_network_id of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._internal_network_id

    @internal_network_id.setter
    def internal_network_id(self, internal_network_id):
        """Sets the internal_network_id of this NatGatewayResponseBody.

        公网NAT网关下行口（DVR的下一跳）所属的network id。

        :param internal_network_id: The internal_network_id of this NatGatewayResponseBody.
        :type internal_network_id: str
        """
        self._internal_network_id = internal_network_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this NatGatewayResponseBody.

        企业项目ID。 创建公网NAT网关实例时，关联的企业项目ID。

        :return: The enterprise_project_id of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this NatGatewayResponseBody.

        企业项目ID。 创建公网NAT网关实例时，关联的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this NatGatewayResponseBody.
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
        if not isinstance(other, NatGatewayResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
