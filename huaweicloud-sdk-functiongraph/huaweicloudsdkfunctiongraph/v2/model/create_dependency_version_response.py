# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDependencyVersionResponse(SdkResponse):

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
        """CreateDependencyVersionResponse

        The model defined in huaweicloud sdk

        :param id: 依赖包版本ID。
        :type id: str
        :param owner: 依赖包拥有者。
        :type owner: str
        :param link: 依赖包在obs的存储地址。
        :type link: str
        :param runtime: 运行时语言。
        :type runtime: str
        :param etag: 依赖包唯一标志。
        :type etag: str
        :param size: 依赖包大小。
        :type size: int
        :param name: 依赖包名。
        :type name: str
        :param description: 依赖包描述。
        :type description: str
        :param file_name: 依赖包文件名。
        :type file_name: str
        :param version: 依赖包版本号
        :type version: int
        :param dep_id: 依赖包ID
        :type dep_id: str
        :param last_modified: 依赖包更新时间
        :type last_modified: int
        """
        
        super(CreateDependencyVersionResponse, self).__init__()

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
        if owner is not None:
            self.owner = owner
        if link is not None:
            self.link = link
        if runtime is not None:
            self.runtime = runtime
        if etag is not None:
            self.etag = etag
        if size is not None:
            self.size = size
        if name is not None:
            self.name = name
        if description is not None:
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
        """Gets the id of this CreateDependencyVersionResponse.

        依赖包版本ID。

        :return: The id of this CreateDependencyVersionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateDependencyVersionResponse.

        依赖包版本ID。

        :param id: The id of this CreateDependencyVersionResponse.
        :type id: str
        """
        self._id = id

    @property
    def owner(self):
        """Gets the owner of this CreateDependencyVersionResponse.

        依赖包拥有者。

        :return: The owner of this CreateDependencyVersionResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CreateDependencyVersionResponse.

        依赖包拥有者。

        :param owner: The owner of this CreateDependencyVersionResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def link(self):
        """Gets the link of this CreateDependencyVersionResponse.

        依赖包在obs的存储地址。

        :return: The link of this CreateDependencyVersionResponse.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this CreateDependencyVersionResponse.

        依赖包在obs的存储地址。

        :param link: The link of this CreateDependencyVersionResponse.
        :type link: str
        """
        self._link = link

    @property
    def runtime(self):
        """Gets the runtime of this CreateDependencyVersionResponse.

        运行时语言。

        :return: The runtime of this CreateDependencyVersionResponse.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this CreateDependencyVersionResponse.

        运行时语言。

        :param runtime: The runtime of this CreateDependencyVersionResponse.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def etag(self):
        """Gets the etag of this CreateDependencyVersionResponse.

        依赖包唯一标志。

        :return: The etag of this CreateDependencyVersionResponse.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this CreateDependencyVersionResponse.

        依赖包唯一标志。

        :param etag: The etag of this CreateDependencyVersionResponse.
        :type etag: str
        """
        self._etag = etag

    @property
    def size(self):
        """Gets the size of this CreateDependencyVersionResponse.

        依赖包大小。

        :return: The size of this CreateDependencyVersionResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateDependencyVersionResponse.

        依赖包大小。

        :param size: The size of this CreateDependencyVersionResponse.
        :type size: int
        """
        self._size = size

    @property
    def name(self):
        """Gets the name of this CreateDependencyVersionResponse.

        依赖包名。

        :return: The name of this CreateDependencyVersionResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDependencyVersionResponse.

        依赖包名。

        :param name: The name of this CreateDependencyVersionResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateDependencyVersionResponse.

        依赖包描述。

        :return: The description of this CreateDependencyVersionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDependencyVersionResponse.

        依赖包描述。

        :param description: The description of this CreateDependencyVersionResponse.
        :type description: str
        """
        self._description = description

    @property
    def file_name(self):
        """Gets the file_name of this CreateDependencyVersionResponse.

        依赖包文件名。

        :return: The file_name of this CreateDependencyVersionResponse.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this CreateDependencyVersionResponse.

        依赖包文件名。

        :param file_name: The file_name of this CreateDependencyVersionResponse.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def version(self):
        """Gets the version of this CreateDependencyVersionResponse.

        依赖包版本号

        :return: The version of this CreateDependencyVersionResponse.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateDependencyVersionResponse.

        依赖包版本号

        :param version: The version of this CreateDependencyVersionResponse.
        :type version: int
        """
        self._version = version

    @property
    def dep_id(self):
        """Gets the dep_id of this CreateDependencyVersionResponse.

        依赖包ID

        :return: The dep_id of this CreateDependencyVersionResponse.
        :rtype: str
        """
        return self._dep_id

    @dep_id.setter
    def dep_id(self, dep_id):
        """Sets the dep_id of this CreateDependencyVersionResponse.

        依赖包ID

        :param dep_id: The dep_id of this CreateDependencyVersionResponse.
        :type dep_id: str
        """
        self._dep_id = dep_id

    @property
    def last_modified(self):
        """Gets the last_modified of this CreateDependencyVersionResponse.

        依赖包更新时间

        :return: The last_modified of this CreateDependencyVersionResponse.
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this CreateDependencyVersionResponse.

        依赖包更新时间

        :param last_modified: The last_modified of this CreateDependencyVersionResponse.
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
        if not isinstance(other, CreateDependencyVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
