# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HraRuleResponse:

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
        'disable': 'bool',
        'scaler_type': 'str',
        'rule_status': 'str',
        'slo_info': 'list[SloInfo]',
        'metrics': 'list[Metrics]',
        'role_replica': 'list[RoleReplica]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'disable': 'disable',
        'scaler_type': 'scaler_type',
        'rule_status': 'rule_status',
        'slo_info': 'slo_info',
        'metrics': 'metrics',
        'role_replica': 'role_replica'
    }

    def __init__(self, id=None, name=None, disable=None, scaler_type=None, rule_status=None, slo_info=None, metrics=None, role_replica=None):
        r"""HraRuleResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 规则ID，在创建HRA策略时即可在返回体中获取，也可通过查询推理单元配比检测信息获取当前用户拥有的HRA策略，其中id字段即为规则ID。 **约束限制：** 不涉及。 **取值范围：** 规则ID。 **默认取值：** 不涉及。
        :type id: str
        :param name: **参数解释：** 规则名称。 **取值范围：** 不涉及。
        :type name: str
        :param disable: **参数解释：** 规则是否禁用。 **取值范围：** - true：禁用。 - false：不禁用。 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type disable: bool
        :param scaler_type: **参数解释：** 扩缩容类型。 **取值范围：** - SIMULATOR_ALGO：模拟器算法扩缩容类型。 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type scaler_type: str
        :param rule_status: **参数解释：** HRA规则状态。 **取值范围：** - CREATING：创建。 - CONFIG_SUCCESS：配置HRA策略成功。 - EXECUTE_SUCCESS：执行HRA策略成功。 - DELETED：删除。 - FAILED：失败。 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type rule_status: str
        :param slo_info: **参数解释：** SLO配置参数信息。 **取值范围：** 不涉及。
        :type slo_info: list[:class:`huaweicloudsdkmodelarts.v1.SloInfo`]
        :param metrics: **参数解释：** 指标信息。 **取值范围：** 不涉及。
        :type metrics: list[:class:`huaweicloudsdkmodelarts.v1.Metrics`]
        :param role_replica: **参数解释：** 角色扩缩策略（不会进行实质扩缩，因此该配置值无效）。
        :type role_replica: list[:class:`huaweicloudsdkmodelarts.v1.RoleReplica`]
        """
        
        

        self._id = None
        self._name = None
        self._disable = None
        self._scaler_type = None
        self._rule_status = None
        self._slo_info = None
        self._metrics = None
        self._role_replica = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if disable is not None:
            self.disable = disable
        if scaler_type is not None:
            self.scaler_type = scaler_type
        if rule_status is not None:
            self.rule_status = rule_status
        if slo_info is not None:
            self.slo_info = slo_info
        if metrics is not None:
            self.metrics = metrics
        if role_replica is not None:
            self.role_replica = role_replica

    @property
    def id(self):
        r"""Gets the id of this HraRuleResponse.

        **参数解释：** 规则ID，在创建HRA策略时即可在返回体中获取，也可通过查询推理单元配比检测信息获取当前用户拥有的HRA策略，其中id字段即为规则ID。 **约束限制：** 不涉及。 **取值范围：** 规则ID。 **默认取值：** 不涉及。

        :return: The id of this HraRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HraRuleResponse.

        **参数解释：** 规则ID，在创建HRA策略时即可在返回体中获取，也可通过查询推理单元配比检测信息获取当前用户拥有的HRA策略，其中id字段即为规则ID。 **约束限制：** 不涉及。 **取值范围：** 规则ID。 **默认取值：** 不涉及。

        :param id: The id of this HraRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this HraRuleResponse.

        **参数解释：** 规则名称。 **取值范围：** 不涉及。

        :return: The name of this HraRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HraRuleResponse.

        **参数解释：** 规则名称。 **取值范围：** 不涉及。

        :param name: The name of this HraRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def disable(self):
        r"""Gets the disable of this HraRuleResponse.

        **参数解释：** 规则是否禁用。 **取值范围：** - true：禁用。 - false：不禁用。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The disable of this HraRuleResponse.
        :rtype: bool
        """
        return self._disable

    @disable.setter
    def disable(self, disable):
        r"""Sets the disable of this HraRuleResponse.

        **参数解释：** 规则是否禁用。 **取值范围：** - true：禁用。 - false：不禁用。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param disable: The disable of this HraRuleResponse.
        :type disable: bool
        """
        self._disable = disable

    @property
    def scaler_type(self):
        r"""Gets the scaler_type of this HraRuleResponse.

        **参数解释：** 扩缩容类型。 **取值范围：** - SIMULATOR_ALGO：模拟器算法扩缩容类型。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The scaler_type of this HraRuleResponse.
        :rtype: str
        """
        return self._scaler_type

    @scaler_type.setter
    def scaler_type(self, scaler_type):
        r"""Sets the scaler_type of this HraRuleResponse.

        **参数解释：** 扩缩容类型。 **取值范围：** - SIMULATOR_ALGO：模拟器算法扩缩容类型。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param scaler_type: The scaler_type of this HraRuleResponse.
        :type scaler_type: str
        """
        self._scaler_type = scaler_type

    @property
    def rule_status(self):
        r"""Gets the rule_status of this HraRuleResponse.

        **参数解释：** HRA规则状态。 **取值范围：** - CREATING：创建。 - CONFIG_SUCCESS：配置HRA策略成功。 - EXECUTE_SUCCESS：执行HRA策略成功。 - DELETED：删除。 - FAILED：失败。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The rule_status of this HraRuleResponse.
        :rtype: str
        """
        return self._rule_status

    @rule_status.setter
    def rule_status(self, rule_status):
        r"""Sets the rule_status of this HraRuleResponse.

        **参数解释：** HRA规则状态。 **取值范围：** - CREATING：创建。 - CONFIG_SUCCESS：配置HRA策略成功。 - EXECUTE_SUCCESS：执行HRA策略成功。 - DELETED：删除。 - FAILED：失败。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param rule_status: The rule_status of this HraRuleResponse.
        :type rule_status: str
        """
        self._rule_status = rule_status

    @property
    def slo_info(self):
        r"""Gets the slo_info of this HraRuleResponse.

        **参数解释：** SLO配置参数信息。 **取值范围：** 不涉及。

        :return: The slo_info of this HraRuleResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.SloInfo`]
        """
        return self._slo_info

    @slo_info.setter
    def slo_info(self, slo_info):
        r"""Sets the slo_info of this HraRuleResponse.

        **参数解释：** SLO配置参数信息。 **取值范围：** 不涉及。

        :param slo_info: The slo_info of this HraRuleResponse.
        :type slo_info: list[:class:`huaweicloudsdkmodelarts.v1.SloInfo`]
        """
        self._slo_info = slo_info

    @property
    def metrics(self):
        r"""Gets the metrics of this HraRuleResponse.

        **参数解释：** 指标信息。 **取值范围：** 不涉及。

        :return: The metrics of this HraRuleResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Metrics`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this HraRuleResponse.

        **参数解释：** 指标信息。 **取值范围：** 不涉及。

        :param metrics: The metrics of this HraRuleResponse.
        :type metrics: list[:class:`huaweicloudsdkmodelarts.v1.Metrics`]
        """
        self._metrics = metrics

    @property
    def role_replica(self):
        r"""Gets the role_replica of this HraRuleResponse.

        **参数解释：** 角色扩缩策略（不会进行实质扩缩，因此该配置值无效）。

        :return: The role_replica of this HraRuleResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.RoleReplica`]
        """
        return self._role_replica

    @role_replica.setter
    def role_replica(self, role_replica):
        r"""Sets the role_replica of this HraRuleResponse.

        **参数解释：** 角色扩缩策略（不会进行实质扩缩，因此该配置值无效）。

        :param role_replica: The role_replica of this HraRuleResponse.
        :type role_replica: list[:class:`huaweicloudsdkmodelarts.v1.RoleReplica`]
        """
        self._role_replica = role_replica

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
        if not isinstance(other, HraRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
