# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HraRuleCreateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scaler_type': 'str',
        'slo_info': 'list[SloInfo]',
        'metrics': 'list[Metrics]',
        'role_replica': 'list[RoleReplica]'
    }

    attribute_map = {
        'scaler_type': 'scaler_type',
        'slo_info': 'slo_info',
        'metrics': 'metrics',
        'role_replica': 'role_replica'
    }

    def __init__(self, scaler_type=None, slo_info=None, metrics=None, role_replica=None):
        r"""HraRuleCreateRequest

        The model defined in huaweicloud sdk

        :param scaler_type: **参数解释：** 扩缩容类型。 **取值范围：** - SIMULATOR_ALGO：模拟器算法扩缩容类型。 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type scaler_type: str
        :param slo_info: **参数解释：** SLO配置参数信息。 **取值范围：** 不涉及。
        :type slo_info: list[:class:`huaweicloudsdkmodelarts.v1.SloInfo`]
        :param metrics: **参数解释：** 指标信息。 **取值范围：** 不涉及。
        :type metrics: list[:class:`huaweicloudsdkmodelarts.v1.Metrics`]
        :param role_replica: **参数解释：** 角色扩缩策略（不会进行实质扩缩，因此该配置值无效）。 **取值范围：** 1~128。
        :type role_replica: list[:class:`huaweicloudsdkmodelarts.v1.RoleReplica`]
        """
        
        

        self._scaler_type = None
        self._slo_info = None
        self._metrics = None
        self._role_replica = None
        self.discriminator = None

        if scaler_type is not None:
            self.scaler_type = scaler_type
        self.slo_info = slo_info
        self.metrics = metrics
        if role_replica is not None:
            self.role_replica = role_replica

    @property
    def scaler_type(self):
        r"""Gets the scaler_type of this HraRuleCreateRequest.

        **参数解释：** 扩缩容类型。 **取值范围：** - SIMULATOR_ALGO：模拟器算法扩缩容类型。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The scaler_type of this HraRuleCreateRequest.
        :rtype: str
        """
        return self._scaler_type

    @scaler_type.setter
    def scaler_type(self, scaler_type):
        r"""Sets the scaler_type of this HraRuleCreateRequest.

        **参数解释：** 扩缩容类型。 **取值范围：** - SIMULATOR_ALGO：模拟器算法扩缩容类型。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param scaler_type: The scaler_type of this HraRuleCreateRequest.
        :type scaler_type: str
        """
        self._scaler_type = scaler_type

    @property
    def slo_info(self):
        r"""Gets the slo_info of this HraRuleCreateRequest.

        **参数解释：** SLO配置参数信息。 **取值范围：** 不涉及。

        :return: The slo_info of this HraRuleCreateRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.SloInfo`]
        """
        return self._slo_info

    @slo_info.setter
    def slo_info(self, slo_info):
        r"""Sets the slo_info of this HraRuleCreateRequest.

        **参数解释：** SLO配置参数信息。 **取值范围：** 不涉及。

        :param slo_info: The slo_info of this HraRuleCreateRequest.
        :type slo_info: list[:class:`huaweicloudsdkmodelarts.v1.SloInfo`]
        """
        self._slo_info = slo_info

    @property
    def metrics(self):
        r"""Gets the metrics of this HraRuleCreateRequest.

        **参数解释：** 指标信息。 **取值范围：** 不涉及。

        :return: The metrics of this HraRuleCreateRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Metrics`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this HraRuleCreateRequest.

        **参数解释：** 指标信息。 **取值范围：** 不涉及。

        :param metrics: The metrics of this HraRuleCreateRequest.
        :type metrics: list[:class:`huaweicloudsdkmodelarts.v1.Metrics`]
        """
        self._metrics = metrics

    @property
    def role_replica(self):
        r"""Gets the role_replica of this HraRuleCreateRequest.

        **参数解释：** 角色扩缩策略（不会进行实质扩缩，因此该配置值无效）。 **取值范围：** 1~128。

        :return: The role_replica of this HraRuleCreateRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.RoleReplica`]
        """
        return self._role_replica

    @role_replica.setter
    def role_replica(self, role_replica):
        r"""Sets the role_replica of this HraRuleCreateRequest.

        **参数解释：** 角色扩缩策略（不会进行实质扩缩，因此该配置值无效）。 **取值范围：** 1~128。

        :param role_replica: The role_replica of this HraRuleCreateRequest.
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
        if not isinstance(other, HraRuleCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
