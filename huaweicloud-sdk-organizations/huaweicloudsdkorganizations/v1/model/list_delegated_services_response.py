# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDelegatedServicesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delegated_services': 'list[DelegatedServiceDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'delegated_services': 'delegated_services',
        'page_info': 'page_info'
    }

    def __init__(self, delegated_services=None, page_info=None):
        r"""ListDelegatedServicesResponse

        The model defined in huaweicloud sdk

        :param delegated_services: 账号是其委托管理员的服务。
        :type delegated_services: list[:class:`huaweicloudsdkorganizations.v1.DelegatedServiceDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        
        super(ListDelegatedServicesResponse, self).__init__()

        self._delegated_services = None
        self._page_info = None
        self.discriminator = None

        if delegated_services is not None:
            self.delegated_services = delegated_services
        if page_info is not None:
            self.page_info = page_info

    @property
    def delegated_services(self):
        r"""Gets the delegated_services of this ListDelegatedServicesResponse.

        账号是其委托管理员的服务。

        :return: The delegated_services of this ListDelegatedServicesResponse.
        :rtype: list[:class:`huaweicloudsdkorganizations.v1.DelegatedServiceDto`]
        """
        return self._delegated_services

    @delegated_services.setter
    def delegated_services(self, delegated_services):
        r"""Sets the delegated_services of this ListDelegatedServicesResponse.

        账号是其委托管理员的服务。

        :param delegated_services: The delegated_services of this ListDelegatedServicesResponse.
        :type delegated_services: list[:class:`huaweicloudsdkorganizations.v1.DelegatedServiceDto`]
        """
        self._delegated_services = delegated_services

    @property
    def page_info(self):
        r"""Gets the page_info of this ListDelegatedServicesResponse.

        :return: The page_info of this ListDelegatedServicesResponse.
        :rtype: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListDelegatedServicesResponse.

        :param page_info: The page_info of this ListDelegatedServicesResponse.
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
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
        if not isinstance(other, ListDelegatedServicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
