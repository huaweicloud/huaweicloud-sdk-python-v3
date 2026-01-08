# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EipNode:

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
        'ip_address': 'str',
        'ip_version': 'int'
    }

    attribute_map = {
        'id': 'id',
        'ip_address': 'ip_address',
        'ip_version': 'ip_version'
    }

    def __init__(self, id=None, ip_address=None, ip_version=None):
        r"""EipNode

        The model defined in huaweicloud sdk

        :param id: **参数解释**：不涉及EIP id。  **取值范围**：不涉及
        :type id: str
        :param ip_address: **参数解释**：EIP地址。  **取值范围**：不涉及
        :type ip_address: str
        :param ip_version: **参数解释**：EIP 地址类型。  **取值范围**：不涉及 - 4：ipv4。 - 6：ipv6
        :type ip_version: int
        """
        
        

        self._id = None
        self._ip_address = None
        self._ip_version = None
        self.discriminator = None

        self.id = id
        self.ip_address = ip_address
        self.ip_version = ip_version

    @property
    def id(self):
        r"""Gets the id of this EipNode.

        **参数解释**：不涉及EIP id。  **取值范围**：不涉及

        :return: The id of this EipNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EipNode.

        **参数解释**：不涉及EIP id。  **取值范围**：不涉及

        :param id: The id of this EipNode.
        :type id: str
        """
        self._id = id

    @property
    def ip_address(self):
        r"""Gets the ip_address of this EipNode.

        **参数解释**：EIP地址。  **取值范围**：不涉及

        :return: The ip_address of this EipNode.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this EipNode.

        **参数解释**：EIP地址。  **取值范围**：不涉及

        :param ip_address: The ip_address of this EipNode.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def ip_version(self):
        r"""Gets the ip_version of this EipNode.

        **参数解释**：EIP 地址类型。  **取值范围**：不涉及 - 4：ipv4。 - 6：ipv6

        :return: The ip_version of this EipNode.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this EipNode.

        **参数解释**：EIP 地址类型。  **取值范围**：不涉及 - 4：ipv4。 - 6：ipv6

        :param ip_version: The ip_version of this EipNode.
        :type ip_version: int
        """
        self._ip_version = ip_version

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
        if not isinstance(other, EipNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
