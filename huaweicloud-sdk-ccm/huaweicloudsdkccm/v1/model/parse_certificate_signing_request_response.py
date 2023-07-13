# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParseCertificateSigningRequestResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_algorithm': 'str',
        'key_algorithm_length': 'str',
        'signature_algorithm': 'str',
        'public_key': 'str',
        'distinguished_name': 'DistinguishedName'
    }

    attribute_map = {
        'key_algorithm': 'key_algorithm',
        'key_algorithm_length': 'key_algorithm_length',
        'signature_algorithm': 'signature_algorithm',
        'public_key': 'public_key',
        'distinguished_name': 'distinguished_name'
    }

    def __init__(self, key_algorithm=None, key_algorithm_length=None, signature_algorithm=None, public_key=None, distinguished_name=None):
        """ParseCertificateSigningRequestResponse

        The model defined in huaweicloud sdk

        :param key_algorithm: 密钥算法。
        :type key_algorithm: str
        :param key_algorithm_length: 密钥算法长度，单位为bit。
        :type key_algorithm_length: str
        :param signature_algorithm: 签名算法，带具体的签名与哈希算法，如\&quot;SHA256withRSA\&quot;。
        :type signature_algorithm: str
        :param public_key: 公钥内容。 &gt; 其中，换行符已被“\\r\\n”替代；
        :type public_key: str
        :param distinguished_name: 
        :type distinguished_name: :class:`huaweicloudsdkccm.v1.DistinguishedName`
        """
        
        super(ParseCertificateSigningRequestResponse, self).__init__()

        self._key_algorithm = None
        self._key_algorithm_length = None
        self._signature_algorithm = None
        self._public_key = None
        self._distinguished_name = None
        self.discriminator = None

        if key_algorithm is not None:
            self.key_algorithm = key_algorithm
        if key_algorithm_length is not None:
            self.key_algorithm_length = key_algorithm_length
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if public_key is not None:
            self.public_key = public_key
        if distinguished_name is not None:
            self.distinguished_name = distinguished_name

    @property
    def key_algorithm(self):
        """Gets the key_algorithm of this ParseCertificateSigningRequestResponse.

        密钥算法。

        :return: The key_algorithm of this ParseCertificateSigningRequestResponse.
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        """Sets the key_algorithm of this ParseCertificateSigningRequestResponse.

        密钥算法。

        :param key_algorithm: The key_algorithm of this ParseCertificateSigningRequestResponse.
        :type key_algorithm: str
        """
        self._key_algorithm = key_algorithm

    @property
    def key_algorithm_length(self):
        """Gets the key_algorithm_length of this ParseCertificateSigningRequestResponse.

        密钥算法长度，单位为bit。

        :return: The key_algorithm_length of this ParseCertificateSigningRequestResponse.
        :rtype: str
        """
        return self._key_algorithm_length

    @key_algorithm_length.setter
    def key_algorithm_length(self, key_algorithm_length):
        """Sets the key_algorithm_length of this ParseCertificateSigningRequestResponse.

        密钥算法长度，单位为bit。

        :param key_algorithm_length: The key_algorithm_length of this ParseCertificateSigningRequestResponse.
        :type key_algorithm_length: str
        """
        self._key_algorithm_length = key_algorithm_length

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this ParseCertificateSigningRequestResponse.

        签名算法，带具体的签名与哈希算法，如\"SHA256withRSA\"。

        :return: The signature_algorithm of this ParseCertificateSigningRequestResponse.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this ParseCertificateSigningRequestResponse.

        签名算法，带具体的签名与哈希算法，如\"SHA256withRSA\"。

        :param signature_algorithm: The signature_algorithm of this ParseCertificateSigningRequestResponse.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def public_key(self):
        """Gets the public_key of this ParseCertificateSigningRequestResponse.

        公钥内容。 > 其中，换行符已被“\\r\\n”替代；

        :return: The public_key of this ParseCertificateSigningRequestResponse.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this ParseCertificateSigningRequestResponse.

        公钥内容。 > 其中，换行符已被“\\r\\n”替代；

        :param public_key: The public_key of this ParseCertificateSigningRequestResponse.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def distinguished_name(self):
        """Gets the distinguished_name of this ParseCertificateSigningRequestResponse.

        :return: The distinguished_name of this ParseCertificateSigningRequestResponse.
        :rtype: :class:`huaweicloudsdkccm.v1.DistinguishedName`
        """
        return self._distinguished_name

    @distinguished_name.setter
    def distinguished_name(self, distinguished_name):
        """Sets the distinguished_name of this ParseCertificateSigningRequestResponse.

        :param distinguished_name: The distinguished_name of this ParseCertificateSigningRequestResponse.
        :type distinguished_name: :class:`huaweicloudsdkccm.v1.DistinguishedName`
        """
        self._distinguished_name = distinguished_name

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
        if not isinstance(other, ParseCertificateSigningRequestResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
