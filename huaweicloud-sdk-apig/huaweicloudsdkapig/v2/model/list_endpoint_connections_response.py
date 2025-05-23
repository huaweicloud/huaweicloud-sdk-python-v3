# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEndpointConnectionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'total': 'int',
        'connections': 'list[EndpointConnection]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'size': 'size',
        'total': 'total',
        'connections': 'connections',
        'x_request_id': 'x-request-id'
    }

    def __init__(self, size=None, total=None, connections=None, x_request_id=None):
        r"""ListEndpointConnectionsResponse

        The model defined in huaweicloud sdk

        :param size: 本次返回的列表长度
        :type size: int
        :param total: 满足条件的记录数
        :type total: int
        :param connections: 连接列表
        :type connections: list[:class:`huaweicloudsdkapig.v2.EndpointConnection`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListEndpointConnectionsResponse, self).__init__()

        self._size = None
        self._total = None
        self._connections = None
        self._x_request_id = None
        self.discriminator = None

        self.size = size
        self.total = total
        if connections is not None:
            self.connections = connections
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def size(self):
        r"""Gets the size of this ListEndpointConnectionsResponse.

        本次返回的列表长度

        :return: The size of this ListEndpointConnectionsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListEndpointConnectionsResponse.

        本次返回的列表长度

        :param size: The size of this ListEndpointConnectionsResponse.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this ListEndpointConnectionsResponse.

        满足条件的记录数

        :return: The total of this ListEndpointConnectionsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListEndpointConnectionsResponse.

        满足条件的记录数

        :param total: The total of this ListEndpointConnectionsResponse.
        :type total: int
        """
        self._total = total

    @property
    def connections(self):
        r"""Gets the connections of this ListEndpointConnectionsResponse.

        连接列表

        :return: The connections of this ListEndpointConnectionsResponse.
        :rtype: list[:class:`huaweicloudsdkapig.v2.EndpointConnection`]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        r"""Sets the connections of this ListEndpointConnectionsResponse.

        连接列表

        :param connections: The connections of this ListEndpointConnectionsResponse.
        :type connections: list[:class:`huaweicloudsdkapig.v2.EndpointConnection`]
        """
        self._connections = connections

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListEndpointConnectionsResponse.

        :return: The x_request_id of this ListEndpointConnectionsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListEndpointConnectionsResponse.

        :param x_request_id: The x_request_id of this ListEndpointConnectionsResponse.
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
        if not isinstance(other, ListEndpointConnectionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
