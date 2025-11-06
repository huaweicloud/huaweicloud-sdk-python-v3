# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListElbCertsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificates': 'list[CertificatesResource]'
    }

    attribute_map = {
        'certificates': 'certificates'
    }

    def __init__(self, certificates=None):
        r"""ListElbCertsResponse

        The model defined in huaweicloud sdk

        :param certificates: 证书列表信息。
        :type certificates: list[:class:`huaweicloudsdkcss.v1.CertificatesResource`]
        """
        
        super().__init__()

        self._certificates = None
        self.discriminator = None

        if certificates is not None:
            self.certificates = certificates

    @property
    def certificates(self):
        r"""Gets the certificates of this ListElbCertsResponse.

        证书列表信息。

        :return: The certificates of this ListElbCertsResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.CertificatesResource`]
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates):
        r"""Sets the certificates of this ListElbCertsResponse.

        证书列表信息。

        :param certificates: The certificates of this ListElbCertsResponse.
        :type certificates: list[:class:`huaweicloudsdkcss.v1.CertificatesResource`]
        """
        self._certificates = certificates

    def to_dict(self):
        import warnings
        warnings.warn("ListElbCertsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListElbCertsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
