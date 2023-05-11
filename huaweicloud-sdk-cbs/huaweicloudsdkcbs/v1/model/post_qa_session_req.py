# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostQaSessionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extends': 'SessionExtends',
        'chat_enable': 'bool',
        'user_id': 'str',
        'question': 'str'
    }

    attribute_map = {
        'extends': 'extends',
        'chat_enable': 'chat_enable',
        'user_id': 'user_id',
        'question': 'question'
    }

    def __init__(self, extends=None, chat_enable=None, user_id=None, question=None):
        """PostQaSessionReq

        The model defined in huaweicloud sdk

        :param extends: 
        :type extends: :class:`huaweicloudsdkcbs.v1.SessionExtends`
        :param chat_enable: 默认true true：使用内部闲聊语料进行兜底 false：不使用闲聊兜底
        :type chat_enable: bool
        :param user_id: 用户id，在日志中用于标识不通用户，可以为任意String。
        :type user_id: str
        :param question: 用户输入。
        :type question: str
        """
        
        

        self._extends = None
        self._chat_enable = None
        self._user_id = None
        self._question = None
        self.discriminator = None

        if extends is not None:
            self.extends = extends
        if chat_enable is not None:
            self.chat_enable = chat_enable
        if user_id is not None:
            self.user_id = user_id
        self.question = question

    @property
    def extends(self):
        """Gets the extends of this PostQaSessionReq.

        :return: The extends of this PostQaSessionReq.
        :rtype: :class:`huaweicloudsdkcbs.v1.SessionExtends`
        """
        return self._extends

    @extends.setter
    def extends(self, extends):
        """Sets the extends of this PostQaSessionReq.

        :param extends: The extends of this PostQaSessionReq.
        :type extends: :class:`huaweicloudsdkcbs.v1.SessionExtends`
        """
        self._extends = extends

    @property
    def chat_enable(self):
        """Gets the chat_enable of this PostQaSessionReq.

        默认true true：使用内部闲聊语料进行兜底 false：不使用闲聊兜底

        :return: The chat_enable of this PostQaSessionReq.
        :rtype: bool
        """
        return self._chat_enable

    @chat_enable.setter
    def chat_enable(self, chat_enable):
        """Sets the chat_enable of this PostQaSessionReq.

        默认true true：使用内部闲聊语料进行兜底 false：不使用闲聊兜底

        :param chat_enable: The chat_enable of this PostQaSessionReq.
        :type chat_enable: bool
        """
        self._chat_enable = chat_enable

    @property
    def user_id(self):
        """Gets the user_id of this PostQaSessionReq.

        用户id，在日志中用于标识不通用户，可以为任意String。

        :return: The user_id of this PostQaSessionReq.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this PostQaSessionReq.

        用户id，在日志中用于标识不通用户，可以为任意String。

        :param user_id: The user_id of this PostQaSessionReq.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def question(self):
        """Gets the question of this PostQaSessionReq.

        用户输入。

        :return: The question of this PostQaSessionReq.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this PostQaSessionReq.

        用户输入。

        :param question: The question of this PostQaSessionReq.
        :type question: str
        """
        self._question = question

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
        if not isinstance(other, PostQaSessionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
