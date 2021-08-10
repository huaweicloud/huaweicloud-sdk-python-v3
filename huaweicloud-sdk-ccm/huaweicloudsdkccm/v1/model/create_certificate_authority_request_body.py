# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCertificateAuthorityRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'crl_configuration': 'CrlConfiguration',
        'distinguished_name': 'DistinguishedName',
        'issuer_id': 'str',
        'key_algorithm': 'str',
        'path_length': 'int',
        'signature_algorithm': 'str',
        'type': 'str',
        'validity': 'Validity'
    }

    attribute_map = {
        'crl_configuration': 'crl_configuration',
        'distinguished_name': 'distinguished_name',
        'issuer_id': 'issuer_id',
        'key_algorithm': 'key_algorithm',
        'path_length': 'path_length',
        'signature_algorithm': 'signature_algorithm',
        'type': 'type',
        'validity': 'validity'
    }

    def __init__(self, crl_configuration=None, distinguished_name=None, issuer_id=None, key_algorithm=None, path_length=None, signature_algorithm=None, type=None, validity=None):
        """CreateCertificateAuthorityRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._crl_configuration = None
        self._distinguished_name = None
        self._issuer_id = None
        self._key_algorithm = None
        self._path_length = None
        self._signature_algorithm = None
        self._type = None
        self._validity = None
        self.discriminator = None

        if crl_configuration is not None:
            self.crl_configuration = crl_configuration
        if distinguished_name is not None:
            self.distinguished_name = distinguished_name
        if issuer_id is not None:
            self.issuer_id = issuer_id
        if key_algorithm is not None:
            self.key_algorithm = key_algorithm
        if path_length is not None:
            self.path_length = path_length
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if type is not None:
            self.type = type
        if validity is not None:
            self.validity = validity

    @property
    def crl_configuration(self):
        """Gets the crl_configuration of this CreateCertificateAuthorityRequestBody.


        :return: The crl_configuration of this CreateCertificateAuthorityRequestBody.
        :rtype: CrlConfiguration
        """
        return self._crl_configuration

    @crl_configuration.setter
    def crl_configuration(self, crl_configuration):
        """Sets the crl_configuration of this CreateCertificateAuthorityRequestBody.


        :param crl_configuration: The crl_configuration of this CreateCertificateAuthorityRequestBody.
        :type: CrlConfiguration
        """
        self._crl_configuration = crl_configuration

    @property
    def distinguished_name(self):
        """Gets the distinguished_name of this CreateCertificateAuthorityRequestBody.


        :return: The distinguished_name of this CreateCertificateAuthorityRequestBody.
        :rtype: DistinguishedName
        """
        return self._distinguished_name

    @distinguished_name.setter
    def distinguished_name(self, distinguished_name):
        """Sets the distinguished_name of this CreateCertificateAuthorityRequestBody.


        :param distinguished_name: The distinguished_name of this CreateCertificateAuthorityRequestBody.
        :type: DistinguishedName
        """
        self._distinguished_name = distinguished_name

    @property
    def issuer_id(self):
        """Gets the issuer_id of this CreateCertificateAuthorityRequestBody.

        签发CA ID

        :return: The issuer_id of this CreateCertificateAuthorityRequestBody.
        :rtype: str
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        """Sets the issuer_id of this CreateCertificateAuthorityRequestBody.

        签发CA ID

        :param issuer_id: The issuer_id of this CreateCertificateAuthorityRequestBody.
        :type: str
        """
        self._issuer_id = issuer_id

    @property
    def key_algorithm(self):
        """Gets the key_algorithm of this CreateCertificateAuthorityRequestBody.

        密钥算法

        :return: The key_algorithm of this CreateCertificateAuthorityRequestBody.
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        """Sets the key_algorithm of this CreateCertificateAuthorityRequestBody.

        密钥算法

        :param key_algorithm: The key_algorithm of this CreateCertificateAuthorityRequestBody.
        :type: str
        """
        self._key_algorithm = key_algorithm

    @property
    def path_length(self):
        """Gets the path_length of this CreateCertificateAuthorityRequestBody.

        路径长度

        :return: The path_length of this CreateCertificateAuthorityRequestBody.
        :rtype: int
        """
        return self._path_length

    @path_length.setter
    def path_length(self, path_length):
        """Sets the path_length of this CreateCertificateAuthorityRequestBody.

        路径长度

        :param path_length: The path_length of this CreateCertificateAuthorityRequestBody.
        :type: int
        """
        self._path_length = path_length

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this CreateCertificateAuthorityRequestBody.

        签名算法

        :return: The signature_algorithm of this CreateCertificateAuthorityRequestBody.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this CreateCertificateAuthorityRequestBody.

        签名算法

        :param signature_algorithm: The signature_algorithm of this CreateCertificateAuthorityRequestBody.
        :type: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def type(self):
        """Gets the type of this CreateCertificateAuthorityRequestBody.

        CA类型

        :return: The type of this CreateCertificateAuthorityRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateCertificateAuthorityRequestBody.

        CA类型

        :param type: The type of this CreateCertificateAuthorityRequestBody.
        :type: str
        """
        self._type = type

    @property
    def validity(self):
        """Gets the validity of this CreateCertificateAuthorityRequestBody.


        :return: The validity of this CreateCertificateAuthorityRequestBody.
        :rtype: Validity
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this CreateCertificateAuthorityRequestBody.


        :param validity: The validity of this CreateCertificateAuthorityRequestBody.
        :type: Validity
        """
        self._validity = validity

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
        if not isinstance(other, CreateCertificateAuthorityRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
