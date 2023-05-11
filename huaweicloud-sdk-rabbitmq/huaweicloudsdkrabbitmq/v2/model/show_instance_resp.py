# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_user': 'str',
        'broker_num': 'int',
        'name': 'str',
        'engine': 'str',
        'engine_version': 'str',
        'specification': 'str',
        'storage_space': 'int',
        'used_storage_space': 'int',
        'connect_address': 'str',
        'port': 'int',
        'status': 'str',
        'description': 'str',
        'instance_id': 'str',
        'resource_spec_code': 'str',
        'charging_mode': 'int',
        'vpc_id': 'str',
        'vpc_name': 'str',
        'created_at': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'order_id': 'str',
        'maintain_begin': 'str',
        'maintain_end': 'str',
        'enable_publicip': 'bool',
        'publicip_address': 'str',
        'publicip_id': 'str',
        'management_connect_address': 'str',
        'ssl_enable': 'bool',
        'enterprise_project_id': 'str',
        'is_logical_volume': 'bool',
        'extend_times': 'int',
        'type': 'str',
        'product_id': 'str',
        'security_group_id': 'str',
        'security_group_name': 'str',
        'subnet_id': 'str',
        'available_zones': 'list[str]',
        'total_storage_space': 'int',
        'storage_resource_id': 'str',
        'storage_spec_code': 'str',
        'ipv6_enable': 'bool',
        'ipv6_connect_addresses': 'list[str]',
        'tags': 'list[TagEntity]'
    }

    attribute_map = {
        'access_user': 'access_user',
        'broker_num': 'broker_num',
        'name': 'name',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'specification': 'specification',
        'storage_space': 'storage_space',
        'used_storage_space': 'used_storage_space',
        'connect_address': 'connect_address',
        'port': 'port',
        'status': 'status',
        'description': 'description',
        'instance_id': 'instance_id',
        'resource_spec_code': 'resource_spec_code',
        'charging_mode': 'charging_mode',
        'vpc_id': 'vpc_id',
        'vpc_name': 'vpc_name',
        'created_at': 'created_at',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'order_id': 'order_id',
        'maintain_begin': 'maintain_begin',
        'maintain_end': 'maintain_end',
        'enable_publicip': 'enable_publicip',
        'publicip_address': 'publicip_address',
        'publicip_id': 'publicip_id',
        'management_connect_address': 'management_connect_address',
        'ssl_enable': 'ssl_enable',
        'enterprise_project_id': 'enterprise_project_id',
        'is_logical_volume': 'is_logical_volume',
        'extend_times': 'extend_times',
        'type': 'type',
        'product_id': 'product_id',
        'security_group_id': 'security_group_id',
        'security_group_name': 'security_group_name',
        'subnet_id': 'subnet_id',
        'available_zones': 'available_zones',
        'total_storage_space': 'total_storage_space',
        'storage_resource_id': 'storage_resource_id',
        'storage_spec_code': 'storage_spec_code',
        'ipv6_enable': 'ipv6_enable',
        'ipv6_connect_addresses': 'ipv6_connect_addresses',
        'tags': 'tags'
    }

    def __init__(self, access_user=None, broker_num=None, name=None, engine=None, engine_version=None, specification=None, storage_space=None, used_storage_space=None, connect_address=None, port=None, status=None, description=None, instance_id=None, resource_spec_code=None, charging_mode=None, vpc_id=None, vpc_name=None, created_at=None, user_id=None, user_name=None, order_id=None, maintain_begin=None, maintain_end=None, enable_publicip=None, publicip_address=None, publicip_id=None, management_connect_address=None, ssl_enable=None, enterprise_project_id=None, is_logical_volume=None, extend_times=None, type=None, product_id=None, security_group_id=None, security_group_name=None, subnet_id=None, available_zones=None, total_storage_space=None, storage_resource_id=None, storage_spec_code=None, ipv6_enable=None, ipv6_connect_addresses=None, tags=None):
        """ShowInstanceResp

        The model defined in huaweicloud sdk

        :param access_user: 认证用户名，只能由英文字母、数字、中划线组成，长度为4~64的字符。
        :type access_user: str
        :param broker_num: 代理个数。
        :type broker_num: int
        :param name: 实例名称。
        :type name: str
        :param engine: 消息引擎。
        :type engine: str
        :param engine_version: 消息引擎版本。
        :type engine_version: str
        :param specification: 实例规格。   - RabbitMQ实例单机返回vm规格。   - RabbitMQ实例集群返回vm规格和节点数。
        :type specification: str
        :param storage_space: 消息存储空间，单位：GB。
        :type storage_space: int
        :param used_storage_space: 已使用的消息存储空间，单位：GB。
        :type used_storage_space: int
        :param connect_address: 实例连接IP地址。
        :type connect_address: str
        :param port: 实例连接端口。
        :type port: int
        :param status: 实例的状态。
        :type status: str
        :param description: 实例描述。
        :type description: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param resource_spec_code: 资源规格标识。   - dms.instance.rabbitmq.single.c3.2u4g：RabbitMQ单机，vm规格2u4g   - dms.instance.rabbitmq.single.c3.4u8g：RabbitMQ单机，vm规格4u8g   - dms.instance.rabbitmq.single.c3.8u16g：RabbitMQ单机，vm规格8u16g   - dms.instance.rabbitmq.single.c3.16u32g：RabbitMQ单机，vm规格16u32g   - dms.instance.rabbitmq.cluster.c3.4u8g.3：RabbitMQ集群，vm规格4u8g，3个节点   - dms.instance.rabbitmq.cluster.c3.4u8g.5：RabbitMQ集群，vm规格4u8g，5个节点   - dms.instance.rabbitmq.cluster.c3.4u8g.7：RabbitMQ集群，vm规格4u8g，7个节点   - dms.instance.rabbitmq.cluster.c3.8u16g.3：RabbitMQ集群，vm规格8u16g，3个节点   - dms.instance.rabbitmq.cluster.c3.8u16g.5：RabbitMQ集群，vm规格8u16g，5个节点   - dms.instance.rabbitmq.cluster.c3.8u16g.7：RabbitMQ集群，vm规格8u16g，7个节点   - dms.instance.rabbitmq.cluster.c3.16u32g.3：RabbitMQ集群，vm规格16u32g，3个节点   - dms.instance.rabbitmq.cluster.c3.16u32g.5：RabbitMQ集群，vm规格16u32g，5个节点   - dms.instance.rabbitmq.cluster.c3.16u32g.7：RabbitMQ集群，vm规格16u32g，7个节点
        :type resource_spec_code: str
        :param charging_mode: 付费模式，1表示按需计费，0表示包年/包月计费。
        :type charging_mode: int
        :param vpc_id: VPC ID。
        :type vpc_id: str
        :param vpc_name: VPC的名称。
        :type vpc_name: str
        :param created_at: 完成创建时间。格式为时间戳，指从格林威治时间 1970年01月01日00时00分00秒起至指定时间的偏差总毫秒数。
        :type created_at: str
        :param user_id: 用户ID。
        :type user_id: str
        :param user_name: 用户名。
        :type user_name: str
        :param order_id: 订单ID，只有在包周期计费时才会有order_id值，其他计费方式order_id值为空。
        :type order_id: str
        :param maintain_begin: 维护时间窗开始时间，格式为HH:mm:ss。
        :type maintain_begin: str
        :param maintain_end: 维护时间窗结束时间，格式为HH:mm:ss。
        :type maintain_end: str
        :param enable_publicip: RabbitMQ实例是否开启公网访问功能。   - true：开启   - false：未开启
        :type enable_publicip: bool
        :param publicip_address: RabbitMQ实例绑定的弹性IP地址。  如果未开启公网访问功能，该字段值为null。
        :type publicip_address: str
        :param publicip_id: RabbitMQ实例绑定的弹性IP地址的ID。  如果未开启公网访问功能，该字段值为null。
        :type publicip_id: str
        :param management_connect_address: RabbitMQ实例的管理地址。
        :type management_connect_address: str
        :param ssl_enable: 是否开启安全认证。   - true：开启   - false：未开启
        :type ssl_enable: bool
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param is_logical_volume: 实例扩容时用于区分老实例与新实例。 - true：新创建的实例，允许磁盘动态扩容不需要重启。 - false：老实例
        :type is_logical_volume: bool
        :param extend_times: 实例扩容磁盘次数，如果超过20次则无法扩容磁盘。
        :type extend_times: int
        :param type: 实例类型：集群，cluster。
        :type type: str
        :param product_id: 产品标识。
        :type product_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param security_group_name: 租户安全组名称。
        :type security_group_name: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param available_zones: 实例节点所在的可用区，返回“可用区ID”。
        :type available_zones: list[str]
        :param total_storage_space: 总共消息存储空间，单位：GB。
        :type total_storage_space: int
        :param storage_resource_id: 存储资源ID。
        :type storage_resource_id: str
        :param storage_spec_code: IO规格。
        :type storage_spec_code: str
        :param ipv6_enable: 是否开启ipv6。
        :type ipv6_enable: bool
        :param ipv6_connect_addresses: IPv6的连接地址。
        :type ipv6_connect_addresses: list[str]
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkrabbitmq.v2.TagEntity`]
        """
        
        

        self._access_user = None
        self._broker_num = None
        self._name = None
        self._engine = None
        self._engine_version = None
        self._specification = None
        self._storage_space = None
        self._used_storage_space = None
        self._connect_address = None
        self._port = None
        self._status = None
        self._description = None
        self._instance_id = None
        self._resource_spec_code = None
        self._charging_mode = None
        self._vpc_id = None
        self._vpc_name = None
        self._created_at = None
        self._user_id = None
        self._user_name = None
        self._order_id = None
        self._maintain_begin = None
        self._maintain_end = None
        self._enable_publicip = None
        self._publicip_address = None
        self._publicip_id = None
        self._management_connect_address = None
        self._ssl_enable = None
        self._enterprise_project_id = None
        self._is_logical_volume = None
        self._extend_times = None
        self._type = None
        self._product_id = None
        self._security_group_id = None
        self._security_group_name = None
        self._subnet_id = None
        self._available_zones = None
        self._total_storage_space = None
        self._storage_resource_id = None
        self._storage_spec_code = None
        self._ipv6_enable = None
        self._ipv6_connect_addresses = None
        self._tags = None
        self.discriminator = None

        if access_user is not None:
            self.access_user = access_user
        if broker_num is not None:
            self.broker_num = broker_num
        if name is not None:
            self.name = name
        if engine is not None:
            self.engine = engine
        if engine_version is not None:
            self.engine_version = engine_version
        if specification is not None:
            self.specification = specification
        if storage_space is not None:
            self.storage_space = storage_space
        if used_storage_space is not None:
            self.used_storage_space = used_storage_space
        if connect_address is not None:
            self.connect_address = connect_address
        if port is not None:
            self.port = port
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if instance_id is not None:
            self.instance_id = instance_id
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_name is not None:
            self.vpc_name = vpc_name
        if created_at is not None:
            self.created_at = created_at
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if order_id is not None:
            self.order_id = order_id
        if maintain_begin is not None:
            self.maintain_begin = maintain_begin
        if maintain_end is not None:
            self.maintain_end = maintain_end
        if enable_publicip is not None:
            self.enable_publicip = enable_publicip
        if publicip_address is not None:
            self.publicip_address = publicip_address
        if publicip_id is not None:
            self.publicip_id = publicip_id
        if management_connect_address is not None:
            self.management_connect_address = management_connect_address
        if ssl_enable is not None:
            self.ssl_enable = ssl_enable
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if is_logical_volume is not None:
            self.is_logical_volume = is_logical_volume
        if extend_times is not None:
            self.extend_times = extend_times
        if type is not None:
            self.type = type
        if product_id is not None:
            self.product_id = product_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if security_group_name is not None:
            self.security_group_name = security_group_name
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if available_zones is not None:
            self.available_zones = available_zones
        if total_storage_space is not None:
            self.total_storage_space = total_storage_space
        if storage_resource_id is not None:
            self.storage_resource_id = storage_resource_id
        if storage_spec_code is not None:
            self.storage_spec_code = storage_spec_code
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if ipv6_connect_addresses is not None:
            self.ipv6_connect_addresses = ipv6_connect_addresses
        if tags is not None:
            self.tags = tags

    @property
    def access_user(self):
        """Gets the access_user of this ShowInstanceResp.

        认证用户名，只能由英文字母、数字、中划线组成，长度为4~64的字符。

        :return: The access_user of this ShowInstanceResp.
        :rtype: str
        """
        return self._access_user

    @access_user.setter
    def access_user(self, access_user):
        """Sets the access_user of this ShowInstanceResp.

        认证用户名，只能由英文字母、数字、中划线组成，长度为4~64的字符。

        :param access_user: The access_user of this ShowInstanceResp.
        :type access_user: str
        """
        self._access_user = access_user

    @property
    def broker_num(self):
        """Gets the broker_num of this ShowInstanceResp.

        代理个数。

        :return: The broker_num of this ShowInstanceResp.
        :rtype: int
        """
        return self._broker_num

    @broker_num.setter
    def broker_num(self, broker_num):
        """Sets the broker_num of this ShowInstanceResp.

        代理个数。

        :param broker_num: The broker_num of this ShowInstanceResp.
        :type broker_num: int
        """
        self._broker_num = broker_num

    @property
    def name(self):
        """Gets the name of this ShowInstanceResp.

        实例名称。

        :return: The name of this ShowInstanceResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowInstanceResp.

        实例名称。

        :param name: The name of this ShowInstanceResp.
        :type name: str
        """
        self._name = name

    @property
    def engine(self):
        """Gets the engine of this ShowInstanceResp.

        消息引擎。

        :return: The engine of this ShowInstanceResp.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ShowInstanceResp.

        消息引擎。

        :param engine: The engine of this ShowInstanceResp.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        """Gets the engine_version of this ShowInstanceResp.

        消息引擎版本。

        :return: The engine_version of this ShowInstanceResp.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this ShowInstanceResp.

        消息引擎版本。

        :param engine_version: The engine_version of this ShowInstanceResp.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def specification(self):
        """Gets the specification of this ShowInstanceResp.

        实例规格。   - RabbitMQ实例单机返回vm规格。   - RabbitMQ实例集群返回vm规格和节点数。

        :return: The specification of this ShowInstanceResp.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        """Sets the specification of this ShowInstanceResp.

        实例规格。   - RabbitMQ实例单机返回vm规格。   - RabbitMQ实例集群返回vm规格和节点数。

        :param specification: The specification of this ShowInstanceResp.
        :type specification: str
        """
        self._specification = specification

    @property
    def storage_space(self):
        """Gets the storage_space of this ShowInstanceResp.

        消息存储空间，单位：GB。

        :return: The storage_space of this ShowInstanceResp.
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        """Sets the storage_space of this ShowInstanceResp.

        消息存储空间，单位：GB。

        :param storage_space: The storage_space of this ShowInstanceResp.
        :type storage_space: int
        """
        self._storage_space = storage_space

    @property
    def used_storage_space(self):
        """Gets the used_storage_space of this ShowInstanceResp.

        已使用的消息存储空间，单位：GB。

        :return: The used_storage_space of this ShowInstanceResp.
        :rtype: int
        """
        return self._used_storage_space

    @used_storage_space.setter
    def used_storage_space(self, used_storage_space):
        """Sets the used_storage_space of this ShowInstanceResp.

        已使用的消息存储空间，单位：GB。

        :param used_storage_space: The used_storage_space of this ShowInstanceResp.
        :type used_storage_space: int
        """
        self._used_storage_space = used_storage_space

    @property
    def connect_address(self):
        """Gets the connect_address of this ShowInstanceResp.

        实例连接IP地址。

        :return: The connect_address of this ShowInstanceResp.
        :rtype: str
        """
        return self._connect_address

    @connect_address.setter
    def connect_address(self, connect_address):
        """Sets the connect_address of this ShowInstanceResp.

        实例连接IP地址。

        :param connect_address: The connect_address of this ShowInstanceResp.
        :type connect_address: str
        """
        self._connect_address = connect_address

    @property
    def port(self):
        """Gets the port of this ShowInstanceResp.

        实例连接端口。

        :return: The port of this ShowInstanceResp.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ShowInstanceResp.

        实例连接端口。

        :param port: The port of this ShowInstanceResp.
        :type port: int
        """
        self._port = port

    @property
    def status(self):
        """Gets the status of this ShowInstanceResp.

        实例的状态。

        :return: The status of this ShowInstanceResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowInstanceResp.

        实例的状态。

        :param status: The status of this ShowInstanceResp.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this ShowInstanceResp.

        实例描述。

        :return: The description of this ShowInstanceResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowInstanceResp.

        实例描述。

        :param description: The description of this ShowInstanceResp.
        :type description: str
        """
        self._description = description

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowInstanceResp.

        实例ID。

        :return: The instance_id of this ShowInstanceResp.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowInstanceResp.

        实例ID。

        :param instance_id: The instance_id of this ShowInstanceResp.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this ShowInstanceResp.

        资源规格标识。   - dms.instance.rabbitmq.single.c3.2u4g：RabbitMQ单机，vm规格2u4g   - dms.instance.rabbitmq.single.c3.4u8g：RabbitMQ单机，vm规格4u8g   - dms.instance.rabbitmq.single.c3.8u16g：RabbitMQ单机，vm规格8u16g   - dms.instance.rabbitmq.single.c3.16u32g：RabbitMQ单机，vm规格16u32g   - dms.instance.rabbitmq.cluster.c3.4u8g.3：RabbitMQ集群，vm规格4u8g，3个节点   - dms.instance.rabbitmq.cluster.c3.4u8g.5：RabbitMQ集群，vm规格4u8g，5个节点   - dms.instance.rabbitmq.cluster.c3.4u8g.7：RabbitMQ集群，vm规格4u8g，7个节点   - dms.instance.rabbitmq.cluster.c3.8u16g.3：RabbitMQ集群，vm规格8u16g，3个节点   - dms.instance.rabbitmq.cluster.c3.8u16g.5：RabbitMQ集群，vm规格8u16g，5个节点   - dms.instance.rabbitmq.cluster.c3.8u16g.7：RabbitMQ集群，vm规格8u16g，7个节点   - dms.instance.rabbitmq.cluster.c3.16u32g.3：RabbitMQ集群，vm规格16u32g，3个节点   - dms.instance.rabbitmq.cluster.c3.16u32g.5：RabbitMQ集群，vm规格16u32g，5个节点   - dms.instance.rabbitmq.cluster.c3.16u32g.7：RabbitMQ集群，vm规格16u32g，7个节点

        :return: The resource_spec_code of this ShowInstanceResp.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this ShowInstanceResp.

        资源规格标识。   - dms.instance.rabbitmq.single.c3.2u4g：RabbitMQ单机，vm规格2u4g   - dms.instance.rabbitmq.single.c3.4u8g：RabbitMQ单机，vm规格4u8g   - dms.instance.rabbitmq.single.c3.8u16g：RabbitMQ单机，vm规格8u16g   - dms.instance.rabbitmq.single.c3.16u32g：RabbitMQ单机，vm规格16u32g   - dms.instance.rabbitmq.cluster.c3.4u8g.3：RabbitMQ集群，vm规格4u8g，3个节点   - dms.instance.rabbitmq.cluster.c3.4u8g.5：RabbitMQ集群，vm规格4u8g，5个节点   - dms.instance.rabbitmq.cluster.c3.4u8g.7：RabbitMQ集群，vm规格4u8g，7个节点   - dms.instance.rabbitmq.cluster.c3.8u16g.3：RabbitMQ集群，vm规格8u16g，3个节点   - dms.instance.rabbitmq.cluster.c3.8u16g.5：RabbitMQ集群，vm规格8u16g，5个节点   - dms.instance.rabbitmq.cluster.c3.8u16g.7：RabbitMQ集群，vm规格8u16g，7个节点   - dms.instance.rabbitmq.cluster.c3.16u32g.3：RabbitMQ集群，vm规格16u32g，3个节点   - dms.instance.rabbitmq.cluster.c3.16u32g.5：RabbitMQ集群，vm规格16u32g，5个节点   - dms.instance.rabbitmq.cluster.c3.16u32g.7：RabbitMQ集群，vm规格16u32g，7个节点

        :param resource_spec_code: The resource_spec_code of this ShowInstanceResp.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def charging_mode(self):
        """Gets the charging_mode of this ShowInstanceResp.

        付费模式，1表示按需计费，0表示包年/包月计费。

        :return: The charging_mode of this ShowInstanceResp.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this ShowInstanceResp.

        付费模式，1表示按需计费，0表示包年/包月计费。

        :param charging_mode: The charging_mode of this ShowInstanceResp.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ShowInstanceResp.

        VPC ID。

        :return: The vpc_id of this ShowInstanceResp.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ShowInstanceResp.

        VPC ID。

        :param vpc_id: The vpc_id of this ShowInstanceResp.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        """Gets the vpc_name of this ShowInstanceResp.

        VPC的名称。

        :return: The vpc_name of this ShowInstanceResp.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this ShowInstanceResp.

        VPC的名称。

        :param vpc_name: The vpc_name of this ShowInstanceResp.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def created_at(self):
        """Gets the created_at of this ShowInstanceResp.

        完成创建时间。格式为时间戳，指从格林威治时间 1970年01月01日00时00分00秒起至指定时间的偏差总毫秒数。

        :return: The created_at of this ShowInstanceResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowInstanceResp.

        完成创建时间。格式为时间戳，指从格林威治时间 1970年01月01日00时00分00秒起至指定时间的偏差总毫秒数。

        :param created_at: The created_at of this ShowInstanceResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def user_id(self):
        """Gets the user_id of this ShowInstanceResp.

        用户ID。

        :return: The user_id of this ShowInstanceResp.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ShowInstanceResp.

        用户ID。

        :param user_id: The user_id of this ShowInstanceResp.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this ShowInstanceResp.

        用户名。

        :return: The user_name of this ShowInstanceResp.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ShowInstanceResp.

        用户名。

        :param user_name: The user_name of this ShowInstanceResp.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def order_id(self):
        """Gets the order_id of this ShowInstanceResp.

        订单ID，只有在包周期计费时才会有order_id值，其他计费方式order_id值为空。

        :return: The order_id of this ShowInstanceResp.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ShowInstanceResp.

        订单ID，只有在包周期计费时才会有order_id值，其他计费方式order_id值为空。

        :param order_id: The order_id of this ShowInstanceResp.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def maintain_begin(self):
        """Gets the maintain_begin of this ShowInstanceResp.

        维护时间窗开始时间，格式为HH:mm:ss。

        :return: The maintain_begin of this ShowInstanceResp.
        :rtype: str
        """
        return self._maintain_begin

    @maintain_begin.setter
    def maintain_begin(self, maintain_begin):
        """Sets the maintain_begin of this ShowInstanceResp.

        维护时间窗开始时间，格式为HH:mm:ss。

        :param maintain_begin: The maintain_begin of this ShowInstanceResp.
        :type maintain_begin: str
        """
        self._maintain_begin = maintain_begin

    @property
    def maintain_end(self):
        """Gets the maintain_end of this ShowInstanceResp.

        维护时间窗结束时间，格式为HH:mm:ss。

        :return: The maintain_end of this ShowInstanceResp.
        :rtype: str
        """
        return self._maintain_end

    @maintain_end.setter
    def maintain_end(self, maintain_end):
        """Sets the maintain_end of this ShowInstanceResp.

        维护时间窗结束时间，格式为HH:mm:ss。

        :param maintain_end: The maintain_end of this ShowInstanceResp.
        :type maintain_end: str
        """
        self._maintain_end = maintain_end

    @property
    def enable_publicip(self):
        """Gets the enable_publicip of this ShowInstanceResp.

        RabbitMQ实例是否开启公网访问功能。   - true：开启   - false：未开启

        :return: The enable_publicip of this ShowInstanceResp.
        :rtype: bool
        """
        return self._enable_publicip

    @enable_publicip.setter
    def enable_publicip(self, enable_publicip):
        """Sets the enable_publicip of this ShowInstanceResp.

        RabbitMQ实例是否开启公网访问功能。   - true：开启   - false：未开启

        :param enable_publicip: The enable_publicip of this ShowInstanceResp.
        :type enable_publicip: bool
        """
        self._enable_publicip = enable_publicip

    @property
    def publicip_address(self):
        """Gets the publicip_address of this ShowInstanceResp.

        RabbitMQ实例绑定的弹性IP地址。  如果未开启公网访问功能，该字段值为null。

        :return: The publicip_address of this ShowInstanceResp.
        :rtype: str
        """
        return self._publicip_address

    @publicip_address.setter
    def publicip_address(self, publicip_address):
        """Sets the publicip_address of this ShowInstanceResp.

        RabbitMQ实例绑定的弹性IP地址。  如果未开启公网访问功能，该字段值为null。

        :param publicip_address: The publicip_address of this ShowInstanceResp.
        :type publicip_address: str
        """
        self._publicip_address = publicip_address

    @property
    def publicip_id(self):
        """Gets the publicip_id of this ShowInstanceResp.

        RabbitMQ实例绑定的弹性IP地址的ID。  如果未开启公网访问功能，该字段值为null。

        :return: The publicip_id of this ShowInstanceResp.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this ShowInstanceResp.

        RabbitMQ实例绑定的弹性IP地址的ID。  如果未开启公网访问功能，该字段值为null。

        :param publicip_id: The publicip_id of this ShowInstanceResp.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def management_connect_address(self):
        """Gets the management_connect_address of this ShowInstanceResp.

        RabbitMQ实例的管理地址。

        :return: The management_connect_address of this ShowInstanceResp.
        :rtype: str
        """
        return self._management_connect_address

    @management_connect_address.setter
    def management_connect_address(self, management_connect_address):
        """Sets the management_connect_address of this ShowInstanceResp.

        RabbitMQ实例的管理地址。

        :param management_connect_address: The management_connect_address of this ShowInstanceResp.
        :type management_connect_address: str
        """
        self._management_connect_address = management_connect_address

    @property
    def ssl_enable(self):
        """Gets the ssl_enable of this ShowInstanceResp.

        是否开启安全认证。   - true：开启   - false：未开启

        :return: The ssl_enable of this ShowInstanceResp.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        """Sets the ssl_enable of this ShowInstanceResp.

        是否开启安全认证。   - true：开启   - false：未开启

        :param ssl_enable: The ssl_enable of this ShowInstanceResp.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowInstanceResp.

        企业项目ID。

        :return: The enterprise_project_id of this ShowInstanceResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowInstanceResp.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ShowInstanceResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def is_logical_volume(self):
        """Gets the is_logical_volume of this ShowInstanceResp.

        实例扩容时用于区分老实例与新实例。 - true：新创建的实例，允许磁盘动态扩容不需要重启。 - false：老实例

        :return: The is_logical_volume of this ShowInstanceResp.
        :rtype: bool
        """
        return self._is_logical_volume

    @is_logical_volume.setter
    def is_logical_volume(self, is_logical_volume):
        """Sets the is_logical_volume of this ShowInstanceResp.

        实例扩容时用于区分老实例与新实例。 - true：新创建的实例，允许磁盘动态扩容不需要重启。 - false：老实例

        :param is_logical_volume: The is_logical_volume of this ShowInstanceResp.
        :type is_logical_volume: bool
        """
        self._is_logical_volume = is_logical_volume

    @property
    def extend_times(self):
        """Gets the extend_times of this ShowInstanceResp.

        实例扩容磁盘次数，如果超过20次则无法扩容磁盘。

        :return: The extend_times of this ShowInstanceResp.
        :rtype: int
        """
        return self._extend_times

    @extend_times.setter
    def extend_times(self, extend_times):
        """Sets the extend_times of this ShowInstanceResp.

        实例扩容磁盘次数，如果超过20次则无法扩容磁盘。

        :param extend_times: The extend_times of this ShowInstanceResp.
        :type extend_times: int
        """
        self._extend_times = extend_times

    @property
    def type(self):
        """Gets the type of this ShowInstanceResp.

        实例类型：集群，cluster。

        :return: The type of this ShowInstanceResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowInstanceResp.

        实例类型：集群，cluster。

        :param type: The type of this ShowInstanceResp.
        :type type: str
        """
        self._type = type

    @property
    def product_id(self):
        """Gets the product_id of this ShowInstanceResp.

        产品标识。

        :return: The product_id of this ShowInstanceResp.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ShowInstanceResp.

        产品标识。

        :param product_id: The product_id of this ShowInstanceResp.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ShowInstanceResp.

        安全组ID。

        :return: The security_group_id of this ShowInstanceResp.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ShowInstanceResp.

        安全组ID。

        :param security_group_id: The security_group_id of this ShowInstanceResp.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def security_group_name(self):
        """Gets the security_group_name of this ShowInstanceResp.

        租户安全组名称。

        :return: The security_group_name of this ShowInstanceResp.
        :rtype: str
        """
        return self._security_group_name

    @security_group_name.setter
    def security_group_name(self, security_group_name):
        """Sets the security_group_name of this ShowInstanceResp.

        租户安全组名称。

        :param security_group_name: The security_group_name of this ShowInstanceResp.
        :type security_group_name: str
        """
        self._security_group_name = security_group_name

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ShowInstanceResp.

        子网ID。

        :return: The subnet_id of this ShowInstanceResp.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ShowInstanceResp.

        子网ID。

        :param subnet_id: The subnet_id of this ShowInstanceResp.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def available_zones(self):
        """Gets the available_zones of this ShowInstanceResp.

        实例节点所在的可用区，返回“可用区ID”。

        :return: The available_zones of this ShowInstanceResp.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this ShowInstanceResp.

        实例节点所在的可用区，返回“可用区ID”。

        :param available_zones: The available_zones of this ShowInstanceResp.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def total_storage_space(self):
        """Gets the total_storage_space of this ShowInstanceResp.

        总共消息存储空间，单位：GB。

        :return: The total_storage_space of this ShowInstanceResp.
        :rtype: int
        """
        return self._total_storage_space

    @total_storage_space.setter
    def total_storage_space(self, total_storage_space):
        """Sets the total_storage_space of this ShowInstanceResp.

        总共消息存储空间，单位：GB。

        :param total_storage_space: The total_storage_space of this ShowInstanceResp.
        :type total_storage_space: int
        """
        self._total_storage_space = total_storage_space

    @property
    def storage_resource_id(self):
        """Gets the storage_resource_id of this ShowInstanceResp.

        存储资源ID。

        :return: The storage_resource_id of this ShowInstanceResp.
        :rtype: str
        """
        return self._storage_resource_id

    @storage_resource_id.setter
    def storage_resource_id(self, storage_resource_id):
        """Sets the storage_resource_id of this ShowInstanceResp.

        存储资源ID。

        :param storage_resource_id: The storage_resource_id of this ShowInstanceResp.
        :type storage_resource_id: str
        """
        self._storage_resource_id = storage_resource_id

    @property
    def storage_spec_code(self):
        """Gets the storage_spec_code of this ShowInstanceResp.

        IO规格。

        :return: The storage_spec_code of this ShowInstanceResp.
        :rtype: str
        """
        return self._storage_spec_code

    @storage_spec_code.setter
    def storage_spec_code(self, storage_spec_code):
        """Sets the storage_spec_code of this ShowInstanceResp.

        IO规格。

        :param storage_spec_code: The storage_spec_code of this ShowInstanceResp.
        :type storage_spec_code: str
        """
        self._storage_spec_code = storage_spec_code

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this ShowInstanceResp.

        是否开启ipv6。

        :return: The ipv6_enable of this ShowInstanceResp.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this ShowInstanceResp.

        是否开启ipv6。

        :param ipv6_enable: The ipv6_enable of this ShowInstanceResp.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def ipv6_connect_addresses(self):
        """Gets the ipv6_connect_addresses of this ShowInstanceResp.

        IPv6的连接地址。

        :return: The ipv6_connect_addresses of this ShowInstanceResp.
        :rtype: list[str]
        """
        return self._ipv6_connect_addresses

    @ipv6_connect_addresses.setter
    def ipv6_connect_addresses(self, ipv6_connect_addresses):
        """Sets the ipv6_connect_addresses of this ShowInstanceResp.

        IPv6的连接地址。

        :param ipv6_connect_addresses: The ipv6_connect_addresses of this ShowInstanceResp.
        :type ipv6_connect_addresses: list[str]
        """
        self._ipv6_connect_addresses = ipv6_connect_addresses

    @property
    def tags(self):
        """Gets the tags of this ShowInstanceResp.

        标签列表。

        :return: The tags of this ShowInstanceResp.
        :rtype: list[:class:`huaweicloudsdkrabbitmq.v2.TagEntity`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowInstanceResp.

        标签列表。

        :param tags: The tags of this ShowInstanceResp.
        :type tags: list[:class:`huaweicloudsdkrabbitmq.v2.TagEntity`]
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
        if not isinstance(other, ShowInstanceResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
