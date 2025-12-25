# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAlarmRequestBody:

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
        'condition': 'Condition',
        'alarm_action_enabled': 'bool',
        'alarm_level': 'int',
        'alarm_type': 'str',
        'alarm_actions': 'list[list[Notification]]',
        'insufficientdata_actions': 'list[list[Notification]]',
        'ok_actions': 'list[list[Notification]]'
    }

    attribute_map = {
        'alarm_name': 'alarm_name',
        'alarm_description': 'alarm_description',
        'condition': 'condition',
        'alarm_action_enabled': 'alarm_action_enabled',
        'alarm_level': 'alarm_level',
        'alarm_type': 'alarm_type',
        'alarm_actions': 'alarm_actions',
        'insufficientdata_actions': 'insufficientdata_actions',
        'ok_actions': 'ok_actions'
    }

    def __init__(self, alarm_name=None, alarm_description=None, condition=None, alarm_action_enabled=None, alarm_level=None, alarm_type=None, alarm_actions=None, insufficientdata_actions=None, ok_actions=None):
        r"""UpdateAlarmRequestBody

        The model defined in huaweicloud sdk

        :param alarm_name: **参数解释**： 告警规则名称 **约束限制**： 不涉及 **取值范围**： 只能包含0-9/a-z/A-Z/_/-或汉字，长度[1, 128]个字符 **默认取值**： 不涉及 
        :type alarm_name: str
        :param alarm_description: **参数解释**： 告警描述。 **约束限制**： 不涉及。 **取值范围**： 长度[0,256]个字符。 **默认取值**： 不涉及。 
        :type alarm_description: str
        :param condition: 
        :type condition: :class:`huaweicloudsdkces.v1.Condition`
        :param alarm_action_enabled: **参数解释**： 是否开启告警通知 **约束限制**： 若alarm_action_enabled为true，对应的alarm_actions、ok_actions至少有一个不能为空。若alarm_actions、ok_actions同时存在时，notificationList值保持一致。 **取值范围**： 只能为true、false - true: 开启告警通知 - false：关闭告警通知 **默认取值**: false。 
        :type alarm_action_enabled: bool
        :param alarm_level: **参数解释**： 告警级别 **约束限制**： 不涉及 **取值范围**： 级别为1、2、3、4。 - 1：紧急 - 2：重要 - 3：次要 - 4：提示 **默认取值**: 2 
        :type alarm_level: int
        :param alarm_type: **参数解释**： 告警类型。 **约束限制**： 不涉及 **取值范围**： - EVENT.SYS：针对系统事件的告警规则。 - EVENT.CUSTOM：针对自定义事件的告警规则。 - RESOURCE_GROUP：针对资源分组的告警规则。 - MULTI_INSTANCE： 针对指定资源的告警规则。 **默认取值**： 不涉及。 
        :type alarm_type: str
        :param alarm_actions: **参数解释**： 告警触发时，通知组/主题订阅的信息。结构样例如下： { \&quot;type\&quot;: \&quot;notification\&quot;,\&quot;notificationList\&quot;:[\&quot;urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\&quot;] } **约束限制**： 最多包含10个告警触发时的通知对象信息。 
        :type alarm_actions: list[list[Notification]]
        :param insufficientdata_actions: **参数解释**： 数据不足触发告警时，通知组/主题订阅的信息。（该参数已废弃，建议无需配置） **约束限制**： 最多包含10个告警动作。 
        :type insufficientdata_actions: list[list[Notification]]
        :param ok_actions: **参数解释**： 告警恢复时，通知组/主题订阅的信息。结构样例如下： { \&quot;type\&quot;: \&quot;notification\&quot;,\&quot;notificationList\&quot;:[\&quot;urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\&quot;] }  **约束限制**： 最多包含10个告警触发时的通知对象信息。 
        :type ok_actions: list[list[Notification]]
        """
        
        

        self._alarm_name = None
        self._alarm_description = None
        self._condition = None
        self._alarm_action_enabled = None
        self._alarm_level = None
        self._alarm_type = None
        self._alarm_actions = None
        self._insufficientdata_actions = None
        self._ok_actions = None
        self.discriminator = None

        if alarm_name is not None:
            self.alarm_name = alarm_name
        if alarm_description is not None:
            self.alarm_description = alarm_description
        if condition is not None:
            self.condition = condition
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

    @property
    def alarm_name(self):
        r"""Gets the alarm_name of this UpdateAlarmRequestBody.

        **参数解释**： 告警规则名称 **约束限制**： 不涉及 **取值范围**： 只能包含0-9/a-z/A-Z/_/-或汉字，长度[1, 128]个字符 **默认取值**： 不涉及 

        :return: The alarm_name of this UpdateAlarmRequestBody.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        r"""Sets the alarm_name of this UpdateAlarmRequestBody.

        **参数解释**： 告警规则名称 **约束限制**： 不涉及 **取值范围**： 只能包含0-9/a-z/A-Z/_/-或汉字，长度[1, 128]个字符 **默认取值**： 不涉及 

        :param alarm_name: The alarm_name of this UpdateAlarmRequestBody.
        :type alarm_name: str
        """
        self._alarm_name = alarm_name

    @property
    def alarm_description(self):
        r"""Gets the alarm_description of this UpdateAlarmRequestBody.

        **参数解释**： 告警描述。 **约束限制**： 不涉及。 **取值范围**： 长度[0,256]个字符。 **默认取值**： 不涉及。 

        :return: The alarm_description of this UpdateAlarmRequestBody.
        :rtype: str
        """
        return self._alarm_description

    @alarm_description.setter
    def alarm_description(self, alarm_description):
        r"""Sets the alarm_description of this UpdateAlarmRequestBody.

        **参数解释**： 告警描述。 **约束限制**： 不涉及。 **取值范围**： 长度[0,256]个字符。 **默认取值**： 不涉及。 

        :param alarm_description: The alarm_description of this UpdateAlarmRequestBody.
        :type alarm_description: str
        """
        self._alarm_description = alarm_description

    @property
    def condition(self):
        r"""Gets the condition of this UpdateAlarmRequestBody.

        :return: The condition of this UpdateAlarmRequestBody.
        :rtype: :class:`huaweicloudsdkces.v1.Condition`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this UpdateAlarmRequestBody.

        :param condition: The condition of this UpdateAlarmRequestBody.
        :type condition: :class:`huaweicloudsdkces.v1.Condition`
        """
        self._condition = condition

    @property
    def alarm_action_enabled(self):
        r"""Gets the alarm_action_enabled of this UpdateAlarmRequestBody.

        **参数解释**： 是否开启告警通知 **约束限制**： 若alarm_action_enabled为true，对应的alarm_actions、ok_actions至少有一个不能为空。若alarm_actions、ok_actions同时存在时，notificationList值保持一致。 **取值范围**： 只能为true、false - true: 开启告警通知 - false：关闭告警通知 **默认取值**: false。 

        :return: The alarm_action_enabled of this UpdateAlarmRequestBody.
        :rtype: bool
        """
        return self._alarm_action_enabled

    @alarm_action_enabled.setter
    def alarm_action_enabled(self, alarm_action_enabled):
        r"""Sets the alarm_action_enabled of this UpdateAlarmRequestBody.

        **参数解释**： 是否开启告警通知 **约束限制**： 若alarm_action_enabled为true，对应的alarm_actions、ok_actions至少有一个不能为空。若alarm_actions、ok_actions同时存在时，notificationList值保持一致。 **取值范围**： 只能为true、false - true: 开启告警通知 - false：关闭告警通知 **默认取值**: false。 

        :param alarm_action_enabled: The alarm_action_enabled of this UpdateAlarmRequestBody.
        :type alarm_action_enabled: bool
        """
        self._alarm_action_enabled = alarm_action_enabled

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this UpdateAlarmRequestBody.

        **参数解释**： 告警级别 **约束限制**： 不涉及 **取值范围**： 级别为1、2、3、4。 - 1：紧急 - 2：重要 - 3：次要 - 4：提示 **默认取值**: 2 

        :return: The alarm_level of this UpdateAlarmRequestBody.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this UpdateAlarmRequestBody.

        **参数解释**： 告警级别 **约束限制**： 不涉及 **取值范围**： 级别为1、2、3、4。 - 1：紧急 - 2：重要 - 3：次要 - 4：提示 **默认取值**: 2 

        :param alarm_level: The alarm_level of this UpdateAlarmRequestBody.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def alarm_type(self):
        r"""Gets the alarm_type of this UpdateAlarmRequestBody.

        **参数解释**： 告警类型。 **约束限制**： 不涉及 **取值范围**： - EVENT.SYS：针对系统事件的告警规则。 - EVENT.CUSTOM：针对自定义事件的告警规则。 - RESOURCE_GROUP：针对资源分组的告警规则。 - MULTI_INSTANCE： 针对指定资源的告警规则。 **默认取值**： 不涉及。 

        :return: The alarm_type of this UpdateAlarmRequestBody.
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        r"""Sets the alarm_type of this UpdateAlarmRequestBody.

        **参数解释**： 告警类型。 **约束限制**： 不涉及 **取值范围**： - EVENT.SYS：针对系统事件的告警规则。 - EVENT.CUSTOM：针对自定义事件的告警规则。 - RESOURCE_GROUP：针对资源分组的告警规则。 - MULTI_INSTANCE： 针对指定资源的告警规则。 **默认取值**： 不涉及。 

        :param alarm_type: The alarm_type of this UpdateAlarmRequestBody.
        :type alarm_type: str
        """
        self._alarm_type = alarm_type

    @property
    def alarm_actions(self):
        r"""Gets the alarm_actions of this UpdateAlarmRequestBody.

        **参数解释**： 告警触发时，通知组/主题订阅的信息。结构样例如下： { \"type\": \"notification\",\"notificationList\":[\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"] } **约束限制**： 最多包含10个告警触发时的通知对象信息。 

        :return: The alarm_actions of this UpdateAlarmRequestBody.
        :rtype: list[list[Notification]]
        """
        return self._alarm_actions

    @alarm_actions.setter
    def alarm_actions(self, alarm_actions):
        r"""Sets the alarm_actions of this UpdateAlarmRequestBody.

        **参数解释**： 告警触发时，通知组/主题订阅的信息。结构样例如下： { \"type\": \"notification\",\"notificationList\":[\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"] } **约束限制**： 最多包含10个告警触发时的通知对象信息。 

        :param alarm_actions: The alarm_actions of this UpdateAlarmRequestBody.
        :type alarm_actions: list[list[Notification]]
        """
        self._alarm_actions = alarm_actions

    @property
    def insufficientdata_actions(self):
        r"""Gets the insufficientdata_actions of this UpdateAlarmRequestBody.

        **参数解释**： 数据不足触发告警时，通知组/主题订阅的信息。（该参数已废弃，建议无需配置） **约束限制**： 最多包含10个告警动作。 

        :return: The insufficientdata_actions of this UpdateAlarmRequestBody.
        :rtype: list[list[Notification]]
        """
        return self._insufficientdata_actions

    @insufficientdata_actions.setter
    def insufficientdata_actions(self, insufficientdata_actions):
        r"""Sets the insufficientdata_actions of this UpdateAlarmRequestBody.

        **参数解释**： 数据不足触发告警时，通知组/主题订阅的信息。（该参数已废弃，建议无需配置） **约束限制**： 最多包含10个告警动作。 

        :param insufficientdata_actions: The insufficientdata_actions of this UpdateAlarmRequestBody.
        :type insufficientdata_actions: list[list[Notification]]
        """
        self._insufficientdata_actions = insufficientdata_actions

    @property
    def ok_actions(self):
        r"""Gets the ok_actions of this UpdateAlarmRequestBody.

        **参数解释**： 告警恢复时，通知组/主题订阅的信息。结构样例如下： { \"type\": \"notification\",\"notificationList\":[\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"] }  **约束限制**： 最多包含10个告警触发时的通知对象信息。 

        :return: The ok_actions of this UpdateAlarmRequestBody.
        :rtype: list[list[Notification]]
        """
        return self._ok_actions

    @ok_actions.setter
    def ok_actions(self, ok_actions):
        r"""Sets the ok_actions of this UpdateAlarmRequestBody.

        **参数解释**： 告警恢复时，通知组/主题订阅的信息。结构样例如下： { \"type\": \"notification\",\"notificationList\":[\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"] }  **约束限制**： 最多包含10个告警触发时的通知对象信息。 

        :param ok_actions: The ok_actions of this UpdateAlarmRequestBody.
        :type ok_actions: list[list[Notification]]
        """
        self._ok_actions = ok_actions

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
        if not isinstance(other, UpdateAlarmRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
