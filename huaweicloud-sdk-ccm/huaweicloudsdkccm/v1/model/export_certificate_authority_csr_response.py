# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportCertificateAuthorityCsrResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'csr': 'str'
    }

    attribute_map = {
        'csr': 'csr'
    }

    def __init__(self, csr=None):
        """ExportCertificateAuthorityCsrResponse

        The model defined in huaweicloud sdk

        :param csr: 证书签名请求内容，有以下两种情况：   - 通过API请求本接口，证书签名请求中换行符已使用\&quot;\\r\\n\&quot;代替；   - 通过console端导出证书签名请求，将得到标准的PEM格式的证书签名请求文件。
        :type csr: str
        """
        
        super(ExportCertificateAuthorityCsrResponse, self).__init__()

        self._csr = None
        self.discriminator = None

        if csr is not None:
            self.csr = csr

    @property
    def csr(self):
        """Gets the csr of this ExportCertificateAuthorityCsrResponse.

        证书签名请求内容，有以下两种情况：   - 通过API请求本接口，证书签名请求中换行符已使用\"\\r\\n\"代替；   - 通过console端导出证书签名请求，将得到标准的PEM格式的证书签名请求文件。

        :return: The csr of this ExportCertificateAuthorityCsrResponse.
        :rtype: str
        """
        return self._csr

    @csr.setter
    def csr(self, csr):
        """Sets the csr of this ExportCertificateAuthorityCsrResponse.

        证书签名请求内容，有以下两种情况：   - 通过API请求本接口，证书签名请求中换行符已使用\"\\r\\n\"代替；   - 通过console端导出证书签名请求，将得到标准的PEM格式的证书签名请求文件。

        :param csr: The csr of this ExportCertificateAuthorityCsrResponse.
        :type csr: str
        """
        self._csr = csr

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
        if not isinstance(other, ExportCertificateAuthorityCsrResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
