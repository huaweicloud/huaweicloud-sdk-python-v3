# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronFirewallPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audited': 'bool',
        'description': 'str',
        'firewall_rules': 'list[str]',
        'id': 'str',
        'name': 'str',
        'public': 'bool',
        'tenant_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'audited': 'audited',
        'description': 'description',
        'firewall_rules': 'firewall_rules',
        'id': 'id',
        'name': 'name',
        'public': 'public',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id'
    }

    def __init__(self, audited=None, description=None, firewall_rules=None, id=None, name=None, public=None, tenant_id=None, project_id=None):
        """NeutronFirewallPolicy

        The model defined in huaweicloud sdk

        :param audited: 审计标记。
        :type audited: bool
        :param description: 网络ACL防火墙策略描述。
        :type description: str
        :param firewall_rules: 策略引用的网络ACL防火墙规则链。
        :type firewall_rules: list[str]
        :param id: 网络ACL防火墙策略uuid标识。
        :type id: str
        :param name: 网络ACL防火墙策略名称。
        :type name: str
        :param public: 是否支持跨租户共享。
        :type public: bool
        :param tenant_id: 项目ID
        :type tenant_id: str
        :param project_id: 项目ID
        :type project_id: str
        """
        
        

        self._audited = None
        self._description = None
        self._firewall_rules = None
        self._id = None
        self._name = None
        self._public = None
        self._tenant_id = None
        self._project_id = None
        self.discriminator = None

        self.audited = audited
        self.description = description
        self.firewall_rules = firewall_rules
        self.id = id
        self.name = name
        self.public = public
        self.tenant_id = tenant_id
        self.project_id = project_id

    @property
    def audited(self):
        """Gets the audited of this NeutronFirewallPolicy.

        审计标记。

        :return: The audited of this NeutronFirewallPolicy.
        :rtype: bool
        """
        return self._audited

    @audited.setter
    def audited(self, audited):
        """Sets the audited of this NeutronFirewallPolicy.

        审计标记。

        :param audited: The audited of this NeutronFirewallPolicy.
        :type audited: bool
        """
        self._audited = audited

    @property
    def description(self):
        """Gets the description of this NeutronFirewallPolicy.

        网络ACL防火墙策略描述。

        :return: The description of this NeutronFirewallPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronFirewallPolicy.

        网络ACL防火墙策略描述。

        :param description: The description of this NeutronFirewallPolicy.
        :type description: str
        """
        self._description = description

    @property
    def firewall_rules(self):
        """Gets the firewall_rules of this NeutronFirewallPolicy.

        策略引用的网络ACL防火墙规则链。

        :return: The firewall_rules of this NeutronFirewallPolicy.
        :rtype: list[str]
        """
        return self._firewall_rules

    @firewall_rules.setter
    def firewall_rules(self, firewall_rules):
        """Sets the firewall_rules of this NeutronFirewallPolicy.

        策略引用的网络ACL防火墙规则链。

        :param firewall_rules: The firewall_rules of this NeutronFirewallPolicy.
        :type firewall_rules: list[str]
        """
        self._firewall_rules = firewall_rules

    @property
    def id(self):
        """Gets the id of this NeutronFirewallPolicy.

        网络ACL防火墙策略uuid标识。

        :return: The id of this NeutronFirewallPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronFirewallPolicy.

        网络ACL防火墙策略uuid标识。

        :param id: The id of this NeutronFirewallPolicy.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NeutronFirewallPolicy.

        网络ACL防火墙策略名称。

        :return: The name of this NeutronFirewallPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronFirewallPolicy.

        网络ACL防火墙策略名称。

        :param name: The name of this NeutronFirewallPolicy.
        :type name: str
        """
        self._name = name

    @property
    def public(self):
        """Gets the public of this NeutronFirewallPolicy.

        是否支持跨租户共享。

        :return: The public of this NeutronFirewallPolicy.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this NeutronFirewallPolicy.

        是否支持跨租户共享。

        :param public: The public of this NeutronFirewallPolicy.
        :type public: bool
        """
        self._public = public

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronFirewallPolicy.

        项目ID

        :return: The tenant_id of this NeutronFirewallPolicy.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronFirewallPolicy.

        项目ID

        :param tenant_id: The tenant_id of this NeutronFirewallPolicy.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this NeutronFirewallPolicy.

        项目ID

        :return: The project_id of this NeutronFirewallPolicy.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NeutronFirewallPolicy.

        项目ID

        :param project_id: The project_id of this NeutronFirewallPolicy.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, NeutronFirewallPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
