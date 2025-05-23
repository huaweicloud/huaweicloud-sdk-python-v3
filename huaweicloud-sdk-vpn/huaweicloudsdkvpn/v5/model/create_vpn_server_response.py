# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVpnServerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpn_server': 'CreateServerResponseBodyVpnServer',
        'request_id': 'str',
        'header_response_token': 'str'
    }

    attribute_map = {
        'vpn_server': 'vpn_server',
        'request_id': 'request_id',
        'header_response_token': 'header-response-token'
    }

    def __init__(self, vpn_server=None, request_id=None, header_response_token=None):
        r"""CreateVpnServerResponse

        The model defined in huaweicloud sdk

        :param vpn_server: 
        :type vpn_server: :class:`huaweicloudsdkvpn.v5.CreateServerResponseBodyVpnServer`
        :param request_id: 请求id
        :type request_id: str
        :param header_response_token: 
        :type header_response_token: str
        """
        
        super(CreateVpnServerResponse, self).__init__()

        self._vpn_server = None
        self._request_id = None
        self._header_response_token = None
        self.discriminator = None

        if vpn_server is not None:
            self.vpn_server = vpn_server
        if request_id is not None:
            self.request_id = request_id
        if header_response_token is not None:
            self.header_response_token = header_response_token

    @property
    def vpn_server(self):
        r"""Gets the vpn_server of this CreateVpnServerResponse.

        :return: The vpn_server of this CreateVpnServerResponse.
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateServerResponseBodyVpnServer`
        """
        return self._vpn_server

    @vpn_server.setter
    def vpn_server(self, vpn_server):
        r"""Sets the vpn_server of this CreateVpnServerResponse.

        :param vpn_server: The vpn_server of this CreateVpnServerResponse.
        :type vpn_server: :class:`huaweicloudsdkvpn.v5.CreateServerResponseBodyVpnServer`
        """
        self._vpn_server = vpn_server

    @property
    def request_id(self):
        r"""Gets the request_id of this CreateVpnServerResponse.

        请求id

        :return: The request_id of this CreateVpnServerResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this CreateVpnServerResponse.

        请求id

        :param request_id: The request_id of this CreateVpnServerResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def header_response_token(self):
        r"""Gets the header_response_token of this CreateVpnServerResponse.

        :return: The header_response_token of this CreateVpnServerResponse.
        :rtype: str
        """
        return self._header_response_token

    @header_response_token.setter
    def header_response_token(self, header_response_token):
        r"""Sets the header_response_token of this CreateVpnServerResponse.

        :param header_response_token: The header_response_token of this CreateVpnServerResponse.
        :type header_response_token: str
        """
        self._header_response_token = header_response_token

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
        if not isinstance(other, CreateVpnServerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
