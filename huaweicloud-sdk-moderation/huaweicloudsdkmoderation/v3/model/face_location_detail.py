# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FaceLocationDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top_left_x': 'int',
        'top_left_y': 'int',
        'bottom_right_x': 'int',
        'bottom_right_y': 'int'
    }

    attribute_map = {
        'top_left_x': 'top_left_x',
        'top_left_y': 'top_left_y',
        'bottom_right_x': 'bottom_right_x',
        'bottom_right_y': 'bottom_right_y'
    }

    def __init__(self, top_left_x=None, top_left_y=None, bottom_right_x=None, bottom_right_y=None):
        """FaceLocationDetail

        The model defined in huaweicloud sdk

        :param top_left_x: 检测出人脸的左上角横坐标。
        :type top_left_x: int
        :param top_left_y: 检测出人脸的左上角纵坐标。
        :type top_left_y: int
        :param bottom_right_x: 检测出人脸的右下角横坐标。
        :type bottom_right_x: int
        :param bottom_right_y: 检测出人脸的右下角纵坐标。
        :type bottom_right_y: int
        """
        
        

        self._top_left_x = None
        self._top_left_y = None
        self._bottom_right_x = None
        self._bottom_right_y = None
        self.discriminator = None

        if top_left_x is not None:
            self.top_left_x = top_left_x
        if top_left_y is not None:
            self.top_left_y = top_left_y
        if bottom_right_x is not None:
            self.bottom_right_x = bottom_right_x
        if bottom_right_y is not None:
            self.bottom_right_y = bottom_right_y

    @property
    def top_left_x(self):
        """Gets the top_left_x of this FaceLocationDetail.

        检测出人脸的左上角横坐标。

        :return: The top_left_x of this FaceLocationDetail.
        :rtype: int
        """
        return self._top_left_x

    @top_left_x.setter
    def top_left_x(self, top_left_x):
        """Sets the top_left_x of this FaceLocationDetail.

        检测出人脸的左上角横坐标。

        :param top_left_x: The top_left_x of this FaceLocationDetail.
        :type top_left_x: int
        """
        self._top_left_x = top_left_x

    @property
    def top_left_y(self):
        """Gets the top_left_y of this FaceLocationDetail.

        检测出人脸的左上角纵坐标。

        :return: The top_left_y of this FaceLocationDetail.
        :rtype: int
        """
        return self._top_left_y

    @top_left_y.setter
    def top_left_y(self, top_left_y):
        """Sets the top_left_y of this FaceLocationDetail.

        检测出人脸的左上角纵坐标。

        :param top_left_y: The top_left_y of this FaceLocationDetail.
        :type top_left_y: int
        """
        self._top_left_y = top_left_y

    @property
    def bottom_right_x(self):
        """Gets the bottom_right_x of this FaceLocationDetail.

        检测出人脸的右下角横坐标。

        :return: The bottom_right_x of this FaceLocationDetail.
        :rtype: int
        """
        return self._bottom_right_x

    @bottom_right_x.setter
    def bottom_right_x(self, bottom_right_x):
        """Sets the bottom_right_x of this FaceLocationDetail.

        检测出人脸的右下角横坐标。

        :param bottom_right_x: The bottom_right_x of this FaceLocationDetail.
        :type bottom_right_x: int
        """
        self._bottom_right_x = bottom_right_x

    @property
    def bottom_right_y(self):
        """Gets the bottom_right_y of this FaceLocationDetail.

        检测出人脸的右下角纵坐标。

        :return: The bottom_right_y of this FaceLocationDetail.
        :rtype: int
        """
        return self._bottom_right_y

    @bottom_right_y.setter
    def bottom_right_y(self, bottom_right_y):
        """Sets the bottom_right_y of this FaceLocationDetail.

        检测出人脸的右下角纵坐标。

        :param bottom_right_y: The bottom_right_y of this FaceLocationDetail.
        :type bottom_right_y: int
        """
        self._bottom_right_y = bottom_right_y

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
        if not isinstance(other, FaceLocationDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
