# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerPhyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'network_nodes': 'list[str]'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'network_nodes': 'network_nodes'
    }

    def __init__(self, resource_id=None, network_nodes=None):
        r"""ServerPhyInfo

        The model defined in huaweicloud sdk

        :param resource_id: **参数解释**：Lite Server实例资源ID。 **取值范围**：长度为[8,36]个字符。
        :type resource_id: str
        :param network_nodes: **参数解释**：Tor信息。 **取值范围**：多个ip信息，IPv4格式。
        :type network_nodes: list[str]
        """
        
        

        self._resource_id = None
        self._network_nodes = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if network_nodes is not None:
            self.network_nodes = network_nodes

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ServerPhyInfo.

        **参数解释**：Lite Server实例资源ID。 **取值范围**：长度为[8,36]个字符。

        :return: The resource_id of this ServerPhyInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ServerPhyInfo.

        **参数解释**：Lite Server实例资源ID。 **取值范围**：长度为[8,36]个字符。

        :param resource_id: The resource_id of this ServerPhyInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def network_nodes(self):
        r"""Gets the network_nodes of this ServerPhyInfo.

        **参数解释**：Tor信息。 **取值范围**：多个ip信息，IPv4格式。

        :return: The network_nodes of this ServerPhyInfo.
        :rtype: list[str]
        """
        return self._network_nodes

    @network_nodes.setter
    def network_nodes(self, network_nodes):
        r"""Sets the network_nodes of this ServerPhyInfo.

        **参数解释**：Tor信息。 **取值范围**：多个ip信息，IPv4格式。

        :param network_nodes: The network_nodes of this ServerPhyInfo.
        :type network_nodes: list[str]
        """
        self._network_nodes = network_nodes

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
        if not isinstance(other, ServerPhyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
