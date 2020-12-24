# coding: utf-8

import pprint
import re

import six





class InstanceResponse:


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
        'status': 'str',
        'private_ips': 'list[str]',
        'private_dns_names': 'list[str]',
        'public_ips': 'list[str]',
        'type': 'str',
        'created': 'str',
        'updated': 'str',
        'db_user_name': 'str',
        'switch_strategy': 'str',
        'maintenance_window': 'str',
        'nodes': 'list[NodeResponse]',
        'related_instance': 'list[RelatedInstance]',
        'name': 'str',
        'datastore': 'Datastore',
        'ha': 'HaResponse',
        'port': 'int',
        'backup_strategy': 'BackupStrategyForResponse',
        'enterprise_project_id': 'str',
        'disk_encryption_id': 'str',
        'flavor_ref': 'str',
        'volume': 'Volume',
        'region': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'charge_info': 'ChargeInfoResponse',
        'time_zone': 'str',
        'tags': 'list[TagResponse]',
        'backup_used_space': 'float',
        'storage_used_space': 'float',
        'order_id': 'str',
        'associated_with_ddm': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'private_ips': 'private_ips',
        'private_dns_names': 'private_dns_names',
        'public_ips': 'public_ips',
        'type': 'type',
        'created': 'created',
        'updated': 'updated',
        'db_user_name': 'db_user_name',
        'switch_strategy': 'switch_strategy',
        'maintenance_window': 'maintenance_window',
        'nodes': 'nodes',
        'related_instance': 'related_instance',
        'name': 'name',
        'datastore': 'datastore',
        'ha': 'ha',
        'port': 'port',
        'backup_strategy': 'backup_strategy',
        'enterprise_project_id': 'enterprise_project_id',
        'disk_encryption_id': 'disk_encryption_id',
        'flavor_ref': 'flavor_ref',
        'volume': 'volume',
        'region': 'region',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'charge_info': 'charge_info',
        'time_zone': 'time_zone',
        'tags': 'tags',
        'backup_used_space': 'backup_used_space',
        'storage_used_space': 'storage_used_space',
        'order_id': 'order_id',
        'associated_with_ddm': 'associated_with_ddm'
    }

    def __init__(self, id=None, status=None, private_ips=None, private_dns_names=None, public_ips=None, type=None, created=None, updated=None, db_user_name=None, switch_strategy=None, maintenance_window=None, nodes=None, related_instance=None, name=None, datastore=None, ha=None, port=None, backup_strategy=None, enterprise_project_id=None, disk_encryption_id=None, flavor_ref=None, volume=None, region=None, vpc_id=None, subnet_id=None, security_group_id=None, charge_info=None, time_zone=None, tags=None, backup_used_space=None, storage_used_space=None, order_id=None, associated_with_ddm=None):
        """InstanceResponse - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._status = None
        self._private_ips = None
        self._private_dns_names = None
        self._public_ips = None
        self._type = None
        self._created = None
        self._updated = None
        self._db_user_name = None
        self._switch_strategy = None
        self._maintenance_window = None
        self._nodes = None
        self._related_instance = None
        self._name = None
        self._datastore = None
        self._ha = None
        self._port = None
        self._backup_strategy = None
        self._enterprise_project_id = None
        self._disk_encryption_id = None
        self._flavor_ref = None
        self._volume = None
        self._region = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._charge_info = None
        self._time_zone = None
        self._tags = None
        self._backup_used_space = None
        self._storage_used_space = None
        self._order_id = None
        self._associated_with_ddm = None
        self.discriminator = None

        self.id = id
        self.status = status
        self.private_ips = private_ips
        if private_dns_names is not None:
            self.private_dns_names = private_dns_names
        self.public_ips = public_ips
        self.type = type
        self.created = created
        self.updated = updated
        self.db_user_name = db_user_name
        self.switch_strategy = switch_strategy
        self.maintenance_window = maintenance_window
        self.nodes = nodes
        self.related_instance = related_instance
        self.name = name
        self.datastore = datastore
        if ha is not None:
            self.ha = ha
        self.port = port
        self.backup_strategy = backup_strategy
        self.enterprise_project_id = enterprise_project_id
        self.disk_encryption_id = disk_encryption_id
        self.flavor_ref = flavor_ref
        self.volume = volume
        self.region = region
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.charge_info = charge_info
        self.time_zone = time_zone
        self.tags = tags
        if backup_used_space is not None:
            self.backup_used_space = backup_used_space
        if storage_used_space is not None:
            self.storage_used_space = storage_used_space
        if order_id is not None:
            self.order_id = order_id
        if associated_with_ddm is not None:
            self.associated_with_ddm = associated_with_ddm

    @property
    def id(self):
        """Gets the id of this InstanceResponse.

        实例ID。

        :return: The id of this InstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstanceResponse.

        实例ID。

        :param id: The id of this InstanceResponse.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this InstanceResponse.

        实例状态。 - 值为“BUILD”，表示实例正在创建。 - 值为“ACTIVE”，表示实例正常。 - 值为“FAILED”，表示实例异常。 - 值为“FROZEN”，表示实例冻结。 - 值为“MODIFYING”，表示实例正在扩容。 - 值为“REBOOTING”，表示实例正在重启。 - 值为“RESTORING”，表示实例正在恢复。 - 值为“MODIFYING INSTANCE TYPE”，表示实例正在转主备。 - 值为“SWITCHOVER”，表示实例正在主备切换。 - 值为“MIGRATING”，表示实例正在迁移。 - 值为“BACKING UP”，表示实例正在进行备份。 - 值为“MODIFYING DATABASE PORT”，表示实例正在修改数据库端口。 - 值为“STORAGE FULL”，表示实例磁盘空间满。

        :return: The status of this InstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstanceResponse.

        实例状态。 - 值为“BUILD”，表示实例正在创建。 - 值为“ACTIVE”，表示实例正常。 - 值为“FAILED”，表示实例异常。 - 值为“FROZEN”，表示实例冻结。 - 值为“MODIFYING”，表示实例正在扩容。 - 值为“REBOOTING”，表示实例正在重启。 - 值为“RESTORING”，表示实例正在恢复。 - 值为“MODIFYING INSTANCE TYPE”，表示实例正在转主备。 - 值为“SWITCHOVER”，表示实例正在主备切换。 - 值为“MIGRATING”，表示实例正在迁移。 - 值为“BACKING UP”，表示实例正在进行备份。 - 值为“MODIFYING DATABASE PORT”，表示实例正在修改数据库端口。 - 值为“STORAGE FULL”，表示实例磁盘空间满。

        :param status: The status of this InstanceResponse.
        :type: str
        """
        self._status = status

    @property
    def private_ips(self):
        """Gets the private_ips of this InstanceResponse.

        实例内网IP地址列表。弹性云服务器创建成功后该值存在，其他情况下为空字符串。

        :return: The private_ips of this InstanceResponse.
        :rtype: list[str]
        """
        return self._private_ips

    @private_ips.setter
    def private_ips(self, private_ips):
        """Sets the private_ips of this InstanceResponse.

        实例内网IP地址列表。弹性云服务器创建成功后该值存在，其他情况下为空字符串。

        :param private_ips: The private_ips of this InstanceResponse.
        :type: list[str]
        """
        self._private_ips = private_ips

    @property
    def private_dns_names(self):
        """Gets the private_dns_names of this InstanceResponse.


        :return: The private_dns_names of this InstanceResponse.
        :rtype: list[str]
        """
        return self._private_dns_names

    @private_dns_names.setter
    def private_dns_names(self, private_dns_names):
        """Sets the private_dns_names of this InstanceResponse.


        :param private_dns_names: The private_dns_names of this InstanceResponse.
        :type: list[str]
        """
        self._private_dns_names = private_dns_names

    @property
    def public_ips(self):
        """Gets the public_ips of this InstanceResponse.

        实例外网IP地址列表。

        :return: The public_ips of this InstanceResponse.
        :rtype: list[str]
        """
        return self._public_ips

    @public_ips.setter
    def public_ips(self, public_ips):
        """Sets the public_ips of this InstanceResponse.

        实例外网IP地址列表。

        :param public_ips: The public_ips of this InstanceResponse.
        :type: list[str]
        """
        self._public_ips = public_ips

    @property
    def type(self):
        """Gets the type of this InstanceResponse.

        实例类型，取值为“Single”，“Ha”或“Replica”，分别对应于单机实例、主备实例、只读实例。

        :return: The type of this InstanceResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InstanceResponse.

        实例类型，取值为“Single”，“Ha”或“Replica”，分别对应于单机实例、主备实例、只读实例。

        :param type: The type of this InstanceResponse.
        :type: str
        """
        self._type = type

    @property
    def created(self):
        """Gets the created of this InstanceResponse.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。  说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :return: The created of this InstanceResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this InstanceResponse.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。  说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :param created: The created of this InstanceResponse.
        :type: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this InstanceResponse.

        更新时间，格式与“created”字段对应格式完全相同。  说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :return: The updated of this InstanceResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this InstanceResponse.

        更新时间，格式与“created”字段对应格式完全相同。  说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :param updated: The updated of this InstanceResponse.
        :type: str
        """
        self._updated = updated

    @property
    def db_user_name(self):
        """Gets the db_user_name of this InstanceResponse.

        默认用户名。

        :return: The db_user_name of this InstanceResponse.
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        """Sets the db_user_name of this InstanceResponse.

        默认用户名。

        :param db_user_name: The db_user_name of this InstanceResponse.
        :type: str
        """
        self._db_user_name = db_user_name

    @property
    def switch_strategy(self):
        """Gets the switch_strategy of this InstanceResponse.

        数据库切换策略。取值为“reliability”或“availability”，分别对应于可靠性优先和可用性优先。

        :return: The switch_strategy of this InstanceResponse.
        :rtype: str
        """
        return self._switch_strategy

    @switch_strategy.setter
    def switch_strategy(self, switch_strategy):
        """Sets the switch_strategy of this InstanceResponse.

        数据库切换策略。取值为“reliability”或“availability”，分别对应于可靠性优先和可用性优先。

        :param switch_strategy: The switch_strategy of this InstanceResponse.
        :type: str
        """
        self._switch_strategy = switch_strategy

    @property
    def maintenance_window(self):
        """Gets the maintenance_window of this InstanceResponse.

        可维护时间窗，为UTC时间。

        :return: The maintenance_window of this InstanceResponse.
        :rtype: str
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """Sets the maintenance_window of this InstanceResponse.

        可维护时间窗，为UTC时间。

        :param maintenance_window: The maintenance_window of this InstanceResponse.
        :type: str
        """
        self._maintenance_window = maintenance_window

    @property
    def nodes(self):
        """Gets the nodes of this InstanceResponse.


        :return: The nodes of this InstanceResponse.
        :rtype: list[NodeResponse]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this InstanceResponse.


        :param nodes: The nodes of this InstanceResponse.
        :type: list[NodeResponse]
        """
        self._nodes = nodes

    @property
    def related_instance(self):
        """Gets the related_instance of this InstanceResponse.


        :return: The related_instance of this InstanceResponse.
        :rtype: list[RelatedInstance]
        """
        return self._related_instance

    @related_instance.setter
    def related_instance(self, related_instance):
        """Sets the related_instance of this InstanceResponse.


        :param related_instance: The related_instance of this InstanceResponse.
        :type: list[RelatedInstance]
        """
        self._related_instance = related_instance

    @property
    def name(self):
        """Gets the name of this InstanceResponse.

        实例名称。

        :return: The name of this InstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceResponse.

        实例名称。

        :param name: The name of this InstanceResponse.
        :type: str
        """
        self._name = name

    @property
    def datastore(self):
        """Gets the datastore of this InstanceResponse.


        :return: The datastore of this InstanceResponse.
        :rtype: Datastore
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this InstanceResponse.


        :param datastore: The datastore of this InstanceResponse.
        :type: Datastore
        """
        self._datastore = datastore

    @property
    def ha(self):
        """Gets the ha of this InstanceResponse.


        :return: The ha of this InstanceResponse.
        :rtype: HaResponse
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        """Sets the ha of this InstanceResponse.


        :param ha: The ha of this InstanceResponse.
        :type: HaResponse
        """
        self._ha = ha

    @property
    def port(self):
        """Gets the port of this InstanceResponse.

        数据库端口信息。  - MySQL数据库端口设置范围为1024～65535（其中12017和33071被RDS系统占用不可设置）。 - PostgreSQL数据库端口修改范围为2100～9500。 - Microsoft SQL Server实例的端口设置范围为1433和2100~9500（其中5355和5985不可设置。对于2017 EE版，5050、5353和5986不可设置）。  当不传该参数时，默认端口如下：  - MySQL默认3306。 - PostgreSQL默认5432。 - Microsoft SQL Server默认1433。

        :return: The port of this InstanceResponse.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this InstanceResponse.

        数据库端口信息。  - MySQL数据库端口设置范围为1024～65535（其中12017和33071被RDS系统占用不可设置）。 - PostgreSQL数据库端口修改范围为2100～9500。 - Microsoft SQL Server实例的端口设置范围为1433和2100~9500（其中5355和5985不可设置。对于2017 EE版，5050、5353和5986不可设置）。  当不传该参数时，默认端口如下：  - MySQL默认3306。 - PostgreSQL默认5432。 - Microsoft SQL Server默认1433。

        :param port: The port of this InstanceResponse.
        :type: int
        """
        self._port = port

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this InstanceResponse.


        :return: The backup_strategy of this InstanceResponse.
        :rtype: BackupStrategyForResponse
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this InstanceResponse.


        :param backup_strategy: The backup_strategy of this InstanceResponse.
        :type: BackupStrategyForResponse
        """
        self._backup_strategy = backup_strategy

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this InstanceResponse.

        企业项目ID。

        :return: The enterprise_project_id of this InstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this InstanceResponse.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this InstanceResponse.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def disk_encryption_id(self):
        """Gets the disk_encryption_id of this InstanceResponse.

        用于磁盘加密的密钥ID。

        :return: The disk_encryption_id of this InstanceResponse.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        """Sets the disk_encryption_id of this InstanceResponse.

        用于磁盘加密的密钥ID。

        :param disk_encryption_id: The disk_encryption_id of this InstanceResponse.
        :type: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this InstanceResponse.

        规格码。

        :return: The flavor_ref of this InstanceResponse.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this InstanceResponse.

        规格码。

        :param flavor_ref: The flavor_ref of this InstanceResponse.
        :type: str
        """
        self._flavor_ref = flavor_ref

    @property
    def volume(self):
        """Gets the volume of this InstanceResponse.


        :return: The volume of this InstanceResponse.
        :rtype: Volume
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this InstanceResponse.


        :param volume: The volume of this InstanceResponse.
        :type: Volume
        """
        self._volume = volume

    @property
    def region(self):
        """Gets the region of this InstanceResponse.

        区域ID。

        :return: The region of this InstanceResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this InstanceResponse.

        区域ID。

        :param region: The region of this InstanceResponse.
        :type: str
        """
        self._region = region

    @property
    def vpc_id(self):
        """Gets the vpc_id of this InstanceResponse.

        虚拟私有云ID。

        :return: The vpc_id of this InstanceResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this InstanceResponse.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this InstanceResponse.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this InstanceResponse.

        子网ID。

        :return: The subnet_id of this InstanceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this InstanceResponse.

        子网ID。

        :param subnet_id: The subnet_id of this InstanceResponse.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this InstanceResponse.

        安全组ID。

        :return: The security_group_id of this InstanceResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this InstanceResponse.

        安全组ID。

        :param security_group_id: The security_group_id of this InstanceResponse.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def charge_info(self):
        """Gets the charge_info of this InstanceResponse.


        :return: The charge_info of this InstanceResponse.
        :rtype: ChargeInfoResponse
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this InstanceResponse.


        :param charge_info: The charge_info of this InstanceResponse.
        :type: ChargeInfoResponse
        """
        self._charge_info = charge_info

    @property
    def time_zone(self):
        """Gets the time_zone of this InstanceResponse.

        时区。

        :return: The time_zone of this InstanceResponse.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this InstanceResponse.

        时区。

        :param time_zone: The time_zone of this InstanceResponse.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def tags(self):
        """Gets the tags of this InstanceResponse.


        :return: The tags of this InstanceResponse.
        :rtype: list[TagResponse]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InstanceResponse.


        :param tags: The tags of this InstanceResponse.
        :type: list[TagResponse]
        """
        self._tags = tags

    @property
    def backup_used_space(self):
        """Gets the backup_used_space of this InstanceResponse.

        备份空间使用量，单位GB。  该字段仅用于查询指定SQL Server实例信息时返回。

        :return: The backup_used_space of this InstanceResponse.
        :rtype: float
        """
        return self._backup_used_space

    @backup_used_space.setter
    def backup_used_space(self, backup_used_space):
        """Sets the backup_used_space of this InstanceResponse.

        备份空间使用量，单位GB。  该字段仅用于查询指定SQL Server实例信息时返回。

        :param backup_used_space: The backup_used_space of this InstanceResponse.
        :type: float
        """
        self._backup_used_space = backup_used_space

    @property
    def storage_used_space(self):
        """Gets the storage_used_space of this InstanceResponse.

        磁盘空间使用量，单位GB。  该字段仅用于查询指定SQL Server实例信息时返回。

        :return: The storage_used_space of this InstanceResponse.
        :rtype: float
        """
        return self._storage_used_space

    @storage_used_space.setter
    def storage_used_space(self, storage_used_space):
        """Sets the storage_used_space of this InstanceResponse.

        磁盘空间使用量，单位GB。  该字段仅用于查询指定SQL Server实例信息时返回。

        :param storage_used_space: The storage_used_space of this InstanceResponse.
        :type: float
        """
        self._storage_used_space = storage_used_space

    @property
    def order_id(self):
        """Gets the order_id of this InstanceResponse.

        订单ID，仅包周期场景返回。

        :return: The order_id of this InstanceResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InstanceResponse.

        订单ID，仅包周期场景返回。

        :param order_id: The order_id of this InstanceResponse.
        :type: str
        """
        self._order_id = order_id

    @property
    def associated_with_ddm(self):
        """Gets the associated_with_ddm of this InstanceResponse.

        是否已被DDM实例关联。

        :return: The associated_with_ddm of this InstanceResponse.
        :rtype: bool
        """
        return self._associated_with_ddm

    @associated_with_ddm.setter
    def associated_with_ddm(self, associated_with_ddm):
        """Sets the associated_with_ddm of this InstanceResponse.

        是否已被DDM实例关联。

        :param associated_with_ddm: The associated_with_ddm of this InstanceResponse.
        :type: bool
        """
        self._associated_with_ddm = associated_with_ddm

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
