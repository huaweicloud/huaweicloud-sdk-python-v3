# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventAlarmTemplateSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_subtype': 'str',
        'alarm_source': 'str',
        'event_source': 'str',
        'monitor_object_templates': 'list[str]',
        'monitor_objects': 'list[dict(str, str)]',
        'trigger_conditions': 'list[EventTriggerCondition]'
    }

    attribute_map = {
        'alarm_subtype': 'alarm_subtype',
        'alarm_source': 'alarm_source',
        'event_source': 'event_source',
        'monitor_object_templates': 'monitor_object_templates',
        'monitor_objects': 'monitor_objects',
        'trigger_conditions': 'trigger_conditions'
    }

    def __init__(self, alarm_subtype=None, alarm_source=None, event_source=None, monitor_object_templates=None, monitor_objects=None, trigger_conditions=None):
        r"""EventAlarmTemplateSpec

        The model defined in huaweicloud sdk

        :param alarm_subtype: 告警规则类别。
        :type alarm_subtype: str
        :param alarm_source: 告警规则来源云服务：CCE 创建标识。
        :type alarm_source: str
        :param event_source: 告警来源。
        :type event_source: str
        :param monitor_object_templates: 监控对象模板（创建告警时需要补齐里面的内容）。
        :type monitor_object_templates: list[str]
        :param monitor_objects: 监控对象列表。键值对形式，键值为： - “event_type”：通知类型 - “event_severity”：告警级别 - “event_name”：事件名称 - “namespace”：命名空间 - “clusterId”：集群id - “customField”：用户自定义字段
        :type monitor_objects: list[dict(str, str)]
        :param trigger_conditions: 触发条件。
        :type trigger_conditions: list[:class:`huaweicloudsdkaom.v2.EventTriggerCondition`]
        """
        
        

        self._alarm_subtype = None
        self._alarm_source = None
        self._event_source = None
        self._monitor_object_templates = None
        self._monitor_objects = None
        self._trigger_conditions = None
        self.discriminator = None

        if alarm_subtype is not None:
            self.alarm_subtype = alarm_subtype
        if alarm_source is not None:
            self.alarm_source = alarm_source
        if event_source is not None:
            self.event_source = event_source
        if monitor_object_templates is not None:
            self.monitor_object_templates = monitor_object_templates
        if monitor_objects is not None:
            self.monitor_objects = monitor_objects
        if trigger_conditions is not None:
            self.trigger_conditions = trigger_conditions

    @property
    def alarm_subtype(self):
        r"""Gets the alarm_subtype of this EventAlarmTemplateSpec.

        告警规则类别。

        :return: The alarm_subtype of this EventAlarmTemplateSpec.
        :rtype: str
        """
        return self._alarm_subtype

    @alarm_subtype.setter
    def alarm_subtype(self, alarm_subtype):
        r"""Sets the alarm_subtype of this EventAlarmTemplateSpec.

        告警规则类别。

        :param alarm_subtype: The alarm_subtype of this EventAlarmTemplateSpec.
        :type alarm_subtype: str
        """
        self._alarm_subtype = alarm_subtype

    @property
    def alarm_source(self):
        r"""Gets the alarm_source of this EventAlarmTemplateSpec.

        告警规则来源云服务：CCE 创建标识。

        :return: The alarm_source of this EventAlarmTemplateSpec.
        :rtype: str
        """
        return self._alarm_source

    @alarm_source.setter
    def alarm_source(self, alarm_source):
        r"""Sets the alarm_source of this EventAlarmTemplateSpec.

        告警规则来源云服务：CCE 创建标识。

        :param alarm_source: The alarm_source of this EventAlarmTemplateSpec.
        :type alarm_source: str
        """
        self._alarm_source = alarm_source

    @property
    def event_source(self):
        r"""Gets the event_source of this EventAlarmTemplateSpec.

        告警来源。

        :return: The event_source of this EventAlarmTemplateSpec.
        :rtype: str
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        r"""Sets the event_source of this EventAlarmTemplateSpec.

        告警来源。

        :param event_source: The event_source of this EventAlarmTemplateSpec.
        :type event_source: str
        """
        self._event_source = event_source

    @property
    def monitor_object_templates(self):
        r"""Gets the monitor_object_templates of this EventAlarmTemplateSpec.

        监控对象模板（创建告警时需要补齐里面的内容）。

        :return: The monitor_object_templates of this EventAlarmTemplateSpec.
        :rtype: list[str]
        """
        return self._monitor_object_templates

    @monitor_object_templates.setter
    def monitor_object_templates(self, monitor_object_templates):
        r"""Sets the monitor_object_templates of this EventAlarmTemplateSpec.

        监控对象模板（创建告警时需要补齐里面的内容）。

        :param monitor_object_templates: The monitor_object_templates of this EventAlarmTemplateSpec.
        :type monitor_object_templates: list[str]
        """
        self._monitor_object_templates = monitor_object_templates

    @property
    def monitor_objects(self):
        r"""Gets the monitor_objects of this EventAlarmTemplateSpec.

        监控对象列表。键值对形式，键值为： - “event_type”：通知类型 - “event_severity”：告警级别 - “event_name”：事件名称 - “namespace”：命名空间 - “clusterId”：集群id - “customField”：用户自定义字段

        :return: The monitor_objects of this EventAlarmTemplateSpec.
        :rtype: list[dict(str, str)]
        """
        return self._monitor_objects

    @monitor_objects.setter
    def monitor_objects(self, monitor_objects):
        r"""Sets the monitor_objects of this EventAlarmTemplateSpec.

        监控对象列表。键值对形式，键值为： - “event_type”：通知类型 - “event_severity”：告警级别 - “event_name”：事件名称 - “namespace”：命名空间 - “clusterId”：集群id - “customField”：用户自定义字段

        :param monitor_objects: The monitor_objects of this EventAlarmTemplateSpec.
        :type monitor_objects: list[dict(str, str)]
        """
        self._monitor_objects = monitor_objects

    @property
    def trigger_conditions(self):
        r"""Gets the trigger_conditions of this EventAlarmTemplateSpec.

        触发条件。

        :return: The trigger_conditions of this EventAlarmTemplateSpec.
        :rtype: list[:class:`huaweicloudsdkaom.v2.EventTriggerCondition`]
        """
        return self._trigger_conditions

    @trigger_conditions.setter
    def trigger_conditions(self, trigger_conditions):
        r"""Sets the trigger_conditions of this EventAlarmTemplateSpec.

        触发条件。

        :param trigger_conditions: The trigger_conditions of this EventAlarmTemplateSpec.
        :type trigger_conditions: list[:class:`huaweicloudsdkaom.v2.EventTriggerCondition`]
        """
        self._trigger_conditions = trigger_conditions

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventAlarmTemplateSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
