# coding: utf-8

import re
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
        'name': 'str',
        'engine': 'str',
        'engine_version': 'str',
        'description': 'str',
        'specification': 'str',
        'storage_space': 'int',
        'partition_num': 'str',
        'used_storage_space': 'int',
        'connect_address': 'str',
        'port': 'int',
        'status': 'str',
        'instance_id': 'str',
        'resource_spec_code': 'str',
        'charging_mode': 'int',
        'vpc_id': 'str',
        'vpc_name': 'str',
        'created_at': 'str',
        'subnet_name': 'str',
        'subnet_cidr': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'access_user': 'str',
        'order_id': 'str',
        'maintain_begin': 'str',
        'maintain_end': 'str',
        'enable_publicip': 'bool',
        'management_connect_address': 'str',
        'ssl_enable': 'bool',
        'sasl_enabled_mechanisms': 'list[str]',
        'ssl_two_way_enable': 'bool',
        'cert_replaced': 'bool',
        'public_management_connect_address': 'str',
        'enterprise_project_id': 'str',
        'is_logical_volume': 'bool',
        'extend_times': 'int',
        'enable_auto_topic': 'bool',
        'type': 'str',
        'product_id': 'str',
        'security_group_id': 'str',
        'security_group_name': 'str',
        'subnet_id': 'str',
        'available_zones': 'list[str]',
        'total_storage_space': 'int',
        'public_connect_address': 'str',
        'storage_resource_id': 'str',
        'storage_spec_code': 'str',
        'service_type': 'str',
        'storage_type': 'str',
        'retention_policy': 'str',
        'kafka_public_status': 'str',
        'public_bandwidth': 'int',
        'kafka_manager_user': 'str',
        'enable_log_collection': 'bool',
        'cross_vpc_info': 'str',
        'ipv6_enable': 'bool',
        'ipv6_connect_addresses': 'list[str]',
        'connector_enable': 'bool',
        'connector_id': 'str',
        'rest_enable': 'bool',
        'rest_connect_address': 'str',
        'public_boundwidth': 'int',
        'message_query_inst_enable': 'bool',
        'vpc_client_plain': 'bool',
        'support_features': 'str',
        'trace_enable': 'bool',
        'agent_enable': 'bool',
        'pod_connect_address': 'str',
        'disk_encrypted': 'bool',
        'disk_encrypted_key': 'str',
        'kafka_private_connect_address': 'str',
        'ces_version': 'str',
        'public_access_enabled': 'str',
        'node_num': 'int',
        'enable_acl': 'bool',
        'new_spec_billing_enable': 'bool',
        'broker_num': 'int',
        'tags': 'list[TagEntity]',
        'dr_enable': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'description': 'description',
        'specification': 'specification',
        'storage_space': 'storage_space',
        'partition_num': 'partition_num',
        'used_storage_space': 'used_storage_space',
        'connect_address': 'connect_address',
        'port': 'port',
        'status': 'status',
        'instance_id': 'instance_id',
        'resource_spec_code': 'resource_spec_code',
        'charging_mode': 'charging_mode',
        'vpc_id': 'vpc_id',
        'vpc_name': 'vpc_name',
        'created_at': 'created_at',
        'subnet_name': 'subnet_name',
        'subnet_cidr': 'subnet_cidr',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'access_user': 'access_user',
        'order_id': 'order_id',
        'maintain_begin': 'maintain_begin',
        'maintain_end': 'maintain_end',
        'enable_publicip': 'enable_publicip',
        'management_connect_address': 'management_connect_address',
        'ssl_enable': 'ssl_enable',
        'sasl_enabled_mechanisms': 'sasl_enabled_mechanisms',
        'ssl_two_way_enable': 'ssl_two_way_enable',
        'cert_replaced': 'cert_replaced',
        'public_management_connect_address': 'public_management_connect_address',
        'enterprise_project_id': 'enterprise_project_id',
        'is_logical_volume': 'is_logical_volume',
        'extend_times': 'extend_times',
        'enable_auto_topic': 'enable_auto_topic',
        'type': 'type',
        'product_id': 'product_id',
        'security_group_id': 'security_group_id',
        'security_group_name': 'security_group_name',
        'subnet_id': 'subnet_id',
        'available_zones': 'available_zones',
        'total_storage_space': 'total_storage_space',
        'public_connect_address': 'public_connect_address',
        'storage_resource_id': 'storage_resource_id',
        'storage_spec_code': 'storage_spec_code',
        'service_type': 'service_type',
        'storage_type': 'storage_type',
        'retention_policy': 'retention_policy',
        'kafka_public_status': 'kafka_public_status',
        'public_bandwidth': 'public_bandwidth',
        'kafka_manager_user': 'kafka_manager_user',
        'enable_log_collection': 'enable_log_collection',
        'cross_vpc_info': 'cross_vpc_info',
        'ipv6_enable': 'ipv6_enable',
        'ipv6_connect_addresses': 'ipv6_connect_addresses',
        'connector_enable': 'connector_enable',
        'connector_id': 'connector_id',
        'rest_enable': 'rest_enable',
        'rest_connect_address': 'rest_connect_address',
        'public_boundwidth': 'public_boundwidth',
        'message_query_inst_enable': 'message_query_inst_enable',
        'vpc_client_plain': 'vpc_client_plain',
        'support_features': 'support_features',
        'trace_enable': 'trace_enable',
        'agent_enable': 'agent_enable',
        'pod_connect_address': 'pod_connect_address',
        'disk_encrypted': 'disk_encrypted',
        'disk_encrypted_key': 'disk_encrypted_key',
        'kafka_private_connect_address': 'kafka_private_connect_address',
        'ces_version': 'ces_version',
        'public_access_enabled': 'public_access_enabled',
        'node_num': 'node_num',
        'enable_acl': 'enable_acl',
        'new_spec_billing_enable': 'new_spec_billing_enable',
        'broker_num': 'broker_num',
        'tags': 'tags',
        'dr_enable': 'dr_enable'
    }

    def __init__(self, name=None, engine=None, engine_version=None, description=None, specification=None, storage_space=None, partition_num=None, used_storage_space=None, connect_address=None, port=None, status=None, instance_id=None, resource_spec_code=None, charging_mode=None, vpc_id=None, vpc_name=None, created_at=None, subnet_name=None, subnet_cidr=None, user_id=None, user_name=None, access_user=None, order_id=None, maintain_begin=None, maintain_end=None, enable_publicip=None, management_connect_address=None, ssl_enable=None, sasl_enabled_mechanisms=None, ssl_two_way_enable=None, cert_replaced=None, public_management_connect_address=None, enterprise_project_id=None, is_logical_volume=None, extend_times=None, enable_auto_topic=None, type=None, product_id=None, security_group_id=None, security_group_name=None, subnet_id=None, available_zones=None, total_storage_space=None, public_connect_address=None, storage_resource_id=None, storage_spec_code=None, service_type=None, storage_type=None, retention_policy=None, kafka_public_status=None, public_bandwidth=None, kafka_manager_user=None, enable_log_collection=None, cross_vpc_info=None, ipv6_enable=None, ipv6_connect_addresses=None, connector_enable=None, connector_id=None, rest_enable=None, rest_connect_address=None, public_boundwidth=None, message_query_inst_enable=None, vpc_client_plain=None, support_features=None, trace_enable=None, agent_enable=None, pod_connect_address=None, disk_encrypted=None, disk_encrypted_key=None, kafka_private_connect_address=None, ces_version=None, public_access_enabled=None, node_num=None, enable_acl=None, new_spec_billing_enable=None, broker_num=None, tags=None, dr_enable=None):
        """ShowInstanceResp

        The model defined in huaweicloud sdk

        :param name: 实例名称。
        :type name: str
        :param engine: 引擎。
        :type engine: str
        :param engine_version: 版本。
        :type engine_version: str
        :param description: 实例描述。
        :type description: str
        :param specification: 实例规格。
        :type specification: str
        :param storage_space: 消息存储空间，单位：GB。
        :type storage_space: int
        :param partition_num: Kafka实例的分区数量。
        :type partition_num: str
        :param used_storage_space: 已使用的消息存储空间，单位：GB。
        :type used_storage_space: int
        :param connect_address: 实例连接IP地址。
        :type connect_address: str
        :param port: 实例连接端口。
        :type port: int
        :param status: 实例的状态。 [详细状态说明见[实例状态说明](https://support.huaweicloud.com/api-kafka/kafka-api-180514012.html)。](tag:hws)[详细状态说明见[实例状态说明](https://support.huaweicloud.com/intl/zh-cn/api-kafka/kafka-api-180514012.html)。](tag:hws_hk)
        :type status: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param resource_spec_code: 资源规格标识。   - dms.instance.kafka.cluster.c3.mini：Kafka实例的基准带宽为100MByte/秒。   - dms.instance.kafka.cluster.c3.small.2：Kafka实例的基准带宽为300MByte/秒。   - dms.instance.kafka.cluster.c3.middle.2：Kafka实例的基准带宽为600MByte/秒。   - dms.instance.kafka.cluster.c3.high.2：Kafka实例的基准带宽为1200MByte/秒。
        :type resource_spec_code: str
        :param charging_mode: [付费模式，1表示按需计费，0表示包年/包月计费。](tag:hc,hk,hws,hws_hk,ctc,sbc,hk_sbc,cmcc,hws_eu)[付费模式，暂未使用。](tag:hws_ocb,ocb) [付费模式，1表示按需计费。](tag:otc,dt,g42,tm)
        :type charging_mode: int
        :param vpc_id: VPC ID。
        :type vpc_id: str
        :param vpc_name: VPC的名称。
        :type vpc_name: str
        :param created_at: 完成创建时间。  格式为时间戳，指从格林威治时间 1970年01月01日00时00分00秒起至指定时间的偏差总毫秒数。
        :type created_at: str
        :param subnet_name: 子网名称。
        :type subnet_name: str
        :param subnet_cidr: 子网网段。
        :type subnet_cidr: str
        :param user_id: 用户ID。
        :type user_id: str
        :param user_name: 用户名。
        :type user_name: str
        :param access_user: 实例访问用户名。
        :type access_user: str
        :param order_id: 订单ID，只有在包周期计费时才会有order_id值，其他计费方式order_id值为空。
        :type order_id: str
        :param maintain_begin: 维护时间窗开始时间，格式为HH:mm:ss。
        :type maintain_begin: str
        :param maintain_end: 维护时间窗结束时间，格式为HH:mm:ss。
        :type maintain_end: str
        :param enable_publicip: 实例是否开启公网访问功能。 - true：开启 - false：未开启
        :type enable_publicip: bool
        :param management_connect_address: Kafka实例的Kafka Manager连接地址。
        :type management_connect_address: str
        :param ssl_enable: 是否开启安全认证。 - true：开启 - false：未开启
        :type ssl_enable: bool
        :param sasl_enabled_mechanisms: 开启SASL后使用的认证机制。 - PLAIN: 简单的用户名密码校验。 - SCRAM-SHA-512: 用户凭证校验，安全性比PLAIN机制更高。
        :type sasl_enabled_mechanisms: list[str]
        :param ssl_two_way_enable: 是否开启双向认证。
        :type ssl_two_way_enable: bool
        :param cert_replaced: 是否能够证书替换。
        :type cert_replaced: bool
        :param public_management_connect_address: 公网访问Kafka Manager连接地址。
        :type public_management_connect_address: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param is_logical_volume: 实例扩容时用于区分老实例与新实例。 - true：新创建的实例，允许磁盘动态扩容不需要重启。 - false：老实例
        :type is_logical_volume: bool
        :param extend_times: 实例扩容磁盘次数，如果超过20次则无法扩容磁盘。
        :type extend_times: int
        :param enable_auto_topic: 是否打开kafka自动创建topic功能。   - true：开启   - false：关闭
        :type enable_auto_topic: bool
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
        :param public_connect_address: 实例公网连接IP地址。当实例开启了公网访问，实例才包含该参数。
        :type public_connect_address: str
        :param storage_resource_id: 存储资源ID。
        :type storage_resource_id: str
        :param storage_spec_code: IO规格。
        :type storage_spec_code: str
        :param service_type: 服务类型。
        :type service_type: str
        :param storage_type: 存储类型。
        :type storage_type: str
        :param retention_policy: 消息老化策略。
        :type retention_policy: str
        :param kafka_public_status: Kafka公网开启状态。
        :type kafka_public_status: str
        :param public_bandwidth: kafka公网访问带宽。
        :type public_bandwidth: int
        :param kafka_manager_user: 登录Kafka Manager的用户名。
        :type kafka_manager_user: str
        :param enable_log_collection: 是否开启消息收集功能。
        :type enable_log_collection: bool
        :param cross_vpc_info: 跨VPC访问信息。
        :type cross_vpc_info: str
        :param ipv6_enable: 是否开启ipv6。
        :type ipv6_enable: bool
        :param ipv6_connect_addresses: IPv6的连接地址。
        :type ipv6_connect_addresses: list[str]
        :param connector_enable: 是否开启转储。新规格产品暂不支持开启转储。
        :type connector_enable: bool
        :param connector_id: 转储任务ID。
        :type connector_id: str
        :param rest_enable: 是否开启Kafka rest功能。
        :type rest_enable: bool
        :param rest_connect_address: Kafka rest连接地址。
        :type rest_connect_address: str
        :param public_boundwidth: kafka公网访问带宽。待删除版本。
        :type public_boundwidth: int
        :param message_query_inst_enable: 是否开启消息查询功能。
        :type message_query_inst_enable: bool
        :param vpc_client_plain: 是否开启VPC明文访问。
        :type vpc_client_plain: bool
        :param support_features: Kafka实例支持的特性功能。
        :type support_features: str
        :param trace_enable: 是否开启消息轨迹功能。
        :type trace_enable: bool
        :param agent_enable: 是否开启代理。
        :type agent_enable: bool
        :param pod_connect_address: 租户侧连接地址。
        :type pod_connect_address: str
        :param disk_encrypted: 是否开启磁盘加密。
        :type disk_encrypted: bool
        :param disk_encrypted_key: 磁盘加密key，未开启磁盘加密时为空。
        :type disk_encrypted_key: str
        :param kafka_private_connect_address: Kafka实例私有连接地址。
        :type kafka_private_connect_address: str
        :param ces_version: 云监控版本。
        :type ces_version: str
        :param public_access_enabled: 区分实例什么时候开启的公网访问：true,actived,closed,false。
        :type public_access_enabled: str
        :param node_num: 节点数。
        :type node_num: int
        :param enable_acl: 是否开启访问控制。
        :type enable_acl: bool
        :param new_spec_billing_enable: 是否启用新规格计费。
        :type new_spec_billing_enable: bool
        :param broker_num: 节点数量。
        :type broker_num: int
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkkafka.v2.TagEntity`]
        :param dr_enable: 是否为容灾实例。
        :type dr_enable: bool
        """
        
        

        self._name = None
        self._engine = None
        self._engine_version = None
        self._description = None
        self._specification = None
        self._storage_space = None
        self._partition_num = None
        self._used_storage_space = None
        self._connect_address = None
        self._port = None
        self._status = None
        self._instance_id = None
        self._resource_spec_code = None
        self._charging_mode = None
        self._vpc_id = None
        self._vpc_name = None
        self._created_at = None
        self._subnet_name = None
        self._subnet_cidr = None
        self._user_id = None
        self._user_name = None
        self._access_user = None
        self._order_id = None
        self._maintain_begin = None
        self._maintain_end = None
        self._enable_publicip = None
        self._management_connect_address = None
        self._ssl_enable = None
        self._sasl_enabled_mechanisms = None
        self._ssl_two_way_enable = None
        self._cert_replaced = None
        self._public_management_connect_address = None
        self._enterprise_project_id = None
        self._is_logical_volume = None
        self._extend_times = None
        self._enable_auto_topic = None
        self._type = None
        self._product_id = None
        self._security_group_id = None
        self._security_group_name = None
        self._subnet_id = None
        self._available_zones = None
        self._total_storage_space = None
        self._public_connect_address = None
        self._storage_resource_id = None
        self._storage_spec_code = None
        self._service_type = None
        self._storage_type = None
        self._retention_policy = None
        self._kafka_public_status = None
        self._public_bandwidth = None
        self._kafka_manager_user = None
        self._enable_log_collection = None
        self._cross_vpc_info = None
        self._ipv6_enable = None
        self._ipv6_connect_addresses = None
        self._connector_enable = None
        self._connector_id = None
        self._rest_enable = None
        self._rest_connect_address = None
        self._public_boundwidth = None
        self._message_query_inst_enable = None
        self._vpc_client_plain = None
        self._support_features = None
        self._trace_enable = None
        self._agent_enable = None
        self._pod_connect_address = None
        self._disk_encrypted = None
        self._disk_encrypted_key = None
        self._kafka_private_connect_address = None
        self._ces_version = None
        self._public_access_enabled = None
        self._node_num = None
        self._enable_acl = None
        self._new_spec_billing_enable = None
        self._broker_num = None
        self._tags = None
        self._dr_enable = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if engine is not None:
            self.engine = engine
        if engine_version is not None:
            self.engine_version = engine_version
        if description is not None:
            self.description = description
        if specification is not None:
            self.specification = specification
        if storage_space is not None:
            self.storage_space = storage_space
        if partition_num is not None:
            self.partition_num = partition_num
        if used_storage_space is not None:
            self.used_storage_space = used_storage_space
        if connect_address is not None:
            self.connect_address = connect_address
        if port is not None:
            self.port = port
        if status is not None:
            self.status = status
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
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if subnet_cidr is not None:
            self.subnet_cidr = subnet_cidr
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if access_user is not None:
            self.access_user = access_user
        if order_id is not None:
            self.order_id = order_id
        if maintain_begin is not None:
            self.maintain_begin = maintain_begin
        if maintain_end is not None:
            self.maintain_end = maintain_end
        if enable_publicip is not None:
            self.enable_publicip = enable_publicip
        if management_connect_address is not None:
            self.management_connect_address = management_connect_address
        if ssl_enable is not None:
            self.ssl_enable = ssl_enable
        if sasl_enabled_mechanisms is not None:
            self.sasl_enabled_mechanisms = sasl_enabled_mechanisms
        if ssl_two_way_enable is not None:
            self.ssl_two_way_enable = ssl_two_way_enable
        if cert_replaced is not None:
            self.cert_replaced = cert_replaced
        if public_management_connect_address is not None:
            self.public_management_connect_address = public_management_connect_address
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if is_logical_volume is not None:
            self.is_logical_volume = is_logical_volume
        if extend_times is not None:
            self.extend_times = extend_times
        if enable_auto_topic is not None:
            self.enable_auto_topic = enable_auto_topic
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
        if public_connect_address is not None:
            self.public_connect_address = public_connect_address
        if storage_resource_id is not None:
            self.storage_resource_id = storage_resource_id
        if storage_spec_code is not None:
            self.storage_spec_code = storage_spec_code
        if service_type is not None:
            self.service_type = service_type
        if storage_type is not None:
            self.storage_type = storage_type
        if retention_policy is not None:
            self.retention_policy = retention_policy
        if kafka_public_status is not None:
            self.kafka_public_status = kafka_public_status
        if public_bandwidth is not None:
            self.public_bandwidth = public_bandwidth
        if kafka_manager_user is not None:
            self.kafka_manager_user = kafka_manager_user
        if enable_log_collection is not None:
            self.enable_log_collection = enable_log_collection
        if cross_vpc_info is not None:
            self.cross_vpc_info = cross_vpc_info
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if ipv6_connect_addresses is not None:
            self.ipv6_connect_addresses = ipv6_connect_addresses
        if connector_enable is not None:
            self.connector_enable = connector_enable
        if connector_id is not None:
            self.connector_id = connector_id
        if rest_enable is not None:
            self.rest_enable = rest_enable
        if rest_connect_address is not None:
            self.rest_connect_address = rest_connect_address
        if public_boundwidth is not None:
            self.public_boundwidth = public_boundwidth
        if message_query_inst_enable is not None:
            self.message_query_inst_enable = message_query_inst_enable
        if vpc_client_plain is not None:
            self.vpc_client_plain = vpc_client_plain
        if support_features is not None:
            self.support_features = support_features
        if trace_enable is not None:
            self.trace_enable = trace_enable
        if agent_enable is not None:
            self.agent_enable = agent_enable
        if pod_connect_address is not None:
            self.pod_connect_address = pod_connect_address
        if disk_encrypted is not None:
            self.disk_encrypted = disk_encrypted
        if disk_encrypted_key is not None:
            self.disk_encrypted_key = disk_encrypted_key
        if kafka_private_connect_address is not None:
            self.kafka_private_connect_address = kafka_private_connect_address
        if ces_version is not None:
            self.ces_version = ces_version
        if public_access_enabled is not None:
            self.public_access_enabled = public_access_enabled
        if node_num is not None:
            self.node_num = node_num
        if enable_acl is not None:
            self.enable_acl = enable_acl
        if new_spec_billing_enable is not None:
            self.new_spec_billing_enable = new_spec_billing_enable
        if broker_num is not None:
            self.broker_num = broker_num
        if tags is not None:
            self.tags = tags
        if dr_enable is not None:
            self.dr_enable = dr_enable

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

        引擎。

        :return: The engine of this ShowInstanceResp.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ShowInstanceResp.

        引擎。

        :param engine: The engine of this ShowInstanceResp.
        :type engine: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        """Gets the engine_version of this ShowInstanceResp.

        版本。

        :return: The engine_version of this ShowInstanceResp.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this ShowInstanceResp.

        版本。

        :param engine_version: The engine_version of this ShowInstanceResp.
        :type engine_version: str
        """
        self._engine_version = engine_version

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
    def specification(self):
        """Gets the specification of this ShowInstanceResp.

        实例规格。

        :return: The specification of this ShowInstanceResp.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        """Sets the specification of this ShowInstanceResp.

        实例规格。

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
    def partition_num(self):
        """Gets the partition_num of this ShowInstanceResp.

        Kafka实例的分区数量。

        :return: The partition_num of this ShowInstanceResp.
        :rtype: str
        """
        return self._partition_num

    @partition_num.setter
    def partition_num(self, partition_num):
        """Sets the partition_num of this ShowInstanceResp.

        Kafka实例的分区数量。

        :param partition_num: The partition_num of this ShowInstanceResp.
        :type partition_num: str
        """
        self._partition_num = partition_num

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

        实例的状态。 [详细状态说明见[实例状态说明](https://support.huaweicloud.com/api-kafka/kafka-api-180514012.html)。](tag:hws)[详细状态说明见[实例状态说明](https://support.huaweicloud.com/intl/zh-cn/api-kafka/kafka-api-180514012.html)。](tag:hws_hk)

        :return: The status of this ShowInstanceResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowInstanceResp.

        实例的状态。 [详细状态说明见[实例状态说明](https://support.huaweicloud.com/api-kafka/kafka-api-180514012.html)。](tag:hws)[详细状态说明见[实例状态说明](https://support.huaweicloud.com/intl/zh-cn/api-kafka/kafka-api-180514012.html)。](tag:hws_hk)

        :param status: The status of this ShowInstanceResp.
        :type status: str
        """
        self._status = status

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

        资源规格标识。   - dms.instance.kafka.cluster.c3.mini：Kafka实例的基准带宽为100MByte/秒。   - dms.instance.kafka.cluster.c3.small.2：Kafka实例的基准带宽为300MByte/秒。   - dms.instance.kafka.cluster.c3.middle.2：Kafka实例的基准带宽为600MByte/秒。   - dms.instance.kafka.cluster.c3.high.2：Kafka实例的基准带宽为1200MByte/秒。

        :return: The resource_spec_code of this ShowInstanceResp.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this ShowInstanceResp.

        资源规格标识。   - dms.instance.kafka.cluster.c3.mini：Kafka实例的基准带宽为100MByte/秒。   - dms.instance.kafka.cluster.c3.small.2：Kafka实例的基准带宽为300MByte/秒。   - dms.instance.kafka.cluster.c3.middle.2：Kafka实例的基准带宽为600MByte/秒。   - dms.instance.kafka.cluster.c3.high.2：Kafka实例的基准带宽为1200MByte/秒。

        :param resource_spec_code: The resource_spec_code of this ShowInstanceResp.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def charging_mode(self):
        """Gets the charging_mode of this ShowInstanceResp.

        [付费模式，1表示按需计费，0表示包年/包月计费。](tag:hc,hk,hws,hws_hk,ctc,sbc,hk_sbc,cmcc,hws_eu)[付费模式，暂未使用。](tag:hws_ocb,ocb) [付费模式，1表示按需计费。](tag:otc,dt,g42,tm)

        :return: The charging_mode of this ShowInstanceResp.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this ShowInstanceResp.

        [付费模式，1表示按需计费，0表示包年/包月计费。](tag:hc,hk,hws,hws_hk,ctc,sbc,hk_sbc,cmcc,hws_eu)[付费模式，暂未使用。](tag:hws_ocb,ocb) [付费模式，1表示按需计费。](tag:otc,dt,g42,tm)

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

        完成创建时间。  格式为时间戳，指从格林威治时间 1970年01月01日00时00分00秒起至指定时间的偏差总毫秒数。

        :return: The created_at of this ShowInstanceResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowInstanceResp.

        完成创建时间。  格式为时间戳，指从格林威治时间 1970年01月01日00时00分00秒起至指定时间的偏差总毫秒数。

        :param created_at: The created_at of this ShowInstanceResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def subnet_name(self):
        """Gets the subnet_name of this ShowInstanceResp.

        子网名称。

        :return: The subnet_name of this ShowInstanceResp.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        """Sets the subnet_name of this ShowInstanceResp.

        子网名称。

        :param subnet_name: The subnet_name of this ShowInstanceResp.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def subnet_cidr(self):
        """Gets the subnet_cidr of this ShowInstanceResp.

        子网网段。

        :return: The subnet_cidr of this ShowInstanceResp.
        :rtype: str
        """
        return self._subnet_cidr

    @subnet_cidr.setter
    def subnet_cidr(self, subnet_cidr):
        """Sets the subnet_cidr of this ShowInstanceResp.

        子网网段。

        :param subnet_cidr: The subnet_cidr of this ShowInstanceResp.
        :type subnet_cidr: str
        """
        self._subnet_cidr = subnet_cidr

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
    def access_user(self):
        """Gets the access_user of this ShowInstanceResp.

        实例访问用户名。

        :return: The access_user of this ShowInstanceResp.
        :rtype: str
        """
        return self._access_user

    @access_user.setter
    def access_user(self, access_user):
        """Sets the access_user of this ShowInstanceResp.

        实例访问用户名。

        :param access_user: The access_user of this ShowInstanceResp.
        :type access_user: str
        """
        self._access_user = access_user

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

        实例是否开启公网访问功能。 - true：开启 - false：未开启

        :return: The enable_publicip of this ShowInstanceResp.
        :rtype: bool
        """
        return self._enable_publicip

    @enable_publicip.setter
    def enable_publicip(self, enable_publicip):
        """Sets the enable_publicip of this ShowInstanceResp.

        实例是否开启公网访问功能。 - true：开启 - false：未开启

        :param enable_publicip: The enable_publicip of this ShowInstanceResp.
        :type enable_publicip: bool
        """
        self._enable_publicip = enable_publicip

    @property
    def management_connect_address(self):
        """Gets the management_connect_address of this ShowInstanceResp.

        Kafka实例的Kafka Manager连接地址。

        :return: The management_connect_address of this ShowInstanceResp.
        :rtype: str
        """
        return self._management_connect_address

    @management_connect_address.setter
    def management_connect_address(self, management_connect_address):
        """Sets the management_connect_address of this ShowInstanceResp.

        Kafka实例的Kafka Manager连接地址。

        :param management_connect_address: The management_connect_address of this ShowInstanceResp.
        :type management_connect_address: str
        """
        self._management_connect_address = management_connect_address

    @property
    def ssl_enable(self):
        """Gets the ssl_enable of this ShowInstanceResp.

        是否开启安全认证。 - true：开启 - false：未开启

        :return: The ssl_enable of this ShowInstanceResp.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        """Sets the ssl_enable of this ShowInstanceResp.

        是否开启安全认证。 - true：开启 - false：未开启

        :param ssl_enable: The ssl_enable of this ShowInstanceResp.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

    @property
    def sasl_enabled_mechanisms(self):
        """Gets the sasl_enabled_mechanisms of this ShowInstanceResp.

        开启SASL后使用的认证机制。 - PLAIN: 简单的用户名密码校验。 - SCRAM-SHA-512: 用户凭证校验，安全性比PLAIN机制更高。

        :return: The sasl_enabled_mechanisms of this ShowInstanceResp.
        :rtype: list[str]
        """
        return self._sasl_enabled_mechanisms

    @sasl_enabled_mechanisms.setter
    def sasl_enabled_mechanisms(self, sasl_enabled_mechanisms):
        """Sets the sasl_enabled_mechanisms of this ShowInstanceResp.

        开启SASL后使用的认证机制。 - PLAIN: 简单的用户名密码校验。 - SCRAM-SHA-512: 用户凭证校验，安全性比PLAIN机制更高。

        :param sasl_enabled_mechanisms: The sasl_enabled_mechanisms of this ShowInstanceResp.
        :type sasl_enabled_mechanisms: list[str]
        """
        self._sasl_enabled_mechanisms = sasl_enabled_mechanisms

    @property
    def ssl_two_way_enable(self):
        """Gets the ssl_two_way_enable of this ShowInstanceResp.

        是否开启双向认证。

        :return: The ssl_two_way_enable of this ShowInstanceResp.
        :rtype: bool
        """
        return self._ssl_two_way_enable

    @ssl_two_way_enable.setter
    def ssl_two_way_enable(self, ssl_two_way_enable):
        """Sets the ssl_two_way_enable of this ShowInstanceResp.

        是否开启双向认证。

        :param ssl_two_way_enable: The ssl_two_way_enable of this ShowInstanceResp.
        :type ssl_two_way_enable: bool
        """
        self._ssl_two_way_enable = ssl_two_way_enable

    @property
    def cert_replaced(self):
        """Gets the cert_replaced of this ShowInstanceResp.

        是否能够证书替换。

        :return: The cert_replaced of this ShowInstanceResp.
        :rtype: bool
        """
        return self._cert_replaced

    @cert_replaced.setter
    def cert_replaced(self, cert_replaced):
        """Sets the cert_replaced of this ShowInstanceResp.

        是否能够证书替换。

        :param cert_replaced: The cert_replaced of this ShowInstanceResp.
        :type cert_replaced: bool
        """
        self._cert_replaced = cert_replaced

    @property
    def public_management_connect_address(self):
        """Gets the public_management_connect_address of this ShowInstanceResp.

        公网访问Kafka Manager连接地址。

        :return: The public_management_connect_address of this ShowInstanceResp.
        :rtype: str
        """
        return self._public_management_connect_address

    @public_management_connect_address.setter
    def public_management_connect_address(self, public_management_connect_address):
        """Sets the public_management_connect_address of this ShowInstanceResp.

        公网访问Kafka Manager连接地址。

        :param public_management_connect_address: The public_management_connect_address of this ShowInstanceResp.
        :type public_management_connect_address: str
        """
        self._public_management_connect_address = public_management_connect_address

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
    def enable_auto_topic(self):
        """Gets the enable_auto_topic of this ShowInstanceResp.

        是否打开kafka自动创建topic功能。   - true：开启   - false：关闭

        :return: The enable_auto_topic of this ShowInstanceResp.
        :rtype: bool
        """
        return self._enable_auto_topic

    @enable_auto_topic.setter
    def enable_auto_topic(self, enable_auto_topic):
        """Sets the enable_auto_topic of this ShowInstanceResp.

        是否打开kafka自动创建topic功能。   - true：开启   - false：关闭

        :param enable_auto_topic: The enable_auto_topic of this ShowInstanceResp.
        :type enable_auto_topic: bool
        """
        self._enable_auto_topic = enable_auto_topic

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
    def public_connect_address(self):
        """Gets the public_connect_address of this ShowInstanceResp.

        实例公网连接IP地址。当实例开启了公网访问，实例才包含该参数。

        :return: The public_connect_address of this ShowInstanceResp.
        :rtype: str
        """
        return self._public_connect_address

    @public_connect_address.setter
    def public_connect_address(self, public_connect_address):
        """Sets the public_connect_address of this ShowInstanceResp.

        实例公网连接IP地址。当实例开启了公网访问，实例才包含该参数。

        :param public_connect_address: The public_connect_address of this ShowInstanceResp.
        :type public_connect_address: str
        """
        self._public_connect_address = public_connect_address

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
    def service_type(self):
        """Gets the service_type of this ShowInstanceResp.

        服务类型。

        :return: The service_type of this ShowInstanceResp.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this ShowInstanceResp.

        服务类型。

        :param service_type: The service_type of this ShowInstanceResp.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def storage_type(self):
        """Gets the storage_type of this ShowInstanceResp.

        存储类型。

        :return: The storage_type of this ShowInstanceResp.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this ShowInstanceResp.

        存储类型。

        :param storage_type: The storage_type of this ShowInstanceResp.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def retention_policy(self):
        """Gets the retention_policy of this ShowInstanceResp.

        消息老化策略。

        :return: The retention_policy of this ShowInstanceResp.
        :rtype: str
        """
        return self._retention_policy

    @retention_policy.setter
    def retention_policy(self, retention_policy):
        """Sets the retention_policy of this ShowInstanceResp.

        消息老化策略。

        :param retention_policy: The retention_policy of this ShowInstanceResp.
        :type retention_policy: str
        """
        self._retention_policy = retention_policy

    @property
    def kafka_public_status(self):
        """Gets the kafka_public_status of this ShowInstanceResp.

        Kafka公网开启状态。

        :return: The kafka_public_status of this ShowInstanceResp.
        :rtype: str
        """
        return self._kafka_public_status

    @kafka_public_status.setter
    def kafka_public_status(self, kafka_public_status):
        """Sets the kafka_public_status of this ShowInstanceResp.

        Kafka公网开启状态。

        :param kafka_public_status: The kafka_public_status of this ShowInstanceResp.
        :type kafka_public_status: str
        """
        self._kafka_public_status = kafka_public_status

    @property
    def public_bandwidth(self):
        """Gets the public_bandwidth of this ShowInstanceResp.

        kafka公网访问带宽。

        :return: The public_bandwidth of this ShowInstanceResp.
        :rtype: int
        """
        return self._public_bandwidth

    @public_bandwidth.setter
    def public_bandwidth(self, public_bandwidth):
        """Sets the public_bandwidth of this ShowInstanceResp.

        kafka公网访问带宽。

        :param public_bandwidth: The public_bandwidth of this ShowInstanceResp.
        :type public_bandwidth: int
        """
        self._public_bandwidth = public_bandwidth

    @property
    def kafka_manager_user(self):
        """Gets the kafka_manager_user of this ShowInstanceResp.

        登录Kafka Manager的用户名。

        :return: The kafka_manager_user of this ShowInstanceResp.
        :rtype: str
        """
        return self._kafka_manager_user

    @kafka_manager_user.setter
    def kafka_manager_user(self, kafka_manager_user):
        """Sets the kafka_manager_user of this ShowInstanceResp.

        登录Kafka Manager的用户名。

        :param kafka_manager_user: The kafka_manager_user of this ShowInstanceResp.
        :type kafka_manager_user: str
        """
        self._kafka_manager_user = kafka_manager_user

    @property
    def enable_log_collection(self):
        """Gets the enable_log_collection of this ShowInstanceResp.

        是否开启消息收集功能。

        :return: The enable_log_collection of this ShowInstanceResp.
        :rtype: bool
        """
        return self._enable_log_collection

    @enable_log_collection.setter
    def enable_log_collection(self, enable_log_collection):
        """Sets the enable_log_collection of this ShowInstanceResp.

        是否开启消息收集功能。

        :param enable_log_collection: The enable_log_collection of this ShowInstanceResp.
        :type enable_log_collection: bool
        """
        self._enable_log_collection = enable_log_collection

    @property
    def cross_vpc_info(self):
        """Gets the cross_vpc_info of this ShowInstanceResp.

        跨VPC访问信息。

        :return: The cross_vpc_info of this ShowInstanceResp.
        :rtype: str
        """
        return self._cross_vpc_info

    @cross_vpc_info.setter
    def cross_vpc_info(self, cross_vpc_info):
        """Sets the cross_vpc_info of this ShowInstanceResp.

        跨VPC访问信息。

        :param cross_vpc_info: The cross_vpc_info of this ShowInstanceResp.
        :type cross_vpc_info: str
        """
        self._cross_vpc_info = cross_vpc_info

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
    def connector_enable(self):
        """Gets the connector_enable of this ShowInstanceResp.

        是否开启转储。新规格产品暂不支持开启转储。

        :return: The connector_enable of this ShowInstanceResp.
        :rtype: bool
        """
        return self._connector_enable

    @connector_enable.setter
    def connector_enable(self, connector_enable):
        """Sets the connector_enable of this ShowInstanceResp.

        是否开启转储。新规格产品暂不支持开启转储。

        :param connector_enable: The connector_enable of this ShowInstanceResp.
        :type connector_enable: bool
        """
        self._connector_enable = connector_enable

    @property
    def connector_id(self):
        """Gets the connector_id of this ShowInstanceResp.

        转储任务ID。

        :return: The connector_id of this ShowInstanceResp.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this ShowInstanceResp.

        转储任务ID。

        :param connector_id: The connector_id of this ShowInstanceResp.
        :type connector_id: str
        """
        self._connector_id = connector_id

    @property
    def rest_enable(self):
        """Gets the rest_enable of this ShowInstanceResp.

        是否开启Kafka rest功能。

        :return: The rest_enable of this ShowInstanceResp.
        :rtype: bool
        """
        return self._rest_enable

    @rest_enable.setter
    def rest_enable(self, rest_enable):
        """Sets the rest_enable of this ShowInstanceResp.

        是否开启Kafka rest功能。

        :param rest_enable: The rest_enable of this ShowInstanceResp.
        :type rest_enable: bool
        """
        self._rest_enable = rest_enable

    @property
    def rest_connect_address(self):
        """Gets the rest_connect_address of this ShowInstanceResp.

        Kafka rest连接地址。

        :return: The rest_connect_address of this ShowInstanceResp.
        :rtype: str
        """
        return self._rest_connect_address

    @rest_connect_address.setter
    def rest_connect_address(self, rest_connect_address):
        """Sets the rest_connect_address of this ShowInstanceResp.

        Kafka rest连接地址。

        :param rest_connect_address: The rest_connect_address of this ShowInstanceResp.
        :type rest_connect_address: str
        """
        self._rest_connect_address = rest_connect_address

    @property
    def public_boundwidth(self):
        """Gets the public_boundwidth of this ShowInstanceResp.

        kafka公网访问带宽。待删除版本。

        :return: The public_boundwidth of this ShowInstanceResp.
        :rtype: int
        """
        return self._public_boundwidth

    @public_boundwidth.setter
    def public_boundwidth(self, public_boundwidth):
        """Sets the public_boundwidth of this ShowInstanceResp.

        kafka公网访问带宽。待删除版本。

        :param public_boundwidth: The public_boundwidth of this ShowInstanceResp.
        :type public_boundwidth: int
        """
        self._public_boundwidth = public_boundwidth

    @property
    def message_query_inst_enable(self):
        """Gets the message_query_inst_enable of this ShowInstanceResp.

        是否开启消息查询功能。

        :return: The message_query_inst_enable of this ShowInstanceResp.
        :rtype: bool
        """
        return self._message_query_inst_enable

    @message_query_inst_enable.setter
    def message_query_inst_enable(self, message_query_inst_enable):
        """Sets the message_query_inst_enable of this ShowInstanceResp.

        是否开启消息查询功能。

        :param message_query_inst_enable: The message_query_inst_enable of this ShowInstanceResp.
        :type message_query_inst_enable: bool
        """
        self._message_query_inst_enable = message_query_inst_enable

    @property
    def vpc_client_plain(self):
        """Gets the vpc_client_plain of this ShowInstanceResp.

        是否开启VPC明文访问。

        :return: The vpc_client_plain of this ShowInstanceResp.
        :rtype: bool
        """
        return self._vpc_client_plain

    @vpc_client_plain.setter
    def vpc_client_plain(self, vpc_client_plain):
        """Sets the vpc_client_plain of this ShowInstanceResp.

        是否开启VPC明文访问。

        :param vpc_client_plain: The vpc_client_plain of this ShowInstanceResp.
        :type vpc_client_plain: bool
        """
        self._vpc_client_plain = vpc_client_plain

    @property
    def support_features(self):
        """Gets the support_features of this ShowInstanceResp.

        Kafka实例支持的特性功能。

        :return: The support_features of this ShowInstanceResp.
        :rtype: str
        """
        return self._support_features

    @support_features.setter
    def support_features(self, support_features):
        """Sets the support_features of this ShowInstanceResp.

        Kafka实例支持的特性功能。

        :param support_features: The support_features of this ShowInstanceResp.
        :type support_features: str
        """
        self._support_features = support_features

    @property
    def trace_enable(self):
        """Gets the trace_enable of this ShowInstanceResp.

        是否开启消息轨迹功能。

        :return: The trace_enable of this ShowInstanceResp.
        :rtype: bool
        """
        return self._trace_enable

    @trace_enable.setter
    def trace_enable(self, trace_enable):
        """Sets the trace_enable of this ShowInstanceResp.

        是否开启消息轨迹功能。

        :param trace_enable: The trace_enable of this ShowInstanceResp.
        :type trace_enable: bool
        """
        self._trace_enable = trace_enable

    @property
    def agent_enable(self):
        """Gets the agent_enable of this ShowInstanceResp.

        是否开启代理。

        :return: The agent_enable of this ShowInstanceResp.
        :rtype: bool
        """
        return self._agent_enable

    @agent_enable.setter
    def agent_enable(self, agent_enable):
        """Sets the agent_enable of this ShowInstanceResp.

        是否开启代理。

        :param agent_enable: The agent_enable of this ShowInstanceResp.
        :type agent_enable: bool
        """
        self._agent_enable = agent_enable

    @property
    def pod_connect_address(self):
        """Gets the pod_connect_address of this ShowInstanceResp.

        租户侧连接地址。

        :return: The pod_connect_address of this ShowInstanceResp.
        :rtype: str
        """
        return self._pod_connect_address

    @pod_connect_address.setter
    def pod_connect_address(self, pod_connect_address):
        """Sets the pod_connect_address of this ShowInstanceResp.

        租户侧连接地址。

        :param pod_connect_address: The pod_connect_address of this ShowInstanceResp.
        :type pod_connect_address: str
        """
        self._pod_connect_address = pod_connect_address

    @property
    def disk_encrypted(self):
        """Gets the disk_encrypted of this ShowInstanceResp.

        是否开启磁盘加密。

        :return: The disk_encrypted of this ShowInstanceResp.
        :rtype: bool
        """
        return self._disk_encrypted

    @disk_encrypted.setter
    def disk_encrypted(self, disk_encrypted):
        """Sets the disk_encrypted of this ShowInstanceResp.

        是否开启磁盘加密。

        :param disk_encrypted: The disk_encrypted of this ShowInstanceResp.
        :type disk_encrypted: bool
        """
        self._disk_encrypted = disk_encrypted

    @property
    def disk_encrypted_key(self):
        """Gets the disk_encrypted_key of this ShowInstanceResp.

        磁盘加密key，未开启磁盘加密时为空。

        :return: The disk_encrypted_key of this ShowInstanceResp.
        :rtype: str
        """
        return self._disk_encrypted_key

    @disk_encrypted_key.setter
    def disk_encrypted_key(self, disk_encrypted_key):
        """Sets the disk_encrypted_key of this ShowInstanceResp.

        磁盘加密key，未开启磁盘加密时为空。

        :param disk_encrypted_key: The disk_encrypted_key of this ShowInstanceResp.
        :type disk_encrypted_key: str
        """
        self._disk_encrypted_key = disk_encrypted_key

    @property
    def kafka_private_connect_address(self):
        """Gets the kafka_private_connect_address of this ShowInstanceResp.

        Kafka实例私有连接地址。

        :return: The kafka_private_connect_address of this ShowInstanceResp.
        :rtype: str
        """
        return self._kafka_private_connect_address

    @kafka_private_connect_address.setter
    def kafka_private_connect_address(self, kafka_private_connect_address):
        """Sets the kafka_private_connect_address of this ShowInstanceResp.

        Kafka实例私有连接地址。

        :param kafka_private_connect_address: The kafka_private_connect_address of this ShowInstanceResp.
        :type kafka_private_connect_address: str
        """
        self._kafka_private_connect_address = kafka_private_connect_address

    @property
    def ces_version(self):
        """Gets the ces_version of this ShowInstanceResp.

        云监控版本。

        :return: The ces_version of this ShowInstanceResp.
        :rtype: str
        """
        return self._ces_version

    @ces_version.setter
    def ces_version(self, ces_version):
        """Sets the ces_version of this ShowInstanceResp.

        云监控版本。

        :param ces_version: The ces_version of this ShowInstanceResp.
        :type ces_version: str
        """
        self._ces_version = ces_version

    @property
    def public_access_enabled(self):
        """Gets the public_access_enabled of this ShowInstanceResp.

        区分实例什么时候开启的公网访问：true,actived,closed,false。

        :return: The public_access_enabled of this ShowInstanceResp.
        :rtype: str
        """
        return self._public_access_enabled

    @public_access_enabled.setter
    def public_access_enabled(self, public_access_enabled):
        """Sets the public_access_enabled of this ShowInstanceResp.

        区分实例什么时候开启的公网访问：true,actived,closed,false。

        :param public_access_enabled: The public_access_enabled of this ShowInstanceResp.
        :type public_access_enabled: str
        """
        self._public_access_enabled = public_access_enabled

    @property
    def node_num(self):
        """Gets the node_num of this ShowInstanceResp.

        节点数。

        :return: The node_num of this ShowInstanceResp.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this ShowInstanceResp.

        节点数。

        :param node_num: The node_num of this ShowInstanceResp.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def enable_acl(self):
        """Gets the enable_acl of this ShowInstanceResp.

        是否开启访问控制。

        :return: The enable_acl of this ShowInstanceResp.
        :rtype: bool
        """
        return self._enable_acl

    @enable_acl.setter
    def enable_acl(self, enable_acl):
        """Sets the enable_acl of this ShowInstanceResp.

        是否开启访问控制。

        :param enable_acl: The enable_acl of this ShowInstanceResp.
        :type enable_acl: bool
        """
        self._enable_acl = enable_acl

    @property
    def new_spec_billing_enable(self):
        """Gets the new_spec_billing_enable of this ShowInstanceResp.

        是否启用新规格计费。

        :return: The new_spec_billing_enable of this ShowInstanceResp.
        :rtype: bool
        """
        return self._new_spec_billing_enable

    @new_spec_billing_enable.setter
    def new_spec_billing_enable(self, new_spec_billing_enable):
        """Sets the new_spec_billing_enable of this ShowInstanceResp.

        是否启用新规格计费。

        :param new_spec_billing_enable: The new_spec_billing_enable of this ShowInstanceResp.
        :type new_spec_billing_enable: bool
        """
        self._new_spec_billing_enable = new_spec_billing_enable

    @property
    def broker_num(self):
        """Gets the broker_num of this ShowInstanceResp.

        节点数量。

        :return: The broker_num of this ShowInstanceResp.
        :rtype: int
        """
        return self._broker_num

    @broker_num.setter
    def broker_num(self, broker_num):
        """Sets the broker_num of this ShowInstanceResp.

        节点数量。

        :param broker_num: The broker_num of this ShowInstanceResp.
        :type broker_num: int
        """
        self._broker_num = broker_num

    @property
    def tags(self):
        """Gets the tags of this ShowInstanceResp.

        标签列表。

        :return: The tags of this ShowInstanceResp.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.TagEntity`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowInstanceResp.

        标签列表。

        :param tags: The tags of this ShowInstanceResp.
        :type tags: list[:class:`huaweicloudsdkkafka.v2.TagEntity`]
        """
        self._tags = tags

    @property
    def dr_enable(self):
        """Gets the dr_enable of this ShowInstanceResp.

        是否为容灾实例。

        :return: The dr_enable of this ShowInstanceResp.
        :rtype: bool
        """
        return self._dr_enable

    @dr_enable.setter
    def dr_enable(self, dr_enable):
        """Sets the dr_enable of this ShowInstanceResp.

        是否为容灾实例。

        :param dr_enable: The dr_enable of this ShowInstanceResp.
        :type dr_enable: bool
        """
        self._dr_enable = dr_enable

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
