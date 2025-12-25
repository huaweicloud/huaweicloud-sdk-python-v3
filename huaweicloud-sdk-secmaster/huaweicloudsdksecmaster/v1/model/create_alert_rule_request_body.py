# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAlertRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'accumulated_times': 'int',
        'alert_description': 'str',
        'alert_name': 'str',
        'alert_remediation': 'str',
        'alert_type': 'dict(str, str)',
        'custom_properties': 'dict(str, str)',
        'description': 'str',
        'event_grouping': 'bool',
        'pipe_id': 'str',
        'pipe_name': 'str',
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
        'accumulated_times': 'accumulated_times',
        'alert_description': 'alert_description',
        'alert_name': 'alert_name',
        'alert_remediation': 'alert_remediation',
        'alert_type': 'alert_type',
        'custom_properties': 'custom_properties',
        'description': 'description',
        'event_grouping': 'event_grouping',
        'pipe_id': 'pipe_id',
        'pipe_name': 'pipe_name',
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

    def __init__(self, accumulated_times=None, alert_description=None, alert_name=None, alert_remediation=None, alert_type=None, custom_properties=None, description=None, event_grouping=None, pipe_id=None, pipe_name=None, query=None, query_type=None, rule_name=None, schedule=None, severity=None, simulation=None, status=None, suppression=None, triggers=None):
        r"""CreateAlertRuleRequestBody

        The model defined in huaweicloud sdk

        :param accumulated_times: 执行次数
        :type accumulated_times: int
        :param alert_description: 告警描述
        :type alert_description: str
        :param alert_name: 告警名称
        :type alert_name: str
        :param alert_remediation: 修复建议
        :type alert_remediation: str
        :param alert_type: 告警类型，通过“查询数据类列表” 接口获取.
        :type alert_type: dict(str, str)
        :param custom_properties: 自定义扩展信息
        :type custom_properties: dict(str, str)
        :param description: 描述
        :type description: str
        :param event_grouping: 告警分组
        :type event_grouping: bool
        :param pipe_id: 数据管道 ID
        :type pipe_id: str
        :param pipe_name: 管道名称
        :type pipe_name: str
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
        
        

        self._accumulated_times = None
        self._alert_description = None
        self._alert_name = None
        self._alert_remediation = None
        self._alert_type = None
        self._custom_properties = None
        self._description = None
        self._event_grouping = None
        self._pipe_id = None
        self._pipe_name = None
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

        if accumulated_times is not None:
            self.accumulated_times = accumulated_times
        if alert_description is not None:
            self.alert_description = alert_description
        self.alert_name = alert_name
        if alert_remediation is not None:
            self.alert_remediation = alert_remediation
        if alert_type is not None:
            self.alert_type = alert_type
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if description is not None:
            self.description = description
        if event_grouping is not None:
            self.event_grouping = event_grouping
        self.pipe_id = pipe_id
        self.pipe_name = pipe_name
        self.query = query
        if query_type is not None:
            self.query_type = query_type
        self.rule_name = rule_name
        self.schedule = schedule
        if severity is not None:
            self.severity = severity
        if simulation is not None:
            self.simulation = simulation
        if status is not None:
            self.status = status
        if suppression is not None:
            self.suppression = suppression
        self.triggers = triggers

    @property
    def accumulated_times(self):
        r"""Gets the accumulated_times of this CreateAlertRuleRequestBody.

        执行次数

        :return: The accumulated_times of this CreateAlertRuleRequestBody.
        :rtype: int
        """
        return self._accumulated_times

    @accumulated_times.setter
    def accumulated_times(self, accumulated_times):
        r"""Sets the accumulated_times of this CreateAlertRuleRequestBody.

        执行次数

        :param accumulated_times: The accumulated_times of this CreateAlertRuleRequestBody.
        :type accumulated_times: int
        """
        self._accumulated_times = accumulated_times

    @property
    def alert_description(self):
        r"""Gets the alert_description of this CreateAlertRuleRequestBody.

        告警描述

        :return: The alert_description of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._alert_description

    @alert_description.setter
    def alert_description(self, alert_description):
        r"""Sets the alert_description of this CreateAlertRuleRequestBody.

        告警描述

        :param alert_description: The alert_description of this CreateAlertRuleRequestBody.
        :type alert_description: str
        """
        self._alert_description = alert_description

    @property
    def alert_name(self):
        r"""Gets the alert_name of this CreateAlertRuleRequestBody.

        告警名称

        :return: The alert_name of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._alert_name

    @alert_name.setter
    def alert_name(self, alert_name):
        r"""Sets the alert_name of this CreateAlertRuleRequestBody.

        告警名称

        :param alert_name: The alert_name of this CreateAlertRuleRequestBody.
        :type alert_name: str
        """
        self._alert_name = alert_name

    @property
    def alert_remediation(self):
        r"""Gets the alert_remediation of this CreateAlertRuleRequestBody.

        修复建议

        :return: The alert_remediation of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._alert_remediation

    @alert_remediation.setter
    def alert_remediation(self, alert_remediation):
        r"""Sets the alert_remediation of this CreateAlertRuleRequestBody.

        修复建议

        :param alert_remediation: The alert_remediation of this CreateAlertRuleRequestBody.
        :type alert_remediation: str
        """
        self._alert_remediation = alert_remediation

    @property
    def alert_type(self):
        r"""Gets the alert_type of this CreateAlertRuleRequestBody.

        告警类型，通过“查询数据类列表” 接口获取.

        :return: The alert_type of this CreateAlertRuleRequestBody.
        :rtype: dict(str, str)
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        r"""Sets the alert_type of this CreateAlertRuleRequestBody.

        告警类型，通过“查询数据类列表” 接口获取.

        :param alert_type: The alert_type of this CreateAlertRuleRequestBody.
        :type alert_type: dict(str, str)
        """
        self._alert_type = alert_type

    @property
    def custom_properties(self):
        r"""Gets the custom_properties of this CreateAlertRuleRequestBody.

        自定义扩展信息

        :return: The custom_properties of this CreateAlertRuleRequestBody.
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        r"""Sets the custom_properties of this CreateAlertRuleRequestBody.

        自定义扩展信息

        :param custom_properties: The custom_properties of this CreateAlertRuleRequestBody.
        :type custom_properties: dict(str, str)
        """
        self._custom_properties = custom_properties

    @property
    def description(self):
        r"""Gets the description of this CreateAlertRuleRequestBody.

        描述

        :return: The description of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAlertRuleRequestBody.

        描述

        :param description: The description of this CreateAlertRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def event_grouping(self):
        r"""Gets the event_grouping of this CreateAlertRuleRequestBody.

        告警分组

        :return: The event_grouping of this CreateAlertRuleRequestBody.
        :rtype: bool
        """
        return self._event_grouping

    @event_grouping.setter
    def event_grouping(self, event_grouping):
        r"""Sets the event_grouping of this CreateAlertRuleRequestBody.

        告警分组

        :param event_grouping: The event_grouping of this CreateAlertRuleRequestBody.
        :type event_grouping: bool
        """
        self._event_grouping = event_grouping

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this CreateAlertRuleRequestBody.

        数据管道 ID

        :return: The pipe_id of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this CreateAlertRuleRequestBody.

        数据管道 ID

        :param pipe_id: The pipe_id of this CreateAlertRuleRequestBody.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def pipe_name(self):
        r"""Gets the pipe_name of this CreateAlertRuleRequestBody.

        管道名称

        :return: The pipe_name of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._pipe_name

    @pipe_name.setter
    def pipe_name(self, pipe_name):
        r"""Sets the pipe_name of this CreateAlertRuleRequestBody.

        管道名称

        :param pipe_name: The pipe_name of this CreateAlertRuleRequestBody.
        :type pipe_name: str
        """
        self._pipe_name = pipe_name

    @property
    def query(self):
        r"""Gets the query of this CreateAlertRuleRequestBody.

        查询语句

        :return: The query of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this CreateAlertRuleRequestBody.

        查询语句

        :param query: The query of this CreateAlertRuleRequestBody.
        :type query: str
        """
        self._query = query

    @property
    def query_type(self):
        r"""Gets the query_type of this CreateAlertRuleRequestBody.

        **参数解释**: 查询语法类型 - SQL查询 **约束限制**: 不涉及  **取值范围**: - SQL **默认值**:  SQL

        :return: The query_type of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this CreateAlertRuleRequestBody.

        **参数解释**: 查询语法类型 - SQL查询 **约束限制**: 不涉及  **取值范围**: - SQL **默认值**:  SQL

        :param query_type: The query_type of this CreateAlertRuleRequestBody.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def rule_name(self):
        r"""Gets the rule_name of this CreateAlertRuleRequestBody.

        告警规则名称

        :return: The rule_name of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this CreateAlertRuleRequestBody.

        告警规则名称

        :param rule_name: The rule_name of this CreateAlertRuleRequestBody.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def schedule(self):
        r"""Gets the schedule of this CreateAlertRuleRequestBody.

        :return: The schedule of this CreateAlertRuleRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Schedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this CreateAlertRuleRequestBody.

        :param schedule: The schedule of this CreateAlertRuleRequestBody.
        :type schedule: :class:`huaweicloudsdksecmaster.v1.Schedule`
        """
        self._schedule = schedule

    @property
    def severity(self):
        r"""Gets the severity of this CreateAlertRuleRequestBody.

        **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及

        :return: The severity of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this CreateAlertRuleRequestBody.

        **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及

        :param severity: The severity of this CreateAlertRuleRequestBody.
        :type severity: str
        """
        self._severity = severity

    @property
    def simulation(self):
        r"""Gets the simulation of this CreateAlertRuleRequestBody.

        模拟告警

        :return: The simulation of this CreateAlertRuleRequestBody.
        :rtype: bool
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        r"""Sets the simulation of this CreateAlertRuleRequestBody.

        模拟告警

        :param simulation: The simulation of this CreateAlertRuleRequestBody.
        :type simulation: bool
        """
        self._simulation = simulation

    @property
    def status(self):
        r"""Gets the status of this CreateAlertRuleRequestBody.

        **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及

        :return: The status of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateAlertRuleRequestBody.

        **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及

        :param status: The status of this CreateAlertRuleRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def suppression(self):
        r"""Gets the suppression of this CreateAlertRuleRequestBody.

        告警抑制

        :return: The suppression of this CreateAlertRuleRequestBody.
        :rtype: bool
        """
        return self._suppression

    @suppression.setter
    def suppression(self, suppression):
        r"""Sets the suppression of this CreateAlertRuleRequestBody.

        告警抑制

        :param suppression: The suppression of this CreateAlertRuleRequestBody.
        :type suppression: bool
        """
        self._suppression = suppression

    @property
    def triggers(self):
        r"""Gets the triggers of this CreateAlertRuleRequestBody.

        告警触发规则

        :return: The triggers of this CreateAlertRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.AlertRuleTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this CreateAlertRuleRequestBody.

        告警触发规则

        :param triggers: The triggers of this CreateAlertRuleRequestBody.
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
        if not isinstance(other, CreateAlertRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
