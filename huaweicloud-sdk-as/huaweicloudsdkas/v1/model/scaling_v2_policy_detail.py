# coding: utf-8

import pprint
import re

import six





class ScalingV2PolicyDetail:


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
        'scaling_policy_id': 'str',
        'scaling_resource_id': 'str',
        'scaling_resource_type': 'str',
        'policy_status': 'str',
        'scaling_policy_type': 'str',
        'alarm_id': 'str',
        'scheduled_policy': 'ScheduledPolicy',
        'scaling_policy_action': 'ScalingPolicyActionV2',
        'cool_down_time': 'int',
        'create_time': 'datetime',
        'meta_data': 'ScalingPolicyV2MetaData'
    }

    attribute_map = {
        'scaling_policy_name': 'scaling_policy_name',
        'scaling_policy_id': 'scaling_policy_id',
        'scaling_resource_id': 'scaling_resource_id',
        'scaling_resource_type': 'scaling_resource_type',
        'policy_status': 'policy_status',
        'scaling_policy_type': 'scaling_policy_type',
        'alarm_id': 'alarm_id',
        'scheduled_policy': 'scheduled_policy',
        'scaling_policy_action': 'scaling_policy_action',
        'cool_down_time': 'cool_down_time',
        'create_time': 'create_time',
        'meta_data': 'meta_data'
    }

    def __init__(self, scaling_policy_name=None, scaling_policy_id=None, scaling_resource_id=None, scaling_resource_type=None, policy_status=None, scaling_policy_type=None, alarm_id=None, scheduled_policy=None, scaling_policy_action=None, cool_down_time=None, create_time=None, meta_data=None):
        """ScalingV2PolicyDetail - a model defined in huaweicloud sdk"""
        
        

        self._scaling_policy_name = None
        self._scaling_policy_id = None
        self._scaling_resource_id = None
        self._scaling_resource_type = None
        self._policy_status = None
        self._scaling_policy_type = None
        self._alarm_id = None
        self._scheduled_policy = None
        self._scaling_policy_action = None
        self._cool_down_time = None
        self._create_time = None
        self._meta_data = None
        self.discriminator = None

        if scaling_policy_name is not None:
            self.scaling_policy_name = scaling_policy_name
        if scaling_policy_id is not None:
            self.scaling_policy_id = scaling_policy_id
        if scaling_resource_id is not None:
            self.scaling_resource_id = scaling_resource_id
        if scaling_resource_type is not None:
            self.scaling_resource_type = scaling_resource_type
        if policy_status is not None:
            self.policy_status = policy_status
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
        if meta_data is not None:
            self.meta_data = meta_data

    @property
    def scaling_policy_name(self):
        """Gets the scaling_policy_name of this ScalingV2PolicyDetail.

        伸缩策略名称。

        :return: The scaling_policy_name of this ScalingV2PolicyDetail.
        :rtype: str
        """
        return self._scaling_policy_name

    @scaling_policy_name.setter
    def scaling_policy_name(self, scaling_policy_name):
        """Sets the scaling_policy_name of this ScalingV2PolicyDetail.

        伸缩策略名称。

        :param scaling_policy_name: The scaling_policy_name of this ScalingV2PolicyDetail.
        :type: str
        """
        self._scaling_policy_name = scaling_policy_name

    @property
    def scaling_policy_id(self):
        """Gets the scaling_policy_id of this ScalingV2PolicyDetail.

        伸缩策略ID。

        :return: The scaling_policy_id of this ScalingV2PolicyDetail.
        :rtype: str
        """
        return self._scaling_policy_id

    @scaling_policy_id.setter
    def scaling_policy_id(self, scaling_policy_id):
        """Sets the scaling_policy_id of this ScalingV2PolicyDetail.

        伸缩策略ID。

        :param scaling_policy_id: The scaling_policy_id of this ScalingV2PolicyDetail.
        :type: str
        """
        self._scaling_policy_id = scaling_policy_id

    @property
    def scaling_resource_id(self):
        """Gets the scaling_resource_id of this ScalingV2PolicyDetail.

        伸缩资源ID。

        :return: The scaling_resource_id of this ScalingV2PolicyDetail.
        :rtype: str
        """
        return self._scaling_resource_id

    @scaling_resource_id.setter
    def scaling_resource_id(self, scaling_resource_id):
        """Sets the scaling_resource_id of this ScalingV2PolicyDetail.

        伸缩资源ID。

        :param scaling_resource_id: The scaling_resource_id of this ScalingV2PolicyDetail.
        :type: str
        """
        self._scaling_resource_id = scaling_resource_id

    @property
    def scaling_resource_type(self):
        """Gets the scaling_resource_type of this ScalingV2PolicyDetail.

        伸缩资源类型。伸缩组：SCALING_GROUP。带宽：BANDWIDTH。

        :return: The scaling_resource_type of this ScalingV2PolicyDetail.
        :rtype: str
        """
        return self._scaling_resource_type

    @scaling_resource_type.setter
    def scaling_resource_type(self, scaling_resource_type):
        """Sets the scaling_resource_type of this ScalingV2PolicyDetail.

        伸缩资源类型。伸缩组：SCALING_GROUP。带宽：BANDWIDTH。

        :param scaling_resource_type: The scaling_resource_type of this ScalingV2PolicyDetail.
        :type: str
        """
        self._scaling_resource_type = scaling_resource_type

    @property
    def policy_status(self):
        """Gets the policy_status of this ScalingV2PolicyDetail.

        伸缩策略状态。INSERVICE：使用中。PAUSED：停止。EXECUTING：执行中。

        :return: The policy_status of this ScalingV2PolicyDetail.
        :rtype: str
        """
        return self._policy_status

    @policy_status.setter
    def policy_status(self, policy_status):
        """Sets the policy_status of this ScalingV2PolicyDetail.

        伸缩策略状态。INSERVICE：使用中。PAUSED：停止。EXECUTING：执行中。

        :param policy_status: The policy_status of this ScalingV2PolicyDetail.
        :type: str
        """
        self._policy_status = policy_status

    @property
    def scaling_policy_type(self):
        """Gets the scaling_policy_type of this ScalingV2PolicyDetail.

        伸缩策略类型：ALARM：告警策略，此时alarm_id有返回，scheduled_policy不会返回。SCHEDULED：定时策略，此时alarm_id不会返回，scheduled_policy有返回，并且recurrence_type、recurrence_value、start_time和end_time不会返回。RECURRENCE：周期策略，此时alarm_id不会返回，scheduled_policy有返回，并且recurrence_type、recurrence_value、start_time和end_time有返回。

        :return: The scaling_policy_type of this ScalingV2PolicyDetail.
        :rtype: str
        """
        return self._scaling_policy_type

    @scaling_policy_type.setter
    def scaling_policy_type(self, scaling_policy_type):
        """Sets the scaling_policy_type of this ScalingV2PolicyDetail.

        伸缩策略类型：ALARM：告警策略，此时alarm_id有返回，scheduled_policy不会返回。SCHEDULED：定时策略，此时alarm_id不会返回，scheduled_policy有返回，并且recurrence_type、recurrence_value、start_time和end_time不会返回。RECURRENCE：周期策略，此时alarm_id不会返回，scheduled_policy有返回，并且recurrence_type、recurrence_value、start_time和end_time有返回。

        :param scaling_policy_type: The scaling_policy_type of this ScalingV2PolicyDetail.
        :type: str
        """
        self._scaling_policy_type = scaling_policy_type

    @property
    def alarm_id(self):
        """Gets the alarm_id of this ScalingV2PolicyDetail.

        告警ID。

        :return: The alarm_id of this ScalingV2PolicyDetail.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this ScalingV2PolicyDetail.

        告警ID。

        :param alarm_id: The alarm_id of this ScalingV2PolicyDetail.
        :type: str
        """
        self._alarm_id = alarm_id

    @property
    def scheduled_policy(self):
        """Gets the scheduled_policy of this ScalingV2PolicyDetail.


        :return: The scheduled_policy of this ScalingV2PolicyDetail.
        :rtype: ScheduledPolicy
        """
        return self._scheduled_policy

    @scheduled_policy.setter
    def scheduled_policy(self, scheduled_policy):
        """Sets the scheduled_policy of this ScalingV2PolicyDetail.


        :param scheduled_policy: The scheduled_policy of this ScalingV2PolicyDetail.
        :type: ScheduledPolicy
        """
        self._scheduled_policy = scheduled_policy

    @property
    def scaling_policy_action(self):
        """Gets the scaling_policy_action of this ScalingV2PolicyDetail.


        :return: The scaling_policy_action of this ScalingV2PolicyDetail.
        :rtype: ScalingPolicyActionV2
        """
        return self._scaling_policy_action

    @scaling_policy_action.setter
    def scaling_policy_action(self, scaling_policy_action):
        """Sets the scaling_policy_action of this ScalingV2PolicyDetail.


        :param scaling_policy_action: The scaling_policy_action of this ScalingV2PolicyDetail.
        :type: ScalingPolicyActionV2
        """
        self._scaling_policy_action = scaling_policy_action

    @property
    def cool_down_time(self):
        """Gets the cool_down_time of this ScalingV2PolicyDetail.

        冷却时间，取值范围0-86400，默认为300，单位是秒。

        :return: The cool_down_time of this ScalingV2PolicyDetail.
        :rtype: int
        """
        return self._cool_down_time

    @cool_down_time.setter
    def cool_down_time(self, cool_down_time):
        """Sets the cool_down_time of this ScalingV2PolicyDetail.

        冷却时间，取值范围0-86400，默认为300，单位是秒。

        :param cool_down_time: The cool_down_time of this ScalingV2PolicyDetail.
        :type: int
        """
        self._cool_down_time = cool_down_time

    @property
    def create_time(self):
        """Gets the create_time of this ScalingV2PolicyDetail.

        创建伸缩策略时间，遵循UTC时间

        :return: The create_time of this ScalingV2PolicyDetail.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ScalingV2PolicyDetail.

        创建伸缩策略时间，遵循UTC时间

        :param create_time: The create_time of this ScalingV2PolicyDetail.
        :type: datetime
        """
        self._create_time = create_time

    @property
    def meta_data(self):
        """Gets the meta_data of this ScalingV2PolicyDetail.


        :return: The meta_data of this ScalingV2PolicyDetail.
        :rtype: ScalingPolicyV2MetaData
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this ScalingV2PolicyDetail.


        :param meta_data: The meta_data of this ScalingV2PolicyDetail.
        :type: ScalingPolicyV2MetaData
        """
        self._meta_data = meta_data

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
        if not isinstance(other, ScalingV2PolicyDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
