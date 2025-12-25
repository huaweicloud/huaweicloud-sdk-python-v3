# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteOneClickAlarmsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'one_click_alarm_ids': 'list[str]',
        'action_type': 'str'
    }

    attribute_map = {
        'one_click_alarm_ids': 'one_click_alarm_ids',
        'action_type': 'action_type'
    }

    def __init__(self, one_click_alarm_ids=None, action_type=None):
        r"""BatchDeleteOneClickAlarmsRequestBody

        The model defined in huaweicloud sdk

        :param one_click_alarm_ids: **参数解释**： 需要批量删除的一键告警ID列表。 **约束限制**： 一键告警ID数量最多为100个，至少1个。 
        :type one_click_alarm_ids: list[str]
        :param action_type: **参数解释**： 操作类型。 **约束限制**： 不涉及。 **取值范围**： 枚举值。取值为disable - disable: 关闭一键告警 **默认取值**： 不涉及。 
        :type action_type: str
        """
        
        

        self._one_click_alarm_ids = None
        self._action_type = None
        self.discriminator = None

        self.one_click_alarm_ids = one_click_alarm_ids
        if action_type is not None:
            self.action_type = action_type

    @property
    def one_click_alarm_ids(self):
        r"""Gets the one_click_alarm_ids of this BatchDeleteOneClickAlarmsRequestBody.

        **参数解释**： 需要批量删除的一键告警ID列表。 **约束限制**： 一键告警ID数量最多为100个，至少1个。 

        :return: The one_click_alarm_ids of this BatchDeleteOneClickAlarmsRequestBody.
        :rtype: list[str]
        """
        return self._one_click_alarm_ids

    @one_click_alarm_ids.setter
    def one_click_alarm_ids(self, one_click_alarm_ids):
        r"""Sets the one_click_alarm_ids of this BatchDeleteOneClickAlarmsRequestBody.

        **参数解释**： 需要批量删除的一键告警ID列表。 **约束限制**： 一键告警ID数量最多为100个，至少1个。 

        :param one_click_alarm_ids: The one_click_alarm_ids of this BatchDeleteOneClickAlarmsRequestBody.
        :type one_click_alarm_ids: list[str]
        """
        self._one_click_alarm_ids = one_click_alarm_ids

    @property
    def action_type(self):
        r"""Gets the action_type of this BatchDeleteOneClickAlarmsRequestBody.

        **参数解释**： 操作类型。 **约束限制**： 不涉及。 **取值范围**： 枚举值。取值为disable - disable: 关闭一键告警 **默认取值**： 不涉及。 

        :return: The action_type of this BatchDeleteOneClickAlarmsRequestBody.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this BatchDeleteOneClickAlarmsRequestBody.

        **参数解释**： 操作类型。 **约束限制**： 不涉及。 **取值范围**： 枚举值。取值为disable - disable: 关闭一键告警 **默认取值**： 不涉及。 

        :param action_type: The action_type of this BatchDeleteOneClickAlarmsRequestBody.
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
        if not isinstance(other, BatchDeleteOneClickAlarmsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
