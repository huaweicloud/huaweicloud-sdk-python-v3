# coding: utf-8

import six

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
        'mode': 'str',
        'region': 'str',
        'datastore': 'ListInstancesDatastoreResult',
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
        'lb_ip_address': 'str',
        'lb_port': 'str',
        'availability_zone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'port': 'port',
        'mode': 'mode',
        'region': 'region',
        'datastore': 'datastore',
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
        'lb_ip_address': 'lb_ip_address',
        'lb_port': 'lb_port',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, id=None, name=None, status=None, port=None, mode=None, region=None, datastore=None, engine=None, created=None, updated=None, db_user_name=None, vpc_id=None, subnet_id=None, security_group_id=None, backup_strategy=None, pay_mode=None, maintenance_window=None, groups=None, enterprise_project_id=None, dedicated_resource_id=None, time_zone=None, actions=None, lb_ip_address=None, lb_port=None, availability_zone=None):
        """ListInstancesResult

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 实例名称。
        :type name: str
        :param status: 实例状态。 取值： - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示实例磁盘已满。 - createfail，表示实例创建失败。 - enlargefail，表示实例扩容节点个数失败。
        :type status: str
        :param port: 数据库端口。
        :type port: str
        :param mode: 实例类型。与请求参数相同。
        :type mode: str
        :param region: 实例所在区域。
        :type region: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesDatastoreResult`
        :param engine: 存储引擎。取值为“rocksDB”。
        :type engine: str
        :param created: 实例创建时间。
        :type created: str
        :param updated: 实例操作最新变更的时间。
        :type updated: str
        :param db_user_name: 默认用户名。取值为“rwuser”。
        :type db_user_name: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesBackupStrategyResult`
        :param pay_mode: 计费方式。 - 取值为“0”，表示按需计费。 - 取值为“1”，表示包年/包月计费。
        :type pay_mode: str
        :param maintenance_window: 系统可维护时间窗。
        :type maintenance_window: str
        :param groups: 组信息。
        :type groups: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesGroupResult`]
        :param enterprise_project_id: 企业项目ID。取值为“0”，表示为default企业项目。
        :type enterprise_project_id: str
        :param dedicated_resource_id: 专属资源ID，只有数据库实例属于专属资源池才会返回该参数。
        :type dedicated_resource_id: str
        :param time_zone: 时区。
        :type time_zone: str
        :param actions: 实例正在执行的动作。
        :type actions: list[str]
        :param lb_ip_address: 负载均衡ip，只有存在负载均衡ip，才会返回该参数。
        :type lb_ip_address: str
        :param lb_port: 负载均衡端口，只有存在负载均衡ip，才会返回该参数。
        :type lb_port: str
        :param availability_zone: 实例可用区。
        :type availability_zone: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._port = None
        self._mode = None
        self._region = None
        self._datastore = None
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
        self._lb_ip_address = None
        self._lb_port = None
        self._availability_zone = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.port = port
        self.mode = mode
        self.region = region
        self.datastore = datastore
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
        if lb_ip_address is not None:
            self.lb_ip_address = lb_ip_address
        if lb_port is not None:
            self.lb_port = lb_port
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def id(self):
        """Gets the id of this ListInstancesResult.

        实例ID。

        :return: The id of this ListInstancesResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListInstancesResult.

        实例ID。

        :param id: The id of this ListInstancesResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListInstancesResult.

        实例名称。

        :return: The name of this ListInstancesResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListInstancesResult.

        实例名称。

        :param name: The name of this ListInstancesResult.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListInstancesResult.

        实例状态。 取值： - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示实例磁盘已满。 - createfail，表示实例创建失败。 - enlargefail，表示实例扩容节点个数失败。

        :return: The status of this ListInstancesResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListInstancesResult.

        实例状态。 取值： - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示实例磁盘已满。 - createfail，表示实例创建失败。 - enlargefail，表示实例扩容节点个数失败。

        :param status: The status of this ListInstancesResult.
        :type status: str
        """
        self._status = status

    @property
    def port(self):
        """Gets the port of this ListInstancesResult.

        数据库端口。

        :return: The port of this ListInstancesResult.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ListInstancesResult.

        数据库端口。

        :param port: The port of this ListInstancesResult.
        :type port: str
        """
        self._port = port

    @property
    def mode(self):
        """Gets the mode of this ListInstancesResult.

        实例类型。与请求参数相同。

        :return: The mode of this ListInstancesResult.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ListInstancesResult.

        实例类型。与请求参数相同。

        :param mode: The mode of this ListInstancesResult.
        :type mode: str
        """
        self._mode = mode

    @property
    def region(self):
        """Gets the region of this ListInstancesResult.

        实例所在区域。

        :return: The region of this ListInstancesResult.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListInstancesResult.

        实例所在区域。

        :param region: The region of this ListInstancesResult.
        :type region: str
        """
        self._region = region

    @property
    def datastore(self):
        """Gets the datastore of this ListInstancesResult.

        :return: The datastore of this ListInstancesResult.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesDatastoreResult`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this ListInstancesResult.

        :param datastore: The datastore of this ListInstancesResult.
        :type datastore: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesDatastoreResult`
        """
        self._datastore = datastore

    @property
    def engine(self):
        """Gets the engine of this ListInstancesResult.

        存储引擎。取值为“rocksDB”。

        :return: The engine of this ListInstancesResult.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ListInstancesResult.

        存储引擎。取值为“rocksDB”。

        :param engine: The engine of this ListInstancesResult.
        :type engine: str
        """
        self._engine = engine

    @property
    def created(self):
        """Gets the created of this ListInstancesResult.

        实例创建时间。

        :return: The created of this ListInstancesResult.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ListInstancesResult.

        实例创建时间。

        :param created: The created of this ListInstancesResult.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ListInstancesResult.

        实例操作最新变更的时间。

        :return: The updated of this ListInstancesResult.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ListInstancesResult.

        实例操作最新变更的时间。

        :param updated: The updated of this ListInstancesResult.
        :type updated: str
        """
        self._updated = updated

    @property
    def db_user_name(self):
        """Gets the db_user_name of this ListInstancesResult.

        默认用户名。取值为“rwuser”。

        :return: The db_user_name of this ListInstancesResult.
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        """Sets the db_user_name of this ListInstancesResult.

        默认用户名。取值为“rwuser”。

        :param db_user_name: The db_user_name of this ListInstancesResult.
        :type db_user_name: str
        """
        self._db_user_name = db_user_name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListInstancesResult.

        虚拟私有云ID。

        :return: The vpc_id of this ListInstancesResult.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListInstancesResult.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this ListInstancesResult.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ListInstancesResult.

        子网ID。

        :return: The subnet_id of this ListInstancesResult.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ListInstancesResult.

        子网ID。

        :param subnet_id: The subnet_id of this ListInstancesResult.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ListInstancesResult.

        安全组ID。

        :return: The security_group_id of this ListInstancesResult.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ListInstancesResult.

        安全组ID。

        :param security_group_id: The security_group_id of this ListInstancesResult.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this ListInstancesResult.

        :return: The backup_strategy of this ListInstancesResult.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesBackupStrategyResult`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this ListInstancesResult.

        :param backup_strategy: The backup_strategy of this ListInstancesResult.
        :type backup_strategy: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesBackupStrategyResult`
        """
        self._backup_strategy = backup_strategy

    @property
    def pay_mode(self):
        """Gets the pay_mode of this ListInstancesResult.

        计费方式。 - 取值为“0”，表示按需计费。 - 取值为“1”，表示包年/包月计费。

        :return: The pay_mode of this ListInstancesResult.
        :rtype: str
        """
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, pay_mode):
        """Sets the pay_mode of this ListInstancesResult.

        计费方式。 - 取值为“0”，表示按需计费。 - 取值为“1”，表示包年/包月计费。

        :param pay_mode: The pay_mode of this ListInstancesResult.
        :type pay_mode: str
        """
        self._pay_mode = pay_mode

    @property
    def maintenance_window(self):
        """Gets the maintenance_window of this ListInstancesResult.

        系统可维护时间窗。

        :return: The maintenance_window of this ListInstancesResult.
        :rtype: str
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """Sets the maintenance_window of this ListInstancesResult.

        系统可维护时间窗。

        :param maintenance_window: The maintenance_window of this ListInstancesResult.
        :type maintenance_window: str
        """
        self._maintenance_window = maintenance_window

    @property
    def groups(self):
        """Gets the groups of this ListInstancesResult.

        组信息。

        :return: The groups of this ListInstancesResult.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesGroupResult`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ListInstancesResult.

        组信息。

        :param groups: The groups of this ListInstancesResult.
        :type groups: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesGroupResult`]
        """
        self._groups = groups

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListInstancesResult.

        企业项目ID。取值为“0”，表示为default企业项目。

        :return: The enterprise_project_id of this ListInstancesResult.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListInstancesResult.

        企业项目ID。取值为“0”，表示为default企业项目。

        :param enterprise_project_id: The enterprise_project_id of this ListInstancesResult.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def dedicated_resource_id(self):
        """Gets the dedicated_resource_id of this ListInstancesResult.

        专属资源ID，只有数据库实例属于专属资源池才会返回该参数。

        :return: The dedicated_resource_id of this ListInstancesResult.
        :rtype: str
        """
        return self._dedicated_resource_id

    @dedicated_resource_id.setter
    def dedicated_resource_id(self, dedicated_resource_id):
        """Sets the dedicated_resource_id of this ListInstancesResult.

        专属资源ID，只有数据库实例属于专属资源池才会返回该参数。

        :param dedicated_resource_id: The dedicated_resource_id of this ListInstancesResult.
        :type dedicated_resource_id: str
        """
        self._dedicated_resource_id = dedicated_resource_id

    @property
    def time_zone(self):
        """Gets the time_zone of this ListInstancesResult.

        时区。

        :return: The time_zone of this ListInstancesResult.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ListInstancesResult.

        时区。

        :param time_zone: The time_zone of this ListInstancesResult.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def actions(self):
        """Gets the actions of this ListInstancesResult.

        实例正在执行的动作。

        :return: The actions of this ListInstancesResult.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ListInstancesResult.

        实例正在执行的动作。

        :param actions: The actions of this ListInstancesResult.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def lb_ip_address(self):
        """Gets the lb_ip_address of this ListInstancesResult.

        负载均衡ip，只有存在负载均衡ip，才会返回该参数。

        :return: The lb_ip_address of this ListInstancesResult.
        :rtype: str
        """
        return self._lb_ip_address

    @lb_ip_address.setter
    def lb_ip_address(self, lb_ip_address):
        """Sets the lb_ip_address of this ListInstancesResult.

        负载均衡ip，只有存在负载均衡ip，才会返回该参数。

        :param lb_ip_address: The lb_ip_address of this ListInstancesResult.
        :type lb_ip_address: str
        """
        self._lb_ip_address = lb_ip_address

    @property
    def lb_port(self):
        """Gets the lb_port of this ListInstancesResult.

        负载均衡端口，只有存在负载均衡ip，才会返回该参数。

        :return: The lb_port of this ListInstancesResult.
        :rtype: str
        """
        return self._lb_port

    @lb_port.setter
    def lb_port(self, lb_port):
        """Sets the lb_port of this ListInstancesResult.

        负载均衡端口，只有存在负载均衡ip，才会返回该参数。

        :param lb_port: The lb_port of this ListInstancesResult.
        :type lb_port: str
        """
        self._lb_port = lb_port

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ListInstancesResult.

        实例可用区。

        :return: The availability_zone of this ListInstancesResult.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ListInstancesResult.

        实例可用区。

        :param availability_zone: The availability_zone of this ListInstancesResult.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, ListInstancesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
