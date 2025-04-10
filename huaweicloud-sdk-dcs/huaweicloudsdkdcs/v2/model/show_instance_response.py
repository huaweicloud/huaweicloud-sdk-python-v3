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
        'vpc_name': 'str',
        'charging_mode': 'int',
        'vpc_id': 'str',
        'user_name': 'str',
        'created_at': 'str',
        'description': 'str',
        'security_group_id': 'str',
        'security_group_name': 'str',
        'max_memory': 'int',
        'used_memory': 'int',
        'capacity': 'int',
        'capacity_minor': 'str',
        'maintain_begin': 'str',
        'maintain_end': 'str',
        'engine': 'str',
        'no_password_access': 'str',
        'ip': 'str',
        'instance_backup_policy': 'InstanceBackupPolicy',
        'az_codes': 'list[str]',
        'available_zones': 'list[str]',
        'access_user': 'str',
        'instance_id': 'str',
        'port': 'int',
        'user_id': 'str',
        'name': 'str',
        'spec_code': 'str',
        'subnet_id': 'str',
        'subnet_name': 'str',
        'subnet_cidr': 'str',
        'engine_version': 'str',
        'order_id': 'str',
        'status': 'str',
        'domain_name': 'str',
        'readonly_domain_name': 'str',
        'enable_publicip': 'bool',
        'publicip_id': 'str',
        'publicip_address': 'str',
        'enable_ssl': 'bool',
        'service_upgrade': 'bool',
        'service_task_id': 'str',
        'enterprise_project_id': 'str',
        'backend_addrs': 'str',
        'features': 'Features',
        'domain_name_info': 'DomainNameInfo',
        'transparent_client_ip_enable': 'bool',
        'sub_status': 'str',
        'tags': 'list[ResourceTag]',
        'cpu_type': 'str',
        'enterprise_project_name': 'str',
        'update_at': 'str',
        'product_type': 'str',
        'storage_type': 'str',
        'launched_at': 'str',
        'cache_mode': 'str',
        'support_slow_log_flag': 'str',
        'db_number': 'int',
        'replica_count': 'int',
        'sharding_count': 'int',
        'bandwidth_info': 'BandwidthInfo',
        'cloud_service_type_code': 'str',
        'cloud_resource_type_code': 'str',
        'inquery_spec_code': 'str'
    }

    attribute_map = {
        'vpc_name': 'vpc_name',
        'charging_mode': 'charging_mode',
        'vpc_id': 'vpc_id',
        'user_name': 'user_name',
        'created_at': 'created_at',
        'description': 'description',
        'security_group_id': 'security_group_id',
        'security_group_name': 'security_group_name',
        'max_memory': 'max_memory',
        'used_memory': 'used_memory',
        'capacity': 'capacity',
        'capacity_minor': 'capacity_minor',
        'maintain_begin': 'maintain_begin',
        'maintain_end': 'maintain_end',
        'engine': 'engine',
        'no_password_access': 'no_password_access',
        'ip': 'ip',
        'instance_backup_policy': 'instance_backup_policy',
        'az_codes': 'az_codes',
        'available_zones': 'available_zones',
        'access_user': 'access_user',
        'instance_id': 'instance_id',
        'port': 'port',
        'user_id': 'user_id',
        'name': 'name',
        'spec_code': 'spec_code',
        'subnet_id': 'subnet_id',
        'subnet_name': 'subnet_name',
        'subnet_cidr': 'subnet_cidr',
        'engine_version': 'engine_version',
        'order_id': 'order_id',
        'status': 'status',
        'domain_name': 'domain_name',
        'readonly_domain_name': 'readonly_domain_name',
        'enable_publicip': 'enable_publicip',
        'publicip_id': 'publicip_id',
        'publicip_address': 'publicip_address',
        'enable_ssl': 'enable_ssl',
        'service_upgrade': 'service_upgrade',
        'service_task_id': 'service_task_id',
        'enterprise_project_id': 'enterprise_project_id',
        'backend_addrs': 'backend_addrs',
        'features': 'features',
        'domain_name_info': 'domain_name_info',
        'transparent_client_ip_enable': 'transparent_client_ip_enable',
        'sub_status': 'sub_status',
        'tags': 'tags',
        'cpu_type': 'cpu_type',
        'enterprise_project_name': 'enterprise_project_name',
        'update_at': 'update_at',
        'product_type': 'product_type',
        'storage_type': 'storage_type',
        'launched_at': 'launched_at',
        'cache_mode': 'cache_mode',
        'support_slow_log_flag': 'support_slow_log_flag',
        'db_number': 'db_number',
        'replica_count': 'replica_count',
        'sharding_count': 'sharding_count',
        'bandwidth_info': 'bandwidth_info',
        'cloud_service_type_code': 'cloud_service_type_code',
        'cloud_resource_type_code': 'cloud_resource_type_code',
        'inquery_spec_code': 'inquery_spec_code'
    }

    def __init__(self, vpc_name=None, charging_mode=None, vpc_id=None, user_name=None, created_at=None, description=None, security_group_id=None, security_group_name=None, max_memory=None, used_memory=None, capacity=None, capacity_minor=None, maintain_begin=None, maintain_end=None, engine=None, no_password_access=None, ip=None, instance_backup_policy=None, az_codes=None, available_zones=None, access_user=None, instance_id=None, port=None, user_id=None, name=None, spec_code=None, subnet_id=None, subnet_name=None, subnet_cidr=None, engine_version=None, order_id=None, status=None, domain_name=None, readonly_domain_name=None, enable_publicip=None, publicip_id=None, publicip_address=None, enable_ssl=None, service_upgrade=None, service_task_id=None, enterprise_project_id=None, backend_addrs=None, features=None, domain_name_info=None, transparent_client_ip_enable=None, sub_status=None, tags=None, cpu_type=None, enterprise_project_name=None, update_at=None, product_type=None, storage_type=None, launched_at=None, cache_mode=None, support_slow_log_flag=None, db_number=None, replica_count=None, sharding_count=None, bandwidth_info=None, cloud_service_type_code=None, cloud_resource_type_code=None, inquery_spec_code=None):
        r"""ShowInstanceResponse

        The model defined in huaweicloud sdk

        :param vpc_name: VPC的名称。
        :type vpc_name: str
        :param charging_mode: 付费模式，0表示按需计费，1表示包年/包月计费。
        :type charging_mode: int
        :param vpc_id: VPC ID
        :type vpc_id: str
        :param user_name: 用户名。
        :type user_name: str
        :param created_at: 完成创建时间。格式为：2017-03-31T12:24:46.297Z
        :type created_at: str
        :param description: 实例描述。
        :type description: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param security_group_name: 租户安全组名称。
        :type security_group_name: str
        :param max_memory: 总内存，单位：MB。
        :type max_memory: int
        :param used_memory: 已使用的内存，单位：MB。
        :type used_memory: int
        :param capacity: 缓存实例的容量（G Byte）。
        :type capacity: int
        :param capacity_minor: 单机小规格的缓存容量。
        :type capacity_minor: str
        :param maintain_begin: 维护时间窗开始时间，为UTC时间，格式为HH:mm:ss
        :type maintain_begin: str
        :param maintain_end: 维护时间窗结束时间，为UTC时间，格式为HH:mm:ss
        :type maintain_end: str
        :param engine: 缓存实例的引擎类型。
        :type engine: str
        :param no_password_access: 是否允许免密码访问缓存实例。 - true：该实例无需密码即可访问。 - false：该实例必须通过密码认证才能访问。 
        :type no_password_access: str
        :param ip: 连接缓存实例的IP地址。如果是集群实例，返回多个IP地址，使用逗号分隔。如：192.168.0.1，192.168.0.2。
        :type ip: str
        :param instance_backup_policy: 
        :type instance_backup_policy: :class:`huaweicloudsdkdcs.v2.InstanceBackupPolicy`
        :param az_codes: 实例所在的可用区。返回“可用区Code”
        :type az_codes: list[str]
        :param available_zones: 实例所在的可用区id。返回\&quot;可用区ID\&quot;
        :type available_zones: list[str]
        :param access_user: 通过密码认证访问缓存实例的认证用户名。
        :type access_user: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param port: 缓存的端口。
        :type port: int
        :param user_id: 用户id。
        :type user_id: str
        :param name: 实例名称。
        :type name: str
        :param spec_code: 产品规格编码
        :type spec_code: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param subnet_name: 子网名称。
        :type subnet_name: str
        :param subnet_cidr: 子网网段。
        :type subnet_cidr: str
        :param engine_version: 缓存版本。
        :type engine_version: str
        :param order_id: 订单ID。
        :type order_id: str
        :param status: 缓存实例的状态。详细状态说明见[缓存实例状态说明](https://support.huaweicloud.com/api-dcs/dcs-api-0312047.html)
        :type status: str
        :param domain_name: 实例的域名。
        :type domain_name: str
        :param readonly_domain_name: 实例的只读域名，只有主备实例有该字段。
        :type readonly_domain_name: str
        :param enable_publicip: Redis缓存实例是否开启公网访问功能。 - true：开启 - false：不开启 
        :type enable_publicip: bool
        :param publicip_id: Redis缓存实例绑定的弹性IP地址的id。 如果未开启公网访问功能，该字段值为null。 
        :type publicip_id: str
        :param publicip_address: Redis缓存实例绑定的弹性IP地址。 如果未开启公网访问功能，该字段值为null。 
        :type publicip_address: str
        :param enable_ssl: Redis缓存实例开启公网访问功能时，是否选择支持ssl。 - true：开启 - false：不开启 
        :type enable_ssl: bool
        :param service_upgrade: 实例是否存在升级任务。 - true：存在 - false：不存在 
        :type service_upgrade: bool
        :param service_task_id: 升级任务的ID。 - 当service_upgrade为true时，为升级任务的ID。 - 当service_upgrade为false时，该参数为空。 
        :type service_task_id: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param backend_addrs: 集群实例的后端服务地址。
        :type backend_addrs: str
        :param features: 
        :type features: :class:`huaweicloudsdkdcs.v2.Features`
        :param domain_name_info: 
        :type domain_name_info: :class:`huaweicloudsdkdcs.v2.DomainNameInfo`
        :param transparent_client_ip_enable: 是否开启客户端ip透传。
        :type transparent_client_ip_enable: bool
        :param sub_status: 实例子状态。
        :type sub_status: str
        :param tags: 实例标签键值。
        :type tags: list[:class:`huaweicloudsdkdcs.v2.ResourceTag`]
        :param cpu_type: 实例CPU类型，通常为x86_64或aarch64
        :type cpu_type: str
        :param enterprise_project_name: 企业项目名称。
        :type enterprise_project_name: str
        :param update_at: 更新时间，形如2022-07-06T09:32:16.502Z
        :type update_at: str
        :param product_type: 版本类型：社区版、企业版
        :type product_type: str
        :param storage_type: 存储类型：内存存储
        :type storage_type: str
        :param launched_at: 启动时间，形如2022-07-06T09:32:16.502Z
        :type launched_at: str
        :param cache_mode: 缓存类型：单机类型，主备类型，主备读写分离，Proxy集群类型，原生集群类型
        :type cache_mode: str
        :param support_slow_log_flag: 是否支持慢日志
        :type support_slow_log_flag: str
        :param db_number: 数据库数量
        :type db_number: int
        :param replica_count: 副本数
        :type replica_count: int
        :param sharding_count: 集群实例分片个数
        :type sharding_count: int
        :param bandwidth_info: 
        :type bandwidth_info: :class:`huaweicloudsdkdcs.v2.BandwidthInfo`
        :param cloud_service_type_code: 云服务类型编码。
        :type cloud_service_type_code: str
        :param cloud_resource_type_code: 云资源类型编码。
        :type cloud_resource_type_code: str
        :param inquery_spec_code: 运营系统中的规格编码
        :type inquery_spec_code: str
        """
        
        super(ShowInstanceResponse, self).__init__()

        self._vpc_name = None
        self._charging_mode = None
        self._vpc_id = None
        self._user_name = None
        self._created_at = None
        self._description = None
        self._security_group_id = None
        self._security_group_name = None
        self._max_memory = None
        self._used_memory = None
        self._capacity = None
        self._capacity_minor = None
        self._maintain_begin = None
        self._maintain_end = None
        self._engine = None
        self._no_password_access = None
        self._ip = None
        self._instance_backup_policy = None
        self._az_codes = None
        self._available_zones = None
        self._access_user = None
        self._instance_id = None
        self._port = None
        self._user_id = None
        self._name = None
        self._spec_code = None
        self._subnet_id = None
        self._subnet_name = None
        self._subnet_cidr = None
        self._engine_version = None
        self._order_id = None
        self._status = None
        self._domain_name = None
        self._readonly_domain_name = None
        self._enable_publicip = None
        self._publicip_id = None
        self._publicip_address = None
        self._enable_ssl = None
        self._service_upgrade = None
        self._service_task_id = None
        self._enterprise_project_id = None
        self._backend_addrs = None
        self._features = None
        self._domain_name_info = None
        self._transparent_client_ip_enable = None
        self._sub_status = None
        self._tags = None
        self._cpu_type = None
        self._enterprise_project_name = None
        self._update_at = None
        self._product_type = None
        self._storage_type = None
        self._launched_at = None
        self._cache_mode = None
        self._support_slow_log_flag = None
        self._db_number = None
        self._replica_count = None
        self._sharding_count = None
        self._bandwidth_info = None
        self._cloud_service_type_code = None
        self._cloud_resource_type_code = None
        self._inquery_spec_code = None
        self.discriminator = None

        if vpc_name is not None:
            self.vpc_name = vpc_name
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if user_name is not None:
            self.user_name = user_name
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if security_group_name is not None:
            self.security_group_name = security_group_name
        if max_memory is not None:
            self.max_memory = max_memory
        if used_memory is not None:
            self.used_memory = used_memory
        if capacity is not None:
            self.capacity = capacity
        if capacity_minor is not None:
            self.capacity_minor = capacity_minor
        if maintain_begin is not None:
            self.maintain_begin = maintain_begin
        if maintain_end is not None:
            self.maintain_end = maintain_end
        if engine is not None:
            self.engine = engine
        if no_password_access is not None:
            self.no_password_access = no_password_access
        if ip is not None:
            self.ip = ip
        if instance_backup_policy is not None:
            self.instance_backup_policy = instance_backup_policy
        if az_codes is not None:
            self.az_codes = az_codes
        if available_zones is not None:
            self.available_zones = available_zones
        if access_user is not None:
            self.access_user = access_user
        if instance_id is not None:
            self.instance_id = instance_id
        if port is not None:
            self.port = port
        if user_id is not None:
            self.user_id = user_id
        if name is not None:
            self.name = name
        if spec_code is not None:
            self.spec_code = spec_code
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if subnet_cidr is not None:
            self.subnet_cidr = subnet_cidr
        if engine_version is not None:
            self.engine_version = engine_version
        if order_id is not None:
            self.order_id = order_id
        if status is not None:
            self.status = status
        if domain_name is not None:
            self.domain_name = domain_name
        if readonly_domain_name is not None:
            self.readonly_domain_name = readonly_domain_name
        if enable_publicip is not None:
            self.enable_publicip = enable_publicip
        if publicip_id is not None:
            self.publicip_id = publicip_id
        if publicip_address is not None:
            self.publicip_address = publicip_address
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl
        if service_upgrade is not None:
            self.service_upgrade = service_upgrade
        if service_task_id is not None:
            self.service_task_id = service_task_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if backend_addrs is not None:
            self.backend_addrs = backend_addrs
        if features is not None:
            self.features = features
        if domain_name_info is not None:
            self.domain_name_info = domain_name_info
        if transparent_client_ip_enable is not None:
            self.transparent_client_ip_enable = transparent_client_ip_enable
        if sub_status is not None:
            self.sub_status = sub_status
        if tags is not None:
            self.tags = tags
        if cpu_type is not None:
            self.cpu_type = cpu_type
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if update_at is not None:
            self.update_at = update_at
        if product_type is not None:
            self.product_type = product_type
        if storage_type is not None:
            self.storage_type = storage_type
        if launched_at is not None:
            self.launched_at = launched_at
        if cache_mode is not None:
            self.cache_mode = cache_mode
        if support_slow_log_flag is not None:
            self.support_slow_log_flag = support_slow_log_flag
        if db_number is not None:
            self.db_number = db_number
        if replica_count is not None:
            self.replica_count = replica_count
        if sharding_count is not None:
            self.sharding_count = sharding_count
        if bandwidth_info is not None:
            self.bandwidth_info = bandwidth_info
        if cloud_service_type_code is not None:
            self.cloud_service_type_code = cloud_service_type_code
        if cloud_resource_type_code is not None:
            self.cloud_resource_type_code = cloud_resource_type_code
        if inquery_spec_code is not None:
            self.inquery_spec_code = inquery_spec_code

    @property
    def vpc_name(self):
        r"""Gets the vpc_name of this ShowInstanceResponse.

        VPC的名称。

        :return: The vpc_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        r"""Sets the vpc_name of this ShowInstanceResponse.

        VPC的名称。

        :param vpc_name: The vpc_name of this ShowInstanceResponse.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ShowInstanceResponse.

        付费模式，0表示按需计费，1表示包年/包月计费。

        :return: The charging_mode of this ShowInstanceResponse.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ShowInstanceResponse.

        付费模式，0表示按需计费，1表示包年/包月计费。

        :param charging_mode: The charging_mode of this ShowInstanceResponse.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ShowInstanceResponse.

        VPC ID

        :return: The vpc_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ShowInstanceResponse.

        VPC ID

        :param vpc_id: The vpc_id of this ShowInstanceResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ShowInstanceResponse.

        用户名。

        :return: The user_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ShowInstanceResponse.

        用户名。

        :param user_name: The user_name of this ShowInstanceResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowInstanceResponse.

        完成创建时间。格式为：2017-03-31T12:24:46.297Z

        :return: The created_at of this ShowInstanceResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowInstanceResponse.

        完成创建时间。格式为：2017-03-31T12:24:46.297Z

        :param created_at: The created_at of this ShowInstanceResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def description(self):
        r"""Gets the description of this ShowInstanceResponse.

        实例描述。

        :return: The description of this ShowInstanceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowInstanceResponse.

        实例描述。

        :param description: The description of this ShowInstanceResponse.
        :type description: str
        """
        self._description = description

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this ShowInstanceResponse.

        安全组ID。

        :return: The security_group_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this ShowInstanceResponse.

        安全组ID。

        :param security_group_id: The security_group_id of this ShowInstanceResponse.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def security_group_name(self):
        r"""Gets the security_group_name of this ShowInstanceResponse.

        租户安全组名称。

        :return: The security_group_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._security_group_name

    @security_group_name.setter
    def security_group_name(self, security_group_name):
        r"""Sets the security_group_name of this ShowInstanceResponse.

        租户安全组名称。

        :param security_group_name: The security_group_name of this ShowInstanceResponse.
        :type security_group_name: str
        """
        self._security_group_name = security_group_name

    @property
    def max_memory(self):
        r"""Gets the max_memory of this ShowInstanceResponse.

        总内存，单位：MB。

        :return: The max_memory of this ShowInstanceResponse.
        :rtype: int
        """
        return self._max_memory

    @max_memory.setter
    def max_memory(self, max_memory):
        r"""Sets the max_memory of this ShowInstanceResponse.

        总内存，单位：MB。

        :param max_memory: The max_memory of this ShowInstanceResponse.
        :type max_memory: int
        """
        self._max_memory = max_memory

    @property
    def used_memory(self):
        r"""Gets the used_memory of this ShowInstanceResponse.

        已使用的内存，单位：MB。

        :return: The used_memory of this ShowInstanceResponse.
        :rtype: int
        """
        return self._used_memory

    @used_memory.setter
    def used_memory(self, used_memory):
        r"""Sets the used_memory of this ShowInstanceResponse.

        已使用的内存，单位：MB。

        :param used_memory: The used_memory of this ShowInstanceResponse.
        :type used_memory: int
        """
        self._used_memory = used_memory

    @property
    def capacity(self):
        r"""Gets the capacity of this ShowInstanceResponse.

        缓存实例的容量（G Byte）。

        :return: The capacity of this ShowInstanceResponse.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this ShowInstanceResponse.

        缓存实例的容量（G Byte）。

        :param capacity: The capacity of this ShowInstanceResponse.
        :type capacity: int
        """
        self._capacity = capacity

    @property
    def capacity_minor(self):
        r"""Gets the capacity_minor of this ShowInstanceResponse.

        单机小规格的缓存容量。

        :return: The capacity_minor of this ShowInstanceResponse.
        :rtype: str
        """
        return self._capacity_minor

    @capacity_minor.setter
    def capacity_minor(self, capacity_minor):
        r"""Sets the capacity_minor of this ShowInstanceResponse.

        单机小规格的缓存容量。

        :param capacity_minor: The capacity_minor of this ShowInstanceResponse.
        :type capacity_minor: str
        """
        self._capacity_minor = capacity_minor

    @property
    def maintain_begin(self):
        r"""Gets the maintain_begin of this ShowInstanceResponse.

        维护时间窗开始时间，为UTC时间，格式为HH:mm:ss

        :return: The maintain_begin of this ShowInstanceResponse.
        :rtype: str
        """
        return self._maintain_begin

    @maintain_begin.setter
    def maintain_begin(self, maintain_begin):
        r"""Sets the maintain_begin of this ShowInstanceResponse.

        维护时间窗开始时间，为UTC时间，格式为HH:mm:ss

        :param maintain_begin: The maintain_begin of this ShowInstanceResponse.
        :type maintain_begin: str
        """
        self._maintain_begin = maintain_begin

    @property
    def maintain_end(self):
        r"""Gets the maintain_end of this ShowInstanceResponse.

        维护时间窗结束时间，为UTC时间，格式为HH:mm:ss

        :return: The maintain_end of this ShowInstanceResponse.
        :rtype: str
        """
        return self._maintain_end

    @maintain_end.setter
    def maintain_end(self, maintain_end):
        r"""Sets the maintain_end of this ShowInstanceResponse.

        维护时间窗结束时间，为UTC时间，格式为HH:mm:ss

        :param maintain_end: The maintain_end of this ShowInstanceResponse.
        :type maintain_end: str
        """
        self._maintain_end = maintain_end

    @property
    def engine(self):
        r"""Gets the engine of this ShowInstanceResponse.

        缓存实例的引擎类型。

        :return: The engine of this ShowInstanceResponse.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ShowInstanceResponse.

        缓存实例的引擎类型。

        :param engine: The engine of this ShowInstanceResponse.
        :type engine: str
        """
        self._engine = engine

    @property
    def no_password_access(self):
        r"""Gets the no_password_access of this ShowInstanceResponse.

        是否允许免密码访问缓存实例。 - true：该实例无需密码即可访问。 - false：该实例必须通过密码认证才能访问。 

        :return: The no_password_access of this ShowInstanceResponse.
        :rtype: str
        """
        return self._no_password_access

    @no_password_access.setter
    def no_password_access(self, no_password_access):
        r"""Sets the no_password_access of this ShowInstanceResponse.

        是否允许免密码访问缓存实例。 - true：该实例无需密码即可访问。 - false：该实例必须通过密码认证才能访问。 

        :param no_password_access: The no_password_access of this ShowInstanceResponse.
        :type no_password_access: str
        """
        self._no_password_access = no_password_access

    @property
    def ip(self):
        r"""Gets the ip of this ShowInstanceResponse.

        连接缓存实例的IP地址。如果是集群实例，返回多个IP地址，使用逗号分隔。如：192.168.0.1，192.168.0.2。

        :return: The ip of this ShowInstanceResponse.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ShowInstanceResponse.

        连接缓存实例的IP地址。如果是集群实例，返回多个IP地址，使用逗号分隔。如：192.168.0.1，192.168.0.2。

        :param ip: The ip of this ShowInstanceResponse.
        :type ip: str
        """
        self._ip = ip

    @property
    def instance_backup_policy(self):
        r"""Gets the instance_backup_policy of this ShowInstanceResponse.

        :return: The instance_backup_policy of this ShowInstanceResponse.
        :rtype: :class:`huaweicloudsdkdcs.v2.InstanceBackupPolicy`
        """
        return self._instance_backup_policy

    @instance_backup_policy.setter
    def instance_backup_policy(self, instance_backup_policy):
        r"""Sets the instance_backup_policy of this ShowInstanceResponse.

        :param instance_backup_policy: The instance_backup_policy of this ShowInstanceResponse.
        :type instance_backup_policy: :class:`huaweicloudsdkdcs.v2.InstanceBackupPolicy`
        """
        self._instance_backup_policy = instance_backup_policy

    @property
    def az_codes(self):
        r"""Gets the az_codes of this ShowInstanceResponse.

        实例所在的可用区。返回“可用区Code”

        :return: The az_codes of this ShowInstanceResponse.
        :rtype: list[str]
        """
        return self._az_codes

    @az_codes.setter
    def az_codes(self, az_codes):
        r"""Sets the az_codes of this ShowInstanceResponse.

        实例所在的可用区。返回“可用区Code”

        :param az_codes: The az_codes of this ShowInstanceResponse.
        :type az_codes: list[str]
        """
        self._az_codes = az_codes

    @property
    def available_zones(self):
        r"""Gets the available_zones of this ShowInstanceResponse.

        实例所在的可用区id。返回\"可用区ID\"

        :return: The available_zones of this ShowInstanceResponse.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this ShowInstanceResponse.

        实例所在的可用区id。返回\"可用区ID\"

        :param available_zones: The available_zones of this ShowInstanceResponse.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def access_user(self):
        r"""Gets the access_user of this ShowInstanceResponse.

        通过密码认证访问缓存实例的认证用户名。

        :return: The access_user of this ShowInstanceResponse.
        :rtype: str
        """
        return self._access_user

    @access_user.setter
    def access_user(self, access_user):
        r"""Sets the access_user of this ShowInstanceResponse.

        通过密码认证访问缓存实例的认证用户名。

        :param access_user: The access_user of this ShowInstanceResponse.
        :type access_user: str
        """
        self._access_user = access_user

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowInstanceResponse.

        实例ID。

        :return: The instance_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowInstanceResponse.

        实例ID。

        :param instance_id: The instance_id of this ShowInstanceResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def port(self):
        r"""Gets the port of this ShowInstanceResponse.

        缓存的端口。

        :return: The port of this ShowInstanceResponse.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ShowInstanceResponse.

        缓存的端口。

        :param port: The port of this ShowInstanceResponse.
        :type port: int
        """
        self._port = port

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowInstanceResponse.

        用户id。

        :return: The user_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowInstanceResponse.

        用户id。

        :param user_id: The user_id of this ShowInstanceResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def name(self):
        r"""Gets the name of this ShowInstanceResponse.

        实例名称。

        :return: The name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowInstanceResponse.

        实例名称。

        :param name: The name of this ShowInstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ShowInstanceResponse.

        产品规格编码

        :return: The spec_code of this ShowInstanceResponse.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ShowInstanceResponse.

        产品规格编码

        :param spec_code: The spec_code of this ShowInstanceResponse.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ShowInstanceResponse.

        子网ID。

        :return: The subnet_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ShowInstanceResponse.

        子网ID。

        :param subnet_id: The subnet_id of this ShowInstanceResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def subnet_name(self):
        r"""Gets the subnet_name of this ShowInstanceResponse.

        子网名称。

        :return: The subnet_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        r"""Sets the subnet_name of this ShowInstanceResponse.

        子网名称。

        :param subnet_name: The subnet_name of this ShowInstanceResponse.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def subnet_cidr(self):
        r"""Gets the subnet_cidr of this ShowInstanceResponse.

        子网网段。

        :return: The subnet_cidr of this ShowInstanceResponse.
        :rtype: str
        """
        return self._subnet_cidr

    @subnet_cidr.setter
    def subnet_cidr(self, subnet_cidr):
        r"""Sets the subnet_cidr of this ShowInstanceResponse.

        子网网段。

        :param subnet_cidr: The subnet_cidr of this ShowInstanceResponse.
        :type subnet_cidr: str
        """
        self._subnet_cidr = subnet_cidr

    @property
    def engine_version(self):
        r"""Gets the engine_version of this ShowInstanceResponse.

        缓存版本。

        :return: The engine_version of this ShowInstanceResponse.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this ShowInstanceResponse.

        缓存版本。

        :param engine_version: The engine_version of this ShowInstanceResponse.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def order_id(self):
        r"""Gets the order_id of this ShowInstanceResponse.

        订单ID。

        :return: The order_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ShowInstanceResponse.

        订单ID。

        :param order_id: The order_id of this ShowInstanceResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def status(self):
        r"""Gets the status of this ShowInstanceResponse.

        缓存实例的状态。详细状态说明见[缓存实例状态说明](https://support.huaweicloud.com/api-dcs/dcs-api-0312047.html)

        :return: The status of this ShowInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowInstanceResponse.

        缓存实例的状态。详细状态说明见[缓存实例状态说明](https://support.huaweicloud.com/api-dcs/dcs-api-0312047.html)

        :param status: The status of this ShowInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowInstanceResponse.

        实例的域名。

        :return: The domain_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowInstanceResponse.

        实例的域名。

        :param domain_name: The domain_name of this ShowInstanceResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def readonly_domain_name(self):
        r"""Gets the readonly_domain_name of this ShowInstanceResponse.

        实例的只读域名，只有主备实例有该字段。

        :return: The readonly_domain_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._readonly_domain_name

    @readonly_domain_name.setter
    def readonly_domain_name(self, readonly_domain_name):
        r"""Sets the readonly_domain_name of this ShowInstanceResponse.

        实例的只读域名，只有主备实例有该字段。

        :param readonly_domain_name: The readonly_domain_name of this ShowInstanceResponse.
        :type readonly_domain_name: str
        """
        self._readonly_domain_name = readonly_domain_name

    @property
    def enable_publicip(self):
        r"""Gets the enable_publicip of this ShowInstanceResponse.

        Redis缓存实例是否开启公网访问功能。 - true：开启 - false：不开启 

        :return: The enable_publicip of this ShowInstanceResponse.
        :rtype: bool
        """
        return self._enable_publicip

    @enable_publicip.setter
    def enable_publicip(self, enable_publicip):
        r"""Sets the enable_publicip of this ShowInstanceResponse.

        Redis缓存实例是否开启公网访问功能。 - true：开启 - false：不开启 

        :param enable_publicip: The enable_publicip of this ShowInstanceResponse.
        :type enable_publicip: bool
        """
        self._enable_publicip = enable_publicip

    @property
    def publicip_id(self):
        r"""Gets the publicip_id of this ShowInstanceResponse.

        Redis缓存实例绑定的弹性IP地址的id。 如果未开启公网访问功能，该字段值为null。 

        :return: The publicip_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        r"""Sets the publicip_id of this ShowInstanceResponse.

        Redis缓存实例绑定的弹性IP地址的id。 如果未开启公网访问功能，该字段值为null。 

        :param publicip_id: The publicip_id of this ShowInstanceResponse.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def publicip_address(self):
        r"""Gets the publicip_address of this ShowInstanceResponse.

        Redis缓存实例绑定的弹性IP地址。 如果未开启公网访问功能，该字段值为null。 

        :return: The publicip_address of this ShowInstanceResponse.
        :rtype: str
        """
        return self._publicip_address

    @publicip_address.setter
    def publicip_address(self, publicip_address):
        r"""Sets the publicip_address of this ShowInstanceResponse.

        Redis缓存实例绑定的弹性IP地址。 如果未开启公网访问功能，该字段值为null。 

        :param publicip_address: The publicip_address of this ShowInstanceResponse.
        :type publicip_address: str
        """
        self._publicip_address = publicip_address

    @property
    def enable_ssl(self):
        r"""Gets the enable_ssl of this ShowInstanceResponse.

        Redis缓存实例开启公网访问功能时，是否选择支持ssl。 - true：开启 - false：不开启 

        :return: The enable_ssl of this ShowInstanceResponse.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        r"""Sets the enable_ssl of this ShowInstanceResponse.

        Redis缓存实例开启公网访问功能时，是否选择支持ssl。 - true：开启 - false：不开启 

        :param enable_ssl: The enable_ssl of this ShowInstanceResponse.
        :type enable_ssl: bool
        """
        self._enable_ssl = enable_ssl

    @property
    def service_upgrade(self):
        r"""Gets the service_upgrade of this ShowInstanceResponse.

        实例是否存在升级任务。 - true：存在 - false：不存在 

        :return: The service_upgrade of this ShowInstanceResponse.
        :rtype: bool
        """
        return self._service_upgrade

    @service_upgrade.setter
    def service_upgrade(self, service_upgrade):
        r"""Sets the service_upgrade of this ShowInstanceResponse.

        实例是否存在升级任务。 - true：存在 - false：不存在 

        :param service_upgrade: The service_upgrade of this ShowInstanceResponse.
        :type service_upgrade: bool
        """
        self._service_upgrade = service_upgrade

    @property
    def service_task_id(self):
        r"""Gets the service_task_id of this ShowInstanceResponse.

        升级任务的ID。 - 当service_upgrade为true时，为升级任务的ID。 - 当service_upgrade为false时，该参数为空。 

        :return: The service_task_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._service_task_id

    @service_task_id.setter
    def service_task_id(self, service_task_id):
        r"""Sets the service_task_id of this ShowInstanceResponse.

        升级任务的ID。 - 当service_upgrade为true时，为升级任务的ID。 - 当service_upgrade为false时，该参数为空。 

        :param service_task_id: The service_task_id of this ShowInstanceResponse.
        :type service_task_id: str
        """
        self._service_task_id = service_task_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowInstanceResponse.

        企业项目ID。

        :return: The enterprise_project_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowInstanceResponse.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ShowInstanceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def backend_addrs(self):
        r"""Gets the backend_addrs of this ShowInstanceResponse.

        集群实例的后端服务地址。

        :return: The backend_addrs of this ShowInstanceResponse.
        :rtype: str
        """
        return self._backend_addrs

    @backend_addrs.setter
    def backend_addrs(self, backend_addrs):
        r"""Sets the backend_addrs of this ShowInstanceResponse.

        集群实例的后端服务地址。

        :param backend_addrs: The backend_addrs of this ShowInstanceResponse.
        :type backend_addrs: str
        """
        self._backend_addrs = backend_addrs

    @property
    def features(self):
        r"""Gets the features of this ShowInstanceResponse.

        :return: The features of this ShowInstanceResponse.
        :rtype: :class:`huaweicloudsdkdcs.v2.Features`
        """
        return self._features

    @features.setter
    def features(self, features):
        r"""Sets the features of this ShowInstanceResponse.

        :param features: The features of this ShowInstanceResponse.
        :type features: :class:`huaweicloudsdkdcs.v2.Features`
        """
        self._features = features

    @property
    def domain_name_info(self):
        r"""Gets the domain_name_info of this ShowInstanceResponse.

        :return: The domain_name_info of this ShowInstanceResponse.
        :rtype: :class:`huaweicloudsdkdcs.v2.DomainNameInfo`
        """
        return self._domain_name_info

    @domain_name_info.setter
    def domain_name_info(self, domain_name_info):
        r"""Sets the domain_name_info of this ShowInstanceResponse.

        :param domain_name_info: The domain_name_info of this ShowInstanceResponse.
        :type domain_name_info: :class:`huaweicloudsdkdcs.v2.DomainNameInfo`
        """
        self._domain_name_info = domain_name_info

    @property
    def transparent_client_ip_enable(self):
        r"""Gets the transparent_client_ip_enable of this ShowInstanceResponse.

        是否开启客户端ip透传。

        :return: The transparent_client_ip_enable of this ShowInstanceResponse.
        :rtype: bool
        """
        return self._transparent_client_ip_enable

    @transparent_client_ip_enable.setter
    def transparent_client_ip_enable(self, transparent_client_ip_enable):
        r"""Sets the transparent_client_ip_enable of this ShowInstanceResponse.

        是否开启客户端ip透传。

        :param transparent_client_ip_enable: The transparent_client_ip_enable of this ShowInstanceResponse.
        :type transparent_client_ip_enable: bool
        """
        self._transparent_client_ip_enable = transparent_client_ip_enable

    @property
    def sub_status(self):
        r"""Gets the sub_status of this ShowInstanceResponse.

        实例子状态。

        :return: The sub_status of this ShowInstanceResponse.
        :rtype: str
        """
        return self._sub_status

    @sub_status.setter
    def sub_status(self, sub_status):
        r"""Sets the sub_status of this ShowInstanceResponse.

        实例子状态。

        :param sub_status: The sub_status of this ShowInstanceResponse.
        :type sub_status: str
        """
        self._sub_status = sub_status

    @property
    def tags(self):
        r"""Gets the tags of this ShowInstanceResponse.

        实例标签键值。

        :return: The tags of this ShowInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowInstanceResponse.

        实例标签键值。

        :param tags: The tags of this ShowInstanceResponse.
        :type tags: list[:class:`huaweicloudsdkdcs.v2.ResourceTag`]
        """
        self._tags = tags

    @property
    def cpu_type(self):
        r"""Gets the cpu_type of this ShowInstanceResponse.

        实例CPU类型，通常为x86_64或aarch64

        :return: The cpu_type of this ShowInstanceResponse.
        :rtype: str
        """
        return self._cpu_type

    @cpu_type.setter
    def cpu_type(self, cpu_type):
        r"""Sets the cpu_type of this ShowInstanceResponse.

        实例CPU类型，通常为x86_64或aarch64

        :param cpu_type: The cpu_type of this ShowInstanceResponse.
        :type cpu_type: str
        """
        self._cpu_type = cpu_type

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this ShowInstanceResponse.

        企业项目名称。

        :return: The enterprise_project_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this ShowInstanceResponse.

        企业项目名称。

        :param enterprise_project_name: The enterprise_project_name of this ShowInstanceResponse.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def update_at(self):
        r"""Gets the update_at of this ShowInstanceResponse.

        更新时间，形如2022-07-06T09:32:16.502Z

        :return: The update_at of this ShowInstanceResponse.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ShowInstanceResponse.

        更新时间，形如2022-07-06T09:32:16.502Z

        :param update_at: The update_at of this ShowInstanceResponse.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def product_type(self):
        r"""Gets the product_type of this ShowInstanceResponse.

        版本类型：社区版、企业版

        :return: The product_type of this ShowInstanceResponse.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        r"""Sets the product_type of this ShowInstanceResponse.

        版本类型：社区版、企业版

        :param product_type: The product_type of this ShowInstanceResponse.
        :type product_type: str
        """
        self._product_type = product_type

    @property
    def storage_type(self):
        r"""Gets the storage_type of this ShowInstanceResponse.

        存储类型：内存存储

        :return: The storage_type of this ShowInstanceResponse.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        r"""Sets the storage_type of this ShowInstanceResponse.

        存储类型：内存存储

        :param storage_type: The storage_type of this ShowInstanceResponse.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def launched_at(self):
        r"""Gets the launched_at of this ShowInstanceResponse.

        启动时间，形如2022-07-06T09:32:16.502Z

        :return: The launched_at of this ShowInstanceResponse.
        :rtype: str
        """
        return self._launched_at

    @launched_at.setter
    def launched_at(self, launched_at):
        r"""Sets the launched_at of this ShowInstanceResponse.

        启动时间，形如2022-07-06T09:32:16.502Z

        :param launched_at: The launched_at of this ShowInstanceResponse.
        :type launched_at: str
        """
        self._launched_at = launched_at

    @property
    def cache_mode(self):
        r"""Gets the cache_mode of this ShowInstanceResponse.

        缓存类型：单机类型，主备类型，主备读写分离，Proxy集群类型，原生集群类型

        :return: The cache_mode of this ShowInstanceResponse.
        :rtype: str
        """
        return self._cache_mode

    @cache_mode.setter
    def cache_mode(self, cache_mode):
        r"""Sets the cache_mode of this ShowInstanceResponse.

        缓存类型：单机类型，主备类型，主备读写分离，Proxy集群类型，原生集群类型

        :param cache_mode: The cache_mode of this ShowInstanceResponse.
        :type cache_mode: str
        """
        self._cache_mode = cache_mode

    @property
    def support_slow_log_flag(self):
        r"""Gets the support_slow_log_flag of this ShowInstanceResponse.

        是否支持慢日志

        :return: The support_slow_log_flag of this ShowInstanceResponse.
        :rtype: str
        """
        return self._support_slow_log_flag

    @support_slow_log_flag.setter
    def support_slow_log_flag(self, support_slow_log_flag):
        r"""Sets the support_slow_log_flag of this ShowInstanceResponse.

        是否支持慢日志

        :param support_slow_log_flag: The support_slow_log_flag of this ShowInstanceResponse.
        :type support_slow_log_flag: str
        """
        self._support_slow_log_flag = support_slow_log_flag

    @property
    def db_number(self):
        r"""Gets the db_number of this ShowInstanceResponse.

        数据库数量

        :return: The db_number of this ShowInstanceResponse.
        :rtype: int
        """
        return self._db_number

    @db_number.setter
    def db_number(self, db_number):
        r"""Sets the db_number of this ShowInstanceResponse.

        数据库数量

        :param db_number: The db_number of this ShowInstanceResponse.
        :type db_number: int
        """
        self._db_number = db_number

    @property
    def replica_count(self):
        r"""Gets the replica_count of this ShowInstanceResponse.

        副本数

        :return: The replica_count of this ShowInstanceResponse.
        :rtype: int
        """
        return self._replica_count

    @replica_count.setter
    def replica_count(self, replica_count):
        r"""Sets the replica_count of this ShowInstanceResponse.

        副本数

        :param replica_count: The replica_count of this ShowInstanceResponse.
        :type replica_count: int
        """
        self._replica_count = replica_count

    @property
    def sharding_count(self):
        r"""Gets the sharding_count of this ShowInstanceResponse.

        集群实例分片个数

        :return: The sharding_count of this ShowInstanceResponse.
        :rtype: int
        """
        return self._sharding_count

    @sharding_count.setter
    def sharding_count(self, sharding_count):
        r"""Sets the sharding_count of this ShowInstanceResponse.

        集群实例分片个数

        :param sharding_count: The sharding_count of this ShowInstanceResponse.
        :type sharding_count: int
        """
        self._sharding_count = sharding_count

    @property
    def bandwidth_info(self):
        r"""Gets the bandwidth_info of this ShowInstanceResponse.

        :return: The bandwidth_info of this ShowInstanceResponse.
        :rtype: :class:`huaweicloudsdkdcs.v2.BandwidthInfo`
        """
        return self._bandwidth_info

    @bandwidth_info.setter
    def bandwidth_info(self, bandwidth_info):
        r"""Sets the bandwidth_info of this ShowInstanceResponse.

        :param bandwidth_info: The bandwidth_info of this ShowInstanceResponse.
        :type bandwidth_info: :class:`huaweicloudsdkdcs.v2.BandwidthInfo`
        """
        self._bandwidth_info = bandwidth_info

    @property
    def cloud_service_type_code(self):
        r"""Gets the cloud_service_type_code of this ShowInstanceResponse.

        云服务类型编码。

        :return: The cloud_service_type_code of this ShowInstanceResponse.
        :rtype: str
        """
        return self._cloud_service_type_code

    @cloud_service_type_code.setter
    def cloud_service_type_code(self, cloud_service_type_code):
        r"""Sets the cloud_service_type_code of this ShowInstanceResponse.

        云服务类型编码。

        :param cloud_service_type_code: The cloud_service_type_code of this ShowInstanceResponse.
        :type cloud_service_type_code: str
        """
        self._cloud_service_type_code = cloud_service_type_code

    @property
    def cloud_resource_type_code(self):
        r"""Gets the cloud_resource_type_code of this ShowInstanceResponse.

        云资源类型编码。

        :return: The cloud_resource_type_code of this ShowInstanceResponse.
        :rtype: str
        """
        return self._cloud_resource_type_code

    @cloud_resource_type_code.setter
    def cloud_resource_type_code(self, cloud_resource_type_code):
        r"""Sets the cloud_resource_type_code of this ShowInstanceResponse.

        云资源类型编码。

        :param cloud_resource_type_code: The cloud_resource_type_code of this ShowInstanceResponse.
        :type cloud_resource_type_code: str
        """
        self._cloud_resource_type_code = cloud_resource_type_code

    @property
    def inquery_spec_code(self):
        r"""Gets the inquery_spec_code of this ShowInstanceResponse.

        运营系统中的规格编码

        :return: The inquery_spec_code of this ShowInstanceResponse.
        :rtype: str
        """
        return self._inquery_spec_code

    @inquery_spec_code.setter
    def inquery_spec_code(self, inquery_spec_code):
        r"""Sets the inquery_spec_code of this ShowInstanceResponse.

        运营系统中的规格编码

        :param inquery_spec_code: The inquery_spec_code of this ShowInstanceResponse.
        :type inquery_spec_code: str
        """
        self._inquery_spec_code = inquery_spec_code

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
