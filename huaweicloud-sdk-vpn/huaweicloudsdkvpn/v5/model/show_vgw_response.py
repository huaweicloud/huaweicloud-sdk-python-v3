# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVgwResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpn_gateway': 'ResponseVpnGateway',
        'request_id': 'str'
    }

    attribute_map = {
        'vpn_gateway': 'vpn_gateway',
        'request_id': 'request_id'
    }

    def __init__(self, vpn_gateway=None, request_id=None):
        """ShowVgwResponse

        The model defined in huaweicloud sdk

        :param vpn_gateway: 
        :type vpn_gateway: :class:`huaweicloudsdkvpn.v5.ResponseVpnGateway`
        :param request_id: 请求ID
        :type request_id: str
        """
        
        super(ShowVgwResponse, self).__init__()

        self._vpn_gateway = None
        self._request_id = None
        self.discriminator = None

        if vpn_gateway is not None:
            self.vpn_gateway = vpn_gateway
        if request_id is not None:
            self.request_id = request_id

    @property
    def vpn_gateway(self):
        """Gets the vpn_gateway of this ShowVgwResponse.

        :return: The vpn_gateway of this ShowVgwResponse.
        :rtype: :class:`huaweicloudsdkvpn.v5.ResponseVpnGateway`
        """
        return self._vpn_gateway

    @vpn_gateway.setter
    def vpn_gateway(self, vpn_gateway):
        """Sets the vpn_gateway of this ShowVgwResponse.

        :param vpn_gateway: The vpn_gateway of this ShowVgwResponse.
        :type vpn_gateway: :class:`huaweicloudsdkvpn.v5.ResponseVpnGateway`
        """
        self._vpn_gateway = vpn_gateway

    @property
    def request_id(self):
        """Gets the request_id of this ShowVgwResponse.

        请求ID

        :return: The request_id of this ShowVgwResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowVgwResponse.

        请求ID

        :param request_id: The request_id of this ShowVgwResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ShowVgwResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
