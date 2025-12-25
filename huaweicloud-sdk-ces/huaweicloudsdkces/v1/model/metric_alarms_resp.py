# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricAlarmsResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_name': 'str',
        'alarm_description': 'str',
        'relation_id': 'str',
        'metric': 'ListAlarmMetricResp',
        'condition': 'AlarmRuleConditionResp',
        'alarm_enabled': 'bool',
        'alarm_level': 'int',
        'alarm_type': 'str',
        'alarm_action_enabled': 'bool',
        'ignore_insufficient_data': 'bool',
        'alarm_actions': 'list[NotificationResp]',
        'ok_actions': 'list[NotificationResp]',
        'insufficientdata_actions': 'list[NotificationResp]',
        'alarm_action_begin_time': 'str',
        'alarm_action_end_time': 'str',
        'effective_timezone': 'str',
        'alarm_id': 'str',
        'update_time': 'int',
        'alarm_state': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'alarm_name': 'alarm_name',
        'alarm_description': 'alarm_description',
        'relation_id': 'relation_id',
        'metric': 'metric',
        'condition': 'condition',
        'alarm_enabled': 'alarm_enabled',
        'alarm_level': 'alarm_level',
        'alarm_type': 'alarm_type',
        'alarm_action_enabled': 'alarm_action_enabled',
        'ignore_insufficient_data': 'ignore_insufficient_data',
        'alarm_actions': 'alarm_actions',
        'ok_actions': 'ok_actions',
        'insufficientdata_actions': 'insufficientdata_actions',
        'alarm_action_begin_time': 'alarm_action_begin_time',
        'alarm_action_end_time': 'alarm_action_end_time',
        'effective_timezone': 'effective_timezone',
        'alarm_id': 'alarm_id',
        'update_time': 'update_time',
        'alarm_state': 'alarm_state',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, alarm_name=None, alarm_description=None, relation_id=None, metric=None, condition=None, alarm_enabled=None, alarm_level=None, alarm_type=None, alarm_action_enabled=None, ignore_insufficient_data=None, alarm_actions=None, ok_actions=None, insufficientdata_actions=None, alarm_action_begin_time=None, alarm_action_end_time=None, effective_timezone=None, alarm_id=None, update_time=None, alarm_state=None, enterprise_project_id=None):
        r"""MetricAlarmsResp

        The model defined in huaweicloud sdk

        :param alarm_name: **参数解释**： 告警名称。 **取值范围**： 只能包含0-9/a-z/A-Z/_/-或汉字，字符长度为[1,128]。 
        :type alarm_name: str
        :param alarm_description: **参数解释**： 告警描述。 **取值范围**： 长度[0,256]个字符。 
        :type alarm_description: str
        :param relation_id: **参数解释**： 告警规则的ID或者资源分组ID。 **取值范围**： 不涉及 
        :type relation_id: str
        :param metric: 
        :type metric: :class:`huaweicloudsdkces.v1.ListAlarmMetricResp`
        :param condition: 
        :type condition: :class:`huaweicloudsdkces.v1.AlarmRuleConditionResp`
        :param alarm_enabled: **参数解释**： 是否启用该条告警。 **取值范围**： 布尔值。 - true:开启。 - false:关闭。 
        :type alarm_enabled: bool
        :param alarm_level: **参数解释**： 告警级别。 **取值范围**： 取值为1、2、3、4 - 1：紧急 - 2：重要 - 3：次要 - 4：提示 
        :type alarm_level: int
        :param alarm_type: **参数解释**： 告警类型。 **取值范围**： 针对事件类型的告警时，告警类型为EVENT.SYS（系统事件）或EVENT.CUSTOM（自定义事件）。 针对资源分组的告警时，告警类型为RESOURCE_GROUP。 针对指定资源的告警时，告警类型为MULTI_INSTANCE。 - EVENT.SYS：针对系统事件的告警类型 - EVENT.CUSTOM：针对自定义事件的告警类型 - RESOURCE_GROUP：针对资源分组的告警类型 - MULTI_INSTANCE：指定资源的告警类型 
        :type alarm_type: str
        :param alarm_action_enabled: **参数解释**： 该条告警触发时，是否开启告警通知。 **取值范围**： 布尔值。 - true：开启告警通知。 - false：不开启告警通知。 
        :type alarm_action_enabled: bool
        :param ignore_insufficient_data: **参数解释**： 数据不足时，是否产生告警记录(不会发送通知)。 **取值范围**： 值为true或者false - true：数据不足时，产生告警记录 - false：数据不足时，不产生告警记录 
        :type ignore_insufficient_data: bool
        :param alarm_actions: **参数解释**： 告警触发时，通知组/主题订阅的信息。 
        :type alarm_actions: list[:class:`huaweicloudsdkces.v1.NotificationResp`]
        :param ok_actions: **参数解释**： 告警触发时，通知组/主题订阅的信息。 
        :type ok_actions: list[:class:`huaweicloudsdkces.v1.NotificationResp`]
        :param insufficientdata_actions: **参数解释**： 告警触发时，通知组/主题订阅的信息。 
        :type insufficientdata_actions: list[:class:`huaweicloudsdkces.v1.NotificationResp`]
        :param alarm_action_begin_time: **参数解释**： 告警规则生效的开始时间，告警规则仅在生效时间内发送通知消息。例如alarm_action_begin_time为8:00，alarm_action_end_time为20:00时，则对应的告警规则仅在08:00-20:00发送通知消息。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 
        :type alarm_action_begin_time: str
        :param alarm_action_end_time: **参数解释**： 告警规则生效的结束时间，告警规则仅在生效时间内发送通知消息。例如alarm_action_begin_time为8:00，alarm_action_end_time为20:00时，则对应的告警规则仅在08:00-20:00发送通知消息。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 
        :type alarm_action_end_time: str
        :param effective_timezone: **参数解释**： 时区，形如：\&quot;GMT-08:00\&quot;、\&quot;GMT+08:00\&quot;、\&quot;GMT+0:00\&quot; **取值范围**： 长度为[1,16]个字符。 
        :type effective_timezone: str
        :param alarm_id: **参数解释**： 告警规则的ID。 **取值范围**： 以al开头，后跟22个数字或字母。字符长度为24 
        :type alarm_id: str
        :param update_time: **参数解释**： 告警状态变更的时间，UNIX时间戳，单位毫秒。 **取值范围** 0 - 9999999999999 
        :type update_time: int
        :param alarm_state: **参数解释**： 告警状态。 **取值范围**： 只能为ok、alarm、insufficient_data。 - ok：正常 - alarm：告警 - insufficient_data：数据不足 
        :type alarm_state: str
        :param enterprise_project_id: **参数解释**： 企业项目ID。 **取值范围**： 只能包含小写字母、数字、“-”、“_”，长度为36个字符。也可取值0或all_granted_eps。0：代表默认企业项目ID，all_granted_eps：代表所有企业项目ID。 
        :type enterprise_project_id: str
        """
        
        

        self._alarm_name = None
        self._alarm_description = None
        self._relation_id = None
        self._metric = None
        self._condition = None
        self._alarm_enabled = None
        self._alarm_level = None
        self._alarm_type = None
        self._alarm_action_enabled = None
        self._ignore_insufficient_data = None
        self._alarm_actions = None
        self._ok_actions = None
        self._insufficientdata_actions = None
        self._alarm_action_begin_time = None
        self._alarm_action_end_time = None
        self._effective_timezone = None
        self._alarm_id = None
        self._update_time = None
        self._alarm_state = None
        self._enterprise_project_id = None
        self.discriminator = None

        if alarm_name is not None:
            self.alarm_name = alarm_name
        if alarm_description is not None:
            self.alarm_description = alarm_description
        if relation_id is not None:
            self.relation_id = relation_id
        if metric is not None:
            self.metric = metric
        if condition is not None:
            self.condition = condition
        if alarm_enabled is not None:
            self.alarm_enabled = alarm_enabled
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if alarm_type is not None:
            self.alarm_type = alarm_type
        if alarm_action_enabled is not None:
            self.alarm_action_enabled = alarm_action_enabled
        if ignore_insufficient_data is not None:
            self.ignore_insufficient_data = ignore_insufficient_data
        if alarm_actions is not None:
            self.alarm_actions = alarm_actions
        if ok_actions is not None:
            self.ok_actions = ok_actions
        if insufficientdata_actions is not None:
            self.insufficientdata_actions = insufficientdata_actions
        if alarm_action_begin_time is not None:
            self.alarm_action_begin_time = alarm_action_begin_time
        if alarm_action_end_time is not None:
            self.alarm_action_end_time = alarm_action_end_time
        if effective_timezone is not None:
            self.effective_timezone = effective_timezone
        if alarm_id is not None:
            self.alarm_id = alarm_id
        if update_time is not None:
            self.update_time = update_time
        if alarm_state is not None:
            self.alarm_state = alarm_state
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def alarm_name(self):
        r"""Gets the alarm_name of this MetricAlarmsResp.

        **参数解释**： 告警名称。 **取值范围**： 只能包含0-9/a-z/A-Z/_/-或汉字，字符长度为[1,128]。 

        :return: The alarm_name of this MetricAlarmsResp.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        r"""Sets the alarm_name of this MetricAlarmsResp.

        **参数解释**： 告警名称。 **取值范围**： 只能包含0-9/a-z/A-Z/_/-或汉字，字符长度为[1,128]。 

        :param alarm_name: The alarm_name of this MetricAlarmsResp.
        :type alarm_name: str
        """
        self._alarm_name = alarm_name

    @property
    def alarm_description(self):
        r"""Gets the alarm_description of this MetricAlarmsResp.

        **参数解释**： 告警描述。 **取值范围**： 长度[0,256]个字符。 

        :return: The alarm_description of this MetricAlarmsResp.
        :rtype: str
        """
        return self._alarm_description

    @alarm_description.setter
    def alarm_description(self, alarm_description):
        r"""Sets the alarm_description of this MetricAlarmsResp.

        **参数解释**： 告警描述。 **取值范围**： 长度[0,256]个字符。 

        :param alarm_description: The alarm_description of this MetricAlarmsResp.
        :type alarm_description: str
        """
        self._alarm_description = alarm_description

    @property
    def relation_id(self):
        r"""Gets the relation_id of this MetricAlarmsResp.

        **参数解释**： 告警规则的ID或者资源分组ID。 **取值范围**： 不涉及 

        :return: The relation_id of this MetricAlarmsResp.
        :rtype: str
        """
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        r"""Sets the relation_id of this MetricAlarmsResp.

        **参数解释**： 告警规则的ID或者资源分组ID。 **取值范围**： 不涉及 

        :param relation_id: The relation_id of this MetricAlarmsResp.
        :type relation_id: str
        """
        self._relation_id = relation_id

    @property
    def metric(self):
        r"""Gets the metric of this MetricAlarmsResp.

        :return: The metric of this MetricAlarmsResp.
        :rtype: :class:`huaweicloudsdkces.v1.ListAlarmMetricResp`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this MetricAlarmsResp.

        :param metric: The metric of this MetricAlarmsResp.
        :type metric: :class:`huaweicloudsdkces.v1.ListAlarmMetricResp`
        """
        self._metric = metric

    @property
    def condition(self):
        r"""Gets the condition of this MetricAlarmsResp.

        :return: The condition of this MetricAlarmsResp.
        :rtype: :class:`huaweicloudsdkces.v1.AlarmRuleConditionResp`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this MetricAlarmsResp.

        :param condition: The condition of this MetricAlarmsResp.
        :type condition: :class:`huaweicloudsdkces.v1.AlarmRuleConditionResp`
        """
        self._condition = condition

    @property
    def alarm_enabled(self):
        r"""Gets the alarm_enabled of this MetricAlarmsResp.

        **参数解释**： 是否启用该条告警。 **取值范围**： 布尔值。 - true:开启。 - false:关闭。 

        :return: The alarm_enabled of this MetricAlarmsResp.
        :rtype: bool
        """
        return self._alarm_enabled

    @alarm_enabled.setter
    def alarm_enabled(self, alarm_enabled):
        r"""Sets the alarm_enabled of this MetricAlarmsResp.

        **参数解释**： 是否启用该条告警。 **取值范围**： 布尔值。 - true:开启。 - false:关闭。 

        :param alarm_enabled: The alarm_enabled of this MetricAlarmsResp.
        :type alarm_enabled: bool
        """
        self._alarm_enabled = alarm_enabled

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this MetricAlarmsResp.

        **参数解释**： 告警级别。 **取值范围**： 取值为1、2、3、4 - 1：紧急 - 2：重要 - 3：次要 - 4：提示 

        :return: The alarm_level of this MetricAlarmsResp.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this MetricAlarmsResp.

        **参数解释**： 告警级别。 **取值范围**： 取值为1、2、3、4 - 1：紧急 - 2：重要 - 3：次要 - 4：提示 

        :param alarm_level: The alarm_level of this MetricAlarmsResp.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def alarm_type(self):
        r"""Gets the alarm_type of this MetricAlarmsResp.

        **参数解释**： 告警类型。 **取值范围**： 针对事件类型的告警时，告警类型为EVENT.SYS（系统事件）或EVENT.CUSTOM（自定义事件）。 针对资源分组的告警时，告警类型为RESOURCE_GROUP。 针对指定资源的告警时，告警类型为MULTI_INSTANCE。 - EVENT.SYS：针对系统事件的告警类型 - EVENT.CUSTOM：针对自定义事件的告警类型 - RESOURCE_GROUP：针对资源分组的告警类型 - MULTI_INSTANCE：指定资源的告警类型 

        :return: The alarm_type of this MetricAlarmsResp.
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        r"""Sets the alarm_type of this MetricAlarmsResp.

        **参数解释**： 告警类型。 **取值范围**： 针对事件类型的告警时，告警类型为EVENT.SYS（系统事件）或EVENT.CUSTOM（自定义事件）。 针对资源分组的告警时，告警类型为RESOURCE_GROUP。 针对指定资源的告警时，告警类型为MULTI_INSTANCE。 - EVENT.SYS：针对系统事件的告警类型 - EVENT.CUSTOM：针对自定义事件的告警类型 - RESOURCE_GROUP：针对资源分组的告警类型 - MULTI_INSTANCE：指定资源的告警类型 

        :param alarm_type: The alarm_type of this MetricAlarmsResp.
        :type alarm_type: str
        """
        self._alarm_type = alarm_type

    @property
    def alarm_action_enabled(self):
        r"""Gets the alarm_action_enabled of this MetricAlarmsResp.

        **参数解释**： 该条告警触发时，是否开启告警通知。 **取值范围**： 布尔值。 - true：开启告警通知。 - false：不开启告警通知。 

        :return: The alarm_action_enabled of this MetricAlarmsResp.
        :rtype: bool
        """
        return self._alarm_action_enabled

    @alarm_action_enabled.setter
    def alarm_action_enabled(self, alarm_action_enabled):
        r"""Sets the alarm_action_enabled of this MetricAlarmsResp.

        **参数解释**： 该条告警触发时，是否开启告警通知。 **取值范围**： 布尔值。 - true：开启告警通知。 - false：不开启告警通知。 

        :param alarm_action_enabled: The alarm_action_enabled of this MetricAlarmsResp.
        :type alarm_action_enabled: bool
        """
        self._alarm_action_enabled = alarm_action_enabled

    @property
    def ignore_insufficient_data(self):
        r"""Gets the ignore_insufficient_data of this MetricAlarmsResp.

        **参数解释**： 数据不足时，是否产生告警记录(不会发送通知)。 **取值范围**： 值为true或者false - true：数据不足时，产生告警记录 - false：数据不足时，不产生告警记录 

        :return: The ignore_insufficient_data of this MetricAlarmsResp.
        :rtype: bool
        """
        return self._ignore_insufficient_data

    @ignore_insufficient_data.setter
    def ignore_insufficient_data(self, ignore_insufficient_data):
        r"""Sets the ignore_insufficient_data of this MetricAlarmsResp.

        **参数解释**： 数据不足时，是否产生告警记录(不会发送通知)。 **取值范围**： 值为true或者false - true：数据不足时，产生告警记录 - false：数据不足时，不产生告警记录 

        :param ignore_insufficient_data: The ignore_insufficient_data of this MetricAlarmsResp.
        :type ignore_insufficient_data: bool
        """
        self._ignore_insufficient_data = ignore_insufficient_data

    @property
    def alarm_actions(self):
        r"""Gets the alarm_actions of this MetricAlarmsResp.

        **参数解释**： 告警触发时，通知组/主题订阅的信息。 

        :return: The alarm_actions of this MetricAlarmsResp.
        :rtype: list[:class:`huaweicloudsdkces.v1.NotificationResp`]
        """
        return self._alarm_actions

    @alarm_actions.setter
    def alarm_actions(self, alarm_actions):
        r"""Sets the alarm_actions of this MetricAlarmsResp.

        **参数解释**： 告警触发时，通知组/主题订阅的信息。 

        :param alarm_actions: The alarm_actions of this MetricAlarmsResp.
        :type alarm_actions: list[:class:`huaweicloudsdkces.v1.NotificationResp`]
        """
        self._alarm_actions = alarm_actions

    @property
    def ok_actions(self):
        r"""Gets the ok_actions of this MetricAlarmsResp.

        **参数解释**： 告警触发时，通知组/主题订阅的信息。 

        :return: The ok_actions of this MetricAlarmsResp.
        :rtype: list[:class:`huaweicloudsdkces.v1.NotificationResp`]
        """
        return self._ok_actions

    @ok_actions.setter
    def ok_actions(self, ok_actions):
        r"""Sets the ok_actions of this MetricAlarmsResp.

        **参数解释**： 告警触发时，通知组/主题订阅的信息。 

        :param ok_actions: The ok_actions of this MetricAlarmsResp.
        :type ok_actions: list[:class:`huaweicloudsdkces.v1.NotificationResp`]
        """
        self._ok_actions = ok_actions

    @property
    def insufficientdata_actions(self):
        r"""Gets the insufficientdata_actions of this MetricAlarmsResp.

        **参数解释**： 告警触发时，通知组/主题订阅的信息。 

        :return: The insufficientdata_actions of this MetricAlarmsResp.
        :rtype: list[:class:`huaweicloudsdkces.v1.NotificationResp`]
        """
        return self._insufficientdata_actions

    @insufficientdata_actions.setter
    def insufficientdata_actions(self, insufficientdata_actions):
        r"""Sets the insufficientdata_actions of this MetricAlarmsResp.

        **参数解释**： 告警触发时，通知组/主题订阅的信息。 

        :param insufficientdata_actions: The insufficientdata_actions of this MetricAlarmsResp.
        :type insufficientdata_actions: list[:class:`huaweicloudsdkces.v1.NotificationResp`]
        """
        self._insufficientdata_actions = insufficientdata_actions

    @property
    def alarm_action_begin_time(self):
        r"""Gets the alarm_action_begin_time of this MetricAlarmsResp.

        **参数解释**： 告警规则生效的开始时间，告警规则仅在生效时间内发送通知消息。例如alarm_action_begin_time为8:00，alarm_action_end_time为20:00时，则对应的告警规则仅在08:00-20:00发送通知消息。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 

        :return: The alarm_action_begin_time of this MetricAlarmsResp.
        :rtype: str
        """
        return self._alarm_action_begin_time

    @alarm_action_begin_time.setter
    def alarm_action_begin_time(self, alarm_action_begin_time):
        r"""Sets the alarm_action_begin_time of this MetricAlarmsResp.

        **参数解释**： 告警规则生效的开始时间，告警规则仅在生效时间内发送通知消息。例如alarm_action_begin_time为8:00，alarm_action_end_time为20:00时，则对应的告警规则仅在08:00-20:00发送通知消息。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 

        :param alarm_action_begin_time: The alarm_action_begin_time of this MetricAlarmsResp.
        :type alarm_action_begin_time: str
        """
        self._alarm_action_begin_time = alarm_action_begin_time

    @property
    def alarm_action_end_time(self):
        r"""Gets the alarm_action_end_time of this MetricAlarmsResp.

        **参数解释**： 告警规则生效的结束时间，告警规则仅在生效时间内发送通知消息。例如alarm_action_begin_time为8:00，alarm_action_end_time为20:00时，则对应的告警规则仅在08:00-20:00发送通知消息。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 

        :return: The alarm_action_end_time of this MetricAlarmsResp.
        :rtype: str
        """
        return self._alarm_action_end_time

    @alarm_action_end_time.setter
    def alarm_action_end_time(self, alarm_action_end_time):
        r"""Sets the alarm_action_end_time of this MetricAlarmsResp.

        **参数解释**： 告警规则生效的结束时间，告警规则仅在生效时间内发送通知消息。例如alarm_action_begin_time为8:00，alarm_action_end_time为20:00时，则对应的告警规则仅在08:00-20:00发送通知消息。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 

        :param alarm_action_end_time: The alarm_action_end_time of this MetricAlarmsResp.
        :type alarm_action_end_time: str
        """
        self._alarm_action_end_time = alarm_action_end_time

    @property
    def effective_timezone(self):
        r"""Gets the effective_timezone of this MetricAlarmsResp.

        **参数解释**： 时区，形如：\"GMT-08:00\"、\"GMT+08:00\"、\"GMT+0:00\" **取值范围**： 长度为[1,16]个字符。 

        :return: The effective_timezone of this MetricAlarmsResp.
        :rtype: str
        """
        return self._effective_timezone

    @effective_timezone.setter
    def effective_timezone(self, effective_timezone):
        r"""Sets the effective_timezone of this MetricAlarmsResp.

        **参数解释**： 时区，形如：\"GMT-08:00\"、\"GMT+08:00\"、\"GMT+0:00\" **取值范围**： 长度为[1,16]个字符。 

        :param effective_timezone: The effective_timezone of this MetricAlarmsResp.
        :type effective_timezone: str
        """
        self._effective_timezone = effective_timezone

    @property
    def alarm_id(self):
        r"""Gets the alarm_id of this MetricAlarmsResp.

        **参数解释**： 告警规则的ID。 **取值范围**： 以al开头，后跟22个数字或字母。字符长度为24 

        :return: The alarm_id of this MetricAlarmsResp.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        r"""Sets the alarm_id of this MetricAlarmsResp.

        **参数解释**： 告警规则的ID。 **取值范围**： 以al开头，后跟22个数字或字母。字符长度为24 

        :param alarm_id: The alarm_id of this MetricAlarmsResp.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def update_time(self):
        r"""Gets the update_time of this MetricAlarmsResp.

        **参数解释**： 告警状态变更的时间，UNIX时间戳，单位毫秒。 **取值范围** 0 - 9999999999999 

        :return: The update_time of this MetricAlarmsResp.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this MetricAlarmsResp.

        **参数解释**： 告警状态变更的时间，UNIX时间戳，单位毫秒。 **取值范围** 0 - 9999999999999 

        :param update_time: The update_time of this MetricAlarmsResp.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def alarm_state(self):
        r"""Gets the alarm_state of this MetricAlarmsResp.

        **参数解释**： 告警状态。 **取值范围**： 只能为ok、alarm、insufficient_data。 - ok：正常 - alarm：告警 - insufficient_data：数据不足 

        :return: The alarm_state of this MetricAlarmsResp.
        :rtype: str
        """
        return self._alarm_state

    @alarm_state.setter
    def alarm_state(self, alarm_state):
        r"""Sets the alarm_state of this MetricAlarmsResp.

        **参数解释**： 告警状态。 **取值范围**： 只能为ok、alarm、insufficient_data。 - ok：正常 - alarm：告警 - insufficient_data：数据不足 

        :param alarm_state: The alarm_state of this MetricAlarmsResp.
        :type alarm_state: str
        """
        self._alarm_state = alarm_state

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this MetricAlarmsResp.

        **参数解释**： 企业项目ID。 **取值范围**： 只能包含小写字母、数字、“-”、“_”，长度为36个字符。也可取值0或all_granted_eps。0：代表默认企业项目ID，all_granted_eps：代表所有企业项目ID。 

        :return: The enterprise_project_id of this MetricAlarmsResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this MetricAlarmsResp.

        **参数解释**： 企业项目ID。 **取值范围**： 只能包含小写字母、数字、“-”、“_”，长度为36个字符。也可取值0或all_granted_eps。0：代表默认企业项目ID，all_granted_eps：代表所有企业项目ID。 

        :param enterprise_project_id: The enterprise_project_id of this MetricAlarmsResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, MetricAlarmsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
