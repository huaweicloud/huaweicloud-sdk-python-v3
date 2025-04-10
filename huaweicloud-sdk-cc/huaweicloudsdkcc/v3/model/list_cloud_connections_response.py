# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudConnectionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'page_info': 'PageInfo',
        'cloud_connections': 'list[CloudConnection]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'page_info': 'page_info',
        'cloud_connections': 'cloud_connections'
    }

    def __init__(self, request_id=None, page_info=None, cloud_connections=None):
        r"""ListCloudConnectionsResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        :param cloud_connections: 云连接实例列表。
        :type cloud_connections: list[:class:`huaweicloudsdkcc.v3.CloudConnection`]
        """
        
        super(ListCloudConnectionsResponse, self).__init__()

        self._request_id = None
        self._page_info = None
        self._cloud_connections = None
        self.discriminator = None

        self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info
        self.cloud_connections = cloud_connections

    @property
    def request_id(self):
        r"""Gets the request_id of this ListCloudConnectionsResponse.

        请求ID。

        :return: The request_id of this ListCloudConnectionsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListCloudConnectionsResponse.

        请求ID。

        :param request_id: The request_id of this ListCloudConnectionsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        r"""Gets the page_info of this ListCloudConnectionsResponse.

        :return: The page_info of this ListCloudConnectionsResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListCloudConnectionsResponse.

        :param page_info: The page_info of this ListCloudConnectionsResponse.
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def cloud_connections(self):
        r"""Gets the cloud_connections of this ListCloudConnectionsResponse.

        云连接实例列表。

        :return: The cloud_connections of this ListCloudConnectionsResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CloudConnection`]
        """
        return self._cloud_connections

    @cloud_connections.setter
    def cloud_connections(self, cloud_connections):
        r"""Sets the cloud_connections of this ListCloudConnectionsResponse.

        云连接实例列表。

        :param cloud_connections: The cloud_connections of this ListCloudConnectionsResponse.
        :type cloud_connections: list[:class:`huaweicloudsdkcc.v3.CloudConnection`]
        """
        self._cloud_connections = cloud_connections

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
        if not isinstance(other, ListCloudConnectionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
