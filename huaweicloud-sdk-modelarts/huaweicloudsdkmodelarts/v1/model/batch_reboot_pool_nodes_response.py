# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchRebootPoolNodesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_names': 'list[str]'
    }

    attribute_map = {
        'node_names': 'nodeNames'
    }

    def __init__(self, node_names=None):
        r"""BatchRebootPoolNodesResponse

        The model defined in huaweicloud sdk

        :param node_names: **参数解释**：节点名称集合。 **约束限制**：不涉及。
        :type node_names: list[str]
        """
        
        super().__init__()

        self._node_names = None
        self.discriminator = None

        self.node_names = node_names

    @property
    def node_names(self):
        r"""Gets the node_names of this BatchRebootPoolNodesResponse.

        **参数解释**：节点名称集合。 **约束限制**：不涉及。

        :return: The node_names of this BatchRebootPoolNodesResponse.
        :rtype: list[str]
        """
        return self._node_names

    @node_names.setter
    def node_names(self, node_names):
        r"""Sets the node_names of this BatchRebootPoolNodesResponse.

        **参数解释**：节点名称集合。 **约束限制**：不涉及。

        :param node_names: The node_names of this BatchRebootPoolNodesResponse.
        :type node_names: list[str]
        """
        self._node_names = node_names

    def to_dict(self):
        import warnings
        warnings.warn("BatchRebootPoolNodesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchRebootPoolNodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
