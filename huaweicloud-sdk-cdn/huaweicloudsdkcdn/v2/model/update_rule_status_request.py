# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRuleStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'status': 'str',
        'priority': 'int'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'status': 'status',
        'priority': 'priority'
    }

    def __init__(self, rule_id=None, status=None, priority=None):
        r"""UpdateRuleStatusRequest

        The model defined in huaweicloud sdk

        :param rule_id: **参数解释：** 规则ID，可以通过查询规则引擎列表接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type rule_id: str
        :param status: **参数解释：** 是否开启规则 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭 **默认取值：** 不涉及
        :type status: str
        :param priority: **参数解释：** 此条规则的优先级，数值越大，优先级越高 **约束限制：** 优先级不能相同 **取值范围：** 1-100 **默认取值：** 不涉及
        :type priority: int
        """
        
        

        self._rule_id = None
        self._status = None
        self._priority = None
        self.discriminator = None

        self.rule_id = rule_id
        if status is not None:
            self.status = status
        if priority is not None:
            self.priority = priority

    @property
    def rule_id(self):
        r"""Gets the rule_id of this UpdateRuleStatusRequest.

        **参数解释：** 规则ID，可以通过查询规则引擎列表接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The rule_id of this UpdateRuleStatusRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this UpdateRuleStatusRequest.

        **参数解释：** 规则ID，可以通过查询规则引擎列表接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param rule_id: The rule_id of this UpdateRuleStatusRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def status(self):
        r"""Gets the status of this UpdateRuleStatusRequest.

        **参数解释：** 是否开启规则 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭 **默认取值：** 不涉及

        :return: The status of this UpdateRuleStatusRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateRuleStatusRequest.

        **参数解释：** 是否开启规则 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭 **默认取值：** 不涉及

        :param status: The status of this UpdateRuleStatusRequest.
        :type status: str
        """
        self._status = status

    @property
    def priority(self):
        r"""Gets the priority of this UpdateRuleStatusRequest.

        **参数解释：** 此条规则的优先级，数值越大，优先级越高 **约束限制：** 优先级不能相同 **取值范围：** 1-100 **默认取值：** 不涉及

        :return: The priority of this UpdateRuleStatusRequest.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this UpdateRuleStatusRequest.

        **参数解释：** 此条规则的优先级，数值越大，优先级越高 **约束限制：** 优先级不能相同 **取值范围：** 1-100 **默认取值：** 不涉及

        :param priority: The priority of this UpdateRuleStatusRequest.
        :type priority: int
        """
        self._priority = priority

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateRuleStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
