# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlertRuleResponse(SdkResponse):

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
        'custom_properties': 'custom_properties',
        'event_grouping': 'event_grouping',
        'schedule': 'schedule',
        'triggers': 'triggers',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, rule_id=None, pipe_id=None, pipe_name=None, create_by=None, create_time=None, update_by=None, update_time=None, delete_time=None, rule_name=None, query=None, query_type=None, status=None, severity=None, custom_properties=None, event_grouping=None, schedule=None, triggers=None, x_request_id=None):
        """ShowAlertRuleResponse

        The model defined in huaweicloud sdk

        :param rule_id: 告警规则 ID。Alert rule ID.
        :type rule_id: str
        :param pipe_id: 数据管道 ID。Pipe ID.
        :type pipe_id: str
        :param pipe_name: 数据管道名称。Pipe name.
        :type pipe_name: str
        :param create_by: 创建人。Create by.
        :type create_by: str
        :param create_time: 创建时间。Create time.
        :type create_time: int
        :param update_by: 更新人。Update by.
        :type update_by: str
        :param update_time: 更新时间。Update time.
        :type update_time: int
        :param delete_time: 删除时间。Delete time.
        :type delete_time: int
        :param rule_name: 告警规则名称。Alert rule name.
        :type rule_name: str
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
        :param event_grouping: 告警分组。Event grouping.
        :type event_grouping: bool
        :param schedule: 
        :type schedule: :class:`huaweicloudsdksecmaster.v2.Schedule`
        :param triggers: 告警触发规则。Alert triggers.
        :type triggers: list[:class:`huaweicloudsdksecmaster.v2.AlertRuleTrigger`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowAlertRuleResponse, self).__init__()

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
        """Gets the rule_id of this ShowAlertRuleResponse.

        告警规则 ID。Alert rule ID.

        :return: The rule_id of this ShowAlertRuleResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this ShowAlertRuleResponse.

        告警规则 ID。Alert rule ID.

        :param rule_id: The rule_id of this ShowAlertRuleResponse.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def pipe_id(self):
        """Gets the pipe_id of this ShowAlertRuleResponse.

        数据管道 ID。Pipe ID.

        :return: The pipe_id of this ShowAlertRuleResponse.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        """Sets the pipe_id of this ShowAlertRuleResponse.

        数据管道 ID。Pipe ID.

        :param pipe_id: The pipe_id of this ShowAlertRuleResponse.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def pipe_name(self):
        """Gets the pipe_name of this ShowAlertRuleResponse.

        数据管道名称。Pipe name.

        :return: The pipe_name of this ShowAlertRuleResponse.
        :rtype: str
        """
        return self._pipe_name

    @pipe_name.setter
    def pipe_name(self, pipe_name):
        """Sets the pipe_name of this ShowAlertRuleResponse.

        数据管道名称。Pipe name.

        :param pipe_name: The pipe_name of this ShowAlertRuleResponse.
        :type pipe_name: str
        """
        self._pipe_name = pipe_name

    @property
    def create_by(self):
        """Gets the create_by of this ShowAlertRuleResponse.

        创建人。Create by.

        :return: The create_by of this ShowAlertRuleResponse.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this ShowAlertRuleResponse.

        创建人。Create by.

        :param create_by: The create_by of this ShowAlertRuleResponse.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        """Gets the create_time of this ShowAlertRuleResponse.

        创建时间。Create time.

        :return: The create_time of this ShowAlertRuleResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowAlertRuleResponse.

        创建时间。Create time.

        :param create_time: The create_time of this ShowAlertRuleResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_by(self):
        """Gets the update_by of this ShowAlertRuleResponse.

        更新人。Update by.

        :return: The update_by of this ShowAlertRuleResponse.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this ShowAlertRuleResponse.

        更新人。Update by.

        :param update_by: The update_by of this ShowAlertRuleResponse.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        """Gets the update_time of this ShowAlertRuleResponse.

        更新时间。Update time.

        :return: The update_time of this ShowAlertRuleResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowAlertRuleResponse.

        更新时间。Update time.

        :param update_time: The update_time of this ShowAlertRuleResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def delete_time(self):
        """Gets the delete_time of this ShowAlertRuleResponse.

        删除时间。Delete time.

        :return: The delete_time of this ShowAlertRuleResponse.
        :rtype: int
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        """Sets the delete_time of this ShowAlertRuleResponse.

        删除时间。Delete time.

        :param delete_time: The delete_time of this ShowAlertRuleResponse.
        :type delete_time: int
        """
        self._delete_time = delete_time

    @property
    def rule_name(self):
        """Gets the rule_name of this ShowAlertRuleResponse.

        告警规则名称。Alert rule name.

        :return: The rule_name of this ShowAlertRuleResponse.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this ShowAlertRuleResponse.

        告警规则名称。Alert rule name.

        :param rule_name: The rule_name of this ShowAlertRuleResponse.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def query(self):
        """Gets the query of this ShowAlertRuleResponse.

        查询语句。Query.

        :return: The query of this ShowAlertRuleResponse.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this ShowAlertRuleResponse.

        查询语句。Query.

        :param query: The query of this ShowAlertRuleResponse.
        :type query: str
        """
        self._query = query

    @property
    def query_type(self):
        """Gets the query_type of this ShowAlertRuleResponse.

        查询语法，SQL。Query type. SQL.

        :return: The query_type of this ShowAlertRuleResponse.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this ShowAlertRuleResponse.

        查询语法，SQL。Query type. SQL.

        :param query_type: The query_type of this ShowAlertRuleResponse.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def status(self):
        """Gets the status of this ShowAlertRuleResponse.

        启用状态，启用、停用。Status, enabled, disabled.

        :return: The status of this ShowAlertRuleResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowAlertRuleResponse.

        启用状态，启用、停用。Status, enabled, disabled.

        :param status: The status of this ShowAlertRuleResponse.
        :type status: str
        """
        self._status = status

    @property
    def severity(self):
        """Gets the severity of this ShowAlertRuleResponse.

        严重程度，提示、低危、中危、高危、致命。Severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :return: The severity of this ShowAlertRuleResponse.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ShowAlertRuleResponse.

        严重程度，提示、低危、中危、高危、致命。Severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :param severity: The severity of this ShowAlertRuleResponse.
        :type severity: str
        """
        self._severity = severity

    @property
    def custom_properties(self):
        """Gets the custom_properties of this ShowAlertRuleResponse.

        自定义扩展信息。Custom properties.

        :return: The custom_properties of this ShowAlertRuleResponse.
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this ShowAlertRuleResponse.

        自定义扩展信息。Custom properties.

        :param custom_properties: The custom_properties of this ShowAlertRuleResponse.
        :type custom_properties: dict(str, str)
        """
        self._custom_properties = custom_properties

    @property
    def event_grouping(self):
        """Gets the event_grouping of this ShowAlertRuleResponse.

        告警分组。Event grouping.

        :return: The event_grouping of this ShowAlertRuleResponse.
        :rtype: bool
        """
        return self._event_grouping

    @event_grouping.setter
    def event_grouping(self, event_grouping):
        """Sets the event_grouping of this ShowAlertRuleResponse.

        告警分组。Event grouping.

        :param event_grouping: The event_grouping of this ShowAlertRuleResponse.
        :type event_grouping: bool
        """
        self._event_grouping = event_grouping

    @property
    def schedule(self):
        """Gets the schedule of this ShowAlertRuleResponse.

        :return: The schedule of this ShowAlertRuleResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.Schedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this ShowAlertRuleResponse.

        :param schedule: The schedule of this ShowAlertRuleResponse.
        :type schedule: :class:`huaweicloudsdksecmaster.v2.Schedule`
        """
        self._schedule = schedule

    @property
    def triggers(self):
        """Gets the triggers of this ShowAlertRuleResponse.

        告警触发规则。Alert triggers.

        :return: The triggers of this ShowAlertRuleResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.AlertRuleTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this ShowAlertRuleResponse.

        告警触发规则。Alert triggers.

        :param triggers: The triggers of this ShowAlertRuleResponse.
        :type triggers: list[:class:`huaweicloudsdksecmaster.v2.AlertRuleTrigger`]
        """
        self._triggers = triggers

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowAlertRuleResponse.

        :return: The x_request_id of this ShowAlertRuleResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowAlertRuleResponse.

        :param x_request_id: The x_request_id of this ShowAlertRuleResponse.
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
        if not isinstance(other, ShowAlertRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
