# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAggregateDiscoveredResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_identifiers': 'list[ResourceIdentifier]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'resource_identifiers': 'resource_identifiers',
        'page_info': 'page_info'
    }

    def __init__(self, resource_identifiers=None, page_info=None):
        r"""ListAggregateDiscoveredResourcesResponse

        The model defined in huaweicloud sdk

        :param resource_identifiers: 资源信息列表。
        :type resource_identifiers: list[:class:`huaweicloudsdkconfig.v1.ResourceIdentifier`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkconfig.v1.PageInfo`
        """
        
        super(ListAggregateDiscoveredResourcesResponse, self).__init__()

        self._resource_identifiers = None
        self._page_info = None
        self.discriminator = None

        if resource_identifiers is not None:
            self.resource_identifiers = resource_identifiers
        if page_info is not None:
            self.page_info = page_info

    @property
    def resource_identifiers(self):
        r"""Gets the resource_identifiers of this ListAggregateDiscoveredResourcesResponse.

        资源信息列表。

        :return: The resource_identifiers of this ListAggregateDiscoveredResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.ResourceIdentifier`]
        """
        return self._resource_identifiers

    @resource_identifiers.setter
    def resource_identifiers(self, resource_identifiers):
        r"""Sets the resource_identifiers of this ListAggregateDiscoveredResourcesResponse.

        资源信息列表。

        :param resource_identifiers: The resource_identifiers of this ListAggregateDiscoveredResourcesResponse.
        :type resource_identifiers: list[:class:`huaweicloudsdkconfig.v1.ResourceIdentifier`]
        """
        self._resource_identifiers = resource_identifiers

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAggregateDiscoveredResourcesResponse.

        :return: The page_info of this ListAggregateDiscoveredResourcesResponse.
        :rtype: :class:`huaweicloudsdkconfig.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAggregateDiscoveredResourcesResponse.

        :param page_info: The page_info of this ListAggregateDiscoveredResourcesResponse.
        :type page_info: :class:`huaweicloudsdkconfig.v1.PageInfo`
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
        if not isinstance(other, ListAggregateDiscoveredResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
