# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHraRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'hra_rules': 'list[HraRuleCreateRequest]',
        'disable': 'bool',
        'min_replicas': 'int',
        'max_replicas': 'int',
        'scale_window': 'int'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'hra_rules': 'hra_rules',
        'disable': 'disable',
        'min_replicas': 'min_replicas',
        'max_replicas': 'max_replicas',
        'scale_window': 'scale_window'
    }

    def __init__(self, workspace_id=None, hra_rules=None, disable=None, min_replicas=None, max_replicas=None, scale_window=None):
        r"""CreateHraRequestBody

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释：** 工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围：** 不涉及。
        :type workspace_id: str
        :param hra_rules: **参数解释：** HRA规则列表。 **约束限制：** 不涉及。
        :type hra_rules: list[:class:`huaweicloudsdkmodelarts.v1.HraRuleCreateRequest`]
        :param disable: **参数解释：** 用户控制的启用/禁用开关。 **取值范围：** true表示禁用，false表示启用 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type disable: bool
        :param min_replicas: **参数解释：** 最小副本数，由于当前版本不会进行实质扩缩，因此该配置值无效。 **取值范围：** 1~128。
        :type min_replicas: int
        :param max_replicas: **参数解释：** 最大副本数，由于当前版本不会进行实质扩缩，因此该配置值无效。 **取值范围：** 1~128。
        :type max_replicas: int
        :param scale_window: **参数解释：** 扩缩容时间窗，由于当前版本不会进行实质扩缩，因此该配置值无效。 **取值范围：** 不涉及。
        :type scale_window: int
        """
        
        

        self._workspace_id = None
        self._hra_rules = None
        self._disable = None
        self._min_replicas = None
        self._max_replicas = None
        self._scale_window = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.hra_rules = hra_rules
        if disable is not None:
            self.disable = disable
        if min_replicas is not None:
            self.min_replicas = min_replicas
        if max_replicas is not None:
            self.max_replicas = max_replicas
        if scale_window is not None:
            self.scale_window = scale_window

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CreateHraRequestBody.

        **参数解释：** 工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围：** 不涉及。

        :return: The workspace_id of this CreateHraRequestBody.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CreateHraRequestBody.

        **参数解释：** 工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **取值范围：** 不涉及。

        :param workspace_id: The workspace_id of this CreateHraRequestBody.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def hra_rules(self):
        r"""Gets the hra_rules of this CreateHraRequestBody.

        **参数解释：** HRA规则列表。 **约束限制：** 不涉及。

        :return: The hra_rules of this CreateHraRequestBody.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.HraRuleCreateRequest`]
        """
        return self._hra_rules

    @hra_rules.setter
    def hra_rules(self, hra_rules):
        r"""Sets the hra_rules of this CreateHraRequestBody.

        **参数解释：** HRA规则列表。 **约束限制：** 不涉及。

        :param hra_rules: The hra_rules of this CreateHraRequestBody.
        :type hra_rules: list[:class:`huaweicloudsdkmodelarts.v1.HraRuleCreateRequest`]
        """
        self._hra_rules = hra_rules

    @property
    def disable(self):
        r"""Gets the disable of this CreateHraRequestBody.

        **参数解释：** 用户控制的启用/禁用开关。 **取值范围：** true表示禁用，false表示启用 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The disable of this CreateHraRequestBody.
        :rtype: bool
        """
        return self._disable

    @disable.setter
    def disable(self, disable):
        r"""Sets the disable of this CreateHraRequestBody.

        **参数解释：** 用户控制的启用/禁用开关。 **取值范围：** true表示禁用，false表示启用 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param disable: The disable of this CreateHraRequestBody.
        :type disable: bool
        """
        self._disable = disable

    @property
    def min_replicas(self):
        r"""Gets the min_replicas of this CreateHraRequestBody.

        **参数解释：** 最小副本数，由于当前版本不会进行实质扩缩，因此该配置值无效。 **取值范围：** 1~128。

        :return: The min_replicas of this CreateHraRequestBody.
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        r"""Sets the min_replicas of this CreateHraRequestBody.

        **参数解释：** 最小副本数，由于当前版本不会进行实质扩缩，因此该配置值无效。 **取值范围：** 1~128。

        :param min_replicas: The min_replicas of this CreateHraRequestBody.
        :type min_replicas: int
        """
        self._min_replicas = min_replicas

    @property
    def max_replicas(self):
        r"""Gets the max_replicas of this CreateHraRequestBody.

        **参数解释：** 最大副本数，由于当前版本不会进行实质扩缩，因此该配置值无效。 **取值范围：** 1~128。

        :return: The max_replicas of this CreateHraRequestBody.
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        r"""Sets the max_replicas of this CreateHraRequestBody.

        **参数解释：** 最大副本数，由于当前版本不会进行实质扩缩，因此该配置值无效。 **取值范围：** 1~128。

        :param max_replicas: The max_replicas of this CreateHraRequestBody.
        :type max_replicas: int
        """
        self._max_replicas = max_replicas

    @property
    def scale_window(self):
        r"""Gets the scale_window of this CreateHraRequestBody.

        **参数解释：** 扩缩容时间窗，由于当前版本不会进行实质扩缩，因此该配置值无效。 **取值范围：** 不涉及。

        :return: The scale_window of this CreateHraRequestBody.
        :rtype: int
        """
        return self._scale_window

    @scale_window.setter
    def scale_window(self, scale_window):
        r"""Sets the scale_window of this CreateHraRequestBody.

        **参数解释：** 扩缩容时间窗，由于当前版本不会进行实质扩缩，因此该配置值无效。 **取值范围：** 不涉及。

        :param scale_window: The scale_window of this CreateHraRequestBody.
        :type scale_window: int
        """
        self._scale_window = scale_window

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
        if not isinstance(other, CreateHraRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
