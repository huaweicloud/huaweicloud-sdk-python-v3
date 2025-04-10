# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateScalingPolicyOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scaling_policy_name': 'str',
        'scaling_policy_type': 'str',
        'alarm_id': 'str',
        'scheduled_policy': 'ScheduledPolicy',
        'scaling_policy_action': 'ScalingPolicyActionV1',
        'cool_down_time': 'int'
    }

    attribute_map = {
        'scaling_policy_name': 'scaling_policy_name',
        'scaling_policy_type': 'scaling_policy_type',
        'alarm_id': 'alarm_id',
        'scheduled_policy': 'scheduled_policy',
        'scaling_policy_action': 'scaling_policy_action',
        'cool_down_time': 'cool_down_time'
    }

    def __init__(self, scaling_policy_name=None, scaling_policy_type=None, alarm_id=None, scheduled_policy=None, scaling_policy_action=None, cool_down_time=None):
        r"""UpdateScalingPolicyOption

        The model defined in huaweicloud sdk

        :param scaling_policy_name: 策略名称(1-64字符)，可以用中文、字母、数字、下划线、中划线的组合。
        :type scaling_policy_name: str
        :param scaling_policy_type: 策略类型。告警策略：ALARM（与alarm_id对应）；定时策略：SCHEDULED（与scheduled_policy对应）；周期策略：RECURRENCE（与scheduled_policy对应）
        :type scaling_policy_type: str
        :param alarm_id: 告警ID，即告警规则的ID，当scaling_policy_type为ALARM时该项必选，此时scheduled_policy不生效。创建告警策略成功后，会自动为该告警ID对应的告警规则的alarm_actions字段增加类型为autoscaling的告警触发动作。告警ID通过查询云监控告警规则列表获取，详见《云监控API参考》的“查询告警规则列表”。
        :type alarm_id: str
        :param scheduled_policy: 
        :type scheduled_policy: :class:`huaweicloudsdkas.v1.ScheduledPolicy`
        :param scaling_policy_action: 
        :type scaling_policy_action: :class:`huaweicloudsdkas.v1.ScalingPolicyActionV1`
        :param cool_down_time: 冷却时间，取值范围0-86400，默认为300，单位是秒。
        :type cool_down_time: int
        """
        
        

        self._scaling_policy_name = None
        self._scaling_policy_type = None
        self._alarm_id = None
        self._scheduled_policy = None
        self._scaling_policy_action = None
        self._cool_down_time = None
        self.discriminator = None

        if scaling_policy_name is not None:
            self.scaling_policy_name = scaling_policy_name
        if scaling_policy_type is not None:
            self.scaling_policy_type = scaling_policy_type
        if alarm_id is not None:
            self.alarm_id = alarm_id
        if scheduled_policy is not None:
            self.scheduled_policy = scheduled_policy
        if scaling_policy_action is not None:
            self.scaling_policy_action = scaling_policy_action
        if cool_down_time is not None:
            self.cool_down_time = cool_down_time

    @property
    def scaling_policy_name(self):
        r"""Gets the scaling_policy_name of this UpdateScalingPolicyOption.

        策略名称(1-64字符)，可以用中文、字母、数字、下划线、中划线的组合。

        :return: The scaling_policy_name of this UpdateScalingPolicyOption.
        :rtype: str
        """
        return self._scaling_policy_name

    @scaling_policy_name.setter
    def scaling_policy_name(self, scaling_policy_name):
        r"""Sets the scaling_policy_name of this UpdateScalingPolicyOption.

        策略名称(1-64字符)，可以用中文、字母、数字、下划线、中划线的组合。

        :param scaling_policy_name: The scaling_policy_name of this UpdateScalingPolicyOption.
        :type scaling_policy_name: str
        """
        self._scaling_policy_name = scaling_policy_name

    @property
    def scaling_policy_type(self):
        r"""Gets the scaling_policy_type of this UpdateScalingPolicyOption.

        策略类型。告警策略：ALARM（与alarm_id对应）；定时策略：SCHEDULED（与scheduled_policy对应）；周期策略：RECURRENCE（与scheduled_policy对应）

        :return: The scaling_policy_type of this UpdateScalingPolicyOption.
        :rtype: str
        """
        return self._scaling_policy_type

    @scaling_policy_type.setter
    def scaling_policy_type(self, scaling_policy_type):
        r"""Sets the scaling_policy_type of this UpdateScalingPolicyOption.

        策略类型。告警策略：ALARM（与alarm_id对应）；定时策略：SCHEDULED（与scheduled_policy对应）；周期策略：RECURRENCE（与scheduled_policy对应）

        :param scaling_policy_type: The scaling_policy_type of this UpdateScalingPolicyOption.
        :type scaling_policy_type: str
        """
        self._scaling_policy_type = scaling_policy_type

    @property
    def alarm_id(self):
        r"""Gets the alarm_id of this UpdateScalingPolicyOption.

        告警ID，即告警规则的ID，当scaling_policy_type为ALARM时该项必选，此时scheduled_policy不生效。创建告警策略成功后，会自动为该告警ID对应的告警规则的alarm_actions字段增加类型为autoscaling的告警触发动作。告警ID通过查询云监控告警规则列表获取，详见《云监控API参考》的“查询告警规则列表”。

        :return: The alarm_id of this UpdateScalingPolicyOption.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        r"""Sets the alarm_id of this UpdateScalingPolicyOption.

        告警ID，即告警规则的ID，当scaling_policy_type为ALARM时该项必选，此时scheduled_policy不生效。创建告警策略成功后，会自动为该告警ID对应的告警规则的alarm_actions字段增加类型为autoscaling的告警触发动作。告警ID通过查询云监控告警规则列表获取，详见《云监控API参考》的“查询告警规则列表”。

        :param alarm_id: The alarm_id of this UpdateScalingPolicyOption.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def scheduled_policy(self):
        r"""Gets the scheduled_policy of this UpdateScalingPolicyOption.

        :return: The scheduled_policy of this UpdateScalingPolicyOption.
        :rtype: :class:`huaweicloudsdkas.v1.ScheduledPolicy`
        """
        return self._scheduled_policy

    @scheduled_policy.setter
    def scheduled_policy(self, scheduled_policy):
        r"""Sets the scheduled_policy of this UpdateScalingPolicyOption.

        :param scheduled_policy: The scheduled_policy of this UpdateScalingPolicyOption.
        :type scheduled_policy: :class:`huaweicloudsdkas.v1.ScheduledPolicy`
        """
        self._scheduled_policy = scheduled_policy

    @property
    def scaling_policy_action(self):
        r"""Gets the scaling_policy_action of this UpdateScalingPolicyOption.

        :return: The scaling_policy_action of this UpdateScalingPolicyOption.
        :rtype: :class:`huaweicloudsdkas.v1.ScalingPolicyActionV1`
        """
        return self._scaling_policy_action

    @scaling_policy_action.setter
    def scaling_policy_action(self, scaling_policy_action):
        r"""Sets the scaling_policy_action of this UpdateScalingPolicyOption.

        :param scaling_policy_action: The scaling_policy_action of this UpdateScalingPolicyOption.
        :type scaling_policy_action: :class:`huaweicloudsdkas.v1.ScalingPolicyActionV1`
        """
        self._scaling_policy_action = scaling_policy_action

    @property
    def cool_down_time(self):
        r"""Gets the cool_down_time of this UpdateScalingPolicyOption.

        冷却时间，取值范围0-86400，默认为300，单位是秒。

        :return: The cool_down_time of this UpdateScalingPolicyOption.
        :rtype: int
        """
        return self._cool_down_time

    @cool_down_time.setter
    def cool_down_time(self, cool_down_time):
        r"""Sets the cool_down_time of this UpdateScalingPolicyOption.

        冷却时间，取值范围0-86400，默认为300，单位是秒。

        :param cool_down_time: The cool_down_time of this UpdateScalingPolicyOption.
        :type cool_down_time: int
        """
        self._cool_down_time = cool_down_time

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
        if not isinstance(other, UpdateScalingPolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
