# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpnGatewayCertificatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpn_gateway_certificates': 'list[VpnGatewayCertificate]',
        'request_id': 'str'
    }

    attribute_map = {
        'vpn_gateway_certificates': 'vpn_gateway_certificates',
        'request_id': 'request_id'
    }

    def __init__(self, vpn_gateway_certificates=None, request_id=None):
        r"""ListVpnGatewayCertificatesResponse

        The model defined in huaweicloud sdk

        :param vpn_gateway_certificates: VPN网关证书信息
        :type vpn_gateway_certificates: list[:class:`huaweicloudsdkvpn.v5.VpnGatewayCertificate`]
        :param request_id: 请求id
        :type request_id: str
        """
        
        super().__init__()

        self._vpn_gateway_certificates = None
        self._request_id = None
        self.discriminator = None

        if vpn_gateway_certificates is not None:
            self.vpn_gateway_certificates = vpn_gateway_certificates
        if request_id is not None:
            self.request_id = request_id

    @property
    def vpn_gateway_certificates(self):
        r"""Gets the vpn_gateway_certificates of this ListVpnGatewayCertificatesResponse.

        VPN网关证书信息

        :return: The vpn_gateway_certificates of this ListVpnGatewayCertificatesResponse.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.VpnGatewayCertificate`]
        """
        return self._vpn_gateway_certificates

    @vpn_gateway_certificates.setter
    def vpn_gateway_certificates(self, vpn_gateway_certificates):
        r"""Sets the vpn_gateway_certificates of this ListVpnGatewayCertificatesResponse.

        VPN网关证书信息

        :param vpn_gateway_certificates: The vpn_gateway_certificates of this ListVpnGatewayCertificatesResponse.
        :type vpn_gateway_certificates: list[:class:`huaweicloudsdkvpn.v5.VpnGatewayCertificate`]
        """
        self._vpn_gateway_certificates = vpn_gateway_certificates

    @property
    def request_id(self):
        r"""Gets the request_id of this ListVpnGatewayCertificatesResponse.

        请求id

        :return: The request_id of this ListVpnGatewayCertificatesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListVpnGatewayCertificatesResponse.

        请求id

        :param request_id: The request_id of this ListVpnGatewayCertificatesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    def to_dict(self):
        import warnings
        warnings.warn("ListVpnGatewayCertificatesResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListVpnGatewayCertificatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
