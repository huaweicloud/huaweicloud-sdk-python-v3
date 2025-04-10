# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleTaskExecuteDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'execute_id': 'str',
        'server_id': 'str',
        'server_name': 'str',
        'status': 'ScheduleTaskStatus',
        'task_type': 'ScheduleTaskTypeEnum',
        'time_zone': 'str',
        'begin_time': 'datetime',
        'end_time': 'datetime',
        'result_code': 'str',
        'result_message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'execute_id': 'execute_id',
        'server_id': 'server_id',
        'server_name': 'server_name',
        'status': 'status',
        'task_type': 'task_type',
        'time_zone': 'time_zone',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'result_code': 'result_code',
        'result_message': 'result_message'
    }

    def __init__(self, id=None, execute_id=None, server_id=None, server_name=None, status=None, task_type=None, time_zone=None, begin_time=None, end_time=None, result_code=None, result_message=None):
        r"""ScheduleTaskExecuteDetail

        The model defined in huaweicloud sdk

        :param id: 定时任务执行记录主键id。
        :type id: str
        :param execute_id: 主任务记录id。
        :type execute_id: str
        :param server_id: 操作的server_id。
        :type server_id: str
        :param server_name: 操作的机器名称。
        :type server_name: str
        :param status: 
        :type status: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskStatus`
        :param task_type: 
        :type task_type: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskTypeEnum`
        :param time_zone: 时区。
        :type time_zone: str
        :param begin_time: 子任务开始时间。
        :type begin_time: datetime
        :param end_time: 子任务结束时间。
        :type end_time: datetime
        :param result_code: 任务执行失败时的错误码。
        :type result_code: str
        :param result_message: 任务失败原因。
        :type result_message: str
        """
        
        

        self._id = None
        self._execute_id = None
        self._server_id = None
        self._server_name = None
        self._status = None
        self._task_type = None
        self._time_zone = None
        self._begin_time = None
        self._end_time = None
        self._result_code = None
        self._result_message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if execute_id is not None:
            self.execute_id = execute_id
        if server_id is not None:
            self.server_id = server_id
        if server_name is not None:
            self.server_name = server_name
        if status is not None:
            self.status = status
        if task_type is not None:
            self.task_type = task_type
        if time_zone is not None:
            self.time_zone = time_zone
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if result_code is not None:
            self.result_code = result_code
        if result_message is not None:
            self.result_message = result_message

    @property
    def id(self):
        r"""Gets the id of this ScheduleTaskExecuteDetail.

        定时任务执行记录主键id。

        :return: The id of this ScheduleTaskExecuteDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScheduleTaskExecuteDetail.

        定时任务执行记录主键id。

        :param id: The id of this ScheduleTaskExecuteDetail.
        :type id: str
        """
        self._id = id

    @property
    def execute_id(self):
        r"""Gets the execute_id of this ScheduleTaskExecuteDetail.

        主任务记录id。

        :return: The execute_id of this ScheduleTaskExecuteDetail.
        :rtype: str
        """
        return self._execute_id

    @execute_id.setter
    def execute_id(self, execute_id):
        r"""Sets the execute_id of this ScheduleTaskExecuteDetail.

        主任务记录id。

        :param execute_id: The execute_id of this ScheduleTaskExecuteDetail.
        :type execute_id: str
        """
        self._execute_id = execute_id

    @property
    def server_id(self):
        r"""Gets the server_id of this ScheduleTaskExecuteDetail.

        操作的server_id。

        :return: The server_id of this ScheduleTaskExecuteDetail.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ScheduleTaskExecuteDetail.

        操作的server_id。

        :param server_id: The server_id of this ScheduleTaskExecuteDetail.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def server_name(self):
        r"""Gets the server_name of this ScheduleTaskExecuteDetail.

        操作的机器名称。

        :return: The server_name of this ScheduleTaskExecuteDetail.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        r"""Sets the server_name of this ScheduleTaskExecuteDetail.

        操作的机器名称。

        :param server_name: The server_name of this ScheduleTaskExecuteDetail.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def status(self):
        r"""Gets the status of this ScheduleTaskExecuteDetail.

        :return: The status of this ScheduleTaskExecuteDetail.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScheduleTaskExecuteDetail.

        :param status: The status of this ScheduleTaskExecuteDetail.
        :type status: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskStatus`
        """
        self._status = status

    @property
    def task_type(self):
        r"""Gets the task_type of this ScheduleTaskExecuteDetail.

        :return: The task_type of this ScheduleTaskExecuteDetail.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskTypeEnum`
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ScheduleTaskExecuteDetail.

        :param task_type: The task_type of this ScheduleTaskExecuteDetail.
        :type task_type: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskTypeEnum`
        """
        self._task_type = task_type

    @property
    def time_zone(self):
        r"""Gets the time_zone of this ScheduleTaskExecuteDetail.

        时区。

        :return: The time_zone of this ScheduleTaskExecuteDetail.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this ScheduleTaskExecuteDetail.

        时区。

        :param time_zone: The time_zone of this ScheduleTaskExecuteDetail.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ScheduleTaskExecuteDetail.

        子任务开始时间。

        :return: The begin_time of this ScheduleTaskExecuteDetail.
        :rtype: datetime
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ScheduleTaskExecuteDetail.

        子任务开始时间。

        :param begin_time: The begin_time of this ScheduleTaskExecuteDetail.
        :type begin_time: datetime
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ScheduleTaskExecuteDetail.

        子任务结束时间。

        :return: The end_time of this ScheduleTaskExecuteDetail.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ScheduleTaskExecuteDetail.

        子任务结束时间。

        :param end_time: The end_time of this ScheduleTaskExecuteDetail.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def result_code(self):
        r"""Gets the result_code of this ScheduleTaskExecuteDetail.

        任务执行失败时的错误码。

        :return: The result_code of this ScheduleTaskExecuteDetail.
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        r"""Sets the result_code of this ScheduleTaskExecuteDetail.

        任务执行失败时的错误码。

        :param result_code: The result_code of this ScheduleTaskExecuteDetail.
        :type result_code: str
        """
        self._result_code = result_code

    @property
    def result_message(self):
        r"""Gets the result_message of this ScheduleTaskExecuteDetail.

        任务失败原因。

        :return: The result_message of this ScheduleTaskExecuteDetail.
        :rtype: str
        """
        return self._result_message

    @result_message.setter
    def result_message(self, result_message):
        r"""Sets the result_message of this ScheduleTaskExecuteDetail.

        任务失败原因。

        :param result_message: The result_message of this ScheduleTaskExecuteDetail.
        :type result_message: str
        """
        self._result_message = result_message

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
        if not isinstance(other, ScheduleTaskExecuteDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
