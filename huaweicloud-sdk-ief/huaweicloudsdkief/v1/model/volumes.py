# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Volumes:

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
        'type': 'str',
        'source': 'str',
        'destination': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'source': 'source',
        'destination': 'destination',
        'read_only': 'read_only'
    }

    def __init__(self, name=None, type=None, source=None, destination=None, read_only=None):
        """Volumes

        The model defined in huaweicloud sdk

        :param name: 卷名称，小写字母或数字，最长63个字符
        :type name: str
        :param type: 卷的类型，支持configMap,secret,emptyDir,hostPath
        :type type: str
        :param source: 卷来源，type为hostPath时输入路径，要求以/开头，后面可包含中划线，反斜杠，下划线，点号，字母，数字； secret时输入secret名称，configMap时输入configMap名称，emptyDir时输入disk或memory
        :type source: str
        :param destination: 卷挂载路径，必须是合法的路径
        :type destination: str
        :param read_only: 读写权限，configMap和secret类型只支持读权限
        :type read_only: bool
        """
        
        

        self._name = None
        self._type = None
        self._source = None
        self._destination = None
        self._read_only = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.source = source
        self.destination = destination
        if read_only is not None:
            self.read_only = read_only

    @property
    def name(self):
        """Gets the name of this Volumes.

        卷名称，小写字母或数字，最长63个字符

        :return: The name of this Volumes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Volumes.

        卷名称，小写字母或数字，最长63个字符

        :param name: The name of this Volumes.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this Volumes.

        卷的类型，支持configMap,secret,emptyDir,hostPath

        :return: The type of this Volumes.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Volumes.

        卷的类型，支持configMap,secret,emptyDir,hostPath

        :param type: The type of this Volumes.
        :type type: str
        """
        self._type = type

    @property
    def source(self):
        """Gets the source of this Volumes.

        卷来源，type为hostPath时输入路径，要求以/开头，后面可包含中划线，反斜杠，下划线，点号，字母，数字； secret时输入secret名称，configMap时输入configMap名称，emptyDir时输入disk或memory

        :return: The source of this Volumes.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Volumes.

        卷来源，type为hostPath时输入路径，要求以/开头，后面可包含中划线，反斜杠，下划线，点号，字母，数字； secret时输入secret名称，configMap时输入configMap名称，emptyDir时输入disk或memory

        :param source: The source of this Volumes.
        :type source: str
        """
        self._source = source

    @property
    def destination(self):
        """Gets the destination of this Volumes.

        卷挂载路径，必须是合法的路径

        :return: The destination of this Volumes.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this Volumes.

        卷挂载路径，必须是合法的路径

        :param destination: The destination of this Volumes.
        :type destination: str
        """
        self._destination = destination

    @property
    def read_only(self):
        """Gets the read_only of this Volumes.

        读写权限，configMap和secret类型只支持读权限

        :return: The read_only of this Volumes.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this Volumes.

        读写权限，configMap和secret类型只支持读权限

        :param read_only: The read_only of this Volumes.
        :type read_only: bool
        """
        self._read_only = read_only

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
        if not isinstance(other, Volumes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
