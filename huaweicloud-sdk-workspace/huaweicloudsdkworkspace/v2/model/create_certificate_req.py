# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCertificateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'distinguished_name': 'DistinguishedName',
        'key_algorithm': 'str',
        'signature_algorithm': 'str',
        'validity': 'CertValidityData',
        'crl_configuration': 'CrlConfigurationData'
    }

    attribute_map = {
        'distinguished_name': 'distinguished_name',
        'key_algorithm': 'key_algorithm',
        'signature_algorithm': 'signature_algorithm',
        'validity': 'validity',
        'crl_configuration': 'crl_configuration'
    }

    def __init__(self, distinguished_name=None, key_algorithm=None, signature_algorithm=None, validity=None, crl_configuration=None):
        r"""CreateCertificateReq

        The model defined in huaweicloud sdk

        :param distinguished_name: 
        :type distinguished_name: :class:`huaweicloudsdkworkspace.v2.DistinguishedName`
        :param key_algorithm: 密钥对生成算法 RSA-2048 RSA-3072。
        :type key_algorithm: str
        :param signature_algorithm: 签名哈希算法 SHA-256 SHA-512。
        :type signature_algorithm: str
        :param validity: 
        :type validity: :class:`huaweicloudsdkworkspace.v2.CertValidityData`
        :param crl_configuration: 
        :type crl_configuration: :class:`huaweicloudsdkworkspace.v2.CrlConfigurationData`
        """
        
        

        self._distinguished_name = None
        self._key_algorithm = None
        self._signature_algorithm = None
        self._validity = None
        self._crl_configuration = None
        self.discriminator = None

        self.distinguished_name = distinguished_name
        self.key_algorithm = key_algorithm
        self.signature_algorithm = signature_algorithm
        self.validity = validity
        self.crl_configuration = crl_configuration

    @property
    def distinguished_name(self):
        r"""Gets the distinguished_name of this CreateCertificateReq.

        :return: The distinguished_name of this CreateCertificateReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.DistinguishedName`
        """
        return self._distinguished_name

    @distinguished_name.setter
    def distinguished_name(self, distinguished_name):
        r"""Sets the distinguished_name of this CreateCertificateReq.

        :param distinguished_name: The distinguished_name of this CreateCertificateReq.
        :type distinguished_name: :class:`huaweicloudsdkworkspace.v2.DistinguishedName`
        """
        self._distinguished_name = distinguished_name

    @property
    def key_algorithm(self):
        r"""Gets the key_algorithm of this CreateCertificateReq.

        密钥对生成算法 RSA-2048 RSA-3072。

        :return: The key_algorithm of this CreateCertificateReq.
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        r"""Sets the key_algorithm of this CreateCertificateReq.

        密钥对生成算法 RSA-2048 RSA-3072。

        :param key_algorithm: The key_algorithm of this CreateCertificateReq.
        :type key_algorithm: str
        """
        self._key_algorithm = key_algorithm

    @property
    def signature_algorithm(self):
        r"""Gets the signature_algorithm of this CreateCertificateReq.

        签名哈希算法 SHA-256 SHA-512。

        :return: The signature_algorithm of this CreateCertificateReq.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        r"""Sets the signature_algorithm of this CreateCertificateReq.

        签名哈希算法 SHA-256 SHA-512。

        :param signature_algorithm: The signature_algorithm of this CreateCertificateReq.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def validity(self):
        r"""Gets the validity of this CreateCertificateReq.

        :return: The validity of this CreateCertificateReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.CertValidityData`
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        r"""Sets the validity of this CreateCertificateReq.

        :param validity: The validity of this CreateCertificateReq.
        :type validity: :class:`huaweicloudsdkworkspace.v2.CertValidityData`
        """
        self._validity = validity

    @property
    def crl_configuration(self):
        r"""Gets the crl_configuration of this CreateCertificateReq.

        :return: The crl_configuration of this CreateCertificateReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.CrlConfigurationData`
        """
        return self._crl_configuration

    @crl_configuration.setter
    def crl_configuration(self, crl_configuration):
        r"""Sets the crl_configuration of this CreateCertificateReq.

        :param crl_configuration: The crl_configuration of this CreateCertificateReq.
        :type crl_configuration: :class:`huaweicloudsdkworkspace.v2.CrlConfigurationData`
        """
        self._crl_configuration = crl_configuration

    def to_dict(self):
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
        if not isinstance(other, CreateCertificateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
