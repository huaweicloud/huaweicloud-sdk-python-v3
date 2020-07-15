# coding: utf-8

import pprint
import re

import six





class Strategy:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'trigger': 'str',
        'event_valid_time': 'int'
    }

    attribute_map = {
        'trigger': 'trigger',
        'event_valid_time': 'event_valid_time'
    }

    def __init__(self, trigger=None, event_valid_time=None):
        """Strategy - a model defined in huaweicloud sdk"""
        
        

        self._trigger = None
        self._event_valid_time = None
        self.discriminator = None

        if trigger is not None:
            self.trigger = trigger
        if event_valid_time is not None:
            self.event_valid_time = event_valid_time

    @property
    def trigger(self):
        """Gets the trigger of this Strategy.

        规则条件触发的判断策略，默认为pulse。 - pulse：设备上报的数据满足条件则触发，不判断上一次上报的数据。 - reverse：设备上一次上报的数据不满足条件，本次上报的数据满足条件则触发。 

        :return: The trigger of this Strategy.
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this Strategy.

        规则条件触发的判断策略，默认为pulse。 - pulse：设备上报的数据满足条件则触发，不判断上一次上报的数据。 - reverse：设备上一次上报的数据不满足条件，本次上报的数据满足条件则触发。 

        :param trigger: The trigger of this Strategy.
        :type: str
        """
        self._trigger = trigger

    @property
    def event_valid_time(self):
        """Gets the event_valid_time of this Strategy.

        设备数据的有效时间，单位为秒，设备数据的产生时间以上报数据中的eventTime为基准。

        :return: The event_valid_time of this Strategy.
        :rtype: int
        """
        return self._event_valid_time

    @event_valid_time.setter
    def event_valid_time(self, event_valid_time):
        """Sets the event_valid_time of this Strategy.

        设备数据的有效时间，单位为秒，设备数据的产生时间以上报数据中的eventTime为基准。

        :param event_valid_time: The event_valid_time of this Strategy.
        :type: int
        """
        self._event_valid_time = event_valid_time

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
        if not isinstance(other, Strategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
