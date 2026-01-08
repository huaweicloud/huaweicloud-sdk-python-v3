# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cert_list': 'list[CertItem]'
    }

    attribute_map = {
        'cert_list': 'cert_list'
    }

    def __init__(self, cert_list=None):
        r"""ListCertsResponse

        The model defined in huaweicloud sdk

        :param cert_list: 证书列表。
        :type cert_list: list[:class:`huaweicloudsdkworkspace.v2.CertItem`]
        """
        
        super().__init__()

        self._cert_list = None
        self.discriminator = None

        if cert_list is not None:
            self.cert_list = cert_list

    @property
    def cert_list(self):
        r"""Gets the cert_list of this ListCertsResponse.

        证书列表。

        :return: The cert_list of this ListCertsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.CertItem`]
        """
        return self._cert_list

    @cert_list.setter
    def cert_list(self, cert_list):
        r"""Sets the cert_list of this ListCertsResponse.

        证书列表。

        :param cert_list: The cert_list of this ListCertsResponse.
        :type cert_list: list[:class:`huaweicloudsdkworkspace.v2.CertItem`]
        """
        self._cert_list = cert_list

    def to_dict(self):
        import warnings
        warnings.warn("ListCertsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCertsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
