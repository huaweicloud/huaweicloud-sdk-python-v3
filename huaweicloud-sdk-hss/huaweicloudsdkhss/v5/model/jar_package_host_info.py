# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JarPackageHostInfo:

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
        'file_name': 'str',
        'name': 'str',
        'catalogue': 'str',
        'file_type': 'str',
        'version': 'str',
        'path': 'str',
        'hash': 'str',
        'size': 'int',
        'uid': 'int',
        'gid': 'int',
        'mode': 'str',
        'pid': 'int',
        'proc_path': 'str',
        'container_id': 'str',
        'container_name': 'str',
        'package_path': 'str',
        'is_embedded': 'int',
        'record_time': 'int'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'file_name': 'file_name',
        'name': 'name',
        'catalogue': 'catalogue',
        'file_type': 'file_type',
        'version': 'version',
        'path': 'path',
        'hash': 'hash',
        'size': 'size',
        'uid': 'uid',
        'gid': 'gid',
        'mode': 'mode',
        'pid': 'pid',
        'proc_path': 'proc_path',
        'container_id': 'container_id',
        'container_name': 'container_name',
        'package_path': 'package_path',
        'is_embedded': 'is_embedded',
        'record_time': 'record_time'
    }

    def __init__(self, agent_id=None, host_id=None, host_name=None, host_ip=None, file_name=None, name=None, catalogue=None, file_type=None, version=None, path=None, hash=None, size=None, uid=None, gid=None, mode=None, pid=None, proc_path=None, container_id=None, container_name=None, package_path=None, is_embedded=None, record_time=None):
        """JarPackageHostInfo

        The model defined in huaweicloud sdk

        :param agent_id: Agent ID
        :type agent_id: str
        :param host_id: 主机id
        :type host_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_ip: 服务器ip
        :type host_ip: str
        :param file_name: Jar包名称
        :type file_name: str
        :param name: Jar包名称(不带后缀)
        :type name: str
        :param catalogue: Jar包类型
        :type catalogue: str
        :param file_type: Jar包后缀
        :type file_type: str
        :param version: Jar包版本
        :type version: str
        :param path: Jar包路径
        :type path: str
        :param hash: Jar包hash
        :type hash: str
        :param size: Jar包大小
        :type size: int
        :param uid: uid
        :type uid: int
        :param gid: gid
        :type gid: int
        :param mode: 文件权限
        :type mode: str
        :param pid: 进程id
        :type pid: int
        :param proc_path: 进程可执行文件路径
        :type proc_path: str
        :param container_id: 容器实例id
        :type container_id: str
        :param container_name: 容器名称
        :type container_name: str
        :param package_path: 包路径
        :type package_path: str
        :param is_embedded: 显示的是否是嵌套包
        :type is_embedded: int
        :param record_time: 扫描时间
        :type record_time: int
        """
        
        

        self._agent_id = None
        self._host_id = None
        self._host_name = None
        self._host_ip = None
        self._file_name = None
        self._name = None
        self._catalogue = None
        self._file_type = None
        self._version = None
        self._path = None
        self._hash = None
        self._size = None
        self._uid = None
        self._gid = None
        self._mode = None
        self._pid = None
        self._proc_path = None
        self._container_id = None
        self._container_name = None
        self._package_path = None
        self._is_embedded = None
        self._record_time = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if file_name is not None:
            self.file_name = file_name
        if name is not None:
            self.name = name
        if catalogue is not None:
            self.catalogue = catalogue
        if file_type is not None:
            self.file_type = file_type
        if version is not None:
            self.version = version
        if path is not None:
            self.path = path
        if hash is not None:
            self.hash = hash
        if size is not None:
            self.size = size
        if uid is not None:
            self.uid = uid
        if gid is not None:
            self.gid = gid
        if mode is not None:
            self.mode = mode
        if pid is not None:
            self.pid = pid
        if proc_path is not None:
            self.proc_path = proc_path
        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name
        if package_path is not None:
            self.package_path = package_path
        if is_embedded is not None:
            self.is_embedded = is_embedded
        if record_time is not None:
            self.record_time = record_time

    @property
    def agent_id(self):
        """Gets the agent_id of this JarPackageHostInfo.

        Agent ID

        :return: The agent_id of this JarPackageHostInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this JarPackageHostInfo.

        Agent ID

        :param agent_id: The agent_id of this JarPackageHostInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_id(self):
        """Gets the host_id of this JarPackageHostInfo.

        主机id

        :return: The host_id of this JarPackageHostInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this JarPackageHostInfo.

        主机id

        :param host_id: The host_id of this JarPackageHostInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        """Gets the host_name of this JarPackageHostInfo.

        服务器名称

        :return: The host_name of this JarPackageHostInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this JarPackageHostInfo.

        服务器名称

        :param host_name: The host_name of this JarPackageHostInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        """Gets the host_ip of this JarPackageHostInfo.

        服务器ip

        :return: The host_ip of this JarPackageHostInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this JarPackageHostInfo.

        服务器ip

        :param host_ip: The host_ip of this JarPackageHostInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def file_name(self):
        """Gets the file_name of this JarPackageHostInfo.

        Jar包名称

        :return: The file_name of this JarPackageHostInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this JarPackageHostInfo.

        Jar包名称

        :param file_name: The file_name of this JarPackageHostInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def name(self):
        """Gets the name of this JarPackageHostInfo.

        Jar包名称(不带后缀)

        :return: The name of this JarPackageHostInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JarPackageHostInfo.

        Jar包名称(不带后缀)

        :param name: The name of this JarPackageHostInfo.
        :type name: str
        """
        self._name = name

    @property
    def catalogue(self):
        """Gets the catalogue of this JarPackageHostInfo.

        Jar包类型

        :return: The catalogue of this JarPackageHostInfo.
        :rtype: str
        """
        return self._catalogue

    @catalogue.setter
    def catalogue(self, catalogue):
        """Sets the catalogue of this JarPackageHostInfo.

        Jar包类型

        :param catalogue: The catalogue of this JarPackageHostInfo.
        :type catalogue: str
        """
        self._catalogue = catalogue

    @property
    def file_type(self):
        """Gets the file_type of this JarPackageHostInfo.

        Jar包后缀

        :return: The file_type of this JarPackageHostInfo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this JarPackageHostInfo.

        Jar包后缀

        :param file_type: The file_type of this JarPackageHostInfo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def version(self):
        """Gets the version of this JarPackageHostInfo.

        Jar包版本

        :return: The version of this JarPackageHostInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this JarPackageHostInfo.

        Jar包版本

        :param version: The version of this JarPackageHostInfo.
        :type version: str
        """
        self._version = version

    @property
    def path(self):
        """Gets the path of this JarPackageHostInfo.

        Jar包路径

        :return: The path of this JarPackageHostInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this JarPackageHostInfo.

        Jar包路径

        :param path: The path of this JarPackageHostInfo.
        :type path: str
        """
        self._path = path

    @property
    def hash(self):
        """Gets the hash of this JarPackageHostInfo.

        Jar包hash

        :return: The hash of this JarPackageHostInfo.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this JarPackageHostInfo.

        Jar包hash

        :param hash: The hash of this JarPackageHostInfo.
        :type hash: str
        """
        self._hash = hash

    @property
    def size(self):
        """Gets the size of this JarPackageHostInfo.

        Jar包大小

        :return: The size of this JarPackageHostInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this JarPackageHostInfo.

        Jar包大小

        :param size: The size of this JarPackageHostInfo.
        :type size: int
        """
        self._size = size

    @property
    def uid(self):
        """Gets the uid of this JarPackageHostInfo.

        uid

        :return: The uid of this JarPackageHostInfo.
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this JarPackageHostInfo.

        uid

        :param uid: The uid of this JarPackageHostInfo.
        :type uid: int
        """
        self._uid = uid

    @property
    def gid(self):
        """Gets the gid of this JarPackageHostInfo.

        gid

        :return: The gid of this JarPackageHostInfo.
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this JarPackageHostInfo.

        gid

        :param gid: The gid of this JarPackageHostInfo.
        :type gid: int
        """
        self._gid = gid

    @property
    def mode(self):
        """Gets the mode of this JarPackageHostInfo.

        文件权限

        :return: The mode of this JarPackageHostInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this JarPackageHostInfo.

        文件权限

        :param mode: The mode of this JarPackageHostInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def pid(self):
        """Gets the pid of this JarPackageHostInfo.

        进程id

        :return: The pid of this JarPackageHostInfo.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this JarPackageHostInfo.

        进程id

        :param pid: The pid of this JarPackageHostInfo.
        :type pid: int
        """
        self._pid = pid

    @property
    def proc_path(self):
        """Gets the proc_path of this JarPackageHostInfo.

        进程可执行文件路径

        :return: The proc_path of this JarPackageHostInfo.
        :rtype: str
        """
        return self._proc_path

    @proc_path.setter
    def proc_path(self, proc_path):
        """Sets the proc_path of this JarPackageHostInfo.

        进程可执行文件路径

        :param proc_path: The proc_path of this JarPackageHostInfo.
        :type proc_path: str
        """
        self._proc_path = proc_path

    @property
    def container_id(self):
        """Gets the container_id of this JarPackageHostInfo.

        容器实例id

        :return: The container_id of this JarPackageHostInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this JarPackageHostInfo.

        容器实例id

        :param container_id: The container_id of this JarPackageHostInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        """Gets the container_name of this JarPackageHostInfo.

        容器名称

        :return: The container_name of this JarPackageHostInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this JarPackageHostInfo.

        容器名称

        :param container_name: The container_name of this JarPackageHostInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def package_path(self):
        """Gets the package_path of this JarPackageHostInfo.

        包路径

        :return: The package_path of this JarPackageHostInfo.
        :rtype: str
        """
        return self._package_path

    @package_path.setter
    def package_path(self, package_path):
        """Sets the package_path of this JarPackageHostInfo.

        包路径

        :param package_path: The package_path of this JarPackageHostInfo.
        :type package_path: str
        """
        self._package_path = package_path

    @property
    def is_embedded(self):
        """Gets the is_embedded of this JarPackageHostInfo.

        显示的是否是嵌套包

        :return: The is_embedded of this JarPackageHostInfo.
        :rtype: int
        """
        return self._is_embedded

    @is_embedded.setter
    def is_embedded(self, is_embedded):
        """Sets the is_embedded of this JarPackageHostInfo.

        显示的是否是嵌套包

        :param is_embedded: The is_embedded of this JarPackageHostInfo.
        :type is_embedded: int
        """
        self._is_embedded = is_embedded

    @property
    def record_time(self):
        """Gets the record_time of this JarPackageHostInfo.

        扫描时间

        :return: The record_time of this JarPackageHostInfo.
        :rtype: int
        """
        return self._record_time

    @record_time.setter
    def record_time(self, record_time):
        """Sets the record_time of this JarPackageHostInfo.

        扫描时间

        :param record_time: The record_time of this JarPackageHostInfo.
        :type record_time: int
        """
        self._record_time = record_time

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
        if not isinstance(other, JarPackageHostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
