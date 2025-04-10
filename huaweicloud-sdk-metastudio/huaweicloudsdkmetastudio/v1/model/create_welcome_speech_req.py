# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWelcomeSpeechReq:

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
        'welcome_speech': 'str',
        'language': 'LanguageEnum'
    }

    attribute_map = {
        'robot_id': 'robot_id',
        'welcome_speech': 'welcome_speech',
        'language': 'language'
    }

    def __init__(self, robot_id=None, welcome_speech=None, language=None):
        r"""CreateWelcomeSpeechReq

        The model defined in huaweicloud sdk

        :param robot_id: 应用ID。
        :type robot_id: str
        :param welcome_speech: 欢迎词。
        :type welcome_speech: str
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        
        

        self._robot_id = None
        self._welcome_speech = None
        self._language = None
        self.discriminator = None

        self.robot_id = robot_id
        self.welcome_speech = welcome_speech
        if language is not None:
            self.language = language

    @property
    def robot_id(self):
        r"""Gets the robot_id of this CreateWelcomeSpeechReq.

        应用ID。

        :return: The robot_id of this CreateWelcomeSpeechReq.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this CreateWelcomeSpeechReq.

        应用ID。

        :param robot_id: The robot_id of this CreateWelcomeSpeechReq.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def welcome_speech(self):
        r"""Gets the welcome_speech of this CreateWelcomeSpeechReq.

        欢迎词。

        :return: The welcome_speech of this CreateWelcomeSpeechReq.
        :rtype: str
        """
        return self._welcome_speech

    @welcome_speech.setter
    def welcome_speech(self, welcome_speech):
        r"""Sets the welcome_speech of this CreateWelcomeSpeechReq.

        欢迎词。

        :param welcome_speech: The welcome_speech of this CreateWelcomeSpeechReq.
        :type welcome_speech: str
        """
        self._welcome_speech = welcome_speech

    @property
    def language(self):
        r"""Gets the language of this CreateWelcomeSpeechReq.

        :return: The language of this CreateWelcomeSpeechReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this CreateWelcomeSpeechReq.

        :param language: The language of this CreateWelcomeSpeechReq.
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
        if not isinstance(other, CreateWelcomeSpeechReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
