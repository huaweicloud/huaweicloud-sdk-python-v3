# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnalysisInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role': 'str',
        'emotion': 'str',
        'speed': 'float'
    }

    attribute_map = {
        'role': 'role',
        'emotion': 'emotion',
        'speed': 'speed'
    }

    def __init__(self, role=None, emotion=None, speed=None):
        """AnalysisInfoResult

        The model defined in huaweicloud sdk

        :param role: 角色类型, 目前仅支持 AGENT(座席), USER(用户)。
        :type role: str
        :param emotion: 情绪类型，目前支持NORMAL(正常)，ANGRY(愤怒)，UNKNOWN(未知)。 在识别配置中emotion为true时存在。
        :type emotion: str
        :param speed: 语速信息，单位是\&quot;每秒字数\&quot;。 在识别配置中speed为true时存在。
        :type speed: float
        """
        
        

        self._role = None
        self._emotion = None
        self._speed = None
        self.discriminator = None

        if role is not None:
            self.role = role
        if emotion is not None:
            self.emotion = emotion
        if speed is not None:
            self.speed = speed

    @property
    def role(self):
        """Gets the role of this AnalysisInfoResult.

        角色类型, 目前仅支持 AGENT(座席), USER(用户)。

        :return: The role of this AnalysisInfoResult.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this AnalysisInfoResult.

        角色类型, 目前仅支持 AGENT(座席), USER(用户)。

        :param role: The role of this AnalysisInfoResult.
        :type role: str
        """
        self._role = role

    @property
    def emotion(self):
        """Gets the emotion of this AnalysisInfoResult.

        情绪类型，目前支持NORMAL(正常)，ANGRY(愤怒)，UNKNOWN(未知)。 在识别配置中emotion为true时存在。

        :return: The emotion of this AnalysisInfoResult.
        :rtype: str
        """
        return self._emotion

    @emotion.setter
    def emotion(self, emotion):
        """Sets the emotion of this AnalysisInfoResult.

        情绪类型，目前支持NORMAL(正常)，ANGRY(愤怒)，UNKNOWN(未知)。 在识别配置中emotion为true时存在。

        :param emotion: The emotion of this AnalysisInfoResult.
        :type emotion: str
        """
        self._emotion = emotion

    @property
    def speed(self):
        """Gets the speed of this AnalysisInfoResult.

        语速信息，单位是\"每秒字数\"。 在识别配置中speed为true时存在。

        :return: The speed of this AnalysisInfoResult.
        :rtype: float
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this AnalysisInfoResult.

        语速信息，单位是\"每秒字数\"。 在识别配置中speed为true时存在。

        :param speed: The speed of this AnalysisInfoResult.
        :type speed: float
        """
        self._speed = speed

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
        if not isinstance(other, AnalysisInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
