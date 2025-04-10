# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventAlarmSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_source': 'str',
        'event_source': 'str',
        'monitor_objects': 'list[dict(str, str)]',
        'trigger_conditions': 'list[EventTriggerCondition]',
        'alarm_rule_template_bind_enable': 'bool',
        'alarm_rule_template_id': 'str'
    }

    attribute_map = {
        'alarm_source': 'alarm_source',
        'event_source': 'event_source',
        'monitor_objects': 'monitor_objects',
        'trigger_conditions': 'trigger_conditions',
        'alarm_rule_template_bind_enable': 'alarm_rule_template_bind_enable',
        'alarm_rule_template_id': 'alarm_rule_template_id'
    }

    def __init__(self, alarm_source=None, event_source=None, monitor_objects=None, trigger_conditions=None, alarm_rule_template_bind_enable=None, alarm_rule_template_id=None):
        r"""EventAlarmSpec

        The model defined in huaweicloud sdk

        :param alarm_source: 告警规则来源。 - “systemEvent”：系统事件 - “customEvent”：自定义事件
        :type alarm_source: str
        :param event_source: 告警来源。 - “RDS” - “EVS” - “CCE” - “LTS” - “AOM”
        :type event_source: str
        :param monitor_objects: 监控对象列表。键值对形式，键值为： - “event_type”：通知类型 - “event_severity”：告警级别 - “event_name”：事件名称 - “namespace”：命名空间 - “clusterId”：集群id - “customField”：用户自定义字段
        :type monitor_objects: list[dict(str, str)]
        :param trigger_conditions: 触发条件。
        :type trigger_conditions: list[:class:`huaweicloudsdkaom.v2.EventTriggerCondition`]
        :param alarm_rule_template_bind_enable: 是否绑定告警规则模版（废弃）。
        :type alarm_rule_template_bind_enable: bool
        :param alarm_rule_template_id: 告警规则模版id（废弃）。
        :type alarm_rule_template_id: str
        """
        
        

        self._alarm_source = None
        self._event_source = None
        self._monitor_objects = None
        self._trigger_conditions = None
        self._alarm_rule_template_bind_enable = None
        self._alarm_rule_template_id = None
        self.discriminator = None

        if alarm_source is not None:
            self.alarm_source = alarm_source
        if event_source is not None:
            self.event_source = event_source
        if monitor_objects is not None:
            self.monitor_objects = monitor_objects
        if trigger_conditions is not None:
            self.trigger_conditions = trigger_conditions
        if alarm_rule_template_bind_enable is not None:
            self.alarm_rule_template_bind_enable = alarm_rule_template_bind_enable
        if alarm_rule_template_id is not None:
            self.alarm_rule_template_id = alarm_rule_template_id

    @property
    def alarm_source(self):
        r"""Gets the alarm_source of this EventAlarmSpec.

        告警规则来源。 - “systemEvent”：系统事件 - “customEvent”：自定义事件

        :return: The alarm_source of this EventAlarmSpec.
        :rtype: str
        """
        return self._alarm_source

    @alarm_source.setter
    def alarm_source(self, alarm_source):
        r"""Sets the alarm_source of this EventAlarmSpec.

        告警规则来源。 - “systemEvent”：系统事件 - “customEvent”：自定义事件

        :param alarm_source: The alarm_source of this EventAlarmSpec.
        :type alarm_source: str
        """
        self._alarm_source = alarm_source

    @property
    def event_source(self):
        r"""Gets the event_source of this EventAlarmSpec.

        告警来源。 - “RDS” - “EVS” - “CCE” - “LTS” - “AOM”

        :return: The event_source of this EventAlarmSpec.
        :rtype: str
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        r"""Sets the event_source of this EventAlarmSpec.

        告警来源。 - “RDS” - “EVS” - “CCE” - “LTS” - “AOM”

        :param event_source: The event_source of this EventAlarmSpec.
        :type event_source: str
        """
        self._event_source = event_source

    @property
    def monitor_objects(self):
        r"""Gets the monitor_objects of this EventAlarmSpec.

        监控对象列表。键值对形式，键值为： - “event_type”：通知类型 - “event_severity”：告警级别 - “event_name”：事件名称 - “namespace”：命名空间 - “clusterId”：集群id - “customField”：用户自定义字段

        :return: The monitor_objects of this EventAlarmSpec.
        :rtype: list[dict(str, str)]
        """
        return self._monitor_objects

    @monitor_objects.setter
    def monitor_objects(self, monitor_objects):
        r"""Sets the monitor_objects of this EventAlarmSpec.

        监控对象列表。键值对形式，键值为： - “event_type”：通知类型 - “event_severity”：告警级别 - “event_name”：事件名称 - “namespace”：命名空间 - “clusterId”：集群id - “customField”：用户自定义字段

        :param monitor_objects: The monitor_objects of this EventAlarmSpec.
        :type monitor_objects: list[dict(str, str)]
        """
        self._monitor_objects = monitor_objects

    @property
    def trigger_conditions(self):
        r"""Gets the trigger_conditions of this EventAlarmSpec.

        触发条件。

        :return: The trigger_conditions of this EventAlarmSpec.
        :rtype: list[:class:`huaweicloudsdkaom.v2.EventTriggerCondition`]
        """
        return self._trigger_conditions

    @trigger_conditions.setter
    def trigger_conditions(self, trigger_conditions):
        r"""Sets the trigger_conditions of this EventAlarmSpec.

        触发条件。

        :param trigger_conditions: The trigger_conditions of this EventAlarmSpec.
        :type trigger_conditions: list[:class:`huaweicloudsdkaom.v2.EventTriggerCondition`]
        """
        self._trigger_conditions = trigger_conditions

    @property
    def alarm_rule_template_bind_enable(self):
        r"""Gets the alarm_rule_template_bind_enable of this EventAlarmSpec.

        是否绑定告警规则模版（废弃）。

        :return: The alarm_rule_template_bind_enable of this EventAlarmSpec.
        :rtype: bool
        """
        return self._alarm_rule_template_bind_enable

    @alarm_rule_template_bind_enable.setter
    def alarm_rule_template_bind_enable(self, alarm_rule_template_bind_enable):
        r"""Sets the alarm_rule_template_bind_enable of this EventAlarmSpec.

        是否绑定告警规则模版（废弃）。

        :param alarm_rule_template_bind_enable: The alarm_rule_template_bind_enable of this EventAlarmSpec.
        :type alarm_rule_template_bind_enable: bool
        """
        self._alarm_rule_template_bind_enable = alarm_rule_template_bind_enable

    @property
    def alarm_rule_template_id(self):
        r"""Gets the alarm_rule_template_id of this EventAlarmSpec.

        告警规则模版id（废弃）。

        :return: The alarm_rule_template_id of this EventAlarmSpec.
        :rtype: str
        """
        return self._alarm_rule_template_id

    @alarm_rule_template_id.setter
    def alarm_rule_template_id(self, alarm_rule_template_id):
        r"""Sets the alarm_rule_template_id of this EventAlarmSpec.

        告警规则模版id（废弃）。

        :param alarm_rule_template_id: The alarm_rule_template_id of this EventAlarmSpec.
        :type alarm_rule_template_id: str
        """
        self._alarm_rule_template_id = alarm_rule_template_id

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
        if not isinstance(other, EventAlarmSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
