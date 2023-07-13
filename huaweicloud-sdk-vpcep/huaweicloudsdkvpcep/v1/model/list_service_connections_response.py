# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServiceConnectionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connections': 'list[ConnectionEndpoints]',
        'total_count': 'int'
    }

    attribute_map = {
        'connections': 'connections',
        'total_count': 'total_count'
    }

    def __init__(self, connections=None, total_count=None):
        """ListServiceConnectionsResponse

        The model defined in huaweicloud sdk

        :param connections: 连接列表。
        :type connections: list[:class:`huaweicloudsdkvpcep.v1.ConnectionEndpoints`]
        :param total_count: 满足查询条件的终端节点总条数，不受分页（即limit、offset参数）影响。
        :type total_count: int
        """
        
        super(ListServiceConnectionsResponse, self).__init__()

        self._connections = None
        self._total_count = None
        self.discriminator = None

        if connections is not None:
            self.connections = connections
        if total_count is not None:
            self.total_count = total_count

    @property
    def connections(self):
        """Gets the connections of this ListServiceConnectionsResponse.

        连接列表。

        :return: The connections of this ListServiceConnectionsResponse.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.ConnectionEndpoints`]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this ListServiceConnectionsResponse.

        连接列表。

        :param connections: The connections of this ListServiceConnectionsResponse.
        :type connections: list[:class:`huaweicloudsdkvpcep.v1.ConnectionEndpoints`]
        """
        self._connections = connections

    @property
    def total_count(self):
        """Gets the total_count of this ListServiceConnectionsResponse.

        满足查询条件的终端节点总条数，不受分页（即limit、offset参数）影响。

        :return: The total_count of this ListServiceConnectionsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListServiceConnectionsResponse.

        满足查询条件的终端节点总条数，不受分页（即limit、offset参数）影响。

        :param total_count: The total_count of this ListServiceConnectionsResponse.
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
        if not isinstance(other, ListServiceConnectionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
