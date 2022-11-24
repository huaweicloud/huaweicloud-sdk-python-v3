# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeExecution:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'input': 'object',
        'output': 'object',
        'begin_time': 'int',
        'end_time': 'int',
        'error_message': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'input': 'input',
        'output': 'output',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'error_message': 'error_message',
        'request_id': 'request_id'
    }

    def __init__(self, status=None, input=None, output=None, begin_time=None, end_time=None, error_message=None, request_id=None):
        """NodeExecution

        The model defined in huaweicloud sdk

        :param status: 流程节点执行状态  最小长度：1  最大长度：32  枚举值：  success  fail  running  timeout  cancel
        :type status: str
        :param input: 函数执行时的入参
        :type input: object
        :param output: 函数执行结果
        :type output: object
        :param begin_time: 节点启动时间，UTC毫秒时间戳格式  最小值：0  最大值：99999999999999999
        :type begin_time: int
        :param end_time: 节点结束时间，UTC毫秒时间戳格式  最小值：0  最大值：99999999999999999
        :type end_time: int
        :param error_message: 节点错误信息，仅在节点出错时非空
        :type error_message: str
        :param request_id: 流程节点请求ID
        :type request_id: str
        """
        
        

        self._status = None
        self._input = None
        self._output = None
        self._begin_time = None
        self._end_time = None
        self._error_message = None
        self._request_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if error_message is not None:
            self.error_message = error_message
        if request_id is not None:
            self.request_id = request_id

    @property
    def status(self):
        """Gets the status of this NodeExecution.

        流程节点执行状态  最小长度：1  最大长度：32  枚举值：  success  fail  running  timeout  cancel

        :return: The status of this NodeExecution.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeExecution.

        流程节点执行状态  最小长度：1  最大长度：32  枚举值：  success  fail  running  timeout  cancel

        :param status: The status of this NodeExecution.
        :type status: str
        """
        self._status = status

    @property
    def input(self):
        """Gets the input of this NodeExecution.

        函数执行时的入参

        :return: The input of this NodeExecution.
        :rtype: object
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this NodeExecution.

        函数执行时的入参

        :param input: The input of this NodeExecution.
        :type input: object
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this NodeExecution.

        函数执行结果

        :return: The output of this NodeExecution.
        :rtype: object
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this NodeExecution.

        函数执行结果

        :param output: The output of this NodeExecution.
        :type output: object
        """
        self._output = output

    @property
    def begin_time(self):
        """Gets the begin_time of this NodeExecution.

        节点启动时间，UTC毫秒时间戳格式  最小值：0  最大值：99999999999999999

        :return: The begin_time of this NodeExecution.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this NodeExecution.

        节点启动时间，UTC毫秒时间戳格式  最小值：0  最大值：99999999999999999

        :param begin_time: The begin_time of this NodeExecution.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this NodeExecution.

        节点结束时间，UTC毫秒时间戳格式  最小值：0  最大值：99999999999999999

        :return: The end_time of this NodeExecution.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this NodeExecution.

        节点结束时间，UTC毫秒时间戳格式  最小值：0  最大值：99999999999999999

        :param end_time: The end_time of this NodeExecution.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def error_message(self):
        """Gets the error_message of this NodeExecution.

        节点错误信息，仅在节点出错时非空

        :return: The error_message of this NodeExecution.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this NodeExecution.

        节点错误信息，仅在节点出错时非空

        :param error_message: The error_message of this NodeExecution.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def request_id(self):
        """Gets the request_id of this NodeExecution.

        流程节点请求ID

        :return: The request_id of this NodeExecution.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this NodeExecution.

        流程节点请求ID

        :param request_id: The request_id of this NodeExecution.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, NodeExecution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
