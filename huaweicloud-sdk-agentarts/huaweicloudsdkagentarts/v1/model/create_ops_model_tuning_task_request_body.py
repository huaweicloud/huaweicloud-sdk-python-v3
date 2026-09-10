# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOpsModelTuningTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'agent': 'OpsTuningTargetAgent',
        'model_name': 'str',
        'training_type': 'str',
        'tuning_method': 'str',
        'reward_setting': 'OpsTuningRewardSetting',
        'parameter_setting': 'OpsTuningParamSetting',
        'dataset': 'OpsDataset',
        'validation_set': 'OpsDataset',
        'validation_set_ratio': 'int',
        'train_product_path': 'str',
        'log_config': 'OpsLogConfig',
        'agency_name': 'str',
        'tags': 'list[OpsTasksTagForTMS]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'agent': 'agent',
        'model_name': 'model_name',
        'training_type': 'training_type',
        'tuning_method': 'tuning_method',
        'reward_setting': 'reward_setting',
        'parameter_setting': 'parameter_setting',
        'dataset': 'dataset',
        'validation_set': 'validation_set',
        'validation_set_ratio': 'validation_set_ratio',
        'train_product_path': 'train_product_path',
        'log_config': 'log_config',
        'agency_name': 'agency_name',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, agent=None, model_name=None, training_type=None, tuning_method=None, reward_setting=None, parameter_setting=None, dataset=None, validation_set=None, validation_set_ratio=None, train_product_path=None, log_config=None, agency_name=None, tags=None):
        r"""CreateOpsModelTuningTaskRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 任务名称，用于标识和区分不同的模型优化任务。  **约束限制：** 不涉及  **取值范围：** 长度1-64个字符，支持中文、字母、数字、中划线及下划线。  **默认取值：** 无
        :type name: str
        :param description: **参数解释：** 任务的详细描述，用于记录任务目的或备注信息。  **约束限制：** 不涉及  **取值范围：** 长度0-1024个字符。  **默认取值：** 无
        :type description: str
        :param agent: 
        :type agent: :class:`huaweicloudsdkagentarts.v1.OpsTuningTargetAgent`
        :param model_name: **参数解释：** 基础调优模型名称，作为本次优化训练的底座模型。  **约束限制：**  必须是系统支持的基础模型。  **取值范围：**  可选值为 qwen3_8b 或 qwen3_1_7b。  **默认取值： ** 无
        :type model_name: str
        :param training_type: **参数解释：** 训练类型，决定模型训练所采用的学习算法类别。  **约束限制：** 目前仅支持强化学习。  **取值范围：** 固定值为rl。  **默认取值：** rl
        :type training_type: str
        :param tuning_method: **参数解释：**  调优方法/算法，指定模型优化所使用的具体算法策略。  **约束限制：**  目前仅支持群组相对优化算法。  **取值范围：**  固定值为 grpo。  **默认取值：**  grpo
        :type tuning_method: str
        :param reward_setting: 
        :type reward_setting: :class:`huaweicloudsdkagentarts.v1.OpsTuningRewardSetting`
        :param parameter_setting: 
        :type parameter_setting: :class:`huaweicloudsdkagentarts.v1.OpsTuningParamSetting`
        :param dataset: 
        :type dataset: :class:`huaweicloudsdkagentarts.v1.OpsDataset`
        :param validation_set: 
        :type validation_set: :class:`huaweicloudsdkagentarts.v1.OpsDataset`
        :param validation_set_ratio: **参数解释：** 验证集比例，使用训练数据集中的部分数据进行验证。  **约束限制：** 不涉及  **取值范围：** 0到99的整数（单位：%）  **默认取值：** 不涉及
        :type validation_set_ratio: int
        :param train_product_path: **参数解释：** 训练产物OBS路径。  **约束限制：** 必须是真实存在的OBS路径且具备读写权限。  **取值范围：** 不涉及  **默认取值：** 无
        :type train_product_path: str
        :param log_config: 
        :type log_config: :class:`huaweicloudsdkagentarts.v1.OpsLogConfig`
        :param agency_name: **参数解释：** 委托名称，赋予服务访问用户资源的权限。  **约束限制：** 必须是IAM中已创建的有效委托。  **取值范围：** 合法的委托名称字符串。  **默认取值：** 无
        :type agency_name: str
        :param tags: **参数解释：** 资源标签列表，用于资源分类。  **约束限制：** 不涉及  **取值范围：** 数组长度0-20。  **默认取值：** 空数组
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTasksTagForTMS`]
        """
        
        

        self._name = None
        self._description = None
        self._agent = None
        self._model_name = None
        self._training_type = None
        self._tuning_method = None
        self._reward_setting = None
        self._parameter_setting = None
        self._dataset = None
        self._validation_set = None
        self._validation_set_ratio = None
        self._train_product_path = None
        self._log_config = None
        self._agency_name = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.agent = agent
        self.model_name = model_name
        if training_type is not None:
            self.training_type = training_type
        if tuning_method is not None:
            self.tuning_method = tuning_method
        self.reward_setting = reward_setting
        self.parameter_setting = parameter_setting
        self.dataset = dataset
        if validation_set is not None:
            self.validation_set = validation_set
        if validation_set_ratio is not None:
            self.validation_set_ratio = validation_set_ratio
        self.train_product_path = train_product_path
        if log_config is not None:
            self.log_config = log_config
        self.agency_name = agency_name
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：** 任务名称，用于标识和区分不同的模型优化任务。  **约束限制：** 不涉及  **取值范围：** 长度1-64个字符，支持中文、字母、数字、中划线及下划线。  **默认取值：** 无

        :return: The name of this CreateOpsModelTuningTaskRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：** 任务名称，用于标识和区分不同的模型优化任务。  **约束限制：** 不涉及  **取值范围：** 长度1-64个字符，支持中文、字母、数字、中划线及下划线。  **默认取值：** 无

        :param name: The name of this CreateOpsModelTuningTaskRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：** 任务的详细描述，用于记录任务目的或备注信息。  **约束限制：** 不涉及  **取值范围：** 长度0-1024个字符。  **默认取值：** 无

        :return: The description of this CreateOpsModelTuningTaskRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：** 任务的详细描述，用于记录任务目的或备注信息。  **约束限制：** 不涉及  **取值范围：** 长度0-1024个字符。  **默认取值：** 无

        :param description: The description of this CreateOpsModelTuningTaskRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def agent(self):
        r"""Gets the agent of this CreateOpsModelTuningTaskRequestBody.

        :return: The agent of this CreateOpsModelTuningTaskRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsTuningTargetAgent`
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        r"""Sets the agent of this CreateOpsModelTuningTaskRequestBody.

        :param agent: The agent of this CreateOpsModelTuningTaskRequestBody.
        :type agent: :class:`huaweicloudsdkagentarts.v1.OpsTuningTargetAgent`
        """
        self._agent = agent

    @property
    def model_name(self):
        r"""Gets the model_name of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：** 基础调优模型名称，作为本次优化训练的底座模型。  **约束限制：**  必须是系统支持的基础模型。  **取值范围：**  可选值为 qwen3_8b 或 qwen3_1_7b。  **默认取值： ** 无

        :return: The model_name of this CreateOpsModelTuningTaskRequestBody.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：** 基础调优模型名称，作为本次优化训练的底座模型。  **约束限制：**  必须是系统支持的基础模型。  **取值范围：**  可选值为 qwen3_8b 或 qwen3_1_7b。  **默认取值： ** 无

        :param model_name: The model_name of this CreateOpsModelTuningTaskRequestBody.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def training_type(self):
        r"""Gets the training_type of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：** 训练类型，决定模型训练所采用的学习算法类别。  **约束限制：** 目前仅支持强化学习。  **取值范围：** 固定值为rl。  **默认取值：** rl

        :return: The training_type of this CreateOpsModelTuningTaskRequestBody.
        :rtype: str
        """
        return self._training_type

    @training_type.setter
    def training_type(self, training_type):
        r"""Sets the training_type of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：** 训练类型，决定模型训练所采用的学习算法类别。  **约束限制：** 目前仅支持强化学习。  **取值范围：** 固定值为rl。  **默认取值：** rl

        :param training_type: The training_type of this CreateOpsModelTuningTaskRequestBody.
        :type training_type: str
        """
        self._training_type = training_type

    @property
    def tuning_method(self):
        r"""Gets the tuning_method of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：**  调优方法/算法，指定模型优化所使用的具体算法策略。  **约束限制：**  目前仅支持群组相对优化算法。  **取值范围：**  固定值为 grpo。  **默认取值：**  grpo

        :return: The tuning_method of this CreateOpsModelTuningTaskRequestBody.
        :rtype: str
        """
        return self._tuning_method

    @tuning_method.setter
    def tuning_method(self, tuning_method):
        r"""Sets the tuning_method of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：**  调优方法/算法，指定模型优化所使用的具体算法策略。  **约束限制：**  目前仅支持群组相对优化算法。  **取值范围：**  固定值为 grpo。  **默认取值：**  grpo

        :param tuning_method: The tuning_method of this CreateOpsModelTuningTaskRequestBody.
        :type tuning_method: str
        """
        self._tuning_method = tuning_method

    @property
    def reward_setting(self):
        r"""Gets the reward_setting of this CreateOpsModelTuningTaskRequestBody.

        :return: The reward_setting of this CreateOpsModelTuningTaskRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsTuningRewardSetting`
        """
        return self._reward_setting

    @reward_setting.setter
    def reward_setting(self, reward_setting):
        r"""Sets the reward_setting of this CreateOpsModelTuningTaskRequestBody.

        :param reward_setting: The reward_setting of this CreateOpsModelTuningTaskRequestBody.
        :type reward_setting: :class:`huaweicloudsdkagentarts.v1.OpsTuningRewardSetting`
        """
        self._reward_setting = reward_setting

    @property
    def parameter_setting(self):
        r"""Gets the parameter_setting of this CreateOpsModelTuningTaskRequestBody.

        :return: The parameter_setting of this CreateOpsModelTuningTaskRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsTuningParamSetting`
        """
        return self._parameter_setting

    @parameter_setting.setter
    def parameter_setting(self, parameter_setting):
        r"""Sets the parameter_setting of this CreateOpsModelTuningTaskRequestBody.

        :param parameter_setting: The parameter_setting of this CreateOpsModelTuningTaskRequestBody.
        :type parameter_setting: :class:`huaweicloudsdkagentarts.v1.OpsTuningParamSetting`
        """
        self._parameter_setting = parameter_setting

    @property
    def dataset(self):
        r"""Gets the dataset of this CreateOpsModelTuningTaskRequestBody.

        :return: The dataset of this CreateOpsModelTuningTaskRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsDataset`
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        r"""Sets the dataset of this CreateOpsModelTuningTaskRequestBody.

        :param dataset: The dataset of this CreateOpsModelTuningTaskRequestBody.
        :type dataset: :class:`huaweicloudsdkagentarts.v1.OpsDataset`
        """
        self._dataset = dataset

    @property
    def validation_set(self):
        r"""Gets the validation_set of this CreateOpsModelTuningTaskRequestBody.

        :return: The validation_set of this CreateOpsModelTuningTaskRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsDataset`
        """
        return self._validation_set

    @validation_set.setter
    def validation_set(self, validation_set):
        r"""Sets the validation_set of this CreateOpsModelTuningTaskRequestBody.

        :param validation_set: The validation_set of this CreateOpsModelTuningTaskRequestBody.
        :type validation_set: :class:`huaweicloudsdkagentarts.v1.OpsDataset`
        """
        self._validation_set = validation_set

    @property
    def validation_set_ratio(self):
        r"""Gets the validation_set_ratio of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：** 验证集比例，使用训练数据集中的部分数据进行验证。  **约束限制：** 不涉及  **取值范围：** 0到99的整数（单位：%）  **默认取值：** 不涉及

        :return: The validation_set_ratio of this CreateOpsModelTuningTaskRequestBody.
        :rtype: int
        """
        return self._validation_set_ratio

    @validation_set_ratio.setter
    def validation_set_ratio(self, validation_set_ratio):
        r"""Sets the validation_set_ratio of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：** 验证集比例，使用训练数据集中的部分数据进行验证。  **约束限制：** 不涉及  **取值范围：** 0到99的整数（单位：%）  **默认取值：** 不涉及

        :param validation_set_ratio: The validation_set_ratio of this CreateOpsModelTuningTaskRequestBody.
        :type validation_set_ratio: int
        """
        self._validation_set_ratio = validation_set_ratio

    @property
    def train_product_path(self):
        r"""Gets the train_product_path of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：** 训练产物OBS路径。  **约束限制：** 必须是真实存在的OBS路径且具备读写权限。  **取值范围：** 不涉及  **默认取值：** 无

        :return: The train_product_path of this CreateOpsModelTuningTaskRequestBody.
        :rtype: str
        """
        return self._train_product_path

    @train_product_path.setter
    def train_product_path(self, train_product_path):
        r"""Sets the train_product_path of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：** 训练产物OBS路径。  **约束限制：** 必须是真实存在的OBS路径且具备读写权限。  **取值范围：** 不涉及  **默认取值：** 无

        :param train_product_path: The train_product_path of this CreateOpsModelTuningTaskRequestBody.
        :type train_product_path: str
        """
        self._train_product_path = train_product_path

    @property
    def log_config(self):
        r"""Gets the log_config of this CreateOpsModelTuningTaskRequestBody.

        :return: The log_config of this CreateOpsModelTuningTaskRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsLogConfig`
        """
        return self._log_config

    @log_config.setter
    def log_config(self, log_config):
        r"""Sets the log_config of this CreateOpsModelTuningTaskRequestBody.

        :param log_config: The log_config of this CreateOpsModelTuningTaskRequestBody.
        :type log_config: :class:`huaweicloudsdkagentarts.v1.OpsLogConfig`
        """
        self._log_config = log_config

    @property
    def agency_name(self):
        r"""Gets the agency_name of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：** 委托名称，赋予服务访问用户资源的权限。  **约束限制：** 必须是IAM中已创建的有效委托。  **取值范围：** 合法的委托名称字符串。  **默认取值：** 无

        :return: The agency_name of this CreateOpsModelTuningTaskRequestBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：** 委托名称，赋予服务访问用户资源的权限。  **约束限制：** 必须是IAM中已创建的有效委托。  **取值范围：** 合法的委托名称字符串。  **默认取值：** 无

        :param agency_name: The agency_name of this CreateOpsModelTuningTaskRequestBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def tags(self):
        r"""Gets the tags of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：** 资源标签列表，用于资源分类。  **约束限制：** 不涉及  **取值范围：** 数组长度0-20。  **默认取值：** 空数组

        :return: The tags of this CreateOpsModelTuningTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTasksTagForTMS`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateOpsModelTuningTaskRequestBody.

        **参数解释：** 资源标签列表，用于资源分类。  **约束限制：** 不涉及  **取值范围：** 数组长度0-20。  **默认取值：** 空数组

        :param tags: The tags of this CreateOpsModelTuningTaskRequestBody.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTasksTagForTMS`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateOpsModelTuningTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
