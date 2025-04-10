# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessesHostResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hash': 'str',
        'host_ip': 'str',
        'host_name': 'str',
        'launch_params': 'str',
        'launch_time': 'int',
        'process_path': 'str',
        'process_pid': 'int',
        'run_permission': 'str',
        'container_id': 'str',
        'container_name': 'str'
    }

    attribute_map = {
        'hash': 'hash',
        'host_ip': 'host_ip',
        'host_name': 'host_name',
        'launch_params': 'launch_params',
        'launch_time': 'launch_time',
        'process_path': 'process_path',
        'process_pid': 'process_pid',
        'run_permission': 'run_permission',
        'container_id': 'container_id',
        'container_name': 'container_name'
    }

    def __init__(self, hash=None, host_ip=None, host_name=None, launch_params=None, launch_time=None, process_path=None, process_pid=None, run_permission=None, container_id=None, container_name=None):
        r"""ProcessesHostResponseInfo

        The model defined in huaweicloud sdk

        :param hash: path对应的sha256值
        :type hash: str
        :param host_ip: 主机ip
        :type host_ip: str
        :param host_name: 主机名称
        :type host_name: str
        :param launch_params: 启动参数
        :type launch_params: str
        :param launch_time: 启动时间
        :type launch_time: int
        :param process_path: 进程可执行文件路径
        :type process_path: str
        :param process_pid: 进程pid
        :type process_pid: int
        :param run_permission: 文件权限
        :type run_permission: str
        :param container_id: 容器id
        :type container_id: str
        :param container_name: 容器名称
        :type container_name: str
        """
        
        

        self._hash = None
        self._host_ip = None
        self._host_name = None
        self._launch_params = None
        self._launch_time = None
        self._process_path = None
        self._process_pid = None
        self._run_permission = None
        self._container_id = None
        self._container_name = None
        self.discriminator = None

        if hash is not None:
            self.hash = hash
        if host_ip is not None:
            self.host_ip = host_ip
        if host_name is not None:
            self.host_name = host_name
        if launch_params is not None:
            self.launch_params = launch_params
        if launch_time is not None:
            self.launch_time = launch_time
        if process_path is not None:
            self.process_path = process_path
        if process_pid is not None:
            self.process_pid = process_pid
        if run_permission is not None:
            self.run_permission = run_permission
        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name

    @property
    def hash(self):
        r"""Gets the hash of this ProcessesHostResponseInfo.

        path对应的sha256值

        :return: The hash of this ProcessesHostResponseInfo.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        r"""Sets the hash of this ProcessesHostResponseInfo.

        path对应的sha256值

        :param hash: The hash of this ProcessesHostResponseInfo.
        :type hash: str
        """
        self._hash = hash

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ProcessesHostResponseInfo.

        主机ip

        :return: The host_ip of this ProcessesHostResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ProcessesHostResponseInfo.

        主机ip

        :param host_ip: The host_ip of this ProcessesHostResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def host_name(self):
        r"""Gets the host_name of this ProcessesHostResponseInfo.

        主机名称

        :return: The host_name of this ProcessesHostResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ProcessesHostResponseInfo.

        主机名称

        :param host_name: The host_name of this ProcessesHostResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def launch_params(self):
        r"""Gets the launch_params of this ProcessesHostResponseInfo.

        启动参数

        :return: The launch_params of this ProcessesHostResponseInfo.
        :rtype: str
        """
        return self._launch_params

    @launch_params.setter
    def launch_params(self, launch_params):
        r"""Sets the launch_params of this ProcessesHostResponseInfo.

        启动参数

        :param launch_params: The launch_params of this ProcessesHostResponseInfo.
        :type launch_params: str
        """
        self._launch_params = launch_params

    @property
    def launch_time(self):
        r"""Gets the launch_time of this ProcessesHostResponseInfo.

        启动时间

        :return: The launch_time of this ProcessesHostResponseInfo.
        :rtype: int
        """
        return self._launch_time

    @launch_time.setter
    def launch_time(self, launch_time):
        r"""Sets the launch_time of this ProcessesHostResponseInfo.

        启动时间

        :param launch_time: The launch_time of this ProcessesHostResponseInfo.
        :type launch_time: int
        """
        self._launch_time = launch_time

    @property
    def process_path(self):
        r"""Gets the process_path of this ProcessesHostResponseInfo.

        进程可执行文件路径

        :return: The process_path of this ProcessesHostResponseInfo.
        :rtype: str
        """
        return self._process_path

    @process_path.setter
    def process_path(self, process_path):
        r"""Sets the process_path of this ProcessesHostResponseInfo.

        进程可执行文件路径

        :param process_path: The process_path of this ProcessesHostResponseInfo.
        :type process_path: str
        """
        self._process_path = process_path

    @property
    def process_pid(self):
        r"""Gets the process_pid of this ProcessesHostResponseInfo.

        进程pid

        :return: The process_pid of this ProcessesHostResponseInfo.
        :rtype: int
        """
        return self._process_pid

    @process_pid.setter
    def process_pid(self, process_pid):
        r"""Sets the process_pid of this ProcessesHostResponseInfo.

        进程pid

        :param process_pid: The process_pid of this ProcessesHostResponseInfo.
        :type process_pid: int
        """
        self._process_pid = process_pid

    @property
    def run_permission(self):
        r"""Gets the run_permission of this ProcessesHostResponseInfo.

        文件权限

        :return: The run_permission of this ProcessesHostResponseInfo.
        :rtype: str
        """
        return self._run_permission

    @run_permission.setter
    def run_permission(self, run_permission):
        r"""Sets the run_permission of this ProcessesHostResponseInfo.

        文件权限

        :param run_permission: The run_permission of this ProcessesHostResponseInfo.
        :type run_permission: str
        """
        self._run_permission = run_permission

    @property
    def container_id(self):
        r"""Gets the container_id of this ProcessesHostResponseInfo.

        容器id

        :return: The container_id of this ProcessesHostResponseInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ProcessesHostResponseInfo.

        容器id

        :param container_id: The container_id of this ProcessesHostResponseInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this ProcessesHostResponseInfo.

        容器名称

        :return: The container_name of this ProcessesHostResponseInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ProcessesHostResponseInfo.

        容器名称

        :param container_name: The container_name of this ProcessesHostResponseInfo.
        :type container_name: str
        """
        self._container_name = container_name

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
        if not isinstance(other, ProcessesHostResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
