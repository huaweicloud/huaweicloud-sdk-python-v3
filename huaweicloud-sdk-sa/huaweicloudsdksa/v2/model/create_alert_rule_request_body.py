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
        'accumulated_times': 'int',
        'custom_properties': 'dict(str, str)',
        'alert_type': 'dict(str, str)',
        'event_grouping': 'bool',
        'suspression': 'bool',
        'simulation': 'bool',
        'schedule': 'Schedule',
        'triggers': 'list[AlertRuleTrigger]'
    }

    attribute_map = {
        'pipe_id': 'pipe_id',
        'rule_name': 'rule_name',
        'description': 'description',
        'query': 'query',
        'query_type': 'query_type',
        'status': 'status',
        'severity': 'severity',
        'accumulated_times': 'accumulated_times',
        'custom_properties': 'custom_properties',
        'alert_type': 'alert_type',
        'event_grouping': 'event_grouping',
        'suspression': 'suspression',
        'simulation': 'simulation',
        'schedule': 'schedule',
        'triggers': 'triggers'
    }

    def __init__(self, pipe_id=None, rule_name=None, description=None, query=None, query_type=None, status=None, severity=None, accumulated_times=None, custom_properties=None, alert_type=None, event_grouping=None, suspression=None, simulation=None, schedule=None, triggers=None):
        r"""CreateAlertRuleRequestBody

        The model defined in huaweicloud sdk

        :param pipe_id: pipe_id
        :type pipe_id: str
        :param rule_name: rule_name
        :type rule_name: str
        :param description: description
        :type description: str
        :param query: query
        :type query: str
        :param query_type: query_type. SQL, CBSL.
        :type query_type: str
        :param status: status. ENABLED, DISABLED
        :type status: str
        :param severity: severity. TIPS, LOW, MEDIUM, HIGH, FATAL
        :type severity: str
        :param accumulated_times: accumulated_times
        :type accumulated_times: int
        :param custom_properties: custom_properties
        :type custom_properties: dict(str, str)
        :param alert_type: alert_type
        :type alert_type: dict(str, str)
        :param event_grouping: event_grouping
        :type event_grouping: bool
        :param suspression: suspression
        :type suspression: bool
        :param simulation: simulation
        :type simulation: bool
        :param schedule: 
        :type schedule: :class:`huaweicloudsdksa.v2.Schedule`
        :param triggers: triggers
        :type triggers: list[:class:`huaweicloudsdksa.v2.AlertRuleTrigger`]
        """
        
        

        self._pipe_id = None
        self._rule_name = None
        self._description = None
        self._query = None
        self._query_type = None
        self._status = None
        self._severity = None
        self._accumulated_times = None
        self._custom_properties = None
        self._alert_type = None
        self._event_grouping = None
        self._suspression = None
        self._simulation = None
        self._schedule = None
        self._triggers = None
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
        if accumulated_times is not None:
            self.accumulated_times = accumulated_times
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

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this CreateAlertRuleRequestBody.

        pipe_id

        :return: The pipe_id of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this CreateAlertRuleRequestBody.

        pipe_id

        :param pipe_id: The pipe_id of this CreateAlertRuleRequestBody.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this CreateAlertRuleRequestBody.

        rule_name

        :return: The rule_name of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this CreateAlertRuleRequestBody.

        rule_name

        :param rule_name: The rule_name of this CreateAlertRuleRequestBody.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def description(self):
        r"""Gets the description of this CreateAlertRuleRequestBody.

        description

        :return: The description of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAlertRuleRequestBody.

        description

        :param description: The description of this CreateAlertRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def query(self):
        r"""Gets the query of this CreateAlertRuleRequestBody.

        query

        :return: The query of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this CreateAlertRuleRequestBody.

        query

        :param query: The query of this CreateAlertRuleRequestBody.
        :type query: str
        """
        self._query = query

    @property
    def query_type(self):
        r"""Gets the query_type of this CreateAlertRuleRequestBody.

        query_type. SQL, CBSL.

        :return: The query_type of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this CreateAlertRuleRequestBody.

        query_type. SQL, CBSL.

        :param query_type: The query_type of this CreateAlertRuleRequestBody.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def status(self):
        r"""Gets the status of this CreateAlertRuleRequestBody.

        status. ENABLED, DISABLED

        :return: The status of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateAlertRuleRequestBody.

        status. ENABLED, DISABLED

        :param status: The status of this CreateAlertRuleRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def severity(self):
        r"""Gets the severity of this CreateAlertRuleRequestBody.

        severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :return: The severity of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this CreateAlertRuleRequestBody.

        severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :param severity: The severity of this CreateAlertRuleRequestBody.
        :type severity: str
        """
        self._severity = severity

    @property
    def accumulated_times(self):
        r"""Gets the accumulated_times of this CreateAlertRuleRequestBody.

        accumulated_times

        :return: The accumulated_times of this CreateAlertRuleRequestBody.
        :rtype: int
        """
        return self._accumulated_times

    @accumulated_times.setter
    def accumulated_times(self, accumulated_times):
        r"""Sets the accumulated_times of this CreateAlertRuleRequestBody.

        accumulated_times

        :param accumulated_times: The accumulated_times of this CreateAlertRuleRequestBody.
        :type accumulated_times: int
        """
        self._accumulated_times = accumulated_times

    @property
    def custom_properties(self):
        r"""Gets the custom_properties of this CreateAlertRuleRequestBody.

        custom_properties

        :return: The custom_properties of this CreateAlertRuleRequestBody.
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        r"""Sets the custom_properties of this CreateAlertRuleRequestBody.

        custom_properties

        :param custom_properties: The custom_properties of this CreateAlertRuleRequestBody.
        :type custom_properties: dict(str, str)
        """
        self._custom_properties = custom_properties

    @property
    def alert_type(self):
        r"""Gets the alert_type of this CreateAlertRuleRequestBody.

        alert_type

        :return: The alert_type of this CreateAlertRuleRequestBody.
        :rtype: dict(str, str)
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        r"""Sets the alert_type of this CreateAlertRuleRequestBody.

        alert_type

        :param alert_type: The alert_type of this CreateAlertRuleRequestBody.
        :type alert_type: dict(str, str)
        """
        self._alert_type = alert_type

    @property
    def event_grouping(self):
        r"""Gets the event_grouping of this CreateAlertRuleRequestBody.

        event_grouping

        :return: The event_grouping of this CreateAlertRuleRequestBody.
        :rtype: bool
        """
        return self._event_grouping

    @event_grouping.setter
    def event_grouping(self, event_grouping):
        r"""Sets the event_grouping of this CreateAlertRuleRequestBody.

        event_grouping

        :param event_grouping: The event_grouping of this CreateAlertRuleRequestBody.
        :type event_grouping: bool
        """
        self._event_grouping = event_grouping

    @property
    def suspression(self):
        r"""Gets the suspression of this CreateAlertRuleRequestBody.

        suspression

        :return: The suspression of this CreateAlertRuleRequestBody.
        :rtype: bool
        """
        return self._suspression

    @suspression.setter
    def suspression(self, suspression):
        r"""Sets the suspression of this CreateAlertRuleRequestBody.

        suspression

        :param suspression: The suspression of this CreateAlertRuleRequestBody.
        :type suspression: bool
        """
        self._suspression = suspression

    @property
    def simulation(self):
        r"""Gets the simulation of this CreateAlertRuleRequestBody.

        simulation

        :return: The simulation of this CreateAlertRuleRequestBody.
        :rtype: bool
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        r"""Sets the simulation of this CreateAlertRuleRequestBody.

        simulation

        :param simulation: The simulation of this CreateAlertRuleRequestBody.
        :type simulation: bool
        """
        self._simulation = simulation

    @property
    def schedule(self):
        r"""Gets the schedule of this CreateAlertRuleRequestBody.

        :return: The schedule of this CreateAlertRuleRequestBody.
        :rtype: :class:`huaweicloudsdksa.v2.Schedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this CreateAlertRuleRequestBody.

        :param schedule: The schedule of this CreateAlertRuleRequestBody.
        :type schedule: :class:`huaweicloudsdksa.v2.Schedule`
        """
        self._schedule = schedule

    @property
    def triggers(self):
        r"""Gets the triggers of this CreateAlertRuleRequestBody.

        triggers

        :return: The triggers of this CreateAlertRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdksa.v2.AlertRuleTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this CreateAlertRuleRequestBody.

        triggers

        :param triggers: The triggers of this CreateAlertRuleRequestBody.
        :type triggers: list[:class:`huaweicloudsdksa.v2.AlertRuleTrigger`]
        """
        self._triggers = triggers

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
