# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServeDeployment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'num_replicas': 'int',
        'max_replicas_per_node': 'int',
        'max_ongoing_requests': 'int',
        'max_queued_requests': 'int',
        'ray_actor_options': 'ServeRayActorOptions'
    }

    attribute_map = {
        'name': 'name',
        'num_replicas': 'num_replicas',
        'max_replicas_per_node': 'max_replicas_per_node',
        'max_ongoing_requests': 'max_ongoing_requests',
        'max_queued_requests': 'max_queued_requests',
        'ray_actor_options': 'ray_actor_options'
    }

    def __init__(self, name=None, num_replicas=None, max_replicas_per_node=None, max_ongoing_requests=None, max_queued_requests=None, ray_actor_options=None):
        r"""ServeDeployment

        The model defined in huaweicloud sdk

        :param name: **参数解释**：Deployment 名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type name: str
        :param num_replicas: **参数解释**：副本数。 **约束限制**：不涉及。 **取值范围**：不小于1。 **默认取值**：不涉及。
        :type num_replicas: int
        :param max_replicas_per_node: **参数解释**：单节点最大副本数。 **约束限制**：不涉及。 **取值范围**：不小于1。 **默认取值**：不涉及。
        :type max_replicas_per_node: int
        :param max_ongoing_requests: **参数解释**：最大进行中请求数。 **约束限制**：不涉及。 **取值范围**：不小于1。 **默认取值**：不涉及。
        :type max_ongoing_requests: int
        :param max_queued_requests: **参数解释**：最大排队请求数。 **约束限制**：不涉及。 **取值范围**：不小于1。 **默认取值**：不涉及。
        :type max_queued_requests: int
        :param ray_actor_options: 
        :type ray_actor_options: :class:`huaweicloudsdkaidatalake.v2.ServeRayActorOptions`
        """
        
        

        self._name = None
        self._num_replicas = None
        self._max_replicas_per_node = None
        self._max_ongoing_requests = None
        self._max_queued_requests = None
        self._ray_actor_options = None
        self.discriminator = None

        self.name = name
        self.num_replicas = num_replicas
        if max_replicas_per_node is not None:
            self.max_replicas_per_node = max_replicas_per_node
        if max_ongoing_requests is not None:
            self.max_ongoing_requests = max_ongoing_requests
        if max_queued_requests is not None:
            self.max_queued_requests = max_queued_requests
        if ray_actor_options is not None:
            self.ray_actor_options = ray_actor_options

    @property
    def name(self):
        r"""Gets the name of this ServeDeployment.

        **参数解释**：Deployment 名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The name of this ServeDeployment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServeDeployment.

        **参数解释**：Deployment 名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param name: The name of this ServeDeployment.
        :type name: str
        """
        self._name = name

    @property
    def num_replicas(self):
        r"""Gets the num_replicas of this ServeDeployment.

        **参数解释**：副本数。 **约束限制**：不涉及。 **取值范围**：不小于1。 **默认取值**：不涉及。

        :return: The num_replicas of this ServeDeployment.
        :rtype: int
        """
        return self._num_replicas

    @num_replicas.setter
    def num_replicas(self, num_replicas):
        r"""Sets the num_replicas of this ServeDeployment.

        **参数解释**：副本数。 **约束限制**：不涉及。 **取值范围**：不小于1。 **默认取值**：不涉及。

        :param num_replicas: The num_replicas of this ServeDeployment.
        :type num_replicas: int
        """
        self._num_replicas = num_replicas

    @property
    def max_replicas_per_node(self):
        r"""Gets the max_replicas_per_node of this ServeDeployment.

        **参数解释**：单节点最大副本数。 **约束限制**：不涉及。 **取值范围**：不小于1。 **默认取值**：不涉及。

        :return: The max_replicas_per_node of this ServeDeployment.
        :rtype: int
        """
        return self._max_replicas_per_node

    @max_replicas_per_node.setter
    def max_replicas_per_node(self, max_replicas_per_node):
        r"""Sets the max_replicas_per_node of this ServeDeployment.

        **参数解释**：单节点最大副本数。 **约束限制**：不涉及。 **取值范围**：不小于1。 **默认取值**：不涉及。

        :param max_replicas_per_node: The max_replicas_per_node of this ServeDeployment.
        :type max_replicas_per_node: int
        """
        self._max_replicas_per_node = max_replicas_per_node

    @property
    def max_ongoing_requests(self):
        r"""Gets the max_ongoing_requests of this ServeDeployment.

        **参数解释**：最大进行中请求数。 **约束限制**：不涉及。 **取值范围**：不小于1。 **默认取值**：不涉及。

        :return: The max_ongoing_requests of this ServeDeployment.
        :rtype: int
        """
        return self._max_ongoing_requests

    @max_ongoing_requests.setter
    def max_ongoing_requests(self, max_ongoing_requests):
        r"""Sets the max_ongoing_requests of this ServeDeployment.

        **参数解释**：最大进行中请求数。 **约束限制**：不涉及。 **取值范围**：不小于1。 **默认取值**：不涉及。

        :param max_ongoing_requests: The max_ongoing_requests of this ServeDeployment.
        :type max_ongoing_requests: int
        """
        self._max_ongoing_requests = max_ongoing_requests

    @property
    def max_queued_requests(self):
        r"""Gets the max_queued_requests of this ServeDeployment.

        **参数解释**：最大排队请求数。 **约束限制**：不涉及。 **取值范围**：不小于1。 **默认取值**：不涉及。

        :return: The max_queued_requests of this ServeDeployment.
        :rtype: int
        """
        return self._max_queued_requests

    @max_queued_requests.setter
    def max_queued_requests(self, max_queued_requests):
        r"""Sets the max_queued_requests of this ServeDeployment.

        **参数解释**：最大排队请求数。 **约束限制**：不涉及。 **取值范围**：不小于1。 **默认取值**：不涉及。

        :param max_queued_requests: The max_queued_requests of this ServeDeployment.
        :type max_queued_requests: int
        """
        self._max_queued_requests = max_queued_requests

    @property
    def ray_actor_options(self):
        r"""Gets the ray_actor_options of this ServeDeployment.

        :return: The ray_actor_options of this ServeDeployment.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ServeRayActorOptions`
        """
        return self._ray_actor_options

    @ray_actor_options.setter
    def ray_actor_options(self, ray_actor_options):
        r"""Sets the ray_actor_options of this ServeDeployment.

        :param ray_actor_options: The ray_actor_options of this ServeDeployment.
        :type ray_actor_options: :class:`huaweicloudsdkaidatalake.v2.ServeRayActorOptions`
        """
        self._ray_actor_options = ray_actor_options

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
        if not isinstance(other, ServeDeployment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
