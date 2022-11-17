# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionsList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'confidence': 'float',
        'action': 'int'
    }

    attribute_map = {
        'confidence': 'confidence',
        'action': 'action'
    }

    def __init__(self, confidence=None, action=None):
        """ActionsList

        The model defined in huaweicloud sdk

        :param confidence: 置信度，取值范围0～1。
        :type confidence: float
        :param action: 动作编号，取值范围：[1,2,3,4]，其中： • 1：左摇头 • 2：右摇头 • 3：点头 • 4：嘴部动作
        :type action: int
        """
        
        

        self._confidence = None
        self._action = None
        self.discriminator = None

        self.confidence = confidence
        if action is not None:
            self.action = action

    @property
    def confidence(self):
        """Gets the confidence of this ActionsList.

        置信度，取值范围0～1。

        :return: The confidence of this ActionsList.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ActionsList.

        置信度，取值范围0～1。

        :param confidence: The confidence of this ActionsList.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def action(self):
        """Gets the action of this ActionsList.

        动作编号，取值范围：[1,2,3,4]，其中： • 1：左摇头 • 2：右摇头 • 3：点头 • 4：嘴部动作

        :return: The action of this ActionsList.
        :rtype: int
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ActionsList.

        动作编号，取值范围：[1,2,3,4]，其中： • 1：左摇头 • 2：右摇头 • 3：点头 • 4：嘴部动作

        :param action: The action of this ActionsList.
        :type action: int
        """
        self._action = action

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
        if not isinstance(other, ActionsList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
