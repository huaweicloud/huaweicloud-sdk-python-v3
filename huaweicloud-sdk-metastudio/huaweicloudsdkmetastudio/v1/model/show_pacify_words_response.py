# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPacifyWordsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pacify_words_id': 'str',
        'pacify_words': 'str',
        'language': 'LanguageEnum',
        'robot_id': 'str',
        'pacify_words_type': 'int',
        'intent': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'pacify_words_id': 'pacify_words_id',
        'pacify_words': 'pacify_words',
        'language': 'language',
        'robot_id': 'robot_id',
        'pacify_words_type': 'pacify_words_type',
        'intent': 'intent',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, pacify_words_id=None, pacify_words=None, language=None, robot_id=None, pacify_words_type=None, intent=None, create_time=None, update_time=None, x_request_id=None):
        r"""ShowPacifyWordsResponse

        The model defined in huaweicloud sdk

        :param pacify_words_id: 安抚话术ID。
        :type pacify_words_id: str
        :param pacify_words: 安抚话术。
        :type pacify_words: str
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param robot_id: 应用ID。
        :type robot_id: str
        :param pacify_words_type: 安抚话术类型 &gt; 0:通用安抚话术, 1:基于意图匹配安抚话术
        :type pacify_words_type: int
        :param intent: 意图名称
        :type intent: str
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowPacifyWordsResponse, self).__init__()

        self._pacify_words_id = None
        self._pacify_words = None
        self._language = None
        self._robot_id = None
        self._pacify_words_type = None
        self._intent = None
        self._create_time = None
        self._update_time = None
        self._x_request_id = None
        self.discriminator = None

        if pacify_words_id is not None:
            self.pacify_words_id = pacify_words_id
        if pacify_words is not None:
            self.pacify_words = pacify_words
        if language is not None:
            self.language = language
        if robot_id is not None:
            self.robot_id = robot_id
        if pacify_words_type is not None:
            self.pacify_words_type = pacify_words_type
        if intent is not None:
            self.intent = intent
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def pacify_words_id(self):
        r"""Gets the pacify_words_id of this ShowPacifyWordsResponse.

        安抚话术ID。

        :return: The pacify_words_id of this ShowPacifyWordsResponse.
        :rtype: str
        """
        return self._pacify_words_id

    @pacify_words_id.setter
    def pacify_words_id(self, pacify_words_id):
        r"""Sets the pacify_words_id of this ShowPacifyWordsResponse.

        安抚话术ID。

        :param pacify_words_id: The pacify_words_id of this ShowPacifyWordsResponse.
        :type pacify_words_id: str
        """
        self._pacify_words_id = pacify_words_id

    @property
    def pacify_words(self):
        r"""Gets the pacify_words of this ShowPacifyWordsResponse.

        安抚话术。

        :return: The pacify_words of this ShowPacifyWordsResponse.
        :rtype: str
        """
        return self._pacify_words

    @pacify_words.setter
    def pacify_words(self, pacify_words):
        r"""Sets the pacify_words of this ShowPacifyWordsResponse.

        安抚话术。

        :param pacify_words: The pacify_words of this ShowPacifyWordsResponse.
        :type pacify_words: str
        """
        self._pacify_words = pacify_words

    @property
    def language(self):
        r"""Gets the language of this ShowPacifyWordsResponse.

        :return: The language of this ShowPacifyWordsResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ShowPacifyWordsResponse.

        :param language: The language of this ShowPacifyWordsResponse.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def robot_id(self):
        r"""Gets the robot_id of this ShowPacifyWordsResponse.

        应用ID。

        :return: The robot_id of this ShowPacifyWordsResponse.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this ShowPacifyWordsResponse.

        应用ID。

        :param robot_id: The robot_id of this ShowPacifyWordsResponse.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def pacify_words_type(self):
        r"""Gets the pacify_words_type of this ShowPacifyWordsResponse.

        安抚话术类型 > 0:通用安抚话术, 1:基于意图匹配安抚话术

        :return: The pacify_words_type of this ShowPacifyWordsResponse.
        :rtype: int
        """
        return self._pacify_words_type

    @pacify_words_type.setter
    def pacify_words_type(self, pacify_words_type):
        r"""Sets the pacify_words_type of this ShowPacifyWordsResponse.

        安抚话术类型 > 0:通用安抚话术, 1:基于意图匹配安抚话术

        :param pacify_words_type: The pacify_words_type of this ShowPacifyWordsResponse.
        :type pacify_words_type: int
        """
        self._pacify_words_type = pacify_words_type

    @property
    def intent(self):
        r"""Gets the intent of this ShowPacifyWordsResponse.

        意图名称

        :return: The intent of this ShowPacifyWordsResponse.
        :rtype: str
        """
        return self._intent

    @intent.setter
    def intent(self, intent):
        r"""Sets the intent of this ShowPacifyWordsResponse.

        意图名称

        :param intent: The intent of this ShowPacifyWordsResponse.
        :type intent: str
        """
        self._intent = intent

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowPacifyWordsResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this ShowPacifyWordsResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowPacifyWordsResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this ShowPacifyWordsResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowPacifyWordsResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this ShowPacifyWordsResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowPacifyWordsResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this ShowPacifyWordsResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowPacifyWordsResponse.

        :return: The x_request_id of this ShowPacifyWordsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowPacifyWordsResponse.

        :param x_request_id: The x_request_id of this ShowPacifyWordsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowPacifyWordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
