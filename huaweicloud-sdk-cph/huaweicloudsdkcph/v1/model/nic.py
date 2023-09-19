# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Nic:

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
        'ipv6_enable': 'bool',
        'ipv6_bandwidth': 'NicIpv6Bandwidth'
    }

    attribute_map = {
        'subnet_id': 'subnet_id',
        'ipv6_enable': 'ipv6_enable',
        'ipv6_bandwidth': 'ipv6_bandwidth'
    }

    def __init__(self, subnet_id=None, ipv6_enable=None, ipv6_bandwidth=None):
        """Nic

        The model defined in huaweicloud sdk

        :param subnet_id: 租户自定义的子网 ID，为待创建的云服务器所属的子网。  需要指定tenant_vpc_id对应VPC下已创建的子网（subnet）的网络ID，UUID格式。
        :type subnet_id: str
        :param ipv6_enable: 是否支持ipv6。  取值为true时，标识此网卡支持ipv6。
        :type ipv6_enable: bool
        :param ipv6_bandwidth: 
        :type ipv6_bandwidth: :class:`huaweicloudsdkcph.v1.NicIpv6Bandwidth`
        """
        
        

        self._subnet_id = None
        self._ipv6_enable = None
        self._ipv6_bandwidth = None
        self.discriminator = None

        self.subnet_id = subnet_id
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth

    @property
    def subnet_id(self):
        """Gets the subnet_id of this Nic.

        租户自定义的子网 ID，为待创建的云服务器所属的子网。  需要指定tenant_vpc_id对应VPC下已创建的子网（subnet）的网络ID，UUID格式。

        :return: The subnet_id of this Nic.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this Nic.

        租户自定义的子网 ID，为待创建的云服务器所属的子网。  需要指定tenant_vpc_id对应VPC下已创建的子网（subnet）的网络ID，UUID格式。

        :param subnet_id: The subnet_id of this Nic.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this Nic.

        是否支持ipv6。  取值为true时，标识此网卡支持ipv6。

        :return: The ipv6_enable of this Nic.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this Nic.

        是否支持ipv6。  取值为true时，标识此网卡支持ipv6。

        :param ipv6_enable: The ipv6_enable of this Nic.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def ipv6_bandwidth(self):
        """Gets the ipv6_bandwidth of this Nic.

        :return: The ipv6_bandwidth of this Nic.
        :rtype: :class:`huaweicloudsdkcph.v1.NicIpv6Bandwidth`
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        """Sets the ipv6_bandwidth of this Nic.

        :param ipv6_bandwidth: The ipv6_bandwidth of this Nic.
        :type ipv6_bandwidth: :class:`huaweicloudsdkcph.v1.NicIpv6Bandwidth`
        """
        self._ipv6_bandwidth = ipv6_bandwidth

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
        if not isinstance(other, Nic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
