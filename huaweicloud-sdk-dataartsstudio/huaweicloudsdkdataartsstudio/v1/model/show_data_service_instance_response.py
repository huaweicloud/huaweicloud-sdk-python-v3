# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataServiceInstanceResponse(SdkResponse):

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
        r"""ShowDataServiceInstanceResponse

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
        
        super(ShowDataServiceInstanceResponse, self).__init__()

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
        r"""Gets the id of this ShowDataServiceInstanceResponse.

        集群ID。

        :return: The id of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowDataServiceInstanceResponse.

        集群ID。

        :param id: The id of this ShowDataServiceInstanceResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowDataServiceInstanceResponse.

        集群名称。

        :return: The name of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowDataServiceInstanceResponse.

        集群名称。

        :param name: The name of this ShowDataServiceInstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowDataServiceInstanceResponse.

        集群描述信息。

        :return: The description of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowDataServiceInstanceResponse.

        集群描述信息。

        :param description: The description of this ShowDataServiceInstanceResponse.
        :type description: str
        """
        self._description = description

    @property
    def external_address(self):
        r"""Gets the external_address of this ShowDataServiceInstanceResponse.

        公网IP地址。

        :return: The external_address of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._external_address

    @external_address.setter
    def external_address(self, external_address):
        r"""Sets the external_address of this ShowDataServiceInstanceResponse.

        公网IP地址。

        :param external_address: The external_address of this ShowDataServiceInstanceResponse.
        :type external_address: str
        """
        self._external_address = external_address

    @property
    def intranet_address(self):
        r"""Gets the intranet_address of this ShowDataServiceInstanceResponse.

        内网IPv4地址。

        :return: The intranet_address of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._intranet_address

    @intranet_address.setter
    def intranet_address(self, intranet_address):
        r"""Sets the intranet_address of this ShowDataServiceInstanceResponse.

        内网IPv4地址。

        :param intranet_address: The intranet_address of this ShowDataServiceInstanceResponse.
        :type intranet_address: str
        """
        self._intranet_address = intranet_address

    @property
    def intranet_address_ipv6(self):
        r"""Gets the intranet_address_ipv6 of this ShowDataServiceInstanceResponse.

        内网IPv6地址。

        :return: The intranet_address_ipv6 of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._intranet_address_ipv6

    @intranet_address_ipv6.setter
    def intranet_address_ipv6(self, intranet_address_ipv6):
        r"""Sets the intranet_address_ipv6 of this ShowDataServiceInstanceResponse.

        内网IPv6地址。

        :param intranet_address_ipv6: The intranet_address_ipv6 of this ShowDataServiceInstanceResponse.
        :type intranet_address_ipv6: str
        """
        self._intranet_address_ipv6 = intranet_address_ipv6

    @property
    def public_zone_id(self):
        r"""Gets the public_zone_id of this ShowDataServiceInstanceResponse.

        公网域名ID。

        :return: The public_zone_id of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._public_zone_id

    @public_zone_id.setter
    def public_zone_id(self, public_zone_id):
        r"""Sets the public_zone_id of this ShowDataServiceInstanceResponse.

        公网域名ID。

        :param public_zone_id: The public_zone_id of this ShowDataServiceInstanceResponse.
        :type public_zone_id: str
        """
        self._public_zone_id = public_zone_id

    @property
    def public_zone_name(self):
        r"""Gets the public_zone_name of this ShowDataServiceInstanceResponse.

        公网域名名称。

        :return: The public_zone_name of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._public_zone_name

    @public_zone_name.setter
    def public_zone_name(self, public_zone_name):
        r"""Sets the public_zone_name of this ShowDataServiceInstanceResponse.

        公网域名名称。

        :param public_zone_name: The public_zone_name of this ShowDataServiceInstanceResponse.
        :type public_zone_name: str
        """
        self._public_zone_name = public_zone_name

    @property
    def private_zone_id(self):
        r"""Gets the private_zone_id of this ShowDataServiceInstanceResponse.

        内网域名ID。

        :return: The private_zone_id of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._private_zone_id

    @private_zone_id.setter
    def private_zone_id(self, private_zone_id):
        r"""Sets the private_zone_id of this ShowDataServiceInstanceResponse.

        内网域名ID。

        :param private_zone_id: The private_zone_id of this ShowDataServiceInstanceResponse.
        :type private_zone_id: str
        """
        self._private_zone_id = private_zone_id

    @property
    def private_zone_name(self):
        r"""Gets the private_zone_name of this ShowDataServiceInstanceResponse.

        内网域名名称。

        :return: The private_zone_name of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._private_zone_name

    @private_zone_name.setter
    def private_zone_name(self, private_zone_name):
        r"""Sets the private_zone_name of this ShowDataServiceInstanceResponse.

        内网域名名称。

        :param private_zone_name: The private_zone_name of this ShowDataServiceInstanceResponse.
        :type private_zone_name: str
        """
        self._private_zone_name = private_zone_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowDataServiceInstanceResponse.

        企业项目ID。

        :return: The enterprise_project_id of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowDataServiceInstanceResponse.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ShowDataServiceInstanceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowDataServiceInstanceResponse.

        创建时间。

        :return: The create_time of this ShowDataServiceInstanceResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowDataServiceInstanceResponse.

        创建时间。

        :param create_time: The create_time of this ShowDataServiceInstanceResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_user(self):
        r"""Gets the create_user of this ShowDataServiceInstanceResponse.

        创建人。

        :return: The create_user of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ShowDataServiceInstanceResponse.

        创建人。

        :param create_user: The create_user of this ShowDataServiceInstanceResponse.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def current_namespace_publish_api_num(self):
        r"""Gets the current_namespace_publish_api_num of this ShowDataServiceInstanceResponse.

        当前工作空间已发布的API数量。

        :return: The current_namespace_publish_api_num of this ShowDataServiceInstanceResponse.
        :rtype: int
        """
        return self._current_namespace_publish_api_num

    @current_namespace_publish_api_num.setter
    def current_namespace_publish_api_num(self, current_namespace_publish_api_num):
        r"""Sets the current_namespace_publish_api_num of this ShowDataServiceInstanceResponse.

        当前工作空间已发布的API数量。

        :param current_namespace_publish_api_num: The current_namespace_publish_api_num of this ShowDataServiceInstanceResponse.
        :type current_namespace_publish_api_num: int
        """
        self._current_namespace_publish_api_num = current_namespace_publish_api_num

    @property
    def all_namespace_publish_api_num(self):
        r"""Gets the all_namespace_publish_api_num of this ShowDataServiceInstanceResponse.

        所有工作空间已发布的API数量。

        :return: The all_namespace_publish_api_num of this ShowDataServiceInstanceResponse.
        :rtype: int
        """
        return self._all_namespace_publish_api_num

    @all_namespace_publish_api_num.setter
    def all_namespace_publish_api_num(self, all_namespace_publish_api_num):
        r"""Sets the all_namespace_publish_api_num of this ShowDataServiceInstanceResponse.

        所有工作空间已发布的API数量。

        :param all_namespace_publish_api_num: The all_namespace_publish_api_num of this ShowDataServiceInstanceResponse.
        :type all_namespace_publish_api_num: int
        """
        self._all_namespace_publish_api_num = all_namespace_publish_api_num

    @property
    def api_publishable_num(self):
        r"""Gets the api_publishable_num of this ShowDataServiceInstanceResponse.

        集群API总配额。

        :return: The api_publishable_num of this ShowDataServiceInstanceResponse.
        :rtype: int
        """
        return self._api_publishable_num

    @api_publishable_num.setter
    def api_publishable_num(self, api_publishable_num):
        r"""Sets the api_publishable_num of this ShowDataServiceInstanceResponse.

        集群API总配额。

        :param api_publishable_num: The api_publishable_num of this ShowDataServiceInstanceResponse.
        :type api_publishable_num: int
        """
        self._api_publishable_num = api_publishable_num

    @property
    def deletable(self):
        r"""Gets the deletable of this ShowDataServiceInstanceResponse.

        集群是否可以删除。

        :return: The deletable of this ShowDataServiceInstanceResponse.
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        r"""Sets the deletable of this ShowDataServiceInstanceResponse.

        集群是否可以删除。

        :param deletable: The deletable of this ShowDataServiceInstanceResponse.
        :type deletable: bool
        """
        self._deletable = deletable

    @property
    def charge_status(self):
        r"""Gets the charge_status of this ShowDataServiceInstanceResponse.

        集群计费状态，NO_CHARGE：未计费、CHARGED：已计费，GRACE：宽限期、RETENTION：保留期。

        :return: The charge_status of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._charge_status

    @charge_status.setter
    def charge_status(self, charge_status):
        r"""Sets the charge_status of this ShowDataServiceInstanceResponse.

        集群计费状态，NO_CHARGE：未计费、CHARGED：已计费，GRACE：宽限期、RETENTION：保留期。

        :param charge_status: The charge_status of this ShowDataServiceInstanceResponse.
        :type charge_status: str
        """
        self._charge_status = charge_status

    @property
    def order_id(self):
        r"""Gets the order_id of this ShowDataServiceInstanceResponse.

        订单ID。

        :return: The order_id of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ShowDataServiceInstanceResponse.

        订单ID。

        :param order_id: The order_id of this ShowDataServiceInstanceResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def order_type(self):
        r"""Gets the order_type of this ShowDataServiceInstanceResponse.

        订单类型，PERIOD：包周期、ON_DEMAND：按需。

        :return: The order_type of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        r"""Sets the order_type of this ShowDataServiceInstanceResponse.

        订单类型，PERIOD：包周期、ON_DEMAND：按需。

        :param order_type: The order_type of this ShowDataServiceInstanceResponse.
        :type order_type: str
        """
        self._order_type = order_type

    @property
    def period_type(self):
        r"""Gets the period_type of this ShowDataServiceInstanceResponse.

        集群订购周期类型。

        :return: The period_type of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this ShowDataServiceInstanceResponse.

        集群订购周期类型。

        :param period_type: The period_type of this ShowDataServiceInstanceResponse.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def instance_status(self):
        r"""Gets the instance_status of this ShowDataServiceInstanceResponse.

        集群状态。

        :return: The instance_status of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this ShowDataServiceInstanceResponse.

        集群状态。

        :param instance_status: The instance_status of this ShowDataServiceInstanceResponse.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def node_num(self):
        r"""Gets the node_num of this ShowDataServiceInstanceResponse.

        节点数量。

        :return: The node_num of this ShowDataServiceInstanceResponse.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this ShowDataServiceInstanceResponse.

        节点数量。

        :param node_num: The node_num of this ShowDataServiceInstanceResponse.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def flavor(self):
        r"""Gets the flavor of this ShowDataServiceInstanceResponse.

        :return: The flavor of this ShowDataServiceInstanceResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.FlavorDTO`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ShowDataServiceInstanceResponse.

        :param flavor: The flavor of this ShowDataServiceInstanceResponse.
        :type flavor: :class:`huaweicloudsdkdataartsstudio.v1.FlavorDTO`
        """
        self._flavor = flavor

    @property
    def gateway_version(self):
        r"""Gets the gateway_version of this ShowDataServiceInstanceResponse.

        集群版本号。

        :return: The gateway_version of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._gateway_version

    @gateway_version.setter
    def gateway_version(self, gateway_version):
        r"""Sets the gateway_version of this ShowDataServiceInstanceResponse.

        集群版本号。

        :param gateway_version: The gateway_version of this ShowDataServiceInstanceResponse.
        :type gateway_version: str
        """
        self._gateway_version = gateway_version

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ShowDataServiceInstanceResponse.

        集群所在可用区编码。

        :return: The availability_zone of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ShowDataServiceInstanceResponse.

        集群所在可用区编码。

        :param availability_zone: The availability_zone of this ShowDataServiceInstanceResponse.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def availability_zone_name(self):
        r"""Gets the availability_zone_name of this ShowDataServiceInstanceResponse.

        集群所在可用区名称。

        :return: The availability_zone_name of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._availability_zone_name

    @availability_zone_name.setter
    def availability_zone_name(self, availability_zone_name):
        r"""Sets the availability_zone_name of this ShowDataServiceInstanceResponse.

        集群所在可用区名称。

        :param availability_zone_name: The availability_zone_name of this ShowDataServiceInstanceResponse.
        :type availability_zone_name: str
        """
        self._availability_zone_name = availability_zone_name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ShowDataServiceInstanceResponse.

        集群所在虚拟私有云ID。

        :return: The vpc_id of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ShowDataServiceInstanceResponse.

        集群所在虚拟私有云ID。

        :param vpc_id: The vpc_id of this ShowDataServiceInstanceResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ShowDataServiceInstanceResponse.

        集群所在子网ID。

        :return: The subnet_id of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ShowDataServiceInstanceResponse.

        集群所在子网ID。

        :param subnet_id: The subnet_id of this ShowDataServiceInstanceResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this ShowDataServiceInstanceResponse.

        集群所在安全组ID。

        :return: The security_group_id of this ShowDataServiceInstanceResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this ShowDataServiceInstanceResponse.

        集群所在安全组ID。

        :param security_group_id: The security_group_id of this ShowDataServiceInstanceResponse.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def nodes(self):
        r"""Gets the nodes of this ShowDataServiceInstanceResponse.

        集群节点列表。

        :return: The nodes of this ShowDataServiceInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.InstanceNodeDTO`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this ShowDataServiceInstanceResponse.

        集群节点列表。

        :param nodes: The nodes of this ShowDataServiceInstanceResponse.
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
        if not isinstance(other, ShowDataServiceInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
