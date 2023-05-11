# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubnetIpAvailability:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'used_ips': 'int',
        'subnet_id': 'str',
        'subnet_name': 'str',
        'ip_version': 'int',
        'cidr': 'str',
        'total_ips': 'int'
    }

    attribute_map = {
        'used_ips': 'used_ips',
        'subnet_id': 'subnet_id',
        'subnet_name': 'subnet_name',
        'ip_version': 'ip_version',
        'cidr': 'cidr',
        'total_ips': 'total_ips'
    }

    def __init__(self, used_ips=None, subnet_id=None, subnet_name=None, ip_version=None, cidr=None, total_ips=None):
        """SubnetIpAvailability

        The model defined in huaweicloud sdk

        :param used_ips: 子网中已经使用的IP数目（不包含系统预留地址）
        :type used_ips: int
        :param subnet_id: 子网ID
        :type subnet_id: str
        :param subnet_name: 子网名称
        :type subnet_name: str
        :param ip_version: 子网的IP版本，取值为4或者6
        :type ip_version: int
        :param cidr: 子网的CIDR
        :type cidr: str
        :param total_ips: 子网中IP总数（不包含系统预留地址）
        :type total_ips: int
        """
        
        

        self._used_ips = None
        self._subnet_id = None
        self._subnet_name = None
        self._ip_version = None
        self._cidr = None
        self._total_ips = None
        self.discriminator = None

        self.used_ips = used_ips
        self.subnet_id = subnet_id
        self.subnet_name = subnet_name
        self.ip_version = ip_version
        self.cidr = cidr
        self.total_ips = total_ips

    @property
    def used_ips(self):
        """Gets the used_ips of this SubnetIpAvailability.

        子网中已经使用的IP数目（不包含系统预留地址）

        :return: The used_ips of this SubnetIpAvailability.
        :rtype: int
        """
        return self._used_ips

    @used_ips.setter
    def used_ips(self, used_ips):
        """Sets the used_ips of this SubnetIpAvailability.

        子网中已经使用的IP数目（不包含系统预留地址）

        :param used_ips: The used_ips of this SubnetIpAvailability.
        :type used_ips: int
        """
        self._used_ips = used_ips

    @property
    def subnet_id(self):
        """Gets the subnet_id of this SubnetIpAvailability.

        子网ID

        :return: The subnet_id of this SubnetIpAvailability.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this SubnetIpAvailability.

        子网ID

        :param subnet_id: The subnet_id of this SubnetIpAvailability.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def subnet_name(self):
        """Gets the subnet_name of this SubnetIpAvailability.

        子网名称

        :return: The subnet_name of this SubnetIpAvailability.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        """Sets the subnet_name of this SubnetIpAvailability.

        子网名称

        :param subnet_name: The subnet_name of this SubnetIpAvailability.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def ip_version(self):
        """Gets the ip_version of this SubnetIpAvailability.

        子网的IP版本，取值为4或者6

        :return: The ip_version of this SubnetIpAvailability.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this SubnetIpAvailability.

        子网的IP版本，取值为4或者6

        :param ip_version: The ip_version of this SubnetIpAvailability.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def cidr(self):
        """Gets the cidr of this SubnetIpAvailability.

        子网的CIDR

        :return: The cidr of this SubnetIpAvailability.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this SubnetIpAvailability.

        子网的CIDR

        :param cidr: The cidr of this SubnetIpAvailability.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def total_ips(self):
        """Gets the total_ips of this SubnetIpAvailability.

        子网中IP总数（不包含系统预留地址）

        :return: The total_ips of this SubnetIpAvailability.
        :rtype: int
        """
        return self._total_ips

    @total_ips.setter
    def total_ips(self, total_ips):
        """Sets the total_ips of this SubnetIpAvailability.

        子网中IP总数（不包含系统预留地址）

        :param total_ips: The total_ips of this SubnetIpAvailability.
        :type total_ips: int
        """
        self._total_ips = total_ips

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
        if not isinstance(other, SubnetIpAvailability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
