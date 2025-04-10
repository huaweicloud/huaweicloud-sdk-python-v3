# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlInstanceInfoDetailUnifyStatus:

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
        'project_id': 'str',
        'status': 'str',
        'port': 'str',
        'alias': 'str',
        'type': 'str',
        'charge_info': 'MysqlInstanceChargeInfo',
        'node_count': 'int',
        'datastore': 'MysqlDatastoreWithKernelVersion',
        'backup_used_space': 'float',
        'created': 'str',
        'updated': 'str',
        'private_write_ips': 'list[str]',
        'private_dns_names': 'list[str]',
        'public_ips': 'str',
        'db_user_name': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'configuration_id': 'str',
        'backup_strategy': 'MysqlBackupStrategy',
        'nodes': 'list[MysqlInstanceNodeInfo]',
        'enterprise_project_id': 'str',
        'time_zone': 'str',
        'az_mode': 'str',
        'master_az_code': 'str',
        'maintenance_window': 'str',
        'tags': 'list[MysqlTags]',
        'dedicated_resource_id': 'str',
        'proxies': 'list[MysqlProxyInfo]',
        'tde_info': 'MysqlTdeInfo'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'status': 'status',
        'port': 'port',
        'alias': 'alias',
        'type': 'type',
        'charge_info': 'charge_info',
        'node_count': 'node_count',
        'datastore': 'datastore',
        'backup_used_space': 'backup_used_space',
        'created': 'created',
        'updated': 'updated',
        'private_write_ips': 'private_write_ips',
        'private_dns_names': 'private_dns_names',
        'public_ips': 'public_ips',
        'db_user_name': 'db_user_name',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'configuration_id': 'configuration_id',
        'backup_strategy': 'backup_strategy',
        'nodes': 'nodes',
        'enterprise_project_id': 'enterprise_project_id',
        'time_zone': 'time_zone',
        'az_mode': 'az_mode',
        'master_az_code': 'master_az_code',
        'maintenance_window': 'maintenance_window',
        'tags': 'tags',
        'dedicated_resource_id': 'dedicated_resource_id',
        'proxies': 'proxies',
        'tde_info': 'tde_info'
    }

    def __init__(self, id=None, name=None, project_id=None, status=None, port=None, alias=None, type=None, charge_info=None, node_count=None, datastore=None, backup_used_space=None, created=None, updated=None, private_write_ips=None, private_dns_names=None, public_ips=None, db_user_name=None, vpc_id=None, subnet_id=None, security_group_id=None, configuration_id=None, backup_strategy=None, nodes=None, enterprise_project_id=None, time_zone=None, az_mode=None, master_az_code=None, maintenance_window=None, tags=None, dedicated_resource_id=None, proxies=None, tde_info=None):
        r"""MysqlInstanceInfoDetailUnifyStatus

        The model defined in huaweicloud sdk

        :param id: 实例ID，严格匹配UUID规则。
        :type id: str
        :param name: 创建的实例名称。
        :type name: str
        :param project_id: 租户在某一Region下的project ID。
        :type project_id: str
        :param status: 实例状态。  取值： - 值为“creating”，表示实例正在创建。 - 值为“normal”，表示实例正常。 - 值为“abnormal”，表示实例异常。 - 值为“createfail”，表示实例创建失败。
        :type status: str
        :param port: 数据库端口号。
        :type port: str
        :param alias: 实例备注
        :type alias: str
        :param type: 实例类型，取Cluster”。
        :type type: str
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkgaussdb.v3.MysqlInstanceChargeInfo`
        :param node_count: 节点个数。
        :type node_count: int
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.MysqlDatastoreWithKernelVersion`
        :param backup_used_space: 备份空间使用大小，单位为GB。
        :type backup_used_space: float
        :param created: 创建时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type created: str
        :param updated: 更新时间，格式与\&quot;created\&quot;字段对应格式完全相同。
        :type updated: str
        :param private_write_ips: 实例的写内网IP地址。
        :type private_write_ips: list[str]
        :param private_dns_names: 实例内网域名列表。实例创建成功后，需要手动申请内网域名，否则查询内网域名为空。
        :type private_dns_names: list[str]
        :param public_ips: 实例的公网IP地址。
        :type public_ips: str
        :param db_user_name: 默认用户名。
        :type db_user_name: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 子网的网络ID信息。
        :type subnet_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param configuration_id: 实例创建的模板ID，或者应用到实例的最新参数组模板ID。
        :type configuration_id: str
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkgaussdb.v3.MysqlBackupStrategy`
        :param nodes: 节点信息。
        :type nodes: list[:class:`huaweicloudsdkgaussdb.v3.MysqlInstanceNodeInfo`]
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param time_zone: 时区。
        :type time_zone: str
        :param az_mode: 可用区模式。  取值范围： - single：单可用区。 - multi：多可用区。
        :type az_mode: str
        :param master_az_code: 主可用区。
        :type master_az_code: str
        :param maintenance_window: 可维护时间窗，为UTC时间。
        :type maintenance_window: str
        :param tags: 实例标签。
        :type tags: list[:class:`huaweicloudsdkgaussdb.v3.MysqlTags`]
        :param dedicated_resource_id: 专属资源池ID，只有数据库实例属于专属资源池才会返回该参数。
        :type dedicated_resource_id: str
        :param proxies: 代理信息。
        :type proxies: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyInfo`]
        :param tde_info: 
        :type tde_info: :class:`huaweicloudsdkgaussdb.v3.MysqlTdeInfo`
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._status = None
        self._port = None
        self._alias = None
        self._type = None
        self._charge_info = None
        self._node_count = None
        self._datastore = None
        self._backup_used_space = None
        self._created = None
        self._updated = None
        self._private_write_ips = None
        self._private_dns_names = None
        self._public_ips = None
        self._db_user_name = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._configuration_id = None
        self._backup_strategy = None
        self._nodes = None
        self._enterprise_project_id = None
        self._time_zone = None
        self._az_mode = None
        self._master_az_code = None
        self._maintenance_window = None
        self._tags = None
        self._dedicated_resource_id = None
        self._proxies = None
        self._tde_info = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.project_id = project_id
        if status is not None:
            self.status = status
        if port is not None:
            self.port = port
        if alias is not None:
            self.alias = alias
        if type is not None:
            self.type = type
        if charge_info is not None:
            self.charge_info = charge_info
        if node_count is not None:
            self.node_count = node_count
        if datastore is not None:
            self.datastore = datastore
        if backup_used_space is not None:
            self.backup_used_space = backup_used_space
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if private_write_ips is not None:
            self.private_write_ips = private_write_ips
        if private_dns_names is not None:
            self.private_dns_names = private_dns_names
        if public_ips is not None:
            self.public_ips = public_ips
        if db_user_name is not None:
            self.db_user_name = db_user_name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if configuration_id is not None:
            self.configuration_id = configuration_id
        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        if nodes is not None:
            self.nodes = nodes
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if time_zone is not None:
            self.time_zone = time_zone
        if az_mode is not None:
            self.az_mode = az_mode
        if master_az_code is not None:
            self.master_az_code = master_az_code
        if maintenance_window is not None:
            self.maintenance_window = maintenance_window
        if tags is not None:
            self.tags = tags
        if dedicated_resource_id is not None:
            self.dedicated_resource_id = dedicated_resource_id
        if proxies is not None:
            self.proxies = proxies
        if tde_info is not None:
            self.tde_info = tde_info

    @property
    def id(self):
        r"""Gets the id of this MysqlInstanceInfoDetailUnifyStatus.

        实例ID，严格匹配UUID规则。

        :return: The id of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MysqlInstanceInfoDetailUnifyStatus.

        实例ID，严格匹配UUID规则。

        :param id: The id of this MysqlInstanceInfoDetailUnifyStatus.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this MysqlInstanceInfoDetailUnifyStatus.

        创建的实例名称。

        :return: The name of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MysqlInstanceInfoDetailUnifyStatus.

        创建的实例名称。

        :param name: The name of this MysqlInstanceInfoDetailUnifyStatus.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this MysqlInstanceInfoDetailUnifyStatus.

        租户在某一Region下的project ID。

        :return: The project_id of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this MysqlInstanceInfoDetailUnifyStatus.

        租户在某一Region下的project ID。

        :param project_id: The project_id of this MysqlInstanceInfoDetailUnifyStatus.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        r"""Gets the status of this MysqlInstanceInfoDetailUnifyStatus.

        实例状态。  取值： - 值为“creating”，表示实例正在创建。 - 值为“normal”，表示实例正常。 - 值为“abnormal”，表示实例异常。 - 值为“createfail”，表示实例创建失败。

        :return: The status of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this MysqlInstanceInfoDetailUnifyStatus.

        实例状态。  取值： - 值为“creating”，表示实例正在创建。 - 值为“normal”，表示实例正常。 - 值为“abnormal”，表示实例异常。 - 值为“createfail”，表示实例创建失败。

        :param status: The status of this MysqlInstanceInfoDetailUnifyStatus.
        :type status: str
        """
        self._status = status

    @property
    def port(self):
        r"""Gets the port of this MysqlInstanceInfoDetailUnifyStatus.

        数据库端口号。

        :return: The port of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this MysqlInstanceInfoDetailUnifyStatus.

        数据库端口号。

        :param port: The port of this MysqlInstanceInfoDetailUnifyStatus.
        :type port: str
        """
        self._port = port

    @property
    def alias(self):
        r"""Gets the alias of this MysqlInstanceInfoDetailUnifyStatus.

        实例备注

        :return: The alias of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this MysqlInstanceInfoDetailUnifyStatus.

        实例备注

        :param alias: The alias of this MysqlInstanceInfoDetailUnifyStatus.
        :type alias: str
        """
        self._alias = alias

    @property
    def type(self):
        r"""Gets the type of this MysqlInstanceInfoDetailUnifyStatus.

        实例类型，取Cluster”。

        :return: The type of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MysqlInstanceInfoDetailUnifyStatus.

        实例类型，取Cluster”。

        :param type: The type of this MysqlInstanceInfoDetailUnifyStatus.
        :type type: str
        """
        self._type = type

    @property
    def charge_info(self):
        r"""Gets the charge_info of this MysqlInstanceInfoDetailUnifyStatus.

        :return: The charge_info of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlInstanceChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        r"""Sets the charge_info of this MysqlInstanceInfoDetailUnifyStatus.

        :param charge_info: The charge_info of this MysqlInstanceInfoDetailUnifyStatus.
        :type charge_info: :class:`huaweicloudsdkgaussdb.v3.MysqlInstanceChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def node_count(self):
        r"""Gets the node_count of this MysqlInstanceInfoDetailUnifyStatus.

        节点个数。

        :return: The node_count of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        r"""Sets the node_count of this MysqlInstanceInfoDetailUnifyStatus.

        节点个数。

        :param node_count: The node_count of this MysqlInstanceInfoDetailUnifyStatus.
        :type node_count: int
        """
        self._node_count = node_count

    @property
    def datastore(self):
        r"""Gets the datastore of this MysqlInstanceInfoDetailUnifyStatus.

        :return: The datastore of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlDatastoreWithKernelVersion`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this MysqlInstanceInfoDetailUnifyStatus.

        :param datastore: The datastore of this MysqlInstanceInfoDetailUnifyStatus.
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.MysqlDatastoreWithKernelVersion`
        """
        self._datastore = datastore

    @property
    def backup_used_space(self):
        r"""Gets the backup_used_space of this MysqlInstanceInfoDetailUnifyStatus.

        备份空间使用大小，单位为GB。

        :return: The backup_used_space of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: float
        """
        return self._backup_used_space

    @backup_used_space.setter
    def backup_used_space(self, backup_used_space):
        r"""Sets the backup_used_space of this MysqlInstanceInfoDetailUnifyStatus.

        备份空间使用大小，单位为GB。

        :param backup_used_space: The backup_used_space of this MysqlInstanceInfoDetailUnifyStatus.
        :type backup_used_space: float
        """
        self._backup_used_space = backup_used_space

    @property
    def created(self):
        r"""Gets the created of this MysqlInstanceInfoDetailUnifyStatus.

        创建时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The created of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this MysqlInstanceInfoDetailUnifyStatus.

        创建时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param created: The created of this MysqlInstanceInfoDetailUnifyStatus.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this MysqlInstanceInfoDetailUnifyStatus.

        更新时间，格式与\"created\"字段对应格式完全相同。

        :return: The updated of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this MysqlInstanceInfoDetailUnifyStatus.

        更新时间，格式与\"created\"字段对应格式完全相同。

        :param updated: The updated of this MysqlInstanceInfoDetailUnifyStatus.
        :type updated: str
        """
        self._updated = updated

    @property
    def private_write_ips(self):
        r"""Gets the private_write_ips of this MysqlInstanceInfoDetailUnifyStatus.

        实例的写内网IP地址。

        :return: The private_write_ips of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: list[str]
        """
        return self._private_write_ips

    @private_write_ips.setter
    def private_write_ips(self, private_write_ips):
        r"""Sets the private_write_ips of this MysqlInstanceInfoDetailUnifyStatus.

        实例的写内网IP地址。

        :param private_write_ips: The private_write_ips of this MysqlInstanceInfoDetailUnifyStatus.
        :type private_write_ips: list[str]
        """
        self._private_write_ips = private_write_ips

    @property
    def private_dns_names(self):
        r"""Gets the private_dns_names of this MysqlInstanceInfoDetailUnifyStatus.

        实例内网域名列表。实例创建成功后，需要手动申请内网域名，否则查询内网域名为空。

        :return: The private_dns_names of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: list[str]
        """
        return self._private_dns_names

    @private_dns_names.setter
    def private_dns_names(self, private_dns_names):
        r"""Sets the private_dns_names of this MysqlInstanceInfoDetailUnifyStatus.

        实例内网域名列表。实例创建成功后，需要手动申请内网域名，否则查询内网域名为空。

        :param private_dns_names: The private_dns_names of this MysqlInstanceInfoDetailUnifyStatus.
        :type private_dns_names: list[str]
        """
        self._private_dns_names = private_dns_names

    @property
    def public_ips(self):
        r"""Gets the public_ips of this MysqlInstanceInfoDetailUnifyStatus.

        实例的公网IP地址。

        :return: The public_ips of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._public_ips

    @public_ips.setter
    def public_ips(self, public_ips):
        r"""Sets the public_ips of this MysqlInstanceInfoDetailUnifyStatus.

        实例的公网IP地址。

        :param public_ips: The public_ips of this MysqlInstanceInfoDetailUnifyStatus.
        :type public_ips: str
        """
        self._public_ips = public_ips

    @property
    def db_user_name(self):
        r"""Gets the db_user_name of this MysqlInstanceInfoDetailUnifyStatus.

        默认用户名。

        :return: The db_user_name of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        r"""Sets the db_user_name of this MysqlInstanceInfoDetailUnifyStatus.

        默认用户名。

        :param db_user_name: The db_user_name of this MysqlInstanceInfoDetailUnifyStatus.
        :type db_user_name: str
        """
        self._db_user_name = db_user_name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this MysqlInstanceInfoDetailUnifyStatus.

        虚拟私有云ID。

        :return: The vpc_id of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this MysqlInstanceInfoDetailUnifyStatus.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this MysqlInstanceInfoDetailUnifyStatus.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this MysqlInstanceInfoDetailUnifyStatus.

        子网的网络ID信息。

        :return: The subnet_id of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this MysqlInstanceInfoDetailUnifyStatus.

        子网的网络ID信息。

        :param subnet_id: The subnet_id of this MysqlInstanceInfoDetailUnifyStatus.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this MysqlInstanceInfoDetailUnifyStatus.

        安全组ID。

        :return: The security_group_id of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this MysqlInstanceInfoDetailUnifyStatus.

        安全组ID。

        :param security_group_id: The security_group_id of this MysqlInstanceInfoDetailUnifyStatus.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def configuration_id(self):
        r"""Gets the configuration_id of this MysqlInstanceInfoDetailUnifyStatus.

        实例创建的模板ID，或者应用到实例的最新参数组模板ID。

        :return: The configuration_id of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        r"""Sets the configuration_id of this MysqlInstanceInfoDetailUnifyStatus.

        实例创建的模板ID，或者应用到实例的最新参数组模板ID。

        :param configuration_id: The configuration_id of this MysqlInstanceInfoDetailUnifyStatus.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def backup_strategy(self):
        r"""Gets the backup_strategy of this MysqlInstanceInfoDetailUnifyStatus.

        :return: The backup_strategy of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlBackupStrategy`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        r"""Sets the backup_strategy of this MysqlInstanceInfoDetailUnifyStatus.

        :param backup_strategy: The backup_strategy of this MysqlInstanceInfoDetailUnifyStatus.
        :type backup_strategy: :class:`huaweicloudsdkgaussdb.v3.MysqlBackupStrategy`
        """
        self._backup_strategy = backup_strategy

    @property
    def nodes(self):
        r"""Gets the nodes of this MysqlInstanceInfoDetailUnifyStatus.

        节点信息。

        :return: The nodes of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.MysqlInstanceNodeInfo`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this MysqlInstanceInfoDetailUnifyStatus.

        节点信息。

        :param nodes: The nodes of this MysqlInstanceInfoDetailUnifyStatus.
        :type nodes: list[:class:`huaweicloudsdkgaussdb.v3.MysqlInstanceNodeInfo`]
        """
        self._nodes = nodes

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this MysqlInstanceInfoDetailUnifyStatus.

        企业项目ID。

        :return: The enterprise_project_id of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this MysqlInstanceInfoDetailUnifyStatus.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this MysqlInstanceInfoDetailUnifyStatus.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def time_zone(self):
        r"""Gets the time_zone of this MysqlInstanceInfoDetailUnifyStatus.

        时区。

        :return: The time_zone of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this MysqlInstanceInfoDetailUnifyStatus.

        时区。

        :param time_zone: The time_zone of this MysqlInstanceInfoDetailUnifyStatus.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def az_mode(self):
        r"""Gets the az_mode of this MysqlInstanceInfoDetailUnifyStatus.

        可用区模式。  取值范围： - single：单可用区。 - multi：多可用区。

        :return: The az_mode of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._az_mode

    @az_mode.setter
    def az_mode(self, az_mode):
        r"""Sets the az_mode of this MysqlInstanceInfoDetailUnifyStatus.

        可用区模式。  取值范围： - single：单可用区。 - multi：多可用区。

        :param az_mode: The az_mode of this MysqlInstanceInfoDetailUnifyStatus.
        :type az_mode: str
        """
        self._az_mode = az_mode

    @property
    def master_az_code(self):
        r"""Gets the master_az_code of this MysqlInstanceInfoDetailUnifyStatus.

        主可用区。

        :return: The master_az_code of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._master_az_code

    @master_az_code.setter
    def master_az_code(self, master_az_code):
        r"""Sets the master_az_code of this MysqlInstanceInfoDetailUnifyStatus.

        主可用区。

        :param master_az_code: The master_az_code of this MysqlInstanceInfoDetailUnifyStatus.
        :type master_az_code: str
        """
        self._master_az_code = master_az_code

    @property
    def maintenance_window(self):
        r"""Gets the maintenance_window of this MysqlInstanceInfoDetailUnifyStatus.

        可维护时间窗，为UTC时间。

        :return: The maintenance_window of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        r"""Sets the maintenance_window of this MysqlInstanceInfoDetailUnifyStatus.

        可维护时间窗，为UTC时间。

        :param maintenance_window: The maintenance_window of this MysqlInstanceInfoDetailUnifyStatus.
        :type maintenance_window: str
        """
        self._maintenance_window = maintenance_window

    @property
    def tags(self):
        r"""Gets the tags of this MysqlInstanceInfoDetailUnifyStatus.

        实例标签。

        :return: The tags of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.MysqlTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this MysqlInstanceInfoDetailUnifyStatus.

        实例标签。

        :param tags: The tags of this MysqlInstanceInfoDetailUnifyStatus.
        :type tags: list[:class:`huaweicloudsdkgaussdb.v3.MysqlTags`]
        """
        self._tags = tags

    @property
    def dedicated_resource_id(self):
        r"""Gets the dedicated_resource_id of this MysqlInstanceInfoDetailUnifyStatus.

        专属资源池ID，只有数据库实例属于专属资源池才会返回该参数。

        :return: The dedicated_resource_id of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: str
        """
        return self._dedicated_resource_id

    @dedicated_resource_id.setter
    def dedicated_resource_id(self, dedicated_resource_id):
        r"""Sets the dedicated_resource_id of this MysqlInstanceInfoDetailUnifyStatus.

        专属资源池ID，只有数据库实例属于专属资源池才会返回该参数。

        :param dedicated_resource_id: The dedicated_resource_id of this MysqlInstanceInfoDetailUnifyStatus.
        :type dedicated_resource_id: str
        """
        self._dedicated_resource_id = dedicated_resource_id

    @property
    def proxies(self):
        r"""Gets the proxies of this MysqlInstanceInfoDetailUnifyStatus.

        代理信息。

        :return: The proxies of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyInfo`]
        """
        return self._proxies

    @proxies.setter
    def proxies(self, proxies):
        r"""Sets the proxies of this MysqlInstanceInfoDetailUnifyStatus.

        代理信息。

        :param proxies: The proxies of this MysqlInstanceInfoDetailUnifyStatus.
        :type proxies: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyInfo`]
        """
        self._proxies = proxies

    @property
    def tde_info(self):
        r"""Gets the tde_info of this MysqlInstanceInfoDetailUnifyStatus.

        :return: The tde_info of this MysqlInstanceInfoDetailUnifyStatus.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlTdeInfo`
        """
        return self._tde_info

    @tde_info.setter
    def tde_info(self, tde_info):
        r"""Sets the tde_info of this MysqlInstanceInfoDetailUnifyStatus.

        :param tde_info: The tde_info of this MysqlInstanceInfoDetailUnifyStatus.
        :type tde_info: :class:`huaweicloudsdkgaussdb.v3.MysqlTdeInfo`
        """
        self._tde_info = tde_info

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
        if not isinstance(other, MysqlInstanceInfoDetailUnifyStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
