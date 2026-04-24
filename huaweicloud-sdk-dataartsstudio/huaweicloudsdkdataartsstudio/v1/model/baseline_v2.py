# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaselineV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'version': 'int',
        'create_time': 'int',
        'last_update_time': 'int',
        'type': 'str',
        'owner_id': 'str',
        'owner_name': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'project_id': 'str',
        'instance_id': 'str',
        'workspace_id': 'str',
        'sla_task_ids': 'list[str]',
        'priority': 'int',
        'sla_min': 'int',
        'buffer': 'int',
        'sla_hour': 'int',
        'exp_min': 'int',
        'exp_hour': 'int',
        'hour_exp_detail': 'str',
        'hour_sla_detail': 'str',
        'enable': 'bool',
        'alarm_enable': 'bool',
        'baseline_alarm_enable': 'bool',
        'smn_topics': 'list[SmnTopic]',
        'event_alarm': 'list[str]',
        'event_smn_topics': 'list[SmnTopic]',
        'sign_enable': 'bool',
        'period': 'list[PeriodSlaTimeV2]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'version': 'version',
        'create_time': 'create_time',
        'last_update_time': 'last_update_time',
        'type': 'type',
        'owner_id': 'owner_id',
        'owner_name': 'owner_name',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'project_id': 'project_id',
        'instance_id': 'instance_id',
        'workspace_id': 'workspace_id',
        'sla_task_ids': 'sla_task_ids',
        'priority': 'priority',
        'sla_min': 'sla_min',
        'buffer': 'buffer',
        'sla_hour': 'sla_hour',
        'exp_min': 'exp_min',
        'exp_hour': 'exp_hour',
        'hour_exp_detail': 'hour_exp_detail',
        'hour_sla_detail': 'hour_sla_detail',
        'enable': 'enable',
        'alarm_enable': 'alarm_enable',
        'baseline_alarm_enable': 'baseline_alarm_enable',
        'smn_topics': 'smn_topics',
        'event_alarm': 'event_alarm',
        'event_smn_topics': 'event_smn_topics',
        'sign_enable': 'sign_enable',
        'period': 'period'
    }

    def __init__(self, id=None, name=None, version=None, create_time=None, last_update_time=None, type=None, owner_id=None, owner_name=None, domain_id=None, domain_name=None, project_id=None, instance_id=None, workspace_id=None, sla_task_ids=None, priority=None, sla_min=None, buffer=None, sla_hour=None, exp_min=None, exp_hour=None, hour_exp_detail=None, hour_sla_detail=None, enable=None, alarm_enable=None, baseline_alarm_enable=None, smn_topics=None, event_alarm=None, event_smn_topics=None, sign_enable=None, period=None):
        r"""BaselineV2

        The model defined in huaweicloud sdk

        :param id: 基线任务ID。
        :type id: str
        :param name: 基线任务名称。
        :type name: str
        :param version: 版本号。
        :type version: int
        :param create_time: 创建时间戳，单位毫秒。
        :type create_time: int
        :param last_update_time: 最后更新时间戳，单位毫秒。
        :type last_update_time: int
        :param type: 基线任务类型。
        :type type: str
        :param owner_id: 责任人用户ID。
        :type owner_id: str
        :param owner_name: 责任人用户名称。
        :type owner_name: str
        :param domain_id: 责任人租户ID。
        :type domain_id: str
        :param domain_name: 责任人租户名称。
        :type domain_name: str
        :param project_id: 项目ID。
        :type project_id: str
        :param instance_id: DataArts Studio实例ID。
        :type instance_id: str
        :param workspace_id: 工作空间ID。
        :type workspace_id: str
        :param sla_task_ids: 保障作业ID列表。
        :type sla_task_ids: list[str]
        :param priority: 优先级。
        :type priority: int
        :param sla_min: 天基线承诺分钟。
        :type sla_min: int
        :param buffer: 预警余量。
        :type buffer: int
        :param sla_hour: 天基线承诺小时。
        :type sla_hour: int
        :param exp_min: 天基线预警分钟。
        :type exp_min: int
        :param exp_hour: 天基线预警小时。
        :type exp_hour: int
        :param hour_exp_detail: 小时基线的预警时间配置（JSON格式），key为周期号，value为hh:mm格式。hh的取值范围为[0,47]，mm的取值范围为[0,59]。
        :type hour_exp_detail: str
        :param hour_sla_detail: 小时基线的承诺时间配置（JSON格式），key为周期号，value为hh:mm格式。hh的取值范围为[0,47]，mm的取值范围为[0,59]。
        :type hour_sla_detail: str
        :param enable: 是否生效。
        :type enable: bool
        :param alarm_enable: 报警是否打开。
        :type alarm_enable: bool
        :param baseline_alarm_enable: 基线报警是否打开。
        :type baseline_alarm_enable: bool
        :param smn_topics: SMN主题列表。
        :type smn_topics: list[:class:`huaweicloudsdkdataartsstudio.v1.SmnTopic`]
        :param event_alarm: 事件告警开启类型。
        :type event_alarm: list[str]
        :param event_smn_topics: 事件告警SMN主题列表。
        :type event_smn_topics: list[:class:`huaweicloudsdkdataartsstudio.v1.SmnTopic`]
        :param sign_enable: 基线签署是否打开。
        :type sign_enable: bool
        :param period: 承诺时间周期列表，小时基线时生效。
        :type period: list[:class:`huaweicloudsdkdataartsstudio.v1.PeriodSlaTimeV2`]
        """
        
        

        self._id = None
        self._name = None
        self._version = None
        self._create_time = None
        self._last_update_time = None
        self._type = None
        self._owner_id = None
        self._owner_name = None
        self._domain_id = None
        self._domain_name = None
        self._project_id = None
        self._instance_id = None
        self._workspace_id = None
        self._sla_task_ids = None
        self._priority = None
        self._sla_min = None
        self._buffer = None
        self._sla_hour = None
        self._exp_min = None
        self._exp_hour = None
        self._hour_exp_detail = None
        self._hour_sla_detail = None
        self._enable = None
        self._alarm_enable = None
        self._baseline_alarm_enable = None
        self._smn_topics = None
        self._event_alarm = None
        self._event_smn_topics = None
        self._sign_enable = None
        self._period = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if create_time is not None:
            self.create_time = create_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if type is not None:
            self.type = type
        if owner_id is not None:
            self.owner_id = owner_id
        if owner_name is not None:
            self.owner_name = owner_name
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if project_id is not None:
            self.project_id = project_id
        if instance_id is not None:
            self.instance_id = instance_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if sla_task_ids is not None:
            self.sla_task_ids = sla_task_ids
        if priority is not None:
            self.priority = priority
        if sla_min is not None:
            self.sla_min = sla_min
        if buffer is not None:
            self.buffer = buffer
        if sla_hour is not None:
            self.sla_hour = sla_hour
        if exp_min is not None:
            self.exp_min = exp_min
        if exp_hour is not None:
            self.exp_hour = exp_hour
        if hour_exp_detail is not None:
            self.hour_exp_detail = hour_exp_detail
        if hour_sla_detail is not None:
            self.hour_sla_detail = hour_sla_detail
        if enable is not None:
            self.enable = enable
        if alarm_enable is not None:
            self.alarm_enable = alarm_enable
        if baseline_alarm_enable is not None:
            self.baseline_alarm_enable = baseline_alarm_enable
        if smn_topics is not None:
            self.smn_topics = smn_topics
        if event_alarm is not None:
            self.event_alarm = event_alarm
        if event_smn_topics is not None:
            self.event_smn_topics = event_smn_topics
        if sign_enable is not None:
            self.sign_enable = sign_enable
        if period is not None:
            self.period = period

    @property
    def id(self):
        r"""Gets the id of this BaselineV2.

        基线任务ID。

        :return: The id of this BaselineV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BaselineV2.

        基线任务ID。

        :param id: The id of this BaselineV2.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BaselineV2.

        基线任务名称。

        :return: The name of this BaselineV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BaselineV2.

        基线任务名称。

        :param name: The name of this BaselineV2.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this BaselineV2.

        版本号。

        :return: The version of this BaselineV2.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this BaselineV2.

        版本号。

        :param version: The version of this BaselineV2.
        :type version: int
        """
        self._version = version

    @property
    def create_time(self):
        r"""Gets the create_time of this BaselineV2.

        创建时间戳，单位毫秒。

        :return: The create_time of this BaselineV2.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this BaselineV2.

        创建时间戳，单位毫秒。

        :param create_time: The create_time of this BaselineV2.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this BaselineV2.

        最后更新时间戳，单位毫秒。

        :return: The last_update_time of this BaselineV2.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this BaselineV2.

        最后更新时间戳，单位毫秒。

        :param last_update_time: The last_update_time of this BaselineV2.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

    @property
    def type(self):
        r"""Gets the type of this BaselineV2.

        基线任务类型。

        :return: The type of this BaselineV2.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BaselineV2.

        基线任务类型。

        :param type: The type of this BaselineV2.
        :type type: str
        """
        self._type = type

    @property
    def owner_id(self):
        r"""Gets the owner_id of this BaselineV2.

        责任人用户ID。

        :return: The owner_id of this BaselineV2.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this BaselineV2.

        责任人用户ID。

        :param owner_id: The owner_id of this BaselineV2.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def owner_name(self):
        r"""Gets the owner_name of this BaselineV2.

        责任人用户名称。

        :return: The owner_name of this BaselineV2.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this BaselineV2.

        责任人用户名称。

        :param owner_name: The owner_name of this BaselineV2.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this BaselineV2.

        责任人租户ID。

        :return: The domain_id of this BaselineV2.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this BaselineV2.

        责任人租户ID。

        :param domain_id: The domain_id of this BaselineV2.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this BaselineV2.

        责任人租户名称。

        :return: The domain_name of this BaselineV2.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this BaselineV2.

        责任人租户名称。

        :param domain_name: The domain_name of this BaselineV2.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def project_id(self):
        r"""Gets the project_id of this BaselineV2.

        项目ID。

        :return: The project_id of this BaselineV2.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BaselineV2.

        项目ID。

        :param project_id: The project_id of this BaselineV2.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BaselineV2.

        DataArts Studio实例ID。

        :return: The instance_id of this BaselineV2.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BaselineV2.

        DataArts Studio实例ID。

        :param instance_id: The instance_id of this BaselineV2.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this BaselineV2.

        工作空间ID。

        :return: The workspace_id of this BaselineV2.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this BaselineV2.

        工作空间ID。

        :param workspace_id: The workspace_id of this BaselineV2.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def sla_task_ids(self):
        r"""Gets the sla_task_ids of this BaselineV2.

        保障作业ID列表。

        :return: The sla_task_ids of this BaselineV2.
        :rtype: list[str]
        """
        return self._sla_task_ids

    @sla_task_ids.setter
    def sla_task_ids(self, sla_task_ids):
        r"""Sets the sla_task_ids of this BaselineV2.

        保障作业ID列表。

        :param sla_task_ids: The sla_task_ids of this BaselineV2.
        :type sla_task_ids: list[str]
        """
        self._sla_task_ids = sla_task_ids

    @property
    def priority(self):
        r"""Gets the priority of this BaselineV2.

        优先级。

        :return: The priority of this BaselineV2.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this BaselineV2.

        优先级。

        :param priority: The priority of this BaselineV2.
        :type priority: int
        """
        self._priority = priority

    @property
    def sla_min(self):
        r"""Gets the sla_min of this BaselineV2.

        天基线承诺分钟。

        :return: The sla_min of this BaselineV2.
        :rtype: int
        """
        return self._sla_min

    @sla_min.setter
    def sla_min(self, sla_min):
        r"""Sets the sla_min of this BaselineV2.

        天基线承诺分钟。

        :param sla_min: The sla_min of this BaselineV2.
        :type sla_min: int
        """
        self._sla_min = sla_min

    @property
    def buffer(self):
        r"""Gets the buffer of this BaselineV2.

        预警余量。

        :return: The buffer of this BaselineV2.
        :rtype: int
        """
        return self._buffer

    @buffer.setter
    def buffer(self, buffer):
        r"""Sets the buffer of this BaselineV2.

        预警余量。

        :param buffer: The buffer of this BaselineV2.
        :type buffer: int
        """
        self._buffer = buffer

    @property
    def sla_hour(self):
        r"""Gets the sla_hour of this BaselineV2.

        天基线承诺小时。

        :return: The sla_hour of this BaselineV2.
        :rtype: int
        """
        return self._sla_hour

    @sla_hour.setter
    def sla_hour(self, sla_hour):
        r"""Sets the sla_hour of this BaselineV2.

        天基线承诺小时。

        :param sla_hour: The sla_hour of this BaselineV2.
        :type sla_hour: int
        """
        self._sla_hour = sla_hour

    @property
    def exp_min(self):
        r"""Gets the exp_min of this BaselineV2.

        天基线预警分钟。

        :return: The exp_min of this BaselineV2.
        :rtype: int
        """
        return self._exp_min

    @exp_min.setter
    def exp_min(self, exp_min):
        r"""Sets the exp_min of this BaselineV2.

        天基线预警分钟。

        :param exp_min: The exp_min of this BaselineV2.
        :type exp_min: int
        """
        self._exp_min = exp_min

    @property
    def exp_hour(self):
        r"""Gets the exp_hour of this BaselineV2.

        天基线预警小时。

        :return: The exp_hour of this BaselineV2.
        :rtype: int
        """
        return self._exp_hour

    @exp_hour.setter
    def exp_hour(self, exp_hour):
        r"""Sets the exp_hour of this BaselineV2.

        天基线预警小时。

        :param exp_hour: The exp_hour of this BaselineV2.
        :type exp_hour: int
        """
        self._exp_hour = exp_hour

    @property
    def hour_exp_detail(self):
        r"""Gets the hour_exp_detail of this BaselineV2.

        小时基线的预警时间配置（JSON格式），key为周期号，value为hh:mm格式。hh的取值范围为[0,47]，mm的取值范围为[0,59]。

        :return: The hour_exp_detail of this BaselineV2.
        :rtype: str
        """
        return self._hour_exp_detail

    @hour_exp_detail.setter
    def hour_exp_detail(self, hour_exp_detail):
        r"""Sets the hour_exp_detail of this BaselineV2.

        小时基线的预警时间配置（JSON格式），key为周期号，value为hh:mm格式。hh的取值范围为[0,47]，mm的取值范围为[0,59]。

        :param hour_exp_detail: The hour_exp_detail of this BaselineV2.
        :type hour_exp_detail: str
        """
        self._hour_exp_detail = hour_exp_detail

    @property
    def hour_sla_detail(self):
        r"""Gets the hour_sla_detail of this BaselineV2.

        小时基线的承诺时间配置（JSON格式），key为周期号，value为hh:mm格式。hh的取值范围为[0,47]，mm的取值范围为[0,59]。

        :return: The hour_sla_detail of this BaselineV2.
        :rtype: str
        """
        return self._hour_sla_detail

    @hour_sla_detail.setter
    def hour_sla_detail(self, hour_sla_detail):
        r"""Sets the hour_sla_detail of this BaselineV2.

        小时基线的承诺时间配置（JSON格式），key为周期号，value为hh:mm格式。hh的取值范围为[0,47]，mm的取值范围为[0,59]。

        :param hour_sla_detail: The hour_sla_detail of this BaselineV2.
        :type hour_sla_detail: str
        """
        self._hour_sla_detail = hour_sla_detail

    @property
    def enable(self):
        r"""Gets the enable of this BaselineV2.

        是否生效。

        :return: The enable of this BaselineV2.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this BaselineV2.

        是否生效。

        :param enable: The enable of this BaselineV2.
        :type enable: bool
        """
        self._enable = enable

    @property
    def alarm_enable(self):
        r"""Gets the alarm_enable of this BaselineV2.

        报警是否打开。

        :return: The alarm_enable of this BaselineV2.
        :rtype: bool
        """
        return self._alarm_enable

    @alarm_enable.setter
    def alarm_enable(self, alarm_enable):
        r"""Sets the alarm_enable of this BaselineV2.

        报警是否打开。

        :param alarm_enable: The alarm_enable of this BaselineV2.
        :type alarm_enable: bool
        """
        self._alarm_enable = alarm_enable

    @property
    def baseline_alarm_enable(self):
        r"""Gets the baseline_alarm_enable of this BaselineV2.

        基线报警是否打开。

        :return: The baseline_alarm_enable of this BaselineV2.
        :rtype: bool
        """
        return self._baseline_alarm_enable

    @baseline_alarm_enable.setter
    def baseline_alarm_enable(self, baseline_alarm_enable):
        r"""Sets the baseline_alarm_enable of this BaselineV2.

        基线报警是否打开。

        :param baseline_alarm_enable: The baseline_alarm_enable of this BaselineV2.
        :type baseline_alarm_enable: bool
        """
        self._baseline_alarm_enable = baseline_alarm_enable

    @property
    def smn_topics(self):
        r"""Gets the smn_topics of this BaselineV2.

        SMN主题列表。

        :return: The smn_topics of this BaselineV2.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SmnTopic`]
        """
        return self._smn_topics

    @smn_topics.setter
    def smn_topics(self, smn_topics):
        r"""Sets the smn_topics of this BaselineV2.

        SMN主题列表。

        :param smn_topics: The smn_topics of this BaselineV2.
        :type smn_topics: list[:class:`huaweicloudsdkdataartsstudio.v1.SmnTopic`]
        """
        self._smn_topics = smn_topics

    @property
    def event_alarm(self):
        r"""Gets the event_alarm of this BaselineV2.

        事件告警开启类型。

        :return: The event_alarm of this BaselineV2.
        :rtype: list[str]
        """
        return self._event_alarm

    @event_alarm.setter
    def event_alarm(self, event_alarm):
        r"""Sets the event_alarm of this BaselineV2.

        事件告警开启类型。

        :param event_alarm: The event_alarm of this BaselineV2.
        :type event_alarm: list[str]
        """
        self._event_alarm = event_alarm

    @property
    def event_smn_topics(self):
        r"""Gets the event_smn_topics of this BaselineV2.

        事件告警SMN主题列表。

        :return: The event_smn_topics of this BaselineV2.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SmnTopic`]
        """
        return self._event_smn_topics

    @event_smn_topics.setter
    def event_smn_topics(self, event_smn_topics):
        r"""Sets the event_smn_topics of this BaselineV2.

        事件告警SMN主题列表。

        :param event_smn_topics: The event_smn_topics of this BaselineV2.
        :type event_smn_topics: list[:class:`huaweicloudsdkdataartsstudio.v1.SmnTopic`]
        """
        self._event_smn_topics = event_smn_topics

    @property
    def sign_enable(self):
        r"""Gets the sign_enable of this BaselineV2.

        基线签署是否打开。

        :return: The sign_enable of this BaselineV2.
        :rtype: bool
        """
        return self._sign_enable

    @sign_enable.setter
    def sign_enable(self, sign_enable):
        r"""Sets the sign_enable of this BaselineV2.

        基线签署是否打开。

        :param sign_enable: The sign_enable of this BaselineV2.
        :type sign_enable: bool
        """
        self._sign_enable = sign_enable

    @property
    def period(self):
        r"""Gets the period of this BaselineV2.

        承诺时间周期列表，小时基线时生效。

        :return: The period of this BaselineV2.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.PeriodSlaTimeV2`]
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this BaselineV2.

        承诺时间周期列表，小时基线时生效。

        :param period: The period of this BaselineV2.
        :type period: list[:class:`huaweicloudsdkdataartsstudio.v1.PeriodSlaTimeV2`]
        """
        self._period = period

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
        if not isinstance(other, BaselineV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
