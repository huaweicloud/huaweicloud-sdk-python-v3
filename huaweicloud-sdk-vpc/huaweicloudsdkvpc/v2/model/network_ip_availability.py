# coding: utf-8

import pprint
import re

import six





class NetworkIpAvailability:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'network_id': 'str',
        'network_name': 'str',
        'tenant_id': 'str',
        'total_ips': 'int',
        'used_ips': 'int',
        'subnet_ip_availability': 'list[SubnetIpAvailability]'
    }

    attribute_map = {
        'network_id': 'network_id',
        'network_name': 'network_name',
        'tenant_id': 'tenant_id',
        'total_ips': 'total_ips',
        'used_ips': 'used_ips',
        'subnet_ip_availability': 'subnet_ip_availability'
    }

    def __init__(self, network_id=None, network_name=None, tenant_id=None, total_ips=None, used_ips=None, subnet_ip_availability=None):
        """NetworkIpAvailability - a model defined in huaweicloud sdk"""
        
        

        self._network_id = None
        self._network_name = None
        self._tenant_id = None
        self._total_ips = None
        self._used_ips = None
        self._subnet_ip_availability = None
        self.discriminator = None

        self.network_id = network_id
        self.network_name = network_name
        self.tenant_id = tenant_id
        self.total_ips = total_ips
        self.used_ips = used_ips
        self.subnet_ip_availability = subnet_ip_availability

    @property
    def network_id(self):
        """Gets the network_id of this NetworkIpAvailability.

        网络ID

        :return: The network_id of this NetworkIpAvailability.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this NetworkIpAvailability.

        网络ID

        :param network_id: The network_id of this NetworkIpAvailability.
        :type: str
        """
        self._network_id = network_id

    @property
    def network_name(self):
        """Gets the network_name of this NetworkIpAvailability.

        网络名称

        :return: The network_name of this NetworkIpAvailability.
        :rtype: str
        """
        return self._network_name

    @network_name.setter
    def network_name(self, network_name):
        """Sets the network_name of this NetworkIpAvailability.

        网络名称

        :param network_name: The network_name of this NetworkIpAvailability.
        :type: str
        """
        self._network_name = network_name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NetworkIpAvailability.

        项目ID

        :return: The tenant_id of this NetworkIpAvailability.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NetworkIpAvailability.

        项目ID

        :param tenant_id: The tenant_id of this NetworkIpAvailability.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def total_ips(self):
        """Gets the total_ips of this NetworkIpAvailability.

        网络中IP总数（不包含系统预留地址）

        :return: The total_ips of this NetworkIpAvailability.
        :rtype: int
        """
        return self._total_ips

    @total_ips.setter
    def total_ips(self, total_ips):
        """Sets the total_ips of this NetworkIpAvailability.

        网络中IP总数（不包含系统预留地址）

        :param total_ips: The total_ips of this NetworkIpAvailability.
        :type: int
        """
        self._total_ips = total_ips

    @property
    def used_ips(self):
        """Gets the used_ips of this NetworkIpAvailability.

        网络中已经使用的IP数目（不包含系统预留地址）

        :return: The used_ips of this NetworkIpAvailability.
        :rtype: int
        """
        return self._used_ips

    @used_ips.setter
    def used_ips(self, used_ips):
        """Sets the used_ips of this NetworkIpAvailability.

        网络中已经使用的IP数目（不包含系统预留地址）

        :param used_ips: The used_ips of this NetworkIpAvailability.
        :type: int
        """
        self._used_ips = used_ips

    @property
    def subnet_ip_availability(self):
        """Gets the subnet_ip_availability of this NetworkIpAvailability.

        子网IP使用情况的对象

        :return: The subnet_ip_availability of this NetworkIpAvailability.
        :rtype: list[SubnetIpAvailability]
        """
        return self._subnet_ip_availability

    @subnet_ip_availability.setter
    def subnet_ip_availability(self, subnet_ip_availability):
        """Sets the subnet_ip_availability of this NetworkIpAvailability.

        子网IP使用情况的对象

        :param subnet_ip_availability: The subnet_ip_availability of this NetworkIpAvailability.
        :type: list[SubnetIpAvailability]
        """
        self._subnet_ip_availability = subnet_ip_availability

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NetworkIpAvailability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
