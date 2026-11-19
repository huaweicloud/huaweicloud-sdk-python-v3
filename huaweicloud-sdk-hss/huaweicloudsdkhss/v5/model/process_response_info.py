# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessResponseInfo:

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
        'host_id': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'process_path': 'str',
        'launch_params': 'str',
        'launch_time': 'int',
        'user_name': 'str',
        'run_permission': 'str',
        'process_pid': 'int',
        'parent_process_pid': 'int',
        'parent_process_name': 'str',
        'hash': 'str',
        'container_id': 'str',
        'container_name': 'str',
        'pod_id': 'str',
        'pod_name': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'process_path': 'process_path',
        'launch_params': 'launch_params',
        'launch_time': 'launch_time',
        'user_name': 'user_name',
        'run_permission': 'run_permission',
        'process_pid': 'process_pid',
        'parent_process_pid': 'parent_process_pid',
        'parent_process_name': 'parent_process_name',
        'hash': 'hash',
        'container_id': 'container_id',
        'container_name': 'container_name',
        'pod_id': 'pod_id',
        'pod_name': 'pod_name'
    }

    def __init__(self, agent_id=None, host_id=None, host_name=None, host_ip=None, process_path=None, launch_params=None, launch_time=None, user_name=None, run_permission=None, process_pid=None, parent_process_pid=None, parent_process_name=None, hash=None, container_id=None, container_name=None, pod_id=None, pod_name=None):
        r"""ProcessResponseInfo

        The model defined in huaweicloud sdk

        :param agent_id: **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **取值范围**: 字符长度1-64位 
        :type agent_id: str
        :param host_id: **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param host_ip: **参数解释**: 服务器IP **取值范围**: 字符长度1-128位 
        :type host_ip: str
        :param process_path: **参数解释**： 进程路径 **取值范围**： 字符长度1-256位 
        :type process_path: str
        :param launch_params: **参数解释** 进程启动参数 **取值范围** 字符长度1-256位 
        :type launch_params: str
        :param launch_time: **参数解释**: 进程启动时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type launch_time: int
        :param user_name: **参数解释**: 用户名 **取值范围**: 字符长度1-64位 
        :type user_name: str
        :param run_permission: **参数解释** 运行权限，对应mode **取值范围** 字符长度1-256位 
        :type run_permission: str
        :param process_pid: **参数解释**： 进程ID **取值范围**： 最小值0，最大值2147483647 
        :type process_pid: int
        :param parent_process_pid: **参数解释**: 父进程id **取值范围**: 最小值0，最大值2147483647 
        :type parent_process_pid: int
        :param parent_process_name: **参数解释** 父进程名称 **取值范围** 字符长度1-256位 
        :type parent_process_name: str
        :param hash: **参数解释** 文件hash **取值范围** 字符长度1-256位 
        :type hash: str
        :param container_id: **参数解释**: 容器ID **取值范围**: 字符长度1-128位 
        :type container_id: str
        :param container_name: **参数解释**： 容器实例名称 **取值范围**： 字符长度1-256位 
        :type container_name: str
        :param pod_id: **参数解释** Pod ID **取值范围** 字符长度1-128位 
        :type pod_id: str
        :param pod_name: **参数解释** Pod名称 **取值范围** 字符长度1-256位 
        :type pod_name: str
        """
        
        

        self._agent_id = None
        self._host_id = None
        self._host_name = None
        self._host_ip = None
        self._process_path = None
        self._launch_params = None
        self._launch_time = None
        self._user_name = None
        self._run_permission = None
        self._process_pid = None
        self._parent_process_pid = None
        self._parent_process_name = None
        self._hash = None
        self._container_id = None
        self._container_name = None
        self._pod_id = None
        self._pod_name = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if process_path is not None:
            self.process_path = process_path
        if launch_params is not None:
            self.launch_params = launch_params
        if launch_time is not None:
            self.launch_time = launch_time
        if user_name is not None:
            self.user_name = user_name
        if run_permission is not None:
            self.run_permission = run_permission
        if process_pid is not None:
            self.process_pid = process_pid
        if parent_process_pid is not None:
            self.parent_process_pid = parent_process_pid
        if parent_process_name is not None:
            self.parent_process_name = parent_process_name
        if hash is not None:
            self.hash = hash
        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name
        if pod_id is not None:
            self.pod_id = pod_id
        if pod_name is not None:
            self.pod_name = pod_name

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ProcessResponseInfo.

        **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **取值范围**: 字符长度1-64位 

        :return: The agent_id of this ProcessResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ProcessResponseInfo.

        **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **取值范围**: 字符长度1-64位 

        :param agent_id: The agent_id of this ProcessResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_id(self):
        r"""Gets the host_id of this ProcessResponseInfo.

        **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this ProcessResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ProcessResponseInfo.

        **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this ProcessResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ProcessResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this ProcessResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ProcessResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this ProcessResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ProcessResponseInfo.

        **参数解释**: 服务器IP **取值范围**: 字符长度1-128位 

        :return: The host_ip of this ProcessResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ProcessResponseInfo.

        **参数解释**: 服务器IP **取值范围**: 字符长度1-128位 

        :param host_ip: The host_ip of this ProcessResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def process_path(self):
        r"""Gets the process_path of this ProcessResponseInfo.

        **参数解释**： 进程路径 **取值范围**： 字符长度1-256位 

        :return: The process_path of this ProcessResponseInfo.
        :rtype: str
        """
        return self._process_path

    @process_path.setter
    def process_path(self, process_path):
        r"""Sets the process_path of this ProcessResponseInfo.

        **参数解释**： 进程路径 **取值范围**： 字符长度1-256位 

        :param process_path: The process_path of this ProcessResponseInfo.
        :type process_path: str
        """
        self._process_path = process_path

    @property
    def launch_params(self):
        r"""Gets the launch_params of this ProcessResponseInfo.

        **参数解释** 进程启动参数 **取值范围** 字符长度1-256位 

        :return: The launch_params of this ProcessResponseInfo.
        :rtype: str
        """
        return self._launch_params

    @launch_params.setter
    def launch_params(self, launch_params):
        r"""Sets the launch_params of this ProcessResponseInfo.

        **参数解释** 进程启动参数 **取值范围** 字符长度1-256位 

        :param launch_params: The launch_params of this ProcessResponseInfo.
        :type launch_params: str
        """
        self._launch_params = launch_params

    @property
    def launch_time(self):
        r"""Gets the launch_time of this ProcessResponseInfo.

        **参数解释**: 进程启动时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The launch_time of this ProcessResponseInfo.
        :rtype: int
        """
        return self._launch_time

    @launch_time.setter
    def launch_time(self, launch_time):
        r"""Sets the launch_time of this ProcessResponseInfo.

        **参数解释**: 进程启动时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param launch_time: The launch_time of this ProcessResponseInfo.
        :type launch_time: int
        """
        self._launch_time = launch_time

    @property
    def user_name(self):
        r"""Gets the user_name of this ProcessResponseInfo.

        **参数解释**: 用户名 **取值范围**: 字符长度1-64位 

        :return: The user_name of this ProcessResponseInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ProcessResponseInfo.

        **参数解释**: 用户名 **取值范围**: 字符长度1-64位 

        :param user_name: The user_name of this ProcessResponseInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def run_permission(self):
        r"""Gets the run_permission of this ProcessResponseInfo.

        **参数解释** 运行权限，对应mode **取值范围** 字符长度1-256位 

        :return: The run_permission of this ProcessResponseInfo.
        :rtype: str
        """
        return self._run_permission

    @run_permission.setter
    def run_permission(self, run_permission):
        r"""Sets the run_permission of this ProcessResponseInfo.

        **参数解释** 运行权限，对应mode **取值范围** 字符长度1-256位 

        :param run_permission: The run_permission of this ProcessResponseInfo.
        :type run_permission: str
        """
        self._run_permission = run_permission

    @property
    def process_pid(self):
        r"""Gets the process_pid of this ProcessResponseInfo.

        **参数解释**： 进程ID **取值范围**： 最小值0，最大值2147483647 

        :return: The process_pid of this ProcessResponseInfo.
        :rtype: int
        """
        return self._process_pid

    @process_pid.setter
    def process_pid(self, process_pid):
        r"""Sets the process_pid of this ProcessResponseInfo.

        **参数解释**： 进程ID **取值范围**： 最小值0，最大值2147483647 

        :param process_pid: The process_pid of this ProcessResponseInfo.
        :type process_pid: int
        """
        self._process_pid = process_pid

    @property
    def parent_process_pid(self):
        r"""Gets the parent_process_pid of this ProcessResponseInfo.

        **参数解释**: 父进程id **取值范围**: 最小值0，最大值2147483647 

        :return: The parent_process_pid of this ProcessResponseInfo.
        :rtype: int
        """
        return self._parent_process_pid

    @parent_process_pid.setter
    def parent_process_pid(self, parent_process_pid):
        r"""Sets the parent_process_pid of this ProcessResponseInfo.

        **参数解释**: 父进程id **取值范围**: 最小值0，最大值2147483647 

        :param parent_process_pid: The parent_process_pid of this ProcessResponseInfo.
        :type parent_process_pid: int
        """
        self._parent_process_pid = parent_process_pid

    @property
    def parent_process_name(self):
        r"""Gets the parent_process_name of this ProcessResponseInfo.

        **参数解释** 父进程名称 **取值范围** 字符长度1-256位 

        :return: The parent_process_name of this ProcessResponseInfo.
        :rtype: str
        """
        return self._parent_process_name

    @parent_process_name.setter
    def parent_process_name(self, parent_process_name):
        r"""Sets the parent_process_name of this ProcessResponseInfo.

        **参数解释** 父进程名称 **取值范围** 字符长度1-256位 

        :param parent_process_name: The parent_process_name of this ProcessResponseInfo.
        :type parent_process_name: str
        """
        self._parent_process_name = parent_process_name

    @property
    def hash(self):
        r"""Gets the hash of this ProcessResponseInfo.

        **参数解释** 文件hash **取值范围** 字符长度1-256位 

        :return: The hash of this ProcessResponseInfo.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        r"""Sets the hash of this ProcessResponseInfo.

        **参数解释** 文件hash **取值范围** 字符长度1-256位 

        :param hash: The hash of this ProcessResponseInfo.
        :type hash: str
        """
        self._hash = hash

    @property
    def container_id(self):
        r"""Gets the container_id of this ProcessResponseInfo.

        **参数解释**: 容器ID **取值范围**: 字符长度1-128位 

        :return: The container_id of this ProcessResponseInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ProcessResponseInfo.

        **参数解释**: 容器ID **取值范围**: 字符长度1-128位 

        :param container_id: The container_id of this ProcessResponseInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this ProcessResponseInfo.

        **参数解释**： 容器实例名称 **取值范围**： 字符长度1-256位 

        :return: The container_name of this ProcessResponseInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ProcessResponseInfo.

        **参数解释**： 容器实例名称 **取值范围**： 字符长度1-256位 

        :param container_name: The container_name of this ProcessResponseInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def pod_id(self):
        r"""Gets the pod_id of this ProcessResponseInfo.

        **参数解释** Pod ID **取值范围** 字符长度1-128位 

        :return: The pod_id of this ProcessResponseInfo.
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        r"""Sets the pod_id of this ProcessResponseInfo.

        **参数解释** Pod ID **取值范围** 字符长度1-128位 

        :param pod_id: The pod_id of this ProcessResponseInfo.
        :type pod_id: str
        """
        self._pod_id = pod_id

    @property
    def pod_name(self):
        r"""Gets the pod_name of this ProcessResponseInfo.

        **参数解释** Pod名称 **取值范围** 字符长度1-256位 

        :return: The pod_name of this ProcessResponseInfo.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this ProcessResponseInfo.

        **参数解释** Pod名称 **取值范围** 字符长度1-256位 

        :param pod_name: The pod_name of this ProcessResponseInfo.
        :type pod_name: str
        """
        self._pod_name = pod_name

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
        if not isinstance(other, ProcessResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
