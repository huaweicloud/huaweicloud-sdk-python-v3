# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPipeResponse(SdkResponse):

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
        'delete_time': 'int',
        'description': 'str',
        'directory': 'str',
        'owner_type': 'str',
        'pipe_alias': 'str',
        'pipe_id': 'str',
        'pipe_name': 'str',
        'process_error': 'str',
        'process_status': 'str',
        'project_id': 'str',
        'resources': 'list[IsapResource]',
        'schema': 'Schema',
        'storage_setting': 'StorageSetting',
        'update_by': 'str',
        'update_time': 'int',
        'workspace_id': 'str'
    }

    attribute_map = {
        'category': 'category',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'delete_time': 'delete_time',
        'description': 'description',
        'directory': 'directory',
        'owner_type': 'owner_type',
        'pipe_alias': 'pipe_alias',
        'pipe_id': 'pipe_id',
        'pipe_name': 'pipe_name',
        'process_error': 'process_error',
        'process_status': 'process_status',
        'project_id': 'project_id',
        'resources': 'resources',
        'schema': 'schema',
        'storage_setting': 'storage_setting',
        'update_by': 'update_by',
        'update_time': 'update_time',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, category=None, create_by=None, create_time=None, delete_time=None, description=None, directory=None, owner_type=None, pipe_alias=None, pipe_id=None, pipe_name=None, process_error=None, process_status=None, project_id=None, resources=None, schema=None, storage_setting=None, update_by=None, update_time=None, workspace_id=None):
        r"""ShowPipeResponse

        The model defined in huaweicloud sdk

        :param category: 资源类型，例如 STREAMING_TO_INDEX
        :type category: str
        :param create_by: 创建者信息
        :type create_by: str
        :param create_time: 创建时间戳
        :type create_time: int
        :param delete_time: 删除时间戳
        :type delete_time: int
        :param description: 描述信息
        :type description: str
        :param directory: 目录路径
        :type directory: str
        :param owner_type: 所有者类型，例如 USER
        :type owner_type: str
        :param pipe_alias: 管道别名
        :type pipe_alias: str
        :param pipe_id: 管道ID
        :type pipe_id: str
        :param pipe_name: 管道名称
        :type pipe_name: str
        :param process_error: 处理错误状态，例如 NONE
        :type process_error: str
        :param process_status: 处理状态，例如 COMPLETED
        :type process_status: str
        :param project_id: 项目ID
        :type project_id: str
        :param resources: 资源列表
        :type resources: list[:class:`huaweicloudsdksecmaster.v1.IsapResource`]
        :param schema: 
        :type schema: :class:`huaweicloudsdksecmaster.v1.Schema`
        :param storage_setting: 
        :type storage_setting: :class:`huaweicloudsdksecmaster.v1.StorageSetting`
        :param update_by: 更新者信息
        :type update_by: str
        :param update_time: 更新时间戳
        :type update_time: int
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        """
        
        super().__init__()

        self._category = None
        self._create_by = None
        self._create_time = None
        self._delete_time = None
        self._description = None
        self._directory = None
        self._owner_type = None
        self._pipe_alias = None
        self._pipe_id = None
        self._pipe_name = None
        self._process_error = None
        self._process_status = None
        self._project_id = None
        self._resources = None
        self._schema = None
        self._storage_setting = None
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
        if delete_time is not None:
            self.delete_time = delete_time
        if description is not None:
            self.description = description
        if directory is not None:
            self.directory = directory
        if owner_type is not None:
            self.owner_type = owner_type
        if pipe_alias is not None:
            self.pipe_alias = pipe_alias
        if pipe_id is not None:
            self.pipe_id = pipe_id
        if pipe_name is not None:
            self.pipe_name = pipe_name
        if process_error is not None:
            self.process_error = process_error
        if process_status is not None:
            self.process_status = process_status
        if project_id is not None:
            self.project_id = project_id
        if resources is not None:
            self.resources = resources
        if schema is not None:
            self.schema = schema
        if storage_setting is not None:
            self.storage_setting = storage_setting
        if update_by is not None:
            self.update_by = update_by
        if update_time is not None:
            self.update_time = update_time
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def category(self):
        r"""Gets the category of this ShowPipeResponse.

        资源类型，例如 STREAMING_TO_INDEX

        :return: The category of this ShowPipeResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowPipeResponse.

        资源类型，例如 STREAMING_TO_INDEX

        :param category: The category of this ShowPipeResponse.
        :type category: str
        """
        self._category = category

    @property
    def create_by(self):
        r"""Gets the create_by of this ShowPipeResponse.

        创建者信息

        :return: The create_by of this ShowPipeResponse.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this ShowPipeResponse.

        创建者信息

        :param create_by: The create_by of this ShowPipeResponse.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowPipeResponse.

        创建时间戳

        :return: The create_time of this ShowPipeResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowPipeResponse.

        创建时间戳

        :param create_time: The create_time of this ShowPipeResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def delete_time(self):
        r"""Gets the delete_time of this ShowPipeResponse.

        删除时间戳

        :return: The delete_time of this ShowPipeResponse.
        :rtype: int
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        r"""Sets the delete_time of this ShowPipeResponse.

        删除时间戳

        :param delete_time: The delete_time of this ShowPipeResponse.
        :type delete_time: int
        """
        self._delete_time = delete_time

    @property
    def description(self):
        r"""Gets the description of this ShowPipeResponse.

        描述信息

        :return: The description of this ShowPipeResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowPipeResponse.

        描述信息

        :param description: The description of this ShowPipeResponse.
        :type description: str
        """
        self._description = description

    @property
    def directory(self):
        r"""Gets the directory of this ShowPipeResponse.

        目录路径

        :return: The directory of this ShowPipeResponse.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this ShowPipeResponse.

        目录路径

        :param directory: The directory of this ShowPipeResponse.
        :type directory: str
        """
        self._directory = directory

    @property
    def owner_type(self):
        r"""Gets the owner_type of this ShowPipeResponse.

        所有者类型，例如 USER

        :return: The owner_type of this ShowPipeResponse.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        r"""Sets the owner_type of this ShowPipeResponse.

        所有者类型，例如 USER

        :param owner_type: The owner_type of this ShowPipeResponse.
        :type owner_type: str
        """
        self._owner_type = owner_type

    @property
    def pipe_alias(self):
        r"""Gets the pipe_alias of this ShowPipeResponse.

        管道别名

        :return: The pipe_alias of this ShowPipeResponse.
        :rtype: str
        """
        return self._pipe_alias

    @pipe_alias.setter
    def pipe_alias(self, pipe_alias):
        r"""Sets the pipe_alias of this ShowPipeResponse.

        管道别名

        :param pipe_alias: The pipe_alias of this ShowPipeResponse.
        :type pipe_alias: str
        """
        self._pipe_alias = pipe_alias

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this ShowPipeResponse.

        管道ID

        :return: The pipe_id of this ShowPipeResponse.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this ShowPipeResponse.

        管道ID

        :param pipe_id: The pipe_id of this ShowPipeResponse.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def pipe_name(self):
        r"""Gets the pipe_name of this ShowPipeResponse.

        管道名称

        :return: The pipe_name of this ShowPipeResponse.
        :rtype: str
        """
        return self._pipe_name

    @pipe_name.setter
    def pipe_name(self, pipe_name):
        r"""Sets the pipe_name of this ShowPipeResponse.

        管道名称

        :param pipe_name: The pipe_name of this ShowPipeResponse.
        :type pipe_name: str
        """
        self._pipe_name = pipe_name

    @property
    def process_error(self):
        r"""Gets the process_error of this ShowPipeResponse.

        处理错误状态，例如 NONE

        :return: The process_error of this ShowPipeResponse.
        :rtype: str
        """
        return self._process_error

    @process_error.setter
    def process_error(self, process_error):
        r"""Sets the process_error of this ShowPipeResponse.

        处理错误状态，例如 NONE

        :param process_error: The process_error of this ShowPipeResponse.
        :type process_error: str
        """
        self._process_error = process_error

    @property
    def process_status(self):
        r"""Gets the process_status of this ShowPipeResponse.

        处理状态，例如 COMPLETED

        :return: The process_status of this ShowPipeResponse.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this ShowPipeResponse.

        处理状态，例如 COMPLETED

        :param process_status: The process_status of this ShowPipeResponse.
        :type process_status: str
        """
        self._process_status = process_status

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowPipeResponse.

        项目ID

        :return: The project_id of this ShowPipeResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowPipeResponse.

        项目ID

        :param project_id: The project_id of this ShowPipeResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resources(self):
        r"""Gets the resources of this ShowPipeResponse.

        资源列表

        :return: The resources of this ShowPipeResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.IsapResource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ShowPipeResponse.

        资源列表

        :param resources: The resources of this ShowPipeResponse.
        :type resources: list[:class:`huaweicloudsdksecmaster.v1.IsapResource`]
        """
        self._resources = resources

    @property
    def schema(self):
        r"""Gets the schema of this ShowPipeResponse.

        :return: The schema of this ShowPipeResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Schema`
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this ShowPipeResponse.

        :param schema: The schema of this ShowPipeResponse.
        :type schema: :class:`huaweicloudsdksecmaster.v1.Schema`
        """
        self._schema = schema

    @property
    def storage_setting(self):
        r"""Gets the storage_setting of this ShowPipeResponse.

        :return: The storage_setting of this ShowPipeResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.StorageSetting`
        """
        return self._storage_setting

    @storage_setting.setter
    def storage_setting(self, storage_setting):
        r"""Sets the storage_setting of this ShowPipeResponse.

        :param storage_setting: The storage_setting of this ShowPipeResponse.
        :type storage_setting: :class:`huaweicloudsdksecmaster.v1.StorageSetting`
        """
        self._storage_setting = storage_setting

    @property
    def update_by(self):
        r"""Gets the update_by of this ShowPipeResponse.

        更新者信息

        :return: The update_by of this ShowPipeResponse.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this ShowPipeResponse.

        更新者信息

        :param update_by: The update_by of this ShowPipeResponse.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowPipeResponse.

        更新时间戳

        :return: The update_time of this ShowPipeResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowPipeResponse.

        更新时间戳

        :param update_time: The update_time of this ShowPipeResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowPipeResponse.

        工作空间ID

        :return: The workspace_id of this ShowPipeResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowPipeResponse.

        工作空间ID

        :param workspace_id: The workspace_id of this ShowPipeResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowPipeResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowPipeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
