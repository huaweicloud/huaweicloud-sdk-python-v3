# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StarRocksInstanceInfoInstances:

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
        'data_vip': 'str',
        'can_enable_public_access': 'bool',
        'current_backup_node_id': 'str',
        'cluster_mode': 'str',
        'status': 'str',
        'is_frozen': 'int',
        'frozen_time': 'int',
        'db_user': 'str',
        'bak_period': 'str',
        'bak_keep_day': 'int',
        'bak_expected_start_time': 'int',
        'data_store_version_id': 'str',
        'data_store_version': 'str',
        'data_store_type': 'str',
        'create_at': 'int',
        'update_at': 'int',
        'delete_at': 'int',
        'db_port': 'str',
        'param_group': 'str',
        'actions': 'list[QueryAction]',
        'create_fail_error_code': 'str',
        'groups': 'list[StarRocksInstanceInfoGroups]',
        'ops_window': 'StarRocksInstanceInfoOpsWindow',
        'tags_info': 'StarRocksInstanceInfoTagsInfo',
        'time_zone': 'str',
        'backup_used_space': 'str',
        'az_mode': 'str',
        'enterprise_project_id': 'str',
        'port_info': 'StarRocksInstanceInfoPortInfo',
        'fe_node_volume_code': 'str',
        'be_node_volume_code': 'str',
        'fe_node_volume_size': 'str',
        'be_node_volume_size': 'str',
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
        'data_vip': 'data_vip',
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
        'data_store_version_id': 'data_store_version_id',
        'data_store_version': 'data_store_version',
        'data_store_type': 'data_store_type',
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
        'enterprise_project_id': 'enterprise_project_id',
        'port_info': 'port_info',
        'fe_node_volume_code': 'fe_node_volume_code',
        'be_node_volume_code': 'be_node_volume_code',
        'fe_node_volume_size': 'fe_node_volume_size',
        'be_node_volume_size': 'be_node_volume_size',
        'support_data_replication': 'support_data_replication',
        'new_version_available': 'new_version_available',
        'ssl_option': 'ssl_option',
        'dedicated_resource_id': 'dedicated_resource_id',
        'pay_model': 'pay_model'
    }

    def __init__(self, id=None, name=None, project_id=None, public_ip=None, data_vip=None, can_enable_public_access=None, current_backup_node_id=None, cluster_mode=None, status=None, is_frozen=None, frozen_time=None, db_user=None, bak_period=None, bak_keep_day=None, bak_expected_start_time=None, data_store_version_id=None, data_store_version=None, data_store_type=None, create_at=None, update_at=None, delete_at=None, db_port=None, param_group=None, actions=None, create_fail_error_code=None, groups=None, ops_window=None, tags_info=None, time_zone=None, backup_used_space=None, az_mode=None, enterprise_project_id=None, port_info=None, fe_node_volume_code=None, be_node_volume_code=None, fe_node_volume_size=None, be_node_volume_size=None, support_data_replication=None, new_version_available=None, ssl_option=None, dedicated_resource_id=None, pay_model=None):
        r"""StarRocksInstanceInfoInstances

        The model defined in huaweicloud sdk

        :param id: 实例ID，严格匹配UUID规则。
        :type id: str
        :param name: 创建的实例名称。
        :type name: str
        :param project_id: 租户在某一Region下的project ID。
        :type project_id: str
        :param public_ip: 公网访问IP。
        :type public_ip: str
        :param data_vip: StarRocks FE节点类型数据IP（多个IP使用逗号分隔）
        :type data_vip: str
        :param can_enable_public_access: 是否可公网访问。
        :type can_enable_public_access: bool
        :param current_backup_node_id: 备份节点ID。
        :type current_backup_node_id: str
        :param cluster_mode: 部署模式。
        :type cluster_mode: str
        :param status: 实例状态。
        :type status: str
        :param is_frozen: 是否冻结。
        :type is_frozen: int
        :param frozen_time: 冻结时间。
        :type frozen_time: int
        :param db_user: 默认用户名。
        :type db_user: str
        :param bak_period: 备份周期。
        :type bak_period: str
        :param bak_keep_day: 备份保存天数。
        :type bak_keep_day: int
        :param bak_expected_start_time: 备份预计开始时间。
        :type bak_expected_start_time: int
        :param data_store_version_id: 数据库版本ID。
        :type data_store_version_id: str
        :param data_store_version: 数据库版本。
        :type data_store_version: str
        :param data_store_type: 数据库引擎。
        :type data_store_type: str
        :param create_at: 实例创建时间。
        :type create_at: int
        :param update_at: 实例更新时间。
        :type update_at: int
        :param delete_at: 实例删除时间。
        :type delete_at: int
        :param db_port: 数据库端口号。
        :type db_port: str
        :param param_group: 参数组。
        :type param_group: str
        :param actions: 实例动作。
        :type actions: list[:class:`huaweicloudsdkgaussdb.v3.QueryAction`]
        :param create_fail_error_code: 实例创建失败错误码。
        :type create_fail_error_code: str
        :param groups: 实例分组。
        :type groups: list[:class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoGroups`]
        :param ops_window: 
        :type ops_window: :class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoOpsWindow`
        :param tags_info: 
        :type tags_info: :class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoTagsInfo`
        :param time_zone: 时区。
        :type time_zone: str
        :param backup_used_space: 备份使用空间。
        :type backup_used_space: str
        :param az_mode: 可用区模式。  取值范围：  - single：单可用区 - multi：多可用区
        :type az_mode: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param port_info: 
        :type port_info: :class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoPortInfo`
        :param fe_node_volume_code: FE节点磁盘类型。
        :type fe_node_volume_code: str
        :param be_node_volume_code: BE节点磁盘类型。
        :type be_node_volume_code: str
        :param fe_node_volume_size: FE节点磁盘大小。
        :type fe_node_volume_size: str
        :param be_node_volume_size: BE节点磁盘大小。
        :type be_node_volume_size: str
        :param support_data_replication: 是否支持副本。
        :type support_data_replication: bool
        :param new_version_available: 是否有数据库新版本。
        :type new_version_available: bool
        :param ssl_option: SSL开关。
        :type ssl_option: bool
        :param dedicated_resource_id: 专属资源池ID，只有数据库实例属于专属资源池才会返回该参数。
        :type dedicated_resource_id: str
        :param pay_model: 支付模式。
        :type pay_model: str
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._public_ip = None
        self._data_vip = None
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
        self._data_store_version_id = None
        self._data_store_version = None
        self._data_store_type = None
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
        self._enterprise_project_id = None
        self._port_info = None
        self._fe_node_volume_code = None
        self._be_node_volume_code = None
        self._fe_node_volume_size = None
        self._be_node_volume_size = None
        self._support_data_replication = None
        self._new_version_available = None
        self._ssl_option = None
        self._dedicated_resource_id = None
        self._pay_model = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if public_ip is not None:
            self.public_ip = public_ip
        if data_vip is not None:
            self.data_vip = data_vip
        if can_enable_public_access is not None:
            self.can_enable_public_access = can_enable_public_access
        if current_backup_node_id is not None:
            self.current_backup_node_id = current_backup_node_id
        if cluster_mode is not None:
            self.cluster_mode = cluster_mode
        if status is not None:
            self.status = status
        if is_frozen is not None:
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
        if data_store_version_id is not None:
            self.data_store_version_id = data_store_version_id
        if data_store_version is not None:
            self.data_store_version = data_store_version
        if data_store_type is not None:
            self.data_store_type = data_store_type
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if delete_at is not None:
            self.delete_at = delete_at
        if db_port is not None:
            self.db_port = db_port
        if param_group is not None:
            self.param_group = param_group
        if actions is not None:
            self.actions = actions
        if create_fail_error_code is not None:
            self.create_fail_error_code = create_fail_error_code
        if groups is not None:
            self.groups = groups
        if ops_window is not None:
            self.ops_window = ops_window
        if tags_info is not None:
            self.tags_info = tags_info
        if time_zone is not None:
            self.time_zone = time_zone
        if backup_used_space is not None:
            self.backup_used_space = backup_used_space
        if az_mode is not None:
            self.az_mode = az_mode
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if port_info is not None:
            self.port_info = port_info
        if fe_node_volume_code is not None:
            self.fe_node_volume_code = fe_node_volume_code
        if be_node_volume_code is not None:
            self.be_node_volume_code = be_node_volume_code
        if fe_node_volume_size is not None:
            self.fe_node_volume_size = fe_node_volume_size
        if be_node_volume_size is not None:
            self.be_node_volume_size = be_node_volume_size
        if support_data_replication is not None:
            self.support_data_replication = support_data_replication
        if new_version_available is not None:
            self.new_version_available = new_version_available
        if ssl_option is not None:
            self.ssl_option = ssl_option
        if dedicated_resource_id is not None:
            self.dedicated_resource_id = dedicated_resource_id
        if pay_model is not None:
            self.pay_model = pay_model

    @property
    def id(self):
        r"""Gets the id of this StarRocksInstanceInfoInstances.

        实例ID，严格匹配UUID规则。

        :return: The id of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StarRocksInstanceInfoInstances.

        实例ID，严格匹配UUID规则。

        :param id: The id of this StarRocksInstanceInfoInstances.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this StarRocksInstanceInfoInstances.

        创建的实例名称。

        :return: The name of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StarRocksInstanceInfoInstances.

        创建的实例名称。

        :param name: The name of this StarRocksInstanceInfoInstances.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this StarRocksInstanceInfoInstances.

        租户在某一Region下的project ID。

        :return: The project_id of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this StarRocksInstanceInfoInstances.

        租户在某一Region下的project ID。

        :param project_id: The project_id of this StarRocksInstanceInfoInstances.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this StarRocksInstanceInfoInstances.

        公网访问IP。

        :return: The public_ip of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this StarRocksInstanceInfoInstances.

        公网访问IP。

        :param public_ip: The public_ip of this StarRocksInstanceInfoInstances.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def data_vip(self):
        r"""Gets the data_vip of this StarRocksInstanceInfoInstances.

        StarRocks FE节点类型数据IP（多个IP使用逗号分隔）

        :return: The data_vip of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._data_vip

    @data_vip.setter
    def data_vip(self, data_vip):
        r"""Sets the data_vip of this StarRocksInstanceInfoInstances.

        StarRocks FE节点类型数据IP（多个IP使用逗号分隔）

        :param data_vip: The data_vip of this StarRocksInstanceInfoInstances.
        :type data_vip: str
        """
        self._data_vip = data_vip

    @property
    def can_enable_public_access(self):
        r"""Gets the can_enable_public_access of this StarRocksInstanceInfoInstances.

        是否可公网访问。

        :return: The can_enable_public_access of this StarRocksInstanceInfoInstances.
        :rtype: bool
        """
        return self._can_enable_public_access

    @can_enable_public_access.setter
    def can_enable_public_access(self, can_enable_public_access):
        r"""Sets the can_enable_public_access of this StarRocksInstanceInfoInstances.

        是否可公网访问。

        :param can_enable_public_access: The can_enable_public_access of this StarRocksInstanceInfoInstances.
        :type can_enable_public_access: bool
        """
        self._can_enable_public_access = can_enable_public_access

    @property
    def current_backup_node_id(self):
        r"""Gets the current_backup_node_id of this StarRocksInstanceInfoInstances.

        备份节点ID。

        :return: The current_backup_node_id of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._current_backup_node_id

    @current_backup_node_id.setter
    def current_backup_node_id(self, current_backup_node_id):
        r"""Sets the current_backup_node_id of this StarRocksInstanceInfoInstances.

        备份节点ID。

        :param current_backup_node_id: The current_backup_node_id of this StarRocksInstanceInfoInstances.
        :type current_backup_node_id: str
        """
        self._current_backup_node_id = current_backup_node_id

    @property
    def cluster_mode(self):
        r"""Gets the cluster_mode of this StarRocksInstanceInfoInstances.

        部署模式。

        :return: The cluster_mode of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._cluster_mode

    @cluster_mode.setter
    def cluster_mode(self, cluster_mode):
        r"""Sets the cluster_mode of this StarRocksInstanceInfoInstances.

        部署模式。

        :param cluster_mode: The cluster_mode of this StarRocksInstanceInfoInstances.
        :type cluster_mode: str
        """
        self._cluster_mode = cluster_mode

    @property
    def status(self):
        r"""Gets the status of this StarRocksInstanceInfoInstances.

        实例状态。

        :return: The status of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StarRocksInstanceInfoInstances.

        实例状态。

        :param status: The status of this StarRocksInstanceInfoInstances.
        :type status: str
        """
        self._status = status

    @property
    def is_frozen(self):
        r"""Gets the is_frozen of this StarRocksInstanceInfoInstances.

        是否冻结。

        :return: The is_frozen of this StarRocksInstanceInfoInstances.
        :rtype: int
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        r"""Sets the is_frozen of this StarRocksInstanceInfoInstances.

        是否冻结。

        :param is_frozen: The is_frozen of this StarRocksInstanceInfoInstances.
        :type is_frozen: int
        """
        self._is_frozen = is_frozen

    @property
    def frozen_time(self):
        r"""Gets the frozen_time of this StarRocksInstanceInfoInstances.

        冻结时间。

        :return: The frozen_time of this StarRocksInstanceInfoInstances.
        :rtype: int
        """
        return self._frozen_time

    @frozen_time.setter
    def frozen_time(self, frozen_time):
        r"""Sets the frozen_time of this StarRocksInstanceInfoInstances.

        冻结时间。

        :param frozen_time: The frozen_time of this StarRocksInstanceInfoInstances.
        :type frozen_time: int
        """
        self._frozen_time = frozen_time

    @property
    def db_user(self):
        r"""Gets the db_user of this StarRocksInstanceInfoInstances.

        默认用户名。

        :return: The db_user of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        r"""Sets the db_user of this StarRocksInstanceInfoInstances.

        默认用户名。

        :param db_user: The db_user of this StarRocksInstanceInfoInstances.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def bak_period(self):
        r"""Gets the bak_period of this StarRocksInstanceInfoInstances.

        备份周期。

        :return: The bak_period of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._bak_period

    @bak_period.setter
    def bak_period(self, bak_period):
        r"""Sets the bak_period of this StarRocksInstanceInfoInstances.

        备份周期。

        :param bak_period: The bak_period of this StarRocksInstanceInfoInstances.
        :type bak_period: str
        """
        self._bak_period = bak_period

    @property
    def bak_keep_day(self):
        r"""Gets the bak_keep_day of this StarRocksInstanceInfoInstances.

        备份保存天数。

        :return: The bak_keep_day of this StarRocksInstanceInfoInstances.
        :rtype: int
        """
        return self._bak_keep_day

    @bak_keep_day.setter
    def bak_keep_day(self, bak_keep_day):
        r"""Sets the bak_keep_day of this StarRocksInstanceInfoInstances.

        备份保存天数。

        :param bak_keep_day: The bak_keep_day of this StarRocksInstanceInfoInstances.
        :type bak_keep_day: int
        """
        self._bak_keep_day = bak_keep_day

    @property
    def bak_expected_start_time(self):
        r"""Gets the bak_expected_start_time of this StarRocksInstanceInfoInstances.

        备份预计开始时间。

        :return: The bak_expected_start_time of this StarRocksInstanceInfoInstances.
        :rtype: int
        """
        return self._bak_expected_start_time

    @bak_expected_start_time.setter
    def bak_expected_start_time(self, bak_expected_start_time):
        r"""Sets the bak_expected_start_time of this StarRocksInstanceInfoInstances.

        备份预计开始时间。

        :param bak_expected_start_time: The bak_expected_start_time of this StarRocksInstanceInfoInstances.
        :type bak_expected_start_time: int
        """
        self._bak_expected_start_time = bak_expected_start_time

    @property
    def data_store_version_id(self):
        r"""Gets the data_store_version_id of this StarRocksInstanceInfoInstances.

        数据库版本ID。

        :return: The data_store_version_id of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._data_store_version_id

    @data_store_version_id.setter
    def data_store_version_id(self, data_store_version_id):
        r"""Sets the data_store_version_id of this StarRocksInstanceInfoInstances.

        数据库版本ID。

        :param data_store_version_id: The data_store_version_id of this StarRocksInstanceInfoInstances.
        :type data_store_version_id: str
        """
        self._data_store_version_id = data_store_version_id

    @property
    def data_store_version(self):
        r"""Gets the data_store_version of this StarRocksInstanceInfoInstances.

        数据库版本。

        :return: The data_store_version of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._data_store_version

    @data_store_version.setter
    def data_store_version(self, data_store_version):
        r"""Sets the data_store_version of this StarRocksInstanceInfoInstances.

        数据库版本。

        :param data_store_version: The data_store_version of this StarRocksInstanceInfoInstances.
        :type data_store_version: str
        """
        self._data_store_version = data_store_version

    @property
    def data_store_type(self):
        r"""Gets the data_store_type of this StarRocksInstanceInfoInstances.

        数据库引擎。

        :return: The data_store_type of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._data_store_type

    @data_store_type.setter
    def data_store_type(self, data_store_type):
        r"""Sets the data_store_type of this StarRocksInstanceInfoInstances.

        数据库引擎。

        :param data_store_type: The data_store_type of this StarRocksInstanceInfoInstances.
        :type data_store_type: str
        """
        self._data_store_type = data_store_type

    @property
    def create_at(self):
        r"""Gets the create_at of this StarRocksInstanceInfoInstances.

        实例创建时间。

        :return: The create_at of this StarRocksInstanceInfoInstances.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this StarRocksInstanceInfoInstances.

        实例创建时间。

        :param create_at: The create_at of this StarRocksInstanceInfoInstances.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this StarRocksInstanceInfoInstances.

        实例更新时间。

        :return: The update_at of this StarRocksInstanceInfoInstances.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this StarRocksInstanceInfoInstances.

        实例更新时间。

        :param update_at: The update_at of this StarRocksInstanceInfoInstances.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def delete_at(self):
        r"""Gets the delete_at of this StarRocksInstanceInfoInstances.

        实例删除时间。

        :return: The delete_at of this StarRocksInstanceInfoInstances.
        :rtype: int
        """
        return self._delete_at

    @delete_at.setter
    def delete_at(self, delete_at):
        r"""Sets the delete_at of this StarRocksInstanceInfoInstances.

        实例删除时间。

        :param delete_at: The delete_at of this StarRocksInstanceInfoInstances.
        :type delete_at: int
        """
        self._delete_at = delete_at

    @property
    def db_port(self):
        r"""Gets the db_port of this StarRocksInstanceInfoInstances.

        数据库端口号。

        :return: The db_port of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._db_port

    @db_port.setter
    def db_port(self, db_port):
        r"""Sets the db_port of this StarRocksInstanceInfoInstances.

        数据库端口号。

        :param db_port: The db_port of this StarRocksInstanceInfoInstances.
        :type db_port: str
        """
        self._db_port = db_port

    @property
    def param_group(self):
        r"""Gets the param_group of this StarRocksInstanceInfoInstances.

        参数组。

        :return: The param_group of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._param_group

    @param_group.setter
    def param_group(self, param_group):
        r"""Sets the param_group of this StarRocksInstanceInfoInstances.

        参数组。

        :param param_group: The param_group of this StarRocksInstanceInfoInstances.
        :type param_group: str
        """
        self._param_group = param_group

    @property
    def actions(self):
        r"""Gets the actions of this StarRocksInstanceInfoInstances.

        实例动作。

        :return: The actions of this StarRocksInstanceInfoInstances.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.QueryAction`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this StarRocksInstanceInfoInstances.

        实例动作。

        :param actions: The actions of this StarRocksInstanceInfoInstances.
        :type actions: list[:class:`huaweicloudsdkgaussdb.v3.QueryAction`]
        """
        self._actions = actions

    @property
    def create_fail_error_code(self):
        r"""Gets the create_fail_error_code of this StarRocksInstanceInfoInstances.

        实例创建失败错误码。

        :return: The create_fail_error_code of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._create_fail_error_code

    @create_fail_error_code.setter
    def create_fail_error_code(self, create_fail_error_code):
        r"""Sets the create_fail_error_code of this StarRocksInstanceInfoInstances.

        实例创建失败错误码。

        :param create_fail_error_code: The create_fail_error_code of this StarRocksInstanceInfoInstances.
        :type create_fail_error_code: str
        """
        self._create_fail_error_code = create_fail_error_code

    @property
    def groups(self):
        r"""Gets the groups of this StarRocksInstanceInfoInstances.

        实例分组。

        :return: The groups of this StarRocksInstanceInfoInstances.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoGroups`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this StarRocksInstanceInfoInstances.

        实例分组。

        :param groups: The groups of this StarRocksInstanceInfoInstances.
        :type groups: list[:class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoGroups`]
        """
        self._groups = groups

    @property
    def ops_window(self):
        r"""Gets the ops_window of this StarRocksInstanceInfoInstances.

        :return: The ops_window of this StarRocksInstanceInfoInstances.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoOpsWindow`
        """
        return self._ops_window

    @ops_window.setter
    def ops_window(self, ops_window):
        r"""Sets the ops_window of this StarRocksInstanceInfoInstances.

        :param ops_window: The ops_window of this StarRocksInstanceInfoInstances.
        :type ops_window: :class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoOpsWindow`
        """
        self._ops_window = ops_window

    @property
    def tags_info(self):
        r"""Gets the tags_info of this StarRocksInstanceInfoInstances.

        :return: The tags_info of this StarRocksInstanceInfoInstances.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoTagsInfo`
        """
        return self._tags_info

    @tags_info.setter
    def tags_info(self, tags_info):
        r"""Sets the tags_info of this StarRocksInstanceInfoInstances.

        :param tags_info: The tags_info of this StarRocksInstanceInfoInstances.
        :type tags_info: :class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoTagsInfo`
        """
        self._tags_info = tags_info

    @property
    def time_zone(self):
        r"""Gets the time_zone of this StarRocksInstanceInfoInstances.

        时区。

        :return: The time_zone of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this StarRocksInstanceInfoInstances.

        时区。

        :param time_zone: The time_zone of this StarRocksInstanceInfoInstances.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def backup_used_space(self):
        r"""Gets the backup_used_space of this StarRocksInstanceInfoInstances.

        备份使用空间。

        :return: The backup_used_space of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._backup_used_space

    @backup_used_space.setter
    def backup_used_space(self, backup_used_space):
        r"""Sets the backup_used_space of this StarRocksInstanceInfoInstances.

        备份使用空间。

        :param backup_used_space: The backup_used_space of this StarRocksInstanceInfoInstances.
        :type backup_used_space: str
        """
        self._backup_used_space = backup_used_space

    @property
    def az_mode(self):
        r"""Gets the az_mode of this StarRocksInstanceInfoInstances.

        可用区模式。  取值范围：  - single：单可用区 - multi：多可用区

        :return: The az_mode of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._az_mode

    @az_mode.setter
    def az_mode(self, az_mode):
        r"""Sets the az_mode of this StarRocksInstanceInfoInstances.

        可用区模式。  取值范围：  - single：单可用区 - multi：多可用区

        :param az_mode: The az_mode of this StarRocksInstanceInfoInstances.
        :type az_mode: str
        """
        self._az_mode = az_mode

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this StarRocksInstanceInfoInstances.

        企业项目ID。

        :return: The enterprise_project_id of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this StarRocksInstanceInfoInstances.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this StarRocksInstanceInfoInstances.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def port_info(self):
        r"""Gets the port_info of this StarRocksInstanceInfoInstances.

        :return: The port_info of this StarRocksInstanceInfoInstances.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoPortInfo`
        """
        return self._port_info

    @port_info.setter
    def port_info(self, port_info):
        r"""Sets the port_info of this StarRocksInstanceInfoInstances.

        :param port_info: The port_info of this StarRocksInstanceInfoInstances.
        :type port_info: :class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoPortInfo`
        """
        self._port_info = port_info

    @property
    def fe_node_volume_code(self):
        r"""Gets the fe_node_volume_code of this StarRocksInstanceInfoInstances.

        FE节点磁盘类型。

        :return: The fe_node_volume_code of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._fe_node_volume_code

    @fe_node_volume_code.setter
    def fe_node_volume_code(self, fe_node_volume_code):
        r"""Sets the fe_node_volume_code of this StarRocksInstanceInfoInstances.

        FE节点磁盘类型。

        :param fe_node_volume_code: The fe_node_volume_code of this StarRocksInstanceInfoInstances.
        :type fe_node_volume_code: str
        """
        self._fe_node_volume_code = fe_node_volume_code

    @property
    def be_node_volume_code(self):
        r"""Gets the be_node_volume_code of this StarRocksInstanceInfoInstances.

        BE节点磁盘类型。

        :return: The be_node_volume_code of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._be_node_volume_code

    @be_node_volume_code.setter
    def be_node_volume_code(self, be_node_volume_code):
        r"""Sets the be_node_volume_code of this StarRocksInstanceInfoInstances.

        BE节点磁盘类型。

        :param be_node_volume_code: The be_node_volume_code of this StarRocksInstanceInfoInstances.
        :type be_node_volume_code: str
        """
        self._be_node_volume_code = be_node_volume_code

    @property
    def fe_node_volume_size(self):
        r"""Gets the fe_node_volume_size of this StarRocksInstanceInfoInstances.

        FE节点磁盘大小。

        :return: The fe_node_volume_size of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._fe_node_volume_size

    @fe_node_volume_size.setter
    def fe_node_volume_size(self, fe_node_volume_size):
        r"""Sets the fe_node_volume_size of this StarRocksInstanceInfoInstances.

        FE节点磁盘大小。

        :param fe_node_volume_size: The fe_node_volume_size of this StarRocksInstanceInfoInstances.
        :type fe_node_volume_size: str
        """
        self._fe_node_volume_size = fe_node_volume_size

    @property
    def be_node_volume_size(self):
        r"""Gets the be_node_volume_size of this StarRocksInstanceInfoInstances.

        BE节点磁盘大小。

        :return: The be_node_volume_size of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._be_node_volume_size

    @be_node_volume_size.setter
    def be_node_volume_size(self, be_node_volume_size):
        r"""Sets the be_node_volume_size of this StarRocksInstanceInfoInstances.

        BE节点磁盘大小。

        :param be_node_volume_size: The be_node_volume_size of this StarRocksInstanceInfoInstances.
        :type be_node_volume_size: str
        """
        self._be_node_volume_size = be_node_volume_size

    @property
    def support_data_replication(self):
        r"""Gets the support_data_replication of this StarRocksInstanceInfoInstances.

        是否支持副本。

        :return: The support_data_replication of this StarRocksInstanceInfoInstances.
        :rtype: bool
        """
        return self._support_data_replication

    @support_data_replication.setter
    def support_data_replication(self, support_data_replication):
        r"""Sets the support_data_replication of this StarRocksInstanceInfoInstances.

        是否支持副本。

        :param support_data_replication: The support_data_replication of this StarRocksInstanceInfoInstances.
        :type support_data_replication: bool
        """
        self._support_data_replication = support_data_replication

    @property
    def new_version_available(self):
        r"""Gets the new_version_available of this StarRocksInstanceInfoInstances.

        是否有数据库新版本。

        :return: The new_version_available of this StarRocksInstanceInfoInstances.
        :rtype: bool
        """
        return self._new_version_available

    @new_version_available.setter
    def new_version_available(self, new_version_available):
        r"""Sets the new_version_available of this StarRocksInstanceInfoInstances.

        是否有数据库新版本。

        :param new_version_available: The new_version_available of this StarRocksInstanceInfoInstances.
        :type new_version_available: bool
        """
        self._new_version_available = new_version_available

    @property
    def ssl_option(self):
        r"""Gets the ssl_option of this StarRocksInstanceInfoInstances.

        SSL开关。

        :return: The ssl_option of this StarRocksInstanceInfoInstances.
        :rtype: bool
        """
        return self._ssl_option

    @ssl_option.setter
    def ssl_option(self, ssl_option):
        r"""Sets the ssl_option of this StarRocksInstanceInfoInstances.

        SSL开关。

        :param ssl_option: The ssl_option of this StarRocksInstanceInfoInstances.
        :type ssl_option: bool
        """
        self._ssl_option = ssl_option

    @property
    def dedicated_resource_id(self):
        r"""Gets the dedicated_resource_id of this StarRocksInstanceInfoInstances.

        专属资源池ID，只有数据库实例属于专属资源池才会返回该参数。

        :return: The dedicated_resource_id of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._dedicated_resource_id

    @dedicated_resource_id.setter
    def dedicated_resource_id(self, dedicated_resource_id):
        r"""Sets the dedicated_resource_id of this StarRocksInstanceInfoInstances.

        专属资源池ID，只有数据库实例属于专属资源池才会返回该参数。

        :param dedicated_resource_id: The dedicated_resource_id of this StarRocksInstanceInfoInstances.
        :type dedicated_resource_id: str
        """
        self._dedicated_resource_id = dedicated_resource_id

    @property
    def pay_model(self):
        r"""Gets the pay_model of this StarRocksInstanceInfoInstances.

        支付模式。

        :return: The pay_model of this StarRocksInstanceInfoInstances.
        :rtype: str
        """
        return self._pay_model

    @pay_model.setter
    def pay_model(self, pay_model):
        r"""Sets the pay_model of this StarRocksInstanceInfoInstances.

        支付模式。

        :param pay_model: The pay_model of this StarRocksInstanceInfoInstances.
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
        if not isinstance(other, StarRocksInstanceInfoInstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
