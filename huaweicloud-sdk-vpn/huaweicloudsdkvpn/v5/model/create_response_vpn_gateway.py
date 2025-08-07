# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResponseVpnGateway:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'attachment_type': 'str',
        'ip_version': 'str',
        'certificate_id': 'str',
        'er_id': 'str',
        'vpc_id': 'str',
        'local_subnets': 'list[str]',
        'local_subnets_v6': 'list[str]',
        'connect_subnet': 'str',
        'network_type': 'str',
        'access_vpc_id': 'str',
        'access_subnet_id': 'str',
        'bgp_asn': 'int',
        'flavor': 'str',
        'connection_number': 'int',
        'used_connection_number': 'int',
        'used_connection_group': 'int',
        'enterprise_project_id': 'str',
        'ha_mode': 'str',
        'policy_template': 'PolicyTemplate',
        'tags': 'list[VpnResourceTag]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'attachment_type': 'attachment_type',
        'ip_version': 'ip_version',
        'certificate_id': 'certificate_id',
        'er_id': 'er_id',
        'vpc_id': 'vpc_id',
        'local_subnets': 'local_subnets',
        'local_subnets_v6': 'local_subnets_v6',
        'connect_subnet': 'connect_subnet',
        'network_type': 'network_type',
        'access_vpc_id': 'access_vpc_id',
        'access_subnet_id': 'access_subnet_id',
        'bgp_asn': 'bgp_asn',
        'flavor': 'flavor',
        'connection_number': 'connection_number',
        'used_connection_number': 'used_connection_number',
        'used_connection_group': 'used_connection_group',
        'enterprise_project_id': 'enterprise_project_id',
        'ha_mode': 'ha_mode',
        'policy_template': 'policy_template',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, attachment_type=None, ip_version=None, certificate_id=None, er_id=None, vpc_id=None, local_subnets=None, local_subnets_v6=None, connect_subnet=None, network_type=None, access_vpc_id=None, access_subnet_id=None, bgp_asn=None, flavor=None, connection_number=None, used_connection_number=None, used_connection_group=None, enterprise_project_id=None, ha_mode=None, policy_template=None, tags=None):
        r"""CreateResponseVpnGateway

        The model defined in huaweicloud sdk

        :param id: VPN网关ID
        :type id: str
        :param name: VPN网关名称
        :type name: str
        :param attachment_type: 关联模式
        :type attachment_type: str
        :param ip_version: 网关的IP协议版本
        :type ip_version: str
        :param certificate_id: 证书ID
        :type certificate_id: str
        :param er_id: VPN网关所连接的ER实例的ID
        :type er_id: str
        :param vpc_id: VPN网关所连接的VPC的ID
        :type vpc_id: str
        :param local_subnets: 本端子网
        :type local_subnets: list[str]
        :param local_subnets_v6: 使能ipv6的本端子网
        :type local_subnets_v6: list[str]
        :param connect_subnet: VPN网关所使用的VPC子网ID
        :type connect_subnet: str
        :param network_type: VPN网关的网络类型，默认为公网(public)
        :type network_type: str
        :param access_vpc_id: VPN网关北向接入VPC ID，不填时默认使用vpc_id字段的值
        :type access_vpc_id: str
        :param access_subnet_id: VPN网关北向接入VPC中的接入子网ID
        :type access_subnet_id: str
        :param bgp_asn: bgp所使用的asn号
        :type bgp_asn: int
        :param flavor: VPN网关的规格类型
        :type flavor: str
        :param connection_number: 最大可创建的VPN连接数
        :type connection_number: int
        :param used_connection_number: 当前已经使用的VPN连接数
        :type used_connection_number: int
        :param used_connection_group: 当前已经使用的VPN连接组个数
        :type used_connection_group: int
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param ha_mode: ha模式
        :type ha_mode: str
        :param policy_template: 
        :type policy_template: :class:`huaweicloudsdkvpn.v5.PolicyTemplate`
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
        """
        
        

        self._id = None
        self._name = None
        self._attachment_type = None
        self._ip_version = None
        self._certificate_id = None
        self._er_id = None
        self._vpc_id = None
        self._local_subnets = None
        self._local_subnets_v6 = None
        self._connect_subnet = None
        self._network_type = None
        self._access_vpc_id = None
        self._access_subnet_id = None
        self._bgp_asn = None
        self._flavor = None
        self._connection_number = None
        self._used_connection_number = None
        self._used_connection_group = None
        self._enterprise_project_id = None
        self._ha_mode = None
        self._policy_template = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if attachment_type is not None:
            self.attachment_type = attachment_type
        if ip_version is not None:
            self.ip_version = ip_version
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if er_id is not None:
            self.er_id = er_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if local_subnets is not None:
            self.local_subnets = local_subnets
        if local_subnets_v6 is not None:
            self.local_subnets_v6 = local_subnets_v6
        if connect_subnet is not None:
            self.connect_subnet = connect_subnet
        if network_type is not None:
            self.network_type = network_type
        if access_vpc_id is not None:
            self.access_vpc_id = access_vpc_id
        if access_subnet_id is not None:
            self.access_subnet_id = access_subnet_id
        if bgp_asn is not None:
            self.bgp_asn = bgp_asn
        if flavor is not None:
            self.flavor = flavor
        if connection_number is not None:
            self.connection_number = connection_number
        if used_connection_number is not None:
            self.used_connection_number = used_connection_number
        if used_connection_group is not None:
            self.used_connection_group = used_connection_group
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if ha_mode is not None:
            self.ha_mode = ha_mode
        if policy_template is not None:
            self.policy_template = policy_template
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        r"""Gets the id of this CreateResponseVpnGateway.

        VPN网关ID

        :return: The id of this CreateResponseVpnGateway.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateResponseVpnGateway.

        VPN网关ID

        :param id: The id of this CreateResponseVpnGateway.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateResponseVpnGateway.

        VPN网关名称

        :return: The name of this CreateResponseVpnGateway.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateResponseVpnGateway.

        VPN网关名称

        :param name: The name of this CreateResponseVpnGateway.
        :type name: str
        """
        self._name = name

    @property
    def attachment_type(self):
        r"""Gets the attachment_type of this CreateResponseVpnGateway.

        关联模式

        :return: The attachment_type of this CreateResponseVpnGateway.
        :rtype: str
        """
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, attachment_type):
        r"""Sets the attachment_type of this CreateResponseVpnGateway.

        关联模式

        :param attachment_type: The attachment_type of this CreateResponseVpnGateway.
        :type attachment_type: str
        """
        self._attachment_type = attachment_type

    @property
    def ip_version(self):
        r"""Gets the ip_version of this CreateResponseVpnGateway.

        网关的IP协议版本

        :return: The ip_version of this CreateResponseVpnGateway.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this CreateResponseVpnGateway.

        网关的IP协议版本

        :param ip_version: The ip_version of this CreateResponseVpnGateway.
        :type ip_version: str
        """
        self._ip_version = ip_version

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this CreateResponseVpnGateway.

        证书ID

        :return: The certificate_id of this CreateResponseVpnGateway.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this CreateResponseVpnGateway.

        证书ID

        :param certificate_id: The certificate_id of this CreateResponseVpnGateway.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def er_id(self):
        r"""Gets the er_id of this CreateResponseVpnGateway.

        VPN网关所连接的ER实例的ID

        :return: The er_id of this CreateResponseVpnGateway.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        r"""Sets the er_id of this CreateResponseVpnGateway.

        VPN网关所连接的ER实例的ID

        :param er_id: The er_id of this CreateResponseVpnGateway.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateResponseVpnGateway.

        VPN网关所连接的VPC的ID

        :return: The vpc_id of this CreateResponseVpnGateway.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateResponseVpnGateway.

        VPN网关所连接的VPC的ID

        :param vpc_id: The vpc_id of this CreateResponseVpnGateway.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def local_subnets(self):
        r"""Gets the local_subnets of this CreateResponseVpnGateway.

        本端子网

        :return: The local_subnets of this CreateResponseVpnGateway.
        :rtype: list[str]
        """
        return self._local_subnets

    @local_subnets.setter
    def local_subnets(self, local_subnets):
        r"""Sets the local_subnets of this CreateResponseVpnGateway.

        本端子网

        :param local_subnets: The local_subnets of this CreateResponseVpnGateway.
        :type local_subnets: list[str]
        """
        self._local_subnets = local_subnets

    @property
    def local_subnets_v6(self):
        r"""Gets the local_subnets_v6 of this CreateResponseVpnGateway.

        使能ipv6的本端子网

        :return: The local_subnets_v6 of this CreateResponseVpnGateway.
        :rtype: list[str]
        """
        return self._local_subnets_v6

    @local_subnets_v6.setter
    def local_subnets_v6(self, local_subnets_v6):
        r"""Sets the local_subnets_v6 of this CreateResponseVpnGateway.

        使能ipv6的本端子网

        :param local_subnets_v6: The local_subnets_v6 of this CreateResponseVpnGateway.
        :type local_subnets_v6: list[str]
        """
        self._local_subnets_v6 = local_subnets_v6

    @property
    def connect_subnet(self):
        r"""Gets the connect_subnet of this CreateResponseVpnGateway.

        VPN网关所使用的VPC子网ID

        :return: The connect_subnet of this CreateResponseVpnGateway.
        :rtype: str
        """
        return self._connect_subnet

    @connect_subnet.setter
    def connect_subnet(self, connect_subnet):
        r"""Sets the connect_subnet of this CreateResponseVpnGateway.

        VPN网关所使用的VPC子网ID

        :param connect_subnet: The connect_subnet of this CreateResponseVpnGateway.
        :type connect_subnet: str
        """
        self._connect_subnet = connect_subnet

    @property
    def network_type(self):
        r"""Gets the network_type of this CreateResponseVpnGateway.

        VPN网关的网络类型，默认为公网(public)

        :return: The network_type of this CreateResponseVpnGateway.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        r"""Sets the network_type of this CreateResponseVpnGateway.

        VPN网关的网络类型，默认为公网(public)

        :param network_type: The network_type of this CreateResponseVpnGateway.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def access_vpc_id(self):
        r"""Gets the access_vpc_id of this CreateResponseVpnGateway.

        VPN网关北向接入VPC ID，不填时默认使用vpc_id字段的值

        :return: The access_vpc_id of this CreateResponseVpnGateway.
        :rtype: str
        """
        return self._access_vpc_id

    @access_vpc_id.setter
    def access_vpc_id(self, access_vpc_id):
        r"""Sets the access_vpc_id of this CreateResponseVpnGateway.

        VPN网关北向接入VPC ID，不填时默认使用vpc_id字段的值

        :param access_vpc_id: The access_vpc_id of this CreateResponseVpnGateway.
        :type access_vpc_id: str
        """
        self._access_vpc_id = access_vpc_id

    @property
    def access_subnet_id(self):
        r"""Gets the access_subnet_id of this CreateResponseVpnGateway.

        VPN网关北向接入VPC中的接入子网ID

        :return: The access_subnet_id of this CreateResponseVpnGateway.
        :rtype: str
        """
        return self._access_subnet_id

    @access_subnet_id.setter
    def access_subnet_id(self, access_subnet_id):
        r"""Sets the access_subnet_id of this CreateResponseVpnGateway.

        VPN网关北向接入VPC中的接入子网ID

        :param access_subnet_id: The access_subnet_id of this CreateResponseVpnGateway.
        :type access_subnet_id: str
        """
        self._access_subnet_id = access_subnet_id

    @property
    def bgp_asn(self):
        r"""Gets the bgp_asn of this CreateResponseVpnGateway.

        bgp所使用的asn号

        :return: The bgp_asn of this CreateResponseVpnGateway.
        :rtype: int
        """
        return self._bgp_asn

    @bgp_asn.setter
    def bgp_asn(self, bgp_asn):
        r"""Sets the bgp_asn of this CreateResponseVpnGateway.

        bgp所使用的asn号

        :param bgp_asn: The bgp_asn of this CreateResponseVpnGateway.
        :type bgp_asn: int
        """
        self._bgp_asn = bgp_asn

    @property
    def flavor(self):
        r"""Gets the flavor of this CreateResponseVpnGateway.

        VPN网关的规格类型

        :return: The flavor of this CreateResponseVpnGateway.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this CreateResponseVpnGateway.

        VPN网关的规格类型

        :param flavor: The flavor of this CreateResponseVpnGateway.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def connection_number(self):
        r"""Gets the connection_number of this CreateResponseVpnGateway.

        最大可创建的VPN连接数

        :return: The connection_number of this CreateResponseVpnGateway.
        :rtype: int
        """
        return self._connection_number

    @connection_number.setter
    def connection_number(self, connection_number):
        r"""Sets the connection_number of this CreateResponseVpnGateway.

        最大可创建的VPN连接数

        :param connection_number: The connection_number of this CreateResponseVpnGateway.
        :type connection_number: int
        """
        self._connection_number = connection_number

    @property
    def used_connection_number(self):
        r"""Gets the used_connection_number of this CreateResponseVpnGateway.

        当前已经使用的VPN连接数

        :return: The used_connection_number of this CreateResponseVpnGateway.
        :rtype: int
        """
        return self._used_connection_number

    @used_connection_number.setter
    def used_connection_number(self, used_connection_number):
        r"""Sets the used_connection_number of this CreateResponseVpnGateway.

        当前已经使用的VPN连接数

        :param used_connection_number: The used_connection_number of this CreateResponseVpnGateway.
        :type used_connection_number: int
        """
        self._used_connection_number = used_connection_number

    @property
    def used_connection_group(self):
        r"""Gets the used_connection_group of this CreateResponseVpnGateway.

        当前已经使用的VPN连接组个数

        :return: The used_connection_group of this CreateResponseVpnGateway.
        :rtype: int
        """
        return self._used_connection_group

    @used_connection_group.setter
    def used_connection_group(self, used_connection_group):
        r"""Sets the used_connection_group of this CreateResponseVpnGateway.

        当前已经使用的VPN连接组个数

        :param used_connection_group: The used_connection_group of this CreateResponseVpnGateway.
        :type used_connection_group: int
        """
        self._used_connection_group = used_connection_group

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateResponseVpnGateway.

        企业项目ID

        :return: The enterprise_project_id of this CreateResponseVpnGateway.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateResponseVpnGateway.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateResponseVpnGateway.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ha_mode(self):
        r"""Gets the ha_mode of this CreateResponseVpnGateway.

        ha模式

        :return: The ha_mode of this CreateResponseVpnGateway.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        r"""Sets the ha_mode of this CreateResponseVpnGateway.

        ha模式

        :param ha_mode: The ha_mode of this CreateResponseVpnGateway.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def policy_template(self):
        r"""Gets the policy_template of this CreateResponseVpnGateway.

        :return: The policy_template of this CreateResponseVpnGateway.
        :rtype: :class:`huaweicloudsdkvpn.v5.PolicyTemplate`
        """
        return self._policy_template

    @policy_template.setter
    def policy_template(self, policy_template):
        r"""Sets the policy_template of this CreateResponseVpnGateway.

        :param policy_template: The policy_template of this CreateResponseVpnGateway.
        :type policy_template: :class:`huaweicloudsdkvpn.v5.PolicyTemplate`
        """
        self._policy_template = policy_template

    @property
    def tags(self):
        r"""Gets the tags of this CreateResponseVpnGateway.

        标签

        :return: The tags of this CreateResponseVpnGateway.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateResponseVpnGateway.

        标签

        :param tags: The tags of this CreateResponseVpnGateway.
        :type tags: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateResponseVpnGateway):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
