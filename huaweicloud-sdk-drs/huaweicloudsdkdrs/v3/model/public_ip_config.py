# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicIpConfig:

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
        'public_ip': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'public_ip': 'public_ip',
        'type': 'type'
    }

    def __init__(self, id=None, public_ip=None, type=None):
        r"""PublicIpConfig

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  指定公网IP的ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type id: str
        :param public_ip: **参数解释**：  指定公网IP地址。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type public_ip: str
        :param type: **参数解释**：  指定公网IP绑定任务的类型。  **约束限制**：  不涉及。  **取值范围**：  - master：主任务或单任务的公网IP - slave：备任务的公网IP  **默认取值**：  不涉及
        :type type: str
        """
        
        

        self._id = None
        self._public_ip = None
        self._type = None
        self.discriminator = None

        self.id = id
        self.public_ip = public_ip
        self.type = type

    @property
    def id(self):
        r"""Gets the id of this PublicIpConfig.

        **参数解释**：  指定公网IP的ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The id of this PublicIpConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PublicIpConfig.

        **参数解释**：  指定公网IP的ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param id: The id of this PublicIpConfig.
        :type id: str
        """
        self._id = id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this PublicIpConfig.

        **参数解释**：  指定公网IP地址。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The public_ip of this PublicIpConfig.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this PublicIpConfig.

        **参数解释**：  指定公网IP地址。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param public_ip: The public_ip of this PublicIpConfig.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def type(self):
        r"""Gets the type of this PublicIpConfig.

        **参数解释**：  指定公网IP绑定任务的类型。  **约束限制**：  不涉及。  **取值范围**：  - master：主任务或单任务的公网IP - slave：备任务的公网IP  **默认取值**：  不涉及

        :return: The type of this PublicIpConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PublicIpConfig.

        **参数解释**：  指定公网IP绑定任务的类型。  **约束限制**：  不涉及。  **取值范围**：  - master：主任务或单任务的公网IP - slave：备任务的公网IP  **默认取值**：  不涉及

        :param type: The type of this PublicIpConfig.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, PublicIpConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
