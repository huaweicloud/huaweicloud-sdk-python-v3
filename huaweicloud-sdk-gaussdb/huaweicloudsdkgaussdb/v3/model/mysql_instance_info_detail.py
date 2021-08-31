# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlInstanceInfoDetail:


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
        'type': 'str',
        'node_count': 'int',
        'datastore': 'MysqlDatastore',
        'backup_used_space': 'int',
        'created': 'str',
        'updated': 'str',
        'private_write_ips': 'list[str]',
        'public_ips': 'str',
        'db_user_name': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'configuration_id': 'str',
        'volume': 'MysqlVolumeInfo',
        'backup_strategy': 'MysqlBackupStrategy',
        'nodes': 'list[MysqlInstanceNodeInfo]',
        'enterprise_project_id': 'str',
        'time_zone': 'str',
        'az_mode': 'str',
        'master_az_code': 'str',
        'maintenance_window': 'str',
        'tags': 'list[MysqlTags]',
        'dedicated_resource_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'status': 'status',
        'port': 'port',
        'type': 'type',
        'node_count': 'node_count',
        'datastore': 'datastore',
        'backup_used_space': 'backup_used_space',
        'created': 'created',
        'updated': 'updated',
        'private_write_ips': 'private_write_ips',
        'public_ips': 'public_ips',
        'db_user_name': 'db_user_name',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'configuration_id': 'configuration_id',
        'volume': 'volume',
        'backup_strategy': 'backup_strategy',
        'nodes': 'nodes',
        'enterprise_project_id': 'enterprise_project_id',
        'time_zone': 'time_zone',
        'az_mode': 'az_mode',
        'master_az_code': 'master_az_code',
        'maintenance_window': 'maintenance_window',
        'tags': 'tags',
        'dedicated_resource_id': 'dedicated_resource_id'
    }

    def __init__(self, id=None, name=None, project_id=None, status=None, port=None, type=None, node_count=None, datastore=None, backup_used_space=None, created=None, updated=None, private_write_ips=None, public_ips=None, db_user_name=None, vpc_id=None, subnet_id=None, security_group_id=None, configuration_id=None, volume=None, backup_strategy=None, nodes=None, enterprise_project_id=None, time_zone=None, az_mode=None, master_az_code=None, maintenance_window=None, tags=None, dedicated_resource_id=None):
        """MysqlInstanceInfoDetail - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._status = None
        self._port = None
        self._type = None
        self._node_count = None
        self._datastore = None
        self._backup_used_space = None
        self._created = None
        self._updated = None
        self._private_write_ips = None
        self._public_ips = None
        self._db_user_name = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._configuration_id = None
        self._volume = None
        self._backup_strategy = None
        self._nodes = None
        self._enterprise_project_id = None
        self._time_zone = None
        self._az_mode = None
        self._master_az_code = None
        self._maintenance_window = None
        self._tags = None
        self._dedicated_resource_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.project_id = project_id
        if status is not None:
            self.status = status
        if port is not None:
            self.port = port
        if type is not None:
            self.type = type
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
        if volume is not None:
            self.volume = volume
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

    @property
    def id(self):
        """Gets the id of this MysqlInstanceInfoDetail.

        实例ID。

        :return: The id of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MysqlInstanceInfoDetail.

        实例ID。

        :param id: The id of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this MysqlInstanceInfoDetail.

        创建的实例名称。

        :return: The name of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MysqlInstanceInfoDetail.

        创建的实例名称。

        :param name: The name of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this MysqlInstanceInfoDetail.

        租户在某一region下的project ID。

        :return: The project_id of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this MysqlInstanceInfoDetail.

        租户在某一region下的project ID。

        :param project_id: The project_id of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._project_id = project_id

    @property
    def status(self):
        """Gets the status of this MysqlInstanceInfoDetail.

        实例状态。 取值： 值为“BUILD”，表示实例正在创建。 值为“ACTIVE”，表示实例正常。 值为“FAILED”，表示实例异常。 值为“FROZEN”，表示实例冻结。 值为“MODIFYING”，表示实例正在扩容。 值为“REBOOTING”，表示实例正在重启。 值为“RESTORING”，表示实例正在恢复。 值为“MODIFYING INSTANCE TYPE”，表示实例正在转主备。 值为“SWITCHOVER”，表示实例正在主备切换。 值为“MIGRATING”，表示实例正在迁移。 值为“BACKING UP”，表示实例正在进行备份。 值为“MODIFYING DATABASE PORT”，表示实例正在修改数据库端口。值为“STORAGE FULL”，表示实例磁盘空间满。

        :return: The status of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MysqlInstanceInfoDetail.

        实例状态。 取值： 值为“BUILD”，表示实例正在创建。 值为“ACTIVE”，表示实例正常。 值为“FAILED”，表示实例异常。 值为“FROZEN”，表示实例冻结。 值为“MODIFYING”，表示实例正在扩容。 值为“REBOOTING”，表示实例正在重启。 值为“RESTORING”，表示实例正在恢复。 值为“MODIFYING INSTANCE TYPE”，表示实例正在转主备。 值为“SWITCHOVER”，表示实例正在主备切换。 值为“MIGRATING”，表示实例正在迁移。 值为“BACKING UP”，表示实例正在进行备份。 值为“MODIFYING DATABASE PORT”，表示实例正在修改数据库端口。值为“STORAGE FULL”，表示实例磁盘空间满。

        :param status: The status of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._status = status

    @property
    def port(self):
        """Gets the port of this MysqlInstanceInfoDetail.

        数据库端口号。

        :return: The port of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this MysqlInstanceInfoDetail.

        数据库端口号。

        :param port: The port of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._port = port

    @property
    def type(self):
        """Gets the type of this MysqlInstanceInfoDetail.

        实例类型，取值为“Cluster”。

        :return: The type of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MysqlInstanceInfoDetail.

        实例类型，取值为“Cluster”。

        :param type: The type of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._type = type

    @property
    def node_count(self):
        """Gets the node_count of this MysqlInstanceInfoDetail.

        节点个数。

        :return: The node_count of this MysqlInstanceInfoDetail.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """Sets the node_count of this MysqlInstanceInfoDetail.

        节点个数。

        :param node_count: The node_count of this MysqlInstanceInfoDetail.
        :type: int
        """
        self._node_count = node_count

    @property
    def datastore(self):
        """Gets the datastore of this MysqlInstanceInfoDetail.


        :return: The datastore of this MysqlInstanceInfoDetail.
        :rtype: MysqlDatastore
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this MysqlInstanceInfoDetail.


        :param datastore: The datastore of this MysqlInstanceInfoDetail.
        :type: MysqlDatastore
        """
        self._datastore = datastore

    @property
    def backup_used_space(self):
        """Gets the backup_used_space of this MysqlInstanceInfoDetail.

        备份空间使用大小，单位为GB。

        :return: The backup_used_space of this MysqlInstanceInfoDetail.
        :rtype: int
        """
        return self._backup_used_space

    @backup_used_space.setter
    def backup_used_space(self, backup_used_space):
        """Sets the backup_used_space of this MysqlInstanceInfoDetail.

        备份空间使用大小，单位为GB。

        :param backup_used_space: The backup_used_space of this MysqlInstanceInfoDetail.
        :type: int
        """
        self._backup_used_space = backup_used_space

    @property
    def created(self):
        """Gets the created of this MysqlInstanceInfoDetail.

        创建时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :return: The created of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this MysqlInstanceInfoDetail.

        创建时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :param created: The created of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this MysqlInstanceInfoDetail.

        更新时间，格式与\"created\"字段对应格式完全相同。说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :return: The updated of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this MysqlInstanceInfoDetail.

        更新时间，格式与\"created\"字段对应格式完全相同。说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :param updated: The updated of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._updated = updated

    @property
    def private_write_ips(self):
        """Gets the private_write_ips of this MysqlInstanceInfoDetail.

        实例的写内网IP。

        :return: The private_write_ips of this MysqlInstanceInfoDetail.
        :rtype: list[str]
        """
        return self._private_write_ips

    @private_write_ips.setter
    def private_write_ips(self, private_write_ips):
        """Sets the private_write_ips of this MysqlInstanceInfoDetail.

        实例的写内网IP。

        :param private_write_ips: The private_write_ips of this MysqlInstanceInfoDetail.
        :type: list[str]
        """
        self._private_write_ips = private_write_ips

    @property
    def public_ips(self):
        """Gets the public_ips of this MysqlInstanceInfoDetail.

        实例的公网IP。

        :return: The public_ips of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._public_ips

    @public_ips.setter
    def public_ips(self, public_ips):
        """Sets the public_ips of this MysqlInstanceInfoDetail.

        实例的公网IP。

        :param public_ips: The public_ips of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._public_ips = public_ips

    @property
    def db_user_name(self):
        """Gets the db_user_name of this MysqlInstanceInfoDetail.

        默认用户名。

        :return: The db_user_name of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        """Sets the db_user_name of this MysqlInstanceInfoDetail.

        默认用户名。

        :param db_user_name: The db_user_name of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._db_user_name = db_user_name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this MysqlInstanceInfoDetail.

        虚拟私有云ID。

        :return: The vpc_id of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this MysqlInstanceInfoDetail.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this MysqlInstanceInfoDetail.

        子网的网络ID信息。

        :return: The subnet_id of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this MysqlInstanceInfoDetail.

        子网的网络ID信息。

        :param subnet_id: The subnet_id of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this MysqlInstanceInfoDetail.

        安全组ID。

        :return: The security_group_id of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this MysqlInstanceInfoDetail.

        安全组ID。

        :param security_group_id: The security_group_id of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def configuration_id(self):
        """Gets the configuration_id of this MysqlInstanceInfoDetail.

        实例创建的模板ID，或者应用到实例的最新参数组模板ID。

        :return: The configuration_id of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this MysqlInstanceInfoDetail.

        实例创建的模板ID，或者应用到实例的最新参数组模板ID。

        :param configuration_id: The configuration_id of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._configuration_id = configuration_id

    @property
    def volume(self):
        """Gets the volume of this MysqlInstanceInfoDetail.


        :return: The volume of this MysqlInstanceInfoDetail.
        :rtype: MysqlVolumeInfo
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this MysqlInstanceInfoDetail.


        :param volume: The volume of this MysqlInstanceInfoDetail.
        :type: MysqlVolumeInfo
        """
        self._volume = volume

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this MysqlInstanceInfoDetail.


        :return: The backup_strategy of this MysqlInstanceInfoDetail.
        :rtype: MysqlBackupStrategy
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this MysqlInstanceInfoDetail.


        :param backup_strategy: The backup_strategy of this MysqlInstanceInfoDetail.
        :type: MysqlBackupStrategy
        """
        self._backup_strategy = backup_strategy

    @property
    def nodes(self):
        """Gets the nodes of this MysqlInstanceInfoDetail.


        :return: The nodes of this MysqlInstanceInfoDetail.
        :rtype: list[MysqlInstanceNodeInfo]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this MysqlInstanceInfoDetail.


        :param nodes: The nodes of this MysqlInstanceInfoDetail.
        :type: list[MysqlInstanceNodeInfo]
        """
        self._nodes = nodes

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this MysqlInstanceInfoDetail.

        企业项目ID。

        :return: The enterprise_project_id of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this MysqlInstanceInfoDetail.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def time_zone(self):
        """Gets the time_zone of this MysqlInstanceInfoDetail.

        时区。

        :return: The time_zone of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this MysqlInstanceInfoDetail.

        时区。

        :param time_zone: The time_zone of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def az_mode(self):
        """Gets the az_mode of this MysqlInstanceInfoDetail.

        可用区模式，单可用区single或多可用区multi。

        :return: The az_mode of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._az_mode

    @az_mode.setter
    def az_mode(self, az_mode):
        """Sets the az_mode of this MysqlInstanceInfoDetail.

        可用区模式，单可用区single或多可用区multi。

        :param az_mode: The az_mode of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._az_mode = az_mode

    @property
    def master_az_code(self):
        """Gets the master_az_code of this MysqlInstanceInfoDetail.

        主可用区。

        :return: The master_az_code of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._master_az_code

    @master_az_code.setter
    def master_az_code(self, master_az_code):
        """Sets the master_az_code of this MysqlInstanceInfoDetail.

        主可用区。

        :param master_az_code: The master_az_code of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._master_az_code = master_az_code

    @property
    def maintenance_window(self):
        """Gets the maintenance_window of this MysqlInstanceInfoDetail.

        可维护时间窗，为UTC时间。

        :return: The maintenance_window of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """Sets the maintenance_window of this MysqlInstanceInfoDetail.

        可维护时间窗，为UTC时间。

        :param maintenance_window: The maintenance_window of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._maintenance_window = maintenance_window

    @property
    def tags(self):
        """Gets the tags of this MysqlInstanceInfoDetail.

        实例标签。

        :return: The tags of this MysqlInstanceInfoDetail.
        :rtype: list[MysqlTags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this MysqlInstanceInfoDetail.

        实例标签。

        :param tags: The tags of this MysqlInstanceInfoDetail.
        :type: list[MysqlTags]
        """
        self._tags = tags

    @property
    def dedicated_resource_id(self):
        """Gets the dedicated_resource_id of this MysqlInstanceInfoDetail.

        专属资源池ID，只有数据库实例属于专属资源池才会返回该参数。

        :return: The dedicated_resource_id of this MysqlInstanceInfoDetail.
        :rtype: str
        """
        return self._dedicated_resource_id

    @dedicated_resource_id.setter
    def dedicated_resource_id(self, dedicated_resource_id):
        """Sets the dedicated_resource_id of this MysqlInstanceInfoDetail.

        专属资源池ID，只有数据库实例属于专属资源池才会返回该参数。

        :param dedicated_resource_id: The dedicated_resource_id of this MysqlInstanceInfoDetail.
        :type: str
        """
        self._dedicated_resource_id = dedicated_resource_id

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
        if not isinstance(other, MysqlInstanceInfoDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
