# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSupportedRegionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_list': 'list[Region]'
    }

    attribute_map = {
        'region_list': 'region_list'
    }

    def __init__(self, region_list=None):
        """ListSupportedRegionResponse

        The model defined in huaweicloud sdk

        :param region_list: region列表。
        :type region_list: list[:class:`huaweicloudsdkapm.v1.Region`]
        """
        
        super(ListSupportedRegionResponse, self).__init__()

        self._region_list = None
        self.discriminator = None

        if region_list is not None:
            self.region_list = region_list

    @property
    def region_list(self):
        """Gets the region_list of this ListSupportedRegionResponse.

        region列表。

        :return: The region_list of this ListSupportedRegionResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.Region`]
        """
        return self._region_list

    @region_list.setter
    def region_list(self, region_list):
        """Sets the region_list of this ListSupportedRegionResponse.

        region列表。

        :param region_list: The region_list of this ListSupportedRegionResponse.
        :type region_list: list[:class:`huaweicloudsdkapm.v1.Region`]
        """
        self._region_list = region_list

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
        if not isinstance(other, ListSupportedRegionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
