# coding: utf-8

import pprint
import re

import six





class RuleCondition:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'device_property_condition': 'DeviceDataCondition',
        'simple_timer_condition': 'SimpleTimerType',
        'daily_timer_condition': 'DailyTimerType',
        'device_message_condition': 'DeviceMessageCondition',
        'device_status_condition': 'DeviceStatusCondition'
    }

    attribute_map = {
        'type': 'type',
        'device_property_condition': 'device_property_condition',
        'simple_timer_condition': 'simple_timer_condition',
        'daily_timer_condition': 'daily_timer_condition',
        'device_message_condition': 'device_message_condition',
        'device_status_condition': 'device_status_condition'
    }

    def __init__(self, type=None, device_property_condition=None, simple_timer_condition=None, daily_timer_condition=None, device_message_condition=None, device_status_condition=None):
        """RuleCondition - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._device_property_condition = None
        self._simple_timer_condition = None
        self._daily_timer_condition = None
        self._device_message_condition = None
        self._device_status_condition = None
        self.discriminator = None

        self.type = type
        if device_property_condition is not None:
            self.device_property_condition = device_property_condition
        if simple_timer_condition is not None:
            self.simple_timer_condition = simple_timer_condition
        if daily_timer_condition is not None:
            self.daily_timer_condition = daily_timer_condition
        if device_message_condition is not None:
            self.device_message_condition = device_message_condition
        if device_status_condition is not None:
            self.device_status_condition = device_status_condition

    @property
    def type(self):
        """Gets the type of this RuleCondition.

        规则条件的类型，取值范围： - DEVICE_DATA：设备数据类型条件。 - SIMPLE_TIMER：简单定时类型条件。 - DAILY_TIMER：每日定时类型条件。 - DEVICE_STATUS：设备状态类型条件。 - DEVICE_LIFE_CYCLE：设备生命周期类型条件。 - DEVICE_MESSAGE：设备消息条件。 - MESSAGE_RESULTS：下行消息结果条件。 

        :return: The type of this RuleCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RuleCondition.

        规则条件的类型，取值范围： - DEVICE_DATA：设备数据类型条件。 - SIMPLE_TIMER：简单定时类型条件。 - DAILY_TIMER：每日定时类型条件。 - DEVICE_STATUS：设备状态类型条件。 - DEVICE_LIFE_CYCLE：设备生命周期类型条件。 - DEVICE_MESSAGE：设备消息条件。 - MESSAGE_RESULTS：下行消息结果条件。 

        :param type: The type of this RuleCondition.
        :type: str
        """
        self._type = type

    @property
    def device_property_condition(self):
        """Gets the device_property_condition of this RuleCondition.


        :return: The device_property_condition of this RuleCondition.
        :rtype: DeviceDataCondition
        """
        return self._device_property_condition

    @device_property_condition.setter
    def device_property_condition(self, device_property_condition):
        """Sets the device_property_condition of this RuleCondition.


        :param device_property_condition: The device_property_condition of this RuleCondition.
        :type: DeviceDataCondition
        """
        self._device_property_condition = device_property_condition

    @property
    def simple_timer_condition(self):
        """Gets the simple_timer_condition of this RuleCondition.


        :return: The simple_timer_condition of this RuleCondition.
        :rtype: SimpleTimerType
        """
        return self._simple_timer_condition

    @simple_timer_condition.setter
    def simple_timer_condition(self, simple_timer_condition):
        """Sets the simple_timer_condition of this RuleCondition.


        :param simple_timer_condition: The simple_timer_condition of this RuleCondition.
        :type: SimpleTimerType
        """
        self._simple_timer_condition = simple_timer_condition

    @property
    def daily_timer_condition(self):
        """Gets the daily_timer_condition of this RuleCondition.


        :return: The daily_timer_condition of this RuleCondition.
        :rtype: DailyTimerType
        """
        return self._daily_timer_condition

    @daily_timer_condition.setter
    def daily_timer_condition(self, daily_timer_condition):
        """Sets the daily_timer_condition of this RuleCondition.


        :param daily_timer_condition: The daily_timer_condition of this RuleCondition.
        :type: DailyTimerType
        """
        self._daily_timer_condition = daily_timer_condition

    @property
    def device_message_condition(self):
        """Gets the device_message_condition of this RuleCondition.


        :return: The device_message_condition of this RuleCondition.
        :rtype: DeviceMessageCondition
        """
        return self._device_message_condition

    @device_message_condition.setter
    def device_message_condition(self, device_message_condition):
        """Sets the device_message_condition of this RuleCondition.


        :param device_message_condition: The device_message_condition of this RuleCondition.
        :type: DeviceMessageCondition
        """
        self._device_message_condition = device_message_condition

    @property
    def device_status_condition(self):
        """Gets the device_status_condition of this RuleCondition.


        :return: The device_status_condition of this RuleCondition.
        :rtype: DeviceStatusCondition
        """
        return self._device_status_condition

    @device_status_condition.setter
    def device_status_condition(self, device_status_condition):
        """Sets the device_status_condition of this RuleCondition.


        :param device_status_condition: The device_status_condition of this RuleCondition.
        :type: DeviceStatusCondition
        """
        self._device_status_condition = device_status_condition

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
        if not isinstance(other, RuleCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
