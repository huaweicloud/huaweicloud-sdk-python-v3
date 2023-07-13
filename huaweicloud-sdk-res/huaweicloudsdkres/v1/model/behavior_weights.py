# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BehaviorWeights:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'behavior_type': 'str',
        'weight': 'int',
        'other_uses': 'list[str]'
    }

    attribute_map = {
        'behavior_type': 'behavior_type',
        'weight': 'weight',
        'other_uses': 'other_uses'
    }

    def __init__(self, behavior_type=None, weight=None, other_uses=None):
        """BehaviorWeights

        The model defined in huaweicloud sdk

        :param behavior_type: 行为类型。
        :type behavior_type: str
        :param weight: 行为权重。
        :type weight: int
        :param other_uses: 其他用途。
        :type other_uses: list[str]
        """
        
        

        self._behavior_type = None
        self._weight = None
        self._other_uses = None
        self.discriminator = None

        if behavior_type is not None:
            self.behavior_type = behavior_type
        if weight is not None:
            self.weight = weight
        if other_uses is not None:
            self.other_uses = other_uses

    @property
    def behavior_type(self):
        """Gets the behavior_type of this BehaviorWeights.

        行为类型。

        :return: The behavior_type of this BehaviorWeights.
        :rtype: str
        """
        return self._behavior_type

    @behavior_type.setter
    def behavior_type(self, behavior_type):
        """Sets the behavior_type of this BehaviorWeights.

        行为类型。

        :param behavior_type: The behavior_type of this BehaviorWeights.
        :type behavior_type: str
        """
        self._behavior_type = behavior_type

    @property
    def weight(self):
        """Gets the weight of this BehaviorWeights.

        行为权重。

        :return: The weight of this BehaviorWeights.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this BehaviorWeights.

        行为权重。

        :param weight: The weight of this BehaviorWeights.
        :type weight: int
        """
        self._weight = weight

    @property
    def other_uses(self):
        """Gets the other_uses of this BehaviorWeights.

        其他用途。

        :return: The other_uses of this BehaviorWeights.
        :rtype: list[str]
        """
        return self._other_uses

    @other_uses.setter
    def other_uses(self, other_uses):
        """Sets the other_uses of this BehaviorWeights.

        其他用途。

        :param other_uses: The other_uses of this BehaviorWeights.
        :type other_uses: list[str]
        """
        self._other_uses = other_uses

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
        if not isinstance(other, BehaviorWeights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
