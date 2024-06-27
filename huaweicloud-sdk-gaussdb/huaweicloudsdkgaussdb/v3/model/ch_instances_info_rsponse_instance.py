# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChInstancesInfoRsponseInstance:

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
        'public_ip': 'str',
        'can_enable_public_access': 'bool',
        'current_backup_node_id': 'str',
        'cluster_mode': 'str',
        'status': 'str',
        'is_frozen': 'int',
        'frozen_time': 'str',
        'db_user': 'str',
        'bak_period': 'str',
        'bak_keep_day': 'int',
        'bak_expected_start_time': 'str',
        'datastore_version_id': 'str',
        'datastore_version': 'str',
        'datastore_type': 'str',
        'create_at': 'int',
        'update_at': 'int',
        'delete_at': 'int',
        'db_port': 'str',
        'param_group': 'ChInstancesInfoRsponseInstanceParamGroup',
        'actions': 'list[ChQueryActionInfo]',
        'create_fail_error_code': 'str',
        'groups': 'list[ChInstancesInfoRsponseInstanceGroups]',
        'ops_window': 'ChInstancesInfoRsponseInstanceOpsWindow',
        'tags_info': 'CreateChInstanceInfoTagsInfo',
        'time_zone': 'str',
        'backup_used_space': 'str',
        'az_mode': 'str',
        'master_az_code': 'str',
        'enterprise_project_id': 'str',
        'port_info': 'ChInstancesInfoRsponseInstancePortInfo',
        'volume_code': 'str',
        'support_data_replication': 'bool',
        'new_version_available': 'bool',
        'ssl_option': 'bool',
        'dedicated_resource_id': 'str',
        'pay_model': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'public_ip': 'public_ip',
        'can_enable_public_access': 'can_enable_public_access',
        'current_backup_node_id': 'current_backup_node_id',
        'cluster_mode': 'cluster_mode',
        'status': 'status',
        'is_frozen': 'is_frozen',
        'frozen_time': 'frozen_time',
        'db_user': 'db_user',
        'bak_period': 'bak_period',
        'bak_keep_day': 'bak_keep_day',
        'bak_expected_start_time': 'bak_expected_start_time',
        'datastore_version_id': 'datastore_version_id',
        'datastore_version': 'datastore_version',
        'datastore_type': 'datastore_type',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'delete_at': 'delete_at',
        'db_port': 'db_port',
        'param_group': 'param_group',
        'actions': 'actions',
        'create_fail_error_code': 'create_fail_error_code',
        'groups': 'groups',
        'ops_window': 'ops_window',
        'tags_info': 'tags_info',
        'time_zone': 'time_zone',
        'backup_used_space': 'backup_used_space',
        'az_mode': 'az_mode',
        'master_az_code': 'master_az_code',
        'enterprise_project_id': 'enterprise_project_id',
        'port_info': 'port_info',
        'volume_code': 'volume_code',
        'support_data_replication': 'support_data_replication',
        'new_version_available': 'new_version_available',
        'ssl_option': 'ssl_option',
        'dedicated_resource_id': 'dedicated_resource_id',
        'pay_model': 'pay_model'
    }

    def __init__(self, id=None, name=None, project_id=None, public_ip=None, can_enable_public_access=None, current_backup_node_id=None, cluster_mode=None, status=None, is_frozen=None, frozen_time=None, db_user=None, bak_period=None, bak_keep_day=None, bak_expected_start_time=None, datastore_version_id=None, datastore_version=None, datastore_type=None, create_at=None, update_at=None, delete_at=None, db_port=None, param_group=None, actions=None, create_fail_error_code=None, groups=None, ops_window=None, tags_info=None, time_zone=None, backup_used_space=None, az_mode=None, master_az_code=None, enterprise_project_id=None, port_info=None, volume_code=None, support_data_replication=None, new_version_available=None, ssl_option=None, dedicated_resource_id=None, pay_model=None):
        """ChInstancesInfoRsponseInstance

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 实例名称。
        :type name: str
        :param project_id: 租户在某一Region下的project ID。
        :type project_id: str
        :param public_ip: 公网访问IP。
        :type public_ip: str
        :param can_enable_public_access: 是否可公网访问。
        :type can_enable_public_access: bool
        :param current_backup_node_id: 备份节点ID。
        :type current_backup_node_id: str
        :param cluster_mode: 部署模式。 取值范围： - Single：单机 - Ha：主备
        :type cluster_mode: str
        :param status: 实例状态。
        :type status: str
        :param is_frozen: 是否冻结。 取值范围： - 0：不冻结 - 1：冻结
        :type is_frozen: int
        :param frozen_time: 冻结时间。
        :type frozen_time: str
        :param db_user: 默认用户。
        :type db_user: str
        :param bak_period: 备份周期。
        :type bak_period: str
        :param bak_keep_day: 备份保存天数。
        :type bak_keep_day: int
        :param bak_expected_start_time: 备份预计开始时间。
        :type bak_expected_start_time: str
        :param datastore_version_id: 数据库版本ID。
        :type datastore_version_id: str
        :param datastore_version: 数据库版本。
        :type datastore_version: str
        :param datastore_type: 数据库引擎。
        :type datastore_type: str
        :param create_at: 实例创建时间。
        :type create_at: int
        :param update_at: 实例更新时间。
        :type update_at: int
        :param delete_at: 实例删除时间。
        :type delete_at: int
        :param db_port: 数据库端口号。取值范围0~65535。
        :type db_port: str
        :param param_group: 
        :type param_group: :class:`huaweicloudsdkgaussdb.v3.ChInstancesInfoRsponseInstanceParamGroup`
        :param actions: 实例动作。
        :type actions: list[:class:`huaweicloudsdkgaussdb.v3.ChQueryActionInfo`]
        :param create_fail_error_code: 实例创建失败错误码。
        :type create_fail_error_code: str
        :param groups: 实例分组。
        :type groups: list[:class:`huaweicloudsdkgaussdb.v3.ChInstancesInfoRsponseInstanceGroups`]
        :param ops_window: 
        :type ops_window: :class:`huaweicloudsdkgaussdb.v3.ChInstancesInfoRsponseInstanceOpsWindow`
        :param tags_info: 
        :type tags_info: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceInfoTagsInfo`
        :param time_zone: 时区。
        :type time_zone: str
        :param backup_used_space: 备份使用空间。
        :type backup_used_space: str
        :param az_mode: 可用区模式。 取值范围： - single：单可用区 - double：多可用区-
        :type az_mode: str
        :param master_az_code: 主可用区。
        :type master_az_code: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param port_info: 
        :type port_info: :class:`huaweicloudsdkgaussdb.v3.ChInstancesInfoRsponseInstancePortInfo`
        :param volume_code: 磁盘规格码。
        :type volume_code: str
        :param support_data_replication: 是否支持副本。
        :type support_data_replication: bool
        :param new_version_available: 是否有数据库新版本。
        :type new_version_available: bool
        :param ssl_option: SSL开关。
        :type ssl_option: bool
        :param dedicated_resource_id: 专属资源池ID。
        :type dedicated_resource_id: str
        :param pay_model: 支付模式。 取值范围： - 0：按需计费 - 1：包周期-
        :type pay_model: str
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._public_ip = None
        self._can_enable_public_access = None
        self._current_backup_node_id = None
        self._cluster_mode = None
        self._status = None
        self._is_frozen = None
        self._frozen_time = None
        self._db_user = None
        self._bak_period = None
        self._bak_keep_day = None
        self._bak_expected_start_time = None
        self._datastore_version_id = None
        self._datastore_version = None
        self._datastore_type = None
        self._create_at = None
        self._update_at = None
        self._delete_at = None
        self._db_port = None
        self._param_group = None
        self._actions = None
        self._create_fail_error_code = None
        self._groups = None
        self._ops_window = None
        self._tags_info = None
        self._time_zone = None
        self._backup_used_space = None
        self._az_mode = None
        self._master_az_code = None
        self._enterprise_project_id = None
        self._port_info = None
        self._volume_code = None
        self._support_data_replication = None
        self._new_version_available = None
        self._ssl_option = None
        self._dedicated_resource_id = None
        self._pay_model = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.project_id = project_id
        if public_ip is not None:
            self.public_ip = public_ip
        self.can_enable_public_access = can_enable_public_access
        if current_backup_node_id is not None:
            self.current_backup_node_id = current_backup_node_id
        self.cluster_mode = cluster_mode
        self.status = status
        self.is_frozen = is_frozen
        if frozen_time is not None:
            self.frozen_time = frozen_time
        if db_user is not None:
            self.db_user = db_user
        if bak_period is not None:
            self.bak_period = bak_period
        if bak_keep_day is not None:
            self.bak_keep_day = bak_keep_day
        if bak_expected_start_time is not None:
            self.bak_expected_start_time = bak_expected_start_time
        self.datastore_version_id = datastore_version_id
        self.datastore_version = datastore_version
        self.datastore_type = datastore_type
        self.create_at = create_at
        self.update_at = update_at
        if delete_at is not None:
            self.delete_at = delete_at
        self.db_port = db_port
        if param_group is not None:
            self.param_group = param_group
        if actions is not None:
            self.actions = actions
        if create_fail_error_code is not None:
            self.create_fail_error_code = create_fail_error_code
        self.groups = groups
        self.ops_window = ops_window
        if tags_info is not None:
            self.tags_info = tags_info
        if time_zone is not None:
            self.time_zone = time_zone
        if backup_used_space is not None:
            self.backup_used_space = backup_used_space
        self.az_mode = az_mode
        if master_az_code is not None:
            self.master_az_code = master_az_code
        self.enterprise_project_id = enterprise_project_id
        self.port_info = port_info
        self.volume_code = volume_code
        self.support_data_replication = support_data_replication
        self.new_version_available = new_version_available
        self.ssl_option = ssl_option
        if dedicated_resource_id is not None:
            self.dedicated_resource_id = dedicated_resource_id
        if pay_model is not None:
            self.pay_model = pay_model

    @property
    def id(self):
        """Gets the id of this ChInstancesInfoRsponseInstance.

        实例ID。

        :return: The id of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChInstancesInfoRsponseInstance.

        实例ID。

        :param id: The id of this ChInstancesInfoRsponseInstance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ChInstancesInfoRsponseInstance.

        实例名称。

        :return: The name of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChInstancesInfoRsponseInstance.

        实例名称。

        :param name: The name of this ChInstancesInfoRsponseInstance.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this ChInstancesInfoRsponseInstance.

        租户在某一Region下的project ID。

        :return: The project_id of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ChInstancesInfoRsponseInstance.

        租户在某一Region下的project ID。

        :param project_id: The project_id of this ChInstancesInfoRsponseInstance.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def public_ip(self):
        """Gets the public_ip of this ChInstancesInfoRsponseInstance.

        公网访问IP。

        :return: The public_ip of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this ChInstancesInfoRsponseInstance.

        公网访问IP。

        :param public_ip: The public_ip of this ChInstancesInfoRsponseInstance.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def can_enable_public_access(self):
        """Gets the can_enable_public_access of this ChInstancesInfoRsponseInstance.

        是否可公网访问。

        :return: The can_enable_public_access of this ChInstancesInfoRsponseInstance.
        :rtype: bool
        """
        return self._can_enable_public_access

    @can_enable_public_access.setter
    def can_enable_public_access(self, can_enable_public_access):
        """Sets the can_enable_public_access of this ChInstancesInfoRsponseInstance.

        是否可公网访问。

        :param can_enable_public_access: The can_enable_public_access of this ChInstancesInfoRsponseInstance.
        :type can_enable_public_access: bool
        """
        self._can_enable_public_access = can_enable_public_access

    @property
    def current_backup_node_id(self):
        """Gets the current_backup_node_id of this ChInstancesInfoRsponseInstance.

        备份节点ID。

        :return: The current_backup_node_id of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._current_backup_node_id

    @current_backup_node_id.setter
    def current_backup_node_id(self, current_backup_node_id):
        """Sets the current_backup_node_id of this ChInstancesInfoRsponseInstance.

        备份节点ID。

        :param current_backup_node_id: The current_backup_node_id of this ChInstancesInfoRsponseInstance.
        :type current_backup_node_id: str
        """
        self._current_backup_node_id = current_backup_node_id

    @property
    def cluster_mode(self):
        """Gets the cluster_mode of this ChInstancesInfoRsponseInstance.

        部署模式。 取值范围： - Single：单机 - Ha：主备

        :return: The cluster_mode of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._cluster_mode

    @cluster_mode.setter
    def cluster_mode(self, cluster_mode):
        """Sets the cluster_mode of this ChInstancesInfoRsponseInstance.

        部署模式。 取值范围： - Single：单机 - Ha：主备

        :param cluster_mode: The cluster_mode of this ChInstancesInfoRsponseInstance.
        :type cluster_mode: str
        """
        self._cluster_mode = cluster_mode

    @property
    def status(self):
        """Gets the status of this ChInstancesInfoRsponseInstance.

        实例状态。

        :return: The status of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ChInstancesInfoRsponseInstance.

        实例状态。

        :param status: The status of this ChInstancesInfoRsponseInstance.
        :type status: str
        """
        self._status = status

    @property
    def is_frozen(self):
        """Gets the is_frozen of this ChInstancesInfoRsponseInstance.

        是否冻结。 取值范围： - 0：不冻结 - 1：冻结

        :return: The is_frozen of this ChInstancesInfoRsponseInstance.
        :rtype: int
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        """Sets the is_frozen of this ChInstancesInfoRsponseInstance.

        是否冻结。 取值范围： - 0：不冻结 - 1：冻结

        :param is_frozen: The is_frozen of this ChInstancesInfoRsponseInstance.
        :type is_frozen: int
        """
        self._is_frozen = is_frozen

    @property
    def frozen_time(self):
        """Gets the frozen_time of this ChInstancesInfoRsponseInstance.

        冻结时间。

        :return: The frozen_time of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._frozen_time

    @frozen_time.setter
    def frozen_time(self, frozen_time):
        """Sets the frozen_time of this ChInstancesInfoRsponseInstance.

        冻结时间。

        :param frozen_time: The frozen_time of this ChInstancesInfoRsponseInstance.
        :type frozen_time: str
        """
        self._frozen_time = frozen_time

    @property
    def db_user(self):
        """Gets the db_user of this ChInstancesInfoRsponseInstance.

        默认用户。

        :return: The db_user of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        """Sets the db_user of this ChInstancesInfoRsponseInstance.

        默认用户。

        :param db_user: The db_user of this ChInstancesInfoRsponseInstance.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def bak_period(self):
        """Gets the bak_period of this ChInstancesInfoRsponseInstance.

        备份周期。

        :return: The bak_period of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._bak_period

    @bak_period.setter
    def bak_period(self, bak_period):
        """Sets the bak_period of this ChInstancesInfoRsponseInstance.

        备份周期。

        :param bak_period: The bak_period of this ChInstancesInfoRsponseInstance.
        :type bak_period: str
        """
        self._bak_period = bak_period

    @property
    def bak_keep_day(self):
        """Gets the bak_keep_day of this ChInstancesInfoRsponseInstance.

        备份保存天数。

        :return: The bak_keep_day of this ChInstancesInfoRsponseInstance.
        :rtype: int
        """
        return self._bak_keep_day

    @bak_keep_day.setter
    def bak_keep_day(self, bak_keep_day):
        """Sets the bak_keep_day of this ChInstancesInfoRsponseInstance.

        备份保存天数。

        :param bak_keep_day: The bak_keep_day of this ChInstancesInfoRsponseInstance.
        :type bak_keep_day: int
        """
        self._bak_keep_day = bak_keep_day

    @property
    def bak_expected_start_time(self):
        """Gets the bak_expected_start_time of this ChInstancesInfoRsponseInstance.

        备份预计开始时间。

        :return: The bak_expected_start_time of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._bak_expected_start_time

    @bak_expected_start_time.setter
    def bak_expected_start_time(self, bak_expected_start_time):
        """Sets the bak_expected_start_time of this ChInstancesInfoRsponseInstance.

        备份预计开始时间。

        :param bak_expected_start_time: The bak_expected_start_time of this ChInstancesInfoRsponseInstance.
        :type bak_expected_start_time: str
        """
        self._bak_expected_start_time = bak_expected_start_time

    @property
    def datastore_version_id(self):
        """Gets the datastore_version_id of this ChInstancesInfoRsponseInstance.

        数据库版本ID。

        :return: The datastore_version_id of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._datastore_version_id

    @datastore_version_id.setter
    def datastore_version_id(self, datastore_version_id):
        """Sets the datastore_version_id of this ChInstancesInfoRsponseInstance.

        数据库版本ID。

        :param datastore_version_id: The datastore_version_id of this ChInstancesInfoRsponseInstance.
        :type datastore_version_id: str
        """
        self._datastore_version_id = datastore_version_id

    @property
    def datastore_version(self):
        """Gets the datastore_version of this ChInstancesInfoRsponseInstance.

        数据库版本。

        :return: The datastore_version of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._datastore_version

    @datastore_version.setter
    def datastore_version(self, datastore_version):
        """Sets the datastore_version of this ChInstancesInfoRsponseInstance.

        数据库版本。

        :param datastore_version: The datastore_version of this ChInstancesInfoRsponseInstance.
        :type datastore_version: str
        """
        self._datastore_version = datastore_version

    @property
    def datastore_type(self):
        """Gets the datastore_type of this ChInstancesInfoRsponseInstance.

        数据库引擎。

        :return: The datastore_type of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this ChInstancesInfoRsponseInstance.

        数据库引擎。

        :param datastore_type: The datastore_type of this ChInstancesInfoRsponseInstance.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def create_at(self):
        """Gets the create_at of this ChInstancesInfoRsponseInstance.

        实例创建时间。

        :return: The create_at of this ChInstancesInfoRsponseInstance.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this ChInstancesInfoRsponseInstance.

        实例创建时间。

        :param create_at: The create_at of this ChInstancesInfoRsponseInstance.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def update_at(self):
        """Gets the update_at of this ChInstancesInfoRsponseInstance.

        实例更新时间。

        :return: The update_at of this ChInstancesInfoRsponseInstance.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this ChInstancesInfoRsponseInstance.

        实例更新时间。

        :param update_at: The update_at of this ChInstancesInfoRsponseInstance.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def delete_at(self):
        """Gets the delete_at of this ChInstancesInfoRsponseInstance.

        实例删除时间。

        :return: The delete_at of this ChInstancesInfoRsponseInstance.
        :rtype: int
        """
        return self._delete_at

    @delete_at.setter
    def delete_at(self, delete_at):
        """Sets the delete_at of this ChInstancesInfoRsponseInstance.

        实例删除时间。

        :param delete_at: The delete_at of this ChInstancesInfoRsponseInstance.
        :type delete_at: int
        """
        self._delete_at = delete_at

    @property
    def db_port(self):
        """Gets the db_port of this ChInstancesInfoRsponseInstance.

        数据库端口号。取值范围0~65535。

        :return: The db_port of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._db_port

    @db_port.setter
    def db_port(self, db_port):
        """Sets the db_port of this ChInstancesInfoRsponseInstance.

        数据库端口号。取值范围0~65535。

        :param db_port: The db_port of this ChInstancesInfoRsponseInstance.
        :type db_port: str
        """
        self._db_port = db_port

    @property
    def param_group(self):
        """Gets the param_group of this ChInstancesInfoRsponseInstance.

        :return: The param_group of this ChInstancesInfoRsponseInstance.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ChInstancesInfoRsponseInstanceParamGroup`
        """
        return self._param_group

    @param_group.setter
    def param_group(self, param_group):
        """Sets the param_group of this ChInstancesInfoRsponseInstance.

        :param param_group: The param_group of this ChInstancesInfoRsponseInstance.
        :type param_group: :class:`huaweicloudsdkgaussdb.v3.ChInstancesInfoRsponseInstanceParamGroup`
        """
        self._param_group = param_group

    @property
    def actions(self):
        """Gets the actions of this ChInstancesInfoRsponseInstance.

        实例动作。

        :return: The actions of this ChInstancesInfoRsponseInstance.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ChQueryActionInfo`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ChInstancesInfoRsponseInstance.

        实例动作。

        :param actions: The actions of this ChInstancesInfoRsponseInstance.
        :type actions: list[:class:`huaweicloudsdkgaussdb.v3.ChQueryActionInfo`]
        """
        self._actions = actions

    @property
    def create_fail_error_code(self):
        """Gets the create_fail_error_code of this ChInstancesInfoRsponseInstance.

        实例创建失败错误码。

        :return: The create_fail_error_code of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._create_fail_error_code

    @create_fail_error_code.setter
    def create_fail_error_code(self, create_fail_error_code):
        """Sets the create_fail_error_code of this ChInstancesInfoRsponseInstance.

        实例创建失败错误码。

        :param create_fail_error_code: The create_fail_error_code of this ChInstancesInfoRsponseInstance.
        :type create_fail_error_code: str
        """
        self._create_fail_error_code = create_fail_error_code

    @property
    def groups(self):
        """Gets the groups of this ChInstancesInfoRsponseInstance.

        实例分组。

        :return: The groups of this ChInstancesInfoRsponseInstance.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ChInstancesInfoRsponseInstanceGroups`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ChInstancesInfoRsponseInstance.

        实例分组。

        :param groups: The groups of this ChInstancesInfoRsponseInstance.
        :type groups: list[:class:`huaweicloudsdkgaussdb.v3.ChInstancesInfoRsponseInstanceGroups`]
        """
        self._groups = groups

    @property
    def ops_window(self):
        """Gets the ops_window of this ChInstancesInfoRsponseInstance.

        :return: The ops_window of this ChInstancesInfoRsponseInstance.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ChInstancesInfoRsponseInstanceOpsWindow`
        """
        return self._ops_window

    @ops_window.setter
    def ops_window(self, ops_window):
        """Sets the ops_window of this ChInstancesInfoRsponseInstance.

        :param ops_window: The ops_window of this ChInstancesInfoRsponseInstance.
        :type ops_window: :class:`huaweicloudsdkgaussdb.v3.ChInstancesInfoRsponseInstanceOpsWindow`
        """
        self._ops_window = ops_window

    @property
    def tags_info(self):
        """Gets the tags_info of this ChInstancesInfoRsponseInstance.

        :return: The tags_info of this ChInstancesInfoRsponseInstance.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceInfoTagsInfo`
        """
        return self._tags_info

    @tags_info.setter
    def tags_info(self, tags_info):
        """Sets the tags_info of this ChInstancesInfoRsponseInstance.

        :param tags_info: The tags_info of this ChInstancesInfoRsponseInstance.
        :type tags_info: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceInfoTagsInfo`
        """
        self._tags_info = tags_info

    @property
    def time_zone(self):
        """Gets the time_zone of this ChInstancesInfoRsponseInstance.

        时区。

        :return: The time_zone of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ChInstancesInfoRsponseInstance.

        时区。

        :param time_zone: The time_zone of this ChInstancesInfoRsponseInstance.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def backup_used_space(self):
        """Gets the backup_used_space of this ChInstancesInfoRsponseInstance.

        备份使用空间。

        :return: The backup_used_space of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._backup_used_space

    @backup_used_space.setter
    def backup_used_space(self, backup_used_space):
        """Sets the backup_used_space of this ChInstancesInfoRsponseInstance.

        备份使用空间。

        :param backup_used_space: The backup_used_space of this ChInstancesInfoRsponseInstance.
        :type backup_used_space: str
        """
        self._backup_used_space = backup_used_space

    @property
    def az_mode(self):
        """Gets the az_mode of this ChInstancesInfoRsponseInstance.

        可用区模式。 取值范围： - single：单可用区 - double：多可用区-

        :return: The az_mode of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._az_mode

    @az_mode.setter
    def az_mode(self, az_mode):
        """Sets the az_mode of this ChInstancesInfoRsponseInstance.

        可用区模式。 取值范围： - single：单可用区 - double：多可用区-

        :param az_mode: The az_mode of this ChInstancesInfoRsponseInstance.
        :type az_mode: str
        """
        self._az_mode = az_mode

    @property
    def master_az_code(self):
        """Gets the master_az_code of this ChInstancesInfoRsponseInstance.

        主可用区。

        :return: The master_az_code of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._master_az_code

    @master_az_code.setter
    def master_az_code(self, master_az_code):
        """Sets the master_az_code of this ChInstancesInfoRsponseInstance.

        主可用区。

        :param master_az_code: The master_az_code of this ChInstancesInfoRsponseInstance.
        :type master_az_code: str
        """
        self._master_az_code = master_az_code

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ChInstancesInfoRsponseInstance.

        企业项目ID。

        :return: The enterprise_project_id of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ChInstancesInfoRsponseInstance.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ChInstancesInfoRsponseInstance.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def port_info(self):
        """Gets the port_info of this ChInstancesInfoRsponseInstance.

        :return: The port_info of this ChInstancesInfoRsponseInstance.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ChInstancesInfoRsponseInstancePortInfo`
        """
        return self._port_info

    @port_info.setter
    def port_info(self, port_info):
        """Sets the port_info of this ChInstancesInfoRsponseInstance.

        :param port_info: The port_info of this ChInstancesInfoRsponseInstance.
        :type port_info: :class:`huaweicloudsdkgaussdb.v3.ChInstancesInfoRsponseInstancePortInfo`
        """
        self._port_info = port_info

    @property
    def volume_code(self):
        """Gets the volume_code of this ChInstancesInfoRsponseInstance.

        磁盘规格码。

        :return: The volume_code of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._volume_code

    @volume_code.setter
    def volume_code(self, volume_code):
        """Sets the volume_code of this ChInstancesInfoRsponseInstance.

        磁盘规格码。

        :param volume_code: The volume_code of this ChInstancesInfoRsponseInstance.
        :type volume_code: str
        """
        self._volume_code = volume_code

    @property
    def support_data_replication(self):
        """Gets the support_data_replication of this ChInstancesInfoRsponseInstance.

        是否支持副本。

        :return: The support_data_replication of this ChInstancesInfoRsponseInstance.
        :rtype: bool
        """
        return self._support_data_replication

    @support_data_replication.setter
    def support_data_replication(self, support_data_replication):
        """Sets the support_data_replication of this ChInstancesInfoRsponseInstance.

        是否支持副本。

        :param support_data_replication: The support_data_replication of this ChInstancesInfoRsponseInstance.
        :type support_data_replication: bool
        """
        self._support_data_replication = support_data_replication

    @property
    def new_version_available(self):
        """Gets the new_version_available of this ChInstancesInfoRsponseInstance.

        是否有数据库新版本。

        :return: The new_version_available of this ChInstancesInfoRsponseInstance.
        :rtype: bool
        """
        return self._new_version_available

    @new_version_available.setter
    def new_version_available(self, new_version_available):
        """Sets the new_version_available of this ChInstancesInfoRsponseInstance.

        是否有数据库新版本。

        :param new_version_available: The new_version_available of this ChInstancesInfoRsponseInstance.
        :type new_version_available: bool
        """
        self._new_version_available = new_version_available

    @property
    def ssl_option(self):
        """Gets the ssl_option of this ChInstancesInfoRsponseInstance.

        SSL开关。

        :return: The ssl_option of this ChInstancesInfoRsponseInstance.
        :rtype: bool
        """
        return self._ssl_option

    @ssl_option.setter
    def ssl_option(self, ssl_option):
        """Sets the ssl_option of this ChInstancesInfoRsponseInstance.

        SSL开关。

        :param ssl_option: The ssl_option of this ChInstancesInfoRsponseInstance.
        :type ssl_option: bool
        """
        self._ssl_option = ssl_option

    @property
    def dedicated_resource_id(self):
        """Gets the dedicated_resource_id of this ChInstancesInfoRsponseInstance.

        专属资源池ID。

        :return: The dedicated_resource_id of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._dedicated_resource_id

    @dedicated_resource_id.setter
    def dedicated_resource_id(self, dedicated_resource_id):
        """Sets the dedicated_resource_id of this ChInstancesInfoRsponseInstance.

        专属资源池ID。

        :param dedicated_resource_id: The dedicated_resource_id of this ChInstancesInfoRsponseInstance.
        :type dedicated_resource_id: str
        """
        self._dedicated_resource_id = dedicated_resource_id

    @property
    def pay_model(self):
        """Gets the pay_model of this ChInstancesInfoRsponseInstance.

        支付模式。 取值范围： - 0：按需计费 - 1：包周期-

        :return: The pay_model of this ChInstancesInfoRsponseInstance.
        :rtype: str
        """
        return self._pay_model

    @pay_model.setter
    def pay_model(self, pay_model):
        """Sets the pay_model of this ChInstancesInfoRsponseInstance.

        支付模式。 取值范围： - 0：按需计费 - 1：包周期-

        :param pay_model: The pay_model of this ChInstancesInfoRsponseInstance.
        :type pay_model: str
        """
        self._pay_model = pay_model

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
        if not isinstance(other, ChInstancesInfoRsponseInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
