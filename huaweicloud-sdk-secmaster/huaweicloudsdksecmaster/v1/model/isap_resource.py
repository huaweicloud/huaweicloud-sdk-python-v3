# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IsapResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'create_by': 'str',
        'create_time': 'int',
        'data_classification': 'str',
        'data_layering': 'str',
        'delete_time': 'int',
        'description': 'str',
        'directory': 'str',
        'display_setting': 'IsapResourceDisplaySetting',
        'format': 'str',
        'lock_status': 'str',
        'owner_type': 'str',
        'pipe_id': 'str',
        'process_error': 'str',
        'process_status': 'str',
        'project_id': 'str',
        'rw_type': 'str',
        'schema': 'Schema',
        'storage_setting': 'StorageSetting',
        'store_size_in_bytes': 'int',
        'table_alias': 'str',
        'table_id': 'str',
        'table_name': 'str',
        'update_by': 'str',
        'update_time': 'int',
        'workspace_id': 'str'
    }

    attribute_map = {
        'category': 'category',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'data_classification': 'data_classification',
        'data_layering': 'data_layering',
        'delete_time': 'delete_time',
        'description': 'description',
        'directory': 'directory',
        'display_setting': 'display_setting',
        'format': 'format',
        'lock_status': 'lock_status',
        'owner_type': 'owner_type',
        'pipe_id': 'pipe_id',
        'process_error': 'process_error',
        'process_status': 'process_status',
        'project_id': 'project_id',
        'rw_type': 'rw_type',
        'schema': 'schema',
        'storage_setting': 'storage_setting',
        'store_size_in_bytes': 'store_size_in_bytes',
        'table_alias': 'table_alias',
        'table_id': 'table_id',
        'table_name': 'table_name',
        'update_by': 'update_by',
        'update_time': 'update_time',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, category=None, create_by=None, create_time=None, data_classification=None, data_layering=None, delete_time=None, description=None, directory=None, display_setting=None, format=None, lock_status=None, owner_type=None, pipe_id=None, process_error=None, process_status=None, project_id=None, rw_type=None, schema=None, storage_setting=None, store_size_in_bytes=None, table_alias=None, table_id=None, table_name=None, update_by=None, update_time=None, workspace_id=None):
        r"""IsapResource

        The model defined in huaweicloud sdk

        :param category: 资源类型，例如 STREAMING 或 INDEX
        :type category: str
        :param create_by: 创建者信息
        :type create_by: str
        :param create_time: 创建时间戳
        :type create_time: int
        :param data_classification: 数据分类，例如 FACTUAL_DATA
        :type data_classification: str
        :param data_layering: 数据分层，例如 ODS
        :type data_layering: str
        :param delete_time: 删除时间戳
        :type delete_time: int
        :param description: 描述信息
        :type description: str
        :param directory: 目录路径
        :type directory: str
        :param display_setting: 
        :type display_setting: :class:`huaweicloudsdksecmaster.v1.IsapResourceDisplaySetting`
        :param format: 数据格式，例如 JSON
        :type format: str
        :param lock_status: 锁定状态，例如 UNLOCKED
        :type lock_status: str
        :param owner_type: 所有者类型，例如 USER
        :type owner_type: str
        :param pipe_id: 管道ID
        :type pipe_id: str
        :param process_error: 处理错误状态，例如 NONE
        :type process_error: str
        :param process_status: 处理状态，例如 COMPLETED
        :type process_status: str
        :param project_id: 项目ID
        :type project_id: str
        :param rw_type: 读写类型，例如 READ_WRITE
        :type rw_type: str
        :param schema: 
        :type schema: :class:`huaweicloudsdksecmaster.v1.Schema`
        :param storage_setting: 
        :type storage_setting: :class:`huaweicloudsdksecmaster.v1.StorageSetting`
        :param store_size_in_bytes: 存储大小（字节）
        :type store_size_in_bytes: int
        :param table_alias: 表别名
        :type table_alias: str
        :param table_id: 表ID
        :type table_id: str
        :param table_name: 表名称
        :type table_name: str
        :param update_by: 更新者信息
        :type update_by: str
        :param update_time: 更新时间戳
        :type update_time: int
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        """
        
        

        self._category = None
        self._create_by = None
        self._create_time = None
        self._data_classification = None
        self._data_layering = None
        self._delete_time = None
        self._description = None
        self._directory = None
        self._display_setting = None
        self._format = None
        self._lock_status = None
        self._owner_type = None
        self._pipe_id = None
        self._process_error = None
        self._process_status = None
        self._project_id = None
        self._rw_type = None
        self._schema = None
        self._storage_setting = None
        self._store_size_in_bytes = None
        self._table_alias = None
        self._table_id = None
        self._table_name = None
        self._update_by = None
        self._update_time = None
        self._workspace_id = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if data_classification is not None:
            self.data_classification = data_classification
        if data_layering is not None:
            self.data_layering = data_layering
        if delete_time is not None:
            self.delete_time = delete_time
        if description is not None:
            self.description = description
        if directory is not None:
            self.directory = directory
        if display_setting is not None:
            self.display_setting = display_setting
        if format is not None:
            self.format = format
        if lock_status is not None:
            self.lock_status = lock_status
        if owner_type is not None:
            self.owner_type = owner_type
        if pipe_id is not None:
            self.pipe_id = pipe_id
        if process_error is not None:
            self.process_error = process_error
        if process_status is not None:
            self.process_status = process_status
        if project_id is not None:
            self.project_id = project_id
        if rw_type is not None:
            self.rw_type = rw_type
        if schema is not None:
            self.schema = schema
        if storage_setting is not None:
            self.storage_setting = storage_setting
        if store_size_in_bytes is not None:
            self.store_size_in_bytes = store_size_in_bytes
        if table_alias is not None:
            self.table_alias = table_alias
        if table_id is not None:
            self.table_id = table_id
        if table_name is not None:
            self.table_name = table_name
        if update_by is not None:
            self.update_by = update_by
        if update_time is not None:
            self.update_time = update_time
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def category(self):
        r"""Gets the category of this IsapResource.

        资源类型，例如 STREAMING 或 INDEX

        :return: The category of this IsapResource.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this IsapResource.

        资源类型，例如 STREAMING 或 INDEX

        :param category: The category of this IsapResource.
        :type category: str
        """
        self._category = category

    @property
    def create_by(self):
        r"""Gets the create_by of this IsapResource.

        创建者信息

        :return: The create_by of this IsapResource.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this IsapResource.

        创建者信息

        :param create_by: The create_by of this IsapResource.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        r"""Gets the create_time of this IsapResource.

        创建时间戳

        :return: The create_time of this IsapResource.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this IsapResource.

        创建时间戳

        :param create_time: The create_time of this IsapResource.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def data_classification(self):
        r"""Gets the data_classification of this IsapResource.

        数据分类，例如 FACTUAL_DATA

        :return: The data_classification of this IsapResource.
        :rtype: str
        """
        return self._data_classification

    @data_classification.setter
    def data_classification(self, data_classification):
        r"""Sets the data_classification of this IsapResource.

        数据分类，例如 FACTUAL_DATA

        :param data_classification: The data_classification of this IsapResource.
        :type data_classification: str
        """
        self._data_classification = data_classification

    @property
    def data_layering(self):
        r"""Gets the data_layering of this IsapResource.

        数据分层，例如 ODS

        :return: The data_layering of this IsapResource.
        :rtype: str
        """
        return self._data_layering

    @data_layering.setter
    def data_layering(self, data_layering):
        r"""Sets the data_layering of this IsapResource.

        数据分层，例如 ODS

        :param data_layering: The data_layering of this IsapResource.
        :type data_layering: str
        """
        self._data_layering = data_layering

    @property
    def delete_time(self):
        r"""Gets the delete_time of this IsapResource.

        删除时间戳

        :return: The delete_time of this IsapResource.
        :rtype: int
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        r"""Sets the delete_time of this IsapResource.

        删除时间戳

        :param delete_time: The delete_time of this IsapResource.
        :type delete_time: int
        """
        self._delete_time = delete_time

    @property
    def description(self):
        r"""Gets the description of this IsapResource.

        描述信息

        :return: The description of this IsapResource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IsapResource.

        描述信息

        :param description: The description of this IsapResource.
        :type description: str
        """
        self._description = description

    @property
    def directory(self):
        r"""Gets the directory of this IsapResource.

        目录路径

        :return: The directory of this IsapResource.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this IsapResource.

        目录路径

        :param directory: The directory of this IsapResource.
        :type directory: str
        """
        self._directory = directory

    @property
    def display_setting(self):
        r"""Gets the display_setting of this IsapResource.

        :return: The display_setting of this IsapResource.
        :rtype: :class:`huaweicloudsdksecmaster.v1.IsapResourceDisplaySetting`
        """
        return self._display_setting

    @display_setting.setter
    def display_setting(self, display_setting):
        r"""Sets the display_setting of this IsapResource.

        :param display_setting: The display_setting of this IsapResource.
        :type display_setting: :class:`huaweicloudsdksecmaster.v1.IsapResourceDisplaySetting`
        """
        self._display_setting = display_setting

    @property
    def format(self):
        r"""Gets the format of this IsapResource.

        数据格式，例如 JSON

        :return: The format of this IsapResource.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this IsapResource.

        数据格式，例如 JSON

        :param format: The format of this IsapResource.
        :type format: str
        """
        self._format = format

    @property
    def lock_status(self):
        r"""Gets the lock_status of this IsapResource.

        锁定状态，例如 UNLOCKED

        :return: The lock_status of this IsapResource.
        :rtype: str
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        r"""Sets the lock_status of this IsapResource.

        锁定状态，例如 UNLOCKED

        :param lock_status: The lock_status of this IsapResource.
        :type lock_status: str
        """
        self._lock_status = lock_status

    @property
    def owner_type(self):
        r"""Gets the owner_type of this IsapResource.

        所有者类型，例如 USER

        :return: The owner_type of this IsapResource.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        r"""Sets the owner_type of this IsapResource.

        所有者类型，例如 USER

        :param owner_type: The owner_type of this IsapResource.
        :type owner_type: str
        """
        self._owner_type = owner_type

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this IsapResource.

        管道ID

        :return: The pipe_id of this IsapResource.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this IsapResource.

        管道ID

        :param pipe_id: The pipe_id of this IsapResource.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def process_error(self):
        r"""Gets the process_error of this IsapResource.

        处理错误状态，例如 NONE

        :return: The process_error of this IsapResource.
        :rtype: str
        """
        return self._process_error

    @process_error.setter
    def process_error(self, process_error):
        r"""Sets the process_error of this IsapResource.

        处理错误状态，例如 NONE

        :param process_error: The process_error of this IsapResource.
        :type process_error: str
        """
        self._process_error = process_error

    @property
    def process_status(self):
        r"""Gets the process_status of this IsapResource.

        处理状态，例如 COMPLETED

        :return: The process_status of this IsapResource.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this IsapResource.

        处理状态，例如 COMPLETED

        :param process_status: The process_status of this IsapResource.
        :type process_status: str
        """
        self._process_status = process_status

    @property
    def project_id(self):
        r"""Gets the project_id of this IsapResource.

        项目ID

        :return: The project_id of this IsapResource.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this IsapResource.

        项目ID

        :param project_id: The project_id of this IsapResource.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def rw_type(self):
        r"""Gets the rw_type of this IsapResource.

        读写类型，例如 READ_WRITE

        :return: The rw_type of this IsapResource.
        :rtype: str
        """
        return self._rw_type

    @rw_type.setter
    def rw_type(self, rw_type):
        r"""Sets the rw_type of this IsapResource.

        读写类型，例如 READ_WRITE

        :param rw_type: The rw_type of this IsapResource.
        :type rw_type: str
        """
        self._rw_type = rw_type

    @property
    def schema(self):
        r"""Gets the schema of this IsapResource.

        :return: The schema of this IsapResource.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Schema`
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this IsapResource.

        :param schema: The schema of this IsapResource.
        :type schema: :class:`huaweicloudsdksecmaster.v1.Schema`
        """
        self._schema = schema

    @property
    def storage_setting(self):
        r"""Gets the storage_setting of this IsapResource.

        :return: The storage_setting of this IsapResource.
        :rtype: :class:`huaweicloudsdksecmaster.v1.StorageSetting`
        """
        return self._storage_setting

    @storage_setting.setter
    def storage_setting(self, storage_setting):
        r"""Sets the storage_setting of this IsapResource.

        :param storage_setting: The storage_setting of this IsapResource.
        :type storage_setting: :class:`huaweicloudsdksecmaster.v1.StorageSetting`
        """
        self._storage_setting = storage_setting

    @property
    def store_size_in_bytes(self):
        r"""Gets the store_size_in_bytes of this IsapResource.

        存储大小（字节）

        :return: The store_size_in_bytes of this IsapResource.
        :rtype: int
        """
        return self._store_size_in_bytes

    @store_size_in_bytes.setter
    def store_size_in_bytes(self, store_size_in_bytes):
        r"""Sets the store_size_in_bytes of this IsapResource.

        存储大小（字节）

        :param store_size_in_bytes: The store_size_in_bytes of this IsapResource.
        :type store_size_in_bytes: int
        """
        self._store_size_in_bytes = store_size_in_bytes

    @property
    def table_alias(self):
        r"""Gets the table_alias of this IsapResource.

        表别名

        :return: The table_alias of this IsapResource.
        :rtype: str
        """
        return self._table_alias

    @table_alias.setter
    def table_alias(self, table_alias):
        r"""Sets the table_alias of this IsapResource.

        表别名

        :param table_alias: The table_alias of this IsapResource.
        :type table_alias: str
        """
        self._table_alias = table_alias

    @property
    def table_id(self):
        r"""Gets the table_id of this IsapResource.

        表ID

        :return: The table_id of this IsapResource.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this IsapResource.

        表ID

        :param table_id: The table_id of this IsapResource.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def table_name(self):
        r"""Gets the table_name of this IsapResource.

        表名称

        :return: The table_name of this IsapResource.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this IsapResource.

        表名称

        :param table_name: The table_name of this IsapResource.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def update_by(self):
        r"""Gets the update_by of this IsapResource.

        更新者信息

        :return: The update_by of this IsapResource.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this IsapResource.

        更新者信息

        :param update_by: The update_by of this IsapResource.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        r"""Gets the update_time of this IsapResource.

        更新时间戳

        :return: The update_time of this IsapResource.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this IsapResource.

        更新时间戳

        :param update_time: The update_time of this IsapResource.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this IsapResource.

        工作空间ID

        :return: The workspace_id of this IsapResource.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this IsapResource.

        工作空间ID

        :param workspace_id: The workspace_id of this IsapResource.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, IsapResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
