# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVgwRequestBodyContent:

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
        'attachment_type': 'str',
        'er_id': 'str',
        'vpc_id': 'str',
        'local_subnets': 'list[str]',
        'connect_subnet': 'str',
        'bgp_asn': 'int',
        'flavor': 'str',
        'availability_zone_ids': 'list[str]',
        'enterprise_project_id': 'str',
        'master_eip': 'CreateRequestEip',
        'slave_eip': 'CreateRequestEip',
        'eip1': 'CreateRequestEip',
        'eip2': 'CreateRequestEip',
        'network_type': 'str',
        'access_vpc_id': 'str',
        'access_subnet_id': 'str',
        'ha_mode': 'str'
    }

    attribute_map = {
        'name': 'name',
        'attachment_type': 'attachment_type',
        'er_id': 'er_id',
        'vpc_id': 'vpc_id',
        'local_subnets': 'local_subnets',
        'connect_subnet': 'connect_subnet',
        'bgp_asn': 'bgp_asn',
        'flavor': 'flavor',
        'availability_zone_ids': 'availability_zone_ids',
        'enterprise_project_id': 'enterprise_project_id',
        'master_eip': 'master_eip',
        'slave_eip': 'slave_eip',
        'eip1': 'eip1',
        'eip2': 'eip2',
        'network_type': 'network_type',
        'access_vpc_id': 'access_vpc_id',
        'access_subnet_id': 'access_subnet_id',
        'ha_mode': 'ha_mode'
    }

    def __init__(self, name=None, attachment_type=None, er_id=None, vpc_id=None, local_subnets=None, connect_subnet=None, bgp_asn=None, flavor=None, availability_zone_ids=None, enterprise_project_id=None, master_eip=None, slave_eip=None, eip1=None, eip2=None, network_type=None, access_vpc_id=None, access_subnet_id=None, ha_mode=None):
        """CreateVgwRequestBodyContent

        The model defined in huaweicloud sdk

        :param name: VPN网关名称
        :type name: str
        :param attachment_type: 关联模式
        :type attachment_type: str
        :param er_id: VPN网关所连接的ER实例的ID，当attachment_type配置为\&quot;er\&quot;时必填，否则不填
        :type er_id: str
        :param vpc_id: VPN网关所连接的VPC的ID
        :type vpc_id: str
        :param local_subnets: 本端子网，当attachment_type配置为\&quot;vpc\&quot;时必填，否则不填
        :type local_subnets: list[str]
        :param connect_subnet: VPN网关所使用的VPC子网ID
        :type connect_subnet: str
        :param bgp_asn: bgp所使用的asn号
        :type bgp_asn: int
        :param flavor: VPN网关的规格类型，当attachment_type为er时不能填写Basic
        :type flavor: str
        :param availability_zone_ids: 不填写则采用默认可用区。如果需要指定可用区可以调用查询VPN网关可用区接口来选择
        :type availability_zone_ids: list[str]
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param master_eip: 
        :type master_eip: :class:`huaweicloudsdkvpn.v5.CreateRequestEip`
        :param slave_eip: 
        :type slave_eip: :class:`huaweicloudsdkvpn.v5.CreateRequestEip`
        :param eip1: 
        :type eip1: :class:`huaweicloudsdkvpn.v5.CreateRequestEip`
        :param eip2: 
        :type eip2: :class:`huaweicloudsdkvpn.v5.CreateRequestEip`
        :param network_type: VPN网关北向类型，默认为公网(public)
        :type network_type: str
        :param access_vpc_id: VPN网关北向接入VPC ID，不填时默认使用vpc_id字段的值
        :type access_vpc_id: str
        :param access_subnet_id: VPN网关北向接入VPC中的接入子网ID，在填写了access_vpc_id时必填
        :type access_subnet_id: str
        :param ha_mode: ha模式
        :type ha_mode: str
        """
        
        

        self._name = None
        self._attachment_type = None
        self._er_id = None
        self._vpc_id = None
        self._local_subnets = None
        self._connect_subnet = None
        self._bgp_asn = None
        self._flavor = None
        self._availability_zone_ids = None
        self._enterprise_project_id = None
        self._master_eip = None
        self._slave_eip = None
        self._eip1 = None
        self._eip2 = None
        self._network_type = None
        self._access_vpc_id = None
        self._access_subnet_id = None
        self._ha_mode = None
        self.discriminator = None

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
        if bgp_asn is not None:
            self.bgp_asn = bgp_asn
        if flavor is not None:
            self.flavor = flavor
        if availability_zone_ids is not None:
            self.availability_zone_ids = availability_zone_ids
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if master_eip is not None:
            self.master_eip = master_eip
        if slave_eip is not None:
            self.slave_eip = slave_eip
        if eip1 is not None:
            self.eip1 = eip1
        if eip2 is not None:
            self.eip2 = eip2
        if network_type is not None:
            self.network_type = network_type
        if access_vpc_id is not None:
            self.access_vpc_id = access_vpc_id
        if access_subnet_id is not None:
            self.access_subnet_id = access_subnet_id
        if ha_mode is not None:
            self.ha_mode = ha_mode

    @property
    def name(self):
        """Gets the name of this CreateVgwRequestBodyContent.

        VPN网关名称

        :return: The name of this CreateVgwRequestBodyContent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVgwRequestBodyContent.

        VPN网关名称

        :param name: The name of this CreateVgwRequestBodyContent.
        :type name: str
        """
        self._name = name

    @property
    def attachment_type(self):
        """Gets the attachment_type of this CreateVgwRequestBodyContent.

        关联模式

        :return: The attachment_type of this CreateVgwRequestBodyContent.
        :rtype: str
        """
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, attachment_type):
        """Sets the attachment_type of this CreateVgwRequestBodyContent.

        关联模式

        :param attachment_type: The attachment_type of this CreateVgwRequestBodyContent.
        :type attachment_type: str
        """
        self._attachment_type = attachment_type

    @property
    def er_id(self):
        """Gets the er_id of this CreateVgwRequestBodyContent.

        VPN网关所连接的ER实例的ID，当attachment_type配置为\"er\"时必填，否则不填

        :return: The er_id of this CreateVgwRequestBodyContent.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        """Sets the er_id of this CreateVgwRequestBodyContent.

        VPN网关所连接的ER实例的ID，当attachment_type配置为\"er\"时必填，否则不填

        :param er_id: The er_id of this CreateVgwRequestBodyContent.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateVgwRequestBodyContent.

        VPN网关所连接的VPC的ID

        :return: The vpc_id of this CreateVgwRequestBodyContent.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateVgwRequestBodyContent.

        VPN网关所连接的VPC的ID

        :param vpc_id: The vpc_id of this CreateVgwRequestBodyContent.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def local_subnets(self):
        """Gets the local_subnets of this CreateVgwRequestBodyContent.

        本端子网，当attachment_type配置为\"vpc\"时必填，否则不填

        :return: The local_subnets of this CreateVgwRequestBodyContent.
        :rtype: list[str]
        """
        return self._local_subnets

    @local_subnets.setter
    def local_subnets(self, local_subnets):
        """Sets the local_subnets of this CreateVgwRequestBodyContent.

        本端子网，当attachment_type配置为\"vpc\"时必填，否则不填

        :param local_subnets: The local_subnets of this CreateVgwRequestBodyContent.
        :type local_subnets: list[str]
        """
        self._local_subnets = local_subnets

    @property
    def connect_subnet(self):
        """Gets the connect_subnet of this CreateVgwRequestBodyContent.

        VPN网关所使用的VPC子网ID

        :return: The connect_subnet of this CreateVgwRequestBodyContent.
        :rtype: str
        """
        return self._connect_subnet

    @connect_subnet.setter
    def connect_subnet(self, connect_subnet):
        """Sets the connect_subnet of this CreateVgwRequestBodyContent.

        VPN网关所使用的VPC子网ID

        :param connect_subnet: The connect_subnet of this CreateVgwRequestBodyContent.
        :type connect_subnet: str
        """
        self._connect_subnet = connect_subnet

    @property
    def bgp_asn(self):
        """Gets the bgp_asn of this CreateVgwRequestBodyContent.

        bgp所使用的asn号

        :return: The bgp_asn of this CreateVgwRequestBodyContent.
        :rtype: int
        """
        return self._bgp_asn

    @bgp_asn.setter
    def bgp_asn(self, bgp_asn):
        """Sets the bgp_asn of this CreateVgwRequestBodyContent.

        bgp所使用的asn号

        :param bgp_asn: The bgp_asn of this CreateVgwRequestBodyContent.
        :type bgp_asn: int
        """
        self._bgp_asn = bgp_asn

    @property
    def flavor(self):
        """Gets the flavor of this CreateVgwRequestBodyContent.

        VPN网关的规格类型，当attachment_type为er时不能填写Basic

        :return: The flavor of this CreateVgwRequestBodyContent.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this CreateVgwRequestBodyContent.

        VPN网关的规格类型，当attachment_type为er时不能填写Basic

        :param flavor: The flavor of this CreateVgwRequestBodyContent.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def availability_zone_ids(self):
        """Gets the availability_zone_ids of this CreateVgwRequestBodyContent.

        不填写则采用默认可用区。如果需要指定可用区可以调用查询VPN网关可用区接口来选择

        :return: The availability_zone_ids of this CreateVgwRequestBodyContent.
        :rtype: list[str]
        """
        return self._availability_zone_ids

    @availability_zone_ids.setter
    def availability_zone_ids(self, availability_zone_ids):
        """Sets the availability_zone_ids of this CreateVgwRequestBodyContent.

        不填写则采用默认可用区。如果需要指定可用区可以调用查询VPN网关可用区接口来选择

        :param availability_zone_ids: The availability_zone_ids of this CreateVgwRequestBodyContent.
        :type availability_zone_ids: list[str]
        """
        self._availability_zone_ids = availability_zone_ids

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateVgwRequestBodyContent.

        企业项目ID

        :return: The enterprise_project_id of this CreateVgwRequestBodyContent.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateVgwRequestBodyContent.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateVgwRequestBodyContent.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def master_eip(self):
        """Gets the master_eip of this CreateVgwRequestBodyContent.

        :return: The master_eip of this CreateVgwRequestBodyContent.
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateRequestEip`
        """
        return self._master_eip

    @master_eip.setter
    def master_eip(self, master_eip):
        """Sets the master_eip of this CreateVgwRequestBodyContent.

        :param master_eip: The master_eip of this CreateVgwRequestBodyContent.
        :type master_eip: :class:`huaweicloudsdkvpn.v5.CreateRequestEip`
        """
        self._master_eip = master_eip

    @property
    def slave_eip(self):
        """Gets the slave_eip of this CreateVgwRequestBodyContent.

        :return: The slave_eip of this CreateVgwRequestBodyContent.
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateRequestEip`
        """
        return self._slave_eip

    @slave_eip.setter
    def slave_eip(self, slave_eip):
        """Sets the slave_eip of this CreateVgwRequestBodyContent.

        :param slave_eip: The slave_eip of this CreateVgwRequestBodyContent.
        :type slave_eip: :class:`huaweicloudsdkvpn.v5.CreateRequestEip`
        """
        self._slave_eip = slave_eip

    @property
    def eip1(self):
        """Gets the eip1 of this CreateVgwRequestBodyContent.

        :return: The eip1 of this CreateVgwRequestBodyContent.
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateRequestEip`
        """
        return self._eip1

    @eip1.setter
    def eip1(self, eip1):
        """Sets the eip1 of this CreateVgwRequestBodyContent.

        :param eip1: The eip1 of this CreateVgwRequestBodyContent.
        :type eip1: :class:`huaweicloudsdkvpn.v5.CreateRequestEip`
        """
        self._eip1 = eip1

    @property
    def eip2(self):
        """Gets the eip2 of this CreateVgwRequestBodyContent.

        :return: The eip2 of this CreateVgwRequestBodyContent.
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateRequestEip`
        """
        return self._eip2

    @eip2.setter
    def eip2(self, eip2):
        """Sets the eip2 of this CreateVgwRequestBodyContent.

        :param eip2: The eip2 of this CreateVgwRequestBodyContent.
        :type eip2: :class:`huaweicloudsdkvpn.v5.CreateRequestEip`
        """
        self._eip2 = eip2

    @property
    def network_type(self):
        """Gets the network_type of this CreateVgwRequestBodyContent.

        VPN网关北向类型，默认为公网(public)

        :return: The network_type of this CreateVgwRequestBodyContent.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this CreateVgwRequestBodyContent.

        VPN网关北向类型，默认为公网(public)

        :param network_type: The network_type of this CreateVgwRequestBodyContent.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def access_vpc_id(self):
        """Gets the access_vpc_id of this CreateVgwRequestBodyContent.

        VPN网关北向接入VPC ID，不填时默认使用vpc_id字段的值

        :return: The access_vpc_id of this CreateVgwRequestBodyContent.
        :rtype: str
        """
        return self._access_vpc_id

    @access_vpc_id.setter
    def access_vpc_id(self, access_vpc_id):
        """Sets the access_vpc_id of this CreateVgwRequestBodyContent.

        VPN网关北向接入VPC ID，不填时默认使用vpc_id字段的值

        :param access_vpc_id: The access_vpc_id of this CreateVgwRequestBodyContent.
        :type access_vpc_id: str
        """
        self._access_vpc_id = access_vpc_id

    @property
    def access_subnet_id(self):
        """Gets the access_subnet_id of this CreateVgwRequestBodyContent.

        VPN网关北向接入VPC中的接入子网ID，在填写了access_vpc_id时必填

        :return: The access_subnet_id of this CreateVgwRequestBodyContent.
        :rtype: str
        """
        return self._access_subnet_id

    @access_subnet_id.setter
    def access_subnet_id(self, access_subnet_id):
        """Sets the access_subnet_id of this CreateVgwRequestBodyContent.

        VPN网关北向接入VPC中的接入子网ID，在填写了access_vpc_id时必填

        :param access_subnet_id: The access_subnet_id of this CreateVgwRequestBodyContent.
        :type access_subnet_id: str
        """
        self._access_subnet_id = access_subnet_id

    @property
    def ha_mode(self):
        """Gets the ha_mode of this CreateVgwRequestBodyContent.

        ha模式

        :return: The ha_mode of this CreateVgwRequestBodyContent.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        """Sets the ha_mode of this CreateVgwRequestBodyContent.

        ha模式

        :param ha_mode: The ha_mode of this CreateVgwRequestBodyContent.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

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
        if not isinstance(other, CreateVgwRequestBodyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
