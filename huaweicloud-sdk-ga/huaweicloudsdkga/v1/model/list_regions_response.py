# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRegionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'regions': 'list[Region]',
        'request_id': 'str'
    }

    attribute_map = {
        'regions': 'regions',
        'request_id': 'request_id'
    }

    def __init__(self, regions=None, request_id=None):
        """ListRegionsResponse

        The model defined in huaweicloud sdk

        :param regions: 区域列表。
        :type regions: list[:class:`huaweicloudsdkga.v1.Region`]
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(ListRegionsResponse, self).__init__()

        self._regions = None
        self._request_id = None
        self.discriminator = None

        if regions is not None:
            self.regions = regions
        if request_id is not None:
            self.request_id = request_id

    @property
    def regions(self):
        """Gets the regions of this ListRegionsResponse.

        区域列表。

        :return: The regions of this ListRegionsResponse.
        :rtype: list[:class:`huaweicloudsdkga.v1.Region`]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this ListRegionsResponse.

        区域列表。

        :param regions: The regions of this ListRegionsResponse.
        :type regions: list[:class:`huaweicloudsdkga.v1.Region`]
        """
        self._regions = regions

    @property
    def request_id(self):
        """Gets the request_id of this ListRegionsResponse.

        请求ID。

        :return: The request_id of this ListRegionsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListRegionsResponse.

        请求ID。

        :param request_id: The request_id of this ListRegionsResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ListRegionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
