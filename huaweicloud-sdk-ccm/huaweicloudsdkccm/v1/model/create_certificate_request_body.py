# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCertificateRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'customized_extension': 'CustomizedExtension',
        'distinguished_name': 'DistinguishedName',
        'issuer_id': 'str',
        'key_algorithm': 'str',
        'key_usages': 'list[str]',
        'signature_algorithm': 'str',
        'subject_alternative_names': 'list[SubjectAlternativeName]',
        'validity': 'Validity'
    }

    attribute_map = {
        'customized_extension': 'customized_extension',
        'distinguished_name': 'distinguished_name',
        'issuer_id': 'issuer_id',
        'key_algorithm': 'key_algorithm',
        'key_usages': 'key_usages',
        'signature_algorithm': 'signature_algorithm',
        'subject_alternative_names': 'subject_alternative_names',
        'validity': 'validity'
    }

    def __init__(self, customized_extension=None, distinguished_name=None, issuer_id=None, key_algorithm=None, key_usages=None, signature_algorithm=None, subject_alternative_names=None, validity=None):
        """CreateCertificateRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._customized_extension = None
        self._distinguished_name = None
        self._issuer_id = None
        self._key_algorithm = None
        self._key_usages = None
        self._signature_algorithm = None
        self._subject_alternative_names = None
        self._validity = None
        self.discriminator = None

        if customized_extension is not None:
            self.customized_extension = customized_extension
        if distinguished_name is not None:
            self.distinguished_name = distinguished_name
        if issuer_id is not None:
            self.issuer_id = issuer_id
        if key_algorithm is not None:
            self.key_algorithm = key_algorithm
        if key_usages is not None:
            self.key_usages = key_usages
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if subject_alternative_names is not None:
            self.subject_alternative_names = subject_alternative_names
        if validity is not None:
            self.validity = validity

    @property
    def customized_extension(self):
        """Gets the customized_extension of this CreateCertificateRequestBody.


        :return: The customized_extension of this CreateCertificateRequestBody.
        :rtype: CustomizedExtension
        """
        return self._customized_extension

    @customized_extension.setter
    def customized_extension(self, customized_extension):
        """Sets the customized_extension of this CreateCertificateRequestBody.


        :param customized_extension: The customized_extension of this CreateCertificateRequestBody.
        :type: CustomizedExtension
        """
        self._customized_extension = customized_extension

    @property
    def distinguished_name(self):
        """Gets the distinguished_name of this CreateCertificateRequestBody.


        :return: The distinguished_name of this CreateCertificateRequestBody.
        :rtype: DistinguishedName
        """
        return self._distinguished_name

    @distinguished_name.setter
    def distinguished_name(self, distinguished_name):
        """Sets the distinguished_name of this CreateCertificateRequestBody.


        :param distinguished_name: The distinguished_name of this CreateCertificateRequestBody.
        :type: DistinguishedName
        """
        self._distinguished_name = distinguished_name

    @property
    def issuer_id(self):
        """Gets the issuer_id of this CreateCertificateRequestBody.

        签发CA ID

        :return: The issuer_id of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        """Sets the issuer_id of this CreateCertificateRequestBody.

        签发CA ID

        :param issuer_id: The issuer_id of this CreateCertificateRequestBody.
        :type: str
        """
        self._issuer_id = issuer_id

    @property
    def key_algorithm(self):
        """Gets the key_algorithm of this CreateCertificateRequestBody.

        密钥算法

        :return: The key_algorithm of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        """Sets the key_algorithm of this CreateCertificateRequestBody.

        密钥算法

        :param key_algorithm: The key_algorithm of this CreateCertificateRequestBody.
        :type: str
        """
        self._key_algorithm = key_algorithm

    @property
    def key_usages(self):
        """Gets the key_usages of this CreateCertificateRequestBody.

        密钥用法

        :return: The key_usages of this CreateCertificateRequestBody.
        :rtype: list[str]
        """
        return self._key_usages

    @key_usages.setter
    def key_usages(self, key_usages):
        """Sets the key_usages of this CreateCertificateRequestBody.

        密钥用法

        :param key_usages: The key_usages of this CreateCertificateRequestBody.
        :type: list[str]
        """
        self._key_usages = key_usages

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this CreateCertificateRequestBody.

        签名算法

        :return: The signature_algorithm of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this CreateCertificateRequestBody.

        签名算法

        :param signature_algorithm: The signature_algorithm of this CreateCertificateRequestBody.
        :type: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def subject_alternative_names(self):
        """Gets the subject_alternative_names of this CreateCertificateRequestBody.

        主题备用名称

        :return: The subject_alternative_names of this CreateCertificateRequestBody.
        :rtype: list[SubjectAlternativeName]
        """
        return self._subject_alternative_names

    @subject_alternative_names.setter
    def subject_alternative_names(self, subject_alternative_names):
        """Sets the subject_alternative_names of this CreateCertificateRequestBody.

        主题备用名称

        :param subject_alternative_names: The subject_alternative_names of this CreateCertificateRequestBody.
        :type: list[SubjectAlternativeName]
        """
        self._subject_alternative_names = subject_alternative_names

    @property
    def validity(self):
        """Gets the validity of this CreateCertificateRequestBody.


        :return: The validity of this CreateCertificateRequestBody.
        :rtype: Validity
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this CreateCertificateRequestBody.


        :param validity: The validity of this CreateCertificateRequestBody.
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
        if not isinstance(other, CreateCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
