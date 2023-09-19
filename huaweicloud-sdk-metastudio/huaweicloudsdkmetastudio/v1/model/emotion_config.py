# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EmotionConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'emotion': 'str'
    }

    attribute_map = {
        'emotion': 'emotion'
    }

    def __init__(self, emotion=None):
        """EmotionConfig

        The model defined in huaweicloud sdk

        :param emotion: 情感标签配置。 * HAPPY：开心 * SAD：悲伤 * CALM：平静 * ANGER：愤怒  默认HAPPY。
        :type emotion: str
        """
        
        

        self._emotion = None
        self.discriminator = None

        if emotion is not None:
            self.emotion = emotion

    @property
    def emotion(self):
        """Gets the emotion of this EmotionConfig.

        情感标签配置。 * HAPPY：开心 * SAD：悲伤 * CALM：平静 * ANGER：愤怒  默认HAPPY。

        :return: The emotion of this EmotionConfig.
        :rtype: str
        """
        return self._emotion

    @emotion.setter
    def emotion(self, emotion):
        """Sets the emotion of this EmotionConfig.

        情感标签配置。 * HAPPY：开心 * SAD：悲伤 * CALM：平静 * ANGER：愤怒  默认HAPPY。

        :param emotion: The emotion of this EmotionConfig.
        :type emotion: str
        """
        self._emotion = emotion

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
        if not isinstance(other, EmotionConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
