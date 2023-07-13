# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EcsNetWork:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'addr': 'str',
        'version': 'int',
        'os_ext_ips_ma_cmac_addr': 'str',
        'os_ext_ip_stype': 'str',
        'os_ext_ip_sport_id': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'tenant_type': 'str'
    }

    attribute_map = {
        'addr': 'addr',
        'version': 'version',
        'os_ext_ips_ma_cmac_addr': 'OS-EXT-IPS-MAC:mac_addr',
        'os_ext_ip_stype': 'OS-EXT-IPS:type',
        'os_ext_ip_sport_id': 'OS-EXT-IPS:port_id',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'tenant_type': 'tenant_type'
    }

    def __init__(self, addr=None, version=None, os_ext_ips_ma_cmac_addr=None, os_ext_ip_stype=None, os_ext_ip_sport_id=None, vpc_id=None, subnet_id=None, tenant_type=None):
        """EcsNetWork

        The model defined in huaweicloud sdk

        :param addr: IP地址信息
        :type addr: str
        :param version: IP地址类型， &#x60;4&#x60; - IPV4 &#x60;6&#x60; - IPV6
        :type version: int
        :param os_ext_ips_ma_cmac_addr: MAC地址
        :type os_ext_ips_ma_cmac_addr: str
        :param os_ext_ip_stype: IP地址分配方式，字符串是大小写不敏感格式 * &#x60;fixed&#x60; - 代表私有IP地址 * &#x60;floating&#x60; - 代表浮动IP地址
        :type os_ext_ip_stype: str
        :param os_ext_ip_sport_id: IP地址对应的端口ID。
        :type os_ext_ip_sport_id: str
        :param vpc_id: 虚拟私有云ID
        :type vpc_id: str
        :param subnet_id: 子网id
        :type subnet_id: str
        :param tenant_type: 租户类别: - tenant: 租户 - resource_tenant: 资源租户
        :type tenant_type: str
        """
        
        

        self._addr = None
        self._version = None
        self._os_ext_ips_ma_cmac_addr = None
        self._os_ext_ip_stype = None
        self._os_ext_ip_sport_id = None
        self._vpc_id = None
        self._subnet_id = None
        self._tenant_type = None
        self.discriminator = None

        if addr is not None:
            self.addr = addr
        if version is not None:
            self.version = version
        if os_ext_ips_ma_cmac_addr is not None:
            self.os_ext_ips_ma_cmac_addr = os_ext_ips_ma_cmac_addr
        if os_ext_ip_stype is not None:
            self.os_ext_ip_stype = os_ext_ip_stype
        if os_ext_ip_sport_id is not None:
            self.os_ext_ip_sport_id = os_ext_ip_sport_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if tenant_type is not None:
            self.tenant_type = tenant_type

    @property
    def addr(self):
        """Gets the addr of this EcsNetWork.

        IP地址信息

        :return: The addr of this EcsNetWork.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this EcsNetWork.

        IP地址信息

        :param addr: The addr of this EcsNetWork.
        :type addr: str
        """
        self._addr = addr

    @property
    def version(self):
        """Gets the version of this EcsNetWork.

        IP地址类型， `4` - IPV4 `6` - IPV6

        :return: The version of this EcsNetWork.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this EcsNetWork.

        IP地址类型， `4` - IPV4 `6` - IPV6

        :param version: The version of this EcsNetWork.
        :type version: int
        """
        self._version = version

    @property
    def os_ext_ips_ma_cmac_addr(self):
        """Gets the os_ext_ips_ma_cmac_addr of this EcsNetWork.

        MAC地址

        :return: The os_ext_ips_ma_cmac_addr of this EcsNetWork.
        :rtype: str
        """
        return self._os_ext_ips_ma_cmac_addr

    @os_ext_ips_ma_cmac_addr.setter
    def os_ext_ips_ma_cmac_addr(self, os_ext_ips_ma_cmac_addr):
        """Sets the os_ext_ips_ma_cmac_addr of this EcsNetWork.

        MAC地址

        :param os_ext_ips_ma_cmac_addr: The os_ext_ips_ma_cmac_addr of this EcsNetWork.
        :type os_ext_ips_ma_cmac_addr: str
        """
        self._os_ext_ips_ma_cmac_addr = os_ext_ips_ma_cmac_addr

    @property
    def os_ext_ip_stype(self):
        """Gets the os_ext_ip_stype of this EcsNetWork.

        IP地址分配方式，字符串是大小写不敏感格式 * `fixed` - 代表私有IP地址 * `floating` - 代表浮动IP地址

        :return: The os_ext_ip_stype of this EcsNetWork.
        :rtype: str
        """
        return self._os_ext_ip_stype

    @os_ext_ip_stype.setter
    def os_ext_ip_stype(self, os_ext_ip_stype):
        """Sets the os_ext_ip_stype of this EcsNetWork.

        IP地址分配方式，字符串是大小写不敏感格式 * `fixed` - 代表私有IP地址 * `floating` - 代表浮动IP地址

        :param os_ext_ip_stype: The os_ext_ip_stype of this EcsNetWork.
        :type os_ext_ip_stype: str
        """
        self._os_ext_ip_stype = os_ext_ip_stype

    @property
    def os_ext_ip_sport_id(self):
        """Gets the os_ext_ip_sport_id of this EcsNetWork.

        IP地址对应的端口ID。

        :return: The os_ext_ip_sport_id of this EcsNetWork.
        :rtype: str
        """
        return self._os_ext_ip_sport_id

    @os_ext_ip_sport_id.setter
    def os_ext_ip_sport_id(self, os_ext_ip_sport_id):
        """Sets the os_ext_ip_sport_id of this EcsNetWork.

        IP地址对应的端口ID。

        :param os_ext_ip_sport_id: The os_ext_ip_sport_id of this EcsNetWork.
        :type os_ext_ip_sport_id: str
        """
        self._os_ext_ip_sport_id = os_ext_ip_sport_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this EcsNetWork.

        虚拟私有云ID

        :return: The vpc_id of this EcsNetWork.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this EcsNetWork.

        虚拟私有云ID

        :param vpc_id: The vpc_id of this EcsNetWork.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this EcsNetWork.

        子网id

        :return: The subnet_id of this EcsNetWork.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this EcsNetWork.

        子网id

        :param subnet_id: The subnet_id of this EcsNetWork.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def tenant_type(self):
        """Gets the tenant_type of this EcsNetWork.

        租户类别: - tenant: 租户 - resource_tenant: 资源租户

        :return: The tenant_type of this EcsNetWork.
        :rtype: str
        """
        return self._tenant_type

    @tenant_type.setter
    def tenant_type(self, tenant_type):
        """Sets the tenant_type of this EcsNetWork.

        租户类别: - tenant: 租户 - resource_tenant: 资源租户

        :param tenant_type: The tenant_type of this EcsNetWork.
        :type tenant_type: str
        """
        self._tenant_type = tenant_type

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
        if not isinstance(other, EcsNetWork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
