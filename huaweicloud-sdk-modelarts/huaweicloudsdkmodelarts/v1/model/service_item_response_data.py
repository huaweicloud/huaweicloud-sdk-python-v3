# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceItemResponseData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'version': 'str',
        'version_count': 'int',
        'description': 'str',
        'type': 'str',
        'deploy_type': 'str',
        'user_name': 'str',
        'workspace_id': 'str',
        'create_at': 'int',
        'update_at': 'int',
        'auth_type': 'str',
        'task_type': 'str',
        'tags': 'list[TagsResponse]',
        'schedule': 'list[ScheduleConfigResponse]',
        'frozen_infos': 'list[FrozenInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'version': 'version',
        'version_count': 'version_count',
        'description': 'description',
        'type': 'type',
        'deploy_type': 'deploy_type',
        'user_name': 'user_name',
        'workspace_id': 'workspace_id',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'auth_type': 'auth_type',
        'task_type': 'task_type',
        'tags': 'tags',
        'schedule': 'schedule',
        'frozen_infos': 'frozen_infos'
    }

    def __init__(self, id=None, name=None, status=None, version=None, version_count=None, description=None, type=None, deploy_type=None, user_name=None, workspace_id=None, create_at=None, update_at=None, auth_type=None, task_type=None, tags=None, schedule=None, frozen_infos=None):
        r"""ServiceItemResponseData

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **取值范围：** 服务ID。
        :type id: str
        :param name: **参数解释：** 服务名，用户在[创建服务](CreateInferService.xml)时自定义。 **取值范围：** 支持1-128个字符，可以包含字母、汉字、数字、连字符和下划线。
        :type name: str
        :param status: **参数解释：** 服务当前状态。 **取值范围：** - DEPLOYING：部署中。 - FAILED：失败。 - STOPPED：停止。 - RUNNING：运行中。 - DELETING：删除中。 - STOPPING：停止中。 - CONCERNING：告警。 - UPGRADING：升级中。 - ERROR：异常。 - INTERRUPTING：中断中。
        :type status: str
        :param version: **参数解释：** 服务版本号，以数字及点号组成，形如1.0.1。 **取值范围：** 1.0.0 ~ 99.99.99，长度不超过8位。
        :type version: str
        :param version_count: **参数解释：** 服务版本数量。 **取值范围：** 不涉及。
        :type version_count: int
        :param description: **参数解释：** 服务描述，由用户[创建服务](CreateInferService.xml)时自行填写。 **取值范围：** 不涉及
        :type description: str
        :param type: **参数解释：** 推理服务类型。 **约束限制：** 不涉及。 **取值范围：** - REAL_TIME：在线服务。 - ASYNC_REAL_TIME：异步服务。 **默认取值：** 不涉及。
        :type type: str
        :param deploy_type: **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。
        :type deploy_type: str
        :param user_name: **参数解释：** 创建服务的用户名。 **取值范围：** 用户名。
        :type user_name: str
        :param workspace_id: **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID。 - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml)。
        :type workspace_id: str
        :param create_at: **参数解释：** 创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。
        :type create_at: int
        :param update_at: **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。
        :type update_at: int
        :param auth_type: **参数解释：** 在线服务认证类型。 **取值范围：** - TOKEN：IAM Token认证。 - API_KEY：API Key认证。 - NONE：无认证。
        :type auth_type: str
        :param task_type: **参数解释：** 模型类型。 **取值范围：** - TEXT_GENERATION：文本生成 - IMAGE_UNDERSTANDING：图像理解 - VIDEO_GENERATION：视频生成 - IMAGE_GENERATION：图像生成 - RERANK：重排序 - VECTOR_MODEL：向量模型 - EMBEDDING：Embedding嵌入
        :type task_type: str
        :param tags: **参数解释：** 在线服务标签数据。
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.TagsResponse`]
        :param schedule: **参数解释：** 定时停止配置。
        :type schedule: list[:class:`huaweicloudsdkmodelarts.v1.ScheduleConfigResponse`]
        :param frozen_infos: **参数解释：** 当服务或者部署被冻结时返回的冻结类型信息。
        :type frozen_infos: list[:class:`huaweicloudsdkmodelarts.v1.FrozenInfo`]
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._version = None
        self._version_count = None
        self._description = None
        self._type = None
        self._deploy_type = None
        self._user_name = None
        self._workspace_id = None
        self._create_at = None
        self._update_at = None
        self._auth_type = None
        self._task_type = None
        self._tags = None
        self._schedule = None
        self._frozen_infos = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version
        if version_count is not None:
            self.version_count = version_count
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if user_name is not None:
            self.user_name = user_name
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if auth_type is not None:
            self.auth_type = auth_type
        self.task_type = task_type
        if tags is not None:
            self.tags = tags
        if schedule is not None:
            self.schedule = schedule
        if frozen_infos is not None:
            self.frozen_infos = frozen_infos

    @property
    def id(self):
        r"""Gets the id of this ServiceItemResponseData.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **取值范围：** 服务ID。

        :return: The id of this ServiceItemResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServiceItemResponseData.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **取值范围：** 服务ID。

        :param id: The id of this ServiceItemResponseData.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ServiceItemResponseData.

        **参数解释：** 服务名，用户在[创建服务](CreateInferService.xml)时自定义。 **取值范围：** 支持1-128个字符，可以包含字母、汉字、数字、连字符和下划线。

        :return: The name of this ServiceItemResponseData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServiceItemResponseData.

        **参数解释：** 服务名，用户在[创建服务](CreateInferService.xml)时自定义。 **取值范围：** 支持1-128个字符，可以包含字母、汉字、数字、连字符和下划线。

        :param name: The name of this ServiceItemResponseData.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ServiceItemResponseData.

        **参数解释：** 服务当前状态。 **取值范围：** - DEPLOYING：部署中。 - FAILED：失败。 - STOPPED：停止。 - RUNNING：运行中。 - DELETING：删除中。 - STOPPING：停止中。 - CONCERNING：告警。 - UPGRADING：升级中。 - ERROR：异常。 - INTERRUPTING：中断中。

        :return: The status of this ServiceItemResponseData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ServiceItemResponseData.

        **参数解释：** 服务当前状态。 **取值范围：** - DEPLOYING：部署中。 - FAILED：失败。 - STOPPED：停止。 - RUNNING：运行中。 - DELETING：删除中。 - STOPPING：停止中。 - CONCERNING：告警。 - UPGRADING：升级中。 - ERROR：异常。 - INTERRUPTING：中断中。

        :param status: The status of this ServiceItemResponseData.
        :type status: str
        """
        self._status = status

    @property
    def version(self):
        r"""Gets the version of this ServiceItemResponseData.

        **参数解释：** 服务版本号，以数字及点号组成，形如1.0.1。 **取值范围：** 1.0.0 ~ 99.99.99，长度不超过8位。

        :return: The version of this ServiceItemResponseData.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ServiceItemResponseData.

        **参数解释：** 服务版本号，以数字及点号组成，形如1.0.1。 **取值范围：** 1.0.0 ~ 99.99.99，长度不超过8位。

        :param version: The version of this ServiceItemResponseData.
        :type version: str
        """
        self._version = version

    @property
    def version_count(self):
        r"""Gets the version_count of this ServiceItemResponseData.

        **参数解释：** 服务版本数量。 **取值范围：** 不涉及。

        :return: The version_count of this ServiceItemResponseData.
        :rtype: int
        """
        return self._version_count

    @version_count.setter
    def version_count(self, version_count):
        r"""Sets the version_count of this ServiceItemResponseData.

        **参数解释：** 服务版本数量。 **取值范围：** 不涉及。

        :param version_count: The version_count of this ServiceItemResponseData.
        :type version_count: int
        """
        self._version_count = version_count

    @property
    def description(self):
        r"""Gets the description of this ServiceItemResponseData.

        **参数解释：** 服务描述，由用户[创建服务](CreateInferService.xml)时自行填写。 **取值范围：** 不涉及

        :return: The description of this ServiceItemResponseData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ServiceItemResponseData.

        **参数解释：** 服务描述，由用户[创建服务](CreateInferService.xml)时自行填写。 **取值范围：** 不涉及

        :param description: The description of this ServiceItemResponseData.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this ServiceItemResponseData.

        **参数解释：** 推理服务类型。 **约束限制：** 不涉及。 **取值范围：** - REAL_TIME：在线服务。 - ASYNC_REAL_TIME：异步服务。 **默认取值：** 不涉及。

        :return: The type of this ServiceItemResponseData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ServiceItemResponseData.

        **参数解释：** 推理服务类型。 **约束限制：** 不涉及。 **取值范围：** - REAL_TIME：在线服务。 - ASYNC_REAL_TIME：异步服务。 **默认取值：** 不涉及。

        :param type: The type of this ServiceItemResponseData.
        :type type: str
        """
        self._type = type

    @property
    def deploy_type(self):
        r"""Gets the deploy_type of this ServiceItemResponseData.

        **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。

        :return: The deploy_type of this ServiceItemResponseData.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        r"""Sets the deploy_type of this ServiceItemResponseData.

        **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。

        :param deploy_type: The deploy_type of this ServiceItemResponseData.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def user_name(self):
        r"""Gets the user_name of this ServiceItemResponseData.

        **参数解释：** 创建服务的用户名。 **取值范围：** 用户名。

        :return: The user_name of this ServiceItemResponseData.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ServiceItemResponseData.

        **参数解释：** 创建服务的用户名。 **取值范围：** 用户名。

        :param user_name: The user_name of this ServiceItemResponseData.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ServiceItemResponseData.

        **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID。 - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml)。

        :return: The workspace_id of this ServiceItemResponseData.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ServiceItemResponseData.

        **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID。 - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml)。

        :param workspace_id: The workspace_id of this ServiceItemResponseData.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def create_at(self):
        r"""Gets the create_at of this ServiceItemResponseData.

        **参数解释：** 创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。

        :return: The create_at of this ServiceItemResponseData.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ServiceItemResponseData.

        **参数解释：** 创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。

        :param create_at: The create_at of this ServiceItemResponseData.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this ServiceItemResponseData.

        **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。

        :return: The update_at of this ServiceItemResponseData.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ServiceItemResponseData.

        **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。

        :param update_at: The update_at of this ServiceItemResponseData.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def auth_type(self):
        r"""Gets the auth_type of this ServiceItemResponseData.

        **参数解释：** 在线服务认证类型。 **取值范围：** - TOKEN：IAM Token认证。 - API_KEY：API Key认证。 - NONE：无认证。

        :return: The auth_type of this ServiceItemResponseData.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this ServiceItemResponseData.

        **参数解释：** 在线服务认证类型。 **取值范围：** - TOKEN：IAM Token认证。 - API_KEY：API Key认证。 - NONE：无认证。

        :param auth_type: The auth_type of this ServiceItemResponseData.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def task_type(self):
        r"""Gets the task_type of this ServiceItemResponseData.

        **参数解释：** 模型类型。 **取值范围：** - TEXT_GENERATION：文本生成 - IMAGE_UNDERSTANDING：图像理解 - VIDEO_GENERATION：视频生成 - IMAGE_GENERATION：图像生成 - RERANK：重排序 - VECTOR_MODEL：向量模型 - EMBEDDING：Embedding嵌入

        :return: The task_type of this ServiceItemResponseData.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ServiceItemResponseData.

        **参数解释：** 模型类型。 **取值范围：** - TEXT_GENERATION：文本生成 - IMAGE_UNDERSTANDING：图像理解 - VIDEO_GENERATION：视频生成 - IMAGE_GENERATION：图像生成 - RERANK：重排序 - VECTOR_MODEL：向量模型 - EMBEDDING：Embedding嵌入

        :param task_type: The task_type of this ServiceItemResponseData.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def tags(self):
        r"""Gets the tags of this ServiceItemResponseData.

        **参数解释：** 在线服务标签数据。

        :return: The tags of this ServiceItemResponseData.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.TagsResponse`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ServiceItemResponseData.

        **参数解释：** 在线服务标签数据。

        :param tags: The tags of this ServiceItemResponseData.
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.TagsResponse`]
        """
        self._tags = tags

    @property
    def schedule(self):
        r"""Gets the schedule of this ServiceItemResponseData.

        **参数解释：** 定时停止配置。

        :return: The schedule of this ServiceItemResponseData.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ScheduleConfigResponse`]
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this ServiceItemResponseData.

        **参数解释：** 定时停止配置。

        :param schedule: The schedule of this ServiceItemResponseData.
        :type schedule: list[:class:`huaweicloudsdkmodelarts.v1.ScheduleConfigResponse`]
        """
        self._schedule = schedule

    @property
    def frozen_infos(self):
        r"""Gets the frozen_infos of this ServiceItemResponseData.

        **参数解释：** 当服务或者部署被冻结时返回的冻结类型信息。

        :return: The frozen_infos of this ServiceItemResponseData.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.FrozenInfo`]
        """
        return self._frozen_infos

    @frozen_infos.setter
    def frozen_infos(self, frozen_infos):
        r"""Sets the frozen_infos of this ServiceItemResponseData.

        **参数解释：** 当服务或者部署被冻结时返回的冻结类型信息。

        :param frozen_infos: The frozen_infos of this ServiceItemResponseData.
        :type frozen_infos: list[:class:`huaweicloudsdkmodelarts.v1.FrozenInfo`]
        """
        self._frozen_infos = frozen_infos

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
        if not isinstance(other, ServiceItemResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
