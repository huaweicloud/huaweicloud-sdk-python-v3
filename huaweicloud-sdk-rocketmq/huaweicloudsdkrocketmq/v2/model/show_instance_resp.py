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
        'subnet_name': 'str',
        'subnet_cidr': 'str',
        'available_zones': 'list[str]',
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
        'namesrv_address': 'str',
        'broker_address': 'str',
        'public_namesrv_address': 'str',
        'public_broker_address': 'str',
        'tags': 'list[TagEntity]',
        'total_storage_space': 'int',
        'resource_spec_code': 'str'
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
        'subnet_name': 'subnet_name',
        'subnet_cidr': 'subnet_cidr',
        'available_zones': 'available_zones',
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
        'namesrv_address': 'namesrv_address',
        'broker_address': 'broker_address',
        'public_namesrv_address': 'public_namesrv_address',
        'public_broker_address': 'public_broker_address',
        'tags': 'tags',
        'total_storage_space': 'total_storage_space',
        'resource_spec_code': 'resource_spec_code'
    }

    def __init__(self, name=None, engine=None, status=None, description=None, type=None, specification=None, engine_version=None, instance_id=None, charging_mode=None, vpc_id=None, vpc_name=None, created_at=None, product_id=None, security_group_id=None, security_group_name=None, subnet_id=None, subnet_name=None, subnet_cidr=None, available_zones=None, user_id=None, user_name=None, maintain_begin=None, maintain_end=None, enable_log_collection=None, storage_space=None, used_storage_space=None, enable_publicip=None, publicip_id=None, publicip_address=None, ssl_enable=None, cross_vpc_info=None, storage_resource_id=None, storage_spec_code=None, service_type=None, storage_type=None, extend_times=None, ipv6_enable=None, support_features=None, disk_encrypted=None, ces_version=None, node_num=None, new_spec_billing_enable=None, enable_acl=None, broker_num=None, namesrv_address=None, broker_address=None, public_namesrv_address=None, public_broker_address=None, tags=None, total_storage_space=None, resource_spec_code=None):
        """ShowInstanceResp

        The model defined in huaweicloud sdk

        :param name: 实例名称。
        :type name: str
        :param engine: 引擎。
        :type engine: str
        :param status: 状态。
        :type status: str
        :param description: 消息描述。
        :type description: str
        :param type: 实例类型：集群，cluster。
        :type type: str
        :param specification: 实例规格。
        :type specification: str
        :param engine_version: 版本。
        :type engine_version: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param charging_mode: [付费模式，1表示按需计费。](tag:hws_eu,hws_hk,)[付费模式，1表示按需计费，0表示包年/包月计费。](tag:hws,ctc) [计费模式，参数暂未使用。](tag:ocb,hws_ocb)
        :type charging_mode: int
        :param vpc_id: 私有云ID。
        :type vpc_id: str
        :param vpc_name: 私有云名称。
        :type vpc_name: str
        :param created_at: 完成创建时间。 格式为时间戳，指从格林威治时间1970年01月01日00时00分00秒起至指定时间的偏差总毫秒数。
        :type created_at: str
        :param product_id: 产品标识。
        :type product_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param security_group_name: 租户安全组名称。
        :type security_group_name: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param subnet_name: 子网名称。
        :type subnet_name: str
        :param subnet_cidr: 子网路由。
        :type subnet_cidr: str
        :param available_zones: IO未售罄的可用区列表。
        :type available_zones: list[str]
        :param user_id: 用户ID。
        :type user_id: str
        :param user_name: 用户名。
        :type user_name: str
        :param maintain_begin: 维护时间窗开始时间，格式为HH:mm:ss。
        :type maintain_begin: str
        :param maintain_end: 维护时间窗结束时间，格式为HH:mm:ss。
        :type maintain_end: str
        :param enable_log_collection: 是否开启消息收集功能。
        :type enable_log_collection: bool
        :param storage_space: 存储空间，单位：GB。
        :type storage_space: int
        :param used_storage_space: 已用消息存储空间，单位：GB。
        :type used_storage_space: int
        :param enable_publicip: 是否开启公网。
        :type enable_publicip: bool
        :param publicip_id: 实例绑定的弹性IP地址的ID。 以英文逗号隔开多个弹性IP地址的ID。 如果开启了公网访问功能（即enable_publicip为true），该字段为必选。
        :type publicip_id: str
        :param publicip_address: 公网IP地址。
        :type publicip_address: str
        :param ssl_enable: 是否开启SSL。
        :type ssl_enable: bool
        :param cross_vpc_info: 跨VPC访问信息。
        :type cross_vpc_info: str
        :param storage_resource_id: 存储资源ID。
        :type storage_resource_id: str
        :param storage_spec_code: 存储规格代码。
        :type storage_spec_code: str
        :param service_type: 服务类型。
        :type service_type: str
        :param storage_type: 存储类型。
        :type storage_type: str
        :param extend_times: 扩展时间。
        :type extend_times: int
        :param ipv6_enable: 是否开启IPv6。
        :type ipv6_enable: bool
        :param support_features: 实例支持的特性功能。
        :type support_features: str
        :param disk_encrypted: 是否开启磁盘加密。
        :type disk_encrypted: bool
        :param ces_version: 云监控版本。
        :type ces_version: str
        :param node_num: 节点数。
        :type node_num: int
        :param new_spec_billing_enable: 是否启用新规格计费。
        :type new_spec_billing_enable: bool
        :param enable_acl: 是否开启访问控制列表。
        :type enable_acl: bool
        :param broker_num: 节点数。
        :type broker_num: int
        :param namesrv_address: 元数据地址。
        :type namesrv_address: str
        :param broker_address: 业务数据地址。
        :type broker_address: str
        :param public_namesrv_address: 公网元数据地址。
        :type public_namesrv_address: str
        :param public_broker_address: 公网业务数据地址。
        :type public_broker_address: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkrocketmq.v2.TagEntity`]
        :param total_storage_space: 总存储空间。
        :type total_storage_space: int
        :param resource_spec_code: 资源规格。
        :type resource_spec_code: str
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
        self._subnet_name = None
        self._subnet_cidr = None
        self._available_zones = None
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
        self._namesrv_address = None
        self._broker_address = None
        self._public_namesrv_address = None
        self._public_broker_address = None
        self._tags = None
        self._total_storage_space = None
        self._resource_spec_code = None
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
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if subnet_cidr is not None:
            self.subnet_cidr = subnet_cidr
        if available_zones is not None:
            self.available_zones = available_zones
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
        if namesrv_address is not None:
            self.namesrv_address = namesrv_address
        if broker_address is not None:
            self.broker_address = broker_address
        if public_namesrv_address is not None:
            self.public_namesrv_address = public_namesrv_address
        if public_broker_address is not None:
            self.public_broker_address = public_broker_address
        if tags is not None:
            self.tags = tags
        if total_storage_space is not None:
            self.total_storage_space = total_storage_space
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code

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
    def status(self):
        """Gets the status of this ShowInstanceResp.

        状态。

        :return: The status of this ShowInstanceResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowInstanceResp.

        状态。

        :param status: The status of this ShowInstanceResp.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this ShowInstanceResp.

        消息描述。

        :return: The description of this ShowInstanceResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowInstanceResp.

        消息描述。

        :param description: The description of this ShowInstanceResp.
        :type description: str
        """
        self._description = description

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
    def charging_mode(self):
        """Gets the charging_mode of this ShowInstanceResp.

        [付费模式，1表示按需计费。](tag:hws_eu,hws_hk,)[付费模式，1表示按需计费，0表示包年/包月计费。](tag:hws,ctc) [计费模式，参数暂未使用。](tag:ocb,hws_ocb)

        :return: The charging_mode of this ShowInstanceResp.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this ShowInstanceResp.

        [付费模式，1表示按需计费。](tag:hws_eu,hws_hk,)[付费模式，1表示按需计费，0表示包年/包月计费。](tag:hws,ctc) [计费模式，参数暂未使用。](tag:ocb,hws_ocb)

        :param charging_mode: The charging_mode of this ShowInstanceResp.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ShowInstanceResp.

        私有云ID。

        :return: The vpc_id of this ShowInstanceResp.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ShowInstanceResp.

        私有云ID。

        :param vpc_id: The vpc_id of this ShowInstanceResp.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        """Gets the vpc_name of this ShowInstanceResp.

        私有云名称。

        :return: The vpc_name of this ShowInstanceResp.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this ShowInstanceResp.

        私有云名称。

        :param vpc_name: The vpc_name of this ShowInstanceResp.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def created_at(self):
        """Gets the created_at of this ShowInstanceResp.

        完成创建时间。 格式为时间戳，指从格林威治时间1970年01月01日00时00分00秒起至指定时间的偏差总毫秒数。

        :return: The created_at of this ShowInstanceResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowInstanceResp.

        完成创建时间。 格式为时间戳，指从格林威治时间1970年01月01日00时00分00秒起至指定时间的偏差总毫秒数。

        :param created_at: The created_at of this ShowInstanceResp.
        :type created_at: str
        """
        self._created_at = created_at

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

        子网路由。

        :return: The subnet_cidr of this ShowInstanceResp.
        :rtype: str
        """
        return self._subnet_cidr

    @subnet_cidr.setter
    def subnet_cidr(self, subnet_cidr):
        """Sets the subnet_cidr of this ShowInstanceResp.

        子网路由。

        :param subnet_cidr: The subnet_cidr of this ShowInstanceResp.
        :type subnet_cidr: str
        """
        self._subnet_cidr = subnet_cidr

    @property
    def available_zones(self):
        """Gets the available_zones of this ShowInstanceResp.

        IO未售罄的可用区列表。

        :return: The available_zones of this ShowInstanceResp.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this ShowInstanceResp.

        IO未售罄的可用区列表。

        :param available_zones: The available_zones of this ShowInstanceResp.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

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
    def storage_space(self):
        """Gets the storage_space of this ShowInstanceResp.

        存储空间，单位：GB。

        :return: The storage_space of this ShowInstanceResp.
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        """Sets the storage_space of this ShowInstanceResp.

        存储空间，单位：GB。

        :param storage_space: The storage_space of this ShowInstanceResp.
        :type storage_space: int
        """
        self._storage_space = storage_space

    @property
    def used_storage_space(self):
        """Gets the used_storage_space of this ShowInstanceResp.

        已用消息存储空间，单位：GB。

        :return: The used_storage_space of this ShowInstanceResp.
        :rtype: int
        """
        return self._used_storage_space

    @used_storage_space.setter
    def used_storage_space(self, used_storage_space):
        """Sets the used_storage_space of this ShowInstanceResp.

        已用消息存储空间，单位：GB。

        :param used_storage_space: The used_storage_space of this ShowInstanceResp.
        :type used_storage_space: int
        """
        self._used_storage_space = used_storage_space

    @property
    def enable_publicip(self):
        """Gets the enable_publicip of this ShowInstanceResp.

        是否开启公网。

        :return: The enable_publicip of this ShowInstanceResp.
        :rtype: bool
        """
        return self._enable_publicip

    @enable_publicip.setter
    def enable_publicip(self, enable_publicip):
        """Sets the enable_publicip of this ShowInstanceResp.

        是否开启公网。

        :param enable_publicip: The enable_publicip of this ShowInstanceResp.
        :type enable_publicip: bool
        """
        self._enable_publicip = enable_publicip

    @property
    def publicip_id(self):
        """Gets the publicip_id of this ShowInstanceResp.

        实例绑定的弹性IP地址的ID。 以英文逗号隔开多个弹性IP地址的ID。 如果开启了公网访问功能（即enable_publicip为true），该字段为必选。

        :return: The publicip_id of this ShowInstanceResp.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this ShowInstanceResp.

        实例绑定的弹性IP地址的ID。 以英文逗号隔开多个弹性IP地址的ID。 如果开启了公网访问功能（即enable_publicip为true），该字段为必选。

        :param publicip_id: The publicip_id of this ShowInstanceResp.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def publicip_address(self):
        """Gets the publicip_address of this ShowInstanceResp.

        公网IP地址。

        :return: The publicip_address of this ShowInstanceResp.
        :rtype: str
        """
        return self._publicip_address

    @publicip_address.setter
    def publicip_address(self, publicip_address):
        """Sets the publicip_address of this ShowInstanceResp.

        公网IP地址。

        :param publicip_address: The publicip_address of this ShowInstanceResp.
        :type publicip_address: str
        """
        self._publicip_address = publicip_address

    @property
    def ssl_enable(self):
        """Gets the ssl_enable of this ShowInstanceResp.

        是否开启SSL。

        :return: The ssl_enable of this ShowInstanceResp.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        """Sets the ssl_enable of this ShowInstanceResp.

        是否开启SSL。

        :param ssl_enable: The ssl_enable of this ShowInstanceResp.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

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

        存储规格代码。

        :return: The storage_spec_code of this ShowInstanceResp.
        :rtype: str
        """
        return self._storage_spec_code

    @storage_spec_code.setter
    def storage_spec_code(self, storage_spec_code):
        """Sets the storage_spec_code of this ShowInstanceResp.

        存储规格代码。

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
    def extend_times(self):
        """Gets the extend_times of this ShowInstanceResp.

        扩展时间。

        :return: The extend_times of this ShowInstanceResp.
        :rtype: int
        """
        return self._extend_times

    @extend_times.setter
    def extend_times(self, extend_times):
        """Sets the extend_times of this ShowInstanceResp.

        扩展时间。

        :param extend_times: The extend_times of this ShowInstanceResp.
        :type extend_times: int
        """
        self._extend_times = extend_times

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this ShowInstanceResp.

        是否开启IPv6。

        :return: The ipv6_enable of this ShowInstanceResp.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this ShowInstanceResp.

        是否开启IPv6。

        :param ipv6_enable: The ipv6_enable of this ShowInstanceResp.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def support_features(self):
        """Gets the support_features of this ShowInstanceResp.

        实例支持的特性功能。

        :return: The support_features of this ShowInstanceResp.
        :rtype: str
        """
        return self._support_features

    @support_features.setter
    def support_features(self, support_features):
        """Sets the support_features of this ShowInstanceResp.

        实例支持的特性功能。

        :param support_features: The support_features of this ShowInstanceResp.
        :type support_features: str
        """
        self._support_features = support_features

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
    def enable_acl(self):
        """Gets the enable_acl of this ShowInstanceResp.

        是否开启访问控制列表。

        :return: The enable_acl of this ShowInstanceResp.
        :rtype: bool
        """
        return self._enable_acl

    @enable_acl.setter
    def enable_acl(self, enable_acl):
        """Sets the enable_acl of this ShowInstanceResp.

        是否开启访问控制列表。

        :param enable_acl: The enable_acl of this ShowInstanceResp.
        :type enable_acl: bool
        """
        self._enable_acl = enable_acl

    @property
    def broker_num(self):
        """Gets the broker_num of this ShowInstanceResp.

        节点数。

        :return: The broker_num of this ShowInstanceResp.
        :rtype: int
        """
        return self._broker_num

    @broker_num.setter
    def broker_num(self, broker_num):
        """Sets the broker_num of this ShowInstanceResp.

        节点数。

        :param broker_num: The broker_num of this ShowInstanceResp.
        :type broker_num: int
        """
        self._broker_num = broker_num

    @property
    def namesrv_address(self):
        """Gets the namesrv_address of this ShowInstanceResp.

        元数据地址。

        :return: The namesrv_address of this ShowInstanceResp.
        :rtype: str
        """
        return self._namesrv_address

    @namesrv_address.setter
    def namesrv_address(self, namesrv_address):
        """Sets the namesrv_address of this ShowInstanceResp.

        元数据地址。

        :param namesrv_address: The namesrv_address of this ShowInstanceResp.
        :type namesrv_address: str
        """
        self._namesrv_address = namesrv_address

    @property
    def broker_address(self):
        """Gets the broker_address of this ShowInstanceResp.

        业务数据地址。

        :return: The broker_address of this ShowInstanceResp.
        :rtype: str
        """
        return self._broker_address

    @broker_address.setter
    def broker_address(self, broker_address):
        """Sets the broker_address of this ShowInstanceResp.

        业务数据地址。

        :param broker_address: The broker_address of this ShowInstanceResp.
        :type broker_address: str
        """
        self._broker_address = broker_address

    @property
    def public_namesrv_address(self):
        """Gets the public_namesrv_address of this ShowInstanceResp.

        公网元数据地址。

        :return: The public_namesrv_address of this ShowInstanceResp.
        :rtype: str
        """
        return self._public_namesrv_address

    @public_namesrv_address.setter
    def public_namesrv_address(self, public_namesrv_address):
        """Sets the public_namesrv_address of this ShowInstanceResp.

        公网元数据地址。

        :param public_namesrv_address: The public_namesrv_address of this ShowInstanceResp.
        :type public_namesrv_address: str
        """
        self._public_namesrv_address = public_namesrv_address

    @property
    def public_broker_address(self):
        """Gets the public_broker_address of this ShowInstanceResp.

        公网业务数据地址。

        :return: The public_broker_address of this ShowInstanceResp.
        :rtype: str
        """
        return self._public_broker_address

    @public_broker_address.setter
    def public_broker_address(self, public_broker_address):
        """Sets the public_broker_address of this ShowInstanceResp.

        公网业务数据地址。

        :param public_broker_address: The public_broker_address of this ShowInstanceResp.
        :type public_broker_address: str
        """
        self._public_broker_address = public_broker_address

    @property
    def tags(self):
        """Gets the tags of this ShowInstanceResp.

        标签列表。

        :return: The tags of this ShowInstanceResp.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.TagEntity`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowInstanceResp.

        标签列表。

        :param tags: The tags of this ShowInstanceResp.
        :type tags: list[:class:`huaweicloudsdkrocketmq.v2.TagEntity`]
        """
        self._tags = tags

    @property
    def total_storage_space(self):
        """Gets the total_storage_space of this ShowInstanceResp.

        总存储空间。

        :return: The total_storage_space of this ShowInstanceResp.
        :rtype: int
        """
        return self._total_storage_space

    @total_storage_space.setter
    def total_storage_space(self, total_storage_space):
        """Sets the total_storage_space of this ShowInstanceResp.

        总存储空间。

        :param total_storage_space: The total_storage_space of this ShowInstanceResp.
        :type total_storage_space: int
        """
        self._total_storage_space = total_storage_space

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this ShowInstanceResp.

        资源规格。

        :return: The resource_spec_code of this ShowInstanceResp.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this ShowInstanceResp.

        资源规格。

        :param resource_spec_code: The resource_spec_code of this ShowInstanceResp.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

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
