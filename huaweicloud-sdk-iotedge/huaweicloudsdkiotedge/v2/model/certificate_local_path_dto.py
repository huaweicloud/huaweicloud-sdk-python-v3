# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertificateLocalPathDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cert_path': 'str',
        'key_path': 'str'
    }

    attribute_map = {
        'cert_path': 'cert_path',
        'key_path': 'key_path'
    }

    def __init__(self, cert_path=None, key_path=None):
        """CertificateLocalPathDTO

        The model defined in huaweicloud sdk

        :param cert_path: 节点数字证书的本地存储路径。
        :type cert_path: str
        :param key_path: 证书私钥的本地存储路径。
        :type key_path: str
        """
        
        

        self._cert_path = None
        self._key_path = None
        self.discriminator = None

        self.cert_path = cert_path
        self.key_path = key_path

    @property
    def cert_path(self):
        """Gets the cert_path of this CertificateLocalPathDTO.

        节点数字证书的本地存储路径。

        :return: The cert_path of this CertificateLocalPathDTO.
        :rtype: str
        """
        return self._cert_path

    @cert_path.setter
    def cert_path(self, cert_path):
        """Sets the cert_path of this CertificateLocalPathDTO.

        节点数字证书的本地存储路径。

        :param cert_path: The cert_path of this CertificateLocalPathDTO.
        :type cert_path: str
        """
        self._cert_path = cert_path

    @property
    def key_path(self):
        """Gets the key_path of this CertificateLocalPathDTO.

        证书私钥的本地存储路径。

        :return: The key_path of this CertificateLocalPathDTO.
        :rtype: str
        """
        return self._key_path

    @key_path.setter
    def key_path(self, key_path):
        """Sets the key_path of this CertificateLocalPathDTO.

        证书私钥的本地存储路径。

        :param key_path: The key_path of this CertificateLocalPathDTO.
        :type key_path: str
        """
        self._key_path = key_path

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
        if not isinstance(other, CertificateLocalPathDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
