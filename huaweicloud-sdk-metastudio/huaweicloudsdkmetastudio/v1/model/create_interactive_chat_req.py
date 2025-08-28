# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInteractiveChatReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_id': 'str',
        'message': 'str',
        'session_id': 'str',
        'language': 'LanguageEnum'
    }

    attribute_map = {
        'role_id': 'role_id',
        'message': 'message',
        'session_id': 'session_id',
        'language': 'language'
    }

    def __init__(self, role_id=None, message=None, session_id=None, language=None):
        r"""CreateInteractiveChatReq

        The model defined in huaweicloud sdk

        :param role_id: 角色ID。
        :type role_id: str
        :param message: 问题
        :type message: str
        :param session_id: 当前对话的唯一标识，用于关联对话上下文内容。
        :type session_id: str
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        
        

        self._role_id = None
        self._message = None
        self._session_id = None
        self._language = None
        self.discriminator = None

        self.role_id = role_id
        self.message = message
        self.session_id = session_id
        if language is not None:
            self.language = language

    @property
    def role_id(self):
        r"""Gets the role_id of this CreateInteractiveChatReq.

        角色ID。

        :return: The role_id of this CreateInteractiveChatReq.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this CreateInteractiveChatReq.

        角色ID。

        :param role_id: The role_id of this CreateInteractiveChatReq.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def message(self):
        r"""Gets the message of this CreateInteractiveChatReq.

        问题

        :return: The message of this CreateInteractiveChatReq.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateInteractiveChatReq.

        问题

        :param message: The message of this CreateInteractiveChatReq.
        :type message: str
        """
        self._message = message

    @property
    def session_id(self):
        r"""Gets the session_id of this CreateInteractiveChatReq.

        当前对话的唯一标识，用于关联对话上下文内容。

        :return: The session_id of this CreateInteractiveChatReq.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this CreateInteractiveChatReq.

        当前对话的唯一标识，用于关联对话上下文内容。

        :param session_id: The session_id of this CreateInteractiveChatReq.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def language(self):
        r"""Gets the language of this CreateInteractiveChatReq.

        :return: The language of this CreateInteractiveChatReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this CreateInteractiveChatReq.

        :param language: The language of this CreateInteractiveChatReq.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

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
        if not isinstance(other, CreateInteractiveChatReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
