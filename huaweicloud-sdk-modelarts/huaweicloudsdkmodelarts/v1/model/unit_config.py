# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnitConfig:

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
        'flavor_display_name': 'str',
        'image': 'ImageInfo',
        'models': 'list[ModelResource]',
        'codes': 'list[Code]',
        'files': 'list[FileInfo]',
        'dumps': 'list[Dump]',
        'count': 'int',
        'cmd': 'str',
        'termination_grace': 'TerminationGrace',
        'envs': 'dict(str, str)',
        'readiness_health': 'Health',
        'startup_health': 'Health',
        'liveness_health': 'Health',
        'port': 'int',
        'recovery': 'str',
        'npu_reset_enable': 'bool',
        'group_count': 'int',
        'affinity': 'Affinity',
        'security_config': 'ServiceSecurityConfig',
        'pool_resource_flavor': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'role': 'role',
        'custom_spec': 'custom_spec',
        'flavor': 'flavor',
        'flavor_display_name': 'flavor_display_name',
        'image': 'image',
        'models': 'models',
        'codes': 'codes',
        'files': 'files',
        'dumps': 'dumps',
        'count': 'count',
        'cmd': 'cmd',
        'termination_grace': 'termination_grace',
        'envs': 'envs',
        'readiness_health': 'readiness_health',
        'startup_health': 'startup_health',
        'liveness_health': 'liveness_health',
        'port': 'port',
        'recovery': 'recovery',
        'npu_reset_enable': 'npu_reset_enable',
        'group_count': 'group_count',
        'affinity': 'affinity',
        'security_config': 'security_config',
        'pool_resource_flavor': 'pool_resource_flavor'
    }

    def __init__(self, id=None, name=None, role=None, custom_spec=None, flavor=None, flavor_display_name=None, image=None, models=None, codes=None, files=None, dumps=None, count=None, cmd=None, termination_grace=None, envs=None, readiness_health=None, startup_health=None, liveness_health=None, port=None, recovery=None, npu_reset_enable=None, group_count=None, affinity=None, security_config=None, pool_resource_flavor=None):
        r"""UnitConfig

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 实例单元ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type id: str
        :param name: **参数解释：** 实例单元角色名称。 **约束限制：** 最大长度为16字符，且需满足正则：^\\[a-z0-9]([-a-z0-9]*[a-z0-9])?$ **默认取值：** 不涉及。
        :type name: str
        :param role: **参数解释：** 实例单元角色。 **约束限制：** 不涉及。 **取值范围：** - COMMON：表示其他角色。 **默认取值：** 不涉及。
        :type role: str
        :param custom_spec: 
        :type custom_spec: :class:`huaweicloudsdkmodelarts.v1.CustomResourceSpec`
        :param flavor: **参数解释：** 资源规格，根据所提供版本选择适合业务的规格。当specification为custom为自定义规格。由custom_spec指定部署的规格配置。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type flavor: str
        :param flavor_display_name: **参数解释：** 资源规格的显示名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type flavor_display_name: str
        :param image: 
        :type image: :class:`huaweicloudsdkmodelarts.v1.ImageInfo`
        :param models: **参数解释：** 废弃参数，推荐使用files进行模型相关配置。 模型相关配置，用户可以在此处选择模型及权重文件配合镜像使用。 **约束限制：** 不涉及。
        :type models: list[:class:`huaweicloudsdkmodelarts.v1.ModelResource`]
        :param codes: **参数解释：** 废弃参数，推荐使用files进行代码相关配置。 代码相关配置，用户可以在此处选择代码所在的obs路径等。 **约束限制：** 不涉及。
        :type codes: list[:class:`huaweicloudsdkmodelarts.v1.Code`]
        :param files: **参数解释：** 模型和代码相关配置，用户可以在此处选择模型及权重文件配合镜像使用以及代码所在的obs路径等。 **约束限制：** 不涉及。
        :type files: list[:class:`huaweicloudsdkmodelarts.v1.FileInfo`]
        :param dumps: **参数解释：** 用户转储配置，用户可以在此处选择要转储的目的obs。 **约束限制：** 最多配置20组。
        :type dumps: list[:class:`huaweicloudsdkmodelarts.v1.Dump`]
        :param count: **参数解释：** 配置实例个数。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type count: int
        :param cmd: **参数解释：** 启动命令。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type cmd: str
        :param termination_grace: 
        :type termination_grace: :class:`huaweicloudsdkmodelarts.v1.TerminationGrace`
        :param envs: **参数解释：** 环境变量。 **约束限制：** 变量键长度不大于64，由字母、数字、下划线、中划线、点组成，不能以数字开头。值的输入内容不能存在HTML标签，包括&lt;^&gt;。
        :type envs: dict(str, str)
        :param readiness_health: 
        :type readiness_health: :class:`huaweicloudsdkmodelarts.v1.Health`
        :param startup_health: 
        :type startup_health: :class:`huaweicloudsdkmodelarts.v1.Health`
        :param liveness_health: 
        :type liveness_health: :class:`huaweicloudsdkmodelarts.v1.Health`
        :param port: **参数解释：** 端口。 **约束限制：** 不涉及。 **取值范围：** [1,65535]。 **默认取值：** 不涉及。
        :type port: int
        :param recovery: **参数解释：** 自动重建策略，开启后，由于部署配置变更或者故障等原因导致Pod重启时，平台将按策略自动执行重建。若不开启，平台将不会主动干预处理。 **约束限制：** 不涉及。 **取值范围：** - Instance：部署副本重建，故障时重新拉起整个部署。 - Role：单元重建，当部署单元内的Pod出现故障时，重启该单元内的所有Pod。 - Pod：Pod重建，故障时重新拉起故障pod。 **默认取值：** 不涉及。
        :type recovery: str
        :param npu_reset_enable: **参数解释：** 是否开启恢复策略。 **约束限制：** 不涉及。 **取值范围：** - true：开启恢复策略。 - false：不开启恢复策略。 **默认取值：** 不涉及。
        :type npu_reset_enable: bool
        :param group_count: **参数解释：** 单元副本数，当部署类型deploy_type为SINGLE或工作负载类型workload_type为DEPLOYMENT时，该参数无效。 **约束限制：** 不涉及。 **取值范围：** [1, 100] 或者为空。 **默认取值：** 默认值为1。
        :type group_count: int
        :param affinity: 
        :type affinity: :class:`huaweicloudsdkmodelarts.v1.Affinity`
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
        self._flavor_display_name = None
        self._image = None
        self._models = None
        self._codes = None
        self._files = None
        self._dumps = None
        self._count = None
        self._cmd = None
        self._termination_grace = None
        self._envs = None
        self._readiness_health = None
        self._startup_health = None
        self._liveness_health = None
        self._port = None
        self._recovery = None
        self._npu_reset_enable = None
        self._group_count = None
        self._affinity = None
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
        if flavor_display_name is not None:
            self.flavor_display_name = flavor_display_name
        self.image = image
        if models is not None:
            self.models = models
        if codes is not None:
            self.codes = codes
        if files is not None:
            self.files = files
        if dumps is not None:
            self.dumps = dumps
        if count is not None:
            self.count = count
        if cmd is not None:
            self.cmd = cmd
        if termination_grace is not None:
            self.termination_grace = termination_grace
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
        if group_count is not None:
            self.group_count = group_count
        if affinity is not None:
            self.affinity = affinity
        if security_config is not None:
            self.security_config = security_config
        if pool_resource_flavor is not None:
            self.pool_resource_flavor = pool_resource_flavor

    @property
    def id(self):
        r"""Gets the id of this UnitConfig.

        **参数解释：** 实例单元ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The id of this UnitConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UnitConfig.

        **参数解释：** 实例单元ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param id: The id of this UnitConfig.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UnitConfig.

        **参数解释：** 实例单元角色名称。 **约束限制：** 最大长度为16字符，且需满足正则：^\\[a-z0-9]([-a-z0-9]*[a-z0-9])?$ **默认取值：** 不涉及。

        :return: The name of this UnitConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UnitConfig.

        **参数解释：** 实例单元角色名称。 **约束限制：** 最大长度为16字符，且需满足正则：^\\[a-z0-9]([-a-z0-9]*[a-z0-9])?$ **默认取值：** 不涉及。

        :param name: The name of this UnitConfig.
        :type name: str
        """
        self._name = name

    @property
    def role(self):
        r"""Gets the role of this UnitConfig.

        **参数解释：** 实例单元角色。 **约束限制：** 不涉及。 **取值范围：** - COMMON：表示其他角色。 **默认取值：** 不涉及。

        :return: The role of this UnitConfig.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this UnitConfig.

        **参数解释：** 实例单元角色。 **约束限制：** 不涉及。 **取值范围：** - COMMON：表示其他角色。 **默认取值：** 不涉及。

        :param role: The role of this UnitConfig.
        :type role: str
        """
        self._role = role

    @property
    def custom_spec(self):
        r"""Gets the custom_spec of this UnitConfig.

        :return: The custom_spec of this UnitConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CustomResourceSpec`
        """
        return self._custom_spec

    @custom_spec.setter
    def custom_spec(self, custom_spec):
        r"""Sets the custom_spec of this UnitConfig.

        :param custom_spec: The custom_spec of this UnitConfig.
        :type custom_spec: :class:`huaweicloudsdkmodelarts.v1.CustomResourceSpec`
        """
        self._custom_spec = custom_spec

    @property
    def flavor(self):
        r"""Gets the flavor of this UnitConfig.

        **参数解释：** 资源规格，根据所提供版本选择适合业务的规格。当specification为custom为自定义规格。由custom_spec指定部署的规格配置。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The flavor of this UnitConfig.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this UnitConfig.

        **参数解释：** 资源规格，根据所提供版本选择适合业务的规格。当specification为custom为自定义规格。由custom_spec指定部署的规格配置。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param flavor: The flavor of this UnitConfig.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def flavor_display_name(self):
        r"""Gets the flavor_display_name of this UnitConfig.

        **参数解释：** 资源规格的显示名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The flavor_display_name of this UnitConfig.
        :rtype: str
        """
        return self._flavor_display_name

    @flavor_display_name.setter
    def flavor_display_name(self, flavor_display_name):
        r"""Sets the flavor_display_name of this UnitConfig.

        **参数解释：** 资源规格的显示名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param flavor_display_name: The flavor_display_name of this UnitConfig.
        :type flavor_display_name: str
        """
        self._flavor_display_name = flavor_display_name

    @property
    def image(self):
        r"""Gets the image of this UnitConfig.

        :return: The image of this UnitConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ImageInfo`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this UnitConfig.

        :param image: The image of this UnitConfig.
        :type image: :class:`huaweicloudsdkmodelarts.v1.ImageInfo`
        """
        self._image = image

    @property
    def models(self):
        r"""Gets the models of this UnitConfig.

        **参数解释：** 废弃参数，推荐使用files进行模型相关配置。 模型相关配置，用户可以在此处选择模型及权重文件配合镜像使用。 **约束限制：** 不涉及。

        :return: The models of this UnitConfig.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ModelResource`]
        """
        return self._models

    @models.setter
    def models(self, models):
        r"""Sets the models of this UnitConfig.

        **参数解释：** 废弃参数，推荐使用files进行模型相关配置。 模型相关配置，用户可以在此处选择模型及权重文件配合镜像使用。 **约束限制：** 不涉及。

        :param models: The models of this UnitConfig.
        :type models: list[:class:`huaweicloudsdkmodelarts.v1.ModelResource`]
        """
        self._models = models

    @property
    def codes(self):
        r"""Gets the codes of this UnitConfig.

        **参数解释：** 废弃参数，推荐使用files进行代码相关配置。 代码相关配置，用户可以在此处选择代码所在的obs路径等。 **约束限制：** 不涉及。

        :return: The codes of this UnitConfig.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Code`]
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        r"""Sets the codes of this UnitConfig.

        **参数解释：** 废弃参数，推荐使用files进行代码相关配置。 代码相关配置，用户可以在此处选择代码所在的obs路径等。 **约束限制：** 不涉及。

        :param codes: The codes of this UnitConfig.
        :type codes: list[:class:`huaweicloudsdkmodelarts.v1.Code`]
        """
        self._codes = codes

    @property
    def files(self):
        r"""Gets the files of this UnitConfig.

        **参数解释：** 模型和代码相关配置，用户可以在此处选择模型及权重文件配合镜像使用以及代码所在的obs路径等。 **约束限制：** 不涉及。

        :return: The files of this UnitConfig.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.FileInfo`]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this UnitConfig.

        **参数解释：** 模型和代码相关配置，用户可以在此处选择模型及权重文件配合镜像使用以及代码所在的obs路径等。 **约束限制：** 不涉及。

        :param files: The files of this UnitConfig.
        :type files: list[:class:`huaweicloudsdkmodelarts.v1.FileInfo`]
        """
        self._files = files

    @property
    def dumps(self):
        r"""Gets the dumps of this UnitConfig.

        **参数解释：** 用户转储配置，用户可以在此处选择要转储的目的obs。 **约束限制：** 最多配置20组。

        :return: The dumps of this UnitConfig.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Dump`]
        """
        return self._dumps

    @dumps.setter
    def dumps(self, dumps):
        r"""Sets the dumps of this UnitConfig.

        **参数解释：** 用户转储配置，用户可以在此处选择要转储的目的obs。 **约束限制：** 最多配置20组。

        :param dumps: The dumps of this UnitConfig.
        :type dumps: list[:class:`huaweicloudsdkmodelarts.v1.Dump`]
        """
        self._dumps = dumps

    @property
    def count(self):
        r"""Gets the count of this UnitConfig.

        **参数解释：** 配置实例个数。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The count of this UnitConfig.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this UnitConfig.

        **参数解释：** 配置实例个数。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param count: The count of this UnitConfig.
        :type count: int
        """
        self._count = count

    @property
    def cmd(self):
        r"""Gets the cmd of this UnitConfig.

        **参数解释：** 启动命令。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The cmd of this UnitConfig.
        :rtype: str
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        r"""Sets the cmd of this UnitConfig.

        **参数解释：** 启动命令。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param cmd: The cmd of this UnitConfig.
        :type cmd: str
        """
        self._cmd = cmd

    @property
    def termination_grace(self):
        r"""Gets the termination_grace of this UnitConfig.

        :return: The termination_grace of this UnitConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.TerminationGrace`
        """
        return self._termination_grace

    @termination_grace.setter
    def termination_grace(self, termination_grace):
        r"""Sets the termination_grace of this UnitConfig.

        :param termination_grace: The termination_grace of this UnitConfig.
        :type termination_grace: :class:`huaweicloudsdkmodelarts.v1.TerminationGrace`
        """
        self._termination_grace = termination_grace

    @property
    def envs(self):
        r"""Gets the envs of this UnitConfig.

        **参数解释：** 环境变量。 **约束限制：** 变量键长度不大于64，由字母、数字、下划线、中划线、点组成，不能以数字开头。值的输入内容不能存在HTML标签，包括<^>。

        :return: The envs of this UnitConfig.
        :rtype: dict(str, str)
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        r"""Sets the envs of this UnitConfig.

        **参数解释：** 环境变量。 **约束限制：** 变量键长度不大于64，由字母、数字、下划线、中划线、点组成，不能以数字开头。值的输入内容不能存在HTML标签，包括<^>。

        :param envs: The envs of this UnitConfig.
        :type envs: dict(str, str)
        """
        self._envs = envs

    @property
    def readiness_health(self):
        r"""Gets the readiness_health of this UnitConfig.

        :return: The readiness_health of this UnitConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Health`
        """
        return self._readiness_health

    @readiness_health.setter
    def readiness_health(self, readiness_health):
        r"""Sets the readiness_health of this UnitConfig.

        :param readiness_health: The readiness_health of this UnitConfig.
        :type readiness_health: :class:`huaweicloudsdkmodelarts.v1.Health`
        """
        self._readiness_health = readiness_health

    @property
    def startup_health(self):
        r"""Gets the startup_health of this UnitConfig.

        :return: The startup_health of this UnitConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Health`
        """
        return self._startup_health

    @startup_health.setter
    def startup_health(self, startup_health):
        r"""Sets the startup_health of this UnitConfig.

        :param startup_health: The startup_health of this UnitConfig.
        :type startup_health: :class:`huaweicloudsdkmodelarts.v1.Health`
        """
        self._startup_health = startup_health

    @property
    def liveness_health(self):
        r"""Gets the liveness_health of this UnitConfig.

        :return: The liveness_health of this UnitConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Health`
        """
        return self._liveness_health

    @liveness_health.setter
    def liveness_health(self, liveness_health):
        r"""Sets the liveness_health of this UnitConfig.

        :param liveness_health: The liveness_health of this UnitConfig.
        :type liveness_health: :class:`huaweicloudsdkmodelarts.v1.Health`
        """
        self._liveness_health = liveness_health

    @property
    def port(self):
        r"""Gets the port of this UnitConfig.

        **参数解释：** 端口。 **约束限制：** 不涉及。 **取值范围：** [1,65535]。 **默认取值：** 不涉及。

        :return: The port of this UnitConfig.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this UnitConfig.

        **参数解释：** 端口。 **约束限制：** 不涉及。 **取值范围：** [1,65535]。 **默认取值：** 不涉及。

        :param port: The port of this UnitConfig.
        :type port: int
        """
        self._port = port

    @property
    def recovery(self):
        r"""Gets the recovery of this UnitConfig.

        **参数解释：** 自动重建策略，开启后，由于部署配置变更或者故障等原因导致Pod重启时，平台将按策略自动执行重建。若不开启，平台将不会主动干预处理。 **约束限制：** 不涉及。 **取值范围：** - Instance：部署副本重建，故障时重新拉起整个部署。 - Role：单元重建，当部署单元内的Pod出现故障时，重启该单元内的所有Pod。 - Pod：Pod重建，故障时重新拉起故障pod。 **默认取值：** 不涉及。

        :return: The recovery of this UnitConfig.
        :rtype: str
        """
        return self._recovery

    @recovery.setter
    def recovery(self, recovery):
        r"""Sets the recovery of this UnitConfig.

        **参数解释：** 自动重建策略，开启后，由于部署配置变更或者故障等原因导致Pod重启时，平台将按策略自动执行重建。若不开启，平台将不会主动干预处理。 **约束限制：** 不涉及。 **取值范围：** - Instance：部署副本重建，故障时重新拉起整个部署。 - Role：单元重建，当部署单元内的Pod出现故障时，重启该单元内的所有Pod。 - Pod：Pod重建，故障时重新拉起故障pod。 **默认取值：** 不涉及。

        :param recovery: The recovery of this UnitConfig.
        :type recovery: str
        """
        self._recovery = recovery

    @property
    def npu_reset_enable(self):
        r"""Gets the npu_reset_enable of this UnitConfig.

        **参数解释：** 是否开启恢复策略。 **约束限制：** 不涉及。 **取值范围：** - true：开启恢复策略。 - false：不开启恢复策略。 **默认取值：** 不涉及。

        :return: The npu_reset_enable of this UnitConfig.
        :rtype: bool
        """
        return self._npu_reset_enable

    @npu_reset_enable.setter
    def npu_reset_enable(self, npu_reset_enable):
        r"""Sets the npu_reset_enable of this UnitConfig.

        **参数解释：** 是否开启恢复策略。 **约束限制：** 不涉及。 **取值范围：** - true：开启恢复策略。 - false：不开启恢复策略。 **默认取值：** 不涉及。

        :param npu_reset_enable: The npu_reset_enable of this UnitConfig.
        :type npu_reset_enable: bool
        """
        self._npu_reset_enable = npu_reset_enable

    @property
    def group_count(self):
        r"""Gets the group_count of this UnitConfig.

        **参数解释：** 单元副本数，当部署类型deploy_type为SINGLE或工作负载类型workload_type为DEPLOYMENT时，该参数无效。 **约束限制：** 不涉及。 **取值范围：** [1, 100] 或者为空。 **默认取值：** 默认值为1。

        :return: The group_count of this UnitConfig.
        :rtype: int
        """
        return self._group_count

    @group_count.setter
    def group_count(self, group_count):
        r"""Sets the group_count of this UnitConfig.

        **参数解释：** 单元副本数，当部署类型deploy_type为SINGLE或工作负载类型workload_type为DEPLOYMENT时，该参数无效。 **约束限制：** 不涉及。 **取值范围：** [1, 100] 或者为空。 **默认取值：** 默认值为1。

        :param group_count: The group_count of this UnitConfig.
        :type group_count: int
        """
        self._group_count = group_count

    @property
    def affinity(self):
        r"""Gets the affinity of this UnitConfig.

        :return: The affinity of this UnitConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Affinity`
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        r"""Sets the affinity of this UnitConfig.

        :param affinity: The affinity of this UnitConfig.
        :type affinity: :class:`huaweicloudsdkmodelarts.v1.Affinity`
        """
        self._affinity = affinity

    @property
    def security_config(self):
        r"""Gets the security_config of this UnitConfig.

        :return: The security_config of this UnitConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServiceSecurityConfig`
        """
        return self._security_config

    @security_config.setter
    def security_config(self, security_config):
        r"""Sets the security_config of this UnitConfig.

        :param security_config: The security_config of this UnitConfig.
        :type security_config: :class:`huaweicloudsdkmodelarts.v1.ServiceSecurityConfig`
        """
        self._security_config = security_config

    @property
    def pool_resource_flavor(self):
        r"""Gets the pool_resource_flavor of this UnitConfig.

        **参数解释：** 节点池资源规格。 **约束限制：** 只能包含字母、数字、点、中划线和下划线。 **取值范围：** 长度不超过128字符。 **默认取值：** 不涉及。

        :return: The pool_resource_flavor of this UnitConfig.
        :rtype: str
        """
        return self._pool_resource_flavor

    @pool_resource_flavor.setter
    def pool_resource_flavor(self, pool_resource_flavor):
        r"""Sets the pool_resource_flavor of this UnitConfig.

        **参数解释：** 节点池资源规格。 **约束限制：** 只能包含字母、数字、点、中划线和下划线。 **取值范围：** 长度不超过128字符。 **默认取值：** 不涉及。

        :param pool_resource_flavor: The pool_resource_flavor of this UnitConfig.
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
        if not isinstance(other, UnitConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
