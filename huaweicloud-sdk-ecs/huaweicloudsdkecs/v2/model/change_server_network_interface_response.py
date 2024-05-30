# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeServerNetworkInterfaceResponse(SdkResponse):

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
        'subnet_id': 'str',
        'ip_address': 'str',
        'ipv6_address': 'str'
    }

    attribute_map = {
        'id': 'id',
        'subnet_id': 'subnet_id',
        'ip_address': 'ip_address',
        'ipv6_address': 'ipv6_address'
    }

    def __init__(self, id=None, subnet_id=None, ip_address=None, ipv6_address=None):
        """ChangeServerNetworkInterfaceResponse

        The model defined in huaweicloud sdk

        :param id: 网卡ID。
        :type id: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param ip_address: 网卡IPv4地址。
        :type ip_address: str
        :param ipv6_address: 网卡IPv6地址，未开通IPv6协议的网卡不返回该字段。
        :type ipv6_address: str
        """
        
        super(ChangeServerNetworkInterfaceResponse, self).__init__()

        self._id = None
        self._subnet_id = None
        self._ip_address = None
        self._ipv6_address = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if ip_address is not None:
            self.ip_address = ip_address
        if ipv6_address is not None:
            self.ipv6_address = ipv6_address

    @property
    def id(self):
        """Gets the id of this ChangeServerNetworkInterfaceResponse.

        网卡ID。

        :return: The id of this ChangeServerNetworkInterfaceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChangeServerNetworkInterfaceResponse.

        网卡ID。

        :param id: The id of this ChangeServerNetworkInterfaceResponse.
        :type id: str
        """
        self._id = id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ChangeServerNetworkInterfaceResponse.

        子网ID。

        :return: The subnet_id of this ChangeServerNetworkInterfaceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ChangeServerNetworkInterfaceResponse.

        子网ID。

        :param subnet_id: The subnet_id of this ChangeServerNetworkInterfaceResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def ip_address(self):
        """Gets the ip_address of this ChangeServerNetworkInterfaceResponse.

        网卡IPv4地址。

        :return: The ip_address of this ChangeServerNetworkInterfaceResponse.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this ChangeServerNetworkInterfaceResponse.

        网卡IPv4地址。

        :param ip_address: The ip_address of this ChangeServerNetworkInterfaceResponse.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def ipv6_address(self):
        """Gets the ipv6_address of this ChangeServerNetworkInterfaceResponse.

        网卡IPv6地址，未开通IPv6协议的网卡不返回该字段。

        :return: The ipv6_address of this ChangeServerNetworkInterfaceResponse.
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """Sets the ipv6_address of this ChangeServerNetworkInterfaceResponse.

        网卡IPv6地址，未开通IPv6协议的网卡不返回该字段。

        :param ipv6_address: The ipv6_address of this ChangeServerNetworkInterfaceResponse.
        :type ipv6_address: str
        """
        self._ipv6_address = ipv6_address

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
        if not isinstance(other, ChangeServerNetworkInterfaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
