# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetBucketCustomDomainBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "CustomDomainConfiguration"

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'certificate_id': 'str',
        'certificate': 'str',
        'certificate_chain': 'str',
        'private_key': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'certificate_id': 'CertificateId',
        'certificate': 'Certificate',
        'certificate_chain': 'CertificateChain',
        'private_key': 'PrivateKey'
    }

    def __init__(self, name=None, certificate_id=None, certificate=None, certificate_chain=None, private_key=None):
        r"""SetBucketCustomDomainBody

        The model defined in huaweicloud sdk

        :param name: Certificate name, a string of 3 to 63 characters. 
        :type name: str
        :param certificate_id: Certificate id. 
        :type certificate_id: str
        :param certificate: Indicates the certificate content, including the intermediate certificate and root certificate. If the certificate_chain field is set to a certificate chain, this field uses only the certificate itself. The carriage return line feed must be replaced with the escape character \\n or \\r\\n. 
        :type certificate: str
        :param certificate_chain: Indicates the certificate content, including the intermediate certificate and root certificate. If the certificate_chain field is set to a certificate chain, this field uses only the certificate itself. The carriage return line feed must be replaced with the escape character \\n or \\r\\n. 
        :type certificate_chain: str
        :param private_key: Private key of the certificate. The private key with password protection cannot be uploaded. The carriage return line feed must be replaced with the escape character \\n or \\r\\n. 
        :type private_key: str
        """
        
        

        self._name = None
        self._certificate_id = None
        self._certificate = None
        self._certificate_chain = None
        self._private_key = None
        self.discriminator = None

        self.name = name
        if certificate_id is not None:
            self.certificate_id = certificate_id
        self.certificate = certificate
        if certificate_chain is not None:
            self.certificate_chain = certificate_chain
        self.private_key = private_key

    @property
    def name(self):
        r"""Gets the name of this SetBucketCustomDomainBody.

        Certificate name, a string of 3 to 63 characters. 

        :return: The name of this SetBucketCustomDomainBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SetBucketCustomDomainBody.

        Certificate name, a string of 3 to 63 characters. 

        :param name: The name of this SetBucketCustomDomainBody.
        :type name: str
        """
        self._name = name

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this SetBucketCustomDomainBody.

        Certificate id. 

        :return: The certificate_id of this SetBucketCustomDomainBody.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this SetBucketCustomDomainBody.

        Certificate id. 

        :param certificate_id: The certificate_id of this SetBucketCustomDomainBody.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def certificate(self):
        r"""Gets the certificate of this SetBucketCustomDomainBody.

        Indicates the certificate content, including the intermediate certificate and root certificate. If the certificate_chain field is set to a certificate chain, this field uses only the certificate itself. The carriage return line feed must be replaced with the escape character \\n or \\r\\n. 

        :return: The certificate of this SetBucketCustomDomainBody.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this SetBucketCustomDomainBody.

        Indicates the certificate content, including the intermediate certificate and root certificate. If the certificate_chain field is set to a certificate chain, this field uses only the certificate itself. The carriage return line feed must be replaced with the escape character \\n or \\r\\n. 

        :param certificate: The certificate of this SetBucketCustomDomainBody.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def certificate_chain(self):
        r"""Gets the certificate_chain of this SetBucketCustomDomainBody.

        Indicates the certificate content, including the intermediate certificate and root certificate. If the certificate_chain field is set to a certificate chain, this field uses only the certificate itself. The carriage return line feed must be replaced with the escape character \\n or \\r\\n. 

        :return: The certificate_chain of this SetBucketCustomDomainBody.
        :rtype: str
        """
        return self._certificate_chain

    @certificate_chain.setter
    def certificate_chain(self, certificate_chain):
        r"""Sets the certificate_chain of this SetBucketCustomDomainBody.

        Indicates the certificate content, including the intermediate certificate and root certificate. If the certificate_chain field is set to a certificate chain, this field uses only the certificate itself. The carriage return line feed must be replaced with the escape character \\n or \\r\\n. 

        :param certificate_chain: The certificate_chain of this SetBucketCustomDomainBody.
        :type certificate_chain: str
        """
        self._certificate_chain = certificate_chain

    @property
    def private_key(self):
        r"""Gets the private_key of this SetBucketCustomDomainBody.

        Private key of the certificate. The private key with password protection cannot be uploaded. The carriage return line feed must be replaced with the escape character \\n or \\r\\n. 

        :return: The private_key of this SetBucketCustomDomainBody.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this SetBucketCustomDomainBody.

        Private key of the certificate. The private key with password protection cannot be uploaded. The carriage return line feed must be replaced with the escape character \\n or \\r\\n. 

        :param private_key: The private_key of this SetBucketCustomDomainBody.
        :type private_key: str
        """
        self._private_key = private_key

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
        if not isinstance(other, SetBucketCustomDomainBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
