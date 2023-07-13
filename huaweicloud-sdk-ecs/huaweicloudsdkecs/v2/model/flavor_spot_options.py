# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorSpotOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'longest_spot_duration_hours': 'int',
        'largest_spot_duration_count': 'int',
        'interruption_policy': 'str'
    }

    attribute_map = {
        'longest_spot_duration_hours': 'longest_spot_duration_hours',
        'largest_spot_duration_count': 'largest_spot_duration_count',
        'interruption_policy': 'interruption_policy'
    }

    def __init__(self, longest_spot_duration_hours=None, largest_spot_duration_count=None, interruption_policy=None):
        """FlavorSpotOptions

        The model defined in huaweicloud sdk

        :param longest_spot_duration_hours: 购买的竞价实例时长
        :type longest_spot_duration_hours: int
        :param largest_spot_duration_count: 购买的“竞价实例时长”的个数。
        :type largest_spot_duration_count: int
        :param interruption_policy: 竞价实例中断策略。  - immediate：立即释放 - delay：延迟释放
        :type interruption_policy: str
        """
        
        

        self._longest_spot_duration_hours = None
        self._largest_spot_duration_count = None
        self._interruption_policy = None
        self.discriminator = None

        if longest_spot_duration_hours is not None:
            self.longest_spot_duration_hours = longest_spot_duration_hours
        if largest_spot_duration_count is not None:
            self.largest_spot_duration_count = largest_spot_duration_count
        if interruption_policy is not None:
            self.interruption_policy = interruption_policy

    @property
    def longest_spot_duration_hours(self):
        """Gets the longest_spot_duration_hours of this FlavorSpotOptions.

        购买的竞价实例时长

        :return: The longest_spot_duration_hours of this FlavorSpotOptions.
        :rtype: int
        """
        return self._longest_spot_duration_hours

    @longest_spot_duration_hours.setter
    def longest_spot_duration_hours(self, longest_spot_duration_hours):
        """Sets the longest_spot_duration_hours of this FlavorSpotOptions.

        购买的竞价实例时长

        :param longest_spot_duration_hours: The longest_spot_duration_hours of this FlavorSpotOptions.
        :type longest_spot_duration_hours: int
        """
        self._longest_spot_duration_hours = longest_spot_duration_hours

    @property
    def largest_spot_duration_count(self):
        """Gets the largest_spot_duration_count of this FlavorSpotOptions.

        购买的“竞价实例时长”的个数。

        :return: The largest_spot_duration_count of this FlavorSpotOptions.
        :rtype: int
        """
        return self._largest_spot_duration_count

    @largest_spot_duration_count.setter
    def largest_spot_duration_count(self, largest_spot_duration_count):
        """Sets the largest_spot_duration_count of this FlavorSpotOptions.

        购买的“竞价实例时长”的个数。

        :param largest_spot_duration_count: The largest_spot_duration_count of this FlavorSpotOptions.
        :type largest_spot_duration_count: int
        """
        self._largest_spot_duration_count = largest_spot_duration_count

    @property
    def interruption_policy(self):
        """Gets the interruption_policy of this FlavorSpotOptions.

        竞价实例中断策略。  - immediate：立即释放 - delay：延迟释放

        :return: The interruption_policy of this FlavorSpotOptions.
        :rtype: str
        """
        return self._interruption_policy

    @interruption_policy.setter
    def interruption_policy(self, interruption_policy):
        """Sets the interruption_policy of this FlavorSpotOptions.

        竞价实例中断策略。  - immediate：立即释放 - delay：延迟释放

        :param interruption_policy: The interruption_policy of this FlavorSpotOptions.
        :type interruption_policy: str
        """
        self._interruption_policy = interruption_policy

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
        if not isinstance(other, FlavorSpotOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
