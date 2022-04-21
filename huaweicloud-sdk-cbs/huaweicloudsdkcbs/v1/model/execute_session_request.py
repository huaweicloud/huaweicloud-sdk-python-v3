# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteSessionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'qabot_id': 'str',
        'session_id': 'str',
        'body': 'PostQaSessionReq'
    }

    attribute_map = {
        'qabot_id': 'qabot_id',
        'session_id': 'session_id',
        'body': 'body'
    }

    def __init__(self, qabot_id=None, session_id=None, body=None):
        """ExecuteSessionRequest

        The model defined in huaweicloud sdk

        :param qabot_id: 机器人标识符。
        :type qabot_id: str
        :param session_id: 会话标识符。
        :type session_id: str
        :param body: Body of the ExecuteSessionRequest
        :type body: :class:`huaweicloudsdkcbs.v1.PostQaSessionReq`
        """
        
        

        self._qabot_id = None
        self._session_id = None
        self._body = None
        self.discriminator = None

        self.qabot_id = qabot_id
        self.session_id = session_id
        if body is not None:
            self.body = body

    @property
    def qabot_id(self):
        """Gets the qabot_id of this ExecuteSessionRequest.

        机器人标识符。

        :return: The qabot_id of this ExecuteSessionRequest.
        :rtype: str
        """
        return self._qabot_id

    @qabot_id.setter
    def qabot_id(self, qabot_id):
        """Sets the qabot_id of this ExecuteSessionRequest.

        机器人标识符。

        :param qabot_id: The qabot_id of this ExecuteSessionRequest.
        :type qabot_id: str
        """
        self._qabot_id = qabot_id

    @property
    def session_id(self):
        """Gets the session_id of this ExecuteSessionRequest.

        会话标识符。

        :return: The session_id of this ExecuteSessionRequest.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this ExecuteSessionRequest.

        会话标识符。

        :param session_id: The session_id of this ExecuteSessionRequest.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def body(self):
        """Gets the body of this ExecuteSessionRequest.


        :return: The body of this ExecuteSessionRequest.
        :rtype: :class:`huaweicloudsdkcbs.v1.PostQaSessionReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ExecuteSessionRequest.


        :param body: The body of this ExecuteSessionRequest.
        :type body: :class:`huaweicloudsdkcbs.v1.PostQaSessionReq`
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
        if not isinstance(other, ExecuteSessionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
