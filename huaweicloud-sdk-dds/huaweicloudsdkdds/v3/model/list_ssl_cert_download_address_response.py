# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSslCertDownloadAddressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certs': 'list[CertInfo]'
    }

    attribute_map = {
        'certs': 'certs'
    }

    def __init__(self, certs=None):
        """ListSslCertDownloadAddressResponse

        The model defined in huaweicloud sdk

        :param certs: 证书列表
        :type certs: list[:class:`huaweicloudsdkdds.v3.CertInfo`]
        """
        
        super(ListSslCertDownloadAddressResponse, self).__init__()

        self._certs = None
        self.discriminator = None

        if certs is not None:
            self.certs = certs

    @property
    def certs(self):
        """Gets the certs of this ListSslCertDownloadAddressResponse.

        证书列表

        :return: The certs of this ListSslCertDownloadAddressResponse.
        :rtype: list[:class:`huaweicloudsdkdds.v3.CertInfo`]
        """
        return self._certs

    @certs.setter
    def certs(self, certs):
        """Sets the certs of this ListSslCertDownloadAddressResponse.

        证书列表

        :param certs: The certs of this ListSslCertDownloadAddressResponse.
        :type certs: list[:class:`huaweicloudsdkdds.v3.CertInfo`]
        """
        self._certs = certs

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
        if not isinstance(other, ListSslCertDownloadAddressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
