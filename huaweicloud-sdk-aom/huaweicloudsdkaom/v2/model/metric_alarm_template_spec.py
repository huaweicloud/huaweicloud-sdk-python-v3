# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricAlarmTemplateSpec:

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
        'monitor_type': 'str',
        'trigger_conditions': 'list[TemplateTriggerCondition]',
        'no_data_conditions': 'list[NoDataCondition]',
        'alarm_tags': 'list[AlarmTags]',
        'recovery_conditions': 'RecoveryCondition'
    }

    attribute_map = {
        'alarm_subtype': 'alarm_subtype',
        'alarm_source': 'alarm_source',
        'monitor_type': 'monitor_type',
        'trigger_conditions': 'trigger_conditions',
        'no_data_conditions': 'no_data_conditions',
        'alarm_tags': 'alarm_tags',
        'recovery_conditions': 'recovery_conditions'
    }

    def __init__(self, alarm_subtype=None, alarm_source=None, monitor_type=None, trigger_conditions=None, no_data_conditions=None, alarm_tags=None, recovery_conditions=None):
        r"""MetricAlarmTemplateSpec

        The model defined in huaweicloud sdk

        :param alarm_subtype: 告警规则类别。
        :type alarm_subtype: str
        :param alarm_source: 告警规则来源云服务：CCE 创建标识。
        :type alarm_source: str
        :param monitor_type: 监控类型。
        :type monitor_type: str
        :param trigger_conditions: 触发条件。
        :type trigger_conditions: list[:class:`huaweicloudsdkaom.v2.TemplateTriggerCondition`]
        :param no_data_conditions: 数据不足条件。
        :type no_data_conditions: list[:class:`huaweicloudsdkaom.v2.NoDataCondition`]
        :param alarm_tags: 告警标签。
        :type alarm_tags: list[:class:`huaweicloudsdkaom.v2.AlarmTags`]
        :param recovery_conditions: 
        :type recovery_conditions: :class:`huaweicloudsdkaom.v2.RecoveryCondition`
        """
        
        

        self._alarm_subtype = None
        self._alarm_source = None
        self._monitor_type = None
        self._trigger_conditions = None
        self._no_data_conditions = None
        self._alarm_tags = None
        self._recovery_conditions = None
        self.discriminator = None

        if alarm_subtype is not None:
            self.alarm_subtype = alarm_subtype
        if alarm_source is not None:
            self.alarm_source = alarm_source
        if monitor_type is not None:
            self.monitor_type = monitor_type
        if trigger_conditions is not None:
            self.trigger_conditions = trigger_conditions
        if no_data_conditions is not None:
            self.no_data_conditions = no_data_conditions
        if alarm_tags is not None:
            self.alarm_tags = alarm_tags
        if recovery_conditions is not None:
            self.recovery_conditions = recovery_conditions

    @property
    def alarm_subtype(self):
        r"""Gets the alarm_subtype of this MetricAlarmTemplateSpec.

        告警规则类别。

        :return: The alarm_subtype of this MetricAlarmTemplateSpec.
        :rtype: str
        """
        return self._alarm_subtype

    @alarm_subtype.setter
    def alarm_subtype(self, alarm_subtype):
        r"""Sets the alarm_subtype of this MetricAlarmTemplateSpec.

        告警规则类别。

        :param alarm_subtype: The alarm_subtype of this MetricAlarmTemplateSpec.
        :type alarm_subtype: str
        """
        self._alarm_subtype = alarm_subtype

    @property
    def alarm_source(self):
        r"""Gets the alarm_source of this MetricAlarmTemplateSpec.

        告警规则来源云服务：CCE 创建标识。

        :return: The alarm_source of this MetricAlarmTemplateSpec.
        :rtype: str
        """
        return self._alarm_source

    @alarm_source.setter
    def alarm_source(self, alarm_source):
        r"""Sets the alarm_source of this MetricAlarmTemplateSpec.

        告警规则来源云服务：CCE 创建标识。

        :param alarm_source: The alarm_source of this MetricAlarmTemplateSpec.
        :type alarm_source: str
        """
        self._alarm_source = alarm_source

    @property
    def monitor_type(self):
        r"""Gets the monitor_type of this MetricAlarmTemplateSpec.

        监控类型。

        :return: The monitor_type of this MetricAlarmTemplateSpec.
        :rtype: str
        """
        return self._monitor_type

    @monitor_type.setter
    def monitor_type(self, monitor_type):
        r"""Sets the monitor_type of this MetricAlarmTemplateSpec.

        监控类型。

        :param monitor_type: The monitor_type of this MetricAlarmTemplateSpec.
        :type monitor_type: str
        """
        self._monitor_type = monitor_type

    @property
    def trigger_conditions(self):
        r"""Gets the trigger_conditions of this MetricAlarmTemplateSpec.

        触发条件。

        :return: The trigger_conditions of this MetricAlarmTemplateSpec.
        :rtype: list[:class:`huaweicloudsdkaom.v2.TemplateTriggerCondition`]
        """
        return self._trigger_conditions

    @trigger_conditions.setter
    def trigger_conditions(self, trigger_conditions):
        r"""Sets the trigger_conditions of this MetricAlarmTemplateSpec.

        触发条件。

        :param trigger_conditions: The trigger_conditions of this MetricAlarmTemplateSpec.
        :type trigger_conditions: list[:class:`huaweicloudsdkaom.v2.TemplateTriggerCondition`]
        """
        self._trigger_conditions = trigger_conditions

    @property
    def no_data_conditions(self):
        r"""Gets the no_data_conditions of this MetricAlarmTemplateSpec.

        数据不足条件。

        :return: The no_data_conditions of this MetricAlarmTemplateSpec.
        :rtype: list[:class:`huaweicloudsdkaom.v2.NoDataCondition`]
        """
        return self._no_data_conditions

    @no_data_conditions.setter
    def no_data_conditions(self, no_data_conditions):
        r"""Sets the no_data_conditions of this MetricAlarmTemplateSpec.

        数据不足条件。

        :param no_data_conditions: The no_data_conditions of this MetricAlarmTemplateSpec.
        :type no_data_conditions: list[:class:`huaweicloudsdkaom.v2.NoDataCondition`]
        """
        self._no_data_conditions = no_data_conditions

    @property
    def alarm_tags(self):
        r"""Gets the alarm_tags of this MetricAlarmTemplateSpec.

        告警标签。

        :return: The alarm_tags of this MetricAlarmTemplateSpec.
        :rtype: list[:class:`huaweicloudsdkaom.v2.AlarmTags`]
        """
        return self._alarm_tags

    @alarm_tags.setter
    def alarm_tags(self, alarm_tags):
        r"""Sets the alarm_tags of this MetricAlarmTemplateSpec.

        告警标签。

        :param alarm_tags: The alarm_tags of this MetricAlarmTemplateSpec.
        :type alarm_tags: list[:class:`huaweicloudsdkaom.v2.AlarmTags`]
        """
        self._alarm_tags = alarm_tags

    @property
    def recovery_conditions(self):
        r"""Gets the recovery_conditions of this MetricAlarmTemplateSpec.

        :return: The recovery_conditions of this MetricAlarmTemplateSpec.
        :rtype: :class:`huaweicloudsdkaom.v2.RecoveryCondition`
        """
        return self._recovery_conditions

    @recovery_conditions.setter
    def recovery_conditions(self, recovery_conditions):
        r"""Sets the recovery_conditions of this MetricAlarmTemplateSpec.

        :param recovery_conditions: The recovery_conditions of this MetricAlarmTemplateSpec.
        :type recovery_conditions: :class:`huaweicloudsdkaom.v2.RecoveryCondition`
        """
        self._recovery_conditions = recovery_conditions

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
        if not isinstance(other, MetricAlarmTemplateSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
