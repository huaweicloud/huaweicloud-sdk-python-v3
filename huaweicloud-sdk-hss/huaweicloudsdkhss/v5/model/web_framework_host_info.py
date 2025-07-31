# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebFrameworkHostInfo:

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
        'name': 'str',
        'version': 'str',
        'path': 'str',
        'file_size': 'int',
        'record_time': 'int',
        'bind_ip_list': 'str',
        'catalogue': 'str',
        'connected_ip_list': 'str',
        'connected_number': 'str',
        'embedder_dir': 'str',
        'file_name': 'str',
        'file_type': 'str',
        'gid': 'int',
        'hash': 'str',
        'is_embedded': 'int',
        'listen_port_list': 'str',
        'mode': 'str',
        'pid': 'int',
        'proc_path': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'name': 'name',
        'version': 'version',
        'path': 'path',
        'file_size': 'file_size',
        'record_time': 'record_time',
        'bind_ip_list': 'bind_ip_list',
        'catalogue': 'catalogue',
        'connected_ip_list': 'connected_ip_list',
        'connected_number': 'connected_number',
        'embedder_dir': 'embedder_dir',
        'file_name': 'file_name',
        'file_type': 'file_type',
        'gid': 'gid',
        'hash': 'hash',
        'is_embedded': 'is_embedded',
        'listen_port_list': 'listen_port_list',
        'mode': 'mode',
        'pid': 'pid',
        'proc_path': 'proc_path',
        'uid': 'uid'
    }

    def __init__(self, agent_id=None, host_id=None, host_name=None, host_ip=None, name=None, version=None, path=None, file_size=None, record_time=None, bind_ip_list=None, catalogue=None, connected_ip_list=None, connected_number=None, embedder_dir=None, file_name=None, file_type=None, gid=None, hash=None, is_embedded=None, listen_port_list=None, mode=None, pid=None, proc_path=None, uid=None):
        r"""WebFrameworkHostInfo

        The model defined in huaweicloud sdk

        :param agent_id: agent_id
        :type agent_id: str
        :param host_id: 主机id
        :type host_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_ip: 服务器ip
        :type host_ip: str
        :param name: 名称
        :type name: str
        :param version: 版本
        :type version: str
        :param path: 路径
        :type path: str
        :param file_size: 大小
        :type file_size: int
        :param record_time: 扫描时间
        :type record_time: int
        :param bind_ip_list: 绑定的ip列表
        :type bind_ip_list: str
        :param catalogue: 软件的类型
        :type catalogue: str
        :param connected_ip_list: 连接的ip列表
        :type connected_ip_list: str
        :param connected_number: 连接数
        :type connected_number: str
        :param embedder_dir: 压缩的目录
        :type embedder_dir: str
        :param file_name: 文件名称
        :type file_name: str
        :param file_type: 文件类型
        :type file_type: str
        :param gid: 用户组id
        :type gid: int
        :param hash: 文件哈希值
        :type hash: str
        :param is_embedded: 是否是压缩的文件
        :type is_embedded: int
        :param listen_port_list: 监听的端口列表
        :type listen_port_list: str
        :param mode: 文件权限
        :type mode: str
        :param pid: 进程id
        :type pid: int
        :param proc_path: 进程路径
        :type proc_path: str
        :param uid: 用户id
        :type uid: str
        """
        
        

        self._agent_id = None
        self._host_id = None
        self._host_name = None
        self._host_ip = None
        self._name = None
        self._version = None
        self._path = None
        self._file_size = None
        self._record_time = None
        self._bind_ip_list = None
        self._catalogue = None
        self._connected_ip_list = None
        self._connected_number = None
        self._embedder_dir = None
        self._file_name = None
        self._file_type = None
        self._gid = None
        self._hash = None
        self._is_embedded = None
        self._listen_port_list = None
        self._mode = None
        self._pid = None
        self._proc_path = None
        self._uid = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if path is not None:
            self.path = path
        if file_size is not None:
            self.file_size = file_size
        if record_time is not None:
            self.record_time = record_time
        if bind_ip_list is not None:
            self.bind_ip_list = bind_ip_list
        if catalogue is not None:
            self.catalogue = catalogue
        if connected_ip_list is not None:
            self.connected_ip_list = connected_ip_list
        if connected_number is not None:
            self.connected_number = connected_number
        if embedder_dir is not None:
            self.embedder_dir = embedder_dir
        if file_name is not None:
            self.file_name = file_name
        if file_type is not None:
            self.file_type = file_type
        if gid is not None:
            self.gid = gid
        if hash is not None:
            self.hash = hash
        if is_embedded is not None:
            self.is_embedded = is_embedded
        if listen_port_list is not None:
            self.listen_port_list = listen_port_list
        if mode is not None:
            self.mode = mode
        if pid is not None:
            self.pid = pid
        if proc_path is not None:
            self.proc_path = proc_path
        if uid is not None:
            self.uid = uid

    @property
    def agent_id(self):
        r"""Gets the agent_id of this WebFrameworkHostInfo.

        agent_id

        :return: The agent_id of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this WebFrameworkHostInfo.

        agent_id

        :param agent_id: The agent_id of this WebFrameworkHostInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_id(self):
        r"""Gets the host_id of this WebFrameworkHostInfo.

        主机id

        :return: The host_id of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this WebFrameworkHostInfo.

        主机id

        :param host_id: The host_id of this WebFrameworkHostInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this WebFrameworkHostInfo.

        服务器名称

        :return: The host_name of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this WebFrameworkHostInfo.

        服务器名称

        :param host_name: The host_name of this WebFrameworkHostInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this WebFrameworkHostInfo.

        服务器ip

        :return: The host_ip of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this WebFrameworkHostInfo.

        服务器ip

        :param host_ip: The host_ip of this WebFrameworkHostInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def name(self):
        r"""Gets the name of this WebFrameworkHostInfo.

        名称

        :return: The name of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WebFrameworkHostInfo.

        名称

        :param name: The name of this WebFrameworkHostInfo.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this WebFrameworkHostInfo.

        版本

        :return: The version of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this WebFrameworkHostInfo.

        版本

        :param version: The version of this WebFrameworkHostInfo.
        :type version: str
        """
        self._version = version

    @property
    def path(self):
        r"""Gets the path of this WebFrameworkHostInfo.

        路径

        :return: The path of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this WebFrameworkHostInfo.

        路径

        :param path: The path of this WebFrameworkHostInfo.
        :type path: str
        """
        self._path = path

    @property
    def file_size(self):
        r"""Gets the file_size of this WebFrameworkHostInfo.

        大小

        :return: The file_size of this WebFrameworkHostInfo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this WebFrameworkHostInfo.

        大小

        :param file_size: The file_size of this WebFrameworkHostInfo.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def record_time(self):
        r"""Gets the record_time of this WebFrameworkHostInfo.

        扫描时间

        :return: The record_time of this WebFrameworkHostInfo.
        :rtype: int
        """
        return self._record_time

    @record_time.setter
    def record_time(self, record_time):
        r"""Sets the record_time of this WebFrameworkHostInfo.

        扫描时间

        :param record_time: The record_time of this WebFrameworkHostInfo.
        :type record_time: int
        """
        self._record_time = record_time

    @property
    def bind_ip_list(self):
        r"""Gets the bind_ip_list of this WebFrameworkHostInfo.

        绑定的ip列表

        :return: The bind_ip_list of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._bind_ip_list

    @bind_ip_list.setter
    def bind_ip_list(self, bind_ip_list):
        r"""Sets the bind_ip_list of this WebFrameworkHostInfo.

        绑定的ip列表

        :param bind_ip_list: The bind_ip_list of this WebFrameworkHostInfo.
        :type bind_ip_list: str
        """
        self._bind_ip_list = bind_ip_list

    @property
    def catalogue(self):
        r"""Gets the catalogue of this WebFrameworkHostInfo.

        软件的类型

        :return: The catalogue of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._catalogue

    @catalogue.setter
    def catalogue(self, catalogue):
        r"""Sets the catalogue of this WebFrameworkHostInfo.

        软件的类型

        :param catalogue: The catalogue of this WebFrameworkHostInfo.
        :type catalogue: str
        """
        self._catalogue = catalogue

    @property
    def connected_ip_list(self):
        r"""Gets the connected_ip_list of this WebFrameworkHostInfo.

        连接的ip列表

        :return: The connected_ip_list of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._connected_ip_list

    @connected_ip_list.setter
    def connected_ip_list(self, connected_ip_list):
        r"""Sets the connected_ip_list of this WebFrameworkHostInfo.

        连接的ip列表

        :param connected_ip_list: The connected_ip_list of this WebFrameworkHostInfo.
        :type connected_ip_list: str
        """
        self._connected_ip_list = connected_ip_list

    @property
    def connected_number(self):
        r"""Gets the connected_number of this WebFrameworkHostInfo.

        连接数

        :return: The connected_number of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._connected_number

    @connected_number.setter
    def connected_number(self, connected_number):
        r"""Sets the connected_number of this WebFrameworkHostInfo.

        连接数

        :param connected_number: The connected_number of this WebFrameworkHostInfo.
        :type connected_number: str
        """
        self._connected_number = connected_number

    @property
    def embedder_dir(self):
        r"""Gets the embedder_dir of this WebFrameworkHostInfo.

        压缩的目录

        :return: The embedder_dir of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._embedder_dir

    @embedder_dir.setter
    def embedder_dir(self, embedder_dir):
        r"""Sets the embedder_dir of this WebFrameworkHostInfo.

        压缩的目录

        :param embedder_dir: The embedder_dir of this WebFrameworkHostInfo.
        :type embedder_dir: str
        """
        self._embedder_dir = embedder_dir

    @property
    def file_name(self):
        r"""Gets the file_name of this WebFrameworkHostInfo.

        文件名称

        :return: The file_name of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this WebFrameworkHostInfo.

        文件名称

        :param file_name: The file_name of this WebFrameworkHostInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_type(self):
        r"""Gets the file_type of this WebFrameworkHostInfo.

        文件类型

        :return: The file_type of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this WebFrameworkHostInfo.

        文件类型

        :param file_type: The file_type of this WebFrameworkHostInfo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def gid(self):
        r"""Gets the gid of this WebFrameworkHostInfo.

        用户组id

        :return: The gid of this WebFrameworkHostInfo.
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        r"""Sets the gid of this WebFrameworkHostInfo.

        用户组id

        :param gid: The gid of this WebFrameworkHostInfo.
        :type gid: int
        """
        self._gid = gid

    @property
    def hash(self):
        r"""Gets the hash of this WebFrameworkHostInfo.

        文件哈希值

        :return: The hash of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        r"""Sets the hash of this WebFrameworkHostInfo.

        文件哈希值

        :param hash: The hash of this WebFrameworkHostInfo.
        :type hash: str
        """
        self._hash = hash

    @property
    def is_embedded(self):
        r"""Gets the is_embedded of this WebFrameworkHostInfo.

        是否是压缩的文件

        :return: The is_embedded of this WebFrameworkHostInfo.
        :rtype: int
        """
        return self._is_embedded

    @is_embedded.setter
    def is_embedded(self, is_embedded):
        r"""Sets the is_embedded of this WebFrameworkHostInfo.

        是否是压缩的文件

        :param is_embedded: The is_embedded of this WebFrameworkHostInfo.
        :type is_embedded: int
        """
        self._is_embedded = is_embedded

    @property
    def listen_port_list(self):
        r"""Gets the listen_port_list of this WebFrameworkHostInfo.

        监听的端口列表

        :return: The listen_port_list of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._listen_port_list

    @listen_port_list.setter
    def listen_port_list(self, listen_port_list):
        r"""Sets the listen_port_list of this WebFrameworkHostInfo.

        监听的端口列表

        :param listen_port_list: The listen_port_list of this WebFrameworkHostInfo.
        :type listen_port_list: str
        """
        self._listen_port_list = listen_port_list

    @property
    def mode(self):
        r"""Gets the mode of this WebFrameworkHostInfo.

        文件权限

        :return: The mode of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this WebFrameworkHostInfo.

        文件权限

        :param mode: The mode of this WebFrameworkHostInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def pid(self):
        r"""Gets the pid of this WebFrameworkHostInfo.

        进程id

        :return: The pid of this WebFrameworkHostInfo.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this WebFrameworkHostInfo.

        进程id

        :param pid: The pid of this WebFrameworkHostInfo.
        :type pid: int
        """
        self._pid = pid

    @property
    def proc_path(self):
        r"""Gets the proc_path of this WebFrameworkHostInfo.

        进程路径

        :return: The proc_path of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._proc_path

    @proc_path.setter
    def proc_path(self, proc_path):
        r"""Sets the proc_path of this WebFrameworkHostInfo.

        进程路径

        :param proc_path: The proc_path of this WebFrameworkHostInfo.
        :type proc_path: str
        """
        self._proc_path = proc_path

    @property
    def uid(self):
        r"""Gets the uid of this WebFrameworkHostInfo.

        用户id

        :return: The uid of this WebFrameworkHostInfo.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this WebFrameworkHostInfo.

        用户id

        :param uid: The uid of this WebFrameworkHostInfo.
        :type uid: str
        """
        self._uid = uid

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
        if not isinstance(other, WebFrameworkHostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
