# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddOrUpdateAlarmRuleV4RequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_notifications': 'AlarmNotification',
        'alarm_rule_description': 'str',
        'alarm_rule_enable': 'bool',
        'alarm_rule_name': 'str',
        'alarm_rule_type': 'str',
        'event_alarm_spec': 'EventAlarmSpec',
        'metric_alarm_spec': 'MetricAlarmSpec',
        'prom_instance_id': 'str'
    }

    attribute_map = {
        'alarm_notifications': 'alarm_notifications',
        'alarm_rule_description': 'alarm_rule_description',
        'alarm_rule_enable': 'alarm_rule_enable',
        'alarm_rule_name': 'alarm_rule_name',
        'alarm_rule_type': 'alarm_rule_type',
        'event_alarm_spec': 'event_alarm_spec',
        'metric_alarm_spec': 'metric_alarm_spec',
        'prom_instance_id': 'prom_instance_id'
    }

    def __init__(self, alarm_notifications=None, alarm_rule_description=None, alarm_rule_enable=None, alarm_rule_name=None, alarm_rule_type=None, event_alarm_spec=None, metric_alarm_spec=None, prom_instance_id=None):
        """AddOrUpdateAlarmRuleV4RequestBody

        The model defined in huaweicloud sdk

        :param alarm_notifications: 
        :type alarm_notifications: :class:`huaweicloudsdkaom.v2.AlarmNotification`
        :param alarm_rule_description: 告警规则描述。
        :type alarm_rule_description: str
        :param alarm_rule_enable: 是否启用。
        :type alarm_rule_enable: bool
        :param alarm_rule_name: 告警规则名称。
        :type alarm_rule_name: str
        :param alarm_rule_type: 告警规则类型。 - “metric”：指标告警规则 - “event”：事件告警规则
        :type alarm_rule_type: str
        :param event_alarm_spec: 
        :type event_alarm_spec: :class:`huaweicloudsdkaom.v2.EventAlarmSpec`
        :param metric_alarm_spec: 
        :type metric_alarm_spec: :class:`huaweicloudsdkaom.v2.MetricAlarmSpec`
        :param prom_instance_id: Prometheus实例id。
        :type prom_instance_id: str
        """
        
        

        self._alarm_notifications = None
        self._alarm_rule_description = None
        self._alarm_rule_enable = None
        self._alarm_rule_name = None
        self._alarm_rule_type = None
        self._event_alarm_spec = None
        self._metric_alarm_spec = None
        self._prom_instance_id = None
        self.discriminator = None

        if alarm_notifications is not None:
            self.alarm_notifications = alarm_notifications
        if alarm_rule_description is not None:
            self.alarm_rule_description = alarm_rule_description
        if alarm_rule_enable is not None:
            self.alarm_rule_enable = alarm_rule_enable
        self.alarm_rule_name = alarm_rule_name
        self.alarm_rule_type = alarm_rule_type
        if event_alarm_spec is not None:
            self.event_alarm_spec = event_alarm_spec
        if metric_alarm_spec is not None:
            self.metric_alarm_spec = metric_alarm_spec
        if prom_instance_id is not None:
            self.prom_instance_id = prom_instance_id

    @property
    def alarm_notifications(self):
        """Gets the alarm_notifications of this AddOrUpdateAlarmRuleV4RequestBody.

        :return: The alarm_notifications of this AddOrUpdateAlarmRuleV4RequestBody.
        :rtype: :class:`huaweicloudsdkaom.v2.AlarmNotification`
        """
        return self._alarm_notifications

    @alarm_notifications.setter
    def alarm_notifications(self, alarm_notifications):
        """Sets the alarm_notifications of this AddOrUpdateAlarmRuleV4RequestBody.

        :param alarm_notifications: The alarm_notifications of this AddOrUpdateAlarmRuleV4RequestBody.
        :type alarm_notifications: :class:`huaweicloudsdkaom.v2.AlarmNotification`
        """
        self._alarm_notifications = alarm_notifications

    @property
    def alarm_rule_description(self):
        """Gets the alarm_rule_description of this AddOrUpdateAlarmRuleV4RequestBody.

        告警规则描述。

        :return: The alarm_rule_description of this AddOrUpdateAlarmRuleV4RequestBody.
        :rtype: str
        """
        return self._alarm_rule_description

    @alarm_rule_description.setter
    def alarm_rule_description(self, alarm_rule_description):
        """Sets the alarm_rule_description of this AddOrUpdateAlarmRuleV4RequestBody.

        告警规则描述。

        :param alarm_rule_description: The alarm_rule_description of this AddOrUpdateAlarmRuleV4RequestBody.
        :type alarm_rule_description: str
        """
        self._alarm_rule_description = alarm_rule_description

    @property
    def alarm_rule_enable(self):
        """Gets the alarm_rule_enable of this AddOrUpdateAlarmRuleV4RequestBody.

        是否启用。

        :return: The alarm_rule_enable of this AddOrUpdateAlarmRuleV4RequestBody.
        :rtype: bool
        """
        return self._alarm_rule_enable

    @alarm_rule_enable.setter
    def alarm_rule_enable(self, alarm_rule_enable):
        """Sets the alarm_rule_enable of this AddOrUpdateAlarmRuleV4RequestBody.

        是否启用。

        :param alarm_rule_enable: The alarm_rule_enable of this AddOrUpdateAlarmRuleV4RequestBody.
        :type alarm_rule_enable: bool
        """
        self._alarm_rule_enable = alarm_rule_enable

    @property
    def alarm_rule_name(self):
        """Gets the alarm_rule_name of this AddOrUpdateAlarmRuleV4RequestBody.

        告警规则名称。

        :return: The alarm_rule_name of this AddOrUpdateAlarmRuleV4RequestBody.
        :rtype: str
        """
        return self._alarm_rule_name

    @alarm_rule_name.setter
    def alarm_rule_name(self, alarm_rule_name):
        """Sets the alarm_rule_name of this AddOrUpdateAlarmRuleV4RequestBody.

        告警规则名称。

        :param alarm_rule_name: The alarm_rule_name of this AddOrUpdateAlarmRuleV4RequestBody.
        :type alarm_rule_name: str
        """
        self._alarm_rule_name = alarm_rule_name

    @property
    def alarm_rule_type(self):
        """Gets the alarm_rule_type of this AddOrUpdateAlarmRuleV4RequestBody.

        告警规则类型。 - “metric”：指标告警规则 - “event”：事件告警规则

        :return: The alarm_rule_type of this AddOrUpdateAlarmRuleV4RequestBody.
        :rtype: str
        """
        return self._alarm_rule_type

    @alarm_rule_type.setter
    def alarm_rule_type(self, alarm_rule_type):
        """Sets the alarm_rule_type of this AddOrUpdateAlarmRuleV4RequestBody.

        告警规则类型。 - “metric”：指标告警规则 - “event”：事件告警规则

        :param alarm_rule_type: The alarm_rule_type of this AddOrUpdateAlarmRuleV4RequestBody.
        :type alarm_rule_type: str
        """
        self._alarm_rule_type = alarm_rule_type

    @property
    def event_alarm_spec(self):
        """Gets the event_alarm_spec of this AddOrUpdateAlarmRuleV4RequestBody.

        :return: The event_alarm_spec of this AddOrUpdateAlarmRuleV4RequestBody.
        :rtype: :class:`huaweicloudsdkaom.v2.EventAlarmSpec`
        """
        return self._event_alarm_spec

    @event_alarm_spec.setter
    def event_alarm_spec(self, event_alarm_spec):
        """Sets the event_alarm_spec of this AddOrUpdateAlarmRuleV4RequestBody.

        :param event_alarm_spec: The event_alarm_spec of this AddOrUpdateAlarmRuleV4RequestBody.
        :type event_alarm_spec: :class:`huaweicloudsdkaom.v2.EventAlarmSpec`
        """
        self._event_alarm_spec = event_alarm_spec

    @property
    def metric_alarm_spec(self):
        """Gets the metric_alarm_spec of this AddOrUpdateAlarmRuleV4RequestBody.

        :return: The metric_alarm_spec of this AddOrUpdateAlarmRuleV4RequestBody.
        :rtype: :class:`huaweicloudsdkaom.v2.MetricAlarmSpec`
        """
        return self._metric_alarm_spec

    @metric_alarm_spec.setter
    def metric_alarm_spec(self, metric_alarm_spec):
        """Sets the metric_alarm_spec of this AddOrUpdateAlarmRuleV4RequestBody.

        :param metric_alarm_spec: The metric_alarm_spec of this AddOrUpdateAlarmRuleV4RequestBody.
        :type metric_alarm_spec: :class:`huaweicloudsdkaom.v2.MetricAlarmSpec`
        """
        self._metric_alarm_spec = metric_alarm_spec

    @property
    def prom_instance_id(self):
        """Gets the prom_instance_id of this AddOrUpdateAlarmRuleV4RequestBody.

        Prometheus实例id。

        :return: The prom_instance_id of this AddOrUpdateAlarmRuleV4RequestBody.
        :rtype: str
        """
        return self._prom_instance_id

    @prom_instance_id.setter
    def prom_instance_id(self, prom_instance_id):
        """Sets the prom_instance_id of this AddOrUpdateAlarmRuleV4RequestBody.

        Prometheus实例id。

        :param prom_instance_id: The prom_instance_id of this AddOrUpdateAlarmRuleV4RequestBody.
        :type prom_instance_id: str
        """
        self._prom_instance_id = prom_instance_id

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
        if not isinstance(other, AddOrUpdateAlarmRuleV4RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
