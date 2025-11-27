# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSslCertDownloadAddressesResponse(SdkResponse):

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
        r"""ListSslCertDownloadAddressesResponse

        The model defined in huaweicloud sdk

        :param certs: **参数解释：** 证书列表。 **取值范围：** 不涉及。
        :type certs: list[:class:`huaweicloudsdkgaussdbfornosql.v3.CertInfo`]
        """
        
        super().__init__()

        self._certs = None
        self.discriminator = None

        if certs is not None:
            self.certs = certs

    @property
    def certs(self):
        r"""Gets the certs of this ListSslCertDownloadAddressesResponse.

        **参数解释：** 证书列表。 **取值范围：** 不涉及。

        :return: The certs of this ListSslCertDownloadAddressesResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.CertInfo`]
        """
        return self._certs

    @certs.setter
    def certs(self, certs):
        r"""Sets the certs of this ListSslCertDownloadAddressesResponse.

        **参数解释：** 证书列表。 **取值范围：** 不涉及。

        :param certs: The certs of this ListSslCertDownloadAddressesResponse.
        :type certs: list[:class:`huaweicloudsdkgaussdbfornosql.v3.CertInfo`]
        """
        self._certs = certs

    def to_dict(self):
        import warnings
        warnings.warn("ListSslCertDownloadAddressesResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSslCertDownloadAddressesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
