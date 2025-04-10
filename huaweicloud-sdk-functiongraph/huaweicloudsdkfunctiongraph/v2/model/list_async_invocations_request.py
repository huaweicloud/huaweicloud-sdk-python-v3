# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAsyncInvocationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'request_id': 'str',
        'marker': 'str',
        'limit': 'str',
        'status': 'str',
        'query_begin_time': 'datetime',
        'query_end_time': 'datetime'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'request_id': 'request_id',
        'marker': 'marker',
        'limit': 'limit',
        'status': 'status',
        'query_begin_time': 'query_begin_time',
        'query_end_time': 'query_end_time'
    }

    def __init__(self, function_urn=None, request_id=None, marker=None, limit=None, status=None, query_begin_time=None, query_end_time=None):
        r"""ListAsyncInvocationsRequest

        The model defined in huaweicloud sdk

        :param function_urn: 函数的URN，详细解释见FunctionGraph函数模型的描述。
        :type function_urn: str
        :param request_id: 需要查询的异步请求ID。如果不指定，默认查询所有异步调用记录
        :type request_id: str
        :param marker: 本次查询起始位置，默认值0
        :type marker: str
        :param limit: 本次查询最大返回的数据条数，最大值500，默认值100
        :type limit: str
        :param status: 本次查询指定的异步调用状态，支持5种状态，如果不指定，则查询所有状态的调用记录 WAIT: 等待 RUNNING: 执行中 SUCCESS: 执行成功 FAIL: 执行失败 DISCARD: 请求丢弃
        :type status: str
        :param query_begin_time: 搜索起始时间（格式为YYYY-MM-DD&#39;T&#39;HH:mm:ss,UTC时间）。如果不指定默认为当前时间前1小时
        :type query_begin_time: datetime
        :param query_end_time: 搜索结束时间（格式为YYYY-MM-DD&#39;T&#39;HH:mm:ss,UTC时间）。如果不指定默认为当前时间
        :type query_end_time: datetime
        """
        
        

        self._function_urn = None
        self._request_id = None
        self._marker = None
        self._limit = None
        self._status = None
        self._query_begin_time = None
        self._query_end_time = None
        self.discriminator = None

        self.function_urn = function_urn
        if request_id is not None:
            self.request_id = request_id
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status
        if query_begin_time is not None:
            self.query_begin_time = query_begin_time
        if query_end_time is not None:
            self.query_end_time = query_end_time

    @property
    def function_urn(self):
        r"""Gets the function_urn of this ListAsyncInvocationsRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :return: The function_urn of this ListAsyncInvocationsRequest.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        r"""Sets the function_urn of this ListAsyncInvocationsRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :param function_urn: The function_urn of this ListAsyncInvocationsRequest.
        :type function_urn: str
        """
        self._function_urn = function_urn

    @property
    def request_id(self):
        r"""Gets the request_id of this ListAsyncInvocationsRequest.

        需要查询的异步请求ID。如果不指定，默认查询所有异步调用记录

        :return: The request_id of this ListAsyncInvocationsRequest.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListAsyncInvocationsRequest.

        需要查询的异步请求ID。如果不指定，默认查询所有异步调用记录

        :param request_id: The request_id of this ListAsyncInvocationsRequest.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def marker(self):
        r"""Gets the marker of this ListAsyncInvocationsRequest.

        本次查询起始位置，默认值0

        :return: The marker of this ListAsyncInvocationsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAsyncInvocationsRequest.

        本次查询起始位置，默认值0

        :param marker: The marker of this ListAsyncInvocationsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListAsyncInvocationsRequest.

        本次查询最大返回的数据条数，最大值500，默认值100

        :return: The limit of this ListAsyncInvocationsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAsyncInvocationsRequest.

        本次查询最大返回的数据条数，最大值500，默认值100

        :param limit: The limit of this ListAsyncInvocationsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def status(self):
        r"""Gets the status of this ListAsyncInvocationsRequest.

        本次查询指定的异步调用状态，支持5种状态，如果不指定，则查询所有状态的调用记录 WAIT: 等待 RUNNING: 执行中 SUCCESS: 执行成功 FAIL: 执行失败 DISCARD: 请求丢弃

        :return: The status of this ListAsyncInvocationsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAsyncInvocationsRequest.

        本次查询指定的异步调用状态，支持5种状态，如果不指定，则查询所有状态的调用记录 WAIT: 等待 RUNNING: 执行中 SUCCESS: 执行成功 FAIL: 执行失败 DISCARD: 请求丢弃

        :param status: The status of this ListAsyncInvocationsRequest.
        :type status: str
        """
        self._status = status

    @property
    def query_begin_time(self):
        r"""Gets the query_begin_time of this ListAsyncInvocationsRequest.

        搜索起始时间（格式为YYYY-MM-DD'T'HH:mm:ss,UTC时间）。如果不指定默认为当前时间前1小时

        :return: The query_begin_time of this ListAsyncInvocationsRequest.
        :rtype: datetime
        """
        return self._query_begin_time

    @query_begin_time.setter
    def query_begin_time(self, query_begin_time):
        r"""Sets the query_begin_time of this ListAsyncInvocationsRequest.

        搜索起始时间（格式为YYYY-MM-DD'T'HH:mm:ss,UTC时间）。如果不指定默认为当前时间前1小时

        :param query_begin_time: The query_begin_time of this ListAsyncInvocationsRequest.
        :type query_begin_time: datetime
        """
        self._query_begin_time = query_begin_time

    @property
    def query_end_time(self):
        r"""Gets the query_end_time of this ListAsyncInvocationsRequest.

        搜索结束时间（格式为YYYY-MM-DD'T'HH:mm:ss,UTC时间）。如果不指定默认为当前时间

        :return: The query_end_time of this ListAsyncInvocationsRequest.
        :rtype: datetime
        """
        return self._query_end_time

    @query_end_time.setter
    def query_end_time(self, query_end_time):
        r"""Sets the query_end_time of this ListAsyncInvocationsRequest.

        搜索结束时间（格式为YYYY-MM-DD'T'HH:mm:ss,UTC时间）。如果不指定默认为当前时间

        :param query_end_time: The query_end_time of this ListAsyncInvocationsRequest.
        :type query_end_time: datetime
        """
        self._query_end_time = query_end_time

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
        if not isinstance(other, ListAsyncInvocationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
