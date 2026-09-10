# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsModelTuningTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'agent': 'OpsTuningTargetAgent',
        'model_name': 'str',
        'train_agent': 'OpsTuningTrainAgent',
        'training_type': 'str',
        'tuning_method': 'str',
        'reward_setting': 'OpsTuningRewardSetting',
        'parameter_setting': 'OpsTuningParamSetting',
        'dataset': 'OpsDatasetInfo',
        'validation_set': 'OpsDatasetInfo',
        'validation_set_ratio': 'int',
        'train_product_path': 'str',
        'log_config': 'OpsLogConfigInfo',
        'agency_name': 'str',
        'status': 'str',
        'fail_detail': 'OpsFailDetail',
        'progress': 'float',
        'created_at': 'int',
        'updated_at': 'int',
        'executed_at': 'int',
        'end_at': 'int',
        'executed_time': 'int',
        'tags': 'list[OpsTasksTagForTMS]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'agent': 'agent',
        'model_name': 'model_name',
        'train_agent': 'train_agent',
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
        'status': 'status',
        'fail_detail': 'fail_detail',
        'progress': 'progress',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'executed_at': 'executed_at',
        'end_at': 'end_at',
        'executed_time': 'executed_time',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, description=None, agent=None, model_name=None, train_agent=None, training_type=None, tuning_method=None, reward_setting=None, parameter_setting=None, dataset=None, validation_set=None, validation_set_ratio=None, train_product_path=None, log_config=None, agency_name=None, status=None, fail_detail=None, progress=None, created_at=None, updated_at=None, executed_at=None, end_at=None, executed_time=None, tags=None):
        r"""OpsModelTuningTask

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 模型优化任务ID。  **取值范围：** UUID格式字符串。
        :type id: str
        :param name: **参数解释：** 任务名称。  **取值范围：** 长度1-64个字符的字符串。
        :type name: str
        :param description: **参数解释：** 任务描述。  **取值范围：** 长度0-255个字符的字符串。
        :type description: str
        :param agent: 
        :type agent: :class:`huaweicloudsdkagentarts.v1.OpsTuningTargetAgent`
        :param model_name: **参数解释：** 调优模型名称。  **取值范围：** qwen3_8b或qwen3_1_7b。
        :type model_name: str
        :param train_agent: 
        :type train_agent: :class:`huaweicloudsdkagentarts.v1.OpsTuningTrainAgent`
        :param training_type: **参数解释：** 训练类型。  **取值范围：** 固定值为rl（强化学习）。
        :type training_type: str
        :param tuning_method: **参数解释：** 调优方法。  **取值范围：** 固定值为grpo（群组相对策略优化）。
        :type tuning_method: str
        :param reward_setting: 
        :type reward_setting: :class:`huaweicloudsdkagentarts.v1.OpsTuningRewardSetting`
        :param parameter_setting: 
        :type parameter_setting: :class:`huaweicloudsdkagentarts.v1.OpsTuningParamSetting`
        :param dataset: 
        :type dataset: :class:`huaweicloudsdkagentarts.v1.OpsDatasetInfo`
        :param validation_set: 
        :type validation_set: :class:`huaweicloudsdkagentarts.v1.OpsDatasetInfo`
        :param validation_set_ratio: **参数解释：** 验证集比例。  **取值范围：** 0到99的整数（单位：%）
        :type validation_set_ratio: int
        :param train_product_path: **参数解释：** 训练产物路径。  **取值范围：** 不涉及
        :type train_product_path: str
        :param log_config: 
        :type log_config: :class:`huaweicloudsdkagentarts.v1.OpsLogConfigInfo`
        :param agency_name: **参数解释：** 委托名称，赋予服务访问用户资源的权限。  **取值范围：** 有效的IAM委托名称字符串。
        :type agency_name: str
        :param status: **参数解释：** 任务状态。  **取值范围：** draft草稿态，training训练中，stopped已停止，success成功，fail失败，deleting删除中，stopping停止中。
        :type status: str
        :param fail_detail: 
        :type fail_detail: :class:`huaweicloudsdkagentarts.v1.OpsFailDetail`
        :param progress: **参数解释：** 任务进度，单位：%。  **取值范围：** 0.0到100.0之间的浮点数。
        :type progress: float
        :param created_at: **参数解释：** 创建时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。
        :type created_at: int
        :param updated_at: **参数解释：** 更新时间（单位：毫秒）  **取值范围：** 13位毫秒级时间戳。
        :type updated_at: int
        :param executed_at: **参数解释：** 运行时长，单位：分钟。  **取值范围：** 13位毫秒级时间戳。
        :type executed_at: int
        :param end_at: **参数解释：** 执行结束时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。
        :type end_at: int
        :param executed_time: **参数解释：** 运行时长，单位：分钟。  **取值范围：** 大于等于0的整数（单位：分钟）
        :type executed_time: int
        :param tags: **参数解释：** 资源标签列表。  **取值范围：** 符合OpsTasksTagForTMS定义的对象数组。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTasksTagForTMS`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._agent = None
        self._model_name = None
        self._train_agent = None
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
        self._status = None
        self._fail_detail = None
        self._progress = None
        self._created_at = None
        self._updated_at = None
        self._executed_at = None
        self._end_at = None
        self._executed_time = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if agent is not None:
            self.agent = agent
        if model_name is not None:
            self.model_name = model_name
        if train_agent is not None:
            self.train_agent = train_agent
        if training_type is not None:
            self.training_type = training_type
        if tuning_method is not None:
            self.tuning_method = tuning_method
        if reward_setting is not None:
            self.reward_setting = reward_setting
        if parameter_setting is not None:
            self.parameter_setting = parameter_setting
        if dataset is not None:
            self.dataset = dataset
        if validation_set is not None:
            self.validation_set = validation_set
        if validation_set_ratio is not None:
            self.validation_set_ratio = validation_set_ratio
        if train_product_path is not None:
            self.train_product_path = train_product_path
        if log_config is not None:
            self.log_config = log_config
        if agency_name is not None:
            self.agency_name = agency_name
        if status is not None:
            self.status = status
        if fail_detail is not None:
            self.fail_detail = fail_detail
        if progress is not None:
            self.progress = progress
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if executed_at is not None:
            self.executed_at = executed_at
        if end_at is not None:
            self.end_at = end_at
        if executed_time is not None:
            self.executed_time = executed_time
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        r"""Gets the id of this OpsModelTuningTask.

        **参数解释：** 模型优化任务ID。  **取值范围：** UUID格式字符串。

        :return: The id of this OpsModelTuningTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpsModelTuningTask.

        **参数解释：** 模型优化任务ID。  **取值范围：** UUID格式字符串。

        :param id: The id of this OpsModelTuningTask.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this OpsModelTuningTask.

        **参数解释：** 任务名称。  **取值范围：** 长度1-64个字符的字符串。

        :return: The name of this OpsModelTuningTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OpsModelTuningTask.

        **参数解释：** 任务名称。  **取值范围：** 长度1-64个字符的字符串。

        :param name: The name of this OpsModelTuningTask.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this OpsModelTuningTask.

        **参数解释：** 任务描述。  **取值范围：** 长度0-255个字符的字符串。

        :return: The description of this OpsModelTuningTask.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this OpsModelTuningTask.

        **参数解释：** 任务描述。  **取值范围：** 长度0-255个字符的字符串。

        :param description: The description of this OpsModelTuningTask.
        :type description: str
        """
        self._description = description

    @property
    def agent(self):
        r"""Gets the agent of this OpsModelTuningTask.

        :return: The agent of this OpsModelTuningTask.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsTuningTargetAgent`
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        r"""Sets the agent of this OpsModelTuningTask.

        :param agent: The agent of this OpsModelTuningTask.
        :type agent: :class:`huaweicloudsdkagentarts.v1.OpsTuningTargetAgent`
        """
        self._agent = agent

    @property
    def model_name(self):
        r"""Gets the model_name of this OpsModelTuningTask.

        **参数解释：** 调优模型名称。  **取值范围：** qwen3_8b或qwen3_1_7b。

        :return: The model_name of this OpsModelTuningTask.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this OpsModelTuningTask.

        **参数解释：** 调优模型名称。  **取值范围：** qwen3_8b或qwen3_1_7b。

        :param model_name: The model_name of this OpsModelTuningTask.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def train_agent(self):
        r"""Gets the train_agent of this OpsModelTuningTask.

        :return: The train_agent of this OpsModelTuningTask.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsTuningTrainAgent`
        """
        return self._train_agent

    @train_agent.setter
    def train_agent(self, train_agent):
        r"""Sets the train_agent of this OpsModelTuningTask.

        :param train_agent: The train_agent of this OpsModelTuningTask.
        :type train_agent: :class:`huaweicloudsdkagentarts.v1.OpsTuningTrainAgent`
        """
        self._train_agent = train_agent

    @property
    def training_type(self):
        r"""Gets the training_type of this OpsModelTuningTask.

        **参数解释：** 训练类型。  **取值范围：** 固定值为rl（强化学习）。

        :return: The training_type of this OpsModelTuningTask.
        :rtype: str
        """
        return self._training_type

    @training_type.setter
    def training_type(self, training_type):
        r"""Sets the training_type of this OpsModelTuningTask.

        **参数解释：** 训练类型。  **取值范围：** 固定值为rl（强化学习）。

        :param training_type: The training_type of this OpsModelTuningTask.
        :type training_type: str
        """
        self._training_type = training_type

    @property
    def tuning_method(self):
        r"""Gets the tuning_method of this OpsModelTuningTask.

        **参数解释：** 调优方法。  **取值范围：** 固定值为grpo（群组相对策略优化）。

        :return: The tuning_method of this OpsModelTuningTask.
        :rtype: str
        """
        return self._tuning_method

    @tuning_method.setter
    def tuning_method(self, tuning_method):
        r"""Sets the tuning_method of this OpsModelTuningTask.

        **参数解释：** 调优方法。  **取值范围：** 固定值为grpo（群组相对策略优化）。

        :param tuning_method: The tuning_method of this OpsModelTuningTask.
        :type tuning_method: str
        """
        self._tuning_method = tuning_method

    @property
    def reward_setting(self):
        r"""Gets the reward_setting of this OpsModelTuningTask.

        :return: The reward_setting of this OpsModelTuningTask.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsTuningRewardSetting`
        """
        return self._reward_setting

    @reward_setting.setter
    def reward_setting(self, reward_setting):
        r"""Sets the reward_setting of this OpsModelTuningTask.

        :param reward_setting: The reward_setting of this OpsModelTuningTask.
        :type reward_setting: :class:`huaweicloudsdkagentarts.v1.OpsTuningRewardSetting`
        """
        self._reward_setting = reward_setting

    @property
    def parameter_setting(self):
        r"""Gets the parameter_setting of this OpsModelTuningTask.

        :return: The parameter_setting of this OpsModelTuningTask.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsTuningParamSetting`
        """
        return self._parameter_setting

    @parameter_setting.setter
    def parameter_setting(self, parameter_setting):
        r"""Sets the parameter_setting of this OpsModelTuningTask.

        :param parameter_setting: The parameter_setting of this OpsModelTuningTask.
        :type parameter_setting: :class:`huaweicloudsdkagentarts.v1.OpsTuningParamSetting`
        """
        self._parameter_setting = parameter_setting

    @property
    def dataset(self):
        r"""Gets the dataset of this OpsModelTuningTask.

        :return: The dataset of this OpsModelTuningTask.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsDatasetInfo`
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        r"""Sets the dataset of this OpsModelTuningTask.

        :param dataset: The dataset of this OpsModelTuningTask.
        :type dataset: :class:`huaweicloudsdkagentarts.v1.OpsDatasetInfo`
        """
        self._dataset = dataset

    @property
    def validation_set(self):
        r"""Gets the validation_set of this OpsModelTuningTask.

        :return: The validation_set of this OpsModelTuningTask.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsDatasetInfo`
        """
        return self._validation_set

    @validation_set.setter
    def validation_set(self, validation_set):
        r"""Sets the validation_set of this OpsModelTuningTask.

        :param validation_set: The validation_set of this OpsModelTuningTask.
        :type validation_set: :class:`huaweicloudsdkagentarts.v1.OpsDatasetInfo`
        """
        self._validation_set = validation_set

    @property
    def validation_set_ratio(self):
        r"""Gets the validation_set_ratio of this OpsModelTuningTask.

        **参数解释：** 验证集比例。  **取值范围：** 0到99的整数（单位：%）

        :return: The validation_set_ratio of this OpsModelTuningTask.
        :rtype: int
        """
        return self._validation_set_ratio

    @validation_set_ratio.setter
    def validation_set_ratio(self, validation_set_ratio):
        r"""Sets the validation_set_ratio of this OpsModelTuningTask.

        **参数解释：** 验证集比例。  **取值范围：** 0到99的整数（单位：%）

        :param validation_set_ratio: The validation_set_ratio of this OpsModelTuningTask.
        :type validation_set_ratio: int
        """
        self._validation_set_ratio = validation_set_ratio

    @property
    def train_product_path(self):
        r"""Gets the train_product_path of this OpsModelTuningTask.

        **参数解释：** 训练产物路径。  **取值范围：** 不涉及

        :return: The train_product_path of this OpsModelTuningTask.
        :rtype: str
        """
        return self._train_product_path

    @train_product_path.setter
    def train_product_path(self, train_product_path):
        r"""Sets the train_product_path of this OpsModelTuningTask.

        **参数解释：** 训练产物路径。  **取值范围：** 不涉及

        :param train_product_path: The train_product_path of this OpsModelTuningTask.
        :type train_product_path: str
        """
        self._train_product_path = train_product_path

    @property
    def log_config(self):
        r"""Gets the log_config of this OpsModelTuningTask.

        :return: The log_config of this OpsModelTuningTask.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsLogConfigInfo`
        """
        return self._log_config

    @log_config.setter
    def log_config(self, log_config):
        r"""Sets the log_config of this OpsModelTuningTask.

        :param log_config: The log_config of this OpsModelTuningTask.
        :type log_config: :class:`huaweicloudsdkagentarts.v1.OpsLogConfigInfo`
        """
        self._log_config = log_config

    @property
    def agency_name(self):
        r"""Gets the agency_name of this OpsModelTuningTask.

        **参数解释：** 委托名称，赋予服务访问用户资源的权限。  **取值范围：** 有效的IAM委托名称字符串。

        :return: The agency_name of this OpsModelTuningTask.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this OpsModelTuningTask.

        **参数解释：** 委托名称，赋予服务访问用户资源的权限。  **取值范围：** 有效的IAM委托名称字符串。

        :param agency_name: The agency_name of this OpsModelTuningTask.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def status(self):
        r"""Gets the status of this OpsModelTuningTask.

        **参数解释：** 任务状态。  **取值范围：** draft草稿态，training训练中，stopped已停止，success成功，fail失败，deleting删除中，stopping停止中。

        :return: The status of this OpsModelTuningTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OpsModelTuningTask.

        **参数解释：** 任务状态。  **取值范围：** draft草稿态，training训练中，stopped已停止，success成功，fail失败，deleting删除中，stopping停止中。

        :param status: The status of this OpsModelTuningTask.
        :type status: str
        """
        self._status = status

    @property
    def fail_detail(self):
        r"""Gets the fail_detail of this OpsModelTuningTask.

        :return: The fail_detail of this OpsModelTuningTask.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsFailDetail`
        """
        return self._fail_detail

    @fail_detail.setter
    def fail_detail(self, fail_detail):
        r"""Sets the fail_detail of this OpsModelTuningTask.

        :param fail_detail: The fail_detail of this OpsModelTuningTask.
        :type fail_detail: :class:`huaweicloudsdkagentarts.v1.OpsFailDetail`
        """
        self._fail_detail = fail_detail

    @property
    def progress(self):
        r"""Gets the progress of this OpsModelTuningTask.

        **参数解释：** 任务进度，单位：%。  **取值范围：** 0.0到100.0之间的浮点数。

        :return: The progress of this OpsModelTuningTask.
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this OpsModelTuningTask.

        **参数解释：** 任务进度，单位：%。  **取值范围：** 0.0到100.0之间的浮点数。

        :param progress: The progress of this OpsModelTuningTask.
        :type progress: float
        """
        self._progress = progress

    @property
    def created_at(self):
        r"""Gets the created_at of this OpsModelTuningTask.

        **参数解释：** 创建时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。

        :return: The created_at of this OpsModelTuningTask.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this OpsModelTuningTask.

        **参数解释：** 创建时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。

        :param created_at: The created_at of this OpsModelTuningTask.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this OpsModelTuningTask.

        **参数解释：** 更新时间（单位：毫秒）  **取值范围：** 13位毫秒级时间戳。

        :return: The updated_at of this OpsModelTuningTask.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this OpsModelTuningTask.

        **参数解释：** 更新时间（单位：毫秒）  **取值范围：** 13位毫秒级时间戳。

        :param updated_at: The updated_at of this OpsModelTuningTask.
        :type updated_at: int
        """
        self._updated_at = updated_at

    @property
    def executed_at(self):
        r"""Gets the executed_at of this OpsModelTuningTask.

        **参数解释：** 运行时长，单位：分钟。  **取值范围：** 13位毫秒级时间戳。

        :return: The executed_at of this OpsModelTuningTask.
        :rtype: int
        """
        return self._executed_at

    @executed_at.setter
    def executed_at(self, executed_at):
        r"""Sets the executed_at of this OpsModelTuningTask.

        **参数解释：** 运行时长，单位：分钟。  **取值范围：** 13位毫秒级时间戳。

        :param executed_at: The executed_at of this OpsModelTuningTask.
        :type executed_at: int
        """
        self._executed_at = executed_at

    @property
    def end_at(self):
        r"""Gets the end_at of this OpsModelTuningTask.

        **参数解释：** 执行结束时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。

        :return: The end_at of this OpsModelTuningTask.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this OpsModelTuningTask.

        **参数解释：** 执行结束时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。

        :param end_at: The end_at of this OpsModelTuningTask.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def executed_time(self):
        r"""Gets the executed_time of this OpsModelTuningTask.

        **参数解释：** 运行时长，单位：分钟。  **取值范围：** 大于等于0的整数（单位：分钟）

        :return: The executed_time of this OpsModelTuningTask.
        :rtype: int
        """
        return self._executed_time

    @executed_time.setter
    def executed_time(self, executed_time):
        r"""Sets the executed_time of this OpsModelTuningTask.

        **参数解释：** 运行时长，单位：分钟。  **取值范围：** 大于等于0的整数（单位：分钟）

        :param executed_time: The executed_time of this OpsModelTuningTask.
        :type executed_time: int
        """
        self._executed_time = executed_time

    @property
    def tags(self):
        r"""Gets the tags of this OpsModelTuningTask.

        **参数解释：** 资源标签列表。  **取值范围：** 符合OpsTasksTagForTMS定义的对象数组。

        :return: The tags of this OpsModelTuningTask.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTasksTagForTMS`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this OpsModelTuningTask.

        **参数解释：** 资源标签列表。  **取值范围：** 符合OpsTasksTagForTMS定义的对象数组。

        :param tags: The tags of this OpsModelTuningTask.
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
        if not isinstance(other, OpsModelTuningTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
