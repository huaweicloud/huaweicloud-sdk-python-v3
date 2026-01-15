# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportCertificatePemReq:

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
        'transaction_id': 'str',
        'crl_configuration': 'CrlConfigurationData',
        'pem_code': 'str'
    }

    attribute_map = {
        'distinguished_name': 'distinguished_name',
        'key_algorithm': 'key_algorithm',
        'transaction_id': 'transaction_id',
        'crl_configuration': 'crl_configuration',
        'pem_code': 'pem_code'
    }

    def __init__(self, distinguished_name=None, key_algorithm=None, transaction_id=None, crl_configuration=None, pem_code=None):
        r"""ImportCertificatePemReq

        The model defined in huaweicloud sdk

        :param distinguished_name: 
        :type distinguished_name: :class:`huaweicloudsdkworkspace.v2.DistinguishedName`
        :param key_algorithm: 密钥对生成算法 RSA-2048 RSA-3072。
        :type key_algorithm: str
        :param transaction_id: 事务id。
        :type transaction_id: str
        :param crl_configuration: 
        :type crl_configuration: :class:`huaweicloudsdkworkspace.v2.CrlConfigurationData`
        :param pem_code: 证书pem。
        :type pem_code: str
        """
        
        

        self._distinguished_name = None
        self._key_algorithm = None
        self._transaction_id = None
        self._crl_configuration = None
        self._pem_code = None
        self.discriminator = None

        self.distinguished_name = distinguished_name
        self.key_algorithm = key_algorithm
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if crl_configuration is not None:
            self.crl_configuration = crl_configuration
        if pem_code is not None:
            self.pem_code = pem_code

    @property
    def distinguished_name(self):
        r"""Gets the distinguished_name of this ImportCertificatePemReq.

        :return: The distinguished_name of this ImportCertificatePemReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.DistinguishedName`
        """
        return self._distinguished_name

    @distinguished_name.setter
    def distinguished_name(self, distinguished_name):
        r"""Sets the distinguished_name of this ImportCertificatePemReq.

        :param distinguished_name: The distinguished_name of this ImportCertificatePemReq.
        :type distinguished_name: :class:`huaweicloudsdkworkspace.v2.DistinguishedName`
        """
        self._distinguished_name = distinguished_name

    @property
    def key_algorithm(self):
        r"""Gets the key_algorithm of this ImportCertificatePemReq.

        密钥对生成算法 RSA-2048 RSA-3072。

        :return: The key_algorithm of this ImportCertificatePemReq.
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        r"""Sets the key_algorithm of this ImportCertificatePemReq.

        密钥对生成算法 RSA-2048 RSA-3072。

        :param key_algorithm: The key_algorithm of this ImportCertificatePemReq.
        :type key_algorithm: str
        """
        self._key_algorithm = key_algorithm

    @property
    def transaction_id(self):
        r"""Gets the transaction_id of this ImportCertificatePemReq.

        事务id。

        :return: The transaction_id of this ImportCertificatePemReq.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        r"""Sets the transaction_id of this ImportCertificatePemReq.

        事务id。

        :param transaction_id: The transaction_id of this ImportCertificatePemReq.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def crl_configuration(self):
        r"""Gets the crl_configuration of this ImportCertificatePemReq.

        :return: The crl_configuration of this ImportCertificatePemReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.CrlConfigurationData`
        """
        return self._crl_configuration

    @crl_configuration.setter
    def crl_configuration(self, crl_configuration):
        r"""Sets the crl_configuration of this ImportCertificatePemReq.

        :param crl_configuration: The crl_configuration of this ImportCertificatePemReq.
        :type crl_configuration: :class:`huaweicloudsdkworkspace.v2.CrlConfigurationData`
        """
        self._crl_configuration = crl_configuration

    @property
    def pem_code(self):
        r"""Gets the pem_code of this ImportCertificatePemReq.

        证书pem。

        :return: The pem_code of this ImportCertificatePemReq.
        :rtype: str
        """
        return self._pem_code

    @pem_code.setter
    def pem_code(self, pem_code):
        r"""Sets the pem_code of this ImportCertificatePemReq.

        证书pem。

        :param pem_code: The pem_code of this ImportCertificatePemReq.
        :type pem_code: str
        """
        self._pem_code = pem_code

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
        if not isinstance(other, ImportCertificatePemReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
