# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubnetOption:

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
        'dhcp_enable': 'bool',
        'primary_dns': 'str',
        'secondary_dns': 'str',
        'dns_list': 'list[str]',
        'ipv6_enable': 'bool',
        'pool_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'dhcp_enable': 'dhcp_enable',
        'primary_dns': 'primary_dns',
        'secondary_dns': 'secondary_dns',
        'dns_list': 'dnsList',
        'ipv6_enable': 'ipv6_enable',
        'pool_id': 'pool_id'
    }

    def __init__(self, name=None, dhcp_enable=None, primary_dns=None, secondary_dns=None, dns_list=None, ipv6_enable=None, pool_id=None):
        r"""UpdateSubnetOption

        The model defined in huaweicloud sdk

        :param name: 子网名称  取值范围：0-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param dhcp_enable: 子网是否开启dhcp功能  取值范围：true（开启），false（关闭）  约束：不填时默认为true。当设置为false时，会导致新创建的实例无法获取IP地址，cloudinit无法注入帐号密码，请谨慎操作。
        :type dhcp_enable: bool
        :param primary_dns: 子网dns服务器地址1  约束：ip格式
        :type primary_dns: str
        :param secondary_dns: 子网dns服务器地址2  约束：ip格式
        :type secondary_dns: str
        :param dns_list: 子网dns服务器地址的集合；如果想使用两个以上dns服务器，请使用该字段。  约束：是子网dns服务器地址1跟子网dns服务器地址2的合集的父集
        :type dns_list: list[str]
        :param ipv6_enable: 是否创建IPv6子网  取值范围：  - true：开启  - false：关闭  约束：   1、若该字段为true，则pool_id字段必填；若该字段为false，则pool_id字段不生效。   2、子网开启IPv6后不支持关闭。
        :type ipv6_enable: bool
        :param pool_id: IPv6线路ID。
        :type pool_id: str
        """
        
        

        self._name = None
        self._dhcp_enable = None
        self._primary_dns = None
        self._secondary_dns = None
        self._dns_list = None
        self._ipv6_enable = None
        self._pool_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if dhcp_enable is not None:
            self.dhcp_enable = dhcp_enable
        if primary_dns is not None:
            self.primary_dns = primary_dns
        if secondary_dns is not None:
            self.secondary_dns = secondary_dns
        if dns_list is not None:
            self.dns_list = dns_list
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if pool_id is not None:
            self.pool_id = pool_id

    @property
    def name(self):
        r"""Gets the name of this UpdateSubnetOption.

        子网名称  取值范围：0-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this UpdateSubnetOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateSubnetOption.

        子网名称  取值范围：0-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this UpdateSubnetOption.
        :type name: str
        """
        self._name = name

    @property
    def dhcp_enable(self):
        r"""Gets the dhcp_enable of this UpdateSubnetOption.

        子网是否开启dhcp功能  取值范围：true（开启），false（关闭）  约束：不填时默认为true。当设置为false时，会导致新创建的实例无法获取IP地址，cloudinit无法注入帐号密码，请谨慎操作。

        :return: The dhcp_enable of this UpdateSubnetOption.
        :rtype: bool
        """
        return self._dhcp_enable

    @dhcp_enable.setter
    def dhcp_enable(self, dhcp_enable):
        r"""Sets the dhcp_enable of this UpdateSubnetOption.

        子网是否开启dhcp功能  取值范围：true（开启），false（关闭）  约束：不填时默认为true。当设置为false时，会导致新创建的实例无法获取IP地址，cloudinit无法注入帐号密码，请谨慎操作。

        :param dhcp_enable: The dhcp_enable of this UpdateSubnetOption.
        :type dhcp_enable: bool
        """
        self._dhcp_enable = dhcp_enable

    @property
    def primary_dns(self):
        r"""Gets the primary_dns of this UpdateSubnetOption.

        子网dns服务器地址1  约束：ip格式

        :return: The primary_dns of this UpdateSubnetOption.
        :rtype: str
        """
        return self._primary_dns

    @primary_dns.setter
    def primary_dns(self, primary_dns):
        r"""Sets the primary_dns of this UpdateSubnetOption.

        子网dns服务器地址1  约束：ip格式

        :param primary_dns: The primary_dns of this UpdateSubnetOption.
        :type primary_dns: str
        """
        self._primary_dns = primary_dns

    @property
    def secondary_dns(self):
        r"""Gets the secondary_dns of this UpdateSubnetOption.

        子网dns服务器地址2  约束：ip格式

        :return: The secondary_dns of this UpdateSubnetOption.
        :rtype: str
        """
        return self._secondary_dns

    @secondary_dns.setter
    def secondary_dns(self, secondary_dns):
        r"""Sets the secondary_dns of this UpdateSubnetOption.

        子网dns服务器地址2  约束：ip格式

        :param secondary_dns: The secondary_dns of this UpdateSubnetOption.
        :type secondary_dns: str
        """
        self._secondary_dns = secondary_dns

    @property
    def dns_list(self):
        r"""Gets the dns_list of this UpdateSubnetOption.

        子网dns服务器地址的集合；如果想使用两个以上dns服务器，请使用该字段。  约束：是子网dns服务器地址1跟子网dns服务器地址2的合集的父集

        :return: The dns_list of this UpdateSubnetOption.
        :rtype: list[str]
        """
        return self._dns_list

    @dns_list.setter
    def dns_list(self, dns_list):
        r"""Sets the dns_list of this UpdateSubnetOption.

        子网dns服务器地址的集合；如果想使用两个以上dns服务器，请使用该字段。  约束：是子网dns服务器地址1跟子网dns服务器地址2的合集的父集

        :param dns_list: The dns_list of this UpdateSubnetOption.
        :type dns_list: list[str]
        """
        self._dns_list = dns_list

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this UpdateSubnetOption.

        是否创建IPv6子网  取值范围：  - true：开启  - false：关闭  约束：   1、若该字段为true，则pool_id字段必填；若该字段为false，则pool_id字段不生效。   2、子网开启IPv6后不支持关闭。

        :return: The ipv6_enable of this UpdateSubnetOption.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this UpdateSubnetOption.

        是否创建IPv6子网  取值范围：  - true：开启  - false：关闭  约束：   1、若该字段为true，则pool_id字段必填；若该字段为false，则pool_id字段不生效。   2、子网开启IPv6后不支持关闭。

        :param ipv6_enable: The ipv6_enable of this UpdateSubnetOption.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def pool_id(self):
        r"""Gets the pool_id of this UpdateSubnetOption.

        IPv6线路ID。

        :return: The pool_id of this UpdateSubnetOption.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this UpdateSubnetOption.

        IPv6线路ID。

        :param pool_id: The pool_id of this UpdateSubnetOption.
        :type pool_id: str
        """
        self._pool_id = pool_id

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
        if not isinstance(other, UpdateSubnetOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
