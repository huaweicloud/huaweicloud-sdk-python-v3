# coding: utf-8

import re
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
        'cloud_connections': 'list[CloudConnection]',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'cloud_connections': 'cloud_connections',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, cloud_connections=None, page_info=None, request_id=None):
        """ListCloudConnectionsResponse

        The model defined in huaweicloud sdk

        :param cloud_connections: 云连接实例列表。
        :type cloud_connections: list[:class:`huaweicloudsdkcc.v3.CloudConnection`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(ListCloudConnectionsResponse, self).__init__()

        self._cloud_connections = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if cloud_connections is not None:
            self.cloud_connections = cloud_connections
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def cloud_connections(self):
        """Gets the cloud_connections of this ListCloudConnectionsResponse.

        云连接实例列表。

        :return: The cloud_connections of this ListCloudConnectionsResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CloudConnection`]
        """
        return self._cloud_connections

    @cloud_connections.setter
    def cloud_connections(self, cloud_connections):
        """Sets the cloud_connections of this ListCloudConnectionsResponse.

        云连接实例列表。

        :param cloud_connections: The cloud_connections of this ListCloudConnectionsResponse.
        :type cloud_connections: list[:class:`huaweicloudsdkcc.v3.CloudConnection`]
        """
        self._cloud_connections = cloud_connections

    @property
    def page_info(self):
        """Gets the page_info of this ListCloudConnectionsResponse.

        :return: The page_info of this ListCloudConnectionsResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListCloudConnectionsResponse.

        :param page_info: The page_info of this ListCloudConnectionsResponse.
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListCloudConnectionsResponse.

        请求ID。

        :return: The request_id of this ListCloudConnectionsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListCloudConnectionsResponse.

        请求ID。

        :param request_id: The request_id of this ListCloudConnectionsResponse.
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
        if not isinstance(other, ListCloudConnectionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
