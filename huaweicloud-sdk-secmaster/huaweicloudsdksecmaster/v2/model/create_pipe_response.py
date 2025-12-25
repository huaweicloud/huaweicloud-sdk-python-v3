# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePipeResponse(SdkResponse):

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
        'pipe_id': 'str',
        'pipe_name': 'str',
        'pipe_alias': 'str',
        'category': 'str',
        'directory': 'str',
        'description': 'str',
        'process_status': 'str',
        'process_error': 'str',
        'owner_type': 'str',
        'resources': 'list[PipeResource]',
        'schema': 'PipeSchema',
        'create_time': 'int',
        'update_time': 'int',
        'delete_time': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'pipe_id': 'pipe_id',
        'pipe_name': 'pipe_name',
        'pipe_alias': 'pipe_alias',
        'category': 'category',
        'directory': 'directory',
        'description': 'description',
        'process_status': 'process_status',
        'process_error': 'process_error',
        'owner_type': 'owner_type',
        'resources': 'resources',
        'schema': 'schema',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'delete_time': 'delete_time'
    }

    def __init__(self, project_id=None, workspace_id=None, pipe_id=None, pipe_name=None, pipe_alias=None, category=None, directory=None, description=None, process_status=None, process_error=None, owner_type=None, resources=None, schema=None, create_time=None, update_time=None, delete_time=None):
        r"""CreatePipeResponse

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: UUID
        :type workspace_id: str
        :param pipe_id: UUID
        :type pipe_id: str
        :param pipe_name: 管道名称
        :type pipe_name: str
        :param pipe_alias: 管道别名
        :type pipe_alias: str
        :param category: **参数解释**: 管道目录 - STREAMING_TO_INDEX 流式写入索引 - STREAMING_TO_LAKE 流式写入数据湖 - STREAMING_TO_INDEX_LAKE 流式写入索引和数据湖 - STREAMING  流式传输中  **约束限制** 不涉及  **取值范围**: - STREAMING_TO_INDEX - STREAMING_TO_LAKE - STREAMING_TO_INDEX_LAKE - STREAMING  **默认值** 不涉及       
        :type category: str
        :param directory: directory 目录分组
        :type directory: str
        :param description: 管道描述
        :type description: str
        :param process_status: **参数解释**: 作业处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - DELETING 删除中 - UPDATING_FAILED 更新失败 - DELETING_FAILED 删除失败  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - DELETING - UPDATING_FAILED - DELETING_FAILED  **默认值** 不涉及   
        :type process_status: str
        :param process_error: **参数解释**: 管道处理错误 - NONE 无  **约束限制** 不涉及 **取值范围**: - NONE  **默认值** 不涉及  
        :type process_error: str
        :param owner_type: **参数解释**: 管道所有者类型 - SYSTEM 系统 - USER 用户 - CLOUD_LOG 云日志  **约束限制** 不涉及 **取值范围**: - SYSTEM - USER - CLOUD_LOG  **默认值** 不涉及  
        :type owner_type: str
        :param resources: 管道资源
        :type resources: list[:class:`huaweicloudsdksecmaster.v2.PipeResource`]
        :param schema: 
        :type schema: :class:`huaweicloudsdksecmaster.v2.PipeSchema`
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
        self._pipe_id = None
        self._pipe_name = None
        self._pipe_alias = None
        self._category = None
        self._directory = None
        self._description = None
        self._process_status = None
        self._process_error = None
        self._owner_type = None
        self._resources = None
        self._schema = None
        self._create_time = None
        self._update_time = None
        self._delete_time = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if pipe_id is not None:
            self.pipe_id = pipe_id
        if pipe_name is not None:
            self.pipe_name = pipe_name
        if pipe_alias is not None:
            self.pipe_alias = pipe_alias
        if category is not None:
            self.category = category
        if directory is not None:
            self.directory = directory
        if description is not None:
            self.description = description
        if process_status is not None:
            self.process_status = process_status
        if process_error is not None:
            self.process_error = process_error
        if owner_type is not None:
            self.owner_type = owner_type
        if resources is not None:
            self.resources = resources
        if schema is not None:
            self.schema = schema
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if delete_time is not None:
            self.delete_time = delete_time

    @property
    def project_id(self):
        r"""Gets the project_id of this CreatePipeResponse.

        项目ID

        :return: The project_id of this CreatePipeResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreatePipeResponse.

        项目ID

        :param project_id: The project_id of this CreatePipeResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CreatePipeResponse.

        UUID

        :return: The workspace_id of this CreatePipeResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CreatePipeResponse.

        UUID

        :param workspace_id: The workspace_id of this CreatePipeResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this CreatePipeResponse.

        UUID

        :return: The pipe_id of this CreatePipeResponse.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this CreatePipeResponse.

        UUID

        :param pipe_id: The pipe_id of this CreatePipeResponse.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def pipe_name(self):
        r"""Gets the pipe_name of this CreatePipeResponse.

        管道名称

        :return: The pipe_name of this CreatePipeResponse.
        :rtype: str
        """
        return self._pipe_name

    @pipe_name.setter
    def pipe_name(self, pipe_name):
        r"""Sets the pipe_name of this CreatePipeResponse.

        管道名称

        :param pipe_name: The pipe_name of this CreatePipeResponse.
        :type pipe_name: str
        """
        self._pipe_name = pipe_name

    @property
    def pipe_alias(self):
        r"""Gets the pipe_alias of this CreatePipeResponse.

        管道别名

        :return: The pipe_alias of this CreatePipeResponse.
        :rtype: str
        """
        return self._pipe_alias

    @pipe_alias.setter
    def pipe_alias(self, pipe_alias):
        r"""Sets the pipe_alias of this CreatePipeResponse.

        管道别名

        :param pipe_alias: The pipe_alias of this CreatePipeResponse.
        :type pipe_alias: str
        """
        self._pipe_alias = pipe_alias

    @property
    def category(self):
        r"""Gets the category of this CreatePipeResponse.

        **参数解释**: 管道目录 - STREAMING_TO_INDEX 流式写入索引 - STREAMING_TO_LAKE 流式写入数据湖 - STREAMING_TO_INDEX_LAKE 流式写入索引和数据湖 - STREAMING  流式传输中  **约束限制** 不涉及  **取值范围**: - STREAMING_TO_INDEX - STREAMING_TO_LAKE - STREAMING_TO_INDEX_LAKE - STREAMING  **默认值** 不涉及       

        :return: The category of this CreatePipeResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreatePipeResponse.

        **参数解释**: 管道目录 - STREAMING_TO_INDEX 流式写入索引 - STREAMING_TO_LAKE 流式写入数据湖 - STREAMING_TO_INDEX_LAKE 流式写入索引和数据湖 - STREAMING  流式传输中  **约束限制** 不涉及  **取值范围**: - STREAMING_TO_INDEX - STREAMING_TO_LAKE - STREAMING_TO_INDEX_LAKE - STREAMING  **默认值** 不涉及       

        :param category: The category of this CreatePipeResponse.
        :type category: str
        """
        self._category = category

    @property
    def directory(self):
        r"""Gets the directory of this CreatePipeResponse.

        directory 目录分组

        :return: The directory of this CreatePipeResponse.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this CreatePipeResponse.

        directory 目录分组

        :param directory: The directory of this CreatePipeResponse.
        :type directory: str
        """
        self._directory = directory

    @property
    def description(self):
        r"""Gets the description of this CreatePipeResponse.

        管道描述

        :return: The description of this CreatePipeResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePipeResponse.

        管道描述

        :param description: The description of this CreatePipeResponse.
        :type description: str
        """
        self._description = description

    @property
    def process_status(self):
        r"""Gets the process_status of this CreatePipeResponse.

        **参数解释**: 作业处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - DELETING 删除中 - UPDATING_FAILED 更新失败 - DELETING_FAILED 删除失败  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - DELETING - UPDATING_FAILED - DELETING_FAILED  **默认值** 不涉及   

        :return: The process_status of this CreatePipeResponse.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this CreatePipeResponse.

        **参数解释**: 作业处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - DELETING 删除中 - UPDATING_FAILED 更新失败 - DELETING_FAILED 删除失败  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - DELETING - UPDATING_FAILED - DELETING_FAILED  **默认值** 不涉及   

        :param process_status: The process_status of this CreatePipeResponse.
        :type process_status: str
        """
        self._process_status = process_status

    @property
    def process_error(self):
        r"""Gets the process_error of this CreatePipeResponse.

        **参数解释**: 管道处理错误 - NONE 无  **约束限制** 不涉及 **取值范围**: - NONE  **默认值** 不涉及  

        :return: The process_error of this CreatePipeResponse.
        :rtype: str
        """
        return self._process_error

    @process_error.setter
    def process_error(self, process_error):
        r"""Sets the process_error of this CreatePipeResponse.

        **参数解释**: 管道处理错误 - NONE 无  **约束限制** 不涉及 **取值范围**: - NONE  **默认值** 不涉及  

        :param process_error: The process_error of this CreatePipeResponse.
        :type process_error: str
        """
        self._process_error = process_error

    @property
    def owner_type(self):
        r"""Gets the owner_type of this CreatePipeResponse.

        **参数解释**: 管道所有者类型 - SYSTEM 系统 - USER 用户 - CLOUD_LOG 云日志  **约束限制** 不涉及 **取值范围**: - SYSTEM - USER - CLOUD_LOG  **默认值** 不涉及  

        :return: The owner_type of this CreatePipeResponse.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        r"""Sets the owner_type of this CreatePipeResponse.

        **参数解释**: 管道所有者类型 - SYSTEM 系统 - USER 用户 - CLOUD_LOG 云日志  **约束限制** 不涉及 **取值范围**: - SYSTEM - USER - CLOUD_LOG  **默认值** 不涉及  

        :param owner_type: The owner_type of this CreatePipeResponse.
        :type owner_type: str
        """
        self._owner_type = owner_type

    @property
    def resources(self):
        r"""Gets the resources of this CreatePipeResponse.

        管道资源

        :return: The resources of this CreatePipeResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.PipeResource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this CreatePipeResponse.

        管道资源

        :param resources: The resources of this CreatePipeResponse.
        :type resources: list[:class:`huaweicloudsdksecmaster.v2.PipeResource`]
        """
        self._resources = resources

    @property
    def schema(self):
        r"""Gets the schema of this CreatePipeResponse.

        :return: The schema of this CreatePipeResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.PipeSchema`
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this CreatePipeResponse.

        :param schema: The schema of this CreatePipeResponse.
        :type schema: :class:`huaweicloudsdksecmaster.v2.PipeSchema`
        """
        self._schema = schema

    @property
    def create_time(self):
        r"""Gets the create_time of this CreatePipeResponse.

        毫秒时间戳

        :return: The create_time of this CreatePipeResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreatePipeResponse.

        毫秒时间戳

        :param create_time: The create_time of this CreatePipeResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CreatePipeResponse.

        毫秒时间戳

        :return: The update_time of this CreatePipeResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreatePipeResponse.

        毫秒时间戳

        :param update_time: The update_time of this CreatePipeResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def delete_time(self):
        r"""Gets the delete_time of this CreatePipeResponse.

        毫秒时间戳

        :return: The delete_time of this CreatePipeResponse.
        :rtype: int
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        r"""Sets the delete_time of this CreatePipeResponse.

        毫秒时间戳

        :param delete_time: The delete_time of this CreatePipeResponse.
        :type delete_time: int
        """
        self._delete_time = delete_time

    def to_dict(self):
        import warnings
        warnings.warn("CreatePipeResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreatePipeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
