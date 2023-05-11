# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeDTO:

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
        """VolumeDTO

        The model defined in huaweicloud sdk

        :param name: 卷名称
        :type name: str
        :param type: 挂载类型
        :type type: str
        :param source: 源路径
        :type source: str
        :param destination: 卷挂载路径
        :type destination: str
        :param read_only: 只读，默认只读
        :type read_only: bool
        """
        
        

        self._name = None
        self._type = None
        self._source = None
        self._destination = None
        self._read_only = None
        self.discriminator = None

        self.name = name
        if type is not None:
            self.type = type
        self.source = source
        self.destination = destination
        if read_only is not None:
            self.read_only = read_only

    @property
    def name(self):
        """Gets the name of this VolumeDTO.

        卷名称

        :return: The name of this VolumeDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumeDTO.

        卷名称

        :param name: The name of this VolumeDTO.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this VolumeDTO.

        挂载类型

        :return: The type of this VolumeDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VolumeDTO.

        挂载类型

        :param type: The type of this VolumeDTO.
        :type type: str
        """
        self._type = type

    @property
    def source(self):
        """Gets the source of this VolumeDTO.

        源路径

        :return: The source of this VolumeDTO.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this VolumeDTO.

        源路径

        :param source: The source of this VolumeDTO.
        :type source: str
        """
        self._source = source

    @property
    def destination(self):
        """Gets the destination of this VolumeDTO.

        卷挂载路径

        :return: The destination of this VolumeDTO.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this VolumeDTO.

        卷挂载路径

        :param destination: The destination of this VolumeDTO.
        :type destination: str
        """
        self._destination = destination

    @property
    def read_only(self):
        """Gets the read_only of this VolumeDTO.

        只读，默认只读

        :return: The read_only of this VolumeDTO.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this VolumeDTO.

        只读，默认只读

        :param read_only: The read_only of this VolumeDTO.
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
        if not isinstance(other, VolumeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
