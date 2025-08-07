# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListP2cVgwConnectionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connections': 'list[Connection]',
        'total_count': 'int',
        'request_id': 'str'
    }

    attribute_map = {
        'connections': 'connections',
        'total_count': 'total_count',
        'request_id': 'request_id'
    }

    def __init__(self, connections=None, total_count=None, request_id=None):
        r"""ListP2cVgwConnectionsResponse

        The model defined in huaweicloud sdk

        :param connections: 连接信息
        :type connections: list[:class:`huaweicloudsdkvpn.v5.Connection`]
        :param total_count: 总计数量
        :type total_count: int
        :param request_id: 请求ID
        :type request_id: str
        """
        
        super(ListP2cVgwConnectionsResponse, self).__init__()

        self._connections = None
        self._total_count = None
        self._request_id = None
        self.discriminator = None

        if connections is not None:
            self.connections = connections
        if total_count is not None:
            self.total_count = total_count
        if request_id is not None:
            self.request_id = request_id

    @property
    def connections(self):
        r"""Gets the connections of this ListP2cVgwConnectionsResponse.

        连接信息

        :return: The connections of this ListP2cVgwConnectionsResponse.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.Connection`]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        r"""Sets the connections of this ListP2cVgwConnectionsResponse.

        连接信息

        :param connections: The connections of this ListP2cVgwConnectionsResponse.
        :type connections: list[:class:`huaweicloudsdkvpn.v5.Connection`]
        """
        self._connections = connections

    @property
    def total_count(self):
        r"""Gets the total_count of this ListP2cVgwConnectionsResponse.

        总计数量

        :return: The total_count of this ListP2cVgwConnectionsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListP2cVgwConnectionsResponse.

        总计数量

        :param total_count: The total_count of this ListP2cVgwConnectionsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def request_id(self):
        r"""Gets the request_id of this ListP2cVgwConnectionsResponse.

        请求ID

        :return: The request_id of this ListP2cVgwConnectionsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListP2cVgwConnectionsResponse.

        请求ID

        :param request_id: The request_id of this ListP2cVgwConnectionsResponse.
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
        if not isinstance(other, ListP2cVgwConnectionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
