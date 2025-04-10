# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreWorkflowExecutionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_urn': 'str',
        'restored_at': 'str',
        'execution_name': 'str',
        'x_request_id': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'execution_urn': 'execution_urn',
        'restored_at': 'restored_at',
        'execution_name': 'execution_name',
        'x_request_id': 'x-request-id',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, execution_urn=None, restored_at=None, execution_name=None, x_request_id=None, connection=None, content_length=None, date=None):
        r"""RestoreWorkflowExecutionResponse

        The model defined in huaweicloud sdk

        :param execution_urn: 运行实例的URN。
        :type execution_urn: str
        :param restored_at: 运行实例的恢复启动时间。
        :type restored_at: str
        :param execution_name: 运行实例的名字。
        :type execution_name: str
        :param x_request_id: 
        :type x_request_id: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(RestoreWorkflowExecutionResponse, self).__init__()

        self._execution_urn = None
        self._restored_at = None
        self._execution_name = None
        self._x_request_id = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if execution_urn is not None:
            self.execution_urn = execution_urn
        if restored_at is not None:
            self.restored_at = restored_at
        if execution_name is not None:
            self.execution_name = execution_name
        if x_request_id is not None:
            self.x_request_id = x_request_id
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date

    @property
    def execution_urn(self):
        r"""Gets the execution_urn of this RestoreWorkflowExecutionResponse.

        运行实例的URN。

        :return: The execution_urn of this RestoreWorkflowExecutionResponse.
        :rtype: str
        """
        return self._execution_urn

    @execution_urn.setter
    def execution_urn(self, execution_urn):
        r"""Sets the execution_urn of this RestoreWorkflowExecutionResponse.

        运行实例的URN。

        :param execution_urn: The execution_urn of this RestoreWorkflowExecutionResponse.
        :type execution_urn: str
        """
        self._execution_urn = execution_urn

    @property
    def restored_at(self):
        r"""Gets the restored_at of this RestoreWorkflowExecutionResponse.

        运行实例的恢复启动时间。

        :return: The restored_at of this RestoreWorkflowExecutionResponse.
        :rtype: str
        """
        return self._restored_at

    @restored_at.setter
    def restored_at(self, restored_at):
        r"""Sets the restored_at of this RestoreWorkflowExecutionResponse.

        运行实例的恢复启动时间。

        :param restored_at: The restored_at of this RestoreWorkflowExecutionResponse.
        :type restored_at: str
        """
        self._restored_at = restored_at

    @property
    def execution_name(self):
        r"""Gets the execution_name of this RestoreWorkflowExecutionResponse.

        运行实例的名字。

        :return: The execution_name of this RestoreWorkflowExecutionResponse.
        :rtype: str
        """
        return self._execution_name

    @execution_name.setter
    def execution_name(self, execution_name):
        r"""Sets the execution_name of this RestoreWorkflowExecutionResponse.

        运行实例的名字。

        :param execution_name: The execution_name of this RestoreWorkflowExecutionResponse.
        :type execution_name: str
        """
        self._execution_name = execution_name

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this RestoreWorkflowExecutionResponse.

        :return: The x_request_id of this RestoreWorkflowExecutionResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this RestoreWorkflowExecutionResponse.

        :param x_request_id: The x_request_id of this RestoreWorkflowExecutionResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def connection(self):
        r"""Gets the connection of this RestoreWorkflowExecutionResponse.

        :return: The connection of this RestoreWorkflowExecutionResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this RestoreWorkflowExecutionResponse.

        :param connection: The connection of this RestoreWorkflowExecutionResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        r"""Gets the content_length of this RestoreWorkflowExecutionResponse.

        :return: The content_length of this RestoreWorkflowExecutionResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this RestoreWorkflowExecutionResponse.

        :param content_length: The content_length of this RestoreWorkflowExecutionResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        r"""Gets the date of this RestoreWorkflowExecutionResponse.

        :return: The date of this RestoreWorkflowExecutionResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this RestoreWorkflowExecutionResponse.

        :param date: The date of this RestoreWorkflowExecutionResponse.
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
        if not isinstance(other, RestoreWorkflowExecutionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
