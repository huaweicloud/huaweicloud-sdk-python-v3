# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertificateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'certificates': 'list[Certificates]'
    }

    attribute_map = {
        'total': 'total',
        'certificates': 'certificates'
    }

    def __init__(self, total=None, certificates=None):
        """ListCertificateResponse

        The model defined in huaweicloud sdk

        :param total: 私有证书总数。
        :type total: int
        :param certificates: 证书列表，详情请参见**Certificates**字段数据结构说明。
        :type certificates: list[:class:`huaweicloudsdkccm.v1.Certificates`]
        """
        
        super(ListCertificateResponse, self).__init__()

        self._total = None
        self._certificates = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if certificates is not None:
            self.certificates = certificates

    @property
    def total(self):
        """Gets the total of this ListCertificateResponse.

        私有证书总数。

        :return: The total of this ListCertificateResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListCertificateResponse.

        私有证书总数。

        :param total: The total of this ListCertificateResponse.
        :type total: int
        """
        self._total = total

    @property
    def certificates(self):
        """Gets the certificates of this ListCertificateResponse.

        证书列表，详情请参见**Certificates**字段数据结构说明。

        :return: The certificates of this ListCertificateResponse.
        :rtype: list[:class:`huaweicloudsdkccm.v1.Certificates`]
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates):
        """Sets the certificates of this ListCertificateResponse.

        证书列表，详情请参见**Certificates**字段数据结构说明。

        :param certificates: The certificates of this ListCertificateResponse.
        :type certificates: list[:class:`huaweicloudsdkccm.v1.Certificates`]
        """
        self._certificates = certificates

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
        if not isinstance(other, ListCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
