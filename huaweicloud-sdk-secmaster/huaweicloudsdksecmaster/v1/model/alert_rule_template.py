# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertRuleTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_properties': 'dict(str, str)',
        'data_source': 'str',
        'event_grouping': 'bool',
        'query': 'str',
        'query_type': 'str',
        'schedule': 'Schedule',
        'severity': 'str',
        'template_id': 'str',
        'template_name': 'str',
        'triggers': 'list[AlertRuleTrigger]',
        'update_time': 'int',
        'version': 'str'
    }

    attribute_map = {
        'custom_properties': 'custom_properties',
        'data_source': 'data_source',
        'event_grouping': 'event_grouping',
        'query': 'query',
        'query_type': 'query_type',
        'schedule': 'schedule',
        'severity': 'severity',
        'template_id': 'template_id',
        'template_name': 'template_name',
        'triggers': 'triggers',
        'update_time': 'update_time',
        'version': 'version'
    }

    def __init__(self, custom_properties=None, data_source=None, event_grouping=None, query=None, query_type=None, schedule=None, severity=None, template_id=None, template_name=None, triggers=None, update_time=None, version=None):
        r"""AlertRuleTemplate

        The model defined in huaweicloud sdk

        :param custom_properties: 自定义扩展信息
        :type custom_properties: dict(str, str)
        :param data_source: 数据源
        :type data_source: str
        :param event_grouping: 告警分组
        :type event_grouping: bool
        :param query: 查询语句
        :type query: str
        :param query_type: **参数解释**: 查询语法类型 - SQL查询 **约束限制**: 不涉及  **取值范围**: - SQL **默认值**:  SQL
        :type query_type: str
        :param schedule: 
        :type schedule: :class:`huaweicloudsdksecmaster.v1.Schedule`
        :param severity: **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及
        :type severity: str
        :param template_id: 告警规则模板 ID
        :type template_id: str
        :param template_name: 告警规则模板名称
        :type template_name: str
        :param triggers: 告警触发规则
        :type triggers: list[:class:`huaweicloudsdksecmaster.v1.AlertRuleTrigger`]
        :param update_time: 更新时间
        :type update_time: int
        :param version: 版本
        :type version: str
        """
        
        

        self._custom_properties = None
        self._data_source = None
        self._event_grouping = None
        self._query = None
        self._query_type = None
        self._schedule = None
        self._severity = None
        self._template_id = None
        self._template_name = None
        self._triggers = None
        self._update_time = None
        self._version = None
        self.discriminator = None

        if custom_properties is not None:
            self.custom_properties = custom_properties
        self.data_source = data_source
        if event_grouping is not None:
            self.event_grouping = event_grouping
        if query is not None:
            self.query = query
        if query_type is not None:
            self.query_type = query_type
        if schedule is not None:
            self.schedule = schedule
        self.severity = severity
        self.template_id = template_id
        self.template_name = template_name
        if triggers is not None:
            self.triggers = triggers
        self.update_time = update_time
        self.version = version

    @property
    def custom_properties(self):
        r"""Gets the custom_properties of this AlertRuleTemplate.

        自定义扩展信息

        :return: The custom_properties of this AlertRuleTemplate.
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        r"""Sets the custom_properties of this AlertRuleTemplate.

        自定义扩展信息

        :param custom_properties: The custom_properties of this AlertRuleTemplate.
        :type custom_properties: dict(str, str)
        """
        self._custom_properties = custom_properties

    @property
    def data_source(self):
        r"""Gets the data_source of this AlertRuleTemplate.

        数据源

        :return: The data_source of this AlertRuleTemplate.
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        r"""Sets the data_source of this AlertRuleTemplate.

        数据源

        :param data_source: The data_source of this AlertRuleTemplate.
        :type data_source: str
        """
        self._data_source = data_source

    @property
    def event_grouping(self):
        r"""Gets the event_grouping of this AlertRuleTemplate.

        告警分组

        :return: The event_grouping of this AlertRuleTemplate.
        :rtype: bool
        """
        return self._event_grouping

    @event_grouping.setter
    def event_grouping(self, event_grouping):
        r"""Sets the event_grouping of this AlertRuleTemplate.

        告警分组

        :param event_grouping: The event_grouping of this AlertRuleTemplate.
        :type event_grouping: bool
        """
        self._event_grouping = event_grouping

    @property
    def query(self):
        r"""Gets the query of this AlertRuleTemplate.

        查询语句

        :return: The query of this AlertRuleTemplate.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this AlertRuleTemplate.

        查询语句

        :param query: The query of this AlertRuleTemplate.
        :type query: str
        """
        self._query = query

    @property
    def query_type(self):
        r"""Gets the query_type of this AlertRuleTemplate.

        **参数解释**: 查询语法类型 - SQL查询 **约束限制**: 不涉及  **取值范围**: - SQL **默认值**:  SQL

        :return: The query_type of this AlertRuleTemplate.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this AlertRuleTemplate.

        **参数解释**: 查询语法类型 - SQL查询 **约束限制**: 不涉及  **取值范围**: - SQL **默认值**:  SQL

        :param query_type: The query_type of this AlertRuleTemplate.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def schedule(self):
        r"""Gets the schedule of this AlertRuleTemplate.

        :return: The schedule of this AlertRuleTemplate.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Schedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this AlertRuleTemplate.

        :param schedule: The schedule of this AlertRuleTemplate.
        :type schedule: :class:`huaweicloudsdksecmaster.v1.Schedule`
        """
        self._schedule = schedule

    @property
    def severity(self):
        r"""Gets the severity of this AlertRuleTemplate.

        **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及

        :return: The severity of this AlertRuleTemplate.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this AlertRuleTemplate.

        **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及

        :param severity: The severity of this AlertRuleTemplate.
        :type severity: str
        """
        self._severity = severity

    @property
    def template_id(self):
        r"""Gets the template_id of this AlertRuleTemplate.

        告警规则模板 ID

        :return: The template_id of this AlertRuleTemplate.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this AlertRuleTemplate.

        告警规则模板 ID

        :param template_id: The template_id of this AlertRuleTemplate.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this AlertRuleTemplate.

        告警规则模板名称

        :return: The template_name of this AlertRuleTemplate.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this AlertRuleTemplate.

        告警规则模板名称

        :param template_name: The template_name of this AlertRuleTemplate.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def triggers(self):
        r"""Gets the triggers of this AlertRuleTemplate.

        告警触发规则

        :return: The triggers of this AlertRuleTemplate.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.AlertRuleTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this AlertRuleTemplate.

        告警触发规则

        :param triggers: The triggers of this AlertRuleTemplate.
        :type triggers: list[:class:`huaweicloudsdksecmaster.v1.AlertRuleTrigger`]
        """
        self._triggers = triggers

    @property
    def update_time(self):
        r"""Gets the update_time of this AlertRuleTemplate.

        更新时间

        :return: The update_time of this AlertRuleTemplate.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AlertRuleTemplate.

        更新时间

        :param update_time: The update_time of this AlertRuleTemplate.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def version(self):
        r"""Gets the version of this AlertRuleTemplate.

        版本

        :return: The version of this AlertRuleTemplate.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AlertRuleTemplate.

        版本

        :param version: The version of this AlertRuleTemplate.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, AlertRuleTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
