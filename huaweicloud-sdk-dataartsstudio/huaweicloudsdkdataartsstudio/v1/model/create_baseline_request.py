# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBaselineRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'name': 'str',
        'owner_name': 'str',
        'type': 'str',
        'sla_task_ids': 'list[str]',
        'priority': 'int',
        'buffer': 'int',
        'enable': 'bool',
        'alarm_enable': 'bool',
        'sign_enable': 'bool',
        'sla_hour': 'str',
        'sla_min': 'str',
        'baseline_alarm_enable': 'bool',
        'smn_topics': 'list[SmnTopicRequest]',
        'event_smn_topics': 'list[SmnTopicRequest]',
        'event_alarm': 'list[str]',
        'period': 'list[PeriodObject]'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'name': 'name',
        'owner_name': 'owner_name',
        'type': 'type',
        'sla_task_ids': 'sla_task_ids',
        'priority': 'priority',
        'buffer': 'buffer',
        'enable': 'enable',
        'alarm_enable': 'alarm_enable',
        'sign_enable': 'sign_enable',
        'sla_hour': 'sla_hour',
        'sla_min': 'sla_min',
        'baseline_alarm_enable': 'baseline_alarm_enable',
        'smn_topics': 'smn_topics',
        'event_smn_topics': 'event_smn_topics',
        'event_alarm': 'event_alarm',
        'period': 'period'
    }

    def __init__(self, workspace_id=None, name=None, owner_name=None, type=None, sla_task_ids=None, priority=None, buffer=None, enable=None, alarm_enable=None, sign_enable=None, sla_hour=None, sla_min=None, baseline_alarm_enable=None, smn_topics=None, event_smn_topics=None, event_alarm=None, period=None):
        r"""CreateBaselineRequest

        The model defined in huaweicloud sdk

        :param workspace_id: 工作空间ID。
        :type workspace_id: str
        :param name: 基线任务名称。只能包含：英文字母、数字、中文、中划线、下划线和点号，且长度不超过128位。
        :type name: str
        :param owner_name: 责任人用户名称。
        :type owner_name: str
        :param type: 基线任务类型。取值为 DAY和HOUR。
        :type type: str
        :param sla_task_ids: 保障作业ID列表。
        :type sla_task_ids: list[str]
        :param priority: 优先级，取值范围是1到5。
        :type priority: int
        :param buffer: 预警余量。单位毫秒，取值范围在0到86400000之间，且必须是整数分钟级别的毫秒。
        :type buffer: int
        :param enable: 是否生效，取值为true或者false。默认为true。
        :type enable: bool
        :param alarm_enable: 报警是否打开，取值为true或者false，默认为true。
        :type alarm_enable: bool
        :param sign_enable: 基线签署是否打开，取值为true或者false。默认为false。
        :type sign_enable: bool
        :param sla_hour: 天基线承诺小时。
        :type sla_hour: str
        :param sla_min: 天基线承诺分钟。
        :type sla_min: str
        :param baseline_alarm_enable: 基线报警是否打开，取值为true或者false。
        :type baseline_alarm_enable: bool
        :param smn_topics: SMN主题列表。
        :type smn_topics: list[:class:`huaweicloudsdkdataartsstudio.v1.SmnTopicRequest`]
        :param event_smn_topics: 事件报警信息。
        :type event_smn_topics: list[:class:`huaweicloudsdkdataartsstudio.v1.SmnTopicRequest`]
        :param event_alarm: 事件告警开启类型，取值为ERROR：出错，SLOW_DOWN：变慢。
        :type event_alarm: list[str]
        :param period: 当type取值为HOUR时，该值需要填写。
        :type period: list[:class:`huaweicloudsdkdataartsstudio.v1.PeriodObject`]
        """
        
        

        self._workspace_id = None
        self._name = None
        self._owner_name = None
        self._type = None
        self._sla_task_ids = None
        self._priority = None
        self._buffer = None
        self._enable = None
        self._alarm_enable = None
        self._sign_enable = None
        self._sla_hour = None
        self._sla_min = None
        self._baseline_alarm_enable = None
        self._smn_topics = None
        self._event_smn_topics = None
        self._event_alarm = None
        self._period = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.name = name
        self.owner_name = owner_name
        self.type = type
        self.sla_task_ids = sla_task_ids
        self.priority = priority
        self.buffer = buffer
        self.enable = enable
        self.alarm_enable = alarm_enable
        self.sign_enable = sign_enable
        self.sla_hour = sla_hour
        self.sla_min = sla_min
        self.baseline_alarm_enable = baseline_alarm_enable
        if smn_topics is not None:
            self.smn_topics = smn_topics
        if event_smn_topics is not None:
            self.event_smn_topics = event_smn_topics
        if event_alarm is not None:
            self.event_alarm = event_alarm
        if period is not None:
            self.period = period

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CreateBaselineRequest.

        工作空间ID。

        :return: The workspace_id of this CreateBaselineRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CreateBaselineRequest.

        工作空间ID。

        :param workspace_id: The workspace_id of this CreateBaselineRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def name(self):
        r"""Gets the name of this CreateBaselineRequest.

        基线任务名称。只能包含：英文字母、数字、中文、中划线、下划线和点号，且长度不超过128位。

        :return: The name of this CreateBaselineRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateBaselineRequest.

        基线任务名称。只能包含：英文字母、数字、中文、中划线、下划线和点号，且长度不超过128位。

        :param name: The name of this CreateBaselineRequest.
        :type name: str
        """
        self._name = name

    @property
    def owner_name(self):
        r"""Gets the owner_name of this CreateBaselineRequest.

        责任人用户名称。

        :return: The owner_name of this CreateBaselineRequest.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this CreateBaselineRequest.

        责任人用户名称。

        :param owner_name: The owner_name of this CreateBaselineRequest.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def type(self):
        r"""Gets the type of this CreateBaselineRequest.

        基线任务类型。取值为 DAY和HOUR。

        :return: The type of this CreateBaselineRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateBaselineRequest.

        基线任务类型。取值为 DAY和HOUR。

        :param type: The type of this CreateBaselineRequest.
        :type type: str
        """
        self._type = type

    @property
    def sla_task_ids(self):
        r"""Gets the sla_task_ids of this CreateBaselineRequest.

        保障作业ID列表。

        :return: The sla_task_ids of this CreateBaselineRequest.
        :rtype: list[str]
        """
        return self._sla_task_ids

    @sla_task_ids.setter
    def sla_task_ids(self, sla_task_ids):
        r"""Sets the sla_task_ids of this CreateBaselineRequest.

        保障作业ID列表。

        :param sla_task_ids: The sla_task_ids of this CreateBaselineRequest.
        :type sla_task_ids: list[str]
        """
        self._sla_task_ids = sla_task_ids

    @property
    def priority(self):
        r"""Gets the priority of this CreateBaselineRequest.

        优先级，取值范围是1到5。

        :return: The priority of this CreateBaselineRequest.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this CreateBaselineRequest.

        优先级，取值范围是1到5。

        :param priority: The priority of this CreateBaselineRequest.
        :type priority: int
        """
        self._priority = priority

    @property
    def buffer(self):
        r"""Gets the buffer of this CreateBaselineRequest.

        预警余量。单位毫秒，取值范围在0到86400000之间，且必须是整数分钟级别的毫秒。

        :return: The buffer of this CreateBaselineRequest.
        :rtype: int
        """
        return self._buffer

    @buffer.setter
    def buffer(self, buffer):
        r"""Sets the buffer of this CreateBaselineRequest.

        预警余量。单位毫秒，取值范围在0到86400000之间，且必须是整数分钟级别的毫秒。

        :param buffer: The buffer of this CreateBaselineRequest.
        :type buffer: int
        """
        self._buffer = buffer

    @property
    def enable(self):
        r"""Gets the enable of this CreateBaselineRequest.

        是否生效，取值为true或者false。默认为true。

        :return: The enable of this CreateBaselineRequest.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this CreateBaselineRequest.

        是否生效，取值为true或者false。默认为true。

        :param enable: The enable of this CreateBaselineRequest.
        :type enable: bool
        """
        self._enable = enable

    @property
    def alarm_enable(self):
        r"""Gets the alarm_enable of this CreateBaselineRequest.

        报警是否打开，取值为true或者false，默认为true。

        :return: The alarm_enable of this CreateBaselineRequest.
        :rtype: bool
        """
        return self._alarm_enable

    @alarm_enable.setter
    def alarm_enable(self, alarm_enable):
        r"""Sets the alarm_enable of this CreateBaselineRequest.

        报警是否打开，取值为true或者false，默认为true。

        :param alarm_enable: The alarm_enable of this CreateBaselineRequest.
        :type alarm_enable: bool
        """
        self._alarm_enable = alarm_enable

    @property
    def sign_enable(self):
        r"""Gets the sign_enable of this CreateBaselineRequest.

        基线签署是否打开，取值为true或者false。默认为false。

        :return: The sign_enable of this CreateBaselineRequest.
        :rtype: bool
        """
        return self._sign_enable

    @sign_enable.setter
    def sign_enable(self, sign_enable):
        r"""Sets the sign_enable of this CreateBaselineRequest.

        基线签署是否打开，取值为true或者false。默认为false。

        :param sign_enable: The sign_enable of this CreateBaselineRequest.
        :type sign_enable: bool
        """
        self._sign_enable = sign_enable

    @property
    def sla_hour(self):
        r"""Gets the sla_hour of this CreateBaselineRequest.

        天基线承诺小时。

        :return: The sla_hour of this CreateBaselineRequest.
        :rtype: str
        """
        return self._sla_hour

    @sla_hour.setter
    def sla_hour(self, sla_hour):
        r"""Sets the sla_hour of this CreateBaselineRequest.

        天基线承诺小时。

        :param sla_hour: The sla_hour of this CreateBaselineRequest.
        :type sla_hour: str
        """
        self._sla_hour = sla_hour

    @property
    def sla_min(self):
        r"""Gets the sla_min of this CreateBaselineRequest.

        天基线承诺分钟。

        :return: The sla_min of this CreateBaselineRequest.
        :rtype: str
        """
        return self._sla_min

    @sla_min.setter
    def sla_min(self, sla_min):
        r"""Sets the sla_min of this CreateBaselineRequest.

        天基线承诺分钟。

        :param sla_min: The sla_min of this CreateBaselineRequest.
        :type sla_min: str
        """
        self._sla_min = sla_min

    @property
    def baseline_alarm_enable(self):
        r"""Gets the baseline_alarm_enable of this CreateBaselineRequest.

        基线报警是否打开，取值为true或者false。

        :return: The baseline_alarm_enable of this CreateBaselineRequest.
        :rtype: bool
        """
        return self._baseline_alarm_enable

    @baseline_alarm_enable.setter
    def baseline_alarm_enable(self, baseline_alarm_enable):
        r"""Sets the baseline_alarm_enable of this CreateBaselineRequest.

        基线报警是否打开，取值为true或者false。

        :param baseline_alarm_enable: The baseline_alarm_enable of this CreateBaselineRequest.
        :type baseline_alarm_enable: bool
        """
        self._baseline_alarm_enable = baseline_alarm_enable

    @property
    def smn_topics(self):
        r"""Gets the smn_topics of this CreateBaselineRequest.

        SMN主题列表。

        :return: The smn_topics of this CreateBaselineRequest.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SmnTopicRequest`]
        """
        return self._smn_topics

    @smn_topics.setter
    def smn_topics(self, smn_topics):
        r"""Sets the smn_topics of this CreateBaselineRequest.

        SMN主题列表。

        :param smn_topics: The smn_topics of this CreateBaselineRequest.
        :type smn_topics: list[:class:`huaweicloudsdkdataartsstudio.v1.SmnTopicRequest`]
        """
        self._smn_topics = smn_topics

    @property
    def event_smn_topics(self):
        r"""Gets the event_smn_topics of this CreateBaselineRequest.

        事件报警信息。

        :return: The event_smn_topics of this CreateBaselineRequest.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SmnTopicRequest`]
        """
        return self._event_smn_topics

    @event_smn_topics.setter
    def event_smn_topics(self, event_smn_topics):
        r"""Sets the event_smn_topics of this CreateBaselineRequest.

        事件报警信息。

        :param event_smn_topics: The event_smn_topics of this CreateBaselineRequest.
        :type event_smn_topics: list[:class:`huaweicloudsdkdataartsstudio.v1.SmnTopicRequest`]
        """
        self._event_smn_topics = event_smn_topics

    @property
    def event_alarm(self):
        r"""Gets the event_alarm of this CreateBaselineRequest.

        事件告警开启类型，取值为ERROR：出错，SLOW_DOWN：变慢。

        :return: The event_alarm of this CreateBaselineRequest.
        :rtype: list[str]
        """
        return self._event_alarm

    @event_alarm.setter
    def event_alarm(self, event_alarm):
        r"""Sets the event_alarm of this CreateBaselineRequest.

        事件告警开启类型，取值为ERROR：出错，SLOW_DOWN：变慢。

        :param event_alarm: The event_alarm of this CreateBaselineRequest.
        :type event_alarm: list[str]
        """
        self._event_alarm = event_alarm

    @property
    def period(self):
        r"""Gets the period of this CreateBaselineRequest.

        当type取值为HOUR时，该值需要填写。

        :return: The period of this CreateBaselineRequest.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.PeriodObject`]
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this CreateBaselineRequest.

        当type取值为HOUR时，该值需要填写。

        :param period: The period of this CreateBaselineRequest.
        :type period: list[:class:`huaweicloudsdkdataartsstudio.v1.PeriodObject`]
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
        if not isinstance(other, CreateBaselineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
