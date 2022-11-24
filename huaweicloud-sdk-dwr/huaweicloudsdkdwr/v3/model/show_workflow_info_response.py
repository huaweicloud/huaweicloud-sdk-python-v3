# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkflowInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'created_at': 'str',
        'definition': 'object',
        'graph_urn': 'str',
        'description': 'str',
        'x_request_id': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'name': 'name',
        'created_at': 'created_at',
        'definition': 'definition',
        'graph_urn': 'graph_urn',
        'description': 'description',
        'x_request_id': 'x-request-id',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, name=None, created_at=None, definition=None, graph_urn=None, description=None, x_request_id=None, connection=None, content_length=None, date=None):
        """ShowWorkflowInfoResponse

        The model defined in huaweicloud sdk

        :param name: 工作流的名称。
        :type name: str
        :param created_at: 工作流的创建时间。
        :type created_at: str
        :param definition: 工作流的定义。
        :type definition: object
        :param graph_urn: 工作流的URN。
        :type graph_urn: str
        :param description: 工作流的描述。
        :type description: str
        :param x_request_id: 
        :type x_request_id: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(ShowWorkflowInfoResponse, self).__init__()

        self._name = None
        self._created_at = None
        self._definition = None
        self._graph_urn = None
        self._description = None
        self._x_request_id = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if definition is not None:
            self.definition = definition
        if graph_urn is not None:
            self.graph_urn = graph_urn
        if description is not None:
            self.description = description
        if x_request_id is not None:
            self.x_request_id = x_request_id
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date

    @property
    def name(self):
        """Gets the name of this ShowWorkflowInfoResponse.

        工作流的名称。

        :return: The name of this ShowWorkflowInfoResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowWorkflowInfoResponse.

        工作流的名称。

        :param name: The name of this ShowWorkflowInfoResponse.
        :type name: str
        """
        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this ShowWorkflowInfoResponse.

        工作流的创建时间。

        :return: The created_at of this ShowWorkflowInfoResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowWorkflowInfoResponse.

        工作流的创建时间。

        :param created_at: The created_at of this ShowWorkflowInfoResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def definition(self):
        """Gets the definition of this ShowWorkflowInfoResponse.

        工作流的定义。

        :return: The definition of this ShowWorkflowInfoResponse.
        :rtype: object
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this ShowWorkflowInfoResponse.

        工作流的定义。

        :param definition: The definition of this ShowWorkflowInfoResponse.
        :type definition: object
        """
        self._definition = definition

    @property
    def graph_urn(self):
        """Gets the graph_urn of this ShowWorkflowInfoResponse.

        工作流的URN。

        :return: The graph_urn of this ShowWorkflowInfoResponse.
        :rtype: str
        """
        return self._graph_urn

    @graph_urn.setter
    def graph_urn(self, graph_urn):
        """Sets the graph_urn of this ShowWorkflowInfoResponse.

        工作流的URN。

        :param graph_urn: The graph_urn of this ShowWorkflowInfoResponse.
        :type graph_urn: str
        """
        self._graph_urn = graph_urn

    @property
    def description(self):
        """Gets the description of this ShowWorkflowInfoResponse.

        工作流的描述。

        :return: The description of this ShowWorkflowInfoResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowWorkflowInfoResponse.

        工作流的描述。

        :param description: The description of this ShowWorkflowInfoResponse.
        :type description: str
        """
        self._description = description

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowWorkflowInfoResponse.

        :return: The x_request_id of this ShowWorkflowInfoResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowWorkflowInfoResponse.

        :param x_request_id: The x_request_id of this ShowWorkflowInfoResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def connection(self):
        """Gets the connection of this ShowWorkflowInfoResponse.

        :return: The connection of this ShowWorkflowInfoResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this ShowWorkflowInfoResponse.

        :param connection: The connection of this ShowWorkflowInfoResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        """Gets the content_length of this ShowWorkflowInfoResponse.

        :return: The content_length of this ShowWorkflowInfoResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this ShowWorkflowInfoResponse.

        :param content_length: The content_length of this ShowWorkflowInfoResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        """Gets the date of this ShowWorkflowInfoResponse.

        :return: The date of this ShowWorkflowInfoResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ShowWorkflowInfoResponse.

        :param date: The date of this ShowWorkflowInfoResponse.
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
        if not isinstance(other, ShowWorkflowInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
