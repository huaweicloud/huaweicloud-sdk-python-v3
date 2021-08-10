# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertificateAuthorityResponse(SdkResponse):


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
        'certificate_authorities': 'list[ShowCertificateAuthorityResponseBody]'
    }

    attribute_map = {
        'total': 'total',
        'certificate_authorities': 'certificate_authorities'
    }

    def __init__(self, total=None, certificate_authorities=None):
        """ListCertificateAuthorityResponse - a model defined in huaweicloud sdk"""
        
        super(ListCertificateAuthorityResponse, self).__init__()

        self._total = None
        self._certificate_authorities = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if certificate_authorities is not None:
            self.certificate_authorities = certificate_authorities

    @property
    def total(self):
        """Gets the total of this ListCertificateAuthorityResponse.

        CA总数

        :return: The total of this ListCertificateAuthorityResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListCertificateAuthorityResponse.

        CA总数

        :param total: The total of this ListCertificateAuthorityResponse.
        :type: int
        """
        self._total = total

    @property
    def certificate_authorities(self):
        """Gets the certificate_authorities of this ListCertificateAuthorityResponse.

        CA列表

        :return: The certificate_authorities of this ListCertificateAuthorityResponse.
        :rtype: list[ShowCertificateAuthorityResponseBody]
        """
        return self._certificate_authorities

    @certificate_authorities.setter
    def certificate_authorities(self, certificate_authorities):
        """Sets the certificate_authorities of this ListCertificateAuthorityResponse.

        CA列表

        :param certificate_authorities: The certificate_authorities of this ListCertificateAuthorityResponse.
        :type: list[ShowCertificateAuthorityResponseBody]
        """
        self._certificate_authorities = certificate_authorities

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
        if not isinstance(other, ListCertificateAuthorityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
