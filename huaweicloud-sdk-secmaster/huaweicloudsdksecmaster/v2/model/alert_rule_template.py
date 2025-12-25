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
        'accumulated_times': 'int',
        'alert_description': 'str',
        'alert_name': 'str',
        'alert_remediation': 'str',
        'alert_type': 'dict(str, str)',
        'create_by': 'str',
        'create_time': 'int',
        'custom_properties': 'dict(str, str)',
        'description': 'str',
        'event_grouping': 'bool',
        'job_mode': 'str',
        'process_status': 'str',
        'query': 'str',
        'query_type': 'str',
        'schedule': 'AlertRuleSchedule',
        'severity': 'str',
        'simulation': 'bool',
        'status': 'str',
        'suppresion': 'bool',
        'table_name': 'str',
        'template_id': 'str',
        'template_name': 'str',
        'triggers': 'list[Trigger]',
        'update_by': 'str',
        'update_time': 'int',
        'update_time_by_user': 'int'
    }

    attribute_map = {
        'accumulated_times': 'accumulated_times',
        'alert_description': 'alert_description',
        'alert_name': 'alert_name',
        'alert_remediation': 'alert_remediation',
        'alert_type': 'alert_type',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'custom_properties': 'custom_properties',
        'description': 'description',
        'event_grouping': 'event_grouping',
        'job_mode': 'job_mode',
        'process_status': 'process_status',
        'query': 'query',
        'query_type': 'query_type',
        'schedule': 'schedule',
        'severity': 'severity',
        'simulation': 'simulation',
        'status': 'status',
        'suppresion': 'suppresion',
        'table_name': 'table_name',
        'template_id': 'template_id',
        'template_name': 'template_name',
        'triggers': 'triggers',
        'update_by': 'update_by',
        'update_time': 'update_time',
        'update_time_by_user': 'update_time_by_user'
    }

    def __init__(self, accumulated_times=None, alert_description=None, alert_name=None, alert_remediation=None, alert_type=None, create_by=None, create_time=None, custom_properties=None, description=None, event_grouping=None, job_mode=None, process_status=None, query=None, query_type=None, schedule=None, severity=None, simulation=None, status=None, suppresion=None, table_name=None, template_id=None, template_name=None, triggers=None, update_by=None, update_time=None, update_time_by_user=None):
        r"""AlertRuleTemplate

        The model defined in huaweicloud sdk

        :param accumulated_times: 累计次数
        :type accumulated_times: int
        :param alert_description: 告警描述
        :type alert_description: str
        :param alert_name: 告警名称
        :type alert_name: str
        :param alert_remediation: 告警修复
        :type alert_remediation: str
        :param alert_type: Map&lt;String,String&gt;
        :type alert_type: dict(str, str)
        :param create_by: Iam用户ID
        :type create_by: str
        :param create_time: 毫秒时间戳
        :type create_time: int
        :param custom_properties: Map&lt;String,String&gt;
        :type custom_properties: dict(str, str)
        :param description: 告警规则模板描述
        :type description: str
        :param event_grouping: 告警组
        :type event_grouping: bool
        :param job_mode: **参数解释**: 作业模式 - STREAMING 流式处理 - BATCH 批处理 - SEARCH 检索  **约束限制** 不涉及 **取值范围**: - STREAMING - BATCH - SEARCH  **默认值** 不涉及  
        :type job_mode: str
        :param process_status: **参数解释**: 处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - ENABLING 启用中 - DISABLING 停用中 - DELETING 删除中 - CREATE_FAILED 创建失败 - UPDATE_FAILED 更新失败 - ENABLE_FAILED 启用失败 - DISABLE_FAILED 停用失败 - DELETE_FAILED 删除失败 - RECOVERING 恢复中  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - ENABLING - DISABLING - DELETING - CREATE_FAILED - UPDATE_FAILED - ENABLE_FAILED - DISABLE_FAILED - DELETE_FAILED - RECOVERING  **默认值** 不涉及         
        :type process_status: str
        :param query: 查询语句
        :type query: str
        :param query_type: **参数解释**: 查询类型 - SQL SQL查询 - CBSL CBSL查询  **约束限制** 不涉及 **取值范围**: - SQL - CBSL  **默认值** 不涉及        
        :type query_type: str
        :param schedule: 
        :type schedule: :class:`huaweicloudsdksecmaster.v2.AlertRuleSchedule`
        :param severity: **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及  
        :type severity: str
        :param simulation: 是否仿真
        :type simulation: bool
        :param status: **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    
        :type status: str
        :param suppresion: 告警抑制
        :type suppresion: bool
        :param table_name: 表名称
        :type table_name: str
        :param template_id: UUID
        :type template_id: str
        :param template_name: 模板名称
        :type template_name: str
        :param triggers: 触发器数组
        :type triggers: list[:class:`huaweicloudsdksecmaster.v2.Trigger`]
        :param update_by: Iam用户ID
        :type update_by: str
        :param update_time: 毫秒时间戳
        :type update_time: int
        :param update_time_by_user: 毫秒时间戳
        :type update_time_by_user: int
        """
        
        

        self._accumulated_times = None
        self._alert_description = None
        self._alert_name = None
        self._alert_remediation = None
        self._alert_type = None
        self._create_by = None
        self._create_time = None
        self._custom_properties = None
        self._description = None
        self._event_grouping = None
        self._job_mode = None
        self._process_status = None
        self._query = None
        self._query_type = None
        self._schedule = None
        self._severity = None
        self._simulation = None
        self._status = None
        self._suppresion = None
        self._table_name = None
        self._template_id = None
        self._template_name = None
        self._triggers = None
        self._update_by = None
        self._update_time = None
        self._update_time_by_user = None
        self.discriminator = None

        if accumulated_times is not None:
            self.accumulated_times = accumulated_times
        if alert_description is not None:
            self.alert_description = alert_description
        if alert_name is not None:
            self.alert_name = alert_name
        if alert_remediation is not None:
            self.alert_remediation = alert_remediation
        if alert_type is not None:
            self.alert_type = alert_type
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if description is not None:
            self.description = description
        if event_grouping is not None:
            self.event_grouping = event_grouping
        if job_mode is not None:
            self.job_mode = job_mode
        if process_status is not None:
            self.process_status = process_status
        if query is not None:
            self.query = query
        if query_type is not None:
            self.query_type = query_type
        if schedule is not None:
            self.schedule = schedule
        if severity is not None:
            self.severity = severity
        if simulation is not None:
            self.simulation = simulation
        if status is not None:
            self.status = status
        if suppresion is not None:
            self.suppresion = suppresion
        if table_name is not None:
            self.table_name = table_name
        if template_id is not None:
            self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if triggers is not None:
            self.triggers = triggers
        if update_by is not None:
            self.update_by = update_by
        if update_time is not None:
            self.update_time = update_time
        if update_time_by_user is not None:
            self.update_time_by_user = update_time_by_user

    @property
    def accumulated_times(self):
        r"""Gets the accumulated_times of this AlertRuleTemplate.

        累计次数

        :return: The accumulated_times of this AlertRuleTemplate.
        :rtype: int
        """
        return self._accumulated_times

    @accumulated_times.setter
    def accumulated_times(self, accumulated_times):
        r"""Sets the accumulated_times of this AlertRuleTemplate.

        累计次数

        :param accumulated_times: The accumulated_times of this AlertRuleTemplate.
        :type accumulated_times: int
        """
        self._accumulated_times = accumulated_times

    @property
    def alert_description(self):
        r"""Gets the alert_description of this AlertRuleTemplate.

        告警描述

        :return: The alert_description of this AlertRuleTemplate.
        :rtype: str
        """
        return self._alert_description

    @alert_description.setter
    def alert_description(self, alert_description):
        r"""Sets the alert_description of this AlertRuleTemplate.

        告警描述

        :param alert_description: The alert_description of this AlertRuleTemplate.
        :type alert_description: str
        """
        self._alert_description = alert_description

    @property
    def alert_name(self):
        r"""Gets the alert_name of this AlertRuleTemplate.

        告警名称

        :return: The alert_name of this AlertRuleTemplate.
        :rtype: str
        """
        return self._alert_name

    @alert_name.setter
    def alert_name(self, alert_name):
        r"""Sets the alert_name of this AlertRuleTemplate.

        告警名称

        :param alert_name: The alert_name of this AlertRuleTemplate.
        :type alert_name: str
        """
        self._alert_name = alert_name

    @property
    def alert_remediation(self):
        r"""Gets the alert_remediation of this AlertRuleTemplate.

        告警修复

        :return: The alert_remediation of this AlertRuleTemplate.
        :rtype: str
        """
        return self._alert_remediation

    @alert_remediation.setter
    def alert_remediation(self, alert_remediation):
        r"""Sets the alert_remediation of this AlertRuleTemplate.

        告警修复

        :param alert_remediation: The alert_remediation of this AlertRuleTemplate.
        :type alert_remediation: str
        """
        self._alert_remediation = alert_remediation

    @property
    def alert_type(self):
        r"""Gets the alert_type of this AlertRuleTemplate.

        Map<String,String>

        :return: The alert_type of this AlertRuleTemplate.
        :rtype: dict(str, str)
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        r"""Sets the alert_type of this AlertRuleTemplate.

        Map<String,String>

        :param alert_type: The alert_type of this AlertRuleTemplate.
        :type alert_type: dict(str, str)
        """
        self._alert_type = alert_type

    @property
    def create_by(self):
        r"""Gets the create_by of this AlertRuleTemplate.

        Iam用户ID

        :return: The create_by of this AlertRuleTemplate.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this AlertRuleTemplate.

        Iam用户ID

        :param create_by: The create_by of this AlertRuleTemplate.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        r"""Gets the create_time of this AlertRuleTemplate.

        毫秒时间戳

        :return: The create_time of this AlertRuleTemplate.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AlertRuleTemplate.

        毫秒时间戳

        :param create_time: The create_time of this AlertRuleTemplate.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def custom_properties(self):
        r"""Gets the custom_properties of this AlertRuleTemplate.

        Map<String,String>

        :return: The custom_properties of this AlertRuleTemplate.
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        r"""Sets the custom_properties of this AlertRuleTemplate.

        Map<String,String>

        :param custom_properties: The custom_properties of this AlertRuleTemplate.
        :type custom_properties: dict(str, str)
        """
        self._custom_properties = custom_properties

    @property
    def description(self):
        r"""Gets the description of this AlertRuleTemplate.

        告警规则模板描述

        :return: The description of this AlertRuleTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AlertRuleTemplate.

        告警规则模板描述

        :param description: The description of this AlertRuleTemplate.
        :type description: str
        """
        self._description = description

    @property
    def event_grouping(self):
        r"""Gets the event_grouping of this AlertRuleTemplate.

        告警组

        :return: The event_grouping of this AlertRuleTemplate.
        :rtype: bool
        """
        return self._event_grouping

    @event_grouping.setter
    def event_grouping(self, event_grouping):
        r"""Sets the event_grouping of this AlertRuleTemplate.

        告警组

        :param event_grouping: The event_grouping of this AlertRuleTemplate.
        :type event_grouping: bool
        """
        self._event_grouping = event_grouping

    @property
    def job_mode(self):
        r"""Gets the job_mode of this AlertRuleTemplate.

        **参数解释**: 作业模式 - STREAMING 流式处理 - BATCH 批处理 - SEARCH 检索  **约束限制** 不涉及 **取值范围**: - STREAMING - BATCH - SEARCH  **默认值** 不涉及  

        :return: The job_mode of this AlertRuleTemplate.
        :rtype: str
        """
        return self._job_mode

    @job_mode.setter
    def job_mode(self, job_mode):
        r"""Sets the job_mode of this AlertRuleTemplate.

        **参数解释**: 作业模式 - STREAMING 流式处理 - BATCH 批处理 - SEARCH 检索  **约束限制** 不涉及 **取值范围**: - STREAMING - BATCH - SEARCH  **默认值** 不涉及  

        :param job_mode: The job_mode of this AlertRuleTemplate.
        :type job_mode: str
        """
        self._job_mode = job_mode

    @property
    def process_status(self):
        r"""Gets the process_status of this AlertRuleTemplate.

        **参数解释**: 处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - ENABLING 启用中 - DISABLING 停用中 - DELETING 删除中 - CREATE_FAILED 创建失败 - UPDATE_FAILED 更新失败 - ENABLE_FAILED 启用失败 - DISABLE_FAILED 停用失败 - DELETE_FAILED 删除失败 - RECOVERING 恢复中  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - ENABLING - DISABLING - DELETING - CREATE_FAILED - UPDATE_FAILED - ENABLE_FAILED - DISABLE_FAILED - DELETE_FAILED - RECOVERING  **默认值** 不涉及         

        :return: The process_status of this AlertRuleTemplate.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this AlertRuleTemplate.

        **参数解释**: 处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - ENABLING 启用中 - DISABLING 停用中 - DELETING 删除中 - CREATE_FAILED 创建失败 - UPDATE_FAILED 更新失败 - ENABLE_FAILED 启用失败 - DISABLE_FAILED 停用失败 - DELETE_FAILED 删除失败 - RECOVERING 恢复中  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - ENABLING - DISABLING - DELETING - CREATE_FAILED - UPDATE_FAILED - ENABLE_FAILED - DISABLE_FAILED - DELETE_FAILED - RECOVERING  **默认值** 不涉及         

        :param process_status: The process_status of this AlertRuleTemplate.
        :type process_status: str
        """
        self._process_status = process_status

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

        **参数解释**: 查询类型 - SQL SQL查询 - CBSL CBSL查询  **约束限制** 不涉及 **取值范围**: - SQL - CBSL  **默认值** 不涉及        

        :return: The query_type of this AlertRuleTemplate.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this AlertRuleTemplate.

        **参数解释**: 查询类型 - SQL SQL查询 - CBSL CBSL查询  **约束限制** 不涉及 **取值范围**: - SQL - CBSL  **默认值** 不涉及        

        :param query_type: The query_type of this AlertRuleTemplate.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def schedule(self):
        r"""Gets the schedule of this AlertRuleTemplate.

        :return: The schedule of this AlertRuleTemplate.
        :rtype: :class:`huaweicloudsdksecmaster.v2.AlertRuleSchedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this AlertRuleTemplate.

        :param schedule: The schedule of this AlertRuleTemplate.
        :type schedule: :class:`huaweicloudsdksecmaster.v2.AlertRuleSchedule`
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
    def simulation(self):
        r"""Gets the simulation of this AlertRuleTemplate.

        是否仿真

        :return: The simulation of this AlertRuleTemplate.
        :rtype: bool
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        r"""Sets the simulation of this AlertRuleTemplate.

        是否仿真

        :param simulation: The simulation of this AlertRuleTemplate.
        :type simulation: bool
        """
        self._simulation = simulation

    @property
    def status(self):
        r"""Gets the status of this AlertRuleTemplate.

        **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    

        :return: The status of this AlertRuleTemplate.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AlertRuleTemplate.

        **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    

        :param status: The status of this AlertRuleTemplate.
        :type status: str
        """
        self._status = status

    @property
    def suppresion(self):
        r"""Gets the suppresion of this AlertRuleTemplate.

        告警抑制

        :return: The suppresion of this AlertRuleTemplate.
        :rtype: bool
        """
        return self._suppresion

    @suppresion.setter
    def suppresion(self, suppresion):
        r"""Sets the suppresion of this AlertRuleTemplate.

        告警抑制

        :param suppresion: The suppresion of this AlertRuleTemplate.
        :type suppresion: bool
        """
        self._suppresion = suppresion

    @property
    def table_name(self):
        r"""Gets the table_name of this AlertRuleTemplate.

        表名称

        :return: The table_name of this AlertRuleTemplate.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this AlertRuleTemplate.

        表名称

        :param table_name: The table_name of this AlertRuleTemplate.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def template_id(self):
        r"""Gets the template_id of this AlertRuleTemplate.

        UUID

        :return: The template_id of this AlertRuleTemplate.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this AlertRuleTemplate.

        UUID

        :param template_id: The template_id of this AlertRuleTemplate.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this AlertRuleTemplate.

        模板名称

        :return: The template_name of this AlertRuleTemplate.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this AlertRuleTemplate.

        模板名称

        :param template_name: The template_name of this AlertRuleTemplate.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def triggers(self):
        r"""Gets the triggers of this AlertRuleTemplate.

        触发器数组

        :return: The triggers of this AlertRuleTemplate.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.Trigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this AlertRuleTemplate.

        触发器数组

        :param triggers: The triggers of this AlertRuleTemplate.
        :type triggers: list[:class:`huaweicloudsdksecmaster.v2.Trigger`]
        """
        self._triggers = triggers

    @property
    def update_by(self):
        r"""Gets the update_by of this AlertRuleTemplate.

        Iam用户ID

        :return: The update_by of this AlertRuleTemplate.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this AlertRuleTemplate.

        Iam用户ID

        :param update_by: The update_by of this AlertRuleTemplate.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        r"""Gets the update_time of this AlertRuleTemplate.

        毫秒时间戳

        :return: The update_time of this AlertRuleTemplate.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AlertRuleTemplate.

        毫秒时间戳

        :param update_time: The update_time of this AlertRuleTemplate.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def update_time_by_user(self):
        r"""Gets the update_time_by_user of this AlertRuleTemplate.

        毫秒时间戳

        :return: The update_time_by_user of this AlertRuleTemplate.
        :rtype: int
        """
        return self._update_time_by_user

    @update_time_by_user.setter
    def update_time_by_user(self, update_time_by_user):
        r"""Sets the update_time_by_user of this AlertRuleTemplate.

        毫秒时间戳

        :param update_time_by_user: The update_time_by_user of this AlertRuleTemplate.
        :type update_time_by_user: int
        """
        self._update_time_by_user = update_time_by_user

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
