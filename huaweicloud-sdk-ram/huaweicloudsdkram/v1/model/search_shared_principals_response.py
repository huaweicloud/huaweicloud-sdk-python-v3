# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchSharedPrincipalsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'shared_principals': 'list[SharedPrincipal]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'shared_principals': 'shared_principals',
        'page_info': 'page_info'
    }

    def __init__(self, shared_principals=None, page_info=None):
        r"""SearchSharedPrincipalsResponse

        The model defined in huaweicloud sdk

        :param shared_principals: 资源使用者的详细信息列表。
        :type shared_principals: list[:class:`huaweicloudsdkram.v1.SharedPrincipal`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkram.v1.PageInfo`
        """
        
        super(SearchSharedPrincipalsResponse, self).__init__()

        self._shared_principals = None
        self._page_info = None
        self.discriminator = None

        if shared_principals is not None:
            self.shared_principals = shared_principals
        if page_info is not None:
            self.page_info = page_info

    @property
    def shared_principals(self):
        r"""Gets the shared_principals of this SearchSharedPrincipalsResponse.

        资源使用者的详细信息列表。

        :return: The shared_principals of this SearchSharedPrincipalsResponse.
        :rtype: list[:class:`huaweicloudsdkram.v1.SharedPrincipal`]
        """
        return self._shared_principals

    @shared_principals.setter
    def shared_principals(self, shared_principals):
        r"""Sets the shared_principals of this SearchSharedPrincipalsResponse.

        资源使用者的详细信息列表。

        :param shared_principals: The shared_principals of this SearchSharedPrincipalsResponse.
        :type shared_principals: list[:class:`huaweicloudsdkram.v1.SharedPrincipal`]
        """
        self._shared_principals = shared_principals

    @property
    def page_info(self):
        r"""Gets the page_info of this SearchSharedPrincipalsResponse.

        :return: The page_info of this SearchSharedPrincipalsResponse.
        :rtype: :class:`huaweicloudsdkram.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this SearchSharedPrincipalsResponse.

        :param page_info: The page_info of this SearchSharedPrincipalsResponse.
        :type page_info: :class:`huaweicloudsdkram.v1.PageInfo`
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
        if not isinstance(other, SearchSharedPrincipalsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
