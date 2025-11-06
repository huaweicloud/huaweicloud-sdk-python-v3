# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_rules': 'list[BatchAlarmRulesBody]',
        'update_action_rules': 'list[BatchUpdateActionRules]',
        'update_type': 'str'
    }

    attribute_map = {
        'alarm_rules': 'alarm_rules',
        'update_action_rules': 'update_action_rules',
        'update_type': 'update_type'
    }

    def __init__(self, alarm_rules=None, update_action_rules=None, update_type=None):
        r"""BatchUpdateRequest

        The model defined in huaweicloud sdk

        :param alarm_rules: 批量启停的告警规则列表。批量启停告警规则时，该参数必填。
        :type alarm_rules: list[:class:`huaweicloudsdkaom.v2.BatchAlarmRulesBody`]
        :param update_action_rules: 批量修改告警行动规则的告警规则列表。批量修改告警行动规则时，该参数必填。
        :type update_action_rules: list[:class:`huaweicloudsdkaom.v2.BatchUpdateActionRules`]
        :param update_type: 更新类型：BATCH_UPDATE_ACTION_RULE。批量修改告警行动规则时，该参数必填。
        :type update_type: str
        """
        
        

        self._alarm_rules = None
        self._update_action_rules = None
        self._update_type = None
        self.discriminator = None

        if alarm_rules is not None:
            self.alarm_rules = alarm_rules
        if update_action_rules is not None:
            self.update_action_rules = update_action_rules
        if update_type is not None:
            self.update_type = update_type

    @property
    def alarm_rules(self):
        r"""Gets the alarm_rules of this BatchUpdateRequest.

        批量启停的告警规则列表。批量启停告警规则时，该参数必填。

        :return: The alarm_rules of this BatchUpdateRequest.
        :rtype: list[:class:`huaweicloudsdkaom.v2.BatchAlarmRulesBody`]
        """
        return self._alarm_rules

    @alarm_rules.setter
    def alarm_rules(self, alarm_rules):
        r"""Sets the alarm_rules of this BatchUpdateRequest.

        批量启停的告警规则列表。批量启停告警规则时，该参数必填。

        :param alarm_rules: The alarm_rules of this BatchUpdateRequest.
        :type alarm_rules: list[:class:`huaweicloudsdkaom.v2.BatchAlarmRulesBody`]
        """
        self._alarm_rules = alarm_rules

    @property
    def update_action_rules(self):
        r"""Gets the update_action_rules of this BatchUpdateRequest.

        批量修改告警行动规则的告警规则列表。批量修改告警行动规则时，该参数必填。

        :return: The update_action_rules of this BatchUpdateRequest.
        :rtype: list[:class:`huaweicloudsdkaom.v2.BatchUpdateActionRules`]
        """
        return self._update_action_rules

    @update_action_rules.setter
    def update_action_rules(self, update_action_rules):
        r"""Sets the update_action_rules of this BatchUpdateRequest.

        批量修改告警行动规则的告警规则列表。批量修改告警行动规则时，该参数必填。

        :param update_action_rules: The update_action_rules of this BatchUpdateRequest.
        :type update_action_rules: list[:class:`huaweicloudsdkaom.v2.BatchUpdateActionRules`]
        """
        self._update_action_rules = update_action_rules

    @property
    def update_type(self):
        r"""Gets the update_type of this BatchUpdateRequest.

        更新类型：BATCH_UPDATE_ACTION_RULE。批量修改告警行动规则时，该参数必填。

        :return: The update_type of this BatchUpdateRequest.
        :rtype: str
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        r"""Sets the update_type of this BatchUpdateRequest.

        更新类型：BATCH_UPDATE_ACTION_RULE。批量修改告警行动规则时，该参数必填。

        :param update_type: The update_type of this BatchUpdateRequest.
        :type update_type: str
        """
        self._update_type = update_type

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
        if not isinstance(other, BatchUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
