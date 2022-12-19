# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAlertRuleResponse(SdkResponse):

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
        'pipe_id': 'str',
        'pipe_name': 'str',
        'create_by': 'str',
        'create_time': 'int',
        'update_by': 'str',
        'update_time': 'int',
        'delete_time': 'int',
        'rule_name': 'str',
        'query': 'str',
        'query_type': 'str',
        'status': 'str',
        'severity': 'str',
        'accumulated_times': 'int',
        'custom_properties': 'dict(str, str)',
        'event_grouping': 'bool',
        'schedule': 'Schedule',
        'triggers': 'list[AlertRuleTrigger]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'pipe_id': 'pipe_id',
        'pipe_name': 'pipe_name',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'update_by': 'update_by',
        'update_time': 'update_time',
        'delete_time': 'delete_time',
        'rule_name': 'rule_name',
        'query': 'query',
        'query_type': 'query_type',
        'status': 'status',
        'severity': 'severity',
        'accumulated_times': 'accumulated_times',
        'custom_properties': 'custom_properties',
        'event_grouping': 'event_grouping',
        'schedule': 'schedule',
        'triggers': 'triggers',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, rule_id=None, pipe_id=None, pipe_name=None, create_by=None, create_time=None, update_by=None, update_time=None, delete_time=None, rule_name=None, query=None, query_type=None, status=None, severity=None, accumulated_times=None, custom_properties=None, event_grouping=None, schedule=None, triggers=None, x_request_id=None):
        """CreateAlertRuleResponse

        The model defined in huaweicloud sdk

        :param rule_id: rule_id
        :type rule_id: str
        :param pipe_id: pipe_id
        :type pipe_id: str
        :param pipe_name: pipe_name
        :type pipe_name: str
        :param create_by: create_by
        :type create_by: str
        :param create_time: create_time
        :type create_time: int
        :param update_by: update_by
        :type update_by: str
        :param update_time: update_time
        :type update_time: int
        :param delete_time: delete_time
        :type delete_time: int
        :param rule_name: rule_name
        :type rule_name: str
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
        :param event_grouping: event_grouping
        :type event_grouping: bool
        :param schedule: 
        :type schedule: :class:`huaweicloudsdksa.v2.Schedule`
        :param triggers: triggers
        :type triggers: list[:class:`huaweicloudsdksa.v2.AlertRuleTrigger`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateAlertRuleResponse, self).__init__()

        self._rule_id = None
        self._pipe_id = None
        self._pipe_name = None
        self._create_by = None
        self._create_time = None
        self._update_by = None
        self._update_time = None
        self._delete_time = None
        self._rule_name = None
        self._query = None
        self._query_type = None
        self._status = None
        self._severity = None
        self._accumulated_times = None
        self._custom_properties = None
        self._event_grouping = None
        self._schedule = None
        self._triggers = None
        self._x_request_id = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if pipe_id is not None:
            self.pipe_id = pipe_id
        if pipe_name is not None:
            self.pipe_name = pipe_name
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if update_by is not None:
            self.update_by = update_by
        if update_time is not None:
            self.update_time = update_time
        if delete_time is not None:
            self.delete_time = delete_time
        if rule_name is not None:
            self.rule_name = rule_name
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
        if event_grouping is not None:
            self.event_grouping = event_grouping
        if schedule is not None:
            self.schedule = schedule
        if triggers is not None:
            self.triggers = triggers
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def rule_id(self):
        """Gets the rule_id of this CreateAlertRuleResponse.

        rule_id

        :return: The rule_id of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this CreateAlertRuleResponse.

        rule_id

        :param rule_id: The rule_id of this CreateAlertRuleResponse.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def pipe_id(self):
        """Gets the pipe_id of this CreateAlertRuleResponse.

        pipe_id

        :return: The pipe_id of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        """Sets the pipe_id of this CreateAlertRuleResponse.

        pipe_id

        :param pipe_id: The pipe_id of this CreateAlertRuleResponse.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def pipe_name(self):
        """Gets the pipe_name of this CreateAlertRuleResponse.

        pipe_name

        :return: The pipe_name of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._pipe_name

    @pipe_name.setter
    def pipe_name(self, pipe_name):
        """Sets the pipe_name of this CreateAlertRuleResponse.

        pipe_name

        :param pipe_name: The pipe_name of this CreateAlertRuleResponse.
        :type pipe_name: str
        """
        self._pipe_name = pipe_name

    @property
    def create_by(self):
        """Gets the create_by of this CreateAlertRuleResponse.

        create_by

        :return: The create_by of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this CreateAlertRuleResponse.

        create_by

        :param create_by: The create_by of this CreateAlertRuleResponse.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        """Gets the create_time of this CreateAlertRuleResponse.

        create_time

        :return: The create_time of this CreateAlertRuleResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateAlertRuleResponse.

        create_time

        :param create_time: The create_time of this CreateAlertRuleResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_by(self):
        """Gets the update_by of this CreateAlertRuleResponse.

        update_by

        :return: The update_by of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this CreateAlertRuleResponse.

        update_by

        :param update_by: The update_by of this CreateAlertRuleResponse.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        """Gets the update_time of this CreateAlertRuleResponse.

        update_time

        :return: The update_time of this CreateAlertRuleResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CreateAlertRuleResponse.

        update_time

        :param update_time: The update_time of this CreateAlertRuleResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def delete_time(self):
        """Gets the delete_time of this CreateAlertRuleResponse.

        delete_time

        :return: The delete_time of this CreateAlertRuleResponse.
        :rtype: int
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        """Sets the delete_time of this CreateAlertRuleResponse.

        delete_time

        :param delete_time: The delete_time of this CreateAlertRuleResponse.
        :type delete_time: int
        """
        self._delete_time = delete_time

    @property
    def rule_name(self):
        """Gets the rule_name of this CreateAlertRuleResponse.

        rule_name

        :return: The rule_name of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this CreateAlertRuleResponse.

        rule_name

        :param rule_name: The rule_name of this CreateAlertRuleResponse.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def query(self):
        """Gets the query of this CreateAlertRuleResponse.

        query

        :return: The query of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this CreateAlertRuleResponse.

        query

        :param query: The query of this CreateAlertRuleResponse.
        :type query: str
        """
        self._query = query

    @property
    def query_type(self):
        """Gets the query_type of this CreateAlertRuleResponse.

        query_type. SQL, CBSL.

        :return: The query_type of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this CreateAlertRuleResponse.

        query_type. SQL, CBSL.

        :param query_type: The query_type of this CreateAlertRuleResponse.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def status(self):
        """Gets the status of this CreateAlertRuleResponse.

        status. ENABLED, DISABLED

        :return: The status of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateAlertRuleResponse.

        status. ENABLED, DISABLED

        :param status: The status of this CreateAlertRuleResponse.
        :type status: str
        """
        self._status = status

    @property
    def severity(self):
        """Gets the severity of this CreateAlertRuleResponse.

        severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :return: The severity of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this CreateAlertRuleResponse.

        severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :param severity: The severity of this CreateAlertRuleResponse.
        :type severity: str
        """
        self._severity = severity

    @property
    def accumulated_times(self):
        """Gets the accumulated_times of this CreateAlertRuleResponse.

        accumulated_times

        :return: The accumulated_times of this CreateAlertRuleResponse.
        :rtype: int
        """
        return self._accumulated_times

    @accumulated_times.setter
    def accumulated_times(self, accumulated_times):
        """Sets the accumulated_times of this CreateAlertRuleResponse.

        accumulated_times

        :param accumulated_times: The accumulated_times of this CreateAlertRuleResponse.
        :type accumulated_times: int
        """
        self._accumulated_times = accumulated_times

    @property
    def custom_properties(self):
        """Gets the custom_properties of this CreateAlertRuleResponse.

        custom_properties

        :return: The custom_properties of this CreateAlertRuleResponse.
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this CreateAlertRuleResponse.

        custom_properties

        :param custom_properties: The custom_properties of this CreateAlertRuleResponse.
        :type custom_properties: dict(str, str)
        """
        self._custom_properties = custom_properties

    @property
    def event_grouping(self):
        """Gets the event_grouping of this CreateAlertRuleResponse.

        event_grouping

        :return: The event_grouping of this CreateAlertRuleResponse.
        :rtype: bool
        """
        return self._event_grouping

    @event_grouping.setter
    def event_grouping(self, event_grouping):
        """Sets the event_grouping of this CreateAlertRuleResponse.

        event_grouping

        :param event_grouping: The event_grouping of this CreateAlertRuleResponse.
        :type event_grouping: bool
        """
        self._event_grouping = event_grouping

    @property
    def schedule(self):
        """Gets the schedule of this CreateAlertRuleResponse.

        :return: The schedule of this CreateAlertRuleResponse.
        :rtype: :class:`huaweicloudsdksa.v2.Schedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this CreateAlertRuleResponse.

        :param schedule: The schedule of this CreateAlertRuleResponse.
        :type schedule: :class:`huaweicloudsdksa.v2.Schedule`
        """
        self._schedule = schedule

    @property
    def triggers(self):
        """Gets the triggers of this CreateAlertRuleResponse.

        triggers

        :return: The triggers of this CreateAlertRuleResponse.
        :rtype: list[:class:`huaweicloudsdksa.v2.AlertRuleTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this CreateAlertRuleResponse.

        triggers

        :param triggers: The triggers of this CreateAlertRuleResponse.
        :type triggers: list[:class:`huaweicloudsdksa.v2.AlertRuleTrigger`]
        """
        self._triggers = triggers

    @property
    def x_request_id(self):
        """Gets the x_request_id of this CreateAlertRuleResponse.

        :return: The x_request_id of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this CreateAlertRuleResponse.

        :param x_request_id: The x_request_id of this CreateAlertRuleResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, CreateAlertRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
