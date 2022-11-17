# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSessionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_id': 'str',
        'greeting': 'str'
    }

    attribute_map = {
        'session_id': 'session_id',
        'greeting': 'greeting'
    }

    def __init__(self, session_id=None, greeting=None):
        """CreateSessionResponse

        The model defined in huaweicloud sdk

        :param session_id: 会话标识符。
        :type session_id: str
        :param greeting: 机器人问候语。
        :type greeting: str
        """
        
        super(CreateSessionResponse, self).__init__()

        self._session_id = None
        self._greeting = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if greeting is not None:
            self.greeting = greeting

    @property
    def session_id(self):
        """Gets the session_id of this CreateSessionResponse.

        会话标识符。

        :return: The session_id of this CreateSessionResponse.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this CreateSessionResponse.

        会话标识符。

        :param session_id: The session_id of this CreateSessionResponse.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def greeting(self):
        """Gets the greeting of this CreateSessionResponse.

        机器人问候语。

        :return: The greeting of this CreateSessionResponse.
        :rtype: str
        """
        return self._greeting

    @greeting.setter
    def greeting(self, greeting):
        """Sets the greeting of this CreateSessionResponse.

        机器人问候语。

        :param greeting: The greeting of this CreateSessionResponse.
        :type greeting: str
        """
        self._greeting = greeting

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
        if not isinstance(other, CreateSessionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
