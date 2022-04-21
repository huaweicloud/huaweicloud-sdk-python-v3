# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageDetectionResultDetailFaceDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'h': 'int',
        'w': 'int',
        'x': 'int',
        'y': 'int'
    }

    attribute_map = {
        'h': 'h',
        'w': 'w',
        'x': 'x',
        'y': 'y'
    }

    def __init__(self, h=None, w=None, x=None, y=None):
        """ImageDetectionResultDetailFaceDetail

        The model defined in huaweicloud sdk

        :param h: 人脸区域高度。
        :type h: int
        :param w: 人脸区域宽度。
        :type w: int
        :param x: 人脸区域左上角到y轴距离。
        :type x: int
        :param y: 人脸区域左上角到x轴距离。
        :type y: int
        """
        
        

        self._h = None
        self._w = None
        self._x = None
        self._y = None
        self.discriminator = None

        if h is not None:
            self.h = h
        if w is not None:
            self.w = w
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    @property
    def h(self):
        """Gets the h of this ImageDetectionResultDetailFaceDetail.

        人脸区域高度。

        :return: The h of this ImageDetectionResultDetailFaceDetail.
        :rtype: int
        """
        return self._h

    @h.setter
    def h(self, h):
        """Sets the h of this ImageDetectionResultDetailFaceDetail.

        人脸区域高度。

        :param h: The h of this ImageDetectionResultDetailFaceDetail.
        :type h: int
        """
        self._h = h

    @property
    def w(self):
        """Gets the w of this ImageDetectionResultDetailFaceDetail.

        人脸区域宽度。

        :return: The w of this ImageDetectionResultDetailFaceDetail.
        :rtype: int
        """
        return self._w

    @w.setter
    def w(self, w):
        """Sets the w of this ImageDetectionResultDetailFaceDetail.

        人脸区域宽度。

        :param w: The w of this ImageDetectionResultDetailFaceDetail.
        :type w: int
        """
        self._w = w

    @property
    def x(self):
        """Gets the x of this ImageDetectionResultDetailFaceDetail.

        人脸区域左上角到y轴距离。

        :return: The x of this ImageDetectionResultDetailFaceDetail.
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this ImageDetectionResultDetailFaceDetail.

        人脸区域左上角到y轴距离。

        :param x: The x of this ImageDetectionResultDetailFaceDetail.
        :type x: int
        """
        self._x = x

    @property
    def y(self):
        """Gets the y of this ImageDetectionResultDetailFaceDetail.

        人脸区域左上角到x轴距离。

        :return: The y of this ImageDetectionResultDetailFaceDetail.
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this ImageDetectionResultDetailFaceDetail.

        人脸区域左上角到x轴距离。

        :param y: The y of this ImageDetectionResultDetailFaceDetail.
        :type y: int
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
        if not isinstance(other, ImageDetectionResultDetailFaceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
