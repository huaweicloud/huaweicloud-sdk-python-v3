# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronRemoveFirewallRuleResponse(SdkResponse):

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
        'firewall_rules': 'list[str]',
        'audited': 'bool',
        'public': 'bool',
        'tenant_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'firewall_rules': 'firewall_rules',
        'audited': 'audited',
        'public': 'public',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id'
    }

    def __init__(self, id=None, name=None, description=None, firewall_rules=None, audited=None, public=None, tenant_id=None, project_id=None):
        """NeutronRemoveFirewallRuleResponse

        The model defined in huaweicloud sdk

        :param id: 功能说明：网络ACL策略ID
        :type id: str
        :param name: 功能说明：网络ACL策略名称
        :type name: str
        :param description: 功能说明：网络ACL策略的描述信息 取值范围：0-255个字符
        :type description: str
        :param firewall_rules: 功能说明：网络ACL策略关联的规则的ID列表
        :type firewall_rules: list[str]
        :param audited: 功能说明：每次policy或者它相关的rule有变动，该参数将会被置为False
        :type audited: bool
        :param public: 功能说明：网络ACL策略是否对其他网络ACL策略可见 取值范围：true(可见)、false(不可见)
        :type public: bool
        :param tenant_id: 功能说明：网络ACL策略所属项目ID
        :type tenant_id: str
        :param project_id: 功能说明：网络ACL策略所属项目ID
        :type project_id: str
        """
        
        super(NeutronRemoveFirewallRuleResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._firewall_rules = None
        self._audited = None
        self._public = None
        self._tenant_id = None
        self._project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if firewall_rules is not None:
            self.firewall_rules = firewall_rules
        if audited is not None:
            self.audited = audited
        if public is not None:
            self.public = public
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if project_id is not None:
            self.project_id = project_id

    @property
    def id(self):
        """Gets the id of this NeutronRemoveFirewallRuleResponse.

        功能说明：网络ACL策略ID

        :return: The id of this NeutronRemoveFirewallRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronRemoveFirewallRuleResponse.

        功能说明：网络ACL策略ID

        :param id: The id of this NeutronRemoveFirewallRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NeutronRemoveFirewallRuleResponse.

        功能说明：网络ACL策略名称

        :return: The name of this NeutronRemoveFirewallRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronRemoveFirewallRuleResponse.

        功能说明：网络ACL策略名称

        :param name: The name of this NeutronRemoveFirewallRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this NeutronRemoveFirewallRuleResponse.

        功能说明：网络ACL策略的描述信息 取值范围：0-255个字符

        :return: The description of this NeutronRemoveFirewallRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronRemoveFirewallRuleResponse.

        功能说明：网络ACL策略的描述信息 取值范围：0-255个字符

        :param description: The description of this NeutronRemoveFirewallRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def firewall_rules(self):
        """Gets the firewall_rules of this NeutronRemoveFirewallRuleResponse.

        功能说明：网络ACL策略关联的规则的ID列表

        :return: The firewall_rules of this NeutronRemoveFirewallRuleResponse.
        :rtype: list[str]
        """
        return self._firewall_rules

    @firewall_rules.setter
    def firewall_rules(self, firewall_rules):
        """Sets the firewall_rules of this NeutronRemoveFirewallRuleResponse.

        功能说明：网络ACL策略关联的规则的ID列表

        :param firewall_rules: The firewall_rules of this NeutronRemoveFirewallRuleResponse.
        :type firewall_rules: list[str]
        """
        self._firewall_rules = firewall_rules

    @property
    def audited(self):
        """Gets the audited of this NeutronRemoveFirewallRuleResponse.

        功能说明：每次policy或者它相关的rule有变动，该参数将会被置为False

        :return: The audited of this NeutronRemoveFirewallRuleResponse.
        :rtype: bool
        """
        return self._audited

    @audited.setter
    def audited(self, audited):
        """Sets the audited of this NeutronRemoveFirewallRuleResponse.

        功能说明：每次policy或者它相关的rule有变动，该参数将会被置为False

        :param audited: The audited of this NeutronRemoveFirewallRuleResponse.
        :type audited: bool
        """
        self._audited = audited

    @property
    def public(self):
        """Gets the public of this NeutronRemoveFirewallRuleResponse.

        功能说明：网络ACL策略是否对其他网络ACL策略可见 取值范围：true(可见)、false(不可见)

        :return: The public of this NeutronRemoveFirewallRuleResponse.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this NeutronRemoveFirewallRuleResponse.

        功能说明：网络ACL策略是否对其他网络ACL策略可见 取值范围：true(可见)、false(不可见)

        :param public: The public of this NeutronRemoveFirewallRuleResponse.
        :type public: bool
        """
        self._public = public

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronRemoveFirewallRuleResponse.

        功能说明：网络ACL策略所属项目ID

        :return: The tenant_id of this NeutronRemoveFirewallRuleResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronRemoveFirewallRuleResponse.

        功能说明：网络ACL策略所属项目ID

        :param tenant_id: The tenant_id of this NeutronRemoveFirewallRuleResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this NeutronRemoveFirewallRuleResponse.

        功能说明：网络ACL策略所属项目ID

        :return: The project_id of this NeutronRemoveFirewallRuleResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NeutronRemoveFirewallRuleResponse.

        功能说明：网络ACL策略所属项目ID

        :param project_id: The project_id of this NeutronRemoveFirewallRuleResponse.
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
        if not isinstance(other, NeutronRemoveFirewallRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
