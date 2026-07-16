# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskTaskResource:

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
        'pool_id': 'str'
    }

    attribute_map = {
        'flavor_id': 'flavor_id',
        'node_count': 'node_count',
        'pool_id': 'pool_id'
    }

    def __init__(self, flavor_id=None, node_count=None, pool_id=None):
        r"""TaskTaskResource

        The model defined in huaweicloud sdk

        :param flavor_id: **参数解释**：训练作业选择的资源规格ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type flavor_id: str
        :param node_count: **参数解释**：训练作业选择的资源副本数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type node_count: int
        :param pool_id: **参数解释**：训练任务选择的资源池ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type pool_id: str
        """
        
        

        self._flavor_id = None
        self._node_count = None
        self._pool_id = None
        self.discriminator = None

        if flavor_id is not None:
            self.flavor_id = flavor_id
        self.node_count = node_count
        if pool_id is not None:
            self.pool_id = pool_id

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this TaskTaskResource.

        **参数解释**：训练作业选择的资源规格ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The flavor_id of this TaskTaskResource.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this TaskTaskResource.

        **参数解释**：训练作业选择的资源规格ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param flavor_id: The flavor_id of this TaskTaskResource.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def node_count(self):
        r"""Gets the node_count of this TaskTaskResource.

        **参数解释**：训练作业选择的资源副本数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The node_count of this TaskTaskResource.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        r"""Sets the node_count of this TaskTaskResource.

        **参数解释**：训练作业选择的资源副本数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param node_count: The node_count of this TaskTaskResource.
        :type node_count: int
        """
        self._node_count = node_count

    @property
    def pool_id(self):
        r"""Gets the pool_id of this TaskTaskResource.

        **参数解释**：训练任务选择的资源池ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The pool_id of this TaskTaskResource.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this TaskTaskResource.

        **参数解释**：训练任务选择的资源池ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param pool_id: The pool_id of this TaskTaskResource.
        :type pool_id: str
        """
        self._pool_id = pool_id

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
        if not isinstance(other, TaskTaskResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
