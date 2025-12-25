# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAlertRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_type': 'dict(str, str)',
        'custom_properties': 'dict(str, str)',
        'description': 'str',
        'event_grouping': 'bool',
        'query': 'str',
        'query_type': 'str',
        'rule_name': 'str',
        'schedule': 'Schedule',
        'severity': 'str',
        'simulation': 'bool',
        'status': 'str',
        'suppression': 'bool',
        'triggers': 'list[AlertRuleTrigger]'
    }

    attribute_map = {
        'alert_type': 'alert_type',
        'custom_properties': 'custom_properties',
        'description': 'description',
        'event_grouping': 'event_grouping',
        'query': 'query',
        'query_type': 'query_type',
        'rule_name': 'rule_name',
        'schedule': 'schedule',
        'severity': 'severity',
        'simulation': 'simulation',
        'status': 'status',
        'suppression': 'suppression',
        'triggers': 'triggers'
    }

    def __init__(self, alert_type=None, custom_properties=None, description=None, event_grouping=None, query=None, query_type=None, rule_name=None, schedule=None, severity=None, simulation=None, status=None, suppression=None, triggers=None):
        r"""UpdateAlertRuleRequestBody

        The model defined in huaweicloud sdk

        :param alert_type: 告警类型，通过“查询数据类列表” 接口获取
        :type alert_type: dict(str, str)
        :param custom_properties: 自定义扩展信息
        :type custom_properties: dict(str, str)
        :param description: 描述
        :type description: str
        :param event_grouping: 告警分组
        :type event_grouping: bool
        :param query: 查询语句
        :type query: str
        :param query_type: **参数解释**: 查询语法类型 - SQL查询 **约束限制**: 不涉及  **取值范围**: - SQL **默认值**:  SQL
        :type query_type: str
        :param rule_name: 告警规则名称
        :type rule_name: str
        :param schedule: 
        :type schedule: :class:`huaweicloudsdksecmaster.v1.Schedule`
        :param severity: **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及
        :type severity: str
        :param simulation: 模拟告警
        :type simulation: bool
        :param status: **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及
        :type status: str
        :param suppression: 告警抑制
        :type suppression: bool
        :param triggers: 告警触发规则
        :type triggers: list[:class:`huaweicloudsdksecmaster.v1.AlertRuleTrigger`]
        """
        
        

        self._alert_type = None
        self._custom_properties = None
        self._description = None
        self._event_grouping = None
        self._query = None
        self._query_type = None
        self._rule_name = None
        self._schedule = None
        self._severity = None
        self._simulation = None
        self._status = None
        self._suppression = None
        self._triggers = None
        self.discriminator = None

        if alert_type is not None:
            self.alert_type = alert_type
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if description is not None:
            self.description = description
        if event_grouping is not None:
            self.event_grouping = event_grouping
        if query is not None:
            self.query = query
        if query_type is not None:
            self.query_type = query_type
        if rule_name is not None:
            self.rule_name = rule_name
        if schedule is not None:
            self.schedule = schedule
        if severity is not None:
            self.severity = severity
        if simulation is not None:
            self.simulation = simulation
        if status is not None:
            self.status = status
        if suppression is not None:
            self.suppression = suppression
        if triggers is not None:
            self.triggers = triggers

    @property
    def alert_type(self):
        r"""Gets the alert_type of this UpdateAlertRuleRequestBody.

        告警类型，通过“查询数据类列表” 接口获取

        :return: The alert_type of this UpdateAlertRuleRequestBody.
        :rtype: dict(str, str)
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        r"""Sets the alert_type of this UpdateAlertRuleRequestBody.

        告警类型，通过“查询数据类列表” 接口获取

        :param alert_type: The alert_type of this UpdateAlertRuleRequestBody.
        :type alert_type: dict(str, str)
        """
        self._alert_type = alert_type

    @property
    def custom_properties(self):
        r"""Gets the custom_properties of this UpdateAlertRuleRequestBody.

        自定义扩展信息

        :return: The custom_properties of this UpdateAlertRuleRequestBody.
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        r"""Sets the custom_properties of this UpdateAlertRuleRequestBody.

        自定义扩展信息

        :param custom_properties: The custom_properties of this UpdateAlertRuleRequestBody.
        :type custom_properties: dict(str, str)
        """
        self._custom_properties = custom_properties

    @property
    def description(self):
        r"""Gets the description of this UpdateAlertRuleRequestBody.

        描述

        :return: The description of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateAlertRuleRequestBody.

        描述

        :param description: The description of this UpdateAlertRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def event_grouping(self):
        r"""Gets the event_grouping of this UpdateAlertRuleRequestBody.

        告警分组

        :return: The event_grouping of this UpdateAlertRuleRequestBody.
        :rtype: bool
        """
        return self._event_grouping

    @event_grouping.setter
    def event_grouping(self, event_grouping):
        r"""Sets the event_grouping of this UpdateAlertRuleRequestBody.

        告警分组

        :param event_grouping: The event_grouping of this UpdateAlertRuleRequestBody.
        :type event_grouping: bool
        """
        self._event_grouping = event_grouping

    @property
    def query(self):
        r"""Gets the query of this UpdateAlertRuleRequestBody.

        查询语句

        :return: The query of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this UpdateAlertRuleRequestBody.

        查询语句

        :param query: The query of this UpdateAlertRuleRequestBody.
        :type query: str
        """
        self._query = query

    @property
    def query_type(self):
        r"""Gets the query_type of this UpdateAlertRuleRequestBody.

        **参数解释**: 查询语法类型 - SQL查询 **约束限制**: 不涉及  **取值范围**: - SQL **默认值**:  SQL

        :return: The query_type of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this UpdateAlertRuleRequestBody.

        **参数解释**: 查询语法类型 - SQL查询 **约束限制**: 不涉及  **取值范围**: - SQL **默认值**:  SQL

        :param query_type: The query_type of this UpdateAlertRuleRequestBody.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def rule_name(self):
        r"""Gets the rule_name of this UpdateAlertRuleRequestBody.

        告警规则名称

        :return: The rule_name of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this UpdateAlertRuleRequestBody.

        告警规则名称

        :param rule_name: The rule_name of this UpdateAlertRuleRequestBody.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def schedule(self):
        r"""Gets the schedule of this UpdateAlertRuleRequestBody.

        :return: The schedule of this UpdateAlertRuleRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Schedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this UpdateAlertRuleRequestBody.

        :param schedule: The schedule of this UpdateAlertRuleRequestBody.
        :type schedule: :class:`huaweicloudsdksecmaster.v1.Schedule`
        """
        self._schedule = schedule

    @property
    def severity(self):
        r"""Gets the severity of this UpdateAlertRuleRequestBody.

        **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及

        :return: The severity of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this UpdateAlertRuleRequestBody.

        **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及

        :param severity: The severity of this UpdateAlertRuleRequestBody.
        :type severity: str
        """
        self._severity = severity

    @property
    def simulation(self):
        r"""Gets the simulation of this UpdateAlertRuleRequestBody.

        模拟告警

        :return: The simulation of this UpdateAlertRuleRequestBody.
        :rtype: bool
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        r"""Sets the simulation of this UpdateAlertRuleRequestBody.

        模拟告警

        :param simulation: The simulation of this UpdateAlertRuleRequestBody.
        :type simulation: bool
        """
        self._simulation = simulation

    @property
    def status(self):
        r"""Gets the status of this UpdateAlertRuleRequestBody.

        **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及

        :return: The status of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateAlertRuleRequestBody.

        **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及

        :param status: The status of this UpdateAlertRuleRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def suppression(self):
        r"""Gets the suppression of this UpdateAlertRuleRequestBody.

        告警抑制

        :return: The suppression of this UpdateAlertRuleRequestBody.
        :rtype: bool
        """
        return self._suppression

    @suppression.setter
    def suppression(self, suppression):
        r"""Sets the suppression of this UpdateAlertRuleRequestBody.

        告警抑制

        :param suppression: The suppression of this UpdateAlertRuleRequestBody.
        :type suppression: bool
        """
        self._suppression = suppression

    @property
    def triggers(self):
        r"""Gets the triggers of this UpdateAlertRuleRequestBody.

        告警触发规则

        :return: The triggers of this UpdateAlertRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.AlertRuleTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this UpdateAlertRuleRequestBody.

        告警触发规则

        :param triggers: The triggers of this UpdateAlertRuleRequestBody.
        :type triggers: list[:class:`huaweicloudsdksecmaster.v1.AlertRuleTrigger`]
        """
        self._triggers = triggers

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
        if not isinstance(other, UpdateAlertRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
