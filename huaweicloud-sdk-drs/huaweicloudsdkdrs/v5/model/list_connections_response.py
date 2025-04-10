# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConnectionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connections': 'list[ConnectionResp]',
        'count': 'int'
    }

    attribute_map = {
        'connections': 'connections',
        'count': 'count'
    }

    def __init__(self, connections=None, count=None):
        r"""ListConnectionsResponse

        The model defined in huaweicloud sdk

        :param connections: 连接信息列表。
        :type connections: list[:class:`huaweicloudsdkdrs.v5.ConnectionResp`]
        :param count: 列表中的项目总数，与分页无关。
        :type count: int
        """
        
        super(ListConnectionsResponse, self).__init__()

        self._connections = None
        self._count = None
        self.discriminator = None

        if connections is not None:
            self.connections = connections
        if count is not None:
            self.count = count

    @property
    def connections(self):
        r"""Gets the connections of this ListConnectionsResponse.

        连接信息列表。

        :return: The connections of this ListConnectionsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ConnectionResp`]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        r"""Sets the connections of this ListConnectionsResponse.

        连接信息列表。

        :param connections: The connections of this ListConnectionsResponse.
        :type connections: list[:class:`huaweicloudsdkdrs.v5.ConnectionResp`]
        """
        self._connections = connections

    @property
    def count(self):
        r"""Gets the count of this ListConnectionsResponse.

        列表中的项目总数，与分页无关。

        :return: The count of this ListConnectionsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListConnectionsResponse.

        列表中的项目总数，与分页无关。

        :param count: The count of this ListConnectionsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListConnectionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
