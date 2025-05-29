# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostPaidServerNic:

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
        'ip_address': 'str',
        'ipv6_enable': 'bool',
        'ipv6_bandwidth': 'PostPaidServerIpv6Bandwidth',
        'allowed_address_pairs': 'list[CreateServerNicAllowedAddressPairs]'
    }

    attribute_map = {
        'subnet_id': 'subnet_id',
        'port_id': 'port_id',
        'ip_address': 'ip_address',
        'ipv6_enable': 'ipv6_enable',
        'ipv6_bandwidth': 'ipv6_bandwidth',
        'allowed_address_pairs': 'allowed_address_pairs'
    }

    def __init__(self, subnet_id=None, port_id=None, ip_address=None, ipv6_enable=None, ipv6_bandwidth=None, allowed_address_pairs=None):
        r"""PostPaidServerNic

        The model defined in huaweicloud sdk

        :param subnet_id: 待创建云服务器所在的子网信息，需要指定vpcid对应VPC下的子网ID，UUID格式。  可以通过VPC服务 [查询子网](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;VPC&amp;api&#x3D;ListSubnets) 接口查询，该接口支持通过创建云服务器填写的vpcid进行过滤查询。
        :type subnet_id: str
        :param port_id: 网卡ID，UUID格式。 当该字段不为空时，表示挂载指定的网卡。port_id和subnet_id不能同时为空。 网卡ID可以从虚拟私有云的“查询端口列表”章节查询到。 约束： 网卡状态必须为DOWN。 网卡的vpcid必须和传入的vpcid一致。 当port_id和subnet_id同时存在的时候，优先使用port_id。当选择port_id不为空时，代表此时使用的是弹性网卡，此时security_groups和ip_address等参数不生效。
        :type port_id: str
        :param ip_address: 待创建云服务器网卡的IP地址，IPv4格式。  约束：  - 不填或空字符串，默认在子网（subnet）中自动分配一个未使用的IP作网卡的IP地址。 - 若指定IP地址，该IP地址必须在子网（subnet）对应的网段内，且未被使用。
        :type ip_address: str
        :param ipv6_enable: 是否支持ipv6。  取值为true时，标识此网卡支持ipv6。
        :type ipv6_enable: bool
        :param ipv6_bandwidth: 
        :type ipv6_bandwidth: :class:`huaweicloudsdkecs.v2.PostPaidServerIpv6Bandwidth`
        :param allowed_address_pairs: IP/Mac对列表， 约束：IP地址不允许为 “0.0.0.0/0” 如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组 如果allowed_address_pairs为“1.1.1.1/0”，表示关闭源目地址检查开关 被绑定的云服务器网卡allowed_address_pairs填“1.1.1.1/0”
        :type allowed_address_pairs: list[:class:`huaweicloudsdkecs.v2.CreateServerNicAllowedAddressPairs`]
        """
        
        

        self._subnet_id = None
        self._port_id = None
        self._ip_address = None
        self._ipv6_enable = None
        self._ipv6_bandwidth = None
        self._allowed_address_pairs = None
        self.discriminator = None

        if subnet_id is not None:
            self.subnet_id = subnet_id
        if port_id is not None:
            self.port_id = port_id
        if ip_address is not None:
            self.ip_address = ip_address
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth
        if allowed_address_pairs is not None:
            self.allowed_address_pairs = allowed_address_pairs

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this PostPaidServerNic.

        待创建云服务器所在的子网信息，需要指定vpcid对应VPC下的子网ID，UUID格式。  可以通过VPC服务 [查询子网](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=VPC&api=ListSubnets) 接口查询，该接口支持通过创建云服务器填写的vpcid进行过滤查询。

        :return: The subnet_id of this PostPaidServerNic.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this PostPaidServerNic.

        待创建云服务器所在的子网信息，需要指定vpcid对应VPC下的子网ID，UUID格式。  可以通过VPC服务 [查询子网](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=VPC&api=ListSubnets) 接口查询，该接口支持通过创建云服务器填写的vpcid进行过滤查询。

        :param subnet_id: The subnet_id of this PostPaidServerNic.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def port_id(self):
        r"""Gets the port_id of this PostPaidServerNic.

        网卡ID，UUID格式。 当该字段不为空时，表示挂载指定的网卡。port_id和subnet_id不能同时为空。 网卡ID可以从虚拟私有云的“查询端口列表”章节查询到。 约束： 网卡状态必须为DOWN。 网卡的vpcid必须和传入的vpcid一致。 当port_id和subnet_id同时存在的时候，优先使用port_id。当选择port_id不为空时，代表此时使用的是弹性网卡，此时security_groups和ip_address等参数不生效。

        :return: The port_id of this PostPaidServerNic.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this PostPaidServerNic.

        网卡ID，UUID格式。 当该字段不为空时，表示挂载指定的网卡。port_id和subnet_id不能同时为空。 网卡ID可以从虚拟私有云的“查询端口列表”章节查询到。 约束： 网卡状态必须为DOWN。 网卡的vpcid必须和传入的vpcid一致。 当port_id和subnet_id同时存在的时候，优先使用port_id。当选择port_id不为空时，代表此时使用的是弹性网卡，此时security_groups和ip_address等参数不生效。

        :param port_id: The port_id of this PostPaidServerNic.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def ip_address(self):
        r"""Gets the ip_address of this PostPaidServerNic.

        待创建云服务器网卡的IP地址，IPv4格式。  约束：  - 不填或空字符串，默认在子网（subnet）中自动分配一个未使用的IP作网卡的IP地址。 - 若指定IP地址，该IP地址必须在子网（subnet）对应的网段内，且未被使用。

        :return: The ip_address of this PostPaidServerNic.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this PostPaidServerNic.

        待创建云服务器网卡的IP地址，IPv4格式。  约束：  - 不填或空字符串，默认在子网（subnet）中自动分配一个未使用的IP作网卡的IP地址。 - 若指定IP地址，该IP地址必须在子网（subnet）对应的网段内，且未被使用。

        :param ip_address: The ip_address of this PostPaidServerNic.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this PostPaidServerNic.

        是否支持ipv6。  取值为true时，标识此网卡支持ipv6。

        :return: The ipv6_enable of this PostPaidServerNic.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this PostPaidServerNic.

        是否支持ipv6。  取值为true时，标识此网卡支持ipv6。

        :param ipv6_enable: The ipv6_enable of this PostPaidServerNic.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def ipv6_bandwidth(self):
        r"""Gets the ipv6_bandwidth of this PostPaidServerNic.

        :return: The ipv6_bandwidth of this PostPaidServerNic.
        :rtype: :class:`huaweicloudsdkecs.v2.PostPaidServerIpv6Bandwidth`
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        r"""Sets the ipv6_bandwidth of this PostPaidServerNic.

        :param ipv6_bandwidth: The ipv6_bandwidth of this PostPaidServerNic.
        :type ipv6_bandwidth: :class:`huaweicloudsdkecs.v2.PostPaidServerIpv6Bandwidth`
        """
        self._ipv6_bandwidth = ipv6_bandwidth

    @property
    def allowed_address_pairs(self):
        r"""Gets the allowed_address_pairs of this PostPaidServerNic.

        IP/Mac对列表， 约束：IP地址不允许为 “0.0.0.0/0” 如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组 如果allowed_address_pairs为“1.1.1.1/0”，表示关闭源目地址检查开关 被绑定的云服务器网卡allowed_address_pairs填“1.1.1.1/0”

        :return: The allowed_address_pairs of this PostPaidServerNic.
        :rtype: list[:class:`huaweicloudsdkecs.v2.CreateServerNicAllowedAddressPairs`]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        r"""Sets the allowed_address_pairs of this PostPaidServerNic.

        IP/Mac对列表， 约束：IP地址不允许为 “0.0.0.0/0” 如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组 如果allowed_address_pairs为“1.1.1.1/0”，表示关闭源目地址检查开关 被绑定的云服务器网卡allowed_address_pairs填“1.1.1.1/0”

        :param allowed_address_pairs: The allowed_address_pairs of this PostPaidServerNic.
        :type allowed_address_pairs: list[:class:`huaweicloudsdkecs.v2.CreateServerNicAllowedAddressPairs`]
        """
        self._allowed_address_pairs = allowed_address_pairs

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
        if not isinstance(other, PostPaidServerNic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
