# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'parent_asset_id': 'str',
        'root_asset_id': 'str',
        'api_version': 'str',
        'asset_name': 'str',
        'asset_group_id': 'str',
        'workspace_id': 'str',
        'asset_type': 'str',
        'sub_asset_type': 'str',
        'asset_desc': 'str',
        'asset_code': 'str',
        'asset_version': 'str',
        'tags': 'dict(str, list[str])',
        'support_actions': 'object',
        'asset_location': 'str',
        'actions': 'list[AssetActionRsp]',
        'status': 'str',
        'dataset_usage': 'str',
        'dataset_file_formats': 'list[str]',
        'dataset_type': 'str',
        'dataset_sub_type': 'str',
        'dataset_schema_format': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'parent_asset_id': 'parent_asset_id',
        'root_asset_id': 'root_asset_id',
        'api_version': 'api_version',
        'asset_name': 'asset_name',
        'asset_group_id': 'asset_group_id',
        'workspace_id': 'workspace_id',
        'asset_type': 'asset_type',
        'sub_asset_type': 'sub_asset_type',
        'asset_desc': 'asset_desc',
        'asset_code': 'asset_code',
        'asset_version': 'asset_version',
        'tags': 'tags',
        'support_actions': 'support_actions',
        'asset_location': 'asset_location',
        'actions': 'actions',
        'status': 'status',
        'dataset_usage': 'dataset_usage',
        'dataset_file_formats': 'dataset_file_formats',
        'dataset_type': 'dataset_type',
        'dataset_sub_type': 'dataset_sub_type',
        'dataset_schema_format': 'dataset_schema_format'
    }

    def __init__(self, asset_id=None, parent_asset_id=None, root_asset_id=None, api_version=None, asset_name=None, asset_group_id=None, workspace_id=None, asset_type=None, sub_asset_type=None, asset_desc=None, asset_code=None, asset_version=None, tags=None, support_actions=None, asset_location=None, actions=None, status=None, dataset_usage=None, dataset_file_formats=None, dataset_type=None, dataset_sub_type=None, dataset_schema_format=None):
        r"""AssetDetail

        The model defined in huaweicloud sdk

        :param asset_id: **参数解释**：资产id。 **取值范围**：不涉及。
        :type asset_id: str
        :param parent_asset_id: **参数解释**：父资产id。 **取值范围**：不涉及。
        :type parent_asset_id: str
        :param root_asset_id: **参数解释**：根资产id。 **取值范围**：不涉及。
        :type root_asset_id: str
        :param api_version: **参数解释**：资产API版本。 **取值范围**：v1,v2。
        :type api_version: str
        :param asset_name: **参数解释**：资产名称。 **取值范围**：不涉及。
        :type asset_name: str
        :param asset_group_id: **参数解释**：需要加入的资产组id。 **取值范围**：0-36位字符，已存在的组id。
        :type asset_group_id: str
        :param workspace_id: **参数解释**：工作空间ID，[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。]未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围**：1-32位字母，数字。
        :type workspace_id: str
        :param asset_type: **参数解释**：资产类型。 **取值范围**：枚举值： - TEMPLATE: 模板资产 - DATASET: 数据集资产 - WORKFLOW: 工作流资产 - IMAGE: 镜像资产 - ALGORITHM：算法资产 - MODEL: 模型资产 - DATASET_TEMPLATE: 数据集模板资产
        :type asset_type: str
        :param sub_asset_type: **参数解释**：资产子类型。 **取值范围**：不涉及。
        :type sub_asset_type: str
        :param asset_desc: **参数解释**：资产描述。 **取值范围**：不涉及。
        :type asset_desc: str
        :param asset_code: **参数解释**：资产code。 **取值范围**：1-60字符，英文字母，数字，中划线，下划线，点。
        :type asset_code: str
        :param asset_version: **参数解释**：资产版本。 **取值范围**：数字或格式为x.y.z，x,y,z为数字。
        :type asset_version: str
        :param tags: **参数解释**：资产tag。 **约束限制**：不涉及。
        :type tags: dict(str, list[str])
        :param support_actions: **参数解释**：资产支持的操作列表，例如监督微调:SFT,LORA微调:LORA,在线部署:ONLINE-DEPLOY,强化学习:AgenticRL。 **约束限制**：不涉及。
        :type support_actions: object
        :param asset_location: **参数解释**：资产文件存储地址,支持OBS（对象存储服务）协议的URL和相对路径。 **取值范围**：0-1024位字符。
        :type asset_location: str
        :param actions: **参数解释**：资产可执行操作详情配置。 **约束限制**：不涉及。
        :type actions: list[:class:`huaweicloudsdkmodelarts.v1.AssetActionRsp`]
        :param status: **参数解释**：资产状态。 **取值范围**：枚举值: - online: 上线 - offline: 下线 - waiting: 等待中
        :type status: str
        :param dataset_usage: **参数解释**：数据集用途。 **取值范围**：1-40位字符。
        :type dataset_usage: str
        :param dataset_file_formats: **参数解释**：数据集存储格式，例如JSONL，TXT，MOBI，EPUB，DOCX，PDF。 **约束限制**：1-40位字符。
        :type dataset_file_formats: list[str]
        :param dataset_type: **参数解释**：数据集模态划分，如音频，图像，视频。 **取值范围**：1-40位字符。
        :type dataset_type: str
        :param dataset_sub_type: **参数解释**：数据集模态细分值，如语义分割。 **取值范围**：1-40位字符。
        :type dataset_sub_type: str
        :param dataset_schema_format: **参数解释**：数据集逻辑规范，如盘古格式。 **取值范围**：1-40位字符。
        :type dataset_schema_format: str
        """
        
        

        self._asset_id = None
        self._parent_asset_id = None
        self._root_asset_id = None
        self._api_version = None
        self._asset_name = None
        self._asset_group_id = None
        self._workspace_id = None
        self._asset_type = None
        self._sub_asset_type = None
        self._asset_desc = None
        self._asset_code = None
        self._asset_version = None
        self._tags = None
        self._support_actions = None
        self._asset_location = None
        self._actions = None
        self._status = None
        self._dataset_usage = None
        self._dataset_file_formats = None
        self._dataset_type = None
        self._dataset_sub_type = None
        self._dataset_schema_format = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if parent_asset_id is not None:
            self.parent_asset_id = parent_asset_id
        if root_asset_id is not None:
            self.root_asset_id = root_asset_id
        if api_version is not None:
            self.api_version = api_version
        self.asset_name = asset_name
        if asset_group_id is not None:
            self.asset_group_id = asset_group_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        self.asset_type = asset_type
        if sub_asset_type is not None:
            self.sub_asset_type = sub_asset_type
        if asset_desc is not None:
            self.asset_desc = asset_desc
        self.asset_code = asset_code
        self.asset_version = asset_version
        if tags is not None:
            self.tags = tags
        if support_actions is not None:
            self.support_actions = support_actions
        if asset_location is not None:
            self.asset_location = asset_location
        if actions is not None:
            self.actions = actions
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

    @property
    def asset_id(self):
        r"""Gets the asset_id of this AssetDetail.

        **参数解释**：资产id。 **取值范围**：不涉及。

        :return: The asset_id of this AssetDetail.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this AssetDetail.

        **参数解释**：资产id。 **取值范围**：不涉及。

        :param asset_id: The asset_id of this AssetDetail.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def parent_asset_id(self):
        r"""Gets the parent_asset_id of this AssetDetail.

        **参数解释**：父资产id。 **取值范围**：不涉及。

        :return: The parent_asset_id of this AssetDetail.
        :rtype: str
        """
        return self._parent_asset_id

    @parent_asset_id.setter
    def parent_asset_id(self, parent_asset_id):
        r"""Sets the parent_asset_id of this AssetDetail.

        **参数解释**：父资产id。 **取值范围**：不涉及。

        :param parent_asset_id: The parent_asset_id of this AssetDetail.
        :type parent_asset_id: str
        """
        self._parent_asset_id = parent_asset_id

    @property
    def root_asset_id(self):
        r"""Gets the root_asset_id of this AssetDetail.

        **参数解释**：根资产id。 **取值范围**：不涉及。

        :return: The root_asset_id of this AssetDetail.
        :rtype: str
        """
        return self._root_asset_id

    @root_asset_id.setter
    def root_asset_id(self, root_asset_id):
        r"""Sets the root_asset_id of this AssetDetail.

        **参数解释**：根资产id。 **取值范围**：不涉及。

        :param root_asset_id: The root_asset_id of this AssetDetail.
        :type root_asset_id: str
        """
        self._root_asset_id = root_asset_id

    @property
    def api_version(self):
        r"""Gets the api_version of this AssetDetail.

        **参数解释**：资产API版本。 **取值范围**：v1,v2。

        :return: The api_version of this AssetDetail.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this AssetDetail.

        **参数解释**：资产API版本。 **取值范围**：v1,v2。

        :param api_version: The api_version of this AssetDetail.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def asset_name(self):
        r"""Gets the asset_name of this AssetDetail.

        **参数解释**：资产名称。 **取值范围**：不涉及。

        :return: The asset_name of this AssetDetail.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this AssetDetail.

        **参数解释**：资产名称。 **取值范围**：不涉及。

        :param asset_name: The asset_name of this AssetDetail.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_group_id(self):
        r"""Gets the asset_group_id of this AssetDetail.

        **参数解释**：需要加入的资产组id。 **取值范围**：0-36位字符，已存在的组id。

        :return: The asset_group_id of this AssetDetail.
        :rtype: str
        """
        return self._asset_group_id

    @asset_group_id.setter
    def asset_group_id(self, asset_group_id):
        r"""Sets the asset_group_id of this AssetDetail.

        **参数解释**：需要加入的资产组id。 **取值范围**：0-36位字符，已存在的组id。

        :param asset_group_id: The asset_group_id of this AssetDetail.
        :type asset_group_id: str
        """
        self._asset_group_id = asset_group_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this AssetDetail.

        **参数解释**：工作空间ID，[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。]未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围**：1-32位字母，数字。

        :return: The workspace_id of this AssetDetail.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this AssetDetail.

        **参数解释**：工作空间ID，[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。]未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围**：1-32位字母，数字。

        :param workspace_id: The workspace_id of this AssetDetail.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def asset_type(self):
        r"""Gets the asset_type of this AssetDetail.

        **参数解释**：资产类型。 **取值范围**：枚举值： - TEMPLATE: 模板资产 - DATASET: 数据集资产 - WORKFLOW: 工作流资产 - IMAGE: 镜像资产 - ALGORITHM：算法资产 - MODEL: 模型资产 - DATASET_TEMPLATE: 数据集模板资产

        :return: The asset_type of this AssetDetail.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this AssetDetail.

        **参数解释**：资产类型。 **取值范围**：枚举值： - TEMPLATE: 模板资产 - DATASET: 数据集资产 - WORKFLOW: 工作流资产 - IMAGE: 镜像资产 - ALGORITHM：算法资产 - MODEL: 模型资产 - DATASET_TEMPLATE: 数据集模板资产

        :param asset_type: The asset_type of this AssetDetail.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def sub_asset_type(self):
        r"""Gets the sub_asset_type of this AssetDetail.

        **参数解释**：资产子类型。 **取值范围**：不涉及。

        :return: The sub_asset_type of this AssetDetail.
        :rtype: str
        """
        return self._sub_asset_type

    @sub_asset_type.setter
    def sub_asset_type(self, sub_asset_type):
        r"""Sets the sub_asset_type of this AssetDetail.

        **参数解释**：资产子类型。 **取值范围**：不涉及。

        :param sub_asset_type: The sub_asset_type of this AssetDetail.
        :type sub_asset_type: str
        """
        self._sub_asset_type = sub_asset_type

    @property
    def asset_desc(self):
        r"""Gets the asset_desc of this AssetDetail.

        **参数解释**：资产描述。 **取值范围**：不涉及。

        :return: The asset_desc of this AssetDetail.
        :rtype: str
        """
        return self._asset_desc

    @asset_desc.setter
    def asset_desc(self, asset_desc):
        r"""Sets the asset_desc of this AssetDetail.

        **参数解释**：资产描述。 **取值范围**：不涉及。

        :param asset_desc: The asset_desc of this AssetDetail.
        :type asset_desc: str
        """
        self._asset_desc = asset_desc

    @property
    def asset_code(self):
        r"""Gets the asset_code of this AssetDetail.

        **参数解释**：资产code。 **取值范围**：1-60字符，英文字母，数字，中划线，下划线，点。

        :return: The asset_code of this AssetDetail.
        :rtype: str
        """
        return self._asset_code

    @asset_code.setter
    def asset_code(self, asset_code):
        r"""Sets the asset_code of this AssetDetail.

        **参数解释**：资产code。 **取值范围**：1-60字符，英文字母，数字，中划线，下划线，点。

        :param asset_code: The asset_code of this AssetDetail.
        :type asset_code: str
        """
        self._asset_code = asset_code

    @property
    def asset_version(self):
        r"""Gets the asset_version of this AssetDetail.

        **参数解释**：资产版本。 **取值范围**：数字或格式为x.y.z，x,y,z为数字。

        :return: The asset_version of this AssetDetail.
        :rtype: str
        """
        return self._asset_version

    @asset_version.setter
    def asset_version(self, asset_version):
        r"""Sets the asset_version of this AssetDetail.

        **参数解释**：资产版本。 **取值范围**：数字或格式为x.y.z，x,y,z为数字。

        :param asset_version: The asset_version of this AssetDetail.
        :type asset_version: str
        """
        self._asset_version = asset_version

    @property
    def tags(self):
        r"""Gets the tags of this AssetDetail.

        **参数解释**：资产tag。 **约束限制**：不涉及。

        :return: The tags of this AssetDetail.
        :rtype: dict(str, list[str])
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this AssetDetail.

        **参数解释**：资产tag。 **约束限制**：不涉及。

        :param tags: The tags of this AssetDetail.
        :type tags: dict(str, list[str])
        """
        self._tags = tags

    @property
    def support_actions(self):
        r"""Gets the support_actions of this AssetDetail.

        **参数解释**：资产支持的操作列表，例如监督微调:SFT,LORA微调:LORA,在线部署:ONLINE-DEPLOY,强化学习:AgenticRL。 **约束限制**：不涉及。

        :return: The support_actions of this AssetDetail.
        :rtype: object
        """
        return self._support_actions

    @support_actions.setter
    def support_actions(self, support_actions):
        r"""Sets the support_actions of this AssetDetail.

        **参数解释**：资产支持的操作列表，例如监督微调:SFT,LORA微调:LORA,在线部署:ONLINE-DEPLOY,强化学习:AgenticRL。 **约束限制**：不涉及。

        :param support_actions: The support_actions of this AssetDetail.
        :type support_actions: object
        """
        self._support_actions = support_actions

    @property
    def asset_location(self):
        r"""Gets the asset_location of this AssetDetail.

        **参数解释**：资产文件存储地址,支持OBS（对象存储服务）协议的URL和相对路径。 **取值范围**：0-1024位字符。

        :return: The asset_location of this AssetDetail.
        :rtype: str
        """
        return self._asset_location

    @asset_location.setter
    def asset_location(self, asset_location):
        r"""Sets the asset_location of this AssetDetail.

        **参数解释**：资产文件存储地址,支持OBS（对象存储服务）协议的URL和相对路径。 **取值范围**：0-1024位字符。

        :param asset_location: The asset_location of this AssetDetail.
        :type asset_location: str
        """
        self._asset_location = asset_location

    @property
    def actions(self):
        r"""Gets the actions of this AssetDetail.

        **参数解释**：资产可执行操作详情配置。 **约束限制**：不涉及。

        :return: The actions of this AssetDetail.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.AssetActionRsp`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this AssetDetail.

        **参数解释**：资产可执行操作详情配置。 **约束限制**：不涉及。

        :param actions: The actions of this AssetDetail.
        :type actions: list[:class:`huaweicloudsdkmodelarts.v1.AssetActionRsp`]
        """
        self._actions = actions

    @property
    def status(self):
        r"""Gets the status of this AssetDetail.

        **参数解释**：资产状态。 **取值范围**：枚举值: - online: 上线 - offline: 下线 - waiting: 等待中

        :return: The status of this AssetDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AssetDetail.

        **参数解释**：资产状态。 **取值范围**：枚举值: - online: 上线 - offline: 下线 - waiting: 等待中

        :param status: The status of this AssetDetail.
        :type status: str
        """
        self._status = status

    @property
    def dataset_usage(self):
        r"""Gets the dataset_usage of this AssetDetail.

        **参数解释**：数据集用途。 **取值范围**：1-40位字符。

        :return: The dataset_usage of this AssetDetail.
        :rtype: str
        """
        return self._dataset_usage

    @dataset_usage.setter
    def dataset_usage(self, dataset_usage):
        r"""Sets the dataset_usage of this AssetDetail.

        **参数解释**：数据集用途。 **取值范围**：1-40位字符。

        :param dataset_usage: The dataset_usage of this AssetDetail.
        :type dataset_usage: str
        """
        self._dataset_usage = dataset_usage

    @property
    def dataset_file_formats(self):
        r"""Gets the dataset_file_formats of this AssetDetail.

        **参数解释**：数据集存储格式，例如JSONL，TXT，MOBI，EPUB，DOCX，PDF。 **约束限制**：1-40位字符。

        :return: The dataset_file_formats of this AssetDetail.
        :rtype: list[str]
        """
        return self._dataset_file_formats

    @dataset_file_formats.setter
    def dataset_file_formats(self, dataset_file_formats):
        r"""Sets the dataset_file_formats of this AssetDetail.

        **参数解释**：数据集存储格式，例如JSONL，TXT，MOBI，EPUB，DOCX，PDF。 **约束限制**：1-40位字符。

        :param dataset_file_formats: The dataset_file_formats of this AssetDetail.
        :type dataset_file_formats: list[str]
        """
        self._dataset_file_formats = dataset_file_formats

    @property
    def dataset_type(self):
        r"""Gets the dataset_type of this AssetDetail.

        **参数解释**：数据集模态划分，如音频，图像，视频。 **取值范围**：1-40位字符。

        :return: The dataset_type of this AssetDetail.
        :rtype: str
        """
        return self._dataset_type

    @dataset_type.setter
    def dataset_type(self, dataset_type):
        r"""Sets the dataset_type of this AssetDetail.

        **参数解释**：数据集模态划分，如音频，图像，视频。 **取值范围**：1-40位字符。

        :param dataset_type: The dataset_type of this AssetDetail.
        :type dataset_type: str
        """
        self._dataset_type = dataset_type

    @property
    def dataset_sub_type(self):
        r"""Gets the dataset_sub_type of this AssetDetail.

        **参数解释**：数据集模态细分值，如语义分割。 **取值范围**：1-40位字符。

        :return: The dataset_sub_type of this AssetDetail.
        :rtype: str
        """
        return self._dataset_sub_type

    @dataset_sub_type.setter
    def dataset_sub_type(self, dataset_sub_type):
        r"""Sets the dataset_sub_type of this AssetDetail.

        **参数解释**：数据集模态细分值，如语义分割。 **取值范围**：1-40位字符。

        :param dataset_sub_type: The dataset_sub_type of this AssetDetail.
        :type dataset_sub_type: str
        """
        self._dataset_sub_type = dataset_sub_type

    @property
    def dataset_schema_format(self):
        r"""Gets the dataset_schema_format of this AssetDetail.

        **参数解释**：数据集逻辑规范，如盘古格式。 **取值范围**：1-40位字符。

        :return: The dataset_schema_format of this AssetDetail.
        :rtype: str
        """
        return self._dataset_schema_format

    @dataset_schema_format.setter
    def dataset_schema_format(self, dataset_schema_format):
        r"""Sets the dataset_schema_format of this AssetDetail.

        **参数解释**：数据集逻辑规范，如盘古格式。 **取值范围**：1-40位字符。

        :param dataset_schema_format: The dataset_schema_format of this AssetDetail.
        :type dataset_schema_format: str
        """
        self._dataset_schema_format = dataset_schema_format

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
        if not isinstance(other, AssetDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
