# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Deployment:

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
        'ray_actor_options': 'RayActorOptions',
        'autoscaling_config': 'AutoscalingConfig',
        'num_replicas': 'int',
        'user_config': 'object',
        'max_replicas_per_node': 'int',
        'max_ongoing_requests': 'int',
        'max_queued_requests': 'int'
    }

    attribute_map = {
        'name': 'name',
        'ray_actor_options': 'ray_actor_options',
        'autoscaling_config': 'autoscaling_config',
        'num_replicas': 'num_replicas',
        'user_config': 'user_config',
        'max_replicas_per_node': 'max_replicas_per_node',
        'max_ongoing_requests': 'max_ongoing_requests',
        'max_queued_requests': 'max_queued_requests'
    }

    def __init__(self, name=None, ray_actor_options=None, autoscaling_config=None, num_replicas=None, user_config=None, max_replicas_per_node=None, max_ongoing_requests=None, max_queued_requests=None):
        r"""Deployment

        The model defined in huaweicloud sdk

        :param name: **参数解释**：Deployment的名称。 **约束限制**：不涉及。 **取值范围**：长度为[1,64]的中文、字母、数字、下划线、中划线、半角句号（.）、空格的组合。 **默认取值**：不涉及。 
        :type name: str
        :param ray_actor_options: 
        :type ray_actor_options: :class:`huaweicloudsdkdataartsfabric.v1.RayActorOptions`
        :param autoscaling_config: 
        :type autoscaling_config: :class:`huaweicloudsdkdataartsfabric.v1.AutoscalingConfig`
        :param num_replicas: **参数解释**：副本数量。 **约束限制**：不涉及。 **取值范围**：[0,1000]。 **默认取值**：不涉及。
        :type num_replicas: int
        :param user_config: **参数解释**：用户自定义配置。 **约束限制**：不涉及。
        :type user_config: object
        :param max_replicas_per_node: **参数解释**：每个节点允许的最大副本数。 **约束限制**：不涉及。 **取值范围**：[1,100]。 **默认取值**：1。
        :type max_replicas_per_node: int
        :param max_ongoing_requests: **参数解释**：每个副本可接受的最大并发请求数。 **约束限制**：不涉及。 **取值范围**：[1,100000]。 **默认取值**：不涉及。
        :type max_ongoing_requests: int
        :param max_queued_requests: **参数解释**：deployment可接受的排队的最大请求数。-1时表示无限制。 **约束限制**：不涉及。 **取值范围**：[-1,100000]。 **默认取值**：不涉及。
        :type max_queued_requests: int
        """
        
        

        self._name = None
        self._ray_actor_options = None
        self._autoscaling_config = None
        self._num_replicas = None
        self._user_config = None
        self._max_replicas_per_node = None
        self._max_ongoing_requests = None
        self._max_queued_requests = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if ray_actor_options is not None:
            self.ray_actor_options = ray_actor_options
        if autoscaling_config is not None:
            self.autoscaling_config = autoscaling_config
        if num_replicas is not None:
            self.num_replicas = num_replicas
        if user_config is not None:
            self.user_config = user_config
        if max_replicas_per_node is not None:
            self.max_replicas_per_node = max_replicas_per_node
        if max_ongoing_requests is not None:
            self.max_ongoing_requests = max_ongoing_requests
        if max_queued_requests is not None:
            self.max_queued_requests = max_queued_requests

    @property
    def name(self):
        r"""Gets the name of this Deployment.

        **参数解释**：Deployment的名称。 **约束限制**：不涉及。 **取值范围**：长度为[1,64]的中文、字母、数字、下划线、中划线、半角句号（.）、空格的组合。 **默认取值**：不涉及。 

        :return: The name of this Deployment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Deployment.

        **参数解释**：Deployment的名称。 **约束限制**：不涉及。 **取值范围**：长度为[1,64]的中文、字母、数字、下划线、中划线、半角句号（.）、空格的组合。 **默认取值**：不涉及。 

        :param name: The name of this Deployment.
        :type name: str
        """
        self._name = name

    @property
    def ray_actor_options(self):
        r"""Gets the ray_actor_options of this Deployment.

        :return: The ray_actor_options of this Deployment.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.RayActorOptions`
        """
        return self._ray_actor_options

    @ray_actor_options.setter
    def ray_actor_options(self, ray_actor_options):
        r"""Sets the ray_actor_options of this Deployment.

        :param ray_actor_options: The ray_actor_options of this Deployment.
        :type ray_actor_options: :class:`huaweicloudsdkdataartsfabric.v1.RayActorOptions`
        """
        self._ray_actor_options = ray_actor_options

    @property
    def autoscaling_config(self):
        r"""Gets the autoscaling_config of this Deployment.

        :return: The autoscaling_config of this Deployment.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.AutoscalingConfig`
        """
        return self._autoscaling_config

    @autoscaling_config.setter
    def autoscaling_config(self, autoscaling_config):
        r"""Sets the autoscaling_config of this Deployment.

        :param autoscaling_config: The autoscaling_config of this Deployment.
        :type autoscaling_config: :class:`huaweicloudsdkdataartsfabric.v1.AutoscalingConfig`
        """
        self._autoscaling_config = autoscaling_config

    @property
    def num_replicas(self):
        r"""Gets the num_replicas of this Deployment.

        **参数解释**：副本数量。 **约束限制**：不涉及。 **取值范围**：[0,1000]。 **默认取值**：不涉及。

        :return: The num_replicas of this Deployment.
        :rtype: int
        """
        return self._num_replicas

    @num_replicas.setter
    def num_replicas(self, num_replicas):
        r"""Sets the num_replicas of this Deployment.

        **参数解释**：副本数量。 **约束限制**：不涉及。 **取值范围**：[0,1000]。 **默认取值**：不涉及。

        :param num_replicas: The num_replicas of this Deployment.
        :type num_replicas: int
        """
        self._num_replicas = num_replicas

    @property
    def user_config(self):
        r"""Gets the user_config of this Deployment.

        **参数解释**：用户自定义配置。 **约束限制**：不涉及。

        :return: The user_config of this Deployment.
        :rtype: object
        """
        return self._user_config

    @user_config.setter
    def user_config(self, user_config):
        r"""Sets the user_config of this Deployment.

        **参数解释**：用户自定义配置。 **约束限制**：不涉及。

        :param user_config: The user_config of this Deployment.
        :type user_config: object
        """
        self._user_config = user_config

    @property
    def max_replicas_per_node(self):
        r"""Gets the max_replicas_per_node of this Deployment.

        **参数解释**：每个节点允许的最大副本数。 **约束限制**：不涉及。 **取值范围**：[1,100]。 **默认取值**：1。

        :return: The max_replicas_per_node of this Deployment.
        :rtype: int
        """
        return self._max_replicas_per_node

    @max_replicas_per_node.setter
    def max_replicas_per_node(self, max_replicas_per_node):
        r"""Sets the max_replicas_per_node of this Deployment.

        **参数解释**：每个节点允许的最大副本数。 **约束限制**：不涉及。 **取值范围**：[1,100]。 **默认取值**：1。

        :param max_replicas_per_node: The max_replicas_per_node of this Deployment.
        :type max_replicas_per_node: int
        """
        self._max_replicas_per_node = max_replicas_per_node

    @property
    def max_ongoing_requests(self):
        r"""Gets the max_ongoing_requests of this Deployment.

        **参数解释**：每个副本可接受的最大并发请求数。 **约束限制**：不涉及。 **取值范围**：[1,100000]。 **默认取值**：不涉及。

        :return: The max_ongoing_requests of this Deployment.
        :rtype: int
        """
        return self._max_ongoing_requests

    @max_ongoing_requests.setter
    def max_ongoing_requests(self, max_ongoing_requests):
        r"""Sets the max_ongoing_requests of this Deployment.

        **参数解释**：每个副本可接受的最大并发请求数。 **约束限制**：不涉及。 **取值范围**：[1,100000]。 **默认取值**：不涉及。

        :param max_ongoing_requests: The max_ongoing_requests of this Deployment.
        :type max_ongoing_requests: int
        """
        self._max_ongoing_requests = max_ongoing_requests

    @property
    def max_queued_requests(self):
        r"""Gets the max_queued_requests of this Deployment.

        **参数解释**：deployment可接受的排队的最大请求数。-1时表示无限制。 **约束限制**：不涉及。 **取值范围**：[-1,100000]。 **默认取值**：不涉及。

        :return: The max_queued_requests of this Deployment.
        :rtype: int
        """
        return self._max_queued_requests

    @max_queued_requests.setter
    def max_queued_requests(self, max_queued_requests):
        r"""Sets the max_queued_requests of this Deployment.

        **参数解释**：deployment可接受的排队的最大请求数。-1时表示无限制。 **约束限制**：不涉及。 **取值范围**：[-1,100000]。 **默认取值**：不涉及。

        :param max_queued_requests: The max_queued_requests of this Deployment.
        :type max_queued_requests: int
        """
        self._max_queued_requests = max_queued_requests

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
        if not isinstance(other, Deployment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
