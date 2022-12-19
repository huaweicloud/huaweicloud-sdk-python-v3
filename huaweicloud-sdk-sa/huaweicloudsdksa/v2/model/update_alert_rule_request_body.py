# coding: utf-8

import re
import six



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
        'suppression': 'bool',
        'simulation': 'bool',
        'schedule': 'Schedule',
        'triggers': 'list[AlertRuleTrigger]'
    }

    attribute_map = {
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
        'suppression': 'suppression',
        'simulation': 'simulation',
        'schedule': 'schedule',
        'triggers': 'triggers'
    }

    def __init__(self, rule_name=None, description=None, query=None, query_type=None, status=None, severity=None, accumulated_times=None, custom_properties=None, alert_type=None, event_grouping=None, suppression=None, simulation=None, schedule=None, triggers=None):
        """UpdateAlertRuleRequestBody

        The model defined in huaweicloud sdk

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
        :param suppression: suppression
        :type suppression: bool
        :param simulation: simulation
        :type simulation: bool
        :param schedule: 
        :type schedule: :class:`huaweicloudsdksa.v2.Schedule`
        :param triggers: triggers
        :type triggers: list[:class:`huaweicloudsdksa.v2.AlertRuleTrigger`]
        """
        
        

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
        self._suppression = None
        self._simulation = None
        self._schedule = None
        self._triggers = None
        self.discriminator = None

        if rule_name is not None:
            self.rule_name = rule_name
        if description is not None:
            self.description = description
        if query is not None:
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
        if suppression is not None:
            self.suppression = suppression
        if simulation is not None:
            self.simulation = simulation
        if schedule is not None:
            self.schedule = schedule
        if triggers is not None:
            self.triggers = triggers

    @property
    def rule_name(self):
        """Gets the rule_name of this UpdateAlertRuleRequestBody.

        rule_name

        :return: The rule_name of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this UpdateAlertRuleRequestBody.

        rule_name

        :param rule_name: The rule_name of this UpdateAlertRuleRequestBody.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def description(self):
        """Gets the description of this UpdateAlertRuleRequestBody.

        description

        :return: The description of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateAlertRuleRequestBody.

        description

        :param description: The description of this UpdateAlertRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def query(self):
        """Gets the query of this UpdateAlertRuleRequestBody.

        query

        :return: The query of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this UpdateAlertRuleRequestBody.

        query

        :param query: The query of this UpdateAlertRuleRequestBody.
        :type query: str
        """
        self._query = query

    @property
    def query_type(self):
        """Gets the query_type of this UpdateAlertRuleRequestBody.

        query_type. SQL, CBSL.

        :return: The query_type of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this UpdateAlertRuleRequestBody.

        query_type. SQL, CBSL.

        :param query_type: The query_type of this UpdateAlertRuleRequestBody.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def status(self):
        """Gets the status of this UpdateAlertRuleRequestBody.

        status. ENABLED, DISABLED

        :return: The status of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateAlertRuleRequestBody.

        status. ENABLED, DISABLED

        :param status: The status of this UpdateAlertRuleRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def severity(self):
        """Gets the severity of this UpdateAlertRuleRequestBody.

        severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :return: The severity of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this UpdateAlertRuleRequestBody.

        severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :param severity: The severity of this UpdateAlertRuleRequestBody.
        :type severity: str
        """
        self._severity = severity

    @property
    def accumulated_times(self):
        """Gets the accumulated_times of this UpdateAlertRuleRequestBody.

        accumulated_times

        :return: The accumulated_times of this UpdateAlertRuleRequestBody.
        :rtype: int
        """
        return self._accumulated_times

    @accumulated_times.setter
    def accumulated_times(self, accumulated_times):
        """Sets the accumulated_times of this UpdateAlertRuleRequestBody.

        accumulated_times

        :param accumulated_times: The accumulated_times of this UpdateAlertRuleRequestBody.
        :type accumulated_times: int
        """
        self._accumulated_times = accumulated_times

    @property
    def custom_properties(self):
        """Gets the custom_properties of this UpdateAlertRuleRequestBody.

        custom_properties

        :return: The custom_properties of this UpdateAlertRuleRequestBody.
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this UpdateAlertRuleRequestBody.

        custom_properties

        :param custom_properties: The custom_properties of this UpdateAlertRuleRequestBody.
        :type custom_properties: dict(str, str)
        """
        self._custom_properties = custom_properties

    @property
    def alert_type(self):
        """Gets the alert_type of this UpdateAlertRuleRequestBody.

        alert_type

        :return: The alert_type of this UpdateAlertRuleRequestBody.
        :rtype: dict(str, str)
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this UpdateAlertRuleRequestBody.

        alert_type

        :param alert_type: The alert_type of this UpdateAlertRuleRequestBody.
        :type alert_type: dict(str, str)
        """
        self._alert_type = alert_type

    @property
    def event_grouping(self):
        """Gets the event_grouping of this UpdateAlertRuleRequestBody.

        event_grouping

        :return: The event_grouping of this UpdateAlertRuleRequestBody.
        :rtype: bool
        """
        return self._event_grouping

    @event_grouping.setter
    def event_grouping(self, event_grouping):
        """Sets the event_grouping of this UpdateAlertRuleRequestBody.

        event_grouping

        :param event_grouping: The event_grouping of this UpdateAlertRuleRequestBody.
        :type event_grouping: bool
        """
        self._event_grouping = event_grouping

    @property
    def suppression(self):
        """Gets the suppression of this UpdateAlertRuleRequestBody.

        suppression

        :return: The suppression of this UpdateAlertRuleRequestBody.
        :rtype: bool
        """
        return self._suppression

    @suppression.setter
    def suppression(self, suppression):
        """Sets the suppression of this UpdateAlertRuleRequestBody.

        suppression

        :param suppression: The suppression of this UpdateAlertRuleRequestBody.
        :type suppression: bool
        """
        self._suppression = suppression

    @property
    def simulation(self):
        """Gets the simulation of this UpdateAlertRuleRequestBody.

        simulation

        :return: The simulation of this UpdateAlertRuleRequestBody.
        :rtype: bool
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this UpdateAlertRuleRequestBody.

        simulation

        :param simulation: The simulation of this UpdateAlertRuleRequestBody.
        :type simulation: bool
        """
        self._simulation = simulation

    @property
    def schedule(self):
        """Gets the schedule of this UpdateAlertRuleRequestBody.

        :return: The schedule of this UpdateAlertRuleRequestBody.
        :rtype: :class:`huaweicloudsdksa.v2.Schedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this UpdateAlertRuleRequestBody.

        :param schedule: The schedule of this UpdateAlertRuleRequestBody.
        :type schedule: :class:`huaweicloudsdksa.v2.Schedule`
        """
        self._schedule = schedule

    @property
    def triggers(self):
        """Gets the triggers of this UpdateAlertRuleRequestBody.

        triggers

        :return: The triggers of this UpdateAlertRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdksa.v2.AlertRuleTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this UpdateAlertRuleRequestBody.

        triggers

        :param triggers: The triggers of this UpdateAlertRuleRequestBody.
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
        if not isinstance(other, UpdateAlertRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
