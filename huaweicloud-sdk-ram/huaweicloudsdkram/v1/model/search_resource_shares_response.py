# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchResourceSharesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_shares': 'list[ResourceShare]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'resource_shares': 'resource_shares',
        'page_info': 'page_info'
    }

    def __init__(self, resource_shares=None, page_info=None):
        """SearchResourceSharesResponse

        The model defined in huaweicloud sdk

        :param resource_shares: 资源共享实例的详细信息列表。
        :type resource_shares: list[:class:`huaweicloudsdkram.v1.ResourceShare`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkram.v1.PageInfo`
        """
        
        super(SearchResourceSharesResponse, self).__init__()

        self._resource_shares = None
        self._page_info = None
        self.discriminator = None

        if resource_shares is not None:
            self.resource_shares = resource_shares
        if page_info is not None:
            self.page_info = page_info

    @property
    def resource_shares(self):
        """Gets the resource_shares of this SearchResourceSharesResponse.

        资源共享实例的详细信息列表。

        :return: The resource_shares of this SearchResourceSharesResponse.
        :rtype: list[:class:`huaweicloudsdkram.v1.ResourceShare`]
        """
        return self._resource_shares

    @resource_shares.setter
    def resource_shares(self, resource_shares):
        """Sets the resource_shares of this SearchResourceSharesResponse.

        资源共享实例的详细信息列表。

        :param resource_shares: The resource_shares of this SearchResourceSharesResponse.
        :type resource_shares: list[:class:`huaweicloudsdkram.v1.ResourceShare`]
        """
        self._resource_shares = resource_shares

    @property
    def page_info(self):
        """Gets the page_info of this SearchResourceSharesResponse.

        :return: The page_info of this SearchResourceSharesResponse.
        :rtype: :class:`huaweicloudsdkram.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this SearchResourceSharesResponse.

        :param page_info: The page_info of this SearchResourceSharesResponse.
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
        if not isinstance(other, SearchResourceSharesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
