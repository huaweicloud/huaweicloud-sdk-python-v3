# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAlarmRuleTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_rule_templates': 'list[str]'
    }

    attribute_map = {
        'alarm_rule_templates': 'alarm_rule_templates'
    }

    def __init__(self, alarm_rule_templates=None):
        r"""DeleteAlarmRuleTemplateRequestBody

        The model defined in huaweicloud sdk

        :param alarm_rule_templates: 告警模板id列表。
        :type alarm_rule_templates: list[str]
        """
        
        

        self._alarm_rule_templates = None
        self.discriminator = None

        self.alarm_rule_templates = alarm_rule_templates

    @property
    def alarm_rule_templates(self):
        r"""Gets the alarm_rule_templates of this DeleteAlarmRuleTemplateRequestBody.

        告警模板id列表。

        :return: The alarm_rule_templates of this DeleteAlarmRuleTemplateRequestBody.
        :rtype: list[str]
        """
        return self._alarm_rule_templates

    @alarm_rule_templates.setter
    def alarm_rule_templates(self, alarm_rule_templates):
        r"""Sets the alarm_rule_templates of this DeleteAlarmRuleTemplateRequestBody.

        告警模板id列表。

        :param alarm_rule_templates: The alarm_rule_templates of this DeleteAlarmRuleTemplateRequestBody.
        :type alarm_rule_templates: list[str]
        """
        self._alarm_rule_templates = alarm_rule_templates

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
        if not isinstance(other, DeleteAlarmRuleTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
