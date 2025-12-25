# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTableSchemaResponse(SdkResponse):

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
        'workspace_id': 'str',
        'table_id': 'str',
        'pipe_id': 'str',
        'table_name': 'str',
        'table_alias': 'str',
        'description': 'str',
        'directory': 'str',
        'category': 'str',
        'lock_status': 'str',
        'process_status': 'str',
        'process_error': 'str',
        'format': 'str',
        'rw_type': 'str',
        'owner_type': 'str',
        'data_layering': 'str',
        'data_classification': 'str',
        'schema': 'IsapTableSchema',
        'storage_setting': 'TableStorageSetting',
        'display_setting': 'TableDisplaySetting',
        'create_time': 'int',
        'update_time': 'int',
        'delete_time': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'table_id': 'table_id',
        'pipe_id': 'pipe_id',
        'table_name': 'table_name',
        'table_alias': 'table_alias',
        'description': 'description',
        'directory': 'directory',
        'category': 'category',
        'lock_status': 'lock_status',
        'process_status': 'process_status',
        'process_error': 'process_error',
        'format': 'format',
        'rw_type': 'rw_type',
        'owner_type': 'owner_type',
        'data_layering': 'data_layering',
        'data_classification': 'data_classification',
        'schema': 'schema',
        'storage_setting': 'storage_setting',
        'display_setting': 'display_setting',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'delete_time': 'delete_time'
    }

    def __init__(self, project_id=None, workspace_id=None, table_id=None, pipe_id=None, table_name=None, table_alias=None, description=None, directory=None, category=None, lock_status=None, process_status=None, process_error=None, format=None, rw_type=None, owner_type=None, data_layering=None, data_classification=None, schema=None, storage_setting=None, display_setting=None, create_time=None, update_time=None, delete_time=None):
        r"""UpdateTableSchemaResponse

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param table_id: UUID
        :type table_id: str
        :param pipe_id: UUID
        :type pipe_id: str
        :param table_name: 表名称
        :type table_name: str
        :param table_alias: 表别名
        :type table_alias: str
        :param description: 相关描述
        :type description: str
        :param directory: directory 目录分组
        :type directory: str
        :param category: **参数解释**: 目录类型 - STREAMING 实时流 - INDEX 索引 - APPLICATION 应用 - TENANT_BUCKET 租户桶 - LAKE 数据湖  **约束限制** 不涉及 **取值范围**: - STREAMING - INDEX - APPLICATION - TENANT_BUCKET - LAKE  **默认值** 不涉及     
        :type category: str
        :param lock_status: **参数解释**: 表锁状态 - LOCKED 已锁 - UNLOCKED 未锁  **约束限制** 不涉及 **取值范围**: - LOCKED - UNLOCKED  **默认值** 不涉及      
        :type lock_status: str
        :param process_status: **参数解释**: 处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - DELETING 删除中 - TRUNCATING 清空中 - UPGRADING   升级中       - CREATE_FAILED 创建失败 - UPDATE_FAILED 更新失败 - DELETE_FAILED 删除失败 - TRUNCATE_FAILED 清空失败 - UPGRADE_FAILED 升级失败        **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - DELETING - TRUNCATING - UPGRADING       - CREATE_FAILED - UPDATE_FAILED - DELETE_FAILED - TRUNCATE_FAILED - UPGRADE_FAILED  **默认值** 不涉及    
        :type process_status: str
        :param process_error: **参数解释**: 表处理错误 - NONE 无 - MISSING_ASSOCIATIONS 关联缺失 - FAILED_INIT_STORAGE_RESOURCES_WHEN_CREATING 创建时初始化存储资源失败 - FAILED_INIT_FLINK_RESOURCES_WHEN_CREATING 创建时初始化 Flink 资源失败 - FAILED_DELETE_FLINK_RESOURCES_WHEN_DELETING 删除时删除 Flink 资源失败 - FAILED_DELETE_STORAGE_RESOURCES_WHEN_DELETING 删除时删除存储资源失败 - FAILED_DELETE_ALL_RESOURCES_WHEN_DELETING 删除时删除所有资源失败 - FAILED_UPDATE_STORAGE_SETTING 更新存储配置失败 - FAILED_UPDATE_FLINK_SCHEMA 更新 Flink 模式失败 - FAILED_UPDATE_STORAGE_SCHEMA 更新存储模式失败 - FAILED_TO_APPLY_RESOURCE 应用资源失败 - FAILED_TO_UPGRADE_RESOURCE_MODEL 升级资源模型失败  **约束限制** 不涉及 **取值范围**: - NONE - MISSING_ASSOCIATIONS - FAILED_INIT_STORAGE_RESOURCES_WHEN_CREATING - FAILED_INIT_FLINK_RESOURCES_WHEN_CREATING - FAILED_DELETE_FLINK_RESOURCES_WHEN_DELETING - FAILED_DELETE_STORAGE_RESOURCES_WHEN_DELETING - FAILED_DELETE_ALL_RESOURCES_WHEN_DELETING - FAILED_UPDATE_STORAGE_SETTING - FAILED_UPDATE_FLINK_SCHEMA - FAILED_UPDATE_STORAGE_SCHEMA - FAILED_TO_APPLY_RESOURCE - FAILED_TO_UPGRADE_RESOURCE_MODEL  **默认值** 不涉及 
        :type process_error: str
        :param format: **参数解释**: 表格式 - JSON Json格式 - DEBEZIUM_JSON Debezium JSON 格式 - CSV CSV格式 - PARQUET PARQUET格式 - ORC ORC格式  **约束限制** 不涉及 **取值范围**: - JSON - DEBEZIUM_JSON - CSV - PARQUET - ORC  **默认值** 不涉及  
        :type format: str
        :param rw_type: **参数解释**: 表读写类型 - READ_ONLY 只读 - READ_WRITE 读写 - WRITE_ONLY 只写  **约束限制** 不涉及 **取值范围**: - READ_ONLY - READ_WRITE - WRITE_ONLY  **默认值** 不涉及       
        :type rw_type: str
        :param owner_type: **参数解释**: 拥有者类型 - SYSTEM 系统 - USER 用户 - SYSTEM_ALLOWED_DELETE 系统可删除 - USER_ALLOWED_DELETE 用户可删除  **约束限制** 不涉及 **取值范围**: - SYSTEM - USER - SYSTEM_ALLOWED_DELETE - USER_ALLOWED_DELETE  **默认值** 不涉及         
        :type owner_type: str
        :param data_layering: **参数解释**: 数据分层 - ODS 操作数据存储层 - DWS 数据汇总层 - ADS 应用数据服务层  **约束限制** 不涉及 **取值范围**: - ODS - DWS - ADS  **默认值** 不涉及     
        :type data_layering: str
        :param data_classification: **参数解释**: 数据分类 - FACTUAL_DATA 事实数据 - DIMENSION_DATA 维度数据  **约束限制** 不涉及 **取值范围**: - FACTUAL_DATA - DIMENSION_DATA  **默认值** 不涉及      
        :type data_classification: str
        :param schema: 
        :type schema: :class:`huaweicloudsdksecmaster.v2.IsapTableSchema`
        :param storage_setting: 
        :type storage_setting: :class:`huaweicloudsdksecmaster.v2.TableStorageSetting`
        :param display_setting: 
        :type display_setting: :class:`huaweicloudsdksecmaster.v2.TableDisplaySetting`
        :param create_time: 毫秒时间戳
        :type create_time: int
        :param update_time: 毫秒时间戳
        :type update_time: int
        :param delete_time: 毫秒时间戳
        :type delete_time: int
        """
        
        super().__init__()

        self._project_id = None
        self._workspace_id = None
        self._table_id = None
        self._pipe_id = None
        self._table_name = None
        self._table_alias = None
        self._description = None
        self._directory = None
        self._category = None
        self._lock_status = None
        self._process_status = None
        self._process_error = None
        self._format = None
        self._rw_type = None
        self._owner_type = None
        self._data_layering = None
        self._data_classification = None
        self._schema = None
        self._storage_setting = None
        self._display_setting = None
        self._create_time = None
        self._update_time = None
        self._delete_time = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if table_id is not None:
            self.table_id = table_id
        if pipe_id is not None:
            self.pipe_id = pipe_id
        if table_name is not None:
            self.table_name = table_name
        if table_alias is not None:
            self.table_alias = table_alias
        if description is not None:
            self.description = description
        if directory is not None:
            self.directory = directory
        if category is not None:
            self.category = category
        if lock_status is not None:
            self.lock_status = lock_status
        if process_status is not None:
            self.process_status = process_status
        if process_error is not None:
            self.process_error = process_error
        if format is not None:
            self.format = format
        if rw_type is not None:
            self.rw_type = rw_type
        if owner_type is not None:
            self.owner_type = owner_type
        if data_layering is not None:
            self.data_layering = data_layering
        if data_classification is not None:
            self.data_classification = data_classification
        if schema is not None:
            self.schema = schema
        if storage_setting is not None:
            self.storage_setting = storage_setting
        if display_setting is not None:
            self.display_setting = display_setting
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if delete_time is not None:
            self.delete_time = delete_time

    @property
    def project_id(self):
        r"""Gets the project_id of this UpdateTableSchemaResponse.

        项目ID

        :return: The project_id of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UpdateTableSchemaResponse.

        项目ID

        :param project_id: The project_id of this UpdateTableSchemaResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this UpdateTableSchemaResponse.

        工作空间ID

        :return: The workspace_id of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this UpdateTableSchemaResponse.

        工作空间ID

        :param workspace_id: The workspace_id of this UpdateTableSchemaResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def table_id(self):
        r"""Gets the table_id of this UpdateTableSchemaResponse.

        UUID

        :return: The table_id of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this UpdateTableSchemaResponse.

        UUID

        :param table_id: The table_id of this UpdateTableSchemaResponse.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this UpdateTableSchemaResponse.

        UUID

        :return: The pipe_id of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this UpdateTableSchemaResponse.

        UUID

        :param pipe_id: The pipe_id of this UpdateTableSchemaResponse.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def table_name(self):
        r"""Gets the table_name of this UpdateTableSchemaResponse.

        表名称

        :return: The table_name of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this UpdateTableSchemaResponse.

        表名称

        :param table_name: The table_name of this UpdateTableSchemaResponse.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def table_alias(self):
        r"""Gets the table_alias of this UpdateTableSchemaResponse.

        表别名

        :return: The table_alias of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._table_alias

    @table_alias.setter
    def table_alias(self, table_alias):
        r"""Sets the table_alias of this UpdateTableSchemaResponse.

        表别名

        :param table_alias: The table_alias of this UpdateTableSchemaResponse.
        :type table_alias: str
        """
        self._table_alias = table_alias

    @property
    def description(self):
        r"""Gets the description of this UpdateTableSchemaResponse.

        相关描述

        :return: The description of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateTableSchemaResponse.

        相关描述

        :param description: The description of this UpdateTableSchemaResponse.
        :type description: str
        """
        self._description = description

    @property
    def directory(self):
        r"""Gets the directory of this UpdateTableSchemaResponse.

        directory 目录分组

        :return: The directory of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this UpdateTableSchemaResponse.

        directory 目录分组

        :param directory: The directory of this UpdateTableSchemaResponse.
        :type directory: str
        """
        self._directory = directory

    @property
    def category(self):
        r"""Gets the category of this UpdateTableSchemaResponse.

        **参数解释**: 目录类型 - STREAMING 实时流 - INDEX 索引 - APPLICATION 应用 - TENANT_BUCKET 租户桶 - LAKE 数据湖  **约束限制** 不涉及 **取值范围**: - STREAMING - INDEX - APPLICATION - TENANT_BUCKET - LAKE  **默认值** 不涉及     

        :return: The category of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this UpdateTableSchemaResponse.

        **参数解释**: 目录类型 - STREAMING 实时流 - INDEX 索引 - APPLICATION 应用 - TENANT_BUCKET 租户桶 - LAKE 数据湖  **约束限制** 不涉及 **取值范围**: - STREAMING - INDEX - APPLICATION - TENANT_BUCKET - LAKE  **默认值** 不涉及     

        :param category: The category of this UpdateTableSchemaResponse.
        :type category: str
        """
        self._category = category

    @property
    def lock_status(self):
        r"""Gets the lock_status of this UpdateTableSchemaResponse.

        **参数解释**: 表锁状态 - LOCKED 已锁 - UNLOCKED 未锁  **约束限制** 不涉及 **取值范围**: - LOCKED - UNLOCKED  **默认值** 不涉及      

        :return: The lock_status of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        r"""Sets the lock_status of this UpdateTableSchemaResponse.

        **参数解释**: 表锁状态 - LOCKED 已锁 - UNLOCKED 未锁  **约束限制** 不涉及 **取值范围**: - LOCKED - UNLOCKED  **默认值** 不涉及      

        :param lock_status: The lock_status of this UpdateTableSchemaResponse.
        :type lock_status: str
        """
        self._lock_status = lock_status

    @property
    def process_status(self):
        r"""Gets the process_status of this UpdateTableSchemaResponse.

        **参数解释**: 处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - DELETING 删除中 - TRUNCATING 清空中 - UPGRADING   升级中       - CREATE_FAILED 创建失败 - UPDATE_FAILED 更新失败 - DELETE_FAILED 删除失败 - TRUNCATE_FAILED 清空失败 - UPGRADE_FAILED 升级失败        **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - DELETING - TRUNCATING - UPGRADING       - CREATE_FAILED - UPDATE_FAILED - DELETE_FAILED - TRUNCATE_FAILED - UPGRADE_FAILED  **默认值** 不涉及    

        :return: The process_status of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this UpdateTableSchemaResponse.

        **参数解释**: 处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - DELETING 删除中 - TRUNCATING 清空中 - UPGRADING   升级中       - CREATE_FAILED 创建失败 - UPDATE_FAILED 更新失败 - DELETE_FAILED 删除失败 - TRUNCATE_FAILED 清空失败 - UPGRADE_FAILED 升级失败        **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - DELETING - TRUNCATING - UPGRADING       - CREATE_FAILED - UPDATE_FAILED - DELETE_FAILED - TRUNCATE_FAILED - UPGRADE_FAILED  **默认值** 不涉及    

        :param process_status: The process_status of this UpdateTableSchemaResponse.
        :type process_status: str
        """
        self._process_status = process_status

    @property
    def process_error(self):
        r"""Gets the process_error of this UpdateTableSchemaResponse.

        **参数解释**: 表处理错误 - NONE 无 - MISSING_ASSOCIATIONS 关联缺失 - FAILED_INIT_STORAGE_RESOURCES_WHEN_CREATING 创建时初始化存储资源失败 - FAILED_INIT_FLINK_RESOURCES_WHEN_CREATING 创建时初始化 Flink 资源失败 - FAILED_DELETE_FLINK_RESOURCES_WHEN_DELETING 删除时删除 Flink 资源失败 - FAILED_DELETE_STORAGE_RESOURCES_WHEN_DELETING 删除时删除存储资源失败 - FAILED_DELETE_ALL_RESOURCES_WHEN_DELETING 删除时删除所有资源失败 - FAILED_UPDATE_STORAGE_SETTING 更新存储配置失败 - FAILED_UPDATE_FLINK_SCHEMA 更新 Flink 模式失败 - FAILED_UPDATE_STORAGE_SCHEMA 更新存储模式失败 - FAILED_TO_APPLY_RESOURCE 应用资源失败 - FAILED_TO_UPGRADE_RESOURCE_MODEL 升级资源模型失败  **约束限制** 不涉及 **取值范围**: - NONE - MISSING_ASSOCIATIONS - FAILED_INIT_STORAGE_RESOURCES_WHEN_CREATING - FAILED_INIT_FLINK_RESOURCES_WHEN_CREATING - FAILED_DELETE_FLINK_RESOURCES_WHEN_DELETING - FAILED_DELETE_STORAGE_RESOURCES_WHEN_DELETING - FAILED_DELETE_ALL_RESOURCES_WHEN_DELETING - FAILED_UPDATE_STORAGE_SETTING - FAILED_UPDATE_FLINK_SCHEMA - FAILED_UPDATE_STORAGE_SCHEMA - FAILED_TO_APPLY_RESOURCE - FAILED_TO_UPGRADE_RESOURCE_MODEL  **默认值** 不涉及 

        :return: The process_error of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._process_error

    @process_error.setter
    def process_error(self, process_error):
        r"""Sets the process_error of this UpdateTableSchemaResponse.

        **参数解释**: 表处理错误 - NONE 无 - MISSING_ASSOCIATIONS 关联缺失 - FAILED_INIT_STORAGE_RESOURCES_WHEN_CREATING 创建时初始化存储资源失败 - FAILED_INIT_FLINK_RESOURCES_WHEN_CREATING 创建时初始化 Flink 资源失败 - FAILED_DELETE_FLINK_RESOURCES_WHEN_DELETING 删除时删除 Flink 资源失败 - FAILED_DELETE_STORAGE_RESOURCES_WHEN_DELETING 删除时删除存储资源失败 - FAILED_DELETE_ALL_RESOURCES_WHEN_DELETING 删除时删除所有资源失败 - FAILED_UPDATE_STORAGE_SETTING 更新存储配置失败 - FAILED_UPDATE_FLINK_SCHEMA 更新 Flink 模式失败 - FAILED_UPDATE_STORAGE_SCHEMA 更新存储模式失败 - FAILED_TO_APPLY_RESOURCE 应用资源失败 - FAILED_TO_UPGRADE_RESOURCE_MODEL 升级资源模型失败  **约束限制** 不涉及 **取值范围**: - NONE - MISSING_ASSOCIATIONS - FAILED_INIT_STORAGE_RESOURCES_WHEN_CREATING - FAILED_INIT_FLINK_RESOURCES_WHEN_CREATING - FAILED_DELETE_FLINK_RESOURCES_WHEN_DELETING - FAILED_DELETE_STORAGE_RESOURCES_WHEN_DELETING - FAILED_DELETE_ALL_RESOURCES_WHEN_DELETING - FAILED_UPDATE_STORAGE_SETTING - FAILED_UPDATE_FLINK_SCHEMA - FAILED_UPDATE_STORAGE_SCHEMA - FAILED_TO_APPLY_RESOURCE - FAILED_TO_UPGRADE_RESOURCE_MODEL  **默认值** 不涉及 

        :param process_error: The process_error of this UpdateTableSchemaResponse.
        :type process_error: str
        """
        self._process_error = process_error

    @property
    def format(self):
        r"""Gets the format of this UpdateTableSchemaResponse.

        **参数解释**: 表格式 - JSON Json格式 - DEBEZIUM_JSON Debezium JSON 格式 - CSV CSV格式 - PARQUET PARQUET格式 - ORC ORC格式  **约束限制** 不涉及 **取值范围**: - JSON - DEBEZIUM_JSON - CSV - PARQUET - ORC  **默认值** 不涉及  

        :return: The format of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this UpdateTableSchemaResponse.

        **参数解释**: 表格式 - JSON Json格式 - DEBEZIUM_JSON Debezium JSON 格式 - CSV CSV格式 - PARQUET PARQUET格式 - ORC ORC格式  **约束限制** 不涉及 **取值范围**: - JSON - DEBEZIUM_JSON - CSV - PARQUET - ORC  **默认值** 不涉及  

        :param format: The format of this UpdateTableSchemaResponse.
        :type format: str
        """
        self._format = format

    @property
    def rw_type(self):
        r"""Gets the rw_type of this UpdateTableSchemaResponse.

        **参数解释**: 表读写类型 - READ_ONLY 只读 - READ_WRITE 读写 - WRITE_ONLY 只写  **约束限制** 不涉及 **取值范围**: - READ_ONLY - READ_WRITE - WRITE_ONLY  **默认值** 不涉及       

        :return: The rw_type of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._rw_type

    @rw_type.setter
    def rw_type(self, rw_type):
        r"""Sets the rw_type of this UpdateTableSchemaResponse.

        **参数解释**: 表读写类型 - READ_ONLY 只读 - READ_WRITE 读写 - WRITE_ONLY 只写  **约束限制** 不涉及 **取值范围**: - READ_ONLY - READ_WRITE - WRITE_ONLY  **默认值** 不涉及       

        :param rw_type: The rw_type of this UpdateTableSchemaResponse.
        :type rw_type: str
        """
        self._rw_type = rw_type

    @property
    def owner_type(self):
        r"""Gets the owner_type of this UpdateTableSchemaResponse.

        **参数解释**: 拥有者类型 - SYSTEM 系统 - USER 用户 - SYSTEM_ALLOWED_DELETE 系统可删除 - USER_ALLOWED_DELETE 用户可删除  **约束限制** 不涉及 **取值范围**: - SYSTEM - USER - SYSTEM_ALLOWED_DELETE - USER_ALLOWED_DELETE  **默认值** 不涉及         

        :return: The owner_type of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        r"""Sets the owner_type of this UpdateTableSchemaResponse.

        **参数解释**: 拥有者类型 - SYSTEM 系统 - USER 用户 - SYSTEM_ALLOWED_DELETE 系统可删除 - USER_ALLOWED_DELETE 用户可删除  **约束限制** 不涉及 **取值范围**: - SYSTEM - USER - SYSTEM_ALLOWED_DELETE - USER_ALLOWED_DELETE  **默认值** 不涉及         

        :param owner_type: The owner_type of this UpdateTableSchemaResponse.
        :type owner_type: str
        """
        self._owner_type = owner_type

    @property
    def data_layering(self):
        r"""Gets the data_layering of this UpdateTableSchemaResponse.

        **参数解释**: 数据分层 - ODS 操作数据存储层 - DWS 数据汇总层 - ADS 应用数据服务层  **约束限制** 不涉及 **取值范围**: - ODS - DWS - ADS  **默认值** 不涉及     

        :return: The data_layering of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._data_layering

    @data_layering.setter
    def data_layering(self, data_layering):
        r"""Sets the data_layering of this UpdateTableSchemaResponse.

        **参数解释**: 数据分层 - ODS 操作数据存储层 - DWS 数据汇总层 - ADS 应用数据服务层  **约束限制** 不涉及 **取值范围**: - ODS - DWS - ADS  **默认值** 不涉及     

        :param data_layering: The data_layering of this UpdateTableSchemaResponse.
        :type data_layering: str
        """
        self._data_layering = data_layering

    @property
    def data_classification(self):
        r"""Gets the data_classification of this UpdateTableSchemaResponse.

        **参数解释**: 数据分类 - FACTUAL_DATA 事实数据 - DIMENSION_DATA 维度数据  **约束限制** 不涉及 **取值范围**: - FACTUAL_DATA - DIMENSION_DATA  **默认值** 不涉及      

        :return: The data_classification of this UpdateTableSchemaResponse.
        :rtype: str
        """
        return self._data_classification

    @data_classification.setter
    def data_classification(self, data_classification):
        r"""Sets the data_classification of this UpdateTableSchemaResponse.

        **参数解释**: 数据分类 - FACTUAL_DATA 事实数据 - DIMENSION_DATA 维度数据  **约束限制** 不涉及 **取值范围**: - FACTUAL_DATA - DIMENSION_DATA  **默认值** 不涉及      

        :param data_classification: The data_classification of this UpdateTableSchemaResponse.
        :type data_classification: str
        """
        self._data_classification = data_classification

    @property
    def schema(self):
        r"""Gets the schema of this UpdateTableSchemaResponse.

        :return: The schema of this UpdateTableSchemaResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IsapTableSchema`
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this UpdateTableSchemaResponse.

        :param schema: The schema of this UpdateTableSchemaResponse.
        :type schema: :class:`huaweicloudsdksecmaster.v2.IsapTableSchema`
        """
        self._schema = schema

    @property
    def storage_setting(self):
        r"""Gets the storage_setting of this UpdateTableSchemaResponse.

        :return: The storage_setting of this UpdateTableSchemaResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.TableStorageSetting`
        """
        return self._storage_setting

    @storage_setting.setter
    def storage_setting(self, storage_setting):
        r"""Sets the storage_setting of this UpdateTableSchemaResponse.

        :param storage_setting: The storage_setting of this UpdateTableSchemaResponse.
        :type storage_setting: :class:`huaweicloudsdksecmaster.v2.TableStorageSetting`
        """
        self._storage_setting = storage_setting

    @property
    def display_setting(self):
        r"""Gets the display_setting of this UpdateTableSchemaResponse.

        :return: The display_setting of this UpdateTableSchemaResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.TableDisplaySetting`
        """
        return self._display_setting

    @display_setting.setter
    def display_setting(self, display_setting):
        r"""Sets the display_setting of this UpdateTableSchemaResponse.

        :param display_setting: The display_setting of this UpdateTableSchemaResponse.
        :type display_setting: :class:`huaweicloudsdksecmaster.v2.TableDisplaySetting`
        """
        self._display_setting = display_setting

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateTableSchemaResponse.

        毫秒时间戳

        :return: The create_time of this UpdateTableSchemaResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateTableSchemaResponse.

        毫秒时间戳

        :param create_time: The create_time of this UpdateTableSchemaResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateTableSchemaResponse.

        毫秒时间戳

        :return: The update_time of this UpdateTableSchemaResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateTableSchemaResponse.

        毫秒时间戳

        :param update_time: The update_time of this UpdateTableSchemaResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def delete_time(self):
        r"""Gets the delete_time of this UpdateTableSchemaResponse.

        毫秒时间戳

        :return: The delete_time of this UpdateTableSchemaResponse.
        :rtype: int
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        r"""Sets the delete_time of this UpdateTableSchemaResponse.

        毫秒时间戳

        :param delete_time: The delete_time of this UpdateTableSchemaResponse.
        :type delete_time: int
        """
        self._delete_time = delete_time

    def to_dict(self):
        import warnings
        warnings.warn("UpdateTableSchemaResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateTableSchemaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
