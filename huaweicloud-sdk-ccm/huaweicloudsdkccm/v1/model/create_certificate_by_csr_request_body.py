# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCertificateByCsrRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'csr': 'str',
        'issuer_id': 'str',
        'subject_alternative_names': 'list[SubjectAlternativeName]',
        'validity': 'Validity'
    }

    attribute_map = {
        'csr': 'csr',
        'issuer_id': 'issuer_id',
        'subject_alternative_names': 'subject_alternative_names',
        'validity': 'validity'
    }

    def __init__(self, csr=None, issuer_id=None, subject_alternative_names=None, validity=None):
        """CreateCertificateByCsrRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._csr = None
        self._issuer_id = None
        self._subject_alternative_names = None
        self._validity = None
        self.discriminator = None

        if csr is not None:
            self.csr = csr
        if issuer_id is not None:
            self.issuer_id = issuer_id
        if subject_alternative_names is not None:
            self.subject_alternative_names = subject_alternative_names
        if validity is not None:
            self.validity = validity

    @property
    def csr(self):
        """Gets the csr of this CreateCertificateByCsrRequestBody.

        证书签名请求

        :return: The csr of this CreateCertificateByCsrRequestBody.
        :rtype: str
        """
        return self._csr

    @csr.setter
    def csr(self, csr):
        """Sets the csr of this CreateCertificateByCsrRequestBody.

        证书签名请求

        :param csr: The csr of this CreateCertificateByCsrRequestBody.
        :type: str
        """
        self._csr = csr

    @property
    def issuer_id(self):
        """Gets the issuer_id of this CreateCertificateByCsrRequestBody.

        签发CA ID

        :return: The issuer_id of this CreateCertificateByCsrRequestBody.
        :rtype: str
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        """Sets the issuer_id of this CreateCertificateByCsrRequestBody.

        签发CA ID

        :param issuer_id: The issuer_id of this CreateCertificateByCsrRequestBody.
        :type: str
        """
        self._issuer_id = issuer_id

    @property
    def subject_alternative_names(self):
        """Gets the subject_alternative_names of this CreateCertificateByCsrRequestBody.

        主题备用名称

        :return: The subject_alternative_names of this CreateCertificateByCsrRequestBody.
        :rtype: list[SubjectAlternativeName]
        """
        return self._subject_alternative_names

    @subject_alternative_names.setter
    def subject_alternative_names(self, subject_alternative_names):
        """Sets the subject_alternative_names of this CreateCertificateByCsrRequestBody.

        主题备用名称

        :param subject_alternative_names: The subject_alternative_names of this CreateCertificateByCsrRequestBody.
        :type: list[SubjectAlternativeName]
        """
        self._subject_alternative_names = subject_alternative_names

    @property
    def validity(self):
        """Gets the validity of this CreateCertificateByCsrRequestBody.


        :return: The validity of this CreateCertificateByCsrRequestBody.
        :rtype: Validity
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this CreateCertificateByCsrRequestBody.


        :param validity: The validity of this CreateCertificateByCsrRequestBody.
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
        if not isinstance(other, CreateCertificateByCsrRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
