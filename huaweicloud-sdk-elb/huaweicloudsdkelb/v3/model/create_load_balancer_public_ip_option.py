# coding: utf-8

import pprint
import re

import six





class CreateLoadBalancerPublicIpOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ip_version': 'int',
        'network_type': 'str',
        'billing_info': 'str',
        'description': 'str',
        'bandwidth': 'CreateLoadBalancerBandwidthOption'
    }

    attribute_map = {
        'ip_version': 'ip_version',
        'network_type': 'network_type',
        'billing_info': 'billing_info',
        'description': 'description',
        'bandwidth': 'bandwidth'
    }

    def __init__(self, ip_version=4, network_type=None, billing_info=None, description=None, bandwidth=None):
        """CreateLoadBalancerPublicIpOption - a model defined in huaweicloud sdk"""
        
        

        self._ip_version = None
        self._network_type = None
        self._billing_info = None
        self._description = None
        self._bandwidth = None
        self.discriminator = None

        if ip_version is not None:
            self.ip_version = ip_version
        self.network_type = network_type
        if billing_info is not None:
            self.billing_info = billing_info
        if description is not None:
            self.description = description
        self.bandwidth = bandwidth

    @property
    def ip_version(self):
        """Gets the ip_version of this CreateLoadBalancerPublicIpOption.

        ip版数。 有效值：4表示IPv4，暂不支持新建IPv6

        :return: The ip_version of this CreateLoadBalancerPublicIpOption.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this CreateLoadBalancerPublicIpOption.

        ip版数。 有效值：4表示IPv4，暂不支持新建IPv6

        :param ip_version: The ip_version of this CreateLoadBalancerPublicIpOption.
        :type: int
        """
        self._ip_version = ip_version

    @property
    def network_type(self):
        """Gets the network_type of this CreateLoadBalancerPublicIpOption.

        弹性公网IP的网络类型，默认5_bgp，更多请参考弹性公网ip创建

        :return: The network_type of this CreateLoadBalancerPublicIpOption.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this CreateLoadBalancerPublicIpOption.

        弹性公网IP的网络类型，默认5_bgp，更多请参考弹性公网ip创建

        :param network_type: The network_type of this CreateLoadBalancerPublicIpOption.
        :type: str
        """
        self._network_type = network_type

    @property
    def billing_info(self):
        """Gets the billing_info of this CreateLoadBalancerPublicIpOption.

        账单信息 如果billinginfo不为空,说明是包周期的带宽

        :return: The billing_info of this CreateLoadBalancerPublicIpOption.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this CreateLoadBalancerPublicIpOption.

        账单信息 如果billinginfo不为空,说明是包周期的带宽

        :param billing_info: The billing_info of this CreateLoadBalancerPublicIpOption.
        :type: str
        """
        self._billing_info = billing_info

    @property
    def description(self):
        """Gets the description of this CreateLoadBalancerPublicIpOption.

        弹性公网IP的描述信息，不支持特殊字符

        :return: The description of this CreateLoadBalancerPublicIpOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateLoadBalancerPublicIpOption.

        弹性公网IP的描述信息，不支持特殊字符

        :param description: The description of this CreateLoadBalancerPublicIpOption.
        :type: str
        """
        self._description = description

    @property
    def bandwidth(self):
        """Gets the bandwidth of this CreateLoadBalancerPublicIpOption.


        :return: The bandwidth of this CreateLoadBalancerPublicIpOption.
        :rtype: CreateLoadBalancerBandwidthOption
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this CreateLoadBalancerPublicIpOption.


        :param bandwidth: The bandwidth of this CreateLoadBalancerPublicIpOption.
        :type: CreateLoadBalancerBandwidthOption
        """
        self._bandwidth = bandwidth

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
        if not isinstance(other, CreateLoadBalancerPublicIpOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
