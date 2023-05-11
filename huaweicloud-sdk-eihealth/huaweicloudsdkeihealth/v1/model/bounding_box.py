# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BoundingBox:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'center': 'list[float]',
        'size': 'list[float]'
    }

    attribute_map = {
        'center': 'center',
        'size': 'size'
    }

    def __init__(self, center=None, size=None):
        """BoundingBox

        The model defined in huaweicloud sdk

        :param center: 口袋中心坐标; x, y, z轴的坐标
        :type center: list[float]
        :param size: 口袋尺寸大小;  x, y, z轴的大小
        :type size: list[float]
        """
        
        

        self._center = None
        self._size = None
        self.discriminator = None

        if center is not None:
            self.center = center
        if size is not None:
            self.size = size

    @property
    def center(self):
        """Gets the center of this BoundingBox.

        口袋中心坐标; x, y, z轴的坐标

        :return: The center of this BoundingBox.
        :rtype: list[float]
        """
        return self._center

    @center.setter
    def center(self, center):
        """Sets the center of this BoundingBox.

        口袋中心坐标; x, y, z轴的坐标

        :param center: The center of this BoundingBox.
        :type center: list[float]
        """
        self._center = center

    @property
    def size(self):
        """Gets the size of this BoundingBox.

        口袋尺寸大小;  x, y, z轴的大小

        :return: The size of this BoundingBox.
        :rtype: list[float]
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BoundingBox.

        口袋尺寸大小;  x, y, z轴的大小

        :param size: The size of this BoundingBox.
        :type size: list[float]
        """
        self._size = size

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
        if not isinstance(other, BoundingBox):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
