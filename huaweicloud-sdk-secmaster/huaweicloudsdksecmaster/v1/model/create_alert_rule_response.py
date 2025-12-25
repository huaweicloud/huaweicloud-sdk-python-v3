# coding: utf-8

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
        'create_by': 'str',
        'create_time': 'int',
        'custom_properties': 'dict(str, str)',
        'delete_time': 'int',
        'event_grouping': 'bool',
        'pipe_id': 'str',
        'pipe_name': 'str',
        'query': 'str',
        'query_type': 'str',
        'rule_id': 'str',
        'rule_name': 'str',
        'schedule': 'Schedule',
        'severity': 'str',
        'status': 'str',
        'triggers': 'list[AlertRuleTrigger]',
        'update_by': 'str',
        'update_time': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'create_by': 'create_by',
        'create_time': 'create_time',
        'custom_properties': 'custom_properties',
        'delete_time': 'delete_time',
        'event_grouping': 'event_grouping',
        'pipe_id': 'pipe_id',
        'pipe_name': 'pipe_name',
        'query': 'query',
        'query_type': 'query_type',
        'rule_id': 'rule_id',
        'rule_name': 'rule_name',
        'schedule': 'schedule',
        'severity': 'severity',
        'status': 'status',
        'triggers': 'triggers',
        'update_by': 'update_by',
        'update_time': 'update_time',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, create_by=None, create_time=None, custom_properties=None, delete_time=None, event_grouping=None, pipe_id=None, pipe_name=None, query=None, query_type=None, rule_id=None, rule_name=None, schedule=None, severity=None, status=None, triggers=None, update_by=None, update_time=None, x_request_id=None):
        r"""CreateAlertRuleResponse

        The model defined in huaweicloud sdk

        :param create_by: 创建人
        :type create_by: str
        :param create_time: 创建时间
        :type create_time: int
        :param custom_properties: 自定义扩展信息
        :type custom_properties: dict(str, str)
        :param delete_time: 删除时间
        :type delete_time: int
        :param event_grouping: 告警分组
        :type event_grouping: bool
        :param pipe_id: 数据管道 ID
        :type pipe_id: str
        :param pipe_name: 数据管道名称
        :type pipe_name: str
        :param query: 查询语句
        :type query: str
        :param query_type: **参数解释**: 查询语法类型 - SQL查询 **约束限制**: 不涉及  **取值范围**: - SQL **默认值**:  SQL
        :type query_type: str
        :param rule_id: 告警规则 ID
        :type rule_id: str
        :param rule_name: 告警规则名称
        :type rule_name: str
        :param schedule: 
        :type schedule: :class:`huaweicloudsdksecmaster.v1.Schedule`
        :param severity: **参数解释**: 状态 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命 **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL **默认值** MEDIUM
        :type severity: str
        :param status: **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及
        :type status: str
        :param triggers: 告警触发规则
        :type triggers: list[:class:`huaweicloudsdksecmaster.v1.AlertRuleTrigger`]
        :param update_by: 更新人
        :type update_by: str
        :param update_time: 更新时间
        :type update_time: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._create_by = None
        self._create_time = None
        self._custom_properties = None
        self._delete_time = None
        self._event_grouping = None
        self._pipe_id = None
        self._pipe_name = None
        self._query = None
        self._query_type = None
        self._rule_id = None
        self._rule_name = None
        self._schedule = None
        self._severity = None
        self._status = None
        self._triggers = None
        self._update_by = None
        self._update_time = None
        self._x_request_id = None
        self.discriminator = None

        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if delete_time is not None:
            self.delete_time = delete_time
        if event_grouping is not None:
            self.event_grouping = event_grouping
        if pipe_id is not None:
            self.pipe_id = pipe_id
        if pipe_name is not None:
            self.pipe_name = pipe_name
        if query is not None:
            self.query = query
        if query_type is not None:
            self.query_type = query_type
        if rule_id is not None:
            self.rule_id = rule_id
        if rule_name is not None:
            self.rule_name = rule_name
        if schedule is not None:
            self.schedule = schedule
        if severity is not None:
            self.severity = severity
        if status is not None:
            self.status = status
        if triggers is not None:
            self.triggers = triggers
        if update_by is not None:
            self.update_by = update_by
        if update_time is not None:
            self.update_time = update_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def create_by(self):
        r"""Gets the create_by of this CreateAlertRuleResponse.

        创建人

        :return: The create_by of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this CreateAlertRuleResponse.

        创建人

        :param create_by: The create_by of this CreateAlertRuleResponse.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateAlertRuleResponse.

        创建时间

        :return: The create_time of this CreateAlertRuleResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateAlertRuleResponse.

        创建时间

        :param create_time: The create_time of this CreateAlertRuleResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def custom_properties(self):
        r"""Gets the custom_properties of this CreateAlertRuleResponse.

        自定义扩展信息

        :return: The custom_properties of this CreateAlertRuleResponse.
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        r"""Sets the custom_properties of this CreateAlertRuleResponse.

        自定义扩展信息

        :param custom_properties: The custom_properties of this CreateAlertRuleResponse.
        :type custom_properties: dict(str, str)
        """
        self._custom_properties = custom_properties

    @property
    def delete_time(self):
        r"""Gets the delete_time of this CreateAlertRuleResponse.

        删除时间

        :return: The delete_time of this CreateAlertRuleResponse.
        :rtype: int
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        r"""Sets the delete_time of this CreateAlertRuleResponse.

        删除时间

        :param delete_time: The delete_time of this CreateAlertRuleResponse.
        :type delete_time: int
        """
        self._delete_time = delete_time

    @property
    def event_grouping(self):
        r"""Gets the event_grouping of this CreateAlertRuleResponse.

        告警分组

        :return: The event_grouping of this CreateAlertRuleResponse.
        :rtype: bool
        """
        return self._event_grouping

    @event_grouping.setter
    def event_grouping(self, event_grouping):
        r"""Sets the event_grouping of this CreateAlertRuleResponse.

        告警分组

        :param event_grouping: The event_grouping of this CreateAlertRuleResponse.
        :type event_grouping: bool
        """
        self._event_grouping = event_grouping

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this CreateAlertRuleResponse.

        数据管道 ID

        :return: The pipe_id of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this CreateAlertRuleResponse.

        数据管道 ID

        :param pipe_id: The pipe_id of this CreateAlertRuleResponse.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def pipe_name(self):
        r"""Gets the pipe_name of this CreateAlertRuleResponse.

        数据管道名称

        :return: The pipe_name of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._pipe_name

    @pipe_name.setter
    def pipe_name(self, pipe_name):
        r"""Sets the pipe_name of this CreateAlertRuleResponse.

        数据管道名称

        :param pipe_name: The pipe_name of this CreateAlertRuleResponse.
        :type pipe_name: str
        """
        self._pipe_name = pipe_name

    @property
    def query(self):
        r"""Gets the query of this CreateAlertRuleResponse.

        查询语句

        :return: The query of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this CreateAlertRuleResponse.

        查询语句

        :param query: The query of this CreateAlertRuleResponse.
        :type query: str
        """
        self._query = query

    @property
    def query_type(self):
        r"""Gets the query_type of this CreateAlertRuleResponse.

        **参数解释**: 查询语法类型 - SQL查询 **约束限制**: 不涉及  **取值范围**: - SQL **默认值**:  SQL

        :return: The query_type of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this CreateAlertRuleResponse.

        **参数解释**: 查询语法类型 - SQL查询 **约束限制**: 不涉及  **取值范围**: - SQL **默认值**:  SQL

        :param query_type: The query_type of this CreateAlertRuleResponse.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def rule_id(self):
        r"""Gets the rule_id of this CreateAlertRuleResponse.

        告警规则 ID

        :return: The rule_id of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this CreateAlertRuleResponse.

        告警规则 ID

        :param rule_id: The rule_id of this CreateAlertRuleResponse.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this CreateAlertRuleResponse.

        告警规则名称

        :return: The rule_name of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this CreateAlertRuleResponse.

        告警规则名称

        :param rule_name: The rule_name of this CreateAlertRuleResponse.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def schedule(self):
        r"""Gets the schedule of this CreateAlertRuleResponse.

        :return: The schedule of this CreateAlertRuleResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Schedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this CreateAlertRuleResponse.

        :param schedule: The schedule of this CreateAlertRuleResponse.
        :type schedule: :class:`huaweicloudsdksecmaster.v1.Schedule`
        """
        self._schedule = schedule

    @property
    def severity(self):
        r"""Gets the severity of this CreateAlertRuleResponse.

        **参数解释**: 状态 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命 **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL **默认值** MEDIUM

        :return: The severity of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this CreateAlertRuleResponse.

        **参数解释**: 状态 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命 **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL **默认值** MEDIUM

        :param severity: The severity of this CreateAlertRuleResponse.
        :type severity: str
        """
        self._severity = severity

    @property
    def status(self):
        r"""Gets the status of this CreateAlertRuleResponse.

        **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及

        :return: The status of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateAlertRuleResponse.

        **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及

        :param status: The status of this CreateAlertRuleResponse.
        :type status: str
        """
        self._status = status

    @property
    def triggers(self):
        r"""Gets the triggers of this CreateAlertRuleResponse.

        告警触发规则

        :return: The triggers of this CreateAlertRuleResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.AlertRuleTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this CreateAlertRuleResponse.

        告警触发规则

        :param triggers: The triggers of this CreateAlertRuleResponse.
        :type triggers: list[:class:`huaweicloudsdksecmaster.v1.AlertRuleTrigger`]
        """
        self._triggers = triggers

    @property
    def update_by(self):
        r"""Gets the update_by of this CreateAlertRuleResponse.

        更新人

        :return: The update_by of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this CreateAlertRuleResponse.

        更新人

        :param update_by: The update_by of this CreateAlertRuleResponse.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateAlertRuleResponse.

        更新时间

        :return: The update_time of this CreateAlertRuleResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateAlertRuleResponse.

        更新时间

        :param update_time: The update_time of this CreateAlertRuleResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateAlertRuleResponse.

        :return: The x_request_id of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateAlertRuleResponse.

        :param x_request_id: The x_request_id of this CreateAlertRuleResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateAlertRuleResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateAlertRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
