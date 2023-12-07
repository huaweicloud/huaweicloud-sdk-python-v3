# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ControlOperation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'control_operate_request_id': 'str',
        'operation_type': 'str',
        'status': 'str',
        'message': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'control_operate_request_id': 'control_operate_request_id',
        'operation_type': 'operation_type',
        'status': 'status',
        'message': 'message',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, control_operate_request_id=None, operation_type=None, status=None, message=None, start_time=None, end_time=None):
        """ControlOperation

        The model defined in huaweicloud sdk

        :param control_operate_request_id: 本次操作控制策略的ID。
        :type control_operate_request_id: str
        :param operation_type: 操作类型，启用控制策略或禁用控制策略。
        :type operation_type: str
        :param status: 控制策略实施的状态 SUCCEEDED | FAILED | IN_PROGRESS。
        :type status: str
        :param message: 控制策略实施失败的错误信息。
        :type message: str
        :param start_time: 操作开始的时间。
        :type start_time: str
        :param end_time: 操作结束的时间。
        :type end_time: str
        """
        
        

        self._control_operate_request_id = None
        self._operation_type = None
        self._status = None
        self._message = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if control_operate_request_id is not None:
            self.control_operate_request_id = control_operate_request_id
        if operation_type is not None:
            self.operation_type = operation_type
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def control_operate_request_id(self):
        """Gets the control_operate_request_id of this ControlOperation.

        本次操作控制策略的ID。

        :return: The control_operate_request_id of this ControlOperation.
        :rtype: str
        """
        return self._control_operate_request_id

    @control_operate_request_id.setter
    def control_operate_request_id(self, control_operate_request_id):
        """Sets the control_operate_request_id of this ControlOperation.

        本次操作控制策略的ID。

        :param control_operate_request_id: The control_operate_request_id of this ControlOperation.
        :type control_operate_request_id: str
        """
        self._control_operate_request_id = control_operate_request_id

    @property
    def operation_type(self):
        """Gets the operation_type of this ControlOperation.

        操作类型，启用控制策略或禁用控制策略。

        :return: The operation_type of this ControlOperation.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this ControlOperation.

        操作类型，启用控制策略或禁用控制策略。

        :param operation_type: The operation_type of this ControlOperation.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def status(self):
        """Gets the status of this ControlOperation.

        控制策略实施的状态 SUCCEEDED | FAILED | IN_PROGRESS。

        :return: The status of this ControlOperation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ControlOperation.

        控制策略实施的状态 SUCCEEDED | FAILED | IN_PROGRESS。

        :param status: The status of this ControlOperation.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        """Gets the message of this ControlOperation.

        控制策略实施失败的错误信息。

        :return: The message of this ControlOperation.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ControlOperation.

        控制策略实施失败的错误信息。

        :param message: The message of this ControlOperation.
        :type message: str
        """
        self._message = message

    @property
    def start_time(self):
        """Gets the start_time of this ControlOperation.

        操作开始的时间。

        :return: The start_time of this ControlOperation.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ControlOperation.

        操作开始的时间。

        :param start_time: The start_time of this ControlOperation.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ControlOperation.

        操作结束的时间。

        :return: The end_time of this ControlOperation.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ControlOperation.

        操作结束的时间。

        :param end_time: The end_time of this ControlOperation.
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
        if not isinstance(other, ControlOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
