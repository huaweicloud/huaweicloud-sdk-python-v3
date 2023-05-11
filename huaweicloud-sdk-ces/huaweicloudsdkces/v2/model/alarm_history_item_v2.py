# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmHistoryItemV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_id': 'str',
        'alarm_id': 'str',
        'name': 'str',
        'status': 'str',
        'level': 'int',
        'type': 'AlarmType',
        'action_enabled': 'bool',
        'begin_time': 'datetime',
        'end_time': 'datetime',
        'metric': 'Metric',
        'condition': 'AlarmCondition',
        'additional_info': 'AdditionalInfo',
        'alarm_actions': 'list[Notification]',
        'ok_actions': 'list[Notification]',
        'data_points': 'list[DataPointInfo]'
    }

    attribute_map = {
        'record_id': 'record_id',
        'alarm_id': 'alarm_id',
        'name': 'name',
        'status': 'status',
        'level': 'level',
        'type': 'type',
        'action_enabled': 'action_enabled',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'metric': 'metric',
        'condition': 'condition',
        'additional_info': 'additional_info',
        'alarm_actions': 'alarm_actions',
        'ok_actions': 'ok_actions',
        'data_points': 'data_points'
    }

    def __init__(self, record_id=None, alarm_id=None, name=None, status=None, level=None, type=None, action_enabled=None, begin_time=None, end_time=None, metric=None, condition=None, additional_info=None, alarm_actions=None, ok_actions=None, data_points=None):
        """AlarmHistoryItemV2

        The model defined in huaweicloud sdk

        :param record_id: 告警记录ID
        :type record_id: str
        :param alarm_id: 告警规则的ID，如：al1603131199286dzxpqK3Ez。
        :type alarm_id: str
        :param name: 告警规则的名称，如：alarm-test01。
        :type name: str
        :param status: 告警记录的状态，取值为ok，alarm，invalid； ok为正常，alarm为告警，invalid为已失效。
        :type status: str
        :param level: 告警记录的告警级别，值为1,2,3,4；1为紧急，2为重要，3为次要，4为提示。
        :type level: int
        :param type: 
        :type type: :class:`huaweicloudsdkces.v2.AlarmType`
        :param action_enabled: 是否发送通知，值为true或者false。
        :type action_enabled: bool
        :param begin_time: 产生时间,UTC时间
        :type begin_time: datetime
        :param end_time: 结束时间，UTC时间
        :type end_time: datetime
        :param metric: 
        :type metric: :class:`huaweicloudsdkces.v2.Metric`
        :param condition: 
        :type condition: :class:`huaweicloudsdkces.v2.AlarmCondition`
        :param additional_info: 
        :type additional_info: :class:`huaweicloudsdkces.v2.AdditionalInfo`
        :param alarm_actions: 告警触发的动作。  结构如下：  {  \&quot;type\&quot;: \&quot;notification\&quot;, \&quot;notification_list\&quot;: [\&quot;urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\&quot;]  }  type取值： notification：通知。 autoscaling：弹性伸缩。 notification_list：告警状态发生变化时，被通知对象的列表。
        :type alarm_actions: list[:class:`huaweicloudsdkces.v2.Notification`]
        :param ok_actions: 告警恢复触发的动作。  结构如下：  {  \&quot;type\&quot;: \&quot;notification\&quot;, \&quot;notification_list\&quot;: [\&quot;urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\&quot;]  } type取值：  notification：通知。  notification_list：告警状态发生变化时，被通知对象的列表。
        :type ok_actions: list[:class:`huaweicloudsdkces.v2.Notification`]
        :param data_points: 计算出该条告警记录的资源监控数据上报时间和监控数值。
        :type data_points: list[:class:`huaweicloudsdkces.v2.DataPointInfo`]
        """
        
        

        self._record_id = None
        self._alarm_id = None
        self._name = None
        self._status = None
        self._level = None
        self._type = None
        self._action_enabled = None
        self._begin_time = None
        self._end_time = None
        self._metric = None
        self._condition = None
        self._additional_info = None
        self._alarm_actions = None
        self._ok_actions = None
        self._data_points = None
        self.discriminator = None

        if record_id is not None:
            self.record_id = record_id
        if alarm_id is not None:
            self.alarm_id = alarm_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if level is not None:
            self.level = level
        if type is not None:
            self.type = type
        if action_enabled is not None:
            self.action_enabled = action_enabled
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if metric is not None:
            self.metric = metric
        if condition is not None:
            self.condition = condition
        if additional_info is not None:
            self.additional_info = additional_info
        if alarm_actions is not None:
            self.alarm_actions = alarm_actions
        if ok_actions is not None:
            self.ok_actions = ok_actions
        if data_points is not None:
            self.data_points = data_points

    @property
    def record_id(self):
        """Gets the record_id of this AlarmHistoryItemV2.

        告警记录ID

        :return: The record_id of this AlarmHistoryItemV2.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this AlarmHistoryItemV2.

        告警记录ID

        :param record_id: The record_id of this AlarmHistoryItemV2.
        :type record_id: str
        """
        self._record_id = record_id

    @property
    def alarm_id(self):
        """Gets the alarm_id of this AlarmHistoryItemV2.

        告警规则的ID，如：al1603131199286dzxpqK3Ez。

        :return: The alarm_id of this AlarmHistoryItemV2.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this AlarmHistoryItemV2.

        告警规则的ID，如：al1603131199286dzxpqK3Ez。

        :param alarm_id: The alarm_id of this AlarmHistoryItemV2.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def name(self):
        """Gets the name of this AlarmHistoryItemV2.

        告警规则的名称，如：alarm-test01。

        :return: The name of this AlarmHistoryItemV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlarmHistoryItemV2.

        告警规则的名称，如：alarm-test01。

        :param name: The name of this AlarmHistoryItemV2.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this AlarmHistoryItemV2.

        告警记录的状态，取值为ok，alarm，invalid； ok为正常，alarm为告警，invalid为已失效。

        :return: The status of this AlarmHistoryItemV2.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AlarmHistoryItemV2.

        告警记录的状态，取值为ok，alarm，invalid； ok为正常，alarm为告警，invalid为已失效。

        :param status: The status of this AlarmHistoryItemV2.
        :type status: str
        """
        self._status = status

    @property
    def level(self):
        """Gets the level of this AlarmHistoryItemV2.

        告警记录的告警级别，值为1,2,3,4；1为紧急，2为重要，3为次要，4为提示。

        :return: The level of this AlarmHistoryItemV2.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this AlarmHistoryItemV2.

        告警记录的告警级别，值为1,2,3,4；1为紧急，2为重要，3为次要，4为提示。

        :param level: The level of this AlarmHistoryItemV2.
        :type level: int
        """
        self._level = level

    @property
    def type(self):
        """Gets the type of this AlarmHistoryItemV2.

        :return: The type of this AlarmHistoryItemV2.
        :rtype: :class:`huaweicloudsdkces.v2.AlarmType`
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AlarmHistoryItemV2.

        :param type: The type of this AlarmHistoryItemV2.
        :type type: :class:`huaweicloudsdkces.v2.AlarmType`
        """
        self._type = type

    @property
    def action_enabled(self):
        """Gets the action_enabled of this AlarmHistoryItemV2.

        是否发送通知，值为true或者false。

        :return: The action_enabled of this AlarmHistoryItemV2.
        :rtype: bool
        """
        return self._action_enabled

    @action_enabled.setter
    def action_enabled(self, action_enabled):
        """Sets the action_enabled of this AlarmHistoryItemV2.

        是否发送通知，值为true或者false。

        :param action_enabled: The action_enabled of this AlarmHistoryItemV2.
        :type action_enabled: bool
        """
        self._action_enabled = action_enabled

    @property
    def begin_time(self):
        """Gets the begin_time of this AlarmHistoryItemV2.

        产生时间,UTC时间

        :return: The begin_time of this AlarmHistoryItemV2.
        :rtype: datetime
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this AlarmHistoryItemV2.

        产生时间,UTC时间

        :param begin_time: The begin_time of this AlarmHistoryItemV2.
        :type begin_time: datetime
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this AlarmHistoryItemV2.

        结束时间，UTC时间

        :return: The end_time of this AlarmHistoryItemV2.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AlarmHistoryItemV2.

        结束时间，UTC时间

        :param end_time: The end_time of this AlarmHistoryItemV2.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def metric(self):
        """Gets the metric of this AlarmHistoryItemV2.

        :return: The metric of this AlarmHistoryItemV2.
        :rtype: :class:`huaweicloudsdkces.v2.Metric`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this AlarmHistoryItemV2.

        :param metric: The metric of this AlarmHistoryItemV2.
        :type metric: :class:`huaweicloudsdkces.v2.Metric`
        """
        self._metric = metric

    @property
    def condition(self):
        """Gets the condition of this AlarmHistoryItemV2.

        :return: The condition of this AlarmHistoryItemV2.
        :rtype: :class:`huaweicloudsdkces.v2.AlarmCondition`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this AlarmHistoryItemV2.

        :param condition: The condition of this AlarmHistoryItemV2.
        :type condition: :class:`huaweicloudsdkces.v2.AlarmCondition`
        """
        self._condition = condition

    @property
    def additional_info(self):
        """Gets the additional_info of this AlarmHistoryItemV2.

        :return: The additional_info of this AlarmHistoryItemV2.
        :rtype: :class:`huaweicloudsdkces.v2.AdditionalInfo`
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this AlarmHistoryItemV2.

        :param additional_info: The additional_info of this AlarmHistoryItemV2.
        :type additional_info: :class:`huaweicloudsdkces.v2.AdditionalInfo`
        """
        self._additional_info = additional_info

    @property
    def alarm_actions(self):
        """Gets the alarm_actions of this AlarmHistoryItemV2.

        告警触发的动作。  结构如下：  {  \"type\": \"notification\", \"notification_list\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  }  type取值： notification：通知。 autoscaling：弹性伸缩。 notification_list：告警状态发生变化时，被通知对象的列表。

        :return: The alarm_actions of this AlarmHistoryItemV2.
        :rtype: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        return self._alarm_actions

    @alarm_actions.setter
    def alarm_actions(self, alarm_actions):
        """Sets the alarm_actions of this AlarmHistoryItemV2.

        告警触发的动作。  结构如下：  {  \"type\": \"notification\", \"notification_list\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  }  type取值： notification：通知。 autoscaling：弹性伸缩。 notification_list：告警状态发生变化时，被通知对象的列表。

        :param alarm_actions: The alarm_actions of this AlarmHistoryItemV2.
        :type alarm_actions: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        self._alarm_actions = alarm_actions

    @property
    def ok_actions(self):
        """Gets the ok_actions of this AlarmHistoryItemV2.

        告警恢复触发的动作。  结构如下：  {  \"type\": \"notification\", \"notification_list\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  } type取值：  notification：通知。  notification_list：告警状态发生变化时，被通知对象的列表。

        :return: The ok_actions of this AlarmHistoryItemV2.
        :rtype: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        return self._ok_actions

    @ok_actions.setter
    def ok_actions(self, ok_actions):
        """Sets the ok_actions of this AlarmHistoryItemV2.

        告警恢复触发的动作。  结构如下：  {  \"type\": \"notification\", \"notification_list\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  } type取值：  notification：通知。  notification_list：告警状态发生变化时，被通知对象的列表。

        :param ok_actions: The ok_actions of this AlarmHistoryItemV2.
        :type ok_actions: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        self._ok_actions = ok_actions

    @property
    def data_points(self):
        """Gets the data_points of this AlarmHistoryItemV2.

        计算出该条告警记录的资源监控数据上报时间和监控数值。

        :return: The data_points of this AlarmHistoryItemV2.
        :rtype: list[:class:`huaweicloudsdkces.v2.DataPointInfo`]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this AlarmHistoryItemV2.

        计算出该条告警记录的资源监控数据上报时间和监控数值。

        :param data_points: The data_points of this AlarmHistoryItemV2.
        :type data_points: list[:class:`huaweicloudsdkces.v2.DataPointInfo`]
        """
        self._data_points = data_points

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
        if not isinstance(other, AlarmHistoryItemV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
