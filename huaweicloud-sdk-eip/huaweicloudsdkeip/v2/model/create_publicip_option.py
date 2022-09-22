# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'ip_version': 'int',
        'alias': 'str',
        'port_id': 'str'
    }

    attribute_map = {
        'ip_address': 'ip_address',
        'type': 'type',
        'ip_version': 'ip_version',
        'alias': 'alias',
        'port_id': 'port_id'
    }

    def __init__(self, ip_address=None, type=None, ip_version=None, alias=None, port_id=None):
        """CreatePublicipOption

        The model defined in huaweicloud sdk

        :param ip_address: 功能说明：希望申请到的弹性公网IP的地址，不指定时由系统自动分配  约束：必须为IP地址格式，且必须在可用地址池范围内
        :type ip_address: str
        :param type: 功能说明：弹性公网IP的类型  取值范围：5_telcom（电信），5_union（联通），5_bgp（全动态BGP），5_sbgp（静态BGP），5_ipv6  东北-大连：5_telcom、5_union  华南-广州：5_bgp、5_sbgp  华东-上海二：5_bgp、5_sbgp  华北-北京一：5_bgp、5_sbgp、5_ipv6  亚太-香港：5_bgp  亚太-曼谷：5_bgp  亚太-新加坡：5_bgp  非洲-约翰内斯堡：5_bgp  西南-贵阳一：5_bgp、5_sbgp  华北-北京四：5_bgp、5_sbgp  约束：必须是系统具体支持的类型。  publicip_id为IPv4端口，所以\&quot;publicip_type\&quot;字段未给定时，默认为5_bgp。
        :type type: str
        :param ip_version: 功能说明：弹性IP弹性公网IP的版本  取值范围：4、6，分别表示创建ipv4和ipv6  约束：必须是系统具体支持的类型  不填或空字符串时，默认创建ipv4
        :type ip_version: int
        :param alias: 功能说明：弹性公网IP名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type alias: str
        :param port_id: 功能说明：端口id  约束：必须是存在的端口id，如果该端口不存在或端口已绑定EIP则会提示出错。
        :type port_id: str
        """
        
        

        self._ip_address = None
        self._type = None
        self._ip_version = None
        self._alias = None
        self._port_id = None
        self.discriminator = None

        if ip_address is not None:
            self.ip_address = ip_address
        self.type = type
        if ip_version is not None:
            self.ip_version = ip_version
        if alias is not None:
            self.alias = alias
        if port_id is not None:
            self.port_id = port_id

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
        :type ip_address: str
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
        :type type: str
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
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def alias(self):
        """Gets the alias of this CreatePublicipOption.

        功能说明：弹性公网IP名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The alias of this CreatePublicipOption.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this CreatePublicipOption.

        功能说明：弹性公网IP名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param alias: The alias of this CreatePublicipOption.
        :type alias: str
        """
        self._alias = alias

    @property
    def port_id(self):
        """Gets the port_id of this CreatePublicipOption.

        功能说明：端口id  约束：必须是存在的端口id，如果该端口不存在或端口已绑定EIP则会提示出错。

        :return: The port_id of this CreatePublicipOption.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this CreatePublicipOption.

        功能说明：端口id  约束：必须是存在的端口id，如果该端口不存在或端口已绑定EIP则会提示出错。

        :param port_id: The port_id of this CreatePublicipOption.
        :type port_id: str
        """
        self._port_id = port_id

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
        if not isinstance(other, CreatePublicipOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
