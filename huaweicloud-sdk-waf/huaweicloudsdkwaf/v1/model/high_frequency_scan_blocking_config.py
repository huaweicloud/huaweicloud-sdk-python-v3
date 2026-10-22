# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HighFrequencyScanBlockingConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'PolicyAction',
        'time_range': 'int',
        'trigger_threshold': 'int',
        'max_num_triggered_rules': 'int',
        'blocking_period': 'int'
    }

    attribute_map = {
        'action': 'action',
        'time_range': 'time_range',
        'trigger_threshold': 'trigger_threshold',
        'max_num_triggered_rules': 'max_num_triggered_rules',
        'blocking_period': 'blocking_period'
    }

    def __init__(self, action=None, time_range=None, trigger_threshold=None, max_num_triggered_rules=None, blocking_period=None):
        r"""HighFrequencyScanBlockingConfig

        The model defined in huaweicloud sdk

        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.PolicyAction`
        :param time_range: 检测时间范围，单位秒
        :type time_range: int
        :param trigger_threshold: 触发阈值，在检测时间内扫描次数超过该值则触发封禁
        :type trigger_threshold: int
        :param max_num_triggered_rules: 最大触发规则数，在检测时间内命中不同防护规则的数量达到该值时触发封禁
        :type max_num_triggered_rules: int
        :param blocking_period: 封禁周期，单位秒
        :type blocking_period: int
        """
        
        

        self._action = None
        self._time_range = None
        self._trigger_threshold = None
        self._max_num_triggered_rules = None
        self._blocking_period = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if time_range is not None:
            self.time_range = time_range
        if trigger_threshold is not None:
            self.trigger_threshold = trigger_threshold
        if max_num_triggered_rules is not None:
            self.max_num_triggered_rules = max_num_triggered_rules
        if blocking_period is not None:
            self.blocking_period = blocking_period

    @property
    def action(self):
        r"""Gets the action of this HighFrequencyScanBlockingConfig.

        :return: The action of this HighFrequencyScanBlockingConfig.
        :rtype: :class:`huaweicloudsdkwaf.v1.PolicyAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this HighFrequencyScanBlockingConfig.

        :param action: The action of this HighFrequencyScanBlockingConfig.
        :type action: :class:`huaweicloudsdkwaf.v1.PolicyAction`
        """
        self._action = action

    @property
    def time_range(self):
        r"""Gets the time_range of this HighFrequencyScanBlockingConfig.

        检测时间范围，单位秒

        :return: The time_range of this HighFrequencyScanBlockingConfig.
        :rtype: int
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        r"""Sets the time_range of this HighFrequencyScanBlockingConfig.

        检测时间范围，单位秒

        :param time_range: The time_range of this HighFrequencyScanBlockingConfig.
        :type time_range: int
        """
        self._time_range = time_range

    @property
    def trigger_threshold(self):
        r"""Gets the trigger_threshold of this HighFrequencyScanBlockingConfig.

        触发阈值，在检测时间内扫描次数超过该值则触发封禁

        :return: The trigger_threshold of this HighFrequencyScanBlockingConfig.
        :rtype: int
        """
        return self._trigger_threshold

    @trigger_threshold.setter
    def trigger_threshold(self, trigger_threshold):
        r"""Sets the trigger_threshold of this HighFrequencyScanBlockingConfig.

        触发阈值，在检测时间内扫描次数超过该值则触发封禁

        :param trigger_threshold: The trigger_threshold of this HighFrequencyScanBlockingConfig.
        :type trigger_threshold: int
        """
        self._trigger_threshold = trigger_threshold

    @property
    def max_num_triggered_rules(self):
        r"""Gets the max_num_triggered_rules of this HighFrequencyScanBlockingConfig.

        最大触发规则数，在检测时间内命中不同防护规则的数量达到该值时触发封禁

        :return: The max_num_triggered_rules of this HighFrequencyScanBlockingConfig.
        :rtype: int
        """
        return self._max_num_triggered_rules

    @max_num_triggered_rules.setter
    def max_num_triggered_rules(self, max_num_triggered_rules):
        r"""Sets the max_num_triggered_rules of this HighFrequencyScanBlockingConfig.

        最大触发规则数，在检测时间内命中不同防护规则的数量达到该值时触发封禁

        :param max_num_triggered_rules: The max_num_triggered_rules of this HighFrequencyScanBlockingConfig.
        :type max_num_triggered_rules: int
        """
        self._max_num_triggered_rules = max_num_triggered_rules

    @property
    def blocking_period(self):
        r"""Gets the blocking_period of this HighFrequencyScanBlockingConfig.

        封禁周期，单位秒

        :return: The blocking_period of this HighFrequencyScanBlockingConfig.
        :rtype: int
        """
        return self._blocking_period

    @blocking_period.setter
    def blocking_period(self, blocking_period):
        r"""Sets the blocking_period of this HighFrequencyScanBlockingConfig.

        封禁周期，单位秒

        :param blocking_period: The blocking_period of this HighFrequencyScanBlockingConfig.
        :type blocking_period: int
        """
        self._blocking_period = blocking_period

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HighFrequencyScanBlockingConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
