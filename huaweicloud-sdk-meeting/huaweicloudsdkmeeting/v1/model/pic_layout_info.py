# coding: utf-8

import pprint
import re

import six





class PicLayoutInfo:


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
        'y': 'int',
        'sub_pic_layout_info_list': 'list[SubPicLayoutInfo]'
    }

    attribute_map = {
        'x': 'x',
        'y': 'y',
        'sub_pic_layout_info_list': 'subPicLayoutInfoList'
    }

    def __init__(self, x=None, y=None, sub_pic_layout_info_list=None):
        """PicLayoutInfo - a model defined in huaweicloud sdk"""
        
        

        self._x = None
        self._y = None
        self._sub_pic_layout_info_list = None
        self.discriminator = None

        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if sub_pic_layout_info_list is not None:
            self.sub_pic_layout_info_list = sub_pic_layout_info_list

    @property
    def x(self):
        """Gets the x of this PicLayoutInfo.

        多画面布局的宽度

        :return: The x of this PicLayoutInfo.
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this PicLayoutInfo.

        多画面布局的宽度

        :param x: The x of this PicLayoutInfo.
        :type: int
        """
        self._x = x

    @property
    def y(self):
        """Gets the y of this PicLayoutInfo.

        多画面布局的高度

        :return: The y of this PicLayoutInfo.
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this PicLayoutInfo.

        多画面布局的高度

        :param y: The y of this PicLayoutInfo.
        :type: int
        """
        self._y = y

    @property
    def sub_pic_layout_info_list(self):
        """Gets the sub_pic_layout_info_list of this PicLayoutInfo.

        子画面布局具体列表

        :return: The sub_pic_layout_info_list of this PicLayoutInfo.
        :rtype: list[SubPicLayoutInfo]
        """
        return self._sub_pic_layout_info_list

    @sub_pic_layout_info_list.setter
    def sub_pic_layout_info_list(self, sub_pic_layout_info_list):
        """Sets the sub_pic_layout_info_list of this PicLayoutInfo.

        子画面布局具体列表

        :param sub_pic_layout_info_list: The sub_pic_layout_info_list of this PicLayoutInfo.
        :type: list[SubPicLayoutInfo]
        """
        self._sub_pic_layout_info_list = sub_pic_layout_info_list

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
        if not isinstance(other, PicLayoutInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
