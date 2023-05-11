# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DirectConnect:

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
        'tenant_id': 'str',
        'name': 'str',
        'description': 'str',
        'port_type': 'str',
        'bandwidth': 'int',
        'location': 'str',
        'peer_location': 'str',
        'device_id': 'str',
        'type': 'str',
        'hosting_id': 'str',
        'charge_mode': 'str',
        'provider': 'str',
        'admin_state_up': 'bool',
        'vlan': 'int',
        'status': 'str',
        'apply_time': 'datetime',
        'create_time': 'datetime',
        'provider_status': 'str',
        'peer_port_type': 'str',
        'peer_provider': 'str',
        'order_id': 'str',
        'product_id': 'str',
        'spec_code': 'str',
        'period_type': 'int',
        'period_num': 'int',
        'vgw_type': 'str',
        'lag_id': 'str',
        'signed_agreement_status': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'name': 'name',
        'description': 'description',
        'port_type': 'port_type',
        'bandwidth': 'bandwidth',
        'location': 'location',
        'peer_location': 'peer_location',
        'device_id': 'device_id',
        'type': 'type',
        'hosting_id': 'hosting_id',
        'charge_mode': 'charge_mode',
        'provider': 'provider',
        'admin_state_up': 'admin_state_up',
        'vlan': 'vlan',
        'status': 'status',
        'apply_time': 'apply_time',
        'create_time': 'create_time',
        'provider_status': 'provider_status',
        'peer_port_type': 'peer_port_type',
        'peer_provider': 'peer_provider',
        'order_id': 'order_id',
        'product_id': 'product_id',
        'spec_code': 'spec_code',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'vgw_type': 'vgw_type',
        'lag_id': 'lag_id',
        'signed_agreement_status': 'signed_agreement_status',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, id=None, tenant_id=None, name=None, description=None, port_type=None, bandwidth=None, location=None, peer_location=None, device_id=None, type=None, hosting_id=None, charge_mode=None, provider=None, admin_state_up=None, vlan=None, status=None, apply_time=None, create_time=None, provider_status=None, peer_port_type=None, peer_provider=None, order_id=None, product_id=None, spec_code=None, period_type=None, period_num=None, vgw_type=None, lag_id=None, signed_agreement_status=None, enterprise_project_id=None, tags=None):
        """DirectConnect

        The model defined in huaweicloud sdk

        :param id: 物理专线标识符ID
        :type id: str
        :param tenant_id: 实例所属项目ID。
        :type tenant_id: str
        :param name: 物理专线名字
        :type name: str
        :param description: 物理专线描述信息
        :type description: str
        :param port_type: 物理专线接入接口的类型，支持1G 10G 40G 100G
        :type port_type: str
        :param bandwidth: 物理专线接入带宽，单位Mbps。
        :type bandwidth: int
        :param location: 专线的接入位置信息
        :type location: str
        :param peer_location: 物理专线对端所在的物理位置，省/市/街道或IDC名字。
        :type peer_location: str
        :param device_id: 物理专线连接的设备的标识ID
        :type device_id: str
        :param type: 物理专线的类型，类似包括标准(standard),运营专线(hosting),托管专线（hosted）
        :type type: str
        :param hosting_id: hosted物理专线对应的hosting物理专线的ID
        :type hosting_id: str
        :param charge_mode: 计费模式：prepayment/bandwidth/traffic
        :type charge_mode: str
        :param provider: 物理专线连接的线路运营商如：中国电信 中国联通 中国移动 中国其他 境外其他专线归属的运营商
        :type provider: str
        :param admin_state_up: 管理状态：true或false
        :type admin_state_up: bool
        :param vlan: 为托管hosted物理专线分配的vlan。
        :type vlan: int
        :param status: 资源状态，合法值是：ACTIVE，DOWN，BUILD，ERROR，PENDING_DELETE，DELETED，APPLY，DENY，PENDING_PAY，PAID，ORDERING，ACCEPT，REJECTED
        :type status: str
        :param apply_time: 物理专线的申请时间
        :type apply_time: datetime
        :param create_time: 物理专线的创建时间
        :type create_time: datetime
        :param provider_status: 物理专线的运营商操作状态，合法值是：ACTIVE， DOWN
        :type provider_status: str
        :param peer_port_type: 连接对端的端口类型
        :type peer_port_type: str
        :param peer_provider: 专线连接对接的运营商
        :type peer_provider: str
        :param order_id: 物理专线对应订单号，用于支持包周期计费，识别用户订单
        :type order_id: str
        :param product_id: 物理专线订单对应产品标识，用于订制包周期套餐等计费策略
        :type product_id: str
        :param spec_code: 物理专线订单对应产品规格，用于订制包周期套餐等计费策略
        :type spec_code: str
        :param period_type: 物理专线对应订单号对应包周期的类型
        :type period_type: int
        :param period_num: 物理专线对应的包周期时间
        :type period_num: int
        :param vgw_type: 专线要求的网关类型
        :type vgw_type: str
        :param lag_id: 物理专线归属的链路聚合组(lag）的ID
        :type lag_id: str
        :param signed_agreement_status: 专线协议的签暑状态
        :type signed_agreement_status: str
        :param enterprise_project_id: 实例所属企业项目ID
        :type enterprise_project_id: str
        :param tags: 标签信息
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        
        

        self._id = None
        self._tenant_id = None
        self._name = None
        self._description = None
        self._port_type = None
        self._bandwidth = None
        self._location = None
        self._peer_location = None
        self._device_id = None
        self._type = None
        self._hosting_id = None
        self._charge_mode = None
        self._provider = None
        self._admin_state_up = None
        self._vlan = None
        self._status = None
        self._apply_time = None
        self._create_time = None
        self._provider_status = None
        self._peer_port_type = None
        self._peer_provider = None
        self._order_id = None
        self._product_id = None
        self._spec_code = None
        self._period_type = None
        self._period_num = None
        self._vgw_type = None
        self._lag_id = None
        self._signed_agreement_status = None
        self._enterprise_project_id = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if port_type is not None:
            self.port_type = port_type
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if location is not None:
            self.location = location
        if peer_location is not None:
            self.peer_location = peer_location
        if device_id is not None:
            self.device_id = device_id
        if type is not None:
            self.type = type
        if hosting_id is not None:
            self.hosting_id = hosting_id
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if provider is not None:
            self.provider = provider
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if vlan is not None:
            self.vlan = vlan
        if status is not None:
            self.status = status
        if apply_time is not None:
            self.apply_time = apply_time
        if create_time is not None:
            self.create_time = create_time
        if provider_status is not None:
            self.provider_status = provider_status
        if peer_port_type is not None:
            self.peer_port_type = peer_port_type
        if peer_provider is not None:
            self.peer_provider = peer_provider
        if order_id is not None:
            self.order_id = order_id
        if product_id is not None:
            self.product_id = product_id
        if spec_code is not None:
            self.spec_code = spec_code
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if vgw_type is not None:
            self.vgw_type = vgw_type
        if lag_id is not None:
            self.lag_id = lag_id
        if signed_agreement_status is not None:
            self.signed_agreement_status = signed_agreement_status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this DirectConnect.

        物理专线标识符ID

        :return: The id of this DirectConnect.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DirectConnect.

        物理专线标识符ID

        :param id: The id of this DirectConnect.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this DirectConnect.

        实例所属项目ID。

        :return: The tenant_id of this DirectConnect.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this DirectConnect.

        实例所属项目ID。

        :param tenant_id: The tenant_id of this DirectConnect.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this DirectConnect.

        物理专线名字

        :return: The name of this DirectConnect.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DirectConnect.

        物理专线名字

        :param name: The name of this DirectConnect.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this DirectConnect.

        物理专线描述信息

        :return: The description of this DirectConnect.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DirectConnect.

        物理专线描述信息

        :param description: The description of this DirectConnect.
        :type description: str
        """
        self._description = description

    @property
    def port_type(self):
        """Gets the port_type of this DirectConnect.

        物理专线接入接口的类型，支持1G 10G 40G 100G

        :return: The port_type of this DirectConnect.
        :rtype: str
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type):
        """Sets the port_type of this DirectConnect.

        物理专线接入接口的类型，支持1G 10G 40G 100G

        :param port_type: The port_type of this DirectConnect.
        :type port_type: str
        """
        self._port_type = port_type

    @property
    def bandwidth(self):
        """Gets the bandwidth of this DirectConnect.

        物理专线接入带宽，单位Mbps。

        :return: The bandwidth of this DirectConnect.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this DirectConnect.

        物理专线接入带宽，单位Mbps。

        :param bandwidth: The bandwidth of this DirectConnect.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def location(self):
        """Gets the location of this DirectConnect.

        专线的接入位置信息

        :return: The location of this DirectConnect.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this DirectConnect.

        专线的接入位置信息

        :param location: The location of this DirectConnect.
        :type location: str
        """
        self._location = location

    @property
    def peer_location(self):
        """Gets the peer_location of this DirectConnect.

        物理专线对端所在的物理位置，省/市/街道或IDC名字。

        :return: The peer_location of this DirectConnect.
        :rtype: str
        """
        return self._peer_location

    @peer_location.setter
    def peer_location(self, peer_location):
        """Sets the peer_location of this DirectConnect.

        物理专线对端所在的物理位置，省/市/街道或IDC名字。

        :param peer_location: The peer_location of this DirectConnect.
        :type peer_location: str
        """
        self._peer_location = peer_location

    @property
    def device_id(self):
        """Gets the device_id of this DirectConnect.

        物理专线连接的设备的标识ID

        :return: The device_id of this DirectConnect.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DirectConnect.

        物理专线连接的设备的标识ID

        :param device_id: The device_id of this DirectConnect.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def type(self):
        """Gets the type of this DirectConnect.

        物理专线的类型，类似包括标准(standard),运营专线(hosting),托管专线（hosted）

        :return: The type of this DirectConnect.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DirectConnect.

        物理专线的类型，类似包括标准(standard),运营专线(hosting),托管专线（hosted）

        :param type: The type of this DirectConnect.
        :type type: str
        """
        self._type = type

    @property
    def hosting_id(self):
        """Gets the hosting_id of this DirectConnect.

        hosted物理专线对应的hosting物理专线的ID

        :return: The hosting_id of this DirectConnect.
        :rtype: str
        """
        return self._hosting_id

    @hosting_id.setter
    def hosting_id(self, hosting_id):
        """Sets the hosting_id of this DirectConnect.

        hosted物理专线对应的hosting物理专线的ID

        :param hosting_id: The hosting_id of this DirectConnect.
        :type hosting_id: str
        """
        self._hosting_id = hosting_id

    @property
    def charge_mode(self):
        """Gets the charge_mode of this DirectConnect.

        计费模式：prepayment/bandwidth/traffic

        :return: The charge_mode of this DirectConnect.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this DirectConnect.

        计费模式：prepayment/bandwidth/traffic

        :param charge_mode: The charge_mode of this DirectConnect.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def provider(self):
        """Gets the provider of this DirectConnect.

        物理专线连接的线路运营商如：中国电信 中国联通 中国移动 中国其他 境外其他专线归属的运营商

        :return: The provider of this DirectConnect.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this DirectConnect.

        物理专线连接的线路运营商如：中国电信 中国联通 中国移动 中国其他 境外其他专线归属的运营商

        :param provider: The provider of this DirectConnect.
        :type provider: str
        """
        self._provider = provider

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this DirectConnect.

        管理状态：true或false

        :return: The admin_state_up of this DirectConnect.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this DirectConnect.

        管理状态：true或false

        :param admin_state_up: The admin_state_up of this DirectConnect.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def vlan(self):
        """Gets the vlan of this DirectConnect.

        为托管hosted物理专线分配的vlan。

        :return: The vlan of this DirectConnect.
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this DirectConnect.

        为托管hosted物理专线分配的vlan。

        :param vlan: The vlan of this DirectConnect.
        :type vlan: int
        """
        self._vlan = vlan

    @property
    def status(self):
        """Gets the status of this DirectConnect.

        资源状态，合法值是：ACTIVE，DOWN，BUILD，ERROR，PENDING_DELETE，DELETED，APPLY，DENY，PENDING_PAY，PAID，ORDERING，ACCEPT，REJECTED

        :return: The status of this DirectConnect.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DirectConnect.

        资源状态，合法值是：ACTIVE，DOWN，BUILD，ERROR，PENDING_DELETE，DELETED，APPLY，DENY，PENDING_PAY，PAID，ORDERING，ACCEPT，REJECTED

        :param status: The status of this DirectConnect.
        :type status: str
        """
        self._status = status

    @property
    def apply_time(self):
        """Gets the apply_time of this DirectConnect.

        物理专线的申请时间

        :return: The apply_time of this DirectConnect.
        :rtype: datetime
        """
        return self._apply_time

    @apply_time.setter
    def apply_time(self, apply_time):
        """Sets the apply_time of this DirectConnect.

        物理专线的申请时间

        :param apply_time: The apply_time of this DirectConnect.
        :type apply_time: datetime
        """
        self._apply_time = apply_time

    @property
    def create_time(self):
        """Gets the create_time of this DirectConnect.

        物理专线的创建时间

        :return: The create_time of this DirectConnect.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DirectConnect.

        物理专线的创建时间

        :param create_time: The create_time of this DirectConnect.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def provider_status(self):
        """Gets the provider_status of this DirectConnect.

        物理专线的运营商操作状态，合法值是：ACTIVE， DOWN

        :return: The provider_status of this DirectConnect.
        :rtype: str
        """
        return self._provider_status

    @provider_status.setter
    def provider_status(self, provider_status):
        """Sets the provider_status of this DirectConnect.

        物理专线的运营商操作状态，合法值是：ACTIVE， DOWN

        :param provider_status: The provider_status of this DirectConnect.
        :type provider_status: str
        """
        self._provider_status = provider_status

    @property
    def peer_port_type(self):
        """Gets the peer_port_type of this DirectConnect.

        连接对端的端口类型

        :return: The peer_port_type of this DirectConnect.
        :rtype: str
        """
        return self._peer_port_type

    @peer_port_type.setter
    def peer_port_type(self, peer_port_type):
        """Sets the peer_port_type of this DirectConnect.

        连接对端的端口类型

        :param peer_port_type: The peer_port_type of this DirectConnect.
        :type peer_port_type: str
        """
        self._peer_port_type = peer_port_type

    @property
    def peer_provider(self):
        """Gets the peer_provider of this DirectConnect.

        专线连接对接的运营商

        :return: The peer_provider of this DirectConnect.
        :rtype: str
        """
        return self._peer_provider

    @peer_provider.setter
    def peer_provider(self, peer_provider):
        """Sets the peer_provider of this DirectConnect.

        专线连接对接的运营商

        :param peer_provider: The peer_provider of this DirectConnect.
        :type peer_provider: str
        """
        self._peer_provider = peer_provider

    @property
    def order_id(self):
        """Gets the order_id of this DirectConnect.

        物理专线对应订单号，用于支持包周期计费，识别用户订单

        :return: The order_id of this DirectConnect.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this DirectConnect.

        物理专线对应订单号，用于支持包周期计费，识别用户订单

        :param order_id: The order_id of this DirectConnect.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def product_id(self):
        """Gets the product_id of this DirectConnect.

        物理专线订单对应产品标识，用于订制包周期套餐等计费策略

        :return: The product_id of this DirectConnect.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this DirectConnect.

        物理专线订单对应产品标识，用于订制包周期套餐等计费策略

        :param product_id: The product_id of this DirectConnect.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def spec_code(self):
        """Gets the spec_code of this DirectConnect.

        物理专线订单对应产品规格，用于订制包周期套餐等计费策略

        :return: The spec_code of this DirectConnect.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this DirectConnect.

        物理专线订单对应产品规格，用于订制包周期套餐等计费策略

        :param spec_code: The spec_code of this DirectConnect.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def period_type(self):
        """Gets the period_type of this DirectConnect.

        物理专线对应订单号对应包周期的类型

        :return: The period_type of this DirectConnect.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this DirectConnect.

        物理专线对应订单号对应包周期的类型

        :param period_type: The period_type of this DirectConnect.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this DirectConnect.

        物理专线对应的包周期时间

        :return: The period_num of this DirectConnect.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this DirectConnect.

        物理专线对应的包周期时间

        :param period_num: The period_num of this DirectConnect.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def vgw_type(self):
        """Gets the vgw_type of this DirectConnect.

        专线要求的网关类型

        :return: The vgw_type of this DirectConnect.
        :rtype: str
        """
        return self._vgw_type

    @vgw_type.setter
    def vgw_type(self, vgw_type):
        """Sets the vgw_type of this DirectConnect.

        专线要求的网关类型

        :param vgw_type: The vgw_type of this DirectConnect.
        :type vgw_type: str
        """
        self._vgw_type = vgw_type

    @property
    def lag_id(self):
        """Gets the lag_id of this DirectConnect.

        物理专线归属的链路聚合组(lag）的ID

        :return: The lag_id of this DirectConnect.
        :rtype: str
        """
        return self._lag_id

    @lag_id.setter
    def lag_id(self, lag_id):
        """Sets the lag_id of this DirectConnect.

        物理专线归属的链路聚合组(lag）的ID

        :param lag_id: The lag_id of this DirectConnect.
        :type lag_id: str
        """
        self._lag_id = lag_id

    @property
    def signed_agreement_status(self):
        """Gets the signed_agreement_status of this DirectConnect.

        专线协议的签暑状态

        :return: The signed_agreement_status of this DirectConnect.
        :rtype: str
        """
        return self._signed_agreement_status

    @signed_agreement_status.setter
    def signed_agreement_status(self, signed_agreement_status):
        """Sets the signed_agreement_status of this DirectConnect.

        专线协议的签暑状态

        :param signed_agreement_status: The signed_agreement_status of this DirectConnect.
        :type signed_agreement_status: str
        """
        self._signed_agreement_status = signed_agreement_status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this DirectConnect.

        实例所属企业项目ID

        :return: The enterprise_project_id of this DirectConnect.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this DirectConnect.

        实例所属企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this DirectConnect.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this DirectConnect.

        标签信息

        :return: The tags of this DirectConnect.
        :rtype: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DirectConnect.

        标签信息

        :param tags: The tags of this DirectConnect.
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
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
        if not isinstance(other, DirectConnect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
