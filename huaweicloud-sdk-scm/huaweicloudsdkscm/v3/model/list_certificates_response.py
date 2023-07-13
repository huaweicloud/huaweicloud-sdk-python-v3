# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertificatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificates': 'list[CertificateDetail]',
        'total_count': 'int'
    }

    attribute_map = {
        'certificates': 'certificates',
        'total_count': 'total_count'
    }

    def __init__(self, certificates=None, total_count=None):
        """ListCertificatesResponse

        The model defined in huaweicloud sdk

        :param certificates: 证书列表，详情请参见CertificateDetail字段数据结构说明。
        :type certificates: list[:class:`huaweicloudsdkscm.v3.CertificateDetail`]
        :param total_count: 证书数量。
        :type total_count: int
        """
        
        super(ListCertificatesResponse, self).__init__()

        self._certificates = None
        self._total_count = None
        self.discriminator = None

        if certificates is not None:
            self.certificates = certificates
        if total_count is not None:
            self.total_count = total_count

    @property
    def certificates(self):
        """Gets the certificates of this ListCertificatesResponse.

        证书列表，详情请参见CertificateDetail字段数据结构说明。

        :return: The certificates of this ListCertificatesResponse.
        :rtype: list[:class:`huaweicloudsdkscm.v3.CertificateDetail`]
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates):
        """Sets the certificates of this ListCertificatesResponse.

        证书列表，详情请参见CertificateDetail字段数据结构说明。

        :param certificates: The certificates of this ListCertificatesResponse.
        :type certificates: list[:class:`huaweicloudsdkscm.v3.CertificateDetail`]
        """
        self._certificates = certificates

    @property
    def total_count(self):
        """Gets the total_count of this ListCertificatesResponse.

        证书数量。

        :return: The total_count of this ListCertificatesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListCertificatesResponse.

        证书数量。

        :param total_count: The total_count of this ListCertificatesResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListCertificatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
