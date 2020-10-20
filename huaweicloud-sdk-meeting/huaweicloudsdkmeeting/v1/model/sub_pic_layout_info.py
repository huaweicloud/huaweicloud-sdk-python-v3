# coding: utf-8

import pprint
import re

import six





class SubPicLayoutInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'left': 'int',
        'top': 'int',
        'x_size': 'int',
        'y_size': 'int'
    }

    attribute_map = {
        'id': 'id',
        'left': 'left',
        'top': 'top',
        'x_size': 'xSize',
        'y_size': 'ySize'
    }

    def __init__(self, id=None, left=None, top=None, x_size=None, y_size=None):
        """SubPicLayoutInfo - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._left = None
        self._top = None
        self._x_size = None
        self._y_size = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if left is not None:
            self.left = left
        if top is not None:
            self.top = top
        if x_size is not None:
            self.x_size = x_size
        if y_size is not None:
            self.y_size = y_size

    @property
    def id(self):
        """Gets the id of this SubPicLayoutInfo.

        画面索引号

        :return: The id of this SubPicLayoutInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubPicLayoutInfo.

        画面索引号

        :param id: The id of this SubPicLayoutInfo.
        :type: int
        """
        self._id = id

    @property
    def left(self):
        """Gets the left of this SubPicLayoutInfo.

        画面从左到右的坐标点

        :return: The left of this SubPicLayoutInfo.
        :rtype: int
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this SubPicLayoutInfo.

        画面从左到右的坐标点

        :param left: The left of this SubPicLayoutInfo.
        :type: int
        """
        self._left = left

    @property
    def top(self):
        """Gets the top of this SubPicLayoutInfo.

        画面从上到下的坐标点

        :return: The top of this SubPicLayoutInfo.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this SubPicLayoutInfo.

        画面从上到下的坐标点

        :param top: The top of this SubPicLayoutInfo.
        :type: int
        """
        self._top = top

    @property
    def x_size(self):
        """Gets the x_size of this SubPicLayoutInfo.

        小画面的宽度

        :return: The x_size of this SubPicLayoutInfo.
        :rtype: int
        """
        return self._x_size

    @x_size.setter
    def x_size(self, x_size):
        """Sets the x_size of this SubPicLayoutInfo.

        小画面的宽度

        :param x_size: The x_size of this SubPicLayoutInfo.
        :type: int
        """
        self._x_size = x_size

    @property
    def y_size(self):
        """Gets the y_size of this SubPicLayoutInfo.

        小画面的高度

        :return: The y_size of this SubPicLayoutInfo.
        :rtype: int
        """
        return self._y_size

    @y_size.setter
    def y_size(self, y_size):
        """Sets the y_size of this SubPicLayoutInfo.

        小画面的高度

        :param y_size: The y_size of this SubPicLayoutInfo.
        :type: int
        """
        self._y_size = y_size

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubPicLayoutInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
