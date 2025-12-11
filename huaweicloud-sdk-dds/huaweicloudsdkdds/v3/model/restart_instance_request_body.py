# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestartInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_type': 'str',
        'target_id': 'str',
        'is_serial': 'bool',
        'is_force': 'bool'
    }

    attribute_map = {
        'target_type': 'target_type',
        'target_id': 'target_id',
        'is_serial': 'is_serial',
        'is_force': 'is_force'
    }

    def __init__(self, target_type=None, target_id=None, is_serial=None, is_force=None):
        r"""RestartInstanceRequestBody

        The model defined in huaweicloud sdk

        :param target_type: **参数解释：** 待重启对象的类型。 **约束限制：** 重启集群实例下的节点或组时，该参数必选。 - 重启mongos节点时，取值为“mongos”。 - 重启shard组时，取值为“shard”。 - 重启config组时，取值为“config”。 - 重启实例（集群、副本集、单节点）时，不传该参数。 **取值范围：** - mongos - shard - config **默认取值：** 不涉及。
        :type target_type: str
        :param target_id: **参数解释：** 待重启对象的ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 **约束限制：** 节点状态为正常时，不允许重启主节点。 **取值范围：** - 重启整个实例时，取值为实例ID。 - 重启集群实例shard或config组时取值为shard或config的组ID。 - 重启单个节点时，取值为对应节点的节点ID。 **默认取值：** 不涉及。
        :type target_id: str
        :param is_serial: **参数解释：** 是否选择节点串行重启。 **约束限制：** 只支持副本集实例。 **取值范围：** - true：表示节点串行重启。 - false：表示节点并行重启。 **默认取值：** false。
        :type is_serial: bool
        :param is_force: **参数解释：** 是否强制重启。 **约束限制：** 仅支持节点状态为异常时进行强制重启。只读节点暂不支持强制重启。 **取值范围：** - true：表示异常节点进行强制重启。 - false：表示进行正常重启。 **默认取值：** false。
        :type is_force: bool
        """
        
        

        self._target_type = None
        self._target_id = None
        self._is_serial = None
        self._is_force = None
        self.discriminator = None

        if target_type is not None:
            self.target_type = target_type
        self.target_id = target_id
        if is_serial is not None:
            self.is_serial = is_serial
        if is_force is not None:
            self.is_force = is_force

    @property
    def target_type(self):
        r"""Gets the target_type of this RestartInstanceRequestBody.

        **参数解释：** 待重启对象的类型。 **约束限制：** 重启集群实例下的节点或组时，该参数必选。 - 重启mongos节点时，取值为“mongos”。 - 重启shard组时，取值为“shard”。 - 重启config组时，取值为“config”。 - 重启实例（集群、副本集、单节点）时，不传该参数。 **取值范围：** - mongos - shard - config **默认取值：** 不涉及。

        :return: The target_type of this RestartInstanceRequestBody.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this RestartInstanceRequestBody.

        **参数解释：** 待重启对象的类型。 **约束限制：** 重启集群实例下的节点或组时，该参数必选。 - 重启mongos节点时，取值为“mongos”。 - 重启shard组时，取值为“shard”。 - 重启config组时，取值为“config”。 - 重启实例（集群、副本集、单节点）时，不传该参数。 **取值范围：** - mongos - shard - config **默认取值：** 不涉及。

        :param target_type: The target_type of this RestartInstanceRequestBody.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def target_id(self):
        r"""Gets the target_id of this RestartInstanceRequestBody.

        **参数解释：** 待重启对象的ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 **约束限制：** 节点状态为正常时，不允许重启主节点。 **取值范围：** - 重启整个实例时，取值为实例ID。 - 重启集群实例shard或config组时取值为shard或config的组ID。 - 重启单个节点时，取值为对应节点的节点ID。 **默认取值：** 不涉及。

        :return: The target_id of this RestartInstanceRequestBody.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this RestartInstanceRequestBody.

        **参数解释：** 待重启对象的ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 **约束限制：** 节点状态为正常时，不允许重启主节点。 **取值范围：** - 重启整个实例时，取值为实例ID。 - 重启集群实例shard或config组时取值为shard或config的组ID。 - 重启单个节点时，取值为对应节点的节点ID。 **默认取值：** 不涉及。

        :param target_id: The target_id of this RestartInstanceRequestBody.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def is_serial(self):
        r"""Gets the is_serial of this RestartInstanceRequestBody.

        **参数解释：** 是否选择节点串行重启。 **约束限制：** 只支持副本集实例。 **取值范围：** - true：表示节点串行重启。 - false：表示节点并行重启。 **默认取值：** false。

        :return: The is_serial of this RestartInstanceRequestBody.
        :rtype: bool
        """
        return self._is_serial

    @is_serial.setter
    def is_serial(self, is_serial):
        r"""Sets the is_serial of this RestartInstanceRequestBody.

        **参数解释：** 是否选择节点串行重启。 **约束限制：** 只支持副本集实例。 **取值范围：** - true：表示节点串行重启。 - false：表示节点并行重启。 **默认取值：** false。

        :param is_serial: The is_serial of this RestartInstanceRequestBody.
        :type is_serial: bool
        """
        self._is_serial = is_serial

    @property
    def is_force(self):
        r"""Gets the is_force of this RestartInstanceRequestBody.

        **参数解释：** 是否强制重启。 **约束限制：** 仅支持节点状态为异常时进行强制重启。只读节点暂不支持强制重启。 **取值范围：** - true：表示异常节点进行强制重启。 - false：表示进行正常重启。 **默认取值：** false。

        :return: The is_force of this RestartInstanceRequestBody.
        :rtype: bool
        """
        return self._is_force

    @is_force.setter
    def is_force(self, is_force):
        r"""Sets the is_force of this RestartInstanceRequestBody.

        **参数解释：** 是否强制重启。 **约束限制：** 仅支持节点状态为异常时进行强制重启。只读节点暂不支持强制重启。 **取值范围：** - true：表示异常节点进行强制重启。 - false：表示进行正常重启。 **默认取值：** false。

        :param is_force: The is_force of this RestartInstanceRequestBody.
        :type is_force: bool
        """
        self._is_force = is_force

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
        if not isinstance(other, RestartInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
