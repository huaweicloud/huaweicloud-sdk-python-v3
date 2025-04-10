# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScalingHistory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule': 'str',
        'action': 'str',
        'count_before_scale': 'int',
        'count_after_scale': 'int',
        'state': 'str',
        'time': 'str'
    }

    attribute_map = {
        'rule': 'rule',
        'action': 'action',
        'count_before_scale': 'count_before_scale',
        'count_after_scale': 'count_after_scale',
        'state': 'state',
        'time': 'time'
    }

    def __init__(self, rule=None, action=None, count_before_scale=None, count_after_scale=None, state=None, time=None):
        r"""ScalingHistory

        The model defined in huaweicloud sdk

        :param rule: 策略规则
        :type rule: str
        :param action: 执行动作
        :type action: str
        :param count_before_scale: 伸缩前节点数
        :type count_before_scale: int
        :param count_after_scale: 伸缩后节点数
        :type count_after_scale: int
        :param state: 执行状态
        :type state: str
        :param time: 执行时间
        :type time: str
        """
        
        

        self._rule = None
        self._action = None
        self._count_before_scale = None
        self._count_after_scale = None
        self._state = None
        self._time = None
        self.discriminator = None

        self.rule = rule
        self.action = action
        self.count_before_scale = count_before_scale
        self.count_after_scale = count_after_scale
        self.state = state
        self.time = time

    @property
    def rule(self):
        r"""Gets the rule of this ScalingHistory.

        策略规则

        :return: The rule of this ScalingHistory.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this ScalingHistory.

        策略规则

        :param rule: The rule of this ScalingHistory.
        :type rule: str
        """
        self._rule = rule

    @property
    def action(self):
        r"""Gets the action of this ScalingHistory.

        执行动作

        :return: The action of this ScalingHistory.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ScalingHistory.

        执行动作

        :param action: The action of this ScalingHistory.
        :type action: str
        """
        self._action = action

    @property
    def count_before_scale(self):
        r"""Gets the count_before_scale of this ScalingHistory.

        伸缩前节点数

        :return: The count_before_scale of this ScalingHistory.
        :rtype: int
        """
        return self._count_before_scale

    @count_before_scale.setter
    def count_before_scale(self, count_before_scale):
        r"""Sets the count_before_scale of this ScalingHistory.

        伸缩前节点数

        :param count_before_scale: The count_before_scale of this ScalingHistory.
        :type count_before_scale: int
        """
        self._count_before_scale = count_before_scale

    @property
    def count_after_scale(self):
        r"""Gets the count_after_scale of this ScalingHistory.

        伸缩后节点数

        :return: The count_after_scale of this ScalingHistory.
        :rtype: int
        """
        return self._count_after_scale

    @count_after_scale.setter
    def count_after_scale(self, count_after_scale):
        r"""Sets the count_after_scale of this ScalingHistory.

        伸缩后节点数

        :param count_after_scale: The count_after_scale of this ScalingHistory.
        :type count_after_scale: int
        """
        self._count_after_scale = count_after_scale

    @property
    def state(self):
        r"""Gets the state of this ScalingHistory.

        执行状态

        :return: The state of this ScalingHistory.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ScalingHistory.

        执行状态

        :param state: The state of this ScalingHistory.
        :type state: str
        """
        self._state = state

    @property
    def time(self):
        r"""Gets the time of this ScalingHistory.

        执行时间

        :return: The time of this ScalingHistory.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ScalingHistory.

        执行时间

        :param time: The time of this ScalingHistory.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, ScalingHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
