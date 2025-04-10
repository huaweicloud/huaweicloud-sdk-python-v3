# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Dependency:

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
        'owner': 'str',
        'link': 'str',
        'runtime': 'str',
        'etag': 'str',
        'size': 'int',
        'name': 'str',
        'description': 'str',
        'file_name': 'str',
        'version': 'int',
        'dep_id': 'str',
        'last_modified': 'int'
    }

    attribute_map = {
        'id': 'id',
        'owner': 'owner',
        'link': 'link',
        'runtime': 'runtime',
        'etag': 'etag',
        'size': 'size',
        'name': 'name',
        'description': 'description',
        'file_name': 'file_name',
        'version': 'version',
        'dep_id': 'dep_id',
        'last_modified': 'last_modified'
    }

    def __init__(self, id=None, owner=None, link=None, runtime=None, etag=None, size=None, name=None, description=None, file_name=None, version=None, dep_id=None, last_modified=None):
        r"""Dependency

        The model defined in huaweicloud sdk

        :param id: 依赖包版本ID。
        :type id: str
        :param owner: 依赖包属主的domainId。
        :type owner: str
        :param link: 依赖包在OBS上的链接。
        :type link: str
        :param runtime: FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。
        :type runtime: str
        :param etag: 依赖包的md5值
        :type etag: str
        :param size: 依赖包大小。
        :type size: int
        :param name: 依赖包名称。
        :type name: str
        :param description: 依赖包描述。
        :type description: str
        :param file_name: 依赖包文件名，如果创建方式为zip时。
        :type file_name: str
        :param version: 依赖包版本编号。
        :type version: int
        :param dep_id: 依赖包ID
        :type dep_id: str
        :param last_modified: 依赖包最后一次更新时间。
        :type last_modified: int
        """
        
        

        self._id = None
        self._owner = None
        self._link = None
        self._runtime = None
        self._etag = None
        self._size = None
        self._name = None
        self._description = None
        self._file_name = None
        self._version = None
        self._dep_id = None
        self._last_modified = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.owner = owner
        self.link = link
        self.runtime = runtime
        self.etag = etag
        self.size = size
        self.name = name
        self.description = description
        if file_name is not None:
            self.file_name = file_name
        if version is not None:
            self.version = version
        if dep_id is not None:
            self.dep_id = dep_id
        if last_modified is not None:
            self.last_modified = last_modified

    @property
    def id(self):
        r"""Gets the id of this Dependency.

        依赖包版本ID。

        :return: The id of this Dependency.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Dependency.

        依赖包版本ID。

        :param id: The id of this Dependency.
        :type id: str
        """
        self._id = id

    @property
    def owner(self):
        r"""Gets the owner of this Dependency.

        依赖包属主的domainId。

        :return: The owner of this Dependency.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this Dependency.

        依赖包属主的domainId。

        :param owner: The owner of this Dependency.
        :type owner: str
        """
        self._owner = owner

    @property
    def link(self):
        r"""Gets the link of this Dependency.

        依赖包在OBS上的链接。

        :return: The link of this Dependency.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        r"""Sets the link of this Dependency.

        依赖包在OBS上的链接。

        :param link: The link of this Dependency.
        :type link: str
        """
        self._link = link

    @property
    def runtime(self):
        r"""Gets the runtime of this Dependency.

        FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。

        :return: The runtime of this Dependency.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this Dependency.

        FunctionGraph函数的执行环境 Java8: Java语言8版本。 Java11: Java语言11版本。 Java17: Java语言17版本（当前仅支持华北-乌兰察布二零二） Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Python3.10: Python语言3.10版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 Node.js16.17: Nodejs语言16.17版本。 Node.js18.15: Nodejs语言18.15版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 C#(.NET Core 6.0): C#语言6.0版本（当前仅支持华北-乌兰察布二零二）。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。 Cangjie1.0：仓颉语言1.0版本。 http: HTTP函数。 Custom Image: 自定义镜像函数。

        :param runtime: The runtime of this Dependency.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def etag(self):
        r"""Gets the etag of this Dependency.

        依赖包的md5值

        :return: The etag of this Dependency.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        r"""Sets the etag of this Dependency.

        依赖包的md5值

        :param etag: The etag of this Dependency.
        :type etag: str
        """
        self._etag = etag

    @property
    def size(self):
        r"""Gets the size of this Dependency.

        依赖包大小。

        :return: The size of this Dependency.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this Dependency.

        依赖包大小。

        :param size: The size of this Dependency.
        :type size: int
        """
        self._size = size

    @property
    def name(self):
        r"""Gets the name of this Dependency.

        依赖包名称。

        :return: The name of this Dependency.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Dependency.

        依赖包名称。

        :param name: The name of this Dependency.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this Dependency.

        依赖包描述。

        :return: The description of this Dependency.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Dependency.

        依赖包描述。

        :param description: The description of this Dependency.
        :type description: str
        """
        self._description = description

    @property
    def file_name(self):
        r"""Gets the file_name of this Dependency.

        依赖包文件名，如果创建方式为zip时。

        :return: The file_name of this Dependency.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this Dependency.

        依赖包文件名，如果创建方式为zip时。

        :param file_name: The file_name of this Dependency.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def version(self):
        r"""Gets the version of this Dependency.

        依赖包版本编号。

        :return: The version of this Dependency.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Dependency.

        依赖包版本编号。

        :param version: The version of this Dependency.
        :type version: int
        """
        self._version = version

    @property
    def dep_id(self):
        r"""Gets the dep_id of this Dependency.

        依赖包ID

        :return: The dep_id of this Dependency.
        :rtype: str
        """
        return self._dep_id

    @dep_id.setter
    def dep_id(self, dep_id):
        r"""Sets the dep_id of this Dependency.

        依赖包ID

        :param dep_id: The dep_id of this Dependency.
        :type dep_id: str
        """
        self._dep_id = dep_id

    @property
    def last_modified(self):
        r"""Gets the last_modified of this Dependency.

        依赖包最后一次更新时间。

        :return: The last_modified of this Dependency.
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        r"""Sets the last_modified of this Dependency.

        依赖包最后一次更新时间。

        :param last_modified: The last_modified of this Dependency.
        :type last_modified: int
        """
        self._last_modified = last_modified

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
        if not isinstance(other, Dependency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
