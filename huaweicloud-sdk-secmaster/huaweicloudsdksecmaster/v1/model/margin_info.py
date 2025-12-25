# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MarginInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top': 'int',
        'left': 'int',
        'bottom': 'int',
        'right': 'int'
    }

    attribute_map = {
        'top': 'top',
        'left': 'left',
        'bottom': 'bottom',
        'right': 'right'
    }

    def __init__(self, top=None, left=None, bottom=None, right=None):
        r"""MarginInfo

        The model defined in huaweicloud sdk

        :param top: 安全报告的上边距
        :type top: int
        :param left: 安全报告的左边距
        :type left: int
        :param bottom: 安全报告的下边距
        :type bottom: int
        :param right: 安全报告的右边距
        :type right: int
        """
        
        

        self._top = None
        self._left = None
        self._bottom = None
        self._right = None
        self.discriminator = None

        if top is not None:
            self.top = top
        if left is not None:
            self.left = left
        if bottom is not None:
            self.bottom = bottom
        if right is not None:
            self.right = right

    @property
    def top(self):
        r"""Gets the top of this MarginInfo.

        安全报告的上边距

        :return: The top of this MarginInfo.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        r"""Sets the top of this MarginInfo.

        安全报告的上边距

        :param top: The top of this MarginInfo.
        :type top: int
        """
        self._top = top

    @property
    def left(self):
        r"""Gets the left of this MarginInfo.

        安全报告的左边距

        :return: The left of this MarginInfo.
        :rtype: int
        """
        return self._left

    @left.setter
    def left(self, left):
        r"""Sets the left of this MarginInfo.

        安全报告的左边距

        :param left: The left of this MarginInfo.
        :type left: int
        """
        self._left = left

    @property
    def bottom(self):
        r"""Gets the bottom of this MarginInfo.

        安全报告的下边距

        :return: The bottom of this MarginInfo.
        :rtype: int
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        r"""Sets the bottom of this MarginInfo.

        安全报告的下边距

        :param bottom: The bottom of this MarginInfo.
        :type bottom: int
        """
        self._bottom = bottom

    @property
    def right(self):
        r"""Gets the right of this MarginInfo.

        安全报告的右边距

        :return: The right of this MarginInfo.
        :rtype: int
        """
        return self._right

    @right.setter
    def right(self, right):
        r"""Sets the right of this MarginInfo.

        安全报告的右边距

        :param right: The right of this MarginInfo.
        :type right: int
        """
        self._right = right

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MarginInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
