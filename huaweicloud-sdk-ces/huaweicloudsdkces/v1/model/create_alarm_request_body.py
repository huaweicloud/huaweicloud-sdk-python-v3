# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAlarmRequestBody:

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
        'metric': 'CreateAlarmMetric',
        'condition': 'Condition',
        'alarm_enabled': 'bool',
        'alarm_action_enabled': 'bool',
        'alarm_level': 'int',
        'alarm_type': 'str',
        'alarm_actions': 'list[Notification]',
        'insufficientdata_actions': 'list[Notification]',
        'ok_actions': 'list[Notification]',
        'enterprise_project_id': 'str',
        'alarm_action_begin_time': 'str',
        'alarm_action_end_time': 'str'
    }

    attribute_map = {
        'alarm_name': 'alarm_name',
        'alarm_description': 'alarm_description',
        'metric': 'metric',
        'condition': 'condition',
        'alarm_enabled': 'alarm_enabled',
        'alarm_action_enabled': 'alarm_action_enabled',
        'alarm_level': 'alarm_level',
        'alarm_type': 'alarm_type',
        'alarm_actions': 'alarm_actions',
        'insufficientdata_actions': 'insufficientdata_actions',
        'ok_actions': 'ok_actions',
        'enterprise_project_id': 'enterprise_project_id',
        'alarm_action_begin_time': 'alarm_action_begin_time',
        'alarm_action_end_time': 'alarm_action_end_time'
    }

    def __init__(self, alarm_name=None, alarm_description=None, metric=None, condition=None, alarm_enabled=None, alarm_action_enabled=None, alarm_level=None, alarm_type=None, alarm_actions=None, insufficientdata_actions=None, ok_actions=None, enterprise_project_id=None, alarm_action_begin_time=None, alarm_action_end_time=None):
        r"""CreateAlarmRequestBody

        The model defined in huaweicloud sdk

        :param alarm_name: **参数解释**： 告警名称。 **约束限制**： 不涉及。 **取值范围**： 只能包含0-9/a-z/A-Z/_/-或汉字，长度1-128。 **默认取值**： 不涉及。 
        :type alarm_name: str
        :param alarm_description: **参数解释**： 告警描述。 **约束限制**： 不涉及。 **取值范围**： 长度[0,256]个字符。 **默认取值**： 不涉及。 
        :type alarm_description: str
        :param metric: 
        :type metric: :class:`huaweicloudsdkces.v1.CreateAlarmMetric`
        :param condition: 
        :type condition: :class:`huaweicloudsdkces.v1.Condition`
        :param alarm_enabled: **参数解释**： 是否启用该条告警。 **约束限制**： 不涉及。 **取值范围**： 布尔值。 - true：开启告警。 - false：不开启告警。 **默认取值**： true 
        :type alarm_enabled: bool
        :param alarm_action_enabled: **参数解释**： 该条告警触发时，是否启用告警通知。 **约束限制**： 不填默认为true，对应的alarm_actions、ok_actions至少有一个不能为空。若alarm_actions、ok_actions同时存在时，alarm_actions和ok_actions中的notification_list值保持一致。 **取值范围**： 布尔值。 - true：开启告警通知。 - false：不开启告警通知。 **默认取值**： true 
        :type alarm_action_enabled: bool
        :param alarm_level: **参数解释**： 告警级别。 **约束限制**： 不涉及。 **取值范围**： 只能为1、2、3、4。分别对应紧急、重要、次要、提示。 **默认取值**： 2 
        :type alarm_level: int
        :param alarm_type: **参数解释**： 告警类型。 **约束限制**： 针对事件类型的告警时，告警类型为EVENT.SYS（系统事件）或EVENT.CUSTOM（自定义事件）。 针对资源分组的告警时，告警类型为RESOURCE_GROUP。 针对指定资源的告警时，告警类型为MULTI_INSTANCE。 **取值范围**： - EVENT.SYS：针对系统事件的告警规则。 - EVENT.CUSTOM：针对自定义事件的告警规则。 - RESOURCE_GROUP：针对资源分组的告警规则。 - MULTI_INSTANCE： 针对指定资源的告警规则。 **默认取值**： 不涉及。 
        :type alarm_type: str
        :param alarm_actions: **参数解释**： 通知组/主题订阅的信息。 **约束限制**： 最多包含20个动作。 
        :type alarm_actions: list[:class:`huaweicloudsdkces.v1.Notification`]
        :param insufficientdata_actions: **参数解释**： 通知组/主题订阅的信息。 **约束限制**： 最多包含20个动作。 
        :type insufficientdata_actions: list[:class:`huaweicloudsdkces.v1.Notification`]
        :param ok_actions: **参数解释**： 通知组/主题订阅的信息。 **约束限制**： 最多包含20个动作。 
        :type ok_actions: list[:class:`huaweicloudsdkces.v1.Notification`]
        :param enterprise_project_id: **参数解释**： 企业项目ID。如何查询企业项目ID，请参考“[获取企业项目ID](ces_03_0061.xml)”。 **约束限制**： 不涉及。 **取值范围**： 长度为0或者32个字符。 **默认取值**： 0，表示默认的企业项目default。 
        :type enterprise_project_id: str
        :param alarm_action_begin_time: **参数解释**： 告警通知开启时间。 **约束限制**： 不涉及。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 **默认取值**： 不涉及。 
        :type alarm_action_begin_time: str
        :param alarm_action_end_time: **参数解释**： 告警通知关闭时间。 **约束限制**： 不涉及。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 **默认取值**： 不涉及。 
        :type alarm_action_end_time: str
        """
        
        

        self._alarm_name = None
        self._alarm_description = None
        self._metric = None
        self._condition = None
        self._alarm_enabled = None
        self._alarm_action_enabled = None
        self._alarm_level = None
        self._alarm_type = None
        self._alarm_actions = None
        self._insufficientdata_actions = None
        self._ok_actions = None
        self._enterprise_project_id = None
        self._alarm_action_begin_time = None
        self._alarm_action_end_time = None
        self.discriminator = None

        self.alarm_name = alarm_name
        if alarm_description is not None:
            self.alarm_description = alarm_description
        self.metric = metric
        self.condition = condition
        if alarm_enabled is not None:
            self.alarm_enabled = alarm_enabled
        if alarm_action_enabled is not None:
            self.alarm_action_enabled = alarm_action_enabled
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if alarm_type is not None:
            self.alarm_type = alarm_type
        if alarm_actions is not None:
            self.alarm_actions = alarm_actions
        if insufficientdata_actions is not None:
            self.insufficientdata_actions = insufficientdata_actions
        if ok_actions is not None:
            self.ok_actions = ok_actions
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if alarm_action_begin_time is not None:
            self.alarm_action_begin_time = alarm_action_begin_time
        if alarm_action_end_time is not None:
            self.alarm_action_end_time = alarm_action_end_time

    @property
    def alarm_name(self):
        r"""Gets the alarm_name of this CreateAlarmRequestBody.

        **参数解释**： 告警名称。 **约束限制**： 不涉及。 **取值范围**： 只能包含0-9/a-z/A-Z/_/-或汉字，长度1-128。 **默认取值**： 不涉及。 

        :return: The alarm_name of this CreateAlarmRequestBody.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        r"""Sets the alarm_name of this CreateAlarmRequestBody.

        **参数解释**： 告警名称。 **约束限制**： 不涉及。 **取值范围**： 只能包含0-9/a-z/A-Z/_/-或汉字，长度1-128。 **默认取值**： 不涉及。 

        :param alarm_name: The alarm_name of this CreateAlarmRequestBody.
        :type alarm_name: str
        """
        self._alarm_name = alarm_name

    @property
    def alarm_description(self):
        r"""Gets the alarm_description of this CreateAlarmRequestBody.

        **参数解释**： 告警描述。 **约束限制**： 不涉及。 **取值范围**： 长度[0,256]个字符。 **默认取值**： 不涉及。 

        :return: The alarm_description of this CreateAlarmRequestBody.
        :rtype: str
        """
        return self._alarm_description

    @alarm_description.setter
    def alarm_description(self, alarm_description):
        r"""Sets the alarm_description of this CreateAlarmRequestBody.

        **参数解释**： 告警描述。 **约束限制**： 不涉及。 **取值范围**： 长度[0,256]个字符。 **默认取值**： 不涉及。 

        :param alarm_description: The alarm_description of this CreateAlarmRequestBody.
        :type alarm_description: str
        """
        self._alarm_description = alarm_description

    @property
    def metric(self):
        r"""Gets the metric of this CreateAlarmRequestBody.

        :return: The metric of this CreateAlarmRequestBody.
        :rtype: :class:`huaweicloudsdkces.v1.CreateAlarmMetric`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this CreateAlarmRequestBody.

        :param metric: The metric of this CreateAlarmRequestBody.
        :type metric: :class:`huaweicloudsdkces.v1.CreateAlarmMetric`
        """
        self._metric = metric

    @property
    def condition(self):
        r"""Gets the condition of this CreateAlarmRequestBody.

        :return: The condition of this CreateAlarmRequestBody.
        :rtype: :class:`huaweicloudsdkces.v1.Condition`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this CreateAlarmRequestBody.

        :param condition: The condition of this CreateAlarmRequestBody.
        :type condition: :class:`huaweicloudsdkces.v1.Condition`
        """
        self._condition = condition

    @property
    def alarm_enabled(self):
        r"""Gets the alarm_enabled of this CreateAlarmRequestBody.

        **参数解释**： 是否启用该条告警。 **约束限制**： 不涉及。 **取值范围**： 布尔值。 - true：开启告警。 - false：不开启告警。 **默认取值**： true 

        :return: The alarm_enabled of this CreateAlarmRequestBody.
        :rtype: bool
        """
        return self._alarm_enabled

    @alarm_enabled.setter
    def alarm_enabled(self, alarm_enabled):
        r"""Sets the alarm_enabled of this CreateAlarmRequestBody.

        **参数解释**： 是否启用该条告警。 **约束限制**： 不涉及。 **取值范围**： 布尔值。 - true：开启告警。 - false：不开启告警。 **默认取值**： true 

        :param alarm_enabled: The alarm_enabled of this CreateAlarmRequestBody.
        :type alarm_enabled: bool
        """
        self._alarm_enabled = alarm_enabled

    @property
    def alarm_action_enabled(self):
        r"""Gets the alarm_action_enabled of this CreateAlarmRequestBody.

        **参数解释**： 该条告警触发时，是否启用告警通知。 **约束限制**： 不填默认为true，对应的alarm_actions、ok_actions至少有一个不能为空。若alarm_actions、ok_actions同时存在时，alarm_actions和ok_actions中的notification_list值保持一致。 **取值范围**： 布尔值。 - true：开启告警通知。 - false：不开启告警通知。 **默认取值**： true 

        :return: The alarm_action_enabled of this CreateAlarmRequestBody.
        :rtype: bool
        """
        return self._alarm_action_enabled

    @alarm_action_enabled.setter
    def alarm_action_enabled(self, alarm_action_enabled):
        r"""Sets the alarm_action_enabled of this CreateAlarmRequestBody.

        **参数解释**： 该条告警触发时，是否启用告警通知。 **约束限制**： 不填默认为true，对应的alarm_actions、ok_actions至少有一个不能为空。若alarm_actions、ok_actions同时存在时，alarm_actions和ok_actions中的notification_list值保持一致。 **取值范围**： 布尔值。 - true：开启告警通知。 - false：不开启告警通知。 **默认取值**： true 

        :param alarm_action_enabled: The alarm_action_enabled of this CreateAlarmRequestBody.
        :type alarm_action_enabled: bool
        """
        self._alarm_action_enabled = alarm_action_enabled

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this CreateAlarmRequestBody.

        **参数解释**： 告警级别。 **约束限制**： 不涉及。 **取值范围**： 只能为1、2、3、4。分别对应紧急、重要、次要、提示。 **默认取值**： 2 

        :return: The alarm_level of this CreateAlarmRequestBody.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this CreateAlarmRequestBody.

        **参数解释**： 告警级别。 **约束限制**： 不涉及。 **取值范围**： 只能为1、2、3、4。分别对应紧急、重要、次要、提示。 **默认取值**： 2 

        :param alarm_level: The alarm_level of this CreateAlarmRequestBody.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def alarm_type(self):
        r"""Gets the alarm_type of this CreateAlarmRequestBody.

        **参数解释**： 告警类型。 **约束限制**： 针对事件类型的告警时，告警类型为EVENT.SYS（系统事件）或EVENT.CUSTOM（自定义事件）。 针对资源分组的告警时，告警类型为RESOURCE_GROUP。 针对指定资源的告警时，告警类型为MULTI_INSTANCE。 **取值范围**： - EVENT.SYS：针对系统事件的告警规则。 - EVENT.CUSTOM：针对自定义事件的告警规则。 - RESOURCE_GROUP：针对资源分组的告警规则。 - MULTI_INSTANCE： 针对指定资源的告警规则。 **默认取值**： 不涉及。 

        :return: The alarm_type of this CreateAlarmRequestBody.
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        r"""Sets the alarm_type of this CreateAlarmRequestBody.

        **参数解释**： 告警类型。 **约束限制**： 针对事件类型的告警时，告警类型为EVENT.SYS（系统事件）或EVENT.CUSTOM（自定义事件）。 针对资源分组的告警时，告警类型为RESOURCE_GROUP。 针对指定资源的告警时，告警类型为MULTI_INSTANCE。 **取值范围**： - EVENT.SYS：针对系统事件的告警规则。 - EVENT.CUSTOM：针对自定义事件的告警规则。 - RESOURCE_GROUP：针对资源分组的告警规则。 - MULTI_INSTANCE： 针对指定资源的告警规则。 **默认取值**： 不涉及。 

        :param alarm_type: The alarm_type of this CreateAlarmRequestBody.
        :type alarm_type: str
        """
        self._alarm_type = alarm_type

    @property
    def alarm_actions(self):
        r"""Gets the alarm_actions of this CreateAlarmRequestBody.

        **参数解释**： 通知组/主题订阅的信息。 **约束限制**： 最多包含20个动作。 

        :return: The alarm_actions of this CreateAlarmRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v1.Notification`]
        """
        return self._alarm_actions

    @alarm_actions.setter
    def alarm_actions(self, alarm_actions):
        r"""Sets the alarm_actions of this CreateAlarmRequestBody.

        **参数解释**： 通知组/主题订阅的信息。 **约束限制**： 最多包含20个动作。 

        :param alarm_actions: The alarm_actions of this CreateAlarmRequestBody.
        :type alarm_actions: list[:class:`huaweicloudsdkces.v1.Notification`]
        """
        self._alarm_actions = alarm_actions

    @property
    def insufficientdata_actions(self):
        r"""Gets the insufficientdata_actions of this CreateAlarmRequestBody.

        **参数解释**： 通知组/主题订阅的信息。 **约束限制**： 最多包含20个动作。 

        :return: The insufficientdata_actions of this CreateAlarmRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v1.Notification`]
        """
        return self._insufficientdata_actions

    @insufficientdata_actions.setter
    def insufficientdata_actions(self, insufficientdata_actions):
        r"""Sets the insufficientdata_actions of this CreateAlarmRequestBody.

        **参数解释**： 通知组/主题订阅的信息。 **约束限制**： 最多包含20个动作。 

        :param insufficientdata_actions: The insufficientdata_actions of this CreateAlarmRequestBody.
        :type insufficientdata_actions: list[:class:`huaweicloudsdkces.v1.Notification`]
        """
        self._insufficientdata_actions = insufficientdata_actions

    @property
    def ok_actions(self):
        r"""Gets the ok_actions of this CreateAlarmRequestBody.

        **参数解释**： 通知组/主题订阅的信息。 **约束限制**： 最多包含20个动作。 

        :return: The ok_actions of this CreateAlarmRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v1.Notification`]
        """
        return self._ok_actions

    @ok_actions.setter
    def ok_actions(self, ok_actions):
        r"""Sets the ok_actions of this CreateAlarmRequestBody.

        **参数解释**： 通知组/主题订阅的信息。 **约束限制**： 最多包含20个动作。 

        :param ok_actions: The ok_actions of this CreateAlarmRequestBody.
        :type ok_actions: list[:class:`huaweicloudsdkces.v1.Notification`]
        """
        self._ok_actions = ok_actions

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateAlarmRequestBody.

        **参数解释**： 企业项目ID。如何查询企业项目ID，请参考“[获取企业项目ID](ces_03_0061.xml)”。 **约束限制**： 不涉及。 **取值范围**： 长度为0或者32个字符。 **默认取值**： 0，表示默认的企业项目default。 

        :return: The enterprise_project_id of this CreateAlarmRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateAlarmRequestBody.

        **参数解释**： 企业项目ID。如何查询企业项目ID，请参考“[获取企业项目ID](ces_03_0061.xml)”。 **约束限制**： 不涉及。 **取值范围**： 长度为0或者32个字符。 **默认取值**： 0，表示默认的企业项目default。 

        :param enterprise_project_id: The enterprise_project_id of this CreateAlarmRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def alarm_action_begin_time(self):
        r"""Gets the alarm_action_begin_time of this CreateAlarmRequestBody.

        **参数解释**： 告警通知开启时间。 **约束限制**： 不涉及。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 **默认取值**： 不涉及。 

        :return: The alarm_action_begin_time of this CreateAlarmRequestBody.
        :rtype: str
        """
        return self._alarm_action_begin_time

    @alarm_action_begin_time.setter
    def alarm_action_begin_time(self, alarm_action_begin_time):
        r"""Sets the alarm_action_begin_time of this CreateAlarmRequestBody.

        **参数解释**： 告警通知开启时间。 **约束限制**： 不涉及。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 **默认取值**： 不涉及。 

        :param alarm_action_begin_time: The alarm_action_begin_time of this CreateAlarmRequestBody.
        :type alarm_action_begin_time: str
        """
        self._alarm_action_begin_time = alarm_action_begin_time

    @property
    def alarm_action_end_time(self):
        r"""Gets the alarm_action_end_time of this CreateAlarmRequestBody.

        **参数解释**： 告警通知关闭时间。 **约束限制**： 不涉及。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 **默认取值**： 不涉及。 

        :return: The alarm_action_end_time of this CreateAlarmRequestBody.
        :rtype: str
        """
        return self._alarm_action_end_time

    @alarm_action_end_time.setter
    def alarm_action_end_time(self, alarm_action_end_time):
        r"""Sets the alarm_action_end_time of this CreateAlarmRequestBody.

        **参数解释**： 告警通知关闭时间。 **约束限制**： 不涉及。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。 **默认取值**： 不涉及。 

        :param alarm_action_end_time: The alarm_action_end_time of this CreateAlarmRequestBody.
        :type alarm_action_end_time: str
        """
        self._alarm_action_end_time = alarm_action_end_time

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
        if not isinstance(other, CreateAlarmRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
