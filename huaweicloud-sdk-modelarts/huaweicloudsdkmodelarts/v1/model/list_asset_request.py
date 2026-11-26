# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sort_dir': 'str',
        'sort_key': 'str',
        'limit': 'int',
        'offset': 'int',
        'workspace_id': 'str',
        'asset_name': 'str',
        'asset_type': 'list[str]',
        'asset_source': 'str',
        'asset_source_type': 'str',
        'asset_code': 'str',
        'asset_version': 'str',
        'asset_group_id': 'str',
        'filter_all_version': 'bool',
        'support_actions': 'list[str]',
        'tag': 'list[str]',
        'is_mine': 'bool',
        'with_actions': 'bool',
        'asset_series': 'str',
        'asset_capabilities': 'list[str]',
        'asset_scenes': 'list[str]',
        'root_asset_id': 'str',
        'parent_asset_id': 'str',
        'is_deleted': 'bool',
        'asset_ids': 'list[str]',
        'tag_mode': 'str',
        'dataset_usage': 'str',
        'status': 'str',
        'dataset_file_formats': 'list[str]',
        'dataset_type': 'str',
        'dataset_sub_type': 'str',
        'dataset_schema_format': 'str',
        'creator': 'str',
        'data_source_id': 'str'
    }

    attribute_map = {
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'limit': 'limit',
        'offset': 'offset',
        'workspace_id': 'workspace_id',
        'asset_name': 'asset_name',
        'asset_type': 'asset_type',
        'asset_source': 'asset_source',
        'asset_source_type': 'asset_source_type',
        'asset_code': 'asset_code',
        'asset_version': 'asset_version',
        'asset_group_id': 'asset_group_id',
        'filter_all_version': 'filter_all_version',
        'support_actions': 'support_actions',
        'tag': 'tag',
        'is_mine': 'is_mine',
        'with_actions': 'with_actions',
        'asset_series': 'asset_series',
        'asset_capabilities': 'asset_capabilities',
        'asset_scenes': 'asset_scenes',
        'root_asset_id': 'root_asset_id',
        'parent_asset_id': 'parent_asset_id',
        'is_deleted': 'is_deleted',
        'asset_ids': 'asset_ids',
        'tag_mode': 'tag_mode',
        'dataset_usage': 'dataset_usage',
        'status': 'status',
        'dataset_file_formats': 'dataset_file_formats',
        'dataset_type': 'dataset_type',
        'dataset_sub_type': 'dataset_sub_type',
        'dataset_schema_format': 'dataset_schema_format',
        'creator': 'creator',
        'data_source_id': 'data_source_id'
    }

    def __init__(self, sort_dir=None, sort_key=None, limit=None, offset=None, workspace_id=None, asset_name=None, asset_type=None, asset_source=None, asset_source_type=None, asset_code=None, asset_version=None, asset_group_id=None, filter_all_version=None, support_actions=None, tag=None, is_mine=None, with_actions=None, asset_series=None, asset_capabilities=None, asset_scenes=None, root_asset_id=None, parent_asset_id=None, is_deleted=None, asset_ids=None, tag_mode=None, dataset_usage=None, status=None, dataset_file_formats=None, dataset_type=None, dataset_sub_type=None, dataset_schema_format=None, creator=None, data_source_id=None):
        r"""ListAssetRequest

        The model defined in huaweicloud sdk

        :param sort_dir: **参数解释**：排序方向。 **约束限制**：不涉及。 **取值范围**： 枚举值： - ASC: 升序 - DESC: 降序。 **默认取值**：DESC。
        :type sort_dir: str
        :param sort_key: **参数解释**：排序字段。 **约束限制**：不涉及。 **取值范围**：枚举值： - created_at: 创建时间 - updated_at: 更新时间。 **默认取值**：created_at。
        :type sort_key: str
        :param limit: **参数解释**：限制量，单次查询总量，必须由数字组成。 **约束限制**：不涉及。 **取值范围**：1-1000。 **默认取值**：100。
        :type limit: int
        :param offset: **参数解释**：偏移量，查询起始偏移，必须由数字组成。 **约束限制**：不涉及。 **取值范围**0-100000000。 **默认取值**：0。
        :type offset: int
        :param workspace_id: 工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。
        :type workspace_id: str
        :param asset_name: **参数解释**：资产名称,支持英文字母，数字，中划线，下划线，点，空格，中文汉字。 **约束限制**：1-128位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_name: str
        :param asset_type: **参数解释**: 资产类型。 **约束限制**: 枚举值: - MODEL: 模型资产 - TEMPLATE: 模板资产 - DATASET: 数据集资产 - WORKFLOW: 工作流资产 - IMAGE: 镜像资产 - ALGORITHM: 算法资产 - DATASET_TEMPLATE: 数据集模板资产 - DATA_OPERATOR: 算子镜像资产 **默认取值**: 不涉及。
        :type asset_type: list[str]
        :param asset_source: **参数解释**：资产来源。 **约束限制**：不涉及。 **取值范围**：枚举值: - Preset: 预置资产 - Publish: 用户发布资产 - Import: 用户导入资产 **默认取值**：不涉及。
        :type asset_source: str
        :param asset_source_type: **参数解释**：用户资产来源。 **约束限制**：1-60位字符，英文字母，数字，下划线、中划线。 **取值范围**：preset_train：精调，custom_train：自定义训练，AgenticRL：强化学习。 **默认取值**：不涉及。
        :type asset_source_type: str
        :param asset_code: **参数解释**：资产编码。 **约束限制**：1-60字母，数字，中划线，下划线，点。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_code: str
        :param asset_version: **参数解释**：资产版本。 **约束限制**：数字或格式为x.y.z，x,y,z为数字。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_version: str
        :param asset_group_id: **参数解释**：资产归属的资产组id，带有该字段将在同一个资产库中所有版本进行条件筛选，否则会筛选所有资产库中的主版本。 **约束限制**：1-36字母数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_group_id: str
        :param filter_all_version: **参数解释**：是否过滤所有版本。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：false。
        :type filter_all_version: bool
        :param support_actions: **参数解释**：资产支持的操作列表，例如SFT：监督微调，LORA微调:LORA，在线部署：ONLINE-DEPLOY，强化学习：AgenticRL。 **约束限制**：每个元素1-30位字符，英文字母，数字，下划线，中划线；最多10个元素。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type support_actions: list[str]
        :param tag: **参数解释**：检索资产时的标签，根据不同资产类型，条件可能不同。 - 需要匹配一个key对应一个value时格式为key&#x3D;value - 需要匹配一个key对应多个value中的任意一个时格式为key&#x3D;value1|value2|value3 - 需要匹配多个条件同时满足时key1&#x3D;value1,key2&#x3D;value2 - 如果需要实现模糊匹配格式为key1%&#x3D;value2（右匹配）key2&#x3D;%value2（左匹配） **约束限制**：不涉及。
        :type tag: list[str]
        :param is_mine: **参数解释**：过滤我创建的资产，boolean类型，取值true：查询我创建的资产，取值false：查询所有资产。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type is_mine: bool
        :param with_actions: **参数解释**：列表查询是否包含action。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type with_actions: bool
        :param asset_series: **参数解释**：资产品牌，例如DeepSeek,Qwen,Wan,GPT,Llama,GLM,ERNIE,Mistral,Kimi,Other。 **约束限制**：不涉及。 **取值范围**：0-100位。 **默认取值**：不涉及。
        :type asset_series: str
        :param asset_capabilities: **参数解释**：资产能力，为自由文本字符串列表(非严格枚举)。推荐使用以下约定值：例如TextGeneration,ImageUnderstanding,ImageGeneration,VideoGeneration,AgenticRL,Other。 **约束限制**：每个元素为1-40位字符；最多10个元素。
        :type asset_capabilities: list[str]
        :param asset_scenes: **参数解释**：资产场景，如DeepThinking。 **约束限制**：不涉及。
        :type asset_scenes: list[str]
        :param root_asset_id: **参数解释**：根资产id。 **约束限制**：1-36个字符，英文字母，数字，中划线，下划线。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type root_asset_id: str
        :param parent_asset_id: **参数解释**：父资产id。 **约束限制**：1-36个字符，英文字母，数字，中划线，下划线。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type parent_asset_id: str
        :param is_deleted: **参数解释**：是否返回软删除的资产。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：false。
        :type is_deleted: bool
        :param asset_ids: **参数解释**：资产id。 **约束限制**：0-100个。
        :type asset_ids: list[str]
        :param tag_mode: **参数解释**：tag组合方式 **约束限制**：不涉及。 **取值范围**：and：与，or：或。 **默认取值**：and。
        :type tag_mode: str
        :param dataset_usage: **参数解释**：数据集用途，例如 GENERAL：通用数据集、EVAL：评测集。 **约束限制**：1-40位字符，英文字母，数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type dataset_usage: str
        :param status: **参数解释**：资产状态。 **约束限制**：不涉及。 **取值范围**：枚举值: - online: 上线 - offline: 下线 - waiting: 等待中 **默认取值**：不涉及。
        :type status: str
        :param dataset_file_formats: **参数解释**：数据集存储格式，例如JSONL，TXT，MOBI，EPUB，DOCX，PDF。 **约束限制**：不涉及。
        :type dataset_file_formats: list[str]
        :param dataset_type: **参数解释**：数据集模态划分，如音频，图像，视频。 **约束限制**：1-40位字符，英文字母，数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type dataset_type: str
        :param dataset_sub_type: **参数解释**：数据集模态细分值，如语义分割。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type dataset_sub_type: str
        :param dataset_schema_format: **参数解释**：数据集逻辑规范，如盘古格式。 **约束限制**：1-40位字符，英文字母，数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type dataset_schema_format: str
        :param creator: **参数解释**：资产创建者。 **约束限制**：1-512位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type creator: str
        :param data_source_id: **参数解释**：数据源的ID信息。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type data_source_id: str
        """
        
        

        self._sort_dir = None
        self._sort_key = None
        self._limit = None
        self._offset = None
        self._workspace_id = None
        self._asset_name = None
        self._asset_type = None
        self._asset_source = None
        self._asset_source_type = None
        self._asset_code = None
        self._asset_version = None
        self._asset_group_id = None
        self._filter_all_version = None
        self._support_actions = None
        self._tag = None
        self._is_mine = None
        self._with_actions = None
        self._asset_series = None
        self._asset_capabilities = None
        self._asset_scenes = None
        self._root_asset_id = None
        self._parent_asset_id = None
        self._is_deleted = None
        self._asset_ids = None
        self._tag_mode = None
        self._dataset_usage = None
        self._status = None
        self._dataset_file_formats = None
        self._dataset_type = None
        self._dataset_sub_type = None
        self._dataset_schema_format = None
        self._creator = None
        self._data_source_id = None
        self.discriminator = None

        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if asset_name is not None:
            self.asset_name = asset_name
        if asset_type is not None:
            self.asset_type = asset_type
        if asset_source is not None:
            self.asset_source = asset_source
        if asset_source_type is not None:
            self.asset_source_type = asset_source_type
        if asset_code is not None:
            self.asset_code = asset_code
        if asset_version is not None:
            self.asset_version = asset_version
        if asset_group_id is not None:
            self.asset_group_id = asset_group_id
        if filter_all_version is not None:
            self.filter_all_version = filter_all_version
        if support_actions is not None:
            self.support_actions = support_actions
        if tag is not None:
            self.tag = tag
        if is_mine is not None:
            self.is_mine = is_mine
        if with_actions is not None:
            self.with_actions = with_actions
        if asset_series is not None:
            self.asset_series = asset_series
        if asset_capabilities is not None:
            self.asset_capabilities = asset_capabilities
        if asset_scenes is not None:
            self.asset_scenes = asset_scenes
        if root_asset_id is not None:
            self.root_asset_id = root_asset_id
        if parent_asset_id is not None:
            self.parent_asset_id = parent_asset_id
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if asset_ids is not None:
            self.asset_ids = asset_ids
        if tag_mode is not None:
            self.tag_mode = tag_mode
        if dataset_usage is not None:
            self.dataset_usage = dataset_usage
        if status is not None:
            self.status = status
        if dataset_file_formats is not None:
            self.dataset_file_formats = dataset_file_formats
        if dataset_type is not None:
            self.dataset_type = dataset_type
        if dataset_sub_type is not None:
            self.dataset_sub_type = dataset_sub_type
        if dataset_schema_format is not None:
            self.dataset_schema_format = dataset_schema_format
        if creator is not None:
            self.creator = creator
        if data_source_id is not None:
            self.data_source_id = data_source_id

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListAssetRequest.

        **参数解释**：排序方向。 **约束限制**：不涉及。 **取值范围**： 枚举值： - ASC: 升序 - DESC: 降序。 **默认取值**：DESC。

        :return: The sort_dir of this ListAssetRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListAssetRequest.

        **参数解释**：排序方向。 **约束限制**：不涉及。 **取值范围**： 枚举值： - ASC: 升序 - DESC: 降序。 **默认取值**：DESC。

        :param sort_dir: The sort_dir of this ListAssetRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListAssetRequest.

        **参数解释**：排序字段。 **约束限制**：不涉及。 **取值范围**：枚举值： - created_at: 创建时间 - updated_at: 更新时间。 **默认取值**：created_at。

        :return: The sort_key of this ListAssetRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListAssetRequest.

        **参数解释**：排序字段。 **约束限制**：不涉及。 **取值范围**：枚举值： - created_at: 创建时间 - updated_at: 更新时间。 **默认取值**：created_at。

        :param sort_key: The sort_key of this ListAssetRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def limit(self):
        r"""Gets the limit of this ListAssetRequest.

        **参数解释**：限制量，单次查询总量，必须由数字组成。 **约束限制**：不涉及。 **取值范围**：1-1000。 **默认取值**：100。

        :return: The limit of this ListAssetRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAssetRequest.

        **参数解释**：限制量，单次查询总量，必须由数字组成。 **约束限制**：不涉及。 **取值范围**：1-1000。 **默认取值**：100。

        :param limit: The limit of this ListAssetRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAssetRequest.

        **参数解释**：偏移量，查询起始偏移，必须由数字组成。 **约束限制**：不涉及。 **取值范围**0-100000000。 **默认取值**：0。

        :return: The offset of this ListAssetRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAssetRequest.

        **参数解释**：偏移量，查询起始偏移，必须由数字组成。 **约束限制**：不涉及。 **取值范围**0-100000000。 **默认取值**：0。

        :param offset: The offset of this ListAssetRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListAssetRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :return: The workspace_id of this ListAssetRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListAssetRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :param workspace_id: The workspace_id of this ListAssetRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def asset_name(self):
        r"""Gets the asset_name of this ListAssetRequest.

        **参数解释**：资产名称,支持英文字母，数字，中划线，下划线，点，空格，中文汉字。 **约束限制**：1-128位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_name of this ListAssetRequest.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this ListAssetRequest.

        **参数解释**：资产名称,支持英文字母，数字，中划线，下划线，点，空格，中文汉字。 **约束限制**：1-128位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_name: The asset_name of this ListAssetRequest.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_type(self):
        r"""Gets the asset_type of this ListAssetRequest.

        **参数解释**: 资产类型。 **约束限制**: 枚举值: - MODEL: 模型资产 - TEMPLATE: 模板资产 - DATASET: 数据集资产 - WORKFLOW: 工作流资产 - IMAGE: 镜像资产 - ALGORITHM: 算法资产 - DATASET_TEMPLATE: 数据集模板资产 - DATA_OPERATOR: 算子镜像资产 **默认取值**: 不涉及。

        :return: The asset_type of this ListAssetRequest.
        :rtype: list[str]
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this ListAssetRequest.

        **参数解释**: 资产类型。 **约束限制**: 枚举值: - MODEL: 模型资产 - TEMPLATE: 模板资产 - DATASET: 数据集资产 - WORKFLOW: 工作流资产 - IMAGE: 镜像资产 - ALGORITHM: 算法资产 - DATASET_TEMPLATE: 数据集模板资产 - DATA_OPERATOR: 算子镜像资产 **默认取值**: 不涉及。

        :param asset_type: The asset_type of this ListAssetRequest.
        :type asset_type: list[str]
        """
        self._asset_type = asset_type

    @property
    def asset_source(self):
        r"""Gets the asset_source of this ListAssetRequest.

        **参数解释**：资产来源。 **约束限制**：不涉及。 **取值范围**：枚举值: - Preset: 预置资产 - Publish: 用户发布资产 - Import: 用户导入资产 **默认取值**：不涉及。

        :return: The asset_source of this ListAssetRequest.
        :rtype: str
        """
        return self._asset_source

    @asset_source.setter
    def asset_source(self, asset_source):
        r"""Sets the asset_source of this ListAssetRequest.

        **参数解释**：资产来源。 **约束限制**：不涉及。 **取值范围**：枚举值: - Preset: 预置资产 - Publish: 用户发布资产 - Import: 用户导入资产 **默认取值**：不涉及。

        :param asset_source: The asset_source of this ListAssetRequest.
        :type asset_source: str
        """
        self._asset_source = asset_source

    @property
    def asset_source_type(self):
        r"""Gets the asset_source_type of this ListAssetRequest.

        **参数解释**：用户资产来源。 **约束限制**：1-60位字符，英文字母，数字，下划线、中划线。 **取值范围**：preset_train：精调，custom_train：自定义训练，AgenticRL：强化学习。 **默认取值**：不涉及。

        :return: The asset_source_type of this ListAssetRequest.
        :rtype: str
        """
        return self._asset_source_type

    @asset_source_type.setter
    def asset_source_type(self, asset_source_type):
        r"""Sets the asset_source_type of this ListAssetRequest.

        **参数解释**：用户资产来源。 **约束限制**：1-60位字符，英文字母，数字，下划线、中划线。 **取值范围**：preset_train：精调，custom_train：自定义训练，AgenticRL：强化学习。 **默认取值**：不涉及。

        :param asset_source_type: The asset_source_type of this ListAssetRequest.
        :type asset_source_type: str
        """
        self._asset_source_type = asset_source_type

    @property
    def asset_code(self):
        r"""Gets the asset_code of this ListAssetRequest.

        **参数解释**：资产编码。 **约束限制**：1-60字母，数字，中划线，下划线，点。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_code of this ListAssetRequest.
        :rtype: str
        """
        return self._asset_code

    @asset_code.setter
    def asset_code(self, asset_code):
        r"""Sets the asset_code of this ListAssetRequest.

        **参数解释**：资产编码。 **约束限制**：1-60字母，数字，中划线，下划线，点。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_code: The asset_code of this ListAssetRequest.
        :type asset_code: str
        """
        self._asset_code = asset_code

    @property
    def asset_version(self):
        r"""Gets the asset_version of this ListAssetRequest.

        **参数解释**：资产版本。 **约束限制**：数字或格式为x.y.z，x,y,z为数字。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_version of this ListAssetRequest.
        :rtype: str
        """
        return self._asset_version

    @asset_version.setter
    def asset_version(self, asset_version):
        r"""Sets the asset_version of this ListAssetRequest.

        **参数解释**：资产版本。 **约束限制**：数字或格式为x.y.z，x,y,z为数字。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_version: The asset_version of this ListAssetRequest.
        :type asset_version: str
        """
        self._asset_version = asset_version

    @property
    def asset_group_id(self):
        r"""Gets the asset_group_id of this ListAssetRequest.

        **参数解释**：资产归属的资产组id，带有该字段将在同一个资产库中所有版本进行条件筛选，否则会筛选所有资产库中的主版本。 **约束限制**：1-36字母数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_group_id of this ListAssetRequest.
        :rtype: str
        """
        return self._asset_group_id

    @asset_group_id.setter
    def asset_group_id(self, asset_group_id):
        r"""Sets the asset_group_id of this ListAssetRequest.

        **参数解释**：资产归属的资产组id，带有该字段将在同一个资产库中所有版本进行条件筛选，否则会筛选所有资产库中的主版本。 **约束限制**：1-36字母数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_group_id: The asset_group_id of this ListAssetRequest.
        :type asset_group_id: str
        """
        self._asset_group_id = asset_group_id

    @property
    def filter_all_version(self):
        r"""Gets the filter_all_version of this ListAssetRequest.

        **参数解释**：是否过滤所有版本。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：false。

        :return: The filter_all_version of this ListAssetRequest.
        :rtype: bool
        """
        return self._filter_all_version

    @filter_all_version.setter
    def filter_all_version(self, filter_all_version):
        r"""Sets the filter_all_version of this ListAssetRequest.

        **参数解释**：是否过滤所有版本。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：false。

        :param filter_all_version: The filter_all_version of this ListAssetRequest.
        :type filter_all_version: bool
        """
        self._filter_all_version = filter_all_version

    @property
    def support_actions(self):
        r"""Gets the support_actions of this ListAssetRequest.

        **参数解释**：资产支持的操作列表，例如SFT：监督微调，LORA微调:LORA，在线部署：ONLINE-DEPLOY，强化学习：AgenticRL。 **约束限制**：每个元素1-30位字符，英文字母，数字，下划线，中划线；最多10个元素。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The support_actions of this ListAssetRequest.
        :rtype: list[str]
        """
        return self._support_actions

    @support_actions.setter
    def support_actions(self, support_actions):
        r"""Sets the support_actions of this ListAssetRequest.

        **参数解释**：资产支持的操作列表，例如SFT：监督微调，LORA微调:LORA，在线部署：ONLINE-DEPLOY，强化学习：AgenticRL。 **约束限制**：每个元素1-30位字符，英文字母，数字，下划线，中划线；最多10个元素。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param support_actions: The support_actions of this ListAssetRequest.
        :type support_actions: list[str]
        """
        self._support_actions = support_actions

    @property
    def tag(self):
        r"""Gets the tag of this ListAssetRequest.

        **参数解释**：检索资产时的标签，根据不同资产类型，条件可能不同。 - 需要匹配一个key对应一个value时格式为key=value - 需要匹配一个key对应多个value中的任意一个时格式为key=value1|value2|value3 - 需要匹配多个条件同时满足时key1=value1,key2=value2 - 如果需要实现模糊匹配格式为key1%=value2（右匹配）key2=%value2（左匹配） **约束限制**：不涉及。

        :return: The tag of this ListAssetRequest.
        :rtype: list[str]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListAssetRequest.

        **参数解释**：检索资产时的标签，根据不同资产类型，条件可能不同。 - 需要匹配一个key对应一个value时格式为key=value - 需要匹配一个key对应多个value中的任意一个时格式为key=value1|value2|value3 - 需要匹配多个条件同时满足时key1=value1,key2=value2 - 如果需要实现模糊匹配格式为key1%=value2（右匹配）key2=%value2（左匹配） **约束限制**：不涉及。

        :param tag: The tag of this ListAssetRequest.
        :type tag: list[str]
        """
        self._tag = tag

    @property
    def is_mine(self):
        r"""Gets the is_mine of this ListAssetRequest.

        **参数解释**：过滤我创建的资产，boolean类型，取值true：查询我创建的资产，取值false：查询所有资产。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The is_mine of this ListAssetRequest.
        :rtype: bool
        """
        return self._is_mine

    @is_mine.setter
    def is_mine(self, is_mine):
        r"""Sets the is_mine of this ListAssetRequest.

        **参数解释**：过滤我创建的资产，boolean类型，取值true：查询我创建的资产，取值false：查询所有资产。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param is_mine: The is_mine of this ListAssetRequest.
        :type is_mine: bool
        """
        self._is_mine = is_mine

    @property
    def with_actions(self):
        r"""Gets the with_actions of this ListAssetRequest.

        **参数解释**：列表查询是否包含action。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The with_actions of this ListAssetRequest.
        :rtype: bool
        """
        return self._with_actions

    @with_actions.setter
    def with_actions(self, with_actions):
        r"""Sets the with_actions of this ListAssetRequest.

        **参数解释**：列表查询是否包含action。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param with_actions: The with_actions of this ListAssetRequest.
        :type with_actions: bool
        """
        self._with_actions = with_actions

    @property
    def asset_series(self):
        r"""Gets the asset_series of this ListAssetRequest.

        **参数解释**：资产品牌，例如DeepSeek,Qwen,Wan,GPT,Llama,GLM,ERNIE,Mistral,Kimi,Other。 **约束限制**：不涉及。 **取值范围**：0-100位。 **默认取值**：不涉及。

        :return: The asset_series of this ListAssetRequest.
        :rtype: str
        """
        return self._asset_series

    @asset_series.setter
    def asset_series(self, asset_series):
        r"""Sets the asset_series of this ListAssetRequest.

        **参数解释**：资产品牌，例如DeepSeek,Qwen,Wan,GPT,Llama,GLM,ERNIE,Mistral,Kimi,Other。 **约束限制**：不涉及。 **取值范围**：0-100位。 **默认取值**：不涉及。

        :param asset_series: The asset_series of this ListAssetRequest.
        :type asset_series: str
        """
        self._asset_series = asset_series

    @property
    def asset_capabilities(self):
        r"""Gets the asset_capabilities of this ListAssetRequest.

        **参数解释**：资产能力，为自由文本字符串列表(非严格枚举)。推荐使用以下约定值：例如TextGeneration,ImageUnderstanding,ImageGeneration,VideoGeneration,AgenticRL,Other。 **约束限制**：每个元素为1-40位字符；最多10个元素。

        :return: The asset_capabilities of this ListAssetRequest.
        :rtype: list[str]
        """
        return self._asset_capabilities

    @asset_capabilities.setter
    def asset_capabilities(self, asset_capabilities):
        r"""Sets the asset_capabilities of this ListAssetRequest.

        **参数解释**：资产能力，为自由文本字符串列表(非严格枚举)。推荐使用以下约定值：例如TextGeneration,ImageUnderstanding,ImageGeneration,VideoGeneration,AgenticRL,Other。 **约束限制**：每个元素为1-40位字符；最多10个元素。

        :param asset_capabilities: The asset_capabilities of this ListAssetRequest.
        :type asset_capabilities: list[str]
        """
        self._asset_capabilities = asset_capabilities

    @property
    def asset_scenes(self):
        r"""Gets the asset_scenes of this ListAssetRequest.

        **参数解释**：资产场景，如DeepThinking。 **约束限制**：不涉及。

        :return: The asset_scenes of this ListAssetRequest.
        :rtype: list[str]
        """
        return self._asset_scenes

    @asset_scenes.setter
    def asset_scenes(self, asset_scenes):
        r"""Sets the asset_scenes of this ListAssetRequest.

        **参数解释**：资产场景，如DeepThinking。 **约束限制**：不涉及。

        :param asset_scenes: The asset_scenes of this ListAssetRequest.
        :type asset_scenes: list[str]
        """
        self._asset_scenes = asset_scenes

    @property
    def root_asset_id(self):
        r"""Gets the root_asset_id of this ListAssetRequest.

        **参数解释**：根资产id。 **约束限制**：1-36个字符，英文字母，数字，中划线，下划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The root_asset_id of this ListAssetRequest.
        :rtype: str
        """
        return self._root_asset_id

    @root_asset_id.setter
    def root_asset_id(self, root_asset_id):
        r"""Sets the root_asset_id of this ListAssetRequest.

        **参数解释**：根资产id。 **约束限制**：1-36个字符，英文字母，数字，中划线，下划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param root_asset_id: The root_asset_id of this ListAssetRequest.
        :type root_asset_id: str
        """
        self._root_asset_id = root_asset_id

    @property
    def parent_asset_id(self):
        r"""Gets the parent_asset_id of this ListAssetRequest.

        **参数解释**：父资产id。 **约束限制**：1-36个字符，英文字母，数字，中划线，下划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The parent_asset_id of this ListAssetRequest.
        :rtype: str
        """
        return self._parent_asset_id

    @parent_asset_id.setter
    def parent_asset_id(self, parent_asset_id):
        r"""Sets the parent_asset_id of this ListAssetRequest.

        **参数解释**：父资产id。 **约束限制**：1-36个字符，英文字母，数字，中划线，下划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param parent_asset_id: The parent_asset_id of this ListAssetRequest.
        :type parent_asset_id: str
        """
        self._parent_asset_id = parent_asset_id

    @property
    def is_deleted(self):
        r"""Gets the is_deleted of this ListAssetRequest.

        **参数解释**：是否返回软删除的资产。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：false。

        :return: The is_deleted of this ListAssetRequest.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        r"""Sets the is_deleted of this ListAssetRequest.

        **参数解释**：是否返回软删除的资产。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：false。

        :param is_deleted: The is_deleted of this ListAssetRequest.
        :type is_deleted: bool
        """
        self._is_deleted = is_deleted

    @property
    def asset_ids(self):
        r"""Gets the asset_ids of this ListAssetRequest.

        **参数解释**：资产id。 **约束限制**：0-100个。

        :return: The asset_ids of this ListAssetRequest.
        :rtype: list[str]
        """
        return self._asset_ids

    @asset_ids.setter
    def asset_ids(self, asset_ids):
        r"""Sets the asset_ids of this ListAssetRequest.

        **参数解释**：资产id。 **约束限制**：0-100个。

        :param asset_ids: The asset_ids of this ListAssetRequest.
        :type asset_ids: list[str]
        """
        self._asset_ids = asset_ids

    @property
    def tag_mode(self):
        r"""Gets the tag_mode of this ListAssetRequest.

        **参数解释**：tag组合方式 **约束限制**：不涉及。 **取值范围**：and：与，or：或。 **默认取值**：and。

        :return: The tag_mode of this ListAssetRequest.
        :rtype: str
        """
        return self._tag_mode

    @tag_mode.setter
    def tag_mode(self, tag_mode):
        r"""Sets the tag_mode of this ListAssetRequest.

        **参数解释**：tag组合方式 **约束限制**：不涉及。 **取值范围**：and：与，or：或。 **默认取值**：and。

        :param tag_mode: The tag_mode of this ListAssetRequest.
        :type tag_mode: str
        """
        self._tag_mode = tag_mode

    @property
    def dataset_usage(self):
        r"""Gets the dataset_usage of this ListAssetRequest.

        **参数解释**：数据集用途，例如 GENERAL：通用数据集、EVAL：评测集。 **约束限制**：1-40位字符，英文字母，数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The dataset_usage of this ListAssetRequest.
        :rtype: str
        """
        return self._dataset_usage

    @dataset_usage.setter
    def dataset_usage(self, dataset_usage):
        r"""Sets the dataset_usage of this ListAssetRequest.

        **参数解释**：数据集用途，例如 GENERAL：通用数据集、EVAL：评测集。 **约束限制**：1-40位字符，英文字母，数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param dataset_usage: The dataset_usage of this ListAssetRequest.
        :type dataset_usage: str
        """
        self._dataset_usage = dataset_usage

    @property
    def status(self):
        r"""Gets the status of this ListAssetRequest.

        **参数解释**：资产状态。 **约束限制**：不涉及。 **取值范围**：枚举值: - online: 上线 - offline: 下线 - waiting: 等待中 **默认取值**：不涉及。

        :return: The status of this ListAssetRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAssetRequest.

        **参数解释**：资产状态。 **约束限制**：不涉及。 **取值范围**：枚举值: - online: 上线 - offline: 下线 - waiting: 等待中 **默认取值**：不涉及。

        :param status: The status of this ListAssetRequest.
        :type status: str
        """
        self._status = status

    @property
    def dataset_file_formats(self):
        r"""Gets the dataset_file_formats of this ListAssetRequest.

        **参数解释**：数据集存储格式，例如JSONL，TXT，MOBI，EPUB，DOCX，PDF。 **约束限制**：不涉及。

        :return: The dataset_file_formats of this ListAssetRequest.
        :rtype: list[str]
        """
        return self._dataset_file_formats

    @dataset_file_formats.setter
    def dataset_file_formats(self, dataset_file_formats):
        r"""Sets the dataset_file_formats of this ListAssetRequest.

        **参数解释**：数据集存储格式，例如JSONL，TXT，MOBI，EPUB，DOCX，PDF。 **约束限制**：不涉及。

        :param dataset_file_formats: The dataset_file_formats of this ListAssetRequest.
        :type dataset_file_formats: list[str]
        """
        self._dataset_file_formats = dataset_file_formats

    @property
    def dataset_type(self):
        r"""Gets the dataset_type of this ListAssetRequest.

        **参数解释**：数据集模态划分，如音频，图像，视频。 **约束限制**：1-40位字符，英文字母，数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The dataset_type of this ListAssetRequest.
        :rtype: str
        """
        return self._dataset_type

    @dataset_type.setter
    def dataset_type(self, dataset_type):
        r"""Sets the dataset_type of this ListAssetRequest.

        **参数解释**：数据集模态划分，如音频，图像，视频。 **约束限制**：1-40位字符，英文字母，数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param dataset_type: The dataset_type of this ListAssetRequest.
        :type dataset_type: str
        """
        self._dataset_type = dataset_type

    @property
    def dataset_sub_type(self):
        r"""Gets the dataset_sub_type of this ListAssetRequest.

        **参数解释**：数据集模态细分值，如语义分割。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The dataset_sub_type of this ListAssetRequest.
        :rtype: str
        """
        return self._dataset_sub_type

    @dataset_sub_type.setter
    def dataset_sub_type(self, dataset_sub_type):
        r"""Sets the dataset_sub_type of this ListAssetRequest.

        **参数解释**：数据集模态细分值，如语义分割。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param dataset_sub_type: The dataset_sub_type of this ListAssetRequest.
        :type dataset_sub_type: str
        """
        self._dataset_sub_type = dataset_sub_type

    @property
    def dataset_schema_format(self):
        r"""Gets the dataset_schema_format of this ListAssetRequest.

        **参数解释**：数据集逻辑规范，如盘古格式。 **约束限制**：1-40位字符，英文字母，数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The dataset_schema_format of this ListAssetRequest.
        :rtype: str
        """
        return self._dataset_schema_format

    @dataset_schema_format.setter
    def dataset_schema_format(self, dataset_schema_format):
        r"""Sets the dataset_schema_format of this ListAssetRequest.

        **参数解释**：数据集逻辑规范，如盘古格式。 **约束限制**：1-40位字符，英文字母，数字，下划线，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param dataset_schema_format: The dataset_schema_format of this ListAssetRequest.
        :type dataset_schema_format: str
        """
        self._dataset_schema_format = dataset_schema_format

    @property
    def creator(self):
        r"""Gets the creator of this ListAssetRequest.

        **参数解释**：资产创建者。 **约束限制**：1-512位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The creator of this ListAssetRequest.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ListAssetRequest.

        **参数解释**：资产创建者。 **约束限制**：1-512位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param creator: The creator of this ListAssetRequest.
        :type creator: str
        """
        self._creator = creator

    @property
    def data_source_id(self):
        r"""Gets the data_source_id of this ListAssetRequest.

        **参数解释**：数据源的ID信息。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The data_source_id of this ListAssetRequest.
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        r"""Sets the data_source_id of this ListAssetRequest.

        **参数解释**：数据源的ID信息。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param data_source_id: The data_source_id of this ListAssetRequest.
        :type data_source_id: str
        """
        self._data_source_id = data_source_id

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
        if not isinstance(other, ListAssetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
