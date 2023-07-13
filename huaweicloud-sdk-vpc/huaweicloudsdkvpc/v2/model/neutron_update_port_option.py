# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronUpdatePortOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'security_groups': 'list[str]',
        'allowed_address_pairs': 'list[AllowedAddressPair]',
        'extra_dhcp_opts': 'list[ExtraDhcpOpt]',
        'port_security_enabled': 'bool',
        'bindingvnic_type': 'str',
        'bindingprofile': 'dict(str, object)'
    }

    attribute_map = {
        'name': 'name',
        'security_groups': 'security_groups',
        'allowed_address_pairs': 'allowed_address_pairs',
        'extra_dhcp_opts': 'extra_dhcp_opts',
        'port_security_enabled': 'port_security_enabled',
        'bindingvnic_type': 'binding:vnic_type',
        'bindingprofile': 'binding:profile'
    }

    def __init__(self, name=None, security_groups=None, allowed_address_pairs=None, extra_dhcp_opts=None, port_security_enabled=None, bindingvnic_type=None, bindingprofile=None):
        """NeutronUpdatePortOption

        The model defined in huaweicloud sdk

        :param name: 功能说明：网络的名称 取值范围：0-255个字符
        :type name: str
        :param security_groups: 功能说明：扩展属性：安全组的UUID 例如：\&quot;security_groups\&quot;: [\&quot;a0608cbf-d047-4f54-8b28-cd7b59853fff\&quot;] 约束：不支持更新为空
        :type security_groups: list[str]
        :param allowed_address_pairs: 功能说明：扩展属性：IP/Mac对列表，allow_address_pair参见“allow_address_pair对象”表 约束：  - IP地址不允许为 “0.0.0.0”  - 如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组  - 硬件SDN环境不支持ip_address属性配置为CIDR格式  - 为虚拟IP配置后端ECS场景，allowed_address_pairs中配置的IP地址，必须为ECS网卡已有的IP地址，否则可能会导致虚拟IP通信异常。
        :type allowed_address_pairs: list[:class:`huaweicloudsdkvpc.v2.AllowedAddressPair`]
        :param extra_dhcp_opts: 扩展属性：DHCP的扩展Option
        :type extra_dhcp_opts: list[:class:`huaweicloudsdkvpc.v2.ExtraDhcpOpt`]
        :param port_security_enabled: 功能说明：端口安全使能标记，如果不使能则安全组和dhcp防欺骗不生效，默认为true
        :type port_security_enabled: bool
        :param bindingvnic_type: 绑定的vNIC类型  - normal: 软交换
        :type bindingvnic_type: str
        :param bindingprofile: 功能说明：扩展属性，提供用户设置自定义信息  - internal_elb字段，布尔类型，普通租户可见。只有在创建内网ELB的虚拟IP的网卡时设置为true。普通租户没有权限更改该字段，由系统维护。 举例：{\&quot;internal_elb\&quot;: true}  - disable_security_groups字段，布尔类型，普通租户可见。默认为false，高性能通信场景下，允许指定为true。仅支持创建port和读取时指定。当前仅支持指定为true，不支持指定为false。 举例：{\&quot;disable_security_groups\&quot;：true }，当前仅支持指定为true，不支持指定为false，指定为true时，FWaaS功能不生效。
        :type bindingprofile: dict(str, object)
        """
        
        

        self._name = None
        self._security_groups = None
        self._allowed_address_pairs = None
        self._extra_dhcp_opts = None
        self._port_security_enabled = None
        self._bindingvnic_type = None
        self._bindingprofile = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if security_groups is not None:
            self.security_groups = security_groups
        if allowed_address_pairs is not None:
            self.allowed_address_pairs = allowed_address_pairs
        if extra_dhcp_opts is not None:
            self.extra_dhcp_opts = extra_dhcp_opts
        if port_security_enabled is not None:
            self.port_security_enabled = port_security_enabled
        if bindingvnic_type is not None:
            self.bindingvnic_type = bindingvnic_type
        if bindingprofile is not None:
            self.bindingprofile = bindingprofile

    @property
    def name(self):
        """Gets the name of this NeutronUpdatePortOption.

        功能说明：网络的名称 取值范围：0-255个字符

        :return: The name of this NeutronUpdatePortOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronUpdatePortOption.

        功能说明：网络的名称 取值范围：0-255个字符

        :param name: The name of this NeutronUpdatePortOption.
        :type name: str
        """
        self._name = name

    @property
    def security_groups(self):
        """Gets the security_groups of this NeutronUpdatePortOption.

        功能说明：扩展属性：安全组的UUID 例如：\"security_groups\": [\"a0608cbf-d047-4f54-8b28-cd7b59853fff\"] 约束：不支持更新为空

        :return: The security_groups of this NeutronUpdatePortOption.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this NeutronUpdatePortOption.

        功能说明：扩展属性：安全组的UUID 例如：\"security_groups\": [\"a0608cbf-d047-4f54-8b28-cd7b59853fff\"] 约束：不支持更新为空

        :param security_groups: The security_groups of this NeutronUpdatePortOption.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def allowed_address_pairs(self):
        """Gets the allowed_address_pairs of this NeutronUpdatePortOption.

        功能说明：扩展属性：IP/Mac对列表，allow_address_pair参见“allow_address_pair对象”表 约束：  - IP地址不允许为 “0.0.0.0”  - 如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组  - 硬件SDN环境不支持ip_address属性配置为CIDR格式  - 为虚拟IP配置后端ECS场景，allowed_address_pairs中配置的IP地址，必须为ECS网卡已有的IP地址，否则可能会导致虚拟IP通信异常。

        :return: The allowed_address_pairs of this NeutronUpdatePortOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.AllowedAddressPair`]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        """Sets the allowed_address_pairs of this NeutronUpdatePortOption.

        功能说明：扩展属性：IP/Mac对列表，allow_address_pair参见“allow_address_pair对象”表 约束：  - IP地址不允许为 “0.0.0.0”  - 如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组  - 硬件SDN环境不支持ip_address属性配置为CIDR格式  - 为虚拟IP配置后端ECS场景，allowed_address_pairs中配置的IP地址，必须为ECS网卡已有的IP地址，否则可能会导致虚拟IP通信异常。

        :param allowed_address_pairs: The allowed_address_pairs of this NeutronUpdatePortOption.
        :type allowed_address_pairs: list[:class:`huaweicloudsdkvpc.v2.AllowedAddressPair`]
        """
        self._allowed_address_pairs = allowed_address_pairs

    @property
    def extra_dhcp_opts(self):
        """Gets the extra_dhcp_opts of this NeutronUpdatePortOption.

        扩展属性：DHCP的扩展Option

        :return: The extra_dhcp_opts of this NeutronUpdatePortOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.ExtraDhcpOpt`]
        """
        return self._extra_dhcp_opts

    @extra_dhcp_opts.setter
    def extra_dhcp_opts(self, extra_dhcp_opts):
        """Sets the extra_dhcp_opts of this NeutronUpdatePortOption.

        扩展属性：DHCP的扩展Option

        :param extra_dhcp_opts: The extra_dhcp_opts of this NeutronUpdatePortOption.
        :type extra_dhcp_opts: list[:class:`huaweicloudsdkvpc.v2.ExtraDhcpOpt`]
        """
        self._extra_dhcp_opts = extra_dhcp_opts

    @property
    def port_security_enabled(self):
        """Gets the port_security_enabled of this NeutronUpdatePortOption.

        功能说明：端口安全使能标记，如果不使能则安全组和dhcp防欺骗不生效，默认为true

        :return: The port_security_enabled of this NeutronUpdatePortOption.
        :rtype: bool
        """
        return self._port_security_enabled

    @port_security_enabled.setter
    def port_security_enabled(self, port_security_enabled):
        """Sets the port_security_enabled of this NeutronUpdatePortOption.

        功能说明：端口安全使能标记，如果不使能则安全组和dhcp防欺骗不生效，默认为true

        :param port_security_enabled: The port_security_enabled of this NeutronUpdatePortOption.
        :type port_security_enabled: bool
        """
        self._port_security_enabled = port_security_enabled

    @property
    def bindingvnic_type(self):
        """Gets the bindingvnic_type of this NeutronUpdatePortOption.

        绑定的vNIC类型  - normal: 软交换

        :return: The bindingvnic_type of this NeutronUpdatePortOption.
        :rtype: str
        """
        return self._bindingvnic_type

    @bindingvnic_type.setter
    def bindingvnic_type(self, bindingvnic_type):
        """Sets the bindingvnic_type of this NeutronUpdatePortOption.

        绑定的vNIC类型  - normal: 软交换

        :param bindingvnic_type: The bindingvnic_type of this NeutronUpdatePortOption.
        :type bindingvnic_type: str
        """
        self._bindingvnic_type = bindingvnic_type

    @property
    def bindingprofile(self):
        """Gets the bindingprofile of this NeutronUpdatePortOption.

        功能说明：扩展属性，提供用户设置自定义信息  - internal_elb字段，布尔类型，普通租户可见。只有在创建内网ELB的虚拟IP的网卡时设置为true。普通租户没有权限更改该字段，由系统维护。 举例：{\"internal_elb\": true}  - disable_security_groups字段，布尔类型，普通租户可见。默认为false，高性能通信场景下，允许指定为true。仅支持创建port和读取时指定。当前仅支持指定为true，不支持指定为false。 举例：{\"disable_security_groups\"：true }，当前仅支持指定为true，不支持指定为false，指定为true时，FWaaS功能不生效。

        :return: The bindingprofile of this NeutronUpdatePortOption.
        :rtype: dict(str, object)
        """
        return self._bindingprofile

    @bindingprofile.setter
    def bindingprofile(self, bindingprofile):
        """Sets the bindingprofile of this NeutronUpdatePortOption.

        功能说明：扩展属性，提供用户设置自定义信息  - internal_elb字段，布尔类型，普通租户可见。只有在创建内网ELB的虚拟IP的网卡时设置为true。普通租户没有权限更改该字段，由系统维护。 举例：{\"internal_elb\": true}  - disable_security_groups字段，布尔类型，普通租户可见。默认为false，高性能通信场景下，允许指定为true。仅支持创建port和读取时指定。当前仅支持指定为true，不支持指定为false。 举例：{\"disable_security_groups\"：true }，当前仅支持指定为true，不支持指定为false，指定为true时，FWaaS功能不生效。

        :param bindingprofile: The bindingprofile of this NeutronUpdatePortOption.
        :type bindingprofile: dict(str, object)
        """
        self._bindingprofile = bindingprofile

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
        if not isinstance(other, NeutronUpdatePortOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
