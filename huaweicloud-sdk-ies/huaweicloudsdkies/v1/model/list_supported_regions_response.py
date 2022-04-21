# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSupportedRegionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'regions': 'list[RegionDetail]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'regions': 'regions',
        'page_info': 'page_info'
    }

    def __init__(self, regions=None, page_info=None):
        """ListSupportedRegionsResponse

        The model defined in huaweicloud sdk

        :param regions: 区域列表
        :type regions: list[:class:`huaweicloudsdkies.v1.RegionDetail`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkies.v1.PageInfo`
        """
        
        super(ListSupportedRegionsResponse, self).__init__()

        self._regions = None
        self._page_info = None
        self.discriminator = None

        if regions is not None:
            self.regions = regions
        if page_info is not None:
            self.page_info = page_info

    @property
    def regions(self):
        """Gets the regions of this ListSupportedRegionsResponse.

        区域列表

        :return: The regions of this ListSupportedRegionsResponse.
        :rtype: list[:class:`huaweicloudsdkies.v1.RegionDetail`]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this ListSupportedRegionsResponse.

        区域列表

        :param regions: The regions of this ListSupportedRegionsResponse.
        :type regions: list[:class:`huaweicloudsdkies.v1.RegionDetail`]
        """
        self._regions = regions

    @property
    def page_info(self):
        """Gets the page_info of this ListSupportedRegionsResponse.


        :return: The page_info of this ListSupportedRegionsResponse.
        :rtype: :class:`huaweicloudsdkies.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListSupportedRegionsResponse.


        :param page_info: The page_info of this ListSupportedRegionsResponse.
        :type page_info: :class:`huaweicloudsdkies.v1.PageInfo`
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
        if not isinstance(other, ListSupportedRegionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
