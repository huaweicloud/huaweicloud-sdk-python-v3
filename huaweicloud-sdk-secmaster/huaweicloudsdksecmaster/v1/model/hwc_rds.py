# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HwcRds:

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
        'protected_status': 'str',
        'status': 'str',
        'alias': 'str',
        'private_ips': 'list[str]',
        'private_dns_names': 'list[str]',
        'public_ips': 'list[str]',
        'port': 'int',
        'enable_ssl': 'bool',
        'type': 'str',
        'ha': 'HwcRdsHa',
        'region': 'str',
        'datastore': 'HwcRdsDatastore',
        'created': 'str',
        'updated': 'str',
        'db_user_name': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'flavor_ref': 'str',
        'cpu': 'str',
        'mem': 'str',
        'volume': 'HwcRdsVolume',
        'tags': 'list[Tag]',
        'enterprise_project_id': 'str',
        'project_id': 'str',
        'switch_strategy': 'str',
        'read_only_by_user': 'bool',
        'backup_strategy': 'HwcRdsBackupStrategy',
        'maintenance_window': 'str',
        'nodes': 'list[HwcRdsNode]',
        'related_instance': 'list[HwcRdsRelatedInstance]',
        'disk_encryption_id': 'str',
        'time_zone': 'str',
        'backup_used_space': 'float',
        'storage_used_space': 'float',
        'associated_with_ddm': 'bool',
        'max_iops': 'int',
        'expiration_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'protected_status': 'protected_status',
        'status': 'status',
        'alias': 'alias',
        'private_ips': 'private_ips',
        'private_dns_names': 'private_dns_names',
        'public_ips': 'public_ips',
        'port': 'port',
        'enable_ssl': 'enable_ssl',
        'type': 'type',
        'ha': 'ha',
        'region': 'region',
        'datastore': 'datastore',
        'created': 'created',
        'updated': 'updated',
        'db_user_name': 'db_user_name',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'flavor_ref': 'flavor_ref',
        'cpu': 'cpu',
        'mem': 'mem',
        'volume': 'volume',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'project_id': 'project_id',
        'switch_strategy': 'switch_strategy',
        'read_only_by_user': 'read_only_by_user',
        'backup_strategy': 'backup_strategy',
        'maintenance_window': 'maintenance_window',
        'nodes': 'nodes',
        'related_instance': 'related_instance',
        'disk_encryption_id': 'disk_encryption_id',
        'time_zone': 'time_zone',
        'backup_used_space': 'backup_used_space',
        'storage_used_space': 'storage_used_space',
        'associated_with_ddm': 'associated_with_ddm',
        'max_iops': 'max_iops',
        'expiration_time': 'expiration_time'
    }

    def __init__(self, id=None, name=None, protected_status=None, status=None, alias=None, private_ips=None, private_dns_names=None, public_ips=None, port=None, enable_ssl=None, type=None, ha=None, region=None, datastore=None, created=None, updated=None, db_user_name=None, vpc_id=None, subnet_id=None, security_group_id=None, flavor_ref=None, cpu=None, mem=None, volume=None, tags=None, enterprise_project_id=None, project_id=None, switch_strategy=None, read_only_by_user=None, backup_strategy=None, maintenance_window=None, nodes=None, related_instance=None, disk_encryption_id=None, time_zone=None, backup_used_space=None, storage_used_space=None, associated_with_ddm=None, max_iops=None, expiration_time=None):
        r"""HwcRds

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 创建的实例名称。
        :type name: str
        :param protected_status: DBSS开启状态：OPEN | CLOSE
        :type protected_status: str
        :param status: 实例状态。 取值： 值为“BUILD”，表示实例正在创建。 值为“ACTIVE”，表示实例正常。 值为“FAILED”，表示实例异常。 值为“FROZEN”，表示实例冻结。 值为“MODIFYING”，表示实例正在扩容。 值为“REBOOTING”，表示实例正在重启。 值为“RESTORING”，表示实例正在恢复。 值为“MODIFYING INSTANCE TYPE”，表示实例正在转主备。 值为“SWITCHOVER”，表示实例正在主备切换。 值为“MIGRATING”，表示实例正在迁移。 值为“BACKING UP”，表示实例正在进行备份。 值为“MODIFYING DATABASE PORT”，表示实例正在修改数据库端口。 值为“STORAGE FULL”，表示实例磁盘空间满。
        :type status: str
        :param alias: 实例的备注信息。
        :type alias: str
        :param private_ips: 实例内网IP地址列表。弹性云服务器创建成功后该值存在，其他情况下为空字符串。
        :type private_ips: list[str]
        :param private_dns_names: 实例内网域名列表。实例创建成功后，需要手动申请内网域名，否则查询内网域名为空。
        :type private_dns_names: list[str]
        :param public_ips: 实例外网IP地址列表。
        :type public_ips: list[str]
        :param port: 数据库端口号。 RDS for MySQL数据库端口设置范围为1024～65535（其中12017和33071被RDS系统占用不可设置）。 RDS for PostgreSQL数据库端口修改范围为2100～9500。 RDS for SQL Server实例的端口设置范围为1433和2100~9500（其中5355和5985不可设置。对于2017 EE、2017 SE、2017 Web版，5050、5353和5986不可设置）。 当不传该参数时，默认端口如下：  RDS for MySQL默认3306。 RDS for PostgreSQL默认5432。 RDS for SQL Server默认1433。
        :type port: int
        :param enable_ssl: 实例开启SSL标志。 取值为“true”：表示实例已开启SSL。 取值为“false”：表示实例未开启SSL。
        :type enable_ssl: bool
        :param type: 实例类型，取值为“Single”，“Ha”或“Replica”, \&quot;Enterprise\&quot;，分别对应于单机实例、主备实例、只读实例、分布式实例（企业版）。
        :type type: str
        :param ha: 
        :type ha: :class:`huaweicloudsdksecmaster.v1.HwcRdsHa`
        :param region: 实例所在区域。
        :type region: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdksecmaster.v1.HwcRdsDatastore`
        :param created: 创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。 说明：创建时返回值为空，数据库实例创建成功后该值不为空。
        :type created: str
        :param updated: 更新时间，格式与“created”字段对应格式完全相同。 说明：创建时返回值为空，数据库实例创建成功后该值不为空。
        :type updated: str
        :param db_user_name: 默认用户名。
        :type db_user_name: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 子网的网络ID信息。
        :type subnet_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param flavor_ref: 规格码。
        :type flavor_ref: str
        :param cpu: CPU大小。例如，1表示1U。
        :type cpu: str
        :param mem: 内存大小（单位：GB）。
        :type mem: str
        :param volume: 
        :type volume: :class:`huaweicloudsdksecmaster.v1.HwcRdsVolume`
        :param tags: 标签列表，没有标签默认为空数组。
        :type tags: list[:class:`huaweicloudsdksecmaster.v1.Tag`]
        :param enterprise_project_id: 企业项目标签ID。
        :type enterprise_project_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param switch_strategy: 数据库切换策略。取值为“reliability”或“availability”，分别对应于可靠性优先和可用性优先。
        :type switch_strategy: str
        :param read_only_by_user: 用户设置的实例只读状态。仅支持RDS for MySQL引擎。 true，表示该实例被设置为只读状态。 false，表示该实例未被设置为只读状态。
        :type read_only_by_user: bool
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdksecmaster.v1.HwcRdsBackupStrategy`
        :param maintenance_window: 可维护时间窗，为UTC时间。
        :type maintenance_window: str
        :param nodes: 主备实例信息
        :type nodes: list[:class:`huaweicloudsdksecmaster.v1.HwcRdsNode`]
        :param related_instance: 所关联的数据库实例列表。
        :type related_instance: list[:class:`huaweicloudsdksecmaster.v1.HwcRdsRelatedInstance`]
        :param disk_encryption_id: 磁盘加密密钥ID。
        :type disk_encryption_id: str
        :param time_zone: 时区。
        :type time_zone: str
        :param backup_used_space: 备份空间使用量，单位GB。 该字段仅用于查询指定RDS for SQL Server单个实例信息时返回。
        :type backup_used_space: float
        :param storage_used_space: 磁盘空间使用量，单位GB。 该字段仅用于查询指定RDS for SQL Server单个实例信息时返回。
        :type storage_used_space: float
        :param associated_with_ddm: 是否已被DDM实例关联。
        :type associated_with_ddm: bool
        :param max_iops: 实例磁盘的最大IOPS值。 当前该字段仅对于SQL Server引擎实例返回。
        :type max_iops: int
        :param expiration_time: 实例的到期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 仅包周期场景返回。
        :type expiration_time: str
        """
        
        

        self._id = None
        self._name = None
        self._protected_status = None
        self._status = None
        self._alias = None
        self._private_ips = None
        self._private_dns_names = None
        self._public_ips = None
        self._port = None
        self._enable_ssl = None
        self._type = None
        self._ha = None
        self._region = None
        self._datastore = None
        self._created = None
        self._updated = None
        self._db_user_name = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._flavor_ref = None
        self._cpu = None
        self._mem = None
        self._volume = None
        self._tags = None
        self._enterprise_project_id = None
        self._project_id = None
        self._switch_strategy = None
        self._read_only_by_user = None
        self._backup_strategy = None
        self._maintenance_window = None
        self._nodes = None
        self._related_instance = None
        self._disk_encryption_id = None
        self._time_zone = None
        self._backup_used_space = None
        self._storage_used_space = None
        self._associated_with_ddm = None
        self._max_iops = None
        self._expiration_time = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.protected_status = protected_status
        self.status = status
        if alias is not None:
            self.alias = alias
        if private_ips is not None:
            self.private_ips = private_ips
        if private_dns_names is not None:
            self.private_dns_names = private_dns_names
        if public_ips is not None:
            self.public_ips = public_ips
        self.port = port
        self.enable_ssl = enable_ssl
        self.type = type
        self.ha = ha
        self.region = region
        self.datastore = datastore
        self.created = created
        if updated is not None:
            self.updated = updated
        if db_user_name is not None:
            self.db_user_name = db_user_name
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.flavor_ref = flavor_ref
        self.cpu = cpu
        self.mem = mem
        self.volume = volume
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.project_id = project_id
        self.switch_strategy = switch_strategy
        self.read_only_by_user = read_only_by_user
        self.backup_strategy = backup_strategy
        self.maintenance_window = maintenance_window
        self.nodes = nodes
        self.related_instance = related_instance
        if disk_encryption_id is not None:
            self.disk_encryption_id = disk_encryption_id
        self.time_zone = time_zone
        if backup_used_space is not None:
            self.backup_used_space = backup_used_space
        self.storage_used_space = storage_used_space
        self.associated_with_ddm = associated_with_ddm
        self.max_iops = max_iops
        self.expiration_time = expiration_time

    @property
    def id(self):
        r"""Gets the id of this HwcRds.

        实例ID。

        :return: The id of this HwcRds.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HwcRds.

        实例ID。

        :param id: The id of this HwcRds.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this HwcRds.

        创建的实例名称。

        :return: The name of this HwcRds.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HwcRds.

        创建的实例名称。

        :param name: The name of this HwcRds.
        :type name: str
        """
        self._name = name

    @property
    def protected_status(self):
        r"""Gets the protected_status of this HwcRds.

        DBSS开启状态：OPEN | CLOSE

        :return: The protected_status of this HwcRds.
        :rtype: str
        """
        return self._protected_status

    @protected_status.setter
    def protected_status(self, protected_status):
        r"""Sets the protected_status of this HwcRds.

        DBSS开启状态：OPEN | CLOSE

        :param protected_status: The protected_status of this HwcRds.
        :type protected_status: str
        """
        self._protected_status = protected_status

    @property
    def status(self):
        r"""Gets the status of this HwcRds.

        实例状态。 取值： 值为“BUILD”，表示实例正在创建。 值为“ACTIVE”，表示实例正常。 值为“FAILED”，表示实例异常。 值为“FROZEN”，表示实例冻结。 值为“MODIFYING”，表示实例正在扩容。 值为“REBOOTING”，表示实例正在重启。 值为“RESTORING”，表示实例正在恢复。 值为“MODIFYING INSTANCE TYPE”，表示实例正在转主备。 值为“SWITCHOVER”，表示实例正在主备切换。 值为“MIGRATING”，表示实例正在迁移。 值为“BACKING UP”，表示实例正在进行备份。 值为“MODIFYING DATABASE PORT”，表示实例正在修改数据库端口。 值为“STORAGE FULL”，表示实例磁盘空间满。

        :return: The status of this HwcRds.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HwcRds.

        实例状态。 取值： 值为“BUILD”，表示实例正在创建。 值为“ACTIVE”，表示实例正常。 值为“FAILED”，表示实例异常。 值为“FROZEN”，表示实例冻结。 值为“MODIFYING”，表示实例正在扩容。 值为“REBOOTING”，表示实例正在重启。 值为“RESTORING”，表示实例正在恢复。 值为“MODIFYING INSTANCE TYPE”，表示实例正在转主备。 值为“SWITCHOVER”，表示实例正在主备切换。 值为“MIGRATING”，表示实例正在迁移。 值为“BACKING UP”，表示实例正在进行备份。 值为“MODIFYING DATABASE PORT”，表示实例正在修改数据库端口。 值为“STORAGE FULL”，表示实例磁盘空间满。

        :param status: The status of this HwcRds.
        :type status: str
        """
        self._status = status

    @property
    def alias(self):
        r"""Gets the alias of this HwcRds.

        实例的备注信息。

        :return: The alias of this HwcRds.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this HwcRds.

        实例的备注信息。

        :param alias: The alias of this HwcRds.
        :type alias: str
        """
        self._alias = alias

    @property
    def private_ips(self):
        r"""Gets the private_ips of this HwcRds.

        实例内网IP地址列表。弹性云服务器创建成功后该值存在，其他情况下为空字符串。

        :return: The private_ips of this HwcRds.
        :rtype: list[str]
        """
        return self._private_ips

    @private_ips.setter
    def private_ips(self, private_ips):
        r"""Sets the private_ips of this HwcRds.

        实例内网IP地址列表。弹性云服务器创建成功后该值存在，其他情况下为空字符串。

        :param private_ips: The private_ips of this HwcRds.
        :type private_ips: list[str]
        """
        self._private_ips = private_ips

    @property
    def private_dns_names(self):
        r"""Gets the private_dns_names of this HwcRds.

        实例内网域名列表。实例创建成功后，需要手动申请内网域名，否则查询内网域名为空。

        :return: The private_dns_names of this HwcRds.
        :rtype: list[str]
        """
        return self._private_dns_names

    @private_dns_names.setter
    def private_dns_names(self, private_dns_names):
        r"""Sets the private_dns_names of this HwcRds.

        实例内网域名列表。实例创建成功后，需要手动申请内网域名，否则查询内网域名为空。

        :param private_dns_names: The private_dns_names of this HwcRds.
        :type private_dns_names: list[str]
        """
        self._private_dns_names = private_dns_names

    @property
    def public_ips(self):
        r"""Gets the public_ips of this HwcRds.

        实例外网IP地址列表。

        :return: The public_ips of this HwcRds.
        :rtype: list[str]
        """
        return self._public_ips

    @public_ips.setter
    def public_ips(self, public_ips):
        r"""Sets the public_ips of this HwcRds.

        实例外网IP地址列表。

        :param public_ips: The public_ips of this HwcRds.
        :type public_ips: list[str]
        """
        self._public_ips = public_ips

    @property
    def port(self):
        r"""Gets the port of this HwcRds.

        数据库端口号。 RDS for MySQL数据库端口设置范围为1024～65535（其中12017和33071被RDS系统占用不可设置）。 RDS for PostgreSQL数据库端口修改范围为2100～9500。 RDS for SQL Server实例的端口设置范围为1433和2100~9500（其中5355和5985不可设置。对于2017 EE、2017 SE、2017 Web版，5050、5353和5986不可设置）。 当不传该参数时，默认端口如下：  RDS for MySQL默认3306。 RDS for PostgreSQL默认5432。 RDS for SQL Server默认1433。

        :return: The port of this HwcRds.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this HwcRds.

        数据库端口号。 RDS for MySQL数据库端口设置范围为1024～65535（其中12017和33071被RDS系统占用不可设置）。 RDS for PostgreSQL数据库端口修改范围为2100～9500。 RDS for SQL Server实例的端口设置范围为1433和2100~9500（其中5355和5985不可设置。对于2017 EE、2017 SE、2017 Web版，5050、5353和5986不可设置）。 当不传该参数时，默认端口如下：  RDS for MySQL默认3306。 RDS for PostgreSQL默认5432。 RDS for SQL Server默认1433。

        :param port: The port of this HwcRds.
        :type port: int
        """
        self._port = port

    @property
    def enable_ssl(self):
        r"""Gets the enable_ssl of this HwcRds.

        实例开启SSL标志。 取值为“true”：表示实例已开启SSL。 取值为“false”：表示实例未开启SSL。

        :return: The enable_ssl of this HwcRds.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        r"""Sets the enable_ssl of this HwcRds.

        实例开启SSL标志。 取值为“true”：表示实例已开启SSL。 取值为“false”：表示实例未开启SSL。

        :param enable_ssl: The enable_ssl of this HwcRds.
        :type enable_ssl: bool
        """
        self._enable_ssl = enable_ssl

    @property
    def type(self):
        r"""Gets the type of this HwcRds.

        实例类型，取值为“Single”，“Ha”或“Replica”, \"Enterprise\"，分别对应于单机实例、主备实例、只读实例、分布式实例（企业版）。

        :return: The type of this HwcRds.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HwcRds.

        实例类型，取值为“Single”，“Ha”或“Replica”, \"Enterprise\"，分别对应于单机实例、主备实例、只读实例、分布式实例（企业版）。

        :param type: The type of this HwcRds.
        :type type: str
        """
        self._type = type

    @property
    def ha(self):
        r"""Gets the ha of this HwcRds.

        :return: The ha of this HwcRds.
        :rtype: :class:`huaweicloudsdksecmaster.v1.HwcRdsHa`
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        r"""Sets the ha of this HwcRds.

        :param ha: The ha of this HwcRds.
        :type ha: :class:`huaweicloudsdksecmaster.v1.HwcRdsHa`
        """
        self._ha = ha

    @property
    def region(self):
        r"""Gets the region of this HwcRds.

        实例所在区域。

        :return: The region of this HwcRds.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this HwcRds.

        实例所在区域。

        :param region: The region of this HwcRds.
        :type region: str
        """
        self._region = region

    @property
    def datastore(self):
        r"""Gets the datastore of this HwcRds.

        :return: The datastore of this HwcRds.
        :rtype: :class:`huaweicloudsdksecmaster.v1.HwcRdsDatastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this HwcRds.

        :param datastore: The datastore of this HwcRds.
        :type datastore: :class:`huaweicloudsdksecmaster.v1.HwcRdsDatastore`
        """
        self._datastore = datastore

    @property
    def created(self):
        r"""Gets the created of this HwcRds.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。 说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :return: The created of this HwcRds.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this HwcRds.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。 说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :param created: The created of this HwcRds.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this HwcRds.

        更新时间，格式与“created”字段对应格式完全相同。 说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :return: The updated of this HwcRds.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this HwcRds.

        更新时间，格式与“created”字段对应格式完全相同。 说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :param updated: The updated of this HwcRds.
        :type updated: str
        """
        self._updated = updated

    @property
    def db_user_name(self):
        r"""Gets the db_user_name of this HwcRds.

        默认用户名。

        :return: The db_user_name of this HwcRds.
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        r"""Sets the db_user_name of this HwcRds.

        默认用户名。

        :param db_user_name: The db_user_name of this HwcRds.
        :type db_user_name: str
        """
        self._db_user_name = db_user_name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this HwcRds.

        虚拟私有云ID。

        :return: The vpc_id of this HwcRds.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this HwcRds.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this HwcRds.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this HwcRds.

        子网的网络ID信息。

        :return: The subnet_id of this HwcRds.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this HwcRds.

        子网的网络ID信息。

        :param subnet_id: The subnet_id of this HwcRds.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this HwcRds.

        安全组ID。

        :return: The security_group_id of this HwcRds.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this HwcRds.

        安全组ID。

        :param security_group_id: The security_group_id of this HwcRds.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this HwcRds.

        规格码。

        :return: The flavor_ref of this HwcRds.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this HwcRds.

        规格码。

        :param flavor_ref: The flavor_ref of this HwcRds.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def cpu(self):
        r"""Gets the cpu of this HwcRds.

        CPU大小。例如，1表示1U。

        :return: The cpu of this HwcRds.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this HwcRds.

        CPU大小。例如，1表示1U。

        :param cpu: The cpu of this HwcRds.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def mem(self):
        r"""Gets the mem of this HwcRds.

        内存大小（单位：GB）。

        :return: The mem of this HwcRds.
        :rtype: str
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        r"""Sets the mem of this HwcRds.

        内存大小（单位：GB）。

        :param mem: The mem of this HwcRds.
        :type mem: str
        """
        self._mem = mem

    @property
    def volume(self):
        r"""Gets the volume of this HwcRds.

        :return: The volume of this HwcRds.
        :rtype: :class:`huaweicloudsdksecmaster.v1.HwcRdsVolume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this HwcRds.

        :param volume: The volume of this HwcRds.
        :type volume: :class:`huaweicloudsdksecmaster.v1.HwcRdsVolume`
        """
        self._volume = volume

    @property
    def tags(self):
        r"""Gets the tags of this HwcRds.

        标签列表，没有标签默认为空数组。

        :return: The tags of this HwcRds.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this HwcRds.

        标签列表，没有标签默认为空数组。

        :param tags: The tags of this HwcRds.
        :type tags: list[:class:`huaweicloudsdksecmaster.v1.Tag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this HwcRds.

        企业项目标签ID。

        :return: The enterprise_project_id of this HwcRds.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this HwcRds.

        企业项目标签ID。

        :param enterprise_project_id: The enterprise_project_id of this HwcRds.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def project_id(self):
        r"""Gets the project_id of this HwcRds.

        项目ID

        :return: The project_id of this HwcRds.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this HwcRds.

        项目ID

        :param project_id: The project_id of this HwcRds.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def switch_strategy(self):
        r"""Gets the switch_strategy of this HwcRds.

        数据库切换策略。取值为“reliability”或“availability”，分别对应于可靠性优先和可用性优先。

        :return: The switch_strategy of this HwcRds.
        :rtype: str
        """
        return self._switch_strategy

    @switch_strategy.setter
    def switch_strategy(self, switch_strategy):
        r"""Sets the switch_strategy of this HwcRds.

        数据库切换策略。取值为“reliability”或“availability”，分别对应于可靠性优先和可用性优先。

        :param switch_strategy: The switch_strategy of this HwcRds.
        :type switch_strategy: str
        """
        self._switch_strategy = switch_strategy

    @property
    def read_only_by_user(self):
        r"""Gets the read_only_by_user of this HwcRds.

        用户设置的实例只读状态。仅支持RDS for MySQL引擎。 true，表示该实例被设置为只读状态。 false，表示该实例未被设置为只读状态。

        :return: The read_only_by_user of this HwcRds.
        :rtype: bool
        """
        return self._read_only_by_user

    @read_only_by_user.setter
    def read_only_by_user(self, read_only_by_user):
        r"""Sets the read_only_by_user of this HwcRds.

        用户设置的实例只读状态。仅支持RDS for MySQL引擎。 true，表示该实例被设置为只读状态。 false，表示该实例未被设置为只读状态。

        :param read_only_by_user: The read_only_by_user of this HwcRds.
        :type read_only_by_user: bool
        """
        self._read_only_by_user = read_only_by_user

    @property
    def backup_strategy(self):
        r"""Gets the backup_strategy of this HwcRds.

        :return: The backup_strategy of this HwcRds.
        :rtype: :class:`huaweicloudsdksecmaster.v1.HwcRdsBackupStrategy`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        r"""Sets the backup_strategy of this HwcRds.

        :param backup_strategy: The backup_strategy of this HwcRds.
        :type backup_strategy: :class:`huaweicloudsdksecmaster.v1.HwcRdsBackupStrategy`
        """
        self._backup_strategy = backup_strategy

    @property
    def maintenance_window(self):
        r"""Gets the maintenance_window of this HwcRds.

        可维护时间窗，为UTC时间。

        :return: The maintenance_window of this HwcRds.
        :rtype: str
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        r"""Sets the maintenance_window of this HwcRds.

        可维护时间窗，为UTC时间。

        :param maintenance_window: The maintenance_window of this HwcRds.
        :type maintenance_window: str
        """
        self._maintenance_window = maintenance_window

    @property
    def nodes(self):
        r"""Gets the nodes of this HwcRds.

        主备实例信息

        :return: The nodes of this HwcRds.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.HwcRdsNode`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this HwcRds.

        主备实例信息

        :param nodes: The nodes of this HwcRds.
        :type nodes: list[:class:`huaweicloudsdksecmaster.v1.HwcRdsNode`]
        """
        self._nodes = nodes

    @property
    def related_instance(self):
        r"""Gets the related_instance of this HwcRds.

        所关联的数据库实例列表。

        :return: The related_instance of this HwcRds.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.HwcRdsRelatedInstance`]
        """
        return self._related_instance

    @related_instance.setter
    def related_instance(self, related_instance):
        r"""Sets the related_instance of this HwcRds.

        所关联的数据库实例列表。

        :param related_instance: The related_instance of this HwcRds.
        :type related_instance: list[:class:`huaweicloudsdksecmaster.v1.HwcRdsRelatedInstance`]
        """
        self._related_instance = related_instance

    @property
    def disk_encryption_id(self):
        r"""Gets the disk_encryption_id of this HwcRds.

        磁盘加密密钥ID。

        :return: The disk_encryption_id of this HwcRds.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        r"""Sets the disk_encryption_id of this HwcRds.

        磁盘加密密钥ID。

        :param disk_encryption_id: The disk_encryption_id of this HwcRds.
        :type disk_encryption_id: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def time_zone(self):
        r"""Gets the time_zone of this HwcRds.

        时区。

        :return: The time_zone of this HwcRds.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this HwcRds.

        时区。

        :param time_zone: The time_zone of this HwcRds.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def backup_used_space(self):
        r"""Gets the backup_used_space of this HwcRds.

        备份空间使用量，单位GB。 该字段仅用于查询指定RDS for SQL Server单个实例信息时返回。

        :return: The backup_used_space of this HwcRds.
        :rtype: float
        """
        return self._backup_used_space

    @backup_used_space.setter
    def backup_used_space(self, backup_used_space):
        r"""Sets the backup_used_space of this HwcRds.

        备份空间使用量，单位GB。 该字段仅用于查询指定RDS for SQL Server单个实例信息时返回。

        :param backup_used_space: The backup_used_space of this HwcRds.
        :type backup_used_space: float
        """
        self._backup_used_space = backup_used_space

    @property
    def storage_used_space(self):
        r"""Gets the storage_used_space of this HwcRds.

        磁盘空间使用量，单位GB。 该字段仅用于查询指定RDS for SQL Server单个实例信息时返回。

        :return: The storage_used_space of this HwcRds.
        :rtype: float
        """
        return self._storage_used_space

    @storage_used_space.setter
    def storage_used_space(self, storage_used_space):
        r"""Sets the storage_used_space of this HwcRds.

        磁盘空间使用量，单位GB。 该字段仅用于查询指定RDS for SQL Server单个实例信息时返回。

        :param storage_used_space: The storage_used_space of this HwcRds.
        :type storage_used_space: float
        """
        self._storage_used_space = storage_used_space

    @property
    def associated_with_ddm(self):
        r"""Gets the associated_with_ddm of this HwcRds.

        是否已被DDM实例关联。

        :return: The associated_with_ddm of this HwcRds.
        :rtype: bool
        """
        return self._associated_with_ddm

    @associated_with_ddm.setter
    def associated_with_ddm(self, associated_with_ddm):
        r"""Sets the associated_with_ddm of this HwcRds.

        是否已被DDM实例关联。

        :param associated_with_ddm: The associated_with_ddm of this HwcRds.
        :type associated_with_ddm: bool
        """
        self._associated_with_ddm = associated_with_ddm

    @property
    def max_iops(self):
        r"""Gets the max_iops of this HwcRds.

        实例磁盘的最大IOPS值。 当前该字段仅对于SQL Server引擎实例返回。

        :return: The max_iops of this HwcRds.
        :rtype: int
        """
        return self._max_iops

    @max_iops.setter
    def max_iops(self, max_iops):
        r"""Sets the max_iops of this HwcRds.

        实例磁盘的最大IOPS值。 当前该字段仅对于SQL Server引擎实例返回。

        :param max_iops: The max_iops of this HwcRds.
        :type max_iops: int
        """
        self._max_iops = max_iops

    @property
    def expiration_time(self):
        r"""Gets the expiration_time of this HwcRds.

        实例的到期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 仅包周期场景返回。

        :return: The expiration_time of this HwcRds.
        :rtype: str
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        r"""Sets the expiration_time of this HwcRds.

        实例的到期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 仅包周期场景返回。

        :param expiration_time: The expiration_time of this HwcRds.
        :type expiration_time: str
        """
        self._expiration_time = expiration_time

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
        if not isinstance(other, HwcRds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
