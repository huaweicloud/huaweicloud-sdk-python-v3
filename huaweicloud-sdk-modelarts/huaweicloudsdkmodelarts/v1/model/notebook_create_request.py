# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotebookCreateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'endpoints': 'list[EndpointsReq]',
        'feature': 'str',
        'flavor': 'str',
        'custom_spec': 'NotebookCustomSpec',
        'image_id': 'str',
        'name': 'str',
        'pool_id': 'str',
        'volume': 'VolumeMountRequest',
        'workspace_id': 'str',
        'hooks': 'CustomHooks',
        'lease': 'LeaseReq',
        'affinity': 'AffinityType',
        'run_user': 'RunUserRequest',
        'data_volumes': 'list[VolumeMountRequest]',
        'user_vpc': 'UserVpcRequest',
        'duration': 'int'
    }

    attribute_map = {
        'description': 'description',
        'endpoints': 'endpoints',
        'feature': 'feature',
        'flavor': 'flavor',
        'custom_spec': 'custom_spec',
        'image_id': 'image_id',
        'name': 'name',
        'pool_id': 'pool_id',
        'volume': 'volume',
        'workspace_id': 'workspace_id',
        'hooks': 'hooks',
        'lease': 'lease',
        'affinity': 'affinity',
        'run_user': 'run_user',
        'data_volumes': 'data_volumes',
        'user_vpc': 'user_vpc',
        'duration': 'duration'
    }

    def __init__(self, description=None, endpoints=None, feature=None, flavor=None, custom_spec=None, image_id=None, name=None, pool_id=None, volume=None, workspace_id=None, hooks=None, lease=None, affinity=None, run_user=None, data_volumes=None, user_vpc=None, duration=None):
        r"""NotebookCreateRequest

        The model defined in huaweicloud sdk

        :param description: **参数解释**：实例描述信息。 **约束限制**：不涉及。 **取值范围**：长度限制为512字符，且不能包含字符&amp;&lt;&gt;\&quot;&#39;/。 **默认取值**：不涉及。
        :type description: str
        :param endpoints: **参数解释**：仅在本地IDE（如PyCharm、VS Code）或SSH客户端接入Notebook。 **约束限制**：仅在本地IDE（如PyCharm、VS Code）或SSH客户端，通过SSH远程接入Notebook实例时需要的相关配置。
        :type endpoints: list[:class:`huaweicloudsdkmodelarts.v1.EndpointsReq`]
        :param feature: **参数解释**：实例类别。 **约束限制**：不涉及。 **取值范围**： - DEFAULT：CodeLab免费规格实例，每个用户最多只能创建一个。 - NOTEBOOK：计费规格实例。  **默认取值**：NOTEBOOK。
        :type feature: str
        :param flavor: **参数解释**：实例的机器规格。如下规格仅供参考，实际支持的规格以具体区域为准。 - modelarts.vm.cpu.2u：Intel CPU通用规格，用于快速数据探索和实验。 - modelarts.vm.cpu.8u：Intel CPU算力增强型，适用于密集计算场景下运算。  **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type flavor: str
        :param custom_spec: 
        :type custom_spec: :class:`huaweicloudsdkmodelarts.v1.NotebookCustomSpec`
        :param image_id: **参数解释**：待创建Notebook实例的镜像，需要指定镜像ID。ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID）。镜像的ID可通过调用[[查询支持的镜像列表](https://support.huaweicloud.com/api-modelarts/ListImage.html)](tag:hc)[[查询支持的镜像列表](https://support.huaweicloud.com/intl/zh-cn/api-modelarts/ListImage.html)](tag:hk)接口获取。 **约束限制**：不涉及。 **取值范围**：调用[[查询支持的镜像列表](https://support.huaweicloud.com/api-modelarts/ListImage.html)](tag:hc)[[查询支持的镜像列表](https://support.huaweicloud.com/intl/zh-cn/api-modelarts/ListImage.html)](tag:hk)接口获取的合法镜像ID列表。 **默认取值**：不涉及。
        :type image_id: str
        :param name: **参数解释**：实例名称。 **约束限制**：不涉及。 **取值范围**：长度限制为128个字符，支持大小写字母、数字、中划线和下划线，名称可重复。 **默认取值**：不涉及。
        :type name: str
        :param pool_id: **参数解释**：专属资源池ID，若需要指定专属资源池创建实例时必填。专属资源池ID可通过[[查询资源池列表](https://support.huaweicloud.com/api-modelarts/ListPools.html)](tag:hc)[[查询资源池列表](https://support.huaweicloud.com/intl/zh-cn/api-modelarts/ListPools.html)](tag:hk)接口获取。 **约束限制**：不涉及。 **取值范围**：调用[[查询资源池列表](https://support.huaweicloud.com/api-modelarts/ListPools.html)](tag:hc)[[查询资源池列表](https://support.huaweicloud.com/intl/zh-cn/api-modelarts/ListPools.html)](tag:hk)接口获取的合法资源池ID列表。 **默认取值**：不涉及。
        :type pool_id: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkmodelarts.v1.VolumeMountRequest`
        :param workspace_id: **参数解释**：工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：0或32位仅包含字符0-9或小写字母a-z的字符串。 **默认取值**：0。
        :type workspace_id: str
        :param hooks: 
        :type hooks: :class:`huaweicloudsdkmodelarts.v1.CustomHooks`
        :param lease: 
        :type lease: :class:`huaweicloudsdkmodelarts.v1.LeaseReq`
        :param affinity: 
        :type affinity: :class:`huaweicloudsdkmodelarts.v1.AffinityType`
        :param run_user: 
        :type run_user: :class:`huaweicloudsdkmodelarts.v1.RunUserRequest`
        :param data_volumes: **参数解释**：实例存储配置。 **约束限制**：不涉及。
        :type data_volumes: list[:class:`huaweicloudsdkmodelarts.v1.VolumeMountRequest`]
        :param user_vpc: 
        :type user_vpc: :class:`huaweicloudsdkmodelarts.v1.UserVpcRequest`
        :param duration: **参数解释**：定时停止，以当前时刻为起点，运行的时长（到期后自动停止）。单位：毫秒。 **约束限制**：不涉及。 **取值范围**：3600000-259200000。 **默认取值**：3600000。
        :type duration: int
        """
        
        

        self._description = None
        self._endpoints = None
        self._feature = None
        self._flavor = None
        self._custom_spec = None
        self._image_id = None
        self._name = None
        self._pool_id = None
        self._volume = None
        self._workspace_id = None
        self._hooks = None
        self._lease = None
        self._affinity = None
        self._run_user = None
        self._data_volumes = None
        self._user_vpc = None
        self._duration = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if endpoints is not None:
            self.endpoints = endpoints
        if feature is not None:
            self.feature = feature
        if flavor is not None:
            self.flavor = flavor
        if custom_spec is not None:
            self.custom_spec = custom_spec
        self.image_id = image_id
        self.name = name
        if pool_id is not None:
            self.pool_id = pool_id
        self.volume = volume
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if hooks is not None:
            self.hooks = hooks
        if lease is not None:
            self.lease = lease
        if affinity is not None:
            self.affinity = affinity
        if run_user is not None:
            self.run_user = run_user
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if user_vpc is not None:
            self.user_vpc = user_vpc
        if duration is not None:
            self.duration = duration

    @property
    def description(self):
        r"""Gets the description of this NotebookCreateRequest.

        **参数解释**：实例描述信息。 **约束限制**：不涉及。 **取值范围**：长度限制为512字符，且不能包含字符&<>\"'/。 **默认取值**：不涉及。

        :return: The description of this NotebookCreateRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this NotebookCreateRequest.

        **参数解释**：实例描述信息。 **约束限制**：不涉及。 **取值范围**：长度限制为512字符，且不能包含字符&<>\"'/。 **默认取值**：不涉及。

        :param description: The description of this NotebookCreateRequest.
        :type description: str
        """
        self._description = description

    @property
    def endpoints(self):
        r"""Gets the endpoints of this NotebookCreateRequest.

        **参数解释**：仅在本地IDE（如PyCharm、VS Code）或SSH客户端接入Notebook。 **约束限制**：仅在本地IDE（如PyCharm、VS Code）或SSH客户端，通过SSH远程接入Notebook实例时需要的相关配置。

        :return: The endpoints of this NotebookCreateRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.EndpointsReq`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this NotebookCreateRequest.

        **参数解释**：仅在本地IDE（如PyCharm、VS Code）或SSH客户端接入Notebook。 **约束限制**：仅在本地IDE（如PyCharm、VS Code）或SSH客户端，通过SSH远程接入Notebook实例时需要的相关配置。

        :param endpoints: The endpoints of this NotebookCreateRequest.
        :type endpoints: list[:class:`huaweicloudsdkmodelarts.v1.EndpointsReq`]
        """
        self._endpoints = endpoints

    @property
    def feature(self):
        r"""Gets the feature of this NotebookCreateRequest.

        **参数解释**：实例类别。 **约束限制**：不涉及。 **取值范围**： - DEFAULT：CodeLab免费规格实例，每个用户最多只能创建一个。 - NOTEBOOK：计费规格实例。  **默认取值**：NOTEBOOK。

        :return: The feature of this NotebookCreateRequest.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this NotebookCreateRequest.

        **参数解释**：实例类别。 **约束限制**：不涉及。 **取值范围**： - DEFAULT：CodeLab免费规格实例，每个用户最多只能创建一个。 - NOTEBOOK：计费规格实例。  **默认取值**：NOTEBOOK。

        :param feature: The feature of this NotebookCreateRequest.
        :type feature: str
        """
        self._feature = feature

    @property
    def flavor(self):
        r"""Gets the flavor of this NotebookCreateRequest.

        **参数解释**：实例的机器规格。如下规格仅供参考，实际支持的规格以具体区域为准。 - modelarts.vm.cpu.2u：Intel CPU通用规格，用于快速数据探索和实验。 - modelarts.vm.cpu.8u：Intel CPU算力增强型，适用于密集计算场景下运算。  **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The flavor of this NotebookCreateRequest.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this NotebookCreateRequest.

        **参数解释**：实例的机器规格。如下规格仅供参考，实际支持的规格以具体区域为准。 - modelarts.vm.cpu.2u：Intel CPU通用规格，用于快速数据探索和实验。 - modelarts.vm.cpu.8u：Intel CPU算力增强型，适用于密集计算场景下运算。  **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param flavor: The flavor of this NotebookCreateRequest.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def custom_spec(self):
        r"""Gets the custom_spec of this NotebookCreateRequest.

        :return: The custom_spec of this NotebookCreateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NotebookCustomSpec`
        """
        return self._custom_spec

    @custom_spec.setter
    def custom_spec(self, custom_spec):
        r"""Sets the custom_spec of this NotebookCreateRequest.

        :param custom_spec: The custom_spec of this NotebookCreateRequest.
        :type custom_spec: :class:`huaweicloudsdkmodelarts.v1.NotebookCustomSpec`
        """
        self._custom_spec = custom_spec

    @property
    def image_id(self):
        r"""Gets the image_id of this NotebookCreateRequest.

        **参数解释**：待创建Notebook实例的镜像，需要指定镜像ID。ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID）。镜像的ID可通过调用[[查询支持的镜像列表](https://support.huaweicloud.com/api-modelarts/ListImage.html)](tag:hc)[[查询支持的镜像列表](https://support.huaweicloud.com/intl/zh-cn/api-modelarts/ListImage.html)](tag:hk)接口获取。 **约束限制**：不涉及。 **取值范围**：调用[[查询支持的镜像列表](https://support.huaweicloud.com/api-modelarts/ListImage.html)](tag:hc)[[查询支持的镜像列表](https://support.huaweicloud.com/intl/zh-cn/api-modelarts/ListImage.html)](tag:hk)接口获取的合法镜像ID列表。 **默认取值**：不涉及。

        :return: The image_id of this NotebookCreateRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this NotebookCreateRequest.

        **参数解释**：待创建Notebook实例的镜像，需要指定镜像ID。ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID）。镜像的ID可通过调用[[查询支持的镜像列表](https://support.huaweicloud.com/api-modelarts/ListImage.html)](tag:hc)[[查询支持的镜像列表](https://support.huaweicloud.com/intl/zh-cn/api-modelarts/ListImage.html)](tag:hk)接口获取。 **约束限制**：不涉及。 **取值范围**：调用[[查询支持的镜像列表](https://support.huaweicloud.com/api-modelarts/ListImage.html)](tag:hc)[[查询支持的镜像列表](https://support.huaweicloud.com/intl/zh-cn/api-modelarts/ListImage.html)](tag:hk)接口获取的合法镜像ID列表。 **默认取值**：不涉及。

        :param image_id: The image_id of this NotebookCreateRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def name(self):
        r"""Gets the name of this NotebookCreateRequest.

        **参数解释**：实例名称。 **约束限制**：不涉及。 **取值范围**：长度限制为128个字符，支持大小写字母、数字、中划线和下划线，名称可重复。 **默认取值**：不涉及。

        :return: The name of this NotebookCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NotebookCreateRequest.

        **参数解释**：实例名称。 **约束限制**：不涉及。 **取值范围**：长度限制为128个字符，支持大小写字母、数字、中划线和下划线，名称可重复。 **默认取值**：不涉及。

        :param name: The name of this NotebookCreateRequest.
        :type name: str
        """
        self._name = name

    @property
    def pool_id(self):
        r"""Gets the pool_id of this NotebookCreateRequest.

        **参数解释**：专属资源池ID，若需要指定专属资源池创建实例时必填。专属资源池ID可通过[[查询资源池列表](https://support.huaweicloud.com/api-modelarts/ListPools.html)](tag:hc)[[查询资源池列表](https://support.huaweicloud.com/intl/zh-cn/api-modelarts/ListPools.html)](tag:hk)接口获取。 **约束限制**：不涉及。 **取值范围**：调用[[查询资源池列表](https://support.huaweicloud.com/api-modelarts/ListPools.html)](tag:hc)[[查询资源池列表](https://support.huaweicloud.com/intl/zh-cn/api-modelarts/ListPools.html)](tag:hk)接口获取的合法资源池ID列表。 **默认取值**：不涉及。

        :return: The pool_id of this NotebookCreateRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this NotebookCreateRequest.

        **参数解释**：专属资源池ID，若需要指定专属资源池创建实例时必填。专属资源池ID可通过[[查询资源池列表](https://support.huaweicloud.com/api-modelarts/ListPools.html)](tag:hc)[[查询资源池列表](https://support.huaweicloud.com/intl/zh-cn/api-modelarts/ListPools.html)](tag:hk)接口获取。 **约束限制**：不涉及。 **取值范围**：调用[[查询资源池列表](https://support.huaweicloud.com/api-modelarts/ListPools.html)](tag:hc)[[查询资源池列表](https://support.huaweicloud.com/intl/zh-cn/api-modelarts/ListPools.html)](tag:hk)接口获取的合法资源池ID列表。 **默认取值**：不涉及。

        :param pool_id: The pool_id of this NotebookCreateRequest.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def volume(self):
        r"""Gets the volume of this NotebookCreateRequest.

        :return: The volume of this NotebookCreateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.VolumeMountRequest`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this NotebookCreateRequest.

        :param volume: The volume of this NotebookCreateRequest.
        :type volume: :class:`huaweicloudsdkmodelarts.v1.VolumeMountRequest`
        """
        self._volume = volume

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this NotebookCreateRequest.

        **参数解释**：工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：0或32位仅包含字符0-9或小写字母a-z的字符串。 **默认取值**：0。

        :return: The workspace_id of this NotebookCreateRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this NotebookCreateRequest.

        **参数解释**：工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：0或32位仅包含字符0-9或小写字母a-z的字符串。 **默认取值**：0。

        :param workspace_id: The workspace_id of this NotebookCreateRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def hooks(self):
        r"""Gets the hooks of this NotebookCreateRequest.

        :return: The hooks of this NotebookCreateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CustomHooks`
        """
        return self._hooks

    @hooks.setter
    def hooks(self, hooks):
        r"""Sets the hooks of this NotebookCreateRequest.

        :param hooks: The hooks of this NotebookCreateRequest.
        :type hooks: :class:`huaweicloudsdkmodelarts.v1.CustomHooks`
        """
        self._hooks = hooks

    @property
    def lease(self):
        r"""Gets the lease of this NotebookCreateRequest.

        :return: The lease of this NotebookCreateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.LeaseReq`
        """
        return self._lease

    @lease.setter
    def lease(self, lease):
        r"""Sets the lease of this NotebookCreateRequest.

        :param lease: The lease of this NotebookCreateRequest.
        :type lease: :class:`huaweicloudsdkmodelarts.v1.LeaseReq`
        """
        self._lease = lease

    @property
    def affinity(self):
        r"""Gets the affinity of this NotebookCreateRequest.

        :return: The affinity of this NotebookCreateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AffinityType`
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        r"""Sets the affinity of this NotebookCreateRequest.

        :param affinity: The affinity of this NotebookCreateRequest.
        :type affinity: :class:`huaweicloudsdkmodelarts.v1.AffinityType`
        """
        self._affinity = affinity

    @property
    def run_user(self):
        r"""Gets the run_user of this NotebookCreateRequest.

        :return: The run_user of this NotebookCreateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.RunUserRequest`
        """
        return self._run_user

    @run_user.setter
    def run_user(self, run_user):
        r"""Sets the run_user of this NotebookCreateRequest.

        :param run_user: The run_user of this NotebookCreateRequest.
        :type run_user: :class:`huaweicloudsdkmodelarts.v1.RunUserRequest`
        """
        self._run_user = run_user

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this NotebookCreateRequest.

        **参数解释**：实例存储配置。 **约束限制**：不涉及。

        :return: The data_volumes of this NotebookCreateRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.VolumeMountRequest`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this NotebookCreateRequest.

        **参数解释**：实例存储配置。 **约束限制**：不涉及。

        :param data_volumes: The data_volumes of this NotebookCreateRequest.
        :type data_volumes: list[:class:`huaweicloudsdkmodelarts.v1.VolumeMountRequest`]
        """
        self._data_volumes = data_volumes

    @property
    def user_vpc(self):
        r"""Gets the user_vpc of this NotebookCreateRequest.

        :return: The user_vpc of this NotebookCreateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UserVpcRequest`
        """
        return self._user_vpc

    @user_vpc.setter
    def user_vpc(self, user_vpc):
        r"""Sets the user_vpc of this NotebookCreateRequest.

        :param user_vpc: The user_vpc of this NotebookCreateRequest.
        :type user_vpc: :class:`huaweicloudsdkmodelarts.v1.UserVpcRequest`
        """
        self._user_vpc = user_vpc

    @property
    def duration(self):
        r"""Gets the duration of this NotebookCreateRequest.

        **参数解释**：定时停止，以当前时刻为起点，运行的时长（到期后自动停止）。单位：毫秒。 **约束限制**：不涉及。 **取值范围**：3600000-259200000。 **默认取值**：3600000。

        :return: The duration of this NotebookCreateRequest.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this NotebookCreateRequest.

        **参数解释**：定时停止，以当前时刻为起点，运行的时长（到期后自动停止）。单位：毫秒。 **约束限制**：不涉及。 **取值范围**：3600000-259200000。 **默认取值**：3600000。

        :param duration: The duration of this NotebookCreateRequest.
        :type duration: int
        """
        self._duration = duration

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
        if not isinstance(other, NotebookCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
