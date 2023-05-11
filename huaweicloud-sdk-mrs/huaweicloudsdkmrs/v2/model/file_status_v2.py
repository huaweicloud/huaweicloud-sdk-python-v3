# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileStatusV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path_suffix': 'str',
        'owner': 'str',
        'group': 'str',
        'permission': 'str',
        'replication': 'int',
        'block_size': 'int',
        'length': 'int',
        'type': 'str',
        'children_num': 'int',
        'access_time': 'int',
        'modification_time': 'int'
    }

    attribute_map = {
        'path_suffix': 'path_suffix',
        'owner': 'owner',
        'group': 'group',
        'permission': 'permission',
        'replication': 'replication',
        'block_size': 'block_size',
        'length': 'length',
        'type': 'type',
        'children_num': 'children_num',
        'access_time': 'access_time',
        'modification_time': 'modification_time'
    }

    def __init__(self, path_suffix=None, owner=None, group=None, permission=None, replication=None, block_size=None, length=None, type=None, children_num=None, access_time=None, modification_time=None):
        """FileStatusV2

        The model defined in huaweicloud sdk

        :param path_suffix: 文件在当前目录下的后缀，如获取“/tmp”目录，下面的“/tmp/test”文件，此处path_suffix内容为“test”。
        :type path_suffix: str
        :param owner: 文件拥有者。
        :type owner: str
        :param group: 文件属组。
        :type group: str
        :param permission: 权限信息。
        :type permission: str
        :param replication: 副本数。
        :type replication: int
        :param block_size: 块大小。
        :type block_size: int
        :param length: 文件长度。
        :type length: int
        :param type: 文件类型： - FILE：文件 - DIRECTORY：目录
        :type type: str
        :param children_num: 该目录下的文件条目数。
        :type children_num: int
        :param access_time: 文件访问时间。
        :type access_time: int
        :param modification_time: 文件修改时间。
        :type modification_time: int
        """
        
        

        self._path_suffix = None
        self._owner = None
        self._group = None
        self._permission = None
        self._replication = None
        self._block_size = None
        self._length = None
        self._type = None
        self._children_num = None
        self._access_time = None
        self._modification_time = None
        self.discriminator = None

        if path_suffix is not None:
            self.path_suffix = path_suffix
        if owner is not None:
            self.owner = owner
        if group is not None:
            self.group = group
        if permission is not None:
            self.permission = permission
        if replication is not None:
            self.replication = replication
        if block_size is not None:
            self.block_size = block_size
        if length is not None:
            self.length = length
        if type is not None:
            self.type = type
        if children_num is not None:
            self.children_num = children_num
        if access_time is not None:
            self.access_time = access_time
        if modification_time is not None:
            self.modification_time = modification_time

    @property
    def path_suffix(self):
        """Gets the path_suffix of this FileStatusV2.

        文件在当前目录下的后缀，如获取“/tmp”目录，下面的“/tmp/test”文件，此处path_suffix内容为“test”。

        :return: The path_suffix of this FileStatusV2.
        :rtype: str
        """
        return self._path_suffix

    @path_suffix.setter
    def path_suffix(self, path_suffix):
        """Sets the path_suffix of this FileStatusV2.

        文件在当前目录下的后缀，如获取“/tmp”目录，下面的“/tmp/test”文件，此处path_suffix内容为“test”。

        :param path_suffix: The path_suffix of this FileStatusV2.
        :type path_suffix: str
        """
        self._path_suffix = path_suffix

    @property
    def owner(self):
        """Gets the owner of this FileStatusV2.

        文件拥有者。

        :return: The owner of this FileStatusV2.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this FileStatusV2.

        文件拥有者。

        :param owner: The owner of this FileStatusV2.
        :type owner: str
        """
        self._owner = owner

    @property
    def group(self):
        """Gets the group of this FileStatusV2.

        文件属组。

        :return: The group of this FileStatusV2.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this FileStatusV2.

        文件属组。

        :param group: The group of this FileStatusV2.
        :type group: str
        """
        self._group = group

    @property
    def permission(self):
        """Gets the permission of this FileStatusV2.

        权限信息。

        :return: The permission of this FileStatusV2.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this FileStatusV2.

        权限信息。

        :param permission: The permission of this FileStatusV2.
        :type permission: str
        """
        self._permission = permission

    @property
    def replication(self):
        """Gets the replication of this FileStatusV2.

        副本数。

        :return: The replication of this FileStatusV2.
        :rtype: int
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        """Sets the replication of this FileStatusV2.

        副本数。

        :param replication: The replication of this FileStatusV2.
        :type replication: int
        """
        self._replication = replication

    @property
    def block_size(self):
        """Gets the block_size of this FileStatusV2.

        块大小。

        :return: The block_size of this FileStatusV2.
        :rtype: int
        """
        return self._block_size

    @block_size.setter
    def block_size(self, block_size):
        """Sets the block_size of this FileStatusV2.

        块大小。

        :param block_size: The block_size of this FileStatusV2.
        :type block_size: int
        """
        self._block_size = block_size

    @property
    def length(self):
        """Gets the length of this FileStatusV2.

        文件长度。

        :return: The length of this FileStatusV2.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this FileStatusV2.

        文件长度。

        :param length: The length of this FileStatusV2.
        :type length: int
        """
        self._length = length

    @property
    def type(self):
        """Gets the type of this FileStatusV2.

        文件类型： - FILE：文件 - DIRECTORY：目录

        :return: The type of this FileStatusV2.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileStatusV2.

        文件类型： - FILE：文件 - DIRECTORY：目录

        :param type: The type of this FileStatusV2.
        :type type: str
        """
        self._type = type

    @property
    def children_num(self):
        """Gets the children_num of this FileStatusV2.

        该目录下的文件条目数。

        :return: The children_num of this FileStatusV2.
        :rtype: int
        """
        return self._children_num

    @children_num.setter
    def children_num(self, children_num):
        """Sets the children_num of this FileStatusV2.

        该目录下的文件条目数。

        :param children_num: The children_num of this FileStatusV2.
        :type children_num: int
        """
        self._children_num = children_num

    @property
    def access_time(self):
        """Gets the access_time of this FileStatusV2.

        文件访问时间。

        :return: The access_time of this FileStatusV2.
        :rtype: int
        """
        return self._access_time

    @access_time.setter
    def access_time(self, access_time):
        """Sets the access_time of this FileStatusV2.

        文件访问时间。

        :param access_time: The access_time of this FileStatusV2.
        :type access_time: int
        """
        self._access_time = access_time

    @property
    def modification_time(self):
        """Gets the modification_time of this FileStatusV2.

        文件修改时间。

        :return: The modification_time of this FileStatusV2.
        :rtype: int
        """
        return self._modification_time

    @modification_time.setter
    def modification_time(self, modification_time):
        """Sets the modification_time of this FileStatusV2.

        文件修改时间。

        :param modification_time: The modification_time of this FileStatusV2.
        :type modification_time: int
        """
        self._modification_time = modification_time

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
        if not isinstance(other, FileStatusV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
