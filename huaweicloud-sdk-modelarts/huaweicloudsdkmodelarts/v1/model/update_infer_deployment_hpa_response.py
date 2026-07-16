# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInferDeploymentHpaResponse(SdkResponse):

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
        'target_resource_id': 'str',
        'target_resource_type': 'str',
        'min_replicas': 'int',
        'max_replicas': 'int',
        'status': 'str',
        'workspace_id': 'str',
        'hpa_rules': 'list[HpaRule]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'target_resource_id': 'target_resource_id',
        'target_resource_type': 'target_resource_type',
        'min_replicas': 'min_replicas',
        'max_replicas': 'max_replicas',
        'status': 'status',
        'workspace_id': 'workspace_id',
        'hpa_rules': 'hpa_rules'
    }

    def __init__(self, id=None, name=None, target_resource_id=None, target_resource_type=None, min_replicas=None, max_replicas=None, status=None, workspace_id=None, hpa_rules=None):
        r"""UpdateInferDeploymentHpaResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 自动扩缩容策略ID **取值范围：** 不涉及。
        :type id: str
        :param name: **参数解释：** 自动扩缩容策略名称 **取值范围：** 不涉及。
        :type name: str
        :param target_resource_id: **参数解释：** 自动扩缩容策略绑定的目标ID **取值范围：** 实例组ID
        :type target_resource_id: str
        :param target_resource_type: **参数解释：** 自动扩缩容策略绑定的目标类型。 **取值范围：** - GROUP：实例组
        :type target_resource_type: str
        :param min_replicas: **参数解释：** 自动扩缩容最小实例数。 **取值范围：** 1-128
        :type min_replicas: int
        :param max_replicas: **参数解释：** 自动扩缩容最大实例数。 **取值范围：** 1-128
        :type max_replicas: int
        :param status: 参数解释：** 自动扩缩容策略状态。 **取值范围：** - INACTIVE：不启用 - ACTIVE：配置成功 - DELETED：已删除
        :type status: str
        :param workspace_id: **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml)
        :type workspace_id: str
        :param hpa_rules: **参数解释：** 自动扩缩容规则列表
        :type hpa_rules: list[:class:`huaweicloudsdkmodelarts.v1.HpaRule`]
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._target_resource_id = None
        self._target_resource_type = None
        self._min_replicas = None
        self._max_replicas = None
        self._status = None
        self._workspace_id = None
        self._hpa_rules = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if target_resource_id is not None:
            self.target_resource_id = target_resource_id
        if target_resource_type is not None:
            self.target_resource_type = target_resource_type
        if min_replicas is not None:
            self.min_replicas = min_replicas
        if max_replicas is not None:
            self.max_replicas = max_replicas
        if status is not None:
            self.status = status
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if hpa_rules is not None:
            self.hpa_rules = hpa_rules

    @property
    def id(self):
        r"""Gets the id of this UpdateInferDeploymentHpaResponse.

        **参数解释：** 自动扩缩容策略ID **取值范围：** 不涉及。

        :return: The id of this UpdateInferDeploymentHpaResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateInferDeploymentHpaResponse.

        **参数解释：** 自动扩缩容策略ID **取值范围：** 不涉及。

        :param id: The id of this UpdateInferDeploymentHpaResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateInferDeploymentHpaResponse.

        **参数解释：** 自动扩缩容策略名称 **取值范围：** 不涉及。

        :return: The name of this UpdateInferDeploymentHpaResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateInferDeploymentHpaResponse.

        **参数解释：** 自动扩缩容策略名称 **取值范围：** 不涉及。

        :param name: The name of this UpdateInferDeploymentHpaResponse.
        :type name: str
        """
        self._name = name

    @property
    def target_resource_id(self):
        r"""Gets the target_resource_id of this UpdateInferDeploymentHpaResponse.

        **参数解释：** 自动扩缩容策略绑定的目标ID **取值范围：** 实例组ID

        :return: The target_resource_id of this UpdateInferDeploymentHpaResponse.
        :rtype: str
        """
        return self._target_resource_id

    @target_resource_id.setter
    def target_resource_id(self, target_resource_id):
        r"""Sets the target_resource_id of this UpdateInferDeploymentHpaResponse.

        **参数解释：** 自动扩缩容策略绑定的目标ID **取值范围：** 实例组ID

        :param target_resource_id: The target_resource_id of this UpdateInferDeploymentHpaResponse.
        :type target_resource_id: str
        """
        self._target_resource_id = target_resource_id

    @property
    def target_resource_type(self):
        r"""Gets the target_resource_type of this UpdateInferDeploymentHpaResponse.

        **参数解释：** 自动扩缩容策略绑定的目标类型。 **取值范围：** - GROUP：实例组

        :return: The target_resource_type of this UpdateInferDeploymentHpaResponse.
        :rtype: str
        """
        return self._target_resource_type

    @target_resource_type.setter
    def target_resource_type(self, target_resource_type):
        r"""Sets the target_resource_type of this UpdateInferDeploymentHpaResponse.

        **参数解释：** 自动扩缩容策略绑定的目标类型。 **取值范围：** - GROUP：实例组

        :param target_resource_type: The target_resource_type of this UpdateInferDeploymentHpaResponse.
        :type target_resource_type: str
        """
        self._target_resource_type = target_resource_type

    @property
    def min_replicas(self):
        r"""Gets the min_replicas of this UpdateInferDeploymentHpaResponse.

        **参数解释：** 自动扩缩容最小实例数。 **取值范围：** 1-128

        :return: The min_replicas of this UpdateInferDeploymentHpaResponse.
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        r"""Sets the min_replicas of this UpdateInferDeploymentHpaResponse.

        **参数解释：** 自动扩缩容最小实例数。 **取值范围：** 1-128

        :param min_replicas: The min_replicas of this UpdateInferDeploymentHpaResponse.
        :type min_replicas: int
        """
        self._min_replicas = min_replicas

    @property
    def max_replicas(self):
        r"""Gets the max_replicas of this UpdateInferDeploymentHpaResponse.

        **参数解释：** 自动扩缩容最大实例数。 **取值范围：** 1-128

        :return: The max_replicas of this UpdateInferDeploymentHpaResponse.
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        r"""Sets the max_replicas of this UpdateInferDeploymentHpaResponse.

        **参数解释：** 自动扩缩容最大实例数。 **取值范围：** 1-128

        :param max_replicas: The max_replicas of this UpdateInferDeploymentHpaResponse.
        :type max_replicas: int
        """
        self._max_replicas = max_replicas

    @property
    def status(self):
        r"""Gets the status of this UpdateInferDeploymentHpaResponse.

        参数解释：** 自动扩缩容策略状态。 **取值范围：** - INACTIVE：不启用 - ACTIVE：配置成功 - DELETED：已删除

        :return: The status of this UpdateInferDeploymentHpaResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateInferDeploymentHpaResponse.

        参数解释：** 自动扩缩容策略状态。 **取值范围：** - INACTIVE：不启用 - ACTIVE：配置成功 - DELETED：已删除

        :param status: The status of this UpdateInferDeploymentHpaResponse.
        :type status: str
        """
        self._status = status

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this UpdateInferDeploymentHpaResponse.

        **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml)

        :return: The workspace_id of this UpdateInferDeploymentHpaResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this UpdateInferDeploymentHpaResponse.

        **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml)

        :param workspace_id: The workspace_id of this UpdateInferDeploymentHpaResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def hpa_rules(self):
        r"""Gets the hpa_rules of this UpdateInferDeploymentHpaResponse.

        **参数解释：** 自动扩缩容规则列表

        :return: The hpa_rules of this UpdateInferDeploymentHpaResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.HpaRule`]
        """
        return self._hpa_rules

    @hpa_rules.setter
    def hpa_rules(self, hpa_rules):
        r"""Sets the hpa_rules of this UpdateInferDeploymentHpaResponse.

        **参数解释：** 自动扩缩容规则列表

        :param hpa_rules: The hpa_rules of this UpdateInferDeploymentHpaResponse.
        :type hpa_rules: list[:class:`huaweicloudsdkmodelarts.v1.HpaRule`]
        """
        self._hpa_rules = hpa_rules

    def to_dict(self):
        import warnings
        warnings.warn("UpdateInferDeploymentHpaResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateInferDeploymentHpaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
