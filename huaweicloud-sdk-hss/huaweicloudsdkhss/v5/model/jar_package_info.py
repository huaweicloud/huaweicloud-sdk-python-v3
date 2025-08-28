# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JarPackageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'file_type': 'str',
        'catalogue': 'str',
        'version': 'str',
        'path': 'str',
        'mode': 'str',
        'uid': 'int',
        'hash': 'str',
        'pid': 'int',
        'proc_path': 'str',
        'record_time': 'int',
        'container_id': 'str',
        'container_name': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'file_type': 'file_type',
        'catalogue': 'catalogue',
        'version': 'version',
        'path': 'path',
        'mode': 'mode',
        'uid': 'uid',
        'hash': 'hash',
        'pid': 'pid',
        'proc_path': 'proc_path',
        'record_time': 'record_time',
        'container_id': 'container_id',
        'container_name': 'container_name'
    }

    def __init__(self, file_name=None, file_type=None, catalogue=None, version=None, path=None, mode=None, uid=None, hash=None, pid=None, proc_path=None, record_time=None, container_id=None, container_name=None):
        r"""JarPackageInfo

        The model defined in huaweicloud sdk

        :param file_name: **参数解释**: 中间件名称 **取值范围**: 字符长度1-256 
        :type file_name: str
        :param file_type: **参数解释**: 中间件类型 **取值范围**: -jar：jar包 -python：python软件包 -npm：npm软件包 
        :type file_type: str
        :param catalogue: **参数解释**: 分类 **取值范围**: -util：默认分类 
        :type catalogue: str
        :param version: **参数解释**: 中间件版本 **取值范围**: 字符长度1-512 
        :type version: str
        :param path: **参数解释**: 中间件路径 **取值范围**: 字符长度1-512 
        :type path: str
        :param mode: **参数解释**: 中间件文件权限 **取值范围**: 字符长度1-32 
        :type mode: str
        :param uid: **参数解释**: uid **取值范围**: 最小值0，最大值2147483647 
        :type uid: int
        :param hash: **参数解释**: 中间件文件hash **取值范围**: 字符长度1-64 
        :type hash: str
        :param pid: **参数解释**: 中间件进程ID **取值范围**: 最小值0，最大值2147483647 
        :type pid: int
        :param proc_path: **参数解释**: 中间件进程路径 **取值范围**: 字符长度1-1024 
        :type proc_path: str
        :param record_time: **参数解释**: 中间件扫描时间 **取值范围**: 最小值0，最大值2^63-1 
        :type record_time: int
        :param container_id: **参数解释**: 容器id **取值范围**: 字符长度1-128 
        :type container_id: str
        :param container_name: **参数解释**: 容器名称 **取值范围**: 字符长度1-256 
        :type container_name: str
        """
        
        

        self._file_name = None
        self._file_type = None
        self._catalogue = None
        self._version = None
        self._path = None
        self._mode = None
        self._uid = None
        self._hash = None
        self._pid = None
        self._proc_path = None
        self._record_time = None
        self._container_id = None
        self._container_name = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if file_type is not None:
            self.file_type = file_type
        if catalogue is not None:
            self.catalogue = catalogue
        if version is not None:
            self.version = version
        if path is not None:
            self.path = path
        if mode is not None:
            self.mode = mode
        if uid is not None:
            self.uid = uid
        if hash is not None:
            self.hash = hash
        if pid is not None:
            self.pid = pid
        if proc_path is not None:
            self.proc_path = proc_path
        if record_time is not None:
            self.record_time = record_time
        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name

    @property
    def file_name(self):
        r"""Gets the file_name of this JarPackageInfo.

        **参数解释**: 中间件名称 **取值范围**: 字符长度1-256 

        :return: The file_name of this JarPackageInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this JarPackageInfo.

        **参数解释**: 中间件名称 **取值范围**: 字符长度1-256 

        :param file_name: The file_name of this JarPackageInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_type(self):
        r"""Gets the file_type of this JarPackageInfo.

        **参数解释**: 中间件类型 **取值范围**: -jar：jar包 -python：python软件包 -npm：npm软件包 

        :return: The file_type of this JarPackageInfo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this JarPackageInfo.

        **参数解释**: 中间件类型 **取值范围**: -jar：jar包 -python：python软件包 -npm：npm软件包 

        :param file_type: The file_type of this JarPackageInfo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def catalogue(self):
        r"""Gets the catalogue of this JarPackageInfo.

        **参数解释**: 分类 **取值范围**: -util：默认分类 

        :return: The catalogue of this JarPackageInfo.
        :rtype: str
        """
        return self._catalogue

    @catalogue.setter
    def catalogue(self, catalogue):
        r"""Sets the catalogue of this JarPackageInfo.

        **参数解释**: 分类 **取值范围**: -util：默认分类 

        :param catalogue: The catalogue of this JarPackageInfo.
        :type catalogue: str
        """
        self._catalogue = catalogue

    @property
    def version(self):
        r"""Gets the version of this JarPackageInfo.

        **参数解释**: 中间件版本 **取值范围**: 字符长度1-512 

        :return: The version of this JarPackageInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this JarPackageInfo.

        **参数解释**: 中间件版本 **取值范围**: 字符长度1-512 

        :param version: The version of this JarPackageInfo.
        :type version: str
        """
        self._version = version

    @property
    def path(self):
        r"""Gets the path of this JarPackageInfo.

        **参数解释**: 中间件路径 **取值范围**: 字符长度1-512 

        :return: The path of this JarPackageInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this JarPackageInfo.

        **参数解释**: 中间件路径 **取值范围**: 字符长度1-512 

        :param path: The path of this JarPackageInfo.
        :type path: str
        """
        self._path = path

    @property
    def mode(self):
        r"""Gets the mode of this JarPackageInfo.

        **参数解释**: 中间件文件权限 **取值范围**: 字符长度1-32 

        :return: The mode of this JarPackageInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this JarPackageInfo.

        **参数解释**: 中间件文件权限 **取值范围**: 字符长度1-32 

        :param mode: The mode of this JarPackageInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def uid(self):
        r"""Gets the uid of this JarPackageInfo.

        **参数解释**: uid **取值范围**: 最小值0，最大值2147483647 

        :return: The uid of this JarPackageInfo.
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this JarPackageInfo.

        **参数解释**: uid **取值范围**: 最小值0，最大值2147483647 

        :param uid: The uid of this JarPackageInfo.
        :type uid: int
        """
        self._uid = uid

    @property
    def hash(self):
        r"""Gets the hash of this JarPackageInfo.

        **参数解释**: 中间件文件hash **取值范围**: 字符长度1-64 

        :return: The hash of this JarPackageInfo.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        r"""Sets the hash of this JarPackageInfo.

        **参数解释**: 中间件文件hash **取值范围**: 字符长度1-64 

        :param hash: The hash of this JarPackageInfo.
        :type hash: str
        """
        self._hash = hash

    @property
    def pid(self):
        r"""Gets the pid of this JarPackageInfo.

        **参数解释**: 中间件进程ID **取值范围**: 最小值0，最大值2147483647 

        :return: The pid of this JarPackageInfo.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this JarPackageInfo.

        **参数解释**: 中间件进程ID **取值范围**: 最小值0，最大值2147483647 

        :param pid: The pid of this JarPackageInfo.
        :type pid: int
        """
        self._pid = pid

    @property
    def proc_path(self):
        r"""Gets the proc_path of this JarPackageInfo.

        **参数解释**: 中间件进程路径 **取值范围**: 字符长度1-1024 

        :return: The proc_path of this JarPackageInfo.
        :rtype: str
        """
        return self._proc_path

    @proc_path.setter
    def proc_path(self, proc_path):
        r"""Sets the proc_path of this JarPackageInfo.

        **参数解释**: 中间件进程路径 **取值范围**: 字符长度1-1024 

        :param proc_path: The proc_path of this JarPackageInfo.
        :type proc_path: str
        """
        self._proc_path = proc_path

    @property
    def record_time(self):
        r"""Gets the record_time of this JarPackageInfo.

        **参数解释**: 中间件扫描时间 **取值范围**: 最小值0，最大值2^63-1 

        :return: The record_time of this JarPackageInfo.
        :rtype: int
        """
        return self._record_time

    @record_time.setter
    def record_time(self, record_time):
        r"""Sets the record_time of this JarPackageInfo.

        **参数解释**: 中间件扫描时间 **取值范围**: 最小值0，最大值2^63-1 

        :param record_time: The record_time of this JarPackageInfo.
        :type record_time: int
        """
        self._record_time = record_time

    @property
    def container_id(self):
        r"""Gets the container_id of this JarPackageInfo.

        **参数解释**: 容器id **取值范围**: 字符长度1-128 

        :return: The container_id of this JarPackageInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this JarPackageInfo.

        **参数解释**: 容器id **取值范围**: 字符长度1-128 

        :param container_id: The container_id of this JarPackageInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this JarPackageInfo.

        **参数解释**: 容器名称 **取值范围**: 字符长度1-256 

        :return: The container_name of this JarPackageInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this JarPackageInfo.

        **参数解释**: 容器名称 **取值范围**: 字符长度1-256 

        :param container_name: The container_name of this JarPackageInfo.
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
        if not isinstance(other, JarPackageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
