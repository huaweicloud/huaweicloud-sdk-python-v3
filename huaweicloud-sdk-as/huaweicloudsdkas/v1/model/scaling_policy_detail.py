# coding: utf-8

import pprint
import re

import six





class ScalingPolicyDetail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_group_id': 'str',
        'scaling_policy_name': 'str',
        'scaling_policy_id': 'str',
        'scaling_policy_type': 'str',
        'alarm_id': 'str',
        'scheduled_policy': 'ScheduledPolicy',
        'scaling_policy_action': 'ScalingPolicyAction',
        'cool_down_time': 'int',
        'create_time': 'datetime'
    }

    attribute_map = {
        'scaling_group_id': 'scaling_group_id',
        'scaling_policy_name': 'scaling_policy_name',
        'scaling_policy_id': 'scaling_policy_id',
        'scaling_policy_type': 'scaling_policy_type',
        'alarm_id': 'alarm_id',
        'scheduled_policy': 'scheduled_policy',
        'scaling_policy_action': 'scaling_policy_action',
        'cool_down_time': 'cool_down_time',
        'create_time': 'create_time'
    }

    def __init__(self, scaling_group_id=None, scaling_policy_name=None, scaling_policy_id=None, scaling_policy_type=None, alarm_id=None, scheduled_policy=None, scaling_policy_action=None, cool_down_time=None, create_time=None):
        """ScalingPolicyDetail - a model defined in huaweicloud sdk"""
        
        

        self._scaling_group_id = None
        self._scaling_policy_name = None
        self._scaling_policy_id = None
        self._scaling_policy_type = None
        self._alarm_id = None
        self._scheduled_policy = None
        self._scaling_policy_action = None
        self._cool_down_time = None
        self._create_time = None
        self.discriminator = None

        if scaling_group_id is not None:
            self.scaling_group_id = scaling_group_id
        if scaling_policy_name is not None:
            self.scaling_policy_name = scaling_policy_name
        if scaling_policy_id is not None:
            self.scaling_policy_id = scaling_policy_id
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
        if create_time is not None:
            self.create_time = create_time

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this ScalingPolicyDetail.

        伸缩组ID。

        :return: The scaling_group_id of this ScalingPolicyDetail.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this ScalingPolicyDetail.

        伸缩组ID。

        :param scaling_group_id: The scaling_group_id of this ScalingPolicyDetail.
        :type: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def scaling_policy_name(self):
        """Gets the scaling_policy_name of this ScalingPolicyDetail.

        伸缩策略名称。

        :return: The scaling_policy_name of this ScalingPolicyDetail.
        :rtype: str
        """
        return self._scaling_policy_name

    @scaling_policy_name.setter
    def scaling_policy_name(self, scaling_policy_name):
        """Sets the scaling_policy_name of this ScalingPolicyDetail.

        伸缩策略名称。

        :param scaling_policy_name: The scaling_policy_name of this ScalingPolicyDetail.
        :type: str
        """
        self._scaling_policy_name = scaling_policy_name

    @property
    def scaling_policy_id(self):
        """Gets the scaling_policy_id of this ScalingPolicyDetail.

        伸缩策略ID。

        :return: The scaling_policy_id of this ScalingPolicyDetail.
        :rtype: str
        """
        return self._scaling_policy_id

    @scaling_policy_id.setter
    def scaling_policy_id(self, scaling_policy_id):
        """Sets the scaling_policy_id of this ScalingPolicyDetail.

        伸缩策略ID。

        :param scaling_policy_id: The scaling_policy_id of this ScalingPolicyDetail.
        :type: str
        """
        self._scaling_policy_id = scaling_policy_id

    @property
    def scaling_policy_type(self):
        """Gets the scaling_policy_type of this ScalingPolicyDetail.

        伸缩策略类型：ALARM：告警策略，此时alarm_id有返回，scheduled_policy不会返回。SCHEDULED：定时策略，此时alarm_id不会返回，scheduled_policy有返回，并且recurrence_type、recurrence_value、start_time和end_time不会返回。RECURRENCE：周期策略，此时alarm_id不会返回，scheduled_policy有返回，并且recurrence_type、recurrence_value、start_time和end_time有返回。

        :return: The scaling_policy_type of this ScalingPolicyDetail.
        :rtype: str
        """
        return self._scaling_policy_type

    @scaling_policy_type.setter
    def scaling_policy_type(self, scaling_policy_type):
        """Sets the scaling_policy_type of this ScalingPolicyDetail.

        伸缩策略类型：ALARM：告警策略，此时alarm_id有返回，scheduled_policy不会返回。SCHEDULED：定时策略，此时alarm_id不会返回，scheduled_policy有返回，并且recurrence_type、recurrence_value、start_time和end_time不会返回。RECURRENCE：周期策略，此时alarm_id不会返回，scheduled_policy有返回，并且recurrence_type、recurrence_value、start_time和end_time有返回。

        :param scaling_policy_type: The scaling_policy_type of this ScalingPolicyDetail.
        :type: str
        """
        self._scaling_policy_type = scaling_policy_type

    @property
    def alarm_id(self):
        """Gets the alarm_id of this ScalingPolicyDetail.

        告警ID，即告警规则的ID，当scaling_policy_type为ALARM时该项必选，此时scheduled_policy不生效。创建告警策略成功后，会自动为该告警ID对应的告警规则的alarm_actions字段增加类型为autoscaling的告警触发动作。告警ID通过查询云监控告警规则列表获取，详见《云监控API参考》的“查询告警规则列表”。

        :return: The alarm_id of this ScalingPolicyDetail.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this ScalingPolicyDetail.

        告警ID，即告警规则的ID，当scaling_policy_type为ALARM时该项必选，此时scheduled_policy不生效。创建告警策略成功后，会自动为该告警ID对应的告警规则的alarm_actions字段增加类型为autoscaling的告警触发动作。告警ID通过查询云监控告警规则列表获取，详见《云监控API参考》的“查询告警规则列表”。

        :param alarm_id: The alarm_id of this ScalingPolicyDetail.
        :type: str
        """
        self._alarm_id = alarm_id

    @property
    def scheduled_policy(self):
        """Gets the scheduled_policy of this ScalingPolicyDetail.


        :return: The scheduled_policy of this ScalingPolicyDetail.
        :rtype: ScheduledPolicy
        """
        return self._scheduled_policy

    @scheduled_policy.setter
    def scheduled_policy(self, scheduled_policy):
        """Sets the scheduled_policy of this ScalingPolicyDetail.


        :param scheduled_policy: The scheduled_policy of this ScalingPolicyDetail.
        :type: ScheduledPolicy
        """
        self._scheduled_policy = scheduled_policy

    @property
    def scaling_policy_action(self):
        """Gets the scaling_policy_action of this ScalingPolicyDetail.


        :return: The scaling_policy_action of this ScalingPolicyDetail.
        :rtype: ScalingPolicyAction
        """
        return self._scaling_policy_action

    @scaling_policy_action.setter
    def scaling_policy_action(self, scaling_policy_action):
        """Sets the scaling_policy_action of this ScalingPolicyDetail.


        :param scaling_policy_action: The scaling_policy_action of this ScalingPolicyDetail.
        :type: ScalingPolicyAction
        """
        self._scaling_policy_action = scaling_policy_action

    @property
    def cool_down_time(self):
        """Gets the cool_down_time of this ScalingPolicyDetail.

        冷却时间，取值范围0-86400，默认为300，单位是秒。

        :return: The cool_down_time of this ScalingPolicyDetail.
        :rtype: int
        """
        return self._cool_down_time

    @cool_down_time.setter
    def cool_down_time(self, cool_down_time):
        """Sets the cool_down_time of this ScalingPolicyDetail.

        冷却时间，取值范围0-86400，默认为300，单位是秒。

        :param cool_down_time: The cool_down_time of this ScalingPolicyDetail.
        :type: int
        """
        self._cool_down_time = cool_down_time

    @property
    def create_time(self):
        """Gets the create_time of this ScalingPolicyDetail.

        创建伸缩策略时间，遵循UTC时间。

        :return: The create_time of this ScalingPolicyDetail.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ScalingPolicyDetail.

        创建伸缩策略时间，遵循UTC时间。

        :param create_time: The create_time of this ScalingPolicyDetail.
        :type: datetime
        """
        self._create_time = create_time

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScalingPolicyDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
