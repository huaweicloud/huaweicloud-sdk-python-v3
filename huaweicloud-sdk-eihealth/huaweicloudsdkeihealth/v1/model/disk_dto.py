# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiskDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'space': 'str'
    }

    attribute_map = {
        'type': 'type',
        'space': 'space'
    }

    def __init__(self, type=None, space=None):
        """DiskDto

        The model defined in huaweicloud sdk

        :param type: 磁盘类型
        :type type: str
        :param space: 磁盘大小
        :type space: str
        """
        
        

        self._type = None
        self._space = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if space is not None:
            self.space = space

    @property
    def type(self):
        """Gets the type of this DiskDto.

        磁盘类型

        :return: The type of this DiskDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DiskDto.

        磁盘类型

        :param type: The type of this DiskDto.
        :type type: str
        """
        self._type = type

    @property
    def space(self):
        """Gets the space of this DiskDto.

        磁盘大小

        :return: The space of this DiskDto.
        :rtype: str
        """
        return self._space

    @space.setter
    def space(self, space):
        """Sets the space of this DiskDto.

        磁盘大小

        :param space: The space of this DiskDto.
        :type space: str
        """
        self._space = space

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
        if not isinstance(other, DiskDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
