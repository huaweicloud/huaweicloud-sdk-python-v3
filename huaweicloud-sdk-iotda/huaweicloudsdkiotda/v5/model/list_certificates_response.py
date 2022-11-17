# coding: utf-8

import re
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
        'certificates': 'list[CertificatesRspDTO]',
        'page': 'Page'
    }

    attribute_map = {
        'certificates': 'certificates',
        'page': 'page'
    }

    def __init__(self, certificates=None, page=None):
        """ListCertificatesResponse

        The model defined in huaweicloud sdk

        :param certificates: 证书列表。
        :type certificates: list[:class:`huaweicloudsdkiotda.v5.CertificatesRspDTO`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        
        super(ListCertificatesResponse, self).__init__()

        self._certificates = None
        self._page = None
        self.discriminator = None

        if certificates is not None:
            self.certificates = certificates
        if page is not None:
            self.page = page

    @property
    def certificates(self):
        """Gets the certificates of this ListCertificatesResponse.

        证书列表。

        :return: The certificates of this ListCertificatesResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.CertificatesRspDTO`]
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates):
        """Sets the certificates of this ListCertificatesResponse.

        证书列表。

        :param certificates: The certificates of this ListCertificatesResponse.
        :type certificates: list[:class:`huaweicloudsdkiotda.v5.CertificatesRspDTO`]
        """
        self._certificates = certificates

    @property
    def page(self):
        """Gets the page of this ListCertificatesResponse.

        :return: The page of this ListCertificatesResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.Page`
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListCertificatesResponse.

        :param page: The page of this ListCertificatesResponse.
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        self._page = page

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
