# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyKafkaPublicIPAccessSwitchReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip_address': 'str',
        'public_boundwidth': 'int',
        'public_ip_id': 'str'
    }

    attribute_map = {
        'eip_address': 'eip_address',
        'public_boundwidth': 'public_boundwidth',
        'public_ip_id': 'publicIpId'
    }

    def __init__(self, eip_address=None, public_boundwidth=None, public_ip_id=None):
        r"""ModifyKafkaPublicIPAccessSwitchReq

        The model defined in huaweicloud sdk

        :param eip_address: **参数解释**： EIP地址。  **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type eip_address: str
        :param public_boundwidth: **参数解释**： 公网带宽。  **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type public_boundwidth: int
        :param public_ip_id: **参数解释**： 公网IP的ID。  **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type public_ip_id: str
        """
        
        

        self._eip_address = None
        self._public_boundwidth = None
        self._public_ip_id = None
        self.discriminator = None

        if eip_address is not None:
            self.eip_address = eip_address
        if public_boundwidth is not None:
            self.public_boundwidth = public_boundwidth
        if public_ip_id is not None:
            self.public_ip_id = public_ip_id

    @property
    def eip_address(self):
        r"""Gets the eip_address of this ModifyKafkaPublicIPAccessSwitchReq.

        **参数解释**： EIP地址。  **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The eip_address of this ModifyKafkaPublicIPAccessSwitchReq.
        :rtype: str
        """
        return self._eip_address

    @eip_address.setter
    def eip_address(self, eip_address):
        r"""Sets the eip_address of this ModifyKafkaPublicIPAccessSwitchReq.

        **参数解释**： EIP地址。  **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param eip_address: The eip_address of this ModifyKafkaPublicIPAccessSwitchReq.
        :type eip_address: str
        """
        self._eip_address = eip_address

    @property
    def public_boundwidth(self):
        r"""Gets the public_boundwidth of this ModifyKafkaPublicIPAccessSwitchReq.

        **参数解释**： 公网带宽。  **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The public_boundwidth of this ModifyKafkaPublicIPAccessSwitchReq.
        :rtype: int
        """
        return self._public_boundwidth

    @public_boundwidth.setter
    def public_boundwidth(self, public_boundwidth):
        r"""Sets the public_boundwidth of this ModifyKafkaPublicIPAccessSwitchReq.

        **参数解释**： 公网带宽。  **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param public_boundwidth: The public_boundwidth of this ModifyKafkaPublicIPAccessSwitchReq.
        :type public_boundwidth: int
        """
        self._public_boundwidth = public_boundwidth

    @property
    def public_ip_id(self):
        r"""Gets the public_ip_id of this ModifyKafkaPublicIPAccessSwitchReq.

        **参数解释**： 公网IP的ID。  **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The public_ip_id of this ModifyKafkaPublicIPAccessSwitchReq.
        :rtype: str
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        r"""Sets the public_ip_id of this ModifyKafkaPublicIPAccessSwitchReq.

        **参数解释**： 公网IP的ID。  **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param public_ip_id: The public_ip_id of this ModifyKafkaPublicIPAccessSwitchReq.
        :type public_ip_id: str
        """
        self._public_ip_id = public_ip_id

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
        if not isinstance(other, ModifyKafkaPublicIPAccessSwitchReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
