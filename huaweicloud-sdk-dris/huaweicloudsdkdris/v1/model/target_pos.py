# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetPos:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'left_top_x': 'int',
        'left_top_y': 'int',
        'right_bottom_x': 'int',
        'right_bottom_y': 'int'
    }

    attribute_map = {
        'left_top_x': 'left_top_x',
        'left_top_y': 'left_top_y',
        'right_bottom_x': 'right_bottom_x',
        'right_bottom_y': 'right_bottom_y'
    }

    def __init__(self, left_top_x=None, left_top_y=None, right_bottom_x=None, right_bottom_y=None):
        """TargetPos

        The model defined in huaweicloud sdk

        :param left_top_x: **参数说明**：目标区域框左上X坐标。
        :type left_top_x: int
        :param left_top_y: **参数说明**：目标区域框左上Y坐标。
        :type left_top_y: int
        :param right_bottom_x: **参数说明**：目标区域框右下X坐标。
        :type right_bottom_x: int
        :param right_bottom_y: **参数说明**：目标区域框右下Y坐标。
        :type right_bottom_y: int
        """
        
        

        self._left_top_x = None
        self._left_top_y = None
        self._right_bottom_x = None
        self._right_bottom_y = None
        self.discriminator = None

        if left_top_x is not None:
            self.left_top_x = left_top_x
        if left_top_y is not None:
            self.left_top_y = left_top_y
        if right_bottom_x is not None:
            self.right_bottom_x = right_bottom_x
        if right_bottom_y is not None:
            self.right_bottom_y = right_bottom_y

    @property
    def left_top_x(self):
        """Gets the left_top_x of this TargetPos.

        **参数说明**：目标区域框左上X坐标。

        :return: The left_top_x of this TargetPos.
        :rtype: int
        """
        return self._left_top_x

    @left_top_x.setter
    def left_top_x(self, left_top_x):
        """Sets the left_top_x of this TargetPos.

        **参数说明**：目标区域框左上X坐标。

        :param left_top_x: The left_top_x of this TargetPos.
        :type left_top_x: int
        """
        self._left_top_x = left_top_x

    @property
    def left_top_y(self):
        """Gets the left_top_y of this TargetPos.

        **参数说明**：目标区域框左上Y坐标。

        :return: The left_top_y of this TargetPos.
        :rtype: int
        """
        return self._left_top_y

    @left_top_y.setter
    def left_top_y(self, left_top_y):
        """Sets the left_top_y of this TargetPos.

        **参数说明**：目标区域框左上Y坐标。

        :param left_top_y: The left_top_y of this TargetPos.
        :type left_top_y: int
        """
        self._left_top_y = left_top_y

    @property
    def right_bottom_x(self):
        """Gets the right_bottom_x of this TargetPos.

        **参数说明**：目标区域框右下X坐标。

        :return: The right_bottom_x of this TargetPos.
        :rtype: int
        """
        return self._right_bottom_x

    @right_bottom_x.setter
    def right_bottom_x(self, right_bottom_x):
        """Sets the right_bottom_x of this TargetPos.

        **参数说明**：目标区域框右下X坐标。

        :param right_bottom_x: The right_bottom_x of this TargetPos.
        :type right_bottom_x: int
        """
        self._right_bottom_x = right_bottom_x

    @property
    def right_bottom_y(self):
        """Gets the right_bottom_y of this TargetPos.

        **参数说明**：目标区域框右下Y坐标。

        :return: The right_bottom_y of this TargetPos.
        :rtype: int
        """
        return self._right_bottom_y

    @right_bottom_y.setter
    def right_bottom_y(self, right_bottom_y):
        """Sets the right_bottom_y of this TargetPos.

        **参数说明**：目标区域框右下Y坐标。

        :param right_bottom_y: The right_bottom_y of this TargetPos.
        :type right_bottom_y: int
        """
        self._right_bottom_y = right_bottom_y

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
        if not isinstance(other, TargetPos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
