# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmParamForV4Db:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_create_time': 'int',
        'alarm_update_time': 'int',
        'alarm_rule_name': 'str',
        'alarm_rule_id': 'int',
        'enterprise_project_id': 'str',
        'prom_instance_id': 'str',
        'alarm_rule_description': 'str',
        'alarm_rule_enable': 'bool',
        'alarm_rule_status': 'str',
        'alarm_rule_type': 'str',
        'metric_alarm_spec': 'MetricAlarmSpec',
        'event_alarm_spec': 'EventAlarmSpec',
        'alarm_notifications': 'AlarmNotification',
        'user_id': 'str'
    }

    attribute_map = {
        'alarm_create_time': 'alarm_create_time',
        'alarm_update_time': 'alarm_update_time',
        'alarm_rule_name': 'alarm_rule_name',
        'alarm_rule_id': 'alarm_rule_id',
        'enterprise_project_id': 'enterprise_project_id',
        'prom_instance_id': 'prom_instance_id',
        'alarm_rule_description': 'alarm_rule_description',
        'alarm_rule_enable': 'alarm_rule_enable',
        'alarm_rule_status': 'alarm_rule_status',
        'alarm_rule_type': 'alarm_rule_type',
        'metric_alarm_spec': 'metric_alarm_spec',
        'event_alarm_spec': 'event_alarm_spec',
        'alarm_notifications': 'alarm_notifications',
        'user_id': 'user_id'
    }

    def __init__(self, alarm_create_time=None, alarm_update_time=None, alarm_rule_name=None, alarm_rule_id=None, enterprise_project_id=None, prom_instance_id=None, alarm_rule_description=None, alarm_rule_enable=None, alarm_rule_status=None, alarm_rule_type=None, metric_alarm_spec=None, event_alarm_spec=None, alarm_notifications=None, user_id=None):
        """AlarmParamForV4Db

        The model defined in huaweicloud sdk

        :param alarm_create_time: 告警规则创建时间。
        :type alarm_create_time: int
        :param alarm_update_time: 告警规则修改时间。
        :type alarm_update_time: int
        :param alarm_rule_name: 告警规则名称。
        :type alarm_rule_name: str
        :param alarm_rule_id: 告警规则id。
        :type alarm_rule_id: int
        :param enterprise_project_id: 企业项目id。
        :type enterprise_project_id: str
        :param prom_instance_id: Prometheus实例id。
        :type prom_instance_id: str
        :param alarm_rule_description: 告警规则描述。
        :type alarm_rule_description: str
        :param alarm_rule_enable: 是否启用。
        :type alarm_rule_enable: bool
        :param alarm_rule_status: 告警状态。 - “OK”：正常 - “alarm”：超限阈值 - “Effective”：生效中 - “Invalid”：停用中
        :type alarm_rule_status: str
        :param alarm_rule_type: 规则类型。 - “metric”：指标告警规则 - “event”：事件告警规则
        :type alarm_rule_type: str
        :param metric_alarm_spec: 
        :type metric_alarm_spec: :class:`huaweicloudsdkaom.v2.MetricAlarmSpec`
        :param event_alarm_spec: 
        :type event_alarm_spec: :class:`huaweicloudsdkaom.v2.EventAlarmSpec`
        :param alarm_notifications: 
        :type alarm_notifications: :class:`huaweicloudsdkaom.v2.AlarmNotification`
        :param user_id: 用户id。
        :type user_id: str
        """
        
        

        self._alarm_create_time = None
        self._alarm_update_time = None
        self._alarm_rule_name = None
        self._alarm_rule_id = None
        self._enterprise_project_id = None
        self._prom_instance_id = None
        self._alarm_rule_description = None
        self._alarm_rule_enable = None
        self._alarm_rule_status = None
        self._alarm_rule_type = None
        self._metric_alarm_spec = None
        self._event_alarm_spec = None
        self._alarm_notifications = None
        self._user_id = None
        self.discriminator = None

        self.alarm_create_time = alarm_create_time
        self.alarm_update_time = alarm_update_time
        self.alarm_rule_name = alarm_rule_name
        self.alarm_rule_id = alarm_rule_id
        self.enterprise_project_id = enterprise_project_id
        if prom_instance_id is not None:
            self.prom_instance_id = prom_instance_id
        self.alarm_rule_description = alarm_rule_description
        self.alarm_rule_enable = alarm_rule_enable
        self.alarm_rule_status = alarm_rule_status
        self.alarm_rule_type = alarm_rule_type
        if metric_alarm_spec is not None:
            self.metric_alarm_spec = metric_alarm_spec
        if event_alarm_spec is not None:
            self.event_alarm_spec = event_alarm_spec
        self.alarm_notifications = alarm_notifications
        if user_id is not None:
            self.user_id = user_id

    @property
    def alarm_create_time(self):
        """Gets the alarm_create_time of this AlarmParamForV4Db.

        告警规则创建时间。

        :return: The alarm_create_time of this AlarmParamForV4Db.
        :rtype: int
        """
        return self._alarm_create_time

    @alarm_create_time.setter
    def alarm_create_time(self, alarm_create_time):
        """Sets the alarm_create_time of this AlarmParamForV4Db.

        告警规则创建时间。

        :param alarm_create_time: The alarm_create_time of this AlarmParamForV4Db.
        :type alarm_create_time: int
        """
        self._alarm_create_time = alarm_create_time

    @property
    def alarm_update_time(self):
        """Gets the alarm_update_time of this AlarmParamForV4Db.

        告警规则修改时间。

        :return: The alarm_update_time of this AlarmParamForV4Db.
        :rtype: int
        """
        return self._alarm_update_time

    @alarm_update_time.setter
    def alarm_update_time(self, alarm_update_time):
        """Sets the alarm_update_time of this AlarmParamForV4Db.

        告警规则修改时间。

        :param alarm_update_time: The alarm_update_time of this AlarmParamForV4Db.
        :type alarm_update_time: int
        """
        self._alarm_update_time = alarm_update_time

    @property
    def alarm_rule_name(self):
        """Gets the alarm_rule_name of this AlarmParamForV4Db.

        告警规则名称。

        :return: The alarm_rule_name of this AlarmParamForV4Db.
        :rtype: str
        """
        return self._alarm_rule_name

    @alarm_rule_name.setter
    def alarm_rule_name(self, alarm_rule_name):
        """Sets the alarm_rule_name of this AlarmParamForV4Db.

        告警规则名称。

        :param alarm_rule_name: The alarm_rule_name of this AlarmParamForV4Db.
        :type alarm_rule_name: str
        """
        self._alarm_rule_name = alarm_rule_name

    @property
    def alarm_rule_id(self):
        """Gets the alarm_rule_id of this AlarmParamForV4Db.

        告警规则id。

        :return: The alarm_rule_id of this AlarmParamForV4Db.
        :rtype: int
        """
        return self._alarm_rule_id

    @alarm_rule_id.setter
    def alarm_rule_id(self, alarm_rule_id):
        """Sets the alarm_rule_id of this AlarmParamForV4Db.

        告警规则id。

        :param alarm_rule_id: The alarm_rule_id of this AlarmParamForV4Db.
        :type alarm_rule_id: int
        """
        self._alarm_rule_id = alarm_rule_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this AlarmParamForV4Db.

        企业项目id。

        :return: The enterprise_project_id of this AlarmParamForV4Db.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this AlarmParamForV4Db.

        企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this AlarmParamForV4Db.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def prom_instance_id(self):
        """Gets the prom_instance_id of this AlarmParamForV4Db.

        Prometheus实例id。

        :return: The prom_instance_id of this AlarmParamForV4Db.
        :rtype: str
        """
        return self._prom_instance_id

    @prom_instance_id.setter
    def prom_instance_id(self, prom_instance_id):
        """Sets the prom_instance_id of this AlarmParamForV4Db.

        Prometheus实例id。

        :param prom_instance_id: The prom_instance_id of this AlarmParamForV4Db.
        :type prom_instance_id: str
        """
        self._prom_instance_id = prom_instance_id

    @property
    def alarm_rule_description(self):
        """Gets the alarm_rule_description of this AlarmParamForV4Db.

        告警规则描述。

        :return: The alarm_rule_description of this AlarmParamForV4Db.
        :rtype: str
        """
        return self._alarm_rule_description

    @alarm_rule_description.setter
    def alarm_rule_description(self, alarm_rule_description):
        """Sets the alarm_rule_description of this AlarmParamForV4Db.

        告警规则描述。

        :param alarm_rule_description: The alarm_rule_description of this AlarmParamForV4Db.
        :type alarm_rule_description: str
        """
        self._alarm_rule_description = alarm_rule_description

    @property
    def alarm_rule_enable(self):
        """Gets the alarm_rule_enable of this AlarmParamForV4Db.

        是否启用。

        :return: The alarm_rule_enable of this AlarmParamForV4Db.
        :rtype: bool
        """
        return self._alarm_rule_enable

    @alarm_rule_enable.setter
    def alarm_rule_enable(self, alarm_rule_enable):
        """Sets the alarm_rule_enable of this AlarmParamForV4Db.

        是否启用。

        :param alarm_rule_enable: The alarm_rule_enable of this AlarmParamForV4Db.
        :type alarm_rule_enable: bool
        """
        self._alarm_rule_enable = alarm_rule_enable

    @property
    def alarm_rule_status(self):
        """Gets the alarm_rule_status of this AlarmParamForV4Db.

        告警状态。 - “OK”：正常 - “alarm”：超限阈值 - “Effective”：生效中 - “Invalid”：停用中

        :return: The alarm_rule_status of this AlarmParamForV4Db.
        :rtype: str
        """
        return self._alarm_rule_status

    @alarm_rule_status.setter
    def alarm_rule_status(self, alarm_rule_status):
        """Sets the alarm_rule_status of this AlarmParamForV4Db.

        告警状态。 - “OK”：正常 - “alarm”：超限阈值 - “Effective”：生效中 - “Invalid”：停用中

        :param alarm_rule_status: The alarm_rule_status of this AlarmParamForV4Db.
        :type alarm_rule_status: str
        """
        self._alarm_rule_status = alarm_rule_status

    @property
    def alarm_rule_type(self):
        """Gets the alarm_rule_type of this AlarmParamForV4Db.

        规则类型。 - “metric”：指标告警规则 - “event”：事件告警规则

        :return: The alarm_rule_type of this AlarmParamForV4Db.
        :rtype: str
        """
        return self._alarm_rule_type

    @alarm_rule_type.setter
    def alarm_rule_type(self, alarm_rule_type):
        """Sets the alarm_rule_type of this AlarmParamForV4Db.

        规则类型。 - “metric”：指标告警规则 - “event”：事件告警规则

        :param alarm_rule_type: The alarm_rule_type of this AlarmParamForV4Db.
        :type alarm_rule_type: str
        """
        self._alarm_rule_type = alarm_rule_type

    @property
    def metric_alarm_spec(self):
        """Gets the metric_alarm_spec of this AlarmParamForV4Db.

        :return: The metric_alarm_spec of this AlarmParamForV4Db.
        :rtype: :class:`huaweicloudsdkaom.v2.MetricAlarmSpec`
        """
        return self._metric_alarm_spec

    @metric_alarm_spec.setter
    def metric_alarm_spec(self, metric_alarm_spec):
        """Sets the metric_alarm_spec of this AlarmParamForV4Db.

        :param metric_alarm_spec: The metric_alarm_spec of this AlarmParamForV4Db.
        :type metric_alarm_spec: :class:`huaweicloudsdkaom.v2.MetricAlarmSpec`
        """
        self._metric_alarm_spec = metric_alarm_spec

    @property
    def event_alarm_spec(self):
        """Gets the event_alarm_spec of this AlarmParamForV4Db.

        :return: The event_alarm_spec of this AlarmParamForV4Db.
        :rtype: :class:`huaweicloudsdkaom.v2.EventAlarmSpec`
        """
        return self._event_alarm_spec

    @event_alarm_spec.setter
    def event_alarm_spec(self, event_alarm_spec):
        """Sets the event_alarm_spec of this AlarmParamForV4Db.

        :param event_alarm_spec: The event_alarm_spec of this AlarmParamForV4Db.
        :type event_alarm_spec: :class:`huaweicloudsdkaom.v2.EventAlarmSpec`
        """
        self._event_alarm_spec = event_alarm_spec

    @property
    def alarm_notifications(self):
        """Gets the alarm_notifications of this AlarmParamForV4Db.

        :return: The alarm_notifications of this AlarmParamForV4Db.
        :rtype: :class:`huaweicloudsdkaom.v2.AlarmNotification`
        """
        return self._alarm_notifications

    @alarm_notifications.setter
    def alarm_notifications(self, alarm_notifications):
        """Sets the alarm_notifications of this AlarmParamForV4Db.

        :param alarm_notifications: The alarm_notifications of this AlarmParamForV4Db.
        :type alarm_notifications: :class:`huaweicloudsdkaom.v2.AlarmNotification`
        """
        self._alarm_notifications = alarm_notifications

    @property
    def user_id(self):
        """Gets the user_id of this AlarmParamForV4Db.

        用户id。

        :return: The user_id of this AlarmParamForV4Db.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AlarmParamForV4Db.

        用户id。

        :param user_id: The user_id of this AlarmParamForV4Db.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, AlarmParamForV4Db):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
