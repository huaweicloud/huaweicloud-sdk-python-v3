# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAddServerNicOption:

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
        'port_id': 'str',
        'security_groups': 'list[ServerNicSecurityGroup]',
        'ip_address': 'str',
        'ipv6_enable': 'bool',
        'ipv6_bandwidth': 'Ipv6Bandwidth'
    }

    attribute_map = {
        'subnet_id': 'subnet_id',
        'port_id': 'port_id',
        'security_groups': 'security_groups',
        'ip_address': 'ip_address',
        'ipv6_enable': 'ipv6_enable',
        'ipv6_bandwidth': 'ipv6_bandwidth'
    }

    def __init__(self, subnet_id=None, port_id=None, security_groups=None, ip_address=None, ipv6_enable=None, ipv6_bandwidth=None):
        r"""BatchAddServerNicOption

        The model defined in huaweicloud sdk

        :param subnet_id: 云服务器添加网卡的信息。  需要指定云服务器所属虚拟私有云下已创建的网络（network）的ID，UUID格式。
        :type subnet_id: str
        :param port_id: 网卡ID，UUID格式。 当该字段不为空时，表示挂载指定的网卡。port_id和subnet_id不能同时为空。 网卡ID可以从虚拟私有云的“查询端口列表”章节查询到。 约束： 网卡状态必须为DOWN。 网卡的vpcid必须和传入的vpcid一致。 当port_id和subnet_id同时存在的时候，优先使用port_id。当选择port_id不为空时，代表此时使用的是弹性网卡，此时security_groups和ip_address等参数不生效。
        :type port_id: str
        :param security_groups: 添加网卡的安全组信息
        :type security_groups: list[:class:`huaweicloudsdkecs.v2.ServerNicSecurityGroup`]
        :param ip_address: IP地址，无该参数表示自动分配IP地址。
        :type ip_address: str
        :param ipv6_enable: 是否支持ipv6。  取值为true时，标识此网卡支持ipv6。
        :type ipv6_enable: bool
        :param ipv6_bandwidth: 
        :type ipv6_bandwidth: :class:`huaweicloudsdkecs.v2.Ipv6Bandwidth`
        """
        
        

        self._subnet_id = None
        self._port_id = None
        self._security_groups = None
        self._ip_address = None
        self._ipv6_enable = None
        self._ipv6_bandwidth = None
        self.discriminator = None

        if subnet_id is not None:
            self.subnet_id = subnet_id
        if port_id is not None:
            self.port_id = port_id
        if security_groups is not None:
            self.security_groups = security_groups
        if ip_address is not None:
            self.ip_address = ip_address
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this BatchAddServerNicOption.

        云服务器添加网卡的信息。  需要指定云服务器所属虚拟私有云下已创建的网络（network）的ID，UUID格式。

        :return: The subnet_id of this BatchAddServerNicOption.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this BatchAddServerNicOption.

        云服务器添加网卡的信息。  需要指定云服务器所属虚拟私有云下已创建的网络（network）的ID，UUID格式。

        :param subnet_id: The subnet_id of this BatchAddServerNicOption.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def port_id(self):
        r"""Gets the port_id of this BatchAddServerNicOption.

        网卡ID，UUID格式。 当该字段不为空时，表示挂载指定的网卡。port_id和subnet_id不能同时为空。 网卡ID可以从虚拟私有云的“查询端口列表”章节查询到。 约束： 网卡状态必须为DOWN。 网卡的vpcid必须和传入的vpcid一致。 当port_id和subnet_id同时存在的时候，优先使用port_id。当选择port_id不为空时，代表此时使用的是弹性网卡，此时security_groups和ip_address等参数不生效。

        :return: The port_id of this BatchAddServerNicOption.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this BatchAddServerNicOption.

        网卡ID，UUID格式。 当该字段不为空时，表示挂载指定的网卡。port_id和subnet_id不能同时为空。 网卡ID可以从虚拟私有云的“查询端口列表”章节查询到。 约束： 网卡状态必须为DOWN。 网卡的vpcid必须和传入的vpcid一致。 当port_id和subnet_id同时存在的时候，优先使用port_id。当选择port_id不为空时，代表此时使用的是弹性网卡，此时security_groups和ip_address等参数不生效。

        :param port_id: The port_id of this BatchAddServerNicOption.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def security_groups(self):
        r"""Gets the security_groups of this BatchAddServerNicOption.

        添加网卡的安全组信息

        :return: The security_groups of this BatchAddServerNicOption.
        :rtype: list[:class:`huaweicloudsdkecs.v2.ServerNicSecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this BatchAddServerNicOption.

        添加网卡的安全组信息

        :param security_groups: The security_groups of this BatchAddServerNicOption.
        :type security_groups: list[:class:`huaweicloudsdkecs.v2.ServerNicSecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def ip_address(self):
        r"""Gets the ip_address of this BatchAddServerNicOption.

        IP地址，无该参数表示自动分配IP地址。

        :return: The ip_address of this BatchAddServerNicOption.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this BatchAddServerNicOption.

        IP地址，无该参数表示自动分配IP地址。

        :param ip_address: The ip_address of this BatchAddServerNicOption.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this BatchAddServerNicOption.

        是否支持ipv6。  取值为true时，标识此网卡支持ipv6。

        :return: The ipv6_enable of this BatchAddServerNicOption.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this BatchAddServerNicOption.

        是否支持ipv6。  取值为true时，标识此网卡支持ipv6。

        :param ipv6_enable: The ipv6_enable of this BatchAddServerNicOption.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def ipv6_bandwidth(self):
        r"""Gets the ipv6_bandwidth of this BatchAddServerNicOption.

        :return: The ipv6_bandwidth of this BatchAddServerNicOption.
        :rtype: :class:`huaweicloudsdkecs.v2.Ipv6Bandwidth`
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        r"""Sets the ipv6_bandwidth of this BatchAddServerNicOption.

        :param ipv6_bandwidth: The ipv6_bandwidth of this BatchAddServerNicOption.
        :type ipv6_bandwidth: :class:`huaweicloudsdkecs.v2.Ipv6Bandwidth`
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
        if not isinstance(other, BatchAddServerNicOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
