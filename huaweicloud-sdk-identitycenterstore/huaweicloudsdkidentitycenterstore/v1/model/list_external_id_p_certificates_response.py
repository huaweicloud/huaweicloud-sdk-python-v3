# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListExternalIdPCertificatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'idp_certificates': 'list[IdpCertificate]'
    }

    attribute_map = {
        'idp_certificates': 'idp_certificates'
    }

    def __init__(self, idp_certificates=None):
        r"""ListExternalIdPCertificatesResponse

        The model defined in huaweicloud sdk

        :param idp_certificates: 外部身份提供商证书列表
        :type idp_certificates: list[:class:`huaweicloudsdkidentitycenterstore.v1.IdpCertificate`]
        """
        
        super(ListExternalIdPCertificatesResponse, self).__init__()

        self._idp_certificates = None
        self.discriminator = None

        if idp_certificates is not None:
            self.idp_certificates = idp_certificates

    @property
    def idp_certificates(self):
        r"""Gets the idp_certificates of this ListExternalIdPCertificatesResponse.

        外部身份提供商证书列表

        :return: The idp_certificates of this ListExternalIdPCertificatesResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.IdpCertificate`]
        """
        return self._idp_certificates

    @idp_certificates.setter
    def idp_certificates(self, idp_certificates):
        r"""Sets the idp_certificates of this ListExternalIdPCertificatesResponse.

        外部身份提供商证书列表

        :param idp_certificates: The idp_certificates of this ListExternalIdPCertificatesResponse.
        :type idp_certificates: list[:class:`huaweicloudsdkidentitycenterstore.v1.IdpCertificate`]
        """
        self._idp_certificates = idp_certificates

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
        if not isinstance(other, ListExternalIdPCertificatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
