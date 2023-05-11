# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'graphs': 'list[GraphItem]',
        'next_offset': 'int',
        'is_truncated': 'bool',
        'x_request_id': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'count': 'count',
        'graphs': 'graphs',
        'next_offset': 'next_offset',
        'is_truncated': 'is_truncated',
        'x_request_id': 'x-request-id',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, count=None, graphs=None, next_offset=None, is_truncated=None, x_request_id=None, connection=None, content_length=None, date=None):
        """ListWorkflowsResponse

        The model defined in huaweicloud sdk

        :param count: 列表总条数。
        :type count: int
        :param graphs: 工作流模板列表信息。
        :type graphs: list[:class:`huaweicloudsdkdwr.v3.GraphItem`]
        :param next_offset: 下一次查询的起始位置。
        :type next_offset: int
        :param is_truncated: 表明是否本次返回的ListWorkflow结果列表被截断。“true”表示本次没有返回全部结果；“false”表示本次已经返回了全部结果。
        :type is_truncated: bool
        :param x_request_id: 
        :type x_request_id: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(ListWorkflowsResponse, self).__init__()

        self._count = None
        self._graphs = None
        self._next_offset = None
        self._is_truncated = None
        self._x_request_id = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if graphs is not None:
            self.graphs = graphs
        if next_offset is not None:
            self.next_offset = next_offset
        if is_truncated is not None:
            self.is_truncated = is_truncated
        if x_request_id is not None:
            self.x_request_id = x_request_id
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date

    @property
    def count(self):
        """Gets the count of this ListWorkflowsResponse.

        列表总条数。

        :return: The count of this ListWorkflowsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListWorkflowsResponse.

        列表总条数。

        :param count: The count of this ListWorkflowsResponse.
        :type count: int
        """
        self._count = count

    @property
    def graphs(self):
        """Gets the graphs of this ListWorkflowsResponse.

        工作流模板列表信息。

        :return: The graphs of this ListWorkflowsResponse.
        :rtype: list[:class:`huaweicloudsdkdwr.v3.GraphItem`]
        """
        return self._graphs

    @graphs.setter
    def graphs(self, graphs):
        """Sets the graphs of this ListWorkflowsResponse.

        工作流模板列表信息。

        :param graphs: The graphs of this ListWorkflowsResponse.
        :type graphs: list[:class:`huaweicloudsdkdwr.v3.GraphItem`]
        """
        self._graphs = graphs

    @property
    def next_offset(self):
        """Gets the next_offset of this ListWorkflowsResponse.

        下一次查询的起始位置。

        :return: The next_offset of this ListWorkflowsResponse.
        :rtype: int
        """
        return self._next_offset

    @next_offset.setter
    def next_offset(self, next_offset):
        """Sets the next_offset of this ListWorkflowsResponse.

        下一次查询的起始位置。

        :param next_offset: The next_offset of this ListWorkflowsResponse.
        :type next_offset: int
        """
        self._next_offset = next_offset

    @property
    def is_truncated(self):
        """Gets the is_truncated of this ListWorkflowsResponse.

        表明是否本次返回的ListWorkflow结果列表被截断。“true”表示本次没有返回全部结果；“false”表示本次已经返回了全部结果。

        :return: The is_truncated of this ListWorkflowsResponse.
        :rtype: bool
        """
        return self._is_truncated

    @is_truncated.setter
    def is_truncated(self, is_truncated):
        """Sets the is_truncated of this ListWorkflowsResponse.

        表明是否本次返回的ListWorkflow结果列表被截断。“true”表示本次没有返回全部结果；“false”表示本次已经返回了全部结果。

        :param is_truncated: The is_truncated of this ListWorkflowsResponse.
        :type is_truncated: bool
        """
        self._is_truncated = is_truncated

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListWorkflowsResponse.

        :return: The x_request_id of this ListWorkflowsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListWorkflowsResponse.

        :param x_request_id: The x_request_id of this ListWorkflowsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def connection(self):
        """Gets the connection of this ListWorkflowsResponse.

        :return: The connection of this ListWorkflowsResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this ListWorkflowsResponse.

        :param connection: The connection of this ListWorkflowsResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        """Gets the content_length of this ListWorkflowsResponse.

        :return: The content_length of this ListWorkflowsResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this ListWorkflowsResponse.

        :param content_length: The content_length of this ListWorkflowsResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        """Gets the date of this ListWorkflowsResponse.

        :return: The date of this ListWorkflowsResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ListWorkflowsResponse.

        :param date: The date of this ListWorkflowsResponse.
        :type date: str
        """
        self._date = date

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
        if not isinstance(other, ListWorkflowsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
