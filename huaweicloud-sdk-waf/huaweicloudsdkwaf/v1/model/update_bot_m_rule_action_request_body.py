# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBotMRuleActionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'defense_action': 'int'
    }

    attribute_map = {
        'defense_action': 'defense_action'
    }

    def __init__(self, defense_action=None):
        r"""UpdateBotMRuleActionRequestBody

        The model defined in huaweicloud sdk

        :param defense_action: 防护动作对应的数字
        :type defense_action: int
        """
        
        

        self._defense_action = None
        self.discriminator = None

        if defense_action is not None:
            self.defense_action = defense_action

    @property
    def defense_action(self):
        r"""Gets the defense_action of this UpdateBotMRuleActionRequestBody.

        防护动作对应的数字

        :return: The defense_action of this UpdateBotMRuleActionRequestBody.
        :rtype: int
        """
        return self._defense_action

    @defense_action.setter
    def defense_action(self, defense_action):
        r"""Sets the defense_action of this UpdateBotMRuleActionRequestBody.

        防护动作对应的数字

        :param defense_action: The defense_action of this UpdateBotMRuleActionRequestBody.
        :type defense_action: int
        """
        self._defense_action = defense_action

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
        if not isinstance(other, UpdateBotMRuleActionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
