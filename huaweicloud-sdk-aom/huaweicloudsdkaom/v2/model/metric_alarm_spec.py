# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricAlarmSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'monitor_type': 'str',
        'no_data_conditions': 'list[NoDataCondition]',
        'alarm_tags': 'list[AlarmTags]',
        'monitor_objects': 'list[dict(str, str)]',
        'recovery_conditions': 'RecoveryCondition',
        'trigger_conditions': 'list[TriggerCondition]',
        'alarm_rule_template_bind_enable': 'bool',
        'alarm_rule_template_id': 'str'
    }

    attribute_map = {
        'monitor_type': 'monitor_type',
        'no_data_conditions': 'no_data_conditions',
        'alarm_tags': 'alarm_tags',
        'monitor_objects': 'monitor_objects',
        'recovery_conditions': 'recovery_conditions',
        'trigger_conditions': 'trigger_conditions',
        'alarm_rule_template_bind_enable': 'alarm_rule_template_bind_enable',
        'alarm_rule_template_id': 'alarm_rule_template_id'
    }

    def __init__(self, monitor_type=None, no_data_conditions=None, alarm_tags=None, monitor_objects=None, recovery_conditions=None, trigger_conditions=None, alarm_rule_template_bind_enable=None, alarm_rule_template_id=None):
        r"""MetricAlarmSpec

        The model defined in huaweicloud sdk

        :param monitor_type: 监控类型。 - “all_metric”：全量指标 - “promql”：PromQL - “resource”：（日落）资源类型
        :type monitor_type: str
        :param no_data_conditions: 无数据处理。
        :type no_data_conditions: list[:class:`huaweicloudsdkaom.v2.NoDataCondition`]
        :param alarm_tags: 告警标签。
        :type alarm_tags: list[:class:`huaweicloudsdkaom.v2.AlarmTags`]
        :param monitor_objects: 监控对象列表。
        :type monitor_objects: list[dict(str, str)]
        :param recovery_conditions: 
        :type recovery_conditions: :class:`huaweicloudsdkaom.v2.RecoveryCondition`
        :param trigger_conditions: 触发条件。
        :type trigger_conditions: list[:class:`huaweicloudsdkaom.v2.TriggerCondition`]
        :param alarm_rule_template_bind_enable: 是否绑定告警规则模版（废弃）。
        :type alarm_rule_template_bind_enable: bool
        :param alarm_rule_template_id: 告警规则模版id（废弃）。
        :type alarm_rule_template_id: str
        """
        
        

        self._monitor_type = None
        self._no_data_conditions = None
        self._alarm_tags = None
        self._monitor_objects = None
        self._recovery_conditions = None
        self._trigger_conditions = None
        self._alarm_rule_template_bind_enable = None
        self._alarm_rule_template_id = None
        self.discriminator = None

        self.monitor_type = monitor_type
        if no_data_conditions is not None:
            self.no_data_conditions = no_data_conditions
        self.alarm_tags = alarm_tags
        if monitor_objects is not None:
            self.monitor_objects = monitor_objects
        self.recovery_conditions = recovery_conditions
        self.trigger_conditions = trigger_conditions
        if alarm_rule_template_bind_enable is not None:
            self.alarm_rule_template_bind_enable = alarm_rule_template_bind_enable
        if alarm_rule_template_id is not None:
            self.alarm_rule_template_id = alarm_rule_template_id

    @property
    def monitor_type(self):
        r"""Gets the monitor_type of this MetricAlarmSpec.

        监控类型。 - “all_metric”：全量指标 - “promql”：PromQL - “resource”：（日落）资源类型

        :return: The monitor_type of this MetricAlarmSpec.
        :rtype: str
        """
        return self._monitor_type

    @monitor_type.setter
    def monitor_type(self, monitor_type):
        r"""Sets the monitor_type of this MetricAlarmSpec.

        监控类型。 - “all_metric”：全量指标 - “promql”：PromQL - “resource”：（日落）资源类型

        :param monitor_type: The monitor_type of this MetricAlarmSpec.
        :type monitor_type: str
        """
        self._monitor_type = monitor_type

    @property
    def no_data_conditions(self):
        r"""Gets the no_data_conditions of this MetricAlarmSpec.

        无数据处理。

        :return: The no_data_conditions of this MetricAlarmSpec.
        :rtype: list[:class:`huaweicloudsdkaom.v2.NoDataCondition`]
        """
        return self._no_data_conditions

    @no_data_conditions.setter
    def no_data_conditions(self, no_data_conditions):
        r"""Sets the no_data_conditions of this MetricAlarmSpec.

        无数据处理。

        :param no_data_conditions: The no_data_conditions of this MetricAlarmSpec.
        :type no_data_conditions: list[:class:`huaweicloudsdkaom.v2.NoDataCondition`]
        """
        self._no_data_conditions = no_data_conditions

    @property
    def alarm_tags(self):
        r"""Gets the alarm_tags of this MetricAlarmSpec.

        告警标签。

        :return: The alarm_tags of this MetricAlarmSpec.
        :rtype: list[:class:`huaweicloudsdkaom.v2.AlarmTags`]
        """
        return self._alarm_tags

    @alarm_tags.setter
    def alarm_tags(self, alarm_tags):
        r"""Sets the alarm_tags of this MetricAlarmSpec.

        告警标签。

        :param alarm_tags: The alarm_tags of this MetricAlarmSpec.
        :type alarm_tags: list[:class:`huaweicloudsdkaom.v2.AlarmTags`]
        """
        self._alarm_tags = alarm_tags

    @property
    def monitor_objects(self):
        r"""Gets the monitor_objects of this MetricAlarmSpec.

        监控对象列表。

        :return: The monitor_objects of this MetricAlarmSpec.
        :rtype: list[dict(str, str)]
        """
        return self._monitor_objects

    @monitor_objects.setter
    def monitor_objects(self, monitor_objects):
        r"""Sets the monitor_objects of this MetricAlarmSpec.

        监控对象列表。

        :param monitor_objects: The monitor_objects of this MetricAlarmSpec.
        :type monitor_objects: list[dict(str, str)]
        """
        self._monitor_objects = monitor_objects

    @property
    def recovery_conditions(self):
        r"""Gets the recovery_conditions of this MetricAlarmSpec.

        :return: The recovery_conditions of this MetricAlarmSpec.
        :rtype: :class:`huaweicloudsdkaom.v2.RecoveryCondition`
        """
        return self._recovery_conditions

    @recovery_conditions.setter
    def recovery_conditions(self, recovery_conditions):
        r"""Sets the recovery_conditions of this MetricAlarmSpec.

        :param recovery_conditions: The recovery_conditions of this MetricAlarmSpec.
        :type recovery_conditions: :class:`huaweicloudsdkaom.v2.RecoveryCondition`
        """
        self._recovery_conditions = recovery_conditions

    @property
    def trigger_conditions(self):
        r"""Gets the trigger_conditions of this MetricAlarmSpec.

        触发条件。

        :return: The trigger_conditions of this MetricAlarmSpec.
        :rtype: list[:class:`huaweicloudsdkaom.v2.TriggerCondition`]
        """
        return self._trigger_conditions

    @trigger_conditions.setter
    def trigger_conditions(self, trigger_conditions):
        r"""Sets the trigger_conditions of this MetricAlarmSpec.

        触发条件。

        :param trigger_conditions: The trigger_conditions of this MetricAlarmSpec.
        :type trigger_conditions: list[:class:`huaweicloudsdkaom.v2.TriggerCondition`]
        """
        self._trigger_conditions = trigger_conditions

    @property
    def alarm_rule_template_bind_enable(self):
        r"""Gets the alarm_rule_template_bind_enable of this MetricAlarmSpec.

        是否绑定告警规则模版（废弃）。

        :return: The alarm_rule_template_bind_enable of this MetricAlarmSpec.
        :rtype: bool
        """
        return self._alarm_rule_template_bind_enable

    @alarm_rule_template_bind_enable.setter
    def alarm_rule_template_bind_enable(self, alarm_rule_template_bind_enable):
        r"""Sets the alarm_rule_template_bind_enable of this MetricAlarmSpec.

        是否绑定告警规则模版（废弃）。

        :param alarm_rule_template_bind_enable: The alarm_rule_template_bind_enable of this MetricAlarmSpec.
        :type alarm_rule_template_bind_enable: bool
        """
        self._alarm_rule_template_bind_enable = alarm_rule_template_bind_enable

    @property
    def alarm_rule_template_id(self):
        r"""Gets the alarm_rule_template_id of this MetricAlarmSpec.

        告警规则模版id（废弃）。

        :return: The alarm_rule_template_id of this MetricAlarmSpec.
        :rtype: str
        """
        return self._alarm_rule_template_id

    @alarm_rule_template_id.setter
    def alarm_rule_template_id(self, alarm_rule_template_id):
        r"""Sets the alarm_rule_template_id of this MetricAlarmSpec.

        告警规则模版id（废弃）。

        :param alarm_rule_template_id: The alarm_rule_template_id of this MetricAlarmSpec.
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
        if not isinstance(other, MetricAlarmSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
