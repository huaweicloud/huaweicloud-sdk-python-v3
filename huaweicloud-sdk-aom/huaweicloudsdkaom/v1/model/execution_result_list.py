# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutionResultList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'begin_time': 'int',
        'end_time': 'int',
        'function_execution_id': 'str',
        'output': 'object',
        'status': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'function_execution_id': 'function_execution_id',
        'output': 'output',
        'status': 'status'
    }

    def __init__(self, node_id=None, begin_time=None, end_time=None, function_execution_id=None, output=None, status=None):
        """ExecutionResultList

        The model defined in huaweicloud sdk

        :param node_id: 流程节点ID。
        :type node_id: str
        :param begin_time: 节点开始执行时间。
        :type begin_time: int
        :param end_time: 节点执行结束时间。
        :type end_time: int
        :param function_execution_id: FunctionGraph的执行id。
        :type function_execution_id: str
        :param output: 节点输出。
        :type output: object
        :param status: 节点状态。
        :type status: str
        """
        
        

        self._node_id = None
        self._begin_time = None
        self._end_time = None
        self._function_execution_id = None
        self._output = None
        self._status = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if function_execution_id is not None:
            self.function_execution_id = function_execution_id
        if output is not None:
            self.output = output
        if status is not None:
            self.status = status

    @property
    def node_id(self):
        """Gets the node_id of this ExecutionResultList.

        流程节点ID。

        :return: The node_id of this ExecutionResultList.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ExecutionResultList.

        流程节点ID。

        :param node_id: The node_id of this ExecutionResultList.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def begin_time(self):
        """Gets the begin_time of this ExecutionResultList.

        节点开始执行时间。

        :return: The begin_time of this ExecutionResultList.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ExecutionResultList.

        节点开始执行时间。

        :param begin_time: The begin_time of this ExecutionResultList.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ExecutionResultList.

        节点执行结束时间。

        :return: The end_time of this ExecutionResultList.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ExecutionResultList.

        节点执行结束时间。

        :param end_time: The end_time of this ExecutionResultList.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def function_execution_id(self):
        """Gets the function_execution_id of this ExecutionResultList.

        FunctionGraph的执行id。

        :return: The function_execution_id of this ExecutionResultList.
        :rtype: str
        """
        return self._function_execution_id

    @function_execution_id.setter
    def function_execution_id(self, function_execution_id):
        """Sets the function_execution_id of this ExecutionResultList.

        FunctionGraph的执行id。

        :param function_execution_id: The function_execution_id of this ExecutionResultList.
        :type function_execution_id: str
        """
        self._function_execution_id = function_execution_id

    @property
    def output(self):
        """Gets the output of this ExecutionResultList.

        节点输出。

        :return: The output of this ExecutionResultList.
        :rtype: object
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this ExecutionResultList.

        节点输出。

        :param output: The output of this ExecutionResultList.
        :type output: object
        """
        self._output = output

    @property
    def status(self):
        """Gets the status of this ExecutionResultList.

        节点状态。

        :return: The status of this ExecutionResultList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExecutionResultList.

        节点状态。

        :param status: The status of this ExecutionResultList.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ExecutionResultList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
