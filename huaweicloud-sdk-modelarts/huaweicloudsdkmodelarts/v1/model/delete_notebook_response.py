# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteNotebookResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_progress': 'list[JobProgress]',
        'description': 'str',
        'endpoints': 'list[EndpointsRes]',
        'fail_reason': 'str',
        'flavor': 'str',
        'custom_spec': 'NotebookCustomSpecRep',
        'id': 'str',
        'image': 'Image',
        'lease': 'Lease',
        'name': 'str',
        'pool': 'Pool',
        'status': 'str',
        'token': 'str',
        'url': 'str',
        'volume': 'VolumeRes',
        'workspace_id': 'str',
        'feature': 'str',
        'billing_items': 'list[str]',
        'user': 'UserResponse',
        'affinity': 'AffinityType',
        'run_user': 'RunUserInfo',
        'data_volumes': 'list[VolumeResponse]',
        'ip': 'str',
        'user_vpc': 'UserVpcResponse',
        'user_id': 'str',
        'is_need_credentials': 'bool',
        'jupyter_version': 'str',
        'tags': 'list[TmsTagResponse]'
    }

    attribute_map = {
        'action_progress': 'action_progress',
        'description': 'description',
        'endpoints': 'endpoints',
        'fail_reason': 'fail_reason',
        'flavor': 'flavor',
        'custom_spec': 'custom_spec',
        'id': 'id',
        'image': 'image',
        'lease': 'lease',
        'name': 'name',
        'pool': 'pool',
        'status': 'status',
        'token': 'token',
        'url': 'url',
        'volume': 'volume',
        'workspace_id': 'workspace_id',
        'feature': 'feature',
        'billing_items': 'billing_items',
        'user': 'user',
        'affinity': 'affinity',
        'run_user': 'run_user',
        'data_volumes': 'data_volumes',
        'ip': 'ip',
        'user_vpc': 'user_vpc',
        'user_id': 'user_id',
        'is_need_credentials': 'is_need_credentials',
        'jupyter_version': 'jupyter_version',
        'tags': 'tags'
    }

    def __init__(self, action_progress=None, description=None, endpoints=None, fail_reason=None, flavor=None, custom_spec=None, id=None, image=None, lease=None, name=None, pool=None, status=None, token=None, url=None, volume=None, workspace_id=None, feature=None, billing_items=None, user=None, affinity=None, run_user=None, data_volumes=None, ip=None, user_vpc=None, user_id=None, is_need_credentials=None, jupyter_version=None, tags=None):
        r"""DeleteNotebookResponse

        The model defined in huaweicloud sdk

        :param action_progress: **参数解释**：实例初始化进度。
        :type action_progress: list[:class:`huaweicloudsdkmodelarts.v1.JobProgress`]
        :param description: **参数解释**：实例描述。 **取值范围**：不涉及。
        :type description: str
        :param endpoints: **参数解释**：本地IDE（如PyCharm、VS Code）或SSH客户端，通过SSH远程接入Notebook实例时需要的相关配置。
        :type endpoints: list[:class:`huaweicloudsdkmodelarts.v1.EndpointsRes`]
        :param fail_reason: **参数解释**：实例失败原因。 **取值范围**：不涉及。
        :type fail_reason: str
        :param flavor: **参数解释**：实例规格， 1.当用户选择系统规格时，返回值为系统规格码； 2.当用户创建实例时选择了自定义规格，则此字段会固定返回\&quot;custom.flavor.spec.code\&quot;。 **取值范围**：不涉及。
        :type flavor: str
        :param custom_spec: 
        :type custom_spec: :class:`huaweicloudsdkmodelarts.v1.NotebookCustomSpecRep`
        :param id: **参数解释**：实例ID。 **取值范围**：不涉及。
        :type id: str
        :param image: 
        :type image: :class:`huaweicloudsdkmodelarts.v1.Image`
        :param lease: 
        :type lease: :class:`huaweicloudsdkmodelarts.v1.Lease`
        :param name: **参数解释**：实例名称。 **取值范围**：不涉及。
        :type name: str
        :param pool: 
        :type pool: :class:`huaweicloudsdkmodelarts.v1.Pool`
        :param status: **参数解释**：实例状态。 **取值范围**：枚举类型，取值如下： - INIT：初始化 - CREATING：创建中 - STARTING：启动中 - STOPPING：停止中 - DELETING：删除中 - RUNNING：运行中 - STOPPED：已停止 - SNAPSHOTTING：快照中(保存镜像时的状态) - CREATE_FAILED：创建失败 - START_FAILED：启动失败 - DELETE_FAILED：删除失败 - ERROR：错误 - DELETED：已删除 - FROZEN：冻结
        :type status: str
        :param token: **参数解释**：Notebook鉴权使用的token信息。 **取值范围**：不涉及。
        :type token: str
        :param url: **参数解释**：实例访问的URL。 **取值范围**：不涉及。
        :type url: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkmodelarts.v1.VolumeRes`
        :param workspace_id: **参数解释**：工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围**：不涉及。
        :type workspace_id: str
        :param feature: **参数解释**：实例类别。 **取值范围**：枚举类型，取值如下： - DEFAULT：CodeLab免费规格实例，每个用户最多只能创建一个。 - NOTEBOOK：计费规格实例。
        :type feature: str
        :param billing_items: **参数解释**：计费资源类型。枚举类型，取值如下： - STORAGE：存储资源计费。 - COMPUTE：计算资源计费。 - ALL：所有计费类型。
        :type billing_items: list[str]
        :param user: 
        :type user: :class:`huaweicloudsdkmodelarts.v1.UserResponse`
        :param affinity: 
        :type affinity: :class:`huaweicloudsdkmodelarts.v1.AffinityType`
        :param run_user: 
        :type run_user: :class:`huaweicloudsdkmodelarts.v1.RunUserInfo`
        :param data_volumes: **参数解释**：扩展存储信息
        :type data_volumes: list[:class:`huaweicloudsdkmodelarts.v1.VolumeResponse`]
        :param ip: **参数解释**：实例所在节点ip。 **取值范围**：不涉及。
        :type ip: str
        :param user_vpc: 
        :type user_vpc: :class:`huaweicloudsdkmodelarts.v1.UserVpcResponse`
        :param user_id: **参数解释**：用户ID。 **取值范围**：不涉及。
        :type user_id: str
        :param is_need_credentials: **参数解释**：是否需要默认创建用户secret，默认为true。 **取值范围**：不涉及。
        :type is_need_credentials: bool
        :param jupyter_version: **参数解释**：jupyter version版本号。 **取值范围**：不涉及。
        :type jupyter_version: str
        :param tags: **参数解释**：实例标签。
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.TmsTagResponse`]
        """
        
        super().__init__()

        self._action_progress = None
        self._description = None
        self._endpoints = None
        self._fail_reason = None
        self._flavor = None
        self._custom_spec = None
        self._id = None
        self._image = None
        self._lease = None
        self._name = None
        self._pool = None
        self._status = None
        self._token = None
        self._url = None
        self._volume = None
        self._workspace_id = None
        self._feature = None
        self._billing_items = None
        self._user = None
        self._affinity = None
        self._run_user = None
        self._data_volumes = None
        self._ip = None
        self._user_vpc = None
        self._user_id = None
        self._is_need_credentials = None
        self._jupyter_version = None
        self._tags = None
        self.discriminator = None

        if action_progress is not None:
            self.action_progress = action_progress
        if description is not None:
            self.description = description
        if endpoints is not None:
            self.endpoints = endpoints
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if flavor is not None:
            self.flavor = flavor
        if custom_spec is not None:
            self.custom_spec = custom_spec
        if id is not None:
            self.id = id
        if image is not None:
            self.image = image
        if lease is not None:
            self.lease = lease
        if name is not None:
            self.name = name
        if pool is not None:
            self.pool = pool
        if status is not None:
            self.status = status
        if token is not None:
            self.token = token
        if url is not None:
            self.url = url
        if volume is not None:
            self.volume = volume
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if feature is not None:
            self.feature = feature
        if billing_items is not None:
            self.billing_items = billing_items
        if user is not None:
            self.user = user
        if affinity is not None:
            self.affinity = affinity
        if run_user is not None:
            self.run_user = run_user
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if ip is not None:
            self.ip = ip
        if user_vpc is not None:
            self.user_vpc = user_vpc
        if user_id is not None:
            self.user_id = user_id
        if is_need_credentials is not None:
            self.is_need_credentials = is_need_credentials
        if jupyter_version is not None:
            self.jupyter_version = jupyter_version
        if tags is not None:
            self.tags = tags

    @property
    def action_progress(self):
        r"""Gets the action_progress of this DeleteNotebookResponse.

        **参数解释**：实例初始化进度。

        :return: The action_progress of this DeleteNotebookResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.JobProgress`]
        """
        return self._action_progress

    @action_progress.setter
    def action_progress(self, action_progress):
        r"""Sets the action_progress of this DeleteNotebookResponse.

        **参数解释**：实例初始化进度。

        :param action_progress: The action_progress of this DeleteNotebookResponse.
        :type action_progress: list[:class:`huaweicloudsdkmodelarts.v1.JobProgress`]
        """
        self._action_progress = action_progress

    @property
    def description(self):
        r"""Gets the description of this DeleteNotebookResponse.

        **参数解释**：实例描述。 **取值范围**：不涉及。

        :return: The description of this DeleteNotebookResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DeleteNotebookResponse.

        **参数解释**：实例描述。 **取值范围**：不涉及。

        :param description: The description of this DeleteNotebookResponse.
        :type description: str
        """
        self._description = description

    @property
    def endpoints(self):
        r"""Gets the endpoints of this DeleteNotebookResponse.

        **参数解释**：本地IDE（如PyCharm、VS Code）或SSH客户端，通过SSH远程接入Notebook实例时需要的相关配置。

        :return: The endpoints of this DeleteNotebookResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.EndpointsRes`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this DeleteNotebookResponse.

        **参数解释**：本地IDE（如PyCharm、VS Code）或SSH客户端，通过SSH远程接入Notebook实例时需要的相关配置。

        :param endpoints: The endpoints of this DeleteNotebookResponse.
        :type endpoints: list[:class:`huaweicloudsdkmodelarts.v1.EndpointsRes`]
        """
        self._endpoints = endpoints

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this DeleteNotebookResponse.

        **参数解释**：实例失败原因。 **取值范围**：不涉及。

        :return: The fail_reason of this DeleteNotebookResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this DeleteNotebookResponse.

        **参数解释**：实例失败原因。 **取值范围**：不涉及。

        :param fail_reason: The fail_reason of this DeleteNotebookResponse.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def flavor(self):
        r"""Gets the flavor of this DeleteNotebookResponse.

        **参数解释**：实例规格， 1.当用户选择系统规格时，返回值为系统规格码； 2.当用户创建实例时选择了自定义规格，则此字段会固定返回\"custom.flavor.spec.code\"。 **取值范围**：不涉及。

        :return: The flavor of this DeleteNotebookResponse.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this DeleteNotebookResponse.

        **参数解释**：实例规格， 1.当用户选择系统规格时，返回值为系统规格码； 2.当用户创建实例时选择了自定义规格，则此字段会固定返回\"custom.flavor.spec.code\"。 **取值范围**：不涉及。

        :param flavor: The flavor of this DeleteNotebookResponse.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def custom_spec(self):
        r"""Gets the custom_spec of this DeleteNotebookResponse.

        :return: The custom_spec of this DeleteNotebookResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NotebookCustomSpecRep`
        """
        return self._custom_spec

    @custom_spec.setter
    def custom_spec(self, custom_spec):
        r"""Sets the custom_spec of this DeleteNotebookResponse.

        :param custom_spec: The custom_spec of this DeleteNotebookResponse.
        :type custom_spec: :class:`huaweicloudsdkmodelarts.v1.NotebookCustomSpecRep`
        """
        self._custom_spec = custom_spec

    @property
    def id(self):
        r"""Gets the id of this DeleteNotebookResponse.

        **参数解释**：实例ID。 **取值范围**：不涉及。

        :return: The id of this DeleteNotebookResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeleteNotebookResponse.

        **参数解释**：实例ID。 **取值范围**：不涉及。

        :param id: The id of this DeleteNotebookResponse.
        :type id: str
        """
        self._id = id

    @property
    def image(self):
        r"""Gets the image of this DeleteNotebookResponse.

        :return: The image of this DeleteNotebookResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Image`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this DeleteNotebookResponse.

        :param image: The image of this DeleteNotebookResponse.
        :type image: :class:`huaweicloudsdkmodelarts.v1.Image`
        """
        self._image = image

    @property
    def lease(self):
        r"""Gets the lease of this DeleteNotebookResponse.

        :return: The lease of this DeleteNotebookResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Lease`
        """
        return self._lease

    @lease.setter
    def lease(self, lease):
        r"""Sets the lease of this DeleteNotebookResponse.

        :param lease: The lease of this DeleteNotebookResponse.
        :type lease: :class:`huaweicloudsdkmodelarts.v1.Lease`
        """
        self._lease = lease

    @property
    def name(self):
        r"""Gets the name of this DeleteNotebookResponse.

        **参数解释**：实例名称。 **取值范围**：不涉及。

        :return: The name of this DeleteNotebookResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DeleteNotebookResponse.

        **参数解释**：实例名称。 **取值范围**：不涉及。

        :param name: The name of this DeleteNotebookResponse.
        :type name: str
        """
        self._name = name

    @property
    def pool(self):
        r"""Gets the pool of this DeleteNotebookResponse.

        :return: The pool of this DeleteNotebookResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Pool`
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        r"""Sets the pool of this DeleteNotebookResponse.

        :param pool: The pool of this DeleteNotebookResponse.
        :type pool: :class:`huaweicloudsdkmodelarts.v1.Pool`
        """
        self._pool = pool

    @property
    def status(self):
        r"""Gets the status of this DeleteNotebookResponse.

        **参数解释**：实例状态。 **取值范围**：枚举类型，取值如下： - INIT：初始化 - CREATING：创建中 - STARTING：启动中 - STOPPING：停止中 - DELETING：删除中 - RUNNING：运行中 - STOPPED：已停止 - SNAPSHOTTING：快照中(保存镜像时的状态) - CREATE_FAILED：创建失败 - START_FAILED：启动失败 - DELETE_FAILED：删除失败 - ERROR：错误 - DELETED：已删除 - FROZEN：冻结

        :return: The status of this DeleteNotebookResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DeleteNotebookResponse.

        **参数解释**：实例状态。 **取值范围**：枚举类型，取值如下： - INIT：初始化 - CREATING：创建中 - STARTING：启动中 - STOPPING：停止中 - DELETING：删除中 - RUNNING：运行中 - STOPPED：已停止 - SNAPSHOTTING：快照中(保存镜像时的状态) - CREATE_FAILED：创建失败 - START_FAILED：启动失败 - DELETE_FAILED：删除失败 - ERROR：错误 - DELETED：已删除 - FROZEN：冻结

        :param status: The status of this DeleteNotebookResponse.
        :type status: str
        """
        self._status = status

    @property
    def token(self):
        r"""Gets the token of this DeleteNotebookResponse.

        **参数解释**：Notebook鉴权使用的token信息。 **取值范围**：不涉及。

        :return: The token of this DeleteNotebookResponse.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this DeleteNotebookResponse.

        **参数解释**：Notebook鉴权使用的token信息。 **取值范围**：不涉及。

        :param token: The token of this DeleteNotebookResponse.
        :type token: str
        """
        self._token = token

    @property
    def url(self):
        r"""Gets the url of this DeleteNotebookResponse.

        **参数解释**：实例访问的URL。 **取值范围**：不涉及。

        :return: The url of this DeleteNotebookResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this DeleteNotebookResponse.

        **参数解释**：实例访问的URL。 **取值范围**：不涉及。

        :param url: The url of this DeleteNotebookResponse.
        :type url: str
        """
        self._url = url

    @property
    def volume(self):
        r"""Gets the volume of this DeleteNotebookResponse.

        :return: The volume of this DeleteNotebookResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.VolumeRes`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this DeleteNotebookResponse.

        :param volume: The volume of this DeleteNotebookResponse.
        :type volume: :class:`huaweicloudsdkmodelarts.v1.VolumeRes`
        """
        self._volume = volume

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this DeleteNotebookResponse.

        **参数解释**：工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围**：不涉及。

        :return: The workspace_id of this DeleteNotebookResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this DeleteNotebookResponse.

        **参数解释**：工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围**：不涉及。

        :param workspace_id: The workspace_id of this DeleteNotebookResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def feature(self):
        r"""Gets the feature of this DeleteNotebookResponse.

        **参数解释**：实例类别。 **取值范围**：枚举类型，取值如下： - DEFAULT：CodeLab免费规格实例，每个用户最多只能创建一个。 - NOTEBOOK：计费规格实例。

        :return: The feature of this DeleteNotebookResponse.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this DeleteNotebookResponse.

        **参数解释**：实例类别。 **取值范围**：枚举类型，取值如下： - DEFAULT：CodeLab免费规格实例，每个用户最多只能创建一个。 - NOTEBOOK：计费规格实例。

        :param feature: The feature of this DeleteNotebookResponse.
        :type feature: str
        """
        self._feature = feature

    @property
    def billing_items(self):
        r"""Gets the billing_items of this DeleteNotebookResponse.

        **参数解释**：计费资源类型。枚举类型，取值如下： - STORAGE：存储资源计费。 - COMPUTE：计算资源计费。 - ALL：所有计费类型。

        :return: The billing_items of this DeleteNotebookResponse.
        :rtype: list[str]
        """
        return self._billing_items

    @billing_items.setter
    def billing_items(self, billing_items):
        r"""Sets the billing_items of this DeleteNotebookResponse.

        **参数解释**：计费资源类型。枚举类型，取值如下： - STORAGE：存储资源计费。 - COMPUTE：计算资源计费。 - ALL：所有计费类型。

        :param billing_items: The billing_items of this DeleteNotebookResponse.
        :type billing_items: list[str]
        """
        self._billing_items = billing_items

    @property
    def user(self):
        r"""Gets the user of this DeleteNotebookResponse.

        :return: The user of this DeleteNotebookResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UserResponse`
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this DeleteNotebookResponse.

        :param user: The user of this DeleteNotebookResponse.
        :type user: :class:`huaweicloudsdkmodelarts.v1.UserResponse`
        """
        self._user = user

    @property
    def affinity(self):
        r"""Gets the affinity of this DeleteNotebookResponse.

        :return: The affinity of this DeleteNotebookResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AffinityType`
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        r"""Sets the affinity of this DeleteNotebookResponse.

        :param affinity: The affinity of this DeleteNotebookResponse.
        :type affinity: :class:`huaweicloudsdkmodelarts.v1.AffinityType`
        """
        self._affinity = affinity

    @property
    def run_user(self):
        r"""Gets the run_user of this DeleteNotebookResponse.

        :return: The run_user of this DeleteNotebookResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.RunUserInfo`
        """
        return self._run_user

    @run_user.setter
    def run_user(self, run_user):
        r"""Sets the run_user of this DeleteNotebookResponse.

        :param run_user: The run_user of this DeleteNotebookResponse.
        :type run_user: :class:`huaweicloudsdkmodelarts.v1.RunUserInfo`
        """
        self._run_user = run_user

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this DeleteNotebookResponse.

        **参数解释**：扩展存储信息

        :return: The data_volumes of this DeleteNotebookResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.VolumeResponse`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this DeleteNotebookResponse.

        **参数解释**：扩展存储信息

        :param data_volumes: The data_volumes of this DeleteNotebookResponse.
        :type data_volumes: list[:class:`huaweicloudsdkmodelarts.v1.VolumeResponse`]
        """
        self._data_volumes = data_volumes

    @property
    def ip(self):
        r"""Gets the ip of this DeleteNotebookResponse.

        **参数解释**：实例所在节点ip。 **取值范围**：不涉及。

        :return: The ip of this DeleteNotebookResponse.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this DeleteNotebookResponse.

        **参数解释**：实例所在节点ip。 **取值范围**：不涉及。

        :param ip: The ip of this DeleteNotebookResponse.
        :type ip: str
        """
        self._ip = ip

    @property
    def user_vpc(self):
        r"""Gets the user_vpc of this DeleteNotebookResponse.

        :return: The user_vpc of this DeleteNotebookResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UserVpcResponse`
        """
        return self._user_vpc

    @user_vpc.setter
    def user_vpc(self, user_vpc):
        r"""Sets the user_vpc of this DeleteNotebookResponse.

        :param user_vpc: The user_vpc of this DeleteNotebookResponse.
        :type user_vpc: :class:`huaweicloudsdkmodelarts.v1.UserVpcResponse`
        """
        self._user_vpc = user_vpc

    @property
    def user_id(self):
        r"""Gets the user_id of this DeleteNotebookResponse.

        **参数解释**：用户ID。 **取值范围**：不涉及。

        :return: The user_id of this DeleteNotebookResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this DeleteNotebookResponse.

        **参数解释**：用户ID。 **取值范围**：不涉及。

        :param user_id: The user_id of this DeleteNotebookResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def is_need_credentials(self):
        r"""Gets the is_need_credentials of this DeleteNotebookResponse.

        **参数解释**：是否需要默认创建用户secret，默认为true。 **取值范围**：不涉及。

        :return: The is_need_credentials of this DeleteNotebookResponse.
        :rtype: bool
        """
        return self._is_need_credentials

    @is_need_credentials.setter
    def is_need_credentials(self, is_need_credentials):
        r"""Sets the is_need_credentials of this DeleteNotebookResponse.

        **参数解释**：是否需要默认创建用户secret，默认为true。 **取值范围**：不涉及。

        :param is_need_credentials: The is_need_credentials of this DeleteNotebookResponse.
        :type is_need_credentials: bool
        """
        self._is_need_credentials = is_need_credentials

    @property
    def jupyter_version(self):
        r"""Gets the jupyter_version of this DeleteNotebookResponse.

        **参数解释**：jupyter version版本号。 **取值范围**：不涉及。

        :return: The jupyter_version of this DeleteNotebookResponse.
        :rtype: str
        """
        return self._jupyter_version

    @jupyter_version.setter
    def jupyter_version(self, jupyter_version):
        r"""Sets the jupyter_version of this DeleteNotebookResponse.

        **参数解释**：jupyter version版本号。 **取值范围**：不涉及。

        :param jupyter_version: The jupyter_version of this DeleteNotebookResponse.
        :type jupyter_version: str
        """
        self._jupyter_version = jupyter_version

    @property
    def tags(self):
        r"""Gets the tags of this DeleteNotebookResponse.

        **参数解释**：实例标签。

        :return: The tags of this DeleteNotebookResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.TmsTagResponse`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this DeleteNotebookResponse.

        **参数解释**：实例标签。

        :param tags: The tags of this DeleteNotebookResponse.
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.TmsTagResponse`]
        """
        self._tags = tags

    def to_dict(self):
        import warnings
        warnings.warn("DeleteNotebookResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DeleteNotebookResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
