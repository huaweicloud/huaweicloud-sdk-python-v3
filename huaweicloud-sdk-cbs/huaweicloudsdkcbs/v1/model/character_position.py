# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CharacterPosition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x': 'int',
        'y': 'str'
    }

    attribute_map = {
        'x': 'x',
        'y': 'y'
    }

    def __init__(self, x=None, y=None):
        r"""CharacterPosition

        The model defined in huaweicloud sdk

        :param x: 从左上为0点出发的横坐标
        :type x: int
        :param y: 从左上为0点出发的纵坐标
        :type y: str
        """
        
        

        self._x = None
        self._y = None
        self.discriminator = None

        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    @property
    def x(self):
        r"""Gets the x of this CharacterPosition.

        从左上为0点出发的横坐标

        :return: The x of this CharacterPosition.
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        r"""Sets the x of this CharacterPosition.

        从左上为0点出发的横坐标

        :param x: The x of this CharacterPosition.
        :type x: int
        """
        self._x = x

    @property
    def y(self):
        r"""Gets the y of this CharacterPosition.

        从左上为0点出发的纵坐标

        :return: The y of this CharacterPosition.
        :rtype: str
        """
        return self._y

    @y.setter
    def y(self, y):
        r"""Sets the y of this CharacterPosition.

        从左上为0点出发的纵坐标

        :param y: The y of this CharacterPosition.
        :type y: str
        """
        self._y = y

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
        if not isinstance(other, CharacterPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
