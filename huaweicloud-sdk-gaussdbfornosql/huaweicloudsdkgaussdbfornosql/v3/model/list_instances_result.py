# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesResult:

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
        'status': 'str',
        'port': 'str',
        'region': 'str',
        'datastore': 'ListInstancesDatastoreResult',
        'mode': 'str',
        'product_type': 'str',
        'engine': 'str',
        'created': 'str',
        'updated': 'str',
        'db_user_name': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'backup_strategy': 'ListInstancesBackupStrategyResult',
        'pay_mode': 'str',
        'maintenance_window': 'str',
        'groups': 'list[ListInstancesGroupResult]',
        'enterprise_project_id': 'str',
        'dedicated_resource_id': 'str',
        'time_zone': 'str',
        'actions': 'list[str]',
        'disk_encryption_id': 'str',
        'lb_ip_address': 'str',
        'lb_port': 'str',
        'availability_zone': 'str',
        'dr_instance_id': 'str',
        'dual_active_info': 'DualActiveInfo',
        'ccm_cert_info': 'CertInfoOption',
        'ssl': 'str',
        'backup_space_usage': 'BackupSpaceUsage'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'port': 'port',
        'region': 'region',
        'datastore': 'datastore',
        'mode': 'mode',
        'product_type': 'product_type',
        'engine': 'engine',
        'created': 'created',
        'updated': 'updated',
        'db_user_name': 'db_user_name',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'backup_strategy': 'backup_strategy',
        'pay_mode': 'pay_mode',
        'maintenance_window': 'maintenance_window',
        'groups': 'groups',
        'enterprise_project_id': 'enterprise_project_id',
        'dedicated_resource_id': 'dedicated_resource_id',
        'time_zone': 'time_zone',
        'actions': 'actions',
        'disk_encryption_id': 'disk_encryption_id',
        'lb_ip_address': 'lb_ip_address',
        'lb_port': 'lb_port',
        'availability_zone': 'availability_zone',
        'dr_instance_id': 'dr_instance_id',
        'dual_active_info': 'dual_active_info',
        'ccm_cert_info': 'ccm_cert_info',
        'ssl': 'ssl',
        'backup_space_usage': 'backup_space_usage'
    }

    def __init__(self, id=None, name=None, status=None, port=None, region=None, datastore=None, mode=None, product_type=None, engine=None, created=None, updated=None, db_user_name=None, vpc_id=None, subnet_id=None, security_group_id=None, backup_strategy=None, pay_mode=None, maintenance_window=None, groups=None, enterprise_project_id=None, dedicated_resource_id=None, time_zone=None, actions=None, disk_encryption_id=None, lb_ip_address=None, lb_port=None, availability_zone=None, dr_instance_id=None, dual_active_info=None, ccm_cert_info=None, ssl=None, backup_space_usage=None):
        r"""ListInstancesResult

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 实例ID。 **取值范围：** 不涉及。
        :type id: str
        :param name: **参数解释：** 实例名称。 **取值范围：** 不涉及。
        :type name: str
        :param status: **参数解释：** 实例状态。 **取值范围：** - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示实例磁盘已满。 - createfail，表示实例创建失败。 - enlargefail，表示实例扩容节点个数失败。
        :type status: str
        :param port: **参数解释：** 数据库端口。 **取值范围：** 不涉及。
        :type port: str
        :param region: **参数解释：** 实例所在区域。 **取值范围：** 不涉及。
        :type region: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesDatastoreResult`
        :param mode: **参数解释：** 实例类型。 **取值范围：** 与请求参数相同。
        :type mode: str
        :param product_type: **参数解释：** 产品类型。 **取值范围：** GeminiDB Redis云原生部署模式集群涉及此字段，取值：   -  Standard 标准型   -  Capacity 容量型
        :type product_type: str
        :param engine: **参数解释：** 存储引擎。 **取值范围：** 取值为“rocksDB”。
        :type engine: str
        :param created: **参数解释：** 实例创建时间。 **取值范围：** 不涉及。
        :type created: str
        :param updated: **参数解释：** 实例操作最新变更的时间。 **取值范围：** 不涉及。
        :type updated: str
        :param db_user_name: **参数解释：** 默认用户名。 **取值范围：** 取值为“rwuser”。
        :type db_user_name: str
        :param vpc_id: **参数解释：** 虚拟私有云ID。 **取值范围：** 不涉及。
        :type vpc_id: str
        :param subnet_id: **参数解释：** 子网ID。 **取值范围：** GeminiDB Cassandra 实例使用多个子网的场景，请参见表 ListInstancesNodeResult字段数据结构说明中的“subnet_id”。
        :type subnet_id: str
        :param security_group_id: **参数解释：** 安全组ID。 **取值范围：** 不涉及。
        :type security_group_id: str
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesBackupStrategyResult`
        :param pay_mode: **参数解释：** 计费方式。 **取值范围：** - 取值为“0”，表示按需计费。 - 取值为“1”，表示包年/包月计费。
        :type pay_mode: str
        :param maintenance_window: **参数解释：** 系统可维护时间窗。 **取值范围：** 不涉及。
        :type maintenance_window: str
        :param groups: **参数解释：** 组信息。 **取值范围：** 不涉及。
        :type groups: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesGroupResult`]
        :param enterprise_project_id: **参数解释：** 企业项目ID。 **取值范围：** 取值为“0”，表示为default企业项目。
        :type enterprise_project_id: str
        :param dedicated_resource_id: **参数解释：** 专属资源ID。只有数据库实例属于专属资源池才会返回该参数。 **取值范围：** 不涉及。
        :type dedicated_resource_id: str
        :param time_zone: **参数解释：** 时区。 **取值范围：** 不涉及。
        :type time_zone: str
        :param actions: **参数解释：** 实例正在执行的动作。 **取值范围：** 不涉及。
        :type actions: list[str]
        :param disk_encryption_id: **参数解释：** 磁盘加密时的密钥ID。 **取值范围：** 不涉及。
        :type disk_encryption_id: str
        :param lb_ip_address: **参数解释：** 负载均衡ip。 **取值范围：** 只有存在负载均衡ip，才会返回该参数。
        :type lb_ip_address: str
        :param lb_port: **参数解释：** 负载均衡端口。 **取值范围：** 只有存在负载均衡ip，才会返回该参数。
        :type lb_port: str
        :param availability_zone: **参数解释：** 实例可用区。 **取值范围：** 不涉及。
        :type availability_zone: str
        :param dr_instance_id: **参数解释：** 容灾实例ID。 **取值范围：** 不涉及。
        :type dr_instance_id: str
        :param dual_active_info: 
        :type dual_active_info: :class:`huaweicloudsdkgaussdbfornosql.v3.DualActiveInfo`
        :param ccm_cert_info: 
        :type ccm_cert_info: :class:`huaweicloudsdkgaussdbfornosql.v3.CertInfoOption`
        :param ssl: **参数解释：** SSL安全连接启用情况。 **取值范围：** - 取值为“0”表示未启用。 - 取值为“1”表示已启用。
        :type ssl: str
        :param backup_space_usage: 
        :type backup_space_usage: :class:`huaweicloudsdkgaussdbfornosql.v3.BackupSpaceUsage`
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._port = None
        self._region = None
        self._datastore = None
        self._mode = None
        self._product_type = None
        self._engine = None
        self._created = None
        self._updated = None
        self._db_user_name = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._backup_strategy = None
        self._pay_mode = None
        self._maintenance_window = None
        self._groups = None
        self._enterprise_project_id = None
        self._dedicated_resource_id = None
        self._time_zone = None
        self._actions = None
        self._disk_encryption_id = None
        self._lb_ip_address = None
        self._lb_port = None
        self._availability_zone = None
        self._dr_instance_id = None
        self._dual_active_info = None
        self._ccm_cert_info = None
        self._ssl = None
        self._backup_space_usage = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.port = port
        self.region = region
        self.datastore = datastore
        self.mode = mode
        if product_type is not None:
            self.product_type = product_type
        self.engine = engine
        self.created = created
        self.updated = updated
        self.db_user_name = db_user_name
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.backup_strategy = backup_strategy
        self.pay_mode = pay_mode
        self.maintenance_window = maintenance_window
        self.groups = groups
        self.enterprise_project_id = enterprise_project_id
        if dedicated_resource_id is not None:
            self.dedicated_resource_id = dedicated_resource_id
        self.time_zone = time_zone
        self.actions = actions
        self.disk_encryption_id = disk_encryption_id
        if lb_ip_address is not None:
            self.lb_ip_address = lb_ip_address
        if lb_port is not None:
            self.lb_port = lb_port
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if dr_instance_id is not None:
            self.dr_instance_id = dr_instance_id
        if dual_active_info is not None:
            self.dual_active_info = dual_active_info
        if ccm_cert_info is not None:
            self.ccm_cert_info = ccm_cert_info
        self.ssl = ssl
        if backup_space_usage is not None:
            self.backup_space_usage = backup_space_usage

    @property
    def id(self):
        r"""Gets the id of this ListInstancesResult.

        **参数解释：** 实例ID。 **取值范围：** 不涉及。

        :return: The id of this ListInstancesResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListInstancesResult.

        **参数解释：** 实例ID。 **取值范围：** 不涉及。

        :param id: The id of this ListInstancesResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListInstancesResult.

        **参数解释：** 实例名称。 **取值范围：** 不涉及。

        :return: The name of this ListInstancesResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListInstancesResult.

        **参数解释：** 实例名称。 **取值范围：** 不涉及。

        :param name: The name of this ListInstancesResult.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListInstancesResult.

        **参数解释：** 实例状态。 **取值范围：** - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示实例磁盘已满。 - createfail，表示实例创建失败。 - enlargefail，表示实例扩容节点个数失败。

        :return: The status of this ListInstancesResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListInstancesResult.

        **参数解释：** 实例状态。 **取值范围：** - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示实例磁盘已满。 - createfail，表示实例创建失败。 - enlargefail，表示实例扩容节点个数失败。

        :param status: The status of this ListInstancesResult.
        :type status: str
        """
        self._status = status

    @property
    def port(self):
        r"""Gets the port of this ListInstancesResult.

        **参数解释：** 数据库端口。 **取值范围：** 不涉及。

        :return: The port of this ListInstancesResult.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ListInstancesResult.

        **参数解释：** 数据库端口。 **取值范围：** 不涉及。

        :param port: The port of this ListInstancesResult.
        :type port: str
        """
        self._port = port

    @property
    def region(self):
        r"""Gets the region of this ListInstancesResult.

        **参数解释：** 实例所在区域。 **取值范围：** 不涉及。

        :return: The region of this ListInstancesResult.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListInstancesResult.

        **参数解释：** 实例所在区域。 **取值范围：** 不涉及。

        :param region: The region of this ListInstancesResult.
        :type region: str
        """
        self._region = region

    @property
    def datastore(self):
        r"""Gets the datastore of this ListInstancesResult.

        :return: The datastore of this ListInstancesResult.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesDatastoreResult`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this ListInstancesResult.

        :param datastore: The datastore of this ListInstancesResult.
        :type datastore: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesDatastoreResult`
        """
        self._datastore = datastore

    @property
    def mode(self):
        r"""Gets the mode of this ListInstancesResult.

        **参数解释：** 实例类型。 **取值范围：** 与请求参数相同。

        :return: The mode of this ListInstancesResult.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ListInstancesResult.

        **参数解释：** 实例类型。 **取值范围：** 与请求参数相同。

        :param mode: The mode of this ListInstancesResult.
        :type mode: str
        """
        self._mode = mode

    @property
    def product_type(self):
        r"""Gets the product_type of this ListInstancesResult.

        **参数解释：** 产品类型。 **取值范围：** GeminiDB Redis云原生部署模式集群涉及此字段，取值：   -  Standard 标准型   -  Capacity 容量型

        :return: The product_type of this ListInstancesResult.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        r"""Sets the product_type of this ListInstancesResult.

        **参数解释：** 产品类型。 **取值范围：** GeminiDB Redis云原生部署模式集群涉及此字段，取值：   -  Standard 标准型   -  Capacity 容量型

        :param product_type: The product_type of this ListInstancesResult.
        :type product_type: str
        """
        self._product_type = product_type

    @property
    def engine(self):
        r"""Gets the engine of this ListInstancesResult.

        **参数解释：** 存储引擎。 **取值范围：** 取值为“rocksDB”。

        :return: The engine of this ListInstancesResult.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ListInstancesResult.

        **参数解释：** 存储引擎。 **取值范围：** 取值为“rocksDB”。

        :param engine: The engine of this ListInstancesResult.
        :type engine: str
        """
        self._engine = engine

    @property
    def created(self):
        r"""Gets the created of this ListInstancesResult.

        **参数解释：** 实例创建时间。 **取值范围：** 不涉及。

        :return: The created of this ListInstancesResult.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ListInstancesResult.

        **参数解释：** 实例创建时间。 **取值范围：** 不涉及。

        :param created: The created of this ListInstancesResult.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ListInstancesResult.

        **参数解释：** 实例操作最新变更的时间。 **取值范围：** 不涉及。

        :return: The updated of this ListInstancesResult.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ListInstancesResult.

        **参数解释：** 实例操作最新变更的时间。 **取值范围：** 不涉及。

        :param updated: The updated of this ListInstancesResult.
        :type updated: str
        """
        self._updated = updated

    @property
    def db_user_name(self):
        r"""Gets the db_user_name of this ListInstancesResult.

        **参数解释：** 默认用户名。 **取值范围：** 取值为“rwuser”。

        :return: The db_user_name of this ListInstancesResult.
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        r"""Sets the db_user_name of this ListInstancesResult.

        **参数解释：** 默认用户名。 **取值范围：** 取值为“rwuser”。

        :param db_user_name: The db_user_name of this ListInstancesResult.
        :type db_user_name: str
        """
        self._db_user_name = db_user_name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListInstancesResult.

        **参数解释：** 虚拟私有云ID。 **取值范围：** 不涉及。

        :return: The vpc_id of this ListInstancesResult.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListInstancesResult.

        **参数解释：** 虚拟私有云ID。 **取值范围：** 不涉及。

        :param vpc_id: The vpc_id of this ListInstancesResult.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ListInstancesResult.

        **参数解释：** 子网ID。 **取值范围：** GeminiDB Cassandra 实例使用多个子网的场景，请参见表 ListInstancesNodeResult字段数据结构说明中的“subnet_id”。

        :return: The subnet_id of this ListInstancesResult.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ListInstancesResult.

        **参数解释：** 子网ID。 **取值范围：** GeminiDB Cassandra 实例使用多个子网的场景，请参见表 ListInstancesNodeResult字段数据结构说明中的“subnet_id”。

        :param subnet_id: The subnet_id of this ListInstancesResult.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this ListInstancesResult.

        **参数解释：** 安全组ID。 **取值范围：** 不涉及。

        :return: The security_group_id of this ListInstancesResult.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this ListInstancesResult.

        **参数解释：** 安全组ID。 **取值范围：** 不涉及。

        :param security_group_id: The security_group_id of this ListInstancesResult.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def backup_strategy(self):
        r"""Gets the backup_strategy of this ListInstancesResult.

        :return: The backup_strategy of this ListInstancesResult.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesBackupStrategyResult`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        r"""Sets the backup_strategy of this ListInstancesResult.

        :param backup_strategy: The backup_strategy of this ListInstancesResult.
        :type backup_strategy: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesBackupStrategyResult`
        """
        self._backup_strategy = backup_strategy

    @property
    def pay_mode(self):
        r"""Gets the pay_mode of this ListInstancesResult.

        **参数解释：** 计费方式。 **取值范围：** - 取值为“0”，表示按需计费。 - 取值为“1”，表示包年/包月计费。

        :return: The pay_mode of this ListInstancesResult.
        :rtype: str
        """
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, pay_mode):
        r"""Sets the pay_mode of this ListInstancesResult.

        **参数解释：** 计费方式。 **取值范围：** - 取值为“0”，表示按需计费。 - 取值为“1”，表示包年/包月计费。

        :param pay_mode: The pay_mode of this ListInstancesResult.
        :type pay_mode: str
        """
        self._pay_mode = pay_mode

    @property
    def maintenance_window(self):
        r"""Gets the maintenance_window of this ListInstancesResult.

        **参数解释：** 系统可维护时间窗。 **取值范围：** 不涉及。

        :return: The maintenance_window of this ListInstancesResult.
        :rtype: str
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        r"""Sets the maintenance_window of this ListInstancesResult.

        **参数解释：** 系统可维护时间窗。 **取值范围：** 不涉及。

        :param maintenance_window: The maintenance_window of this ListInstancesResult.
        :type maintenance_window: str
        """
        self._maintenance_window = maintenance_window

    @property
    def groups(self):
        r"""Gets the groups of this ListInstancesResult.

        **参数解释：** 组信息。 **取值范围：** 不涉及。

        :return: The groups of this ListInstancesResult.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesGroupResult`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this ListInstancesResult.

        **参数解释：** 组信息。 **取值范围：** 不涉及。

        :param groups: The groups of this ListInstancesResult.
        :type groups: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesGroupResult`]
        """
        self._groups = groups

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListInstancesResult.

        **参数解释：** 企业项目ID。 **取值范围：** 取值为“0”，表示为default企业项目。

        :return: The enterprise_project_id of this ListInstancesResult.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListInstancesResult.

        **参数解释：** 企业项目ID。 **取值范围：** 取值为“0”，表示为default企业项目。

        :param enterprise_project_id: The enterprise_project_id of this ListInstancesResult.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def dedicated_resource_id(self):
        r"""Gets the dedicated_resource_id of this ListInstancesResult.

        **参数解释：** 专属资源ID。只有数据库实例属于专属资源池才会返回该参数。 **取值范围：** 不涉及。

        :return: The dedicated_resource_id of this ListInstancesResult.
        :rtype: str
        """
        return self._dedicated_resource_id

    @dedicated_resource_id.setter
    def dedicated_resource_id(self, dedicated_resource_id):
        r"""Sets the dedicated_resource_id of this ListInstancesResult.

        **参数解释：** 专属资源ID。只有数据库实例属于专属资源池才会返回该参数。 **取值范围：** 不涉及。

        :param dedicated_resource_id: The dedicated_resource_id of this ListInstancesResult.
        :type dedicated_resource_id: str
        """
        self._dedicated_resource_id = dedicated_resource_id

    @property
    def time_zone(self):
        r"""Gets the time_zone of this ListInstancesResult.

        **参数解释：** 时区。 **取值范围：** 不涉及。

        :return: The time_zone of this ListInstancesResult.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this ListInstancesResult.

        **参数解释：** 时区。 **取值范围：** 不涉及。

        :param time_zone: The time_zone of this ListInstancesResult.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def actions(self):
        r"""Gets the actions of this ListInstancesResult.

        **参数解释：** 实例正在执行的动作。 **取值范围：** 不涉及。

        :return: The actions of this ListInstancesResult.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this ListInstancesResult.

        **参数解释：** 实例正在执行的动作。 **取值范围：** 不涉及。

        :param actions: The actions of this ListInstancesResult.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def disk_encryption_id(self):
        r"""Gets the disk_encryption_id of this ListInstancesResult.

        **参数解释：** 磁盘加密时的密钥ID。 **取值范围：** 不涉及。

        :return: The disk_encryption_id of this ListInstancesResult.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        r"""Sets the disk_encryption_id of this ListInstancesResult.

        **参数解释：** 磁盘加密时的密钥ID。 **取值范围：** 不涉及。

        :param disk_encryption_id: The disk_encryption_id of this ListInstancesResult.
        :type disk_encryption_id: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def lb_ip_address(self):
        r"""Gets the lb_ip_address of this ListInstancesResult.

        **参数解释：** 负载均衡ip。 **取值范围：** 只有存在负载均衡ip，才会返回该参数。

        :return: The lb_ip_address of this ListInstancesResult.
        :rtype: str
        """
        return self._lb_ip_address

    @lb_ip_address.setter
    def lb_ip_address(self, lb_ip_address):
        r"""Sets the lb_ip_address of this ListInstancesResult.

        **参数解释：** 负载均衡ip。 **取值范围：** 只有存在负载均衡ip，才会返回该参数。

        :param lb_ip_address: The lb_ip_address of this ListInstancesResult.
        :type lb_ip_address: str
        """
        self._lb_ip_address = lb_ip_address

    @property
    def lb_port(self):
        r"""Gets the lb_port of this ListInstancesResult.

        **参数解释：** 负载均衡端口。 **取值范围：** 只有存在负载均衡ip，才会返回该参数。

        :return: The lb_port of this ListInstancesResult.
        :rtype: str
        """
        return self._lb_port

    @lb_port.setter
    def lb_port(self, lb_port):
        r"""Sets the lb_port of this ListInstancesResult.

        **参数解释：** 负载均衡端口。 **取值范围：** 只有存在负载均衡ip，才会返回该参数。

        :param lb_port: The lb_port of this ListInstancesResult.
        :type lb_port: str
        """
        self._lb_port = lb_port

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListInstancesResult.

        **参数解释：** 实例可用区。 **取值范围：** 不涉及。

        :return: The availability_zone of this ListInstancesResult.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListInstancesResult.

        **参数解释：** 实例可用区。 **取值范围：** 不涉及。

        :param availability_zone: The availability_zone of this ListInstancesResult.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def dr_instance_id(self):
        r"""Gets the dr_instance_id of this ListInstancesResult.

        **参数解释：** 容灾实例ID。 **取值范围：** 不涉及。

        :return: The dr_instance_id of this ListInstancesResult.
        :rtype: str
        """
        return self._dr_instance_id

    @dr_instance_id.setter
    def dr_instance_id(self, dr_instance_id):
        r"""Sets the dr_instance_id of this ListInstancesResult.

        **参数解释：** 容灾实例ID。 **取值范围：** 不涉及。

        :param dr_instance_id: The dr_instance_id of this ListInstancesResult.
        :type dr_instance_id: str
        """
        self._dr_instance_id = dr_instance_id

    @property
    def dual_active_info(self):
        r"""Gets the dual_active_info of this ListInstancesResult.

        :return: The dual_active_info of this ListInstancesResult.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DualActiveInfo`
        """
        return self._dual_active_info

    @dual_active_info.setter
    def dual_active_info(self, dual_active_info):
        r"""Sets the dual_active_info of this ListInstancesResult.

        :param dual_active_info: The dual_active_info of this ListInstancesResult.
        :type dual_active_info: :class:`huaweicloudsdkgaussdbfornosql.v3.DualActiveInfo`
        """
        self._dual_active_info = dual_active_info

    @property
    def ccm_cert_info(self):
        r"""Gets the ccm_cert_info of this ListInstancesResult.

        :return: The ccm_cert_info of this ListInstancesResult.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CertInfoOption`
        """
        return self._ccm_cert_info

    @ccm_cert_info.setter
    def ccm_cert_info(self, ccm_cert_info):
        r"""Sets the ccm_cert_info of this ListInstancesResult.

        :param ccm_cert_info: The ccm_cert_info of this ListInstancesResult.
        :type ccm_cert_info: :class:`huaweicloudsdkgaussdbfornosql.v3.CertInfoOption`
        """
        self._ccm_cert_info = ccm_cert_info

    @property
    def ssl(self):
        r"""Gets the ssl of this ListInstancesResult.

        **参数解释：** SSL安全连接启用情况。 **取值范围：** - 取值为“0”表示未启用。 - 取值为“1”表示已启用。

        :return: The ssl of this ListInstancesResult.
        :rtype: str
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        r"""Sets the ssl of this ListInstancesResult.

        **参数解释：** SSL安全连接启用情况。 **取值范围：** - 取值为“0”表示未启用。 - 取值为“1”表示已启用。

        :param ssl: The ssl of this ListInstancesResult.
        :type ssl: str
        """
        self._ssl = ssl

    @property
    def backup_space_usage(self):
        r"""Gets the backup_space_usage of this ListInstancesResult.

        :return: The backup_space_usage of this ListInstancesResult.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.BackupSpaceUsage`
        """
        return self._backup_space_usage

    @backup_space_usage.setter
    def backup_space_usage(self, backup_space_usage):
        r"""Sets the backup_space_usage of this ListInstancesResult.

        :param backup_space_usage: The backup_space_usage of this ListInstancesResult.
        :type backup_space_usage: :class:`huaweicloudsdkgaussdbfornosql.v3.BackupSpaceUsage`
        """
        self._backup_space_usage = backup_space_usage

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListInstancesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
