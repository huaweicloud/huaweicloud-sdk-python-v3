# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInternetBandwidthFilterTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resources': 'list[GeipResource]',
        'total_count': 'int',
        'request_id': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'resources': 'resources',
        'total_count': 'total_count',
        'request_id': 'request_id',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, resources=None, total_count=None, request_id=None, x_request_id=None):
        """ListInternetBandwidthFilterTagsResponse

        The model defined in huaweicloud sdk

        :param resources: 资源列表
        :type resources: list[:class:`huaweicloudsdkgeip.v3.GeipResource`]
        :param total_count: 当前列表中资源数量。
        :type total_count: int
        :param request_id: 本次请求的编号
        :type request_id: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListInternetBandwidthFilterTagsResponse, self).__init__()

        self._resources = None
        self._total_count = None
        self._request_id = None
        self._x_request_id = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if total_count is not None:
            self.total_count = total_count
        if request_id is not None:
            self.request_id = request_id
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def resources(self):
        """Gets the resources of this ListInternetBandwidthFilterTagsResponse.

        资源列表

        :return: The resources of this ListInternetBandwidthFilterTagsResponse.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.GeipResource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ListInternetBandwidthFilterTagsResponse.

        资源列表

        :param resources: The resources of this ListInternetBandwidthFilterTagsResponse.
        :type resources: list[:class:`huaweicloudsdkgeip.v3.GeipResource`]
        """
        self._resources = resources

    @property
    def total_count(self):
        """Gets the total_count of this ListInternetBandwidthFilterTagsResponse.

        当前列表中资源数量。

        :return: The total_count of this ListInternetBandwidthFilterTagsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListInternetBandwidthFilterTagsResponse.

        当前列表中资源数量。

        :param total_count: The total_count of this ListInternetBandwidthFilterTagsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def request_id(self):
        """Gets the request_id of this ListInternetBandwidthFilterTagsResponse.

        本次请求的编号

        :return: The request_id of this ListInternetBandwidthFilterTagsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListInternetBandwidthFilterTagsResponse.

        本次请求的编号

        :param request_id: The request_id of this ListInternetBandwidthFilterTagsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListInternetBandwidthFilterTagsResponse.

        :return: The x_request_id of this ListInternetBandwidthFilterTagsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListInternetBandwidthFilterTagsResponse.

        :param x_request_id: The x_request_id of this ListInternetBandwidthFilterTagsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListInternetBandwidthFilterTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
