# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Resource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy': 'str',
        'flavor_id': 'str',
        'flavor_name': 'str',
        'node_count': 'int',
        'pool_id': 'str',
        'pool_group_id': 'str',
        'flavor_detail': 'FlavorDetail',
        'main_container_allocated_resources': 'MainContainerAllocatedResources',
        'main_container_customized_flavor': 'MainContainerCustomizedFlavor'
    }

    attribute_map = {
        'policy': 'policy',
        'flavor_id': 'flavor_id',
        'flavor_name': 'flavor_name',
        'node_count': 'node_count',
        'pool_id': 'pool_id',
        'pool_group_id': 'pool_group_id',
        'flavor_detail': 'flavor_detail',
        'main_container_allocated_resources': 'main_container_allocated_resources',
        'main_container_customized_flavor': 'main_container_customized_flavor'
    }

    def __init__(self, policy=None, flavor_id=None, flavor_name=None, node_count=None, pool_id=None, pool_group_id=None, flavor_detail=None, main_container_allocated_resources=None, main_container_customized_flavor=None):
        r"""Resource

        The model defined in huaweicloud sdk

        :param policy: **参数解释**：训练作业资源规格模式。 **取值范围**： - regular：标准模式
        :type policy: str
        :param flavor_id: **参数解释**：训练作业资源规格id。 **取值范围**：CPU规格专属资源池不支持指定flavor_id。GPU/Ascend规格专属资源池可选取值如下： - modelarts.pool.visual.xlarge（1卡） - modelarts.pool.visual.2xlarge（2卡） - modelarts.pool.visual.4xlarge（4卡） - modelarts.pool.visual.8xlarge（8卡）
        :type flavor_id: str
        :param flavor_name: **参数解释**：使用flavor_id时，由ModelArts返回的只读规格名称。 **取值范围**：不涉及。
        :type flavor_name: str
        :param node_count: **参数解释**：训练作业选择的资源副本数。 **取值范围**：不涉及。
        :type node_count: int
        :param pool_id: **参数解释**：训练作业选择的资源池ID。 **取值范围**：不涉及。
        :type pool_id: str
        :param pool_group_id: **参数解释**：训练作业选择的资源池联邦ID。 **取值范围**：不涉及。
        :type pool_group_id: str
        :param flavor_detail: 
        :type flavor_detail: :class:`huaweicloudsdkmodelarts.v1.FlavorDetail`
        :param main_container_allocated_resources: 
        :type main_container_allocated_resources: :class:`huaweicloudsdkmodelarts.v1.MainContainerAllocatedResources`
        :param main_container_customized_flavor: 
        :type main_container_customized_flavor: :class:`huaweicloudsdkmodelarts.v1.MainContainerCustomizedFlavor`
        """
        
        

        self._policy = None
        self._flavor_id = None
        self._flavor_name = None
        self._node_count = None
        self._pool_id = None
        self._pool_group_id = None
        self._flavor_detail = None
        self._main_container_allocated_resources = None
        self._main_container_customized_flavor = None
        self.discriminator = None

        if policy is not None:
            self.policy = policy
        self.flavor_id = flavor_id
        if flavor_name is not None:
            self.flavor_name = flavor_name
        self.node_count = node_count
        if pool_id is not None:
            self.pool_id = pool_id
        if pool_group_id is not None:
            self.pool_group_id = pool_group_id
        if flavor_detail is not None:
            self.flavor_detail = flavor_detail
        if main_container_allocated_resources is not None:
            self.main_container_allocated_resources = main_container_allocated_resources
        if main_container_customized_flavor is not None:
            self.main_container_customized_flavor = main_container_customized_flavor

    @property
    def policy(self):
        r"""Gets the policy of this Resource.

        **参数解释**：训练作业资源规格模式。 **取值范围**： - regular：标准模式

        :return: The policy of this Resource.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this Resource.

        **参数解释**：训练作业资源规格模式。 **取值范围**： - regular：标准模式

        :param policy: The policy of this Resource.
        :type policy: str
        """
        self._policy = policy

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this Resource.

        **参数解释**：训练作业资源规格id。 **取值范围**：CPU规格专属资源池不支持指定flavor_id。GPU/Ascend规格专属资源池可选取值如下： - modelarts.pool.visual.xlarge（1卡） - modelarts.pool.visual.2xlarge（2卡） - modelarts.pool.visual.4xlarge（4卡） - modelarts.pool.visual.8xlarge（8卡）

        :return: The flavor_id of this Resource.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this Resource.

        **参数解释**：训练作业资源规格id。 **取值范围**：CPU规格专属资源池不支持指定flavor_id。GPU/Ascend规格专属资源池可选取值如下： - modelarts.pool.visual.xlarge（1卡） - modelarts.pool.visual.2xlarge（2卡） - modelarts.pool.visual.4xlarge（4卡） - modelarts.pool.visual.8xlarge（8卡）

        :param flavor_id: The flavor_id of this Resource.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def flavor_name(self):
        r"""Gets the flavor_name of this Resource.

        **参数解释**：使用flavor_id时，由ModelArts返回的只读规格名称。 **取值范围**：不涉及。

        :return: The flavor_name of this Resource.
        :rtype: str
        """
        return self._flavor_name

    @flavor_name.setter
    def flavor_name(self, flavor_name):
        r"""Sets the flavor_name of this Resource.

        **参数解释**：使用flavor_id时，由ModelArts返回的只读规格名称。 **取值范围**：不涉及。

        :param flavor_name: The flavor_name of this Resource.
        :type flavor_name: str
        """
        self._flavor_name = flavor_name

    @property
    def node_count(self):
        r"""Gets the node_count of this Resource.

        **参数解释**：训练作业选择的资源副本数。 **取值范围**：不涉及。

        :return: The node_count of this Resource.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        r"""Sets the node_count of this Resource.

        **参数解释**：训练作业选择的资源副本数。 **取值范围**：不涉及。

        :param node_count: The node_count of this Resource.
        :type node_count: int
        """
        self._node_count = node_count

    @property
    def pool_id(self):
        r"""Gets the pool_id of this Resource.

        **参数解释**：训练作业选择的资源池ID。 **取值范围**：不涉及。

        :return: The pool_id of this Resource.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this Resource.

        **参数解释**：训练作业选择的资源池ID。 **取值范围**：不涉及。

        :param pool_id: The pool_id of this Resource.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def pool_group_id(self):
        r"""Gets the pool_group_id of this Resource.

        **参数解释**：训练作业选择的资源池联邦ID。 **取值范围**：不涉及。

        :return: The pool_group_id of this Resource.
        :rtype: str
        """
        return self._pool_group_id

    @pool_group_id.setter
    def pool_group_id(self, pool_group_id):
        r"""Sets the pool_group_id of this Resource.

        **参数解释**：训练作业选择的资源池联邦ID。 **取值范围**：不涉及。

        :param pool_group_id: The pool_group_id of this Resource.
        :type pool_group_id: str
        """
        self._pool_group_id = pool_group_id

    @property
    def flavor_detail(self):
        r"""Gets the flavor_detail of this Resource.

        :return: The flavor_detail of this Resource.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.FlavorDetail`
        """
        return self._flavor_detail

    @flavor_detail.setter
    def flavor_detail(self, flavor_detail):
        r"""Sets the flavor_detail of this Resource.

        :param flavor_detail: The flavor_detail of this Resource.
        :type flavor_detail: :class:`huaweicloudsdkmodelarts.v1.FlavorDetail`
        """
        self._flavor_detail = flavor_detail

    @property
    def main_container_allocated_resources(self):
        r"""Gets the main_container_allocated_resources of this Resource.

        :return: The main_container_allocated_resources of this Resource.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.MainContainerAllocatedResources`
        """
        return self._main_container_allocated_resources

    @main_container_allocated_resources.setter
    def main_container_allocated_resources(self, main_container_allocated_resources):
        r"""Sets the main_container_allocated_resources of this Resource.

        :param main_container_allocated_resources: The main_container_allocated_resources of this Resource.
        :type main_container_allocated_resources: :class:`huaweicloudsdkmodelarts.v1.MainContainerAllocatedResources`
        """
        self._main_container_allocated_resources = main_container_allocated_resources

    @property
    def main_container_customized_flavor(self):
        r"""Gets the main_container_customized_flavor of this Resource.

        :return: The main_container_customized_flavor of this Resource.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.MainContainerCustomizedFlavor`
        """
        return self._main_container_customized_flavor

    @main_container_customized_flavor.setter
    def main_container_customized_flavor(self, main_container_customized_flavor):
        r"""Sets the main_container_customized_flavor of this Resource.

        :param main_container_customized_flavor: The main_container_customized_flavor of this Resource.
        :type main_container_customized_flavor: :class:`huaweicloudsdkmodelarts.v1.MainContainerCustomizedFlavor`
        """
        self._main_container_customized_flavor = main_container_customized_flavor

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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
