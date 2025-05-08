# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDetail:

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
        'engine': 'str',
        'status': 'str',
        'description': 'str',
        'type': 'str',
        'specification': 'str',
        'engine_version': 'str',
        'instance_id': 'str',
        'charging_mode': 'int',
        'vpc_id': 'str',
        'vpc_name': 'str',
        'created_at': 'str',
        'product_id': 'str',
        'security_group_id': 'str',
        'security_group_name': 'str',
        'subnet_id': 'str',
        'subnet_cidr': 'str',
        'available_zones': 'list[str]',
        'available_zone_names': 'list[str]',
        'user_id': 'str',
        'user_name': 'str',
        'maintain_begin': 'str',
        'maintain_end': 'str',
        'enable_log_collection': 'bool',
        'storage_space': 'int',
        'used_storage_space': 'int',
        'enable_publicip': 'bool',
        'publicip_id': 'str',
        'publicip_address': 'str',
        'ssl_enable': 'bool',
        'cross_vpc_info': 'str',
        'storage_resource_id': 'str',
        'storage_spec_code': 'str',
        'service_type': 'str',
        'storage_type': 'str',
        'extend_times': 'int',
        'ipv6_enable': 'bool',
        'support_features': 'str',
        'disk_encrypted': 'bool',
        'ces_version': 'str',
        'node_num': 'int',
        'new_spec_billing_enable': 'bool',
        'enable_acl': 'bool',
        'broker_num': 'int',
        'dns_enable': 'bool',
        'namesrv_address': 'str',
        'namesrv_domain_name': 'str',
        'broker_address': 'str',
        'public_namesrv_address': 'str',
        'public_namesrv_domain_name': 'str',
        'public_broker_address': 'str',
        'grpc_address': 'str',
        'grpc_domain_name': 'str',
        'public_grpc_address': 'str',
        'public_grpc_domain_name': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[TagEntity]',
        'total_storage_space': 'int',
        'resource_spec_code': 'str',
        'produce_portion': 'int',
        'consume_portion': 'int',
        'dr_enable': 'bool',
        'config_ssl_need_restart_process': 'bool',
        'tls_mode': 'str'
    }

    attribute_map = {
        'name': 'name',
        'engine': 'engine',
        'status': 'status',
        'description': 'description',
        'type': 'type',
        'specification': 'specification',
        'engine_version': 'engine_version',
        'instance_id': 'instance_id',
        'charging_mode': 'charging_mode',
        'vpc_id': 'vpc_id',
        'vpc_name': 'vpc_name',
        'created_at': 'created_at',
        'product_id': 'product_id',
        'security_group_id': 'security_group_id',
        'security_group_name': 'security_group_name',
        'subnet_id': 'subnet_id',
        'subnet_cidr': 'subnet_cidr',
        'available_zones': 'available_zones',
        'available_zone_names': 'available_zone_names',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'maintain_begin': 'maintain_begin',
        'maintain_end': 'maintain_end',
        'enable_log_collection': 'enable_log_collection',
        'storage_space': 'storage_space',
        'used_storage_space': 'used_storage_space',
        'enable_publicip': 'enable_publicip',
        'publicip_id': 'publicip_id',
        'publicip_address': 'publicip_address',
        'ssl_enable': 'ssl_enable',
        'cross_vpc_info': 'cross_vpc_info',
        'storage_resource_id': 'storage_resource_id',
        'storage_spec_code': 'storage_spec_code',
        'service_type': 'service_type',
        'storage_type': 'storage_type',
        'extend_times': 'extend_times',
        'ipv6_enable': 'ipv6_enable',
        'support_features': 'support_features',
        'disk_encrypted': 'disk_encrypted',
        'ces_version': 'ces_version',
        'node_num': 'node_num',
        'new_spec_billing_enable': 'new_spec_billing_enable',
        'enable_acl': 'enable_acl',
        'broker_num': 'broker_num',
        'dns_enable': 'dns_enable',
        'namesrv_address': 'namesrv_address',
        'namesrv_domain_name': 'namesrv_domain_name',
        'broker_address': 'broker_address',
        'public_namesrv_address': 'public_namesrv_address',
        'public_namesrv_domain_name': 'public_namesrv_domain_name',
        'public_broker_address': 'public_broker_address',
        'grpc_address': 'grpc_address',
        'grpc_domain_name': 'grpc_domain_name',
        'public_grpc_address': 'public_grpc_address',
        'public_grpc_domain_name': 'public_grpc_domain_name',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'total_storage_space': 'total_storage_space',
        'resource_spec_code': 'resource_spec_code',
        'produce_portion': 'produce_portion',
        'consume_portion': 'consume_portion',
        'dr_enable': 'dr_enable',
        'config_ssl_need_restart_process': 'config_ssl_need_restart_process',
        'tls_mode': 'tls_mode'
    }

    def __init__(self, name=None, engine=None, status=None, description=None, type=None, specification=None, engine_version=None, instance_id=None, charging_mode=None, vpc_id=None, vpc_name=None, created_at=None, product_id=None, security_group_id=None, security_group_name=None, subnet_id=None, subnet_cidr=None, available_zones=None, available_zone_names=None, user_id=None, user_name=None, maintain_begin=None, maintain_end=None, enable_log_collection=None, storage_space=None, used_storage_space=None, enable_publicip=None, publicip_id=None, publicip_address=None, ssl_enable=None, cross_vpc_info=None, storage_resource_id=None, storage_spec_code=None, service_type=None, storage_type=None, extend_times=None, ipv6_enable=None, support_features=None, disk_encrypted=None, ces_version=None, node_num=None, new_spec_billing_enable=None, enable_acl=None, broker_num=None, dns_enable=None, namesrv_address=None, namesrv_domain_name=None, broker_address=None, public_namesrv_address=None, public_namesrv_domain_name=None, public_broker_address=None, grpc_address=None, grpc_domain_name=None, public_grpc_address=None, public_grpc_domain_name=None, enterprise_project_id=None, tags=None, total_storage_space=None, resource_spec_code=None, produce_portion=None, consume_portion=None, dr_enable=None, config_ssl_need_restart_process=None, tls_mode=None):
        r"""InstanceDetail

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 实例名称。 **取值范围**： 不涉及。
        :type name: str
        :param engine: **参数解释**： 消息引擎。 **取值范围**： 不涉及。
        :type engine: str
        :param status: **参数解释**： 状态。 **取值范围**： 不涉及。
        :type status: str
        :param description: **参数解释**： 消息描述。 **取值范围**： 不涉及。
        :type description: str
        :param type: **参数解释**： 实例类型。 **取值范围**： - single：单机。 - cluster：集群。
        :type type: str
        :param specification: **参数解释**： 实例规格。 **取值范围**： 不涉及。
        :type specification: str
        :param engine_version: **参数解释**： 实例版本。 **取值范围**： 不涉及。
        :type engine_version: str
        :param instance_id: **参数解释**： 实例ID。 **取值范围**： 不涉及。
        :type instance_id: str
        :param charging_mode: **参数解释**： 付费模式。 **取值范围**： [1表示按需计费。](tag:hws_eu,g42,hk_g42,tm,sbc,hk_sbc,hk_tm)[1表示按需计费，0表示包年/包月计费。](tag:hws,hws_eu,hws_hk,ctc) [计费模式，参数暂未使用。](tag:ocb,hws_ocb,hcs,fcs)
        :type charging_mode: int
        :param vpc_id: **参数解释**： 私有云ID。 **取值范围**： 不涉及。
        :type vpc_id: str
        :param vpc_name: **参数解释**： 私有云名称。 **取值范围**： 不涉及。
        :type vpc_name: str
        :param created_at: **参数解释**： 完成创建时间。  格式为时间戳，指从格林威治时间1970年01月01日00时00分00秒起至指定时间的偏差总毫秒数。 **取值范围**： 不涉及。
        :type created_at: str
        :param product_id: **参数解释**： 产品标识。 **取值范围**： 不涉及。
        :type product_id: str
        :param security_group_id: **参数解释**： 安全组ID。 **取值范围**： 不涉及。
        :type security_group_id: str
        :param security_group_name: **参数解释**： 安全组名称。 **取值范围**： 不涉及。
        :type security_group_name: str
        :param subnet_id: **参数解释**： 子网ID。 **取值范围**： 不涉及。
        :type subnet_id: str
        :param subnet_cidr: **参数解释**： 子网路由（仅RocketMQ 5.x版本会显示此字段）。 **取值范围**： 不涉及。
        :type subnet_cidr: str
        :param available_zones: **参数解释**： 可用区ID列表。 **取值范围**： 不涉及。
        :type available_zones: list[str]
        :param available_zone_names: **参数解释**： 可用区名称列表。
        :type available_zone_names: list[str]
        :param user_id: **参数解释**： 用户ID。 **取值范围**： 不涉及。
        :type user_id: str
        :param user_name: **参数解释**： 用户名。 **取值范围**： 不涉及。
        :type user_name: str
        :param maintain_begin: **参数解释**： 维护时间窗开始时间，格式为HH:mm:ss。 **取值范围**： 不涉及。
        :type maintain_begin: str
        :param maintain_end: **参数解释**： 维护时间窗结束时间，格式为HH:mm:ss。 **取值范围**： 不涉及。
        :type maintain_end: str
        :param enable_log_collection: **参数解释**： 是否开启消息收集功能。 **取值范围**： - true：开启。 - false：不开启。
        :type enable_log_collection: bool
        :param storage_space: **参数解释**： 存储空间，单位：GB。 **取值范围**： 不涉及。
        :type storage_space: int
        :param used_storage_space: **参数解释**： 已用消息存储空间，单位：GB。 **取值范围**： 不涉及。
        :type used_storage_space: int
        :param enable_publicip: **参数解释**： 是否开启公网。 **取值范围**： - true：开启。 - false：不开启。
        :type enable_publicip: bool
        :param publicip_id: **参数解释**： 实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。 **取值范围**： 不涉及。
        :type publicip_id: str
        :param publicip_address: **参数解释**： 公网IP地址。 **取值范围**： 不涉及。
        :type publicip_address: str
        :param ssl_enable: **参数解释**： 是否开启SSL。 **取值范围**： - true：开启。 - false：未开启。
        :type ssl_enable: bool
        :param cross_vpc_info: **参数解释**： 跨VPC访问信息。 **取值范围**： 不涉及。
        :type cross_vpc_info: str
        :param storage_resource_id: **参数解释**： 存储资源ID。 **取值范围**： 不涉及。
        :type storage_resource_id: str
        :param storage_spec_code: **参数解释**： 存储规格代码。 **取值范围**： 不涉及。
        :type storage_spec_code: str
        :param service_type: **参数解释**： 服务类型。 **取值范围**： 不涉及。
        :type service_type: str
        :param storage_type: **参数解释**： 存储类型。 **取值范围**： 不涉及。
        :type storage_type: str
        :param extend_times: **参数解释**： 扩展时间。 **取值范围**： 不涉及。
        :type extend_times: int
        :param ipv6_enable: **参数解释**： 是否开启IPv6。 **取值范围**： - true：开启。 - false：未开启。
        :type ipv6_enable: bool
        :param support_features: **参数解释**： 实例支持的特性功能。 **取值范围**： 不涉及。
        :type support_features: str
        :param disk_encrypted: **参数解释**： 是否开启磁盘加密。 **取值范围**： - true：开启。 - false：不开启。
        :type disk_encrypted: bool
        :param ces_version: **参数解释**： 云监控版本。 **取值范围**： 不涉及。
        :type ces_version: str
        :param node_num: **参数解释**： 节点数。 **取值范围**： 不涉及。
        :type node_num: int
        :param new_spec_billing_enable: **参数解释**： 是否启用新规格计费。 **取值范围**： - true：开启。 - false：未开启。
        :type new_spec_billing_enable: bool
        :param enable_acl: **参数解释**： 是否开启访问控制列表。 **取值范围**： - true：开启。 - false：未开启。
        :type enable_acl: bool
        :param broker_num: **参数解释**： Broker节点数（仅RocketMQ 4.8.0版本会显示此字段）。 **取值范围**： 不涉及。
        :type broker_num: int
        :param dns_enable: **参数解释**： 实例是否开启域名访问功能。 **取值范围**： - true：开启。 - false：未开启。
        :type dns_enable: bool
        :param namesrv_address: **参数解释**： 元数据地址。 **取值范围**： 不涉及。
        :type namesrv_address: str
        :param namesrv_domain_name: **参数解释**： 元数据域名。 **取值范围**： 不涉及。
        :type namesrv_domain_name: str
        :param broker_address: **参数解释**： 业务数据地址。 **取值范围**： 不涉及。
        :type broker_address: str
        :param public_namesrv_address: **参数解释**： 公网元数据地址。 **取值范围**： 不涉及。
        :type public_namesrv_address: str
        :param public_namesrv_domain_name: **参数解释**： 公网元数据域名。 **取值范围**： 不涉及。
        :type public_namesrv_domain_name: str
        :param public_broker_address: **参数解释**： 公网业务数据地址。 **取值范围**： 不涉及。
        :type public_broker_address: str
        :param grpc_address: **参数解释**： grpc连接地址（仅RocketMQ 5.x版本会显示此字段）。 **取值范围**： 不涉及。
        :type grpc_address: str
        :param grpc_domain_name: **参数解释**： grpc连接域名（仅RocketMQ 5.x版本会显示此字段）。 **取值范围**： 不涉及。
        :type grpc_domain_name: str
        :param public_grpc_address: **参数解释**： 公网grpc连接地址（仅RocketMQ 5.x版本会显示此字段）。 **取值范围**： 不涉及。
        :type public_grpc_address: str
        :param public_grpc_domain_name: **参数解释**： 公网grpc连接域名（仅RocketMQ 5.x版本会显示此字段）。 **取值范围**： 不涉及。
        :type public_grpc_domain_name: str
        :param enterprise_project_id: **参数解释**： 企业项目ID。 **取值范围**： 不涉及。
        :type enterprise_project_id: str
        :param tags: **参数解释**： 标签列表。 **取值范围**： 不涉及。
        :type tags: list[:class:`huaweicloudsdkrocketmq.v2.TagEntity`]
        :param total_storage_space: **参数解释**： 总存储空间。 **取值范围**： 不涉及。
        :type total_storage_space: int
        :param resource_spec_code: **参数解释**： 资源规格。 **取值范围**： 不涉及。
        :type resource_spec_code: str
        :param produce_portion: **参数解释**： 生产TPS占比。 **取值范围**： 不涉及。
        :type produce_portion: int
        :param consume_portion: **参数解释**： 消费TPS占比。 **取值范围**： 不涉及。
        :type consume_portion: int
        :param dr_enable: **参数解释**： 是否为容灾实例。 **取值范围**： 不涉及。
        :type dr_enable: bool
        :param config_ssl_need_restart_process: **参数解释**： 配置ssl是否需要重启。 **取值范围**： 不涉及。
        :type config_ssl_need_restart_process: bool
        :param tls_mode: **参数解释**： 实例使用的安全协议。 **取值范围**： 不涉及。
        :type tls_mode: str
        """
        
        

        self._name = None
        self._engine = None
        self._status = None
        self._description = None
        self._type = None
        self._specification = None
        self._engine_version = None
        self._instance_id = None
        self._charging_mode = None
        self._vpc_id = None
        self._vpc_name = None
        self._created_at = None
        self._product_id = None
        self._security_group_id = None
        self._security_group_name = None
        self._subnet_id = None
        self._subnet_cidr = None
        self._available_zones = None
        self._available_zone_names = None
        self._user_id = None
        self._user_name = None
        self._maintain_begin = None
        self._maintain_end = None
        self._enable_log_collection = None
        self._storage_space = None
        self._used_storage_space = None
        self._enable_publicip = None
        self._publicip_id = None
        self._publicip_address = None
        self._ssl_enable = None
        self._cross_vpc_info = None
        self._storage_resource_id = None
        self._storage_spec_code = None
        self._service_type = None
        self._storage_type = None
        self._extend_times = None
        self._ipv6_enable = None
        self._support_features = None
        self._disk_encrypted = None
        self._ces_version = None
        self._node_num = None
        self._new_spec_billing_enable = None
        self._enable_acl = None
        self._broker_num = None
        self._dns_enable = None
        self._namesrv_address = None
        self._namesrv_domain_name = None
        self._broker_address = None
        self._public_namesrv_address = None
        self._public_namesrv_domain_name = None
        self._public_broker_address = None
        self._grpc_address = None
        self._grpc_domain_name = None
        self._public_grpc_address = None
        self._public_grpc_domain_name = None
        self._enterprise_project_id = None
        self._tags = None
        self._total_storage_space = None
        self._resource_spec_code = None
        self._produce_portion = None
        self._consume_portion = None
        self._dr_enable = None
        self._config_ssl_need_restart_process = None
        self._tls_mode = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if engine is not None:
            self.engine = engine
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if specification is not None:
            self.specification = specification
        if engine_version is not None:
            self.engine_version = engine_version
        if instance_id is not None:
            self.instance_id = instance_id
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_name is not None:
            self.vpc_name = vpc_name
        if created_at is not None:
            self.created_at = created_at
        if product_id is not None:
            self.product_id = product_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if security_group_name is not None:
            self.security_group_name = security_group_name
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if subnet_cidr is not None:
            self.subnet_cidr = subnet_cidr
        if available_zones is not None:
            self.available_zones = available_zones
        if available_zone_names is not None:
            self.available_zone_names = available_zone_names
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if maintain_begin is not None:
            self.maintain_begin = maintain_begin
        if maintain_end is not None:
            self.maintain_end = maintain_end
        if enable_log_collection is not None:
            self.enable_log_collection = enable_log_collection
        if storage_space is not None:
            self.storage_space = storage_space
        if used_storage_space is not None:
            self.used_storage_space = used_storage_space
        if enable_publicip is not None:
            self.enable_publicip = enable_publicip
        if publicip_id is not None:
            self.publicip_id = publicip_id
        if publicip_address is not None:
            self.publicip_address = publicip_address
        if ssl_enable is not None:
            self.ssl_enable = ssl_enable
        if cross_vpc_info is not None:
            self.cross_vpc_info = cross_vpc_info
        if storage_resource_id is not None:
            self.storage_resource_id = storage_resource_id
        if storage_spec_code is not None:
            self.storage_spec_code = storage_spec_code
        if service_type is not None:
            self.service_type = service_type
        if storage_type is not None:
            self.storage_type = storage_type
        if extend_times is not None:
            self.extend_times = extend_times
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if support_features is not None:
            self.support_features = support_features
        if disk_encrypted is not None:
            self.disk_encrypted = disk_encrypted
        if ces_version is not None:
            self.ces_version = ces_version
        if node_num is not None:
            self.node_num = node_num
        if new_spec_billing_enable is not None:
            self.new_spec_billing_enable = new_spec_billing_enable
        if enable_acl is not None:
            self.enable_acl = enable_acl
        if broker_num is not None:
            self.broker_num = broker_num
        if dns_enable is not None:
            self.dns_enable = dns_enable
        if namesrv_address is not None:
            self.namesrv_address = namesrv_address
        if namesrv_domain_name is not None:
            self.namesrv_domain_name = namesrv_domain_name
        if broker_address is not None:
            self.broker_address = broker_address
        if public_namesrv_address is not None:
            self.public_namesrv_address = public_namesrv_address
        if public_namesrv_domain_name is not None:
            self.public_namesrv_domain_name = public_namesrv_domain_name
        if public_broker_address is not None:
            self.public_broker_address = public_broker_address
        if grpc_address is not None:
            self.grpc_address = grpc_address
        if grpc_domain_name is not None:
            self.grpc_domain_name = grpc_domain_name
        if public_grpc_address is not None:
            self.public_grpc_address = public_grpc_address
        if public_grpc_domain_name is not None:
            self.public_grpc_domain_name = public_grpc_domain_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if total_storage_space is not None:
            self.total_storage_space = total_storage_space
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if produce_portion is not None:
            self.produce_portion = produce_portion
        if consume_portion is not None:
            self.consume_portion = consume_portion
        if dr_enable is not None:
            self.dr_enable = dr_enable
        if config_ssl_need_restart_process is not None:
            self.config_ssl_need_restart_process = config_ssl_need_restart_process
        if tls_mode is not None:
            self.tls_mode = tls_mode

    @property
    def name(self):
        r"""Gets the name of this InstanceDetail.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :return: The name of this InstanceDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstanceDetail.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :param name: The name of this InstanceDetail.
        :type name: str
        """
        self._name = name

    @property
    def engine(self):
        r"""Gets the engine of this InstanceDetail.

        **参数解释**： 消息引擎。 **取值范围**： 不涉及。

        :return: The engine of this InstanceDetail.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this InstanceDetail.

        **参数解释**： 消息引擎。 **取值范围**： 不涉及。

        :param engine: The engine of this InstanceDetail.
        :type engine: str
        """
        self._engine = engine

    @property
    def status(self):
        r"""Gets the status of this InstanceDetail.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :return: The status of this InstanceDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InstanceDetail.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :param status: The status of this InstanceDetail.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this InstanceDetail.

        **参数解释**： 消息描述。 **取值范围**： 不涉及。

        :return: The description of this InstanceDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this InstanceDetail.

        **参数解释**： 消息描述。 **取值范围**： 不涉及。

        :param description: The description of this InstanceDetail.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this InstanceDetail.

        **参数解释**： 实例类型。 **取值范围**： - single：单机。 - cluster：集群。

        :return: The type of this InstanceDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this InstanceDetail.

        **参数解释**： 实例类型。 **取值范围**： - single：单机。 - cluster：集群。

        :param type: The type of this InstanceDetail.
        :type type: str
        """
        self._type = type

    @property
    def specification(self):
        r"""Gets the specification of this InstanceDetail.

        **参数解释**： 实例规格。 **取值范围**： 不涉及。

        :return: The specification of this InstanceDetail.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this InstanceDetail.

        **参数解释**： 实例规格。 **取值范围**： 不涉及。

        :param specification: The specification of this InstanceDetail.
        :type specification: str
        """
        self._specification = specification

    @property
    def engine_version(self):
        r"""Gets the engine_version of this InstanceDetail.

        **参数解释**： 实例版本。 **取值范围**： 不涉及。

        :return: The engine_version of this InstanceDetail.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this InstanceDetail.

        **参数解释**： 实例版本。 **取值范围**： 不涉及。

        :param engine_version: The engine_version of this InstanceDetail.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceDetail.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。

        :return: The instance_id of this InstanceDetail.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceDetail.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。

        :param instance_id: The instance_id of this InstanceDetail.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this InstanceDetail.

        **参数解释**： 付费模式。 **取值范围**： [1表示按需计费。](tag:hws_eu,g42,hk_g42,tm,sbc,hk_sbc,hk_tm)[1表示按需计费，0表示包年/包月计费。](tag:hws,hws_eu,hws_hk,ctc) [计费模式，参数暂未使用。](tag:ocb,hws_ocb,hcs,fcs)

        :return: The charging_mode of this InstanceDetail.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this InstanceDetail.

        **参数解释**： 付费模式。 **取值范围**： [1表示按需计费。](tag:hws_eu,g42,hk_g42,tm,sbc,hk_sbc,hk_tm)[1表示按需计费，0表示包年/包月计费。](tag:hws,hws_eu,hws_hk,ctc) [计费模式，参数暂未使用。](tag:ocb,hws_ocb,hcs,fcs)

        :param charging_mode: The charging_mode of this InstanceDetail.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this InstanceDetail.

        **参数解释**： 私有云ID。 **取值范围**： 不涉及。

        :return: The vpc_id of this InstanceDetail.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this InstanceDetail.

        **参数解释**： 私有云ID。 **取值范围**： 不涉及。

        :param vpc_id: The vpc_id of this InstanceDetail.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        r"""Gets the vpc_name of this InstanceDetail.

        **参数解释**： 私有云名称。 **取值范围**： 不涉及。

        :return: The vpc_name of this InstanceDetail.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        r"""Sets the vpc_name of this InstanceDetail.

        **参数解释**： 私有云名称。 **取值范围**： 不涉及。

        :param vpc_name: The vpc_name of this InstanceDetail.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def created_at(self):
        r"""Gets the created_at of this InstanceDetail.

        **参数解释**： 完成创建时间。  格式为时间戳，指从格林威治时间1970年01月01日00时00分00秒起至指定时间的偏差总毫秒数。 **取值范围**： 不涉及。

        :return: The created_at of this InstanceDetail.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this InstanceDetail.

        **参数解释**： 完成创建时间。  格式为时间戳，指从格林威治时间1970年01月01日00时00分00秒起至指定时间的偏差总毫秒数。 **取值范围**： 不涉及。

        :param created_at: The created_at of this InstanceDetail.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def product_id(self):
        r"""Gets the product_id of this InstanceDetail.

        **参数解释**： 产品标识。 **取值范围**： 不涉及。

        :return: The product_id of this InstanceDetail.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this InstanceDetail.

        **参数解释**： 产品标识。 **取值范围**： 不涉及。

        :param product_id: The product_id of this InstanceDetail.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this InstanceDetail.

        **参数解释**： 安全组ID。 **取值范围**： 不涉及。

        :return: The security_group_id of this InstanceDetail.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this InstanceDetail.

        **参数解释**： 安全组ID。 **取值范围**： 不涉及。

        :param security_group_id: The security_group_id of this InstanceDetail.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def security_group_name(self):
        r"""Gets the security_group_name of this InstanceDetail.

        **参数解释**： 安全组名称。 **取值范围**： 不涉及。

        :return: The security_group_name of this InstanceDetail.
        :rtype: str
        """
        return self._security_group_name

    @security_group_name.setter
    def security_group_name(self, security_group_name):
        r"""Sets the security_group_name of this InstanceDetail.

        **参数解释**： 安全组名称。 **取值范围**： 不涉及。

        :param security_group_name: The security_group_name of this InstanceDetail.
        :type security_group_name: str
        """
        self._security_group_name = security_group_name

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this InstanceDetail.

        **参数解释**： 子网ID。 **取值范围**： 不涉及。

        :return: The subnet_id of this InstanceDetail.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this InstanceDetail.

        **参数解释**： 子网ID。 **取值范围**： 不涉及。

        :param subnet_id: The subnet_id of this InstanceDetail.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def subnet_cidr(self):
        r"""Gets the subnet_cidr of this InstanceDetail.

        **参数解释**： 子网路由（仅RocketMQ 5.x版本会显示此字段）。 **取值范围**： 不涉及。

        :return: The subnet_cidr of this InstanceDetail.
        :rtype: str
        """
        return self._subnet_cidr

    @subnet_cidr.setter
    def subnet_cidr(self, subnet_cidr):
        r"""Sets the subnet_cidr of this InstanceDetail.

        **参数解释**： 子网路由（仅RocketMQ 5.x版本会显示此字段）。 **取值范围**： 不涉及。

        :param subnet_cidr: The subnet_cidr of this InstanceDetail.
        :type subnet_cidr: str
        """
        self._subnet_cidr = subnet_cidr

    @property
    def available_zones(self):
        r"""Gets the available_zones of this InstanceDetail.

        **参数解释**： 可用区ID列表。 **取值范围**： 不涉及。

        :return: The available_zones of this InstanceDetail.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this InstanceDetail.

        **参数解释**： 可用区ID列表。 **取值范围**： 不涉及。

        :param available_zones: The available_zones of this InstanceDetail.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def available_zone_names(self):
        r"""Gets the available_zone_names of this InstanceDetail.

        **参数解释**： 可用区名称列表。

        :return: The available_zone_names of this InstanceDetail.
        :rtype: list[str]
        """
        return self._available_zone_names

    @available_zone_names.setter
    def available_zone_names(self, available_zone_names):
        r"""Sets the available_zone_names of this InstanceDetail.

        **参数解释**： 可用区名称列表。

        :param available_zone_names: The available_zone_names of this InstanceDetail.
        :type available_zone_names: list[str]
        """
        self._available_zone_names = available_zone_names

    @property
    def user_id(self):
        r"""Gets the user_id of this InstanceDetail.

        **参数解释**： 用户ID。 **取值范围**： 不涉及。

        :return: The user_id of this InstanceDetail.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this InstanceDetail.

        **参数解释**： 用户ID。 **取值范围**： 不涉及。

        :param user_id: The user_id of this InstanceDetail.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this InstanceDetail.

        **参数解释**： 用户名。 **取值范围**： 不涉及。

        :return: The user_name of this InstanceDetail.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this InstanceDetail.

        **参数解释**： 用户名。 **取值范围**： 不涉及。

        :param user_name: The user_name of this InstanceDetail.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def maintain_begin(self):
        r"""Gets the maintain_begin of this InstanceDetail.

        **参数解释**： 维护时间窗开始时间，格式为HH:mm:ss。 **取值范围**： 不涉及。

        :return: The maintain_begin of this InstanceDetail.
        :rtype: str
        """
        return self._maintain_begin

    @maintain_begin.setter
    def maintain_begin(self, maintain_begin):
        r"""Sets the maintain_begin of this InstanceDetail.

        **参数解释**： 维护时间窗开始时间，格式为HH:mm:ss。 **取值范围**： 不涉及。

        :param maintain_begin: The maintain_begin of this InstanceDetail.
        :type maintain_begin: str
        """
        self._maintain_begin = maintain_begin

    @property
    def maintain_end(self):
        r"""Gets the maintain_end of this InstanceDetail.

        **参数解释**： 维护时间窗结束时间，格式为HH:mm:ss。 **取值范围**： 不涉及。

        :return: The maintain_end of this InstanceDetail.
        :rtype: str
        """
        return self._maintain_end

    @maintain_end.setter
    def maintain_end(self, maintain_end):
        r"""Sets the maintain_end of this InstanceDetail.

        **参数解释**： 维护时间窗结束时间，格式为HH:mm:ss。 **取值范围**： 不涉及。

        :param maintain_end: The maintain_end of this InstanceDetail.
        :type maintain_end: str
        """
        self._maintain_end = maintain_end

    @property
    def enable_log_collection(self):
        r"""Gets the enable_log_collection of this InstanceDetail.

        **参数解释**： 是否开启消息收集功能。 **取值范围**： - true：开启。 - false：不开启。

        :return: The enable_log_collection of this InstanceDetail.
        :rtype: bool
        """
        return self._enable_log_collection

    @enable_log_collection.setter
    def enable_log_collection(self, enable_log_collection):
        r"""Sets the enable_log_collection of this InstanceDetail.

        **参数解释**： 是否开启消息收集功能。 **取值范围**： - true：开启。 - false：不开启。

        :param enable_log_collection: The enable_log_collection of this InstanceDetail.
        :type enable_log_collection: bool
        """
        self._enable_log_collection = enable_log_collection

    @property
    def storage_space(self):
        r"""Gets the storage_space of this InstanceDetail.

        **参数解释**： 存储空间，单位：GB。 **取值范围**： 不涉及。

        :return: The storage_space of this InstanceDetail.
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        r"""Sets the storage_space of this InstanceDetail.

        **参数解释**： 存储空间，单位：GB。 **取值范围**： 不涉及。

        :param storage_space: The storage_space of this InstanceDetail.
        :type storage_space: int
        """
        self._storage_space = storage_space

    @property
    def used_storage_space(self):
        r"""Gets the used_storage_space of this InstanceDetail.

        **参数解释**： 已用消息存储空间，单位：GB。 **取值范围**： 不涉及。

        :return: The used_storage_space of this InstanceDetail.
        :rtype: int
        """
        return self._used_storage_space

    @used_storage_space.setter
    def used_storage_space(self, used_storage_space):
        r"""Sets the used_storage_space of this InstanceDetail.

        **参数解释**： 已用消息存储空间，单位：GB。 **取值范围**： 不涉及。

        :param used_storage_space: The used_storage_space of this InstanceDetail.
        :type used_storage_space: int
        """
        self._used_storage_space = used_storage_space

    @property
    def enable_publicip(self):
        r"""Gets the enable_publicip of this InstanceDetail.

        **参数解释**： 是否开启公网。 **取值范围**： - true：开启。 - false：不开启。

        :return: The enable_publicip of this InstanceDetail.
        :rtype: bool
        """
        return self._enable_publicip

    @enable_publicip.setter
    def enable_publicip(self, enable_publicip):
        r"""Sets the enable_publicip of this InstanceDetail.

        **参数解释**： 是否开启公网。 **取值范围**： - true：开启。 - false：不开启。

        :param enable_publicip: The enable_publicip of this InstanceDetail.
        :type enable_publicip: bool
        """
        self._enable_publicip = enable_publicip

    @property
    def publicip_id(self):
        r"""Gets the publicip_id of this InstanceDetail.

        **参数解释**： 实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。 **取值范围**： 不涉及。

        :return: The publicip_id of this InstanceDetail.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        r"""Sets the publicip_id of this InstanceDetail.

        **参数解释**： 实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。 **取值范围**： 不涉及。

        :param publicip_id: The publicip_id of this InstanceDetail.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def publicip_address(self):
        r"""Gets the publicip_address of this InstanceDetail.

        **参数解释**： 公网IP地址。 **取值范围**： 不涉及。

        :return: The publicip_address of this InstanceDetail.
        :rtype: str
        """
        return self._publicip_address

    @publicip_address.setter
    def publicip_address(self, publicip_address):
        r"""Sets the publicip_address of this InstanceDetail.

        **参数解释**： 公网IP地址。 **取值范围**： 不涉及。

        :param publicip_address: The publicip_address of this InstanceDetail.
        :type publicip_address: str
        """
        self._publicip_address = publicip_address

    @property
    def ssl_enable(self):
        r"""Gets the ssl_enable of this InstanceDetail.

        **参数解释**： 是否开启SSL。 **取值范围**： - true：开启。 - false：未开启。

        :return: The ssl_enable of this InstanceDetail.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        r"""Sets the ssl_enable of this InstanceDetail.

        **参数解释**： 是否开启SSL。 **取值范围**： - true：开启。 - false：未开启。

        :param ssl_enable: The ssl_enable of this InstanceDetail.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

    @property
    def cross_vpc_info(self):
        r"""Gets the cross_vpc_info of this InstanceDetail.

        **参数解释**： 跨VPC访问信息。 **取值范围**： 不涉及。

        :return: The cross_vpc_info of this InstanceDetail.
        :rtype: str
        """
        return self._cross_vpc_info

    @cross_vpc_info.setter
    def cross_vpc_info(self, cross_vpc_info):
        r"""Sets the cross_vpc_info of this InstanceDetail.

        **参数解释**： 跨VPC访问信息。 **取值范围**： 不涉及。

        :param cross_vpc_info: The cross_vpc_info of this InstanceDetail.
        :type cross_vpc_info: str
        """
        self._cross_vpc_info = cross_vpc_info

    @property
    def storage_resource_id(self):
        r"""Gets the storage_resource_id of this InstanceDetail.

        **参数解释**： 存储资源ID。 **取值范围**： 不涉及。

        :return: The storage_resource_id of this InstanceDetail.
        :rtype: str
        """
        return self._storage_resource_id

    @storage_resource_id.setter
    def storage_resource_id(self, storage_resource_id):
        r"""Sets the storage_resource_id of this InstanceDetail.

        **参数解释**： 存储资源ID。 **取值范围**： 不涉及。

        :param storage_resource_id: The storage_resource_id of this InstanceDetail.
        :type storage_resource_id: str
        """
        self._storage_resource_id = storage_resource_id

    @property
    def storage_spec_code(self):
        r"""Gets the storage_spec_code of this InstanceDetail.

        **参数解释**： 存储规格代码。 **取值范围**： 不涉及。

        :return: The storage_spec_code of this InstanceDetail.
        :rtype: str
        """
        return self._storage_spec_code

    @storage_spec_code.setter
    def storage_spec_code(self, storage_spec_code):
        r"""Sets the storage_spec_code of this InstanceDetail.

        **参数解释**： 存储规格代码。 **取值范围**： 不涉及。

        :param storage_spec_code: The storage_spec_code of this InstanceDetail.
        :type storage_spec_code: str
        """
        self._storage_spec_code = storage_spec_code

    @property
    def service_type(self):
        r"""Gets the service_type of this InstanceDetail.

        **参数解释**： 服务类型。 **取值范围**： 不涉及。

        :return: The service_type of this InstanceDetail.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this InstanceDetail.

        **参数解释**： 服务类型。 **取值范围**： 不涉及。

        :param service_type: The service_type of this InstanceDetail.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def storage_type(self):
        r"""Gets the storage_type of this InstanceDetail.

        **参数解释**： 存储类型。 **取值范围**： 不涉及。

        :return: The storage_type of this InstanceDetail.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        r"""Sets the storage_type of this InstanceDetail.

        **参数解释**： 存储类型。 **取值范围**： 不涉及。

        :param storage_type: The storage_type of this InstanceDetail.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def extend_times(self):
        r"""Gets the extend_times of this InstanceDetail.

        **参数解释**： 扩展时间。 **取值范围**： 不涉及。

        :return: The extend_times of this InstanceDetail.
        :rtype: int
        """
        return self._extend_times

    @extend_times.setter
    def extend_times(self, extend_times):
        r"""Sets the extend_times of this InstanceDetail.

        **参数解释**： 扩展时间。 **取值范围**： 不涉及。

        :param extend_times: The extend_times of this InstanceDetail.
        :type extend_times: int
        """
        self._extend_times = extend_times

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this InstanceDetail.

        **参数解释**： 是否开启IPv6。 **取值范围**： - true：开启。 - false：未开启。

        :return: The ipv6_enable of this InstanceDetail.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this InstanceDetail.

        **参数解释**： 是否开启IPv6。 **取值范围**： - true：开启。 - false：未开启。

        :param ipv6_enable: The ipv6_enable of this InstanceDetail.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def support_features(self):
        r"""Gets the support_features of this InstanceDetail.

        **参数解释**： 实例支持的特性功能。 **取值范围**： 不涉及。

        :return: The support_features of this InstanceDetail.
        :rtype: str
        """
        return self._support_features

    @support_features.setter
    def support_features(self, support_features):
        r"""Sets the support_features of this InstanceDetail.

        **参数解释**： 实例支持的特性功能。 **取值范围**： 不涉及。

        :param support_features: The support_features of this InstanceDetail.
        :type support_features: str
        """
        self._support_features = support_features

    @property
    def disk_encrypted(self):
        r"""Gets the disk_encrypted of this InstanceDetail.

        **参数解释**： 是否开启磁盘加密。 **取值范围**： - true：开启。 - false：不开启。

        :return: The disk_encrypted of this InstanceDetail.
        :rtype: bool
        """
        return self._disk_encrypted

    @disk_encrypted.setter
    def disk_encrypted(self, disk_encrypted):
        r"""Sets the disk_encrypted of this InstanceDetail.

        **参数解释**： 是否开启磁盘加密。 **取值范围**： - true：开启。 - false：不开启。

        :param disk_encrypted: The disk_encrypted of this InstanceDetail.
        :type disk_encrypted: bool
        """
        self._disk_encrypted = disk_encrypted

    @property
    def ces_version(self):
        r"""Gets the ces_version of this InstanceDetail.

        **参数解释**： 云监控版本。 **取值范围**： 不涉及。

        :return: The ces_version of this InstanceDetail.
        :rtype: str
        """
        return self._ces_version

    @ces_version.setter
    def ces_version(self, ces_version):
        r"""Sets the ces_version of this InstanceDetail.

        **参数解释**： 云监控版本。 **取值范围**： 不涉及。

        :param ces_version: The ces_version of this InstanceDetail.
        :type ces_version: str
        """
        self._ces_version = ces_version

    @property
    def node_num(self):
        r"""Gets the node_num of this InstanceDetail.

        **参数解释**： 节点数。 **取值范围**： 不涉及。

        :return: The node_num of this InstanceDetail.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this InstanceDetail.

        **参数解释**： 节点数。 **取值范围**： 不涉及。

        :param node_num: The node_num of this InstanceDetail.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def new_spec_billing_enable(self):
        r"""Gets the new_spec_billing_enable of this InstanceDetail.

        **参数解释**： 是否启用新规格计费。 **取值范围**： - true：开启。 - false：未开启。

        :return: The new_spec_billing_enable of this InstanceDetail.
        :rtype: bool
        """
        return self._new_spec_billing_enable

    @new_spec_billing_enable.setter
    def new_spec_billing_enable(self, new_spec_billing_enable):
        r"""Sets the new_spec_billing_enable of this InstanceDetail.

        **参数解释**： 是否启用新规格计费。 **取值范围**： - true：开启。 - false：未开启。

        :param new_spec_billing_enable: The new_spec_billing_enable of this InstanceDetail.
        :type new_spec_billing_enable: bool
        """
        self._new_spec_billing_enable = new_spec_billing_enable

    @property
    def enable_acl(self):
        r"""Gets the enable_acl of this InstanceDetail.

        **参数解释**： 是否开启访问控制列表。 **取值范围**： - true：开启。 - false：未开启。

        :return: The enable_acl of this InstanceDetail.
        :rtype: bool
        """
        return self._enable_acl

    @enable_acl.setter
    def enable_acl(self, enable_acl):
        r"""Sets the enable_acl of this InstanceDetail.

        **参数解释**： 是否开启访问控制列表。 **取值范围**： - true：开启。 - false：未开启。

        :param enable_acl: The enable_acl of this InstanceDetail.
        :type enable_acl: bool
        """
        self._enable_acl = enable_acl

    @property
    def broker_num(self):
        r"""Gets the broker_num of this InstanceDetail.

        **参数解释**： Broker节点数（仅RocketMQ 4.8.0版本会显示此字段）。 **取值范围**： 不涉及。

        :return: The broker_num of this InstanceDetail.
        :rtype: int
        """
        return self._broker_num

    @broker_num.setter
    def broker_num(self, broker_num):
        r"""Sets the broker_num of this InstanceDetail.

        **参数解释**： Broker节点数（仅RocketMQ 4.8.0版本会显示此字段）。 **取值范围**： 不涉及。

        :param broker_num: The broker_num of this InstanceDetail.
        :type broker_num: int
        """
        self._broker_num = broker_num

    @property
    def dns_enable(self):
        r"""Gets the dns_enable of this InstanceDetail.

        **参数解释**： 实例是否开启域名访问功能。 **取值范围**： - true：开启。 - false：未开启。

        :return: The dns_enable of this InstanceDetail.
        :rtype: bool
        """
        return self._dns_enable

    @dns_enable.setter
    def dns_enable(self, dns_enable):
        r"""Sets the dns_enable of this InstanceDetail.

        **参数解释**： 实例是否开启域名访问功能。 **取值范围**： - true：开启。 - false：未开启。

        :param dns_enable: The dns_enable of this InstanceDetail.
        :type dns_enable: bool
        """
        self._dns_enable = dns_enable

    @property
    def namesrv_address(self):
        r"""Gets the namesrv_address of this InstanceDetail.

        **参数解释**： 元数据地址。 **取值范围**： 不涉及。

        :return: The namesrv_address of this InstanceDetail.
        :rtype: str
        """
        return self._namesrv_address

    @namesrv_address.setter
    def namesrv_address(self, namesrv_address):
        r"""Sets the namesrv_address of this InstanceDetail.

        **参数解释**： 元数据地址。 **取值范围**： 不涉及。

        :param namesrv_address: The namesrv_address of this InstanceDetail.
        :type namesrv_address: str
        """
        self._namesrv_address = namesrv_address

    @property
    def namesrv_domain_name(self):
        r"""Gets the namesrv_domain_name of this InstanceDetail.

        **参数解释**： 元数据域名。 **取值范围**： 不涉及。

        :return: The namesrv_domain_name of this InstanceDetail.
        :rtype: str
        """
        return self._namesrv_domain_name

    @namesrv_domain_name.setter
    def namesrv_domain_name(self, namesrv_domain_name):
        r"""Sets the namesrv_domain_name of this InstanceDetail.

        **参数解释**： 元数据域名。 **取值范围**： 不涉及。

        :param namesrv_domain_name: The namesrv_domain_name of this InstanceDetail.
        :type namesrv_domain_name: str
        """
        self._namesrv_domain_name = namesrv_domain_name

    @property
    def broker_address(self):
        r"""Gets the broker_address of this InstanceDetail.

        **参数解释**： 业务数据地址。 **取值范围**： 不涉及。

        :return: The broker_address of this InstanceDetail.
        :rtype: str
        """
        return self._broker_address

    @broker_address.setter
    def broker_address(self, broker_address):
        r"""Sets the broker_address of this InstanceDetail.

        **参数解释**： 业务数据地址。 **取值范围**： 不涉及。

        :param broker_address: The broker_address of this InstanceDetail.
        :type broker_address: str
        """
        self._broker_address = broker_address

    @property
    def public_namesrv_address(self):
        r"""Gets the public_namesrv_address of this InstanceDetail.

        **参数解释**： 公网元数据地址。 **取值范围**： 不涉及。

        :return: The public_namesrv_address of this InstanceDetail.
        :rtype: str
        """
        return self._public_namesrv_address

    @public_namesrv_address.setter
    def public_namesrv_address(self, public_namesrv_address):
        r"""Sets the public_namesrv_address of this InstanceDetail.

        **参数解释**： 公网元数据地址。 **取值范围**： 不涉及。

        :param public_namesrv_address: The public_namesrv_address of this InstanceDetail.
        :type public_namesrv_address: str
        """
        self._public_namesrv_address = public_namesrv_address

    @property
    def public_namesrv_domain_name(self):
        r"""Gets the public_namesrv_domain_name of this InstanceDetail.

        **参数解释**： 公网元数据域名。 **取值范围**： 不涉及。

        :return: The public_namesrv_domain_name of this InstanceDetail.
        :rtype: str
        """
        return self._public_namesrv_domain_name

    @public_namesrv_domain_name.setter
    def public_namesrv_domain_name(self, public_namesrv_domain_name):
        r"""Sets the public_namesrv_domain_name of this InstanceDetail.

        **参数解释**： 公网元数据域名。 **取值范围**： 不涉及。

        :param public_namesrv_domain_name: The public_namesrv_domain_name of this InstanceDetail.
        :type public_namesrv_domain_name: str
        """
        self._public_namesrv_domain_name = public_namesrv_domain_name

    @property
    def public_broker_address(self):
        r"""Gets the public_broker_address of this InstanceDetail.

        **参数解释**： 公网业务数据地址。 **取值范围**： 不涉及。

        :return: The public_broker_address of this InstanceDetail.
        :rtype: str
        """
        return self._public_broker_address

    @public_broker_address.setter
    def public_broker_address(self, public_broker_address):
        r"""Sets the public_broker_address of this InstanceDetail.

        **参数解释**： 公网业务数据地址。 **取值范围**： 不涉及。

        :param public_broker_address: The public_broker_address of this InstanceDetail.
        :type public_broker_address: str
        """
        self._public_broker_address = public_broker_address

    @property
    def grpc_address(self):
        r"""Gets the grpc_address of this InstanceDetail.

        **参数解释**： grpc连接地址（仅RocketMQ 5.x版本会显示此字段）。 **取值范围**： 不涉及。

        :return: The grpc_address of this InstanceDetail.
        :rtype: str
        """
        return self._grpc_address

    @grpc_address.setter
    def grpc_address(self, grpc_address):
        r"""Sets the grpc_address of this InstanceDetail.

        **参数解释**： grpc连接地址（仅RocketMQ 5.x版本会显示此字段）。 **取值范围**： 不涉及。

        :param grpc_address: The grpc_address of this InstanceDetail.
        :type grpc_address: str
        """
        self._grpc_address = grpc_address

    @property
    def grpc_domain_name(self):
        r"""Gets the grpc_domain_name of this InstanceDetail.

        **参数解释**： grpc连接域名（仅RocketMQ 5.x版本会显示此字段）。 **取值范围**： 不涉及。

        :return: The grpc_domain_name of this InstanceDetail.
        :rtype: str
        """
        return self._grpc_domain_name

    @grpc_domain_name.setter
    def grpc_domain_name(self, grpc_domain_name):
        r"""Sets the grpc_domain_name of this InstanceDetail.

        **参数解释**： grpc连接域名（仅RocketMQ 5.x版本会显示此字段）。 **取值范围**： 不涉及。

        :param grpc_domain_name: The grpc_domain_name of this InstanceDetail.
        :type grpc_domain_name: str
        """
        self._grpc_domain_name = grpc_domain_name

    @property
    def public_grpc_address(self):
        r"""Gets the public_grpc_address of this InstanceDetail.

        **参数解释**： 公网grpc连接地址（仅RocketMQ 5.x版本会显示此字段）。 **取值范围**： 不涉及。

        :return: The public_grpc_address of this InstanceDetail.
        :rtype: str
        """
        return self._public_grpc_address

    @public_grpc_address.setter
    def public_grpc_address(self, public_grpc_address):
        r"""Sets the public_grpc_address of this InstanceDetail.

        **参数解释**： 公网grpc连接地址（仅RocketMQ 5.x版本会显示此字段）。 **取值范围**： 不涉及。

        :param public_grpc_address: The public_grpc_address of this InstanceDetail.
        :type public_grpc_address: str
        """
        self._public_grpc_address = public_grpc_address

    @property
    def public_grpc_domain_name(self):
        r"""Gets the public_grpc_domain_name of this InstanceDetail.

        **参数解释**： 公网grpc连接域名（仅RocketMQ 5.x版本会显示此字段）。 **取值范围**： 不涉及。

        :return: The public_grpc_domain_name of this InstanceDetail.
        :rtype: str
        """
        return self._public_grpc_domain_name

    @public_grpc_domain_name.setter
    def public_grpc_domain_name(self, public_grpc_domain_name):
        r"""Sets the public_grpc_domain_name of this InstanceDetail.

        **参数解释**： 公网grpc连接域名（仅RocketMQ 5.x版本会显示此字段）。 **取值范围**： 不涉及。

        :param public_grpc_domain_name: The public_grpc_domain_name of this InstanceDetail.
        :type public_grpc_domain_name: str
        """
        self._public_grpc_domain_name = public_grpc_domain_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this InstanceDetail.

        **参数解释**： 企业项目ID。 **取值范围**： 不涉及。

        :return: The enterprise_project_id of this InstanceDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this InstanceDetail.

        **参数解释**： 企业项目ID。 **取值范围**： 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this InstanceDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this InstanceDetail.

        **参数解释**： 标签列表。 **取值范围**： 不涉及。

        :return: The tags of this InstanceDetail.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.TagEntity`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this InstanceDetail.

        **参数解释**： 标签列表。 **取值范围**： 不涉及。

        :param tags: The tags of this InstanceDetail.
        :type tags: list[:class:`huaweicloudsdkrocketmq.v2.TagEntity`]
        """
        self._tags = tags

    @property
    def total_storage_space(self):
        r"""Gets the total_storage_space of this InstanceDetail.

        **参数解释**： 总存储空间。 **取值范围**： 不涉及。

        :return: The total_storage_space of this InstanceDetail.
        :rtype: int
        """
        return self._total_storage_space

    @total_storage_space.setter
    def total_storage_space(self, total_storage_space):
        r"""Sets the total_storage_space of this InstanceDetail.

        **参数解释**： 总存储空间。 **取值范围**： 不涉及。

        :param total_storage_space: The total_storage_space of this InstanceDetail.
        :type total_storage_space: int
        """
        self._total_storage_space = total_storage_space

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this InstanceDetail.

        **参数解释**： 资源规格。 **取值范围**： 不涉及。

        :return: The resource_spec_code of this InstanceDetail.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this InstanceDetail.

        **参数解释**： 资源规格。 **取值范围**： 不涉及。

        :param resource_spec_code: The resource_spec_code of this InstanceDetail.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def produce_portion(self):
        r"""Gets the produce_portion of this InstanceDetail.

        **参数解释**： 生产TPS占比。 **取值范围**： 不涉及。

        :return: The produce_portion of this InstanceDetail.
        :rtype: int
        """
        return self._produce_portion

    @produce_portion.setter
    def produce_portion(self, produce_portion):
        r"""Sets the produce_portion of this InstanceDetail.

        **参数解释**： 生产TPS占比。 **取值范围**： 不涉及。

        :param produce_portion: The produce_portion of this InstanceDetail.
        :type produce_portion: int
        """
        self._produce_portion = produce_portion

    @property
    def consume_portion(self):
        r"""Gets the consume_portion of this InstanceDetail.

        **参数解释**： 消费TPS占比。 **取值范围**： 不涉及。

        :return: The consume_portion of this InstanceDetail.
        :rtype: int
        """
        return self._consume_portion

    @consume_portion.setter
    def consume_portion(self, consume_portion):
        r"""Sets the consume_portion of this InstanceDetail.

        **参数解释**： 消费TPS占比。 **取值范围**： 不涉及。

        :param consume_portion: The consume_portion of this InstanceDetail.
        :type consume_portion: int
        """
        self._consume_portion = consume_portion

    @property
    def dr_enable(self):
        r"""Gets the dr_enable of this InstanceDetail.

        **参数解释**： 是否为容灾实例。 **取值范围**： 不涉及。

        :return: The dr_enable of this InstanceDetail.
        :rtype: bool
        """
        return self._dr_enable

    @dr_enable.setter
    def dr_enable(self, dr_enable):
        r"""Sets the dr_enable of this InstanceDetail.

        **参数解释**： 是否为容灾实例。 **取值范围**： 不涉及。

        :param dr_enable: The dr_enable of this InstanceDetail.
        :type dr_enable: bool
        """
        self._dr_enable = dr_enable

    @property
    def config_ssl_need_restart_process(self):
        r"""Gets the config_ssl_need_restart_process of this InstanceDetail.

        **参数解释**： 配置ssl是否需要重启。 **取值范围**： 不涉及。

        :return: The config_ssl_need_restart_process of this InstanceDetail.
        :rtype: bool
        """
        return self._config_ssl_need_restart_process

    @config_ssl_need_restart_process.setter
    def config_ssl_need_restart_process(self, config_ssl_need_restart_process):
        r"""Sets the config_ssl_need_restart_process of this InstanceDetail.

        **参数解释**： 配置ssl是否需要重启。 **取值范围**： 不涉及。

        :param config_ssl_need_restart_process: The config_ssl_need_restart_process of this InstanceDetail.
        :type config_ssl_need_restart_process: bool
        """
        self._config_ssl_need_restart_process = config_ssl_need_restart_process

    @property
    def tls_mode(self):
        r"""Gets the tls_mode of this InstanceDetail.

        **参数解释**： 实例使用的安全协议。 **取值范围**： 不涉及。

        :return: The tls_mode of this InstanceDetail.
        :rtype: str
        """
        return self._tls_mode

    @tls_mode.setter
    def tls_mode(self, tls_mode):
        r"""Sets the tls_mode of this InstanceDetail.

        **参数解释**： 实例使用的安全协议。 **取值范围**： 不涉及。

        :param tls_mode: The tls_mode of this InstanceDetail.
        :type tls_mode: str
        """
        self._tls_mode = tls_mode

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
        if not isinstance(other, InstanceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
