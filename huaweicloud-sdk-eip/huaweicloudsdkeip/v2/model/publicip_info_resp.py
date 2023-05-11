# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicipInfoResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip_address': 'str',
        'publicip_id': 'str',
        'publicip_type': 'str',
        'publicipv6_address': 'str',
        'ip_version': 'int'
    }

    attribute_map = {
        'publicip_address': 'publicip_address',
        'publicip_id': 'publicip_id',
        'publicip_type': 'publicip_type',
        'publicipv6_address': 'publicipv6_address',
        'ip_version': 'ip_version'
    }

    def __init__(self, publicip_address=None, publicip_id=None, publicip_type=None, publicipv6_address=None, ip_version=None):
        """PublicipInfoResp

        The model defined in huaweicloud sdk

        :param publicip_address: 功能说明：弹性公网IP或者IPv6端口的地址
        :type publicip_address: str
        :param publicip_id: 功能说明：带宽对应的弹性公网IP或者IPv6端口的唯一标识
        :type publicip_id: str
        :param publicip_type: 功能说明：弹性公网IP或者IPv6端口的类型  取值范围：5_telcom（电信），5_union（联通），5_bgp（全动态BGP），5_sbgp（静态BGP），5_ipv6  东北-大连：5_telcom、5_union  华南-广州：5_bgp、5_sbgp  华东-上海二：5_bgp、5_sbgp  华北-北京一：5_bgp、5_sbgp、5_ipv6  亚太-香港：5_bgp  亚太-曼谷：5_bgp  亚太-新加坡：5_bgp  非洲-约翰内斯堡：5_bgp  西南-贵阳一：5_bgp、5_sbgp  华北-北京四：5_bgp、5_sbgp  约束：必须是系统具体支持的类型
        :type publicip_type: str
        :param publicipv6_address: 功能说明：IPv4时无此字段，IPv6时为申请到的弹性公网IP地址
        :type publicipv6_address: str
        :param ip_version: IP版本信息  取值范围：  4：IPv4  6：IPv6
        :type ip_version: int
        """
        
        

        self._publicip_address = None
        self._publicip_id = None
        self._publicip_type = None
        self._publicipv6_address = None
        self._ip_version = None
        self.discriminator = None

        if publicip_address is not None:
            self.publicip_address = publicip_address
        if publicip_id is not None:
            self.publicip_id = publicip_id
        if publicip_type is not None:
            self.publicip_type = publicip_type
        if publicipv6_address is not None:
            self.publicipv6_address = publicipv6_address
        if ip_version is not None:
            self.ip_version = ip_version

    @property
    def publicip_address(self):
        """Gets the publicip_address of this PublicipInfoResp.

        功能说明：弹性公网IP或者IPv6端口的地址

        :return: The publicip_address of this PublicipInfoResp.
        :rtype: str
        """
        return self._publicip_address

    @publicip_address.setter
    def publicip_address(self, publicip_address):
        """Sets the publicip_address of this PublicipInfoResp.

        功能说明：弹性公网IP或者IPv6端口的地址

        :param publicip_address: The publicip_address of this PublicipInfoResp.
        :type publicip_address: str
        """
        self._publicip_address = publicip_address

    @property
    def publicip_id(self):
        """Gets the publicip_id of this PublicipInfoResp.

        功能说明：带宽对应的弹性公网IP或者IPv6端口的唯一标识

        :return: The publicip_id of this PublicipInfoResp.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this PublicipInfoResp.

        功能说明：带宽对应的弹性公网IP或者IPv6端口的唯一标识

        :param publicip_id: The publicip_id of this PublicipInfoResp.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def publicip_type(self):
        """Gets the publicip_type of this PublicipInfoResp.

        功能说明：弹性公网IP或者IPv6端口的类型  取值范围：5_telcom（电信），5_union（联通），5_bgp（全动态BGP），5_sbgp（静态BGP），5_ipv6  东北-大连：5_telcom、5_union  华南-广州：5_bgp、5_sbgp  华东-上海二：5_bgp、5_sbgp  华北-北京一：5_bgp、5_sbgp、5_ipv6  亚太-香港：5_bgp  亚太-曼谷：5_bgp  亚太-新加坡：5_bgp  非洲-约翰内斯堡：5_bgp  西南-贵阳一：5_bgp、5_sbgp  华北-北京四：5_bgp、5_sbgp  约束：必须是系统具体支持的类型

        :return: The publicip_type of this PublicipInfoResp.
        :rtype: str
        """
        return self._publicip_type

    @publicip_type.setter
    def publicip_type(self, publicip_type):
        """Sets the publicip_type of this PublicipInfoResp.

        功能说明：弹性公网IP或者IPv6端口的类型  取值范围：5_telcom（电信），5_union（联通），5_bgp（全动态BGP），5_sbgp（静态BGP），5_ipv6  东北-大连：5_telcom、5_union  华南-广州：5_bgp、5_sbgp  华东-上海二：5_bgp、5_sbgp  华北-北京一：5_bgp、5_sbgp、5_ipv6  亚太-香港：5_bgp  亚太-曼谷：5_bgp  亚太-新加坡：5_bgp  非洲-约翰内斯堡：5_bgp  西南-贵阳一：5_bgp、5_sbgp  华北-北京四：5_bgp、5_sbgp  约束：必须是系统具体支持的类型

        :param publicip_type: The publicip_type of this PublicipInfoResp.
        :type publicip_type: str
        """
        self._publicip_type = publicip_type

    @property
    def publicipv6_address(self):
        """Gets the publicipv6_address of this PublicipInfoResp.

        功能说明：IPv4时无此字段，IPv6时为申请到的弹性公网IP地址

        :return: The publicipv6_address of this PublicipInfoResp.
        :rtype: str
        """
        return self._publicipv6_address

    @publicipv6_address.setter
    def publicipv6_address(self, publicipv6_address):
        """Sets the publicipv6_address of this PublicipInfoResp.

        功能说明：IPv4时无此字段，IPv6时为申请到的弹性公网IP地址

        :param publicipv6_address: The publicipv6_address of this PublicipInfoResp.
        :type publicipv6_address: str
        """
        self._publicipv6_address = publicipv6_address

    @property
    def ip_version(self):
        """Gets the ip_version of this PublicipInfoResp.

        IP版本信息  取值范围：  4：IPv4  6：IPv6

        :return: The ip_version of this PublicipInfoResp.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this PublicipInfoResp.

        IP版本信息  取值范围：  4：IPv4  6：IPv6

        :param ip_version: The ip_version of this PublicipInfoResp.
        :type ip_version: int
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
        if not isinstance(other, PublicipInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
