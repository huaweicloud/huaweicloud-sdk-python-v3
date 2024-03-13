# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmInfoResponseAlarmInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_time': 'int',
        'job_name': 'str',
        'schedule_type': 'int',
        'send_msg': 'str',
        'plan_time': 'int',
        'remind_type': 'int',
        'send_status': 'int',
        'job_id': 'int'
    }

    attribute_map = {
        'alarm_time': 'alarm_time',
        'job_name': 'job_name',
        'schedule_type': 'schedule_type',
        'send_msg': 'send_msg',
        'plan_time': 'plan_time',
        'remind_type': 'remind_type',
        'send_status': 'send_status',
        'job_id': 'job_id'
    }

    def __init__(self, alarm_time=None, job_name=None, schedule_type=None, send_msg=None, plan_time=None, remind_type=None, send_status=None, job_id=None):
        """AlarmInfoResponseAlarmInfo

        The model defined in huaweicloud sdk

        :param alarm_time: 告警通知时间
        :type alarm_time: int
        :param job_name: 作业名称
        :type job_name: str
        :param schedule_type: 作业实例调度方式，取值范围：0 正常调度，2手工调度，5补数据，6子作业调度，7单次调度
        :type schedule_type: int
        :param send_msg: 发送信息
        :type send_msg: str
        :param plan_time: 计划时间
        :type plan_time: int
        :param remind_type: 告警通知类型，取值范围：0 运行成功，1 运行异常/失败， 12 未完成，13 运行取消
        :type remind_type: int
        :param send_status: 发送状态，取值范围：0 发送成功，1：发送失败
        :type send_status: int
        :param job_id: 作业ID
        :type job_id: int
        """
        
        

        self._alarm_time = None
        self._job_name = None
        self._schedule_type = None
        self._send_msg = None
        self._plan_time = None
        self._remind_type = None
        self._send_status = None
        self._job_id = None
        self.discriminator = None

        if alarm_time is not None:
            self.alarm_time = alarm_time
        if job_name is not None:
            self.job_name = job_name
        if schedule_type is not None:
            self.schedule_type = schedule_type
        if send_msg is not None:
            self.send_msg = send_msg
        if plan_time is not None:
            self.plan_time = plan_time
        if remind_type is not None:
            self.remind_type = remind_type
        if send_status is not None:
            self.send_status = send_status
        if job_id is not None:
            self.job_id = job_id

    @property
    def alarm_time(self):
        """Gets the alarm_time of this AlarmInfoResponseAlarmInfo.

        告警通知时间

        :return: The alarm_time of this AlarmInfoResponseAlarmInfo.
        :rtype: int
        """
        return self._alarm_time

    @alarm_time.setter
    def alarm_time(self, alarm_time):
        """Sets the alarm_time of this AlarmInfoResponseAlarmInfo.

        告警通知时间

        :param alarm_time: The alarm_time of this AlarmInfoResponseAlarmInfo.
        :type alarm_time: int
        """
        self._alarm_time = alarm_time

    @property
    def job_name(self):
        """Gets the job_name of this AlarmInfoResponseAlarmInfo.

        作业名称

        :return: The job_name of this AlarmInfoResponseAlarmInfo.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this AlarmInfoResponseAlarmInfo.

        作业名称

        :param job_name: The job_name of this AlarmInfoResponseAlarmInfo.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def schedule_type(self):
        """Gets the schedule_type of this AlarmInfoResponseAlarmInfo.

        作业实例调度方式，取值范围：0 正常调度，2手工调度，5补数据，6子作业调度，7单次调度

        :return: The schedule_type of this AlarmInfoResponseAlarmInfo.
        :rtype: int
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this AlarmInfoResponseAlarmInfo.

        作业实例调度方式，取值范围：0 正常调度，2手工调度，5补数据，6子作业调度，7单次调度

        :param schedule_type: The schedule_type of this AlarmInfoResponseAlarmInfo.
        :type schedule_type: int
        """
        self._schedule_type = schedule_type

    @property
    def send_msg(self):
        """Gets the send_msg of this AlarmInfoResponseAlarmInfo.

        发送信息

        :return: The send_msg of this AlarmInfoResponseAlarmInfo.
        :rtype: str
        """
        return self._send_msg

    @send_msg.setter
    def send_msg(self, send_msg):
        """Sets the send_msg of this AlarmInfoResponseAlarmInfo.

        发送信息

        :param send_msg: The send_msg of this AlarmInfoResponseAlarmInfo.
        :type send_msg: str
        """
        self._send_msg = send_msg

    @property
    def plan_time(self):
        """Gets the plan_time of this AlarmInfoResponseAlarmInfo.

        计划时间

        :return: The plan_time of this AlarmInfoResponseAlarmInfo.
        :rtype: int
        """
        return self._plan_time

    @plan_time.setter
    def plan_time(self, plan_time):
        """Sets the plan_time of this AlarmInfoResponseAlarmInfo.

        计划时间

        :param plan_time: The plan_time of this AlarmInfoResponseAlarmInfo.
        :type plan_time: int
        """
        self._plan_time = plan_time

    @property
    def remind_type(self):
        """Gets the remind_type of this AlarmInfoResponseAlarmInfo.

        告警通知类型，取值范围：0 运行成功，1 运行异常/失败， 12 未完成，13 运行取消

        :return: The remind_type of this AlarmInfoResponseAlarmInfo.
        :rtype: int
        """
        return self._remind_type

    @remind_type.setter
    def remind_type(self, remind_type):
        """Sets the remind_type of this AlarmInfoResponseAlarmInfo.

        告警通知类型，取值范围：0 运行成功，1 运行异常/失败， 12 未完成，13 运行取消

        :param remind_type: The remind_type of this AlarmInfoResponseAlarmInfo.
        :type remind_type: int
        """
        self._remind_type = remind_type

    @property
    def send_status(self):
        """Gets the send_status of this AlarmInfoResponseAlarmInfo.

        发送状态，取值范围：0 发送成功，1：发送失败

        :return: The send_status of this AlarmInfoResponseAlarmInfo.
        :rtype: int
        """
        return self._send_status

    @send_status.setter
    def send_status(self, send_status):
        """Sets the send_status of this AlarmInfoResponseAlarmInfo.

        发送状态，取值范围：0 发送成功，1：发送失败

        :param send_status: The send_status of this AlarmInfoResponseAlarmInfo.
        :type send_status: int
        """
        self._send_status = send_status

    @property
    def job_id(self):
        """Gets the job_id of this AlarmInfoResponseAlarmInfo.

        作业ID

        :return: The job_id of this AlarmInfoResponseAlarmInfo.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this AlarmInfoResponseAlarmInfo.

        作业ID

        :param job_id: The job_id of this AlarmInfoResponseAlarmInfo.
        :type job_id: int
        """
        self._job_id = job_id

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
        if not isinstance(other, AlarmInfoResponseAlarmInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
