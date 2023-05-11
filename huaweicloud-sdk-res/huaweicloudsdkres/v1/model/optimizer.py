# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Optimizer:

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
        'learning_rate': 'float',
        'initial_accumulator_value': 'float',
        'lambda1': 'float',
        'lambda2': 'float',
        'epsilon': 'float',
        'decay_rate': 'float',
        'decay_steps': 'float'
    }

    attribute_map = {
        'type': 'type',
        'learning_rate': 'learning_rate',
        'initial_accumulator_value': 'initial_accumulator_value',
        'lambda1': 'lambda1',
        'lambda2': 'lambda2',
        'epsilon': 'epsilon',
        'decay_rate': 'decay_rate',
        'decay_steps': 'decay_steps'
    }

    def __init__(self, type=None, learning_rate=None, initial_accumulator_value=None, lambda1=None, lambda2=None, epsilon=None, decay_rate=None, decay_steps=None):
        """Optimizer

        The model defined in huaweicloud sdk

        :param type: 优化器类型。
        :type type: str
        :param learning_rate: 学习率。
        :type learning_rate: float
        :param initial_accumulator_value: 初始梯度累加和。
        :type initial_accumulator_value: float
        :param lambda1: L1正则项系数。
        :type lambda1: float
        :param lambda2: L2正则项系数。
        :type lambda2: float
        :param epsilon: 数值稳定常量。
        :type epsilon: float
        :param decay_rate: 衰减因子。
        :type decay_rate: float
        :param decay_steps: 衰减步长。
        :type decay_steps: float
        """
        
        

        self._type = None
        self._learning_rate = None
        self._initial_accumulator_value = None
        self._lambda1 = None
        self._lambda2 = None
        self._epsilon = None
        self._decay_rate = None
        self._decay_steps = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if learning_rate is not None:
            self.learning_rate = learning_rate
        if initial_accumulator_value is not None:
            self.initial_accumulator_value = initial_accumulator_value
        if lambda1 is not None:
            self.lambda1 = lambda1
        if lambda2 is not None:
            self.lambda2 = lambda2
        if epsilon is not None:
            self.epsilon = epsilon
        if decay_rate is not None:
            self.decay_rate = decay_rate
        if decay_steps is not None:
            self.decay_steps = decay_steps

    @property
    def type(self):
        """Gets the type of this Optimizer.

        优化器类型。

        :return: The type of this Optimizer.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Optimizer.

        优化器类型。

        :param type: The type of this Optimizer.
        :type type: str
        """
        self._type = type

    @property
    def learning_rate(self):
        """Gets the learning_rate of this Optimizer.

        学习率。

        :return: The learning_rate of this Optimizer.
        :rtype: float
        """
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, learning_rate):
        """Sets the learning_rate of this Optimizer.

        学习率。

        :param learning_rate: The learning_rate of this Optimizer.
        :type learning_rate: float
        """
        self._learning_rate = learning_rate

    @property
    def initial_accumulator_value(self):
        """Gets the initial_accumulator_value of this Optimizer.

        初始梯度累加和。

        :return: The initial_accumulator_value of this Optimizer.
        :rtype: float
        """
        return self._initial_accumulator_value

    @initial_accumulator_value.setter
    def initial_accumulator_value(self, initial_accumulator_value):
        """Sets the initial_accumulator_value of this Optimizer.

        初始梯度累加和。

        :param initial_accumulator_value: The initial_accumulator_value of this Optimizer.
        :type initial_accumulator_value: float
        """
        self._initial_accumulator_value = initial_accumulator_value

    @property
    def lambda1(self):
        """Gets the lambda1 of this Optimizer.

        L1正则项系数。

        :return: The lambda1 of this Optimizer.
        :rtype: float
        """
        return self._lambda1

    @lambda1.setter
    def lambda1(self, lambda1):
        """Sets the lambda1 of this Optimizer.

        L1正则项系数。

        :param lambda1: The lambda1 of this Optimizer.
        :type lambda1: float
        """
        self._lambda1 = lambda1

    @property
    def lambda2(self):
        """Gets the lambda2 of this Optimizer.

        L2正则项系数。

        :return: The lambda2 of this Optimizer.
        :rtype: float
        """
        return self._lambda2

    @lambda2.setter
    def lambda2(self, lambda2):
        """Sets the lambda2 of this Optimizer.

        L2正则项系数。

        :param lambda2: The lambda2 of this Optimizer.
        :type lambda2: float
        """
        self._lambda2 = lambda2

    @property
    def epsilon(self):
        """Gets the epsilon of this Optimizer.

        数值稳定常量。

        :return: The epsilon of this Optimizer.
        :rtype: float
        """
        return self._epsilon

    @epsilon.setter
    def epsilon(self, epsilon):
        """Sets the epsilon of this Optimizer.

        数值稳定常量。

        :param epsilon: The epsilon of this Optimizer.
        :type epsilon: float
        """
        self._epsilon = epsilon

    @property
    def decay_rate(self):
        """Gets the decay_rate of this Optimizer.

        衰减因子。

        :return: The decay_rate of this Optimizer.
        :rtype: float
        """
        return self._decay_rate

    @decay_rate.setter
    def decay_rate(self, decay_rate):
        """Sets the decay_rate of this Optimizer.

        衰减因子。

        :param decay_rate: The decay_rate of this Optimizer.
        :type decay_rate: float
        """
        self._decay_rate = decay_rate

    @property
    def decay_steps(self):
        """Gets the decay_steps of this Optimizer.

        衰减步长。

        :return: The decay_steps of this Optimizer.
        :rtype: float
        """
        return self._decay_steps

    @decay_steps.setter
    def decay_steps(self, decay_steps):
        """Sets the decay_steps of this Optimizer.

        衰减步长。

        :param decay_steps: The decay_steps of this Optimizer.
        :type decay_steps: float
        """
        self._decay_steps = decay_steps

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
        if not isinstance(other, Optimizer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
