# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Volume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'destination': 'str',
        'key': 'str',
        'name': 'str',
        'read_only': 'bool',
        'source': 'str',
        'type': 'str'
    }

    attribute_map = {
        'destination': 'destination',
        'key': 'key',
        'name': 'name',
        'read_only': 'read_only',
        'source': 'source',
        'type': 'type'
    }

    def __init__(self, destination=None, key=None, name=None, read_only=None, source=None, type=None):
        """Volume

        The model defined in huaweicloud sdk

        :param destination: 卷挂载路径，必须是合法的路径
        :type destination: str
        :param key: 卷的类型，支持configMap,secret,emptyDir,hostPath
        :type key: str
        :param name: 卷名称，小写字母或数字，最长63个字符
        :type name: str
        :param read_only: 读写权限，configMap和secret类型只支持读权限
        :type read_only: bool
        :param source: 卷来源，type为hostPath时输入路径，要求以/开头，后面可包含中划线，反斜杠，下划线，点号，字母，数字； secret时输入secret名称，configMap时输入configMap名称，emptyDir时输入disk或memory
        :type source: str
        :param type: 卷的类型，支持configMap,secret,emptyDir,hostPath
        :type type: str
        """
        
        

        self._destination = None
        self._key = None
        self._name = None
        self._read_only = None
        self._source = None
        self._type = None
        self.discriminator = None

        self.destination = destination
        self.key = key
        self.name = name
        self.read_only = read_only
        self.source = source
        self.type = type

    @property
    def destination(self):
        """Gets the destination of this Volume.

        卷挂载路径，必须是合法的路径

        :return: The destination of this Volume.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this Volume.

        卷挂载路径，必须是合法的路径

        :param destination: The destination of this Volume.
        :type destination: str
        """
        self._destination = destination

    @property
    def key(self):
        """Gets the key of this Volume.

        卷的类型，支持configMap,secret,emptyDir,hostPath

        :return: The key of this Volume.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Volume.

        卷的类型，支持configMap,secret,emptyDir,hostPath

        :param key: The key of this Volume.
        :type key: str
        """
        self._key = key

    @property
    def name(self):
        """Gets the name of this Volume.

        卷名称，小写字母或数字，最长63个字符

        :return: The name of this Volume.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Volume.

        卷名称，小写字母或数字，最长63个字符

        :param name: The name of this Volume.
        :type name: str
        """
        self._name = name

    @property
    def read_only(self):
        """Gets the read_only of this Volume.

        读写权限，configMap和secret类型只支持读权限

        :return: The read_only of this Volume.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this Volume.

        读写权限，configMap和secret类型只支持读权限

        :param read_only: The read_only of this Volume.
        :type read_only: bool
        """
        self._read_only = read_only

    @property
    def source(self):
        """Gets the source of this Volume.

        卷来源，type为hostPath时输入路径，要求以/开头，后面可包含中划线，反斜杠，下划线，点号，字母，数字； secret时输入secret名称，configMap时输入configMap名称，emptyDir时输入disk或memory

        :return: The source of this Volume.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Volume.

        卷来源，type为hostPath时输入路径，要求以/开头，后面可包含中划线，反斜杠，下划线，点号，字母，数字； secret时输入secret名称，configMap时输入configMap名称，emptyDir时输入disk或memory

        :param source: The source of this Volume.
        :type source: str
        """
        self._source = source

    @property
    def type(self):
        """Gets the type of this Volume.

        卷的类型，支持configMap,secret,emptyDir,hostPath

        :return: The type of this Volume.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Volume.

        卷的类型，支持configMap,secret,emptyDir,hostPath

        :param type: The type of this Volume.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, Volume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
