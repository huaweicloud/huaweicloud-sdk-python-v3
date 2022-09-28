# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IoAccInfoDto:

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
        'type': 'str',
        'space': 'int',
        'free_space': 'float'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'space': 'space',
        'free_space': 'free_space'
    }

    def __init__(self, id=None, type=None, space=None, free_space=None):
        """IoAccInfoDto

        The model defined in huaweicloud sdk

        :param id: io加速实例id
        :type id: str
        :param type: io加速实例类型
        :type type: str
        :param space: io加速实例总容量
        :type space: int
        :param free_space: io加速实例空闲容量
        :type free_space: float
        """
        
        

        self._id = None
        self._type = None
        self._space = None
        self._free_space = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if space is not None:
            self.space = space
        if free_space is not None:
            self.free_space = free_space

    @property
    def id(self):
        """Gets the id of this IoAccInfoDto.

        io加速实例id

        :return: The id of this IoAccInfoDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IoAccInfoDto.

        io加速实例id

        :param id: The id of this IoAccInfoDto.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this IoAccInfoDto.

        io加速实例类型

        :return: The type of this IoAccInfoDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoAccInfoDto.

        io加速实例类型

        :param type: The type of this IoAccInfoDto.
        :type type: str
        """
        self._type = type

    @property
    def space(self):
        """Gets the space of this IoAccInfoDto.

        io加速实例总容量

        :return: The space of this IoAccInfoDto.
        :rtype: int
        """
        return self._space

    @space.setter
    def space(self, space):
        """Sets the space of this IoAccInfoDto.

        io加速实例总容量

        :param space: The space of this IoAccInfoDto.
        :type space: int
        """
        self._space = space

    @property
    def free_space(self):
        """Gets the free_space of this IoAccInfoDto.

        io加速实例空闲容量

        :return: The free_space of this IoAccInfoDto.
        :rtype: float
        """
        return self._free_space

    @free_space.setter
    def free_space(self, free_space):
        """Sets the free_space of this IoAccInfoDto.

        io加速实例空闲容量

        :param free_space: The free_space of this IoAccInfoDto.
        :type free_space: float
        """
        self._free_space = free_space

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
        if not isinstance(other, IoAccInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
