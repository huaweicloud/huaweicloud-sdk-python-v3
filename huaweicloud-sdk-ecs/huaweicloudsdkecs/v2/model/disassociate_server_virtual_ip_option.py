# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateServerVirtualIpOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'subnet_id': 'str',
        'ip_address': 'str',
        'reverse_binding': 'bool'
    }

    attribute_map = {
        'subnet_id': 'subnet_id',
        'ip_address': 'ip_address',
        'reverse_binding': 'reverse_binding'
    }

    def __init__(self, subnet_id=None, ip_address=None, reverse_binding=None):
        """DisassociateServerVirtualIpOption

        The model defined in huaweicloud sdk

        :param subnet_id: 云服务器添加网卡的信息。  约束：解绑虚拟IP时，subnet_id为空字符串
        :type subnet_id: str
        :param ip_address: 网卡即将配置的虚拟IP的地址。  约束：解绑虚拟IP时，ip_address为空字符串
        :type ip_address: str
        :param reverse_binding: 虚拟IP的allowed_address_pairs属性是否添加网卡的IP/Mac对。
        :type reverse_binding: bool
        """
        
        

        self._subnet_id = None
        self._ip_address = None
        self._reverse_binding = None
        self.discriminator = None

        self.subnet_id = subnet_id
        self.ip_address = ip_address
        if reverse_binding is not None:
            self.reverse_binding = reverse_binding

    @property
    def subnet_id(self):
        """Gets the subnet_id of this DisassociateServerVirtualIpOption.

        云服务器添加网卡的信息。  约束：解绑虚拟IP时，subnet_id为空字符串

        :return: The subnet_id of this DisassociateServerVirtualIpOption.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this DisassociateServerVirtualIpOption.

        云服务器添加网卡的信息。  约束：解绑虚拟IP时，subnet_id为空字符串

        :param subnet_id: The subnet_id of this DisassociateServerVirtualIpOption.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def ip_address(self):
        """Gets the ip_address of this DisassociateServerVirtualIpOption.

        网卡即将配置的虚拟IP的地址。  约束：解绑虚拟IP时，ip_address为空字符串

        :return: The ip_address of this DisassociateServerVirtualIpOption.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DisassociateServerVirtualIpOption.

        网卡即将配置的虚拟IP的地址。  约束：解绑虚拟IP时，ip_address为空字符串

        :param ip_address: The ip_address of this DisassociateServerVirtualIpOption.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def reverse_binding(self):
        """Gets the reverse_binding of this DisassociateServerVirtualIpOption.

        虚拟IP的allowed_address_pairs属性是否添加网卡的IP/Mac对。

        :return: The reverse_binding of this DisassociateServerVirtualIpOption.
        :rtype: bool
        """
        return self._reverse_binding

    @reverse_binding.setter
    def reverse_binding(self, reverse_binding):
        """Sets the reverse_binding of this DisassociateServerVirtualIpOption.

        虚拟IP的allowed_address_pairs属性是否添加网卡的IP/Mac对。

        :param reverse_binding: The reverse_binding of this DisassociateServerVirtualIpOption.
        :type reverse_binding: bool
        """
        self._reverse_binding = reverse_binding

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
        if not isinstance(other, DisassociateServerVirtualIpOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
