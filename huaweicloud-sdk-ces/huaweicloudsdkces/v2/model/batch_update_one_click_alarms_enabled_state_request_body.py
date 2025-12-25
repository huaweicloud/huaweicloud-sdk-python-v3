# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateOneClickAlarmsEnabledStateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_ids': 'list[str]',
        'alarm_enabled': 'bool',
        'retain_when_all_disabled': 'bool',
        'action_type': 'str'
    }

    attribute_map = {
        'alarm_ids': 'alarm_ids',
        'alarm_enabled': 'alarm_enabled',
        'retain_when_all_disabled': 'retain_when_all_disabled',
        'action_type': 'action_type'
    }

    def __init__(self, alarm_ids=None, alarm_enabled=None, retain_when_all_disabled=None, action_type=None):
        r"""BatchUpdateOneClickAlarmsEnabledStateRequestBody

        The model defined in huaweicloud sdk

        :param alarm_ids: **参数解释** 需要批量启停的告警规则的ID列表 **约束限制** 包含的告警规则ID个数为1到100 
        :type alarm_ids: list[str]
        :param alarm_enabled: **参数解释**： 是否开启告警规则。     **约束限制**： 不涉及。 **取值范围**： 布尔值。 - true:开启。 - false:关闭。 **默认取值**： true 
        :type alarm_enabled: bool
        :param retain_when_all_disabled: **参数解释** 一键告警中的规则全部被停用时是否保留规则信息 **约束限制** 不涉及 **取值范围** - true:保留规则信息 - false:不保留规则信息 **默认取值** false 
        :type retain_when_all_disabled: bool
        :param action_type: **参数解释** 当传此参数时，将会批量停用一键告警规则 **约束限制** 不涉及 **取值范围** - disable: 表示将会批量停用一键告警规则 **默认取值** 不涉及 
        :type action_type: str
        """
        
        

        self._alarm_ids = None
        self._alarm_enabled = None
        self._retain_when_all_disabled = None
        self._action_type = None
        self.discriminator = None

        self.alarm_ids = alarm_ids
        self.alarm_enabled = alarm_enabled
        if retain_when_all_disabled is not None:
            self.retain_when_all_disabled = retain_when_all_disabled
        if action_type is not None:
            self.action_type = action_type

    @property
    def alarm_ids(self):
        r"""Gets the alarm_ids of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.

        **参数解释** 需要批量启停的告警规则的ID列表 **约束限制** 包含的告警规则ID个数为1到100 

        :return: The alarm_ids of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.
        :rtype: list[str]
        """
        return self._alarm_ids

    @alarm_ids.setter
    def alarm_ids(self, alarm_ids):
        r"""Sets the alarm_ids of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.

        **参数解释** 需要批量启停的告警规则的ID列表 **约束限制** 包含的告警规则ID个数为1到100 

        :param alarm_ids: The alarm_ids of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.
        :type alarm_ids: list[str]
        """
        self._alarm_ids = alarm_ids

    @property
    def alarm_enabled(self):
        r"""Gets the alarm_enabled of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.

        **参数解释**： 是否开启告警规则。     **约束限制**： 不涉及。 **取值范围**： 布尔值。 - true:开启。 - false:关闭。 **默认取值**： true 

        :return: The alarm_enabled of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.
        :rtype: bool
        """
        return self._alarm_enabled

    @alarm_enabled.setter
    def alarm_enabled(self, alarm_enabled):
        r"""Sets the alarm_enabled of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.

        **参数解释**： 是否开启告警规则。     **约束限制**： 不涉及。 **取值范围**： 布尔值。 - true:开启。 - false:关闭。 **默认取值**： true 

        :param alarm_enabled: The alarm_enabled of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.
        :type alarm_enabled: bool
        """
        self._alarm_enabled = alarm_enabled

    @property
    def retain_when_all_disabled(self):
        r"""Gets the retain_when_all_disabled of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.

        **参数解释** 一键告警中的规则全部被停用时是否保留规则信息 **约束限制** 不涉及 **取值范围** - true:保留规则信息 - false:不保留规则信息 **默认取值** false 

        :return: The retain_when_all_disabled of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.
        :rtype: bool
        """
        return self._retain_when_all_disabled

    @retain_when_all_disabled.setter
    def retain_when_all_disabled(self, retain_when_all_disabled):
        r"""Sets the retain_when_all_disabled of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.

        **参数解释** 一键告警中的规则全部被停用时是否保留规则信息 **约束限制** 不涉及 **取值范围** - true:保留规则信息 - false:不保留规则信息 **默认取值** false 

        :param retain_when_all_disabled: The retain_when_all_disabled of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.
        :type retain_when_all_disabled: bool
        """
        self._retain_when_all_disabled = retain_when_all_disabled

    @property
    def action_type(self):
        r"""Gets the action_type of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.

        **参数解释** 当传此参数时，将会批量停用一键告警规则 **约束限制** 不涉及 **取值范围** - disable: 表示将会批量停用一键告警规则 **默认取值** 不涉及 

        :return: The action_type of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.

        **参数解释** 当传此参数时，将会批量停用一键告警规则 **约束限制** 不涉及 **取值范围** - disable: 表示将会批量停用一键告警规则 **默认取值** 不涉及 

        :param action_type: The action_type of this BatchUpdateOneClickAlarmsEnabledStateRequestBody.
        :type action_type: str
        """
        self._action_type = action_type

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
        if not isinstance(other, BatchUpdateOneClickAlarmsEnabledStateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
