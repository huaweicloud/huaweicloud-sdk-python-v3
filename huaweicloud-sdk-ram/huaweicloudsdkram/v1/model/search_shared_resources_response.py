# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchSharedResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'shared_resources': 'list[SharedResource]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'shared_resources': 'shared_resources',
        'page_info': 'page_info'
    }

    def __init__(self, shared_resources=None, page_info=None):
        """SearchSharedResourcesResponse

        The model defined in huaweicloud sdk

        :param shared_resources: 共享资源的信息列表。
        :type shared_resources: list[:class:`huaweicloudsdkram.v1.SharedResource`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkram.v1.PageInfo`
        """
        
        super(SearchSharedResourcesResponse, self).__init__()

        self._shared_resources = None
        self._page_info = None
        self.discriminator = None

        if shared_resources is not None:
            self.shared_resources = shared_resources
        if page_info is not None:
            self.page_info = page_info

    @property
    def shared_resources(self):
        """Gets the shared_resources of this SearchSharedResourcesResponse.

        共享资源的信息列表。

        :return: The shared_resources of this SearchSharedResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkram.v1.SharedResource`]
        """
        return self._shared_resources

    @shared_resources.setter
    def shared_resources(self, shared_resources):
        """Sets the shared_resources of this SearchSharedResourcesResponse.

        共享资源的信息列表。

        :param shared_resources: The shared_resources of this SearchSharedResourcesResponse.
        :type shared_resources: list[:class:`huaweicloudsdkram.v1.SharedResource`]
        """
        self._shared_resources = shared_resources

    @property
    def page_info(self):
        """Gets the page_info of this SearchSharedResourcesResponse.

        :return: The page_info of this SearchSharedResourcesResponse.
        :rtype: :class:`huaweicloudsdkram.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this SearchSharedResourcesResponse.

        :param page_info: The page_info of this SearchSharedResourcesResponse.
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
        if not isinstance(other, SearchSharedResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
