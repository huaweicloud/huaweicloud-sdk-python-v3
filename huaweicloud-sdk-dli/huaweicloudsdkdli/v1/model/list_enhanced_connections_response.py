# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnhancedConnectionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'connections': 'list[ListEnhancedConnectionsDetail]',
        'count': 'int'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'connections': 'connections',
        'count': 'count'
    }

    def __init__(self, is_success=None, message=None, connections=None, count=None):
        """ListEnhancedConnectionsResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param connections: 跨源连接信息列表。
        :type connections: list[:class:`huaweicloudsdkdli.v1.ListEnhancedConnectionsDetail`]
        :param count: 返回的跨源连接个数。
        :type count: int
        """
        
        super(ListEnhancedConnectionsResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._connections = None
        self._count = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if connections is not None:
            self.connections = connections
        if count is not None:
            self.count = count

    @property
    def is_success(self):
        """Gets the is_success of this ListEnhancedConnectionsResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this ListEnhancedConnectionsResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ListEnhancedConnectionsResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ListEnhancedConnectionsResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ListEnhancedConnectionsResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ListEnhancedConnectionsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListEnhancedConnectionsResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ListEnhancedConnectionsResponse.
        :type message: str
        """
        self._message = message

    @property
    def connections(self):
        """Gets the connections of this ListEnhancedConnectionsResponse.

        跨源连接信息列表。

        :return: The connections of this ListEnhancedConnectionsResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.ListEnhancedConnectionsDetail`]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this ListEnhancedConnectionsResponse.

        跨源连接信息列表。

        :param connections: The connections of this ListEnhancedConnectionsResponse.
        :type connections: list[:class:`huaweicloudsdkdli.v1.ListEnhancedConnectionsDetail`]
        """
        self._connections = connections

    @property
    def count(self):
        """Gets the count of this ListEnhancedConnectionsResponse.

        返回的跨源连接个数。

        :return: The count of this ListEnhancedConnectionsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListEnhancedConnectionsResponse.

        返回的跨源连接个数。

        :param count: The count of this ListEnhancedConnectionsResponse.
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
        if not isinstance(other, ListEnhancedConnectionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
