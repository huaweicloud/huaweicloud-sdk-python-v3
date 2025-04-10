# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryInstanceResponse:

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
        'remark': 'str',
        'status': 'str',
        'port': 'str',
        'mode': 'str',
        'region': 'str',
        'datastore': 'DatastoreItem',
        'engine': 'str',
        'created': 'str',
        'updated': 'str',
        'db_user_name': 'str',
        'ssl': 'int',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'backup_strategy': 'BackupStrategyForItemResponse',
        'pay_mode': 'str',
        'maintenance_window': 'str',
        'groups': 'list[GroupResponseItem]',
        'disk_encryption_id': 'str',
        'enterprise_project_id': 'str',
        'time_zone': 'str',
        'dss_pool_id': 'str',
        'actions': 'list[str]',
        'order_id': 'str',
        'tags': 'list[TagResponse]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'remark': 'remark',
        'status': 'status',
        'port': 'port',
        'mode': 'mode',
        'region': 'region',
        'datastore': 'datastore',
        'engine': 'engine',
        'created': 'created',
        'updated': 'updated',
        'db_user_name': 'db_user_name',
        'ssl': 'ssl',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'backup_strategy': 'backup_strategy',
        'pay_mode': 'pay_mode',
        'maintenance_window': 'maintenance_window',
        'groups': 'groups',
        'disk_encryption_id': 'disk_encryption_id',
        'enterprise_project_id': 'enterprise_project_id',
        'time_zone': 'time_zone',
        'dss_pool_id': 'dss_pool_id',
        'actions': 'actions',
        'order_id': 'order_id',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, remark=None, status=None, port=None, mode=None, region=None, datastore=None, engine=None, created=None, updated=None, db_user_name=None, ssl=None, vpc_id=None, subnet_id=None, security_group_id=None, backup_strategy=None, pay_mode=None, maintenance_window=None, groups=None, disk_encryption_id=None, enterprise_project_id=None, time_zone=None, dss_pool_id=None, actions=None, order_id=None, tags=None):
        r"""QueryInstanceResponse

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 实例名称。
        :type name: str
        :param remark: 实例备注。
        :type remark: str
        :param status: 实例状态。 取值： - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示实例磁盘已满。 - createfail，表示实例创建失败。 - enlargefail，表示实例扩容节点个数失败。
        :type status: str
        :param port: 数据库端口号。文档数据库实例支持的端口号范围为2100～9500。
        :type port: str
        :param mode: 实例类型。与请求参数相同。
        :type mode: str
        :param region: 实例所在区域。
        :type region: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkdds.v3.DatastoreItem`
        :param engine: 存储引擎。取值为“wiredTiger”。
        :type engine: str
        :param created: 实例创建时间。
        :type created: str
        :param updated: 实例操作最新变更的时间。
        :type updated: str
        :param db_user_name: 默认用户名。取值为“rwuser”。
        :type db_user_name: str
        :param ssl: 是否开启SSL安全连接。 - 取值为“1”，表示开启。 - 取值为“0”，表示不开启。
        :type ssl: int
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkdds.v3.BackupStrategyForItemResponse`
        :param pay_mode: 计费方式。 - 取值为“0”，表示按需计费。 - 取值为“1”，表示包年/包月计费。
        :type pay_mode: str
        :param maintenance_window: 系统可维护时间窗。
        :type maintenance_window: str
        :param groups: 组信息。
        :type groups: list[:class:`huaweicloudsdkdds.v3.GroupResponseItem`]
        :param disk_encryption_id: 磁盘加密的密钥ID。
        :type disk_encryption_id: str
        :param enterprise_project_id: 企业项目ID。取值为“0”，表示为default企业项目。
        :type enterprise_project_id: str
        :param time_zone: 时区。
        :type time_zone: str
        :param dss_pool_id: 专属存储池ID。
        :type dss_pool_id: str
        :param actions: 实例正在执行的动作。
        :type actions: list[str]
        :param order_id: 订单ID，仅包周期场景返回。
        :type order_id: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkdds.v3.TagResponse`]
        """
        
        

        self._id = None
        self._name = None
        self._remark = None
        self._status = None
        self._port = None
        self._mode = None
        self._region = None
        self._datastore = None
        self._engine = None
        self._created = None
        self._updated = None
        self._db_user_name = None
        self._ssl = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._backup_strategy = None
        self._pay_mode = None
        self._maintenance_window = None
        self._groups = None
        self._disk_encryption_id = None
        self._enterprise_project_id = None
        self._time_zone = None
        self._dss_pool_id = None
        self._actions = None
        self._order_id = None
        self._tags = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.remark = remark
        self.status = status
        self.port = port
        self.mode = mode
        self.region = region
        self.datastore = datastore
        self.engine = engine
        self.created = created
        self.updated = updated
        self.db_user_name = db_user_name
        self.ssl = ssl
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.backup_strategy = backup_strategy
        if pay_mode is not None:
            self.pay_mode = pay_mode
        self.maintenance_window = maintenance_window
        self.groups = groups
        self.disk_encryption_id = disk_encryption_id
        self.enterprise_project_id = enterprise_project_id
        self.time_zone = time_zone
        if dss_pool_id is not None:
            self.dss_pool_id = dss_pool_id
        self.actions = actions
        if order_id is not None:
            self.order_id = order_id
        self.tags = tags

    @property
    def id(self):
        r"""Gets the id of this QueryInstanceResponse.

        实例ID。

        :return: The id of this QueryInstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this QueryInstanceResponse.

        实例ID。

        :param id: The id of this QueryInstanceResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this QueryInstanceResponse.

        实例名称。

        :return: The name of this QueryInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this QueryInstanceResponse.

        实例名称。

        :param name: The name of this QueryInstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def remark(self):
        r"""Gets the remark of this QueryInstanceResponse.

        实例备注。

        :return: The remark of this QueryInstanceResponse.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this QueryInstanceResponse.

        实例备注。

        :param remark: The remark of this QueryInstanceResponse.
        :type remark: str
        """
        self._remark = remark

    @property
    def status(self):
        r"""Gets the status of this QueryInstanceResponse.

        实例状态。 取值： - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示实例磁盘已满。 - createfail，表示实例创建失败。 - enlargefail，表示实例扩容节点个数失败。

        :return: The status of this QueryInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this QueryInstanceResponse.

        实例状态。 取值： - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示实例磁盘已满。 - createfail，表示实例创建失败。 - enlargefail，表示实例扩容节点个数失败。

        :param status: The status of this QueryInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def port(self):
        r"""Gets the port of this QueryInstanceResponse.

        数据库端口号。文档数据库实例支持的端口号范围为2100～9500。

        :return: The port of this QueryInstanceResponse.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this QueryInstanceResponse.

        数据库端口号。文档数据库实例支持的端口号范围为2100～9500。

        :param port: The port of this QueryInstanceResponse.
        :type port: str
        """
        self._port = port

    @property
    def mode(self):
        r"""Gets the mode of this QueryInstanceResponse.

        实例类型。与请求参数相同。

        :return: The mode of this QueryInstanceResponse.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this QueryInstanceResponse.

        实例类型。与请求参数相同。

        :param mode: The mode of this QueryInstanceResponse.
        :type mode: str
        """
        self._mode = mode

    @property
    def region(self):
        r"""Gets the region of this QueryInstanceResponse.

        实例所在区域。

        :return: The region of this QueryInstanceResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this QueryInstanceResponse.

        实例所在区域。

        :param region: The region of this QueryInstanceResponse.
        :type region: str
        """
        self._region = region

    @property
    def datastore(self):
        r"""Gets the datastore of this QueryInstanceResponse.

        :return: The datastore of this QueryInstanceResponse.
        :rtype: :class:`huaweicloudsdkdds.v3.DatastoreItem`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this QueryInstanceResponse.

        :param datastore: The datastore of this QueryInstanceResponse.
        :type datastore: :class:`huaweicloudsdkdds.v3.DatastoreItem`
        """
        self._datastore = datastore

    @property
    def engine(self):
        r"""Gets the engine of this QueryInstanceResponse.

        存储引擎。取值为“wiredTiger”。

        :return: The engine of this QueryInstanceResponse.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this QueryInstanceResponse.

        存储引擎。取值为“wiredTiger”。

        :param engine: The engine of this QueryInstanceResponse.
        :type engine: str
        """
        self._engine = engine

    @property
    def created(self):
        r"""Gets the created of this QueryInstanceResponse.

        实例创建时间。

        :return: The created of this QueryInstanceResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this QueryInstanceResponse.

        实例创建时间。

        :param created: The created of this QueryInstanceResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this QueryInstanceResponse.

        实例操作最新变更的时间。

        :return: The updated of this QueryInstanceResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this QueryInstanceResponse.

        实例操作最新变更的时间。

        :param updated: The updated of this QueryInstanceResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def db_user_name(self):
        r"""Gets the db_user_name of this QueryInstanceResponse.

        默认用户名。取值为“rwuser”。

        :return: The db_user_name of this QueryInstanceResponse.
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        r"""Sets the db_user_name of this QueryInstanceResponse.

        默认用户名。取值为“rwuser”。

        :param db_user_name: The db_user_name of this QueryInstanceResponse.
        :type db_user_name: str
        """
        self._db_user_name = db_user_name

    @property
    def ssl(self):
        r"""Gets the ssl of this QueryInstanceResponse.

        是否开启SSL安全连接。 - 取值为“1”，表示开启。 - 取值为“0”，表示不开启。

        :return: The ssl of this QueryInstanceResponse.
        :rtype: int
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        r"""Sets the ssl of this QueryInstanceResponse.

        是否开启SSL安全连接。 - 取值为“1”，表示开启。 - 取值为“0”，表示不开启。

        :param ssl: The ssl of this QueryInstanceResponse.
        :type ssl: int
        """
        self._ssl = ssl

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this QueryInstanceResponse.

        虚拟私有云ID。

        :return: The vpc_id of this QueryInstanceResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this QueryInstanceResponse.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this QueryInstanceResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this QueryInstanceResponse.

        子网ID。

        :return: The subnet_id of this QueryInstanceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this QueryInstanceResponse.

        子网ID。

        :param subnet_id: The subnet_id of this QueryInstanceResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this QueryInstanceResponse.

        安全组ID。

        :return: The security_group_id of this QueryInstanceResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this QueryInstanceResponse.

        安全组ID。

        :param security_group_id: The security_group_id of this QueryInstanceResponse.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def backup_strategy(self):
        r"""Gets the backup_strategy of this QueryInstanceResponse.

        :return: The backup_strategy of this QueryInstanceResponse.
        :rtype: :class:`huaweicloudsdkdds.v3.BackupStrategyForItemResponse`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        r"""Sets the backup_strategy of this QueryInstanceResponse.

        :param backup_strategy: The backup_strategy of this QueryInstanceResponse.
        :type backup_strategy: :class:`huaweicloudsdkdds.v3.BackupStrategyForItemResponse`
        """
        self._backup_strategy = backup_strategy

    @property
    def pay_mode(self):
        r"""Gets the pay_mode of this QueryInstanceResponse.

        计费方式。 - 取值为“0”，表示按需计费。 - 取值为“1”，表示包年/包月计费。

        :return: The pay_mode of this QueryInstanceResponse.
        :rtype: str
        """
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, pay_mode):
        r"""Sets the pay_mode of this QueryInstanceResponse.

        计费方式。 - 取值为“0”，表示按需计费。 - 取值为“1”，表示包年/包月计费。

        :param pay_mode: The pay_mode of this QueryInstanceResponse.
        :type pay_mode: str
        """
        self._pay_mode = pay_mode

    @property
    def maintenance_window(self):
        r"""Gets the maintenance_window of this QueryInstanceResponse.

        系统可维护时间窗。

        :return: The maintenance_window of this QueryInstanceResponse.
        :rtype: str
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        r"""Sets the maintenance_window of this QueryInstanceResponse.

        系统可维护时间窗。

        :param maintenance_window: The maintenance_window of this QueryInstanceResponse.
        :type maintenance_window: str
        """
        self._maintenance_window = maintenance_window

    @property
    def groups(self):
        r"""Gets the groups of this QueryInstanceResponse.

        组信息。

        :return: The groups of this QueryInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdds.v3.GroupResponseItem`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this QueryInstanceResponse.

        组信息。

        :param groups: The groups of this QueryInstanceResponse.
        :type groups: list[:class:`huaweicloudsdkdds.v3.GroupResponseItem`]
        """
        self._groups = groups

    @property
    def disk_encryption_id(self):
        r"""Gets the disk_encryption_id of this QueryInstanceResponse.

        磁盘加密的密钥ID。

        :return: The disk_encryption_id of this QueryInstanceResponse.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        r"""Sets the disk_encryption_id of this QueryInstanceResponse.

        磁盘加密的密钥ID。

        :param disk_encryption_id: The disk_encryption_id of this QueryInstanceResponse.
        :type disk_encryption_id: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this QueryInstanceResponse.

        企业项目ID。取值为“0”，表示为default企业项目。

        :return: The enterprise_project_id of this QueryInstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this QueryInstanceResponse.

        企业项目ID。取值为“0”，表示为default企业项目。

        :param enterprise_project_id: The enterprise_project_id of this QueryInstanceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def time_zone(self):
        r"""Gets the time_zone of this QueryInstanceResponse.

        时区。

        :return: The time_zone of this QueryInstanceResponse.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this QueryInstanceResponse.

        时区。

        :param time_zone: The time_zone of this QueryInstanceResponse.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def dss_pool_id(self):
        r"""Gets the dss_pool_id of this QueryInstanceResponse.

        专属存储池ID。

        :return: The dss_pool_id of this QueryInstanceResponse.
        :rtype: str
        """
        return self._dss_pool_id

    @dss_pool_id.setter
    def dss_pool_id(self, dss_pool_id):
        r"""Sets the dss_pool_id of this QueryInstanceResponse.

        专属存储池ID。

        :param dss_pool_id: The dss_pool_id of this QueryInstanceResponse.
        :type dss_pool_id: str
        """
        self._dss_pool_id = dss_pool_id

    @property
    def actions(self):
        r"""Gets the actions of this QueryInstanceResponse.

        实例正在执行的动作。

        :return: The actions of this QueryInstanceResponse.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this QueryInstanceResponse.

        实例正在执行的动作。

        :param actions: The actions of this QueryInstanceResponse.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def order_id(self):
        r"""Gets the order_id of this QueryInstanceResponse.

        订单ID，仅包周期场景返回。

        :return: The order_id of this QueryInstanceResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this QueryInstanceResponse.

        订单ID，仅包周期场景返回。

        :param order_id: The order_id of this QueryInstanceResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def tags(self):
        r"""Gets the tags of this QueryInstanceResponse.

        标签列表。

        :return: The tags of this QueryInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdds.v3.TagResponse`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this QueryInstanceResponse.

        标签列表。

        :param tags: The tags of this QueryInstanceResponse.
        :type tags: list[:class:`huaweicloudsdkdds.v3.TagResponse`]
        """
        self._tags = tags

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
        if not isinstance(other, QueryInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
