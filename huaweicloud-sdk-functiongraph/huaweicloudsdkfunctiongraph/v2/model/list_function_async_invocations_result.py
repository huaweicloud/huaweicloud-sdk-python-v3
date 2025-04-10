# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionAsyncInvocationsResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'status': 'str',
        'error_message': 'str',
        'error_code': 'int',
        'start_time': 'datetime',
        'end_time': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'status': 'status',
        'error_message': 'error_message',
        'error_code': 'error_code',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, request_id=None, status=None, error_message=None, error_code=None, start_time=None, end_time=None):
        r"""ListFunctionAsyncInvocationsResult

        The model defined in huaweicloud sdk

        :param request_id: 异步调用请求ID
        :type request_id: str
        :param status: 异步调用状态，支持5种状态 WAIT: 等待 RUNNING: 执行中 SUCCESS: 执行成功 FAIL: 执行失败 DISCARD: 请求丢弃
        :type status: str
        :param error_message: 异步调用错误信息，如果执行成功，则返回空
        :type error_message: str
        :param error_code: 异步调用错误码，如果执行成功，则返回0
        :type error_code: int
        :param start_time: 异步调用开始时间（格式为YYYY-MM-DD&#39;T&#39;HH:mm:ss,UTC时间）。
        :type start_time: datetime
        :param end_time: 异步调用结束时间（格式为YYYY-MM-DD&#39;T&#39;HH:mm:ss,UTC时间）。
        :type end_time: str
        """
        
        

        self._request_id = None
        self._status = None
        self._error_message = None
        self._error_code = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if status is not None:
            self.status = status
        if error_message is not None:
            self.error_message = error_message
        if error_code is not None:
            self.error_code = error_code
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def request_id(self):
        r"""Gets the request_id of this ListFunctionAsyncInvocationsResult.

        异步调用请求ID

        :return: The request_id of this ListFunctionAsyncInvocationsResult.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListFunctionAsyncInvocationsResult.

        异步调用请求ID

        :param request_id: The request_id of this ListFunctionAsyncInvocationsResult.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def status(self):
        r"""Gets the status of this ListFunctionAsyncInvocationsResult.

        异步调用状态，支持5种状态 WAIT: 等待 RUNNING: 执行中 SUCCESS: 执行成功 FAIL: 执行失败 DISCARD: 请求丢弃

        :return: The status of this ListFunctionAsyncInvocationsResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListFunctionAsyncInvocationsResult.

        异步调用状态，支持5种状态 WAIT: 等待 RUNNING: 执行中 SUCCESS: 执行成功 FAIL: 执行失败 DISCARD: 请求丢弃

        :param status: The status of this ListFunctionAsyncInvocationsResult.
        :type status: str
        """
        self._status = status

    @property
    def error_message(self):
        r"""Gets the error_message of this ListFunctionAsyncInvocationsResult.

        异步调用错误信息，如果执行成功，则返回空

        :return: The error_message of this ListFunctionAsyncInvocationsResult.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this ListFunctionAsyncInvocationsResult.

        异步调用错误信息，如果执行成功，则返回空

        :param error_message: The error_message of this ListFunctionAsyncInvocationsResult.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def error_code(self):
        r"""Gets the error_code of this ListFunctionAsyncInvocationsResult.

        异步调用错误码，如果执行成功，则返回0

        :return: The error_code of this ListFunctionAsyncInvocationsResult.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ListFunctionAsyncInvocationsResult.

        异步调用错误码，如果执行成功，则返回0

        :param error_code: The error_code of this ListFunctionAsyncInvocationsResult.
        :type error_code: int
        """
        self._error_code = error_code

    @property
    def start_time(self):
        r"""Gets the start_time of this ListFunctionAsyncInvocationsResult.

        异步调用开始时间（格式为YYYY-MM-DD'T'HH:mm:ss,UTC时间）。

        :return: The start_time of this ListFunctionAsyncInvocationsResult.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListFunctionAsyncInvocationsResult.

        异步调用开始时间（格式为YYYY-MM-DD'T'HH:mm:ss,UTC时间）。

        :param start_time: The start_time of this ListFunctionAsyncInvocationsResult.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListFunctionAsyncInvocationsResult.

        异步调用结束时间（格式为YYYY-MM-DD'T'HH:mm:ss,UTC时间）。

        :return: The end_time of this ListFunctionAsyncInvocationsResult.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListFunctionAsyncInvocationsResult.

        异步调用结束时间（格式为YYYY-MM-DD'T'HH:mm:ss,UTC时间）。

        :param end_time: The end_time of this ListFunctionAsyncInvocationsResult.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListFunctionAsyncInvocationsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
