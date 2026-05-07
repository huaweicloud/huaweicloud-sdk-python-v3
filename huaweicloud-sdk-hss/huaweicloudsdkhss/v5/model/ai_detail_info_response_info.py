# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AIDetailInfoResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_name': 'str',
        'server_ip': 'str',
        'ai_application': 'str',
        'ai_tool': 'str',
        'type': 'str',
        'version': 'str',
        'startup_path': 'str',
        'startup_time': 'int',
        'install_path': 'str',
        'cmdline': 'str',
        'first_scan_time': 'int',
        'latest_scan_time': 'int',
        'container_name': 'str',
        'container_id': 'str',
        'host_id': 'str',
        'pid': 'int',
        'ppid': 'int',
        'user': 'str',
        'net_info': 'list[AIProcessNetInfo]'
    }

    attribute_map = {
        'server_name': 'server_name',
        'server_ip': 'server_ip',
        'ai_application': 'ai_application',
        'ai_tool': 'ai_tool',
        'type': 'type',
        'version': 'version',
        'startup_path': 'startup_path',
        'startup_time': 'startup_time',
        'install_path': 'install_path',
        'cmdline': 'cmdline',
        'first_scan_time': 'first_scan_time',
        'latest_scan_time': 'latest_scan_time',
        'container_name': 'container_name',
        'container_id': 'container_id',
        'host_id': 'host_id',
        'pid': 'pid',
        'ppid': 'ppid',
        'user': 'user',
        'net_info': 'net_info'
    }

    def __init__(self, server_name=None, server_ip=None, ai_application=None, ai_tool=None, type=None, version=None, startup_path=None, startup_time=None, install_path=None, cmdline=None, first_scan_time=None, latest_scan_time=None, container_name=None, container_id=None, host_id=None, pid=None, ppid=None, user=None, net_info=None):
        r"""AIDetailInfoResponseInfo

        The model defined in huaweicloud sdk

        :param server_name: **参数解释**： category&#x3D;&#x3D;host时 表示服务器名称 category&#x3D;&#x3D;container时 表示节点名称 category&#x3D;&#x3D;serverless时 表示实例名称 **取值范围**： 字符长度1-256位 
        :type server_name: str
        :param server_ip: **参数解释**： category&#x3D;&#x3D;host时 表示服务器IP地址 category&#x3D;&#x3D;container时 表示节点IP地址 category&#x3D;&#x3D;serverless时 表示实例IP地址        **取值范围**： 字符长度1-128位 
        :type server_ip: str
        :param ai_application: **参数解释**： AI应用名称 **取值范围**： 字符长度1-256位 
        :type ai_application: str
        :param ai_tool: **参数解释**： AI工具名称 **取值范围**： 字符长度1-256位 
        :type ai_tool: str
        :param type: **参数解释**： AI应用类型 **取值范围**： 字符长度1-256位 
        :type type: str
        :param version: **参数解释**： 版本号 **取值范围**： 字符长度1-64位 
        :type version: str
        :param startup_path: **参数解释**： 应用启动路径 **取值范围**： 字符长度1-512位 
        :type startup_path: str
        :param startup_time: **参数解释**： 应用启动时间 **取值范围**： 时间戳，毫秒级 
        :type startup_time: int
        :param install_path: **参数解释**： 安装路径 **取值范围**： 字符长度1-512位 
        :type install_path: str
        :param cmdline: **参数解释**： 应用启动命令行 **取值范围**： 字符长度1-512位 
        :type cmdline: str
        :param first_scan_time: **参数解释**： 首次扫描时间 **取值范围**： 时间戳，毫秒级 
        :type first_scan_time: int
        :param latest_scan_time: **参数解释**： 最近一次扫描时间 **取值范围**： 时间戳，毫秒级 
        :type latest_scan_time: int
        :param container_name: **参数解释**： 容器名称 **取值范围**： 字符长度1-256位 
        :type container_name: str
        :param container_id: **参数解释**： 容器ID **取值范围**： 字符长度1-128位 
        :type container_id: str
        :param host_id: **参数解释**： 服务器ID，查看服务器详情使用 **取值范围**： 字符长度1-128位 
        :type host_id: str
        :param pid: **参数解释**： 应用进程PID **取值范围**： 取值0-2147483647 
        :type pid: int
        :param ppid: **参数解释**： 应用进程的父进程PID **取值范围**： 取值0-2147483647 
        :type ppid: int
        :param user: **参数解释**： 应用运行用户 **取值范围**： 字符长度1-128位 
        :type user: str
        :param net_info: **参数解释**： 应用进程监听网络信息 
        :type net_info: list[:class:`huaweicloudsdkhss.v5.AIProcessNetInfo`]
        """
        
        

        self._server_name = None
        self._server_ip = None
        self._ai_application = None
        self._ai_tool = None
        self._type = None
        self._version = None
        self._startup_path = None
        self._startup_time = None
        self._install_path = None
        self._cmdline = None
        self._first_scan_time = None
        self._latest_scan_time = None
        self._container_name = None
        self._container_id = None
        self._host_id = None
        self._pid = None
        self._ppid = None
        self._user = None
        self._net_info = None
        self.discriminator = None

        if server_name is not None:
            self.server_name = server_name
        if server_ip is not None:
            self.server_ip = server_ip
        if ai_application is not None:
            self.ai_application = ai_application
        if ai_tool is not None:
            self.ai_tool = ai_tool
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if startup_path is not None:
            self.startup_path = startup_path
        if startup_time is not None:
            self.startup_time = startup_time
        if install_path is not None:
            self.install_path = install_path
        if cmdline is not None:
            self.cmdline = cmdline
        if first_scan_time is not None:
            self.first_scan_time = first_scan_time
        if latest_scan_time is not None:
            self.latest_scan_time = latest_scan_time
        if container_name is not None:
            self.container_name = container_name
        if container_id is not None:
            self.container_id = container_id
        if host_id is not None:
            self.host_id = host_id
        if pid is not None:
            self.pid = pid
        if ppid is not None:
            self.ppid = ppid
        if user is not None:
            self.user = user
        if net_info is not None:
            self.net_info = net_info

    @property
    def server_name(self):
        r"""Gets the server_name of this AIDetailInfoResponseInfo.

        **参数解释**： category==host时 表示服务器名称 category==container时 表示节点名称 category==serverless时 表示实例名称 **取值范围**： 字符长度1-256位 

        :return: The server_name of this AIDetailInfoResponseInfo.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        r"""Sets the server_name of this AIDetailInfoResponseInfo.

        **参数解释**： category==host时 表示服务器名称 category==container时 表示节点名称 category==serverless时 表示实例名称 **取值范围**： 字符长度1-256位 

        :param server_name: The server_name of this AIDetailInfoResponseInfo.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def server_ip(self):
        r"""Gets the server_ip of this AIDetailInfoResponseInfo.

        **参数解释**： category==host时 表示服务器IP地址 category==container时 表示节点IP地址 category==serverless时 表示实例IP地址        **取值范围**： 字符长度1-128位 

        :return: The server_ip of this AIDetailInfoResponseInfo.
        :rtype: str
        """
        return self._server_ip

    @server_ip.setter
    def server_ip(self, server_ip):
        r"""Sets the server_ip of this AIDetailInfoResponseInfo.

        **参数解释**： category==host时 表示服务器IP地址 category==container时 表示节点IP地址 category==serverless时 表示实例IP地址        **取值范围**： 字符长度1-128位 

        :param server_ip: The server_ip of this AIDetailInfoResponseInfo.
        :type server_ip: str
        """
        self._server_ip = server_ip

    @property
    def ai_application(self):
        r"""Gets the ai_application of this AIDetailInfoResponseInfo.

        **参数解释**： AI应用名称 **取值范围**： 字符长度1-256位 

        :return: The ai_application of this AIDetailInfoResponseInfo.
        :rtype: str
        """
        return self._ai_application

    @ai_application.setter
    def ai_application(self, ai_application):
        r"""Sets the ai_application of this AIDetailInfoResponseInfo.

        **参数解释**： AI应用名称 **取值范围**： 字符长度1-256位 

        :param ai_application: The ai_application of this AIDetailInfoResponseInfo.
        :type ai_application: str
        """
        self._ai_application = ai_application

    @property
    def ai_tool(self):
        r"""Gets the ai_tool of this AIDetailInfoResponseInfo.

        **参数解释**： AI工具名称 **取值范围**： 字符长度1-256位 

        :return: The ai_tool of this AIDetailInfoResponseInfo.
        :rtype: str
        """
        return self._ai_tool

    @ai_tool.setter
    def ai_tool(self, ai_tool):
        r"""Sets the ai_tool of this AIDetailInfoResponseInfo.

        **参数解释**： AI工具名称 **取值范围**： 字符长度1-256位 

        :param ai_tool: The ai_tool of this AIDetailInfoResponseInfo.
        :type ai_tool: str
        """
        self._ai_tool = ai_tool

    @property
    def type(self):
        r"""Gets the type of this AIDetailInfoResponseInfo.

        **参数解释**： AI应用类型 **取值范围**： 字符长度1-256位 

        :return: The type of this AIDetailInfoResponseInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AIDetailInfoResponseInfo.

        **参数解释**： AI应用类型 **取值范围**： 字符长度1-256位 

        :param type: The type of this AIDetailInfoResponseInfo.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this AIDetailInfoResponseInfo.

        **参数解释**： 版本号 **取值范围**： 字符长度1-64位 

        :return: The version of this AIDetailInfoResponseInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AIDetailInfoResponseInfo.

        **参数解释**： 版本号 **取值范围**： 字符长度1-64位 

        :param version: The version of this AIDetailInfoResponseInfo.
        :type version: str
        """
        self._version = version

    @property
    def startup_path(self):
        r"""Gets the startup_path of this AIDetailInfoResponseInfo.

        **参数解释**： 应用启动路径 **取值范围**： 字符长度1-512位 

        :return: The startup_path of this AIDetailInfoResponseInfo.
        :rtype: str
        """
        return self._startup_path

    @startup_path.setter
    def startup_path(self, startup_path):
        r"""Sets the startup_path of this AIDetailInfoResponseInfo.

        **参数解释**： 应用启动路径 **取值范围**： 字符长度1-512位 

        :param startup_path: The startup_path of this AIDetailInfoResponseInfo.
        :type startup_path: str
        """
        self._startup_path = startup_path

    @property
    def startup_time(self):
        r"""Gets the startup_time of this AIDetailInfoResponseInfo.

        **参数解释**： 应用启动时间 **取值范围**： 时间戳，毫秒级 

        :return: The startup_time of this AIDetailInfoResponseInfo.
        :rtype: int
        """
        return self._startup_time

    @startup_time.setter
    def startup_time(self, startup_time):
        r"""Sets the startup_time of this AIDetailInfoResponseInfo.

        **参数解释**： 应用启动时间 **取值范围**： 时间戳，毫秒级 

        :param startup_time: The startup_time of this AIDetailInfoResponseInfo.
        :type startup_time: int
        """
        self._startup_time = startup_time

    @property
    def install_path(self):
        r"""Gets the install_path of this AIDetailInfoResponseInfo.

        **参数解释**： 安装路径 **取值范围**： 字符长度1-512位 

        :return: The install_path of this AIDetailInfoResponseInfo.
        :rtype: str
        """
        return self._install_path

    @install_path.setter
    def install_path(self, install_path):
        r"""Sets the install_path of this AIDetailInfoResponseInfo.

        **参数解释**： 安装路径 **取值范围**： 字符长度1-512位 

        :param install_path: The install_path of this AIDetailInfoResponseInfo.
        :type install_path: str
        """
        self._install_path = install_path

    @property
    def cmdline(self):
        r"""Gets the cmdline of this AIDetailInfoResponseInfo.

        **参数解释**： 应用启动命令行 **取值范围**： 字符长度1-512位 

        :return: The cmdline of this AIDetailInfoResponseInfo.
        :rtype: str
        """
        return self._cmdline

    @cmdline.setter
    def cmdline(self, cmdline):
        r"""Sets the cmdline of this AIDetailInfoResponseInfo.

        **参数解释**： 应用启动命令行 **取值范围**： 字符长度1-512位 

        :param cmdline: The cmdline of this AIDetailInfoResponseInfo.
        :type cmdline: str
        """
        self._cmdline = cmdline

    @property
    def first_scan_time(self):
        r"""Gets the first_scan_time of this AIDetailInfoResponseInfo.

        **参数解释**： 首次扫描时间 **取值范围**： 时间戳，毫秒级 

        :return: The first_scan_time of this AIDetailInfoResponseInfo.
        :rtype: int
        """
        return self._first_scan_time

    @first_scan_time.setter
    def first_scan_time(self, first_scan_time):
        r"""Sets the first_scan_time of this AIDetailInfoResponseInfo.

        **参数解释**： 首次扫描时间 **取值范围**： 时间戳，毫秒级 

        :param first_scan_time: The first_scan_time of this AIDetailInfoResponseInfo.
        :type first_scan_time: int
        """
        self._first_scan_time = first_scan_time

    @property
    def latest_scan_time(self):
        r"""Gets the latest_scan_time of this AIDetailInfoResponseInfo.

        **参数解释**： 最近一次扫描时间 **取值范围**： 时间戳，毫秒级 

        :return: The latest_scan_time of this AIDetailInfoResponseInfo.
        :rtype: int
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        r"""Sets the latest_scan_time of this AIDetailInfoResponseInfo.

        **参数解释**： 最近一次扫描时间 **取值范围**： 时间戳，毫秒级 

        :param latest_scan_time: The latest_scan_time of this AIDetailInfoResponseInfo.
        :type latest_scan_time: int
        """
        self._latest_scan_time = latest_scan_time

    @property
    def container_name(self):
        r"""Gets the container_name of this AIDetailInfoResponseInfo.

        **参数解释**： 容器名称 **取值范围**： 字符长度1-256位 

        :return: The container_name of this AIDetailInfoResponseInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this AIDetailInfoResponseInfo.

        **参数解释**： 容器名称 **取值范围**： 字符长度1-256位 

        :param container_name: The container_name of this AIDetailInfoResponseInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def container_id(self):
        r"""Gets the container_id of this AIDetailInfoResponseInfo.

        **参数解释**： 容器ID **取值范围**： 字符长度1-128位 

        :return: The container_id of this AIDetailInfoResponseInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this AIDetailInfoResponseInfo.

        **参数解释**： 容器ID **取值范围**： 字符长度1-128位 

        :param container_id: The container_id of this AIDetailInfoResponseInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def host_id(self):
        r"""Gets the host_id of this AIDetailInfoResponseInfo.

        **参数解释**： 服务器ID，查看服务器详情使用 **取值范围**： 字符长度1-128位 

        :return: The host_id of this AIDetailInfoResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this AIDetailInfoResponseInfo.

        **参数解释**： 服务器ID，查看服务器详情使用 **取值范围**： 字符长度1-128位 

        :param host_id: The host_id of this AIDetailInfoResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def pid(self):
        r"""Gets the pid of this AIDetailInfoResponseInfo.

        **参数解释**： 应用进程PID **取值范围**： 取值0-2147483647 

        :return: The pid of this AIDetailInfoResponseInfo.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this AIDetailInfoResponseInfo.

        **参数解释**： 应用进程PID **取值范围**： 取值0-2147483647 

        :param pid: The pid of this AIDetailInfoResponseInfo.
        :type pid: int
        """
        self._pid = pid

    @property
    def ppid(self):
        r"""Gets the ppid of this AIDetailInfoResponseInfo.

        **参数解释**： 应用进程的父进程PID **取值范围**： 取值0-2147483647 

        :return: The ppid of this AIDetailInfoResponseInfo.
        :rtype: int
        """
        return self._ppid

    @ppid.setter
    def ppid(self, ppid):
        r"""Sets the ppid of this AIDetailInfoResponseInfo.

        **参数解释**： 应用进程的父进程PID **取值范围**： 取值0-2147483647 

        :param ppid: The ppid of this AIDetailInfoResponseInfo.
        :type ppid: int
        """
        self._ppid = ppid

    @property
    def user(self):
        r"""Gets the user of this AIDetailInfoResponseInfo.

        **参数解释**： 应用运行用户 **取值范围**： 字符长度1-128位 

        :return: The user of this AIDetailInfoResponseInfo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this AIDetailInfoResponseInfo.

        **参数解释**： 应用运行用户 **取值范围**： 字符长度1-128位 

        :param user: The user of this AIDetailInfoResponseInfo.
        :type user: str
        """
        self._user = user

    @property
    def net_info(self):
        r"""Gets the net_info of this AIDetailInfoResponseInfo.

        **参数解释**： 应用进程监听网络信息 

        :return: The net_info of this AIDetailInfoResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AIProcessNetInfo`]
        """
        return self._net_info

    @net_info.setter
    def net_info(self, net_info):
        r"""Sets the net_info of this AIDetailInfoResponseInfo.

        **参数解释**： 应用进程监听网络信息 

        :param net_info: The net_info of this AIDetailInfoResponseInfo.
        :type net_info: list[:class:`huaweicloudsdkhss.v5.AIProcessNetInfo`]
        """
        self._net_info = net_info

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
        if not isinstance(other, AIDetailInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
