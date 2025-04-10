# coding: utf-8

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
        'enterprise_project_id': 'str',
        'session_conf': 'SessionConfiguration',
        'ngport_ip_address': 'str',
        'billing_info': 'str',
        'dnat_rules_limit': 'int',
        'snat_rule_public_ip_limit': 'int'
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
        'enterprise_project_id': 'enterprise_project_id',
        'session_conf': 'session_conf',
        'ngport_ip_address': 'ngport_ip_address',
        'billing_info': 'billing_info',
        'dnat_rules_limit': 'dnat_rules_limit',
        'snat_rule_public_ip_limit': 'snat_rule_public_ip_limit'
    }

    def __init__(self, id=None, tenant_id=None, name=None, description=None, spec=None, status=None, admin_state_up=None, created_at=None, router_id=None, internal_network_id=None, enterprise_project_id=None, session_conf=None, ngport_ip_address=None, billing_info=None, dnat_rules_limit=None, snat_rule_public_ip_limit=None):
        r"""NatGatewayResponseBody

        The model defined in huaweicloud sdk

        :param id: 公网NAT网关实例的ID。
        :type id: str
        :param tenant_id: 项目的ID。
        :type tenant_id: str
        :param name: 公网NAT网关实例的名字，长度限制为64。
        :type name: str
        :param description: 公网NAT网关实例的描述，长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param spec: 公网NAT网关的规格。 取值为： “1”：小型，SNAT最大连接数10000 “2”：中型，SNAT最大连接数50000 “3”：大型，SNAT最大连接数200000 “4”：超大型，SNAT最大连接数1000000 
        :type spec: str
        :param status: 公网NAT网关实例的状态。 取值为： \&quot;ACTIVE\&quot;: 可用 \&quot;PENDING_CREATE\&quot;：创建中 \&quot;PENDING_UPDATE\&quot;：更新中 \&quot;PENDING_DELETE\&quot;：删除中 \&quot;INACTIVE\&quot;：不可用
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
        :param session_conf: 
        :type session_conf: :class:`huaweicloudsdknat.v2.SessionConfiguration`
        :param ngport_ip_address: 公网NAT网关私有IP地址，由VPC中子网分配。
        :type ngport_ip_address: str
        :param billing_info: 订单信息。此字段只有在订购包周期资源时才会有订单信息，而在订购按需资源时则为空。
        :type billing_info: str
        :param dnat_rules_limit: 公网NAT网关下DNAT规则数量限制，默认为200。
        :type dnat_rules_limit: int
        :param snat_rule_public_ip_limit: 公网NAT网关下SNAT规则EIP池中EIP数量限制，默认为20。
        :type snat_rule_public_ip_limit: int
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
        self._session_conf = None
        self._ngport_ip_address = None
        self._billing_info = None
        self._dnat_rules_limit = None
        self._snat_rule_public_ip_limit = None
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
        self.session_conf = session_conf
        self.ngport_ip_address = ngport_ip_address
        self.billing_info = billing_info
        self.dnat_rules_limit = dnat_rules_limit
        self.snat_rule_public_ip_limit = snat_rule_public_ip_limit

    @property
    def id(self):
        r"""Gets the id of this NatGatewayResponseBody.

        公网NAT网关实例的ID。

        :return: The id of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NatGatewayResponseBody.

        公网NAT网关实例的ID。

        :param id: The id of this NatGatewayResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this NatGatewayResponseBody.

        项目的ID。

        :return: The tenant_id of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this NatGatewayResponseBody.

        项目的ID。

        :param tenant_id: The tenant_id of this NatGatewayResponseBody.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        r"""Gets the name of this NatGatewayResponseBody.

        公网NAT网关实例的名字，长度限制为64。

        :return: The name of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NatGatewayResponseBody.

        公网NAT网关实例的名字，长度限制为64。

        :param name: The name of this NatGatewayResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this NatGatewayResponseBody.

        公网NAT网关实例的描述，长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this NatGatewayResponseBody.

        公网NAT网关实例的描述，长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this NatGatewayResponseBody.
        :type description: str
        """
        self._description = description

    @property
    def spec(self):
        r"""Gets the spec of this NatGatewayResponseBody.

        公网NAT网关的规格。 取值为： “1”：小型，SNAT最大连接数10000 “2”：中型，SNAT最大连接数50000 “3”：大型，SNAT最大连接数200000 “4”：超大型，SNAT最大连接数1000000 

        :return: The spec of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this NatGatewayResponseBody.

        公网NAT网关的规格。 取值为： “1”：小型，SNAT最大连接数10000 “2”：中型，SNAT最大连接数50000 “3”：大型，SNAT最大连接数200000 “4”：超大型，SNAT最大连接数1000000 

        :param spec: The spec of this NatGatewayResponseBody.
        :type spec: str
        """
        self._spec = spec

    @property
    def status(self):
        r"""Gets the status of this NatGatewayResponseBody.

        公网NAT网关实例的状态。 取值为： \"ACTIVE\": 可用 \"PENDING_CREATE\"：创建中 \"PENDING_UPDATE\"：更新中 \"PENDING_DELETE\"：删除中 \"INACTIVE\"：不可用

        :return: The status of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NatGatewayResponseBody.

        公网NAT网关实例的状态。 取值为： \"ACTIVE\": 可用 \"PENDING_CREATE\"：创建中 \"PENDING_UPDATE\"：更新中 \"PENDING_DELETE\"：删除中 \"INACTIVE\"：不可用

        :param status: The status of this NatGatewayResponseBody.
        :type status: str
        """
        self._status = status

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this NatGatewayResponseBody.

        解冻/冻结状态。 取值范围： - \"true\"：解冻 - \"false\"：冻结

        :return: The admin_state_up of this NatGatewayResponseBody.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this NatGatewayResponseBody.

        解冻/冻结状态。 取值范围： - \"true\"：解冻 - \"false\"：冻结

        :param admin_state_up: The admin_state_up of this NatGatewayResponseBody.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def created_at(self):
        r"""Gets the created_at of this NatGatewayResponseBody.

        公网NAT网关实例的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。

        :return: The created_at of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this NatGatewayResponseBody.

        公网NAT网关实例的创建时间，格式是yyyy-mm-dd hh:mm:ss.SSSSSS。

        :param created_at: The created_at of this NatGatewayResponseBody.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def router_id(self):
        r"""Gets the router_id of this NatGatewayResponseBody.

        VPC的id。

        :return: The router_id of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        r"""Sets the router_id of this NatGatewayResponseBody.

        VPC的id。

        :param router_id: The router_id of this NatGatewayResponseBody.
        :type router_id: str
        """
        self._router_id = router_id

    @property
    def internal_network_id(self):
        r"""Gets the internal_network_id of this NatGatewayResponseBody.

        公网NAT网关下行口（DVR的下一跳）所属的network id。

        :return: The internal_network_id of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._internal_network_id

    @internal_network_id.setter
    def internal_network_id(self, internal_network_id):
        r"""Sets the internal_network_id of this NatGatewayResponseBody.

        公网NAT网关下行口（DVR的下一跳）所属的network id。

        :param internal_network_id: The internal_network_id of this NatGatewayResponseBody.
        :type internal_network_id: str
        """
        self._internal_network_id = internal_network_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this NatGatewayResponseBody.

        企业项目ID。 创建公网NAT网关实例时，关联的企业项目ID。

        :return: The enterprise_project_id of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this NatGatewayResponseBody.

        企业项目ID。 创建公网NAT网关实例时，关联的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this NatGatewayResponseBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def session_conf(self):
        r"""Gets the session_conf of this NatGatewayResponseBody.

        :return: The session_conf of this NatGatewayResponseBody.
        :rtype: :class:`huaweicloudsdknat.v2.SessionConfiguration`
        """
        return self._session_conf

    @session_conf.setter
    def session_conf(self, session_conf):
        r"""Sets the session_conf of this NatGatewayResponseBody.

        :param session_conf: The session_conf of this NatGatewayResponseBody.
        :type session_conf: :class:`huaweicloudsdknat.v2.SessionConfiguration`
        """
        self._session_conf = session_conf

    @property
    def ngport_ip_address(self):
        r"""Gets the ngport_ip_address of this NatGatewayResponseBody.

        公网NAT网关私有IP地址，由VPC中子网分配。

        :return: The ngport_ip_address of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._ngport_ip_address

    @ngport_ip_address.setter
    def ngport_ip_address(self, ngport_ip_address):
        r"""Sets the ngport_ip_address of this NatGatewayResponseBody.

        公网NAT网关私有IP地址，由VPC中子网分配。

        :param ngport_ip_address: The ngport_ip_address of this NatGatewayResponseBody.
        :type ngport_ip_address: str
        """
        self._ngport_ip_address = ngport_ip_address

    @property
    def billing_info(self):
        r"""Gets the billing_info of this NatGatewayResponseBody.

        订单信息。此字段只有在订购包周期资源时才会有订单信息，而在订购按需资源时则为空。

        :return: The billing_info of this NatGatewayResponseBody.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        r"""Sets the billing_info of this NatGatewayResponseBody.

        订单信息。此字段只有在订购包周期资源时才会有订单信息，而在订购按需资源时则为空。

        :param billing_info: The billing_info of this NatGatewayResponseBody.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def dnat_rules_limit(self):
        r"""Gets the dnat_rules_limit of this NatGatewayResponseBody.

        公网NAT网关下DNAT规则数量限制，默认为200。

        :return: The dnat_rules_limit of this NatGatewayResponseBody.
        :rtype: int
        """
        return self._dnat_rules_limit

    @dnat_rules_limit.setter
    def dnat_rules_limit(self, dnat_rules_limit):
        r"""Sets the dnat_rules_limit of this NatGatewayResponseBody.

        公网NAT网关下DNAT规则数量限制，默认为200。

        :param dnat_rules_limit: The dnat_rules_limit of this NatGatewayResponseBody.
        :type dnat_rules_limit: int
        """
        self._dnat_rules_limit = dnat_rules_limit

    @property
    def snat_rule_public_ip_limit(self):
        r"""Gets the snat_rule_public_ip_limit of this NatGatewayResponseBody.

        公网NAT网关下SNAT规则EIP池中EIP数量限制，默认为20。

        :return: The snat_rule_public_ip_limit of this NatGatewayResponseBody.
        :rtype: int
        """
        return self._snat_rule_public_ip_limit

    @snat_rule_public_ip_limit.setter
    def snat_rule_public_ip_limit(self, snat_rule_public_ip_limit):
        r"""Sets the snat_rule_public_ip_limit of this NatGatewayResponseBody.

        公网NAT网关下SNAT规则EIP池中EIP数量限制，默认为20。

        :param snat_rule_public_ip_limit: The snat_rule_public_ip_limit of this NatGatewayResponseBody.
        :type snat_rule_public_ip_limit: int
        """
        self._snat_rule_public_ip_limit = snat_rule_public_ip_limit

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
