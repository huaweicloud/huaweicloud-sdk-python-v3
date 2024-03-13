# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicsAgentNodeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'agent_vpcep_eps_id': 'str',
        'ecs_server_id': 'str',
        'league_server_ip_security_group_rule': 'str',
        'league_server_snat_ip': 'str',
        'nat_eip': 'str',
        'nat_eip_id': 'str',
        'node_az': 'str',
        'node_id': 'str',
        'node_ip': 'str',
        'node_name': 'str',
        'server_to_agent_vpcep_epi_id': 'str',
        'server_to_agent_vpcep_epi_ip': 'str',
        'snat_rule_id': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'agent_vpcep_eps_id': 'agent_vpcep_eps_id',
        'ecs_server_id': 'ecs_server_id',
        'league_server_ip_security_group_rule': 'league_server_ip_security_group_rule',
        'league_server_snat_ip': 'league_server_snat_ip',
        'nat_eip': 'nat_eip',
        'nat_eip_id': 'nat_eip_id',
        'node_az': 'node_az',
        'node_id': 'node_id',
        'node_ip': 'node_ip',
        'node_name': 'node_name',
        'server_to_agent_vpcep_epi_id': 'server_to_agent_vpcep_epi_id',
        'server_to_agent_vpcep_epi_ip': 'server_to_agent_vpcep_epi_ip',
        'snat_rule_id': 'snat_rule_id'
    }

    def __init__(self, agent_id=None, agent_vpcep_eps_id=None, ecs_server_id=None, league_server_ip_security_group_rule=None, league_server_snat_ip=None, nat_eip=None, nat_eip_id=None, node_az=None, node_id=None, node_ip=None, node_name=None, server_to_agent_vpcep_epi_id=None, server_to_agent_vpcep_epi_ip=None, snat_rule_id=None):
        """TicsAgentNodeInfo

        The model defined in huaweicloud sdk

        :param agent_id: 可信节点Id
        :type agent_id: str
        :param agent_vpcep_eps_id: 无eip场景下,agent的eps id
        :type agent_vpcep_eps_id: str
        :param ecs_server_id: 弹性云服务器Id，IEF部署同node_id
        :type ecs_server_id: str
        :param league_server_ip_security_group_rule: 入方向安全组规则ID
        :type league_server_ip_security_group_rule: str
        :param league_server_snat_ip: 联盟server组件的ip，为server的snatip，设置代理节点的入方向安全组规则
        :type league_server_snat_ip: str
        :param nat_eip: 可信节点绑定的网关的ip，CCE部署时会返回该值
        :type nat_eip: str
        :param nat_eip_id: 可信节点绑定的网关的ip的Id，CCE部署时会返回该值
        :type nat_eip_id: str
        :param node_az: 弹性云服务器所在可用区，CCE部署时会返回该值
        :type node_az: str
        :param node_id: 可信节点部署的虚机id，CCE部署情况返回CCE节点ID。
        :type node_id: str
        :param node_ip: 弹性云服务器的私网ip
        :type node_ip: str
        :param node_name: 弹性云服务器的名称
        :type node_name: str
        :param server_to_agent_vpcep_epi_id: 无eip场景下,server访问agent的epi id
        :type server_to_agent_vpcep_epi_id: str
        :param server_to_agent_vpcep_epi_ip: 无eip场景下,server访问agent的ip
        :type server_to_agent_vpcep_epi_ip: str
        :param snat_rule_id: 节点绑定的snat id
        :type snat_rule_id: str
        """
        
        

        self._agent_id = None
        self._agent_vpcep_eps_id = None
        self._ecs_server_id = None
        self._league_server_ip_security_group_rule = None
        self._league_server_snat_ip = None
        self._nat_eip = None
        self._nat_eip_id = None
        self._node_az = None
        self._node_id = None
        self._node_ip = None
        self._node_name = None
        self._server_to_agent_vpcep_epi_id = None
        self._server_to_agent_vpcep_epi_ip = None
        self._snat_rule_id = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if agent_vpcep_eps_id is not None:
            self.agent_vpcep_eps_id = agent_vpcep_eps_id
        if ecs_server_id is not None:
            self.ecs_server_id = ecs_server_id
        if league_server_ip_security_group_rule is not None:
            self.league_server_ip_security_group_rule = league_server_ip_security_group_rule
        if league_server_snat_ip is not None:
            self.league_server_snat_ip = league_server_snat_ip
        if nat_eip is not None:
            self.nat_eip = nat_eip
        if nat_eip_id is not None:
            self.nat_eip_id = nat_eip_id
        if node_az is not None:
            self.node_az = node_az
        if node_id is not None:
            self.node_id = node_id
        if node_ip is not None:
            self.node_ip = node_ip
        if node_name is not None:
            self.node_name = node_name
        if server_to_agent_vpcep_epi_id is not None:
            self.server_to_agent_vpcep_epi_id = server_to_agent_vpcep_epi_id
        if server_to_agent_vpcep_epi_ip is not None:
            self.server_to_agent_vpcep_epi_ip = server_to_agent_vpcep_epi_ip
        if snat_rule_id is not None:
            self.snat_rule_id = snat_rule_id

    @property
    def agent_id(self):
        """Gets the agent_id of this TicsAgentNodeInfo.

        可信节点Id

        :return: The agent_id of this TicsAgentNodeInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this TicsAgentNodeInfo.

        可信节点Id

        :param agent_id: The agent_id of this TicsAgentNodeInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_vpcep_eps_id(self):
        """Gets the agent_vpcep_eps_id of this TicsAgentNodeInfo.

        无eip场景下,agent的eps id

        :return: The agent_vpcep_eps_id of this TicsAgentNodeInfo.
        :rtype: str
        """
        return self._agent_vpcep_eps_id

    @agent_vpcep_eps_id.setter
    def agent_vpcep_eps_id(self, agent_vpcep_eps_id):
        """Sets the agent_vpcep_eps_id of this TicsAgentNodeInfo.

        无eip场景下,agent的eps id

        :param agent_vpcep_eps_id: The agent_vpcep_eps_id of this TicsAgentNodeInfo.
        :type agent_vpcep_eps_id: str
        """
        self._agent_vpcep_eps_id = agent_vpcep_eps_id

    @property
    def ecs_server_id(self):
        """Gets the ecs_server_id of this TicsAgentNodeInfo.

        弹性云服务器Id，IEF部署同node_id

        :return: The ecs_server_id of this TicsAgentNodeInfo.
        :rtype: str
        """
        return self._ecs_server_id

    @ecs_server_id.setter
    def ecs_server_id(self, ecs_server_id):
        """Sets the ecs_server_id of this TicsAgentNodeInfo.

        弹性云服务器Id，IEF部署同node_id

        :param ecs_server_id: The ecs_server_id of this TicsAgentNodeInfo.
        :type ecs_server_id: str
        """
        self._ecs_server_id = ecs_server_id

    @property
    def league_server_ip_security_group_rule(self):
        """Gets the league_server_ip_security_group_rule of this TicsAgentNodeInfo.

        入方向安全组规则ID

        :return: The league_server_ip_security_group_rule of this TicsAgentNodeInfo.
        :rtype: str
        """
        return self._league_server_ip_security_group_rule

    @league_server_ip_security_group_rule.setter
    def league_server_ip_security_group_rule(self, league_server_ip_security_group_rule):
        """Sets the league_server_ip_security_group_rule of this TicsAgentNodeInfo.

        入方向安全组规则ID

        :param league_server_ip_security_group_rule: The league_server_ip_security_group_rule of this TicsAgentNodeInfo.
        :type league_server_ip_security_group_rule: str
        """
        self._league_server_ip_security_group_rule = league_server_ip_security_group_rule

    @property
    def league_server_snat_ip(self):
        """Gets the league_server_snat_ip of this TicsAgentNodeInfo.

        联盟server组件的ip，为server的snatip，设置代理节点的入方向安全组规则

        :return: The league_server_snat_ip of this TicsAgentNodeInfo.
        :rtype: str
        """
        return self._league_server_snat_ip

    @league_server_snat_ip.setter
    def league_server_snat_ip(self, league_server_snat_ip):
        """Sets the league_server_snat_ip of this TicsAgentNodeInfo.

        联盟server组件的ip，为server的snatip，设置代理节点的入方向安全组规则

        :param league_server_snat_ip: The league_server_snat_ip of this TicsAgentNodeInfo.
        :type league_server_snat_ip: str
        """
        self._league_server_snat_ip = league_server_snat_ip

    @property
    def nat_eip(self):
        """Gets the nat_eip of this TicsAgentNodeInfo.

        可信节点绑定的网关的ip，CCE部署时会返回该值

        :return: The nat_eip of this TicsAgentNodeInfo.
        :rtype: str
        """
        return self._nat_eip

    @nat_eip.setter
    def nat_eip(self, nat_eip):
        """Sets the nat_eip of this TicsAgentNodeInfo.

        可信节点绑定的网关的ip，CCE部署时会返回该值

        :param nat_eip: The nat_eip of this TicsAgentNodeInfo.
        :type nat_eip: str
        """
        self._nat_eip = nat_eip

    @property
    def nat_eip_id(self):
        """Gets the nat_eip_id of this TicsAgentNodeInfo.

        可信节点绑定的网关的ip的Id，CCE部署时会返回该值

        :return: The nat_eip_id of this TicsAgentNodeInfo.
        :rtype: str
        """
        return self._nat_eip_id

    @nat_eip_id.setter
    def nat_eip_id(self, nat_eip_id):
        """Sets the nat_eip_id of this TicsAgentNodeInfo.

        可信节点绑定的网关的ip的Id，CCE部署时会返回该值

        :param nat_eip_id: The nat_eip_id of this TicsAgentNodeInfo.
        :type nat_eip_id: str
        """
        self._nat_eip_id = nat_eip_id

    @property
    def node_az(self):
        """Gets the node_az of this TicsAgentNodeInfo.

        弹性云服务器所在可用区，CCE部署时会返回该值

        :return: The node_az of this TicsAgentNodeInfo.
        :rtype: str
        """
        return self._node_az

    @node_az.setter
    def node_az(self, node_az):
        """Sets the node_az of this TicsAgentNodeInfo.

        弹性云服务器所在可用区，CCE部署时会返回该值

        :param node_az: The node_az of this TicsAgentNodeInfo.
        :type node_az: str
        """
        self._node_az = node_az

    @property
    def node_id(self):
        """Gets the node_id of this TicsAgentNodeInfo.

        可信节点部署的虚机id，CCE部署情况返回CCE节点ID。

        :return: The node_id of this TicsAgentNodeInfo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this TicsAgentNodeInfo.

        可信节点部署的虚机id，CCE部署情况返回CCE节点ID。

        :param node_id: The node_id of this TicsAgentNodeInfo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_ip(self):
        """Gets the node_ip of this TicsAgentNodeInfo.

        弹性云服务器的私网ip

        :return: The node_ip of this TicsAgentNodeInfo.
        :rtype: str
        """
        return self._node_ip

    @node_ip.setter
    def node_ip(self, node_ip):
        """Sets the node_ip of this TicsAgentNodeInfo.

        弹性云服务器的私网ip

        :param node_ip: The node_ip of this TicsAgentNodeInfo.
        :type node_ip: str
        """
        self._node_ip = node_ip

    @property
    def node_name(self):
        """Gets the node_name of this TicsAgentNodeInfo.

        弹性云服务器的名称

        :return: The node_name of this TicsAgentNodeInfo.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this TicsAgentNodeInfo.

        弹性云服务器的名称

        :param node_name: The node_name of this TicsAgentNodeInfo.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def server_to_agent_vpcep_epi_id(self):
        """Gets the server_to_agent_vpcep_epi_id of this TicsAgentNodeInfo.

        无eip场景下,server访问agent的epi id

        :return: The server_to_agent_vpcep_epi_id of this TicsAgentNodeInfo.
        :rtype: str
        """
        return self._server_to_agent_vpcep_epi_id

    @server_to_agent_vpcep_epi_id.setter
    def server_to_agent_vpcep_epi_id(self, server_to_agent_vpcep_epi_id):
        """Sets the server_to_agent_vpcep_epi_id of this TicsAgentNodeInfo.

        无eip场景下,server访问agent的epi id

        :param server_to_agent_vpcep_epi_id: The server_to_agent_vpcep_epi_id of this TicsAgentNodeInfo.
        :type server_to_agent_vpcep_epi_id: str
        """
        self._server_to_agent_vpcep_epi_id = server_to_agent_vpcep_epi_id

    @property
    def server_to_agent_vpcep_epi_ip(self):
        """Gets the server_to_agent_vpcep_epi_ip of this TicsAgentNodeInfo.

        无eip场景下,server访问agent的ip

        :return: The server_to_agent_vpcep_epi_ip of this TicsAgentNodeInfo.
        :rtype: str
        """
        return self._server_to_agent_vpcep_epi_ip

    @server_to_agent_vpcep_epi_ip.setter
    def server_to_agent_vpcep_epi_ip(self, server_to_agent_vpcep_epi_ip):
        """Sets the server_to_agent_vpcep_epi_ip of this TicsAgentNodeInfo.

        无eip场景下,server访问agent的ip

        :param server_to_agent_vpcep_epi_ip: The server_to_agent_vpcep_epi_ip of this TicsAgentNodeInfo.
        :type server_to_agent_vpcep_epi_ip: str
        """
        self._server_to_agent_vpcep_epi_ip = server_to_agent_vpcep_epi_ip

    @property
    def snat_rule_id(self):
        """Gets the snat_rule_id of this TicsAgentNodeInfo.

        节点绑定的snat id

        :return: The snat_rule_id of this TicsAgentNodeInfo.
        :rtype: str
        """
        return self._snat_rule_id

    @snat_rule_id.setter
    def snat_rule_id(self, snat_rule_id):
        """Sets the snat_rule_id of this TicsAgentNodeInfo.

        节点绑定的snat id

        :param snat_rule_id: The snat_rule_id of this TicsAgentNodeInfo.
        :type snat_rule_id: str
        """
        self._snat_rule_id = snat_rule_id

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
        if not isinstance(other, TicsAgentNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
