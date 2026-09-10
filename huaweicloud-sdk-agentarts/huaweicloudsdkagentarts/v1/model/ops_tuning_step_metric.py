# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsTuningStepMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'step': 'int',
        'reward_value': 'float',
        'eval_reward_value': 'float',
        'time_consume': 'float',
        'response_length': 'float'
    }

    attribute_map = {
        'step': 'step',
        'reward_value': 'reward_value',
        'eval_reward_value': 'eval_reward_value',
        'time_consume': 'time_consume',
        'response_length': 'response_length'
    }

    def __init__(self, step=None, reward_value=None, eval_reward_value=None, time_consume=None, response_length=None):
        r"""OpsTuningStepMetric

        The model defined in huaweicloud sdk

        :param step: **参数解释：** 训练迭代步数，单位：step。  **取值范围：** 大于等于0的整数。
        :type step: int
        :param reward_value: **参数解释：** 在该步数下计算得出的奖励值，反映模型生成结果的质量。  **取值范围：** 浮点数。
        :type reward_value: float
        :param eval_reward_value: **参数解释：** 在该步数下计算得出验证集上的奖励值，反映模型生成结果的质量。  **取值范围：** 浮点数。
        :type eval_reward_value: float
        :param time_consume: **参数解释：** 该步数的耗时时长，单位：秒。  **取值范围**： 大于等于0的浮点数。
        :type time_consume: float
        :param response_length: **参数解释：** 模型在该步数生成的平均响应长度，单位：token。  **取值范围：** 大于等于0的浮点数。
        :type response_length: float
        """
        
        

        self._step = None
        self._reward_value = None
        self._eval_reward_value = None
        self._time_consume = None
        self._response_length = None
        self.discriminator = None

        if step is not None:
            self.step = step
        if reward_value is not None:
            self.reward_value = reward_value
        if eval_reward_value is not None:
            self.eval_reward_value = eval_reward_value
        if time_consume is not None:
            self.time_consume = time_consume
        if response_length is not None:
            self.response_length = response_length

    @property
    def step(self):
        r"""Gets the step of this OpsTuningStepMetric.

        **参数解释：** 训练迭代步数，单位：step。  **取值范围：** 大于等于0的整数。

        :return: The step of this OpsTuningStepMetric.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this OpsTuningStepMetric.

        **参数解释：** 训练迭代步数，单位：step。  **取值范围：** 大于等于0的整数。

        :param step: The step of this OpsTuningStepMetric.
        :type step: int
        """
        self._step = step

    @property
    def reward_value(self):
        r"""Gets the reward_value of this OpsTuningStepMetric.

        **参数解释：** 在该步数下计算得出的奖励值，反映模型生成结果的质量。  **取值范围：** 浮点数。

        :return: The reward_value of this OpsTuningStepMetric.
        :rtype: float
        """
        return self._reward_value

    @reward_value.setter
    def reward_value(self, reward_value):
        r"""Sets the reward_value of this OpsTuningStepMetric.

        **参数解释：** 在该步数下计算得出的奖励值，反映模型生成结果的质量。  **取值范围：** 浮点数。

        :param reward_value: The reward_value of this OpsTuningStepMetric.
        :type reward_value: float
        """
        self._reward_value = reward_value

    @property
    def eval_reward_value(self):
        r"""Gets the eval_reward_value of this OpsTuningStepMetric.

        **参数解释：** 在该步数下计算得出验证集上的奖励值，反映模型生成结果的质量。  **取值范围：** 浮点数。

        :return: The eval_reward_value of this OpsTuningStepMetric.
        :rtype: float
        """
        return self._eval_reward_value

    @eval_reward_value.setter
    def eval_reward_value(self, eval_reward_value):
        r"""Sets the eval_reward_value of this OpsTuningStepMetric.

        **参数解释：** 在该步数下计算得出验证集上的奖励值，反映模型生成结果的质量。  **取值范围：** 浮点数。

        :param eval_reward_value: The eval_reward_value of this OpsTuningStepMetric.
        :type eval_reward_value: float
        """
        self._eval_reward_value = eval_reward_value

    @property
    def time_consume(self):
        r"""Gets the time_consume of this OpsTuningStepMetric.

        **参数解释：** 该步数的耗时时长，单位：秒。  **取值范围**： 大于等于0的浮点数。

        :return: The time_consume of this OpsTuningStepMetric.
        :rtype: float
        """
        return self._time_consume

    @time_consume.setter
    def time_consume(self, time_consume):
        r"""Sets the time_consume of this OpsTuningStepMetric.

        **参数解释：** 该步数的耗时时长，单位：秒。  **取值范围**： 大于等于0的浮点数。

        :param time_consume: The time_consume of this OpsTuningStepMetric.
        :type time_consume: float
        """
        self._time_consume = time_consume

    @property
    def response_length(self):
        r"""Gets the response_length of this OpsTuningStepMetric.

        **参数解释：** 模型在该步数生成的平均响应长度，单位：token。  **取值范围：** 大于等于0的浮点数。

        :return: The response_length of this OpsTuningStepMetric.
        :rtype: float
        """
        return self._response_length

    @response_length.setter
    def response_length(self, response_length):
        r"""Sets the response_length of this OpsTuningStepMetric.

        **参数解释：** 模型在该步数生成的平均响应长度，单位：token。  **取值范围：** 大于等于0的浮点数。

        :param response_length: The response_length of this OpsTuningStepMetric.
        :type response_length: float
        """
        self._response_length = response_length

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
        if not isinstance(other, OpsTuningStepMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
