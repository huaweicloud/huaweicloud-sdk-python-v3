# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWorkflowResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'graph_name': 'str',
        'graph_urn': 'str',
        'last_modified': 'str',
        'x_request_id': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'graph_name': 'graph_name',
        'graph_urn': 'graph_urn',
        'last_modified': 'last_modified',
        'x_request_id': 'x-request-id',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, graph_name=None, graph_urn=None, last_modified=None, x_request_id=None, connection=None, content_length=None, date=None):
        """UpdateWorkflowResponse

        The model defined in huaweicloud sdk

        :param graph_name: 工作流名称。
        :type graph_name: str
        :param graph_urn: 工作流的URN。
        :type graph_urn: str
        :param last_modified: 工作流更新的时间。
        :type last_modified: str
        :param x_request_id: 
        :type x_request_id: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(UpdateWorkflowResponse, self).__init__()

        self._graph_name = None
        self._graph_urn = None
        self._last_modified = None
        self._x_request_id = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if graph_name is not None:
            self.graph_name = graph_name
        if graph_urn is not None:
            self.graph_urn = graph_urn
        if last_modified is not None:
            self.last_modified = last_modified
        if x_request_id is not None:
            self.x_request_id = x_request_id
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date

    @property
    def graph_name(self):
        """Gets the graph_name of this UpdateWorkflowResponse.

        工作流名称。

        :return: The graph_name of this UpdateWorkflowResponse.
        :rtype: str
        """
        return self._graph_name

    @graph_name.setter
    def graph_name(self, graph_name):
        """Sets the graph_name of this UpdateWorkflowResponse.

        工作流名称。

        :param graph_name: The graph_name of this UpdateWorkflowResponse.
        :type graph_name: str
        """
        self._graph_name = graph_name

    @property
    def graph_urn(self):
        """Gets the graph_urn of this UpdateWorkflowResponse.

        工作流的URN。

        :return: The graph_urn of this UpdateWorkflowResponse.
        :rtype: str
        """
        return self._graph_urn

    @graph_urn.setter
    def graph_urn(self, graph_urn):
        """Sets the graph_urn of this UpdateWorkflowResponse.

        工作流的URN。

        :param graph_urn: The graph_urn of this UpdateWorkflowResponse.
        :type graph_urn: str
        """
        self._graph_urn = graph_urn

    @property
    def last_modified(self):
        """Gets the last_modified of this UpdateWorkflowResponse.

        工作流更新的时间。

        :return: The last_modified of this UpdateWorkflowResponse.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this UpdateWorkflowResponse.

        工作流更新的时间。

        :param last_modified: The last_modified of this UpdateWorkflowResponse.
        :type last_modified: str
        """
        self._last_modified = last_modified

    @property
    def x_request_id(self):
        """Gets the x_request_id of this UpdateWorkflowResponse.

        :return: The x_request_id of this UpdateWorkflowResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this UpdateWorkflowResponse.

        :param x_request_id: The x_request_id of this UpdateWorkflowResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def connection(self):
        """Gets the connection of this UpdateWorkflowResponse.

        :return: The connection of this UpdateWorkflowResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this UpdateWorkflowResponse.

        :param connection: The connection of this UpdateWorkflowResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        """Gets the content_length of this UpdateWorkflowResponse.

        :return: The content_length of this UpdateWorkflowResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this UpdateWorkflowResponse.

        :param content_length: The content_length of this UpdateWorkflowResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        """Gets the date of this UpdateWorkflowResponse.

        :return: The date of this UpdateWorkflowResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this UpdateWorkflowResponse.

        :param date: The date of this UpdateWorkflowResponse.
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
        if not isinstance(other, UpdateWorkflowResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
