# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddTunnelResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('tunnel_access_token')

    openapi_types = {
        'tunnel_id': 'str',
        'tunnel_access_token': 'str',
        'expires_in': 'int',
        'tunnel_uri': 'str'
    }

    attribute_map = {
        'tunnel_id': 'tunnel_id',
        'tunnel_access_token': 'tunnel_access_token',
        'expires_in': 'expires_in',
        'tunnel_uri': 'tunnel_uri'
    }

    def __init__(self, tunnel_id=None, tunnel_access_token=None, expires_in=None, tunnel_uri=None):
        """AddTunnelResponse

        The model defined in huaweicloud sdk

        :param tunnel_id: 隧道ID
        :type tunnel_id: str
        :param tunnel_access_token: 鉴权信息
        :type tunnel_access_token: str
        :param expires_in: 鉴权信息的过期时间, 单位：秒
        :type expires_in: int
        :param tunnel_uri: websocket接入地址
        :type tunnel_uri: str
        """
        
        super(AddTunnelResponse, self).__init__()

        self._tunnel_id = None
        self._tunnel_access_token = None
        self._expires_in = None
        self._tunnel_uri = None
        self.discriminator = None

        if tunnel_id is not None:
            self.tunnel_id = tunnel_id
        if tunnel_access_token is not None:
            self.tunnel_access_token = tunnel_access_token
        if expires_in is not None:
            self.expires_in = expires_in
        if tunnel_uri is not None:
            self.tunnel_uri = tunnel_uri

    @property
    def tunnel_id(self):
        """Gets the tunnel_id of this AddTunnelResponse.

        隧道ID

        :return: The tunnel_id of this AddTunnelResponse.
        :rtype: str
        """
        return self._tunnel_id

    @tunnel_id.setter
    def tunnel_id(self, tunnel_id):
        """Sets the tunnel_id of this AddTunnelResponse.

        隧道ID

        :param tunnel_id: The tunnel_id of this AddTunnelResponse.
        :type tunnel_id: str
        """
        self._tunnel_id = tunnel_id

    @property
    def tunnel_access_token(self):
        """Gets the tunnel_access_token of this AddTunnelResponse.

        鉴权信息

        :return: The tunnel_access_token of this AddTunnelResponse.
        :rtype: str
        """
        return self._tunnel_access_token

    @tunnel_access_token.setter
    def tunnel_access_token(self, tunnel_access_token):
        """Sets the tunnel_access_token of this AddTunnelResponse.

        鉴权信息

        :param tunnel_access_token: The tunnel_access_token of this AddTunnelResponse.
        :type tunnel_access_token: str
        """
        self._tunnel_access_token = tunnel_access_token

    @property
    def expires_in(self):
        """Gets the expires_in of this AddTunnelResponse.

        鉴权信息的过期时间, 单位：秒

        :return: The expires_in of this AddTunnelResponse.
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this AddTunnelResponse.

        鉴权信息的过期时间, 单位：秒

        :param expires_in: The expires_in of this AddTunnelResponse.
        :type expires_in: int
        """
        self._expires_in = expires_in

    @property
    def tunnel_uri(self):
        """Gets the tunnel_uri of this AddTunnelResponse.

        websocket接入地址

        :return: The tunnel_uri of this AddTunnelResponse.
        :rtype: str
        """
        return self._tunnel_uri

    @tunnel_uri.setter
    def tunnel_uri(self, tunnel_uri):
        """Sets the tunnel_uri of this AddTunnelResponse.

        websocket接入地址

        :param tunnel_uri: The tunnel_uri of this AddTunnelResponse.
        :type tunnel_uri: str
        """
        self._tunnel_uri = tunnel_uri

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
        if not isinstance(other, AddTunnelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
