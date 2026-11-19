# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDefenderPluginsResponseBodyData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_version': 'str',
        'instance_port': 'int',
        'agent_app_type': 'str',
        'agent_runtime_env': 'str',
        'cluster_id': 'str',
        'cluster_type': 'str',
        'cluster_name': 'str',
        'host_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'host_status': 'str',
        'host_id': 'str',
        'os_type': 'str',
        'os_name': 'str',
        'os_version': 'str',
        'kernel_version': 'str',
        'agent_status': 'str',
        'defender_status': 'str',
        'failed_reason': 'str',
        'container_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'instance_version': 'instance_version',
        'instance_port': 'instance_port',
        'agent_app_type': 'agent_app_type',
        'agent_runtime_env': 'agent_runtime_env',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'cluster_name': 'cluster_name',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'host_status': 'host_status',
        'host_id': 'host_id',
        'os_type': 'os_type',
        'os_name': 'os_name',
        'os_version': 'os_version',
        'kernel_version': 'kernel_version',
        'agent_status': 'agent_status',
        'defender_status': 'defender_status',
        'failed_reason': 'failed_reason',
        'container_id': 'container_id'
    }

    def __init__(self, instance_id=None, instance_name=None, instance_version=None, instance_port=None, agent_app_type=None, agent_runtime_env=None, cluster_id=None, cluster_type=None, cluster_name=None, host_name=None, public_ip=None, private_ip=None, host_status=None, host_id=None, os_type=None, os_name=None, os_version=None, kernel_version=None, agent_status=None, defender_status=None, failed_reason=None, container_id=None):
        r"""ListDefenderPluginsResponseBodyData

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**： 实例ID **取值范围**： 字符长度为1-128位 
        :type instance_id: str
        :param instance_name: **参数解释**： 实例名称，即智能体应用名称 **取值范围**： 字符长度为1-128位 
        :type instance_name: str
        :param instance_version: **参数解释**： 实例版本号，即智能体应用版本号 **取值范围**： 字符长度为1-64位 
        :type instance_version: str
        :param instance_port: **参数解释**： 实例端口，即智能体应用监听端口 **取值范围**： 最小值0，最大值65535 
        :type instance_port: int
        :param agent_app_type: **参数解释**： 智能体应用类型 **取值范围**： - openclaw：OpenClaw 
        :type agent_app_type: str
        :param agent_runtime_env: **参数解释**： 智能体运行环境 **取值范围**： - ECS - CCE 
        :type agent_runtime_env: str
        :param cluster_id: **参数解释**： 集群ID，仅agent_runtime_env为CCE时返回 **取值范围**： 字符长度为1-128位 
        :type cluster_id: str
        :param cluster_type: **参数解释**： 集群类型 **取值范围**： - CCE：云容器引擎 
        :type cluster_type: str
        :param cluster_name: **参数解释**： 集群名称，仅agent_runtime_env为CCE时返回 **取值范围**： 字符长度为1-256位 
        :type cluster_name: str
        :param host_name: **参数解释**： 服务器名称 **取值范围**： 字符长度为1-256位 
        :type host_name: str
        :param public_ip: **参数解释**： 服务器公网IP地址 **取值范围**： 字符长度为1-128位 
        :type public_ip: str
        :param private_ip: **参数解释**： 服务器私有IP地址 **取值范围**： 字符长度为1-128位 
        :type private_ip: str
        :param host_status: **参数解释**： 服务器状态 **取值范围**： - ACTIVE：运行中 - SHUTOFF：已关机 - BUILD：创建中 - ERROR：异常 - DELETED：已删除 - REBOOT：重启中 
        :type host_status: str
        :param host_id: **参数解释**： 服务器ID **取值范围**： 字符长度为1-128位 
        :type host_id: str
        :param os_type: **参数解释**： 操作系统类型 **取值范围**： - Linux - Windows 
        :type os_type: str
        :param os_name: **参数解释**： 操作系统名称 **取值范围**： - EulerOS 2.9 - CentOS 7.9 - Ubuntu 20.04 - 其他操作系统名称 
        :type os_name: str
        :param os_version: **参数解释**： 操作系统版本号 **取值范围**： 字符长度为1-64位 
        :type os_version: str
        :param kernel_version: **参数解释**： 操作系统内核版本号 **取值范围**： 字符长度为1-128位 
        :type kernel_version: str
        :param agent_status: **参数解释**： Agent状态 **取值范围**： - online：在线 - offline：离线 - not_installed：未安装 - install_failed：安装失败 - installing：安装中 
        :type agent_status: str
        :param defender_status: **参数解释**： 智能体卫士插件状态 **取值范围**： - not_installed：未安装 - install_failed：安装失败 - online：在线 - offline：离线 - installing：安装中 
        :type defender_status: str
        :param failed_reason: **参数解释**： 安装或卸载失败原因，仅defender_status为install_failed时返回 **取值范围**： 字符长度为0-1024位 
        :type failed_reason: str
        :param container_id: **参数解释**： 容器实例ID **取值范围**： 字符长度0-128位 
        :type container_id: str
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._instance_version = None
        self._instance_port = None
        self._agent_app_type = None
        self._agent_runtime_env = None
        self._cluster_id = None
        self._cluster_type = None
        self._cluster_name = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._host_status = None
        self._host_id = None
        self._os_type = None
        self._os_name = None
        self._os_version = None
        self._kernel_version = None
        self._agent_status = None
        self._defender_status = None
        self._failed_reason = None
        self._container_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_version is not None:
            self.instance_version = instance_version
        if instance_port is not None:
            self.instance_port = instance_port
        if agent_app_type is not None:
            self.agent_app_type = agent_app_type
        if agent_runtime_env is not None:
            self.agent_runtime_env = agent_runtime_env
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if host_status is not None:
            self.host_status = host_status
        if host_id is not None:
            self.host_id = host_id
        if os_type is not None:
            self.os_type = os_type
        if os_name is not None:
            self.os_name = os_name
        if os_version is not None:
            self.os_version = os_version
        if kernel_version is not None:
            self.kernel_version = kernel_version
        if agent_status is not None:
            self.agent_status = agent_status
        if defender_status is not None:
            self.defender_status = defender_status
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if container_id is not None:
            self.container_id = container_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 实例ID **取值范围**： 字符长度为1-128位 

        :return: The instance_id of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 实例ID **取值范围**： 字符长度为1-128位 

        :param instance_id: The instance_id of this ListDefenderPluginsResponseBodyData.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 实例名称，即智能体应用名称 **取值范围**： 字符长度为1-128位 

        :return: The instance_name of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 实例名称，即智能体应用名称 **取值范围**： 字符长度为1-128位 

        :param instance_name: The instance_name of this ListDefenderPluginsResponseBodyData.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_version(self):
        r"""Gets the instance_version of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 实例版本号，即智能体应用版本号 **取值范围**： 字符长度为1-64位 

        :return: The instance_version of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._instance_version

    @instance_version.setter
    def instance_version(self, instance_version):
        r"""Sets the instance_version of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 实例版本号，即智能体应用版本号 **取值范围**： 字符长度为1-64位 

        :param instance_version: The instance_version of this ListDefenderPluginsResponseBodyData.
        :type instance_version: str
        """
        self._instance_version = instance_version

    @property
    def instance_port(self):
        r"""Gets the instance_port of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 实例端口，即智能体应用监听端口 **取值范围**： 最小值0，最大值65535 

        :return: The instance_port of this ListDefenderPluginsResponseBodyData.
        :rtype: int
        """
        return self._instance_port

    @instance_port.setter
    def instance_port(self, instance_port):
        r"""Sets the instance_port of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 实例端口，即智能体应用监听端口 **取值范围**： 最小值0，最大值65535 

        :param instance_port: The instance_port of this ListDefenderPluginsResponseBodyData.
        :type instance_port: int
        """
        self._instance_port = instance_port

    @property
    def agent_app_type(self):
        r"""Gets the agent_app_type of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 智能体应用类型 **取值范围**： - openclaw：OpenClaw 

        :return: The agent_app_type of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._agent_app_type

    @agent_app_type.setter
    def agent_app_type(self, agent_app_type):
        r"""Sets the agent_app_type of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 智能体应用类型 **取值范围**： - openclaw：OpenClaw 

        :param agent_app_type: The agent_app_type of this ListDefenderPluginsResponseBodyData.
        :type agent_app_type: str
        """
        self._agent_app_type = agent_app_type

    @property
    def agent_runtime_env(self):
        r"""Gets the agent_runtime_env of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 智能体运行环境 **取值范围**： - ECS - CCE 

        :return: The agent_runtime_env of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._agent_runtime_env

    @agent_runtime_env.setter
    def agent_runtime_env(self, agent_runtime_env):
        r"""Sets the agent_runtime_env of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 智能体运行环境 **取值范围**： - ECS - CCE 

        :param agent_runtime_env: The agent_runtime_env of this ListDefenderPluginsResponseBodyData.
        :type agent_runtime_env: str
        """
        self._agent_runtime_env = agent_runtime_env

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 集群ID，仅agent_runtime_env为CCE时返回 **取值范围**： 字符长度为1-128位 

        :return: The cluster_id of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 集群ID，仅agent_runtime_env为CCE时返回 **取值范围**： 字符长度为1-128位 

        :param cluster_id: The cluster_id of this ListDefenderPluginsResponseBodyData.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 集群类型 **取值范围**： - CCE：云容器引擎 

        :return: The cluster_type of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 集群类型 **取值范围**： - CCE：云容器引擎 

        :param cluster_type: The cluster_type of this ListDefenderPluginsResponseBodyData.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 集群名称，仅agent_runtime_env为CCE时返回 **取值范围**： 字符长度为1-256位 

        :return: The cluster_name of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 集群名称，仅agent_runtime_env为CCE时返回 **取值范围**： 字符长度为1-256位 

        :param cluster_name: The cluster_name of this ListDefenderPluginsResponseBodyData.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def host_name(self):
        r"""Gets the host_name of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 服务器名称 **取值范围**： 字符长度为1-256位 

        :return: The host_name of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 服务器名称 **取值范围**： 字符长度为1-256位 

        :param host_name: The host_name of this ListDefenderPluginsResponseBodyData.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 服务器公网IP地址 **取值范围**： 字符长度为1-128位 

        :return: The public_ip of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 服务器公网IP地址 **取值范围**： 字符长度为1-128位 

        :param public_ip: The public_ip of this ListDefenderPluginsResponseBodyData.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 服务器私有IP地址 **取值范围**： 字符长度为1-128位 

        :return: The private_ip of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 服务器私有IP地址 **取值范围**： 字符长度为1-128位 

        :param private_ip: The private_ip of this ListDefenderPluginsResponseBodyData.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def host_status(self):
        r"""Gets the host_status of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 服务器状态 **取值范围**： - ACTIVE：运行中 - SHUTOFF：已关机 - BUILD：创建中 - ERROR：异常 - DELETED：已删除 - REBOOT：重启中 

        :return: The host_status of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 服务器状态 **取值范围**： - ACTIVE：运行中 - SHUTOFF：已关机 - BUILD：创建中 - ERROR：异常 - DELETED：已删除 - REBOOT：重启中 

        :param host_status: The host_status of this ListDefenderPluginsResponseBodyData.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def host_id(self):
        r"""Gets the host_id of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 服务器ID **取值范围**： 字符长度为1-128位 

        :return: The host_id of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 服务器ID **取值范围**： 字符长度为1-128位 

        :param host_id: The host_id of this ListDefenderPluginsResponseBodyData.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def os_type(self):
        r"""Gets the os_type of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 操作系统类型 **取值范围**： - Linux - Windows 

        :return: The os_type of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 操作系统类型 **取值范围**： - Linux - Windows 

        :param os_type: The os_type of this ListDefenderPluginsResponseBodyData.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_name(self):
        r"""Gets the os_name of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 操作系统名称 **取值范围**： - EulerOS 2.9 - CentOS 7.9 - Ubuntu 20.04 - 其他操作系统名称 

        :return: The os_name of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 操作系统名称 **取值范围**： - EulerOS 2.9 - CentOS 7.9 - Ubuntu 20.04 - 其他操作系统名称 

        :param os_name: The os_name of this ListDefenderPluginsResponseBodyData.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_version(self):
        r"""Gets the os_version of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 操作系统版本号 **取值范围**： 字符长度为1-64位 

        :return: The os_version of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 操作系统版本号 **取值范围**： 字符长度为1-64位 

        :param os_version: The os_version of this ListDefenderPluginsResponseBodyData.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def kernel_version(self):
        r"""Gets the kernel_version of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 操作系统内核版本号 **取值范围**： 字符长度为1-128位 

        :return: The kernel_version of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        r"""Sets the kernel_version of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 操作系统内核版本号 **取值范围**： 字符长度为1-128位 

        :param kernel_version: The kernel_version of this ListDefenderPluginsResponseBodyData.
        :type kernel_version: str
        """
        self._kernel_version = kernel_version

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ListDefenderPluginsResponseBodyData.

        **参数解释**： Agent状态 **取值范围**： - online：在线 - offline：离线 - not_installed：未安装 - install_failed：安装失败 - installing：安装中 

        :return: The agent_status of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ListDefenderPluginsResponseBodyData.

        **参数解释**： Agent状态 **取值范围**： - online：在线 - offline：离线 - not_installed：未安装 - install_failed：安装失败 - installing：安装中 

        :param agent_status: The agent_status of this ListDefenderPluginsResponseBodyData.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def defender_status(self):
        r"""Gets the defender_status of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 智能体卫士插件状态 **取值范围**： - not_installed：未安装 - install_failed：安装失败 - online：在线 - offline：离线 - installing：安装中 

        :return: The defender_status of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._defender_status

    @defender_status.setter
    def defender_status(self, defender_status):
        r"""Sets the defender_status of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 智能体卫士插件状态 **取值范围**： - not_installed：未安装 - install_failed：安装失败 - online：在线 - offline：离线 - installing：安装中 

        :param defender_status: The defender_status of this ListDefenderPluginsResponseBodyData.
        :type defender_status: str
        """
        self._defender_status = defender_status

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 安装或卸载失败原因，仅defender_status为install_failed时返回 **取值范围**： 字符长度为0-1024位 

        :return: The failed_reason of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 安装或卸载失败原因，仅defender_status为install_failed时返回 **取值范围**： 字符长度为0-1024位 

        :param failed_reason: The failed_reason of this ListDefenderPluginsResponseBodyData.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def container_id(self):
        r"""Gets the container_id of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 容器实例ID **取值范围**： 字符长度0-128位 

        :return: The container_id of this ListDefenderPluginsResponseBodyData.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ListDefenderPluginsResponseBodyData.

        **参数解释**： 容器实例ID **取值范围**： 字符长度0-128位 

        :param container_id: The container_id of this ListDefenderPluginsResponseBodyData.
        :type container_id: str
        """
        self._container_id = container_id

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
        if not isinstance(other, ListDefenderPluginsResponseBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
