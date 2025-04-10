# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlaRuleInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status_type': 'str',
        'triggering_rule_enable': 'bool',
        'pre_warning_rule_enable': 'bool',
        'escalate_rule_enable': 'bool',
        'triggering_rule': 'SlaTriggeringRuleInfo',
        'pre_warning_rule': 'SlaPreWarningRuleInfo',
        'escalate_rules': 'list[SlaEscalationRuleInfo]'
    }

    attribute_map = {
        'status_type': 'status_type',
        'triggering_rule_enable': 'triggering_rule_enable',
        'pre_warning_rule_enable': 'pre_warning_rule_enable',
        'escalate_rule_enable': 'escalate_rule_enable',
        'triggering_rule': 'triggering_rule',
        'pre_warning_rule': 'pre_warning_rule',
        'escalate_rules': 'escalate_rules'
    }

    def __init__(self, status_type=None, triggering_rule_enable=None, pre_warning_rule_enable=None, escalate_rule_enable=None, triggering_rule=None, pre_warning_rule=None, escalate_rules=None):
        r"""SlaRuleInfo

        The model defined in huaweicloud sdk

        :param status_type: 状态类型: EVENT_TICKET_NOT_ACCEPTED EVENT_TICKET_PROCESSING EVENT_TICKET_RESOLVED ALARM_TICKET_ALARMING CHANGE_REVIEW CHANGE_IMPLEMENTATION CHANGE_VERIFICATION TO_DO_TASKS_TO_BE_HANDLED TO_DO_TASKS_PROCESSING ISSUE_TICKET_NOT_ACCEPTED ISSUE_TICKET_POSITIONING ISSUE_TICKET_WAITING_IMPLEMENT ISSUE_TICKET_RESOLVED
        :type status_type: str
        :param triggering_rule_enable: 触发规则是否生效
        :type triggering_rule_enable: bool
        :param pre_warning_rule_enable: 预警规则是否生效
        :type pre_warning_rule_enable: bool
        :param escalate_rule_enable: 上升规则是否生效
        :type escalate_rule_enable: bool
        :param triggering_rule: 
        :type triggering_rule: :class:`huaweicloudsdkcoc.v1.SlaTriggeringRuleInfo`
        :param pre_warning_rule: 
        :type pre_warning_rule: :class:`huaweicloudsdkcoc.v1.SlaPreWarningRuleInfo`
        :param escalate_rules: 通知配置
        :type escalate_rules: list[:class:`huaweicloudsdkcoc.v1.SlaEscalationRuleInfo`]
        """
        
        

        self._status_type = None
        self._triggering_rule_enable = None
        self._pre_warning_rule_enable = None
        self._escalate_rule_enable = None
        self._triggering_rule = None
        self._pre_warning_rule = None
        self._escalate_rules = None
        self.discriminator = None

        self.status_type = status_type
        self.triggering_rule_enable = triggering_rule_enable
        self.pre_warning_rule_enable = pre_warning_rule_enable
        if escalate_rule_enable is not None:
            self.escalate_rule_enable = escalate_rule_enable
        if triggering_rule is not None:
            self.triggering_rule = triggering_rule
        if pre_warning_rule is not None:
            self.pre_warning_rule = pre_warning_rule
        if escalate_rules is not None:
            self.escalate_rules = escalate_rules

    @property
    def status_type(self):
        r"""Gets the status_type of this SlaRuleInfo.

        状态类型: EVENT_TICKET_NOT_ACCEPTED EVENT_TICKET_PROCESSING EVENT_TICKET_RESOLVED ALARM_TICKET_ALARMING CHANGE_REVIEW CHANGE_IMPLEMENTATION CHANGE_VERIFICATION TO_DO_TASKS_TO_BE_HANDLED TO_DO_TASKS_PROCESSING ISSUE_TICKET_NOT_ACCEPTED ISSUE_TICKET_POSITIONING ISSUE_TICKET_WAITING_IMPLEMENT ISSUE_TICKET_RESOLVED

        :return: The status_type of this SlaRuleInfo.
        :rtype: str
        """
        return self._status_type

    @status_type.setter
    def status_type(self, status_type):
        r"""Sets the status_type of this SlaRuleInfo.

        状态类型: EVENT_TICKET_NOT_ACCEPTED EVENT_TICKET_PROCESSING EVENT_TICKET_RESOLVED ALARM_TICKET_ALARMING CHANGE_REVIEW CHANGE_IMPLEMENTATION CHANGE_VERIFICATION TO_DO_TASKS_TO_BE_HANDLED TO_DO_TASKS_PROCESSING ISSUE_TICKET_NOT_ACCEPTED ISSUE_TICKET_POSITIONING ISSUE_TICKET_WAITING_IMPLEMENT ISSUE_TICKET_RESOLVED

        :param status_type: The status_type of this SlaRuleInfo.
        :type status_type: str
        """
        self._status_type = status_type

    @property
    def triggering_rule_enable(self):
        r"""Gets the triggering_rule_enable of this SlaRuleInfo.

        触发规则是否生效

        :return: The triggering_rule_enable of this SlaRuleInfo.
        :rtype: bool
        """
        return self._triggering_rule_enable

    @triggering_rule_enable.setter
    def triggering_rule_enable(self, triggering_rule_enable):
        r"""Sets the triggering_rule_enable of this SlaRuleInfo.

        触发规则是否生效

        :param triggering_rule_enable: The triggering_rule_enable of this SlaRuleInfo.
        :type triggering_rule_enable: bool
        """
        self._triggering_rule_enable = triggering_rule_enable

    @property
    def pre_warning_rule_enable(self):
        r"""Gets the pre_warning_rule_enable of this SlaRuleInfo.

        预警规则是否生效

        :return: The pre_warning_rule_enable of this SlaRuleInfo.
        :rtype: bool
        """
        return self._pre_warning_rule_enable

    @pre_warning_rule_enable.setter
    def pre_warning_rule_enable(self, pre_warning_rule_enable):
        r"""Sets the pre_warning_rule_enable of this SlaRuleInfo.

        预警规则是否生效

        :param pre_warning_rule_enable: The pre_warning_rule_enable of this SlaRuleInfo.
        :type pre_warning_rule_enable: bool
        """
        self._pre_warning_rule_enable = pre_warning_rule_enable

    @property
    def escalate_rule_enable(self):
        r"""Gets the escalate_rule_enable of this SlaRuleInfo.

        上升规则是否生效

        :return: The escalate_rule_enable of this SlaRuleInfo.
        :rtype: bool
        """
        return self._escalate_rule_enable

    @escalate_rule_enable.setter
    def escalate_rule_enable(self, escalate_rule_enable):
        r"""Sets the escalate_rule_enable of this SlaRuleInfo.

        上升规则是否生效

        :param escalate_rule_enable: The escalate_rule_enable of this SlaRuleInfo.
        :type escalate_rule_enable: bool
        """
        self._escalate_rule_enable = escalate_rule_enable

    @property
    def triggering_rule(self):
        r"""Gets the triggering_rule of this SlaRuleInfo.

        :return: The triggering_rule of this SlaRuleInfo.
        :rtype: :class:`huaweicloudsdkcoc.v1.SlaTriggeringRuleInfo`
        """
        return self._triggering_rule

    @triggering_rule.setter
    def triggering_rule(self, triggering_rule):
        r"""Sets the triggering_rule of this SlaRuleInfo.

        :param triggering_rule: The triggering_rule of this SlaRuleInfo.
        :type triggering_rule: :class:`huaweicloudsdkcoc.v1.SlaTriggeringRuleInfo`
        """
        self._triggering_rule = triggering_rule

    @property
    def pre_warning_rule(self):
        r"""Gets the pre_warning_rule of this SlaRuleInfo.

        :return: The pre_warning_rule of this SlaRuleInfo.
        :rtype: :class:`huaweicloudsdkcoc.v1.SlaPreWarningRuleInfo`
        """
        return self._pre_warning_rule

    @pre_warning_rule.setter
    def pre_warning_rule(self, pre_warning_rule):
        r"""Sets the pre_warning_rule of this SlaRuleInfo.

        :param pre_warning_rule: The pre_warning_rule of this SlaRuleInfo.
        :type pre_warning_rule: :class:`huaweicloudsdkcoc.v1.SlaPreWarningRuleInfo`
        """
        self._pre_warning_rule = pre_warning_rule

    @property
    def escalate_rules(self):
        r"""Gets the escalate_rules of this SlaRuleInfo.

        通知配置

        :return: The escalate_rules of this SlaRuleInfo.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.SlaEscalationRuleInfo`]
        """
        return self._escalate_rules

    @escalate_rules.setter
    def escalate_rules(self, escalate_rules):
        r"""Sets the escalate_rules of this SlaRuleInfo.

        通知配置

        :param escalate_rules: The escalate_rules of this SlaRuleInfo.
        :type escalate_rules: list[:class:`huaweicloudsdkcoc.v1.SlaEscalationRuleInfo`]
        """
        self._escalate_rules = escalate_rules

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
        if not isinstance(other, SlaRuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
