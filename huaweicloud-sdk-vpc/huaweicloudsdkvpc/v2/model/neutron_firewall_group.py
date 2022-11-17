# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronFirewallGroup:

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
        'name': 'str',
        'description': 'str',
        'admin_state_up': 'bool',
        'egress_firewall_policy_id': 'str',
        'ingress_firewall_policy_id': 'str',
        'ports': 'list[str]',
        'public': 'bool',
        'status': 'str',
        'tenant_id': 'str',
        'project_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'admin_state_up': 'admin_state_up',
        'egress_firewall_policy_id': 'egress_firewall_policy_id',
        'ingress_firewall_policy_id': 'ingress_firewall_policy_id',
        'ports': 'ports',
        'public': 'public',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, admin_state_up=None, egress_firewall_policy_id=None, ingress_firewall_policy_id=None, ports=None, public=None, status=None, tenant_id=None, project_id=None, created_at=None, updated_at=None):
        """NeutronFirewallGroup

        The model defined in huaweicloud sdk

        :param id: 功能说明：网络ACL组的ID
        :type id: str
        :param name: 功能说明：网络ACL组名称 取值范围：0-255个字符
        :type name: str
        :param description: 功能说明：网络ACL组描述 取值范围：0-255个字符
        :type description: str
        :param admin_state_up: 网络ACL防火墙是否受管理员控制。
        :type admin_state_up: bool
        :param egress_firewall_policy_id: 功能说明：出方向网络ACL策略ID
        :type egress_firewall_policy_id: str
        :param ingress_firewall_policy_id: 功能说明：入方向网络ACL策略ID
        :type ingress_firewall_policy_id: str
        :param ports: 取值范围：网络ACL组绑定的端口列表
        :type ports: list[str]
        :param public: 功能说明：是否支持跨租户共享 取值范围：true/false
        :type public: bool
        :param status: 功能说明：网络ACL组状态
        :type status: str
        :param tenant_id: 功能说明：网络ACL组所属项目ID
        :type tenant_id: str
        :param project_id: 功能说明：网络ACL组所属项目ID
        :type project_id: str
        :param created_at: 功能说明：资源创建时间，UTC时间 格式：yyyy-MM-ddTHH:mm:ss
        :type created_at: datetime
        :param updated_at: 功能说明：资源更新时间，UTC时间 格式：yyyy-MM-ddTHH:mm:ss
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._admin_state_up = None
        self._egress_firewall_policy_id = None
        self._ingress_firewall_policy_id = None
        self._ports = None
        self._public = None
        self._status = None
        self._tenant_id = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.admin_state_up = admin_state_up
        self.egress_firewall_policy_id = egress_firewall_policy_id
        self.ingress_firewall_policy_id = ingress_firewall_policy_id
        self.ports = ports
        self.public = public
        self.status = status
        self.tenant_id = tenant_id
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this NeutronFirewallGroup.

        功能说明：网络ACL组的ID

        :return: The id of this NeutronFirewallGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronFirewallGroup.

        功能说明：网络ACL组的ID

        :param id: The id of this NeutronFirewallGroup.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NeutronFirewallGroup.

        功能说明：网络ACL组名称 取值范围：0-255个字符

        :return: The name of this NeutronFirewallGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronFirewallGroup.

        功能说明：网络ACL组名称 取值范围：0-255个字符

        :param name: The name of this NeutronFirewallGroup.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this NeutronFirewallGroup.

        功能说明：网络ACL组描述 取值范围：0-255个字符

        :return: The description of this NeutronFirewallGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronFirewallGroup.

        功能说明：网络ACL组描述 取值范围：0-255个字符

        :param description: The description of this NeutronFirewallGroup.
        :type description: str
        """
        self._description = description

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this NeutronFirewallGroup.

        网络ACL防火墙是否受管理员控制。

        :return: The admin_state_up of this NeutronFirewallGroup.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this NeutronFirewallGroup.

        网络ACL防火墙是否受管理员控制。

        :param admin_state_up: The admin_state_up of this NeutronFirewallGroup.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def egress_firewall_policy_id(self):
        """Gets the egress_firewall_policy_id of this NeutronFirewallGroup.

        功能说明：出方向网络ACL策略ID

        :return: The egress_firewall_policy_id of this NeutronFirewallGroup.
        :rtype: str
        """
        return self._egress_firewall_policy_id

    @egress_firewall_policy_id.setter
    def egress_firewall_policy_id(self, egress_firewall_policy_id):
        """Sets the egress_firewall_policy_id of this NeutronFirewallGroup.

        功能说明：出方向网络ACL策略ID

        :param egress_firewall_policy_id: The egress_firewall_policy_id of this NeutronFirewallGroup.
        :type egress_firewall_policy_id: str
        """
        self._egress_firewall_policy_id = egress_firewall_policy_id

    @property
    def ingress_firewall_policy_id(self):
        """Gets the ingress_firewall_policy_id of this NeutronFirewallGroup.

        功能说明：入方向网络ACL策略ID

        :return: The ingress_firewall_policy_id of this NeutronFirewallGroup.
        :rtype: str
        """
        return self._ingress_firewall_policy_id

    @ingress_firewall_policy_id.setter
    def ingress_firewall_policy_id(self, ingress_firewall_policy_id):
        """Sets the ingress_firewall_policy_id of this NeutronFirewallGroup.

        功能说明：入方向网络ACL策略ID

        :param ingress_firewall_policy_id: The ingress_firewall_policy_id of this NeutronFirewallGroup.
        :type ingress_firewall_policy_id: str
        """
        self._ingress_firewall_policy_id = ingress_firewall_policy_id

    @property
    def ports(self):
        """Gets the ports of this NeutronFirewallGroup.

        取值范围：网络ACL组绑定的端口列表

        :return: The ports of this NeutronFirewallGroup.
        :rtype: list[str]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this NeutronFirewallGroup.

        取值范围：网络ACL组绑定的端口列表

        :param ports: The ports of this NeutronFirewallGroup.
        :type ports: list[str]
        """
        self._ports = ports

    @property
    def public(self):
        """Gets the public of this NeutronFirewallGroup.

        功能说明：是否支持跨租户共享 取值范围：true/false

        :return: The public of this NeutronFirewallGroup.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this NeutronFirewallGroup.

        功能说明：是否支持跨租户共享 取值范围：true/false

        :param public: The public of this NeutronFirewallGroup.
        :type public: bool
        """
        self._public = public

    @property
    def status(self):
        """Gets the status of this NeutronFirewallGroup.

        功能说明：网络ACL组状态

        :return: The status of this NeutronFirewallGroup.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NeutronFirewallGroup.

        功能说明：网络ACL组状态

        :param status: The status of this NeutronFirewallGroup.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronFirewallGroup.

        功能说明：网络ACL组所属项目ID

        :return: The tenant_id of this NeutronFirewallGroup.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronFirewallGroup.

        功能说明：网络ACL组所属项目ID

        :param tenant_id: The tenant_id of this NeutronFirewallGroup.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this NeutronFirewallGroup.

        功能说明：网络ACL组所属项目ID

        :return: The project_id of this NeutronFirewallGroup.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NeutronFirewallGroup.

        功能说明：网络ACL组所属项目ID

        :param project_id: The project_id of this NeutronFirewallGroup.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this NeutronFirewallGroup.

        功能说明：资源创建时间，UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this NeutronFirewallGroup.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NeutronFirewallGroup.

        功能说明：资源创建时间，UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this NeutronFirewallGroup.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this NeutronFirewallGroup.

        功能说明：资源更新时间，UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this NeutronFirewallGroup.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NeutronFirewallGroup.

        功能说明：资源更新时间，UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this NeutronFirewallGroup.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, NeutronFirewallGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
