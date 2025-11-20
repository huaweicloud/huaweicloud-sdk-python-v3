# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServerCertificateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_certificates': 'list[ServerCertificateDTO]',
        'page': 'Page'
    }

    attribute_map = {
        'server_certificates': 'server_certificates',
        'page': 'page'
    }

    def __init__(self, server_certificates=None, page=None):
        r"""ListServerCertificateResponse

        The model defined in huaweicloud sdk

        :param server_certificates: **参数说明**：服务端证书列表。
        :type server_certificates: list[:class:`huaweicloudsdkiotda.v5.ServerCertificateDTO`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        
        super().__init__()

        self._server_certificates = None
        self._page = None
        self.discriminator = None

        if server_certificates is not None:
            self.server_certificates = server_certificates
        if page is not None:
            self.page = page

    @property
    def server_certificates(self):
        r"""Gets the server_certificates of this ListServerCertificateResponse.

        **参数说明**：服务端证书列表。

        :return: The server_certificates of this ListServerCertificateResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.ServerCertificateDTO`]
        """
        return self._server_certificates

    @server_certificates.setter
    def server_certificates(self, server_certificates):
        r"""Sets the server_certificates of this ListServerCertificateResponse.

        **参数说明**：服务端证书列表。

        :param server_certificates: The server_certificates of this ListServerCertificateResponse.
        :type server_certificates: list[:class:`huaweicloudsdkiotda.v5.ServerCertificateDTO`]
        """
        self._server_certificates = server_certificates

    @property
    def page(self):
        r"""Gets the page of this ListServerCertificateResponse.

        :return: The page of this ListServerCertificateResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.Page`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListServerCertificateResponse.

        :param page: The page of this ListServerCertificateResponse.
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        self._page = page

    def to_dict(self):
        import warnings
        warnings.warn("ListServerCertificateResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListServerCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
