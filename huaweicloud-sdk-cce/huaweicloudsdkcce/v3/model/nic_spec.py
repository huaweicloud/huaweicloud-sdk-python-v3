# coding: utf-8

import pprint
import re

import six





class NicSpec:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'fixed_ips': 'list[str]',
        'ip_block': 'str',
        'subnet_id': 'str'
    }

    attribute_map = {
        'fixed_ips': 'fixedIps',
        'ip_block': 'ipBlock',
        'subnet_id': 'subnetId'
    }

    def __init__(self, fixed_ips=None, ip_block=None, subnet_id=None):
        """NicSpec - a model defined in huaweicloud sdk"""
        
        

        self._fixed_ips = None
        self._ip_block = None
        self._subnet_id = None
        self.discriminator = None

        if fixed_ips is not None:
            self.fixed_ips = fixed_ips
        if ip_block is not None:
            self.ip_block = ip_block
        if subnet_id is not None:
            self.subnet_id = subnet_id

    @property
    def fixed_ips(self):
        """Gets the fixed_ips of this NicSpec.

        主网卡的IP将通过fixedIps指定，数量不得大于创建的节点数。fixedIps或ipBlock同时只能指定一个。

        :return: The fixed_ips of this NicSpec.
        :rtype: list[str]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        """Sets the fixed_ips of this NicSpec.

        主网卡的IP将通过fixedIps指定，数量不得大于创建的节点数。fixedIps或ipBlock同时只能指定一个。

        :param fixed_ips: The fixed_ips of this NicSpec.
        :type: list[str]
        """
        self._fixed_ips = fixed_ips

    @property
    def ip_block(self):
        """Gets the ip_block of this NicSpec.

        IP段的CIDR格式，创建的节点IP将属于该IP段内。fixedIps或ipBlock同时只能指定一个。

        :return: The ip_block of this NicSpec.
        :rtype: str
        """
        return self._ip_block

    @ip_block.setter
    def ip_block(self, ip_block):
        """Sets the ip_block of this NicSpec.

        IP段的CIDR格式，创建的节点IP将属于该IP段内。fixedIps或ipBlock同时只能指定一个。

        :param ip_block: The ip_block of this NicSpec.
        :type: str
        """
        self._ip_block = ip_block

    @property
    def subnet_id(self):
        """Gets the subnet_id of this NicSpec.

        网卡所在子网的ID。  

        :return: The subnet_id of this NicSpec.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this NicSpec.

        网卡所在子网的ID。  

        :param subnet_id: The subnet_id of this NicSpec.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NicSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
