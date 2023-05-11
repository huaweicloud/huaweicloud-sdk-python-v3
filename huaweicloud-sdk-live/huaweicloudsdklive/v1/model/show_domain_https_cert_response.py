# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainHttpsCertResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificate_format': 'str',
        'certificate': 'str',
        'certificate_key': 'str',
        'force_redirect': 'bool'
    }

    attribute_map = {
        'certificate_format': 'certificate_format',
        'certificate': 'certificate',
        'certificate_key': 'certificate_key',
        'force_redirect': 'force_redirect'
    }

    def __init__(self, certificate_format=None, certificate=None, certificate_key=None, force_redirect=None):
        """ShowDomainHttpsCertResponse

        The model defined in huaweicloud sdk

        :param certificate_format: 证书格式，默认为PEM，当前只支持PEM格式
        :type certificate_format: str
        :param certificate: 证书内容
        :type certificate: str
        :param certificate_key: 私钥内容
        :type certificate_key: str
        :param force_redirect: 是否开启重定向，默认false
        :type force_redirect: bool
        """
        
        super(ShowDomainHttpsCertResponse, self).__init__()

        self._certificate_format = None
        self._certificate = None
        self._certificate_key = None
        self._force_redirect = None
        self.discriminator = None

        if certificate_format is not None:
            self.certificate_format = certificate_format
        if certificate is not None:
            self.certificate = certificate
        if certificate_key is not None:
            self.certificate_key = certificate_key
        if force_redirect is not None:
            self.force_redirect = force_redirect

    @property
    def certificate_format(self):
        """Gets the certificate_format of this ShowDomainHttpsCertResponse.

        证书格式，默认为PEM，当前只支持PEM格式

        :return: The certificate_format of this ShowDomainHttpsCertResponse.
        :rtype: str
        """
        return self._certificate_format

    @certificate_format.setter
    def certificate_format(self, certificate_format):
        """Sets the certificate_format of this ShowDomainHttpsCertResponse.

        证书格式，默认为PEM，当前只支持PEM格式

        :param certificate_format: The certificate_format of this ShowDomainHttpsCertResponse.
        :type certificate_format: str
        """
        self._certificate_format = certificate_format

    @property
    def certificate(self):
        """Gets the certificate of this ShowDomainHttpsCertResponse.

        证书内容

        :return: The certificate of this ShowDomainHttpsCertResponse.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this ShowDomainHttpsCertResponse.

        证书内容

        :param certificate: The certificate of this ShowDomainHttpsCertResponse.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def certificate_key(self):
        """Gets the certificate_key of this ShowDomainHttpsCertResponse.

        私钥内容

        :return: The certificate_key of this ShowDomainHttpsCertResponse.
        :rtype: str
        """
        return self._certificate_key

    @certificate_key.setter
    def certificate_key(self, certificate_key):
        """Sets the certificate_key of this ShowDomainHttpsCertResponse.

        私钥内容

        :param certificate_key: The certificate_key of this ShowDomainHttpsCertResponse.
        :type certificate_key: str
        """
        self._certificate_key = certificate_key

    @property
    def force_redirect(self):
        """Gets the force_redirect of this ShowDomainHttpsCertResponse.

        是否开启重定向，默认false

        :return: The force_redirect of this ShowDomainHttpsCertResponse.
        :rtype: bool
        """
        return self._force_redirect

    @force_redirect.setter
    def force_redirect(self, force_redirect):
        """Sets the force_redirect of this ShowDomainHttpsCertResponse.

        是否开启重定向，默认false

        :param force_redirect: The force_redirect of this ShowDomainHttpsCertResponse.
        :type force_redirect: bool
        """
        self._force_redirect = force_redirect

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
        if not isinstance(other, ShowDomainHttpsCertResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
