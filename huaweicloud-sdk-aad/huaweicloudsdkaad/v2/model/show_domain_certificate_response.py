# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainCertificateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'domain_name': 'str',
        'cert_info': 'CertInfo'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'cert_info': 'cert_info'
    }

    def __init__(self, domain_id=None, domain_name=None, cert_info=None):
        r"""ShowDomainCertificateResponse

        The model defined in huaweicloud sdk

        :param domain_id: 域名id
        :type domain_id: str
        :param domain_name: 域名
        :type domain_name: str
        :param cert_info: 
        :type cert_info: :class:`huaweicloudsdkaad.v2.CertInfo`
        """
        
        super(ShowDomainCertificateResponse, self).__init__()

        self._domain_id = None
        self._domain_name = None
        self._cert_info = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if cert_info is not None:
            self.cert_info = cert_info

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowDomainCertificateResponse.

        域名id

        :return: The domain_id of this ShowDomainCertificateResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowDomainCertificateResponse.

        域名id

        :param domain_id: The domain_id of this ShowDomainCertificateResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowDomainCertificateResponse.

        域名

        :return: The domain_name of this ShowDomainCertificateResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowDomainCertificateResponse.

        域名

        :param domain_name: The domain_name of this ShowDomainCertificateResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def cert_info(self):
        r"""Gets the cert_info of this ShowDomainCertificateResponse.

        :return: The cert_info of this ShowDomainCertificateResponse.
        :rtype: :class:`huaweicloudsdkaad.v2.CertInfo`
        """
        return self._cert_info

    @cert_info.setter
    def cert_info(self, cert_info):
        r"""Sets the cert_info of this ShowDomainCertificateResponse.

        :param cert_info: The cert_info of this ShowDomainCertificateResponse.
        :type cert_info: :class:`huaweicloudsdkaad.v2.CertInfo`
        """
        self._cert_info = cert_info

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
        if not isinstance(other, ShowDomainCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
