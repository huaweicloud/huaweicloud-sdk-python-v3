# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWebSocketTokenResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'web_socket_token': 'str'
    }

    attribute_map = {
        'web_socket_token': 'webSocketToken'
    }

    def __init__(self, web_socket_token=None):
        r"""CreateWebSocketTokenResponse

        The model defined in huaweicloud sdk

        :param web_socket_token: WebSocket建链Token(有效期1分钟，且一次有效)。
        :type web_socket_token: str
        """
        
        super(CreateWebSocketTokenResponse, self).__init__()

        self._web_socket_token = None
        self.discriminator = None

        if web_socket_token is not None:
            self.web_socket_token = web_socket_token

    @property
    def web_socket_token(self):
        r"""Gets the web_socket_token of this CreateWebSocketTokenResponse.

        WebSocket建链Token(有效期1分钟，且一次有效)。

        :return: The web_socket_token of this CreateWebSocketTokenResponse.
        :rtype: str
        """
        return self._web_socket_token

    @web_socket_token.setter
    def web_socket_token(self, web_socket_token):
        r"""Sets the web_socket_token of this CreateWebSocketTokenResponse.

        WebSocket建链Token(有效期1分钟，且一次有效)。

        :param web_socket_token: The web_socket_token of this CreateWebSocketTokenResponse.
        :type web_socket_token: str
        """
        self._web_socket_token = web_socket_token

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
        if not isinstance(other, CreateWebSocketTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
