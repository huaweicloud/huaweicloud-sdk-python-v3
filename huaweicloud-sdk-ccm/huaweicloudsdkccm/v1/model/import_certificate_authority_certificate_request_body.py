# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportCertificateAuthorityCertificateRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'certificate': 'str',
        'certificate_chain': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'certificate_chain': 'certificate_chain'
    }

    def __init__(self, certificate=None, certificate_chain=None):
        """ImportCertificateAuthorityCertificateRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._certificate = None
        self._certificate_chain = None
        self.discriminator = None

        if certificate is not None:
            self.certificate = certificate
        if certificate_chain is not None:
            self.certificate_chain = certificate_chain

    @property
    def certificate(self):
        """Gets the certificate of this ImportCertificateAuthorityCertificateRequestBody.

        证书内容

        :return: The certificate of this ImportCertificateAuthorityCertificateRequestBody.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this ImportCertificateAuthorityCertificateRequestBody.

        证书内容

        :param certificate: The certificate of this ImportCertificateAuthorityCertificateRequestBody.
        :type: str
        """
        self._certificate = certificate

    @property
    def certificate_chain(self):
        """Gets the certificate_chain of this ImportCertificateAuthorityCertificateRequestBody.

        证书链内容

        :return: The certificate_chain of this ImportCertificateAuthorityCertificateRequestBody.
        :rtype: str
        """
        return self._certificate_chain

    @certificate_chain.setter
    def certificate_chain(self, certificate_chain):
        """Sets the certificate_chain of this ImportCertificateAuthorityCertificateRequestBody.

        证书链内容

        :param certificate_chain: The certificate_chain of this ImportCertificateAuthorityCertificateRequestBody.
        :type: str
        """
        self._certificate_chain = certificate_chain

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImportCertificateAuthorityCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other