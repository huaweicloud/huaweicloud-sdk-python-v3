# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PortHostResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'container_id': 'str',
        'host_id': 'str',
        'host_ip': 'str',
        'host_name': 'str',
        'laddr': 'str',
        'path': 'str',
        'pid': 'int',
        'port': 'int',
        'status': 'str',
        'type': 'str',
        'container_name': 'str',
        'agent_id': 'str'
    }

    attribute_map = {
        'container_id': 'container_id',
        'host_id': 'host_id',
        'host_ip': 'host_ip',
        'host_name': 'host_name',
        'laddr': 'laddr',
        'path': 'path',
        'pid': 'pid',
        'port': 'port',
        'status': 'status',
        'type': 'type',
        'container_name': 'container_name',
        'agent_id': 'agent_id'
    }

    def __init__(self, container_id=None, host_id=None, host_ip=None, host_name=None, laddr=None, path=None, pid=None, port=None, status=None, type=None, container_name=None, agent_id=None):
        r"""PortHostResponseInfo

        The model defined in huaweicloud sdk

        :param container_id: **参数解释**: 容器ID **取值范围**: 字符长度1-128位 
        :type container_id: str
        :param host_id: **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param host_ip: **参数解释**: 服务器IP **取值范围**: 字符长度1-128位 
        :type host_ip: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param laddr: **参数解释**: 端口的监听IP地址（0.0.0.0表示监听所有网卡） **取值范围**: 支持IPv4或IPv6格式，IPv4长度7-15位，IPv6长度15-39位 
        :type laddr: str
        :param path: **参数解释**: 占用当前端口的进程对应的可执行文件绝对路径 **取值范围**: 字符长度0-512位 
        :type path: str
        :param pid: **参数解释**: 占用当前端口的进程ID **取值范围**: 非负整数，最小值0（无对应进程时为0）；单位：个 
        :type pid: int
        :param port: **参数解释**: 端口的具体编号 **取值范围**: 1-65535（TCP/UDP标准端口范围） 
        :type port: int
        :param status: 状态
        :type status: str
        :param type: **参数解释**: 端口类型 **取值范围**: 目前包括TCP，UDP两种 
        :type type: str
        :param container_name: **参数解释**： 容器实例名称，只有容器类型的告警有 **取值范围**： 字符长度1-256位 
        :type container_name: str
        :param agent_id: **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type agent_id: str
        """
        
        

        self._container_id = None
        self._host_id = None
        self._host_ip = None
        self._host_name = None
        self._laddr = None
        self._path = None
        self._pid = None
        self._port = None
        self._status = None
        self._type = None
        self._container_name = None
        self._agent_id = None
        self.discriminator = None

        if container_id is not None:
            self.container_id = container_id
        if host_id is not None:
            self.host_id = host_id
        if host_ip is not None:
            self.host_ip = host_ip
        if host_name is not None:
            self.host_name = host_name
        if laddr is not None:
            self.laddr = laddr
        if path is not None:
            self.path = path
        if pid is not None:
            self.pid = pid
        if port is not None:
            self.port = port
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if container_name is not None:
            self.container_name = container_name
        if agent_id is not None:
            self.agent_id = agent_id

    @property
    def container_id(self):
        r"""Gets the container_id of this PortHostResponseInfo.

        **参数解释**: 容器ID **取值范围**: 字符长度1-128位 

        :return: The container_id of this PortHostResponseInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this PortHostResponseInfo.

        **参数解释**: 容器ID **取值范围**: 字符长度1-128位 

        :param container_id: The container_id of this PortHostResponseInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def host_id(self):
        r"""Gets the host_id of this PortHostResponseInfo.

        **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this PortHostResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this PortHostResponseInfo.

        **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this PortHostResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_ip(self):
        r"""Gets the host_ip of this PortHostResponseInfo.

        **参数解释**: 服务器IP **取值范围**: 字符长度1-128位 

        :return: The host_ip of this PortHostResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this PortHostResponseInfo.

        **参数解释**: 服务器IP **取值范围**: 字符长度1-128位 

        :param host_ip: The host_ip of this PortHostResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def host_name(self):
        r"""Gets the host_name of this PortHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this PortHostResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this PortHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this PortHostResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def laddr(self):
        r"""Gets the laddr of this PortHostResponseInfo.

        **参数解释**: 端口的监听IP地址（0.0.0.0表示监听所有网卡） **取值范围**: 支持IPv4或IPv6格式，IPv4长度7-15位，IPv6长度15-39位 

        :return: The laddr of this PortHostResponseInfo.
        :rtype: str
        """
        return self._laddr

    @laddr.setter
    def laddr(self, laddr):
        r"""Sets the laddr of this PortHostResponseInfo.

        **参数解释**: 端口的监听IP地址（0.0.0.0表示监听所有网卡） **取值范围**: 支持IPv4或IPv6格式，IPv4长度7-15位，IPv6长度15-39位 

        :param laddr: The laddr of this PortHostResponseInfo.
        :type laddr: str
        """
        self._laddr = laddr

    @property
    def path(self):
        r"""Gets the path of this PortHostResponseInfo.

        **参数解释**: 占用当前端口的进程对应的可执行文件绝对路径 **取值范围**: 字符长度0-512位 

        :return: The path of this PortHostResponseInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this PortHostResponseInfo.

        **参数解释**: 占用当前端口的进程对应的可执行文件绝对路径 **取值范围**: 字符长度0-512位 

        :param path: The path of this PortHostResponseInfo.
        :type path: str
        """
        self._path = path

    @property
    def pid(self):
        r"""Gets the pid of this PortHostResponseInfo.

        **参数解释**: 占用当前端口的进程ID **取值范围**: 非负整数，最小值0（无对应进程时为0）；单位：个 

        :return: The pid of this PortHostResponseInfo.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this PortHostResponseInfo.

        **参数解释**: 占用当前端口的进程ID **取值范围**: 非负整数，最小值0（无对应进程时为0）；单位：个 

        :param pid: The pid of this PortHostResponseInfo.
        :type pid: int
        """
        self._pid = pid

    @property
    def port(self):
        r"""Gets the port of this PortHostResponseInfo.

        **参数解释**: 端口的具体编号 **取值范围**: 1-65535（TCP/UDP标准端口范围） 

        :return: The port of this PortHostResponseInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this PortHostResponseInfo.

        **参数解释**: 端口的具体编号 **取值范围**: 1-65535（TCP/UDP标准端口范围） 

        :param port: The port of this PortHostResponseInfo.
        :type port: int
        """
        self._port = port

    @property
    def status(self):
        r"""Gets the status of this PortHostResponseInfo.

        状态

        :return: The status of this PortHostResponseInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PortHostResponseInfo.

        状态

        :param status: The status of this PortHostResponseInfo.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this PortHostResponseInfo.

        **参数解释**: 端口类型 **取值范围**: 目前包括TCP，UDP两种 

        :return: The type of this PortHostResponseInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PortHostResponseInfo.

        **参数解释**: 端口类型 **取值范围**: 目前包括TCP，UDP两种 

        :param type: The type of this PortHostResponseInfo.
        :type type: str
        """
        self._type = type

    @property
    def container_name(self):
        r"""Gets the container_name of this PortHostResponseInfo.

        **参数解释**： 容器实例名称，只有容器类型的告警有 **取值范围**： 字符长度1-256位 

        :return: The container_name of this PortHostResponseInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this PortHostResponseInfo.

        **参数解释**： 容器实例名称，只有容器类型的告警有 **取值范围**： 字符长度1-256位 

        :param container_name: The container_name of this PortHostResponseInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def agent_id(self):
        r"""Gets the agent_id of this PortHostResponseInfo.

        **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The agent_id of this PortHostResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this PortHostResponseInfo.

        **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param agent_id: The agent_id of this PortHostResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PortHostResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
