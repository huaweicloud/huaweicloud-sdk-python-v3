# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostRequestsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extends': 'Extends',
        'chat_enable': 'bool',
        'user_id': 'str',
        'question': 'str',
        'session_id': 'str',
        'query_types': 'list[int]'
    }

    attribute_map = {
        'extends': 'extends',
        'chat_enable': 'chat_enable',
        'user_id': 'user_id',
        'question': 'question',
        'session_id': 'session_id',
        'query_types': 'query_types'
    }

    def __init__(self, extends=None, chat_enable=None, user_id=None, question=None, session_id=None, query_types=None):
        r"""PostRequestsReq

        The model defined in huaweicloud sdk

        :param extends: 
        :type extends: :class:`huaweicloudsdkcbs.v1.Extends`
        :param chat_enable: 默认false true：使用内部闲聊语料进行兜底 false：不使用闲聊兜底
        :type chat_enable: bool
        :param user_id: 用户id，在日志中用于标识不通用户，可以为任意String
        :type user_id: str
        :param question: 用户输入
        :type question: str
        :param session_id: 会话标识符，UUID格式。如：c04e6f7b-61d7-4a2d-a0c8-f9ecd2f62359。  每次对话开启，机器人创建会话id，下次请求中传入该id表示继续该轮对话，每轮会话有效时间为2分钟。 若传入的会话id已过期或者为空，则机器人会重新创建新的会话id（重新创建会话id会消耗一定时间）。
        :type session_id: str
        :param query_types: 指定发送的机器人类型集合。  0 知识库问答。  1 技能问答。  2 闲聊问答。  3 图谱问答。  4 文档问答。  5 表格问答。  非必填字段。如果不填，会使用默认的机器人融合策略。
        :type query_types: list[int]
        """
        
        

        self._extends = None
        self._chat_enable = None
        self._user_id = None
        self._question = None
        self._session_id = None
        self._query_types = None
        self.discriminator = None

        if extends is not None:
            self.extends = extends
        if chat_enable is not None:
            self.chat_enable = chat_enable
        if user_id is not None:
            self.user_id = user_id
        self.question = question
        if session_id is not None:
            self.session_id = session_id
        if query_types is not None:
            self.query_types = query_types

    @property
    def extends(self):
        r"""Gets the extends of this PostRequestsReq.

        :return: The extends of this PostRequestsReq.
        :rtype: :class:`huaweicloudsdkcbs.v1.Extends`
        """
        return self._extends

    @extends.setter
    def extends(self, extends):
        r"""Sets the extends of this PostRequestsReq.

        :param extends: The extends of this PostRequestsReq.
        :type extends: :class:`huaweicloudsdkcbs.v1.Extends`
        """
        self._extends = extends

    @property
    def chat_enable(self):
        r"""Gets the chat_enable of this PostRequestsReq.

        默认false true：使用内部闲聊语料进行兜底 false：不使用闲聊兜底

        :return: The chat_enable of this PostRequestsReq.
        :rtype: bool
        """
        return self._chat_enable

    @chat_enable.setter
    def chat_enable(self, chat_enable):
        r"""Sets the chat_enable of this PostRequestsReq.

        默认false true：使用内部闲聊语料进行兜底 false：不使用闲聊兜底

        :param chat_enable: The chat_enable of this PostRequestsReq.
        :type chat_enable: bool
        """
        self._chat_enable = chat_enable

    @property
    def user_id(self):
        r"""Gets the user_id of this PostRequestsReq.

        用户id，在日志中用于标识不通用户，可以为任意String

        :return: The user_id of this PostRequestsReq.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this PostRequestsReq.

        用户id，在日志中用于标识不通用户，可以为任意String

        :param user_id: The user_id of this PostRequestsReq.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def question(self):
        r"""Gets the question of this PostRequestsReq.

        用户输入

        :return: The question of this PostRequestsReq.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        r"""Sets the question of this PostRequestsReq.

        用户输入

        :param question: The question of this PostRequestsReq.
        :type question: str
        """
        self._question = question

    @property
    def session_id(self):
        r"""Gets the session_id of this PostRequestsReq.

        会话标识符，UUID格式。如：c04e6f7b-61d7-4a2d-a0c8-f9ecd2f62359。  每次对话开启，机器人创建会话id，下次请求中传入该id表示继续该轮对话，每轮会话有效时间为2分钟。 若传入的会话id已过期或者为空，则机器人会重新创建新的会话id（重新创建会话id会消耗一定时间）。

        :return: The session_id of this PostRequestsReq.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this PostRequestsReq.

        会话标识符，UUID格式。如：c04e6f7b-61d7-4a2d-a0c8-f9ecd2f62359。  每次对话开启，机器人创建会话id，下次请求中传入该id表示继续该轮对话，每轮会话有效时间为2分钟。 若传入的会话id已过期或者为空，则机器人会重新创建新的会话id（重新创建会话id会消耗一定时间）。

        :param session_id: The session_id of this PostRequestsReq.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def query_types(self):
        r"""Gets the query_types of this PostRequestsReq.

        指定发送的机器人类型集合。  0 知识库问答。  1 技能问答。  2 闲聊问答。  3 图谱问答。  4 文档问答。  5 表格问答。  非必填字段。如果不填，会使用默认的机器人融合策略。

        :return: The query_types of this PostRequestsReq.
        :rtype: list[int]
        """
        return self._query_types

    @query_types.setter
    def query_types(self, query_types):
        r"""Sets the query_types of this PostRequestsReq.

        指定发送的机器人类型集合。  0 知识库问答。  1 技能问答。  2 闲聊问答。  3 图谱问答。  4 文档问答。  5 表格问答。  非必填字段。如果不填，会使用默认的机器人融合策略。

        :param query_types: The query_types of this PostRequestsReq.
        :type query_types: list[int]
        """
        self._query_types = query_types

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
        if not isinstance(other, PostRequestsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
