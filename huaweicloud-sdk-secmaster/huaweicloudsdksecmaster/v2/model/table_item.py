# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableItem:

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
        'table_name': 'str',
        'table_alias': 'str',
        'directory': 'str',
        'description': 'str',
        'category': 'str',
        'lock_status': 'str',
        'process_status': 'str',
        'process_error': 'str',
        'edit_type': 'str',
        'format': 'str',
        'rw_type': 'str',
        'owner_type': 'str',
        'data_layering': 'str',
        'data_classification': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'delete_time': 'int',
        'store_size_in_bytes': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'table_id': 'table_id',
        'table_name': 'table_name',
        'table_alias': 'table_alias',
        'directory': 'directory',
        'description': 'description',
        'category': 'category',
        'lock_status': 'lock_status',
        'process_status': 'process_status',
        'process_error': 'process_error',
        'edit_type': 'edit_type',
        'format': 'format',
        'rw_type': 'rw_type',
        'owner_type': 'owner_type',
        'data_layering': 'data_layering',
        'data_classification': 'data_classification',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'delete_time': 'delete_time',
        'store_size_in_bytes': 'store_size_in_bytes'
    }

    def __init__(self, project_id=None, workspace_id=None, table_id=None, table_name=None, table_alias=None, directory=None, description=None, category=None, lock_status=None, process_status=None, process_error=None, edit_type=None, format=None, rw_type=None, owner_type=None, data_layering=None, data_classification=None, create_time=None, update_time=None, delete_time=None, store_size_in_bytes=None):
        r"""TableItem

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param table_id: UUID
        :type table_id: str
        :param table_name: Table name 表名
        :type table_name: str
        :param table_alias: 表别名
        :type table_alias: str
        :param directory: directory 目录分组
        :type directory: str
        :param description: 表描述
        :type description: str
        :param category: **参数解释**: 表类别 - STREAMING 流式传输 - INDEX 索引 - APPLICATION 应用 - TENANT_OBS 租户对象存储 - LAKE 数据湖  **约束限制** 不涉及 **取值范围**: - STREAMING - INDEX - APPLICATION - TENANT_OBS - LAKE  **默认值** 不涉及      
        :type category: str
        :param lock_status: **参数解释**: 表锁状态 - LOCKED 已锁 - UNLOCKED 未锁  **约束限制** 不涉及 **取值范围**: - LOCKED - UNLOCKED  **默认值** 不涉及      
        :type lock_status: str
        :param process_status: **参数解释**: 表处理状态 - COMPLETED 处理完成 - CREATING 创建中 - UPDATING 更新中 - DELETING 删除中 - TRUNCATING 清空中 - CREATE_FAILED 创建失败 - UPDATING_FAILED 更新失败 - DELETING_FAILED 删除失败 - TRUNCATE_FAILED 清空失败  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - DELETING - TRUNCATING - CREATE_FAILED - UPDATING_FAILED - DELETING_FAILED - TRUNCATE_FAILED  **默认值** 不涉及        
        :type process_status: str
        :param process_error: **参数解释**: 表处理错误 - NONE 无  **约束限制** 不涉及 **取值范围**: - NONE  **默认值** 不涉及  
        :type process_error: str
        :param edit_type: **参数解释**: 表编辑类型 - MODIFIABLE 可任意修改态 - APPENDED 追加态 (原来的内容锁定，只可追加) - LOCKED 锁定态 (完全锁定，不可修改)  **约束限制** 不涉及 **取值范围**: - MODIFIABLE - APPENDED - LOCKED  **默认值** 不涉及      
        :type edit_type: str
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
        :param create_time: 毫秒时间戳
        :type create_time: int
        :param update_time: 毫秒时间戳
        :type update_time: int
        :param delete_time: 毫秒时间戳
        :type delete_time: int
        :param store_size_in_bytes: 已使用存储容量
        :type store_size_in_bytes: int
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._table_id = None
        self._table_name = None
        self._table_alias = None
        self._directory = None
        self._description = None
        self._category = None
        self._lock_status = None
        self._process_status = None
        self._process_error = None
        self._edit_type = None
        self._format = None
        self._rw_type = None
        self._owner_type = None
        self._data_layering = None
        self._data_classification = None
        self._create_time = None
        self._update_time = None
        self._delete_time = None
        self._store_size_in_bytes = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if table_id is not None:
            self.table_id = table_id
        if table_name is not None:
            self.table_name = table_name
        if table_alias is not None:
            self.table_alias = table_alias
        if directory is not None:
            self.directory = directory
        if description is not None:
            self.description = description
        if category is not None:
            self.category = category
        if lock_status is not None:
            self.lock_status = lock_status
        if process_status is not None:
            self.process_status = process_status
        if process_error is not None:
            self.process_error = process_error
        if edit_type is not None:
            self.edit_type = edit_type
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
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if delete_time is not None:
            self.delete_time = delete_time
        if store_size_in_bytes is not None:
            self.store_size_in_bytes = store_size_in_bytes

    @property
    def project_id(self):
        r"""Gets the project_id of this TableItem.

        项目ID

        :return: The project_id of this TableItem.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TableItem.

        项目ID

        :param project_id: The project_id of this TableItem.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this TableItem.

        工作空间ID

        :return: The workspace_id of this TableItem.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this TableItem.

        工作空间ID

        :param workspace_id: The workspace_id of this TableItem.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def table_id(self):
        r"""Gets the table_id of this TableItem.

        UUID

        :return: The table_id of this TableItem.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this TableItem.

        UUID

        :param table_id: The table_id of this TableItem.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def table_name(self):
        r"""Gets the table_name of this TableItem.

        Table name 表名

        :return: The table_name of this TableItem.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this TableItem.

        Table name 表名

        :param table_name: The table_name of this TableItem.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def table_alias(self):
        r"""Gets the table_alias of this TableItem.

        表别名

        :return: The table_alias of this TableItem.
        :rtype: str
        """
        return self._table_alias

    @table_alias.setter
    def table_alias(self, table_alias):
        r"""Sets the table_alias of this TableItem.

        表别名

        :param table_alias: The table_alias of this TableItem.
        :type table_alias: str
        """
        self._table_alias = table_alias

    @property
    def directory(self):
        r"""Gets the directory of this TableItem.

        directory 目录分组

        :return: The directory of this TableItem.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this TableItem.

        directory 目录分组

        :param directory: The directory of this TableItem.
        :type directory: str
        """
        self._directory = directory

    @property
    def description(self):
        r"""Gets the description of this TableItem.

        表描述

        :return: The description of this TableItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TableItem.

        表描述

        :param description: The description of this TableItem.
        :type description: str
        """
        self._description = description

    @property
    def category(self):
        r"""Gets the category of this TableItem.

        **参数解释**: 表类别 - STREAMING 流式传输 - INDEX 索引 - APPLICATION 应用 - TENANT_OBS 租户对象存储 - LAKE 数据湖  **约束限制** 不涉及 **取值范围**: - STREAMING - INDEX - APPLICATION - TENANT_OBS - LAKE  **默认值** 不涉及      

        :return: The category of this TableItem.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this TableItem.

        **参数解释**: 表类别 - STREAMING 流式传输 - INDEX 索引 - APPLICATION 应用 - TENANT_OBS 租户对象存储 - LAKE 数据湖  **约束限制** 不涉及 **取值范围**: - STREAMING - INDEX - APPLICATION - TENANT_OBS - LAKE  **默认值** 不涉及      

        :param category: The category of this TableItem.
        :type category: str
        """
        self._category = category

    @property
    def lock_status(self):
        r"""Gets the lock_status of this TableItem.

        **参数解释**: 表锁状态 - LOCKED 已锁 - UNLOCKED 未锁  **约束限制** 不涉及 **取值范围**: - LOCKED - UNLOCKED  **默认值** 不涉及      

        :return: The lock_status of this TableItem.
        :rtype: str
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        r"""Sets the lock_status of this TableItem.

        **参数解释**: 表锁状态 - LOCKED 已锁 - UNLOCKED 未锁  **约束限制** 不涉及 **取值范围**: - LOCKED - UNLOCKED  **默认值** 不涉及      

        :param lock_status: The lock_status of this TableItem.
        :type lock_status: str
        """
        self._lock_status = lock_status

    @property
    def process_status(self):
        r"""Gets the process_status of this TableItem.

        **参数解释**: 表处理状态 - COMPLETED 处理完成 - CREATING 创建中 - UPDATING 更新中 - DELETING 删除中 - TRUNCATING 清空中 - CREATE_FAILED 创建失败 - UPDATING_FAILED 更新失败 - DELETING_FAILED 删除失败 - TRUNCATE_FAILED 清空失败  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - DELETING - TRUNCATING - CREATE_FAILED - UPDATING_FAILED - DELETING_FAILED - TRUNCATE_FAILED  **默认值** 不涉及        

        :return: The process_status of this TableItem.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this TableItem.

        **参数解释**: 表处理状态 - COMPLETED 处理完成 - CREATING 创建中 - UPDATING 更新中 - DELETING 删除中 - TRUNCATING 清空中 - CREATE_FAILED 创建失败 - UPDATING_FAILED 更新失败 - DELETING_FAILED 删除失败 - TRUNCATE_FAILED 清空失败  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - DELETING - TRUNCATING - CREATE_FAILED - UPDATING_FAILED - DELETING_FAILED - TRUNCATE_FAILED  **默认值** 不涉及        

        :param process_status: The process_status of this TableItem.
        :type process_status: str
        """
        self._process_status = process_status

    @property
    def process_error(self):
        r"""Gets the process_error of this TableItem.

        **参数解释**: 表处理错误 - NONE 无  **约束限制** 不涉及 **取值范围**: - NONE  **默认值** 不涉及  

        :return: The process_error of this TableItem.
        :rtype: str
        """
        return self._process_error

    @process_error.setter
    def process_error(self, process_error):
        r"""Sets the process_error of this TableItem.

        **参数解释**: 表处理错误 - NONE 无  **约束限制** 不涉及 **取值范围**: - NONE  **默认值** 不涉及  

        :param process_error: The process_error of this TableItem.
        :type process_error: str
        """
        self._process_error = process_error

    @property
    def edit_type(self):
        r"""Gets the edit_type of this TableItem.

        **参数解释**: 表编辑类型 - MODIFIABLE 可任意修改态 - APPENDED 追加态 (原来的内容锁定，只可追加) - LOCKED 锁定态 (完全锁定，不可修改)  **约束限制** 不涉及 **取值范围**: - MODIFIABLE - APPENDED - LOCKED  **默认值** 不涉及      

        :return: The edit_type of this TableItem.
        :rtype: str
        """
        return self._edit_type

    @edit_type.setter
    def edit_type(self, edit_type):
        r"""Sets the edit_type of this TableItem.

        **参数解释**: 表编辑类型 - MODIFIABLE 可任意修改态 - APPENDED 追加态 (原来的内容锁定，只可追加) - LOCKED 锁定态 (完全锁定，不可修改)  **约束限制** 不涉及 **取值范围**: - MODIFIABLE - APPENDED - LOCKED  **默认值** 不涉及      

        :param edit_type: The edit_type of this TableItem.
        :type edit_type: str
        """
        self._edit_type = edit_type

    @property
    def format(self):
        r"""Gets the format of this TableItem.

        **参数解释**: 表格式 - JSON Json格式 - DEBEZIUM_JSON Debezium JSON 格式 - CSV CSV格式 - PARQUET PARQUET格式 - ORC ORC格式  **约束限制** 不涉及 **取值范围**: - JSON - DEBEZIUM_JSON - CSV - PARQUET - ORC  **默认值** 不涉及  

        :return: The format of this TableItem.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this TableItem.

        **参数解释**: 表格式 - JSON Json格式 - DEBEZIUM_JSON Debezium JSON 格式 - CSV CSV格式 - PARQUET PARQUET格式 - ORC ORC格式  **约束限制** 不涉及 **取值范围**: - JSON - DEBEZIUM_JSON - CSV - PARQUET - ORC  **默认值** 不涉及  

        :param format: The format of this TableItem.
        :type format: str
        """
        self._format = format

    @property
    def rw_type(self):
        r"""Gets the rw_type of this TableItem.

        **参数解释**: 表读写类型 - READ_ONLY 只读 - READ_WRITE 读写 - WRITE_ONLY 只写  **约束限制** 不涉及 **取值范围**: - READ_ONLY - READ_WRITE - WRITE_ONLY  **默认值** 不涉及       

        :return: The rw_type of this TableItem.
        :rtype: str
        """
        return self._rw_type

    @rw_type.setter
    def rw_type(self, rw_type):
        r"""Sets the rw_type of this TableItem.

        **参数解释**: 表读写类型 - READ_ONLY 只读 - READ_WRITE 读写 - WRITE_ONLY 只写  **约束限制** 不涉及 **取值范围**: - READ_ONLY - READ_WRITE - WRITE_ONLY  **默认值** 不涉及       

        :param rw_type: The rw_type of this TableItem.
        :type rw_type: str
        """
        self._rw_type = rw_type

    @property
    def owner_type(self):
        r"""Gets the owner_type of this TableItem.

        **参数解释**: 拥有者类型 - SYSTEM 系统 - USER 用户 - SYSTEM_ALLOWED_DELETE 系统可删除 - USER_ALLOWED_DELETE 用户可删除  **约束限制** 不涉及 **取值范围**: - SYSTEM - USER - SYSTEM_ALLOWED_DELETE - USER_ALLOWED_DELETE  **默认值** 不涉及         

        :return: The owner_type of this TableItem.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        r"""Sets the owner_type of this TableItem.

        **参数解释**: 拥有者类型 - SYSTEM 系统 - USER 用户 - SYSTEM_ALLOWED_DELETE 系统可删除 - USER_ALLOWED_DELETE 用户可删除  **约束限制** 不涉及 **取值范围**: - SYSTEM - USER - SYSTEM_ALLOWED_DELETE - USER_ALLOWED_DELETE  **默认值** 不涉及         

        :param owner_type: The owner_type of this TableItem.
        :type owner_type: str
        """
        self._owner_type = owner_type

    @property
    def data_layering(self):
        r"""Gets the data_layering of this TableItem.

        **参数解释**: 数据分层 - ODS 操作数据存储层 - DWS 数据汇总层 - ADS 应用数据服务层  **约束限制** 不涉及 **取值范围**: - ODS - DWS - ADS  **默认值** 不涉及     

        :return: The data_layering of this TableItem.
        :rtype: str
        """
        return self._data_layering

    @data_layering.setter
    def data_layering(self, data_layering):
        r"""Sets the data_layering of this TableItem.

        **参数解释**: 数据分层 - ODS 操作数据存储层 - DWS 数据汇总层 - ADS 应用数据服务层  **约束限制** 不涉及 **取值范围**: - ODS - DWS - ADS  **默认值** 不涉及     

        :param data_layering: The data_layering of this TableItem.
        :type data_layering: str
        """
        self._data_layering = data_layering

    @property
    def data_classification(self):
        r"""Gets the data_classification of this TableItem.

        **参数解释**: 数据分类 - FACTUAL_DATA 事实数据 - DIMENSION_DATA 维度数据  **约束限制** 不涉及 **取值范围**: - FACTUAL_DATA - DIMENSION_DATA  **默认值** 不涉及      

        :return: The data_classification of this TableItem.
        :rtype: str
        """
        return self._data_classification

    @data_classification.setter
    def data_classification(self, data_classification):
        r"""Sets the data_classification of this TableItem.

        **参数解释**: 数据分类 - FACTUAL_DATA 事实数据 - DIMENSION_DATA 维度数据  **约束限制** 不涉及 **取值范围**: - FACTUAL_DATA - DIMENSION_DATA  **默认值** 不涉及      

        :param data_classification: The data_classification of this TableItem.
        :type data_classification: str
        """
        self._data_classification = data_classification

    @property
    def create_time(self):
        r"""Gets the create_time of this TableItem.

        毫秒时间戳

        :return: The create_time of this TableItem.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TableItem.

        毫秒时间戳

        :param create_time: The create_time of this TableItem.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this TableItem.

        毫秒时间戳

        :return: The update_time of this TableItem.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TableItem.

        毫秒时间戳

        :param update_time: The update_time of this TableItem.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def delete_time(self):
        r"""Gets the delete_time of this TableItem.

        毫秒时间戳

        :return: The delete_time of this TableItem.
        :rtype: int
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        r"""Sets the delete_time of this TableItem.

        毫秒时间戳

        :param delete_time: The delete_time of this TableItem.
        :type delete_time: int
        """
        self._delete_time = delete_time

    @property
    def store_size_in_bytes(self):
        r"""Gets the store_size_in_bytes of this TableItem.

        已使用存储容量

        :return: The store_size_in_bytes of this TableItem.
        :rtype: int
        """
        return self._store_size_in_bytes

    @store_size_in_bytes.setter
    def store_size_in_bytes(self, store_size_in_bytes):
        r"""Sets the store_size_in_bytes of this TableItem.

        已使用存储容量

        :param store_size_in_bytes: The store_size_in_bytes of this TableItem.
        :type store_size_in_bytes: int
        """
        self._store_size_in_bytes = store_size_in_bytes

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
        if not isinstance(other, TableItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
