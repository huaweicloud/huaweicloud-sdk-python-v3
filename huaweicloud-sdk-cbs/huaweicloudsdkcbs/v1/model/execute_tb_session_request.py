# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteTbSessionRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bot_id': 'str',
        'session_id': 'str',
        'body': 'ExecuteTbSessionReq'
    }

    attribute_map = {
        'bot_id': 'bot_id',
        'session_id': 'session_id',
        'body': 'body'
    }

    def __init__(self, bot_id=None, session_id=None, body=None):
        """ExecuteTbSessionRequest - a model defined in huaweicloud sdk"""
        
        

        self._bot_id = None
        self._session_id = None
        self._body = None
        self.discriminator = None

        self.bot_id = bot_id
        self.session_id = session_id
        if body is not None:
            self.body = body

    @property
    def bot_id(self):
        """Gets the bot_id of this ExecuteTbSessionRequest.

        话务机器人ID

        :return: The bot_id of this ExecuteTbSessionRequest.
        :rtype: str
        """
        return self._bot_id

    @bot_id.setter
    def bot_id(self, bot_id):
        """Sets the bot_id of this ExecuteTbSessionRequest.

        话务机器人ID

        :param bot_id: The bot_id of this ExecuteTbSessionRequest.
        :type: str
        """
        self._bot_id = bot_id

    @property
    def session_id(self):
        """Gets the session_id of this ExecuteTbSessionRequest.

        会话ID，在发起会话API的请求结果消息体response当中产生。

        :return: The session_id of this ExecuteTbSessionRequest.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this ExecuteTbSessionRequest.

        会话ID，在发起会话API的请求结果消息体response当中产生。

        :param session_id: The session_id of this ExecuteTbSessionRequest.
        :type: str
        """
        self._session_id = session_id

    @property
    def body(self):
        """Gets the body of this ExecuteTbSessionRequest.


        :return: The body of this ExecuteTbSessionRequest.
        :rtype: ExecuteTbSessionReq
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ExecuteTbSessionRequest.


        :param body: The body of this ExecuteTbSessionRequest.
        :type: ExecuteTbSessionReq
        """
        self._body = body

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
        if not isinstance(other, ExecuteTbSessionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
