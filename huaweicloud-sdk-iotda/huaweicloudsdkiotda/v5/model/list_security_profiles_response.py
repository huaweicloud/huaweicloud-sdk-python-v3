# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityProfilesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_profiles': 'list[SecurityProfileDTO]',
        'page': 'Page'
    }

    attribute_map = {
        'security_profiles': 'security_profiles',
        'page': 'page'
    }

    def __init__(self, security_profiles=None, page=None):
        r"""ListSecurityProfilesResponse

        The model defined in huaweicloud sdk

        :param security_profiles: 安全态势感知配置信息列表。
        :type security_profiles: list[:class:`huaweicloudsdkiotda.v5.SecurityProfileDTO`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        
        super(ListSecurityProfilesResponse, self).__init__()

        self._security_profiles = None
        self._page = None
        self.discriminator = None

        if security_profiles is not None:
            self.security_profiles = security_profiles
        if page is not None:
            self.page = page

    @property
    def security_profiles(self):
        r"""Gets the security_profiles of this ListSecurityProfilesResponse.

        安全态势感知配置信息列表。

        :return: The security_profiles of this ListSecurityProfilesResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.SecurityProfileDTO`]
        """
        return self._security_profiles

    @security_profiles.setter
    def security_profiles(self, security_profiles):
        r"""Sets the security_profiles of this ListSecurityProfilesResponse.

        安全态势感知配置信息列表。

        :param security_profiles: The security_profiles of this ListSecurityProfilesResponse.
        :type security_profiles: list[:class:`huaweicloudsdkiotda.v5.SecurityProfileDTO`]
        """
        self._security_profiles = security_profiles

    @property
    def page(self):
        r"""Gets the page of this ListSecurityProfilesResponse.

        :return: The page of this ListSecurityProfilesResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.Page`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListSecurityProfilesResponse.

        :param page: The page of this ListSecurityProfilesResponse.
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        self._page = page

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
        if not isinstance(other, ListSecurityProfilesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
