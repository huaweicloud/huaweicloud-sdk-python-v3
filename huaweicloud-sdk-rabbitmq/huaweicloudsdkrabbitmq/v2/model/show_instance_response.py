# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceResponse(SdkResponse):

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
        'dns_enable': 'bool',
        'connect_address': 'str',
        'connect_domain_name': 'str',
        'public_connect_address': 'str',
        'public_connect_domain_name': 'str',
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
        'management_connect_domain_name': 'str',
        'public_management_connect_address': 'str',
        'public_management_connect_domain_name': 'str',
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
        'available_zone_names': 'list[str]',
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
        'dns_enable': 'dns_enable',
        'connect_address': 'connect_address',
        'connect_domain_name': 'connect_domain_name',
        'public_connect_address': 'public_connect_address',
        'public_connect_domain_name': 'public_connect_domain_name',
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
        'management_connect_domain_name': 'management_connect_domain_name',
        'public_management_connect_address': 'public_management_connect_address',
        'public_management_connect_domain_name': 'public_management_connect_domain_name',
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
        'available_zone_names': 'available_zone_names',
        'total_storage_space': 'total_storage_space',
        'storage_resource_id': 'storage_resource_id',
        'storage_spec_code': 'storage_spec_code',
        'ipv6_enable': 'ipv6_enable',
        'ipv6_connect_addresses': 'ipv6_connect_addresses',
        'tags': 'tags'
    }

    def __init__(self, access_user=None, broker_num=None, name=None, engine=None, engine_version=None, specification=None, storage_space=None, used_storage_space=None, dns_enable=None, connect_address=None, connect_domain_name=None, public_connect_address=None, public_connect_domain_name=None, port=None, status=None, description=None, instance_id=None, resource_spec_code=None, charging_mode=None, vpc_id=None, vpc_name=None, created_at=None, user_id=None, user_name=None, order_id=None, maintain_begin=None, maintain_end=None, enable_publicip=None, publicip_address=None, publicip_id=None, management_connect_address=None, management_connect_domain_name=None, public_management_connect_address=None, public_management_connect_domain_name=None, ssl_enable=None, enterprise_project_id=None, is_logical_volume=None, extend_times=None, type=None, product_id=None, security_group_id=None, security_group_name=None, subnet_id=None, available_zones=None, available_zone_names=None, total_storage_space=None, storage_resource_id=None, storage_spec_code=None, ipv6_enable=None, ipv6_connect_addresses=None, tags=None):
        r"""ShowInstanceResponse

        The model defined in huaweicloud sdk

        :param access_user: **参数解释**： 认证用户名。 **取值范围**： 不涉及。
        :type access_user: str
        :param broker_num: **参数解释**： 代理个数。 **取值范围**： - 1 - 3 - 5 - 7
        :type broker_num: int
        :param name: **参数解释**： 实例名称。 **取值范围**： 不涉及。
        :type name: str
        :param engine: **参数解释**： 消息引擎。 **取值范围**： 不涉及。
        :type engine: str
        :param engine_version: **参数解释**： 消息引擎版本。 **取值范围**： 不涉及。
        :type engine_version: str
        :param specification: **参数解释**： 实例规格。 **取值范围**： - 单机实例：返回vm规格。 - 集群实例：返回vm规格和节点数。
        :type specification: str
        :param storage_space: **参数解释**： 消息存储空间，单位：GB。 **取值范围**： 不涉及。
        :type storage_space: int
        :param used_storage_space: **参数解释**： 已使用的消息存储空间，单位：GB。 **取值范围**： 不涉及。
        :type used_storage_space: int
        :param dns_enable: **参数解释**： 实例是否开启域名访问功能。 **取值范围**： - true：开启 - false：未开启
        :type dns_enable: bool
        :param connect_address: **参数解释**： 实例内网连接IP地址。 **取值范围**： 不涉及。
        :type connect_address: str
        :param connect_domain_name: **参数解释**： 实例内网连接域名。 **取值范围**： 不涉及。
        :type connect_domain_name: str
        :param public_connect_address: **参数解释**： 实例公网连接IP地址。 **取值范围**： 不涉及。
        :type public_connect_address: str
        :param public_connect_domain_name: **参数解释**： 实例公网连接域名。 **取值范围**： 不涉及。
        :type public_connect_domain_name: str
        :param port: **参数解释**： 实例连接端口。 **取值范围**： 不涉及。
        :type port: int
        :param status: **参数解释**： 实例状态。 **取值范围**： [详细状态说明请参考[实例状态说明](rabbitmq-api-180514012.xml)](tag:hws,hws_eu,hws_hk,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm)[详细状态说明请参考[实例状态说明](kafka-api-180514012.xml)](tag:hcs)。
        :type status: str
        :param description: **参数解释**： 实例描述。 **取值范围**： 不涉及。
        :type description: str
        :param instance_id: **参数解释**： 实例ID。 **取值范围**： 不涉及。
        :type instance_id: str
        :param resource_spec_code: **参数解释**： 资源规格标识。 **取值范围**： [- dms.instance.rabbitmq.single.c3.2u4g：RabbitMQ单机，vm规格2u4g - dms.instance.rabbitmq.single.c3.4u8g：RabbitMQ单机，vm规格4u8g - dms.instance.rabbitmq.single.c3.8u16g：RabbitMQ单机，vm规格8u16g - dms.instance.rabbitmq.single.c3.16u32g：RabbitMQ单机，vm规格16u32g - dms.instance.rabbitmq.cluster.c3.4u8g.3：RabbitMQ集群，vm规格4u8g，3个节点 - dms.instance.rabbitmq.cluster.c3.4u8g.5：RabbitMQ集群，vm规格4u8g，5个节点 - dms.instance.rabbitmq.cluster.c3.4u8g.7：RabbitMQ集群，vm规格4u8g，7个节点 - dms.instance.rabbitmq.cluster.c3.8u16g.3：RabbitMQ集群，vm规格8u16g，3个节点 - dms.instance.rabbitmq.cluster.c3.8u16g.5：RabbitMQ集群，vm规格8u16g，5个节点 - dms.instance.rabbitmq.cluster.c3.8u16g.7：RabbitMQ集群，vm规格8u16g，7个节点 - dms.instance.rabbitmq.cluster.c3.16u32g.3：RabbitMQ集群，vm规格16u32g，3个节点 - dms.instance.rabbitmq.cluster.c3.16u32g.5：RabbitMQ集群，vm规格16u32g，5个节点 - dms.instance.rabbitmq.cluster.c3.16u32g.7：RabbitMQ集群，vm规格16u32g，7个节点](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm,sbc)
        :type resource_spec_code: str
        :param charging_mode: **参数解释**： 付费模式。 **取值范围**： - 1：按需计费。 - 0：包年/包月计费。
        :type charging_mode: int
        :param vpc_id: **参数解释**： VPC ID。 **取值范围**： 不涉及。
        :type vpc_id: str
        :param vpc_name: **参数解释**： VPC的名称。 **取值范围**： 不涉及。
        :type vpc_name: str
        :param created_at: **参数解释**： 完成创建时间。格式为时间戳，指从格林威治时间 1970年01月01日00时00分00秒起至指定时间的偏差总毫秒数。 **取值范围**： 不涉及。
        :type created_at: str
        :param user_id: **参数解释**： 用户ID。 **取值范围**： 不涉及。
        :type user_id: str
        :param user_name: **参数解释**： 用户名。 **取值范围**： 不涉及。
        :type user_name: str
        :param order_id: **参数解释**： 订单ID，只有在包周期计费时才会有order_id值，其他计费方式order_id值为空。 **取值范围**： 不涉及。
        :type order_id: str
        :param maintain_begin: **参数解释**： 维护时间窗开始时间，格式为HH:mm:ss。 **取值范围**： 不涉及。
        :type maintain_begin: str
        :param maintain_end: **参数解释**： 维护时间窗结束时间，格式为HH:mm:ss。 **取值范围**： 不涉及。
        :type maintain_end: str
        :param enable_publicip: **参数解释**： RabbitMQ实例是否开启公网访问功能。 **取值范围**： - true：开启 - false：未开启
        :type enable_publicip: bool
        :param publicip_address: **参数解释**： RabbitMQ实例绑定的弹性IP地址。  如果未开启公网访问功能，该字段值为null。 **取值范围**： - true：开启 - false：未开启
        :type publicip_address: str
        :param publicip_id: **参数解释**： RabbitMQ实例绑定的弹性IP地址的ID。  如果未开启公网访问功能，该字段值为null。 **取值范围**： 不涉及。
        :type publicip_id: str
        :param management_connect_address: **参数解释**： RabbitMQ实例的管理地址。 **取值范围**： 不涉及。
        :type management_connect_address: str
        :param management_connect_domain_name: **参数解释**： RabbitMQ实例的管理域名。 **取值范围**： 不涉及。
        :type management_connect_domain_name: str
        :param public_management_connect_address: **参数解释**： RabbitMQ实例的公网管理地址。 **取值范围**： 不涉及。
        :type public_management_connect_address: str
        :param public_management_connect_domain_name: **参数解释**： RabbitMQ实例的公网管理域名。 **取值范围**： 不涉及。
        :type public_management_connect_domain_name: str
        :param ssl_enable: **参数解释**： 是否开启安全认证。 **取值范围**： - true：开启 - false：未开启
        :type ssl_enable: bool
        :param enterprise_project_id: **参数解释**： 企业项目ID。 **取值范围**： 不涉及。
        :type enterprise_project_id: str
        :param is_logical_volume: **参数解释**： 实例扩容时用于区分老实例与新实例。 **取值范围**： - true：新创建的实例，允许磁盘动态扩容不需要重启。 - false：特别老的实例不支持磁盘扩容。
        :type is_logical_volume: bool
        :param extend_times: **参数解释**： 实例扩容磁盘次数，如果超过20次则无法扩容磁盘。 **取值范围**： 不涉及。
        :type extend_times: int
        :param type: **参数解释**： 实例类型。 **取值范围**： - single：单机。 - cluster：集群。
        :type type: str
        :param product_id: **参数解释**： 产品标识。 **取值范围**： 不涉及。
        :type product_id: str
        :param security_group_id: **参数解释**： 安全组ID。 **取值范围**： 不涉及。
        :type security_group_id: str
        :param security_group_name: **参数解释**： 租户安全组名称。 **取值范围**： 不涉及。
        :type security_group_name: str
        :param subnet_id: **参数解释**： 子网ID。 **取值范围**： 不涉及。
        :type subnet_id: str
        :param available_zones: **参数解释**： 实例节点所在的可用区ID。
        :type available_zones: list[str]
        :param available_zone_names: **参数解释**： 实例节点所在的可用区名称。
        :type available_zone_names: list[str]
        :param total_storage_space: **参数解释**： 总共消息存储空间，单位：GB。 **取值范围**： 不涉及。
        :type total_storage_space: int
        :param storage_resource_id: **参数解释**： 存储资源ID。 **取值范围**： 不涉及。
        :type storage_resource_id: str
        :param storage_spec_code: **参数解释**： IO规格。 **取值范围**： 不涉及。
        :type storage_spec_code: str
        :param ipv6_enable: **参数解释**： 是否开启IPv6。 **取值范围**： - true：开启。 - false：不开启。
        :type ipv6_enable: bool
        :param ipv6_connect_addresses: **参数解释**： IPv6的连接地址。
        :type ipv6_connect_addresses: list[str]
        :param tags: **参数解释**： 标签列表。
        :type tags: list[:class:`huaweicloudsdkrabbitmq.v2.TagEntity`]
        """
        
        super(ShowInstanceResponse, self).__init__()

        self._access_user = None
        self._broker_num = None
        self._name = None
        self._engine = None
        self._engine_version = None
        self._specification = None
        self._storage_space = None
        self._used_storage_space = None
        self._dns_enable = None
        self._connect_address = None
        self._connect_domain_name = None
        self._public_connect_address = None
        self._public_connect_domain_name = None
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
        self._management_connect_domain_name = None
        self._public_management_connect_address = None
        self._public_management_connect_domain_name = None
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
        self._available_zone_names = None
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
        if dns_enable is not None:
            self.dns_enable = dns_enable
        if connect_address is not None:
            self.connect_address = connect_address
        if connect_domain_name is not None:
            self.connect_domain_name = connect_domain_name
        if public_connect_address is not None:
            self.public_connect_address = public_connect_address
        if public_connect_domain_name is not None:
            self.public_connect_domain_name = public_connect_domain_name
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
        if management_connect_domain_name is not None:
            self.management_connect_domain_name = management_connect_domain_name
        if public_management_connect_address is not None:
            self.public_management_connect_address = public_management_connect_address
        if public_management_connect_domain_name is not None:
            self.public_management_connect_domain_name = public_management_connect_domain_name
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
        if available_zone_names is not None:
            self.available_zone_names = available_zone_names
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
        r"""Gets the access_user of this ShowInstanceResponse.

        **参数解释**： 认证用户名。 **取值范围**： 不涉及。

        :return: The access_user of this ShowInstanceResponse.
        :rtype: str
        """
        return self._access_user

    @access_user.setter
    def access_user(self, access_user):
        r"""Sets the access_user of this ShowInstanceResponse.

        **参数解释**： 认证用户名。 **取值范围**： 不涉及。

        :param access_user: The access_user of this ShowInstanceResponse.
        :type access_user: str
        """
        self._access_user = access_user

    @property
    def broker_num(self):
        r"""Gets the broker_num of this ShowInstanceResponse.

        **参数解释**： 代理个数。 **取值范围**： - 1 - 3 - 5 - 7

        :return: The broker_num of this ShowInstanceResponse.
        :rtype: int
        """
        return self._broker_num

    @broker_num.setter
    def broker_num(self, broker_num):
        r"""Sets the broker_num of this ShowInstanceResponse.

        **参数解释**： 代理个数。 **取值范围**： - 1 - 3 - 5 - 7

        :param broker_num: The broker_num of this ShowInstanceResponse.
        :type broker_num: int
        """
        self._broker_num = broker_num

    @property
    def name(self):
        r"""Gets the name of this ShowInstanceResponse.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :return: The name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowInstanceResponse.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :param name: The name of this ShowInstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def engine(self):
        r"""Gets the engine of this ShowInstanceResponse.

        **参数解释**： 消息引擎。 **取值范围**： 不涉及。

        :return: The engine of this ShowInstanceResponse.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ShowInstanceResponse.

        **参数解释**： 消息引擎。 **取值范围**： 不涉及。

        :param engine: The engine of this ShowInstanceResponse.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        r"""Gets the engine_version of this ShowInstanceResponse.

        **参数解释**： 消息引擎版本。 **取值范围**： 不涉及。

        :return: The engine_version of this ShowInstanceResponse.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this ShowInstanceResponse.

        **参数解释**： 消息引擎版本。 **取值范围**： 不涉及。

        :param engine_version: The engine_version of this ShowInstanceResponse.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def specification(self):
        r"""Gets the specification of this ShowInstanceResponse.

        **参数解释**： 实例规格。 **取值范围**： - 单机实例：返回vm规格。 - 集群实例：返回vm规格和节点数。

        :return: The specification of this ShowInstanceResponse.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this ShowInstanceResponse.

        **参数解释**： 实例规格。 **取值范围**： - 单机实例：返回vm规格。 - 集群实例：返回vm规格和节点数。

        :param specification: The specification of this ShowInstanceResponse.
        :type specification: str
        """
        self._specification = specification

    @property
    def storage_space(self):
        r"""Gets the storage_space of this ShowInstanceResponse.

        **参数解释**： 消息存储空间，单位：GB。 **取值范围**： 不涉及。

        :return: The storage_space of this ShowInstanceResponse.
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        r"""Sets the storage_space of this ShowInstanceResponse.

        **参数解释**： 消息存储空间，单位：GB。 **取值范围**： 不涉及。

        :param storage_space: The storage_space of this ShowInstanceResponse.
        :type storage_space: int
        """
        self._storage_space = storage_space

    @property
    def used_storage_space(self):
        r"""Gets the used_storage_space of this ShowInstanceResponse.

        **参数解释**： 已使用的消息存储空间，单位：GB。 **取值范围**： 不涉及。

        :return: The used_storage_space of this ShowInstanceResponse.
        :rtype: int
        """
        return self._used_storage_space

    @used_storage_space.setter
    def used_storage_space(self, used_storage_space):
        r"""Sets the used_storage_space of this ShowInstanceResponse.

        **参数解释**： 已使用的消息存储空间，单位：GB。 **取值范围**： 不涉及。

        :param used_storage_space: The used_storage_space of this ShowInstanceResponse.
        :type used_storage_space: int
        """
        self._used_storage_space = used_storage_space

    @property
    def dns_enable(self):
        r"""Gets the dns_enable of this ShowInstanceResponse.

        **参数解释**： 实例是否开启域名访问功能。 **取值范围**： - true：开启 - false：未开启

        :return: The dns_enable of this ShowInstanceResponse.
        :rtype: bool
        """
        return self._dns_enable

    @dns_enable.setter
    def dns_enable(self, dns_enable):
        r"""Sets the dns_enable of this ShowInstanceResponse.

        **参数解释**： 实例是否开启域名访问功能。 **取值范围**： - true：开启 - false：未开启

        :param dns_enable: The dns_enable of this ShowInstanceResponse.
        :type dns_enable: bool
        """
        self._dns_enable = dns_enable

    @property
    def connect_address(self):
        r"""Gets the connect_address of this ShowInstanceResponse.

        **参数解释**： 实例内网连接IP地址。 **取值范围**： 不涉及。

        :return: The connect_address of this ShowInstanceResponse.
        :rtype: str
        """
        return self._connect_address

    @connect_address.setter
    def connect_address(self, connect_address):
        r"""Sets the connect_address of this ShowInstanceResponse.

        **参数解释**： 实例内网连接IP地址。 **取值范围**： 不涉及。

        :param connect_address: The connect_address of this ShowInstanceResponse.
        :type connect_address: str
        """
        self._connect_address = connect_address

    @property
    def connect_domain_name(self):
        r"""Gets the connect_domain_name of this ShowInstanceResponse.

        **参数解释**： 实例内网连接域名。 **取值范围**： 不涉及。

        :return: The connect_domain_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._connect_domain_name

    @connect_domain_name.setter
    def connect_domain_name(self, connect_domain_name):
        r"""Sets the connect_domain_name of this ShowInstanceResponse.

        **参数解释**： 实例内网连接域名。 **取值范围**： 不涉及。

        :param connect_domain_name: The connect_domain_name of this ShowInstanceResponse.
        :type connect_domain_name: str
        """
        self._connect_domain_name = connect_domain_name

    @property
    def public_connect_address(self):
        r"""Gets the public_connect_address of this ShowInstanceResponse.

        **参数解释**： 实例公网连接IP地址。 **取值范围**： 不涉及。

        :return: The public_connect_address of this ShowInstanceResponse.
        :rtype: str
        """
        return self._public_connect_address

    @public_connect_address.setter
    def public_connect_address(self, public_connect_address):
        r"""Sets the public_connect_address of this ShowInstanceResponse.

        **参数解释**： 实例公网连接IP地址。 **取值范围**： 不涉及。

        :param public_connect_address: The public_connect_address of this ShowInstanceResponse.
        :type public_connect_address: str
        """
        self._public_connect_address = public_connect_address

    @property
    def public_connect_domain_name(self):
        r"""Gets the public_connect_domain_name of this ShowInstanceResponse.

        **参数解释**： 实例公网连接域名。 **取值范围**： 不涉及。

        :return: The public_connect_domain_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._public_connect_domain_name

    @public_connect_domain_name.setter
    def public_connect_domain_name(self, public_connect_domain_name):
        r"""Sets the public_connect_domain_name of this ShowInstanceResponse.

        **参数解释**： 实例公网连接域名。 **取值范围**： 不涉及。

        :param public_connect_domain_name: The public_connect_domain_name of this ShowInstanceResponse.
        :type public_connect_domain_name: str
        """
        self._public_connect_domain_name = public_connect_domain_name

    @property
    def port(self):
        r"""Gets the port of this ShowInstanceResponse.

        **参数解释**： 实例连接端口。 **取值范围**： 不涉及。

        :return: The port of this ShowInstanceResponse.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ShowInstanceResponse.

        **参数解释**： 实例连接端口。 **取值范围**： 不涉及。

        :param port: The port of this ShowInstanceResponse.
        :type port: int
        """
        self._port = port

    @property
    def status(self):
        r"""Gets the status of this ShowInstanceResponse.

        **参数解释**： 实例状态。 **取值范围**： [详细状态说明请参考[实例状态说明](rabbitmq-api-180514012.xml)](tag:hws,hws_eu,hws_hk,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm)[详细状态说明请参考[实例状态说明](kafka-api-180514012.xml)](tag:hcs)。

        :return: The status of this ShowInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowInstanceResponse.

        **参数解释**： 实例状态。 **取值范围**： [详细状态说明请参考[实例状态说明](rabbitmq-api-180514012.xml)](tag:hws,hws_eu,hws_hk,cmcc,ctc,sbc,hk_sbc,g42,hk_g42,tm,hk_tm)[详细状态说明请参考[实例状态说明](kafka-api-180514012.xml)](tag:hcs)。

        :param status: The status of this ShowInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this ShowInstanceResponse.

        **参数解释**： 实例描述。 **取值范围**： 不涉及。

        :return: The description of this ShowInstanceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowInstanceResponse.

        **参数解释**： 实例描述。 **取值范围**： 不涉及。

        :param description: The description of this ShowInstanceResponse.
        :type description: str
        """
        self._description = description

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowInstanceResponse.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。

        :return: The instance_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowInstanceResponse.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。

        :param instance_id: The instance_id of this ShowInstanceResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ShowInstanceResponse.

        **参数解释**： 资源规格标识。 **取值范围**： [- dms.instance.rabbitmq.single.c3.2u4g：RabbitMQ单机，vm规格2u4g - dms.instance.rabbitmq.single.c3.4u8g：RabbitMQ单机，vm规格4u8g - dms.instance.rabbitmq.single.c3.8u16g：RabbitMQ单机，vm规格8u16g - dms.instance.rabbitmq.single.c3.16u32g：RabbitMQ单机，vm规格16u32g - dms.instance.rabbitmq.cluster.c3.4u8g.3：RabbitMQ集群，vm规格4u8g，3个节点 - dms.instance.rabbitmq.cluster.c3.4u8g.5：RabbitMQ集群，vm规格4u8g，5个节点 - dms.instance.rabbitmq.cluster.c3.4u8g.7：RabbitMQ集群，vm规格4u8g，7个节点 - dms.instance.rabbitmq.cluster.c3.8u16g.3：RabbitMQ集群，vm规格8u16g，3个节点 - dms.instance.rabbitmq.cluster.c3.8u16g.5：RabbitMQ集群，vm规格8u16g，5个节点 - dms.instance.rabbitmq.cluster.c3.8u16g.7：RabbitMQ集群，vm规格8u16g，7个节点 - dms.instance.rabbitmq.cluster.c3.16u32g.3：RabbitMQ集群，vm规格16u32g，3个节点 - dms.instance.rabbitmq.cluster.c3.16u32g.5：RabbitMQ集群，vm规格16u32g，5个节点 - dms.instance.rabbitmq.cluster.c3.16u32g.7：RabbitMQ集群，vm规格16u32g，7个节点](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm,sbc)

        :return: The resource_spec_code of this ShowInstanceResponse.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ShowInstanceResponse.

        **参数解释**： 资源规格标识。 **取值范围**： [- dms.instance.rabbitmq.single.c3.2u4g：RabbitMQ单机，vm规格2u4g - dms.instance.rabbitmq.single.c3.4u8g：RabbitMQ单机，vm规格4u8g - dms.instance.rabbitmq.single.c3.8u16g：RabbitMQ单机，vm规格8u16g - dms.instance.rabbitmq.single.c3.16u32g：RabbitMQ单机，vm规格16u32g - dms.instance.rabbitmq.cluster.c3.4u8g.3：RabbitMQ集群，vm规格4u8g，3个节点 - dms.instance.rabbitmq.cluster.c3.4u8g.5：RabbitMQ集群，vm规格4u8g，5个节点 - dms.instance.rabbitmq.cluster.c3.4u8g.7：RabbitMQ集群，vm规格4u8g，7个节点 - dms.instance.rabbitmq.cluster.c3.8u16g.3：RabbitMQ集群，vm规格8u16g，3个节点 - dms.instance.rabbitmq.cluster.c3.8u16g.5：RabbitMQ集群，vm规格8u16g，5个节点 - dms.instance.rabbitmq.cluster.c3.8u16g.7：RabbitMQ集群，vm规格8u16g，7个节点 - dms.instance.rabbitmq.cluster.c3.16u32g.3：RabbitMQ集群，vm规格16u32g，3个节点 - dms.instance.rabbitmq.cluster.c3.16u32g.5：RabbitMQ集群，vm规格16u32g，5个节点 - dms.instance.rabbitmq.cluster.c3.16u32g.7：RabbitMQ集群，vm规格16u32g，7个节点](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm,sbc)

        :param resource_spec_code: The resource_spec_code of this ShowInstanceResponse.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ShowInstanceResponse.

        **参数解释**： 付费模式。 **取值范围**： - 1：按需计费。 - 0：包年/包月计费。

        :return: The charging_mode of this ShowInstanceResponse.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ShowInstanceResponse.

        **参数解释**： 付费模式。 **取值范围**： - 1：按需计费。 - 0：包年/包月计费。

        :param charging_mode: The charging_mode of this ShowInstanceResponse.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ShowInstanceResponse.

        **参数解释**： VPC ID。 **取值范围**： 不涉及。

        :return: The vpc_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ShowInstanceResponse.

        **参数解释**： VPC ID。 **取值范围**： 不涉及。

        :param vpc_id: The vpc_id of this ShowInstanceResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        r"""Gets the vpc_name of this ShowInstanceResponse.

        **参数解释**： VPC的名称。 **取值范围**： 不涉及。

        :return: The vpc_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        r"""Sets the vpc_name of this ShowInstanceResponse.

        **参数解释**： VPC的名称。 **取值范围**： 不涉及。

        :param vpc_name: The vpc_name of this ShowInstanceResponse.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowInstanceResponse.

        **参数解释**： 完成创建时间。格式为时间戳，指从格林威治时间 1970年01月01日00时00分00秒起至指定时间的偏差总毫秒数。 **取值范围**： 不涉及。

        :return: The created_at of this ShowInstanceResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowInstanceResponse.

        **参数解释**： 完成创建时间。格式为时间戳，指从格林威治时间 1970年01月01日00时00分00秒起至指定时间的偏差总毫秒数。 **取值范围**： 不涉及。

        :param created_at: The created_at of this ShowInstanceResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowInstanceResponse.

        **参数解释**： 用户ID。 **取值范围**： 不涉及。

        :return: The user_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowInstanceResponse.

        **参数解释**： 用户ID。 **取值范围**： 不涉及。

        :param user_id: The user_id of this ShowInstanceResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ShowInstanceResponse.

        **参数解释**： 用户名。 **取值范围**： 不涉及。

        :return: The user_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ShowInstanceResponse.

        **参数解释**： 用户名。 **取值范围**： 不涉及。

        :param user_name: The user_name of this ShowInstanceResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def order_id(self):
        r"""Gets the order_id of this ShowInstanceResponse.

        **参数解释**： 订单ID，只有在包周期计费时才会有order_id值，其他计费方式order_id值为空。 **取值范围**： 不涉及。

        :return: The order_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ShowInstanceResponse.

        **参数解释**： 订单ID，只有在包周期计费时才会有order_id值，其他计费方式order_id值为空。 **取值范围**： 不涉及。

        :param order_id: The order_id of this ShowInstanceResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def maintain_begin(self):
        r"""Gets the maintain_begin of this ShowInstanceResponse.

        **参数解释**： 维护时间窗开始时间，格式为HH:mm:ss。 **取值范围**： 不涉及。

        :return: The maintain_begin of this ShowInstanceResponse.
        :rtype: str
        """
        return self._maintain_begin

    @maintain_begin.setter
    def maintain_begin(self, maintain_begin):
        r"""Sets the maintain_begin of this ShowInstanceResponse.

        **参数解释**： 维护时间窗开始时间，格式为HH:mm:ss。 **取值范围**： 不涉及。

        :param maintain_begin: The maintain_begin of this ShowInstanceResponse.
        :type maintain_begin: str
        """
        self._maintain_begin = maintain_begin

    @property
    def maintain_end(self):
        r"""Gets the maintain_end of this ShowInstanceResponse.

        **参数解释**： 维护时间窗结束时间，格式为HH:mm:ss。 **取值范围**： 不涉及。

        :return: The maintain_end of this ShowInstanceResponse.
        :rtype: str
        """
        return self._maintain_end

    @maintain_end.setter
    def maintain_end(self, maintain_end):
        r"""Sets the maintain_end of this ShowInstanceResponse.

        **参数解释**： 维护时间窗结束时间，格式为HH:mm:ss。 **取值范围**： 不涉及。

        :param maintain_end: The maintain_end of this ShowInstanceResponse.
        :type maintain_end: str
        """
        self._maintain_end = maintain_end

    @property
    def enable_publicip(self):
        r"""Gets the enable_publicip of this ShowInstanceResponse.

        **参数解释**： RabbitMQ实例是否开启公网访问功能。 **取值范围**： - true：开启 - false：未开启

        :return: The enable_publicip of this ShowInstanceResponse.
        :rtype: bool
        """
        return self._enable_publicip

    @enable_publicip.setter
    def enable_publicip(self, enable_publicip):
        r"""Sets the enable_publicip of this ShowInstanceResponse.

        **参数解释**： RabbitMQ实例是否开启公网访问功能。 **取值范围**： - true：开启 - false：未开启

        :param enable_publicip: The enable_publicip of this ShowInstanceResponse.
        :type enable_publicip: bool
        """
        self._enable_publicip = enable_publicip

    @property
    def publicip_address(self):
        r"""Gets the publicip_address of this ShowInstanceResponse.

        **参数解释**： RabbitMQ实例绑定的弹性IP地址。  如果未开启公网访问功能，该字段值为null。 **取值范围**： - true：开启 - false：未开启

        :return: The publicip_address of this ShowInstanceResponse.
        :rtype: str
        """
        return self._publicip_address

    @publicip_address.setter
    def publicip_address(self, publicip_address):
        r"""Sets the publicip_address of this ShowInstanceResponse.

        **参数解释**： RabbitMQ实例绑定的弹性IP地址。  如果未开启公网访问功能，该字段值为null。 **取值范围**： - true：开启 - false：未开启

        :param publicip_address: The publicip_address of this ShowInstanceResponse.
        :type publicip_address: str
        """
        self._publicip_address = publicip_address

    @property
    def publicip_id(self):
        r"""Gets the publicip_id of this ShowInstanceResponse.

        **参数解释**： RabbitMQ实例绑定的弹性IP地址的ID。  如果未开启公网访问功能，该字段值为null。 **取值范围**： 不涉及。

        :return: The publicip_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        r"""Sets the publicip_id of this ShowInstanceResponse.

        **参数解释**： RabbitMQ实例绑定的弹性IP地址的ID。  如果未开启公网访问功能，该字段值为null。 **取值范围**： 不涉及。

        :param publicip_id: The publicip_id of this ShowInstanceResponse.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def management_connect_address(self):
        r"""Gets the management_connect_address of this ShowInstanceResponse.

        **参数解释**： RabbitMQ实例的管理地址。 **取值范围**： 不涉及。

        :return: The management_connect_address of this ShowInstanceResponse.
        :rtype: str
        """
        return self._management_connect_address

    @management_connect_address.setter
    def management_connect_address(self, management_connect_address):
        r"""Sets the management_connect_address of this ShowInstanceResponse.

        **参数解释**： RabbitMQ实例的管理地址。 **取值范围**： 不涉及。

        :param management_connect_address: The management_connect_address of this ShowInstanceResponse.
        :type management_connect_address: str
        """
        self._management_connect_address = management_connect_address

    @property
    def management_connect_domain_name(self):
        r"""Gets the management_connect_domain_name of this ShowInstanceResponse.

        **参数解释**： RabbitMQ实例的管理域名。 **取值范围**： 不涉及。

        :return: The management_connect_domain_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._management_connect_domain_name

    @management_connect_domain_name.setter
    def management_connect_domain_name(self, management_connect_domain_name):
        r"""Sets the management_connect_domain_name of this ShowInstanceResponse.

        **参数解释**： RabbitMQ实例的管理域名。 **取值范围**： 不涉及。

        :param management_connect_domain_name: The management_connect_domain_name of this ShowInstanceResponse.
        :type management_connect_domain_name: str
        """
        self._management_connect_domain_name = management_connect_domain_name

    @property
    def public_management_connect_address(self):
        r"""Gets the public_management_connect_address of this ShowInstanceResponse.

        **参数解释**： RabbitMQ实例的公网管理地址。 **取值范围**： 不涉及。

        :return: The public_management_connect_address of this ShowInstanceResponse.
        :rtype: str
        """
        return self._public_management_connect_address

    @public_management_connect_address.setter
    def public_management_connect_address(self, public_management_connect_address):
        r"""Sets the public_management_connect_address of this ShowInstanceResponse.

        **参数解释**： RabbitMQ实例的公网管理地址。 **取值范围**： 不涉及。

        :param public_management_connect_address: The public_management_connect_address of this ShowInstanceResponse.
        :type public_management_connect_address: str
        """
        self._public_management_connect_address = public_management_connect_address

    @property
    def public_management_connect_domain_name(self):
        r"""Gets the public_management_connect_domain_name of this ShowInstanceResponse.

        **参数解释**： RabbitMQ实例的公网管理域名。 **取值范围**： 不涉及。

        :return: The public_management_connect_domain_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._public_management_connect_domain_name

    @public_management_connect_domain_name.setter
    def public_management_connect_domain_name(self, public_management_connect_domain_name):
        r"""Sets the public_management_connect_domain_name of this ShowInstanceResponse.

        **参数解释**： RabbitMQ实例的公网管理域名。 **取值范围**： 不涉及。

        :param public_management_connect_domain_name: The public_management_connect_domain_name of this ShowInstanceResponse.
        :type public_management_connect_domain_name: str
        """
        self._public_management_connect_domain_name = public_management_connect_domain_name

    @property
    def ssl_enable(self):
        r"""Gets the ssl_enable of this ShowInstanceResponse.

        **参数解释**： 是否开启安全认证。 **取值范围**： - true：开启 - false：未开启

        :return: The ssl_enable of this ShowInstanceResponse.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        r"""Sets the ssl_enable of this ShowInstanceResponse.

        **参数解释**： 是否开启安全认证。 **取值范围**： - true：开启 - false：未开启

        :param ssl_enable: The ssl_enable of this ShowInstanceResponse.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowInstanceResponse.

        **参数解释**： 企业项目ID。 **取值范围**： 不涉及。

        :return: The enterprise_project_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowInstanceResponse.

        **参数解释**： 企业项目ID。 **取值范围**： 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this ShowInstanceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def is_logical_volume(self):
        r"""Gets the is_logical_volume of this ShowInstanceResponse.

        **参数解释**： 实例扩容时用于区分老实例与新实例。 **取值范围**： - true：新创建的实例，允许磁盘动态扩容不需要重启。 - false：特别老的实例不支持磁盘扩容。

        :return: The is_logical_volume of this ShowInstanceResponse.
        :rtype: bool
        """
        return self._is_logical_volume

    @is_logical_volume.setter
    def is_logical_volume(self, is_logical_volume):
        r"""Sets the is_logical_volume of this ShowInstanceResponse.

        **参数解释**： 实例扩容时用于区分老实例与新实例。 **取值范围**： - true：新创建的实例，允许磁盘动态扩容不需要重启。 - false：特别老的实例不支持磁盘扩容。

        :param is_logical_volume: The is_logical_volume of this ShowInstanceResponse.
        :type is_logical_volume: bool
        """
        self._is_logical_volume = is_logical_volume

    @property
    def extend_times(self):
        r"""Gets the extend_times of this ShowInstanceResponse.

        **参数解释**： 实例扩容磁盘次数，如果超过20次则无法扩容磁盘。 **取值范围**： 不涉及。

        :return: The extend_times of this ShowInstanceResponse.
        :rtype: int
        """
        return self._extend_times

    @extend_times.setter
    def extend_times(self, extend_times):
        r"""Sets the extend_times of this ShowInstanceResponse.

        **参数解释**： 实例扩容磁盘次数，如果超过20次则无法扩容磁盘。 **取值范围**： 不涉及。

        :param extend_times: The extend_times of this ShowInstanceResponse.
        :type extend_times: int
        """
        self._extend_times = extend_times

    @property
    def type(self):
        r"""Gets the type of this ShowInstanceResponse.

        **参数解释**： 实例类型。 **取值范围**： - single：单机。 - cluster：集群。

        :return: The type of this ShowInstanceResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowInstanceResponse.

        **参数解释**： 实例类型。 **取值范围**： - single：单机。 - cluster：集群。

        :param type: The type of this ShowInstanceResponse.
        :type type: str
        """
        self._type = type

    @property
    def product_id(self):
        r"""Gets the product_id of this ShowInstanceResponse.

        **参数解释**： 产品标识。 **取值范围**： 不涉及。

        :return: The product_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ShowInstanceResponse.

        **参数解释**： 产品标识。 **取值范围**： 不涉及。

        :param product_id: The product_id of this ShowInstanceResponse.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this ShowInstanceResponse.

        **参数解释**： 安全组ID。 **取值范围**： 不涉及。

        :return: The security_group_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this ShowInstanceResponse.

        **参数解释**： 安全组ID。 **取值范围**： 不涉及。

        :param security_group_id: The security_group_id of this ShowInstanceResponse.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def security_group_name(self):
        r"""Gets the security_group_name of this ShowInstanceResponse.

        **参数解释**： 租户安全组名称。 **取值范围**： 不涉及。

        :return: The security_group_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._security_group_name

    @security_group_name.setter
    def security_group_name(self, security_group_name):
        r"""Sets the security_group_name of this ShowInstanceResponse.

        **参数解释**： 租户安全组名称。 **取值范围**： 不涉及。

        :param security_group_name: The security_group_name of this ShowInstanceResponse.
        :type security_group_name: str
        """
        self._security_group_name = security_group_name

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ShowInstanceResponse.

        **参数解释**： 子网ID。 **取值范围**： 不涉及。

        :return: The subnet_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ShowInstanceResponse.

        **参数解释**： 子网ID。 **取值范围**： 不涉及。

        :param subnet_id: The subnet_id of this ShowInstanceResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def available_zones(self):
        r"""Gets the available_zones of this ShowInstanceResponse.

        **参数解释**： 实例节点所在的可用区ID。

        :return: The available_zones of this ShowInstanceResponse.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this ShowInstanceResponse.

        **参数解释**： 实例节点所在的可用区ID。

        :param available_zones: The available_zones of this ShowInstanceResponse.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def available_zone_names(self):
        r"""Gets the available_zone_names of this ShowInstanceResponse.

        **参数解释**： 实例节点所在的可用区名称。

        :return: The available_zone_names of this ShowInstanceResponse.
        :rtype: list[str]
        """
        return self._available_zone_names

    @available_zone_names.setter
    def available_zone_names(self, available_zone_names):
        r"""Sets the available_zone_names of this ShowInstanceResponse.

        **参数解释**： 实例节点所在的可用区名称。

        :param available_zone_names: The available_zone_names of this ShowInstanceResponse.
        :type available_zone_names: list[str]
        """
        self._available_zone_names = available_zone_names

    @property
    def total_storage_space(self):
        r"""Gets the total_storage_space of this ShowInstanceResponse.

        **参数解释**： 总共消息存储空间，单位：GB。 **取值范围**： 不涉及。

        :return: The total_storage_space of this ShowInstanceResponse.
        :rtype: int
        """
        return self._total_storage_space

    @total_storage_space.setter
    def total_storage_space(self, total_storage_space):
        r"""Sets the total_storage_space of this ShowInstanceResponse.

        **参数解释**： 总共消息存储空间，单位：GB。 **取值范围**： 不涉及。

        :param total_storage_space: The total_storage_space of this ShowInstanceResponse.
        :type total_storage_space: int
        """
        self._total_storage_space = total_storage_space

    @property
    def storage_resource_id(self):
        r"""Gets the storage_resource_id of this ShowInstanceResponse.

        **参数解释**： 存储资源ID。 **取值范围**： 不涉及。

        :return: The storage_resource_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._storage_resource_id

    @storage_resource_id.setter
    def storage_resource_id(self, storage_resource_id):
        r"""Sets the storage_resource_id of this ShowInstanceResponse.

        **参数解释**： 存储资源ID。 **取值范围**： 不涉及。

        :param storage_resource_id: The storage_resource_id of this ShowInstanceResponse.
        :type storage_resource_id: str
        """
        self._storage_resource_id = storage_resource_id

    @property
    def storage_spec_code(self):
        r"""Gets the storage_spec_code of this ShowInstanceResponse.

        **参数解释**： IO规格。 **取值范围**： 不涉及。

        :return: The storage_spec_code of this ShowInstanceResponse.
        :rtype: str
        """
        return self._storage_spec_code

    @storage_spec_code.setter
    def storage_spec_code(self, storage_spec_code):
        r"""Sets the storage_spec_code of this ShowInstanceResponse.

        **参数解释**： IO规格。 **取值范围**： 不涉及。

        :param storage_spec_code: The storage_spec_code of this ShowInstanceResponse.
        :type storage_spec_code: str
        """
        self._storage_spec_code = storage_spec_code

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this ShowInstanceResponse.

        **参数解释**： 是否开启IPv6。 **取值范围**： - true：开启。 - false：不开启。

        :return: The ipv6_enable of this ShowInstanceResponse.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this ShowInstanceResponse.

        **参数解释**： 是否开启IPv6。 **取值范围**： - true：开启。 - false：不开启。

        :param ipv6_enable: The ipv6_enable of this ShowInstanceResponse.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def ipv6_connect_addresses(self):
        r"""Gets the ipv6_connect_addresses of this ShowInstanceResponse.

        **参数解释**： IPv6的连接地址。

        :return: The ipv6_connect_addresses of this ShowInstanceResponse.
        :rtype: list[str]
        """
        return self._ipv6_connect_addresses

    @ipv6_connect_addresses.setter
    def ipv6_connect_addresses(self, ipv6_connect_addresses):
        r"""Sets the ipv6_connect_addresses of this ShowInstanceResponse.

        **参数解释**： IPv6的连接地址。

        :param ipv6_connect_addresses: The ipv6_connect_addresses of this ShowInstanceResponse.
        :type ipv6_connect_addresses: list[str]
        """
        self._ipv6_connect_addresses = ipv6_connect_addresses

    @property
    def tags(self):
        r"""Gets the tags of this ShowInstanceResponse.

        **参数解释**： 标签列表。

        :return: The tags of this ShowInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkrabbitmq.v2.TagEntity`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowInstanceResponse.

        **参数解释**： 标签列表。

        :param tags: The tags of this ShowInstanceResponse.
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
        if not isinstance(other, ShowInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
