# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmHistoryInfoResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_id': 'str',
        'alarm_name': 'str',
        'alarm_description': 'str',
        'metric': 'MetricInfoResp',
        'condition': 'ConditionResp',
        'alarm_level': 'int',
        'alarm_type': 'str',
        'alarm_enabled': 'bool',
        'alarm_action_enabled': 'bool',
        'alarm_actions': 'list[list[NotificationResp]]',
        'ok_actions': 'list[list[NotificationResp]]',
        'insufficientdata_actions': 'list[list[NotificationResp]]',
        'update_time': 'int',
        'enterprise_project_id': 'str',
        'trigger_time': 'int',
        'alarm_status': 'str',
        'datapoints': 'list[DataPointForAlarmHistoryResp]',
        'additional_info': 'AdditionalInfoResp',
        'notification_manner': 'str'
    }

    attribute_map = {
        'alarm_id': 'alarm_id',
        'alarm_name': 'alarm_name',
        'alarm_description': 'alarm_description',
        'metric': 'metric',
        'condition': 'condition',
        'alarm_level': 'alarm_level',
        'alarm_type': 'alarm_type',
        'alarm_enabled': 'alarm_enabled',
        'alarm_action_enabled': 'alarm_action_enabled',
        'alarm_actions': 'alarm_actions',
        'ok_actions': 'ok_actions',
        'insufficientdata_actions': 'insufficientdata_actions',
        'update_time': 'update_time',
        'enterprise_project_id': 'enterprise_project_id',
        'trigger_time': 'trigger_time',
        'alarm_status': 'alarm_status',
        'datapoints': 'datapoints',
        'additional_info': 'additional_info',
        'notification_manner': 'notification_manner'
    }

    def __init__(self, alarm_id=None, alarm_name=None, alarm_description=None, metric=None, condition=None, alarm_level=None, alarm_type=None, alarm_enabled=None, alarm_action_enabled=None, alarm_actions=None, ok_actions=None, insufficientdata_actions=None, update_time=None, enterprise_project_id=None, trigger_time=None, alarm_status=None, datapoints=None, additional_info=None, notification_manner=None):
        r"""AlarmHistoryInfoResp

        The model defined in huaweicloud sdk

        :param alarm_id: **参数解释**： 告警规则的ID，如：al1603131199286dzxpqK3Ez。 **取值范围**： 字符串长度为24 
        :type alarm_id: str
        :param alarm_name: **参数解释**： 告警规则的名称，如：alarm-test01 **取值范围**： 字符串长度在 1 到 128 之间 
        :type alarm_name: str
        :param alarm_description: **参数解释**： 告警规则的描述 **取值范围**： 字符串长度在 0 到 256 之间 
        :type alarm_description: str
        :param metric: 
        :type metric: :class:`huaweicloudsdkces.v1.MetricInfoResp`
        :param condition: 
        :type condition: :class:`huaweicloudsdkces.v1.ConditionResp`
        :param alarm_level: **参数解释**： 告警记录的告警级别。 **取值范围**： 枚举值： - 1：紧急 - 2：重要 - 3：次要 - 4：提示 
        :type alarm_level: int
        :param alarm_type: **参数解释**： 告警规则类型 **取值范围**： 枚举值: - ALL_INSTANCE：全部资源指标告警 - RESOURCE_GROUP：资源分组指标告警 - MULTI_INSTANCE：指定资源指标告警 - EVENT.SYS：系统事件告警 - EVENT.CUSTOM：自定义事件告警 - DNSHealthCheck：健康检查告警 
        :type alarm_type: str
        :param alarm_enabled: **参数解释**： 告警规则是否被启用 **取值范围**： 值为true或者false - true：开启 - false：关闭 
        :type alarm_enabled: bool
        :param alarm_action_enabled: **参数解释**： 是否发送通知 **取值范围**： 值为true或者false - true：发送通知 - false：不发送通知 
        :type alarm_action_enabled: bool
        :param alarm_actions: **参数解释**： 告警触发时，通知组/主题订阅的信息。结构如下：{  \&quot;type\&quot;: \&quot;notification\&quot;, \&quot;notificationList\&quot;: [\&quot;urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\&quot;]  } 
        :type alarm_actions: list[list[NotificationResp]]
        :param ok_actions: **参数解释**： 告警恢复时，通知组/主题订阅的信息。结构如下：{  \&quot;type\&quot;: \&quot;notification\&quot;, \&quot;notificationList\&quot;: [\&quot;urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\&quot;]  } 
        :type ok_actions: list[list[NotificationResp]]
        :param insufficientdata_actions: **参数解释**： 数据不足时触发告警时，通知组/主题订阅的信息。结构如下：{  \&quot;type\&quot;: \&quot;notification\&quot;, \&quot;notificationList\&quot;: [\&quot;urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\&quot;]  } 
        :type insufficientdata_actions: list[list[NotificationResp]]
        :param update_time: **参数解释**： 告警状态变更的时间，UNIX时间戳，单位毫秒，如：1603131199000 **取值范围**： 不涉及 
        :type update_time: int
        :param enterprise_project_id: **参数解释**： 企业项目ID **取值范围**： 只能包含小写字母、数字、“-”、“_”，可以自定义企业项目ID，长度为36个字符。也可以为0（代表默认企业项目ID），all_granted_eps（代表所有企业项目ID） 
        :type enterprise_project_id: str
        :param trigger_time: **参数解释**： 计算出该条告警历史的时间，UNIX时间戳，单位毫秒，如：1603131199469 **取值范围**： 不涉及 
        :type trigger_time: int
        :param alarm_status: **参数解释**： 告警规则的状态 **取值范围**： 枚举值： - ok：正常 - alarm：告警 - insufficient_data：数据不足 - invalid：已失效 
        :type alarm_status: str
        :param datapoints: **参数解释**： 计算出该条告警历史的资源监控数据的一组数据上报时间和监控数值 
        :type datapoints: list[:class:`huaweicloudsdkces.v1.DataPointForAlarmHistoryResp`]
        :param additional_info: 
        :type additional_info: :class:`huaweicloudsdkces.v1.AdditionalInfoResp`
        :param notification_manner: **参数解释** 通知方式 **取值范围**： 枚举值： - NOTIFICATION_POLICY：通知策略 - NOTIFICATION_GROUP：通知组 - TOPIC_SUBSCRIPTION：主题订阅 
        :type notification_manner: str
        """
        
        

        self._alarm_id = None
        self._alarm_name = None
        self._alarm_description = None
        self._metric = None
        self._condition = None
        self._alarm_level = None
        self._alarm_type = None
        self._alarm_enabled = None
        self._alarm_action_enabled = None
        self._alarm_actions = None
        self._ok_actions = None
        self._insufficientdata_actions = None
        self._update_time = None
        self._enterprise_project_id = None
        self._trigger_time = None
        self._alarm_status = None
        self._datapoints = None
        self._additional_info = None
        self._notification_manner = None
        self.discriminator = None

        if alarm_id is not None:
            self.alarm_id = alarm_id
        if alarm_name is not None:
            self.alarm_name = alarm_name
        if alarm_description is not None:
            self.alarm_description = alarm_description
        if metric is not None:
            self.metric = metric
        if condition is not None:
            self.condition = condition
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if alarm_type is not None:
            self.alarm_type = alarm_type
        if alarm_enabled is not None:
            self.alarm_enabled = alarm_enabled
        if alarm_action_enabled is not None:
            self.alarm_action_enabled = alarm_action_enabled
        if alarm_actions is not None:
            self.alarm_actions = alarm_actions
        if ok_actions is not None:
            self.ok_actions = ok_actions
        if insufficientdata_actions is not None:
            self.insufficientdata_actions = insufficientdata_actions
        if update_time is not None:
            self.update_time = update_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if trigger_time is not None:
            self.trigger_time = trigger_time
        if alarm_status is not None:
            self.alarm_status = alarm_status
        if datapoints is not None:
            self.datapoints = datapoints
        if additional_info is not None:
            self.additional_info = additional_info
        if notification_manner is not None:
            self.notification_manner = notification_manner

    @property
    def alarm_id(self):
        r"""Gets the alarm_id of this AlarmHistoryInfoResp.

        **参数解释**： 告警规则的ID，如：al1603131199286dzxpqK3Ez。 **取值范围**： 字符串长度为24 

        :return: The alarm_id of this AlarmHistoryInfoResp.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        r"""Sets the alarm_id of this AlarmHistoryInfoResp.

        **参数解释**： 告警规则的ID，如：al1603131199286dzxpqK3Ez。 **取值范围**： 字符串长度为24 

        :param alarm_id: The alarm_id of this AlarmHistoryInfoResp.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def alarm_name(self):
        r"""Gets the alarm_name of this AlarmHistoryInfoResp.

        **参数解释**： 告警规则的名称，如：alarm-test01 **取值范围**： 字符串长度在 1 到 128 之间 

        :return: The alarm_name of this AlarmHistoryInfoResp.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        r"""Sets the alarm_name of this AlarmHistoryInfoResp.

        **参数解释**： 告警规则的名称，如：alarm-test01 **取值范围**： 字符串长度在 1 到 128 之间 

        :param alarm_name: The alarm_name of this AlarmHistoryInfoResp.
        :type alarm_name: str
        """
        self._alarm_name = alarm_name

    @property
    def alarm_description(self):
        r"""Gets the alarm_description of this AlarmHistoryInfoResp.

        **参数解释**： 告警规则的描述 **取值范围**： 字符串长度在 0 到 256 之间 

        :return: The alarm_description of this AlarmHistoryInfoResp.
        :rtype: str
        """
        return self._alarm_description

    @alarm_description.setter
    def alarm_description(self, alarm_description):
        r"""Sets the alarm_description of this AlarmHistoryInfoResp.

        **参数解释**： 告警规则的描述 **取值范围**： 字符串长度在 0 到 256 之间 

        :param alarm_description: The alarm_description of this AlarmHistoryInfoResp.
        :type alarm_description: str
        """
        self._alarm_description = alarm_description

    @property
    def metric(self):
        r"""Gets the metric of this AlarmHistoryInfoResp.

        :return: The metric of this AlarmHistoryInfoResp.
        :rtype: :class:`huaweicloudsdkces.v1.MetricInfoResp`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this AlarmHistoryInfoResp.

        :param metric: The metric of this AlarmHistoryInfoResp.
        :type metric: :class:`huaweicloudsdkces.v1.MetricInfoResp`
        """
        self._metric = metric

    @property
    def condition(self):
        r"""Gets the condition of this AlarmHistoryInfoResp.

        :return: The condition of this AlarmHistoryInfoResp.
        :rtype: :class:`huaweicloudsdkces.v1.ConditionResp`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this AlarmHistoryInfoResp.

        :param condition: The condition of this AlarmHistoryInfoResp.
        :type condition: :class:`huaweicloudsdkces.v1.ConditionResp`
        """
        self._condition = condition

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this AlarmHistoryInfoResp.

        **参数解释**： 告警记录的告警级别。 **取值范围**： 枚举值： - 1：紧急 - 2：重要 - 3：次要 - 4：提示 

        :return: The alarm_level of this AlarmHistoryInfoResp.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this AlarmHistoryInfoResp.

        **参数解释**： 告警记录的告警级别。 **取值范围**： 枚举值： - 1：紧急 - 2：重要 - 3：次要 - 4：提示 

        :param alarm_level: The alarm_level of this AlarmHistoryInfoResp.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def alarm_type(self):
        r"""Gets the alarm_type of this AlarmHistoryInfoResp.

        **参数解释**： 告警规则类型 **取值范围**： 枚举值: - ALL_INSTANCE：全部资源指标告警 - RESOURCE_GROUP：资源分组指标告警 - MULTI_INSTANCE：指定资源指标告警 - EVENT.SYS：系统事件告警 - EVENT.CUSTOM：自定义事件告警 - DNSHealthCheck：健康检查告警 

        :return: The alarm_type of this AlarmHistoryInfoResp.
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        r"""Sets the alarm_type of this AlarmHistoryInfoResp.

        **参数解释**： 告警规则类型 **取值范围**： 枚举值: - ALL_INSTANCE：全部资源指标告警 - RESOURCE_GROUP：资源分组指标告警 - MULTI_INSTANCE：指定资源指标告警 - EVENT.SYS：系统事件告警 - EVENT.CUSTOM：自定义事件告警 - DNSHealthCheck：健康检查告警 

        :param alarm_type: The alarm_type of this AlarmHistoryInfoResp.
        :type alarm_type: str
        """
        self._alarm_type = alarm_type

    @property
    def alarm_enabled(self):
        r"""Gets the alarm_enabled of this AlarmHistoryInfoResp.

        **参数解释**： 告警规则是否被启用 **取值范围**： 值为true或者false - true：开启 - false：关闭 

        :return: The alarm_enabled of this AlarmHistoryInfoResp.
        :rtype: bool
        """
        return self._alarm_enabled

    @alarm_enabled.setter
    def alarm_enabled(self, alarm_enabled):
        r"""Sets the alarm_enabled of this AlarmHistoryInfoResp.

        **参数解释**： 告警规则是否被启用 **取值范围**： 值为true或者false - true：开启 - false：关闭 

        :param alarm_enabled: The alarm_enabled of this AlarmHistoryInfoResp.
        :type alarm_enabled: bool
        """
        self._alarm_enabled = alarm_enabled

    @property
    def alarm_action_enabled(self):
        r"""Gets the alarm_action_enabled of this AlarmHistoryInfoResp.

        **参数解释**： 是否发送通知 **取值范围**： 值为true或者false - true：发送通知 - false：不发送通知 

        :return: The alarm_action_enabled of this AlarmHistoryInfoResp.
        :rtype: bool
        """
        return self._alarm_action_enabled

    @alarm_action_enabled.setter
    def alarm_action_enabled(self, alarm_action_enabled):
        r"""Sets the alarm_action_enabled of this AlarmHistoryInfoResp.

        **参数解释**： 是否发送通知 **取值范围**： 值为true或者false - true：发送通知 - false：不发送通知 

        :param alarm_action_enabled: The alarm_action_enabled of this AlarmHistoryInfoResp.
        :type alarm_action_enabled: bool
        """
        self._alarm_action_enabled = alarm_action_enabled

    @property
    def alarm_actions(self):
        r"""Gets the alarm_actions of this AlarmHistoryInfoResp.

        **参数解释**： 告警触发时，通知组/主题订阅的信息。结构如下：{  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  } 

        :return: The alarm_actions of this AlarmHistoryInfoResp.
        :rtype: list[list[NotificationResp]]
        """
        return self._alarm_actions

    @alarm_actions.setter
    def alarm_actions(self, alarm_actions):
        r"""Sets the alarm_actions of this AlarmHistoryInfoResp.

        **参数解释**： 告警触发时，通知组/主题订阅的信息。结构如下：{  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  } 

        :param alarm_actions: The alarm_actions of this AlarmHistoryInfoResp.
        :type alarm_actions: list[list[NotificationResp]]
        """
        self._alarm_actions = alarm_actions

    @property
    def ok_actions(self):
        r"""Gets the ok_actions of this AlarmHistoryInfoResp.

        **参数解释**： 告警恢复时，通知组/主题订阅的信息。结构如下：{  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  } 

        :return: The ok_actions of this AlarmHistoryInfoResp.
        :rtype: list[list[NotificationResp]]
        """
        return self._ok_actions

    @ok_actions.setter
    def ok_actions(self, ok_actions):
        r"""Sets the ok_actions of this AlarmHistoryInfoResp.

        **参数解释**： 告警恢复时，通知组/主题订阅的信息。结构如下：{  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  } 

        :param ok_actions: The ok_actions of this AlarmHistoryInfoResp.
        :type ok_actions: list[list[NotificationResp]]
        """
        self._ok_actions = ok_actions

    @property
    def insufficientdata_actions(self):
        r"""Gets the insufficientdata_actions of this AlarmHistoryInfoResp.

        **参数解释**： 数据不足时触发告警时，通知组/主题订阅的信息。结构如下：{  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  } 

        :return: The insufficientdata_actions of this AlarmHistoryInfoResp.
        :rtype: list[list[NotificationResp]]
        """
        return self._insufficientdata_actions

    @insufficientdata_actions.setter
    def insufficientdata_actions(self, insufficientdata_actions):
        r"""Sets the insufficientdata_actions of this AlarmHistoryInfoResp.

        **参数解释**： 数据不足时触发告警时，通知组/主题订阅的信息。结构如下：{  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  } 

        :param insufficientdata_actions: The insufficientdata_actions of this AlarmHistoryInfoResp.
        :type insufficientdata_actions: list[list[NotificationResp]]
        """
        self._insufficientdata_actions = insufficientdata_actions

    @property
    def update_time(self):
        r"""Gets the update_time of this AlarmHistoryInfoResp.

        **参数解释**： 告警状态变更的时间，UNIX时间戳，单位毫秒，如：1603131199000 **取值范围**： 不涉及 

        :return: The update_time of this AlarmHistoryInfoResp.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AlarmHistoryInfoResp.

        **参数解释**： 告警状态变更的时间，UNIX时间戳，单位毫秒，如：1603131199000 **取值范围**： 不涉及 

        :param update_time: The update_time of this AlarmHistoryInfoResp.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this AlarmHistoryInfoResp.

        **参数解释**： 企业项目ID **取值范围**： 只能包含小写字母、数字、“-”、“_”，可以自定义企业项目ID，长度为36个字符。也可以为0（代表默认企业项目ID），all_granted_eps（代表所有企业项目ID） 

        :return: The enterprise_project_id of this AlarmHistoryInfoResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this AlarmHistoryInfoResp.

        **参数解释**： 企业项目ID **取值范围**： 只能包含小写字母、数字、“-”、“_”，可以自定义企业项目ID，长度为36个字符。也可以为0（代表默认企业项目ID），all_granted_eps（代表所有企业项目ID） 

        :param enterprise_project_id: The enterprise_project_id of this AlarmHistoryInfoResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def trigger_time(self):
        r"""Gets the trigger_time of this AlarmHistoryInfoResp.

        **参数解释**： 计算出该条告警历史的时间，UNIX时间戳，单位毫秒，如：1603131199469 **取值范围**： 不涉及 

        :return: The trigger_time of this AlarmHistoryInfoResp.
        :rtype: int
        """
        return self._trigger_time

    @trigger_time.setter
    def trigger_time(self, trigger_time):
        r"""Sets the trigger_time of this AlarmHistoryInfoResp.

        **参数解释**： 计算出该条告警历史的时间，UNIX时间戳，单位毫秒，如：1603131199469 **取值范围**： 不涉及 

        :param trigger_time: The trigger_time of this AlarmHistoryInfoResp.
        :type trigger_time: int
        """
        self._trigger_time = trigger_time

    @property
    def alarm_status(self):
        r"""Gets the alarm_status of this AlarmHistoryInfoResp.

        **参数解释**： 告警规则的状态 **取值范围**： 枚举值： - ok：正常 - alarm：告警 - insufficient_data：数据不足 - invalid：已失效 

        :return: The alarm_status of this AlarmHistoryInfoResp.
        :rtype: str
        """
        return self._alarm_status

    @alarm_status.setter
    def alarm_status(self, alarm_status):
        r"""Sets the alarm_status of this AlarmHistoryInfoResp.

        **参数解释**： 告警规则的状态 **取值范围**： 枚举值： - ok：正常 - alarm：告警 - insufficient_data：数据不足 - invalid：已失效 

        :param alarm_status: The alarm_status of this AlarmHistoryInfoResp.
        :type alarm_status: str
        """
        self._alarm_status = alarm_status

    @property
    def datapoints(self):
        r"""Gets the datapoints of this AlarmHistoryInfoResp.

        **参数解释**： 计算出该条告警历史的资源监控数据的一组数据上报时间和监控数值 

        :return: The datapoints of this AlarmHistoryInfoResp.
        :rtype: list[:class:`huaweicloudsdkces.v1.DataPointForAlarmHistoryResp`]
        """
        return self._datapoints

    @datapoints.setter
    def datapoints(self, datapoints):
        r"""Sets the datapoints of this AlarmHistoryInfoResp.

        **参数解释**： 计算出该条告警历史的资源监控数据的一组数据上报时间和监控数值 

        :param datapoints: The datapoints of this AlarmHistoryInfoResp.
        :type datapoints: list[:class:`huaweicloudsdkces.v1.DataPointForAlarmHistoryResp`]
        """
        self._datapoints = datapoints

    @property
    def additional_info(self):
        r"""Gets the additional_info of this AlarmHistoryInfoResp.

        :return: The additional_info of this AlarmHistoryInfoResp.
        :rtype: :class:`huaweicloudsdkces.v1.AdditionalInfoResp`
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        r"""Sets the additional_info of this AlarmHistoryInfoResp.

        :param additional_info: The additional_info of this AlarmHistoryInfoResp.
        :type additional_info: :class:`huaweicloudsdkces.v1.AdditionalInfoResp`
        """
        self._additional_info = additional_info

    @property
    def notification_manner(self):
        r"""Gets the notification_manner of this AlarmHistoryInfoResp.

        **参数解释** 通知方式 **取值范围**： 枚举值： - NOTIFICATION_POLICY：通知策略 - NOTIFICATION_GROUP：通知组 - TOPIC_SUBSCRIPTION：主题订阅 

        :return: The notification_manner of this AlarmHistoryInfoResp.
        :rtype: str
        """
        return self._notification_manner

    @notification_manner.setter
    def notification_manner(self, notification_manner):
        r"""Sets the notification_manner of this AlarmHistoryInfoResp.

        **参数解释** 通知方式 **取值范围**： 枚举值： - NOTIFICATION_POLICY：通知策略 - NOTIFICATION_GROUP：通知组 - TOPIC_SUBSCRIPTION：主题订阅 

        :param notification_manner: The notification_manner of this AlarmHistoryInfoResp.
        :type notification_manner: str
        """
        self._notification_manner = notification_manner

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
        if not isinstance(other, AlarmHistoryInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
