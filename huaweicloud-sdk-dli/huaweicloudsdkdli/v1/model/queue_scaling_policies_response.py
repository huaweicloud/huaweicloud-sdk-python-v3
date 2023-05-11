# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueueScalingPoliciesResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'priority': 'int',
        'impact_start_time': 'str',
        'impact_stop_time': 'str',
        'min_cu': 'int',
        'max_cu': 'int'
    }

    attribute_map = {
        'priority': 'priority',
        'impact_start_time': 'impact_start_time',
        'impact_stop_time': 'impact_stop_time',
        'min_cu': 'min_cu',
        'max_cu': 'max_cu'
    }

    def __init__(self, priority=None, impact_start_time=None, impact_stop_time=None, min_cu=None, max_cu=None):
        """QueueScalingPoliciesResponse

        The model defined in huaweicloud sdk

        :param priority: 策略优先级1-100，100优先级最高
        :type priority: int
        :param impact_start_time: 开始时间
        :type impact_start_time: str
        :param impact_stop_time: 结束时间
        :type impact_stop_time: str
        :param min_cu: 最小cu数量
        :type min_cu: int
        :param max_cu: 最大cu数量
        :type max_cu: int
        """
        
        

        self._priority = None
        self._impact_start_time = None
        self._impact_stop_time = None
        self._min_cu = None
        self._max_cu = None
        self.discriminator = None

        if priority is not None:
            self.priority = priority
        if impact_start_time is not None:
            self.impact_start_time = impact_start_time
        if impact_stop_time is not None:
            self.impact_stop_time = impact_stop_time
        if min_cu is not None:
            self.min_cu = min_cu
        if max_cu is not None:
            self.max_cu = max_cu

    @property
    def priority(self):
        """Gets the priority of this QueueScalingPoliciesResponse.

        策略优先级1-100，100优先级最高

        :return: The priority of this QueueScalingPoliciesResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this QueueScalingPoliciesResponse.

        策略优先级1-100，100优先级最高

        :param priority: The priority of this QueueScalingPoliciesResponse.
        :type priority: int
        """
        self._priority = priority

    @property
    def impact_start_time(self):
        """Gets the impact_start_time of this QueueScalingPoliciesResponse.

        开始时间

        :return: The impact_start_time of this QueueScalingPoliciesResponse.
        :rtype: str
        """
        return self._impact_start_time

    @impact_start_time.setter
    def impact_start_time(self, impact_start_time):
        """Sets the impact_start_time of this QueueScalingPoliciesResponse.

        开始时间

        :param impact_start_time: The impact_start_time of this QueueScalingPoliciesResponse.
        :type impact_start_time: str
        """
        self._impact_start_time = impact_start_time

    @property
    def impact_stop_time(self):
        """Gets the impact_stop_time of this QueueScalingPoliciesResponse.

        结束时间

        :return: The impact_stop_time of this QueueScalingPoliciesResponse.
        :rtype: str
        """
        return self._impact_stop_time

    @impact_stop_time.setter
    def impact_stop_time(self, impact_stop_time):
        """Sets the impact_stop_time of this QueueScalingPoliciesResponse.

        结束时间

        :param impact_stop_time: The impact_stop_time of this QueueScalingPoliciesResponse.
        :type impact_stop_time: str
        """
        self._impact_stop_time = impact_stop_time

    @property
    def min_cu(self):
        """Gets the min_cu of this QueueScalingPoliciesResponse.

        最小cu数量

        :return: The min_cu of this QueueScalingPoliciesResponse.
        :rtype: int
        """
        return self._min_cu

    @min_cu.setter
    def min_cu(self, min_cu):
        """Sets the min_cu of this QueueScalingPoliciesResponse.

        最小cu数量

        :param min_cu: The min_cu of this QueueScalingPoliciesResponse.
        :type min_cu: int
        """
        self._min_cu = min_cu

    @property
    def max_cu(self):
        """Gets the max_cu of this QueueScalingPoliciesResponse.

        最大cu数量

        :return: The max_cu of this QueueScalingPoliciesResponse.
        :rtype: int
        """
        return self._max_cu

    @max_cu.setter
    def max_cu(self, max_cu):
        """Sets the max_cu of this QueueScalingPoliciesResponse.

        最大cu数量

        :param max_cu: The max_cu of this QueueScalingPoliciesResponse.
        :type max_cu: int
        """
        self._max_cu = max_cu

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
        if not isinstance(other, QueueScalingPoliciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
