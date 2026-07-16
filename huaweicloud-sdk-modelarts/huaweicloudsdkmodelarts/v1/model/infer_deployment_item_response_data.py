# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InferDeploymentItemResponseData:

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
        'infer_name': 'str',
        'service_group_name': 'str',
        'status': 'str',
        'lts_state': 'str',
        'mirror_traffic_enable': 'bool',
        'mirror_traffic_weight': 'str',
        'weight': 'int',
        'traffic_ratio': 'str',
        'pool_id': 'str',
        'version': 'str',
        'deploy_type': 'str',
        'create_at': 'int',
        'update_at': 'int',
        'frozen_infos': 'list[FrozenInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'infer_name': 'infer_name',
        'service_group_name': 'service_group_name',
        'status': 'status',
        'lts_state': 'lts_state',
        'mirror_traffic_enable': 'mirror_traffic_enable',
        'mirror_traffic_weight': 'mirror_traffic_weight',
        'weight': 'weight',
        'traffic_ratio': 'traffic_ratio',
        'pool_id': 'pool_id',
        'version': 'version',
        'deploy_type': 'deploy_type',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'frozen_infos': 'frozen_infos'
    }

    def __init__(self, id=None, name=None, infer_name=None, service_group_name=None, status=None, lts_state=None, mirror_traffic_enable=None, mirror_traffic_weight=None, weight=None, traffic_ratio=None, pool_id=None, version=None, deploy_type=None, create_at=None, update_at=None, frozen_infos=None):
        r"""InferDeploymentItemResponseData

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **取值范围：** 服务ID。
        :type id: str
        :param name: **参数解释：** 部署名，用户在[创建服务](CreateInferService.xml)时自定义。 **取值范围：** 支持1-128个字符，可以包含字母、汉字、数字、连字符和下划线。
        :type name: str
        :param infer_name: **参数解释：** 部署ID。 **取值范围：** 不涉及
        :type infer_name: str
        :param service_group_name: **参数解释：** 服务实例组id。 **取值范围：** 不涉及
        :type service_group_name: str
        :param status: **参数解释：** 服务当前状态，一次只支持一种状态筛选。默认不过滤。 **取值范围：** - DEPLOYING：部署中。 - FAILED：失败。 - STOPPED：停止。 - RUNNING：运行中。 - DELETING：删除中。 - STOPPING：停止中。 - CONCERNING：告警。 - DELETED：已删除。 - RESTARTING：重启中。 - UPGRADING：升级中。 - ERROR：异常。 - INTERRUPTING：中断中。
        :type status: str
        :param lts_state: **参数解释：** 部署对接lts状态。 **取值范围：** - ON：开启。 - OFF：关闭。
        :type lts_state: str
        :param mirror_traffic_enable: **参数解释：** 是否开启镜像流量。 **取值范围：** 不涉及
        :type mirror_traffic_enable: bool
        :param mirror_traffic_weight: **参数解释：** 镜像流量权重。 **取值范围：** 50。
        :type mirror_traffic_weight: str
        :param weight: **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **取值范围：** [0, 100]。
        :type weight: int
        :param traffic_ratio: **参数解释：** 流量比例，单个部署实例预期接收用户的流量与总流量比值，是由流量权重配置和部署状态计算所得的值。 **取值范围：** 0.00%~100.00%。
        :type traffic_ratio: str
        :param pool_id: **参数解释：** 专属资源池ID。 **取值范围：** 50。
        :type pool_id: str
        :param version: **参数解释：** 服务版本号，以数字及点号组成，形如1.0.1。 **取值范围：** 版本长度不超过8位。
        :type version: str
        :param deploy_type: **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。 - DIST：分布式部署。
        :type deploy_type: str
        :param create_at: **参数解释：** 创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字
        :type create_at: int
        :param update_at: **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。
        :type update_at: int
        :param frozen_infos: **参数解释：** 当服务或者部署被冻结时返回的冻结类型信息。
        :type frozen_infos: list[:class:`huaweicloudsdkmodelarts.v1.FrozenInfo`]
        """
        
        

        self._id = None
        self._name = None
        self._infer_name = None
        self._service_group_name = None
        self._status = None
        self._lts_state = None
        self._mirror_traffic_enable = None
        self._mirror_traffic_weight = None
        self._weight = None
        self._traffic_ratio = None
        self._pool_id = None
        self._version = None
        self._deploy_type = None
        self._create_at = None
        self._update_at = None
        self._frozen_infos = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if infer_name is not None:
            self.infer_name = infer_name
        if service_group_name is not None:
            self.service_group_name = service_group_name
        if status is not None:
            self.status = status
        if lts_state is not None:
            self.lts_state = lts_state
        if mirror_traffic_enable is not None:
            self.mirror_traffic_enable = mirror_traffic_enable
        if mirror_traffic_weight is not None:
            self.mirror_traffic_weight = mirror_traffic_weight
        if weight is not None:
            self.weight = weight
        if traffic_ratio is not None:
            self.traffic_ratio = traffic_ratio
        if pool_id is not None:
            self.pool_id = pool_id
        if version is not None:
            self.version = version
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if frozen_infos is not None:
            self.frozen_infos = frozen_infos

    @property
    def id(self):
        r"""Gets the id of this InferDeploymentItemResponseData.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **取值范围：** 服务ID。

        :return: The id of this InferDeploymentItemResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InferDeploymentItemResponseData.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **取值范围：** 服务ID。

        :param id: The id of this InferDeploymentItemResponseData.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this InferDeploymentItemResponseData.

        **参数解释：** 部署名，用户在[创建服务](CreateInferService.xml)时自定义。 **取值范围：** 支持1-128个字符，可以包含字母、汉字、数字、连字符和下划线。

        :return: The name of this InferDeploymentItemResponseData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InferDeploymentItemResponseData.

        **参数解释：** 部署名，用户在[创建服务](CreateInferService.xml)时自定义。 **取值范围：** 支持1-128个字符，可以包含字母、汉字、数字、连字符和下划线。

        :param name: The name of this InferDeploymentItemResponseData.
        :type name: str
        """
        self._name = name

    @property
    def infer_name(self):
        r"""Gets the infer_name of this InferDeploymentItemResponseData.

        **参数解释：** 部署ID。 **取值范围：** 不涉及

        :return: The infer_name of this InferDeploymentItemResponseData.
        :rtype: str
        """
        return self._infer_name

    @infer_name.setter
    def infer_name(self, infer_name):
        r"""Sets the infer_name of this InferDeploymentItemResponseData.

        **参数解释：** 部署ID。 **取值范围：** 不涉及

        :param infer_name: The infer_name of this InferDeploymentItemResponseData.
        :type infer_name: str
        """
        self._infer_name = infer_name

    @property
    def service_group_name(self):
        r"""Gets the service_group_name of this InferDeploymentItemResponseData.

        **参数解释：** 服务实例组id。 **取值范围：** 不涉及

        :return: The service_group_name of this InferDeploymentItemResponseData.
        :rtype: str
        """
        return self._service_group_name

    @service_group_name.setter
    def service_group_name(self, service_group_name):
        r"""Sets the service_group_name of this InferDeploymentItemResponseData.

        **参数解释：** 服务实例组id。 **取值范围：** 不涉及

        :param service_group_name: The service_group_name of this InferDeploymentItemResponseData.
        :type service_group_name: str
        """
        self._service_group_name = service_group_name

    @property
    def status(self):
        r"""Gets the status of this InferDeploymentItemResponseData.

        **参数解释：** 服务当前状态，一次只支持一种状态筛选。默认不过滤。 **取值范围：** - DEPLOYING：部署中。 - FAILED：失败。 - STOPPED：停止。 - RUNNING：运行中。 - DELETING：删除中。 - STOPPING：停止中。 - CONCERNING：告警。 - DELETED：已删除。 - RESTARTING：重启中。 - UPGRADING：升级中。 - ERROR：异常。 - INTERRUPTING：中断中。

        :return: The status of this InferDeploymentItemResponseData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InferDeploymentItemResponseData.

        **参数解释：** 服务当前状态，一次只支持一种状态筛选。默认不过滤。 **取值范围：** - DEPLOYING：部署中。 - FAILED：失败。 - STOPPED：停止。 - RUNNING：运行中。 - DELETING：删除中。 - STOPPING：停止中。 - CONCERNING：告警。 - DELETED：已删除。 - RESTARTING：重启中。 - UPGRADING：升级中。 - ERROR：异常。 - INTERRUPTING：中断中。

        :param status: The status of this InferDeploymentItemResponseData.
        :type status: str
        """
        self._status = status

    @property
    def lts_state(self):
        r"""Gets the lts_state of this InferDeploymentItemResponseData.

        **参数解释：** 部署对接lts状态。 **取值范围：** - ON：开启。 - OFF：关闭。

        :return: The lts_state of this InferDeploymentItemResponseData.
        :rtype: str
        """
        return self._lts_state

    @lts_state.setter
    def lts_state(self, lts_state):
        r"""Sets the lts_state of this InferDeploymentItemResponseData.

        **参数解释：** 部署对接lts状态。 **取值范围：** - ON：开启。 - OFF：关闭。

        :param lts_state: The lts_state of this InferDeploymentItemResponseData.
        :type lts_state: str
        """
        self._lts_state = lts_state

    @property
    def mirror_traffic_enable(self):
        r"""Gets the mirror_traffic_enable of this InferDeploymentItemResponseData.

        **参数解释：** 是否开启镜像流量。 **取值范围：** 不涉及

        :return: The mirror_traffic_enable of this InferDeploymentItemResponseData.
        :rtype: bool
        """
        return self._mirror_traffic_enable

    @mirror_traffic_enable.setter
    def mirror_traffic_enable(self, mirror_traffic_enable):
        r"""Sets the mirror_traffic_enable of this InferDeploymentItemResponseData.

        **参数解释：** 是否开启镜像流量。 **取值范围：** 不涉及

        :param mirror_traffic_enable: The mirror_traffic_enable of this InferDeploymentItemResponseData.
        :type mirror_traffic_enable: bool
        """
        self._mirror_traffic_enable = mirror_traffic_enable

    @property
    def mirror_traffic_weight(self):
        r"""Gets the mirror_traffic_weight of this InferDeploymentItemResponseData.

        **参数解释：** 镜像流量权重。 **取值范围：** 50。

        :return: The mirror_traffic_weight of this InferDeploymentItemResponseData.
        :rtype: str
        """
        return self._mirror_traffic_weight

    @mirror_traffic_weight.setter
    def mirror_traffic_weight(self, mirror_traffic_weight):
        r"""Sets the mirror_traffic_weight of this InferDeploymentItemResponseData.

        **参数解释：** 镜像流量权重。 **取值范围：** 50。

        :param mirror_traffic_weight: The mirror_traffic_weight of this InferDeploymentItemResponseData.
        :type mirror_traffic_weight: str
        """
        self._mirror_traffic_weight = mirror_traffic_weight

    @property
    def weight(self):
        r"""Gets the weight of this InferDeploymentItemResponseData.

        **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **取值范围：** [0, 100]。

        :return: The weight of this InferDeploymentItemResponseData.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this InferDeploymentItemResponseData.

        **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **取值范围：** [0, 100]。

        :param weight: The weight of this InferDeploymentItemResponseData.
        :type weight: int
        """
        self._weight = weight

    @property
    def traffic_ratio(self):
        r"""Gets the traffic_ratio of this InferDeploymentItemResponseData.

        **参数解释：** 流量比例，单个部署实例预期接收用户的流量与总流量比值，是由流量权重配置和部署状态计算所得的值。 **取值范围：** 0.00%~100.00%。

        :return: The traffic_ratio of this InferDeploymentItemResponseData.
        :rtype: str
        """
        return self._traffic_ratio

    @traffic_ratio.setter
    def traffic_ratio(self, traffic_ratio):
        r"""Sets the traffic_ratio of this InferDeploymentItemResponseData.

        **参数解释：** 流量比例，单个部署实例预期接收用户的流量与总流量比值，是由流量权重配置和部署状态计算所得的值。 **取值范围：** 0.00%~100.00%。

        :param traffic_ratio: The traffic_ratio of this InferDeploymentItemResponseData.
        :type traffic_ratio: str
        """
        self._traffic_ratio = traffic_ratio

    @property
    def pool_id(self):
        r"""Gets the pool_id of this InferDeploymentItemResponseData.

        **参数解释：** 专属资源池ID。 **取值范围：** 50。

        :return: The pool_id of this InferDeploymentItemResponseData.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this InferDeploymentItemResponseData.

        **参数解释：** 专属资源池ID。 **取值范围：** 50。

        :param pool_id: The pool_id of this InferDeploymentItemResponseData.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def version(self):
        r"""Gets the version of this InferDeploymentItemResponseData.

        **参数解释：** 服务版本号，以数字及点号组成，形如1.0.1。 **取值范围：** 版本长度不超过8位。

        :return: The version of this InferDeploymentItemResponseData.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this InferDeploymentItemResponseData.

        **参数解释：** 服务版本号，以数字及点号组成，形如1.0.1。 **取值范围：** 版本长度不超过8位。

        :param version: The version of this InferDeploymentItemResponseData.
        :type version: str
        """
        self._version = version

    @property
    def deploy_type(self):
        r"""Gets the deploy_type of this InferDeploymentItemResponseData.

        **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。 - DIST：分布式部署。

        :return: The deploy_type of this InferDeploymentItemResponseData.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        r"""Sets the deploy_type of this InferDeploymentItemResponseData.

        **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。 - DIST：分布式部署。

        :param deploy_type: The deploy_type of this InferDeploymentItemResponseData.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def create_at(self):
        r"""Gets the create_at of this InferDeploymentItemResponseData.

        **参数解释：** 创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字

        :return: The create_at of this InferDeploymentItemResponseData.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this InferDeploymentItemResponseData.

        **参数解释：** 创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字

        :param create_at: The create_at of this InferDeploymentItemResponseData.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this InferDeploymentItemResponseData.

        **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。

        :return: The update_at of this InferDeploymentItemResponseData.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this InferDeploymentItemResponseData.

        **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。

        :param update_at: The update_at of this InferDeploymentItemResponseData.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def frozen_infos(self):
        r"""Gets the frozen_infos of this InferDeploymentItemResponseData.

        **参数解释：** 当服务或者部署被冻结时返回的冻结类型信息。

        :return: The frozen_infos of this InferDeploymentItemResponseData.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.FrozenInfo`]
        """
        return self._frozen_infos

    @frozen_infos.setter
    def frozen_infos(self, frozen_infos):
        r"""Sets the frozen_infos of this InferDeploymentItemResponseData.

        **参数解释：** 当服务或者部署被冻结时返回的冻结类型信息。

        :param frozen_infos: The frozen_infos of this InferDeploymentItemResponseData.
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
        if not isinstance(other, InferDeploymentItemResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
