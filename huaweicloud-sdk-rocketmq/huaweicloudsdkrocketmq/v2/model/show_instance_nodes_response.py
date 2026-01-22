# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceNodesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nodes': 'list[NodeContextEntity]',
        'total': 'int'
    }

    attribute_map = {
        'nodes': 'nodes',
        'total': 'total'
    }

    def __init__(self, nodes=None, total=None):
        r"""ShowInstanceNodesResponse

        The model defined in huaweicloud sdk

        :param nodes: **参数解释**： 后台任务ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type nodes: list[:class:`huaweicloudsdkrocketmq.v2.NodeContextEntity`]
        :param total: **参数解释**： 总个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type total: int
        """
        
        super().__init__()

        self._nodes = None
        self._total = None
        self.discriminator = None

        if nodes is not None:
            self.nodes = nodes
        if total is not None:
            self.total = total

    @property
    def nodes(self):
        r"""Gets the nodes of this ShowInstanceNodesResponse.

        **参数解释**： 后台任务ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The nodes of this ShowInstanceNodesResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.NodeContextEntity`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this ShowInstanceNodesResponse.

        **参数解释**： 后台任务ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param nodes: The nodes of this ShowInstanceNodesResponse.
        :type nodes: list[:class:`huaweicloudsdkrocketmq.v2.NodeContextEntity`]
        """
        self._nodes = nodes

    @property
    def total(self):
        r"""Gets the total of this ShowInstanceNodesResponse.

        **参数解释**： 总个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The total of this ShowInstanceNodesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowInstanceNodesResponse.

        **参数解释**： 总个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param total: The total of this ShowInstanceNodesResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ShowInstanceNodesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowInstanceNodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
