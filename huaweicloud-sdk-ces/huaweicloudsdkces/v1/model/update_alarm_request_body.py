# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAlarmRequestBody:

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
        'condition': 'Condition',
        'alarm_action_enabled': 'bool',
        'alarm_level': 'int',
        'alarm_type': 'str',
        'alarm_actions': 'list[AlarmActions]',
        'insufficientdata_actions': 'list[AlarmActions]',
        'ok_actions': 'list[AlarmActions]'
    }

    attribute_map = {
        'alarm_name': 'alarm_name',
        'alarm_description': 'alarm_description',
        'condition': 'condition',
        'alarm_action_enabled': 'alarm_action_enabled',
        'alarm_level': 'alarm_level',
        'alarm_type': 'alarm_type',
        'alarm_actions': 'alarm_actions',
        'insufficientdata_actions': 'insufficientdata_actions',
        'ok_actions': 'ok_actions'
    }

    def __init__(self, alarm_name=None, alarm_description=None, condition=None, alarm_action_enabled=None, alarm_level=None, alarm_type=None, alarm_actions=None, insufficientdata_actions=None, ok_actions=None):
        """UpdateAlarmRequestBody

        The model defined in huaweicloud sdk

        :param alarm_name: 告警名称，只能包含0-9/a-z/A-Z/_/-或汉字。
        :type alarm_name: str
        :param alarm_description: 告警描述，长度0-256。
        :type alarm_description: str
        :param condition: 
        :type condition: :class:`huaweicloudsdkces.v1.Condition`
        :param alarm_action_enabled: 是否启用该条告警触发的动作，默认为true。注：若alarm_action_enabled为true，对应的alarm_actions、ok_actions至少有一个不能为空。若alarm_actions、ok_actions同时存在时，notificationList值保持一致。
        :type alarm_action_enabled: bool
        :param alarm_level: 告警级别，默认为2，级别为1、2、3、4。分别对应紧急、重要、次要、提示。
        :type alarm_level: int
        :param alarm_type: 告警类型，支持的枚举类型：EVENT.SYS：针对系统事件的告警规则；EVENT.CUSTOM：针对自定义事件的告警规则；RESOURCE_GROUP：针对资源分组的告警规则。
        :type alarm_type: str
        :param alarm_actions: 告警触发的动作。 结构样例如下： { \&quot;type\&quot;: \&quot;notification\&quot;,\&quot;notificationList\&quot;: [\&quot;urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\&quot;] } type取值： notification：通知。 autoscaling：弹性伸缩。
        :type alarm_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        :param insufficientdata_actions: 数据不足触发的动作（该参数已废弃，建议无需配置）。
        :type insufficientdata_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        :param ok_actions: 告警恢复触发的动作
        :type ok_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        
        

        self._alarm_name = None
        self._alarm_description = None
        self._condition = None
        self._alarm_action_enabled = None
        self._alarm_level = None
        self._alarm_type = None
        self._alarm_actions = None
        self._insufficientdata_actions = None
        self._ok_actions = None
        self.discriminator = None

        if alarm_name is not None:
            self.alarm_name = alarm_name
        if alarm_description is not None:
            self.alarm_description = alarm_description
        if condition is not None:
            self.condition = condition
        if alarm_action_enabled is not None:
            self.alarm_action_enabled = alarm_action_enabled
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if alarm_type is not None:
            self.alarm_type = alarm_type
        if alarm_actions is not None:
            self.alarm_actions = alarm_actions
        if insufficientdata_actions is not None:
            self.insufficientdata_actions = insufficientdata_actions
        if ok_actions is not None:
            self.ok_actions = ok_actions

    @property
    def alarm_name(self):
        """Gets the alarm_name of this UpdateAlarmRequestBody.

        告警名称，只能包含0-9/a-z/A-Z/_/-或汉字。

        :return: The alarm_name of this UpdateAlarmRequestBody.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        """Sets the alarm_name of this UpdateAlarmRequestBody.

        告警名称，只能包含0-9/a-z/A-Z/_/-或汉字。

        :param alarm_name: The alarm_name of this UpdateAlarmRequestBody.
        :type alarm_name: str
        """
        self._alarm_name = alarm_name

    @property
    def alarm_description(self):
        """Gets the alarm_description of this UpdateAlarmRequestBody.

        告警描述，长度0-256。

        :return: The alarm_description of this UpdateAlarmRequestBody.
        :rtype: str
        """
        return self._alarm_description

    @alarm_description.setter
    def alarm_description(self, alarm_description):
        """Sets the alarm_description of this UpdateAlarmRequestBody.

        告警描述，长度0-256。

        :param alarm_description: The alarm_description of this UpdateAlarmRequestBody.
        :type alarm_description: str
        """
        self._alarm_description = alarm_description

    @property
    def condition(self):
        """Gets the condition of this UpdateAlarmRequestBody.

        :return: The condition of this UpdateAlarmRequestBody.
        :rtype: :class:`huaweicloudsdkces.v1.Condition`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this UpdateAlarmRequestBody.

        :param condition: The condition of this UpdateAlarmRequestBody.
        :type condition: :class:`huaweicloudsdkces.v1.Condition`
        """
        self._condition = condition

    @property
    def alarm_action_enabled(self):
        """Gets the alarm_action_enabled of this UpdateAlarmRequestBody.

        是否启用该条告警触发的动作，默认为true。注：若alarm_action_enabled为true，对应的alarm_actions、ok_actions至少有一个不能为空。若alarm_actions、ok_actions同时存在时，notificationList值保持一致。

        :return: The alarm_action_enabled of this UpdateAlarmRequestBody.
        :rtype: bool
        """
        return self._alarm_action_enabled

    @alarm_action_enabled.setter
    def alarm_action_enabled(self, alarm_action_enabled):
        """Sets the alarm_action_enabled of this UpdateAlarmRequestBody.

        是否启用该条告警触发的动作，默认为true。注：若alarm_action_enabled为true，对应的alarm_actions、ok_actions至少有一个不能为空。若alarm_actions、ok_actions同时存在时，notificationList值保持一致。

        :param alarm_action_enabled: The alarm_action_enabled of this UpdateAlarmRequestBody.
        :type alarm_action_enabled: bool
        """
        self._alarm_action_enabled = alarm_action_enabled

    @property
    def alarm_level(self):
        """Gets the alarm_level of this UpdateAlarmRequestBody.

        告警级别，默认为2，级别为1、2、3、4。分别对应紧急、重要、次要、提示。

        :return: The alarm_level of this UpdateAlarmRequestBody.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this UpdateAlarmRequestBody.

        告警级别，默认为2，级别为1、2、3、4。分别对应紧急、重要、次要、提示。

        :param alarm_level: The alarm_level of this UpdateAlarmRequestBody.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def alarm_type(self):
        """Gets the alarm_type of this UpdateAlarmRequestBody.

        告警类型，支持的枚举类型：EVENT.SYS：针对系统事件的告警规则；EVENT.CUSTOM：针对自定义事件的告警规则；RESOURCE_GROUP：针对资源分组的告警规则。

        :return: The alarm_type of this UpdateAlarmRequestBody.
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        """Sets the alarm_type of this UpdateAlarmRequestBody.

        告警类型，支持的枚举类型：EVENT.SYS：针对系统事件的告警规则；EVENT.CUSTOM：针对自定义事件的告警规则；RESOURCE_GROUP：针对资源分组的告警规则。

        :param alarm_type: The alarm_type of this UpdateAlarmRequestBody.
        :type alarm_type: str
        """
        self._alarm_type = alarm_type

    @property
    def alarm_actions(self):
        """Gets the alarm_actions of this UpdateAlarmRequestBody.

        告警触发的动作。 结构样例如下： { \"type\": \"notification\",\"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"] } type取值： notification：通知。 autoscaling：弹性伸缩。

        :return: The alarm_actions of this UpdateAlarmRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        return self._alarm_actions

    @alarm_actions.setter
    def alarm_actions(self, alarm_actions):
        """Sets the alarm_actions of this UpdateAlarmRequestBody.

        告警触发的动作。 结构样例如下： { \"type\": \"notification\",\"notificationList\": [\"urn:smn:southchina:68438a86d98e427e907e0097b7e35d47:sd\"] } type取值： notification：通知。 autoscaling：弹性伸缩。

        :param alarm_actions: The alarm_actions of this UpdateAlarmRequestBody.
        :type alarm_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        self._alarm_actions = alarm_actions

    @property
    def insufficientdata_actions(self):
        """Gets the insufficientdata_actions of this UpdateAlarmRequestBody.

        数据不足触发的动作（该参数已废弃，建议无需配置）。

        :return: The insufficientdata_actions of this UpdateAlarmRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        return self._insufficientdata_actions

    @insufficientdata_actions.setter
    def insufficientdata_actions(self, insufficientdata_actions):
        """Sets the insufficientdata_actions of this UpdateAlarmRequestBody.

        数据不足触发的动作（该参数已废弃，建议无需配置）。

        :param insufficientdata_actions: The insufficientdata_actions of this UpdateAlarmRequestBody.
        :type insufficientdata_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        self._insufficientdata_actions = insufficientdata_actions

    @property
    def ok_actions(self):
        """Gets the ok_actions of this UpdateAlarmRequestBody.

        告警恢复触发的动作

        :return: The ok_actions of this UpdateAlarmRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        return self._ok_actions

    @ok_actions.setter
    def ok_actions(self, ok_actions):
        """Sets the ok_actions of this UpdateAlarmRequestBody.

        告警恢复触发的动作

        :param ok_actions: The ok_actions of this UpdateAlarmRequestBody.
        :type ok_actions: list[:class:`huaweicloudsdkces.v1.AlarmActions`]
        """
        self._ok_actions = ok_actions

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
        if not isinstance(other, UpdateAlarmRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
