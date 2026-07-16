# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetNodesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_names': 'list[str]',
        'rolling_config': 'ResetNodesRequestRollingConfig',
        'node_config': 'ResetNodesRequestNodeConfig'
    }

    attribute_map = {
        'node_names': 'nodeNames',
        'rolling_config': 'rollingConfig',
        'node_config': 'nodeConfig'
    }

    def __init__(self, node_names=None, rolling_config=None, node_config=None):
        r"""ResetNodesRequest

        The model defined in huaweicloud sdk

        :param node_names: **参数解释**：需要重置的节点名称列表。 **约束限制**：不涉及。
        :type node_names: list[str]
        :param rolling_config: 
        :type rolling_config: :class:`huaweicloudsdkmodelarts.v1.ResetNodesRequestRollingConfig`
        :param node_config: 
        :type node_config: :class:`huaweicloudsdkmodelarts.v1.ResetNodesRequestNodeConfig`
        """
        
        

        self._node_names = None
        self._rolling_config = None
        self._node_config = None
        self.discriminator = None

        self.node_names = node_names
        self.rolling_config = rolling_config
        if node_config is not None:
            self.node_config = node_config

    @property
    def node_names(self):
        r"""Gets the node_names of this ResetNodesRequest.

        **参数解释**：需要重置的节点名称列表。 **约束限制**：不涉及。

        :return: The node_names of this ResetNodesRequest.
        :rtype: list[str]
        """
        return self._node_names

    @node_names.setter
    def node_names(self, node_names):
        r"""Sets the node_names of this ResetNodesRequest.

        **参数解释**：需要重置的节点名称列表。 **约束限制**：不涉及。

        :param node_names: The node_names of this ResetNodesRequest.
        :type node_names: list[str]
        """
        self._node_names = node_names

    @property
    def rolling_config(self):
        r"""Gets the rolling_config of this ResetNodesRequest.

        :return: The rolling_config of this ResetNodesRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ResetNodesRequestRollingConfig`
        """
        return self._rolling_config

    @rolling_config.setter
    def rolling_config(self, rolling_config):
        r"""Sets the rolling_config of this ResetNodesRequest.

        :param rolling_config: The rolling_config of this ResetNodesRequest.
        :type rolling_config: :class:`huaweicloudsdkmodelarts.v1.ResetNodesRequestRollingConfig`
        """
        self._rolling_config = rolling_config

    @property
    def node_config(self):
        r"""Gets the node_config of this ResetNodesRequest.

        :return: The node_config of this ResetNodesRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ResetNodesRequestNodeConfig`
        """
        return self._node_config

    @node_config.setter
    def node_config(self, node_config):
        r"""Sets the node_config of this ResetNodesRequest.

        :param node_config: The node_config of this ResetNodesRequest.
        :type node_config: :class:`huaweicloudsdkmodelarts.v1.ResetNodesRequestNodeConfig`
        """
        self._node_config = node_config

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
        if not isinstance(other, ResetNodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
