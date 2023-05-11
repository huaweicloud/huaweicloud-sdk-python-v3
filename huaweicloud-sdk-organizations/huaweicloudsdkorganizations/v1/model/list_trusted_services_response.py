# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTrustedServicesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trusted_services': 'list[TrustedServiceDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'trusted_services': 'trusted_services',
        'page_info': 'page_info'
    }

    def __init__(self, trusted_services=None, page_info=None):
        """ListTrustedServicesResponse

        The model defined in huaweicloud sdk

        :param trusted_services: 启用与组织集成的服务主体列表。
        :type trusted_services: list[:class:`huaweicloudsdkorganizations.v1.TrustedServiceDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        
        super(ListTrustedServicesResponse, self).__init__()

        self._trusted_services = None
        self._page_info = None
        self.discriminator = None

        if trusted_services is not None:
            self.trusted_services = trusted_services
        if page_info is not None:
            self.page_info = page_info

    @property
    def trusted_services(self):
        """Gets the trusted_services of this ListTrustedServicesResponse.

        启用与组织集成的服务主体列表。

        :return: The trusted_services of this ListTrustedServicesResponse.
        :rtype: list[:class:`huaweicloudsdkorganizations.v1.TrustedServiceDto`]
        """
        return self._trusted_services

    @trusted_services.setter
    def trusted_services(self, trusted_services):
        """Sets the trusted_services of this ListTrustedServicesResponse.

        启用与组织集成的服务主体列表。

        :param trusted_services: The trusted_services of this ListTrustedServicesResponse.
        :type trusted_services: list[:class:`huaweicloudsdkorganizations.v1.TrustedServiceDto`]
        """
        self._trusted_services = trusted_services

    @property
    def page_info(self):
        """Gets the page_info of this ListTrustedServicesResponse.

        :return: The page_info of this ListTrustedServicesResponse.
        :rtype: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListTrustedServicesResponse.

        :param page_info: The page_info of this ListTrustedServicesResponse.
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
        if not isinstance(other, ListTrustedServicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
