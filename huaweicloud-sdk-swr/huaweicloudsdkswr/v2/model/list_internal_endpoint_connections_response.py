# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInternalEndpointConnectionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connections': 'list[ConnectionItem]',
        'total_count': 'int'
    }

    attribute_map = {
        'connections': 'connections',
        'total_count': 'total_count'
    }

    def __init__(self, connections=None, total_count=None):
        r"""ListInternalEndpointConnectionsResponse

        The model defined in huaweicloud sdk

        :param connections: 连接列表
        :type connections: list[:class:`huaweicloudsdkswr.v2.ConnectionItem`]
        :param total_count: 满足查询条件的连接总条数
        :type total_count: int
        """
        
        super().__init__()

        self._connections = None
        self._total_count = None
        self.discriminator = None

        if connections is not None:
            self.connections = connections
        if total_count is not None:
            self.total_count = total_count

    @property
    def connections(self):
        r"""Gets the connections of this ListInternalEndpointConnectionsResponse.

        连接列表

        :return: The connections of this ListInternalEndpointConnectionsResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.ConnectionItem`]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        r"""Sets the connections of this ListInternalEndpointConnectionsResponse.

        连接列表

        :param connections: The connections of this ListInternalEndpointConnectionsResponse.
        :type connections: list[:class:`huaweicloudsdkswr.v2.ConnectionItem`]
        """
        self._connections = connections

    @property
    def total_count(self):
        r"""Gets the total_count of this ListInternalEndpointConnectionsResponse.

        满足查询条件的连接总条数

        :return: The total_count of this ListInternalEndpointConnectionsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListInternalEndpointConnectionsResponse.

        满足查询条件的连接总条数

        :param total_count: The total_count of this ListInternalEndpointConnectionsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ListInternalEndpointConnectionsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListInternalEndpointConnectionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
