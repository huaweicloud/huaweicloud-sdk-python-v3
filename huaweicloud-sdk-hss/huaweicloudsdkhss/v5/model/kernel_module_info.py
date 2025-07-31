# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KernelModuleInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'file_name': 'str',
        'version': 'str',
        'srcversion': 'str',
        'path': 'str',
        'size': 'int',
        'mode': 'str',
        'uid': 'int',
        'ctime': 'int',
        'mtime': 'int',
        'hash': 'str',
        'desc': 'str',
        'record_time': 'int',
        'first_scan_time': 'int'
    }

    attribute_map = {
        'name': 'name',
        'file_name': 'file_name',
        'version': 'version',
        'srcversion': 'srcversion',
        'path': 'path',
        'size': 'size',
        'mode': 'mode',
        'uid': 'uid',
        'ctime': 'ctime',
        'mtime': 'mtime',
        'hash': 'hash',
        'desc': 'desc',
        'record_time': 'record_time',
        'first_scan_time': 'first_scan_time'
    }

    def __init__(self, name=None, file_name=None, version=None, srcversion=None, path=None, size=None, mode=None, uid=None, ctime=None, mtime=None, hash=None, desc=None, record_time=None, first_scan_time=None):
        r"""KernelModuleInfo

        The model defined in huaweicloud sdk

        :param name: 内核模块名称
        :type name: str
        :param file_name: 文件名称
        :type file_name: str
        :param version: 内核模块版本号
        :type version: str
        :param srcversion: 源码版本号
        :type srcversion: str
        :param path: 文件路径
        :type path: str
        :param size: 文件大小
        :type size: int
        :param mode: 文件权限
        :type mode: str
        :param uid: 文件用户ID
        :type uid: int
        :param ctime: 文件创建时间
        :type ctime: int
        :param mtime: 最后修改时间
        :type mtime: int
        :param hash: 文件哈希
        :type hash: str
        :param desc: 内核模块描述信息
        :type desc: str
        :param record_time: 扫描时间
        :type record_time: int
        :param first_scan_time: 首次扫描时间
        :type first_scan_time: int
        """
        
        

        self._name = None
        self._file_name = None
        self._version = None
        self._srcversion = None
        self._path = None
        self._size = None
        self._mode = None
        self._uid = None
        self._ctime = None
        self._mtime = None
        self._hash = None
        self._desc = None
        self._record_time = None
        self._first_scan_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if file_name is not None:
            self.file_name = file_name
        if version is not None:
            self.version = version
        if srcversion is not None:
            self.srcversion = srcversion
        if path is not None:
            self.path = path
        if size is not None:
            self.size = size
        if mode is not None:
            self.mode = mode
        if uid is not None:
            self.uid = uid
        if ctime is not None:
            self.ctime = ctime
        if mtime is not None:
            self.mtime = mtime
        if hash is not None:
            self.hash = hash
        if desc is not None:
            self.desc = desc
        if record_time is not None:
            self.record_time = record_time
        if first_scan_time is not None:
            self.first_scan_time = first_scan_time

    @property
    def name(self):
        r"""Gets the name of this KernelModuleInfo.

        内核模块名称

        :return: The name of this KernelModuleInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this KernelModuleInfo.

        内核模块名称

        :param name: The name of this KernelModuleInfo.
        :type name: str
        """
        self._name = name

    @property
    def file_name(self):
        r"""Gets the file_name of this KernelModuleInfo.

        文件名称

        :return: The file_name of this KernelModuleInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this KernelModuleInfo.

        文件名称

        :param file_name: The file_name of this KernelModuleInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def version(self):
        r"""Gets the version of this KernelModuleInfo.

        内核模块版本号

        :return: The version of this KernelModuleInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this KernelModuleInfo.

        内核模块版本号

        :param version: The version of this KernelModuleInfo.
        :type version: str
        """
        self._version = version

    @property
    def srcversion(self):
        r"""Gets the srcversion of this KernelModuleInfo.

        源码版本号

        :return: The srcversion of this KernelModuleInfo.
        :rtype: str
        """
        return self._srcversion

    @srcversion.setter
    def srcversion(self, srcversion):
        r"""Sets the srcversion of this KernelModuleInfo.

        源码版本号

        :param srcversion: The srcversion of this KernelModuleInfo.
        :type srcversion: str
        """
        self._srcversion = srcversion

    @property
    def path(self):
        r"""Gets the path of this KernelModuleInfo.

        文件路径

        :return: The path of this KernelModuleInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this KernelModuleInfo.

        文件路径

        :param path: The path of this KernelModuleInfo.
        :type path: str
        """
        self._path = path

    @property
    def size(self):
        r"""Gets the size of this KernelModuleInfo.

        文件大小

        :return: The size of this KernelModuleInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this KernelModuleInfo.

        文件大小

        :param size: The size of this KernelModuleInfo.
        :type size: int
        """
        self._size = size

    @property
    def mode(self):
        r"""Gets the mode of this KernelModuleInfo.

        文件权限

        :return: The mode of this KernelModuleInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this KernelModuleInfo.

        文件权限

        :param mode: The mode of this KernelModuleInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def uid(self):
        r"""Gets the uid of this KernelModuleInfo.

        文件用户ID

        :return: The uid of this KernelModuleInfo.
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this KernelModuleInfo.

        文件用户ID

        :param uid: The uid of this KernelModuleInfo.
        :type uid: int
        """
        self._uid = uid

    @property
    def ctime(self):
        r"""Gets the ctime of this KernelModuleInfo.

        文件创建时间

        :return: The ctime of this KernelModuleInfo.
        :rtype: int
        """
        return self._ctime

    @ctime.setter
    def ctime(self, ctime):
        r"""Sets the ctime of this KernelModuleInfo.

        文件创建时间

        :param ctime: The ctime of this KernelModuleInfo.
        :type ctime: int
        """
        self._ctime = ctime

    @property
    def mtime(self):
        r"""Gets the mtime of this KernelModuleInfo.

        最后修改时间

        :return: The mtime of this KernelModuleInfo.
        :rtype: int
        """
        return self._mtime

    @mtime.setter
    def mtime(self, mtime):
        r"""Sets the mtime of this KernelModuleInfo.

        最后修改时间

        :param mtime: The mtime of this KernelModuleInfo.
        :type mtime: int
        """
        self._mtime = mtime

    @property
    def hash(self):
        r"""Gets the hash of this KernelModuleInfo.

        文件哈希

        :return: The hash of this KernelModuleInfo.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        r"""Sets the hash of this KernelModuleInfo.

        文件哈希

        :param hash: The hash of this KernelModuleInfo.
        :type hash: str
        """
        self._hash = hash

    @property
    def desc(self):
        r"""Gets the desc of this KernelModuleInfo.

        内核模块描述信息

        :return: The desc of this KernelModuleInfo.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this KernelModuleInfo.

        内核模块描述信息

        :param desc: The desc of this KernelModuleInfo.
        :type desc: str
        """
        self._desc = desc

    @property
    def record_time(self):
        r"""Gets the record_time of this KernelModuleInfo.

        扫描时间

        :return: The record_time of this KernelModuleInfo.
        :rtype: int
        """
        return self._record_time

    @record_time.setter
    def record_time(self, record_time):
        r"""Sets the record_time of this KernelModuleInfo.

        扫描时间

        :param record_time: The record_time of this KernelModuleInfo.
        :type record_time: int
        """
        self._record_time = record_time

    @property
    def first_scan_time(self):
        r"""Gets the first_scan_time of this KernelModuleInfo.

        首次扫描时间

        :return: The first_scan_time of this KernelModuleInfo.
        :rtype: int
        """
        return self._first_scan_time

    @first_scan_time.setter
    def first_scan_time(self, first_scan_time):
        r"""Sets the first_scan_time of this KernelModuleInfo.

        首次扫描时间

        :param first_scan_time: The first_scan_time of this KernelModuleInfo.
        :type first_scan_time: int
        """
        self._first_scan_time = first_scan_time

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
        if not isinstance(other, KernelModuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
