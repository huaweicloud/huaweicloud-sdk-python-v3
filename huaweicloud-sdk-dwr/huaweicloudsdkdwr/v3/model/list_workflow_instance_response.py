# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowInstanceResponse(SdkResponse):

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
        'executions': 'list[Execution]',
        'is_truncated': 'bool',
        'next_offset': 'int',
        'x_request_id': 'str',
        'content_length': 'str',
        'date': 'str',
        'content_type': 'str'
    }

    attribute_map = {
        'count': 'count',
        'executions': 'executions',
        'is_truncated': 'is_truncated',
        'next_offset': 'next_offset',
        'x_request_id': 'X-Request-Id',
        'content_length': 'Content-Length',
        'date': 'Date',
        'content_type': 'Content-Type'
    }

    def __init__(self, count=None, executions=None, is_truncated=None, next_offset=None, x_request_id=None, content_length=None, date=None, content_type=None):
        """ListWorkflowInstanceResponse

        The model defined in huaweicloud sdk

        :param count: 满足条件的运行实例个数。
        :type count: int
        :param executions: 实例信息列表
        :type executions: list[:class:`huaweicloudsdkdwr.v3.Execution`]
        :param is_truncated: 表明是否本次返回的结果列表被截断。true：表示本次没有返回全部结果。false：表示本次已经返回了全部结果。
        :type is_truncated: bool
        :param next_offset: 如果本次没有返回全部结果，响应请求中将包含此字段，用于标明本次请求列举到的最后一个工作流实例。后续请求可以指定Marker等于该值来列举剩余的工作流实例。如果is_truncated为false，该字段不会返回。
        :type next_offset: int
        :param x_request_id: 
        :type x_request_id: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        :param content_type: 
        :type content_type: str
        """
        
        super(ListWorkflowInstanceResponse, self).__init__()

        self._count = None
        self._executions = None
        self._is_truncated = None
        self._next_offset = None
        self._x_request_id = None
        self._content_length = None
        self._date = None
        self._content_type = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if executions is not None:
            self.executions = executions
        if is_truncated is not None:
            self.is_truncated = is_truncated
        if next_offset is not None:
            self.next_offset = next_offset
        if x_request_id is not None:
            self.x_request_id = x_request_id
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date
        if content_type is not None:
            self.content_type = content_type

    @property
    def count(self):
        """Gets the count of this ListWorkflowInstanceResponse.

        满足条件的运行实例个数。

        :return: The count of this ListWorkflowInstanceResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListWorkflowInstanceResponse.

        满足条件的运行实例个数。

        :param count: The count of this ListWorkflowInstanceResponse.
        :type count: int
        """
        self._count = count

    @property
    def executions(self):
        """Gets the executions of this ListWorkflowInstanceResponse.

        实例信息列表

        :return: The executions of this ListWorkflowInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdwr.v3.Execution`]
        """
        return self._executions

    @executions.setter
    def executions(self, executions):
        """Sets the executions of this ListWorkflowInstanceResponse.

        实例信息列表

        :param executions: The executions of this ListWorkflowInstanceResponse.
        :type executions: list[:class:`huaweicloudsdkdwr.v3.Execution`]
        """
        self._executions = executions

    @property
    def is_truncated(self):
        """Gets the is_truncated of this ListWorkflowInstanceResponse.

        表明是否本次返回的结果列表被截断。true：表示本次没有返回全部结果。false：表示本次已经返回了全部结果。

        :return: The is_truncated of this ListWorkflowInstanceResponse.
        :rtype: bool
        """
        return self._is_truncated

    @is_truncated.setter
    def is_truncated(self, is_truncated):
        """Sets the is_truncated of this ListWorkflowInstanceResponse.

        表明是否本次返回的结果列表被截断。true：表示本次没有返回全部结果。false：表示本次已经返回了全部结果。

        :param is_truncated: The is_truncated of this ListWorkflowInstanceResponse.
        :type is_truncated: bool
        """
        self._is_truncated = is_truncated

    @property
    def next_offset(self):
        """Gets the next_offset of this ListWorkflowInstanceResponse.

        如果本次没有返回全部结果，响应请求中将包含此字段，用于标明本次请求列举到的最后一个工作流实例。后续请求可以指定Marker等于该值来列举剩余的工作流实例。如果is_truncated为false，该字段不会返回。

        :return: The next_offset of this ListWorkflowInstanceResponse.
        :rtype: int
        """
        return self._next_offset

    @next_offset.setter
    def next_offset(self, next_offset):
        """Sets the next_offset of this ListWorkflowInstanceResponse.

        如果本次没有返回全部结果，响应请求中将包含此字段，用于标明本次请求列举到的最后一个工作流实例。后续请求可以指定Marker等于该值来列举剩余的工作流实例。如果is_truncated为false，该字段不会返回。

        :param next_offset: The next_offset of this ListWorkflowInstanceResponse.
        :type next_offset: int
        """
        self._next_offset = next_offset

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListWorkflowInstanceResponse.

        :return: The x_request_id of this ListWorkflowInstanceResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListWorkflowInstanceResponse.

        :param x_request_id: The x_request_id of this ListWorkflowInstanceResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def content_length(self):
        """Gets the content_length of this ListWorkflowInstanceResponse.

        :return: The content_length of this ListWorkflowInstanceResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this ListWorkflowInstanceResponse.

        :param content_length: The content_length of this ListWorkflowInstanceResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        """Gets the date of this ListWorkflowInstanceResponse.

        :return: The date of this ListWorkflowInstanceResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ListWorkflowInstanceResponse.

        :param date: The date of this ListWorkflowInstanceResponse.
        :type date: str
        """
        self._date = date

    @property
    def content_type(self):
        """Gets the content_type of this ListWorkflowInstanceResponse.

        :return: The content_type of this ListWorkflowInstanceResponse.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ListWorkflowInstanceResponse.

        :param content_type: The content_type of this ListWorkflowInstanceResponse.
        :type content_type: str
        """
        self._content_type = content_type

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
        if not isinstance(other, ListWorkflowInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
