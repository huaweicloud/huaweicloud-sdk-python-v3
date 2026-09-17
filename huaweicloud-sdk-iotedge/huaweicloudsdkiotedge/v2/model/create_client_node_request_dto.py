# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClientNodeRequestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_node_id': 'str'
    }

    attribute_map = {
        'client_node_id': 'client_node_id'
    }

    def __init__(self, client_node_id=None):
        r"""CreateClientNodeRequestDTO

        The model defined in huaweicloud sdk

        :param client_node_id: 客户端节点ID，即边缘节点ID
        :type client_node_id: str
        """
        
        

        self._client_node_id = None
        self.discriminator = None

        self.client_node_id = client_node_id

    @property
    def client_node_id(self):
        r"""Gets the client_node_id of this CreateClientNodeRequestDTO.

        客户端节点ID，即边缘节点ID

        :return: The client_node_id of this CreateClientNodeRequestDTO.
        :rtype: str
        """
        return self._client_node_id

    @client_node_id.setter
    def client_node_id(self, client_node_id):
        r"""Sets the client_node_id of this CreateClientNodeRequestDTO.

        客户端节点ID，即边缘节点ID

        :param client_node_id: The client_node_id of this CreateClientNodeRequestDTO.
        :type client_node_id: str
        """
        self._client_node_id = client_node_id

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
        if not isinstance(other, CreateClientNodeRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
