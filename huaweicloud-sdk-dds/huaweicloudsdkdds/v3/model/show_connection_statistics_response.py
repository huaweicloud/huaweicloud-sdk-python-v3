# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConnectionStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_connections': 'int',
        'total_inner_connections': 'int',
        'total_outer_connections': 'int',
        'inner_connections': 'list[QueryConnectionsResponse]',
        'outer_connections': 'list[QueryConnectionsResponse]'
    }

    attribute_map = {
        'total_connections': 'total_connections',
        'total_inner_connections': 'total_inner_connections',
        'total_outer_connections': 'total_outer_connections',
        'inner_connections': 'inner_connections',
        'outer_connections': 'outer_connections'
    }

    def __init__(self, total_connections=None, total_inner_connections=None, total_outer_connections=None, inner_connections=None, outer_connections=None):
        """ShowConnectionStatisticsResponse

        The model defined in huaweicloud sdk

        :param total_connections: 总连接数，包括内部连接与外部连接。
        :type total_connections: int
        :param total_inner_connections: 内部总连接数。
        :type total_inner_connections: int
        :param total_outer_connections: 外部总连接数。
        :type total_outer_connections: int
        :param inner_connections: 内部连接统计信息数组，最大记录数为200条。
        :type inner_connections: list[:class:`huaweicloudsdkdds.v3.QueryConnectionsResponse`]
        :param outer_connections: 外部连接统计信息数组，最大记录数为200条。
        :type outer_connections: list[:class:`huaweicloudsdkdds.v3.QueryConnectionsResponse`]
        """
        
        super(ShowConnectionStatisticsResponse, self).__init__()

        self._total_connections = None
        self._total_inner_connections = None
        self._total_outer_connections = None
        self._inner_connections = None
        self._outer_connections = None
        self.discriminator = None

        if total_connections is not None:
            self.total_connections = total_connections
        if total_inner_connections is not None:
            self.total_inner_connections = total_inner_connections
        if total_outer_connections is not None:
            self.total_outer_connections = total_outer_connections
        if inner_connections is not None:
            self.inner_connections = inner_connections
        if outer_connections is not None:
            self.outer_connections = outer_connections

    @property
    def total_connections(self):
        """Gets the total_connections of this ShowConnectionStatisticsResponse.

        总连接数，包括内部连接与外部连接。

        :return: The total_connections of this ShowConnectionStatisticsResponse.
        :rtype: int
        """
        return self._total_connections

    @total_connections.setter
    def total_connections(self, total_connections):
        """Sets the total_connections of this ShowConnectionStatisticsResponse.

        总连接数，包括内部连接与外部连接。

        :param total_connections: The total_connections of this ShowConnectionStatisticsResponse.
        :type total_connections: int
        """
        self._total_connections = total_connections

    @property
    def total_inner_connections(self):
        """Gets the total_inner_connections of this ShowConnectionStatisticsResponse.

        内部总连接数。

        :return: The total_inner_connections of this ShowConnectionStatisticsResponse.
        :rtype: int
        """
        return self._total_inner_connections

    @total_inner_connections.setter
    def total_inner_connections(self, total_inner_connections):
        """Sets the total_inner_connections of this ShowConnectionStatisticsResponse.

        内部总连接数。

        :param total_inner_connections: The total_inner_connections of this ShowConnectionStatisticsResponse.
        :type total_inner_connections: int
        """
        self._total_inner_connections = total_inner_connections

    @property
    def total_outer_connections(self):
        """Gets the total_outer_connections of this ShowConnectionStatisticsResponse.

        外部总连接数。

        :return: The total_outer_connections of this ShowConnectionStatisticsResponse.
        :rtype: int
        """
        return self._total_outer_connections

    @total_outer_connections.setter
    def total_outer_connections(self, total_outer_connections):
        """Sets the total_outer_connections of this ShowConnectionStatisticsResponse.

        外部总连接数。

        :param total_outer_connections: The total_outer_connections of this ShowConnectionStatisticsResponse.
        :type total_outer_connections: int
        """
        self._total_outer_connections = total_outer_connections

    @property
    def inner_connections(self):
        """Gets the inner_connections of this ShowConnectionStatisticsResponse.

        内部连接统计信息数组，最大记录数为200条。

        :return: The inner_connections of this ShowConnectionStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkdds.v3.QueryConnectionsResponse`]
        """
        return self._inner_connections

    @inner_connections.setter
    def inner_connections(self, inner_connections):
        """Sets the inner_connections of this ShowConnectionStatisticsResponse.

        内部连接统计信息数组，最大记录数为200条。

        :param inner_connections: The inner_connections of this ShowConnectionStatisticsResponse.
        :type inner_connections: list[:class:`huaweicloudsdkdds.v3.QueryConnectionsResponse`]
        """
        self._inner_connections = inner_connections

    @property
    def outer_connections(self):
        """Gets the outer_connections of this ShowConnectionStatisticsResponse.

        外部连接统计信息数组，最大记录数为200条。

        :return: The outer_connections of this ShowConnectionStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkdds.v3.QueryConnectionsResponse`]
        """
        return self._outer_connections

    @outer_connections.setter
    def outer_connections(self, outer_connections):
        """Sets the outer_connections of this ShowConnectionStatisticsResponse.

        外部连接统计信息数组，最大记录数为200条。

        :param outer_connections: The outer_connections of this ShowConnectionStatisticsResponse.
        :type outer_connections: list[:class:`huaweicloudsdkdds.v3.QueryConnectionsResponse`]
        """
        self._outer_connections = outer_connections

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
        if not isinstance(other, ShowConnectionStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
