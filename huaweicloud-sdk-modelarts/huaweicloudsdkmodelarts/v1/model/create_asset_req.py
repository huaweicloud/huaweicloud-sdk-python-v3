# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAssetReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_asset_id': 'str',
        'api_version': 'str',
        'asset_name': 'str',
        'asset_source': 'str',
        'asset_source_type': 'str',
        'asset_code': 'str',
        'asset_desc': 'str',
        'asset_group_desc': 'str',
        'asset_version': 'str',
        'support_actions': 'list[str]',
        'asset_location': 'str',
        'asset_type': 'str',
        'asset_group_id': 'str',
        'asset_series': 'str',
        'asset_capabilities': 'list[str]',
        'actions': 'list[AssetActionReq]',
        'source_operation': 'str',
        'source_job_name': 'str',
        'source_job_id': 'str',
        'status': 'str',
        'dataset_usage': 'str',
        'dataset_file_formats': 'list[str]',
        'dataset_type': 'str',
        'dataset_sub_type': 'str',
        'dataset_schema_format': 'str',
        'import_file_source': 'str',
        'data_source_id': 'str'
    }

    attribute_map = {
        'parent_asset_id': 'parent_asset_id',
        'api_version': 'api_version',
        'asset_name': 'asset_name',
        'asset_source': 'asset_source',
        'asset_source_type': 'asset_source_type',
        'asset_code': 'asset_code',
        'asset_desc': 'asset_desc',
        'asset_group_desc': 'asset_group_desc',
        'asset_version': 'asset_version',
        'support_actions': 'support_actions',
        'asset_location': 'asset_location',
        'asset_type': 'asset_type',
        'asset_group_id': 'asset_group_id',
        'asset_series': 'asset_series',
        'asset_capabilities': 'asset_capabilities',
        'actions': 'actions',
        'source_operation': 'source_operation',
        'source_job_name': 'source_job_name',
        'source_job_id': 'source_job_id',
        'status': 'status',
        'dataset_usage': 'dataset_usage',
        'dataset_file_formats': 'dataset_file_formats',
        'dataset_type': 'dataset_type',
        'dataset_sub_type': 'dataset_sub_type',
        'dataset_schema_format': 'dataset_schema_format',
        'import_file_source': 'import_file_source',
        'data_source_id': 'data_source_id'
    }

    def __init__(self, parent_asset_id=None, api_version=None, asset_name=None, asset_source=None, asset_source_type=None, asset_code=None, asset_desc=None, asset_group_desc=None, asset_version=None, support_actions=None, asset_location=None, asset_type=None, asset_group_id=None, asset_series=None, asset_capabilities=None, actions=None, source_operation=None, source_job_name=None, source_job_id=None, status=None, dataset_usage=None, dataset_file_formats=None, dataset_type=None, dataset_sub_type=None, dataset_schema_format=None, import_file_source=None, data_source_id=None):
        r"""CreateAssetReq

        The model defined in huaweicloud sdk

        :param parent_asset_id: **参数解释**：父资产id。 **约束限制**：1-36位字符，英文字母，数字，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type parent_asset_id: str
        :param api_version: **参数解释**：资产API版本，固定v2。 **约束限制**：固定v2。 **取值范围**：v2。 **默认取值**：v2。
        :type api_version: str
        :param asset_name: **参数解释**：资产名称。 **约束限制**：1-128位字符，只包含中文、字母、数字、中划线、下划线。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_name: str
        :param asset_source: **参数解释**：用户资产来源。 **约束限制**：不涉及。 **取值范围**：枚举值： - Publish：发布 - Import：导入 **默认取值**：不涉及。
        :type asset_source: str
        :param asset_source_type: **参数解释**：用户资产来源类型。 **约束限制**：不涉及。 **取值范围**：枚举值： - preset_train：预训练 - custom_train：用户训练 - AgenticRL：强化学习 - DATA_CLEANING：数据清洗 - DATA_IMPORT：数据导入 - DATA_ANNOTATION：数据标注 **默认取值**：不涉及。
        :type asset_source_type: str
        :param asset_code: **参数解释**：资产code。 **约束限制**：1-60字符，英文字母，数字，中划线，下划线，点。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_code: str
        :param asset_desc: **参数解释**：资产描述。 **约束限制**：0-512位字符，不能包含英文尖括号（即 &lt; 或 &gt;）。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_desc: str
        :param asset_group_desc: **参数解释**：资产组描述。 **约束限制**：0-512位字符，不能包含英文尖括号（即 &lt; 或 &gt;）。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_group_desc: str
        :param asset_version: **参数解释**：资产版本号。 **约束限制**：0-99数字字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_version: str
        :param support_actions: **参数解释**：资产支持的操作列表，例如监督微调:SFT,LORA微调:LORA,在线部署:ONLINE-DEPLOY,强化学习:AgenticRL。 **约束限制**：不涉及。
        :type support_actions: list[str]
        :param asset_location: **参数解释**：资产文件存储地址,支持OBS（对象存储服务）协议的URL和相对路径。 **约束限制**：0-1024位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_location: str
        :param asset_type: **参数解释**：资产类型。 **约束限制**：当不传parent_asset_id时必填。 **取值范围**：枚举值: - MODEL: 模型资产 - TEMPLATE: 模板资产 - DATASET: 数据集资产 - WORKFLOW: 工作流资产 - IMAGE: 镜像资产 - ALGORITHM：算法资产 - DATASET_TEMPLATE: 数据集模板资产 - DATA_OPERATOR：算子镜像资产 **默认取值**：不涉及。
        :type asset_type: str
        :param asset_group_id: **参数解释**：需要加入的资产组id。 **约束限制**：1-36位字符，已存在的组id。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_group_id: str
        :param asset_series: **参数解释**：资产品牌，例如DeepSeek,Qwen,Wan,GPT,Llama,GLM,ERNIE,Mistral,Kimi,Other。 **约束限制**：1-40位字符，仅支持英文字母、数字、下划线和中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_series: str
        :param asset_capabilities: **参数解释**：资产能力，为自由文本字符串列表(非严格枚举)。推荐使用以下约定值：例如TextGeneration,ImageUnderstanding,ImageGeneration,VideoGeneration,Other。 **约束限制**：每个元素1-40位字符，仅支持英文字母、数字、下划线和中划线；最多10个元素。
        :type asset_capabilities: list[str]
        :param actions: **参数解释**：资产可执行操作详情配置。 **约束限制**：不涉及。
        :type actions: list[:class:`huaweicloudsdkmodelarts.v1.AssetActionReq`]
        :param source_operation: **参数解释**：模型来源于哪个操作。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type source_operation: str
        :param source_job_name: **参数解释**：模型来源作业的名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type source_job_name: str
        :param source_job_id: **参数解释**：模型来源作业的ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type source_job_id: str
        :param status: **参数解释**：资产状态。 **约束限制**：不涉及。 **取值范围**：枚举值: - online: 上线 - offline: 下线 - waiting: 等待中 **默认取值**：不涉及。
        :type status: str
        :param dataset_usage: **参数解释**：数据集用途。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type dataset_usage: str
        :param dataset_file_formats: **参数解释**：数据集存储格式，例如JSONL，TXT，MOBI，EPUB，DOCX，PDF。 **约束限制**：0-40位字符。
        :type dataset_file_formats: list[str]
        :param dataset_type: **参数解释**：数据集模态划分，如音频，图像，视频。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type dataset_type: str
        :param dataset_sub_type: **参数解释**：数据集模态细分值，如语义分割。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type dataset_sub_type: str
        :param dataset_schema_format: **参数解释**：数据集逻辑规范，如盘古格式。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type dataset_schema_format: str
        :param import_file_source: **参数解释**：导入文件来源。 **约束限制**：数据集资产导入时需要。 **取值范围**：枚举值: - OBS: 从OBS导入 - LOCAL: 从本地导入 **默认取值**：不涉及。
        :type import_file_source: str
        :param data_source_id: **参数解释**：数据集资产数据源的ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type data_source_id: str
        """
        
        

        self._parent_asset_id = None
        self._api_version = None
        self._asset_name = None
        self._asset_source = None
        self._asset_source_type = None
        self._asset_code = None
        self._asset_desc = None
        self._asset_group_desc = None
        self._asset_version = None
        self._support_actions = None
        self._asset_location = None
        self._asset_type = None
        self._asset_group_id = None
        self._asset_series = None
        self._asset_capabilities = None
        self._actions = None
        self._source_operation = None
        self._source_job_name = None
        self._source_job_id = None
        self._status = None
        self._dataset_usage = None
        self._dataset_file_formats = None
        self._dataset_type = None
        self._dataset_sub_type = None
        self._dataset_schema_format = None
        self._import_file_source = None
        self._data_source_id = None
        self.discriminator = None

        if parent_asset_id is not None:
            self.parent_asset_id = parent_asset_id
        if api_version is not None:
            self.api_version = api_version
        if asset_name is not None:
            self.asset_name = asset_name
        if asset_source is not None:
            self.asset_source = asset_source
        if asset_source_type is not None:
            self.asset_source_type = asset_source_type
        if asset_code is not None:
            self.asset_code = asset_code
        if asset_desc is not None:
            self.asset_desc = asset_desc
        if asset_group_desc is not None:
            self.asset_group_desc = asset_group_desc
        self.asset_version = asset_version
        if support_actions is not None:
            self.support_actions = support_actions
        if asset_location is not None:
            self.asset_location = asset_location
        if asset_type is not None:
            self.asset_type = asset_type
        if asset_group_id is not None:
            self.asset_group_id = asset_group_id
        if asset_series is not None:
            self.asset_series = asset_series
        if asset_capabilities is not None:
            self.asset_capabilities = asset_capabilities
        if actions is not None:
            self.actions = actions
        if source_operation is not None:
            self.source_operation = source_operation
        if source_job_name is not None:
            self.source_job_name = source_job_name
        if source_job_id is not None:
            self.source_job_id = source_job_id
        if status is not None:
            self.status = status
        if dataset_usage is not None:
            self.dataset_usage = dataset_usage
        if dataset_file_formats is not None:
            self.dataset_file_formats = dataset_file_formats
        if dataset_type is not None:
            self.dataset_type = dataset_type
        if dataset_sub_type is not None:
            self.dataset_sub_type = dataset_sub_type
        if dataset_schema_format is not None:
            self.dataset_schema_format = dataset_schema_format
        if import_file_source is not None:
            self.import_file_source = import_file_source
        if data_source_id is not None:
            self.data_source_id = data_source_id

    @property
    def parent_asset_id(self):
        r"""Gets the parent_asset_id of this CreateAssetReq.

        **参数解释**：父资产id。 **约束限制**：1-36位字符，英文字母，数字，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The parent_asset_id of this CreateAssetReq.
        :rtype: str
        """
        return self._parent_asset_id

    @parent_asset_id.setter
    def parent_asset_id(self, parent_asset_id):
        r"""Sets the parent_asset_id of this CreateAssetReq.

        **参数解释**：父资产id。 **约束限制**：1-36位字符，英文字母，数字，中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param parent_asset_id: The parent_asset_id of this CreateAssetReq.
        :type parent_asset_id: str
        """
        self._parent_asset_id = parent_asset_id

    @property
    def api_version(self):
        r"""Gets the api_version of this CreateAssetReq.

        **参数解释**：资产API版本，固定v2。 **约束限制**：固定v2。 **取值范围**：v2。 **默认取值**：v2。

        :return: The api_version of this CreateAssetReq.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this CreateAssetReq.

        **参数解释**：资产API版本，固定v2。 **约束限制**：固定v2。 **取值范围**：v2。 **默认取值**：v2。

        :param api_version: The api_version of this CreateAssetReq.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def asset_name(self):
        r"""Gets the asset_name of this CreateAssetReq.

        **参数解释**：资产名称。 **约束限制**：1-128位字符，只包含中文、字母、数字、中划线、下划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_name of this CreateAssetReq.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this CreateAssetReq.

        **参数解释**：资产名称。 **约束限制**：1-128位字符，只包含中文、字母、数字、中划线、下划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_name: The asset_name of this CreateAssetReq.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_source(self):
        r"""Gets the asset_source of this CreateAssetReq.

        **参数解释**：用户资产来源。 **约束限制**：不涉及。 **取值范围**：枚举值： - Publish：发布 - Import：导入 **默认取值**：不涉及。

        :return: The asset_source of this CreateAssetReq.
        :rtype: str
        """
        return self._asset_source

    @asset_source.setter
    def asset_source(self, asset_source):
        r"""Sets the asset_source of this CreateAssetReq.

        **参数解释**：用户资产来源。 **约束限制**：不涉及。 **取值范围**：枚举值： - Publish：发布 - Import：导入 **默认取值**：不涉及。

        :param asset_source: The asset_source of this CreateAssetReq.
        :type asset_source: str
        """
        self._asset_source = asset_source

    @property
    def asset_source_type(self):
        r"""Gets the asset_source_type of this CreateAssetReq.

        **参数解释**：用户资产来源类型。 **约束限制**：不涉及。 **取值范围**：枚举值： - preset_train：预训练 - custom_train：用户训练 - AgenticRL：强化学习 - DATA_CLEANING：数据清洗 - DATA_IMPORT：数据导入 - DATA_ANNOTATION：数据标注 **默认取值**：不涉及。

        :return: The asset_source_type of this CreateAssetReq.
        :rtype: str
        """
        return self._asset_source_type

    @asset_source_type.setter
    def asset_source_type(self, asset_source_type):
        r"""Sets the asset_source_type of this CreateAssetReq.

        **参数解释**：用户资产来源类型。 **约束限制**：不涉及。 **取值范围**：枚举值： - preset_train：预训练 - custom_train：用户训练 - AgenticRL：强化学习 - DATA_CLEANING：数据清洗 - DATA_IMPORT：数据导入 - DATA_ANNOTATION：数据标注 **默认取值**：不涉及。

        :param asset_source_type: The asset_source_type of this CreateAssetReq.
        :type asset_source_type: str
        """
        self._asset_source_type = asset_source_type

    @property
    def asset_code(self):
        r"""Gets the asset_code of this CreateAssetReq.

        **参数解释**：资产code。 **约束限制**：1-60字符，英文字母，数字，中划线，下划线，点。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_code of this CreateAssetReq.
        :rtype: str
        """
        return self._asset_code

    @asset_code.setter
    def asset_code(self, asset_code):
        r"""Sets the asset_code of this CreateAssetReq.

        **参数解释**：资产code。 **约束限制**：1-60字符，英文字母，数字，中划线，下划线，点。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_code: The asset_code of this CreateAssetReq.
        :type asset_code: str
        """
        self._asset_code = asset_code

    @property
    def asset_desc(self):
        r"""Gets the asset_desc of this CreateAssetReq.

        **参数解释**：资产描述。 **约束限制**：0-512位字符，不能包含英文尖括号（即 < 或 >）。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_desc of this CreateAssetReq.
        :rtype: str
        """
        return self._asset_desc

    @asset_desc.setter
    def asset_desc(self, asset_desc):
        r"""Sets the asset_desc of this CreateAssetReq.

        **参数解释**：资产描述。 **约束限制**：0-512位字符，不能包含英文尖括号（即 < 或 >）。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_desc: The asset_desc of this CreateAssetReq.
        :type asset_desc: str
        """
        self._asset_desc = asset_desc

    @property
    def asset_group_desc(self):
        r"""Gets the asset_group_desc of this CreateAssetReq.

        **参数解释**：资产组描述。 **约束限制**：0-512位字符，不能包含英文尖括号（即 < 或 >）。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_group_desc of this CreateAssetReq.
        :rtype: str
        """
        return self._asset_group_desc

    @asset_group_desc.setter
    def asset_group_desc(self, asset_group_desc):
        r"""Sets the asset_group_desc of this CreateAssetReq.

        **参数解释**：资产组描述。 **约束限制**：0-512位字符，不能包含英文尖括号（即 < 或 >）。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_group_desc: The asset_group_desc of this CreateAssetReq.
        :type asset_group_desc: str
        """
        self._asset_group_desc = asset_group_desc

    @property
    def asset_version(self):
        r"""Gets the asset_version of this CreateAssetReq.

        **参数解释**：资产版本号。 **约束限制**：0-99数字字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_version of this CreateAssetReq.
        :rtype: str
        """
        return self._asset_version

    @asset_version.setter
    def asset_version(self, asset_version):
        r"""Sets the asset_version of this CreateAssetReq.

        **参数解释**：资产版本号。 **约束限制**：0-99数字字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_version: The asset_version of this CreateAssetReq.
        :type asset_version: str
        """
        self._asset_version = asset_version

    @property
    def support_actions(self):
        r"""Gets the support_actions of this CreateAssetReq.

        **参数解释**：资产支持的操作列表，例如监督微调:SFT,LORA微调:LORA,在线部署:ONLINE-DEPLOY,强化学习:AgenticRL。 **约束限制**：不涉及。

        :return: The support_actions of this CreateAssetReq.
        :rtype: list[str]
        """
        return self._support_actions

    @support_actions.setter
    def support_actions(self, support_actions):
        r"""Sets the support_actions of this CreateAssetReq.

        **参数解释**：资产支持的操作列表，例如监督微调:SFT,LORA微调:LORA,在线部署:ONLINE-DEPLOY,强化学习:AgenticRL。 **约束限制**：不涉及。

        :param support_actions: The support_actions of this CreateAssetReq.
        :type support_actions: list[str]
        """
        self._support_actions = support_actions

    @property
    def asset_location(self):
        r"""Gets the asset_location of this CreateAssetReq.

        **参数解释**：资产文件存储地址,支持OBS（对象存储服务）协议的URL和相对路径。 **约束限制**：0-1024位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_location of this CreateAssetReq.
        :rtype: str
        """
        return self._asset_location

    @asset_location.setter
    def asset_location(self, asset_location):
        r"""Sets the asset_location of this CreateAssetReq.

        **参数解释**：资产文件存储地址,支持OBS（对象存储服务）协议的URL和相对路径。 **约束限制**：0-1024位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_location: The asset_location of this CreateAssetReq.
        :type asset_location: str
        """
        self._asset_location = asset_location

    @property
    def asset_type(self):
        r"""Gets the asset_type of this CreateAssetReq.

        **参数解释**：资产类型。 **约束限制**：当不传parent_asset_id时必填。 **取值范围**：枚举值: - MODEL: 模型资产 - TEMPLATE: 模板资产 - DATASET: 数据集资产 - WORKFLOW: 工作流资产 - IMAGE: 镜像资产 - ALGORITHM：算法资产 - DATASET_TEMPLATE: 数据集模板资产 - DATA_OPERATOR：算子镜像资产 **默认取值**：不涉及。

        :return: The asset_type of this CreateAssetReq.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this CreateAssetReq.

        **参数解释**：资产类型。 **约束限制**：当不传parent_asset_id时必填。 **取值范围**：枚举值: - MODEL: 模型资产 - TEMPLATE: 模板资产 - DATASET: 数据集资产 - WORKFLOW: 工作流资产 - IMAGE: 镜像资产 - ALGORITHM：算法资产 - DATASET_TEMPLATE: 数据集模板资产 - DATA_OPERATOR：算子镜像资产 **默认取值**：不涉及。

        :param asset_type: The asset_type of this CreateAssetReq.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def asset_group_id(self):
        r"""Gets the asset_group_id of this CreateAssetReq.

        **参数解释**：需要加入的资产组id。 **约束限制**：1-36位字符，已存在的组id。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_group_id of this CreateAssetReq.
        :rtype: str
        """
        return self._asset_group_id

    @asset_group_id.setter
    def asset_group_id(self, asset_group_id):
        r"""Sets the asset_group_id of this CreateAssetReq.

        **参数解释**：需要加入的资产组id。 **约束限制**：1-36位字符，已存在的组id。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_group_id: The asset_group_id of this CreateAssetReq.
        :type asset_group_id: str
        """
        self._asset_group_id = asset_group_id

    @property
    def asset_series(self):
        r"""Gets the asset_series of this CreateAssetReq.

        **参数解释**：资产品牌，例如DeepSeek,Qwen,Wan,GPT,Llama,GLM,ERNIE,Mistral,Kimi,Other。 **约束限制**：1-40位字符，仅支持英文字母、数字、下划线和中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_series of this CreateAssetReq.
        :rtype: str
        """
        return self._asset_series

    @asset_series.setter
    def asset_series(self, asset_series):
        r"""Sets the asset_series of this CreateAssetReq.

        **参数解释**：资产品牌，例如DeepSeek,Qwen,Wan,GPT,Llama,GLM,ERNIE,Mistral,Kimi,Other。 **约束限制**：1-40位字符，仅支持英文字母、数字、下划线和中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_series: The asset_series of this CreateAssetReq.
        :type asset_series: str
        """
        self._asset_series = asset_series

    @property
    def asset_capabilities(self):
        r"""Gets the asset_capabilities of this CreateAssetReq.

        **参数解释**：资产能力，为自由文本字符串列表(非严格枚举)。推荐使用以下约定值：例如TextGeneration,ImageUnderstanding,ImageGeneration,VideoGeneration,Other。 **约束限制**：每个元素1-40位字符，仅支持英文字母、数字、下划线和中划线；最多10个元素。

        :return: The asset_capabilities of this CreateAssetReq.
        :rtype: list[str]
        """
        return self._asset_capabilities

    @asset_capabilities.setter
    def asset_capabilities(self, asset_capabilities):
        r"""Sets the asset_capabilities of this CreateAssetReq.

        **参数解释**：资产能力，为自由文本字符串列表(非严格枚举)。推荐使用以下约定值：例如TextGeneration,ImageUnderstanding,ImageGeneration,VideoGeneration,Other。 **约束限制**：每个元素1-40位字符，仅支持英文字母、数字、下划线和中划线；最多10个元素。

        :param asset_capabilities: The asset_capabilities of this CreateAssetReq.
        :type asset_capabilities: list[str]
        """
        self._asset_capabilities = asset_capabilities

    @property
    def actions(self):
        r"""Gets the actions of this CreateAssetReq.

        **参数解释**：资产可执行操作详情配置。 **约束限制**：不涉及。

        :return: The actions of this CreateAssetReq.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.AssetActionReq`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this CreateAssetReq.

        **参数解释**：资产可执行操作详情配置。 **约束限制**：不涉及。

        :param actions: The actions of this CreateAssetReq.
        :type actions: list[:class:`huaweicloudsdkmodelarts.v1.AssetActionReq`]
        """
        self._actions = actions

    @property
    def source_operation(self):
        r"""Gets the source_operation of this CreateAssetReq.

        **参数解释**：模型来源于哪个操作。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The source_operation of this CreateAssetReq.
        :rtype: str
        """
        return self._source_operation

    @source_operation.setter
    def source_operation(self, source_operation):
        r"""Sets the source_operation of this CreateAssetReq.

        **参数解释**：模型来源于哪个操作。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param source_operation: The source_operation of this CreateAssetReq.
        :type source_operation: str
        """
        self._source_operation = source_operation

    @property
    def source_job_name(self):
        r"""Gets the source_job_name of this CreateAssetReq.

        **参数解释**：模型来源作业的名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The source_job_name of this CreateAssetReq.
        :rtype: str
        """
        return self._source_job_name

    @source_job_name.setter
    def source_job_name(self, source_job_name):
        r"""Sets the source_job_name of this CreateAssetReq.

        **参数解释**：模型来源作业的名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param source_job_name: The source_job_name of this CreateAssetReq.
        :type source_job_name: str
        """
        self._source_job_name = source_job_name

    @property
    def source_job_id(self):
        r"""Gets the source_job_id of this CreateAssetReq.

        **参数解释**：模型来源作业的ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The source_job_id of this CreateAssetReq.
        :rtype: str
        """
        return self._source_job_id

    @source_job_id.setter
    def source_job_id(self, source_job_id):
        r"""Sets the source_job_id of this CreateAssetReq.

        **参数解释**：模型来源作业的ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param source_job_id: The source_job_id of this CreateAssetReq.
        :type source_job_id: str
        """
        self._source_job_id = source_job_id

    @property
    def status(self):
        r"""Gets the status of this CreateAssetReq.

        **参数解释**：资产状态。 **约束限制**：不涉及。 **取值范围**：枚举值: - online: 上线 - offline: 下线 - waiting: 等待中 **默认取值**：不涉及。

        :return: The status of this CreateAssetReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateAssetReq.

        **参数解释**：资产状态。 **约束限制**：不涉及。 **取值范围**：枚举值: - online: 上线 - offline: 下线 - waiting: 等待中 **默认取值**：不涉及。

        :param status: The status of this CreateAssetReq.
        :type status: str
        """
        self._status = status

    @property
    def dataset_usage(self):
        r"""Gets the dataset_usage of this CreateAssetReq.

        **参数解释**：数据集用途。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The dataset_usage of this CreateAssetReq.
        :rtype: str
        """
        return self._dataset_usage

    @dataset_usage.setter
    def dataset_usage(self, dataset_usage):
        r"""Sets the dataset_usage of this CreateAssetReq.

        **参数解释**：数据集用途。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param dataset_usage: The dataset_usage of this CreateAssetReq.
        :type dataset_usage: str
        """
        self._dataset_usage = dataset_usage

    @property
    def dataset_file_formats(self):
        r"""Gets the dataset_file_formats of this CreateAssetReq.

        **参数解释**：数据集存储格式，例如JSONL，TXT，MOBI，EPUB，DOCX，PDF。 **约束限制**：0-40位字符。

        :return: The dataset_file_formats of this CreateAssetReq.
        :rtype: list[str]
        """
        return self._dataset_file_formats

    @dataset_file_formats.setter
    def dataset_file_formats(self, dataset_file_formats):
        r"""Sets the dataset_file_formats of this CreateAssetReq.

        **参数解释**：数据集存储格式，例如JSONL，TXT，MOBI，EPUB，DOCX，PDF。 **约束限制**：0-40位字符。

        :param dataset_file_formats: The dataset_file_formats of this CreateAssetReq.
        :type dataset_file_formats: list[str]
        """
        self._dataset_file_formats = dataset_file_formats

    @property
    def dataset_type(self):
        r"""Gets the dataset_type of this CreateAssetReq.

        **参数解释**：数据集模态划分，如音频，图像，视频。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The dataset_type of this CreateAssetReq.
        :rtype: str
        """
        return self._dataset_type

    @dataset_type.setter
    def dataset_type(self, dataset_type):
        r"""Sets the dataset_type of this CreateAssetReq.

        **参数解释**：数据集模态划分，如音频，图像，视频。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param dataset_type: The dataset_type of this CreateAssetReq.
        :type dataset_type: str
        """
        self._dataset_type = dataset_type

    @property
    def dataset_sub_type(self):
        r"""Gets the dataset_sub_type of this CreateAssetReq.

        **参数解释**：数据集模态细分值，如语义分割。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The dataset_sub_type of this CreateAssetReq.
        :rtype: str
        """
        return self._dataset_sub_type

    @dataset_sub_type.setter
    def dataset_sub_type(self, dataset_sub_type):
        r"""Sets the dataset_sub_type of this CreateAssetReq.

        **参数解释**：数据集模态细分值，如语义分割。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param dataset_sub_type: The dataset_sub_type of this CreateAssetReq.
        :type dataset_sub_type: str
        """
        self._dataset_sub_type = dataset_sub_type

    @property
    def dataset_schema_format(self):
        r"""Gets the dataset_schema_format of this CreateAssetReq.

        **参数解释**：数据集逻辑规范，如盘古格式。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The dataset_schema_format of this CreateAssetReq.
        :rtype: str
        """
        return self._dataset_schema_format

    @dataset_schema_format.setter
    def dataset_schema_format(self, dataset_schema_format):
        r"""Sets the dataset_schema_format of this CreateAssetReq.

        **参数解释**：数据集逻辑规范，如盘古格式。 **约束限制**：1-40位字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param dataset_schema_format: The dataset_schema_format of this CreateAssetReq.
        :type dataset_schema_format: str
        """
        self._dataset_schema_format = dataset_schema_format

    @property
    def import_file_source(self):
        r"""Gets the import_file_source of this CreateAssetReq.

        **参数解释**：导入文件来源。 **约束限制**：数据集资产导入时需要。 **取值范围**：枚举值: - OBS: 从OBS导入 - LOCAL: 从本地导入 **默认取值**：不涉及。

        :return: The import_file_source of this CreateAssetReq.
        :rtype: str
        """
        return self._import_file_source

    @import_file_source.setter
    def import_file_source(self, import_file_source):
        r"""Sets the import_file_source of this CreateAssetReq.

        **参数解释**：导入文件来源。 **约束限制**：数据集资产导入时需要。 **取值范围**：枚举值: - OBS: 从OBS导入 - LOCAL: 从本地导入 **默认取值**：不涉及。

        :param import_file_source: The import_file_source of this CreateAssetReq.
        :type import_file_source: str
        """
        self._import_file_source = import_file_source

    @property
    def data_source_id(self):
        r"""Gets the data_source_id of this CreateAssetReq.

        **参数解释**：数据集资产数据源的ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The data_source_id of this CreateAssetReq.
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        r"""Sets the data_source_id of this CreateAssetReq.

        **参数解释**：数据集资产数据源的ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param data_source_id: The data_source_id of this CreateAssetReq.
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
        if not isinstance(other, CreateAssetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
