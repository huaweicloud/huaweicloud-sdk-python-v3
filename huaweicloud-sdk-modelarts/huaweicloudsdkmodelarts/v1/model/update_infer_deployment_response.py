# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInferDeploymentResponse(SdkResponse):

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
        'workspace_id': 'str',
        'type': 'str',
        'deploy_type': 'str',
        'status': 'str',
        'failure_reason': 'str',
        'version': 'ServiceVersionResponse',
        'predict_url': 'list[PredictUrlResponse]',
        'dispatcher_group_id': 'str',
        'tags': 'list[TagsResponse]',
        'deploy_timeout_minutes': 'int',
        'schedule': 'list[ScheduleConfigResponse]',
        'create_at': 'str',
        'update_at': 'str',
        'task_type': 'str',
        'provider': 'str',
        'frozen_infos': 'list[FrozenInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'workspace_id': 'workspace_id',
        'type': 'type',
        'deploy_type': 'deploy_type',
        'status': 'status',
        'failure_reason': 'failure_reason',
        'version': 'version',
        'predict_url': 'predict_url',
        'dispatcher_group_id': 'dispatcher_group_id',
        'tags': 'tags',
        'deploy_timeout_minutes': 'deploy_timeout_minutes',
        'schedule': 'schedule',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'task_type': 'task_type',
        'provider': 'provider',
        'frozen_infos': 'frozen_infos'
    }

    def __init__(self, id=None, name=None, workspace_id=None, type=None, deploy_type=None, status=None, failure_reason=None, version=None, predict_url=None, dispatcher_group_id=None, tags=None, deploy_timeout_minutes=None, schedule=None, create_at=None, update_at=None, task_type=None, provider=None, frozen_infos=None):
        r"""UpdateInferDeploymentResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **取值范围：** 不涉及。
        :type id: str
        :param name: **参数解释：** 服务名，用户在[创建服务](CreateInferService.xml)时自定义的名称。 **取值范围：** 支持1-64位字符，可包含字母、中文、数字、中划线、下划线。
        :type name: str
        :param workspace_id: **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID。 - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml)。
        :type workspace_id: str
        :param type: **参数解释：** 推理服务类型。 **取值范围：** - REAL_TIME：在线服务。 - ASYNC_REAL_TIME：异步服务。
        :type type: str
        :param deploy_type: **参数解释：** 部署方式。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。
        :type deploy_type: str
        :param status: **参数解释：** 服务当前状态。 **取值范围：** - DEPLOYING：部署中 。 - FAILED：失败 。 - STOPPED：停止。 - RUNNING：运行中。 - DELETING：删除中 。 - STOPPING：停止中 。 - CONCERNING：告警 。 - UPGRADING：升级中 。 - ERROR：异常 。 - INIT：待部署。
        :type status: str
        :param failure_reason: **参数解释：** 在线服务失败原因。 **取值范围：** 不涉及。
        :type failure_reason: str
        :param version: 
        :type version: :class:`huaweicloudsdkmodelarts.v1.ServiceVersionResponse`
        :param predict_url: **参数解释：** 在线服务访问地址，创建服务接口无返回，详情接口中返回。
        :type predict_url: list[:class:`huaweicloudsdkmodelarts.v1.PredictUrlResponse`]
        :param dispatcher_group_id: **参数解释：** 服务绑定的dispatcher组ID，创建服务接口无返回，详情接口中返回。 **取值范围：** 不涉及。
        :type dispatcher_group_id: str
        :param tags: **参数解释：** TMS对接标签类。
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.TagsResponse`]
        :param deploy_timeout_minutes: **参数解释：** 部署超时时间。
        :type deploy_timeout_minutes: int
        :param schedule: **参数解释：** 定时停止配置。
        :type schedule: list[:class:`huaweicloudsdkmodelarts.v1.ScheduleConfigResponse`]
        :param create_at: **参数解释：** 创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字，如1609459200000。
        :type create_at: str
        :param update_at: **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字，如1609459200000。
        :type update_at: str
        :param task_type: **参数解释：** 模型类型。 **取值范围：** - TEXT_GENERATION：文本生成 - IMAGE_UNDERSTANDING：图像理解 - VIDEO_GENERATION：视频生成 - IMAGE_GENERATION：图像生成 - RERANK：重排序 - VECTOR_MODEL：向量模型 - EMBEDDING：Embedding嵌入
        :type task_type: str
        :param provider: **参数解释：** 服务提供者的账号id（创建服务时通过X-Auth-Token-Provider请求头解析iam token而来），该值不为空时，该服务的所有更新操作需要在请求头中添加X-Auth-Token-Provider，取值为该账号id的domain级或project级token。
        :type provider: str
        :param frozen_infos: **参数解释：** 当服务或者部署被冻结时返回的冻结类型信息。
        :type frozen_infos: list[:class:`huaweicloudsdkmodelarts.v1.FrozenInfo`]
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._workspace_id = None
        self._type = None
        self._deploy_type = None
        self._status = None
        self._failure_reason = None
        self._version = None
        self._predict_url = None
        self._dispatcher_group_id = None
        self._tags = None
        self._deploy_timeout_minutes = None
        self._schedule = None
        self._create_at = None
        self._update_at = None
        self._task_type = None
        self._provider = None
        self._frozen_infos = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if type is not None:
            self.type = type
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if status is not None:
            self.status = status
        if failure_reason is not None:
            self.failure_reason = failure_reason
        if version is not None:
            self.version = version
        if predict_url is not None:
            self.predict_url = predict_url
        if dispatcher_group_id is not None:
            self.dispatcher_group_id = dispatcher_group_id
        if tags is not None:
            self.tags = tags
        if deploy_timeout_minutes is not None:
            self.deploy_timeout_minutes = deploy_timeout_minutes
        if schedule is not None:
            self.schedule = schedule
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if task_type is not None:
            self.task_type = task_type
        if provider is not None:
            self.provider = provider
        if frozen_infos is not None:
            self.frozen_infos = frozen_infos

    @property
    def id(self):
        r"""Gets the id of this UpdateInferDeploymentResponse.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **取值范围：** 不涉及。

        :return: The id of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateInferDeploymentResponse.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **取值范围：** 不涉及。

        :param id: The id of this UpdateInferDeploymentResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateInferDeploymentResponse.

        **参数解释：** 服务名，用户在[创建服务](CreateInferService.xml)时自定义的名称。 **取值范围：** 支持1-64位字符，可包含字母、中文、数字、中划线、下划线。

        :return: The name of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateInferDeploymentResponse.

        **参数解释：** 服务名，用户在[创建服务](CreateInferService.xml)时自定义的名称。 **取值范围：** 支持1-64位字符，可包含字母、中文、数字、中划线、下划线。

        :param name: The name of this UpdateInferDeploymentResponse.
        :type name: str
        """
        self._name = name

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this UpdateInferDeploymentResponse.

        **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID。 - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml)。

        :return: The workspace_id of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this UpdateInferDeploymentResponse.

        **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID。 - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml)。

        :param workspace_id: The workspace_id of this UpdateInferDeploymentResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def type(self):
        r"""Gets the type of this UpdateInferDeploymentResponse.

        **参数解释：** 推理服务类型。 **取值范围：** - REAL_TIME：在线服务。 - ASYNC_REAL_TIME：异步服务。

        :return: The type of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateInferDeploymentResponse.

        **参数解释：** 推理服务类型。 **取值范围：** - REAL_TIME：在线服务。 - ASYNC_REAL_TIME：异步服务。

        :param type: The type of this UpdateInferDeploymentResponse.
        :type type: str
        """
        self._type = type

    @property
    def deploy_type(self):
        r"""Gets the deploy_type of this UpdateInferDeploymentResponse.

        **参数解释：** 部署方式。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。

        :return: The deploy_type of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        r"""Sets the deploy_type of this UpdateInferDeploymentResponse.

        **参数解释：** 部署方式。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。

        :param deploy_type: The deploy_type of this UpdateInferDeploymentResponse.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def status(self):
        r"""Gets the status of this UpdateInferDeploymentResponse.

        **参数解释：** 服务当前状态。 **取值范围：** - DEPLOYING：部署中 。 - FAILED：失败 。 - STOPPED：停止。 - RUNNING：运行中。 - DELETING：删除中 。 - STOPPING：停止中 。 - CONCERNING：告警 。 - UPGRADING：升级中 。 - ERROR：异常 。 - INIT：待部署。

        :return: The status of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateInferDeploymentResponse.

        **参数解释：** 服务当前状态。 **取值范围：** - DEPLOYING：部署中 。 - FAILED：失败 。 - STOPPED：停止。 - RUNNING：运行中。 - DELETING：删除中 。 - STOPPING：停止中 。 - CONCERNING：告警 。 - UPGRADING：升级中 。 - ERROR：异常 。 - INIT：待部署。

        :param status: The status of this UpdateInferDeploymentResponse.
        :type status: str
        """
        self._status = status

    @property
    def failure_reason(self):
        r"""Gets the failure_reason of this UpdateInferDeploymentResponse.

        **参数解释：** 在线服务失败原因。 **取值范围：** 不涉及。

        :return: The failure_reason of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        r"""Sets the failure_reason of this UpdateInferDeploymentResponse.

        **参数解释：** 在线服务失败原因。 **取值范围：** 不涉及。

        :param failure_reason: The failure_reason of this UpdateInferDeploymentResponse.
        :type failure_reason: str
        """
        self._failure_reason = failure_reason

    @property
    def version(self):
        r"""Gets the version of this UpdateInferDeploymentResponse.

        :return: The version of this UpdateInferDeploymentResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServiceVersionResponse`
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpdateInferDeploymentResponse.

        :param version: The version of this UpdateInferDeploymentResponse.
        :type version: :class:`huaweicloudsdkmodelarts.v1.ServiceVersionResponse`
        """
        self._version = version

    @property
    def predict_url(self):
        r"""Gets the predict_url of this UpdateInferDeploymentResponse.

        **参数解释：** 在线服务访问地址，创建服务接口无返回，详情接口中返回。

        :return: The predict_url of this UpdateInferDeploymentResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.PredictUrlResponse`]
        """
        return self._predict_url

    @predict_url.setter
    def predict_url(self, predict_url):
        r"""Sets the predict_url of this UpdateInferDeploymentResponse.

        **参数解释：** 在线服务访问地址，创建服务接口无返回，详情接口中返回。

        :param predict_url: The predict_url of this UpdateInferDeploymentResponse.
        :type predict_url: list[:class:`huaweicloudsdkmodelarts.v1.PredictUrlResponse`]
        """
        self._predict_url = predict_url

    @property
    def dispatcher_group_id(self):
        r"""Gets the dispatcher_group_id of this UpdateInferDeploymentResponse.

        **参数解释：** 服务绑定的dispatcher组ID，创建服务接口无返回，详情接口中返回。 **取值范围：** 不涉及。

        :return: The dispatcher_group_id of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._dispatcher_group_id

    @dispatcher_group_id.setter
    def dispatcher_group_id(self, dispatcher_group_id):
        r"""Sets the dispatcher_group_id of this UpdateInferDeploymentResponse.

        **参数解释：** 服务绑定的dispatcher组ID，创建服务接口无返回，详情接口中返回。 **取值范围：** 不涉及。

        :param dispatcher_group_id: The dispatcher_group_id of this UpdateInferDeploymentResponse.
        :type dispatcher_group_id: str
        """
        self._dispatcher_group_id = dispatcher_group_id

    @property
    def tags(self):
        r"""Gets the tags of this UpdateInferDeploymentResponse.

        **参数解释：** TMS对接标签类。

        :return: The tags of this UpdateInferDeploymentResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.TagsResponse`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateInferDeploymentResponse.

        **参数解释：** TMS对接标签类。

        :param tags: The tags of this UpdateInferDeploymentResponse.
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.TagsResponse`]
        """
        self._tags = tags

    @property
    def deploy_timeout_minutes(self):
        r"""Gets the deploy_timeout_minutes of this UpdateInferDeploymentResponse.

        **参数解释：** 部署超时时间。

        :return: The deploy_timeout_minutes of this UpdateInferDeploymentResponse.
        :rtype: int
        """
        return self._deploy_timeout_minutes

    @deploy_timeout_minutes.setter
    def deploy_timeout_minutes(self, deploy_timeout_minutes):
        r"""Sets the deploy_timeout_minutes of this UpdateInferDeploymentResponse.

        **参数解释：** 部署超时时间。

        :param deploy_timeout_minutes: The deploy_timeout_minutes of this UpdateInferDeploymentResponse.
        :type deploy_timeout_minutes: int
        """
        self._deploy_timeout_minutes = deploy_timeout_minutes

    @property
    def schedule(self):
        r"""Gets the schedule of this UpdateInferDeploymentResponse.

        **参数解释：** 定时停止配置。

        :return: The schedule of this UpdateInferDeploymentResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ScheduleConfigResponse`]
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this UpdateInferDeploymentResponse.

        **参数解释：** 定时停止配置。

        :param schedule: The schedule of this UpdateInferDeploymentResponse.
        :type schedule: list[:class:`huaweicloudsdkmodelarts.v1.ScheduleConfigResponse`]
        """
        self._schedule = schedule

    @property
    def create_at(self):
        r"""Gets the create_at of this UpdateInferDeploymentResponse.

        **参数解释：** 创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字，如1609459200000。

        :return: The create_at of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this UpdateInferDeploymentResponse.

        **参数解释：** 创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字，如1609459200000。

        :param create_at: The create_at of this UpdateInferDeploymentResponse.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this UpdateInferDeploymentResponse.

        **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字，如1609459200000。

        :return: The update_at of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this UpdateInferDeploymentResponse.

        **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字，如1609459200000。

        :param update_at: The update_at of this UpdateInferDeploymentResponse.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def task_type(self):
        r"""Gets the task_type of this UpdateInferDeploymentResponse.

        **参数解释：** 模型类型。 **取值范围：** - TEXT_GENERATION：文本生成 - IMAGE_UNDERSTANDING：图像理解 - VIDEO_GENERATION：视频生成 - IMAGE_GENERATION：图像生成 - RERANK：重排序 - VECTOR_MODEL：向量模型 - EMBEDDING：Embedding嵌入

        :return: The task_type of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this UpdateInferDeploymentResponse.

        **参数解释：** 模型类型。 **取值范围：** - TEXT_GENERATION：文本生成 - IMAGE_UNDERSTANDING：图像理解 - VIDEO_GENERATION：视频生成 - IMAGE_GENERATION：图像生成 - RERANK：重排序 - VECTOR_MODEL：向量模型 - EMBEDDING：Embedding嵌入

        :param task_type: The task_type of this UpdateInferDeploymentResponse.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def provider(self):
        r"""Gets the provider of this UpdateInferDeploymentResponse.

        **参数解释：** 服务提供者的账号id（创建服务时通过X-Auth-Token-Provider请求头解析iam token而来），该值不为空时，该服务的所有更新操作需要在请求头中添加X-Auth-Token-Provider，取值为该账号id的domain级或project级token。

        :return: The provider of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this UpdateInferDeploymentResponse.

        **参数解释：** 服务提供者的账号id（创建服务时通过X-Auth-Token-Provider请求头解析iam token而来），该值不为空时，该服务的所有更新操作需要在请求头中添加X-Auth-Token-Provider，取值为该账号id的domain级或project级token。

        :param provider: The provider of this UpdateInferDeploymentResponse.
        :type provider: str
        """
        self._provider = provider

    @property
    def frozen_infos(self):
        r"""Gets the frozen_infos of this UpdateInferDeploymentResponse.

        **参数解释：** 当服务或者部署被冻结时返回的冻结类型信息。

        :return: The frozen_infos of this UpdateInferDeploymentResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.FrozenInfo`]
        """
        return self._frozen_infos

    @frozen_infos.setter
    def frozen_infos(self, frozen_infos):
        r"""Sets the frozen_infos of this UpdateInferDeploymentResponse.

        **参数解释：** 当服务或者部署被冻结时返回的冻结类型信息。

        :param frozen_infos: The frozen_infos of this UpdateInferDeploymentResponse.
        :type frozen_infos: list[:class:`huaweicloudsdkmodelarts.v1.FrozenInfo`]
        """
        self._frozen_infos = frozen_infos

    def to_dict(self):
        import warnings
        warnings.warn("UpdateInferDeploymentResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateInferDeploymentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
