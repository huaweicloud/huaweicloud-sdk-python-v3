# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronCreateFirewallGroupOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'ingress_firewall_policy_id': 'str',
        'egress_firewall_policy_id': 'str',
        'ports': 'list[str]',
        'admin_state_up': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'ingress_firewall_policy_id': 'ingress_firewall_policy_id',
        'egress_firewall_policy_id': 'egress_firewall_policy_id',
        'ports': 'ports',
        'admin_state_up': 'admin_state_up'
    }

    def __init__(self, name=None, description=None, ingress_firewall_policy_id=None, egress_firewall_policy_id=None, ports=None, admin_state_up=None):
        """NeutronCreateFirewallGroupOption

        The model defined in huaweicloud sdk

        :param name: 功能说明：网络ACL组名称 取值范围：0-255个字符
        :type name: str
        :param description: 功能说明：网络ACL防火墙组描述 取值范围：最长255个字符
        :type description: str
        :param ingress_firewall_policy_id: 功能说明：入方向网络ACL策略
        :type ingress_firewall_policy_id: str
        :param egress_firewall_policy_id: 功能说明：出方向网络ACL策略
        :type egress_firewall_policy_id: str
        :param ports: 功能说明：网络ACL防火墙组绑定的端口列表 约束：必须为分布式router的端口id
        :type ports: list[str]
        :param admin_state_up: 功能说明：网络ACL是否受管理员控制
        :type admin_state_up: bool
        """
        
        

        self._name = None
        self._description = None
        self._ingress_firewall_policy_id = None
        self._egress_firewall_policy_id = None
        self._ports = None
        self._admin_state_up = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if ingress_firewall_policy_id is not None:
            self.ingress_firewall_policy_id = ingress_firewall_policy_id
        if egress_firewall_policy_id is not None:
            self.egress_firewall_policy_id = egress_firewall_policy_id
        if ports is not None:
            self.ports = ports
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up

    @property
    def name(self):
        """Gets the name of this NeutronCreateFirewallGroupOption.

        功能说明：网络ACL组名称 取值范围：0-255个字符

        :return: The name of this NeutronCreateFirewallGroupOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronCreateFirewallGroupOption.

        功能说明：网络ACL组名称 取值范围：0-255个字符

        :param name: The name of this NeutronCreateFirewallGroupOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this NeutronCreateFirewallGroupOption.

        功能说明：网络ACL防火墙组描述 取值范围：最长255个字符

        :return: The description of this NeutronCreateFirewallGroupOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronCreateFirewallGroupOption.

        功能说明：网络ACL防火墙组描述 取值范围：最长255个字符

        :param description: The description of this NeutronCreateFirewallGroupOption.
        :type description: str
        """
        self._description = description

    @property
    def ingress_firewall_policy_id(self):
        """Gets the ingress_firewall_policy_id of this NeutronCreateFirewallGroupOption.

        功能说明：入方向网络ACL策略

        :return: The ingress_firewall_policy_id of this NeutronCreateFirewallGroupOption.
        :rtype: str
        """
        return self._ingress_firewall_policy_id

    @ingress_firewall_policy_id.setter
    def ingress_firewall_policy_id(self, ingress_firewall_policy_id):
        """Sets the ingress_firewall_policy_id of this NeutronCreateFirewallGroupOption.

        功能说明：入方向网络ACL策略

        :param ingress_firewall_policy_id: The ingress_firewall_policy_id of this NeutronCreateFirewallGroupOption.
        :type ingress_firewall_policy_id: str
        """
        self._ingress_firewall_policy_id = ingress_firewall_policy_id

    @property
    def egress_firewall_policy_id(self):
        """Gets the egress_firewall_policy_id of this NeutronCreateFirewallGroupOption.

        功能说明：出方向网络ACL策略

        :return: The egress_firewall_policy_id of this NeutronCreateFirewallGroupOption.
        :rtype: str
        """
        return self._egress_firewall_policy_id

    @egress_firewall_policy_id.setter
    def egress_firewall_policy_id(self, egress_firewall_policy_id):
        """Sets the egress_firewall_policy_id of this NeutronCreateFirewallGroupOption.

        功能说明：出方向网络ACL策略

        :param egress_firewall_policy_id: The egress_firewall_policy_id of this NeutronCreateFirewallGroupOption.
        :type egress_firewall_policy_id: str
        """
        self._egress_firewall_policy_id = egress_firewall_policy_id

    @property
    def ports(self):
        """Gets the ports of this NeutronCreateFirewallGroupOption.

        功能说明：网络ACL防火墙组绑定的端口列表 约束：必须为分布式router的端口id

        :return: The ports of this NeutronCreateFirewallGroupOption.
        :rtype: list[str]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this NeutronCreateFirewallGroupOption.

        功能说明：网络ACL防火墙组绑定的端口列表 约束：必须为分布式router的端口id

        :param ports: The ports of this NeutronCreateFirewallGroupOption.
        :type ports: list[str]
        """
        self._ports = ports

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this NeutronCreateFirewallGroupOption.

        功能说明：网络ACL是否受管理员控制

        :return: The admin_state_up of this NeutronCreateFirewallGroupOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this NeutronCreateFirewallGroupOption.

        功能说明：网络ACL是否受管理员控制

        :param admin_state_up: The admin_state_up of this NeutronCreateFirewallGroupOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

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
        if not isinstance(other, NeutronCreateFirewallGroupOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
