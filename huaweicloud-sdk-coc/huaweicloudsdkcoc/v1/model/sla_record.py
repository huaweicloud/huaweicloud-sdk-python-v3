# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlaRecord:

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
        'sub_trigger_node': 'str',
        'sla_status': 'bool',
        'sla_order_id': 'str',
        'duration': 'int',
        'triggering_rule_enable': 'bool',
        'triggering_rule': 'SlaTriggeringRuleInfo',
        'break_time': 'str',
        'owner_id': 'str',
        'owner_name': 'str',
        'notice_time': 'str',
        'status_start_time': 'str',
        'pre_warning_rule_enable': 'bool',
        'pre_warning_rule': 'SlaPreWarningRuleInfo',
        'escalate_rule_enable': 'bool',
        'escalate_rules': 'list[SlaEscalationRuleInfo]',
        'current_node': 'bool'
    }

    attribute_map = {
        'status_type': 'status_type',
        'sub_trigger_node': 'sub_trigger_node',
        'sla_status': 'sla_status',
        'sla_order_id': 'sla_order_id',
        'duration': 'duration',
        'triggering_rule_enable': 'triggering_rule_enable',
        'triggering_rule': 'triggering_rule',
        'break_time': 'break_time',
        'owner_id': 'owner_id',
        'owner_name': 'owner_name',
        'notice_time': 'notice_time',
        'status_start_time': 'status_start_time',
        'pre_warning_rule_enable': 'pre_warning_rule_enable',
        'pre_warning_rule': 'pre_warning_rule',
        'escalate_rule_enable': 'escalate_rule_enable',
        'escalate_rules': 'escalate_rules',
        'current_node': 'current_node'
    }

    def __init__(self, status_type=None, sub_trigger_node=None, sla_status=None, sla_order_id=None, duration=None, triggering_rule_enable=None, triggering_rule=None, break_time=None, owner_id=None, owner_name=None, notice_time=None, status_start_time=None, pre_warning_rule_enable=None, pre_warning_rule=None, escalate_rule_enable=None, escalate_rules=None, current_node=None):
        r"""SlaRecord

        The model defined in huaweicloud sdk

        :param status_type: 状态类型: EVENT_TICKET_NOT_ACCEPTED EVENT_TICKET_PROCESSING EVENT_TICKET_NOT_IN_TIME EVENT_TICKET_RESOLVED ALARM_TICKET_RESOLVED ALARM_TICKET_ALARMING ALARM_TICKET_NOT_IN_TIME CHANGE_NOT_IN_TIME CHANGE_REVIEW CHANGE_IMPLEMENTATION CHANGE_VERIFICATION TO_DO_TASKS_NOT_IN_TIME TO_DO_TASKS_TO_BE_HANDLED TO_DO_TASKS_PROCESSING TO_DO_TASKS_COMPLETED ISSUE_TICKET_NOT_IN_TIME ISSUE_TICKET_NOT_ACCEPTED ISSUE_TICKET_POSITIONING ISSUE_TICKET_WAITING_IMPLEMENT ISSUE_TICKET_RESOLVED
        :type status_type: str
        :param sub_trigger_node: 子状态(NORMAL,FORWARDING,RESUBMIT)
        :type sub_trigger_node: str
        :param sla_status: Sla状态  false 未打破
        :type sla_status: bool
        :param sla_order_id: 工单ID
        :type sla_order_id: str
        :param duration: 持续时间
        :type duration: int
        :param triggering_rule_enable: SLA 触发规则是否开启
        :type triggering_rule_enable: bool
        :param triggering_rule: 
        :type triggering_rule: :class:`huaweicloudsdkcoc.v1.SlaTriggeringRuleInfo`
        :param break_time: 打破时间
        :type break_time: str
        :param owner_id: 对象ID
        :type owner_id: str
        :param owner_name: 对象人名
        :type owner_name: str
        :param notice_time: 通知时间
        :type notice_time: str
        :param status_start_time: 状态开始时间
        :type status_start_time: str
        :param pre_warning_rule_enable: SLA 预警通知是否开启
        :type pre_warning_rule_enable: bool
        :param pre_warning_rule: 
        :type pre_warning_rule: :class:`huaweicloudsdkcoc.v1.SlaPreWarningRuleInfo`
        :param escalate_rule_enable: SLA 上升通知是否开启
        :type escalate_rule_enable: bool
        :param escalate_rules: SLA 上升通知配置
        :type escalate_rules: list[:class:`huaweicloudsdkcoc.v1.SlaEscalationRuleInfo`]
        :param current_node: SLA是否在当前状态
        :type current_node: bool
        """
        
        

        self._status_type = None
        self._sub_trigger_node = None
        self._sla_status = None
        self._sla_order_id = None
        self._duration = None
        self._triggering_rule_enable = None
        self._triggering_rule = None
        self._break_time = None
        self._owner_id = None
        self._owner_name = None
        self._notice_time = None
        self._status_start_time = None
        self._pre_warning_rule_enable = None
        self._pre_warning_rule = None
        self._escalate_rule_enable = None
        self._escalate_rules = None
        self._current_node = None
        self.discriminator = None

        if status_type is not None:
            self.status_type = status_type
        if sub_trigger_node is not None:
            self.sub_trigger_node = sub_trigger_node
        if sla_status is not None:
            self.sla_status = sla_status
        if sla_order_id is not None:
            self.sla_order_id = sla_order_id
        if duration is not None:
            self.duration = duration
        if triggering_rule_enable is not None:
            self.triggering_rule_enable = triggering_rule_enable
        if triggering_rule is not None:
            self.triggering_rule = triggering_rule
        if break_time is not None:
            self.break_time = break_time
        if owner_id is not None:
            self.owner_id = owner_id
        if owner_name is not None:
            self.owner_name = owner_name
        if notice_time is not None:
            self.notice_time = notice_time
        if status_start_time is not None:
            self.status_start_time = status_start_time
        if pre_warning_rule_enable is not None:
            self.pre_warning_rule_enable = pre_warning_rule_enable
        if pre_warning_rule is not None:
            self.pre_warning_rule = pre_warning_rule
        if escalate_rule_enable is not None:
            self.escalate_rule_enable = escalate_rule_enable
        if escalate_rules is not None:
            self.escalate_rules = escalate_rules
        if current_node is not None:
            self.current_node = current_node

    @property
    def status_type(self):
        r"""Gets the status_type of this SlaRecord.

        状态类型: EVENT_TICKET_NOT_ACCEPTED EVENT_TICKET_PROCESSING EVENT_TICKET_NOT_IN_TIME EVENT_TICKET_RESOLVED ALARM_TICKET_RESOLVED ALARM_TICKET_ALARMING ALARM_TICKET_NOT_IN_TIME CHANGE_NOT_IN_TIME CHANGE_REVIEW CHANGE_IMPLEMENTATION CHANGE_VERIFICATION TO_DO_TASKS_NOT_IN_TIME TO_DO_TASKS_TO_BE_HANDLED TO_DO_TASKS_PROCESSING TO_DO_TASKS_COMPLETED ISSUE_TICKET_NOT_IN_TIME ISSUE_TICKET_NOT_ACCEPTED ISSUE_TICKET_POSITIONING ISSUE_TICKET_WAITING_IMPLEMENT ISSUE_TICKET_RESOLVED

        :return: The status_type of this SlaRecord.
        :rtype: str
        """
        return self._status_type

    @status_type.setter
    def status_type(self, status_type):
        r"""Sets the status_type of this SlaRecord.

        状态类型: EVENT_TICKET_NOT_ACCEPTED EVENT_TICKET_PROCESSING EVENT_TICKET_NOT_IN_TIME EVENT_TICKET_RESOLVED ALARM_TICKET_RESOLVED ALARM_TICKET_ALARMING ALARM_TICKET_NOT_IN_TIME CHANGE_NOT_IN_TIME CHANGE_REVIEW CHANGE_IMPLEMENTATION CHANGE_VERIFICATION TO_DO_TASKS_NOT_IN_TIME TO_DO_TASKS_TO_BE_HANDLED TO_DO_TASKS_PROCESSING TO_DO_TASKS_COMPLETED ISSUE_TICKET_NOT_IN_TIME ISSUE_TICKET_NOT_ACCEPTED ISSUE_TICKET_POSITIONING ISSUE_TICKET_WAITING_IMPLEMENT ISSUE_TICKET_RESOLVED

        :param status_type: The status_type of this SlaRecord.
        :type status_type: str
        """
        self._status_type = status_type

    @property
    def sub_trigger_node(self):
        r"""Gets the sub_trigger_node of this SlaRecord.

        子状态(NORMAL,FORWARDING,RESUBMIT)

        :return: The sub_trigger_node of this SlaRecord.
        :rtype: str
        """
        return self._sub_trigger_node

    @sub_trigger_node.setter
    def sub_trigger_node(self, sub_trigger_node):
        r"""Sets the sub_trigger_node of this SlaRecord.

        子状态(NORMAL,FORWARDING,RESUBMIT)

        :param sub_trigger_node: The sub_trigger_node of this SlaRecord.
        :type sub_trigger_node: str
        """
        self._sub_trigger_node = sub_trigger_node

    @property
    def sla_status(self):
        r"""Gets the sla_status of this SlaRecord.

        Sla状态  false 未打破

        :return: The sla_status of this SlaRecord.
        :rtype: bool
        """
        return self._sla_status

    @sla_status.setter
    def sla_status(self, sla_status):
        r"""Sets the sla_status of this SlaRecord.

        Sla状态  false 未打破

        :param sla_status: The sla_status of this SlaRecord.
        :type sla_status: bool
        """
        self._sla_status = sla_status

    @property
    def sla_order_id(self):
        r"""Gets the sla_order_id of this SlaRecord.

        工单ID

        :return: The sla_order_id of this SlaRecord.
        :rtype: str
        """
        return self._sla_order_id

    @sla_order_id.setter
    def sla_order_id(self, sla_order_id):
        r"""Sets the sla_order_id of this SlaRecord.

        工单ID

        :param sla_order_id: The sla_order_id of this SlaRecord.
        :type sla_order_id: str
        """
        self._sla_order_id = sla_order_id

    @property
    def duration(self):
        r"""Gets the duration of this SlaRecord.

        持续时间

        :return: The duration of this SlaRecord.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this SlaRecord.

        持续时间

        :param duration: The duration of this SlaRecord.
        :type duration: int
        """
        self._duration = duration

    @property
    def triggering_rule_enable(self):
        r"""Gets the triggering_rule_enable of this SlaRecord.

        SLA 触发规则是否开启

        :return: The triggering_rule_enable of this SlaRecord.
        :rtype: bool
        """
        return self._triggering_rule_enable

    @triggering_rule_enable.setter
    def triggering_rule_enable(self, triggering_rule_enable):
        r"""Sets the triggering_rule_enable of this SlaRecord.

        SLA 触发规则是否开启

        :param triggering_rule_enable: The triggering_rule_enable of this SlaRecord.
        :type triggering_rule_enable: bool
        """
        self._triggering_rule_enable = triggering_rule_enable

    @property
    def triggering_rule(self):
        r"""Gets the triggering_rule of this SlaRecord.

        :return: The triggering_rule of this SlaRecord.
        :rtype: :class:`huaweicloudsdkcoc.v1.SlaTriggeringRuleInfo`
        """
        return self._triggering_rule

    @triggering_rule.setter
    def triggering_rule(self, triggering_rule):
        r"""Sets the triggering_rule of this SlaRecord.

        :param triggering_rule: The triggering_rule of this SlaRecord.
        :type triggering_rule: :class:`huaweicloudsdkcoc.v1.SlaTriggeringRuleInfo`
        """
        self._triggering_rule = triggering_rule

    @property
    def break_time(self):
        r"""Gets the break_time of this SlaRecord.

        打破时间

        :return: The break_time of this SlaRecord.
        :rtype: str
        """
        return self._break_time

    @break_time.setter
    def break_time(self, break_time):
        r"""Sets the break_time of this SlaRecord.

        打破时间

        :param break_time: The break_time of this SlaRecord.
        :type break_time: str
        """
        self._break_time = break_time

    @property
    def owner_id(self):
        r"""Gets the owner_id of this SlaRecord.

        对象ID

        :return: The owner_id of this SlaRecord.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this SlaRecord.

        对象ID

        :param owner_id: The owner_id of this SlaRecord.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def owner_name(self):
        r"""Gets the owner_name of this SlaRecord.

        对象人名

        :return: The owner_name of this SlaRecord.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this SlaRecord.

        对象人名

        :param owner_name: The owner_name of this SlaRecord.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def notice_time(self):
        r"""Gets the notice_time of this SlaRecord.

        通知时间

        :return: The notice_time of this SlaRecord.
        :rtype: str
        """
        return self._notice_time

    @notice_time.setter
    def notice_time(self, notice_time):
        r"""Sets the notice_time of this SlaRecord.

        通知时间

        :param notice_time: The notice_time of this SlaRecord.
        :type notice_time: str
        """
        self._notice_time = notice_time

    @property
    def status_start_time(self):
        r"""Gets the status_start_time of this SlaRecord.

        状态开始时间

        :return: The status_start_time of this SlaRecord.
        :rtype: str
        """
        return self._status_start_time

    @status_start_time.setter
    def status_start_time(self, status_start_time):
        r"""Sets the status_start_time of this SlaRecord.

        状态开始时间

        :param status_start_time: The status_start_time of this SlaRecord.
        :type status_start_time: str
        """
        self._status_start_time = status_start_time

    @property
    def pre_warning_rule_enable(self):
        r"""Gets the pre_warning_rule_enable of this SlaRecord.

        SLA 预警通知是否开启

        :return: The pre_warning_rule_enable of this SlaRecord.
        :rtype: bool
        """
        return self._pre_warning_rule_enable

    @pre_warning_rule_enable.setter
    def pre_warning_rule_enable(self, pre_warning_rule_enable):
        r"""Sets the pre_warning_rule_enable of this SlaRecord.

        SLA 预警通知是否开启

        :param pre_warning_rule_enable: The pre_warning_rule_enable of this SlaRecord.
        :type pre_warning_rule_enable: bool
        """
        self._pre_warning_rule_enable = pre_warning_rule_enable

    @property
    def pre_warning_rule(self):
        r"""Gets the pre_warning_rule of this SlaRecord.

        :return: The pre_warning_rule of this SlaRecord.
        :rtype: :class:`huaweicloudsdkcoc.v1.SlaPreWarningRuleInfo`
        """
        return self._pre_warning_rule

    @pre_warning_rule.setter
    def pre_warning_rule(self, pre_warning_rule):
        r"""Sets the pre_warning_rule of this SlaRecord.

        :param pre_warning_rule: The pre_warning_rule of this SlaRecord.
        :type pre_warning_rule: :class:`huaweicloudsdkcoc.v1.SlaPreWarningRuleInfo`
        """
        self._pre_warning_rule = pre_warning_rule

    @property
    def escalate_rule_enable(self):
        r"""Gets the escalate_rule_enable of this SlaRecord.

        SLA 上升通知是否开启

        :return: The escalate_rule_enable of this SlaRecord.
        :rtype: bool
        """
        return self._escalate_rule_enable

    @escalate_rule_enable.setter
    def escalate_rule_enable(self, escalate_rule_enable):
        r"""Sets the escalate_rule_enable of this SlaRecord.

        SLA 上升通知是否开启

        :param escalate_rule_enable: The escalate_rule_enable of this SlaRecord.
        :type escalate_rule_enable: bool
        """
        self._escalate_rule_enable = escalate_rule_enable

    @property
    def escalate_rules(self):
        r"""Gets the escalate_rules of this SlaRecord.

        SLA 上升通知配置

        :return: The escalate_rules of this SlaRecord.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.SlaEscalationRuleInfo`]
        """
        return self._escalate_rules

    @escalate_rules.setter
    def escalate_rules(self, escalate_rules):
        r"""Sets the escalate_rules of this SlaRecord.

        SLA 上升通知配置

        :param escalate_rules: The escalate_rules of this SlaRecord.
        :type escalate_rules: list[:class:`huaweicloudsdkcoc.v1.SlaEscalationRuleInfo`]
        """
        self._escalate_rules = escalate_rules

    @property
    def current_node(self):
        r"""Gets the current_node of this SlaRecord.

        SLA是否在当前状态

        :return: The current_node of this SlaRecord.
        :rtype: bool
        """
        return self._current_node

    @current_node.setter
    def current_node(self, current_node):
        r"""Sets the current_node of this SlaRecord.

        SLA是否在当前状态

        :param current_node: The current_node of this SlaRecord.
        :type current_node: bool
        """
        self._current_node = current_node

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
        if not isinstance(other, SlaRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
