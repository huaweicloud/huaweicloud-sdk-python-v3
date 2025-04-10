# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostRequestsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'question': 'str',
        'answers': 'list[Answers]',
        'extends': 'OldExtends'
    }

    attribute_map = {
        'request_id': 'request_id',
        'question': 'question',
        'answers': 'answers',
        'extends': 'extends'
    }

    def __init__(self, request_id=None, question=None, answers=None, extends=None):
        r"""PostRequestsResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。  调用失败时无此字段。
        :type request_id: str
        :param question: 问题。  调用失败时无此字段。
        :type question: str
        :param answers: 最相似的问题集。 调用失败时无此字段。
        :type answers: list[:class:`huaweicloudsdkcbs.v1.Answers`]
        :param extends: 
        :type extends: :class:`huaweicloudsdkcbs.v1.OldExtends`
        """
        
        super(PostRequestsResponse, self).__init__()

        self._request_id = None
        self._question = None
        self._answers = None
        self._extends = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if question is not None:
            self.question = question
        if answers is not None:
            self.answers = answers
        if extends is not None:
            self.extends = extends

    @property
    def request_id(self):
        r"""Gets the request_id of this PostRequestsResponse.

        请求ID。  调用失败时无此字段。

        :return: The request_id of this PostRequestsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this PostRequestsResponse.

        请求ID。  调用失败时无此字段。

        :param request_id: The request_id of this PostRequestsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def question(self):
        r"""Gets the question of this PostRequestsResponse.

        问题。  调用失败时无此字段。

        :return: The question of this PostRequestsResponse.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        r"""Sets the question of this PostRequestsResponse.

        问题。  调用失败时无此字段。

        :param question: The question of this PostRequestsResponse.
        :type question: str
        """
        self._question = question

    @property
    def answers(self):
        r"""Gets the answers of this PostRequestsResponse.

        最相似的问题集。 调用失败时无此字段。

        :return: The answers of this PostRequestsResponse.
        :rtype: list[:class:`huaweicloudsdkcbs.v1.Answers`]
        """
        return self._answers

    @answers.setter
    def answers(self, answers):
        r"""Sets the answers of this PostRequestsResponse.

        最相似的问题集。 调用失败时无此字段。

        :param answers: The answers of this PostRequestsResponse.
        :type answers: list[:class:`huaweicloudsdkcbs.v1.Answers`]
        """
        self._answers = answers

    @property
    def extends(self):
        r"""Gets the extends of this PostRequestsResponse.

        :return: The extends of this PostRequestsResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.OldExtends`
        """
        return self._extends

    @extends.setter
    def extends(self, extends):
        r"""Sets the extends of this PostRequestsResponse.

        :param extends: The extends of this PostRequestsResponse.
        :type extends: :class:`huaweicloudsdkcbs.v1.OldExtends`
        """
        self._extends = extends

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
        if not isinstance(other, PostRequestsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
