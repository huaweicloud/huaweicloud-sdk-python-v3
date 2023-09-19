# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnimationConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'animation': 'str'
    }

    attribute_map = {
        'animation': 'animation'
    }

    def __init__(self, animation=None):
        """AnimationConfig

        The model defined in huaweicloud sdk

        :param animation: 动作资产ID。
        :type animation: str
        """
        
        

        self._animation = None
        self.discriminator = None

        if animation is not None:
            self.animation = animation

    @property
    def animation(self):
        """Gets the animation of this AnimationConfig.

        动作资产ID。

        :return: The animation of this AnimationConfig.
        :rtype: str
        """
        return self._animation

    @animation.setter
    def animation(self, animation):
        """Sets the animation of this AnimationConfig.

        动作资产ID。

        :param animation: The animation of this AnimationConfig.
        :type animation: str
        """
        self._animation = animation

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
        if not isinstance(other, AnimationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
