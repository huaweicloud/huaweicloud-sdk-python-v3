# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOpsEvaluationTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_id': 'str',
        'creator': 'str',
        'domain_id': 'str',
        'run_at': 'datetime',
        'tags': 'list[OpsTmsTag]',
        'eval_mode': 'str',
        'name': 'str',
        'description': 'str',
        'dataset_id': 'str',
        'dataset_version': 'str',
        'human_read_version': 'str',
        'dataset_name': 'str',
        'input_source_type': 'str',
        'input_source': 'OpsInputSource',
        'runtime_config': 'RuntimeConfig',
        'evaluation_object_config': 'object'
    }

    attribute_map = {
        'account_id': 'account_id',
        'creator': 'creator',
        'domain_id': 'domain_id',
        'run_at': 'run_at',
        'tags': 'tags',
        'eval_mode': 'eval_mode',
        'name': 'name',
        'description': 'description',
        'dataset_id': 'dataset_id',
        'dataset_version': 'dataset_version',
        'human_read_version': 'human_read_version',
        'dataset_name': 'dataset_name',
        'input_source_type': 'input_source_type',
        'input_source': 'input_source',
        'runtime_config': 'runtime_config',
        'evaluation_object_config': 'evaluation_object_config'
    }

    def __init__(self, account_id=None, creator=None, domain_id=None, run_at=None, tags=None, eval_mode=None, name=None, description=None, dataset_id=None, dataset_version=None, human_read_version=None, dataset_name=None, input_source_type=None, input_source=None, runtime_config=None, evaluation_object_config=None):
        r"""CreateOpsEvaluationTaskRequestBody

        The model defined in huaweicloud sdk

        :param account_id: **参数解释：** 租户账号ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type account_id: str
        :param creator: **参数解释：** 创建人用户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type creator: str
        :param domain_id: **参数解释：** 租户域ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type domain_id: str
        :param run_at: **参数解释：** 计划执行时间。 **约束限制：** 不涉及。 **取值范围：** ISO 8601 时间格式，长度范围为0~40。 **默认取值：** 不涉及。
        :type run_at: datetime
        :param tags: **参数解释：** 创建评估任务时绑定的TMS标签列表。 **约束限制：** 数组长度0到50。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        :param eval_mode: **参数解释：** 评估模式，指定任务是在线评估还是离线评估，影响任务的执行环境和策略。 **约束限制：** 字符串类型，最小长度为1，最大长度为36。 **取值范围：** 枚举值：OFFLINE（离线）、ONLINE（在线）。字符最小长度为1，最大长度为36。 **默认取值：** OFFLINE。
        :type eval_mode: str
        :param name: **参数解释：** 评估任务的名称，用于标识和区分不同的评估任务，方便管理和查找。 **约束限制：** 字符串类型，最小长度为4，最大长度为100。 **取值范围：** 字符长度4-100。 **默认取值：** 不涉及。
        :type name: str
        :param description: **参数解释：** 评估任务的描述信息，详细说明任务的目的、范围和预期结果等背景信息。 **约束限制：** 字符串类型，最大长度为400。 **取值范围：** 字符长度0-400。 **默认取值：** 不涉及。
        :type description: str
        :param dataset_id: **参数解释：** 评测集ID，离线任务使用的数据集唯一标识符，用于指定评估的数据来源。 通过1.1-创建评测集 - CreateOpsDataset获取。 **约束限制：** 字符串类型，最大长度为36。 **取值范围：** 字符长度0-36，符合通用唯一识别码(UUID)标准的字符串。 **默认取值：** 不涉及。
        :type dataset_id: str
        :param dataset_version: **参数解释：** 评测集版本号，离线任务使用的评测集版本标识。 **约束限制：** 字符串类型，最大长度为36。 **取值范围：** 字符长度0-36，系统内有效的评测集版本标识。 **默认取值：** 不涉及。
        :type dataset_version: str
        :param human_read_version: **参数解释：** 评测集版本，离线任务使用的评测集可读版本标识。 **约束限制：** 字符串类型，最大长度为36。 **取值范围：** 字符长度0-36，如0.0.1格式。 **默认取值：** 不涉及。
        :type human_read_version: str
        :param dataset_name: **参数解释：** 评测集名称，离线任务使用的评测集显示名称。 **约束限制：** 字符串类型，最小长度为2，最大长度为100。 **取值范围：** 字符长度2-100。 **默认取值：** 不涉及。
        :type dataset_name: str
        :param input_source_type: **参数解释：** 评估数据来源，指定评估数据的类型和来源，影响数据的获取方式。 **约束限制：** 字符串类型，最大长度为36。 **取值范围：** 字符长度1-36，枚举值：DATASET_DYNAMIC、DATASET_STATIC、TRACE_STREAM。 **默认取值：** DATASET_DYNAMIC。
        :type input_source_type: str
        :param input_source: 
        :type input_source: :class:`huaweicloudsdkagentarts.v1.OpsInputSource`
        :param runtime_config: 
        :type runtime_config: :class:`huaweicloudsdkagentarts.v1.RuntimeConfig`
        :param evaluation_object_config: **参数解释：** 评估对象配置，指定被评估的对象信息（如模型、流等）。 **约束限制：** 结构化对象。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type evaluation_object_config: object
        """
        
        

        self._account_id = None
        self._creator = None
        self._domain_id = None
        self._run_at = None
        self._tags = None
        self._eval_mode = None
        self._name = None
        self._description = None
        self._dataset_id = None
        self._dataset_version = None
        self._human_read_version = None
        self._dataset_name = None
        self._input_source_type = None
        self._input_source = None
        self._runtime_config = None
        self._evaluation_object_config = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if creator is not None:
            self.creator = creator
        if domain_id is not None:
            self.domain_id = domain_id
        if run_at is not None:
            self.run_at = run_at
        if tags is not None:
            self.tags = tags
        if eval_mode is not None:
            self.eval_mode = eval_mode
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if dataset_version is not None:
            self.dataset_version = dataset_version
        if human_read_version is not None:
            self.human_read_version = human_read_version
        if dataset_name is not None:
            self.dataset_name = dataset_name
        if input_source_type is not None:
            self.input_source_type = input_source_type
        if input_source is not None:
            self.input_source = input_source
        if runtime_config is not None:
            self.runtime_config = runtime_config
        if evaluation_object_config is not None:
            self.evaluation_object_config = evaluation_object_config

    @property
    def account_id(self):
        r"""Gets the account_id of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 租户账号ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The account_id of this CreateOpsEvaluationTaskRequestBody.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 租户账号ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param account_id: The account_id of this CreateOpsEvaluationTaskRequestBody.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def creator(self):
        r"""Gets the creator of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 创建人用户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The creator of this CreateOpsEvaluationTaskRequestBody.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 创建人用户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param creator: The creator of this CreateOpsEvaluationTaskRequestBody.
        :type creator: str
        """
        self._creator = creator

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 租户域ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The domain_id of this CreateOpsEvaluationTaskRequestBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 租户域ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param domain_id: The domain_id of this CreateOpsEvaluationTaskRequestBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def run_at(self):
        r"""Gets the run_at of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 计划执行时间。 **约束限制：** 不涉及。 **取值范围：** ISO 8601 时间格式，长度范围为0~40。 **默认取值：** 不涉及。

        :return: The run_at of this CreateOpsEvaluationTaskRequestBody.
        :rtype: datetime
        """
        return self._run_at

    @run_at.setter
    def run_at(self, run_at):
        r"""Sets the run_at of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 计划执行时间。 **约束限制：** 不涉及。 **取值范围：** ISO 8601 时间格式，长度范围为0~40。 **默认取值：** 不涉及。

        :param run_at: The run_at of this CreateOpsEvaluationTaskRequestBody.
        :type run_at: datetime
        """
        self._run_at = run_at

    @property
    def tags(self):
        r"""Gets the tags of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 创建评估任务时绑定的TMS标签列表。 **约束限制：** 数组长度0到50。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tags of this CreateOpsEvaluationTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 创建评估任务时绑定的TMS标签列表。 **约束限制：** 数组长度0到50。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tags: The tags of this CreateOpsEvaluationTaskRequestBody.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        self._tags = tags

    @property
    def eval_mode(self):
        r"""Gets the eval_mode of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评估模式，指定任务是在线评估还是离线评估，影响任务的执行环境和策略。 **约束限制：** 字符串类型，最小长度为1，最大长度为36。 **取值范围：** 枚举值：OFFLINE（离线）、ONLINE（在线）。字符最小长度为1，最大长度为36。 **默认取值：** OFFLINE。

        :return: The eval_mode of this CreateOpsEvaluationTaskRequestBody.
        :rtype: str
        """
        return self._eval_mode

    @eval_mode.setter
    def eval_mode(self, eval_mode):
        r"""Sets the eval_mode of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评估模式，指定任务是在线评估还是离线评估，影响任务的执行环境和策略。 **约束限制：** 字符串类型，最小长度为1，最大长度为36。 **取值范围：** 枚举值：OFFLINE（离线）、ONLINE（在线）。字符最小长度为1，最大长度为36。 **默认取值：** OFFLINE。

        :param eval_mode: The eval_mode of this CreateOpsEvaluationTaskRequestBody.
        :type eval_mode: str
        """
        self._eval_mode = eval_mode

    @property
    def name(self):
        r"""Gets the name of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评估任务的名称，用于标识和区分不同的评估任务，方便管理和查找。 **约束限制：** 字符串类型，最小长度为4，最大长度为100。 **取值范围：** 字符长度4-100。 **默认取值：** 不涉及。

        :return: The name of this CreateOpsEvaluationTaskRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评估任务的名称，用于标识和区分不同的评估任务，方便管理和查找。 **约束限制：** 字符串类型，最小长度为4，最大长度为100。 **取值范围：** 字符长度4-100。 **默认取值：** 不涉及。

        :param name: The name of this CreateOpsEvaluationTaskRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评估任务的描述信息，详细说明任务的目的、范围和预期结果等背景信息。 **约束限制：** 字符串类型，最大长度为400。 **取值范围：** 字符长度0-400。 **默认取值：** 不涉及。

        :return: The description of this CreateOpsEvaluationTaskRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评估任务的描述信息，详细说明任务的目的、范围和预期结果等背景信息。 **约束限制：** 字符串类型，最大长度为400。 **取值范围：** 字符长度0-400。 **默认取值：** 不涉及。

        :param description: The description of this CreateOpsEvaluationTaskRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def dataset_id(self):
        r"""Gets the dataset_id of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评测集ID，离线任务使用的数据集唯一标识符，用于指定评估的数据来源。 通过1.1-创建评测集 - CreateOpsDataset获取。 **约束限制：** 字符串类型，最大长度为36。 **取值范围：** 字符长度0-36，符合通用唯一识别码(UUID)标准的字符串。 **默认取值：** 不涉及。

        :return: The dataset_id of this CreateOpsEvaluationTaskRequestBody.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        r"""Sets the dataset_id of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评测集ID，离线任务使用的数据集唯一标识符，用于指定评估的数据来源。 通过1.1-创建评测集 - CreateOpsDataset获取。 **约束限制：** 字符串类型，最大长度为36。 **取值范围：** 字符长度0-36，符合通用唯一识别码(UUID)标准的字符串。 **默认取值：** 不涉及。

        :param dataset_id: The dataset_id of this CreateOpsEvaluationTaskRequestBody.
        :type dataset_id: str
        """
        self._dataset_id = dataset_id

    @property
    def dataset_version(self):
        r"""Gets the dataset_version of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评测集版本号，离线任务使用的评测集版本标识。 **约束限制：** 字符串类型，最大长度为36。 **取值范围：** 字符长度0-36，系统内有效的评测集版本标识。 **默认取值：** 不涉及。

        :return: The dataset_version of this CreateOpsEvaluationTaskRequestBody.
        :rtype: str
        """
        return self._dataset_version

    @dataset_version.setter
    def dataset_version(self, dataset_version):
        r"""Sets the dataset_version of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评测集版本号，离线任务使用的评测集版本标识。 **约束限制：** 字符串类型，最大长度为36。 **取值范围：** 字符长度0-36，系统内有效的评测集版本标识。 **默认取值：** 不涉及。

        :param dataset_version: The dataset_version of this CreateOpsEvaluationTaskRequestBody.
        :type dataset_version: str
        """
        self._dataset_version = dataset_version

    @property
    def human_read_version(self):
        r"""Gets the human_read_version of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评测集版本，离线任务使用的评测集可读版本标识。 **约束限制：** 字符串类型，最大长度为36。 **取值范围：** 字符长度0-36，如0.0.1格式。 **默认取值：** 不涉及。

        :return: The human_read_version of this CreateOpsEvaluationTaskRequestBody.
        :rtype: str
        """
        return self._human_read_version

    @human_read_version.setter
    def human_read_version(self, human_read_version):
        r"""Sets the human_read_version of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评测集版本，离线任务使用的评测集可读版本标识。 **约束限制：** 字符串类型，最大长度为36。 **取值范围：** 字符长度0-36，如0.0.1格式。 **默认取值：** 不涉及。

        :param human_read_version: The human_read_version of this CreateOpsEvaluationTaskRequestBody.
        :type human_read_version: str
        """
        self._human_read_version = human_read_version

    @property
    def dataset_name(self):
        r"""Gets the dataset_name of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评测集名称，离线任务使用的评测集显示名称。 **约束限制：** 字符串类型，最小长度为2，最大长度为100。 **取值范围：** 字符长度2-100。 **默认取值：** 不涉及。

        :return: The dataset_name of this CreateOpsEvaluationTaskRequestBody.
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        r"""Sets the dataset_name of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评测集名称，离线任务使用的评测集显示名称。 **约束限制：** 字符串类型，最小长度为2，最大长度为100。 **取值范围：** 字符长度2-100。 **默认取值：** 不涉及。

        :param dataset_name: The dataset_name of this CreateOpsEvaluationTaskRequestBody.
        :type dataset_name: str
        """
        self._dataset_name = dataset_name

    @property
    def input_source_type(self):
        r"""Gets the input_source_type of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评估数据来源，指定评估数据的类型和来源，影响数据的获取方式。 **约束限制：** 字符串类型，最大长度为36。 **取值范围：** 字符长度1-36，枚举值：DATASET_DYNAMIC、DATASET_STATIC、TRACE_STREAM。 **默认取值：** DATASET_DYNAMIC。

        :return: The input_source_type of this CreateOpsEvaluationTaskRequestBody.
        :rtype: str
        """
        return self._input_source_type

    @input_source_type.setter
    def input_source_type(self, input_source_type):
        r"""Sets the input_source_type of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评估数据来源，指定评估数据的类型和来源，影响数据的获取方式。 **约束限制：** 字符串类型，最大长度为36。 **取值范围：** 字符长度1-36，枚举值：DATASET_DYNAMIC、DATASET_STATIC、TRACE_STREAM。 **默认取值：** DATASET_DYNAMIC。

        :param input_source_type: The input_source_type of this CreateOpsEvaluationTaskRequestBody.
        :type input_source_type: str
        """
        self._input_source_type = input_source_type

    @property
    def input_source(self):
        r"""Gets the input_source of this CreateOpsEvaluationTaskRequestBody.

        :return: The input_source of this CreateOpsEvaluationTaskRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsInputSource`
        """
        return self._input_source

    @input_source.setter
    def input_source(self, input_source):
        r"""Sets the input_source of this CreateOpsEvaluationTaskRequestBody.

        :param input_source: The input_source of this CreateOpsEvaluationTaskRequestBody.
        :type input_source: :class:`huaweicloudsdkagentarts.v1.OpsInputSource`
        """
        self._input_source = input_source

    @property
    def runtime_config(self):
        r"""Gets the runtime_config of this CreateOpsEvaluationTaskRequestBody.

        :return: The runtime_config of this CreateOpsEvaluationTaskRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.RuntimeConfig`
        """
        return self._runtime_config

    @runtime_config.setter
    def runtime_config(self, runtime_config):
        r"""Sets the runtime_config of this CreateOpsEvaluationTaskRequestBody.

        :param runtime_config: The runtime_config of this CreateOpsEvaluationTaskRequestBody.
        :type runtime_config: :class:`huaweicloudsdkagentarts.v1.RuntimeConfig`
        """
        self._runtime_config = runtime_config

    @property
    def evaluation_object_config(self):
        r"""Gets the evaluation_object_config of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评估对象配置，指定被评估的对象信息（如模型、流等）。 **约束限制：** 结构化对象。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The evaluation_object_config of this CreateOpsEvaluationTaskRequestBody.
        :rtype: object
        """
        return self._evaluation_object_config

    @evaluation_object_config.setter
    def evaluation_object_config(self, evaluation_object_config):
        r"""Sets the evaluation_object_config of this CreateOpsEvaluationTaskRequestBody.

        **参数解释：** 评估对象配置，指定被评估的对象信息（如模型、流等）。 **约束限制：** 结构化对象。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param evaluation_object_config: The evaluation_object_config of this CreateOpsEvaluationTaskRequestBody.
        :type evaluation_object_config: object
        """
        self._evaluation_object_config = evaluation_object_config

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
        if not isinstance(other, CreateOpsEvaluationTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
