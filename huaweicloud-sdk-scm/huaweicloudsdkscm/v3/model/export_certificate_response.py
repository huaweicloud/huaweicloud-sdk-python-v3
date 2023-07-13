# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportCertificateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'entire_certificate': 'str',
        'certificate': 'str',
        'certificate_chain': 'str',
        'private_key': 'str',
        'enc_certificate': 'str',
        'enc_private_key': 'str'
    }

    attribute_map = {
        'entire_certificate': 'entire_certificate',
        'certificate': 'certificate',
        'certificate_chain': 'certificate_chain',
        'private_key': 'private_key',
        'enc_certificate': 'enc_certificate',
        'enc_private_key': 'enc_private_key'
    }

    def __init__(self, entire_certificate=None, certificate=None, certificate_chain=None, private_key=None, enc_certificate=None, enc_private_key=None):
        """ExportCertificateResponse

        The model defined in huaweicloud sdk

        :param entire_certificate: 证书及证书链。
        :type entire_certificate: str
        :param certificate: 证书内容，不包含证书链。
        :type certificate: str
        :param certificate_chain: 证书链。
        :type certificate_chain: str
        :param private_key: 证书私钥。
        :type private_key: str
        :param enc_certificate: 国密证书返回，加密证书内容。
        :type enc_certificate: str
        :param enc_private_key: 国密证书返回，加密证书私钥。
        :type enc_private_key: str
        """
        
        super(ExportCertificateResponse, self).__init__()

        self._entire_certificate = None
        self._certificate = None
        self._certificate_chain = None
        self._private_key = None
        self._enc_certificate = None
        self._enc_private_key = None
        self.discriminator = None

        if entire_certificate is not None:
            self.entire_certificate = entire_certificate
        if certificate is not None:
            self.certificate = certificate
        if certificate_chain is not None:
            self.certificate_chain = certificate_chain
        if private_key is not None:
            self.private_key = private_key
        if enc_certificate is not None:
            self.enc_certificate = enc_certificate
        if enc_private_key is not None:
            self.enc_private_key = enc_private_key

    @property
    def entire_certificate(self):
        """Gets the entire_certificate of this ExportCertificateResponse.

        证书及证书链。

        :return: The entire_certificate of this ExportCertificateResponse.
        :rtype: str
        """
        return self._entire_certificate

    @entire_certificate.setter
    def entire_certificate(self, entire_certificate):
        """Sets the entire_certificate of this ExportCertificateResponse.

        证书及证书链。

        :param entire_certificate: The entire_certificate of this ExportCertificateResponse.
        :type entire_certificate: str
        """
        self._entire_certificate = entire_certificate

    @property
    def certificate(self):
        """Gets the certificate of this ExportCertificateResponse.

        证书内容，不包含证书链。

        :return: The certificate of this ExportCertificateResponse.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this ExportCertificateResponse.

        证书内容，不包含证书链。

        :param certificate: The certificate of this ExportCertificateResponse.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def certificate_chain(self):
        """Gets the certificate_chain of this ExportCertificateResponse.

        证书链。

        :return: The certificate_chain of this ExportCertificateResponse.
        :rtype: str
        """
        return self._certificate_chain

    @certificate_chain.setter
    def certificate_chain(self, certificate_chain):
        """Sets the certificate_chain of this ExportCertificateResponse.

        证书链。

        :param certificate_chain: The certificate_chain of this ExportCertificateResponse.
        :type certificate_chain: str
        """
        self._certificate_chain = certificate_chain

    @property
    def private_key(self):
        """Gets the private_key of this ExportCertificateResponse.

        证书私钥。

        :return: The private_key of this ExportCertificateResponse.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this ExportCertificateResponse.

        证书私钥。

        :param private_key: The private_key of this ExportCertificateResponse.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def enc_certificate(self):
        """Gets the enc_certificate of this ExportCertificateResponse.

        国密证书返回，加密证书内容。

        :return: The enc_certificate of this ExportCertificateResponse.
        :rtype: str
        """
        return self._enc_certificate

    @enc_certificate.setter
    def enc_certificate(self, enc_certificate):
        """Sets the enc_certificate of this ExportCertificateResponse.

        国密证书返回，加密证书内容。

        :param enc_certificate: The enc_certificate of this ExportCertificateResponse.
        :type enc_certificate: str
        """
        self._enc_certificate = enc_certificate

    @property
    def enc_private_key(self):
        """Gets the enc_private_key of this ExportCertificateResponse.

        国密证书返回，加密证书私钥。

        :return: The enc_private_key of this ExportCertificateResponse.
        :rtype: str
        """
        return self._enc_private_key

    @enc_private_key.setter
    def enc_private_key(self, enc_private_key):
        """Sets the enc_private_key of this ExportCertificateResponse.

        国密证书返回，加密证书私钥。

        :param enc_private_key: The enc_private_key of this ExportCertificateResponse.
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
        if not isinstance(other, ExportCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
