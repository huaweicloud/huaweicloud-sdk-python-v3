# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportClientCaCertificateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_ca_certificate': 'ImportClientCaCertificateRequestBodyClientCaCertificate'
    }

    attribute_map = {
        'client_ca_certificate': 'client_ca_certificate'
    }

    def __init__(self, client_ca_certificate=None):
        r"""ImportClientCaCertificateRequestBody

        The model defined in huaweicloud sdk

        :param client_ca_certificate: 
        :type client_ca_certificate: :class:`huaweicloudsdkvpn.v5.ImportClientCaCertificateRequestBodyClientCaCertificate`
        """
        
        

        self._client_ca_certificate = None
        self.discriminator = None

        self.client_ca_certificate = client_ca_certificate

    @property
    def client_ca_certificate(self):
        r"""Gets the client_ca_certificate of this ImportClientCaCertificateRequestBody.

        :return: The client_ca_certificate of this ImportClientCaCertificateRequestBody.
        :rtype: :class:`huaweicloudsdkvpn.v5.ImportClientCaCertificateRequestBodyClientCaCertificate`
        """
        return self._client_ca_certificate

    @client_ca_certificate.setter
    def client_ca_certificate(self, client_ca_certificate):
        r"""Sets the client_ca_certificate of this ImportClientCaCertificateRequestBody.

        :param client_ca_certificate: The client_ca_certificate of this ImportClientCaCertificateRequestBody.
        :type client_ca_certificate: :class:`huaweicloudsdkvpn.v5.ImportClientCaCertificateRequestBodyClientCaCertificate`
        """
        self._client_ca_certificate = client_ca_certificate

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
        if not isinstance(other, ImportClientCaCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
