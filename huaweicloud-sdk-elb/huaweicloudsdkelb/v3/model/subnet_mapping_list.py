# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubnetMappingList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subnet_cidr_id': 'str',
        'dst_subnet_cidr_id': 'str'
    }

    attribute_map = {
        'subnet_cidr_id': 'subnet_cidr_id',
        'dst_subnet_cidr_id': 'dst_subnet_cidr_id'
    }

    def __init__(self, subnet_cidr_id=None, dst_subnet_cidr_id=None):
        r"""SubnetMappingList

        The model defined in huaweicloud sdk

        :param subnet_cidr_id: **参数解释**：源监听器下后端服务器所在VPC的子网ID。  **约束限制**：不涉及  **取值范围**：标准的UUID格式，长度为36个字符。  **默认取值**：不涉及
        :type subnet_cidr_id: str
        :param dst_subnet_cidr_id: **参数解释**：新监听器下后端服务器需要绑定的VPC子网ID。  **约束限制**：该VPC子网ID需要存在，且与源子网网段相同。  **取值范围**：标准的UUID格式，长度为36个字符。  **默认取值**：不涉及
        :type dst_subnet_cidr_id: str
        """
        
        

        self._subnet_cidr_id = None
        self._dst_subnet_cidr_id = None
        self.discriminator = None

        self.subnet_cidr_id = subnet_cidr_id
        self.dst_subnet_cidr_id = dst_subnet_cidr_id

    @property
    def subnet_cidr_id(self):
        r"""Gets the subnet_cidr_id of this SubnetMappingList.

        **参数解释**：源监听器下后端服务器所在VPC的子网ID。  **约束限制**：不涉及  **取值范围**：标准的UUID格式，长度为36个字符。  **默认取值**：不涉及

        :return: The subnet_cidr_id of this SubnetMappingList.
        :rtype: str
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        r"""Sets the subnet_cidr_id of this SubnetMappingList.

        **参数解释**：源监听器下后端服务器所在VPC的子网ID。  **约束限制**：不涉及  **取值范围**：标准的UUID格式，长度为36个字符。  **默认取值**：不涉及

        :param subnet_cidr_id: The subnet_cidr_id of this SubnetMappingList.
        :type subnet_cidr_id: str
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def dst_subnet_cidr_id(self):
        r"""Gets the dst_subnet_cidr_id of this SubnetMappingList.

        **参数解释**：新监听器下后端服务器需要绑定的VPC子网ID。  **约束限制**：该VPC子网ID需要存在，且与源子网网段相同。  **取值范围**：标准的UUID格式，长度为36个字符。  **默认取值**：不涉及

        :return: The dst_subnet_cidr_id of this SubnetMappingList.
        :rtype: str
        """
        return self._dst_subnet_cidr_id

    @dst_subnet_cidr_id.setter
    def dst_subnet_cidr_id(self, dst_subnet_cidr_id):
        r"""Sets the dst_subnet_cidr_id of this SubnetMappingList.

        **参数解释**：新监听器下后端服务器需要绑定的VPC子网ID。  **约束限制**：该VPC子网ID需要存在，且与源子网网段相同。  **取值范围**：标准的UUID格式，长度为36个字符。  **默认取值**：不涉及

        :param dst_subnet_cidr_id: The dst_subnet_cidr_id of this SubnetMappingList.
        :type dst_subnet_cidr_id: str
        """
        self._dst_subnet_cidr_id = dst_subnet_cidr_id

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
        if not isinstance(other, SubnetMappingList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
