# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmHistoryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'alarm_id': 'str',
        'alarm_name': 'str',
        'alarm_description': 'str',
        'metric': 'MetricInfo',
        'condition': 'Condition',
        'alarm_level': 'int',
        'alarm_type': 'str',
        'alarm_enabled': 'bool',
        'alarm_action_enabled': 'bool',
        'alarm_actions': 'list[AlarmActions]',
        'ok_actions': 'list[AlarmActions]',
        'insufficientdata_actions': 'list[AlarmActions]',
        'update_time': 'int',
        'enterprise_project_id': 'str',
        'trigger_time': 'int',
        'alarm_status': 'str',
        'datapoints': 'list[DataPointForAlarmHistory]',
        'additional_info': 'AdditionalInfo'
    }

    attribute_map = {
        'alarm_id': 'alarm_id',
        'alarm_name': 'alarm_name',
        'alarm_description': 'alarm_description',
        'metric': 'metric',
        'condition': 'condition',
        'alarm_level': 'alarm_level',
        'alarm_type': 'alarm_type',
        'alarm_enabled': 'alarm_enabled',
        'alarm_action_enabled': 'alarm_action_enabled',
        'alarm_actions': 'alarm_actions',
        'ok_actions': 'ok_actions',
        'insufficientdata_actions': 'insufficientdata_actions',
        'update_time': 'update_time',
        'enterprise_project_id': 'enterprise_project_id',
        'trigger_time': 'trigger_time',
        'alarm_status': 'alarm_status',
        'datapoints': 'datapoints',
        'additional_info': 'additional_info'
    }

    def __init__(self, alarm_id=None, alarm_name=None, alarm_description=None, metric=None, condition=None, alarm_level=None, alarm_type=None, alarm_enabled=None, alarm_action_enabled=None, alarm_actions=None, ok_actions=None, insufficientdata_actions=None, update_time=None, enterprise_project_id=None, trigger_time=None, alarm_status=None, datapoints=None, additional_info=None):
        """AlarmHistoryInfo

        The model defined in huaweicloud sdk

        :param alarm_id: 告警规则的ID，如：al1603131199286dzxpqK3Ez。
        :type alarm_id: str
        :param alarm_name: 告警规则的名称，如：alarm-test01。
        :type alarm_name: str
        :param alarm_description: 告警规则的描述。
        :type alarm_description: str
        :param metric: 
        :type metric: :class:`huaweicloudsdkces.v1.MetricInfo`
        :param condition: 
        :type condition: :class:`huaweicloudsdkces.v1.Condition`
        :param alarm_level: 告警历史的告警级别，值为1,2,3,4；1为紧急，2为重要，3为次要，4为提示。
        :type alarm_level: int
        :param alarm_type: 告警类型； 仅针对事件告警的参数，枚举类型：值为EVENT.SYS或者EVENT.CUSTOM
        :type alarm_type: str
        :param alarm_enabled: 告警规则是否被启用，值为true或者false。
        :type alarm_enabled: bool
        :param alarm_action_enabled: 告警规则的告警触发动作是否被启用，值为true或者false。
        :type alarm_action_enabled: bool
        :param alarm_actions: 告警触发的动作。  结构如下：  {  \&quot;type\&quot;: \&quot;notification\&quot;, \&quot;notificationList\&quot;: [\&quot;urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\&quot;]  }  type取值： notification：通知。 autoscaling：弹性伸缩。 notificationList：告警状态发生变化时，被通知对象的列表。
        :type alarm_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        :param ok_actions: 告警恢复触发的动作。  结构如下：  {  \&quot;type\&quot;: \&quot;notification\&quot;, \&quot;notificationList\&quot;: [\&quot;urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\&quot;]  } type取值：  notification：通知。  notificationList：告警状态发生变化时，被通知对象的列表。
        :type ok_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        :param insufficientdata_actions: 数据不足触发的动作。  结构如下：  {  \&quot;type\&quot;: \&quot;notification\&quot;, \&quot;notificationList\&quot;: [\&quot;urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\&quot;]  }  type取值： 数据不足触发告警通知类型，取值为notification。 notificationList：数据不足触发告警通知时，被通知对象的ID列表。
        :type insufficientdata_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        :param update_time: 告警状态变更的时间，UNIX时间戳，单位毫秒，如：1603131199000。
        :type update_time: int
        :param enterprise_project_id: 企业项目ID。 值为all_granted_eps时，表示所有企业项目；值为0时，表示默认的企业项目default。
        :type enterprise_project_id: str
        :param trigger_time: 计算出该条告警历史的时间，UNIX时间戳，单位毫秒，如：1603131199469。
        :type trigger_time: int
        :param alarm_status: 告警历史的状态，取值为ok，alarm，insufficient_data； ok为正常，alarm为告警，insufficient_data为数据不足。
        :type alarm_status: str
        :param datapoints: 计算出该条告警历史的资源监控数据的一组数据上报时间和监控数值。
        :type datapoints: list[:class:`huaweicloudsdkces.v1.DataPointForAlarmHistory`]
        :param additional_info: 
        :type additional_info: :class:`huaweicloudsdkces.v1.AdditionalInfo`
        """
        
        

        self._alarm_id = None
        self._alarm_name = None
        self._alarm_description = None
        self._metric = None
        self._condition = None
        self._alarm_level = None
        self._alarm_type = None
        self._alarm_enabled = None
        self._alarm_action_enabled = None
        self._alarm_actions = None
        self._ok_actions = None
        self._insufficientdata_actions = None
        self._update_time = None
        self._enterprise_project_id = None
        self._trigger_time = None
        self._alarm_status = None
        self._datapoints = None
        self._additional_info = None
        self.discriminator = None

        if alarm_id is not None:
            self.alarm_id = alarm_id
        if alarm_name is not None:
            self.alarm_name = alarm_name
        if alarm_description is not None:
            self.alarm_description = alarm_description
        if metric is not None:
            self.metric = metric
        if condition is not None:
            self.condition = condition
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if alarm_type is not None:
            self.alarm_type = alarm_type
        if alarm_enabled is not None:
            self.alarm_enabled = alarm_enabled
        if alarm_action_enabled is not None:
            self.alarm_action_enabled = alarm_action_enabled
        if alarm_actions is not None:
            self.alarm_actions = alarm_actions
        if ok_actions is not None:
            self.ok_actions = ok_actions
        if insufficientdata_actions is not None:
            self.insufficientdata_actions = insufficientdata_actions
        if update_time is not None:
            self.update_time = update_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if trigger_time is not None:
            self.trigger_time = trigger_time
        if alarm_status is not None:
            self.alarm_status = alarm_status
        if datapoints is not None:
            self.datapoints = datapoints
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def alarm_id(self):
        """Gets the alarm_id of this AlarmHistoryInfo.

        告警规则的ID，如：al1603131199286dzxpqK3Ez。

        :return: The alarm_id of this AlarmHistoryInfo.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this AlarmHistoryInfo.

        告警规则的ID，如：al1603131199286dzxpqK3Ez。

        :param alarm_id: The alarm_id of this AlarmHistoryInfo.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def alarm_name(self):
        """Gets the alarm_name of this AlarmHistoryInfo.

        告警规则的名称，如：alarm-test01。

        :return: The alarm_name of this AlarmHistoryInfo.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        """Sets the alarm_name of this AlarmHistoryInfo.

        告警规则的名称，如：alarm-test01。

        :param alarm_name: The alarm_name of this AlarmHistoryInfo.
        :type alarm_name: str
        """
        self._alarm_name = alarm_name

    @property
    def alarm_description(self):
        """Gets the alarm_description of this AlarmHistoryInfo.

        告警规则的描述。

        :return: The alarm_description of this AlarmHistoryInfo.
        :rtype: str
        """
        return self._alarm_description

    @alarm_description.setter
    def alarm_description(self, alarm_description):
        """Sets the alarm_description of this AlarmHistoryInfo.

        告警规则的描述。

        :param alarm_description: The alarm_description of this AlarmHistoryInfo.
        :type alarm_description: str
        """
        self._alarm_description = alarm_description

    @property
    def metric(self):
        """Gets the metric of this AlarmHistoryInfo.


        :return: The metric of this AlarmHistoryInfo.
        :rtype: :class:`huaweicloudsdkces.v1.MetricInfo`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this AlarmHistoryInfo.


        :param metric: The metric of this AlarmHistoryInfo.
        :type metric: :class:`huaweicloudsdkces.v1.MetricInfo`
        """
        self._metric = metric

    @property
    def condition(self):
        """Gets the condition of this AlarmHistoryInfo.


        :return: The condition of this AlarmHistoryInfo.
        :rtype: :class:`huaweicloudsdkces.v1.Condition`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this AlarmHistoryInfo.


        :param condition: The condition of this AlarmHistoryInfo.
        :type condition: :class:`huaweicloudsdkces.v1.Condition`
        """
        self._condition = condition

    @property
    def alarm_level(self):
        """Gets the alarm_level of this AlarmHistoryInfo.

        告警历史的告警级别，值为1,2,3,4；1为紧急，2为重要，3为次要，4为提示。

        :return: The alarm_level of this AlarmHistoryInfo.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this AlarmHistoryInfo.

        告警历史的告警级别，值为1,2,3,4；1为紧急，2为重要，3为次要，4为提示。

        :param alarm_level: The alarm_level of this AlarmHistoryInfo.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def alarm_type(self):
        """Gets the alarm_type of this AlarmHistoryInfo.

        告警类型； 仅针对事件告警的参数，枚举类型：值为EVENT.SYS或者EVENT.CUSTOM

        :return: The alarm_type of this AlarmHistoryInfo.
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        """Sets the alarm_type of this AlarmHistoryInfo.

        告警类型； 仅针对事件告警的参数，枚举类型：值为EVENT.SYS或者EVENT.CUSTOM

        :param alarm_type: The alarm_type of this AlarmHistoryInfo.
        :type alarm_type: str
        """
        self._alarm_type = alarm_type

    @property
    def alarm_enabled(self):
        """Gets the alarm_enabled of this AlarmHistoryInfo.

        告警规则是否被启用，值为true或者false。

        :return: The alarm_enabled of this AlarmHistoryInfo.
        :rtype: bool
        """
        return self._alarm_enabled

    @alarm_enabled.setter
    def alarm_enabled(self, alarm_enabled):
        """Sets the alarm_enabled of this AlarmHistoryInfo.

        告警规则是否被启用，值为true或者false。

        :param alarm_enabled: The alarm_enabled of this AlarmHistoryInfo.
        :type alarm_enabled: bool
        """
        self._alarm_enabled = alarm_enabled

    @property
    def alarm_action_enabled(self):
        """Gets the alarm_action_enabled of this AlarmHistoryInfo.

        告警规则的告警触发动作是否被启用，值为true或者false。

        :return: The alarm_action_enabled of this AlarmHistoryInfo.
        :rtype: bool
        """
        return self._alarm_action_enabled

    @alarm_action_enabled.setter
    def alarm_action_enabled(self, alarm_action_enabled):
        """Sets the alarm_action_enabled of this AlarmHistoryInfo.

        告警规则的告警触发动作是否被启用，值为true或者false。

        :param alarm_action_enabled: The alarm_action_enabled of this AlarmHistoryInfo.
        :type alarm_action_enabled: bool
        """
        self._alarm_action_enabled = alarm_action_enabled

    @property
    def alarm_actions(self):
        """Gets the alarm_actions of this AlarmHistoryInfo.

        告警触发的动作。  结构如下：  {  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  }  type取值： notification：通知。 autoscaling：弹性伸缩。 notificationList：告警状态发生变化时，被通知对象的列表。

        :return: The alarm_actions of this AlarmHistoryInfo.
        :rtype: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        return self._alarm_actions

    @alarm_actions.setter
    def alarm_actions(self, alarm_actions):
        """Sets the alarm_actions of this AlarmHistoryInfo.

        告警触发的动作。  结构如下：  {  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  }  type取值： notification：通知。 autoscaling：弹性伸缩。 notificationList：告警状态发生变化时，被通知对象的列表。

        :param alarm_actions: The alarm_actions of this AlarmHistoryInfo.
        :type alarm_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        self._alarm_actions = alarm_actions

    @property
    def ok_actions(self):
        """Gets the ok_actions of this AlarmHistoryInfo.

        告警恢复触发的动作。  结构如下：  {  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  } type取值：  notification：通知。  notificationList：告警状态发生变化时，被通知对象的列表。

        :return: The ok_actions of this AlarmHistoryInfo.
        :rtype: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        return self._ok_actions

    @ok_actions.setter
    def ok_actions(self, ok_actions):
        """Sets the ok_actions of this AlarmHistoryInfo.

        告警恢复触发的动作。  结构如下：  {  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  } type取值：  notification：通知。  notificationList：告警状态发生变化时，被通知对象的列表。

        :param ok_actions: The ok_actions of this AlarmHistoryInfo.
        :type ok_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        self._ok_actions = ok_actions

    @property
    def insufficientdata_actions(self):
        """Gets the insufficientdata_actions of this AlarmHistoryInfo.

        数据不足触发的动作。  结构如下：  {  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  }  type取值： 数据不足触发告警通知类型，取值为notification。 notificationList：数据不足触发告警通知时，被通知对象的ID列表。

        :return: The insufficientdata_actions of this AlarmHistoryInfo.
        :rtype: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        return self._insufficientdata_actions

    @insufficientdata_actions.setter
    def insufficientdata_actions(self, insufficientdata_actions):
        """Sets the insufficientdata_actions of this AlarmHistoryInfo.

        数据不足触发的动作。  结构如下：  {  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  }  type取值： 数据不足触发告警通知类型，取值为notification。 notificationList：数据不足触发告警通知时，被通知对象的ID列表。

        :param insufficientdata_actions: The insufficientdata_actions of this AlarmHistoryInfo.
        :type insufficientdata_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        self._insufficientdata_actions = insufficientdata_actions

    @property
    def update_time(self):
        """Gets the update_time of this AlarmHistoryInfo.

        告警状态变更的时间，UNIX时间戳，单位毫秒，如：1603131199000。

        :return: The update_time of this AlarmHistoryInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AlarmHistoryInfo.

        告警状态变更的时间，UNIX时间戳，单位毫秒，如：1603131199000。

        :param update_time: The update_time of this AlarmHistoryInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this AlarmHistoryInfo.

        企业项目ID。 值为all_granted_eps时，表示所有企业项目；值为0时，表示默认的企业项目default。

        :return: The enterprise_project_id of this AlarmHistoryInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this AlarmHistoryInfo.

        企业项目ID。 值为all_granted_eps时，表示所有企业项目；值为0时，表示默认的企业项目default。

        :param enterprise_project_id: The enterprise_project_id of this AlarmHistoryInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def trigger_time(self):
        """Gets the trigger_time of this AlarmHistoryInfo.

        计算出该条告警历史的时间，UNIX时间戳，单位毫秒，如：1603131199469。

        :return: The trigger_time of this AlarmHistoryInfo.
        :rtype: int
        """
        return self._trigger_time

    @trigger_time.setter
    def trigger_time(self, trigger_time):
        """Sets the trigger_time of this AlarmHistoryInfo.

        计算出该条告警历史的时间，UNIX时间戳，单位毫秒，如：1603131199469。

        :param trigger_time: The trigger_time of this AlarmHistoryInfo.
        :type trigger_time: int
        """
        self._trigger_time = trigger_time

    @property
    def alarm_status(self):
        """Gets the alarm_status of this AlarmHistoryInfo.

        告警历史的状态，取值为ok，alarm，insufficient_data； ok为正常，alarm为告警，insufficient_data为数据不足。

        :return: The alarm_status of this AlarmHistoryInfo.
        :rtype: str
        """
        return self._alarm_status

    @alarm_status.setter
    def alarm_status(self, alarm_status):
        """Sets the alarm_status of this AlarmHistoryInfo.

        告警历史的状态，取值为ok，alarm，insufficient_data； ok为正常，alarm为告警，insufficient_data为数据不足。

        :param alarm_status: The alarm_status of this AlarmHistoryInfo.
        :type alarm_status: str
        """
        self._alarm_status = alarm_status

    @property
    def datapoints(self):
        """Gets the datapoints of this AlarmHistoryInfo.

        计算出该条告警历史的资源监控数据的一组数据上报时间和监控数值。

        :return: The datapoints of this AlarmHistoryInfo.
        :rtype: list[:class:`huaweicloudsdkces.v1.DataPointForAlarmHistory`]
        """
        return self._datapoints

    @datapoints.setter
    def datapoints(self, datapoints):
        """Sets the datapoints of this AlarmHistoryInfo.

        计算出该条告警历史的资源监控数据的一组数据上报时间和监控数值。

        :param datapoints: The datapoints of this AlarmHistoryInfo.
        :type datapoints: list[:class:`huaweicloudsdkces.v1.DataPointForAlarmHistory`]
        """
        self._datapoints = datapoints

    @property
    def additional_info(self):
        """Gets the additional_info of this AlarmHistoryInfo.


        :return: The additional_info of this AlarmHistoryInfo.
        :rtype: :class:`huaweicloudsdkces.v1.AdditionalInfo`
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this AlarmHistoryInfo.


        :param additional_info: The additional_info of this AlarmHistoryInfo.
        :type additional_info: :class:`huaweicloudsdkces.v1.AdditionalInfo`
        """
        self._additional_info = additional_info

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
        if not isinstance(other, AlarmHistoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
