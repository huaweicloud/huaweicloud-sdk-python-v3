# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnitConfigResponse:

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
        'role': 'str',
        'custom_spec': 'CustomResourceSpec',
        'flavor': 'str',
        'image': 'ImageInfoResponse',
        'models': 'list[InferModelResponse]',
        'files': 'list[FileResponse]',
        'codes': 'list[CodeResponse]',
        'dumps': 'list[DumpResponse]',
        'count': 'int',
        'group_count': 'int',
        'cmd': 'str',
        'envs': 'dict(str, str)',
        'readiness_health': 'HealthResponse',
        'startup_health': 'HealthResponse',
        'liveness_health': 'HealthResponse',
        'port': 'int',
        'recovery': 'str',
        'npu_reset_enable': 'bool',
        'affinity': 'AffinityResponse',
        'flavor_display_name': 'str',
        'termination_grace': 'TerminationGrace',
        'security_config': 'ServiceSecurityConfig',
        'pool_resource_flavor': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'role': 'role',
        'custom_spec': 'custom_spec',
        'flavor': 'flavor',
        'image': 'image',
        'models': 'models',
        'files': 'files',
        'codes': 'codes',
        'dumps': 'dumps',
        'count': 'count',
        'group_count': 'group_count',
        'cmd': 'cmd',
        'envs': 'envs',
        'readiness_health': 'readiness_health',
        'startup_health': 'startup_health',
        'liveness_health': 'liveness_health',
        'port': 'port',
        'recovery': 'recovery',
        'npu_reset_enable': 'npu_reset_enable',
        'affinity': 'affinity',
        'flavor_display_name': 'flavor_display_name',
        'termination_grace': 'termination_grace',
        'security_config': 'security_config',
        'pool_resource_flavor': 'pool_resource_flavor'
    }

    def __init__(self, id=None, name=None, role=None, custom_spec=None, flavor=None, image=None, models=None, files=None, codes=None, dumps=None, count=None, group_count=None, cmd=None, envs=None, readiness_health=None, startup_health=None, liveness_health=None, port=None, recovery=None, npu_reset_enable=None, affinity=None, flavor_display_name=None, termination_grace=None, security_config=None, pool_resource_flavor=None):
        r"""UnitConfigResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 实例单元ID。 **取值范围：** 不涉及。
        :type id: str
        :param name: **参数解释：** 实例单元名称。 **取值范围：** 不涉及。
        :type name: str
        :param role: **参数解释：** 实例单元角色。 **取值范围：** - COMMON：表示其他角色。
        :type role: str
        :param custom_spec: 
        :type custom_spec: :class:`huaweicloudsdkmodelarts.v1.CustomResourceSpec`
        :param flavor: **参数解释：** 资源规格，根据所提供版本选择适合业务的规格。当specification为custom时表示自定义规格。由custom_spec指定部署的规格配置。 **取值范围：** 不涉及。
        :type flavor: str
        :param image: 
        :type image: :class:`huaweicloudsdkmodelarts.v1.ImageInfoResponse`
        :param models: **参数解释：** 模型相关配置，用户可以在此处选择模型及权重文件配合镜像使用。
        :type models: list[:class:`huaweicloudsdkmodelarts.v1.InferModelResponse`]
        :param files: **参数解释：** 模型和代码相关配置，用户可以在此处选择模型及权重文件配合镜像使用以及代码所在的obs路径等。
        :type files: list[:class:`huaweicloudsdkmodelarts.v1.FileResponse`]
        :param codes: **参数解释：** 代码相关配置，用户可以在此处选择代码所在的obs路径等。
        :type codes: list[:class:`huaweicloudsdkmodelarts.v1.CodeResponse`]
        :param dumps: **参数解释：** 转储相关配置，用户可以在此处选择转储的目的obs路径等。
        :type dumps: list[:class:`huaweicloudsdkmodelarts.v1.DumpResponse`]
        :param count: **参数解释：** 配置实例个数。 **取值范围：** 不涉及。
        :type count: int
        :param group_count: **参数解释：** 单元副本数，当部署类型deploy_type为SINGLE或工作负载类型workload_type为DEPLOYMENT时，该参数无效。 **取值范围：** [1, 100] 或者为空。 **默认取值：** 默认值为1。
        :type group_count: int
        :param cmd: **参数解释：** 启动命令。 **取值范围：** 不涉及。
        :type cmd: str
        :param envs: **参数解释：** 环境变量。
        :type envs: dict(str, str)
        :param readiness_health: 
        :type readiness_health: :class:`huaweicloudsdkmodelarts.v1.HealthResponse`
        :param startup_health: 
        :type startup_health: :class:`huaweicloudsdkmodelarts.v1.HealthResponse`
        :param liveness_health: 
        :type liveness_health: :class:`huaweicloudsdkmodelarts.v1.HealthResponse`
        :param port: **参数解释：** 端口。 **取值范围：** [1,65535]。
        :type port: int
        :param recovery: **参数解释：** 自动重建策略，开启后，由于部署配置变更或者故障等原因导致Pod重启时，平台将按策略自动执行重建。若不开启，平台将不会主动干预处理。 **取值范围：** - Instance：部署副本重建，故障时重新拉起整个部署。 - Role：单元重建，当部署单元内的Pod出现故障时，重启该单元内的所有Pod。 - Pod：Pod重建，故障时重新拉起故障pod。
        :type recovery: str
        :param npu_reset_enable: **参数解释：** 是否开启恢复策略。 **取值范围：** - true：开启恢复策略。 - false：不开启恢复策略。
        :type npu_reset_enable: bool
        :param affinity: 
        :type affinity: :class:`huaweicloudsdkmodelarts.v1.AffinityResponse`
        :param flavor_display_name: **参数解释：** 规格展示名。仅使用切分规格部署的服务返回有此字段。 **取值范围：** 不涉及。
        :type flavor_display_name: str
        :param termination_grace: 
        :type termination_grace: :class:`huaweicloudsdkmodelarts.v1.TerminationGrace`
        :param security_config: 
        :type security_config: :class:`huaweicloudsdkmodelarts.v1.ServiceSecurityConfig`
        :param pool_resource_flavor: **参数解释：** 节点池资源规格。 **约束限制：** 只能包含字母、数字、点、中划线和下划线。 **取值范围：** 长度不超过128字符。 **默认取值：** 不涉及。
        :type pool_resource_flavor: str
        """
        
        

        self._id = None
        self._name = None
        self._role = None
        self._custom_spec = None
        self._flavor = None
        self._image = None
        self._models = None
        self._files = None
        self._codes = None
        self._dumps = None
        self._count = None
        self._group_count = None
        self._cmd = None
        self._envs = None
        self._readiness_health = None
        self._startup_health = None
        self._liveness_health = None
        self._port = None
        self._recovery = None
        self._npu_reset_enable = None
        self._affinity = None
        self._flavor_display_name = None
        self._termination_grace = None
        self._security_config = None
        self._pool_resource_flavor = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if role is not None:
            self.role = role
        if custom_spec is not None:
            self.custom_spec = custom_spec
        if flavor is not None:
            self.flavor = flavor
        self.image = image
        if models is not None:
            self.models = models
        if files is not None:
            self.files = files
        if codes is not None:
            self.codes = codes
        if dumps is not None:
            self.dumps = dumps
        if count is not None:
            self.count = count
        if group_count is not None:
            self.group_count = group_count
        if cmd is not None:
            self.cmd = cmd
        if envs is not None:
            self.envs = envs
        if readiness_health is not None:
            self.readiness_health = readiness_health
        if startup_health is not None:
            self.startup_health = startup_health
        if liveness_health is not None:
            self.liveness_health = liveness_health
        if port is not None:
            self.port = port
        if recovery is not None:
            self.recovery = recovery
        if npu_reset_enable is not None:
            self.npu_reset_enable = npu_reset_enable
        if affinity is not None:
            self.affinity = affinity
        if flavor_display_name is not None:
            self.flavor_display_name = flavor_display_name
        if termination_grace is not None:
            self.termination_grace = termination_grace
        if security_config is not None:
            self.security_config = security_config
        if pool_resource_flavor is not None:
            self.pool_resource_flavor = pool_resource_flavor

    @property
    def id(self):
        r"""Gets the id of this UnitConfigResponse.

        **参数解释：** 实例单元ID。 **取值范围：** 不涉及。

        :return: The id of this UnitConfigResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UnitConfigResponse.

        **参数解释：** 实例单元ID。 **取值范围：** 不涉及。

        :param id: The id of this UnitConfigResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UnitConfigResponse.

        **参数解释：** 实例单元名称。 **取值范围：** 不涉及。

        :return: The name of this UnitConfigResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UnitConfigResponse.

        **参数解释：** 实例单元名称。 **取值范围：** 不涉及。

        :param name: The name of this UnitConfigResponse.
        :type name: str
        """
        self._name = name

    @property
    def role(self):
        r"""Gets the role of this UnitConfigResponse.

        **参数解释：** 实例单元角色。 **取值范围：** - COMMON：表示其他角色。

        :return: The role of this UnitConfigResponse.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this UnitConfigResponse.

        **参数解释：** 实例单元角色。 **取值范围：** - COMMON：表示其他角色。

        :param role: The role of this UnitConfigResponse.
        :type role: str
        """
        self._role = role

    @property
    def custom_spec(self):
        r"""Gets the custom_spec of this UnitConfigResponse.

        :return: The custom_spec of this UnitConfigResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CustomResourceSpec`
        """
        return self._custom_spec

    @custom_spec.setter
    def custom_spec(self, custom_spec):
        r"""Sets the custom_spec of this UnitConfigResponse.

        :param custom_spec: The custom_spec of this UnitConfigResponse.
        :type custom_spec: :class:`huaweicloudsdkmodelarts.v1.CustomResourceSpec`
        """
        self._custom_spec = custom_spec

    @property
    def flavor(self):
        r"""Gets the flavor of this UnitConfigResponse.

        **参数解释：** 资源规格，根据所提供版本选择适合业务的规格。当specification为custom时表示自定义规格。由custom_spec指定部署的规格配置。 **取值范围：** 不涉及。

        :return: The flavor of this UnitConfigResponse.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this UnitConfigResponse.

        **参数解释：** 资源规格，根据所提供版本选择适合业务的规格。当specification为custom时表示自定义规格。由custom_spec指定部署的规格配置。 **取值范围：** 不涉及。

        :param flavor: The flavor of this UnitConfigResponse.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def image(self):
        r"""Gets the image of this UnitConfigResponse.

        :return: The image of this UnitConfigResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ImageInfoResponse`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this UnitConfigResponse.

        :param image: The image of this UnitConfigResponse.
        :type image: :class:`huaweicloudsdkmodelarts.v1.ImageInfoResponse`
        """
        self._image = image

    @property
    def models(self):
        r"""Gets the models of this UnitConfigResponse.

        **参数解释：** 模型相关配置，用户可以在此处选择模型及权重文件配合镜像使用。

        :return: The models of this UnitConfigResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.InferModelResponse`]
        """
        return self._models

    @models.setter
    def models(self, models):
        r"""Sets the models of this UnitConfigResponse.

        **参数解释：** 模型相关配置，用户可以在此处选择模型及权重文件配合镜像使用。

        :param models: The models of this UnitConfigResponse.
        :type models: list[:class:`huaweicloudsdkmodelarts.v1.InferModelResponse`]
        """
        self._models = models

    @property
    def files(self):
        r"""Gets the files of this UnitConfigResponse.

        **参数解释：** 模型和代码相关配置，用户可以在此处选择模型及权重文件配合镜像使用以及代码所在的obs路径等。

        :return: The files of this UnitConfigResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.FileResponse`]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this UnitConfigResponse.

        **参数解释：** 模型和代码相关配置，用户可以在此处选择模型及权重文件配合镜像使用以及代码所在的obs路径等。

        :param files: The files of this UnitConfigResponse.
        :type files: list[:class:`huaweicloudsdkmodelarts.v1.FileResponse`]
        """
        self._files = files

    @property
    def codes(self):
        r"""Gets the codes of this UnitConfigResponse.

        **参数解释：** 代码相关配置，用户可以在此处选择代码所在的obs路径等。

        :return: The codes of this UnitConfigResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.CodeResponse`]
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        r"""Sets the codes of this UnitConfigResponse.

        **参数解释：** 代码相关配置，用户可以在此处选择代码所在的obs路径等。

        :param codes: The codes of this UnitConfigResponse.
        :type codes: list[:class:`huaweicloudsdkmodelarts.v1.CodeResponse`]
        """
        self._codes = codes

    @property
    def dumps(self):
        r"""Gets the dumps of this UnitConfigResponse.

        **参数解释：** 转储相关配置，用户可以在此处选择转储的目的obs路径等。

        :return: The dumps of this UnitConfigResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.DumpResponse`]
        """
        return self._dumps

    @dumps.setter
    def dumps(self, dumps):
        r"""Sets the dumps of this UnitConfigResponse.

        **参数解释：** 转储相关配置，用户可以在此处选择转储的目的obs路径等。

        :param dumps: The dumps of this UnitConfigResponse.
        :type dumps: list[:class:`huaweicloudsdkmodelarts.v1.DumpResponse`]
        """
        self._dumps = dumps

    @property
    def count(self):
        r"""Gets the count of this UnitConfigResponse.

        **参数解释：** 配置实例个数。 **取值范围：** 不涉及。

        :return: The count of this UnitConfigResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this UnitConfigResponse.

        **参数解释：** 配置实例个数。 **取值范围：** 不涉及。

        :param count: The count of this UnitConfigResponse.
        :type count: int
        """
        self._count = count

    @property
    def group_count(self):
        r"""Gets the group_count of this UnitConfigResponse.

        **参数解释：** 单元副本数，当部署类型deploy_type为SINGLE或工作负载类型workload_type为DEPLOYMENT时，该参数无效。 **取值范围：** [1, 100] 或者为空。 **默认取值：** 默认值为1。

        :return: The group_count of this UnitConfigResponse.
        :rtype: int
        """
        return self._group_count

    @group_count.setter
    def group_count(self, group_count):
        r"""Sets the group_count of this UnitConfigResponse.

        **参数解释：** 单元副本数，当部署类型deploy_type为SINGLE或工作负载类型workload_type为DEPLOYMENT时，该参数无效。 **取值范围：** [1, 100] 或者为空。 **默认取值：** 默认值为1。

        :param group_count: The group_count of this UnitConfigResponse.
        :type group_count: int
        """
        self._group_count = group_count

    @property
    def cmd(self):
        r"""Gets the cmd of this UnitConfigResponse.

        **参数解释：** 启动命令。 **取值范围：** 不涉及。

        :return: The cmd of this UnitConfigResponse.
        :rtype: str
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        r"""Sets the cmd of this UnitConfigResponse.

        **参数解释：** 启动命令。 **取值范围：** 不涉及。

        :param cmd: The cmd of this UnitConfigResponse.
        :type cmd: str
        """
        self._cmd = cmd

    @property
    def envs(self):
        r"""Gets the envs of this UnitConfigResponse.

        **参数解释：** 环境变量。

        :return: The envs of this UnitConfigResponse.
        :rtype: dict(str, str)
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        r"""Sets the envs of this UnitConfigResponse.

        **参数解释：** 环境变量。

        :param envs: The envs of this UnitConfigResponse.
        :type envs: dict(str, str)
        """
        self._envs = envs

    @property
    def readiness_health(self):
        r"""Gets the readiness_health of this UnitConfigResponse.

        :return: The readiness_health of this UnitConfigResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.HealthResponse`
        """
        return self._readiness_health

    @readiness_health.setter
    def readiness_health(self, readiness_health):
        r"""Sets the readiness_health of this UnitConfigResponse.

        :param readiness_health: The readiness_health of this UnitConfigResponse.
        :type readiness_health: :class:`huaweicloudsdkmodelarts.v1.HealthResponse`
        """
        self._readiness_health = readiness_health

    @property
    def startup_health(self):
        r"""Gets the startup_health of this UnitConfigResponse.

        :return: The startup_health of this UnitConfigResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.HealthResponse`
        """
        return self._startup_health

    @startup_health.setter
    def startup_health(self, startup_health):
        r"""Sets the startup_health of this UnitConfigResponse.

        :param startup_health: The startup_health of this UnitConfigResponse.
        :type startup_health: :class:`huaweicloudsdkmodelarts.v1.HealthResponse`
        """
        self._startup_health = startup_health

    @property
    def liveness_health(self):
        r"""Gets the liveness_health of this UnitConfigResponse.

        :return: The liveness_health of this UnitConfigResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.HealthResponse`
        """
        return self._liveness_health

    @liveness_health.setter
    def liveness_health(self, liveness_health):
        r"""Sets the liveness_health of this UnitConfigResponse.

        :param liveness_health: The liveness_health of this UnitConfigResponse.
        :type liveness_health: :class:`huaweicloudsdkmodelarts.v1.HealthResponse`
        """
        self._liveness_health = liveness_health

    @property
    def port(self):
        r"""Gets the port of this UnitConfigResponse.

        **参数解释：** 端口。 **取值范围：** [1,65535]。

        :return: The port of this UnitConfigResponse.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this UnitConfigResponse.

        **参数解释：** 端口。 **取值范围：** [1,65535]。

        :param port: The port of this UnitConfigResponse.
        :type port: int
        """
        self._port = port

    @property
    def recovery(self):
        r"""Gets the recovery of this UnitConfigResponse.

        **参数解释：** 自动重建策略，开启后，由于部署配置变更或者故障等原因导致Pod重启时，平台将按策略自动执行重建。若不开启，平台将不会主动干预处理。 **取值范围：** - Instance：部署副本重建，故障时重新拉起整个部署。 - Role：单元重建，当部署单元内的Pod出现故障时，重启该单元内的所有Pod。 - Pod：Pod重建，故障时重新拉起故障pod。

        :return: The recovery of this UnitConfigResponse.
        :rtype: str
        """
        return self._recovery

    @recovery.setter
    def recovery(self, recovery):
        r"""Sets the recovery of this UnitConfigResponse.

        **参数解释：** 自动重建策略，开启后，由于部署配置变更或者故障等原因导致Pod重启时，平台将按策略自动执行重建。若不开启，平台将不会主动干预处理。 **取值范围：** - Instance：部署副本重建，故障时重新拉起整个部署。 - Role：单元重建，当部署单元内的Pod出现故障时，重启该单元内的所有Pod。 - Pod：Pod重建，故障时重新拉起故障pod。

        :param recovery: The recovery of this UnitConfigResponse.
        :type recovery: str
        """
        self._recovery = recovery

    @property
    def npu_reset_enable(self):
        r"""Gets the npu_reset_enable of this UnitConfigResponse.

        **参数解释：** 是否开启恢复策略。 **取值范围：** - true：开启恢复策略。 - false：不开启恢复策略。

        :return: The npu_reset_enable of this UnitConfigResponse.
        :rtype: bool
        """
        return self._npu_reset_enable

    @npu_reset_enable.setter
    def npu_reset_enable(self, npu_reset_enable):
        r"""Sets the npu_reset_enable of this UnitConfigResponse.

        **参数解释：** 是否开启恢复策略。 **取值范围：** - true：开启恢复策略。 - false：不开启恢复策略。

        :param npu_reset_enable: The npu_reset_enable of this UnitConfigResponse.
        :type npu_reset_enable: bool
        """
        self._npu_reset_enable = npu_reset_enable

    @property
    def affinity(self):
        r"""Gets the affinity of this UnitConfigResponse.

        :return: The affinity of this UnitConfigResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AffinityResponse`
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        r"""Sets the affinity of this UnitConfigResponse.

        :param affinity: The affinity of this UnitConfigResponse.
        :type affinity: :class:`huaweicloudsdkmodelarts.v1.AffinityResponse`
        """
        self._affinity = affinity

    @property
    def flavor_display_name(self):
        r"""Gets the flavor_display_name of this UnitConfigResponse.

        **参数解释：** 规格展示名。仅使用切分规格部署的服务返回有此字段。 **取值范围：** 不涉及。

        :return: The flavor_display_name of this UnitConfigResponse.
        :rtype: str
        """
        return self._flavor_display_name

    @flavor_display_name.setter
    def flavor_display_name(self, flavor_display_name):
        r"""Sets the flavor_display_name of this UnitConfigResponse.

        **参数解释：** 规格展示名。仅使用切分规格部署的服务返回有此字段。 **取值范围：** 不涉及。

        :param flavor_display_name: The flavor_display_name of this UnitConfigResponse.
        :type flavor_display_name: str
        """
        self._flavor_display_name = flavor_display_name

    @property
    def termination_grace(self):
        r"""Gets the termination_grace of this UnitConfigResponse.

        :return: The termination_grace of this UnitConfigResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.TerminationGrace`
        """
        return self._termination_grace

    @termination_grace.setter
    def termination_grace(self, termination_grace):
        r"""Sets the termination_grace of this UnitConfigResponse.

        :param termination_grace: The termination_grace of this UnitConfigResponse.
        :type termination_grace: :class:`huaweicloudsdkmodelarts.v1.TerminationGrace`
        """
        self._termination_grace = termination_grace

    @property
    def security_config(self):
        r"""Gets the security_config of this UnitConfigResponse.

        :return: The security_config of this UnitConfigResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServiceSecurityConfig`
        """
        return self._security_config

    @security_config.setter
    def security_config(self, security_config):
        r"""Sets the security_config of this UnitConfigResponse.

        :param security_config: The security_config of this UnitConfigResponse.
        :type security_config: :class:`huaweicloudsdkmodelarts.v1.ServiceSecurityConfig`
        """
        self._security_config = security_config

    @property
    def pool_resource_flavor(self):
        r"""Gets the pool_resource_flavor of this UnitConfigResponse.

        **参数解释：** 节点池资源规格。 **约束限制：** 只能包含字母、数字、点、中划线和下划线。 **取值范围：** 长度不超过128字符。 **默认取值：** 不涉及。

        :return: The pool_resource_flavor of this UnitConfigResponse.
        :rtype: str
        """
        return self._pool_resource_flavor

    @pool_resource_flavor.setter
    def pool_resource_flavor(self, pool_resource_flavor):
        r"""Sets the pool_resource_flavor of this UnitConfigResponse.

        **参数解释：** 节点池资源规格。 **约束限制：** 只能包含字母、数字、点、中划线和下划线。 **取值范围：** 长度不超过128字符。 **默认取值：** 不涉及。

        :param pool_resource_flavor: The pool_resource_flavor of this UnitConfigResponse.
        :type pool_resource_flavor: str
        """
        self._pool_resource_flavor = pool_resource_flavor

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
        if not isinstance(other, UnitConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
