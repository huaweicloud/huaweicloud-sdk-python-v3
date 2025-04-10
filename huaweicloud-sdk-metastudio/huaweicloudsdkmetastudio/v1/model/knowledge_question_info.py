# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KnowledgeQuestionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'question_id': 'str',
        'question': 'str',
        'intent_id': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'question_id': 'question_id',
        'question': 'question',
        'intent_id': 'intent_id',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, question_id=None, question=None, intent_id=None, create_time=None, update_time=None):
        r"""KnowledgeQuestionInfo

        The model defined in huaweicloud sdk

        :param question_id: 问法ID。
        :type question_id: str
        :param question: 问法。
        :type question: str
        :param intent_id: 意图ID。
        :type intent_id: str
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        """
        
        

        self._question_id = None
        self._question = None
        self._intent_id = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if question_id is not None:
            self.question_id = question_id
        self.question = question
        self.intent_id = intent_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def question_id(self):
        r"""Gets the question_id of this KnowledgeQuestionInfo.

        问法ID。

        :return: The question_id of this KnowledgeQuestionInfo.
        :rtype: str
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        r"""Sets the question_id of this KnowledgeQuestionInfo.

        问法ID。

        :param question_id: The question_id of this KnowledgeQuestionInfo.
        :type question_id: str
        """
        self._question_id = question_id

    @property
    def question(self):
        r"""Gets the question of this KnowledgeQuestionInfo.

        问法。

        :return: The question of this KnowledgeQuestionInfo.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        r"""Sets the question of this KnowledgeQuestionInfo.

        问法。

        :param question: The question of this KnowledgeQuestionInfo.
        :type question: str
        """
        self._question = question

    @property
    def intent_id(self):
        r"""Gets the intent_id of this KnowledgeQuestionInfo.

        意图ID。

        :return: The intent_id of this KnowledgeQuestionInfo.
        :rtype: str
        """
        return self._intent_id

    @intent_id.setter
    def intent_id(self, intent_id):
        r"""Sets the intent_id of this KnowledgeQuestionInfo.

        意图ID。

        :param intent_id: The intent_id of this KnowledgeQuestionInfo.
        :type intent_id: str
        """
        self._intent_id = intent_id

    @property
    def create_time(self):
        r"""Gets the create_time of this KnowledgeQuestionInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this KnowledgeQuestionInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this KnowledgeQuestionInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this KnowledgeQuestionInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this KnowledgeQuestionInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this KnowledgeQuestionInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this KnowledgeQuestionInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this KnowledgeQuestionInfo.
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
        if not isinstance(other, KnowledgeQuestionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
