# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HotQuestionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hot_question_id': 'str',
        'hot_question': 'str',
        'language': 'LanguageEnum',
        'robot_id': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'hot_question_id': 'hot_question_id',
        'hot_question': 'hot_question',
        'language': 'language',
        'robot_id': 'robot_id',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, hot_question_id=None, hot_question=None, language=None, robot_id=None, create_time=None, update_time=None):
        r"""HotQuestionInfo

        The model defined in huaweicloud sdk

        :param hot_question_id: 热点问题ID。
        :type hot_question_id: str
        :param hot_question: 热点问题。
        :type hot_question: str
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param robot_id: 机器人ID。
        :type robot_id: str
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        """
        
        

        self._hot_question_id = None
        self._hot_question = None
        self._language = None
        self._robot_id = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if hot_question_id is not None:
            self.hot_question_id = hot_question_id
        if hot_question is not None:
            self.hot_question = hot_question
        if language is not None:
            self.language = language
        if robot_id is not None:
            self.robot_id = robot_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def hot_question_id(self):
        r"""Gets the hot_question_id of this HotQuestionInfo.

        热点问题ID。

        :return: The hot_question_id of this HotQuestionInfo.
        :rtype: str
        """
        return self._hot_question_id

    @hot_question_id.setter
    def hot_question_id(self, hot_question_id):
        r"""Sets the hot_question_id of this HotQuestionInfo.

        热点问题ID。

        :param hot_question_id: The hot_question_id of this HotQuestionInfo.
        :type hot_question_id: str
        """
        self._hot_question_id = hot_question_id

    @property
    def hot_question(self):
        r"""Gets the hot_question of this HotQuestionInfo.

        热点问题。

        :return: The hot_question of this HotQuestionInfo.
        :rtype: str
        """
        return self._hot_question

    @hot_question.setter
    def hot_question(self, hot_question):
        r"""Sets the hot_question of this HotQuestionInfo.

        热点问题。

        :param hot_question: The hot_question of this HotQuestionInfo.
        :type hot_question: str
        """
        self._hot_question = hot_question

    @property
    def language(self):
        r"""Gets the language of this HotQuestionInfo.

        :return: The language of this HotQuestionInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this HotQuestionInfo.

        :param language: The language of this HotQuestionInfo.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def robot_id(self):
        r"""Gets the robot_id of this HotQuestionInfo.

        机器人ID。

        :return: The robot_id of this HotQuestionInfo.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this HotQuestionInfo.

        机器人ID。

        :param robot_id: The robot_id of this HotQuestionInfo.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def create_time(self):
        r"""Gets the create_time of this HotQuestionInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this HotQuestionInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this HotQuestionInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this HotQuestionInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this HotQuestionInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this HotQuestionInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this HotQuestionInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this HotQuestionInfo.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, HotQuestionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
