# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DurationStrategies:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'strategy': 'str',
        'estimated_upgrade_duration': 'int'
    }

    attribute_map = {
        'strategy': 'strategy',
        'estimated_upgrade_duration': 'estimated_upgrade_duration'
    }

    def __init__(self, strategy=None, estimated_upgrade_duration=None):
        """DurationStrategies

        The model defined in huaweicloud sdk

        :param strategy: 升级策略 - minimized_interrupt_time，表示最短中断时间 - minimized_upgrade_time，最短升级时长
        :type strategy: str
        :param estimated_upgrade_duration: 升级时长，单位为分钟
        :type estimated_upgrade_duration: int
        """
        
        

        self._strategy = None
        self._estimated_upgrade_duration = None
        self.discriminator = None

        self.strategy = strategy
        self.estimated_upgrade_duration = estimated_upgrade_duration

    @property
    def strategy(self):
        """Gets the strategy of this DurationStrategies.

        升级策略 - minimized_interrupt_time，表示最短中断时间 - minimized_upgrade_time，最短升级时长

        :return: The strategy of this DurationStrategies.
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """Sets the strategy of this DurationStrategies.

        升级策略 - minimized_interrupt_time，表示最短中断时间 - minimized_upgrade_time，最短升级时长

        :param strategy: The strategy of this DurationStrategies.
        :type strategy: str
        """
        self._strategy = strategy

    @property
    def estimated_upgrade_duration(self):
        """Gets the estimated_upgrade_duration of this DurationStrategies.

        升级时长，单位为分钟

        :return: The estimated_upgrade_duration of this DurationStrategies.
        :rtype: int
        """
        return self._estimated_upgrade_duration

    @estimated_upgrade_duration.setter
    def estimated_upgrade_duration(self, estimated_upgrade_duration):
        """Sets the estimated_upgrade_duration of this DurationStrategies.

        升级时长，单位为分钟

        :param estimated_upgrade_duration: The estimated_upgrade_duration of this DurationStrategies.
        :type estimated_upgrade_duration: int
        """
        self._estimated_upgrade_duration = estimated_upgrade_duration

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
        if not isinstance(other, DurationStrategies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
