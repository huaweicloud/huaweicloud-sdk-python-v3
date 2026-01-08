# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'protocol': 'str',
        'type': 'str',
        'lb_algorithm': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'protocol': 'protocol',
        'type': 'type',
        'lb_algorithm': 'lb_algorithm'
    }

    def __init__(self, id=None, name=None, protocol=None, type=None, lb_algorithm=None):
        r"""PoolNode

        The model defined in huaweicloud sdk

        :param id: **取值范围**：后端服务器组id。  **取值范围**：不涉及
        :type id: str
        :param name: **取值范围**：后端服务器组名称。  **取值范围**：不涉及
        :type name: str
        :param protocol: **取值范围**：后端服务器组协议。  **取值范围**：不涉及
        :type protocol: str
        :param type: **取值范围**：后端服务器组类型。  **取值范围**：不涉及
        :type type: str
        :param lb_algorithm: **取值范围**：后端服务器组负载均衡算法。  **取值范围**：不涉及
        :type lb_algorithm: str
        """
        
        

        self._id = None
        self._name = None
        self._protocol = None
        self._type = None
        self._lb_algorithm = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.protocol = protocol
        self.type = type
        self.lb_algorithm = lb_algorithm

    @property
    def id(self):
        r"""Gets the id of this PoolNode.

        **取值范围**：后端服务器组id。  **取值范围**：不涉及

        :return: The id of this PoolNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PoolNode.

        **取值范围**：后端服务器组id。  **取值范围**：不涉及

        :param id: The id of this PoolNode.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this PoolNode.

        **取值范围**：后端服务器组名称。  **取值范围**：不涉及

        :return: The name of this PoolNode.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PoolNode.

        **取值范围**：后端服务器组名称。  **取值范围**：不涉及

        :param name: The name of this PoolNode.
        :type name: str
        """
        self._name = name

    @property
    def protocol(self):
        r"""Gets the protocol of this PoolNode.

        **取值范围**：后端服务器组协议。  **取值范围**：不涉及

        :return: The protocol of this PoolNode.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this PoolNode.

        **取值范围**：后端服务器组协议。  **取值范围**：不涉及

        :param protocol: The protocol of this PoolNode.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def type(self):
        r"""Gets the type of this PoolNode.

        **取值范围**：后端服务器组类型。  **取值范围**：不涉及

        :return: The type of this PoolNode.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PoolNode.

        **取值范围**：后端服务器组类型。  **取值范围**：不涉及

        :param type: The type of this PoolNode.
        :type type: str
        """
        self._type = type

    @property
    def lb_algorithm(self):
        r"""Gets the lb_algorithm of this PoolNode.

        **取值范围**：后端服务器组负载均衡算法。  **取值范围**：不涉及

        :return: The lb_algorithm of this PoolNode.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        r"""Sets the lb_algorithm of this PoolNode.

        **取值范围**：后端服务器组负载均衡算法。  **取值范围**：不涉及

        :param lb_algorithm: The lb_algorithm of this PoolNode.
        :type lb_algorithm: str
        """
        self._lb_algorithm = lb_algorithm

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
        if not isinstance(other, PoolNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
