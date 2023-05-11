# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubJobEntities:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_type': 'str',
        'size': 'int',
        'volume_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'volume_type': 'volume_type',
        'size': 'size',
        'volume_id': 'volume_id',
        'name': 'name'
    }

    def __init__(self, volume_type=None, size=None, volume_id=None, name=None):
        """SubJobEntities

        The model defined in huaweicloud sdk

        :param volume_type: 云硬盘的类型。
        :type volume_type: str
        :param size: 云硬盘的容量，单位为GB。
        :type size: int
        :param volume_id: 云硬盘的ID。
        :type volume_id: str
        :param name: 云硬盘的名称。
        :type name: str
        """
        
        

        self._volume_type = None
        self._size = None
        self._volume_id = None
        self._name = None
        self.discriminator = None

        if volume_type is not None:
            self.volume_type = volume_type
        if size is not None:
            self.size = size
        if volume_id is not None:
            self.volume_id = volume_id
        if name is not None:
            self.name = name

    @property
    def volume_type(self):
        """Gets the volume_type of this SubJobEntities.

        云硬盘的类型。

        :return: The volume_type of this SubJobEntities.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this SubJobEntities.

        云硬盘的类型。

        :param volume_type: The volume_type of this SubJobEntities.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def size(self):
        """Gets the size of this SubJobEntities.

        云硬盘的容量，单位为GB。

        :return: The size of this SubJobEntities.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SubJobEntities.

        云硬盘的容量，单位为GB。

        :param size: The size of this SubJobEntities.
        :type size: int
        """
        self._size = size

    @property
    def volume_id(self):
        """Gets the volume_id of this SubJobEntities.

        云硬盘的ID。

        :return: The volume_id of this SubJobEntities.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this SubJobEntities.

        云硬盘的ID。

        :param volume_id: The volume_id of this SubJobEntities.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def name(self):
        """Gets the name of this SubJobEntities.

        云硬盘的名称。

        :return: The name of this SubJobEntities.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubJobEntities.

        云硬盘的名称。

        :param name: The name of this SubJobEntities.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, SubJobEntities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
