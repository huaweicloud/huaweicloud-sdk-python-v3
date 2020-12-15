# coding: utf-8

import pprint
import re

import six





class ClusterCert:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'certificate_authority_data': 'str',
        'insecure_skip_tls_verify': 'bool',
        'server': 'str'
    }

    attribute_map = {
        'certificate_authority_data': 'certificate-authority-data',
        'insecure_skip_tls_verify': 'insecure-skip-tls-verify',
        'server': 'server'
    }

    def __init__(self, certificate_authority_data=None, insecure_skip_tls_verify=None, server=None):
        """ClusterCert - a model defined in huaweicloud sdk"""
        
        

        self._certificate_authority_data = None
        self._insecure_skip_tls_verify = None
        self._server = None
        self.discriminator = None

        if certificate_authority_data is not None:
            self.certificate_authority_data = certificate_authority_data
        if insecure_skip_tls_verify is not None:
            self.insecure_skip_tls_verify = insecure_skip_tls_verify
        if server is not None:
            self.server = server

    @property
    def certificate_authority_data(self):
        """Gets the certificate_authority_data of this ClusterCert.

        证书授权数据。

        :return: The certificate_authority_data of this ClusterCert.
        :rtype: str
        """
        return self._certificate_authority_data

    @certificate_authority_data.setter
    def certificate_authority_data(self, certificate_authority_data):
        """Sets the certificate_authority_data of this ClusterCert.

        证书授权数据。

        :param certificate_authority_data: The certificate_authority_data of this ClusterCert.
        :type: str
        """
        self._certificate_authority_data = certificate_authority_data

    @property
    def insecure_skip_tls_verify(self):
        """Gets the insecure_skip_tls_verify of this ClusterCert.

        不校验服务端证书，在 cluster 类型为 externalCluster 时，该值为 true。

        :return: The insecure_skip_tls_verify of this ClusterCert.
        :rtype: bool
        """
        return self._insecure_skip_tls_verify

    @insecure_skip_tls_verify.setter
    def insecure_skip_tls_verify(self, insecure_skip_tls_verify):
        """Sets the insecure_skip_tls_verify of this ClusterCert.

        不校验服务端证书，在 cluster 类型为 externalCluster 时，该值为 true。

        :param insecure_skip_tls_verify: The insecure_skip_tls_verify of this ClusterCert.
        :type: bool
        """
        self._insecure_skip_tls_verify = insecure_skip_tls_verify

    @property
    def server(self):
        """Gets the server of this ClusterCert.

        服务器地址。

        :return: The server of this ClusterCert.
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this ClusterCert.

        服务器地址。

        :param server: The server of this ClusterCert.
        :type: str
        """
        self._server = server

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClusterCert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
