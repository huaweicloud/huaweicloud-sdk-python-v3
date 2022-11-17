# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStackOutputsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_request_id': 'str',
        'stack_name': 'str',
        'stack_id': 'str',
        'executor': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'client_request_id': 'Client-Request-Id',
        'stack_name': 'stack_name',
        'stack_id': 'stack_id',
        'executor': 'executor',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, client_request_id=None, stack_name=None, stack_id=None, executor=None, limit=None, marker=None):
        """ListStackOutputsRequest

        The model defined in huaweicloud sdk

        :param client_request_id: 用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID
        :type client_request_id: str
        :param stack_name: 用户希望操作的资源栈名
        :type stack_name: str
        :param stack_id: 用户希望描述的栈的Id。若stack_name和stack_id同时存在，则IaC会检查是否两个匹配，否则返回400
        :type stack_id: str
        :param executor: 执行操作者的名字，将用做未来的审计工作。
        :type executor: str
        :param limit: 分页limit
        :type limit: int
        :param marker: 当一页无法发回所有的细节，上一次的请求将返回next_marker以指引还有更多页数，客户可以将next_marker中的值放到此处以查询下一页的信息。
        :type marker: str
        """
        
        

        self._client_request_id = None
        self._stack_name = None
        self._stack_id = None
        self._executor = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.client_request_id = client_request_id
        self.stack_name = stack_name
        if stack_id is not None:
            self.stack_id = stack_id
        if executor is not None:
            self.executor = executor
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def client_request_id(self):
        """Gets the client_request_id of this ListStackOutputsRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :return: The client_request_id of this ListStackOutputsRequest.
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this ListStackOutputsRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :param client_request_id: The client_request_id of this ListStackOutputsRequest.
        :type client_request_id: str
        """
        self._client_request_id = client_request_id

    @property
    def stack_name(self):
        """Gets the stack_name of this ListStackOutputsRequest.

        用户希望操作的资源栈名

        :return: The stack_name of this ListStackOutputsRequest.
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        """Sets the stack_name of this ListStackOutputsRequest.

        用户希望操作的资源栈名

        :param stack_name: The stack_name of this ListStackOutputsRequest.
        :type stack_name: str
        """
        self._stack_name = stack_name

    @property
    def stack_id(self):
        """Gets the stack_id of this ListStackOutputsRequest.

        用户希望描述的栈的Id。若stack_name和stack_id同时存在，则IaC会检查是否两个匹配，否则返回400

        :return: The stack_id of this ListStackOutputsRequest.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this ListStackOutputsRequest.

        用户希望描述的栈的Id。若stack_name和stack_id同时存在，则IaC会检查是否两个匹配，否则返回400

        :param stack_id: The stack_id of this ListStackOutputsRequest.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def executor(self):
        """Gets the executor of this ListStackOutputsRequest.

        执行操作者的名字，将用做未来的审计工作。

        :return: The executor of this ListStackOutputsRequest.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        """Sets the executor of this ListStackOutputsRequest.

        执行操作者的名字，将用做未来的审计工作。

        :param executor: The executor of this ListStackOutputsRequest.
        :type executor: str
        """
        self._executor = executor

    @property
    def limit(self):
        """Gets the limit of this ListStackOutputsRequest.

        分页limit

        :return: The limit of this ListStackOutputsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListStackOutputsRequest.

        分页limit

        :param limit: The limit of this ListStackOutputsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListStackOutputsRequest.

        当一页无法发回所有的细节，上一次的请求将返回next_marker以指引还有更多页数，客户可以将next_marker中的值放到此处以查询下一页的信息。

        :return: The marker of this ListStackOutputsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListStackOutputsRequest.

        当一页无法发回所有的细节，上一次的请求将返回next_marker以指引还有更多页数，客户可以将next_marker中的值放到此处以查询下一页的信息。

        :param marker: The marker of this ListStackOutputsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListStackOutputsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
