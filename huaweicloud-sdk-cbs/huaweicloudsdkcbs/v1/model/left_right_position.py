# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LeftRightPosition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'left': 'Position',
        'right': 'Position'
    }

    attribute_map = {
        'left': 'left',
        'right': 'right'
    }

    def __init__(self, left=None, right=None):
        """LeftRightPosition

        The model defined in huaweicloud sdk

        :param left: 
        :type left: :class:`huaweicloudsdkcbs.v1.Position`
        :param right: 
        :type right: :class:`huaweicloudsdkcbs.v1.Position`
        """
        
        

        self._left = None
        self._right = None
        self.discriminator = None

        self.left = left
        self.right = right

    @property
    def left(self):
        """Gets the left of this LeftRightPosition.

        :return: The left of this LeftRightPosition.
        :rtype: :class:`huaweicloudsdkcbs.v1.Position`
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this LeftRightPosition.

        :param left: The left of this LeftRightPosition.
        :type left: :class:`huaweicloudsdkcbs.v1.Position`
        """
        self._left = left

    @property
    def right(self):
        """Gets the right of this LeftRightPosition.

        :return: The right of this LeftRightPosition.
        :rtype: :class:`huaweicloudsdkcbs.v1.Position`
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this LeftRightPosition.

        :param right: The right of this LeftRightPosition.
        :type right: :class:`huaweicloudsdkcbs.v1.Position`
        """
        self._right = right

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
        if not isinstance(other, LeftRightPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
