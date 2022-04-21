# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerInterfaceFixedIp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ip_address': 'str',
        'subnet_id': 'str'
    }

    attribute_map = {
        'ip_address': 'ip_address',
        'subnet_id': 'subnet_id'
    }

    def __init__(self, ip_address=None, subnet_id=None):
        """ServerInterfaceFixedIp

        The model defined in huaweicloud sdk

        :param ip_address: 网卡私网IP信息。
        :type ip_address: str
        :param subnet_id: 网卡私网IP对应子网信息。
        :type subnet_id: str
        """
        
        

        self._ip_address = None
        self._subnet_id = None
        self.discriminator = None

        if ip_address is not None:
            self.ip_address = ip_address
        if subnet_id is not None:
            self.subnet_id = subnet_id

    @property
    def ip_address(self):
        """Gets the ip_address of this ServerInterfaceFixedIp.

        网卡私网IP信息。

        :return: The ip_address of this ServerInterfaceFixedIp.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this ServerInterfaceFixedIp.

        网卡私网IP信息。

        :param ip_address: The ip_address of this ServerInterfaceFixedIp.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ServerInterfaceFixedIp.

        网卡私网IP对应子网信息。

        :return: The subnet_id of this ServerInterfaceFixedIp.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ServerInterfaceFixedIp.

        网卡私网IP对应子网信息。

        :param subnet_id: The subnet_id of this ServerInterfaceFixedIp.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

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
        if not isinstance(other, ServerInterfaceFixedIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
