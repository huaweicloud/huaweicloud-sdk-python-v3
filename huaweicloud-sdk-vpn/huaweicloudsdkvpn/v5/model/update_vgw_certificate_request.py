# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVgwCertificateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vgw_id': 'str',
        'certificate_id': 'str',
        'body': 'VpnGatewayCertificateRequestBody'
    }

    attribute_map = {
        'vgw_id': 'vgw_id',
        'certificate_id': 'certificate_id',
        'body': 'body'
    }

    def __init__(self, vgw_id=None, certificate_id=None, body=None):
        """UpdateVgwCertificateRequest

        The model defined in huaweicloud sdk

        :param vgw_id: VPN网关实例ID
        :type vgw_id: str
        :param certificate_id: VPN网关证书ID
        :type certificate_id: str
        :param body: Body of the UpdateVgwCertificateRequest
        :type body: :class:`huaweicloudsdkvpn.v5.VpnGatewayCertificateRequestBody`
        """
        
        

        self._vgw_id = None
        self._certificate_id = None
        self._body = None
        self.discriminator = None

        self.vgw_id = vgw_id
        self.certificate_id = certificate_id
        if body is not None:
            self.body = body

    @property
    def vgw_id(self):
        """Gets the vgw_id of this UpdateVgwCertificateRequest.

        VPN网关实例ID

        :return: The vgw_id of this UpdateVgwCertificateRequest.
        :rtype: str
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        """Sets the vgw_id of this UpdateVgwCertificateRequest.

        VPN网关实例ID

        :param vgw_id: The vgw_id of this UpdateVgwCertificateRequest.
        :type vgw_id: str
        """
        self._vgw_id = vgw_id

    @property
    def certificate_id(self):
        """Gets the certificate_id of this UpdateVgwCertificateRequest.

        VPN网关证书ID

        :return: The certificate_id of this UpdateVgwCertificateRequest.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this UpdateVgwCertificateRequest.

        VPN网关证书ID

        :param certificate_id: The certificate_id of this UpdateVgwCertificateRequest.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def body(self):
        """Gets the body of this UpdateVgwCertificateRequest.

        :return: The body of this UpdateVgwCertificateRequest.
        :rtype: :class:`huaweicloudsdkvpn.v5.VpnGatewayCertificateRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateVgwCertificateRequest.

        :param body: The body of this UpdateVgwCertificateRequest.
        :type body: :class:`huaweicloudsdkvpn.v5.VpnGatewayCertificateRequestBody`
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
        if not isinstance(other, UpdateVgwCertificateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
