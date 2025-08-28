# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProxyProtocolExtension:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vip_address': 'str',
        'ipv6_vip_address': 'str',
        'extension': 'Extension'
    }

    attribute_map = {
        'vip_address': 'vip_address',
        'ipv6_vip_address': 'ipv6_vip_address',
        'extension': 'extension'
    }

    def __init__(self, vip_address=None, ipv6_vip_address=None, extension=None):
        r"""ProxyProtocolExtension

        The model defined in huaweicloud sdk

        :param vip_address: **参数解释**：ipv4 vip地址。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type vip_address: str
        :param ipv6_vip_address: **参数解释**：ipv6 vip地址。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type ipv6_vip_address: str
        :param extension: 
        :type extension: :class:`huaweicloudsdkelb.v3.Extension`
        """
        
        

        self._vip_address = None
        self._ipv6_vip_address = None
        self._extension = None
        self.discriminator = None

        if vip_address is not None:
            self.vip_address = vip_address
        if ipv6_vip_address is not None:
            self.ipv6_vip_address = ipv6_vip_address
        self.extension = extension

    @property
    def vip_address(self):
        r"""Gets the vip_address of this ProxyProtocolExtension.

        **参数解释**：ipv4 vip地址。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The vip_address of this ProxyProtocolExtension.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        r"""Sets the vip_address of this ProxyProtocolExtension.

        **参数解释**：ipv4 vip地址。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param vip_address: The vip_address of this ProxyProtocolExtension.
        :type vip_address: str
        """
        self._vip_address = vip_address

    @property
    def ipv6_vip_address(self):
        r"""Gets the ipv6_vip_address of this ProxyProtocolExtension.

        **参数解释**：ipv6 vip地址。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The ipv6_vip_address of this ProxyProtocolExtension.
        :rtype: str
        """
        return self._ipv6_vip_address

    @ipv6_vip_address.setter
    def ipv6_vip_address(self, ipv6_vip_address):
        r"""Sets the ipv6_vip_address of this ProxyProtocolExtension.

        **参数解释**：ipv6 vip地址。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param ipv6_vip_address: The ipv6_vip_address of this ProxyProtocolExtension.
        :type ipv6_vip_address: str
        """
        self._ipv6_vip_address = ipv6_vip_address

    @property
    def extension(self):
        r"""Gets the extension of this ProxyProtocolExtension.

        :return: The extension of this ProxyProtocolExtension.
        :rtype: :class:`huaweicloudsdkelb.v3.Extension`
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        r"""Sets the extension of this ProxyProtocolExtension.

        :param extension: The extension of this ProxyProtocolExtension.
        :type extension: :class:`huaweicloudsdkelb.v3.Extension`
        """
        self._extension = extension

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProxyProtocolExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
