# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetOperationRecordRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_id': 'str',
        'project_id': 'str',
        'workspace_id': 'str',
        'job_type': 'str',
        'job_id': 'str',
        'job_name': 'str',
        'job_status': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'asset_id': 'str',
        'service': 'str',
        'asset_code': 'str',
        'asset_name': 'str',
        'asset_version': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'is_deleted': 'bool',
        'details': 'str',
        'record_extend_message': 'str'
    }

    attribute_map = {
        'record_id': 'record_id',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'job_type': 'job_type',
        'job_id': 'job_id',
        'job_name': 'job_name',
        'job_status': 'job_status',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'asset_id': 'asset_id',
        'service': 'service',
        'asset_code': 'asset_code',
        'asset_name': 'asset_name',
        'asset_version': 'asset_version',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'is_deleted': 'is_deleted',
        'details': 'details',
        'record_extend_message': 'record_extend_message'
    }

    def __init__(self, record_id=None, project_id=None, workspace_id=None, job_type=None, job_id=None, job_name=None, job_status=None, user_id=None, user_name=None, asset_id=None, service=None, asset_code=None, asset_name=None, asset_version=None, created_at=None, updated_at=None, is_deleted=None, details=None, record_extend_message=None):
        r"""AssetOperationRecordRsp

        The model defined in huaweicloud sdk

        :param record_id: **参数解释**：操作记录ID。 **取值范围**：不涉及。
        :type record_id: str
        :param project_id: **参数解释**：华为云项目ID，获取方法请参见[获取项目ID和名称](modelarts_03_0147.xml)。 **取值范围**：不涉及。
        :type project_id: str
        :param workspace_id: **参数解释**：工作空间ID，[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。]未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围**：不涉及。
        :type workspace_id: str
        :param job_type: **参数解释**：作业类型。 **取值范围**：枚举值: - PRETRAIN: 预训练 - SFT: 全量微调 - RFT: 强化微调 - RLHF: 强化学习 - QUANTIZATION: 量化 - MANUAL-EVALUATION: 人工评测 - AUTO-EVALUATION: 自动评测 - ONLINE-DEPLOY: 在线部署 - EDGE-DEPLOY: 边缘部署 - LORA: LoRA微调 - QLORA: Q-LoRA微调 - DATA-CLEANING: 数据清洗 - DATA-IMPORT: 数据导入 - DATA-ANNOTATION: 数据标注
        :type job_type: str
        :param job_id: **参数解释**：关联任务ID。 **取值范围**：不涉及。
        :type job_id: str
        :param job_name: **参数解释**：关联任务名称。 **取值范围**：不涉及。
        :type job_name: str
        :param job_status: **参数解释**：关联任务状态。 **取值范围**：枚举值: - INIT: 初始化 - RUNNING: 运行中 - STOPPED: 已停止 - FAILED: 失败 - SUCCEED: 成功 - DELETED: 已删除
        :type job_status: str
        :param user_id: **参数解释**：操作用户ID。 **取值范围**：不涉及。
        :type user_id: str
        :param user_name: **参数解释**：操作用户的用户名。 **取值范围**：不涉及。
        :type user_name: str
        :param asset_id: **参数解释**：资产ID。 **取值范围**：不涉及。
        :type asset_id: str
        :param service: **参数解释**：来源服务。 **取值范围**：不涉及。
        :type service: str
        :param asset_code: **参数解释**：资产编码。 **取值范围**：不涉及。
        :type asset_code: str
        :param asset_name: **参数解释**：资产名称，支持英文字母，数字，中划线，下划线，点，空格，中文汉字。 **取值范围**：不涉及。
        :type asset_name: str
        :param asset_version: **参数解释**：资产版本。 **取值范围**：不涉及。
        :type asset_version: str
        :param created_at: **参数解释**：操作记录创建时间。
        :type created_at: datetime
        :param updated_at: **参数解释**：操作记录更新时间。
        :type updated_at: datetime
        :param is_deleted: **参数解释**：任务是否删除（true: 已删除，false: 未删除）。 **取值范围**：不涉及。
        :type is_deleted: bool
        :param details: **参数解释**：服务操作详情。 **取值范围**：不涉及。
        :type details: str
        :param record_extend_message: **参数解释**：预留扩展信息字段。 **取值范围**：不涉及。
        :type record_extend_message: str
        """
        
        

        self._record_id = None
        self._project_id = None
        self._workspace_id = None
        self._job_type = None
        self._job_id = None
        self._job_name = None
        self._job_status = None
        self._user_id = None
        self._user_name = None
        self._asset_id = None
        self._service = None
        self._asset_code = None
        self._asset_name = None
        self._asset_version = None
        self._created_at = None
        self._updated_at = None
        self._is_deleted = None
        self._details = None
        self._record_extend_message = None
        self.discriminator = None

        if record_id is not None:
            self.record_id = record_id
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        self.job_type = job_type
        self.job_id = job_id
        self.job_name = job_name
        self.job_status = job_status
        self.user_id = user_id
        self.user_name = user_name
        self.asset_id = asset_id
        self.service = service
        if asset_code is not None:
            self.asset_code = asset_code
        if asset_name is not None:
            self.asset_name = asset_name
        if asset_version is not None:
            self.asset_version = asset_version
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if details is not None:
            self.details = details
        if record_extend_message is not None:
            self.record_extend_message = record_extend_message

    @property
    def record_id(self):
        r"""Gets the record_id of this AssetOperationRecordRsp.

        **参数解释**：操作记录ID。 **取值范围**：不涉及。

        :return: The record_id of this AssetOperationRecordRsp.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        r"""Sets the record_id of this AssetOperationRecordRsp.

        **参数解释**：操作记录ID。 **取值范围**：不涉及。

        :param record_id: The record_id of this AssetOperationRecordRsp.
        :type record_id: str
        """
        self._record_id = record_id

    @property
    def project_id(self):
        r"""Gets the project_id of this AssetOperationRecordRsp.

        **参数解释**：华为云项目ID，获取方法请参见[获取项目ID和名称](modelarts_03_0147.xml)。 **取值范围**：不涉及。

        :return: The project_id of this AssetOperationRecordRsp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AssetOperationRecordRsp.

        **参数解释**：华为云项目ID，获取方法请参见[获取项目ID和名称](modelarts_03_0147.xml)。 **取值范围**：不涉及。

        :param project_id: The project_id of this AssetOperationRecordRsp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this AssetOperationRecordRsp.

        **参数解释**：工作空间ID，[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。]未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围**：不涉及。

        :return: The workspace_id of this AssetOperationRecordRsp.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this AssetOperationRecordRsp.

        **参数解释**：工作空间ID，[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。]未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围**：不涉及。

        :param workspace_id: The workspace_id of this AssetOperationRecordRsp.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def job_type(self):
        r"""Gets the job_type of this AssetOperationRecordRsp.

        **参数解释**：作业类型。 **取值范围**：枚举值: - PRETRAIN: 预训练 - SFT: 全量微调 - RFT: 强化微调 - RLHF: 强化学习 - QUANTIZATION: 量化 - MANUAL-EVALUATION: 人工评测 - AUTO-EVALUATION: 自动评测 - ONLINE-DEPLOY: 在线部署 - EDGE-DEPLOY: 边缘部署 - LORA: LoRA微调 - QLORA: Q-LoRA微调 - DATA-CLEANING: 数据清洗 - DATA-IMPORT: 数据导入 - DATA-ANNOTATION: 数据标注

        :return: The job_type of this AssetOperationRecordRsp.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this AssetOperationRecordRsp.

        **参数解释**：作业类型。 **取值范围**：枚举值: - PRETRAIN: 预训练 - SFT: 全量微调 - RFT: 强化微调 - RLHF: 强化学习 - QUANTIZATION: 量化 - MANUAL-EVALUATION: 人工评测 - AUTO-EVALUATION: 自动评测 - ONLINE-DEPLOY: 在线部署 - EDGE-DEPLOY: 边缘部署 - LORA: LoRA微调 - QLORA: Q-LoRA微调 - DATA-CLEANING: 数据清洗 - DATA-IMPORT: 数据导入 - DATA-ANNOTATION: 数据标注

        :param job_type: The job_type of this AssetOperationRecordRsp.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def job_id(self):
        r"""Gets the job_id of this AssetOperationRecordRsp.

        **参数解释**：关联任务ID。 **取值范围**：不涉及。

        :return: The job_id of this AssetOperationRecordRsp.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this AssetOperationRecordRsp.

        **参数解释**：关联任务ID。 **取值范围**：不涉及。

        :param job_id: The job_id of this AssetOperationRecordRsp.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this AssetOperationRecordRsp.

        **参数解释**：关联任务名称。 **取值范围**：不涉及。

        :return: The job_name of this AssetOperationRecordRsp.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this AssetOperationRecordRsp.

        **参数解释**：关联任务名称。 **取值范围**：不涉及。

        :param job_name: The job_name of this AssetOperationRecordRsp.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_status(self):
        r"""Gets the job_status of this AssetOperationRecordRsp.

        **参数解释**：关联任务状态。 **取值范围**：枚举值: - INIT: 初始化 - RUNNING: 运行中 - STOPPED: 已停止 - FAILED: 失败 - SUCCEED: 成功 - DELETED: 已删除

        :return: The job_status of this AssetOperationRecordRsp.
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        r"""Sets the job_status of this AssetOperationRecordRsp.

        **参数解释**：关联任务状态。 **取值范围**：枚举值: - INIT: 初始化 - RUNNING: 运行中 - STOPPED: 已停止 - FAILED: 失败 - SUCCEED: 成功 - DELETED: 已删除

        :param job_status: The job_status of this AssetOperationRecordRsp.
        :type job_status: str
        """
        self._job_status = job_status

    @property
    def user_id(self):
        r"""Gets the user_id of this AssetOperationRecordRsp.

        **参数解释**：操作用户ID。 **取值范围**：不涉及。

        :return: The user_id of this AssetOperationRecordRsp.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this AssetOperationRecordRsp.

        **参数解释**：操作用户ID。 **取值范围**：不涉及。

        :param user_id: The user_id of this AssetOperationRecordRsp.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this AssetOperationRecordRsp.

        **参数解释**：操作用户的用户名。 **取值范围**：不涉及。

        :return: The user_name of this AssetOperationRecordRsp.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this AssetOperationRecordRsp.

        **参数解释**：操作用户的用户名。 **取值范围**：不涉及。

        :param user_name: The user_name of this AssetOperationRecordRsp.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def asset_id(self):
        r"""Gets the asset_id of this AssetOperationRecordRsp.

        **参数解释**：资产ID。 **取值范围**：不涉及。

        :return: The asset_id of this AssetOperationRecordRsp.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this AssetOperationRecordRsp.

        **参数解释**：资产ID。 **取值范围**：不涉及。

        :param asset_id: The asset_id of this AssetOperationRecordRsp.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def service(self):
        r"""Gets the service of this AssetOperationRecordRsp.

        **参数解释**：来源服务。 **取值范围**：不涉及。

        :return: The service of this AssetOperationRecordRsp.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this AssetOperationRecordRsp.

        **参数解释**：来源服务。 **取值范围**：不涉及。

        :param service: The service of this AssetOperationRecordRsp.
        :type service: str
        """
        self._service = service

    @property
    def asset_code(self):
        r"""Gets the asset_code of this AssetOperationRecordRsp.

        **参数解释**：资产编码。 **取值范围**：不涉及。

        :return: The asset_code of this AssetOperationRecordRsp.
        :rtype: str
        """
        return self._asset_code

    @asset_code.setter
    def asset_code(self, asset_code):
        r"""Sets the asset_code of this AssetOperationRecordRsp.

        **参数解释**：资产编码。 **取值范围**：不涉及。

        :param asset_code: The asset_code of this AssetOperationRecordRsp.
        :type asset_code: str
        """
        self._asset_code = asset_code

    @property
    def asset_name(self):
        r"""Gets the asset_name of this AssetOperationRecordRsp.

        **参数解释**：资产名称，支持英文字母，数字，中划线，下划线，点，空格，中文汉字。 **取值范围**：不涉及。

        :return: The asset_name of this AssetOperationRecordRsp.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this AssetOperationRecordRsp.

        **参数解释**：资产名称，支持英文字母，数字，中划线，下划线，点，空格，中文汉字。 **取值范围**：不涉及。

        :param asset_name: The asset_name of this AssetOperationRecordRsp.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_version(self):
        r"""Gets the asset_version of this AssetOperationRecordRsp.

        **参数解释**：资产版本。 **取值范围**：不涉及。

        :return: The asset_version of this AssetOperationRecordRsp.
        :rtype: str
        """
        return self._asset_version

    @asset_version.setter
    def asset_version(self, asset_version):
        r"""Sets the asset_version of this AssetOperationRecordRsp.

        **参数解释**：资产版本。 **取值范围**：不涉及。

        :param asset_version: The asset_version of this AssetOperationRecordRsp.
        :type asset_version: str
        """
        self._asset_version = asset_version

    @property
    def created_at(self):
        r"""Gets the created_at of this AssetOperationRecordRsp.

        **参数解释**：操作记录创建时间。

        :return: The created_at of this AssetOperationRecordRsp.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this AssetOperationRecordRsp.

        **参数解释**：操作记录创建时间。

        :param created_at: The created_at of this AssetOperationRecordRsp.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this AssetOperationRecordRsp.

        **参数解释**：操作记录更新时间。

        :return: The updated_at of this AssetOperationRecordRsp.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this AssetOperationRecordRsp.

        **参数解释**：操作记录更新时间。

        :param updated_at: The updated_at of this AssetOperationRecordRsp.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def is_deleted(self):
        r"""Gets the is_deleted of this AssetOperationRecordRsp.

        **参数解释**：任务是否删除（true: 已删除，false: 未删除）。 **取值范围**：不涉及。

        :return: The is_deleted of this AssetOperationRecordRsp.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        r"""Sets the is_deleted of this AssetOperationRecordRsp.

        **参数解释**：任务是否删除（true: 已删除，false: 未删除）。 **取值范围**：不涉及。

        :param is_deleted: The is_deleted of this AssetOperationRecordRsp.
        :type is_deleted: bool
        """
        self._is_deleted = is_deleted

    @property
    def details(self):
        r"""Gets the details of this AssetOperationRecordRsp.

        **参数解释**：服务操作详情。 **取值范围**：不涉及。

        :return: The details of this AssetOperationRecordRsp.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        r"""Sets the details of this AssetOperationRecordRsp.

        **参数解释**：服务操作详情。 **取值范围**：不涉及。

        :param details: The details of this AssetOperationRecordRsp.
        :type details: str
        """
        self._details = details

    @property
    def record_extend_message(self):
        r"""Gets the record_extend_message of this AssetOperationRecordRsp.

        **参数解释**：预留扩展信息字段。 **取值范围**：不涉及。

        :return: The record_extend_message of this AssetOperationRecordRsp.
        :rtype: str
        """
        return self._record_extend_message

    @record_extend_message.setter
    def record_extend_message(self, record_extend_message):
        r"""Sets the record_extend_message of this AssetOperationRecordRsp.

        **参数解释**：预留扩展信息字段。 **取值范围**：不涉及。

        :param record_extend_message: The record_extend_message of this AssetOperationRecordRsp.
        :type record_extend_message: str
        """
        self._record_extend_message = record_extend_message

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
        if not isinstance(other, AssetOperationRecordRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
