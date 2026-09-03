# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFtDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'task_id': 'str',
        'task_name': 'str',
        'task_desc': 'str',
        'metadata': 'JobMetadataResponse',
        'spec': 'SpecResponse',
        'model_asset_id': 'str',
        'model_type': 'str',
        'model_source': 'str',
        'train_type': 'str',
        'checkpoint_config': 'str',
        'task_parameters': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'train_process': 'float',
        'datasets_config': 'list[DatasetConfig]',
        'status': 'Status',
        'auto_publish_config': 'str',
        'asset_code': 'str',
        'asset_name': 'str',
        'asset_desc': 'str',
        'asset_series': 'str',
        'asset_version': 'str',
        'asset_type': 'str',
        'asset_source': 'str',
        'asset_group_id': 'str',
        'sub_asset_type': 'str',
        'category': 'str',
        'api_version': 'str',
        'root_asset_id': 'str',
        'train_cost_time': 'int',
        'workspace_id': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'pool_type': 'str',
        'pool_id': 'str',
        'pool_node_count': 'str',
        'flavor_id': 'str',
        'priority': 'int',
        'training_info': 'str',
        'train_output_path': 'str',
        'asset_capabilities': 'list[str]',
        'continue_task': 'ContinueTask'
    }

    attribute_map = {
        'project_id': 'project_id',
        'task_id': 'task_id',
        'task_name': 'task_name',
        'task_desc': 'task_desc',
        'metadata': 'metadata',
        'spec': 'spec',
        'model_asset_id': 'model_asset_id',
        'model_type': 'model_type',
        'model_source': 'model_source',
        'train_type': 'train_type',
        'checkpoint_config': 'checkpoint_config',
        'task_parameters': 'task_parameters',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'train_process': 'train_process',
        'datasets_config': 'datasets_config',
        'status': 'status',
        'auto_publish_config': 'auto_publish_config',
        'asset_code': 'asset_code',
        'asset_name': 'asset_name',
        'asset_desc': 'asset_desc',
        'asset_series': 'asset_series',
        'asset_version': 'asset_version',
        'asset_type': 'asset_type',
        'asset_source': 'asset_source',
        'asset_group_id': 'asset_group_id',
        'sub_asset_type': 'sub_asset_type',
        'category': 'category',
        'api_version': 'api_version',
        'root_asset_id': 'root_asset_id',
        'train_cost_time': 'train_cost_time',
        'workspace_id': 'workspace_id',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'pool_type': 'pool_type',
        'pool_id': 'pool_id',
        'pool_node_count': 'pool_node_count',
        'flavor_id': 'flavor_id',
        'priority': 'priority',
        'training_info': 'training_info',
        'train_output_path': 'train_output_path',
        'asset_capabilities': 'asset_capabilities',
        'continue_task': 'continue_task'
    }

    def __init__(self, project_id=None, task_id=None, task_name=None, task_desc=None, metadata=None, spec=None, model_asset_id=None, model_type=None, model_source=None, train_type=None, checkpoint_config=None, task_parameters=None, create_time=None, update_time=None, train_process=None, datasets_config=None, status=None, auto_publish_config=None, asset_code=None, asset_name=None, asset_desc=None, asset_series=None, asset_version=None, asset_type=None, asset_source=None, asset_group_id=None, sub_asset_type=None, category=None, api_version=None, root_asset_id=None, train_cost_time=None, workspace_id=None, user_id=None, user_name=None, pool_type=None, pool_id=None, pool_node_count=None, flavor_id=None, priority=None, training_info=None, train_output_path=None, asset_capabilities=None, continue_task=None):
        r"""ShowFtDetailResponse

        The model defined in huaweicloud sdk

        :param project_id: 项目id。
        :type project_id: str
        :param task_id: 训练任务id。
        :type task_id: str
        :param task_name: 训练任务名称。
        :type task_name: str
        :param task_desc: 训练任务描述信息。
        :type task_desc: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.JobMetadataResponse`
        :param spec: 
        :type spec: :class:`huaweicloudsdkmodelarts.v1.SpecResponse`
        :param model_asset_id: 模型id。
        :type model_asset_id: str
        :param model_type: **参数解释：** 模型类型，取值为TextGeneration|ImageUnderstanding，依次为：文本生成、图像理解。 **约束限制：** 不涉及 **取值范围：** TextGeneration|ImageUnderstanding **默认取值：** 不涉及
        :type model_type: str
        :param model_source: 模型来源
        :type model_source: str
        :param train_type: **参数解释：** 训练类型，支持SFT（全量微调）、PRETRAIN（预训练）、LORA（lora微调）、DPO（dpo强化学习）、RFT（rft强化学习）。 **约束限制：** 不涉及 **取值范围：** SFT（全量微调）、PRETRAIN（预训练）、LORA（lora微调）、DPO（dpo强化学习）、RFT（rft强化学习） 默认取值： SFT
        :type train_type: str
        :param checkpoint_config: 断点续训相关配置。
        :type checkpoint_config: str
        :param task_parameters: 训练任参数信息。
        :type task_parameters: str
        :param create_time: 创建时间。
        :type create_time: int
        :param update_time: 训练任务更新时间，当修改、或者训练任务状态发生变化时进行更新。
        :type update_time: int
        :param train_process: 训练任务进度。
        :type train_process: float
        :param datasets_config: 该训练任务数据集相关的配置。
        :type datasets_config: list[:class:`huaweicloudsdkmodelarts.v1.DatasetConfig`]
        :param status: 
        :type status: :class:`huaweicloudsdkmodelarts.v1.Status`
        :param auto_publish_config: 自动发布配置信息
        :type auto_publish_config: str
        :param asset_code: 模型资产名
        :type asset_code: str
        :param asset_name: 资产名称
        :type asset_name: str
        :param asset_desc: 模型资产描述信息
        :type asset_desc: str
        :param asset_series: 模型系列
        :type asset_series: str
        :param asset_version: 资产版本
        :type asset_version: str
        :param asset_type: 资产类型
        :type asset_type: str
        :param asset_source: 资产来源
        :type asset_source: str
        :param asset_group_id: 资产组id
        :type asset_group_id: str
        :param sub_asset_type: 资产子类型
        :type sub_asset_type: str
        :param category: 资产类别
        :type category: str
        :param api_version: 资产API版本
        :type api_version: str
        :param root_asset_id: 根资产ID
        :type root_asset_id: str
        :param train_cost_time: 训练任务耗时
        :type train_cost_time: int
        :param workspace_id: 任务所属工作空间名称
        :type workspace_id: str
        :param user_id: 用户id
        :type user_id: str
        :param user_name: 用户名称
        :type user_name: str
        :param pool_type: 资源池类型
        :type pool_type: str
        :param pool_id: 资源池ID
        :type pool_id: str
        :param pool_node_count: 使用的资源池实例数
        :type pool_node_count: str
        :param flavor_id: 使用的资源池卡数
        :type flavor_id: str
        :param priority: 优先级
        :type priority: int
        :param training_info: 训练预估时长
        :type training_info: str
        :param train_output_path: **参数解释**：训练产物输出路径，如\&quot;obs://yyy/test/\&quot;。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type train_output_path: str
        :param asset_capabilities: 训练模型类型
        :type asset_capabilities: list[str]
        :param continue_task: 
        :type continue_task: :class:`huaweicloudsdkmodelarts.v1.ContinueTask`
        """
        
        super().__init__()

        self._project_id = None
        self._task_id = None
        self._task_name = None
        self._task_desc = None
        self._metadata = None
        self._spec = None
        self._model_asset_id = None
        self._model_type = None
        self._model_source = None
        self._train_type = None
        self._checkpoint_config = None
        self._task_parameters = None
        self._create_time = None
        self._update_time = None
        self._train_process = None
        self._datasets_config = None
        self._status = None
        self._auto_publish_config = None
        self._asset_code = None
        self._asset_name = None
        self._asset_desc = None
        self._asset_series = None
        self._asset_version = None
        self._asset_type = None
        self._asset_source = None
        self._asset_group_id = None
        self._sub_asset_type = None
        self._category = None
        self._api_version = None
        self._root_asset_id = None
        self._train_cost_time = None
        self._workspace_id = None
        self._user_id = None
        self._user_name = None
        self._pool_type = None
        self._pool_id = None
        self._pool_node_count = None
        self._flavor_id = None
        self._priority = None
        self._training_info = None
        self._train_output_path = None
        self._asset_capabilities = None
        self._continue_task = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if task_desc is not None:
            self.task_desc = task_desc
        if metadata is not None:
            self.metadata = metadata
        if spec is not None:
            self.spec = spec
        if model_asset_id is not None:
            self.model_asset_id = model_asset_id
        if model_type is not None:
            self.model_type = model_type
        if model_source is not None:
            self.model_source = model_source
        if train_type is not None:
            self.train_type = train_type
        if checkpoint_config is not None:
            self.checkpoint_config = checkpoint_config
        if task_parameters is not None:
            self.task_parameters = task_parameters
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if train_process is not None:
            self.train_process = train_process
        if datasets_config is not None:
            self.datasets_config = datasets_config
        if status is not None:
            self.status = status
        if auto_publish_config is not None:
            self.auto_publish_config = auto_publish_config
        if asset_code is not None:
            self.asset_code = asset_code
        if asset_name is not None:
            self.asset_name = asset_name
        if asset_desc is not None:
            self.asset_desc = asset_desc
        if asset_series is not None:
            self.asset_series = asset_series
        if asset_version is not None:
            self.asset_version = asset_version
        if asset_type is not None:
            self.asset_type = asset_type
        if asset_source is not None:
            self.asset_source = asset_source
        if asset_group_id is not None:
            self.asset_group_id = asset_group_id
        if sub_asset_type is not None:
            self.sub_asset_type = sub_asset_type
        if category is not None:
            self.category = category
        if api_version is not None:
            self.api_version = api_version
        if root_asset_id is not None:
            self.root_asset_id = root_asset_id
        if train_cost_time is not None:
            self.train_cost_time = train_cost_time
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if pool_type is not None:
            self.pool_type = pool_type
        if pool_id is not None:
            self.pool_id = pool_id
        if pool_node_count is not None:
            self.pool_node_count = pool_node_count
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if priority is not None:
            self.priority = priority
        if training_info is not None:
            self.training_info = training_info
        if train_output_path is not None:
            self.train_output_path = train_output_path
        if asset_capabilities is not None:
            self.asset_capabilities = asset_capabilities
        if continue_task is not None:
            self.continue_task = continue_task

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowFtDetailResponse.

        项目id。

        :return: The project_id of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowFtDetailResponse.

        项目id。

        :param project_id: The project_id of this ShowFtDetailResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowFtDetailResponse.

        训练任务id。

        :return: The task_id of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowFtDetailResponse.

        训练任务id。

        :param task_id: The task_id of this ShowFtDetailResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ShowFtDetailResponse.

        训练任务名称。

        :return: The task_name of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ShowFtDetailResponse.

        训练任务名称。

        :param task_name: The task_name of this ShowFtDetailResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_desc(self):
        r"""Gets the task_desc of this ShowFtDetailResponse.

        训练任务描述信息。

        :return: The task_desc of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._task_desc

    @task_desc.setter
    def task_desc(self, task_desc):
        r"""Sets the task_desc of this ShowFtDetailResponse.

        训练任务描述信息。

        :param task_desc: The task_desc of this ShowFtDetailResponse.
        :type task_desc: str
        """
        self._task_desc = task_desc

    @property
    def metadata(self):
        r"""Gets the metadata of this ShowFtDetailResponse.

        :return: The metadata of this ShowFtDetailResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.JobMetadataResponse`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ShowFtDetailResponse.

        :param metadata: The metadata of this ShowFtDetailResponse.
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.JobMetadataResponse`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this ShowFtDetailResponse.

        :return: The spec of this ShowFtDetailResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.SpecResponse`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this ShowFtDetailResponse.

        :param spec: The spec of this ShowFtDetailResponse.
        :type spec: :class:`huaweicloudsdkmodelarts.v1.SpecResponse`
        """
        self._spec = spec

    @property
    def model_asset_id(self):
        r"""Gets the model_asset_id of this ShowFtDetailResponse.

        模型id。

        :return: The model_asset_id of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._model_asset_id

    @model_asset_id.setter
    def model_asset_id(self, model_asset_id):
        r"""Sets the model_asset_id of this ShowFtDetailResponse.

        模型id。

        :param model_asset_id: The model_asset_id of this ShowFtDetailResponse.
        :type model_asset_id: str
        """
        self._model_asset_id = model_asset_id

    @property
    def model_type(self):
        r"""Gets the model_type of this ShowFtDetailResponse.

        **参数解释：** 模型类型，取值为TextGeneration|ImageUnderstanding，依次为：文本生成、图像理解。 **约束限制：** 不涉及 **取值范围：** TextGeneration|ImageUnderstanding **默认取值：** 不涉及

        :return: The model_type of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        r"""Sets the model_type of this ShowFtDetailResponse.

        **参数解释：** 模型类型，取值为TextGeneration|ImageUnderstanding，依次为：文本生成、图像理解。 **约束限制：** 不涉及 **取值范围：** TextGeneration|ImageUnderstanding **默认取值：** 不涉及

        :param model_type: The model_type of this ShowFtDetailResponse.
        :type model_type: str
        """
        self._model_type = model_type

    @property
    def model_source(self):
        r"""Gets the model_source of this ShowFtDetailResponse.

        模型来源

        :return: The model_source of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._model_source

    @model_source.setter
    def model_source(self, model_source):
        r"""Sets the model_source of this ShowFtDetailResponse.

        模型来源

        :param model_source: The model_source of this ShowFtDetailResponse.
        :type model_source: str
        """
        self._model_source = model_source

    @property
    def train_type(self):
        r"""Gets the train_type of this ShowFtDetailResponse.

        **参数解释：** 训练类型，支持SFT（全量微调）、PRETRAIN（预训练）、LORA（lora微调）、DPO（dpo强化学习）、RFT（rft强化学习）。 **约束限制：** 不涉及 **取值范围：** SFT（全量微调）、PRETRAIN（预训练）、LORA（lora微调）、DPO（dpo强化学习）、RFT（rft强化学习） 默认取值： SFT

        :return: The train_type of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._train_type

    @train_type.setter
    def train_type(self, train_type):
        r"""Sets the train_type of this ShowFtDetailResponse.

        **参数解释：** 训练类型，支持SFT（全量微调）、PRETRAIN（预训练）、LORA（lora微调）、DPO（dpo强化学习）、RFT（rft强化学习）。 **约束限制：** 不涉及 **取值范围：** SFT（全量微调）、PRETRAIN（预训练）、LORA（lora微调）、DPO（dpo强化学习）、RFT（rft强化学习） 默认取值： SFT

        :param train_type: The train_type of this ShowFtDetailResponse.
        :type train_type: str
        """
        self._train_type = train_type

    @property
    def checkpoint_config(self):
        r"""Gets the checkpoint_config of this ShowFtDetailResponse.

        断点续训相关配置。

        :return: The checkpoint_config of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._checkpoint_config

    @checkpoint_config.setter
    def checkpoint_config(self, checkpoint_config):
        r"""Sets the checkpoint_config of this ShowFtDetailResponse.

        断点续训相关配置。

        :param checkpoint_config: The checkpoint_config of this ShowFtDetailResponse.
        :type checkpoint_config: str
        """
        self._checkpoint_config = checkpoint_config

    @property
    def task_parameters(self):
        r"""Gets the task_parameters of this ShowFtDetailResponse.

        训练任参数信息。

        :return: The task_parameters of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._task_parameters

    @task_parameters.setter
    def task_parameters(self, task_parameters):
        r"""Sets the task_parameters of this ShowFtDetailResponse.

        训练任参数信息。

        :param task_parameters: The task_parameters of this ShowFtDetailResponse.
        :type task_parameters: str
        """
        self._task_parameters = task_parameters

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowFtDetailResponse.

        创建时间。

        :return: The create_time of this ShowFtDetailResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowFtDetailResponse.

        创建时间。

        :param create_time: The create_time of this ShowFtDetailResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowFtDetailResponse.

        训练任务更新时间，当修改、或者训练任务状态发生变化时进行更新。

        :return: The update_time of this ShowFtDetailResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowFtDetailResponse.

        训练任务更新时间，当修改、或者训练任务状态发生变化时进行更新。

        :param update_time: The update_time of this ShowFtDetailResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def train_process(self):
        r"""Gets the train_process of this ShowFtDetailResponse.

        训练任务进度。

        :return: The train_process of this ShowFtDetailResponse.
        :rtype: float
        """
        return self._train_process

    @train_process.setter
    def train_process(self, train_process):
        r"""Sets the train_process of this ShowFtDetailResponse.

        训练任务进度。

        :param train_process: The train_process of this ShowFtDetailResponse.
        :type train_process: float
        """
        self._train_process = train_process

    @property
    def datasets_config(self):
        r"""Gets the datasets_config of this ShowFtDetailResponse.

        该训练任务数据集相关的配置。

        :return: The datasets_config of this ShowFtDetailResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.DatasetConfig`]
        """
        return self._datasets_config

    @datasets_config.setter
    def datasets_config(self, datasets_config):
        r"""Sets the datasets_config of this ShowFtDetailResponse.

        该训练任务数据集相关的配置。

        :param datasets_config: The datasets_config of this ShowFtDetailResponse.
        :type datasets_config: list[:class:`huaweicloudsdkmodelarts.v1.DatasetConfig`]
        """
        self._datasets_config = datasets_config

    @property
    def status(self):
        r"""Gets the status of this ShowFtDetailResponse.

        :return: The status of this ShowFtDetailResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Status`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowFtDetailResponse.

        :param status: The status of this ShowFtDetailResponse.
        :type status: :class:`huaweicloudsdkmodelarts.v1.Status`
        """
        self._status = status

    @property
    def auto_publish_config(self):
        r"""Gets the auto_publish_config of this ShowFtDetailResponse.

        自动发布配置信息

        :return: The auto_publish_config of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._auto_publish_config

    @auto_publish_config.setter
    def auto_publish_config(self, auto_publish_config):
        r"""Sets the auto_publish_config of this ShowFtDetailResponse.

        自动发布配置信息

        :param auto_publish_config: The auto_publish_config of this ShowFtDetailResponse.
        :type auto_publish_config: str
        """
        self._auto_publish_config = auto_publish_config

    @property
    def asset_code(self):
        r"""Gets the asset_code of this ShowFtDetailResponse.

        模型资产名

        :return: The asset_code of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._asset_code

    @asset_code.setter
    def asset_code(self, asset_code):
        r"""Sets the asset_code of this ShowFtDetailResponse.

        模型资产名

        :param asset_code: The asset_code of this ShowFtDetailResponse.
        :type asset_code: str
        """
        self._asset_code = asset_code

    @property
    def asset_name(self):
        r"""Gets the asset_name of this ShowFtDetailResponse.

        资产名称

        :return: The asset_name of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this ShowFtDetailResponse.

        资产名称

        :param asset_name: The asset_name of this ShowFtDetailResponse.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_desc(self):
        r"""Gets the asset_desc of this ShowFtDetailResponse.

        模型资产描述信息

        :return: The asset_desc of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._asset_desc

    @asset_desc.setter
    def asset_desc(self, asset_desc):
        r"""Sets the asset_desc of this ShowFtDetailResponse.

        模型资产描述信息

        :param asset_desc: The asset_desc of this ShowFtDetailResponse.
        :type asset_desc: str
        """
        self._asset_desc = asset_desc

    @property
    def asset_series(self):
        r"""Gets the asset_series of this ShowFtDetailResponse.

        模型系列

        :return: The asset_series of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._asset_series

    @asset_series.setter
    def asset_series(self, asset_series):
        r"""Sets the asset_series of this ShowFtDetailResponse.

        模型系列

        :param asset_series: The asset_series of this ShowFtDetailResponse.
        :type asset_series: str
        """
        self._asset_series = asset_series

    @property
    def asset_version(self):
        r"""Gets the asset_version of this ShowFtDetailResponse.

        资产版本

        :return: The asset_version of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._asset_version

    @asset_version.setter
    def asset_version(self, asset_version):
        r"""Sets the asset_version of this ShowFtDetailResponse.

        资产版本

        :param asset_version: The asset_version of this ShowFtDetailResponse.
        :type asset_version: str
        """
        self._asset_version = asset_version

    @property
    def asset_type(self):
        r"""Gets the asset_type of this ShowFtDetailResponse.

        资产类型

        :return: The asset_type of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this ShowFtDetailResponse.

        资产类型

        :param asset_type: The asset_type of this ShowFtDetailResponse.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def asset_source(self):
        r"""Gets the asset_source of this ShowFtDetailResponse.

        资产来源

        :return: The asset_source of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._asset_source

    @asset_source.setter
    def asset_source(self, asset_source):
        r"""Sets the asset_source of this ShowFtDetailResponse.

        资产来源

        :param asset_source: The asset_source of this ShowFtDetailResponse.
        :type asset_source: str
        """
        self._asset_source = asset_source

    @property
    def asset_group_id(self):
        r"""Gets the asset_group_id of this ShowFtDetailResponse.

        资产组id

        :return: The asset_group_id of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._asset_group_id

    @asset_group_id.setter
    def asset_group_id(self, asset_group_id):
        r"""Sets the asset_group_id of this ShowFtDetailResponse.

        资产组id

        :param asset_group_id: The asset_group_id of this ShowFtDetailResponse.
        :type asset_group_id: str
        """
        self._asset_group_id = asset_group_id

    @property
    def sub_asset_type(self):
        r"""Gets the sub_asset_type of this ShowFtDetailResponse.

        资产子类型

        :return: The sub_asset_type of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._sub_asset_type

    @sub_asset_type.setter
    def sub_asset_type(self, sub_asset_type):
        r"""Sets the sub_asset_type of this ShowFtDetailResponse.

        资产子类型

        :param sub_asset_type: The sub_asset_type of this ShowFtDetailResponse.
        :type sub_asset_type: str
        """
        self._sub_asset_type = sub_asset_type

    @property
    def category(self):
        r"""Gets the category of this ShowFtDetailResponse.

        资产类别

        :return: The category of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowFtDetailResponse.

        资产类别

        :param category: The category of this ShowFtDetailResponse.
        :type category: str
        """
        self._category = category

    @property
    def api_version(self):
        r"""Gets the api_version of this ShowFtDetailResponse.

        资产API版本

        :return: The api_version of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ShowFtDetailResponse.

        资产API版本

        :param api_version: The api_version of this ShowFtDetailResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def root_asset_id(self):
        r"""Gets the root_asset_id of this ShowFtDetailResponse.

        根资产ID

        :return: The root_asset_id of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._root_asset_id

    @root_asset_id.setter
    def root_asset_id(self, root_asset_id):
        r"""Sets the root_asset_id of this ShowFtDetailResponse.

        根资产ID

        :param root_asset_id: The root_asset_id of this ShowFtDetailResponse.
        :type root_asset_id: str
        """
        self._root_asset_id = root_asset_id

    @property
    def train_cost_time(self):
        r"""Gets the train_cost_time of this ShowFtDetailResponse.

        训练任务耗时

        :return: The train_cost_time of this ShowFtDetailResponse.
        :rtype: int
        """
        return self._train_cost_time

    @train_cost_time.setter
    def train_cost_time(self, train_cost_time):
        r"""Sets the train_cost_time of this ShowFtDetailResponse.

        训练任务耗时

        :param train_cost_time: The train_cost_time of this ShowFtDetailResponse.
        :type train_cost_time: int
        """
        self._train_cost_time = train_cost_time

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowFtDetailResponse.

        任务所属工作空间名称

        :return: The workspace_id of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowFtDetailResponse.

        任务所属工作空间名称

        :param workspace_id: The workspace_id of this ShowFtDetailResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowFtDetailResponse.

        用户id

        :return: The user_id of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowFtDetailResponse.

        用户id

        :param user_id: The user_id of this ShowFtDetailResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ShowFtDetailResponse.

        用户名称

        :return: The user_name of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ShowFtDetailResponse.

        用户名称

        :param user_name: The user_name of this ShowFtDetailResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def pool_type(self):
        r"""Gets the pool_type of this ShowFtDetailResponse.

        资源池类型

        :return: The pool_type of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._pool_type

    @pool_type.setter
    def pool_type(self, pool_type):
        r"""Sets the pool_type of this ShowFtDetailResponse.

        资源池类型

        :param pool_type: The pool_type of this ShowFtDetailResponse.
        :type pool_type: str
        """
        self._pool_type = pool_type

    @property
    def pool_id(self):
        r"""Gets the pool_id of this ShowFtDetailResponse.

        资源池ID

        :return: The pool_id of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this ShowFtDetailResponse.

        资源池ID

        :param pool_id: The pool_id of this ShowFtDetailResponse.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def pool_node_count(self):
        r"""Gets the pool_node_count of this ShowFtDetailResponse.

        使用的资源池实例数

        :return: The pool_node_count of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._pool_node_count

    @pool_node_count.setter
    def pool_node_count(self, pool_node_count):
        r"""Sets the pool_node_count of this ShowFtDetailResponse.

        使用的资源池实例数

        :param pool_node_count: The pool_node_count of this ShowFtDetailResponse.
        :type pool_node_count: str
        """
        self._pool_node_count = pool_node_count

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this ShowFtDetailResponse.

        使用的资源池卡数

        :return: The flavor_id of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this ShowFtDetailResponse.

        使用的资源池卡数

        :param flavor_id: The flavor_id of this ShowFtDetailResponse.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def priority(self):
        r"""Gets the priority of this ShowFtDetailResponse.

        优先级

        :return: The priority of this ShowFtDetailResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ShowFtDetailResponse.

        优先级

        :param priority: The priority of this ShowFtDetailResponse.
        :type priority: int
        """
        self._priority = priority

    @property
    def training_info(self):
        r"""Gets the training_info of this ShowFtDetailResponse.

        训练预估时长

        :return: The training_info of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._training_info

    @training_info.setter
    def training_info(self, training_info):
        r"""Sets the training_info of this ShowFtDetailResponse.

        训练预估时长

        :param training_info: The training_info of this ShowFtDetailResponse.
        :type training_info: str
        """
        self._training_info = training_info

    @property
    def train_output_path(self):
        r"""Gets the train_output_path of this ShowFtDetailResponse.

        **参数解释**：训练产物输出路径，如\"obs://yyy/test/\"。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The train_output_path of this ShowFtDetailResponse.
        :rtype: str
        """
        return self._train_output_path

    @train_output_path.setter
    def train_output_path(self, train_output_path):
        r"""Sets the train_output_path of this ShowFtDetailResponse.

        **参数解释**：训练产物输出路径，如\"obs://yyy/test/\"。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param train_output_path: The train_output_path of this ShowFtDetailResponse.
        :type train_output_path: str
        """
        self._train_output_path = train_output_path

    @property
    def asset_capabilities(self):
        r"""Gets the asset_capabilities of this ShowFtDetailResponse.

        训练模型类型

        :return: The asset_capabilities of this ShowFtDetailResponse.
        :rtype: list[str]
        """
        return self._asset_capabilities

    @asset_capabilities.setter
    def asset_capabilities(self, asset_capabilities):
        r"""Sets the asset_capabilities of this ShowFtDetailResponse.

        训练模型类型

        :param asset_capabilities: The asset_capabilities of this ShowFtDetailResponse.
        :type asset_capabilities: list[str]
        """
        self._asset_capabilities = asset_capabilities

    @property
    def continue_task(self):
        r"""Gets the continue_task of this ShowFtDetailResponse.

        :return: The continue_task of this ShowFtDetailResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ContinueTask`
        """
        return self._continue_task

    @continue_task.setter
    def continue_task(self, continue_task):
        r"""Sets the continue_task of this ShowFtDetailResponse.

        :param continue_task: The continue_task of this ShowFtDetailResponse.
        :type continue_task: :class:`huaweicloudsdkmodelarts.v1.ContinueTask`
        """
        self._continue_task = continue_task

    def to_dict(self):
        import warnings
        warnings.warn("ShowFtDetailResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowFtDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
