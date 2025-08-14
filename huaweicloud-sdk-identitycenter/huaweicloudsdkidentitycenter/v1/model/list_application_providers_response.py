# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationProvidersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_providers': 'list[ApplicationProviderDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'application_providers': 'application_providers',
        'page_info': 'page_info'
    }

    def __init__(self, application_providers=None, page_info=None):
        r"""ListApplicationProvidersResponse

        The model defined in huaweicloud sdk

        :param application_providers: 应用程序提供商列表
        :type application_providers: list[:class:`huaweicloudsdkidentitycenter.v1.ApplicationProviderDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        
        super(ListApplicationProvidersResponse, self).__init__()

        self._application_providers = None
        self._page_info = None
        self.discriminator = None

        if application_providers is not None:
            self.application_providers = application_providers
        if page_info is not None:
            self.page_info = page_info

    @property
    def application_providers(self):
        r"""Gets the application_providers of this ListApplicationProvidersResponse.

        应用程序提供商列表

        :return: The application_providers of this ListApplicationProvidersResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenter.v1.ApplicationProviderDto`]
        """
        return self._application_providers

    @application_providers.setter
    def application_providers(self, application_providers):
        r"""Sets the application_providers of this ListApplicationProvidersResponse.

        应用程序提供商列表

        :param application_providers: The application_providers of this ListApplicationProvidersResponse.
        :type application_providers: list[:class:`huaweicloudsdkidentitycenter.v1.ApplicationProviderDto`]
        """
        self._application_providers = application_providers

    @property
    def page_info(self):
        r"""Gets the page_info of this ListApplicationProvidersResponse.

        :return: The page_info of this ListApplicationProvidersResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListApplicationProvidersResponse.

        :param page_info: The page_info of this ListApplicationProvidersResponse.
        :type page_info: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListApplicationProvidersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
