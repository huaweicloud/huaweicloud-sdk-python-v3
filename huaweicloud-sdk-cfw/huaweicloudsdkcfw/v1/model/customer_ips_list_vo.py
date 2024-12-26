# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomerIpsListVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'int',
        'affected_os': 'int',
        'attack_type': 'int',
        'config_status': 'int',
        'content': 'str',
        'dst_port_type': 'int',
        'dst_ports': 'str',
        'group_id': 'str',
        'ips_cfw_id': 'str',
        'ips_id': 'str',
        'ips_name': 'str',
        'protocol': 'int',
        'severity': 'int',
        'software': 'int',
        'src_port_type': 'int',
        'src_ports': 'str'
    }

    attribute_map = {
        'action': 'action',
        'affected_os': 'affected_os',
        'attack_type': 'attack_type',
        'config_status': 'config_status',
        'content': 'content',
        'dst_port_type': 'dst_port_type',
        'dst_ports': 'dst_ports',
        'group_id': 'group_id',
        'ips_cfw_id': 'ips_cfw_id',
        'ips_id': 'ips_id',
        'ips_name': 'ips_name',
        'protocol': 'protocol',
        'severity': 'severity',
        'software': 'software',
        'src_port_type': 'src_port_type',
        'src_ports': 'src_ports'
    }

    def __init__(self, action=None, affected_os=None, attack_type=None, config_status=None, content=None, dst_port_type=None, dst_ports=None, group_id=None, ips_cfw_id=None, ips_id=None, ips_name=None, protocol=None, severity=None, software=None, src_port_type=None, src_ports=None):
        """CustomerIpsListVO

        The model defined in huaweicloud sdk

        :param action: 动作（0：只记录日志，1：重置/拦截）
        :type action: int
        :param affected_os: 操作系统
        :type affected_os: int
        :param attack_type: 攻击类型
        :type attack_type: int
        :param config_status: 规则状态（0：初始化，1：配置中，2：配置成功，3：配置失败）
        :type config_status: int
        :param content: 内容json存储
        :type content: str
        :param dst_port_type: 目的端口类型
        :type dst_port_type: int
        :param dst_ports: 目的端口
        :type dst_ports: str
        :param group_id: 防火墙集群id
        :type group_id: str
        :param ips_cfw_id: cfw侧自定义ips规则id
        :type ips_cfw_id: str
        :param ips_id: 山石侧规则id
        :type ips_id: str
        :param ips_name: ips规则名称
        :type ips_name: str
        :param protocol: 协议
        :type protocol: int
        :param severity: 严重程度（critical：致命，high：高危，medium:中危，low:低危）
        :type severity: int
        :param software: 影响软件
        :type software: int
        :param src_port_type: 源端口类型
        :type src_port_type: int
        :param src_ports: 源端口
        :type src_ports: str
        """
        
        

        self._action = None
        self._affected_os = None
        self._attack_type = None
        self._config_status = None
        self._content = None
        self._dst_port_type = None
        self._dst_ports = None
        self._group_id = None
        self._ips_cfw_id = None
        self._ips_id = None
        self._ips_name = None
        self._protocol = None
        self._severity = None
        self._software = None
        self._src_port_type = None
        self._src_ports = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if affected_os is not None:
            self.affected_os = affected_os
        if attack_type is not None:
            self.attack_type = attack_type
        if config_status is not None:
            self.config_status = config_status
        if content is not None:
            self.content = content
        if dst_port_type is not None:
            self.dst_port_type = dst_port_type
        if dst_ports is not None:
            self.dst_ports = dst_ports
        if group_id is not None:
            self.group_id = group_id
        if ips_cfw_id is not None:
            self.ips_cfw_id = ips_cfw_id
        if ips_id is not None:
            self.ips_id = ips_id
        if ips_name is not None:
            self.ips_name = ips_name
        if protocol is not None:
            self.protocol = protocol
        if severity is not None:
            self.severity = severity
        if software is not None:
            self.software = software
        if src_port_type is not None:
            self.src_port_type = src_port_type
        if src_ports is not None:
            self.src_ports = src_ports

    @property
    def action(self):
        """Gets the action of this CustomerIpsListVO.

        动作（0：只记录日志，1：重置/拦截）

        :return: The action of this CustomerIpsListVO.
        :rtype: int
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CustomerIpsListVO.

        动作（0：只记录日志，1：重置/拦截）

        :param action: The action of this CustomerIpsListVO.
        :type action: int
        """
        self._action = action

    @property
    def affected_os(self):
        """Gets the affected_os of this CustomerIpsListVO.

        操作系统

        :return: The affected_os of this CustomerIpsListVO.
        :rtype: int
        """
        return self._affected_os

    @affected_os.setter
    def affected_os(self, affected_os):
        """Sets the affected_os of this CustomerIpsListVO.

        操作系统

        :param affected_os: The affected_os of this CustomerIpsListVO.
        :type affected_os: int
        """
        self._affected_os = affected_os

    @property
    def attack_type(self):
        """Gets the attack_type of this CustomerIpsListVO.

        攻击类型

        :return: The attack_type of this CustomerIpsListVO.
        :rtype: int
        """
        return self._attack_type

    @attack_type.setter
    def attack_type(self, attack_type):
        """Sets the attack_type of this CustomerIpsListVO.

        攻击类型

        :param attack_type: The attack_type of this CustomerIpsListVO.
        :type attack_type: int
        """
        self._attack_type = attack_type

    @property
    def config_status(self):
        """Gets the config_status of this CustomerIpsListVO.

        规则状态（0：初始化，1：配置中，2：配置成功，3：配置失败）

        :return: The config_status of this CustomerIpsListVO.
        :rtype: int
        """
        return self._config_status

    @config_status.setter
    def config_status(self, config_status):
        """Sets the config_status of this CustomerIpsListVO.

        规则状态（0：初始化，1：配置中，2：配置成功，3：配置失败）

        :param config_status: The config_status of this CustomerIpsListVO.
        :type config_status: int
        """
        self._config_status = config_status

    @property
    def content(self):
        """Gets the content of this CustomerIpsListVO.

        内容json存储

        :return: The content of this CustomerIpsListVO.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CustomerIpsListVO.

        内容json存储

        :param content: The content of this CustomerIpsListVO.
        :type content: str
        """
        self._content = content

    @property
    def dst_port_type(self):
        """Gets the dst_port_type of this CustomerIpsListVO.

        目的端口类型

        :return: The dst_port_type of this CustomerIpsListVO.
        :rtype: int
        """
        return self._dst_port_type

    @dst_port_type.setter
    def dst_port_type(self, dst_port_type):
        """Sets the dst_port_type of this CustomerIpsListVO.

        目的端口类型

        :param dst_port_type: The dst_port_type of this CustomerIpsListVO.
        :type dst_port_type: int
        """
        self._dst_port_type = dst_port_type

    @property
    def dst_ports(self):
        """Gets the dst_ports of this CustomerIpsListVO.

        目的端口

        :return: The dst_ports of this CustomerIpsListVO.
        :rtype: str
        """
        return self._dst_ports

    @dst_ports.setter
    def dst_ports(self, dst_ports):
        """Sets the dst_ports of this CustomerIpsListVO.

        目的端口

        :param dst_ports: The dst_ports of this CustomerIpsListVO.
        :type dst_ports: str
        """
        self._dst_ports = dst_ports

    @property
    def group_id(self):
        """Gets the group_id of this CustomerIpsListVO.

        防火墙集群id

        :return: The group_id of this CustomerIpsListVO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this CustomerIpsListVO.

        防火墙集群id

        :param group_id: The group_id of this CustomerIpsListVO.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def ips_cfw_id(self):
        """Gets the ips_cfw_id of this CustomerIpsListVO.

        cfw侧自定义ips规则id

        :return: The ips_cfw_id of this CustomerIpsListVO.
        :rtype: str
        """
        return self._ips_cfw_id

    @ips_cfw_id.setter
    def ips_cfw_id(self, ips_cfw_id):
        """Sets the ips_cfw_id of this CustomerIpsListVO.

        cfw侧自定义ips规则id

        :param ips_cfw_id: The ips_cfw_id of this CustomerIpsListVO.
        :type ips_cfw_id: str
        """
        self._ips_cfw_id = ips_cfw_id

    @property
    def ips_id(self):
        """Gets the ips_id of this CustomerIpsListVO.

        山石侧规则id

        :return: The ips_id of this CustomerIpsListVO.
        :rtype: str
        """
        return self._ips_id

    @ips_id.setter
    def ips_id(self, ips_id):
        """Sets the ips_id of this CustomerIpsListVO.

        山石侧规则id

        :param ips_id: The ips_id of this CustomerIpsListVO.
        :type ips_id: str
        """
        self._ips_id = ips_id

    @property
    def ips_name(self):
        """Gets the ips_name of this CustomerIpsListVO.

        ips规则名称

        :return: The ips_name of this CustomerIpsListVO.
        :rtype: str
        """
        return self._ips_name

    @ips_name.setter
    def ips_name(self, ips_name):
        """Sets the ips_name of this CustomerIpsListVO.

        ips规则名称

        :param ips_name: The ips_name of this CustomerIpsListVO.
        :type ips_name: str
        """
        self._ips_name = ips_name

    @property
    def protocol(self):
        """Gets the protocol of this CustomerIpsListVO.

        协议

        :return: The protocol of this CustomerIpsListVO.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CustomerIpsListVO.

        协议

        :param protocol: The protocol of this CustomerIpsListVO.
        :type protocol: int
        """
        self._protocol = protocol

    @property
    def severity(self):
        """Gets the severity of this CustomerIpsListVO.

        严重程度（critical：致命，high：高危，medium:中危，low:低危）

        :return: The severity of this CustomerIpsListVO.
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this CustomerIpsListVO.

        严重程度（critical：致命，high：高危，medium:中危，low:低危）

        :param severity: The severity of this CustomerIpsListVO.
        :type severity: int
        """
        self._severity = severity

    @property
    def software(self):
        """Gets the software of this CustomerIpsListVO.

        影响软件

        :return: The software of this CustomerIpsListVO.
        :rtype: int
        """
        return self._software

    @software.setter
    def software(self, software):
        """Sets the software of this CustomerIpsListVO.

        影响软件

        :param software: The software of this CustomerIpsListVO.
        :type software: int
        """
        self._software = software

    @property
    def src_port_type(self):
        """Gets the src_port_type of this CustomerIpsListVO.

        源端口类型

        :return: The src_port_type of this CustomerIpsListVO.
        :rtype: int
        """
        return self._src_port_type

    @src_port_type.setter
    def src_port_type(self, src_port_type):
        """Sets the src_port_type of this CustomerIpsListVO.

        源端口类型

        :param src_port_type: The src_port_type of this CustomerIpsListVO.
        :type src_port_type: int
        """
        self._src_port_type = src_port_type

    @property
    def src_ports(self):
        """Gets the src_ports of this CustomerIpsListVO.

        源端口

        :return: The src_ports of this CustomerIpsListVO.
        :rtype: str
        """
        return self._src_ports

    @src_ports.setter
    def src_ports(self, src_ports):
        """Sets the src_ports of this CustomerIpsListVO.

        源端口

        :param src_ports: The src_ports of this CustomerIpsListVO.
        :type src_ports: str
        """
        self._src_ports = src_ports

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
        if not isinstance(other, CustomerIpsListVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
