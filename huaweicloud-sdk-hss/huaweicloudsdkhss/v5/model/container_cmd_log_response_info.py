# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerCmdLogResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_name': 'str',
        'cluster_id': 'str',
        'cluster_type': 'str',
        'time': 'int',
        'host_id': 'str',
        'host_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'container_name': 'str',
        'container_id': 'str',
        'cmd': 'str',
        'path': 'str',
        'process_pid': 'int',
        'user_name': 'str',
        'group_name': 'str',
        'parent_process_pid': 'int',
        'parent_path': 'str'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'time': 'time',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'container_name': 'container_name',
        'container_id': 'container_id',
        'cmd': 'cmd',
        'path': 'path',
        'process_pid': 'process_pid',
        'user_name': 'user_name',
        'group_name': 'group_name',
        'parent_process_pid': 'parent_process_pid',
        'parent_path': 'parent_path'
    }

    def __init__(self, cluster_name=None, cluster_id=None, cluster_type=None, time=None, host_id=None, host_name=None, private_ip=None, public_ip=None, container_name=None, container_id=None, cmd=None, path=None, process_pid=None, user_name=None, group_name=None, parent_process_pid=None, parent_path=None):
        r"""ContainerCmdLogResponseInfo

        The model defined in huaweicloud sdk

        :param cluster_name: 集群名称
        :type cluster_name: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_type: 集群类型，包含以下几种： - cce：cce集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群
        :type cluster_type: str
        :param time: 日志产生的时间
        :type time: int
        :param host_id: 主机ID
        :type host_id: str
        :param host_name: 主机名称
        :type host_name: str
        :param private_ip: 容器所在主机的私网ip
        :type private_ip: str
        :param public_ip: 主机ip
        :type public_ip: str
        :param container_name: 产生日志的容器名称
        :type container_name: str
        :param container_id: 产生日志的容器id
        :type container_id: str
        :param cmd: 执行的命令
        :type cmd: str
        :param path: 命令行对应的进程路径
        :type path: str
        :param process_pid: 命令行对应的进程pid
        :type process_pid: int
        :param user_name: 执行命令的用户
        :type user_name: str
        :param group_name: 执行命令的用户所属用户组
        :type group_name: str
        :param parent_process_pid: 父进程pid
        :type parent_process_pid: int
        :param parent_path: 父进程路径
        :type parent_path: str
        """
        
        

        self._cluster_name = None
        self._cluster_id = None
        self._cluster_type = None
        self._time = None
        self._host_id = None
        self._host_name = None
        self._private_ip = None
        self._public_ip = None
        self._container_name = None
        self._container_id = None
        self._cmd = None
        self._path = None
        self._process_pid = None
        self._user_name = None
        self._group_name = None
        self._parent_process_pid = None
        self._parent_path = None
        self.discriminator = None

        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if time is not None:
            self.time = time
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if container_name is not None:
            self.container_name = container_name
        if container_id is not None:
            self.container_id = container_id
        if cmd is not None:
            self.cmd = cmd
        if path is not None:
            self.path = path
        if process_pid is not None:
            self.process_pid = process_pid
        if user_name is not None:
            self.user_name = user_name
        if group_name is not None:
            self.group_name = group_name
        if parent_process_pid is not None:
            self.parent_process_pid = parent_process_pid
        if parent_path is not None:
            self.parent_path = parent_path

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ContainerCmdLogResponseInfo.

        集群名称

        :return: The cluster_name of this ContainerCmdLogResponseInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ContainerCmdLogResponseInfo.

        集群名称

        :param cluster_name: The cluster_name of this ContainerCmdLogResponseInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ContainerCmdLogResponseInfo.

        集群id

        :return: The cluster_id of this ContainerCmdLogResponseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ContainerCmdLogResponseInfo.

        集群id

        :param cluster_id: The cluster_id of this ContainerCmdLogResponseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ContainerCmdLogResponseInfo.

        集群类型，包含以下几种： - cce：cce集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群

        :return: The cluster_type of this ContainerCmdLogResponseInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ContainerCmdLogResponseInfo.

        集群类型，包含以下几种： - cce：cce集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群

        :param cluster_type: The cluster_type of this ContainerCmdLogResponseInfo.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def time(self):
        r"""Gets the time of this ContainerCmdLogResponseInfo.

        日志产生的时间

        :return: The time of this ContainerCmdLogResponseInfo.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ContainerCmdLogResponseInfo.

        日志产生的时间

        :param time: The time of this ContainerCmdLogResponseInfo.
        :type time: int
        """
        self._time = time

    @property
    def host_id(self):
        r"""Gets the host_id of this ContainerCmdLogResponseInfo.

        主机ID

        :return: The host_id of this ContainerCmdLogResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ContainerCmdLogResponseInfo.

        主机ID

        :param host_id: The host_id of this ContainerCmdLogResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ContainerCmdLogResponseInfo.

        主机名称

        :return: The host_name of this ContainerCmdLogResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ContainerCmdLogResponseInfo.

        主机名称

        :param host_name: The host_name of this ContainerCmdLogResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ContainerCmdLogResponseInfo.

        容器所在主机的私网ip

        :return: The private_ip of this ContainerCmdLogResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ContainerCmdLogResponseInfo.

        容器所在主机的私网ip

        :param private_ip: The private_ip of this ContainerCmdLogResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ContainerCmdLogResponseInfo.

        主机ip

        :return: The public_ip of this ContainerCmdLogResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ContainerCmdLogResponseInfo.

        主机ip

        :param public_ip: The public_ip of this ContainerCmdLogResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def container_name(self):
        r"""Gets the container_name of this ContainerCmdLogResponseInfo.

        产生日志的容器名称

        :return: The container_name of this ContainerCmdLogResponseInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ContainerCmdLogResponseInfo.

        产生日志的容器名称

        :param container_name: The container_name of this ContainerCmdLogResponseInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def container_id(self):
        r"""Gets the container_id of this ContainerCmdLogResponseInfo.

        产生日志的容器id

        :return: The container_id of this ContainerCmdLogResponseInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ContainerCmdLogResponseInfo.

        产生日志的容器id

        :param container_id: The container_id of this ContainerCmdLogResponseInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def cmd(self):
        r"""Gets the cmd of this ContainerCmdLogResponseInfo.

        执行的命令

        :return: The cmd of this ContainerCmdLogResponseInfo.
        :rtype: str
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        r"""Sets the cmd of this ContainerCmdLogResponseInfo.

        执行的命令

        :param cmd: The cmd of this ContainerCmdLogResponseInfo.
        :type cmd: str
        """
        self._cmd = cmd

    @property
    def path(self):
        r"""Gets the path of this ContainerCmdLogResponseInfo.

        命令行对应的进程路径

        :return: The path of this ContainerCmdLogResponseInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ContainerCmdLogResponseInfo.

        命令行对应的进程路径

        :param path: The path of this ContainerCmdLogResponseInfo.
        :type path: str
        """
        self._path = path

    @property
    def process_pid(self):
        r"""Gets the process_pid of this ContainerCmdLogResponseInfo.

        命令行对应的进程pid

        :return: The process_pid of this ContainerCmdLogResponseInfo.
        :rtype: int
        """
        return self._process_pid

    @process_pid.setter
    def process_pid(self, process_pid):
        r"""Sets the process_pid of this ContainerCmdLogResponseInfo.

        命令行对应的进程pid

        :param process_pid: The process_pid of this ContainerCmdLogResponseInfo.
        :type process_pid: int
        """
        self._process_pid = process_pid

    @property
    def user_name(self):
        r"""Gets the user_name of this ContainerCmdLogResponseInfo.

        执行命令的用户

        :return: The user_name of this ContainerCmdLogResponseInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ContainerCmdLogResponseInfo.

        执行命令的用户

        :param user_name: The user_name of this ContainerCmdLogResponseInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def group_name(self):
        r"""Gets the group_name of this ContainerCmdLogResponseInfo.

        执行命令的用户所属用户组

        :return: The group_name of this ContainerCmdLogResponseInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ContainerCmdLogResponseInfo.

        执行命令的用户所属用户组

        :param group_name: The group_name of this ContainerCmdLogResponseInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def parent_process_pid(self):
        r"""Gets the parent_process_pid of this ContainerCmdLogResponseInfo.

        父进程pid

        :return: The parent_process_pid of this ContainerCmdLogResponseInfo.
        :rtype: int
        """
        return self._parent_process_pid

    @parent_process_pid.setter
    def parent_process_pid(self, parent_process_pid):
        r"""Sets the parent_process_pid of this ContainerCmdLogResponseInfo.

        父进程pid

        :param parent_process_pid: The parent_process_pid of this ContainerCmdLogResponseInfo.
        :type parent_process_pid: int
        """
        self._parent_process_pid = parent_process_pid

    @property
    def parent_path(self):
        r"""Gets the parent_path of this ContainerCmdLogResponseInfo.

        父进程路径

        :return: The parent_path of this ContainerCmdLogResponseInfo.
        :rtype: str
        """
        return self._parent_path

    @parent_path.setter
    def parent_path(self, parent_path):
        r"""Sets the parent_path of this ContainerCmdLogResponseInfo.

        父进程路径

        :param parent_path: The parent_path of this ContainerCmdLogResponseInfo.
        :type parent_path: str
        """
        self._parent_path = parent_path

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
        if not isinstance(other, ContainerCmdLogResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
