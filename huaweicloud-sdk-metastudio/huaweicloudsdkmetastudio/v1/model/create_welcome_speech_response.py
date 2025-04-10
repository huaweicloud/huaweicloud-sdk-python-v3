# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWelcomeSpeechResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'welcome_speech_id': 'str',
        'welcome_speech': 'str',
        'enable_welcome_speech': 'bool',
        'language': 'LanguageEnum',
        'robot_id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'welcome_speech_id': 'welcome_speech_id',
        'welcome_speech': 'welcome_speech',
        'enable_welcome_speech': 'enable_welcome_speech',
        'language': 'language',
        'robot_id': 'robot_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, welcome_speech_id=None, welcome_speech=None, enable_welcome_speech=None, language=None, robot_id=None, create_time=None, update_time=None, x_request_id=None):
        r"""CreateWelcomeSpeechResponse

        The model defined in huaweicloud sdk

        :param welcome_speech_id: 欢迎词ID。
        :type welcome_speech_id: str
        :param welcome_speech: 欢迎词。
        :type welcome_speech: str
        :param enable_welcome_speech: 欢迎词功能开关。
        :type enable_welcome_speech: bool
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param robot_id: 应用ID。
        :type robot_id: str
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateWelcomeSpeechResponse, self).__init__()

        self._welcome_speech_id = None
        self._welcome_speech = None
        self._enable_welcome_speech = None
        self._language = None
        self._robot_id = None
        self._create_time = None
        self._update_time = None
        self._x_request_id = None
        self.discriminator = None

        if welcome_speech_id is not None:
            self.welcome_speech_id = welcome_speech_id
        if welcome_speech is not None:
            self.welcome_speech = welcome_speech
        if enable_welcome_speech is not None:
            self.enable_welcome_speech = enable_welcome_speech
        if language is not None:
            self.language = language
        if robot_id is not None:
            self.robot_id = robot_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def welcome_speech_id(self):
        r"""Gets the welcome_speech_id of this CreateWelcomeSpeechResponse.

        欢迎词ID。

        :return: The welcome_speech_id of this CreateWelcomeSpeechResponse.
        :rtype: str
        """
        return self._welcome_speech_id

    @welcome_speech_id.setter
    def welcome_speech_id(self, welcome_speech_id):
        r"""Sets the welcome_speech_id of this CreateWelcomeSpeechResponse.

        欢迎词ID。

        :param welcome_speech_id: The welcome_speech_id of this CreateWelcomeSpeechResponse.
        :type welcome_speech_id: str
        """
        self._welcome_speech_id = welcome_speech_id

    @property
    def welcome_speech(self):
        r"""Gets the welcome_speech of this CreateWelcomeSpeechResponse.

        欢迎词。

        :return: The welcome_speech of this CreateWelcomeSpeechResponse.
        :rtype: str
        """
        return self._welcome_speech

    @welcome_speech.setter
    def welcome_speech(self, welcome_speech):
        r"""Sets the welcome_speech of this CreateWelcomeSpeechResponse.

        欢迎词。

        :param welcome_speech: The welcome_speech of this CreateWelcomeSpeechResponse.
        :type welcome_speech: str
        """
        self._welcome_speech = welcome_speech

    @property
    def enable_welcome_speech(self):
        r"""Gets the enable_welcome_speech of this CreateWelcomeSpeechResponse.

        欢迎词功能开关。

        :return: The enable_welcome_speech of this CreateWelcomeSpeechResponse.
        :rtype: bool
        """
        return self._enable_welcome_speech

    @enable_welcome_speech.setter
    def enable_welcome_speech(self, enable_welcome_speech):
        r"""Sets the enable_welcome_speech of this CreateWelcomeSpeechResponse.

        欢迎词功能开关。

        :param enable_welcome_speech: The enable_welcome_speech of this CreateWelcomeSpeechResponse.
        :type enable_welcome_speech: bool
        """
        self._enable_welcome_speech = enable_welcome_speech

    @property
    def language(self):
        r"""Gets the language of this CreateWelcomeSpeechResponse.

        :return: The language of this CreateWelcomeSpeechResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this CreateWelcomeSpeechResponse.

        :param language: The language of this CreateWelcomeSpeechResponse.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def robot_id(self):
        r"""Gets the robot_id of this CreateWelcomeSpeechResponse.

        应用ID。

        :return: The robot_id of this CreateWelcomeSpeechResponse.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this CreateWelcomeSpeechResponse.

        应用ID。

        :param robot_id: The robot_id of this CreateWelcomeSpeechResponse.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateWelcomeSpeechResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this CreateWelcomeSpeechResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateWelcomeSpeechResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this CreateWelcomeSpeechResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateWelcomeSpeechResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this CreateWelcomeSpeechResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateWelcomeSpeechResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this CreateWelcomeSpeechResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateWelcomeSpeechResponse.

        :return: The x_request_id of this CreateWelcomeSpeechResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateWelcomeSpeechResponse.

        :param x_request_id: The x_request_id of this CreateWelcomeSpeechResponse.
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
        if not isinstance(other, CreateWelcomeSpeechResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
