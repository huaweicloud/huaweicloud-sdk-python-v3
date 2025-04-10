# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmLogResponseAlarmLog:

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
        'alarm_life': 'str',
        'send_email': 'bool',
        'alarm_time': 'str',
        'alarm_type': 'str',
        'alarm_fix_time': 'str',
        'alarm_status': 'str',
        'alarm_risk': 'str',
        'alarm_description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'alarm_life': 'alarmLife',
        'send_email': 'sendEmail',
        'alarm_time': 'alarm_time',
        'alarm_type': 'alarm_type',
        'alarm_fix_time': 'alarm_fix_time',
        'alarm_status': 'alarm_status',
        'alarm_risk': 'alarm_risk',
        'alarm_description': 'alarm_description'
    }

    def __init__(self, id=None, alarm_life=None, send_email=None, alarm_time=None, alarm_type=None, alarm_fix_time=None, alarm_status=None, alarm_risk=None, alarm_description=None):
        r"""AlarmLogResponseAlarmLog

        The model defined in huaweicloud sdk

        :param id: 告警ID
        :type id: str
        :param alarm_life: 告警状态 - ON - OFF
        :type alarm_life: str
        :param send_email: 是否发送邮件
        :type send_email: bool
        :param alarm_time: 告警发生时间
        :type alarm_time: str
        :param alarm_type: 告警类型 - RISK_RULE: 风险规则 - RISK_CPU: CPU超限 - RISK_MEMORY: 内存超限 - RISK_DISK: 磁盘超限 - RISK_DISK_CAPACITY: 磁盘容量不足六个月 - RISK_BACKUP: 备份失败 - AUDIT_QPS_OVERFLOW: 流量超限入库延迟告警 - RISK_AGENT: Agent异常 - AUDIT_BACKUP_FAILED: 实例备份失败(运维侧)
        :type alarm_type: str
        :param alarm_fix_time: 告警恢复时间
        :type alarm_fix_time: str
        :param alarm_status: 告警确认状态 - DONE: 已确认 - UNDO: 未确认
        :type alarm_status: str
        :param alarm_risk: 告警风险等级 - LOW - MEDIUM - HIGH
        :type alarm_risk: str
        :param alarm_description: 告警描述信息
        :type alarm_description: str
        """
        
        

        self._id = None
        self._alarm_life = None
        self._send_email = None
        self._alarm_time = None
        self._alarm_type = None
        self._alarm_fix_time = None
        self._alarm_status = None
        self._alarm_risk = None
        self._alarm_description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if alarm_life is not None:
            self.alarm_life = alarm_life
        if send_email is not None:
            self.send_email = send_email
        if alarm_time is not None:
            self.alarm_time = alarm_time
        if alarm_type is not None:
            self.alarm_type = alarm_type
        if alarm_fix_time is not None:
            self.alarm_fix_time = alarm_fix_time
        if alarm_status is not None:
            self.alarm_status = alarm_status
        if alarm_risk is not None:
            self.alarm_risk = alarm_risk
        if alarm_description is not None:
            self.alarm_description = alarm_description

    @property
    def id(self):
        r"""Gets the id of this AlarmLogResponseAlarmLog.

        告警ID

        :return: The id of this AlarmLogResponseAlarmLog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AlarmLogResponseAlarmLog.

        告警ID

        :param id: The id of this AlarmLogResponseAlarmLog.
        :type id: str
        """
        self._id = id

    @property
    def alarm_life(self):
        r"""Gets the alarm_life of this AlarmLogResponseAlarmLog.

        告警状态 - ON - OFF

        :return: The alarm_life of this AlarmLogResponseAlarmLog.
        :rtype: str
        """
        return self._alarm_life

    @alarm_life.setter
    def alarm_life(self, alarm_life):
        r"""Sets the alarm_life of this AlarmLogResponseAlarmLog.

        告警状态 - ON - OFF

        :param alarm_life: The alarm_life of this AlarmLogResponseAlarmLog.
        :type alarm_life: str
        """
        self._alarm_life = alarm_life

    @property
    def send_email(self):
        r"""Gets the send_email of this AlarmLogResponseAlarmLog.

        是否发送邮件

        :return: The send_email of this AlarmLogResponseAlarmLog.
        :rtype: bool
        """
        return self._send_email

    @send_email.setter
    def send_email(self, send_email):
        r"""Sets the send_email of this AlarmLogResponseAlarmLog.

        是否发送邮件

        :param send_email: The send_email of this AlarmLogResponseAlarmLog.
        :type send_email: bool
        """
        self._send_email = send_email

    @property
    def alarm_time(self):
        r"""Gets the alarm_time of this AlarmLogResponseAlarmLog.

        告警发生时间

        :return: The alarm_time of this AlarmLogResponseAlarmLog.
        :rtype: str
        """
        return self._alarm_time

    @alarm_time.setter
    def alarm_time(self, alarm_time):
        r"""Sets the alarm_time of this AlarmLogResponseAlarmLog.

        告警发生时间

        :param alarm_time: The alarm_time of this AlarmLogResponseAlarmLog.
        :type alarm_time: str
        """
        self._alarm_time = alarm_time

    @property
    def alarm_type(self):
        r"""Gets the alarm_type of this AlarmLogResponseAlarmLog.

        告警类型 - RISK_RULE: 风险规则 - RISK_CPU: CPU超限 - RISK_MEMORY: 内存超限 - RISK_DISK: 磁盘超限 - RISK_DISK_CAPACITY: 磁盘容量不足六个月 - RISK_BACKUP: 备份失败 - AUDIT_QPS_OVERFLOW: 流量超限入库延迟告警 - RISK_AGENT: Agent异常 - AUDIT_BACKUP_FAILED: 实例备份失败(运维侧)

        :return: The alarm_type of this AlarmLogResponseAlarmLog.
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        r"""Sets the alarm_type of this AlarmLogResponseAlarmLog.

        告警类型 - RISK_RULE: 风险规则 - RISK_CPU: CPU超限 - RISK_MEMORY: 内存超限 - RISK_DISK: 磁盘超限 - RISK_DISK_CAPACITY: 磁盘容量不足六个月 - RISK_BACKUP: 备份失败 - AUDIT_QPS_OVERFLOW: 流量超限入库延迟告警 - RISK_AGENT: Agent异常 - AUDIT_BACKUP_FAILED: 实例备份失败(运维侧)

        :param alarm_type: The alarm_type of this AlarmLogResponseAlarmLog.
        :type alarm_type: str
        """
        self._alarm_type = alarm_type

    @property
    def alarm_fix_time(self):
        r"""Gets the alarm_fix_time of this AlarmLogResponseAlarmLog.

        告警恢复时间

        :return: The alarm_fix_time of this AlarmLogResponseAlarmLog.
        :rtype: str
        """
        return self._alarm_fix_time

    @alarm_fix_time.setter
    def alarm_fix_time(self, alarm_fix_time):
        r"""Sets the alarm_fix_time of this AlarmLogResponseAlarmLog.

        告警恢复时间

        :param alarm_fix_time: The alarm_fix_time of this AlarmLogResponseAlarmLog.
        :type alarm_fix_time: str
        """
        self._alarm_fix_time = alarm_fix_time

    @property
    def alarm_status(self):
        r"""Gets the alarm_status of this AlarmLogResponseAlarmLog.

        告警确认状态 - DONE: 已确认 - UNDO: 未确认

        :return: The alarm_status of this AlarmLogResponseAlarmLog.
        :rtype: str
        """
        return self._alarm_status

    @alarm_status.setter
    def alarm_status(self, alarm_status):
        r"""Sets the alarm_status of this AlarmLogResponseAlarmLog.

        告警确认状态 - DONE: 已确认 - UNDO: 未确认

        :param alarm_status: The alarm_status of this AlarmLogResponseAlarmLog.
        :type alarm_status: str
        """
        self._alarm_status = alarm_status

    @property
    def alarm_risk(self):
        r"""Gets the alarm_risk of this AlarmLogResponseAlarmLog.

        告警风险等级 - LOW - MEDIUM - HIGH

        :return: The alarm_risk of this AlarmLogResponseAlarmLog.
        :rtype: str
        """
        return self._alarm_risk

    @alarm_risk.setter
    def alarm_risk(self, alarm_risk):
        r"""Sets the alarm_risk of this AlarmLogResponseAlarmLog.

        告警风险等级 - LOW - MEDIUM - HIGH

        :param alarm_risk: The alarm_risk of this AlarmLogResponseAlarmLog.
        :type alarm_risk: str
        """
        self._alarm_risk = alarm_risk

    @property
    def alarm_description(self):
        r"""Gets the alarm_description of this AlarmLogResponseAlarmLog.

        告警描述信息

        :return: The alarm_description of this AlarmLogResponseAlarmLog.
        :rtype: str
        """
        return self._alarm_description

    @alarm_description.setter
    def alarm_description(self, alarm_description):
        r"""Sets the alarm_description of this AlarmLogResponseAlarmLog.

        告警描述信息

        :param alarm_description: The alarm_description of this AlarmLogResponseAlarmLog.
        :type alarm_description: str
        """
        self._alarm_description = alarm_description

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
        if not isinstance(other, AlarmLogResponseAlarmLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
