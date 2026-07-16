# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpecResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_id': 'str',
        'node_count': 'int',
        'pool_id': 'str',
        'pool_group_id': 'str',
        'main_container_customized_flavor': 'MainContainerCustomizedFlavor'
    }

    attribute_map = {
        'flavor_id': 'flavor_id',
        'node_count': 'node_count',
        'pool_id': 'pool_id',
        'pool_group_id': 'pool_group_id',
        'main_container_customized_flavor': 'main_container_customized_flavor'
    }

    def __init__(self, flavor_id=None, node_count=None, pool_id=None, pool_group_id=None, main_container_customized_flavor=None):
        r"""SpecResource

        The model defined in huaweicloud sdk

        :param flavor_id: **参数解释**：训练作业资源规格id。 **约束限制**：不涉及。 **取值范围**：CPU规格专属资源池不支持指定flavor_id。GPU/Ascend规格专属资源池可选取值如下： - modelarts.pool.visual.xlarge（1卡） - modelarts.pool.visual.2xlarge（2卡） - modelarts.pool.visual.4xlarge（4卡） - modelarts.pool.visual.8xlarge（8卡） - modelarts.pool.visual.16xlarge（16卡，当前仅限Snt9b23超节点资源池）  **默认取值**：不涉及。
        :type flavor_id: str
        :param node_count: **参数解释**：资源池创建训练作业使用节点数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：默认单节点。
        :type node_count: int
        :param pool_id: **参数解释**：专属资源池id。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type pool_id: str
        :param pool_group_id: **参数解释**：资源池联邦id。 **约束限制**：当kind为federated_pool_job时，该字段必填。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type pool_group_id: str
        :param main_container_customized_flavor: 
        :type main_container_customized_flavor: :class:`huaweicloudsdkmodelarts.v1.MainContainerCustomizedFlavor`
        """
        
        

        self._flavor_id = None
        self._node_count = None
        self._pool_id = None
        self._pool_group_id = None
        self._main_container_customized_flavor = None
        self.discriminator = None

        if flavor_id is not None:
            self.flavor_id = flavor_id
        self.node_count = node_count
        if pool_id is not None:
            self.pool_id = pool_id
        if pool_group_id is not None:
            self.pool_group_id = pool_group_id
        if main_container_customized_flavor is not None:
            self.main_container_customized_flavor = main_container_customized_flavor

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this SpecResource.

        **参数解释**：训练作业资源规格id。 **约束限制**：不涉及。 **取值范围**：CPU规格专属资源池不支持指定flavor_id。GPU/Ascend规格专属资源池可选取值如下： - modelarts.pool.visual.xlarge（1卡） - modelarts.pool.visual.2xlarge（2卡） - modelarts.pool.visual.4xlarge（4卡） - modelarts.pool.visual.8xlarge（8卡） - modelarts.pool.visual.16xlarge（16卡，当前仅限Snt9b23超节点资源池）  **默认取值**：不涉及。

        :return: The flavor_id of this SpecResource.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this SpecResource.

        **参数解释**：训练作业资源规格id。 **约束限制**：不涉及。 **取值范围**：CPU规格专属资源池不支持指定flavor_id。GPU/Ascend规格专属资源池可选取值如下： - modelarts.pool.visual.xlarge（1卡） - modelarts.pool.visual.2xlarge（2卡） - modelarts.pool.visual.4xlarge（4卡） - modelarts.pool.visual.8xlarge（8卡） - modelarts.pool.visual.16xlarge（16卡，当前仅限Snt9b23超节点资源池）  **默认取值**：不涉及。

        :param flavor_id: The flavor_id of this SpecResource.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def node_count(self):
        r"""Gets the node_count of this SpecResource.

        **参数解释**：资源池创建训练作业使用节点数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：默认单节点。

        :return: The node_count of this SpecResource.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        r"""Sets the node_count of this SpecResource.

        **参数解释**：资源池创建训练作业使用节点数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：默认单节点。

        :param node_count: The node_count of this SpecResource.
        :type node_count: int
        """
        self._node_count = node_count

    @property
    def pool_id(self):
        r"""Gets the pool_id of this SpecResource.

        **参数解释**：专属资源池id。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The pool_id of this SpecResource.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this SpecResource.

        **参数解释**：专属资源池id。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param pool_id: The pool_id of this SpecResource.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def pool_group_id(self):
        r"""Gets the pool_group_id of this SpecResource.

        **参数解释**：资源池联邦id。 **约束限制**：当kind为federated_pool_job时，该字段必填。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The pool_group_id of this SpecResource.
        :rtype: str
        """
        return self._pool_group_id

    @pool_group_id.setter
    def pool_group_id(self, pool_group_id):
        r"""Sets the pool_group_id of this SpecResource.

        **参数解释**：资源池联邦id。 **约束限制**：当kind为federated_pool_job时，该字段必填。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param pool_group_id: The pool_group_id of this SpecResource.
        :type pool_group_id: str
        """
        self._pool_group_id = pool_group_id

    @property
    def main_container_customized_flavor(self):
        r"""Gets the main_container_customized_flavor of this SpecResource.

        :return: The main_container_customized_flavor of this SpecResource.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.MainContainerCustomizedFlavor`
        """
        return self._main_container_customized_flavor

    @main_container_customized_flavor.setter
    def main_container_customized_flavor(self, main_container_customized_flavor):
        r"""Sets the main_container_customized_flavor of this SpecResource.

        :param main_container_customized_flavor: The main_container_customized_flavor of this SpecResource.
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
        if not isinstance(other, SpecResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
