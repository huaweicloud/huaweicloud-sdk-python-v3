# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Vag:

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
        'project_id': 'str',
        'site_id': 'str',
        'vag_ip': 'str',
        'private_ip': 'str',
        'private_ipv6': 'str',
        'vag_port_id': 'str',
        'ssh_user': 'str',
        'ssh_pwd': 'str',
        'vm_id': 'str',
        'name': 'str',
        'internal_ip': 'str',
        'internal_ipv6': 'str',
        'internal_port_id': 'str',
        'external_ip': 'str',
        'external_id': 'str',
        'root_user': 'str',
        'root_pwd': 'str',
        'status': 'str',
        'availability_zone': 'str',
        'create_time': 'int',
        'create_time_str': 'str',
        'state': 'str',
        'number_of_online_user': 'int',
        'running_status': 'str',
        'domain_id': 'str',
        'version': 'str',
        'latest_version': 'str',
        'access_edge_version': 'str',
        'tenant_lock': 'int',
        'resource_pool_id': 'str',
        'role': 'str',
        'resource_pool_type': 'str',
        'edge_sk': 'str',
        'has_heartbeat': 'bool',
        'user_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'site_id': 'site_id',
        'vag_ip': 'vag_ip',
        'private_ip': 'private_ip',
        'private_ipv6': 'private_ipv6',
        'vag_port_id': 'vag_port_id',
        'ssh_user': 'ssh_user',
        'ssh_pwd': 'ssh_pwd',
        'vm_id': 'vm_id',
        'name': 'name',
        'internal_ip': 'internal_ip',
        'internal_ipv6': 'internal_ipv6',
        'internal_port_id': 'internal_port_id',
        'external_ip': 'external_ip',
        'external_id': 'external_id',
        'root_user': 'root_user',
        'root_pwd': 'root_pwd',
        'status': 'status',
        'availability_zone': 'availability_zone',
        'create_time': 'create_time',
        'create_time_str': 'create_time_str',
        'state': 'state',
        'number_of_online_user': 'number_of_online_user',
        'running_status': 'running_status',
        'domain_id': 'domain_id',
        'version': 'version',
        'latest_version': 'latest_version',
        'access_edge_version': 'access_edge_version',
        'tenant_lock': 'tenant_lock',
        'resource_pool_id': 'resource_pool_id',
        'role': 'role',
        'resource_pool_type': 'resource_pool_type',
        'edge_sk': 'edge_sk',
        'has_heartbeat': 'has_heartbeat',
        'user_count': 'user_count'
    }

    def __init__(self, id=None, project_id=None, site_id=None, vag_ip=None, private_ip=None, private_ipv6=None, vag_port_id=None, ssh_user=None, ssh_pwd=None, vm_id=None, name=None, internal_ip=None, internal_ipv6=None, internal_port_id=None, external_ip=None, external_id=None, root_user=None, root_pwd=None, status=None, availability_zone=None, create_time=None, create_time_str=None, state=None, number_of_online_user=None, running_status=None, domain_id=None, version=None, latest_version=None, access_edge_version=None, tenant_lock=None, resource_pool_id=None, role=None, resource_pool_type=None, edge_sk=None, has_heartbeat=None, user_count=None):
        """Vag

        The model defined in huaweicloud sdk

        :param id: vAG信息ID
        :type id: str
        :param project_id: 项目ID
        :type project_id: str
        :param site_id: 站点ID
        :type site_id: str
        :param vag_ip: vAG IP，与管理节点相同的IP
        :type vag_ip: str
        :param private_ip: vAG内网IP，HDA往这个IP上报心跳
        :type private_ip: str
        :param private_ipv6: vAG内网IPv6
        :type private_ipv6: str
        :param vag_port_id: vAG端口ID，与管理节点相同的端口的ID
        :type vag_port_id: str
        :param ssh_user: SSH用户的名称，固定为gandalf
        :type ssh_user: str
        :param ssh_pwd: SSH用户的密码
        :type ssh_pwd: str
        :param vm_id: vAG所属ECS的ID
        :type vm_id: str
        :param name: vAG所属机器名
        :type name: str
        :param internal_ip: vAG内部通信IP，最终租户VPC的子网IP
        :type internal_ip: str
        :param internal_ipv6: vAG内部通信IPV6
        :type internal_ipv6: str
        :param internal_port_id: vAG内部通信端口ID，最终租户VPC的子网中端口的ID
        :type internal_port_id: str
        :param external_ip: 外部通信IP，可能独立的EIP
        :type external_ip: str
        :param external_id: 外部通信ID，可能独立的EIP ID
        :type external_id: str
        :param root_user: root用户的名称，固定为root
        :type root_user: str
        :param root_pwd: root用户的密码
        :type root_pwd: str
        :param status: vag操作状态
        :type status: str
        :param availability_zone: 可用分区
        :type availability_zone: str
        :param create_time: 创建时间
        :type create_time: int
        :param create_time_str: 创建时间字符串
        :type create_time_str: str
        :param state: vag服务状态 NOT_USE：维护，ON_USE：启用，CANCELLATION：退服
        :type state: str
        :param number_of_online_user: 在线用户数
        :type number_of_online_user: int
        :param running_status: vag运行状态
        :type running_status: str
        :param domain_id: 租户侧domainId
        :type domain_id: str
        :param version: vag当前版本号
        :type version: str
        :param latest_version: vag最新版本号。
        :type latest_version: str
        :param access_edge_version: wksAccessEdge版本号
        :type access_edge_version: str
        :param tenant_lock: 项目是否被锁定 0是未锁定 1是锁定
        :type tenant_lock: int
        :param resource_pool_id: 资源池id
        :type resource_pool_id: str
        :param role: agent角色，如：vag,vap4down,vap4up,authConnector
        :type role: str
        :param resource_pool_type: 资源池类型，public,private
        :type resource_pool_type: str
        :param edge_sk: 边缘sk
        :type edge_sk: str
        :param has_heartbeat: 是否有心跳
        :type has_heartbeat: bool
        :param user_count: VAG负载个数
        :type user_count: int
        """
        
        

        self._id = None
        self._project_id = None
        self._site_id = None
        self._vag_ip = None
        self._private_ip = None
        self._private_ipv6 = None
        self._vag_port_id = None
        self._ssh_user = None
        self._ssh_pwd = None
        self._vm_id = None
        self._name = None
        self._internal_ip = None
        self._internal_ipv6 = None
        self._internal_port_id = None
        self._external_ip = None
        self._external_id = None
        self._root_user = None
        self._root_pwd = None
        self._status = None
        self._availability_zone = None
        self._create_time = None
        self._create_time_str = None
        self._state = None
        self._number_of_online_user = None
        self._running_status = None
        self._domain_id = None
        self._version = None
        self._latest_version = None
        self._access_edge_version = None
        self._tenant_lock = None
        self._resource_pool_id = None
        self._role = None
        self._resource_pool_type = None
        self._edge_sk = None
        self._has_heartbeat = None
        self._user_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if site_id is not None:
            self.site_id = site_id
        if vag_ip is not None:
            self.vag_ip = vag_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if private_ipv6 is not None:
            self.private_ipv6 = private_ipv6
        if vag_port_id is not None:
            self.vag_port_id = vag_port_id
        if ssh_user is not None:
            self.ssh_user = ssh_user
        if ssh_pwd is not None:
            self.ssh_pwd = ssh_pwd
        if vm_id is not None:
            self.vm_id = vm_id
        if name is not None:
            self.name = name
        if internal_ip is not None:
            self.internal_ip = internal_ip
        if internal_ipv6 is not None:
            self.internal_ipv6 = internal_ipv6
        if internal_port_id is not None:
            self.internal_port_id = internal_port_id
        if external_ip is not None:
            self.external_ip = external_ip
        if external_id is not None:
            self.external_id = external_id
        if root_user is not None:
            self.root_user = root_user
        if root_pwd is not None:
            self.root_pwd = root_pwd
        if status is not None:
            self.status = status
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if create_time is not None:
            self.create_time = create_time
        if create_time_str is not None:
            self.create_time_str = create_time_str
        if state is not None:
            self.state = state
        if number_of_online_user is not None:
            self.number_of_online_user = number_of_online_user
        if running_status is not None:
            self.running_status = running_status
        if domain_id is not None:
            self.domain_id = domain_id
        if version is not None:
            self.version = version
        if latest_version is not None:
            self.latest_version = latest_version
        if access_edge_version is not None:
            self.access_edge_version = access_edge_version
        if tenant_lock is not None:
            self.tenant_lock = tenant_lock
        if resource_pool_id is not None:
            self.resource_pool_id = resource_pool_id
        if role is not None:
            self.role = role
        if resource_pool_type is not None:
            self.resource_pool_type = resource_pool_type
        if edge_sk is not None:
            self.edge_sk = edge_sk
        if has_heartbeat is not None:
            self.has_heartbeat = has_heartbeat
        if user_count is not None:
            self.user_count = user_count

    @property
    def id(self):
        """Gets the id of this Vag.

        vAG信息ID

        :return: The id of this Vag.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Vag.

        vAG信息ID

        :param id: The id of this Vag.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this Vag.

        项目ID

        :return: The project_id of this Vag.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Vag.

        项目ID

        :param project_id: The project_id of this Vag.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def site_id(self):
        """Gets the site_id of this Vag.

        站点ID

        :return: The site_id of this Vag.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this Vag.

        站点ID

        :param site_id: The site_id of this Vag.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def vag_ip(self):
        """Gets the vag_ip of this Vag.

        vAG IP，与管理节点相同的IP

        :return: The vag_ip of this Vag.
        :rtype: str
        """
        return self._vag_ip

    @vag_ip.setter
    def vag_ip(self, vag_ip):
        """Sets the vag_ip of this Vag.

        vAG IP，与管理节点相同的IP

        :param vag_ip: The vag_ip of this Vag.
        :type vag_ip: str
        """
        self._vag_ip = vag_ip

    @property
    def private_ip(self):
        """Gets the private_ip of this Vag.

        vAG内网IP，HDA往这个IP上报心跳

        :return: The private_ip of this Vag.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this Vag.

        vAG内网IP，HDA往这个IP上报心跳

        :param private_ip: The private_ip of this Vag.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def private_ipv6(self):
        """Gets the private_ipv6 of this Vag.

        vAG内网IPv6

        :return: The private_ipv6 of this Vag.
        :rtype: str
        """
        return self._private_ipv6

    @private_ipv6.setter
    def private_ipv6(self, private_ipv6):
        """Sets the private_ipv6 of this Vag.

        vAG内网IPv6

        :param private_ipv6: The private_ipv6 of this Vag.
        :type private_ipv6: str
        """
        self._private_ipv6 = private_ipv6

    @property
    def vag_port_id(self):
        """Gets the vag_port_id of this Vag.

        vAG端口ID，与管理节点相同的端口的ID

        :return: The vag_port_id of this Vag.
        :rtype: str
        """
        return self._vag_port_id

    @vag_port_id.setter
    def vag_port_id(self, vag_port_id):
        """Sets the vag_port_id of this Vag.

        vAG端口ID，与管理节点相同的端口的ID

        :param vag_port_id: The vag_port_id of this Vag.
        :type vag_port_id: str
        """
        self._vag_port_id = vag_port_id

    @property
    def ssh_user(self):
        """Gets the ssh_user of this Vag.

        SSH用户的名称，固定为gandalf

        :return: The ssh_user of this Vag.
        :rtype: str
        """
        return self._ssh_user

    @ssh_user.setter
    def ssh_user(self, ssh_user):
        """Sets the ssh_user of this Vag.

        SSH用户的名称，固定为gandalf

        :param ssh_user: The ssh_user of this Vag.
        :type ssh_user: str
        """
        self._ssh_user = ssh_user

    @property
    def ssh_pwd(self):
        """Gets the ssh_pwd of this Vag.

        SSH用户的密码

        :return: The ssh_pwd of this Vag.
        :rtype: str
        """
        return self._ssh_pwd

    @ssh_pwd.setter
    def ssh_pwd(self, ssh_pwd):
        """Sets the ssh_pwd of this Vag.

        SSH用户的密码

        :param ssh_pwd: The ssh_pwd of this Vag.
        :type ssh_pwd: str
        """
        self._ssh_pwd = ssh_pwd

    @property
    def vm_id(self):
        """Gets the vm_id of this Vag.

        vAG所属ECS的ID

        :return: The vm_id of this Vag.
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this Vag.

        vAG所属ECS的ID

        :param vm_id: The vm_id of this Vag.
        :type vm_id: str
        """
        self._vm_id = vm_id

    @property
    def name(self):
        """Gets the name of this Vag.

        vAG所属机器名

        :return: The name of this Vag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Vag.

        vAG所属机器名

        :param name: The name of this Vag.
        :type name: str
        """
        self._name = name

    @property
    def internal_ip(self):
        """Gets the internal_ip of this Vag.

        vAG内部通信IP，最终租户VPC的子网IP

        :return: The internal_ip of this Vag.
        :rtype: str
        """
        return self._internal_ip

    @internal_ip.setter
    def internal_ip(self, internal_ip):
        """Sets the internal_ip of this Vag.

        vAG内部通信IP，最终租户VPC的子网IP

        :param internal_ip: The internal_ip of this Vag.
        :type internal_ip: str
        """
        self._internal_ip = internal_ip

    @property
    def internal_ipv6(self):
        """Gets the internal_ipv6 of this Vag.

        vAG内部通信IPV6

        :return: The internal_ipv6 of this Vag.
        :rtype: str
        """
        return self._internal_ipv6

    @internal_ipv6.setter
    def internal_ipv6(self, internal_ipv6):
        """Sets the internal_ipv6 of this Vag.

        vAG内部通信IPV6

        :param internal_ipv6: The internal_ipv6 of this Vag.
        :type internal_ipv6: str
        """
        self._internal_ipv6 = internal_ipv6

    @property
    def internal_port_id(self):
        """Gets the internal_port_id of this Vag.

        vAG内部通信端口ID，最终租户VPC的子网中端口的ID

        :return: The internal_port_id of this Vag.
        :rtype: str
        """
        return self._internal_port_id

    @internal_port_id.setter
    def internal_port_id(self, internal_port_id):
        """Sets the internal_port_id of this Vag.

        vAG内部通信端口ID，最终租户VPC的子网中端口的ID

        :param internal_port_id: The internal_port_id of this Vag.
        :type internal_port_id: str
        """
        self._internal_port_id = internal_port_id

    @property
    def external_ip(self):
        """Gets the external_ip of this Vag.

        外部通信IP，可能独立的EIP

        :return: The external_ip of this Vag.
        :rtype: str
        """
        return self._external_ip

    @external_ip.setter
    def external_ip(self, external_ip):
        """Sets the external_ip of this Vag.

        外部通信IP，可能独立的EIP

        :param external_ip: The external_ip of this Vag.
        :type external_ip: str
        """
        self._external_ip = external_ip

    @property
    def external_id(self):
        """Gets the external_id of this Vag.

        外部通信ID，可能独立的EIP ID

        :return: The external_id of this Vag.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Vag.

        外部通信ID，可能独立的EIP ID

        :param external_id: The external_id of this Vag.
        :type external_id: str
        """
        self._external_id = external_id

    @property
    def root_user(self):
        """Gets the root_user of this Vag.

        root用户的名称，固定为root

        :return: The root_user of this Vag.
        :rtype: str
        """
        return self._root_user

    @root_user.setter
    def root_user(self, root_user):
        """Sets the root_user of this Vag.

        root用户的名称，固定为root

        :param root_user: The root_user of this Vag.
        :type root_user: str
        """
        self._root_user = root_user

    @property
    def root_pwd(self):
        """Gets the root_pwd of this Vag.

        root用户的密码

        :return: The root_pwd of this Vag.
        :rtype: str
        """
        return self._root_pwd

    @root_pwd.setter
    def root_pwd(self, root_pwd):
        """Sets the root_pwd of this Vag.

        root用户的密码

        :param root_pwd: The root_pwd of this Vag.
        :type root_pwd: str
        """
        self._root_pwd = root_pwd

    @property
    def status(self):
        """Gets the status of this Vag.

        vag操作状态

        :return: The status of this Vag.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Vag.

        vag操作状态

        :param status: The status of this Vag.
        :type status: str
        """
        self._status = status

    @property
    def availability_zone(self):
        """Gets the availability_zone of this Vag.

        可用分区

        :return: The availability_zone of this Vag.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this Vag.

        可用分区

        :param availability_zone: The availability_zone of this Vag.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def create_time(self):
        """Gets the create_time of this Vag.

        创建时间

        :return: The create_time of this Vag.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Vag.

        创建时间

        :param create_time: The create_time of this Vag.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_time_str(self):
        """Gets the create_time_str of this Vag.

        创建时间字符串

        :return: The create_time_str of this Vag.
        :rtype: str
        """
        return self._create_time_str

    @create_time_str.setter
    def create_time_str(self, create_time_str):
        """Sets the create_time_str of this Vag.

        创建时间字符串

        :param create_time_str: The create_time_str of this Vag.
        :type create_time_str: str
        """
        self._create_time_str = create_time_str

    @property
    def state(self):
        """Gets the state of this Vag.

        vag服务状态 NOT_USE：维护，ON_USE：启用，CANCELLATION：退服

        :return: The state of this Vag.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Vag.

        vag服务状态 NOT_USE：维护，ON_USE：启用，CANCELLATION：退服

        :param state: The state of this Vag.
        :type state: str
        """
        self._state = state

    @property
    def number_of_online_user(self):
        """Gets the number_of_online_user of this Vag.

        在线用户数

        :return: The number_of_online_user of this Vag.
        :rtype: int
        """
        return self._number_of_online_user

    @number_of_online_user.setter
    def number_of_online_user(self, number_of_online_user):
        """Sets the number_of_online_user of this Vag.

        在线用户数

        :param number_of_online_user: The number_of_online_user of this Vag.
        :type number_of_online_user: int
        """
        self._number_of_online_user = number_of_online_user

    @property
    def running_status(self):
        """Gets the running_status of this Vag.

        vag运行状态

        :return: The running_status of this Vag.
        :rtype: str
        """
        return self._running_status

    @running_status.setter
    def running_status(self, running_status):
        """Sets the running_status of this Vag.

        vag运行状态

        :param running_status: The running_status of this Vag.
        :type running_status: str
        """
        self._running_status = running_status

    @property
    def domain_id(self):
        """Gets the domain_id of this Vag.

        租户侧domainId

        :return: The domain_id of this Vag.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this Vag.

        租户侧domainId

        :param domain_id: The domain_id of this Vag.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def version(self):
        """Gets the version of this Vag.

        vag当前版本号

        :return: The version of this Vag.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Vag.

        vag当前版本号

        :param version: The version of this Vag.
        :type version: str
        """
        self._version = version

    @property
    def latest_version(self):
        """Gets the latest_version of this Vag.

        vag最新版本号。

        :return: The latest_version of this Vag.
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this Vag.

        vag最新版本号。

        :param latest_version: The latest_version of this Vag.
        :type latest_version: str
        """
        self._latest_version = latest_version

    @property
    def access_edge_version(self):
        """Gets the access_edge_version of this Vag.

        wksAccessEdge版本号

        :return: The access_edge_version of this Vag.
        :rtype: str
        """
        return self._access_edge_version

    @access_edge_version.setter
    def access_edge_version(self, access_edge_version):
        """Sets the access_edge_version of this Vag.

        wksAccessEdge版本号

        :param access_edge_version: The access_edge_version of this Vag.
        :type access_edge_version: str
        """
        self._access_edge_version = access_edge_version

    @property
    def tenant_lock(self):
        """Gets the tenant_lock of this Vag.

        项目是否被锁定 0是未锁定 1是锁定

        :return: The tenant_lock of this Vag.
        :rtype: int
        """
        return self._tenant_lock

    @tenant_lock.setter
    def tenant_lock(self, tenant_lock):
        """Sets the tenant_lock of this Vag.

        项目是否被锁定 0是未锁定 1是锁定

        :param tenant_lock: The tenant_lock of this Vag.
        :type tenant_lock: int
        """
        self._tenant_lock = tenant_lock

    @property
    def resource_pool_id(self):
        """Gets the resource_pool_id of this Vag.

        资源池id

        :return: The resource_pool_id of this Vag.
        :rtype: str
        """
        return self._resource_pool_id

    @resource_pool_id.setter
    def resource_pool_id(self, resource_pool_id):
        """Sets the resource_pool_id of this Vag.

        资源池id

        :param resource_pool_id: The resource_pool_id of this Vag.
        :type resource_pool_id: str
        """
        self._resource_pool_id = resource_pool_id

    @property
    def role(self):
        """Gets the role of this Vag.

        agent角色，如：vag,vap4down,vap4up,authConnector

        :return: The role of this Vag.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Vag.

        agent角色，如：vag,vap4down,vap4up,authConnector

        :param role: The role of this Vag.
        :type role: str
        """
        self._role = role

    @property
    def resource_pool_type(self):
        """Gets the resource_pool_type of this Vag.

        资源池类型，public,private

        :return: The resource_pool_type of this Vag.
        :rtype: str
        """
        return self._resource_pool_type

    @resource_pool_type.setter
    def resource_pool_type(self, resource_pool_type):
        """Sets the resource_pool_type of this Vag.

        资源池类型，public,private

        :param resource_pool_type: The resource_pool_type of this Vag.
        :type resource_pool_type: str
        """
        self._resource_pool_type = resource_pool_type

    @property
    def edge_sk(self):
        """Gets the edge_sk of this Vag.

        边缘sk

        :return: The edge_sk of this Vag.
        :rtype: str
        """
        return self._edge_sk

    @edge_sk.setter
    def edge_sk(self, edge_sk):
        """Sets the edge_sk of this Vag.

        边缘sk

        :param edge_sk: The edge_sk of this Vag.
        :type edge_sk: str
        """
        self._edge_sk = edge_sk

    @property
    def has_heartbeat(self):
        """Gets the has_heartbeat of this Vag.

        是否有心跳

        :return: The has_heartbeat of this Vag.
        :rtype: bool
        """
        return self._has_heartbeat

    @has_heartbeat.setter
    def has_heartbeat(self, has_heartbeat):
        """Sets the has_heartbeat of this Vag.

        是否有心跳

        :param has_heartbeat: The has_heartbeat of this Vag.
        :type has_heartbeat: bool
        """
        self._has_heartbeat = has_heartbeat

    @property
    def user_count(self):
        """Gets the user_count of this Vag.

        VAG负载个数

        :return: The user_count of this Vag.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this Vag.

        VAG负载个数

        :param user_count: The user_count of this Vag.
        :type user_count: int
        """
        self._user_count = user_count

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
        if not isinstance(other, Vag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
