# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTransitIpsByTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resources': 'list[Resource]',
        'request_id': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'resources': 'resources',
        'request_id': 'request_id',
        'total_count': 'total_count'
    }

    def __init__(self, resources=None, request_id=None, total_count=None):
        r"""ListTransitIpsByTagsResponse

        The model defined in huaweicloud sdk

        :param resources: 资源列表。
        :type resources: list[:class:`huaweicloudsdknat.v2.Resource`]
        :param request_id: 请求id。
        :type request_id: str
        :param total_count: 总记录数。
        :type total_count: int
        """
        
        super(ListTransitIpsByTagsResponse, self).__init__()

        self._resources = None
        self._request_id = None
        self._total_count = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if request_id is not None:
            self.request_id = request_id
        if total_count is not None:
            self.total_count = total_count

    @property
    def resources(self):
        r"""Gets the resources of this ListTransitIpsByTagsResponse.

        资源列表。

        :return: The resources of this ListTransitIpsByTagsResponse.
        :rtype: list[:class:`huaweicloudsdknat.v2.Resource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ListTransitIpsByTagsResponse.

        资源列表。

        :param resources: The resources of this ListTransitIpsByTagsResponse.
        :type resources: list[:class:`huaweicloudsdknat.v2.Resource`]
        """
        self._resources = resources

    @property
    def request_id(self):
        r"""Gets the request_id of this ListTransitIpsByTagsResponse.

        请求id。

        :return: The request_id of this ListTransitIpsByTagsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListTransitIpsByTagsResponse.

        请求id。

        :param request_id: The request_id of this ListTransitIpsByTagsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def total_count(self):
        r"""Gets the total_count of this ListTransitIpsByTagsResponse.

        总记录数。

        :return: The total_count of this ListTransitIpsByTagsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListTransitIpsByTagsResponse.

        总记录数。

        :param total_count: The total_count of this ListTransitIpsByTagsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListTransitIpsByTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
