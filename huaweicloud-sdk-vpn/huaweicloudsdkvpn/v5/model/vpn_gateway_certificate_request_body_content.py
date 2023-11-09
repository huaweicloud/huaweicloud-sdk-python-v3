# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpnGatewayCertificateRequestBodyContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('certificate')
    sensitive_list.append('private_key')
    sensitive_list.append('certificate_chain')
    sensitive_list.append('enc_certificate')
    sensitive_list.append('enc_private_key')

    openapi_types = {
        'name': 'str',
        'certificate': 'str',
        'private_key': 'str',
        'certificate_chain': 'str',
        'enc_certificate': 'str',
        'enc_private_key': 'str'
    }

    attribute_map = {
        'name': 'name',
        'certificate': 'certificate',
        'private_key': 'private_key',
        'certificate_chain': 'certificate_chain',
        'enc_certificate': 'enc_certificate',
        'enc_private_key': 'enc_private_key'
    }

    def __init__(self, name=None, certificate=None, private_key=None, certificate_chain=None, enc_certificate=None, enc_private_key=None):
        """VpnGatewayCertificateRequestBodyContent

        The model defined in huaweicloud sdk

        :param name: VPN网关证书名称
        :type name: str
        :param certificate: 证书内容，国密证书时为签名证书内容
        :type certificate: str
        :param private_key: 证书私钥，国密证书时为签名证书私钥
        :type private_key: str
        :param certificate_chain: VPN网关CA证书内容
        :type certificate_chain: str
        :param enc_certificate: 国密证书的加密证书内容
        :type enc_certificate: str
        :param enc_private_key: 国密证书的加密证书私钥
        :type enc_private_key: str
        """
        
        

        self._name = None
        self._certificate = None
        self._private_key = None
        self._certificate_chain = None
        self._enc_certificate = None
        self._enc_private_key = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if certificate is not None:
            self.certificate = certificate
        if private_key is not None:
            self.private_key = private_key
        if certificate_chain is not None:
            self.certificate_chain = certificate_chain
        if enc_certificate is not None:
            self.enc_certificate = enc_certificate
        if enc_private_key is not None:
            self.enc_private_key = enc_private_key

    @property
    def name(self):
        """Gets the name of this VpnGatewayCertificateRequestBodyContent.

        VPN网关证书名称

        :return: The name of this VpnGatewayCertificateRequestBodyContent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VpnGatewayCertificateRequestBodyContent.

        VPN网关证书名称

        :param name: The name of this VpnGatewayCertificateRequestBodyContent.
        :type name: str
        """
        self._name = name

    @property
    def certificate(self):
        """Gets the certificate of this VpnGatewayCertificateRequestBodyContent.

        证书内容，国密证书时为签名证书内容

        :return: The certificate of this VpnGatewayCertificateRequestBodyContent.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this VpnGatewayCertificateRequestBodyContent.

        证书内容，国密证书时为签名证书内容

        :param certificate: The certificate of this VpnGatewayCertificateRequestBodyContent.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def private_key(self):
        """Gets the private_key of this VpnGatewayCertificateRequestBodyContent.

        证书私钥，国密证书时为签名证书私钥

        :return: The private_key of this VpnGatewayCertificateRequestBodyContent.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this VpnGatewayCertificateRequestBodyContent.

        证书私钥，国密证书时为签名证书私钥

        :param private_key: The private_key of this VpnGatewayCertificateRequestBodyContent.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def certificate_chain(self):
        """Gets the certificate_chain of this VpnGatewayCertificateRequestBodyContent.

        VPN网关CA证书内容

        :return: The certificate_chain of this VpnGatewayCertificateRequestBodyContent.
        :rtype: str
        """
        return self._certificate_chain

    @certificate_chain.setter
    def certificate_chain(self, certificate_chain):
        """Sets the certificate_chain of this VpnGatewayCertificateRequestBodyContent.

        VPN网关CA证书内容

        :param certificate_chain: The certificate_chain of this VpnGatewayCertificateRequestBodyContent.
        :type certificate_chain: str
        """
        self._certificate_chain = certificate_chain

    @property
    def enc_certificate(self):
        """Gets the enc_certificate of this VpnGatewayCertificateRequestBodyContent.

        国密证书的加密证书内容

        :return: The enc_certificate of this VpnGatewayCertificateRequestBodyContent.
        :rtype: str
        """
        return self._enc_certificate

    @enc_certificate.setter
    def enc_certificate(self, enc_certificate):
        """Sets the enc_certificate of this VpnGatewayCertificateRequestBodyContent.

        国密证书的加密证书内容

        :param enc_certificate: The enc_certificate of this VpnGatewayCertificateRequestBodyContent.
        :type enc_certificate: str
        """
        self._enc_certificate = enc_certificate

    @property
    def enc_private_key(self):
        """Gets the enc_private_key of this VpnGatewayCertificateRequestBodyContent.

        国密证书的加密证书私钥

        :return: The enc_private_key of this VpnGatewayCertificateRequestBodyContent.
        :rtype: str
        """
        return self._enc_private_key

    @enc_private_key.setter
    def enc_private_key(self, enc_private_key):
        """Sets the enc_private_key of this VpnGatewayCertificateRequestBodyContent.

        国密证书的加密证书私钥

        :param enc_private_key: The enc_private_key of this VpnGatewayCertificateRequestBodyContent.
        :type enc_private_key: str
        """
        self._enc_private_key = enc_private_key

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
        if not isinstance(other, VpnGatewayCertificateRequestBodyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
