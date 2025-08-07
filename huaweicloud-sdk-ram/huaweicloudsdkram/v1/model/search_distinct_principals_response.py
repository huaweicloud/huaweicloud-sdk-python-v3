# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchDistinctPrincipalsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'distinct_shared_principals': 'list[DistinctSharedPrincipal]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'distinct_shared_principals': 'distinct_shared_principals',
        'page_info': 'page_info'
    }

    def __init__(self, distinct_shared_principals=None, page_info=None):
        r"""SearchDistinctPrincipalsResponse

        The model defined in huaweicloud sdk

        :param distinct_shared_principals: 不同角色的信息列表。
        :type distinct_shared_principals: list[:class:`huaweicloudsdkram.v1.DistinctSharedPrincipal`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkram.v1.PageInfo`
        """
        
        super(SearchDistinctPrincipalsResponse, self).__init__()

        self._distinct_shared_principals = None
        self._page_info = None
        self.discriminator = None

        if distinct_shared_principals is not None:
            self.distinct_shared_principals = distinct_shared_principals
        if page_info is not None:
            self.page_info = page_info

    @property
    def distinct_shared_principals(self):
        r"""Gets the distinct_shared_principals of this SearchDistinctPrincipalsResponse.

        不同角色的信息列表。

        :return: The distinct_shared_principals of this SearchDistinctPrincipalsResponse.
        :rtype: list[:class:`huaweicloudsdkram.v1.DistinctSharedPrincipal`]
        """
        return self._distinct_shared_principals

    @distinct_shared_principals.setter
    def distinct_shared_principals(self, distinct_shared_principals):
        r"""Sets the distinct_shared_principals of this SearchDistinctPrincipalsResponse.

        不同角色的信息列表。

        :param distinct_shared_principals: The distinct_shared_principals of this SearchDistinctPrincipalsResponse.
        :type distinct_shared_principals: list[:class:`huaweicloudsdkram.v1.DistinctSharedPrincipal`]
        """
        self._distinct_shared_principals = distinct_shared_principals

    @property
    def page_info(self):
        r"""Gets the page_info of this SearchDistinctPrincipalsResponse.

        :return: The page_info of this SearchDistinctPrincipalsResponse.
        :rtype: :class:`huaweicloudsdkram.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this SearchDistinctPrincipalsResponse.

        :param page_info: The page_info of this SearchDistinctPrincipalsResponse.
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
        if not isinstance(other, SearchDistinctPrincipalsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
