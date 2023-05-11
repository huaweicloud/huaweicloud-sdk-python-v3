# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateQaAskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'lang_result': 'LangResult',
        'reply_type': 'str',
        'session_id': 'str',
        'request_id': 'str',
        'answers_detail': 'AnswerDetail'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'lang_result': 'lang_result',
        'reply_type': 'reply_type',
        'session_id': 'session_id',
        'request_id': 'request_id',
        'answers_detail': 'answers_detail'
    }

    def __init__(self, error_code=None, error_msg=None, lang_result=None, reply_type=None, session_id=None, request_id=None, answers_detail=None):
        """CreateQaAskResponse

        The model defined in huaweicloud sdk

        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误描述
        :type error_msg: str
        :param lang_result: 
        :type lang_result: :class:`huaweicloudsdkosm.v2.LangResult`
        :param reply_type: - QA_BOT:  - TASK_BOT:  - CHAT_BOT:  - GRAPH_BOT:  - HW_CLOUD:  
        :type reply_type: str
        :param session_id: 会话ID
        :type session_id: str
        :param request_id: 请求ID
        :type request_id: str
        :param answers_detail: 
        :type answers_detail: :class:`huaweicloudsdkosm.v2.AnswerDetail`
        """
        
        super(CreateQaAskResponse, self).__init__()

        self._error_code = None
        self._error_msg = None
        self._lang_result = None
        self._reply_type = None
        self._session_id = None
        self._request_id = None
        self._answers_detail = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if lang_result is not None:
            self.lang_result = lang_result
        if reply_type is not None:
            self.reply_type = reply_type
        if session_id is not None:
            self.session_id = session_id
        if request_id is not None:
            self.request_id = request_id
        if answers_detail is not None:
            self.answers_detail = answers_detail

    @property
    def error_code(self):
        """Gets the error_code of this CreateQaAskResponse.

        错误码

        :return: The error_code of this CreateQaAskResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CreateQaAskResponse.

        错误码

        :param error_code: The error_code of this CreateQaAskResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this CreateQaAskResponse.

        错误描述

        :return: The error_msg of this CreateQaAskResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this CreateQaAskResponse.

        错误描述

        :param error_msg: The error_msg of this CreateQaAskResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def lang_result(self):
        """Gets the lang_result of this CreateQaAskResponse.

        :return: The lang_result of this CreateQaAskResponse.
        :rtype: :class:`huaweicloudsdkosm.v2.LangResult`
        """
        return self._lang_result

    @lang_result.setter
    def lang_result(self, lang_result):
        """Sets the lang_result of this CreateQaAskResponse.

        :param lang_result: The lang_result of this CreateQaAskResponse.
        :type lang_result: :class:`huaweicloudsdkosm.v2.LangResult`
        """
        self._lang_result = lang_result

    @property
    def reply_type(self):
        """Gets the reply_type of this CreateQaAskResponse.

        - QA_BOT:  - TASK_BOT:  - CHAT_BOT:  - GRAPH_BOT:  - HW_CLOUD:  

        :return: The reply_type of this CreateQaAskResponse.
        :rtype: str
        """
        return self._reply_type

    @reply_type.setter
    def reply_type(self, reply_type):
        """Sets the reply_type of this CreateQaAskResponse.

        - QA_BOT:  - TASK_BOT:  - CHAT_BOT:  - GRAPH_BOT:  - HW_CLOUD:  

        :param reply_type: The reply_type of this CreateQaAskResponse.
        :type reply_type: str
        """
        self._reply_type = reply_type

    @property
    def session_id(self):
        """Gets the session_id of this CreateQaAskResponse.

        会话ID

        :return: The session_id of this CreateQaAskResponse.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this CreateQaAskResponse.

        会话ID

        :param session_id: The session_id of this CreateQaAskResponse.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def request_id(self):
        """Gets the request_id of this CreateQaAskResponse.

        请求ID

        :return: The request_id of this CreateQaAskResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateQaAskResponse.

        请求ID

        :param request_id: The request_id of this CreateQaAskResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def answers_detail(self):
        """Gets the answers_detail of this CreateQaAskResponse.

        :return: The answers_detail of this CreateQaAskResponse.
        :rtype: :class:`huaweicloudsdkosm.v2.AnswerDetail`
        """
        return self._answers_detail

    @answers_detail.setter
    def answers_detail(self, answers_detail):
        """Sets the answers_detail of this CreateQaAskResponse.

        :param answers_detail: The answers_detail of this CreateQaAskResponse.
        :type answers_detail: :class:`huaweicloudsdkosm.v2.AnswerDetail`
        """
        self._answers_detail = answers_detail

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
        if not isinstance(other, CreateQaAskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
