# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAiOpsRequestBodyAlarm:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'level': 'str',
        'smn_topic': 'str'
    }

    attribute_map = {
        'level': 'level',
        'smn_topic': 'smn_topic'
    }

    def __init__(self, level=None, smn_topic=None):
        r"""CreateAiOpsRequestBodyAlarm

        The model defined in huaweicloud sdk

        :param level: **参数解释**： 报告发送风险类别，当前功能已废弃。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type level: str
        :param smn_topic: **参数解释**： 报告发送主题，当前功能已废弃。 **约束限制**： 不涉及 **默认取值**： 不涉及
        :type smn_topic: str
        """
        
        

        self._level = None
        self._smn_topic = None
        self.discriminator = None

        if level is not None:
            self.level = level
        if smn_topic is not None:
            self.smn_topic = smn_topic

    @property
    def level(self):
        r"""Gets the level of this CreateAiOpsRequestBodyAlarm.

        **参数解释**： 报告发送风险类别，当前功能已废弃。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The level of this CreateAiOpsRequestBodyAlarm.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this CreateAiOpsRequestBodyAlarm.

        **参数解释**： 报告发送风险类别，当前功能已废弃。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param level: The level of this CreateAiOpsRequestBodyAlarm.
        :type level: str
        """
        self._level = level

    @property
    def smn_topic(self):
        r"""Gets the smn_topic of this CreateAiOpsRequestBodyAlarm.

        **参数解释**： 报告发送主题，当前功能已废弃。 **约束限制**： 不涉及 **默认取值**： 不涉及

        :return: The smn_topic of this CreateAiOpsRequestBodyAlarm.
        :rtype: str
        """
        return self._smn_topic

    @smn_topic.setter
    def smn_topic(self, smn_topic):
        r"""Sets the smn_topic of this CreateAiOpsRequestBodyAlarm.

        **参数解释**： 报告发送主题，当前功能已废弃。 **约束限制**： 不涉及 **默认取值**： 不涉及

        :param smn_topic: The smn_topic of this CreateAiOpsRequestBodyAlarm.
        :type smn_topic: str
        """
        self._smn_topic = smn_topic

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
        if not isinstance(other, CreateAiOpsRequestBodyAlarm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
