# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolMetadataUpdateAnnotations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_modelarts_description': 'str',
        'os_modelarts_order_id': 'str',
        'os_modelarts_pool_scheduler_queue_strategy': 'str',
        'os_modelarts_pool_scheduler_queue_strategy_config': 'str'
    }

    attribute_map = {
        'os_modelarts_description': 'os.modelarts/description',
        'os_modelarts_order_id': 'os.modelarts/order.id',
        'os_modelarts_pool_scheduler_queue_strategy': 'os.modelarts.pool/scheduler.queue.strategy',
        'os_modelarts_pool_scheduler_queue_strategy_config': 'os.modelarts.pool/scheduler.queue.strategy.config'
    }

    def __init__(self, os_modelarts_description=None, os_modelarts_order_id=None, os_modelarts_pool_scheduler_queue_strategy=None, os_modelarts_pool_scheduler_queue_strategy_config=None):
        r"""PoolMetadataUpdateAnnotations

        The model defined in huaweicloud sdk

        :param os_modelarts_description: **参数解释**：资源池描述信息，用于说明资源池用于某种指定场景。不能包含特殊字符!&lt;&gt;&#x3D;&amp;\&quot;&#39;。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_description: str
        :param os_modelarts_order_id: **参数解释**：订单id，包周期创建和变更的时候需要传递该参数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_order_id: str
        :param os_modelarts_pool_scheduler_queue_strategy: **参数解释**：资源池的调度算法。 **约束限制**：不涉及。 **取值范围**：可选值如下： - FIFO：先进先出，默认值 - Range：遍历调度 - Step: 阶梯轮询 - Rank: 分级调度 **默认取值**：FIFO。
        :type os_modelarts_pool_scheduler_queue_strategy: str
        :param os_modelarts_pool_scheduler_queue_strategy_config: **参数解释**：资源池的调度策略配置。 **约束限制**：仅当调度策略为Step或Rank时生效。 **取值范围**：Json字符串，自行配置，示例如下： - Step: {\&quot;step_config\&quot;:{\&quot;timeout\&quot;:300}} - Rank: {\&quot;rank_config\&quot;:[{\&quot;max_priority\&quot;:3,\&quot;min_priority\&quot;:3,\&quot;rank_strategy\&quot;:\&quot;Step\&quot;,\&quot;step_config\&quot;:{\&quot;timeout\&quot;:300}},{\&quot;max_priority\&quot;:2,\&quot;min_priority\&quot;:1,\&quot;rank_strategy\&quot;:\&quot;Range\&quot;}]} **默认取值**：不涉及。
        :type os_modelarts_pool_scheduler_queue_strategy_config: str
        """
        
        

        self._os_modelarts_description = None
        self._os_modelarts_order_id = None
        self._os_modelarts_pool_scheduler_queue_strategy = None
        self._os_modelarts_pool_scheduler_queue_strategy_config = None
        self.discriminator = None

        if os_modelarts_description is not None:
            self.os_modelarts_description = os_modelarts_description
        if os_modelarts_order_id is not None:
            self.os_modelarts_order_id = os_modelarts_order_id
        if os_modelarts_pool_scheduler_queue_strategy is not None:
            self.os_modelarts_pool_scheduler_queue_strategy = os_modelarts_pool_scheduler_queue_strategy
        if os_modelarts_pool_scheduler_queue_strategy_config is not None:
            self.os_modelarts_pool_scheduler_queue_strategy_config = os_modelarts_pool_scheduler_queue_strategy_config

    @property
    def os_modelarts_description(self):
        r"""Gets the os_modelarts_description of this PoolMetadataUpdateAnnotations.

        **参数解释**：资源池描述信息，用于说明资源池用于某种指定场景。不能包含特殊字符!<>=&\"'。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_description of this PoolMetadataUpdateAnnotations.
        :rtype: str
        """
        return self._os_modelarts_description

    @os_modelarts_description.setter
    def os_modelarts_description(self, os_modelarts_description):
        r"""Sets the os_modelarts_description of this PoolMetadataUpdateAnnotations.

        **参数解释**：资源池描述信息，用于说明资源池用于某种指定场景。不能包含特殊字符!<>=&\"'。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_description: The os_modelarts_description of this PoolMetadataUpdateAnnotations.
        :type os_modelarts_description: str
        """
        self._os_modelarts_description = os_modelarts_description

    @property
    def os_modelarts_order_id(self):
        r"""Gets the os_modelarts_order_id of this PoolMetadataUpdateAnnotations.

        **参数解释**：订单id，包周期创建和变更的时候需要传递该参数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_order_id of this PoolMetadataUpdateAnnotations.
        :rtype: str
        """
        return self._os_modelarts_order_id

    @os_modelarts_order_id.setter
    def os_modelarts_order_id(self, os_modelarts_order_id):
        r"""Sets the os_modelarts_order_id of this PoolMetadataUpdateAnnotations.

        **参数解释**：订单id，包周期创建和变更的时候需要传递该参数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_order_id: The os_modelarts_order_id of this PoolMetadataUpdateAnnotations.
        :type os_modelarts_order_id: str
        """
        self._os_modelarts_order_id = os_modelarts_order_id

    @property
    def os_modelarts_pool_scheduler_queue_strategy(self):
        r"""Gets the os_modelarts_pool_scheduler_queue_strategy of this PoolMetadataUpdateAnnotations.

        **参数解释**：资源池的调度算法。 **约束限制**：不涉及。 **取值范围**：可选值如下： - FIFO：先进先出，默认值 - Range：遍历调度 - Step: 阶梯轮询 - Rank: 分级调度 **默认取值**：FIFO。

        :return: The os_modelarts_pool_scheduler_queue_strategy of this PoolMetadataUpdateAnnotations.
        :rtype: str
        """
        return self._os_modelarts_pool_scheduler_queue_strategy

    @os_modelarts_pool_scheduler_queue_strategy.setter
    def os_modelarts_pool_scheduler_queue_strategy(self, os_modelarts_pool_scheduler_queue_strategy):
        r"""Sets the os_modelarts_pool_scheduler_queue_strategy of this PoolMetadataUpdateAnnotations.

        **参数解释**：资源池的调度算法。 **约束限制**：不涉及。 **取值范围**：可选值如下： - FIFO：先进先出，默认值 - Range：遍历调度 - Step: 阶梯轮询 - Rank: 分级调度 **默认取值**：FIFO。

        :param os_modelarts_pool_scheduler_queue_strategy: The os_modelarts_pool_scheduler_queue_strategy of this PoolMetadataUpdateAnnotations.
        :type os_modelarts_pool_scheduler_queue_strategy: str
        """
        self._os_modelarts_pool_scheduler_queue_strategy = os_modelarts_pool_scheduler_queue_strategy

    @property
    def os_modelarts_pool_scheduler_queue_strategy_config(self):
        r"""Gets the os_modelarts_pool_scheduler_queue_strategy_config of this PoolMetadataUpdateAnnotations.

        **参数解释**：资源池的调度策略配置。 **约束限制**：仅当调度策略为Step或Rank时生效。 **取值范围**：Json字符串，自行配置，示例如下： - Step: {\"step_config\":{\"timeout\":300}} - Rank: {\"rank_config\":[{\"max_priority\":3,\"min_priority\":3,\"rank_strategy\":\"Step\",\"step_config\":{\"timeout\":300}},{\"max_priority\":2,\"min_priority\":1,\"rank_strategy\":\"Range\"}]} **默认取值**：不涉及。

        :return: The os_modelarts_pool_scheduler_queue_strategy_config of this PoolMetadataUpdateAnnotations.
        :rtype: str
        """
        return self._os_modelarts_pool_scheduler_queue_strategy_config

    @os_modelarts_pool_scheduler_queue_strategy_config.setter
    def os_modelarts_pool_scheduler_queue_strategy_config(self, os_modelarts_pool_scheduler_queue_strategy_config):
        r"""Sets the os_modelarts_pool_scheduler_queue_strategy_config of this PoolMetadataUpdateAnnotations.

        **参数解释**：资源池的调度策略配置。 **约束限制**：仅当调度策略为Step或Rank时生效。 **取值范围**：Json字符串，自行配置，示例如下： - Step: {\"step_config\":{\"timeout\":300}} - Rank: {\"rank_config\":[{\"max_priority\":3,\"min_priority\":3,\"rank_strategy\":\"Step\",\"step_config\":{\"timeout\":300}},{\"max_priority\":2,\"min_priority\":1,\"rank_strategy\":\"Range\"}]} **默认取值**：不涉及。

        :param os_modelarts_pool_scheduler_queue_strategy_config: The os_modelarts_pool_scheduler_queue_strategy_config of this PoolMetadataUpdateAnnotations.
        :type os_modelarts_pool_scheduler_queue_strategy_config: str
        """
        self._os_modelarts_pool_scheduler_queue_strategy_config = os_modelarts_pool_scheduler_queue_strategy_config

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
        if not isinstance(other, PoolMetadataUpdateAnnotations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
