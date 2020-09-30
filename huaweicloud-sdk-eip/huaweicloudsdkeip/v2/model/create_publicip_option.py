# coding: utf-8

import pprint
import re

import six





class CreatePublicipOption:


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
        'type': 'str',
        'ip_version': 'int'
    }

    attribute_map = {
        'ip_address': 'ip_address',
        'type': 'type',
        'ip_version': 'ip_version'
    }

    def __init__(self, ip_address=None, type=None, ip_version=4):
        """CreatePublicipOption - a model defined in huaweicloud sdk"""
        
        

        self._ip_address = None
        self._type = None
        self._ip_version = None
        self.discriminator = None

        if ip_address is not None:
            self.ip_address = ip_address
        self.type = type
        if ip_version is not None:
            self.ip_version = ip_version

    @property
    def ip_address(self):
        """Gets the ip_address of this CreatePublicipOption.

        功能说明：希望申请到的弹性公网IP的地址，不指定时由系统自动分配  约束：必须为IP地址格式，且必须在可用地址池范围内

        :return: The ip_address of this CreatePublicipOption.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this CreatePublicipOption.

        功能说明：希望申请到的弹性公网IP的地址，不指定时由系统自动分配  约束：必须为IP地址格式，且必须在可用地址池范围内

        :param ip_address: The ip_address of this CreatePublicipOption.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def type(self):
        """Gets the type of this CreatePublicipOption.

        功能说明：弹性公网IP的类型  取值范围：5_telcom（电信），5_union（联通），5_bgp（全动态BGP），5_sbgp（静态BGP），5_ipv6  东北-大连：5_telcom、5_union  华南-广州：5_bgp、5_sbgp  华东-上海二：5_bgp、5_sbgp  华北-北京一：5_bgp、5_sbgp、5_ipv6  亚太-香港：5_bgp  亚太-曼谷：5_bgp  亚太-新加坡：5_bgp  非洲-约翰内斯堡：5_bgp  西南-贵阳一：5_bgp、5_sbgp  华北-北京四：5_bgp、5_sbgp  约束：必须是系统具体支持的类型。  publicip_id为IPv4端口，所以\"publicip_type\"字段未给定时，默认为5_bgp。

        :return: The type of this CreatePublicipOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreatePublicipOption.

        功能说明：弹性公网IP的类型  取值范围：5_telcom（电信），5_union（联通），5_bgp（全动态BGP），5_sbgp（静态BGP），5_ipv6  东北-大连：5_telcom、5_union  华南-广州：5_bgp、5_sbgp  华东-上海二：5_bgp、5_sbgp  华北-北京一：5_bgp、5_sbgp、5_ipv6  亚太-香港：5_bgp  亚太-曼谷：5_bgp  亚太-新加坡：5_bgp  非洲-约翰内斯堡：5_bgp  西南-贵阳一：5_bgp、5_sbgp  华北-北京四：5_bgp、5_sbgp  约束：必须是系统具体支持的类型。  publicip_id为IPv4端口，所以\"publicip_type\"字段未给定时，默认为5_bgp。

        :param type: The type of this CreatePublicipOption.
        :type: str
        """
        self._type = type

    @property
    def ip_version(self):
        """Gets the ip_version of this CreatePublicipOption.

        功能说明：弹性IP弹性公网IP的版本  取值范围：4、6，分别表示创建ipv4和ipv6  约束：必须是系统具体支持的类型  不填或空字符串时，默认创建ipv4

        :return: The ip_version of this CreatePublicipOption.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this CreatePublicipOption.

        功能说明：弹性IP弹性公网IP的版本  取值范围：4、6，分别表示创建ipv4和ipv6  约束：必须是系统具体支持的类型  不填或空字符串时，默认创建ipv4

        :param ip_version: The ip_version of this CreatePublicipOption.
        :type: int
        """
        self._ip_version = ip_version

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
        if not isinstance(other, CreatePublicipOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
