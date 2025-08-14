# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportExternalIdPCertificateReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x509_certificate_in_pem': 'str',
        'certificate_use': 'str'
    }

    attribute_map = {
        'x509_certificate_in_pem': 'x509_certificate_in_pem',
        'certificate_use': 'certificate_use'
    }

    def __init__(self, x509_certificate_in_pem=None, certificate_use=None):
        r"""ImportExternalIdPCertificateReqBody

        The model defined in huaweicloud sdk

        :param x509_certificate_in_pem: PEM格式的身份提供商证书内容
        :type x509_certificate_in_pem: str
        :param certificate_use: 身份提供商证书用途，目前仅支持签名
        :type certificate_use: str
        """
        
        

        self._x509_certificate_in_pem = None
        self._certificate_use = None
        self.discriminator = None

        self.x509_certificate_in_pem = x509_certificate_in_pem
        self.certificate_use = certificate_use

    @property
    def x509_certificate_in_pem(self):
        r"""Gets the x509_certificate_in_pem of this ImportExternalIdPCertificateReqBody.

        PEM格式的身份提供商证书内容

        :return: The x509_certificate_in_pem of this ImportExternalIdPCertificateReqBody.
        :rtype: str
        """
        return self._x509_certificate_in_pem

    @x509_certificate_in_pem.setter
    def x509_certificate_in_pem(self, x509_certificate_in_pem):
        r"""Sets the x509_certificate_in_pem of this ImportExternalIdPCertificateReqBody.

        PEM格式的身份提供商证书内容

        :param x509_certificate_in_pem: The x509_certificate_in_pem of this ImportExternalIdPCertificateReqBody.
        :type x509_certificate_in_pem: str
        """
        self._x509_certificate_in_pem = x509_certificate_in_pem

    @property
    def certificate_use(self):
        r"""Gets the certificate_use of this ImportExternalIdPCertificateReqBody.

        身份提供商证书用途，目前仅支持签名

        :return: The certificate_use of this ImportExternalIdPCertificateReqBody.
        :rtype: str
        """
        return self._certificate_use

    @certificate_use.setter
    def certificate_use(self, certificate_use):
        r"""Sets the certificate_use of this ImportExternalIdPCertificateReqBody.

        身份提供商证书用途，目前仅支持签名

        :param certificate_use: The certificate_use of this ImportExternalIdPCertificateReqBody.
        :type certificate_use: str
        """
        self._certificate_use = certificate_use

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
        if not isinstance(other, ImportExternalIdPCertificateReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
