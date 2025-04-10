# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWelcomeSpeechSwitchReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'robot_id': 'str',
        'enable_welcome_speech': 'bool',
        'language': 'LanguageEnum'
    }

    attribute_map = {
        'robot_id': 'robot_id',
        'enable_welcome_speech': 'enable_welcome_speech',
        'language': 'language'
    }

    def __init__(self, robot_id=None, enable_welcome_speech=None, language=None):
        r"""UpdateWelcomeSpeechSwitchReq

        The model defined in huaweicloud sdk

        :param robot_id: 应用ID。
        :type robot_id: str
        :param enable_welcome_speech: 欢迎词功能开关。
        :type enable_welcome_speech: bool
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        
        

        self._robot_id = None
        self._enable_welcome_speech = None
        self._language = None
        self.discriminator = None

        self.robot_id = robot_id
        self.enable_welcome_speech = enable_welcome_speech
        if language is not None:
            self.language = language

    @property
    def robot_id(self):
        r"""Gets the robot_id of this UpdateWelcomeSpeechSwitchReq.

        应用ID。

        :return: The robot_id of this UpdateWelcomeSpeechSwitchReq.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this UpdateWelcomeSpeechSwitchReq.

        应用ID。

        :param robot_id: The robot_id of this UpdateWelcomeSpeechSwitchReq.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def enable_welcome_speech(self):
        r"""Gets the enable_welcome_speech of this UpdateWelcomeSpeechSwitchReq.

        欢迎词功能开关。

        :return: The enable_welcome_speech of this UpdateWelcomeSpeechSwitchReq.
        :rtype: bool
        """
        return self._enable_welcome_speech

    @enable_welcome_speech.setter
    def enable_welcome_speech(self, enable_welcome_speech):
        r"""Sets the enable_welcome_speech of this UpdateWelcomeSpeechSwitchReq.

        欢迎词功能开关。

        :param enable_welcome_speech: The enable_welcome_speech of this UpdateWelcomeSpeechSwitchReq.
        :type enable_welcome_speech: bool
        """
        self._enable_welcome_speech = enable_welcome_speech

    @property
    def language(self):
        r"""Gets the language of this UpdateWelcomeSpeechSwitchReq.

        :return: The language of this UpdateWelcomeSpeechSwitchReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this UpdateWelcomeSpeechSwitchReq.

        :param language: The language of this UpdateWelcomeSpeechSwitchReq.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

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
        if not isinstance(other, UpdateWelcomeSpeechSwitchReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
