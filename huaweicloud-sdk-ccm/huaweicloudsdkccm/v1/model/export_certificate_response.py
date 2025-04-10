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
        'private_key': 'str',
        'certificate': 'str',
        'certificate_chain': 'str',
        'enc_certificate': 'str',
        'enc_private_key': 'str',
        'enc_sm2_enveloped_key': 'str',
        'signed_and_enveloped_data': 'str'
    }

    attribute_map = {
        'private_key': 'private_key',
        'certificate': 'certificate',
        'certificate_chain': 'certificate_chain',
        'enc_certificate': 'enc_certificate',
        'enc_private_key': 'enc_private_key',
        'enc_sm2_enveloped_key': 'enc_sm2_enveloped_key',
        'signed_and_enveloped_data': 'signed_and_enveloped_data'
    }

    def __init__(self, private_key=None, certificate=None, certificate_chain=None, enc_certificate=None, enc_private_key=None, enc_sm2_enveloped_key=None, signed_and_enveloped_data=None):
        r"""ExportCertificateResponse

        The model defined in huaweicloud sdk

        :param private_key: 私钥内容。
        :type private_key: str
        :param certificate: 证书内容。
        :type certificate: str
        :param certificate_chain: 证书链内容。
        :type certificate_chain: str
        :param enc_certificate: 加密证书内容。
        :type enc_certificate: str
        :param enc_private_key: 加密私钥内容。
        :type enc_private_key: str
        :param enc_sm2_enveloped_key: 加密私钥的国密GMT0009标准规范SM2数字信封。
        :type enc_sm2_enveloped_key: str
        :param signed_and_enveloped_data: 加密私钥的国密GMT0010标准规范签名数字信封。
        :type signed_and_enveloped_data: str
        """
        
        super(ExportCertificateResponse, self).__init__()

        self._private_key = None
        self._certificate = None
        self._certificate_chain = None
        self._enc_certificate = None
        self._enc_private_key = None
        self._enc_sm2_enveloped_key = None
        self._signed_and_enveloped_data = None
        self.discriminator = None

        if private_key is not None:
            self.private_key = private_key
        if certificate is not None:
            self.certificate = certificate
        if certificate_chain is not None:
            self.certificate_chain = certificate_chain
        if enc_certificate is not None:
            self.enc_certificate = enc_certificate
        if enc_private_key is not None:
            self.enc_private_key = enc_private_key
        if enc_sm2_enveloped_key is not None:
            self.enc_sm2_enveloped_key = enc_sm2_enveloped_key
        if signed_and_enveloped_data is not None:
            self.signed_and_enveloped_data = signed_and_enveloped_data

    @property
    def private_key(self):
        r"""Gets the private_key of this ExportCertificateResponse.

        私钥内容。

        :return: The private_key of this ExportCertificateResponse.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this ExportCertificateResponse.

        私钥内容。

        :param private_key: The private_key of this ExportCertificateResponse.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def certificate(self):
        r"""Gets the certificate of this ExportCertificateResponse.

        证书内容。

        :return: The certificate of this ExportCertificateResponse.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this ExportCertificateResponse.

        证书内容。

        :param certificate: The certificate of this ExportCertificateResponse.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def certificate_chain(self):
        r"""Gets the certificate_chain of this ExportCertificateResponse.

        证书链内容。

        :return: The certificate_chain of this ExportCertificateResponse.
        :rtype: str
        """
        return self._certificate_chain

    @certificate_chain.setter
    def certificate_chain(self, certificate_chain):
        r"""Sets the certificate_chain of this ExportCertificateResponse.

        证书链内容。

        :param certificate_chain: The certificate_chain of this ExportCertificateResponse.
        :type certificate_chain: str
        """
        self._certificate_chain = certificate_chain

    @property
    def enc_certificate(self):
        r"""Gets the enc_certificate of this ExportCertificateResponse.

        加密证书内容。

        :return: The enc_certificate of this ExportCertificateResponse.
        :rtype: str
        """
        return self._enc_certificate

    @enc_certificate.setter
    def enc_certificate(self, enc_certificate):
        r"""Sets the enc_certificate of this ExportCertificateResponse.

        加密证书内容。

        :param enc_certificate: The enc_certificate of this ExportCertificateResponse.
        :type enc_certificate: str
        """
        self._enc_certificate = enc_certificate

    @property
    def enc_private_key(self):
        r"""Gets the enc_private_key of this ExportCertificateResponse.

        加密私钥内容。

        :return: The enc_private_key of this ExportCertificateResponse.
        :rtype: str
        """
        return self._enc_private_key

    @enc_private_key.setter
    def enc_private_key(self, enc_private_key):
        r"""Sets the enc_private_key of this ExportCertificateResponse.

        加密私钥内容。

        :param enc_private_key: The enc_private_key of this ExportCertificateResponse.
        :type enc_private_key: str
        """
        self._enc_private_key = enc_private_key

    @property
    def enc_sm2_enveloped_key(self):
        r"""Gets the enc_sm2_enveloped_key of this ExportCertificateResponse.

        加密私钥的国密GMT0009标准规范SM2数字信封。

        :return: The enc_sm2_enveloped_key of this ExportCertificateResponse.
        :rtype: str
        """
        return self._enc_sm2_enveloped_key

    @enc_sm2_enveloped_key.setter
    def enc_sm2_enveloped_key(self, enc_sm2_enveloped_key):
        r"""Sets the enc_sm2_enveloped_key of this ExportCertificateResponse.

        加密私钥的国密GMT0009标准规范SM2数字信封。

        :param enc_sm2_enveloped_key: The enc_sm2_enveloped_key of this ExportCertificateResponse.
        :type enc_sm2_enveloped_key: str
        """
        self._enc_sm2_enveloped_key = enc_sm2_enveloped_key

    @property
    def signed_and_enveloped_data(self):
        r"""Gets the signed_and_enveloped_data of this ExportCertificateResponse.

        加密私钥的国密GMT0010标准规范签名数字信封。

        :return: The signed_and_enveloped_data of this ExportCertificateResponse.
        :rtype: str
        """
        return self._signed_and_enveloped_data

    @signed_and_enveloped_data.setter
    def signed_and_enveloped_data(self, signed_and_enveloped_data):
        r"""Sets the signed_and_enveloped_data of this ExportCertificateResponse.

        加密私钥的国密GMT0010标准规范签名数字信封。

        :param signed_and_enveloped_data: The signed_and_enveloped_data of this ExportCertificateResponse.
        :type signed_and_enveloped_data: str
        """
        self._signed_and_enveloped_data = signed_and_enveloped_data

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
