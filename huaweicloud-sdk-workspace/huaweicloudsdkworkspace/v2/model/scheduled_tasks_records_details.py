# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduledTasksRecordsDetails:

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
        'record_id': 'str',
        'desktop_id': 'str',
        'desktop_name': 'str',
        'exec_status': 'str',
        'result_code': 'str',
        'fail_reason': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'record_id': 'record_id',
        'desktop_id': 'desktop_id',
        'desktop_name': 'desktop_name',
        'exec_status': 'exec_status',
        'result_code': 'result_code',
        'fail_reason': 'fail_reason',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'time_zone': 'time_zone'
    }

    def __init__(self, id=None, record_id=None, desktop_id=None, desktop_name=None, exec_status=None, result_code=None, fail_reason=None, start_time=None, end_time=None, time_zone=None):
        """ScheduledTasksRecordsDetails

        The model defined in huaweicloud sdk

        :param id: 任务执行记录详情id
        :type id: str
        :param record_id: 任务执行记录id
        :type record_id: str
        :param desktop_id: 桌面id
        :type desktop_id: str
        :param desktop_name: 桌面名称。
        :type desktop_name: str
        :param exec_status: 执行状态。
        :type exec_status: str
        :param result_code: 失败或者跳过原因的错误码。
        :type result_code: str
        :param fail_reason: 失败或者跳过原因。
        :type fail_reason: str
        :param start_time: 执行开始时间，格式为yyyy-MM-dd HH:mm:ss。
        :type start_time: str
        :param end_time: 执行结束时间，格式为yyyy-MM-dd HH:mm:ss。
        :type end_time: str
        :param time_zone: 时区
        :type time_zone: str
        """
        
        

        self._id = None
        self._record_id = None
        self._desktop_id = None
        self._desktop_name = None
        self._exec_status = None
        self._result_code = None
        self._fail_reason = None
        self._start_time = None
        self._end_time = None
        self._time_zone = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if record_id is not None:
            self.record_id = record_id
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if exec_status is not None:
            self.exec_status = exec_status
        if result_code is not None:
            self.result_code = result_code
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def id(self):
        """Gets the id of this ScheduledTasksRecordsDetails.

        任务执行记录详情id

        :return: The id of this ScheduledTasksRecordsDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScheduledTasksRecordsDetails.

        任务执行记录详情id

        :param id: The id of this ScheduledTasksRecordsDetails.
        :type id: str
        """
        self._id = id

    @property
    def record_id(self):
        """Gets the record_id of this ScheduledTasksRecordsDetails.

        任务执行记录id

        :return: The record_id of this ScheduledTasksRecordsDetails.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this ScheduledTasksRecordsDetails.

        任务执行记录id

        :param record_id: The record_id of this ScheduledTasksRecordsDetails.
        :type record_id: str
        """
        self._record_id = record_id

    @property
    def desktop_id(self):
        """Gets the desktop_id of this ScheduledTasksRecordsDetails.

        桌面id

        :return: The desktop_id of this ScheduledTasksRecordsDetails.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this ScheduledTasksRecordsDetails.

        桌面id

        :param desktop_id: The desktop_id of this ScheduledTasksRecordsDetails.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_name(self):
        """Gets the desktop_name of this ScheduledTasksRecordsDetails.

        桌面名称。

        :return: The desktop_name of this ScheduledTasksRecordsDetails.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        """Sets the desktop_name of this ScheduledTasksRecordsDetails.

        桌面名称。

        :param desktop_name: The desktop_name of this ScheduledTasksRecordsDetails.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def exec_status(self):
        """Gets the exec_status of this ScheduledTasksRecordsDetails.

        执行状态。

        :return: The exec_status of this ScheduledTasksRecordsDetails.
        :rtype: str
        """
        return self._exec_status

    @exec_status.setter
    def exec_status(self, exec_status):
        """Sets the exec_status of this ScheduledTasksRecordsDetails.

        执行状态。

        :param exec_status: The exec_status of this ScheduledTasksRecordsDetails.
        :type exec_status: str
        """
        self._exec_status = exec_status

    @property
    def result_code(self):
        """Gets the result_code of this ScheduledTasksRecordsDetails.

        失败或者跳过原因的错误码。

        :return: The result_code of this ScheduledTasksRecordsDetails.
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this ScheduledTasksRecordsDetails.

        失败或者跳过原因的错误码。

        :param result_code: The result_code of this ScheduledTasksRecordsDetails.
        :type result_code: str
        """
        self._result_code = result_code

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ScheduledTasksRecordsDetails.

        失败或者跳过原因。

        :return: The fail_reason of this ScheduledTasksRecordsDetails.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ScheduledTasksRecordsDetails.

        失败或者跳过原因。

        :param fail_reason: The fail_reason of this ScheduledTasksRecordsDetails.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def start_time(self):
        """Gets the start_time of this ScheduledTasksRecordsDetails.

        执行开始时间，格式为yyyy-MM-dd HH:mm:ss。

        :return: The start_time of this ScheduledTasksRecordsDetails.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ScheduledTasksRecordsDetails.

        执行开始时间，格式为yyyy-MM-dd HH:mm:ss。

        :param start_time: The start_time of this ScheduledTasksRecordsDetails.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ScheduledTasksRecordsDetails.

        执行结束时间，格式为yyyy-MM-dd HH:mm:ss。

        :return: The end_time of this ScheduledTasksRecordsDetails.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ScheduledTasksRecordsDetails.

        执行结束时间，格式为yyyy-MM-dd HH:mm:ss。

        :param end_time: The end_time of this ScheduledTasksRecordsDetails.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def time_zone(self):
        """Gets the time_zone of this ScheduledTasksRecordsDetails.

        时区

        :return: The time_zone of this ScheduledTasksRecordsDetails.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ScheduledTasksRecordsDetails.

        时区

        :param time_zone: The time_zone of this ScheduledTasksRecordsDetails.
        :type time_zone: str
        """
        self._time_zone = time_zone

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
        if not isinstance(other, ScheduledTasksRecordsDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
