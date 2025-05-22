# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodePoolNodeAutoscaling:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'min_node_count': 'int',
        'max_node_count': 'int',
        'scale_down_cooldown_time': 'int',
        'priority': 'int',
        'scale_down_unneeded_time': 'int',
        'scale_down_utilization_threshold': 'float'
    }

    attribute_map = {
        'enable': 'enable',
        'min_node_count': 'minNodeCount',
        'max_node_count': 'maxNodeCount',
        'scale_down_cooldown_time': 'scaleDownCooldownTime',
        'priority': 'priority',
        'scale_down_unneeded_time': 'scaleDownUnneededTime',
        'scale_down_utilization_threshold': 'scaleDownUtilizationThreshold'
    }

    def __init__(self, enable=None, min_node_count=None, max_node_count=None, scale_down_cooldown_time=None, priority=None, scale_down_unneeded_time=None, scale_down_utilization_threshold=None):
        r"""NodePoolNodeAutoscaling

        The model defined in huaweicloud sdk

        :param enable: 是否开启自动扩缩容
        :type enable: bool
        :param min_node_count: 若开启自动扩缩容，最小能缩容的节点个数。不可大于集群规格所允许的节点上限
        :type min_node_count: int
        :param max_node_count: 若开启自动扩缩容，最大能扩容的节点个数，应大于等于 minNodeCount，且不超过集群规格对应的节点数量上限。
        :type max_node_count: int
        :param scale_down_cooldown_time: 节点保留时间，单位为分钟，扩容出来的节点在这个时间内不会被缩掉
        :type scale_down_cooldown_time: int
        :param priority: 节点池权重，更高的权重在扩容时拥有更高的优先级
        :type priority: int
        :param scale_down_unneeded_time: **参数解释**： 缩容非必要时间。单位为分钟，该参数用于指定在确定可以进行缩容操作之前，节点处于不需要状态的持续时间。 当节点在指定的这段时间内一直处于不需要的状态时，autoscaler 插件才会考虑对其进行缩容操作。 这样可以避免因资源的短暂波动而频繁触发缩容，增强系统的稳定性。如果未设置该参数，autoscaler 插件插件会使用默认的时间阈值。 **约束限制**： 不涉及 **取值范围**： 0-2147483647。 &gt; 注意：如果传值为-1，代表取值为空。  **默认取值**： 默认为空
        :type scale_down_unneeded_time: int
        :param scale_down_utilization_threshold: **参数解释**： 缩容利用率阈值。运行在该节点上的所有 Pod 的 CPU 或内存总和除以该节点相应的可分配资源， 当该比值低于此阈值时，该节点可被考虑进行缩容。例如，设置为 0.3 表示当资源利用率低于 30% 时， 会触发缩容操作的评估。如果未设置该参数，autoscaler 插件会使用默认的利用率阈值。 **约束限制**： 不涉及 **取值范围**： 0-1。 &gt; 注意：如果传值为-1，代表取值为空。  **默认取值**： 默认为空
        :type scale_down_utilization_threshold: float
        """
        
        

        self._enable = None
        self._min_node_count = None
        self._max_node_count = None
        self._scale_down_cooldown_time = None
        self._priority = None
        self._scale_down_unneeded_time = None
        self._scale_down_utilization_threshold = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if min_node_count is not None:
            self.min_node_count = min_node_count
        if max_node_count is not None:
            self.max_node_count = max_node_count
        if scale_down_cooldown_time is not None:
            self.scale_down_cooldown_time = scale_down_cooldown_time
        if priority is not None:
            self.priority = priority
        if scale_down_unneeded_time is not None:
            self.scale_down_unneeded_time = scale_down_unneeded_time
        if scale_down_utilization_threshold is not None:
            self.scale_down_utilization_threshold = scale_down_utilization_threshold

    @property
    def enable(self):
        r"""Gets the enable of this NodePoolNodeAutoscaling.

        是否开启自动扩缩容

        :return: The enable of this NodePoolNodeAutoscaling.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this NodePoolNodeAutoscaling.

        是否开启自动扩缩容

        :param enable: The enable of this NodePoolNodeAutoscaling.
        :type enable: bool
        """
        self._enable = enable

    @property
    def min_node_count(self):
        r"""Gets the min_node_count of this NodePoolNodeAutoscaling.

        若开启自动扩缩容，最小能缩容的节点个数。不可大于集群规格所允许的节点上限

        :return: The min_node_count of this NodePoolNodeAutoscaling.
        :rtype: int
        """
        return self._min_node_count

    @min_node_count.setter
    def min_node_count(self, min_node_count):
        r"""Sets the min_node_count of this NodePoolNodeAutoscaling.

        若开启自动扩缩容，最小能缩容的节点个数。不可大于集群规格所允许的节点上限

        :param min_node_count: The min_node_count of this NodePoolNodeAutoscaling.
        :type min_node_count: int
        """
        self._min_node_count = min_node_count

    @property
    def max_node_count(self):
        r"""Gets the max_node_count of this NodePoolNodeAutoscaling.

        若开启自动扩缩容，最大能扩容的节点个数，应大于等于 minNodeCount，且不超过集群规格对应的节点数量上限。

        :return: The max_node_count of this NodePoolNodeAutoscaling.
        :rtype: int
        """
        return self._max_node_count

    @max_node_count.setter
    def max_node_count(self, max_node_count):
        r"""Sets the max_node_count of this NodePoolNodeAutoscaling.

        若开启自动扩缩容，最大能扩容的节点个数，应大于等于 minNodeCount，且不超过集群规格对应的节点数量上限。

        :param max_node_count: The max_node_count of this NodePoolNodeAutoscaling.
        :type max_node_count: int
        """
        self._max_node_count = max_node_count

    @property
    def scale_down_cooldown_time(self):
        r"""Gets the scale_down_cooldown_time of this NodePoolNodeAutoscaling.

        节点保留时间，单位为分钟，扩容出来的节点在这个时间内不会被缩掉

        :return: The scale_down_cooldown_time of this NodePoolNodeAutoscaling.
        :rtype: int
        """
        return self._scale_down_cooldown_time

    @scale_down_cooldown_time.setter
    def scale_down_cooldown_time(self, scale_down_cooldown_time):
        r"""Sets the scale_down_cooldown_time of this NodePoolNodeAutoscaling.

        节点保留时间，单位为分钟，扩容出来的节点在这个时间内不会被缩掉

        :param scale_down_cooldown_time: The scale_down_cooldown_time of this NodePoolNodeAutoscaling.
        :type scale_down_cooldown_time: int
        """
        self._scale_down_cooldown_time = scale_down_cooldown_time

    @property
    def priority(self):
        r"""Gets the priority of this NodePoolNodeAutoscaling.

        节点池权重，更高的权重在扩容时拥有更高的优先级

        :return: The priority of this NodePoolNodeAutoscaling.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this NodePoolNodeAutoscaling.

        节点池权重，更高的权重在扩容时拥有更高的优先级

        :param priority: The priority of this NodePoolNodeAutoscaling.
        :type priority: int
        """
        self._priority = priority

    @property
    def scale_down_unneeded_time(self):
        r"""Gets the scale_down_unneeded_time of this NodePoolNodeAutoscaling.

        **参数解释**： 缩容非必要时间。单位为分钟，该参数用于指定在确定可以进行缩容操作之前，节点处于不需要状态的持续时间。 当节点在指定的这段时间内一直处于不需要的状态时，autoscaler 插件才会考虑对其进行缩容操作。 这样可以避免因资源的短暂波动而频繁触发缩容，增强系统的稳定性。如果未设置该参数，autoscaler 插件插件会使用默认的时间阈值。 **约束限制**： 不涉及 **取值范围**： 0-2147483647。 > 注意：如果传值为-1，代表取值为空。  **默认取值**： 默认为空

        :return: The scale_down_unneeded_time of this NodePoolNodeAutoscaling.
        :rtype: int
        """
        return self._scale_down_unneeded_time

    @scale_down_unneeded_time.setter
    def scale_down_unneeded_time(self, scale_down_unneeded_time):
        r"""Sets the scale_down_unneeded_time of this NodePoolNodeAutoscaling.

        **参数解释**： 缩容非必要时间。单位为分钟，该参数用于指定在确定可以进行缩容操作之前，节点处于不需要状态的持续时间。 当节点在指定的这段时间内一直处于不需要的状态时，autoscaler 插件才会考虑对其进行缩容操作。 这样可以避免因资源的短暂波动而频繁触发缩容，增强系统的稳定性。如果未设置该参数，autoscaler 插件插件会使用默认的时间阈值。 **约束限制**： 不涉及 **取值范围**： 0-2147483647。 > 注意：如果传值为-1，代表取值为空。  **默认取值**： 默认为空

        :param scale_down_unneeded_time: The scale_down_unneeded_time of this NodePoolNodeAutoscaling.
        :type scale_down_unneeded_time: int
        """
        self._scale_down_unneeded_time = scale_down_unneeded_time

    @property
    def scale_down_utilization_threshold(self):
        r"""Gets the scale_down_utilization_threshold of this NodePoolNodeAutoscaling.

        **参数解释**： 缩容利用率阈值。运行在该节点上的所有 Pod 的 CPU 或内存总和除以该节点相应的可分配资源， 当该比值低于此阈值时，该节点可被考虑进行缩容。例如，设置为 0.3 表示当资源利用率低于 30% 时， 会触发缩容操作的评估。如果未设置该参数，autoscaler 插件会使用默认的利用率阈值。 **约束限制**： 不涉及 **取值范围**： 0-1。 > 注意：如果传值为-1，代表取值为空。  **默认取值**： 默认为空

        :return: The scale_down_utilization_threshold of this NodePoolNodeAutoscaling.
        :rtype: float
        """
        return self._scale_down_utilization_threshold

    @scale_down_utilization_threshold.setter
    def scale_down_utilization_threshold(self, scale_down_utilization_threshold):
        r"""Sets the scale_down_utilization_threshold of this NodePoolNodeAutoscaling.

        **参数解释**： 缩容利用率阈值。运行在该节点上的所有 Pod 的 CPU 或内存总和除以该节点相应的可分配资源， 当该比值低于此阈值时，该节点可被考虑进行缩容。例如，设置为 0.3 表示当资源利用率低于 30% 时， 会触发缩容操作的评估。如果未设置该参数，autoscaler 插件会使用默认的利用率阈值。 **约束限制**： 不涉及 **取值范围**： 0-1。 > 注意：如果传值为-1，代表取值为空。  **默认取值**： 默认为空

        :param scale_down_utilization_threshold: The scale_down_utilization_threshold of this NodePoolNodeAutoscaling.
        :type scale_down_utilization_threshold: float
        """
        self._scale_down_utilization_threshold = scale_down_utilization_threshold

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodePoolNodeAutoscaling):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
