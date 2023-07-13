# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostOldRequestsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extends': 'OldExtends',
        'chat_enable': 'bool',
        'threshold_enable': 'bool',
        'user_id': 'str',
        'question': 'str',
        'operate_type': 'int',
        'session_id': 'str'
    }

    attribute_map = {
        'extends': 'extends',
        'chat_enable': 'chat_enable',
        'threshold_enable': 'threshold_enable',
        'user_id': 'user_id',
        'question': 'question',
        'operate_type': 'operate_type',
        'session_id': 'session_id'
    }

    def __init__(self, extends=None, chat_enable=None, threshold_enable=None, user_id=None, question=None, operate_type=None, session_id=None):
        """PostOldRequestsReq

        The model defined in huaweicloud sdk

        :param extends: 
        :type extends: :class:`huaweicloudsdkcbs.v1.OldExtends`
        :param chat_enable: 默认false true：使用内部闲聊语料进行兜底 false：不使用闲聊兜底
        :type chat_enable: bool
        :param threshold_enable: true：启动内部阈值 返回经过阈值处理之后的答案。 false：不启用内部阈值 返回原答案。
        :type threshold_enable: bool
        :param user_id: 用户id，在日志中用于标识不通用户，可以为任意String
        :type user_id: str
        :param question: 用户输入
        :type question: str
        :param operate_type: 调用接口时候传入，用以标记的问答的行为，默认为0，最终会展示在问答日志里。 0 用户输入 1 单击热点问题 3 单击推荐问题 4 单击问题提示
        :type operate_type: int
        :param session_id: 会话标识符，UUID格式。如：c04e6f7b-61d7-4a2d-a0c8-f9ecd2f62359。  每次对话开启，机器人创建会话id，下次请求中传入该id表示继续该轮对话，每轮会话有效时间为2分钟。 若传入的会话id已过期或者为空，则机器人会重新创建新的会话id（重新创建会话id会消耗一定时间）。
        :type session_id: str
        """
        
        

        self._extends = None
        self._chat_enable = None
        self._threshold_enable = None
        self._user_id = None
        self._question = None
        self._operate_type = None
        self._session_id = None
        self.discriminator = None

        if extends is not None:
            self.extends = extends
        if chat_enable is not None:
            self.chat_enable = chat_enable
        if threshold_enable is not None:
            self.threshold_enable = threshold_enable
        if user_id is not None:
            self.user_id = user_id
        self.question = question
        if operate_type is not None:
            self.operate_type = operate_type
        if session_id is not None:
            self.session_id = session_id

    @property
    def extends(self):
        """Gets the extends of this PostOldRequestsReq.

        :return: The extends of this PostOldRequestsReq.
        :rtype: :class:`huaweicloudsdkcbs.v1.OldExtends`
        """
        return self._extends

    @extends.setter
    def extends(self, extends):
        """Sets the extends of this PostOldRequestsReq.

        :param extends: The extends of this PostOldRequestsReq.
        :type extends: :class:`huaweicloudsdkcbs.v1.OldExtends`
        """
        self._extends = extends

    @property
    def chat_enable(self):
        """Gets the chat_enable of this PostOldRequestsReq.

        默认false true：使用内部闲聊语料进行兜底 false：不使用闲聊兜底

        :return: The chat_enable of this PostOldRequestsReq.
        :rtype: bool
        """
        return self._chat_enable

    @chat_enable.setter
    def chat_enable(self, chat_enable):
        """Sets the chat_enable of this PostOldRequestsReq.

        默认false true：使用内部闲聊语料进行兜底 false：不使用闲聊兜底

        :param chat_enable: The chat_enable of this PostOldRequestsReq.
        :type chat_enable: bool
        """
        self._chat_enable = chat_enable

    @property
    def threshold_enable(self):
        """Gets the threshold_enable of this PostOldRequestsReq.

        true：启动内部阈值 返回经过阈值处理之后的答案。 false：不启用内部阈值 返回原答案。

        :return: The threshold_enable of this PostOldRequestsReq.
        :rtype: bool
        """
        return self._threshold_enable

    @threshold_enable.setter
    def threshold_enable(self, threshold_enable):
        """Sets the threshold_enable of this PostOldRequestsReq.

        true：启动内部阈值 返回经过阈值处理之后的答案。 false：不启用内部阈值 返回原答案。

        :param threshold_enable: The threshold_enable of this PostOldRequestsReq.
        :type threshold_enable: bool
        """
        self._threshold_enable = threshold_enable

    @property
    def user_id(self):
        """Gets the user_id of this PostOldRequestsReq.

        用户id，在日志中用于标识不通用户，可以为任意String

        :return: The user_id of this PostOldRequestsReq.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this PostOldRequestsReq.

        用户id，在日志中用于标识不通用户，可以为任意String

        :param user_id: The user_id of this PostOldRequestsReq.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def question(self):
        """Gets the question of this PostOldRequestsReq.

        用户输入

        :return: The question of this PostOldRequestsReq.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this PostOldRequestsReq.

        用户输入

        :param question: The question of this PostOldRequestsReq.
        :type question: str
        """
        self._question = question

    @property
    def operate_type(self):
        """Gets the operate_type of this PostOldRequestsReq.

        调用接口时候传入，用以标记的问答的行为，默认为0，最终会展示在问答日志里。 0 用户输入 1 单击热点问题 3 单击推荐问题 4 单击问题提示

        :return: The operate_type of this PostOldRequestsReq.
        :rtype: int
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        """Sets the operate_type of this PostOldRequestsReq.

        调用接口时候传入，用以标记的问答的行为，默认为0，最终会展示在问答日志里。 0 用户输入 1 单击热点问题 3 单击推荐问题 4 单击问题提示

        :param operate_type: The operate_type of this PostOldRequestsReq.
        :type operate_type: int
        """
        self._operate_type = operate_type

    @property
    def session_id(self):
        """Gets the session_id of this PostOldRequestsReq.

        会话标识符，UUID格式。如：c04e6f7b-61d7-4a2d-a0c8-f9ecd2f62359。  每次对话开启，机器人创建会话id，下次请求中传入该id表示继续该轮对话，每轮会话有效时间为2分钟。 若传入的会话id已过期或者为空，则机器人会重新创建新的会话id（重新创建会话id会消耗一定时间）。

        :return: The session_id of this PostOldRequestsReq.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this PostOldRequestsReq.

        会话标识符，UUID格式。如：c04e6f7b-61d7-4a2d-a0c8-f9ecd2f62359。  每次对话开启，机器人创建会话id，下次请求中传入该id表示继续该轮对话，每轮会话有效时间为2分钟。 若传入的会话id已过期或者为空，则机器人会重新创建新的会话id（重新创建会话id会消耗一定时间）。

        :param session_id: The session_id of this PostOldRequestsReq.
        :type session_id: str
        """
        self._session_id = session_id

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
        if not isinstance(other, PostOldRequestsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
