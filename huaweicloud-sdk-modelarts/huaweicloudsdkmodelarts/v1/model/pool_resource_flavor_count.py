# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolResourceFlavorCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'count': 'int',
        'max_count': 'int',
        'azs': 'list[PoolNodeAz]',
        'node_pool': 'str'
    }

    attribute_map = {
        'flavor': 'flavor',
        'count': 'count',
        'max_count': 'maxCount',
        'azs': 'azs',
        'node_pool': 'nodePool'
    }

    def __init__(self, flavor=None, count=None, max_count=None, azs=None, node_pool=None):
        r"""PoolResourceFlavorCount

        The model defined in huaweicloud sdk

        :param flavor: **参数解释**：资源规格ID。 **取值范围**：不涉及。
        :type flavor: str
        :param count: **参数解释**：资源池中资源规格实例数量。 **取值范围**：不涉及。
        :type count: int
        :param max_count: **参数解释**：资源池中资源规格实例弹性数量。物理池中该值和count相同。 **取值范围**：不涉及。
        :type max_count: int
        :param azs: **参数解释**：资源池中期望创建的资源规格实例的az分布。
        :type azs: list[:class:`huaweicloudsdkmodelarts.v1.PoolNodeAz`]
        :param node_pool: **参数解释**：节点池ID。 **取值范围**：不涉及。
        :type node_pool: str
        """
        
        

        self._flavor = None
        self._count = None
        self._max_count = None
        self._azs = None
        self._node_pool = None
        self.discriminator = None

        self.flavor = flavor
        self.count = count
        self.max_count = max_count
        if azs is not None:
            self.azs = azs
        if node_pool is not None:
            self.node_pool = node_pool

    @property
    def flavor(self):
        r"""Gets the flavor of this PoolResourceFlavorCount.

        **参数解释**：资源规格ID。 **取值范围**：不涉及。

        :return: The flavor of this PoolResourceFlavorCount.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this PoolResourceFlavorCount.

        **参数解释**：资源规格ID。 **取值范围**：不涉及。

        :param flavor: The flavor of this PoolResourceFlavorCount.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def count(self):
        r"""Gets the count of this PoolResourceFlavorCount.

        **参数解释**：资源池中资源规格实例数量。 **取值范围**：不涉及。

        :return: The count of this PoolResourceFlavorCount.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this PoolResourceFlavorCount.

        **参数解释**：资源池中资源规格实例数量。 **取值范围**：不涉及。

        :param count: The count of this PoolResourceFlavorCount.
        :type count: int
        """
        self._count = count

    @property
    def max_count(self):
        r"""Gets the max_count of this PoolResourceFlavorCount.

        **参数解释**：资源池中资源规格实例弹性数量。物理池中该值和count相同。 **取值范围**：不涉及。

        :return: The max_count of this PoolResourceFlavorCount.
        :rtype: int
        """
        return self._max_count

    @max_count.setter
    def max_count(self, max_count):
        r"""Sets the max_count of this PoolResourceFlavorCount.

        **参数解释**：资源池中资源规格实例弹性数量。物理池中该值和count相同。 **取值范围**：不涉及。

        :param max_count: The max_count of this PoolResourceFlavorCount.
        :type max_count: int
        """
        self._max_count = max_count

    @property
    def azs(self):
        r"""Gets the azs of this PoolResourceFlavorCount.

        **参数解释**：资源池中期望创建的资源规格实例的az分布。

        :return: The azs of this PoolResourceFlavorCount.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.PoolNodeAz`]
        """
        return self._azs

    @azs.setter
    def azs(self, azs):
        r"""Sets the azs of this PoolResourceFlavorCount.

        **参数解释**：资源池中期望创建的资源规格实例的az分布。

        :param azs: The azs of this PoolResourceFlavorCount.
        :type azs: list[:class:`huaweicloudsdkmodelarts.v1.PoolNodeAz`]
        """
        self._azs = azs

    @property
    def node_pool(self):
        r"""Gets the node_pool of this PoolResourceFlavorCount.

        **参数解释**：节点池ID。 **取值范围**：不涉及。

        :return: The node_pool of this PoolResourceFlavorCount.
        :rtype: str
        """
        return self._node_pool

    @node_pool.setter
    def node_pool(self, node_pool):
        r"""Sets the node_pool of this PoolResourceFlavorCount.

        **参数解释**：节点池ID。 **取值范围**：不涉及。

        :param node_pool: The node_pool of this PoolResourceFlavorCount.
        :type node_pool: str
        """
        self._node_pool = node_pool

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
        if not isinstance(other, PoolResourceFlavorCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
