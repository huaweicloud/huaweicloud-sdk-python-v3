# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProgressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'name': 'str',
        'total': 'int',
        'completed': 'bool',
        'cancelled': 'bool',
        'informations': 'list[str]',
        'code': 'str',
        'reason': 'str',
        'submitted_time': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'server_ip': 'str',
        'last_modified_time': 'int',
        'finished_count': 'int',
        'return_value': 'object',
        'exception_message': 'str',
        'line_up_num': 'int',
        'asyn_operation_key': 'str',
        'is_ended': 'bool',
        'finished_percent': 'int'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'total': 'total',
        'completed': 'completed',
        'cancelled': 'cancelled',
        'informations': 'informations',
        'code': 'code',
        'reason': 'reason',
        'submitted_time': 'submitted_time',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'server_ip': 'server_ip',
        'last_modified_time': 'last_modified_time',
        'finished_count': 'finished_count',
        'return_value': 'return_value',
        'exception_message': 'exception_message',
        'line_up_num': 'line_up_num',
        'asyn_operation_key': 'asyn_operation_key',
        'is_ended': 'is_ended',
        'finished_percent': 'finished_percent'
    }

    def __init__(self, uri=None, name=None, total=None, completed=None, cancelled=None, informations=None, code=None, reason=None, submitted_time=None, begin_time=None, end_time=None, server_ip=None, last_modified_time=None, finished_count=None, return_value=None, exception_message=None, line_up_num=None, asyn_operation_key=None, is_ended=None, finished_percent=None):
        """ShowProgressResponse

        The model defined in huaweicloud sdk

        :param uri: 进度uri
        :type uri: str
        :param name: 异步进度名称
        :type name: str
        :param total: 资源总数
        :type total: int
        :param completed: 异步操作是否完成
        :type completed: bool
        :param cancelled: 异步操作是否取消
        :type cancelled: bool
        :param informations: 提示信息列表
        :type informations: list[str]
        :param code: 错误编码
        :type code: str
        :param reason: 错误信息
        :type reason: str
        :param submitted_time: 提交时间
        :type submitted_time: str
        :param begin_time: 开始时间
        :type begin_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param server_ip: 服务ip
        :type server_ip: str
        :param last_modified_time: 最后修改时间
        :type last_modified_time: int
        :param finished_count: 执行完成总数
        :type finished_count: int
        :param return_value: 异步操作返回值
        :type return_value: object
        :param exception_message: 异常信息
        :type exception_message: str
        :param line_up_num: 行编号
        :type line_up_num: int
        :param asyn_operation_key: 异步操作的key
        :type asyn_operation_key: str
        :param is_ended: 是否结束
        :type is_ended: bool
        :param finished_percent: 异步操作完成进度
        :type finished_percent: int
        """
        
        super(ShowProgressResponse, self).__init__()

        self._uri = None
        self._name = None
        self._total = None
        self._completed = None
        self._cancelled = None
        self._informations = None
        self._code = None
        self._reason = None
        self._submitted_time = None
        self._begin_time = None
        self._end_time = None
        self._server_ip = None
        self._last_modified_time = None
        self._finished_count = None
        self._return_value = None
        self._exception_message = None
        self._line_up_num = None
        self._asyn_operation_key = None
        self._is_ended = None
        self._finished_percent = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if total is not None:
            self.total = total
        if completed is not None:
            self.completed = completed
        if cancelled is not None:
            self.cancelled = cancelled
        if informations is not None:
            self.informations = informations
        if code is not None:
            self.code = code
        if reason is not None:
            self.reason = reason
        if submitted_time is not None:
            self.submitted_time = submitted_time
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if server_ip is not None:
            self.server_ip = server_ip
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if finished_count is not None:
            self.finished_count = finished_count
        if return_value is not None:
            self.return_value = return_value
        if exception_message is not None:
            self.exception_message = exception_message
        if line_up_num is not None:
            self.line_up_num = line_up_num
        if asyn_operation_key is not None:
            self.asyn_operation_key = asyn_operation_key
        if is_ended is not None:
            self.is_ended = is_ended
        if finished_percent is not None:
            self.finished_percent = finished_percent

    @property
    def uri(self):
        """Gets the uri of this ShowProgressResponse.

        进度uri

        :return: The uri of this ShowProgressResponse.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ShowProgressResponse.

        进度uri

        :param uri: The uri of this ShowProgressResponse.
        :type uri: str
        """
        self._uri = uri

    @property
    def name(self):
        """Gets the name of this ShowProgressResponse.

        异步进度名称

        :return: The name of this ShowProgressResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowProgressResponse.

        异步进度名称

        :param name: The name of this ShowProgressResponse.
        :type name: str
        """
        self._name = name

    @property
    def total(self):
        """Gets the total of this ShowProgressResponse.

        资源总数

        :return: The total of this ShowProgressResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowProgressResponse.

        资源总数

        :param total: The total of this ShowProgressResponse.
        :type total: int
        """
        self._total = total

    @property
    def completed(self):
        """Gets the completed of this ShowProgressResponse.

        异步操作是否完成

        :return: The completed of this ShowProgressResponse.
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this ShowProgressResponse.

        异步操作是否完成

        :param completed: The completed of this ShowProgressResponse.
        :type completed: bool
        """
        self._completed = completed

    @property
    def cancelled(self):
        """Gets the cancelled of this ShowProgressResponse.

        异步操作是否取消

        :return: The cancelled of this ShowProgressResponse.
        :rtype: bool
        """
        return self._cancelled

    @cancelled.setter
    def cancelled(self, cancelled):
        """Sets the cancelled of this ShowProgressResponse.

        异步操作是否取消

        :param cancelled: The cancelled of this ShowProgressResponse.
        :type cancelled: bool
        """
        self._cancelled = cancelled

    @property
    def informations(self):
        """Gets the informations of this ShowProgressResponse.

        提示信息列表

        :return: The informations of this ShowProgressResponse.
        :rtype: list[str]
        """
        return self._informations

    @informations.setter
    def informations(self, informations):
        """Sets the informations of this ShowProgressResponse.

        提示信息列表

        :param informations: The informations of this ShowProgressResponse.
        :type informations: list[str]
        """
        self._informations = informations

    @property
    def code(self):
        """Gets the code of this ShowProgressResponse.

        错误编码

        :return: The code of this ShowProgressResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ShowProgressResponse.

        错误编码

        :param code: The code of this ShowProgressResponse.
        :type code: str
        """
        self._code = code

    @property
    def reason(self):
        """Gets the reason of this ShowProgressResponse.

        错误信息

        :return: The reason of this ShowProgressResponse.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ShowProgressResponse.

        错误信息

        :param reason: The reason of this ShowProgressResponse.
        :type reason: str
        """
        self._reason = reason

    @property
    def submitted_time(self):
        """Gets the submitted_time of this ShowProgressResponse.

        提交时间

        :return: The submitted_time of this ShowProgressResponse.
        :rtype: str
        """
        return self._submitted_time

    @submitted_time.setter
    def submitted_time(self, submitted_time):
        """Sets the submitted_time of this ShowProgressResponse.

        提交时间

        :param submitted_time: The submitted_time of this ShowProgressResponse.
        :type submitted_time: str
        """
        self._submitted_time = submitted_time

    @property
    def begin_time(self):
        """Gets the begin_time of this ShowProgressResponse.

        开始时间

        :return: The begin_time of this ShowProgressResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ShowProgressResponse.

        开始时间

        :param begin_time: The begin_time of this ShowProgressResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowProgressResponse.

        结束时间

        :return: The end_time of this ShowProgressResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowProgressResponse.

        结束时间

        :param end_time: The end_time of this ShowProgressResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def server_ip(self):
        """Gets the server_ip of this ShowProgressResponse.

        服务ip

        :return: The server_ip of this ShowProgressResponse.
        :rtype: str
        """
        return self._server_ip

    @server_ip.setter
    def server_ip(self, server_ip):
        """Sets the server_ip of this ShowProgressResponse.

        服务ip

        :param server_ip: The server_ip of this ShowProgressResponse.
        :type server_ip: str
        """
        self._server_ip = server_ip

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this ShowProgressResponse.

        最后修改时间

        :return: The last_modified_time of this ShowProgressResponse.
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this ShowProgressResponse.

        最后修改时间

        :param last_modified_time: The last_modified_time of this ShowProgressResponse.
        :type last_modified_time: int
        """
        self._last_modified_time = last_modified_time

    @property
    def finished_count(self):
        """Gets the finished_count of this ShowProgressResponse.

        执行完成总数

        :return: The finished_count of this ShowProgressResponse.
        :rtype: int
        """
        return self._finished_count

    @finished_count.setter
    def finished_count(self, finished_count):
        """Sets the finished_count of this ShowProgressResponse.

        执行完成总数

        :param finished_count: The finished_count of this ShowProgressResponse.
        :type finished_count: int
        """
        self._finished_count = finished_count

    @property
    def return_value(self):
        """Gets the return_value of this ShowProgressResponse.

        异步操作返回值

        :return: The return_value of this ShowProgressResponse.
        :rtype: object
        """
        return self._return_value

    @return_value.setter
    def return_value(self, return_value):
        """Sets the return_value of this ShowProgressResponse.

        异步操作返回值

        :param return_value: The return_value of this ShowProgressResponse.
        :type return_value: object
        """
        self._return_value = return_value

    @property
    def exception_message(self):
        """Gets the exception_message of this ShowProgressResponse.

        异常信息

        :return: The exception_message of this ShowProgressResponse.
        :rtype: str
        """
        return self._exception_message

    @exception_message.setter
    def exception_message(self, exception_message):
        """Sets the exception_message of this ShowProgressResponse.

        异常信息

        :param exception_message: The exception_message of this ShowProgressResponse.
        :type exception_message: str
        """
        self._exception_message = exception_message

    @property
    def line_up_num(self):
        """Gets the line_up_num of this ShowProgressResponse.

        行编号

        :return: The line_up_num of this ShowProgressResponse.
        :rtype: int
        """
        return self._line_up_num

    @line_up_num.setter
    def line_up_num(self, line_up_num):
        """Sets the line_up_num of this ShowProgressResponse.

        行编号

        :param line_up_num: The line_up_num of this ShowProgressResponse.
        :type line_up_num: int
        """
        self._line_up_num = line_up_num

    @property
    def asyn_operation_key(self):
        """Gets the asyn_operation_key of this ShowProgressResponse.

        异步操作的key

        :return: The asyn_operation_key of this ShowProgressResponse.
        :rtype: str
        """
        return self._asyn_operation_key

    @asyn_operation_key.setter
    def asyn_operation_key(self, asyn_operation_key):
        """Sets the asyn_operation_key of this ShowProgressResponse.

        异步操作的key

        :param asyn_operation_key: The asyn_operation_key of this ShowProgressResponse.
        :type asyn_operation_key: str
        """
        self._asyn_operation_key = asyn_operation_key

    @property
    def is_ended(self):
        """Gets the is_ended of this ShowProgressResponse.

        是否结束

        :return: The is_ended of this ShowProgressResponse.
        :rtype: bool
        """
        return self._is_ended

    @is_ended.setter
    def is_ended(self, is_ended):
        """Sets the is_ended of this ShowProgressResponse.

        是否结束

        :param is_ended: The is_ended of this ShowProgressResponse.
        :type is_ended: bool
        """
        self._is_ended = is_ended

    @property
    def finished_percent(self):
        """Gets the finished_percent of this ShowProgressResponse.

        异步操作完成进度

        :return: The finished_percent of this ShowProgressResponse.
        :rtype: int
        """
        return self._finished_percent

    @finished_percent.setter
    def finished_percent(self, finished_percent):
        """Sets the finished_percent of this ShowProgressResponse.

        异步操作完成进度

        :param finished_percent: The finished_percent of this ShowProgressResponse.
        :type finished_percent: int
        """
        self._finished_percent = finished_percent

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
        if not isinstance(other, ShowProgressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
