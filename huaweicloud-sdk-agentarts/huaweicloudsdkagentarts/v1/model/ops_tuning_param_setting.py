# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsTuningParamSetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'actor_optimizer_lr': 'str',
        'train_batch_size': 'int',
        'rollout_num': 'int',
        'epoch_num': 'int',
        'max_length': 'int',
        'ckpt_save_step': 'int'
    }

    attribute_map = {
        'actor_optimizer_lr': 'actor_optimizer_lr',
        'train_batch_size': 'train_batch_size',
        'rollout_num': 'rollout_num',
        'epoch_num': 'epoch_num',
        'max_length': 'max_length',
        'ckpt_save_step': 'ckpt_save_step'
    }

    def __init__(self, actor_optimizer_lr=None, train_batch_size=None, rollout_num=None, epoch_num=None, max_length=None, ckpt_save_step=None):
        r"""OpsTuningParamSetting

        The model defined in huaweicloud sdk

        :param actor_optimizer_lr: **参数解释：** 优化器学习率，控制模型参数更新的步长。  **约束限制：** 数值过大可能导致训练震荡，过小可能导致收敛缓慢。  **取值范围：** 科学计数法字符串，如1.0E-5。  **默认取值：** 无
        :type actor_optimizer_lr: str
        :param train_batch_size: **参数解释：** 批大小，单次训练迭代中使用的样本数量。  **约束限制：** 不涉及  **取值范围：** 正整数，单位为个样本。  **默认取值：** 无
        :type train_batch_size: int
        :param rollout_num: **参数解释：** 分组大小，GRPO算法中每次生成用于对比的样本组数量。  **约束限制：** 不涉及  **取值范围：** 正整数，单位为个分组。  **默认取值：** 无
        :type rollout_num: int
        :param epoch_num: **参数解释：** 训练轮数，全量数据集被模型训练的次数。  **约束限制：** 不涉及  **取值范围：** 取值范围：1到1000的正整数，单位为轮。  **默认取值：** 无
        :type epoch_num: int
        :param max_length: **参数解释：** 最大长度，模型生成序列的最大Token数。  **约束限制：** 不涉及  **取值范围：** 1到100000的正整数，单位为个Token。  **默认取值：** 无
        :type max_length: int
        :param ckpt_save_step: **参数解释：** 保存频率，每隔多少个训练步保存一次模型检查点。  **约束限制：** 不涉及  **取值范围：** 1到10000的正整数，单位为步。  **默认取值：** 无
        :type ckpt_save_step: int
        """
        
        

        self._actor_optimizer_lr = None
        self._train_batch_size = None
        self._rollout_num = None
        self._epoch_num = None
        self._max_length = None
        self._ckpt_save_step = None
        self.discriminator = None

        self.actor_optimizer_lr = actor_optimizer_lr
        self.train_batch_size = train_batch_size
        self.rollout_num = rollout_num
        self.epoch_num = epoch_num
        self.max_length = max_length
        self.ckpt_save_step = ckpt_save_step

    @property
    def actor_optimizer_lr(self):
        r"""Gets the actor_optimizer_lr of this OpsTuningParamSetting.

        **参数解释：** 优化器学习率，控制模型参数更新的步长。  **约束限制：** 数值过大可能导致训练震荡，过小可能导致收敛缓慢。  **取值范围：** 科学计数法字符串，如1.0E-5。  **默认取值：** 无

        :return: The actor_optimizer_lr of this OpsTuningParamSetting.
        :rtype: str
        """
        return self._actor_optimizer_lr

    @actor_optimizer_lr.setter
    def actor_optimizer_lr(self, actor_optimizer_lr):
        r"""Sets the actor_optimizer_lr of this OpsTuningParamSetting.

        **参数解释：** 优化器学习率，控制模型参数更新的步长。  **约束限制：** 数值过大可能导致训练震荡，过小可能导致收敛缓慢。  **取值范围：** 科学计数法字符串，如1.0E-5。  **默认取值：** 无

        :param actor_optimizer_lr: The actor_optimizer_lr of this OpsTuningParamSetting.
        :type actor_optimizer_lr: str
        """
        self._actor_optimizer_lr = actor_optimizer_lr

    @property
    def train_batch_size(self):
        r"""Gets the train_batch_size of this OpsTuningParamSetting.

        **参数解释：** 批大小，单次训练迭代中使用的样本数量。  **约束限制：** 不涉及  **取值范围：** 正整数，单位为个样本。  **默认取值：** 无

        :return: The train_batch_size of this OpsTuningParamSetting.
        :rtype: int
        """
        return self._train_batch_size

    @train_batch_size.setter
    def train_batch_size(self, train_batch_size):
        r"""Sets the train_batch_size of this OpsTuningParamSetting.

        **参数解释：** 批大小，单次训练迭代中使用的样本数量。  **约束限制：** 不涉及  **取值范围：** 正整数，单位为个样本。  **默认取值：** 无

        :param train_batch_size: The train_batch_size of this OpsTuningParamSetting.
        :type train_batch_size: int
        """
        self._train_batch_size = train_batch_size

    @property
    def rollout_num(self):
        r"""Gets the rollout_num of this OpsTuningParamSetting.

        **参数解释：** 分组大小，GRPO算法中每次生成用于对比的样本组数量。  **约束限制：** 不涉及  **取值范围：** 正整数，单位为个分组。  **默认取值：** 无

        :return: The rollout_num of this OpsTuningParamSetting.
        :rtype: int
        """
        return self._rollout_num

    @rollout_num.setter
    def rollout_num(self, rollout_num):
        r"""Sets the rollout_num of this OpsTuningParamSetting.

        **参数解释：** 分组大小，GRPO算法中每次生成用于对比的样本组数量。  **约束限制：** 不涉及  **取值范围：** 正整数，单位为个分组。  **默认取值：** 无

        :param rollout_num: The rollout_num of this OpsTuningParamSetting.
        :type rollout_num: int
        """
        self._rollout_num = rollout_num

    @property
    def epoch_num(self):
        r"""Gets the epoch_num of this OpsTuningParamSetting.

        **参数解释：** 训练轮数，全量数据集被模型训练的次数。  **约束限制：** 不涉及  **取值范围：** 取值范围：1到1000的正整数，单位为轮。  **默认取值：** 无

        :return: The epoch_num of this OpsTuningParamSetting.
        :rtype: int
        """
        return self._epoch_num

    @epoch_num.setter
    def epoch_num(self, epoch_num):
        r"""Sets the epoch_num of this OpsTuningParamSetting.

        **参数解释：** 训练轮数，全量数据集被模型训练的次数。  **约束限制：** 不涉及  **取值范围：** 取值范围：1到1000的正整数，单位为轮。  **默认取值：** 无

        :param epoch_num: The epoch_num of this OpsTuningParamSetting.
        :type epoch_num: int
        """
        self._epoch_num = epoch_num

    @property
    def max_length(self):
        r"""Gets the max_length of this OpsTuningParamSetting.

        **参数解释：** 最大长度，模型生成序列的最大Token数。  **约束限制：** 不涉及  **取值范围：** 1到100000的正整数，单位为个Token。  **默认取值：** 无

        :return: The max_length of this OpsTuningParamSetting.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        r"""Sets the max_length of this OpsTuningParamSetting.

        **参数解释：** 最大长度，模型生成序列的最大Token数。  **约束限制：** 不涉及  **取值范围：** 1到100000的正整数，单位为个Token。  **默认取值：** 无

        :param max_length: The max_length of this OpsTuningParamSetting.
        :type max_length: int
        """
        self._max_length = max_length

    @property
    def ckpt_save_step(self):
        r"""Gets the ckpt_save_step of this OpsTuningParamSetting.

        **参数解释：** 保存频率，每隔多少个训练步保存一次模型检查点。  **约束限制：** 不涉及  **取值范围：** 1到10000的正整数，单位为步。  **默认取值：** 无

        :return: The ckpt_save_step of this OpsTuningParamSetting.
        :rtype: int
        """
        return self._ckpt_save_step

    @ckpt_save_step.setter
    def ckpt_save_step(self, ckpt_save_step):
        r"""Sets the ckpt_save_step of this OpsTuningParamSetting.

        **参数解释：** 保存频率，每隔多少个训练步保存一次模型检查点。  **约束限制：** 不涉及  **取值范围：** 1到10000的正整数，单位为步。  **默认取值：** 无

        :param ckpt_save_step: The ckpt_save_step of this OpsTuningParamSetting.
        :type ckpt_save_step: int
        """
        self._ckpt_save_step = ckpt_save_step

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
        if not isinstance(other, OpsTuningParamSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
