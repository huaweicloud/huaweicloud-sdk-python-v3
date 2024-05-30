# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDetailDTO:

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
        'description': 'str',
        'external_address': 'str',
        'intranet_address': 'str',
        'intranet_address_ipv6': 'str',
        'public_zone_id': 'str',
        'public_zone_name': 'str',
        'private_zone_id': 'str',
        'private_zone_name': 'str',
        'enterprise_project_id': 'str',
        'create_time': 'int',
        'create_user': 'str',
        'current_namespace_publish_api_num': 'int',
        'all_namespace_publish_api_num': 'int',
        'api_publishable_num': 'int',
        'deletable': 'bool',
        'charge_status': 'str',
        'order_id': 'str',
        'order_type': 'str',
        'period_type': 'str',
        'instance_status': 'str',
        'node_num': 'int',
        'flavor': 'FlavorDTO',
        'gateway_version': 'str',
        'availability_zone': 'str',
        'availability_zone_name': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'nodes': 'list[InstanceNodeDTO]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'external_address': 'external_address',
        'intranet_address': 'intranet_address',
        'intranet_address_ipv6': 'intranet_address_ipv6',
        'public_zone_id': 'public_zone_id',
        'public_zone_name': 'public_zone_name',
        'private_zone_id': 'private_zone_id',
        'private_zone_name': 'private_zone_name',
        'enterprise_project_id': 'enterprise_project_id',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'current_namespace_publish_api_num': 'current_namespace_publish_api_num',
        'all_namespace_publish_api_num': 'all_namespace_publish_api_num',
        'api_publishable_num': 'api_publishable_num',
        'deletable': 'deletable',
        'charge_status': 'charge_status',
        'order_id': 'order_id',
        'order_type': 'order_type',
        'period_type': 'period_type',
        'instance_status': 'instance_status',
        'node_num': 'node_num',
        'flavor': 'flavor',
        'gateway_version': 'gateway_version',
        'availability_zone': 'availability_zone',
        'availability_zone_name': 'availability_zone_name',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'nodes': 'nodes'
    }

    def __init__(self, id=None, name=None, description=None, external_address=None, intranet_address=None, intranet_address_ipv6=None, public_zone_id=None, public_zone_name=None, private_zone_id=None, private_zone_name=None, enterprise_project_id=None, create_time=None, create_user=None, current_namespace_publish_api_num=None, all_namespace_publish_api_num=None, api_publishable_num=None, deletable=None, charge_status=None, order_id=None, order_type=None, period_type=None, instance_status=None, node_num=None, flavor=None, gateway_version=None, availability_zone=None, availability_zone_name=None, vpc_id=None, subnet_id=None, security_group_id=None, nodes=None):
        """InstanceDetailDTO

        The model defined in huaweicloud sdk

        :param id: 集群ID。
        :type id: str
        :param name: 集群名称。
        :type name: str
        :param description: 集群描述信息。
        :type description: str
        :param external_address: 公网IP地址。
        :type external_address: str
        :param intranet_address: 内网IPv4地址。
        :type intranet_address: str
        :param intranet_address_ipv6: 内网IPv6地址。
        :type intranet_address_ipv6: str
        :param public_zone_id: 公网域名ID。
        :type public_zone_id: str
        :param public_zone_name: 公网域名名称。
        :type public_zone_name: str
        :param private_zone_id: 内网域名ID。
        :type private_zone_id: str
        :param private_zone_name: 内网域名名称。
        :type private_zone_name: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param create_time: 创建时间。
        :type create_time: int
        :param create_user: 创建人。
        :type create_user: str
        :param current_namespace_publish_api_num: 当前工作空间已发布的API数量。
        :type current_namespace_publish_api_num: int
        :param all_namespace_publish_api_num: 所有工作空间已发布的API数量。
        :type all_namespace_publish_api_num: int
        :param api_publishable_num: 集群API总配额。
        :type api_publishable_num: int
        :param deletable: 集群是否可以删除。
        :type deletable: bool
        :param charge_status: 集群计费状态，NO_CHARGE：未计费、CHARGED：已计费，GRACE：宽限期、RETENTION：保留期。
        :type charge_status: str
        :param order_id: 订单ID。
        :type order_id: str
        :param order_type: 订单类型，PERIOD：包周期、ON_DEMAND：按需。
        :type order_type: str
        :param period_type: 集群订购周期类型。
        :type period_type: str
        :param instance_status: 集群状态。
        :type instance_status: str
        :param node_num: 节点数量。
        :type node_num: int
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkdataartsstudio.v1.FlavorDTO`
        :param gateway_version: 集群版本号。
        :type gateway_version: str
        :param availability_zone: 集群所在可用区编码。
        :type availability_zone: str
        :param availability_zone_name: 集群所在可用区名称。
        :type availability_zone_name: str
        :param vpc_id: 集群所在虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 集群所在子网ID。
        :type subnet_id: str
        :param security_group_id: 集群所在安全组ID。
        :type security_group_id: str
        :param nodes: 集群节点列表。
        :type nodes: list[:class:`huaweicloudsdkdataartsstudio.v1.InstanceNodeDTO`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._external_address = None
        self._intranet_address = None
        self._intranet_address_ipv6 = None
        self._public_zone_id = None
        self._public_zone_name = None
        self._private_zone_id = None
        self._private_zone_name = None
        self._enterprise_project_id = None
        self._create_time = None
        self._create_user = None
        self._current_namespace_publish_api_num = None
        self._all_namespace_publish_api_num = None
        self._api_publishable_num = None
        self._deletable = None
        self._charge_status = None
        self._order_id = None
        self._order_type = None
        self._period_type = None
        self._instance_status = None
        self._node_num = None
        self._flavor = None
        self._gateway_version = None
        self._availability_zone = None
        self._availability_zone_name = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._nodes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if external_address is not None:
            self.external_address = external_address
        if intranet_address is not None:
            self.intranet_address = intranet_address
        if intranet_address_ipv6 is not None:
            self.intranet_address_ipv6 = intranet_address_ipv6
        if public_zone_id is not None:
            self.public_zone_id = public_zone_id
        if public_zone_name is not None:
            self.public_zone_name = public_zone_name
        if private_zone_id is not None:
            self.private_zone_id = private_zone_id
        if private_zone_name is not None:
            self.private_zone_name = private_zone_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if current_namespace_publish_api_num is not None:
            self.current_namespace_publish_api_num = current_namespace_publish_api_num
        if all_namespace_publish_api_num is not None:
            self.all_namespace_publish_api_num = all_namespace_publish_api_num
        if api_publishable_num is not None:
            self.api_publishable_num = api_publishable_num
        if deletable is not None:
            self.deletable = deletable
        if charge_status is not None:
            self.charge_status = charge_status
        if order_id is not None:
            self.order_id = order_id
        if order_type is not None:
            self.order_type = order_type
        if period_type is not None:
            self.period_type = period_type
        if instance_status is not None:
            self.instance_status = instance_status
        if node_num is not None:
            self.node_num = node_num
        if flavor is not None:
            self.flavor = flavor
        if gateway_version is not None:
            self.gateway_version = gateway_version
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if availability_zone_name is not None:
            self.availability_zone_name = availability_zone_name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if nodes is not None:
            self.nodes = nodes

    @property
    def id(self):
        """Gets the id of this InstanceDetailDTO.

        集群ID。

        :return: The id of this InstanceDetailDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstanceDetailDTO.

        集群ID。

        :param id: The id of this InstanceDetailDTO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this InstanceDetailDTO.

        集群名称。

        :return: The name of this InstanceDetailDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceDetailDTO.

        集群名称。

        :param name: The name of this InstanceDetailDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this InstanceDetailDTO.

        集群描述信息。

        :return: The description of this InstanceDetailDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstanceDetailDTO.

        集群描述信息。

        :param description: The description of this InstanceDetailDTO.
        :type description: str
        """
        self._description = description

    @property
    def external_address(self):
        """Gets the external_address of this InstanceDetailDTO.

        公网IP地址。

        :return: The external_address of this InstanceDetailDTO.
        :rtype: str
        """
        return self._external_address

    @external_address.setter
    def external_address(self, external_address):
        """Sets the external_address of this InstanceDetailDTO.

        公网IP地址。

        :param external_address: The external_address of this InstanceDetailDTO.
        :type external_address: str
        """
        self._external_address = external_address

    @property
    def intranet_address(self):
        """Gets the intranet_address of this InstanceDetailDTO.

        内网IPv4地址。

        :return: The intranet_address of this InstanceDetailDTO.
        :rtype: str
        """
        return self._intranet_address

    @intranet_address.setter
    def intranet_address(self, intranet_address):
        """Sets the intranet_address of this InstanceDetailDTO.

        内网IPv4地址。

        :param intranet_address: The intranet_address of this InstanceDetailDTO.
        :type intranet_address: str
        """
        self._intranet_address = intranet_address

    @property
    def intranet_address_ipv6(self):
        """Gets the intranet_address_ipv6 of this InstanceDetailDTO.

        内网IPv6地址。

        :return: The intranet_address_ipv6 of this InstanceDetailDTO.
        :rtype: str
        """
        return self._intranet_address_ipv6

    @intranet_address_ipv6.setter
    def intranet_address_ipv6(self, intranet_address_ipv6):
        """Sets the intranet_address_ipv6 of this InstanceDetailDTO.

        内网IPv6地址。

        :param intranet_address_ipv6: The intranet_address_ipv6 of this InstanceDetailDTO.
        :type intranet_address_ipv6: str
        """
        self._intranet_address_ipv6 = intranet_address_ipv6

    @property
    def public_zone_id(self):
        """Gets the public_zone_id of this InstanceDetailDTO.

        公网域名ID。

        :return: The public_zone_id of this InstanceDetailDTO.
        :rtype: str
        """
        return self._public_zone_id

    @public_zone_id.setter
    def public_zone_id(self, public_zone_id):
        """Sets the public_zone_id of this InstanceDetailDTO.

        公网域名ID。

        :param public_zone_id: The public_zone_id of this InstanceDetailDTO.
        :type public_zone_id: str
        """
        self._public_zone_id = public_zone_id

    @property
    def public_zone_name(self):
        """Gets the public_zone_name of this InstanceDetailDTO.

        公网域名名称。

        :return: The public_zone_name of this InstanceDetailDTO.
        :rtype: str
        """
        return self._public_zone_name

    @public_zone_name.setter
    def public_zone_name(self, public_zone_name):
        """Sets the public_zone_name of this InstanceDetailDTO.

        公网域名名称。

        :param public_zone_name: The public_zone_name of this InstanceDetailDTO.
        :type public_zone_name: str
        """
        self._public_zone_name = public_zone_name

    @property
    def private_zone_id(self):
        """Gets the private_zone_id of this InstanceDetailDTO.

        内网域名ID。

        :return: The private_zone_id of this InstanceDetailDTO.
        :rtype: str
        """
        return self._private_zone_id

    @private_zone_id.setter
    def private_zone_id(self, private_zone_id):
        """Sets the private_zone_id of this InstanceDetailDTO.

        内网域名ID。

        :param private_zone_id: The private_zone_id of this InstanceDetailDTO.
        :type private_zone_id: str
        """
        self._private_zone_id = private_zone_id

    @property
    def private_zone_name(self):
        """Gets the private_zone_name of this InstanceDetailDTO.

        内网域名名称。

        :return: The private_zone_name of this InstanceDetailDTO.
        :rtype: str
        """
        return self._private_zone_name

    @private_zone_name.setter
    def private_zone_name(self, private_zone_name):
        """Sets the private_zone_name of this InstanceDetailDTO.

        内网域名名称。

        :param private_zone_name: The private_zone_name of this InstanceDetailDTO.
        :type private_zone_name: str
        """
        self._private_zone_name = private_zone_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this InstanceDetailDTO.

        企业项目ID。

        :return: The enterprise_project_id of this InstanceDetailDTO.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this InstanceDetailDTO.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this InstanceDetailDTO.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def create_time(self):
        """Gets the create_time of this InstanceDetailDTO.

        创建时间。

        :return: The create_time of this InstanceDetailDTO.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this InstanceDetailDTO.

        创建时间。

        :param create_time: The create_time of this InstanceDetailDTO.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this InstanceDetailDTO.

        创建人。

        :return: The create_user of this InstanceDetailDTO.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this InstanceDetailDTO.

        创建人。

        :param create_user: The create_user of this InstanceDetailDTO.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def current_namespace_publish_api_num(self):
        """Gets the current_namespace_publish_api_num of this InstanceDetailDTO.

        当前工作空间已发布的API数量。

        :return: The current_namespace_publish_api_num of this InstanceDetailDTO.
        :rtype: int
        """
        return self._current_namespace_publish_api_num

    @current_namespace_publish_api_num.setter
    def current_namespace_publish_api_num(self, current_namespace_publish_api_num):
        """Sets the current_namespace_publish_api_num of this InstanceDetailDTO.

        当前工作空间已发布的API数量。

        :param current_namespace_publish_api_num: The current_namespace_publish_api_num of this InstanceDetailDTO.
        :type current_namespace_publish_api_num: int
        """
        self._current_namespace_publish_api_num = current_namespace_publish_api_num

    @property
    def all_namespace_publish_api_num(self):
        """Gets the all_namespace_publish_api_num of this InstanceDetailDTO.

        所有工作空间已发布的API数量。

        :return: The all_namespace_publish_api_num of this InstanceDetailDTO.
        :rtype: int
        """
        return self._all_namespace_publish_api_num

    @all_namespace_publish_api_num.setter
    def all_namespace_publish_api_num(self, all_namespace_publish_api_num):
        """Sets the all_namespace_publish_api_num of this InstanceDetailDTO.

        所有工作空间已发布的API数量。

        :param all_namespace_publish_api_num: The all_namespace_publish_api_num of this InstanceDetailDTO.
        :type all_namespace_publish_api_num: int
        """
        self._all_namespace_publish_api_num = all_namespace_publish_api_num

    @property
    def api_publishable_num(self):
        """Gets the api_publishable_num of this InstanceDetailDTO.

        集群API总配额。

        :return: The api_publishable_num of this InstanceDetailDTO.
        :rtype: int
        """
        return self._api_publishable_num

    @api_publishable_num.setter
    def api_publishable_num(self, api_publishable_num):
        """Sets the api_publishable_num of this InstanceDetailDTO.

        集群API总配额。

        :param api_publishable_num: The api_publishable_num of this InstanceDetailDTO.
        :type api_publishable_num: int
        """
        self._api_publishable_num = api_publishable_num

    @property
    def deletable(self):
        """Gets the deletable of this InstanceDetailDTO.

        集群是否可以删除。

        :return: The deletable of this InstanceDetailDTO.
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        """Sets the deletable of this InstanceDetailDTO.

        集群是否可以删除。

        :param deletable: The deletable of this InstanceDetailDTO.
        :type deletable: bool
        """
        self._deletable = deletable

    @property
    def charge_status(self):
        """Gets the charge_status of this InstanceDetailDTO.

        集群计费状态，NO_CHARGE：未计费、CHARGED：已计费，GRACE：宽限期、RETENTION：保留期。

        :return: The charge_status of this InstanceDetailDTO.
        :rtype: str
        """
        return self._charge_status

    @charge_status.setter
    def charge_status(self, charge_status):
        """Sets the charge_status of this InstanceDetailDTO.

        集群计费状态，NO_CHARGE：未计费、CHARGED：已计费，GRACE：宽限期、RETENTION：保留期。

        :param charge_status: The charge_status of this InstanceDetailDTO.
        :type charge_status: str
        """
        self._charge_status = charge_status

    @property
    def order_id(self):
        """Gets the order_id of this InstanceDetailDTO.

        订单ID。

        :return: The order_id of this InstanceDetailDTO.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InstanceDetailDTO.

        订单ID。

        :param order_id: The order_id of this InstanceDetailDTO.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def order_type(self):
        """Gets the order_type of this InstanceDetailDTO.

        订单类型，PERIOD：包周期、ON_DEMAND：按需。

        :return: The order_type of this InstanceDetailDTO.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this InstanceDetailDTO.

        订单类型，PERIOD：包周期、ON_DEMAND：按需。

        :param order_type: The order_type of this InstanceDetailDTO.
        :type order_type: str
        """
        self._order_type = order_type

    @property
    def period_type(self):
        """Gets the period_type of this InstanceDetailDTO.

        集群订购周期类型。

        :return: The period_type of this InstanceDetailDTO.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this InstanceDetailDTO.

        集群订购周期类型。

        :param period_type: The period_type of this InstanceDetailDTO.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def instance_status(self):
        """Gets the instance_status of this InstanceDetailDTO.

        集群状态。

        :return: The instance_status of this InstanceDetailDTO.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        """Sets the instance_status of this InstanceDetailDTO.

        集群状态。

        :param instance_status: The instance_status of this InstanceDetailDTO.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def node_num(self):
        """Gets the node_num of this InstanceDetailDTO.

        节点数量。

        :return: The node_num of this InstanceDetailDTO.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this InstanceDetailDTO.

        节点数量。

        :param node_num: The node_num of this InstanceDetailDTO.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def flavor(self):
        """Gets the flavor of this InstanceDetailDTO.

        :return: The flavor of this InstanceDetailDTO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.FlavorDTO`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this InstanceDetailDTO.

        :param flavor: The flavor of this InstanceDetailDTO.
        :type flavor: :class:`huaweicloudsdkdataartsstudio.v1.FlavorDTO`
        """
        self._flavor = flavor

    @property
    def gateway_version(self):
        """Gets the gateway_version of this InstanceDetailDTO.

        集群版本号。

        :return: The gateway_version of this InstanceDetailDTO.
        :rtype: str
        """
        return self._gateway_version

    @gateway_version.setter
    def gateway_version(self, gateway_version):
        """Sets the gateway_version of this InstanceDetailDTO.

        集群版本号。

        :param gateway_version: The gateway_version of this InstanceDetailDTO.
        :type gateway_version: str
        """
        self._gateway_version = gateway_version

    @property
    def availability_zone(self):
        """Gets the availability_zone of this InstanceDetailDTO.

        集群所在可用区编码。

        :return: The availability_zone of this InstanceDetailDTO.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this InstanceDetailDTO.

        集群所在可用区编码。

        :param availability_zone: The availability_zone of this InstanceDetailDTO.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def availability_zone_name(self):
        """Gets the availability_zone_name of this InstanceDetailDTO.

        集群所在可用区名称。

        :return: The availability_zone_name of this InstanceDetailDTO.
        :rtype: str
        """
        return self._availability_zone_name

    @availability_zone_name.setter
    def availability_zone_name(self, availability_zone_name):
        """Sets the availability_zone_name of this InstanceDetailDTO.

        集群所在可用区名称。

        :param availability_zone_name: The availability_zone_name of this InstanceDetailDTO.
        :type availability_zone_name: str
        """
        self._availability_zone_name = availability_zone_name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this InstanceDetailDTO.

        集群所在虚拟私有云ID。

        :return: The vpc_id of this InstanceDetailDTO.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this InstanceDetailDTO.

        集群所在虚拟私有云ID。

        :param vpc_id: The vpc_id of this InstanceDetailDTO.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this InstanceDetailDTO.

        集群所在子网ID。

        :return: The subnet_id of this InstanceDetailDTO.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this InstanceDetailDTO.

        集群所在子网ID。

        :param subnet_id: The subnet_id of this InstanceDetailDTO.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this InstanceDetailDTO.

        集群所在安全组ID。

        :return: The security_group_id of this InstanceDetailDTO.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this InstanceDetailDTO.

        集群所在安全组ID。

        :param security_group_id: The security_group_id of this InstanceDetailDTO.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def nodes(self):
        """Gets the nodes of this InstanceDetailDTO.

        集群节点列表。

        :return: The nodes of this InstanceDetailDTO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.InstanceNodeDTO`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this InstanceDetailDTO.

        集群节点列表。

        :param nodes: The nodes of this InstanceDetailDTO.
        :type nodes: list[:class:`huaweicloudsdkdataartsstudio.v1.InstanceNodeDTO`]
        """
        self._nodes = nodes

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
        if not isinstance(other, InstanceDetailDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
