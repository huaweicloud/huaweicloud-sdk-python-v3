# coding: utf-8

import six

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
        'pipe_id': 'str',
        'rule_name': 'str',
        'description': 'str',
        'query': 'str',
        'query_type': 'str',
        'status': 'str',
        'severity': 'str',
        'custom_properties': 'dict(str, str)',
        'alert_type': 'dict(str, str)',
        'event_grouping': 'bool',
        'suspression': 'bool',
        'simulation': 'bool',
        'schedule': 'Schedule',
        'triggers': 'list[AlertRuleTrigger]',
        'pipe_name': 'str',
        'alert_name': 'str',
        'alert_description': 'str',
        'alert_remediation': 'str',
        'accumulated_times': 'int'
    }

    attribute_map = {
        'pipe_id': 'pipe_id',
        'rule_name': 'rule_name',
        'description': 'description',
        'query': 'query',
        'query_type': 'query_type',
        'status': 'status',
        'severity': 'severity',
        'custom_properties': 'custom_properties',
        'alert_type': 'alert_type',
        'event_grouping': 'event_grouping',
        'suspression': 'suspression',
        'simulation': 'simulation',
        'schedule': 'schedule',
        'triggers': 'triggers',
        'pipe_name': 'pipe_name',
        'alert_name': 'alert_name',
        'alert_description': 'alert_description',
        'alert_remediation': 'alert_remediation',
        'accumulated_times': 'accumulated_times'
    }

    def __init__(self, pipe_id=None, rule_name=None, description=None, query=None, query_type=None, status=None, severity=None, custom_properties=None, alert_type=None, event_grouping=None, suspression=None, simulation=None, schedule=None, triggers=None, pipe_name=None, alert_name=None, alert_description=None, alert_remediation=None, accumulated_times=None):
        r"""CreateAlertRuleRequestBody

        The model defined in huaweicloud sdk

        :param pipe_id: 数据管道 ID。Pipe ID.
        :type pipe_id: str
        :param rule_name: 告警规则名称。Alert rule name.
        :type rule_name: str
        :param description: 描述。Description.
        :type description: str
        :param query: 查询语句。Query.
        :type query: str
        :param query_type: 查询语法，SQL。Query type. SQL.
        :type query_type: str
        :param status: 启用状态，启用、停用。Status, enabled, disabled.
        :type status: str
        :param severity: 严重程度，提示、低危、中危、高危、致命。Severity. TIPS, LOW, MEDIUM, HIGH, FATAL
        :type severity: str
        :param custom_properties: 自定义扩展信息。Custom properties.
        :type custom_properties: dict(str, str)
        :param alert_type: 告警类型。Alert type.
        :type alert_type: dict(str, str)
        :param event_grouping: 告警分组。Event grouping.
        :type event_grouping: bool
        :param suspression: 告警抑制。Suspression.
        :type suspression: bool
        :param simulation: 模拟告警。Simulation.
        :type simulation: bool
        :param schedule: 
        :type schedule: :class:`huaweicloudsdksecmaster.v2.Schedule`
        :param triggers: 告警触发规则。Alert triggers.
        :type triggers: list[:class:`huaweicloudsdksecmaster.v2.AlertRuleTrigger`]
        :param pipe_name: 管道名称
        :type pipe_name: str
        :param alert_name: 告警名称
        :type alert_name: str
        :param alert_description: 告警描述
        :type alert_description: str
        :param alert_remediation: 修复建议
        :type alert_remediation: str
        :param accumulated_times: 执行次数
        :type accumulated_times: int
        """
        
        

        self._pipe_id = None
        self._rule_name = None
        self._description = None
        self._query = None
        self._query_type = None
        self._status = None
        self._severity = None
        self._custom_properties = None
        self._alert_type = None
        self._event_grouping = None
        self._suspression = None
        self._simulation = None
        self._schedule = None
        self._triggers = None
        self._pipe_name = None
        self._alert_name = None
        self._alert_description = None
        self._alert_remediation = None
        self._accumulated_times = None
        self.discriminator = None

        self.pipe_id = pipe_id
        self.rule_name = rule_name
        if description is not None:
            self.description = description
        self.query = query
        if query_type is not None:
            self.query_type = query_type
        if status is not None:
            self.status = status
        if severity is not None:
            self.severity = severity
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if alert_type is not None:
            self.alert_type = alert_type
        if event_grouping is not None:
            self.event_grouping = event_grouping
        if suspression is not None:
            self.suspression = suspression
        if simulation is not None:
            self.simulation = simulation
        self.schedule = schedule
        self.triggers = triggers
        self.pipe_name = pipe_name
        self.alert_name = alert_name
        if alert_description is not None:
            self.alert_description = alert_description
        if alert_remediation is not None:
            self.alert_remediation = alert_remediation
        if accumulated_times is not None:
            self.accumulated_times = accumulated_times

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this CreateAlertRuleRequestBody.

        数据管道 ID。Pipe ID.

        :return: The pipe_id of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this CreateAlertRuleRequestBody.

        数据管道 ID。Pipe ID.

        :param pipe_id: The pipe_id of this CreateAlertRuleRequestBody.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this CreateAlertRuleRequestBody.

        告警规则名称。Alert rule name.

        :return: The rule_name of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this CreateAlertRuleRequestBody.

        告警规则名称。Alert rule name.

        :param rule_name: The rule_name of this CreateAlertRuleRequestBody.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def description(self):
        r"""Gets the description of this CreateAlertRuleRequestBody.

        描述。Description.

        :return: The description of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAlertRuleRequestBody.

        描述。Description.

        :param description: The description of this CreateAlertRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def query(self):
        r"""Gets the query of this CreateAlertRuleRequestBody.

        查询语句。Query.

        :return: The query of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this CreateAlertRuleRequestBody.

        查询语句。Query.

        :param query: The query of this CreateAlertRuleRequestBody.
        :type query: str
        """
        self._query = query

    @property
    def query_type(self):
        r"""Gets the query_type of this CreateAlertRuleRequestBody.

        查询语法，SQL。Query type. SQL.

        :return: The query_type of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this CreateAlertRuleRequestBody.

        查询语法，SQL。Query type. SQL.

        :param query_type: The query_type of this CreateAlertRuleRequestBody.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def status(self):
        r"""Gets the status of this CreateAlertRuleRequestBody.

        启用状态，启用、停用。Status, enabled, disabled.

        :return: The status of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateAlertRuleRequestBody.

        启用状态，启用、停用。Status, enabled, disabled.

        :param status: The status of this CreateAlertRuleRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def severity(self):
        r"""Gets the severity of this CreateAlertRuleRequestBody.

        严重程度，提示、低危、中危、高危、致命。Severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :return: The severity of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this CreateAlertRuleRequestBody.

        严重程度，提示、低危、中危、高危、致命。Severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :param severity: The severity of this CreateAlertRuleRequestBody.
        :type severity: str
        """
        self._severity = severity

    @property
    def custom_properties(self):
        r"""Gets the custom_properties of this CreateAlertRuleRequestBody.

        自定义扩展信息。Custom properties.

        :return: The custom_properties of this CreateAlertRuleRequestBody.
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        r"""Sets the custom_properties of this CreateAlertRuleRequestBody.

        自定义扩展信息。Custom properties.

        :param custom_properties: The custom_properties of this CreateAlertRuleRequestBody.
        :type custom_properties: dict(str, str)
        """
        self._custom_properties = custom_properties

    @property
    def alert_type(self):
        r"""Gets the alert_type of this CreateAlertRuleRequestBody.

        告警类型。Alert type.

        :return: The alert_type of this CreateAlertRuleRequestBody.
        :rtype: dict(str, str)
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        r"""Sets the alert_type of this CreateAlertRuleRequestBody.

        告警类型。Alert type.

        :param alert_type: The alert_type of this CreateAlertRuleRequestBody.
        :type alert_type: dict(str, str)
        """
        self._alert_type = alert_type

    @property
    def event_grouping(self):
        r"""Gets the event_grouping of this CreateAlertRuleRequestBody.

        告警分组。Event grouping.

        :return: The event_grouping of this CreateAlertRuleRequestBody.
        :rtype: bool
        """
        return self._event_grouping

    @event_grouping.setter
    def event_grouping(self, event_grouping):
        r"""Sets the event_grouping of this CreateAlertRuleRequestBody.

        告警分组。Event grouping.

        :param event_grouping: The event_grouping of this CreateAlertRuleRequestBody.
        :type event_grouping: bool
        """
        self._event_grouping = event_grouping

    @property
    def suspression(self):
        r"""Gets the suspression of this CreateAlertRuleRequestBody.

        告警抑制。Suspression.

        :return: The suspression of this CreateAlertRuleRequestBody.
        :rtype: bool
        """
        return self._suspression

    @suspression.setter
    def suspression(self, suspression):
        r"""Sets the suspression of this CreateAlertRuleRequestBody.

        告警抑制。Suspression.

        :param suspression: The suspression of this CreateAlertRuleRequestBody.
        :type suspression: bool
        """
        self._suspression = suspression

    @property
    def simulation(self):
        r"""Gets the simulation of this CreateAlertRuleRequestBody.

        模拟告警。Simulation.

        :return: The simulation of this CreateAlertRuleRequestBody.
        :rtype: bool
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        r"""Sets the simulation of this CreateAlertRuleRequestBody.

        模拟告警。Simulation.

        :param simulation: The simulation of this CreateAlertRuleRequestBody.
        :type simulation: bool
        """
        self._simulation = simulation

    @property
    def schedule(self):
        r"""Gets the schedule of this CreateAlertRuleRequestBody.

        :return: The schedule of this CreateAlertRuleRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.Schedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this CreateAlertRuleRequestBody.

        :param schedule: The schedule of this CreateAlertRuleRequestBody.
        :type schedule: :class:`huaweicloudsdksecmaster.v2.Schedule`
        """
        self._schedule = schedule

    @property
    def triggers(self):
        r"""Gets the triggers of this CreateAlertRuleRequestBody.

        告警触发规则。Alert triggers.

        :return: The triggers of this CreateAlertRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.AlertRuleTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this CreateAlertRuleRequestBody.

        告警触发规则。Alert triggers.

        :param triggers: The triggers of this CreateAlertRuleRequestBody.
        :type triggers: list[:class:`huaweicloudsdksecmaster.v2.AlertRuleTrigger`]
        """
        self._triggers = triggers

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
        if not isinstance(other, CreateAlertRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
