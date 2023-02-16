# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateQuestionInSessionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'answers': 'list[AnswerQaPair]',
        'error_code': 'str',
        'error_msg': 'str',
        'answer_type': 'int',
        'request_id': 'str'
    }

    attribute_map = {
        'answers': 'answers',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'answer_type': 'answer_type',
        'request_id': 'request_id'
    }

    def __init__(self, answers=None, error_code=None, error_msg=None, answer_type=None, request_id=None):
        """CreateQuestionInSessionResponse

        The model defined in huaweicloud sdk

        :param answers: 答案列表
        :type answers: list[:class:`huaweicloudsdkosm.v2.AnswerQaPair`]
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误描述
        :type error_msg: str
        :param answer_type: 答案类型：0 知识库回复,1 技能回复,2 闲聊回复,3 华为云答案。
        :type answer_type: int
        :param request_id: 请求Id
        :type request_id: str
        """
        
        super(CreateQuestionInSessionResponse, self).__init__()

        self._answers = None
        self._error_code = None
        self._error_msg = None
        self._answer_type = None
        self._request_id = None
        self.discriminator = None

        if answers is not None:
            self.answers = answers
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if answer_type is not None:
            self.answer_type = answer_type
        if request_id is not None:
            self.request_id = request_id

    @property
    def answers(self):
        """Gets the answers of this CreateQuestionInSessionResponse.

        答案列表

        :return: The answers of this CreateQuestionInSessionResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.AnswerQaPair`]
        """
        return self._answers

    @answers.setter
    def answers(self, answers):
        """Sets the answers of this CreateQuestionInSessionResponse.

        答案列表

        :param answers: The answers of this CreateQuestionInSessionResponse.
        :type answers: list[:class:`huaweicloudsdkosm.v2.AnswerQaPair`]
        """
        self._answers = answers

    @property
    def error_code(self):
        """Gets the error_code of this CreateQuestionInSessionResponse.

        错误码

        :return: The error_code of this CreateQuestionInSessionResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CreateQuestionInSessionResponse.

        错误码

        :param error_code: The error_code of this CreateQuestionInSessionResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this CreateQuestionInSessionResponse.

        错误描述

        :return: The error_msg of this CreateQuestionInSessionResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this CreateQuestionInSessionResponse.

        错误描述

        :param error_msg: The error_msg of this CreateQuestionInSessionResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def answer_type(self):
        """Gets the answer_type of this CreateQuestionInSessionResponse.

        答案类型：0 知识库回复,1 技能回复,2 闲聊回复,3 华为云答案。

        :return: The answer_type of this CreateQuestionInSessionResponse.
        :rtype: int
        """
        return self._answer_type

    @answer_type.setter
    def answer_type(self, answer_type):
        """Sets the answer_type of this CreateQuestionInSessionResponse.

        答案类型：0 知识库回复,1 技能回复,2 闲聊回复,3 华为云答案。

        :param answer_type: The answer_type of this CreateQuestionInSessionResponse.
        :type answer_type: int
        """
        self._answer_type = answer_type

    @property
    def request_id(self):
        """Gets the request_id of this CreateQuestionInSessionResponse.

        请求Id

        :return: The request_id of this CreateQuestionInSessionResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateQuestionInSessionResponse.

        请求Id

        :param request_id: The request_id of this CreateQuestionInSessionResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, CreateQuestionInSessionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
