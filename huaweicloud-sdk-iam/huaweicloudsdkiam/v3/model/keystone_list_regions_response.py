# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneListRegionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'links': 'Links',
        'regions': 'list[Region]'
    }

    attribute_map = {
        'links': 'links',
        'regions': 'regions'
    }

    def __init__(self, links=None, regions=None):
        """KeystoneListRegionsResponse

        The model defined in huaweicloud sdk

        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        :param regions: 区域信息列表。
        :type regions: list[:class:`huaweicloudsdkiam.v3.Region`]
        """
        
        super(KeystoneListRegionsResponse, self).__init__()

        self._links = None
        self._regions = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if regions is not None:
            self.regions = regions

    @property
    def links(self):
        """Gets the links of this KeystoneListRegionsResponse.

        :return: The links of this KeystoneListRegionsResponse.
        :rtype: :class:`huaweicloudsdkiam.v3.Links`
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this KeystoneListRegionsResponse.

        :param links: The links of this KeystoneListRegionsResponse.
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        """
        self._links = links

    @property
    def regions(self):
        """Gets the regions of this KeystoneListRegionsResponse.

        区域信息列表。

        :return: The regions of this KeystoneListRegionsResponse.
        :rtype: list[:class:`huaweicloudsdkiam.v3.Region`]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this KeystoneListRegionsResponse.

        区域信息列表。

        :param regions: The regions of this KeystoneListRegionsResponse.
        :type regions: list[:class:`huaweicloudsdkiam.v3.Region`]
        """
        self._regions = regions

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
        if not isinstance(other, KeystoneListRegionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
