# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePacifyWordsReq:

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
        'pacify_words_type': 'int',
        'intent': 'str',
        'pacify_words': 'str',
        'language': 'LanguageEnum'
    }

    attribute_map = {
        'robot_id': 'robot_id',
        'pacify_words_type': 'pacify_words_type',
        'intent': 'intent',
        'pacify_words': 'pacify_words',
        'language': 'language'
    }

    def __init__(self, robot_id=None, pacify_words_type=None, intent=None, pacify_words=None, language=None):
        """CreatePacifyWordsReq

        The model defined in huaweicloud sdk

        :param robot_id: 应用ID。
        :type robot_id: str
        :param pacify_words_type: 安抚话术类型 &gt; 0:通用安抚话术, 1:意图匹配安抚话术
        :type pacify_words_type: int
        :param intent: 意图名称
        :type intent: str
        :param pacify_words: 安抚话术。
        :type pacify_words: str
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        
        

        self._robot_id = None
        self._pacify_words_type = None
        self._intent = None
        self._pacify_words = None
        self._language = None
        self.discriminator = None

        self.robot_id = robot_id
        self.pacify_words_type = pacify_words_type
        if intent is not None:
            self.intent = intent
        self.pacify_words = pacify_words
        self.language = language

    @property
    def robot_id(self):
        """Gets the robot_id of this CreatePacifyWordsReq.

        应用ID。

        :return: The robot_id of this CreatePacifyWordsReq.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        """Sets the robot_id of this CreatePacifyWordsReq.

        应用ID。

        :param robot_id: The robot_id of this CreatePacifyWordsReq.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def pacify_words_type(self):
        """Gets the pacify_words_type of this CreatePacifyWordsReq.

        安抚话术类型 > 0:通用安抚话术, 1:意图匹配安抚话术

        :return: The pacify_words_type of this CreatePacifyWordsReq.
        :rtype: int
        """
        return self._pacify_words_type

    @pacify_words_type.setter
    def pacify_words_type(self, pacify_words_type):
        """Sets the pacify_words_type of this CreatePacifyWordsReq.

        安抚话术类型 > 0:通用安抚话术, 1:意图匹配安抚话术

        :param pacify_words_type: The pacify_words_type of this CreatePacifyWordsReq.
        :type pacify_words_type: int
        """
        self._pacify_words_type = pacify_words_type

    @property
    def intent(self):
        """Gets the intent of this CreatePacifyWordsReq.

        意图名称

        :return: The intent of this CreatePacifyWordsReq.
        :rtype: str
        """
        return self._intent

    @intent.setter
    def intent(self, intent):
        """Sets the intent of this CreatePacifyWordsReq.

        意图名称

        :param intent: The intent of this CreatePacifyWordsReq.
        :type intent: str
        """
        self._intent = intent

    @property
    def pacify_words(self):
        """Gets the pacify_words of this CreatePacifyWordsReq.

        安抚话术。

        :return: The pacify_words of this CreatePacifyWordsReq.
        :rtype: str
        """
        return self._pacify_words

    @pacify_words.setter
    def pacify_words(self, pacify_words):
        """Sets the pacify_words of this CreatePacifyWordsReq.

        安抚话术。

        :param pacify_words: The pacify_words of this CreatePacifyWordsReq.
        :type pacify_words: str
        """
        self._pacify_words = pacify_words

    @property
    def language(self):
        """Gets the language of this CreatePacifyWordsReq.

        :return: The language of this CreatePacifyWordsReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this CreatePacifyWordsReq.

        :param language: The language of this CreatePacifyWordsReq.
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
        if not isinstance(other, CreatePacifyWordsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
