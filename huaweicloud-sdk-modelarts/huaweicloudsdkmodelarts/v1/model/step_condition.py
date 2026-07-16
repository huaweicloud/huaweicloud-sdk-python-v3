# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StepCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'left': 'object',
        'right': 'object'
    }

    attribute_map = {
        'type': 'type',
        'left': 'left',
        'right': 'right'
    }

    def __init__(self, type=None, left=None, right=None):
        r"""StepCondition

        The model defined in huaweicloud sdk

        :param type: 判断类型，例如&#x3D;&#x3D;（等于）、!&#x3D;（不等于）、&gt;（大于）、&gt;&#x3D;（大于等于）、&lt;（小于）、&lt;&#x3D;（小于等于）、in（包含）、or（或）。
        :type type: str
        :param left: 节点执行条件为true时的分支。
        :type left: object
        :param right: 节点执行条件为false时的分支。
        :type right: object
        """
        
        

        self._type = None
        self._left = None
        self._right = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right

    @property
    def type(self):
        r"""Gets the type of this StepCondition.

        判断类型，例如==（等于）、!=（不等于）、>（大于）、>=（大于等于）、<（小于）、<=（小于等于）、in（包含）、or（或）。

        :return: The type of this StepCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this StepCondition.

        判断类型，例如==（等于）、!=（不等于）、>（大于）、>=（大于等于）、<（小于）、<=（小于等于）、in（包含）、or（或）。

        :param type: The type of this StepCondition.
        :type type: str
        """
        self._type = type

    @property
    def left(self):
        r"""Gets the left of this StepCondition.

        节点执行条件为true时的分支。

        :return: The left of this StepCondition.
        :rtype: object
        """
        return self._left

    @left.setter
    def left(self, left):
        r"""Sets the left of this StepCondition.

        节点执行条件为true时的分支。

        :param left: The left of this StepCondition.
        :type left: object
        """
        self._left = left

    @property
    def right(self):
        r"""Gets the right of this StepCondition.

        节点执行条件为false时的分支。

        :return: The right of this StepCondition.
        :rtype: object
        """
        return self._right

    @right.setter
    def right(self, right):
        r"""Sets the right of this StepCondition.

        节点执行条件为false时的分支。

        :param right: The right of this StepCondition.
        :type right: object
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
        if not isinstance(other, StepCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
