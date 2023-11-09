# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVgwResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpn_gateway': 'UpdateResponseVpnGateway',
        'request_id': 'str',
        'header_response_token': 'str'
    }

    attribute_map = {
        'vpn_gateway': 'vpn_gateway',
        'request_id': 'request_id',
        'header_response_token': 'header-response-token'
    }

    def __init__(self, vpn_gateway=None, request_id=None, header_response_token=None):
        """UpdateVgwResponse

        The model defined in huaweicloud sdk

        :param vpn_gateway: 
        :type vpn_gateway: :class:`huaweicloudsdkvpn.v5.UpdateResponseVpnGateway`
        :param request_id: 请求ID
        :type request_id: str
        :param header_response_token: 
        :type header_response_token: str
        """
        
        super(UpdateVgwResponse, self).__init__()

        self._vpn_gateway = None
        self._request_id = None
        self._header_response_token = None
        self.discriminator = None

        if vpn_gateway is not None:
            self.vpn_gateway = vpn_gateway
        if request_id is not None:
            self.request_id = request_id
        if header_response_token is not None:
            self.header_response_token = header_response_token

    @property
    def vpn_gateway(self):
        """Gets the vpn_gateway of this UpdateVgwResponse.

        :return: The vpn_gateway of this UpdateVgwResponse.
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateResponseVpnGateway`
        """
        return self._vpn_gateway

    @vpn_gateway.setter
    def vpn_gateway(self, vpn_gateway):
        """Sets the vpn_gateway of this UpdateVgwResponse.

        :param vpn_gateway: The vpn_gateway of this UpdateVgwResponse.
        :type vpn_gateway: :class:`huaweicloudsdkvpn.v5.UpdateResponseVpnGateway`
        """
        self._vpn_gateway = vpn_gateway

    @property
    def request_id(self):
        """Gets the request_id of this UpdateVgwResponse.

        请求ID

        :return: The request_id of this UpdateVgwResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this UpdateVgwResponse.

        请求ID

        :param request_id: The request_id of this UpdateVgwResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def header_response_token(self):
        """Gets the header_response_token of this UpdateVgwResponse.

        :return: The header_response_token of this UpdateVgwResponse.
        :rtype: str
        """
        return self._header_response_token

    @header_response_token.setter
    def header_response_token(self, header_response_token):
        """Sets the header_response_token of this UpdateVgwResponse.

        :param header_response_token: The header_response_token of this UpdateVgwResponse.
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
        if not isinstance(other, UpdateVgwResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
