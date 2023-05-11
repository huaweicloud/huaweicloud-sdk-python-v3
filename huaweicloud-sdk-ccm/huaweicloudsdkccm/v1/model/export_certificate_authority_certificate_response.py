# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportCertificateAuthorityCertificateResponse(SdkResponse):

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
        """ExportCertificateAuthorityCertificateResponse

        The model defined in huaweicloud sdk

        :param certificate: 证书内容。  &gt;  - 通过API请求本接口，证书内容中换行符已使用\&quot;\\r\\n\&quot;代替；  &gt;  - 通过console端导出证书，将得到标准的PEM格式的证书文件。
        :type certificate: str
        :param certificate_chain: 证书链内容，证书链中排列顺序（从上至下）：中间证书&gt;...&gt;根证书。 &gt;  - 通过API请求本接口，证书链内容中换行符已使用\&quot;\\r\\n\&quot;代替； &gt;  - 通过console端导出证书链，将得到标准的PEM格式的证书链文件。
        :type certificate_chain: str
        """
        
        super(ExportCertificateAuthorityCertificateResponse, self).__init__()

        self._certificate = None
        self._certificate_chain = None
        self.discriminator = None

        if certificate is not None:
            self.certificate = certificate
        if certificate_chain is not None:
            self.certificate_chain = certificate_chain

    @property
    def certificate(self):
        """Gets the certificate of this ExportCertificateAuthorityCertificateResponse.

        证书内容。  >  - 通过API请求本接口，证书内容中换行符已使用\"\\r\\n\"代替；  >  - 通过console端导出证书，将得到标准的PEM格式的证书文件。

        :return: The certificate of this ExportCertificateAuthorityCertificateResponse.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this ExportCertificateAuthorityCertificateResponse.

        证书内容。  >  - 通过API请求本接口，证书内容中换行符已使用\"\\r\\n\"代替；  >  - 通过console端导出证书，将得到标准的PEM格式的证书文件。

        :param certificate: The certificate of this ExportCertificateAuthorityCertificateResponse.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def certificate_chain(self):
        """Gets the certificate_chain of this ExportCertificateAuthorityCertificateResponse.

        证书链内容，证书链中排列顺序（从上至下）：中间证书>...>根证书。 >  - 通过API请求本接口，证书链内容中换行符已使用\"\\r\\n\"代替； >  - 通过console端导出证书链，将得到标准的PEM格式的证书链文件。

        :return: The certificate_chain of this ExportCertificateAuthorityCertificateResponse.
        :rtype: str
        """
        return self._certificate_chain

    @certificate_chain.setter
    def certificate_chain(self, certificate_chain):
        """Sets the certificate_chain of this ExportCertificateAuthorityCertificateResponse.

        证书链内容，证书链中排列顺序（从上至下）：中间证书>...>根证书。 >  - 通过API请求本接口，证书链内容中换行符已使用\"\\r\\n\"代替； >  - 通过console端导出证书链，将得到标准的PEM格式的证书链文件。

        :param certificate_chain: The certificate_chain of this ExportCertificateAuthorityCertificateResponse.
        :type certificate_chain: str
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
        if not isinstance(other, ExportCertificateAuthorityCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
