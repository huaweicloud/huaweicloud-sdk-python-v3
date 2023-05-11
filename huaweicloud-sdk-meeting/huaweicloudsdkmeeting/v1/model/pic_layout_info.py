# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        """PicLayoutInfo

        The model defined in huaweicloud sdk

        :param x: 横向小格子数。
        :type x: int
        :param y: 纵向小格子数。
        :type y: int
        :param sub_pic_layout_info_list: 多画面信息。
        :type sub_pic_layout_info_list: list[:class:`huaweicloudsdkmeeting.v1.SubPicLayoutInfo`]
        """
        
        

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

        横向小格子数。

        :return: The x of this PicLayoutInfo.
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this PicLayoutInfo.

        横向小格子数。

        :param x: The x of this PicLayoutInfo.
        :type x: int
        """
        self._x = x

    @property
    def y(self):
        """Gets the y of this PicLayoutInfo.

        纵向小格子数。

        :return: The y of this PicLayoutInfo.
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this PicLayoutInfo.

        纵向小格子数。

        :param y: The y of this PicLayoutInfo.
        :type y: int
        """
        self._y = y

    @property
    def sub_pic_layout_info_list(self):
        """Gets the sub_pic_layout_info_list of this PicLayoutInfo.

        多画面信息。

        :return: The sub_pic_layout_info_list of this PicLayoutInfo.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.SubPicLayoutInfo`]
        """
        return self._sub_pic_layout_info_list

    @sub_pic_layout_info_list.setter
    def sub_pic_layout_info_list(self, sub_pic_layout_info_list):
        """Sets the sub_pic_layout_info_list of this PicLayoutInfo.

        多画面信息。

        :param sub_pic_layout_info_list: The sub_pic_layout_info_list of this PicLayoutInfo.
        :type sub_pic_layout_info_list: list[:class:`huaweicloudsdkmeeting.v1.SubPicLayoutInfo`]
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
        if not isinstance(other, PicLayoutInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
