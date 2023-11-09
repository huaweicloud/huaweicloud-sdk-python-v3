# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateResponseVpnGateway:

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
        'er_id': 'str',
        'vpc_id': 'str',
        'local_subnets': 'list[str]',
        'connect_subnet': 'str',
        'network_type': 'str',
        'access_vpc_id': 'str',
        'access_subnet_id': 'str',
        'access_private_ips': 'list[str]',
        'access_private_ip_1': 'str',
        'access_private_ip_2': 'str',
        'bgp_asn': 'int',
        'flavor': 'str',
        'availability_zone_ids': 'list[str]',
        'connection_number': 'int',
        'used_connection_number': 'int',
        'used_connection_group': 'int',
        'enterprise_project_id': 'str',
        'ha_mode': 'str',
        'master_eip': 'ResponseEip',
        'slave_eip': 'ResponseEip',
        'eip1': 'ResponseEip',
        'eip2': 'ResponseEip',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'attachment_type': 'attachment_type',
        'er_id': 'er_id',
        'vpc_id': 'vpc_id',
        'local_subnets': 'local_subnets',
        'connect_subnet': 'connect_subnet',
        'network_type': 'network_type',
        'access_vpc_id': 'access_vpc_id',
        'access_subnet_id': 'access_subnet_id',
        'access_private_ips': 'access_private_ips',
        'access_private_ip_1': 'access_private_ip_1',
        'access_private_ip_2': 'access_private_ip_2',
        'bgp_asn': 'bgp_asn',
        'flavor': 'flavor',
        'availability_zone_ids': 'availability_zone_ids',
        'connection_number': 'connection_number',
        'used_connection_number': 'used_connection_number',
        'used_connection_group': 'used_connection_group',
        'enterprise_project_id': 'enterprise_project_id',
        'ha_mode': 'ha_mode',
        'master_eip': 'master_eip',
        'slave_eip': 'slave_eip',
        'eip1': 'eip1',
        'eip2': 'eip2',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, attachment_type=None, er_id=None, vpc_id=None, local_subnets=None, connect_subnet=None, network_type=None, access_vpc_id=None, access_subnet_id=None, access_private_ips=None, access_private_ip_1=None, access_private_ip_2=None, bgp_asn=None, flavor=None, availability_zone_ids=None, connection_number=None, used_connection_number=None, used_connection_group=None, enterprise_project_id=None, ha_mode=None, master_eip=None, slave_eip=None, eip1=None, eip2=None, created_at=None, updated_at=None):
        """UpdateResponseVpnGateway

        The model defined in huaweicloud sdk

        :param id: VPN网关ID
        :type id: str
        :param name: VPN网关名称
        :type name: str
        :param attachment_type: 关联模式
        :type attachment_type: str
        :param er_id: VPN网关所连接的ER实例的ID
        :type er_id: str
        :param vpc_id: VPN网关所连接的VPC的ID
        :type vpc_id: str
        :param local_subnets: 本端子网
        :type local_subnets: list[str]
        :param connect_subnet: VPN网关所使用的VPC子网ID
        :type connect_subnet: str
        :param network_type: VPN网关北向类型，默认为公网(public)
        :type network_type: str
        :param access_vpc_id: VPN网关北向接入VPC ID，不填时默认使用vpc_id字段的值
        :type access_vpc_id: str
        :param access_subnet_id: VPN网关北向接入VPC中的接入子网ID
        :type access_subnet_id: str
        :param access_private_ips: VPN网关北向接入私网IP列表，当VPN网关的北向类型是私网(private)时有值
        :type access_private_ips: list[str]
        :param access_private_ip_1: VPN网关北向接入私网IP列表，当VPN网关的北向类型是私网(private)时有值,主备模式代表主worker的私网IP
        :type access_private_ip_1: str
        :param access_private_ip_2: VPN网关北向接入私网IP列表，当VPN网关的北向类型是私网(private)时有值,主备模式代表备worker的私网IP
        :type access_private_ip_2: str
        :param bgp_asn: bgp所使用的asn号
        :type bgp_asn: int
        :param flavor: VPN网关的规格类型
        :type flavor: str
        :param availability_zone_ids: 可用区列表
        :type availability_zone_ids: list[str]
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
        :param master_eip: 
        :type master_eip: :class:`huaweicloudsdkvpn.v5.ResponseEip`
        :param slave_eip: 
        :type slave_eip: :class:`huaweicloudsdkvpn.v5.ResponseEip`
        :param eip1: 
        :type eip1: :class:`huaweicloudsdkvpn.v5.ResponseEip`
        :param eip2: 
        :type eip2: :class:`huaweicloudsdkvpn.v5.ResponseEip`
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._attachment_type = None
        self._er_id = None
        self._vpc_id = None
        self._local_subnets = None
        self._connect_subnet = None
        self._network_type = None
        self._access_vpc_id = None
        self._access_subnet_id = None
        self._access_private_ips = None
        self._access_private_ip_1 = None
        self._access_private_ip_2 = None
        self._bgp_asn = None
        self._flavor = None
        self._availability_zone_ids = None
        self._connection_number = None
        self._used_connection_number = None
        self._used_connection_group = None
        self._enterprise_project_id = None
        self._ha_mode = None
        self._master_eip = None
        self._slave_eip = None
        self._eip1 = None
        self._eip2 = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if attachment_type is not None:
            self.attachment_type = attachment_type
        if er_id is not None:
            self.er_id = er_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if local_subnets is not None:
            self.local_subnets = local_subnets
        if connect_subnet is not None:
            self.connect_subnet = connect_subnet
        if network_type is not None:
            self.network_type = network_type
        if access_vpc_id is not None:
            self.access_vpc_id = access_vpc_id
        if access_subnet_id is not None:
            self.access_subnet_id = access_subnet_id
        if access_private_ips is not None:
            self.access_private_ips = access_private_ips
        if access_private_ip_1 is not None:
            self.access_private_ip_1 = access_private_ip_1
        if access_private_ip_2 is not None:
            self.access_private_ip_2 = access_private_ip_2
        if bgp_asn is not None:
            self.bgp_asn = bgp_asn
        if flavor is not None:
            self.flavor = flavor
        if availability_zone_ids is not None:
            self.availability_zone_ids = availability_zone_ids
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
        if master_eip is not None:
            self.master_eip = master_eip
        if slave_eip is not None:
            self.slave_eip = slave_eip
        if eip1 is not None:
            self.eip1 = eip1
        if eip2 is not None:
            self.eip2 = eip2
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this UpdateResponseVpnGateway.

        VPN网关ID

        :return: The id of this UpdateResponseVpnGateway.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateResponseVpnGateway.

        VPN网关ID

        :param id: The id of this UpdateResponseVpnGateway.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateResponseVpnGateway.

        VPN网关名称

        :return: The name of this UpdateResponseVpnGateway.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateResponseVpnGateway.

        VPN网关名称

        :param name: The name of this UpdateResponseVpnGateway.
        :type name: str
        """
        self._name = name

    @property
    def attachment_type(self):
        """Gets the attachment_type of this UpdateResponseVpnGateway.

        关联模式

        :return: The attachment_type of this UpdateResponseVpnGateway.
        :rtype: str
        """
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, attachment_type):
        """Sets the attachment_type of this UpdateResponseVpnGateway.

        关联模式

        :param attachment_type: The attachment_type of this UpdateResponseVpnGateway.
        :type attachment_type: str
        """
        self._attachment_type = attachment_type

    @property
    def er_id(self):
        """Gets the er_id of this UpdateResponseVpnGateway.

        VPN网关所连接的ER实例的ID

        :return: The er_id of this UpdateResponseVpnGateway.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        """Sets the er_id of this UpdateResponseVpnGateway.

        VPN网关所连接的ER实例的ID

        :param er_id: The er_id of this UpdateResponseVpnGateway.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this UpdateResponseVpnGateway.

        VPN网关所连接的VPC的ID

        :return: The vpc_id of this UpdateResponseVpnGateway.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this UpdateResponseVpnGateway.

        VPN网关所连接的VPC的ID

        :param vpc_id: The vpc_id of this UpdateResponseVpnGateway.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def local_subnets(self):
        """Gets the local_subnets of this UpdateResponseVpnGateway.

        本端子网

        :return: The local_subnets of this UpdateResponseVpnGateway.
        :rtype: list[str]
        """
        return self._local_subnets

    @local_subnets.setter
    def local_subnets(self, local_subnets):
        """Sets the local_subnets of this UpdateResponseVpnGateway.

        本端子网

        :param local_subnets: The local_subnets of this UpdateResponseVpnGateway.
        :type local_subnets: list[str]
        """
        self._local_subnets = local_subnets

    @property
    def connect_subnet(self):
        """Gets the connect_subnet of this UpdateResponseVpnGateway.

        VPN网关所使用的VPC子网ID

        :return: The connect_subnet of this UpdateResponseVpnGateway.
        :rtype: str
        """
        return self._connect_subnet

    @connect_subnet.setter
    def connect_subnet(self, connect_subnet):
        """Sets the connect_subnet of this UpdateResponseVpnGateway.

        VPN网关所使用的VPC子网ID

        :param connect_subnet: The connect_subnet of this UpdateResponseVpnGateway.
        :type connect_subnet: str
        """
        self._connect_subnet = connect_subnet

    @property
    def network_type(self):
        """Gets the network_type of this UpdateResponseVpnGateway.

        VPN网关北向类型，默认为公网(public)

        :return: The network_type of this UpdateResponseVpnGateway.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this UpdateResponseVpnGateway.

        VPN网关北向类型，默认为公网(public)

        :param network_type: The network_type of this UpdateResponseVpnGateway.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def access_vpc_id(self):
        """Gets the access_vpc_id of this UpdateResponseVpnGateway.

        VPN网关北向接入VPC ID，不填时默认使用vpc_id字段的值

        :return: The access_vpc_id of this UpdateResponseVpnGateway.
        :rtype: str
        """
        return self._access_vpc_id

    @access_vpc_id.setter
    def access_vpc_id(self, access_vpc_id):
        """Sets the access_vpc_id of this UpdateResponseVpnGateway.

        VPN网关北向接入VPC ID，不填时默认使用vpc_id字段的值

        :param access_vpc_id: The access_vpc_id of this UpdateResponseVpnGateway.
        :type access_vpc_id: str
        """
        self._access_vpc_id = access_vpc_id

    @property
    def access_subnet_id(self):
        """Gets the access_subnet_id of this UpdateResponseVpnGateway.

        VPN网关北向接入VPC中的接入子网ID

        :return: The access_subnet_id of this UpdateResponseVpnGateway.
        :rtype: str
        """
        return self._access_subnet_id

    @access_subnet_id.setter
    def access_subnet_id(self, access_subnet_id):
        """Sets the access_subnet_id of this UpdateResponseVpnGateway.

        VPN网关北向接入VPC中的接入子网ID

        :param access_subnet_id: The access_subnet_id of this UpdateResponseVpnGateway.
        :type access_subnet_id: str
        """
        self._access_subnet_id = access_subnet_id

    @property
    def access_private_ips(self):
        """Gets the access_private_ips of this UpdateResponseVpnGateway.

        VPN网关北向接入私网IP列表，当VPN网关的北向类型是私网(private)时有值

        :return: The access_private_ips of this UpdateResponseVpnGateway.
        :rtype: list[str]
        """
        return self._access_private_ips

    @access_private_ips.setter
    def access_private_ips(self, access_private_ips):
        """Sets the access_private_ips of this UpdateResponseVpnGateway.

        VPN网关北向接入私网IP列表，当VPN网关的北向类型是私网(private)时有值

        :param access_private_ips: The access_private_ips of this UpdateResponseVpnGateway.
        :type access_private_ips: list[str]
        """
        self._access_private_ips = access_private_ips

    @property
    def access_private_ip_1(self):
        """Gets the access_private_ip_1 of this UpdateResponseVpnGateway.

        VPN网关北向接入私网IP列表，当VPN网关的北向类型是私网(private)时有值,主备模式代表主worker的私网IP

        :return: The access_private_ip_1 of this UpdateResponseVpnGateway.
        :rtype: str
        """
        return self._access_private_ip_1

    @access_private_ip_1.setter
    def access_private_ip_1(self, access_private_ip_1):
        """Sets the access_private_ip_1 of this UpdateResponseVpnGateway.

        VPN网关北向接入私网IP列表，当VPN网关的北向类型是私网(private)时有值,主备模式代表主worker的私网IP

        :param access_private_ip_1: The access_private_ip_1 of this UpdateResponseVpnGateway.
        :type access_private_ip_1: str
        """
        self._access_private_ip_1 = access_private_ip_1

    @property
    def access_private_ip_2(self):
        """Gets the access_private_ip_2 of this UpdateResponseVpnGateway.

        VPN网关北向接入私网IP列表，当VPN网关的北向类型是私网(private)时有值,主备模式代表备worker的私网IP

        :return: The access_private_ip_2 of this UpdateResponseVpnGateway.
        :rtype: str
        """
        return self._access_private_ip_2

    @access_private_ip_2.setter
    def access_private_ip_2(self, access_private_ip_2):
        """Sets the access_private_ip_2 of this UpdateResponseVpnGateway.

        VPN网关北向接入私网IP列表，当VPN网关的北向类型是私网(private)时有值,主备模式代表备worker的私网IP

        :param access_private_ip_2: The access_private_ip_2 of this UpdateResponseVpnGateway.
        :type access_private_ip_2: str
        """
        self._access_private_ip_2 = access_private_ip_2

    @property
    def bgp_asn(self):
        """Gets the bgp_asn of this UpdateResponseVpnGateway.

        bgp所使用的asn号

        :return: The bgp_asn of this UpdateResponseVpnGateway.
        :rtype: int
        """
        return self._bgp_asn

    @bgp_asn.setter
    def bgp_asn(self, bgp_asn):
        """Sets the bgp_asn of this UpdateResponseVpnGateway.

        bgp所使用的asn号

        :param bgp_asn: The bgp_asn of this UpdateResponseVpnGateway.
        :type bgp_asn: int
        """
        self._bgp_asn = bgp_asn

    @property
    def flavor(self):
        """Gets the flavor of this UpdateResponseVpnGateway.

        VPN网关的规格类型

        :return: The flavor of this UpdateResponseVpnGateway.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this UpdateResponseVpnGateway.

        VPN网关的规格类型

        :param flavor: The flavor of this UpdateResponseVpnGateway.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def availability_zone_ids(self):
        """Gets the availability_zone_ids of this UpdateResponseVpnGateway.

        可用区列表

        :return: The availability_zone_ids of this UpdateResponseVpnGateway.
        :rtype: list[str]
        """
        return self._availability_zone_ids

    @availability_zone_ids.setter
    def availability_zone_ids(self, availability_zone_ids):
        """Sets the availability_zone_ids of this UpdateResponseVpnGateway.

        可用区列表

        :param availability_zone_ids: The availability_zone_ids of this UpdateResponseVpnGateway.
        :type availability_zone_ids: list[str]
        """
        self._availability_zone_ids = availability_zone_ids

    @property
    def connection_number(self):
        """Gets the connection_number of this UpdateResponseVpnGateway.

        最大可创建的VPN连接数

        :return: The connection_number of this UpdateResponseVpnGateway.
        :rtype: int
        """
        return self._connection_number

    @connection_number.setter
    def connection_number(self, connection_number):
        """Sets the connection_number of this UpdateResponseVpnGateway.

        最大可创建的VPN连接数

        :param connection_number: The connection_number of this UpdateResponseVpnGateway.
        :type connection_number: int
        """
        self._connection_number = connection_number

    @property
    def used_connection_number(self):
        """Gets the used_connection_number of this UpdateResponseVpnGateway.

        当前已经使用的VPN连接数

        :return: The used_connection_number of this UpdateResponseVpnGateway.
        :rtype: int
        """
        return self._used_connection_number

    @used_connection_number.setter
    def used_connection_number(self, used_connection_number):
        """Sets the used_connection_number of this UpdateResponseVpnGateway.

        当前已经使用的VPN连接数

        :param used_connection_number: The used_connection_number of this UpdateResponseVpnGateway.
        :type used_connection_number: int
        """
        self._used_connection_number = used_connection_number

    @property
    def used_connection_group(self):
        """Gets the used_connection_group of this UpdateResponseVpnGateway.

        当前已经使用的VPN连接组个数

        :return: The used_connection_group of this UpdateResponseVpnGateway.
        :rtype: int
        """
        return self._used_connection_group

    @used_connection_group.setter
    def used_connection_group(self, used_connection_group):
        """Sets the used_connection_group of this UpdateResponseVpnGateway.

        当前已经使用的VPN连接组个数

        :param used_connection_group: The used_connection_group of this UpdateResponseVpnGateway.
        :type used_connection_group: int
        """
        self._used_connection_group = used_connection_group

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this UpdateResponseVpnGateway.

        企业项目ID

        :return: The enterprise_project_id of this UpdateResponseVpnGateway.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this UpdateResponseVpnGateway.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this UpdateResponseVpnGateway.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ha_mode(self):
        """Gets the ha_mode of this UpdateResponseVpnGateway.

        ha模式

        :return: The ha_mode of this UpdateResponseVpnGateway.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        """Sets the ha_mode of this UpdateResponseVpnGateway.

        ha模式

        :param ha_mode: The ha_mode of this UpdateResponseVpnGateway.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def master_eip(self):
        """Gets the master_eip of this UpdateResponseVpnGateway.

        :return: The master_eip of this UpdateResponseVpnGateway.
        :rtype: :class:`huaweicloudsdkvpn.v5.ResponseEip`
        """
        return self._master_eip

    @master_eip.setter
    def master_eip(self, master_eip):
        """Sets the master_eip of this UpdateResponseVpnGateway.

        :param master_eip: The master_eip of this UpdateResponseVpnGateway.
        :type master_eip: :class:`huaweicloudsdkvpn.v5.ResponseEip`
        """
        self._master_eip = master_eip

    @property
    def slave_eip(self):
        """Gets the slave_eip of this UpdateResponseVpnGateway.

        :return: The slave_eip of this UpdateResponseVpnGateway.
        :rtype: :class:`huaweicloudsdkvpn.v5.ResponseEip`
        """
        return self._slave_eip

    @slave_eip.setter
    def slave_eip(self, slave_eip):
        """Sets the slave_eip of this UpdateResponseVpnGateway.

        :param slave_eip: The slave_eip of this UpdateResponseVpnGateway.
        :type slave_eip: :class:`huaweicloudsdkvpn.v5.ResponseEip`
        """
        self._slave_eip = slave_eip

    @property
    def eip1(self):
        """Gets the eip1 of this UpdateResponseVpnGateway.

        :return: The eip1 of this UpdateResponseVpnGateway.
        :rtype: :class:`huaweicloudsdkvpn.v5.ResponseEip`
        """
        return self._eip1

    @eip1.setter
    def eip1(self, eip1):
        """Sets the eip1 of this UpdateResponseVpnGateway.

        :param eip1: The eip1 of this UpdateResponseVpnGateway.
        :type eip1: :class:`huaweicloudsdkvpn.v5.ResponseEip`
        """
        self._eip1 = eip1

    @property
    def eip2(self):
        """Gets the eip2 of this UpdateResponseVpnGateway.

        :return: The eip2 of this UpdateResponseVpnGateway.
        :rtype: :class:`huaweicloudsdkvpn.v5.ResponseEip`
        """
        return self._eip2

    @eip2.setter
    def eip2(self, eip2):
        """Sets the eip2 of this UpdateResponseVpnGateway.

        :param eip2: The eip2 of this UpdateResponseVpnGateway.
        :type eip2: :class:`huaweicloudsdkvpn.v5.ResponseEip`
        """
        self._eip2 = eip2

    @property
    def created_at(self):
        """Gets the created_at of this UpdateResponseVpnGateway.

        创建时间

        :return: The created_at of this UpdateResponseVpnGateway.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UpdateResponseVpnGateway.

        创建时间

        :param created_at: The created_at of this UpdateResponseVpnGateway.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this UpdateResponseVpnGateway.

        更新时间

        :return: The updated_at of this UpdateResponseVpnGateway.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UpdateResponseVpnGateway.

        更新时间

        :param updated_at: The updated_at of this UpdateResponseVpnGateway.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, UpdateResponseVpnGateway):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
