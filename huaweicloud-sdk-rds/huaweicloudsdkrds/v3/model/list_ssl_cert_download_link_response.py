# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSslCertDownloadLinkResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cert_info_list': 'list[DownloadInfoRsp]'
    }

    attribute_map = {
        'cert_info_list': 'cert_info_list'
    }

    def __init__(self, cert_info_list=None):
        r"""ListSslCertDownloadLinkResponse

        The model defined in huaweicloud sdk

        :param cert_info_list: 
        :type cert_info_list: list[:class:`huaweicloudsdkrds.v3.DownloadInfoRsp`]
        """
        
        super().__init__()

        self._cert_info_list = None
        self.discriminator = None

        if cert_info_list is not None:
            self.cert_info_list = cert_info_list

    @property
    def cert_info_list(self):
        r"""Gets the cert_info_list of this ListSslCertDownloadLinkResponse.

        :return: The cert_info_list of this ListSslCertDownloadLinkResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.DownloadInfoRsp`]
        """
        return self._cert_info_list

    @cert_info_list.setter
    def cert_info_list(self, cert_info_list):
        r"""Sets the cert_info_list of this ListSslCertDownloadLinkResponse.

        :param cert_info_list: The cert_info_list of this ListSslCertDownloadLinkResponse.
        :type cert_info_list: list[:class:`huaweicloudsdkrds.v3.DownloadInfoRsp`]
        """
        self._cert_info_list = cert_info_list

    def to_dict(self):
        import warnings
        warnings.warn("ListSslCertDownloadLinkResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSslCertDownloadLinkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
