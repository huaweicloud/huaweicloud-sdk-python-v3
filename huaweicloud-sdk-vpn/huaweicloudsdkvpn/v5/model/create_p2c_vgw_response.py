# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateP2cVgwResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'p2c_vpn_gateway': 'ResponseP2cVgw',
        'request_id': 'str',
        'header_response_token': 'str'
    }

    attribute_map = {
        'p2c_vpn_gateway': 'p2c_vpn_gateway',
        'request_id': 'request_id',
        'header_response_token': 'header-response-token'
    }

    def __init__(self, p2c_vpn_gateway=None, request_id=None, header_response_token=None):
        r"""CreateP2cVgwResponse

        The model defined in huaweicloud sdk

        :param p2c_vpn_gateway: 
        :type p2c_vpn_gateway: :class:`huaweicloudsdkvpn.v5.ResponseP2cVgw`
        :param request_id: 请求ID
        :type request_id: str
        :param header_response_token: 
        :type header_response_token: str
        """
        
        super(CreateP2cVgwResponse, self).__init__()

        self._p2c_vpn_gateway = None
        self._request_id = None
        self._header_response_token = None
        self.discriminator = None

        if p2c_vpn_gateway is not None:
            self.p2c_vpn_gateway = p2c_vpn_gateway
        if request_id is not None:
            self.request_id = request_id
        if header_response_token is not None:
            self.header_response_token = header_response_token

    @property
    def p2c_vpn_gateway(self):
        r"""Gets the p2c_vpn_gateway of this CreateP2cVgwResponse.

        :return: The p2c_vpn_gateway of this CreateP2cVgwResponse.
        :rtype: :class:`huaweicloudsdkvpn.v5.ResponseP2cVgw`
        """
        return self._p2c_vpn_gateway

    @p2c_vpn_gateway.setter
    def p2c_vpn_gateway(self, p2c_vpn_gateway):
        r"""Sets the p2c_vpn_gateway of this CreateP2cVgwResponse.

        :param p2c_vpn_gateway: The p2c_vpn_gateway of this CreateP2cVgwResponse.
        :type p2c_vpn_gateway: :class:`huaweicloudsdkvpn.v5.ResponseP2cVgw`
        """
        self._p2c_vpn_gateway = p2c_vpn_gateway

    @property
    def request_id(self):
        r"""Gets the request_id of this CreateP2cVgwResponse.

        请求ID

        :return: The request_id of this CreateP2cVgwResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this CreateP2cVgwResponse.

        请求ID

        :param request_id: The request_id of this CreateP2cVgwResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def header_response_token(self):
        r"""Gets the header_response_token of this CreateP2cVgwResponse.

        :return: The header_response_token of this CreateP2cVgwResponse.
        :rtype: str
        """
        return self._header_response_token

    @header_response_token.setter
    def header_response_token(self, header_response_token):
        r"""Sets the header_response_token of this CreateP2cVgwResponse.

        :param header_response_token: The header_response_token of this CreateP2cVgwResponse.
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
        if not isinstance(other, CreateP2cVgwResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
