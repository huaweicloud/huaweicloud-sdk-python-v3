# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmRuleTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_rule_templates': 'list[AlarmRuleTemplateBody]',
        'count': 'int'
    }

    attribute_map = {
        'alarm_rule_templates': 'alarm_rule_templates',
        'count': 'count'
    }

    def __init__(self, alarm_rule_templates=None, count=None):
        r"""ListAlarmRuleTemplateResponse

        The model defined in huaweicloud sdk

        :param alarm_rule_templates: 告警模板列表。
        :type alarm_rule_templates: list[:class:`huaweicloudsdkaom.v2.AlarmRuleTemplateBody`]
        :param count: 告警模板总数。
        :type count: int
        """
        
        super().__init__()

        self._alarm_rule_templates = None
        self._count = None
        self.discriminator = None

        if alarm_rule_templates is not None:
            self.alarm_rule_templates = alarm_rule_templates
        if count is not None:
            self.count = count

    @property
    def alarm_rule_templates(self):
        r"""Gets the alarm_rule_templates of this ListAlarmRuleTemplateResponse.

        告警模板列表。

        :return: The alarm_rule_templates of this ListAlarmRuleTemplateResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v2.AlarmRuleTemplateBody`]
        """
        return self._alarm_rule_templates

    @alarm_rule_templates.setter
    def alarm_rule_templates(self, alarm_rule_templates):
        r"""Sets the alarm_rule_templates of this ListAlarmRuleTemplateResponse.

        告警模板列表。

        :param alarm_rule_templates: The alarm_rule_templates of this ListAlarmRuleTemplateResponse.
        :type alarm_rule_templates: list[:class:`huaweicloudsdkaom.v2.AlarmRuleTemplateBody`]
        """
        self._alarm_rule_templates = alarm_rule_templates

    @property
    def count(self):
        r"""Gets the count of this ListAlarmRuleTemplateResponse.

        告警模板总数。

        :return: The count of this ListAlarmRuleTemplateResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListAlarmRuleTemplateResponse.

        告警模板总数。

        :param count: The count of this ListAlarmRuleTemplateResponse.
        :type count: int
        """
        self._count = count

    def to_dict(self):
        import warnings
        warnings.warn("ListAlarmRuleTemplateResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListAlarmRuleTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
