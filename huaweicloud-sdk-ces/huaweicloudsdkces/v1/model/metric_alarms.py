# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricAlarms:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'alarm_name': 'str',
        'alarm_description': 'str',
        'metric': 'MetricInfoForAlarm',
        'condition': 'Condition',
        'alarm_enabled': 'bool',
        'alarm_level': 'int',
        'alarm_type': 'str',
        'alarm_action_enabled': 'bool',
        'alarm_actions': 'list[AlarmActions]',
        'ok_actions': 'list[AlarmActions]',
        'insufficientdata_actions': 'list[AlarmActions]',
        'alarm_action_begin_time': 'str',
        'alarm_action_end_time': 'str',
        'alarm_id': 'str',
        'update_time': 'int',
        'alarm_state': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'alarm_name': 'alarm_name',
        'alarm_description': 'alarm_description',
        'metric': 'metric',
        'condition': 'condition',
        'alarm_enabled': 'alarm_enabled',
        'alarm_level': 'alarm_level',
        'alarm_type': 'alarm_type',
        'alarm_action_enabled': 'alarm_action_enabled',
        'alarm_actions': 'alarm_actions',
        'ok_actions': 'ok_actions',
        'insufficientdata_actions': 'insufficientdata_actions',
        'alarm_action_begin_time': 'alarm_action_begin_time',
        'alarm_action_end_time': 'alarm_action_end_time',
        'alarm_id': 'alarm_id',
        'update_time': 'update_time',
        'alarm_state': 'alarm_state',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, alarm_name=None, alarm_description=None, metric=None, condition=None, alarm_enabled=None, alarm_level=None, alarm_type=None, alarm_action_enabled=None, alarm_actions=None, ok_actions=None, insufficientdata_actions=None, alarm_action_begin_time=None, alarm_action_end_time=None, alarm_id=None, update_time=None, alarm_state=None, enterprise_project_id=None):
        """MetricAlarms

        The model defined in huaweicloud sdk

        :param alarm_name: 告警名称。
        :type alarm_name: str
        :param alarm_description: 告警描述。
        :type alarm_description: str
        :param metric: 
        :type metric: :class:`huaweicloudsdkces.v1.MetricInfoForAlarm`
        :param condition: 
        :type condition: :class:`huaweicloudsdkces.v1.Condition`
        :param alarm_enabled: 是否启用该条告警。
        :type alarm_enabled: bool
        :param alarm_level: 告警级别，默认为2，级别为1、2、3、4。分别对应紧急、重要、次要、提示。
        :type alarm_level: int
        :param alarm_type: 告警类型。 仅针对事件告警的参数，枚举类型：EVENT.SYS或者EVENT.CUSTOM
        :type alarm_type: str
        :param alarm_action_enabled: 是否启用该条告警触发的动作。
        :type alarm_action_enabled: bool
        :param alarm_actions: 告警触发的动作。  结构如下：  {  \&quot;type\&quot;: \&quot;notification\&quot;, \&quot;notificationList\&quot;: [\&quot;urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\&quot;]  }  type取值： notification：通知。 autoscaling：弹性伸缩。 notificationList：告警状态发生变化时，被通知对象的列表。
        :type alarm_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        :param ok_actions: 告警恢复触发的动作。  结构如下：  {  \&quot;type\&quot;: \&quot;notification\&quot;, \&quot;notificationList\&quot;: [\&quot;urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\&quot;]  } type取值：  notification：通知。  notificationList：告警状态发生变化时，被通知对象的列表。
        :type ok_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        :param insufficientdata_actions: 数据不足触发的动作。  结构如下：  {  \&quot;type\&quot;: \&quot;notification\&quot;, \&quot;notificationList\&quot;: [\&quot;urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\&quot;]  }  type取值： 数据不足触发告警通知类型，取值为notification。 notificationList：数据不足触发告警通知时，被通知对象的ID列表。
        :type insufficientdata_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        :param alarm_action_begin_time: 告警规则生效的开始时间，告警规则仅在生效时间内发送通知消息。例如alarm_action_begin_time为8:00，alarm_action_end_time为20:00时，则对应的告警规则仅在08:00-20:00发送通知消息。
        :type alarm_action_begin_time: str
        :param alarm_action_end_time: 告警规则生效的结束时间，告警规则仅在生效时间内发送通知消息。例如alarm_action_begin_time为8:00，alarm_action_end_time为20:00时，则对应的告警规则仅在08:00-20:00发送通知消息。
        :type alarm_action_end_time: str
        :param alarm_id: 告警规则的ID。
        :type alarm_id: str
        :param update_time: 告警状态变更的时间，UNIX时间戳，单位毫秒。
        :type update_time: int
        :param alarm_state: 告警状态，取值说明：  ok，正常 alarm，告警 insufficient_data，数据不足
        :type alarm_state: str
        :param enterprise_project_id: 企业项目ID。 取值为all_granted_eps时，表示所有企业项目; 取值为0时，表示默认的企业项目default。
        :type enterprise_project_id: str
        """
        
        

        self._alarm_name = None
        self._alarm_description = None
        self._metric = None
        self._condition = None
        self._alarm_enabled = None
        self._alarm_level = None
        self._alarm_type = None
        self._alarm_action_enabled = None
        self._alarm_actions = None
        self._ok_actions = None
        self._insufficientdata_actions = None
        self._alarm_action_begin_time = None
        self._alarm_action_end_time = None
        self._alarm_id = None
        self._update_time = None
        self._alarm_state = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.alarm_name = alarm_name
        if alarm_description is not None:
            self.alarm_description = alarm_description
        self.metric = metric
        self.condition = condition
        if alarm_enabled is not None:
            self.alarm_enabled = alarm_enabled
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if alarm_type is not None:
            self.alarm_type = alarm_type
        if alarm_action_enabled is not None:
            self.alarm_action_enabled = alarm_action_enabled
        if alarm_actions is not None:
            self.alarm_actions = alarm_actions
        if ok_actions is not None:
            self.ok_actions = ok_actions
        if insufficientdata_actions is not None:
            self.insufficientdata_actions = insufficientdata_actions
        if alarm_action_begin_time is not None:
            self.alarm_action_begin_time = alarm_action_begin_time
        if alarm_action_end_time is not None:
            self.alarm_action_end_time = alarm_action_end_time
        self.alarm_id = alarm_id
        self.update_time = update_time
        self.alarm_state = alarm_state
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def alarm_name(self):
        """Gets the alarm_name of this MetricAlarms.

        告警名称。

        :return: The alarm_name of this MetricAlarms.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        """Sets the alarm_name of this MetricAlarms.

        告警名称。

        :param alarm_name: The alarm_name of this MetricAlarms.
        :type alarm_name: str
        """
        self._alarm_name = alarm_name

    @property
    def alarm_description(self):
        """Gets the alarm_description of this MetricAlarms.

        告警描述。

        :return: The alarm_description of this MetricAlarms.
        :rtype: str
        """
        return self._alarm_description

    @alarm_description.setter
    def alarm_description(self, alarm_description):
        """Sets the alarm_description of this MetricAlarms.

        告警描述。

        :param alarm_description: The alarm_description of this MetricAlarms.
        :type alarm_description: str
        """
        self._alarm_description = alarm_description

    @property
    def metric(self):
        """Gets the metric of this MetricAlarms.


        :return: The metric of this MetricAlarms.
        :rtype: :class:`huaweicloudsdkces.v1.MetricInfoForAlarm`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this MetricAlarms.


        :param metric: The metric of this MetricAlarms.
        :type metric: :class:`huaweicloudsdkces.v1.MetricInfoForAlarm`
        """
        self._metric = metric

    @property
    def condition(self):
        """Gets the condition of this MetricAlarms.


        :return: The condition of this MetricAlarms.
        :rtype: :class:`huaweicloudsdkces.v1.Condition`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this MetricAlarms.


        :param condition: The condition of this MetricAlarms.
        :type condition: :class:`huaweicloudsdkces.v1.Condition`
        """
        self._condition = condition

    @property
    def alarm_enabled(self):
        """Gets the alarm_enabled of this MetricAlarms.

        是否启用该条告警。

        :return: The alarm_enabled of this MetricAlarms.
        :rtype: bool
        """
        return self._alarm_enabled

    @alarm_enabled.setter
    def alarm_enabled(self, alarm_enabled):
        """Sets the alarm_enabled of this MetricAlarms.

        是否启用该条告警。

        :param alarm_enabled: The alarm_enabled of this MetricAlarms.
        :type alarm_enabled: bool
        """
        self._alarm_enabled = alarm_enabled

    @property
    def alarm_level(self):
        """Gets the alarm_level of this MetricAlarms.

        告警级别，默认为2，级别为1、2、3、4。分别对应紧急、重要、次要、提示。

        :return: The alarm_level of this MetricAlarms.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this MetricAlarms.

        告警级别，默认为2，级别为1、2、3、4。分别对应紧急、重要、次要、提示。

        :param alarm_level: The alarm_level of this MetricAlarms.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def alarm_type(self):
        """Gets the alarm_type of this MetricAlarms.

        告警类型。 仅针对事件告警的参数，枚举类型：EVENT.SYS或者EVENT.CUSTOM

        :return: The alarm_type of this MetricAlarms.
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        """Sets the alarm_type of this MetricAlarms.

        告警类型。 仅针对事件告警的参数，枚举类型：EVENT.SYS或者EVENT.CUSTOM

        :param alarm_type: The alarm_type of this MetricAlarms.
        :type alarm_type: str
        """
        self._alarm_type = alarm_type

    @property
    def alarm_action_enabled(self):
        """Gets the alarm_action_enabled of this MetricAlarms.

        是否启用该条告警触发的动作。

        :return: The alarm_action_enabled of this MetricAlarms.
        :rtype: bool
        """
        return self._alarm_action_enabled

    @alarm_action_enabled.setter
    def alarm_action_enabled(self, alarm_action_enabled):
        """Sets the alarm_action_enabled of this MetricAlarms.

        是否启用该条告警触发的动作。

        :param alarm_action_enabled: The alarm_action_enabled of this MetricAlarms.
        :type alarm_action_enabled: bool
        """
        self._alarm_action_enabled = alarm_action_enabled

    @property
    def alarm_actions(self):
        """Gets the alarm_actions of this MetricAlarms.

        告警触发的动作。  结构如下：  {  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  }  type取值： notification：通知。 autoscaling：弹性伸缩。 notificationList：告警状态发生变化时，被通知对象的列表。

        :return: The alarm_actions of this MetricAlarms.
        :rtype: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        return self._alarm_actions

    @alarm_actions.setter
    def alarm_actions(self, alarm_actions):
        """Sets the alarm_actions of this MetricAlarms.

        告警触发的动作。  结构如下：  {  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  }  type取值： notification：通知。 autoscaling：弹性伸缩。 notificationList：告警状态发生变化时，被通知对象的列表。

        :param alarm_actions: The alarm_actions of this MetricAlarms.
        :type alarm_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        self._alarm_actions = alarm_actions

    @property
    def ok_actions(self):
        """Gets the ok_actions of this MetricAlarms.

        告警恢复触发的动作。  结构如下：  {  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  } type取值：  notification：通知。  notificationList：告警状态发生变化时，被通知对象的列表。

        :return: The ok_actions of this MetricAlarms.
        :rtype: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        return self._ok_actions

    @ok_actions.setter
    def ok_actions(self, ok_actions):
        """Sets the ok_actions of this MetricAlarms.

        告警恢复触发的动作。  结构如下：  {  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  } type取值：  notification：通知。  notificationList：告警状态发生变化时，被通知对象的列表。

        :param ok_actions: The ok_actions of this MetricAlarms.
        :type ok_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        self._ok_actions = ok_actions

    @property
    def insufficientdata_actions(self):
        """Gets the insufficientdata_actions of this MetricAlarms.

        数据不足触发的动作。  结构如下：  {  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  }  type取值： 数据不足触发告警通知类型，取值为notification。 notificationList：数据不足触发告警通知时，被通知对象的ID列表。

        :return: The insufficientdata_actions of this MetricAlarms.
        :rtype: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        return self._insufficientdata_actions

    @insufficientdata_actions.setter
    def insufficientdata_actions(self, insufficientdata_actions):
        """Sets the insufficientdata_actions of this MetricAlarms.

        数据不足触发的动作。  结构如下：  {  \"type\": \"notification\", \"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"]  }  type取值： 数据不足触发告警通知类型，取值为notification。 notificationList：数据不足触发告警通知时，被通知对象的ID列表。

        :param insufficientdata_actions: The insufficientdata_actions of this MetricAlarms.
        :type insufficientdata_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        self._insufficientdata_actions = insufficientdata_actions

    @property
    def alarm_action_begin_time(self):
        """Gets the alarm_action_begin_time of this MetricAlarms.

        告警规则生效的开始时间，告警规则仅在生效时间内发送通知消息。例如alarm_action_begin_time为8:00，alarm_action_end_time为20:00时，则对应的告警规则仅在08:00-20:00发送通知消息。

        :return: The alarm_action_begin_time of this MetricAlarms.
        :rtype: str
        """
        return self._alarm_action_begin_time

    @alarm_action_begin_time.setter
    def alarm_action_begin_time(self, alarm_action_begin_time):
        """Sets the alarm_action_begin_time of this MetricAlarms.

        告警规则生效的开始时间，告警规则仅在生效时间内发送通知消息。例如alarm_action_begin_time为8:00，alarm_action_end_time为20:00时，则对应的告警规则仅在08:00-20:00发送通知消息。

        :param alarm_action_begin_time: The alarm_action_begin_time of this MetricAlarms.
        :type alarm_action_begin_time: str
        """
        self._alarm_action_begin_time = alarm_action_begin_time

    @property
    def alarm_action_end_time(self):
        """Gets the alarm_action_end_time of this MetricAlarms.

        告警规则生效的结束时间，告警规则仅在生效时间内发送通知消息。例如alarm_action_begin_time为8:00，alarm_action_end_time为20:00时，则对应的告警规则仅在08:00-20:00发送通知消息。

        :return: The alarm_action_end_time of this MetricAlarms.
        :rtype: str
        """
        return self._alarm_action_end_time

    @alarm_action_end_time.setter
    def alarm_action_end_time(self, alarm_action_end_time):
        """Sets the alarm_action_end_time of this MetricAlarms.

        告警规则生效的结束时间，告警规则仅在生效时间内发送通知消息。例如alarm_action_begin_time为8:00，alarm_action_end_time为20:00时，则对应的告警规则仅在08:00-20:00发送通知消息。

        :param alarm_action_end_time: The alarm_action_end_time of this MetricAlarms.
        :type alarm_action_end_time: str
        """
        self._alarm_action_end_time = alarm_action_end_time

    @property
    def alarm_id(self):
        """Gets the alarm_id of this MetricAlarms.

        告警规则的ID。

        :return: The alarm_id of this MetricAlarms.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this MetricAlarms.

        告警规则的ID。

        :param alarm_id: The alarm_id of this MetricAlarms.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def update_time(self):
        """Gets the update_time of this MetricAlarms.

        告警状态变更的时间，UNIX时间戳，单位毫秒。

        :return: The update_time of this MetricAlarms.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this MetricAlarms.

        告警状态变更的时间，UNIX时间戳，单位毫秒。

        :param update_time: The update_time of this MetricAlarms.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def alarm_state(self):
        """Gets the alarm_state of this MetricAlarms.

        告警状态，取值说明：  ok，正常 alarm，告警 insufficient_data，数据不足

        :return: The alarm_state of this MetricAlarms.
        :rtype: str
        """
        return self._alarm_state

    @alarm_state.setter
    def alarm_state(self, alarm_state):
        """Sets the alarm_state of this MetricAlarms.

        告警状态，取值说明：  ok，正常 alarm，告警 insufficient_data，数据不足

        :param alarm_state: The alarm_state of this MetricAlarms.
        :type alarm_state: str
        """
        self._alarm_state = alarm_state

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this MetricAlarms.

        企业项目ID。 取值为all_granted_eps时，表示所有企业项目; 取值为0时，表示默认的企业项目default。

        :return: The enterprise_project_id of this MetricAlarms.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this MetricAlarms.

        企业项目ID。 取值为all_granted_eps时，表示所有企业项目; 取值为0时，表示默认的企业项目default。

        :param enterprise_project_id: The enterprise_project_id of this MetricAlarms.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, MetricAlarms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
