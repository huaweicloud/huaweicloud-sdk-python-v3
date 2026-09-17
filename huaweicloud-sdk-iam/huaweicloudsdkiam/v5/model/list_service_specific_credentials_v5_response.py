# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServiceSpecificCredentialsV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_specific_credentials': 'list[ServiceSpecificCredentialMetadata]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'service_specific_credentials': 'service_specific_credentials',
        'page_info': 'page_info'
    }

    def __init__(self, service_specific_credentials=None, page_info=None):
        r"""ListServiceSpecificCredentialsV5Response

        The model defined in huaweicloud sdk

        :param service_specific_credentials: 服务专属凭证列表。
        :type service_specific_credentials: list[:class:`huaweicloudsdkiam.v5.ServiceSpecificCredentialMetadata`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        
        super().__init__()

        self._service_specific_credentials = None
        self._page_info = None
        self.discriminator = None

        if service_specific_credentials is not None:
            self.service_specific_credentials = service_specific_credentials
        if page_info is not None:
            self.page_info = page_info

    @property
    def service_specific_credentials(self):
        r"""Gets the service_specific_credentials of this ListServiceSpecificCredentialsV5Response.

        服务专属凭证列表。

        :return: The service_specific_credentials of this ListServiceSpecificCredentialsV5Response.
        :rtype: list[:class:`huaweicloudsdkiam.v5.ServiceSpecificCredentialMetadata`]
        """
        return self._service_specific_credentials

    @service_specific_credentials.setter
    def service_specific_credentials(self, service_specific_credentials):
        r"""Sets the service_specific_credentials of this ListServiceSpecificCredentialsV5Response.

        服务专属凭证列表。

        :param service_specific_credentials: The service_specific_credentials of this ListServiceSpecificCredentialsV5Response.
        :type service_specific_credentials: list[:class:`huaweicloudsdkiam.v5.ServiceSpecificCredentialMetadata`]
        """
        self._service_specific_credentials = service_specific_credentials

    @property
    def page_info(self):
        r"""Gets the page_info of this ListServiceSpecificCredentialsV5Response.

        :return: The page_info of this ListServiceSpecificCredentialsV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListServiceSpecificCredentialsV5Response.

        :param page_info: The page_info of this ListServiceSpecificCredentialsV5Response.
        :type page_info: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListServiceSpecificCredentialsV5Response.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListServiceSpecificCredentialsV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
