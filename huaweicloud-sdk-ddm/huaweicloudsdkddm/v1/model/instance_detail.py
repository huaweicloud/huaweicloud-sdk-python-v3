# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDetail:

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
        'alias': 'str',
        'project_id': 'str',
        'cluster_mode': 'str',
        'status': 'str',
        'bpdomain_id': 'str',
        'user_id': 'str',
        'datastore_version': 'str',
        'datastore_type': 'str',
        'create_at': 'str',
        'update_at': 'str',
        'delete_at': 'str',
        'new_version_available': 'bool',
        'rollback_version_available': 'bool',
        'degrade_version_available': 'bool',
        'public_ip': 'str',
        'port': 'str',
        'create_fail_error_code': 'str',
        'time_zone': 'str',
        'pay_model': 'str',
        'order_id': 'str',
        'period': 'int',
        'is_frozen': 'bool',
        'frozen_time': 'str',
        'actions': 'list[ActionInfo]',
        'only_default_group': 'bool',
        'groups': 'list[DdmGroupInfo]',
        'extend_map': 'dict(str, str)',
        'tags_info': 'list[TagsInfo]',
        'admin_user_name': 'str',
        'eip_binding_info': 'object',
        'enable_ssl': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'alias': 'alias',
        'project_id': 'project_id',
        'cluster_mode': 'cluster_mode',
        'status': 'status',
        'bpdomain_id': 'bpdomain_id',
        'user_id': 'user_id',
        'datastore_version': 'datastore_version',
        'datastore_type': 'datastore_type',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'delete_at': 'delete_at',
        'new_version_available': 'new_version_available',
        'rollback_version_available': 'rollback_version_available',
        'degrade_version_available': 'degrade_version_available',
        'public_ip': 'public_ip',
        'port': 'port',
        'create_fail_error_code': 'create_fail_error_code',
        'time_zone': 'time_zone',
        'pay_model': 'pay_model',
        'order_id': 'order_id',
        'period': 'period',
        'is_frozen': 'is_frozen',
        'frozen_time': 'frozen_time',
        'actions': 'actions',
        'only_default_group': 'only_default_group',
        'groups': 'groups',
        'extend_map': 'extend_map',
        'tags_info': 'tags_info',
        'admin_user_name': 'admin_user_name',
        'eip_binding_info': 'eip_binding_info',
        'enable_ssl': 'enable_ssl'
    }

    def __init__(self, id=None, name=None, alias=None, project_id=None, cluster_mode=None, status=None, bpdomain_id=None, user_id=None, datastore_version=None, datastore_type=None, create_at=None, update_at=None, delete_at=None, new_version_available=None, rollback_version_available=None, degrade_version_available=None, public_ip=None, port=None, create_fail_error_code=None, time_zone=None, pay_model=None, order_id=None, period=None, is_frozen=None, frozen_time=None, actions=None, only_default_group=None, groups=None, extend_map=None, tags_info=None, admin_user_name=None, eip_binding_info=None, enable_ssl=None):
        r"""InstanceDetail

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 实例名称。
        :type name: str
        :param alias: 实例别名。
        :type alias: str
        :param project_id: 项目ID。
        :type project_id: str
        :param cluster_mode: 集群模式。
        :type cluster_mode: str
        :param status: 状态。
        :type status: str
        :param bpdomain_id: bpdomain_id
        :type bpdomain_id: str
        :param user_id: 账户ID。
        :type user_id: str
        :param datastore_version: 数据库版本。
        :type datastore_version: str
        :param datastore_type: 数据库类型。
        :type datastore_type: str
        :param create_at: 创建时间。
        :type create_at: str
        :param update_at: 更新时间。
        :type update_at: str
        :param delete_at: 删除时间。
        :type delete_at: str
        :param new_version_available: 是否有版本可升级。
        :type new_version_available: bool
        :param rollback_version_available: 是否有版本可回滚。
        :type rollback_version_available: bool
        :param degrade_version_available: 是否有版本可降级。
        :type degrade_version_available: bool
        :param public_ip: 公共ip。
        :type public_ip: str
        :param port: 端口。
        :type port: str
        :param create_fail_error_code: 创建失败原因编码。
        :type create_fail_error_code: str
        :param time_zone: 时区。
        :type time_zone: str
        :param pay_model: 付费模式。
        :type pay_model: str
        :param order_id: 订单ID。
        :type order_id: str
        :param period: 周期。
        :type period: int
        :param is_frozen: 是否冻结。
        :type is_frozen: bool
        :param frozen_time: 冻结时间。
        :type frozen_time: str
        :param actions: 锁状态。
        :type actions: list[:class:`huaweicloudsdkddm.v1.ActionInfo`]
        :param only_default_group: 是否只有默认组。
        :type only_default_group: bool
        :param groups: 组信息。
        :type groups: list[:class:`huaweicloudsdkddm.v1.DdmGroupInfo`]
        :param extend_map: 其他信息。
        :type extend_map: dict(str, str)
        :param tags_info: 标签信息。
        :type tags_info: list[:class:`huaweicloudsdkddm.v1.TagsInfo`]
        :param admin_user_name: 管理员账号。
        :type admin_user_name: str
        :param eip_binding_info: 绑定eip信息。
        :type eip_binding_info: object
        :param enable_ssl: 是否支持ssl。
        :type enable_ssl: int
        """
        
        

        self._id = None
        self._name = None
        self._alias = None
        self._project_id = None
        self._cluster_mode = None
        self._status = None
        self._bpdomain_id = None
        self._user_id = None
        self._datastore_version = None
        self._datastore_type = None
        self._create_at = None
        self._update_at = None
        self._delete_at = None
        self._new_version_available = None
        self._rollback_version_available = None
        self._degrade_version_available = None
        self._public_ip = None
        self._port = None
        self._create_fail_error_code = None
        self._time_zone = None
        self._pay_model = None
        self._order_id = None
        self._period = None
        self._is_frozen = None
        self._frozen_time = None
        self._actions = None
        self._only_default_group = None
        self._groups = None
        self._extend_map = None
        self._tags_info = None
        self._admin_user_name = None
        self._eip_binding_info = None
        self._enable_ssl = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if alias is not None:
            self.alias = alias
        if project_id is not None:
            self.project_id = project_id
        if cluster_mode is not None:
            self.cluster_mode = cluster_mode
        if status is not None:
            self.status = status
        if bpdomain_id is not None:
            self.bpdomain_id = bpdomain_id
        if user_id is not None:
            self.user_id = user_id
        if datastore_version is not None:
            self.datastore_version = datastore_version
        if datastore_type is not None:
            self.datastore_type = datastore_type
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if delete_at is not None:
            self.delete_at = delete_at
        if new_version_available is not None:
            self.new_version_available = new_version_available
        if rollback_version_available is not None:
            self.rollback_version_available = rollback_version_available
        if degrade_version_available is not None:
            self.degrade_version_available = degrade_version_available
        if public_ip is not None:
            self.public_ip = public_ip
        if port is not None:
            self.port = port
        if create_fail_error_code is not None:
            self.create_fail_error_code = create_fail_error_code
        if time_zone is not None:
            self.time_zone = time_zone
        if pay_model is not None:
            self.pay_model = pay_model
        if order_id is not None:
            self.order_id = order_id
        if period is not None:
            self.period = period
        if is_frozen is not None:
            self.is_frozen = is_frozen
        if frozen_time is not None:
            self.frozen_time = frozen_time
        if actions is not None:
            self.actions = actions
        if only_default_group is not None:
            self.only_default_group = only_default_group
        if groups is not None:
            self.groups = groups
        if extend_map is not None:
            self.extend_map = extend_map
        if tags_info is not None:
            self.tags_info = tags_info
        if admin_user_name is not None:
            self.admin_user_name = admin_user_name
        if eip_binding_info is not None:
            self.eip_binding_info = eip_binding_info
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl

    @property
    def id(self):
        r"""Gets the id of this InstanceDetail.

        实例ID。

        :return: The id of this InstanceDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InstanceDetail.

        实例ID。

        :param id: The id of this InstanceDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this InstanceDetail.

        实例名称。

        :return: The name of this InstanceDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstanceDetail.

        实例名称。

        :param name: The name of this InstanceDetail.
        :type name: str
        """
        self._name = name

    @property
    def alias(self):
        r"""Gets the alias of this InstanceDetail.

        实例别名。

        :return: The alias of this InstanceDetail.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this InstanceDetail.

        实例别名。

        :param alias: The alias of this InstanceDetail.
        :type alias: str
        """
        self._alias = alias

    @property
    def project_id(self):
        r"""Gets the project_id of this InstanceDetail.

        项目ID。

        :return: The project_id of this InstanceDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this InstanceDetail.

        项目ID。

        :param project_id: The project_id of this InstanceDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def cluster_mode(self):
        r"""Gets the cluster_mode of this InstanceDetail.

        集群模式。

        :return: The cluster_mode of this InstanceDetail.
        :rtype: str
        """
        return self._cluster_mode

    @cluster_mode.setter
    def cluster_mode(self, cluster_mode):
        r"""Sets the cluster_mode of this InstanceDetail.

        集群模式。

        :param cluster_mode: The cluster_mode of this InstanceDetail.
        :type cluster_mode: str
        """
        self._cluster_mode = cluster_mode

    @property
    def status(self):
        r"""Gets the status of this InstanceDetail.

        状态。

        :return: The status of this InstanceDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InstanceDetail.

        状态。

        :param status: The status of this InstanceDetail.
        :type status: str
        """
        self._status = status

    @property
    def bpdomain_id(self):
        r"""Gets the bpdomain_id of this InstanceDetail.

        bpdomain_id

        :return: The bpdomain_id of this InstanceDetail.
        :rtype: str
        """
        return self._bpdomain_id

    @bpdomain_id.setter
    def bpdomain_id(self, bpdomain_id):
        r"""Sets the bpdomain_id of this InstanceDetail.

        bpdomain_id

        :param bpdomain_id: The bpdomain_id of this InstanceDetail.
        :type bpdomain_id: str
        """
        self._bpdomain_id = bpdomain_id

    @property
    def user_id(self):
        r"""Gets the user_id of this InstanceDetail.

        账户ID。

        :return: The user_id of this InstanceDetail.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this InstanceDetail.

        账户ID。

        :param user_id: The user_id of this InstanceDetail.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def datastore_version(self):
        r"""Gets the datastore_version of this InstanceDetail.

        数据库版本。

        :return: The datastore_version of this InstanceDetail.
        :rtype: str
        """
        return self._datastore_version

    @datastore_version.setter
    def datastore_version(self, datastore_version):
        r"""Sets the datastore_version of this InstanceDetail.

        数据库版本。

        :param datastore_version: The datastore_version of this InstanceDetail.
        :type datastore_version: str
        """
        self._datastore_version = datastore_version

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this InstanceDetail.

        数据库类型。

        :return: The datastore_type of this InstanceDetail.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this InstanceDetail.

        数据库类型。

        :param datastore_type: The datastore_type of this InstanceDetail.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def create_at(self):
        r"""Gets the create_at of this InstanceDetail.

        创建时间。

        :return: The create_at of this InstanceDetail.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this InstanceDetail.

        创建时间。

        :param create_at: The create_at of this InstanceDetail.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this InstanceDetail.

        更新时间。

        :return: The update_at of this InstanceDetail.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this InstanceDetail.

        更新时间。

        :param update_at: The update_at of this InstanceDetail.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def delete_at(self):
        r"""Gets the delete_at of this InstanceDetail.

        删除时间。

        :return: The delete_at of this InstanceDetail.
        :rtype: str
        """
        return self._delete_at

    @delete_at.setter
    def delete_at(self, delete_at):
        r"""Sets the delete_at of this InstanceDetail.

        删除时间。

        :param delete_at: The delete_at of this InstanceDetail.
        :type delete_at: str
        """
        self._delete_at = delete_at

    @property
    def new_version_available(self):
        r"""Gets the new_version_available of this InstanceDetail.

        是否有版本可升级。

        :return: The new_version_available of this InstanceDetail.
        :rtype: bool
        """
        return self._new_version_available

    @new_version_available.setter
    def new_version_available(self, new_version_available):
        r"""Sets the new_version_available of this InstanceDetail.

        是否有版本可升级。

        :param new_version_available: The new_version_available of this InstanceDetail.
        :type new_version_available: bool
        """
        self._new_version_available = new_version_available

    @property
    def rollback_version_available(self):
        r"""Gets the rollback_version_available of this InstanceDetail.

        是否有版本可回滚。

        :return: The rollback_version_available of this InstanceDetail.
        :rtype: bool
        """
        return self._rollback_version_available

    @rollback_version_available.setter
    def rollback_version_available(self, rollback_version_available):
        r"""Sets the rollback_version_available of this InstanceDetail.

        是否有版本可回滚。

        :param rollback_version_available: The rollback_version_available of this InstanceDetail.
        :type rollback_version_available: bool
        """
        self._rollback_version_available = rollback_version_available

    @property
    def degrade_version_available(self):
        r"""Gets the degrade_version_available of this InstanceDetail.

        是否有版本可降级。

        :return: The degrade_version_available of this InstanceDetail.
        :rtype: bool
        """
        return self._degrade_version_available

    @degrade_version_available.setter
    def degrade_version_available(self, degrade_version_available):
        r"""Sets the degrade_version_available of this InstanceDetail.

        是否有版本可降级。

        :param degrade_version_available: The degrade_version_available of this InstanceDetail.
        :type degrade_version_available: bool
        """
        self._degrade_version_available = degrade_version_available

    @property
    def public_ip(self):
        r"""Gets the public_ip of this InstanceDetail.

        公共ip。

        :return: The public_ip of this InstanceDetail.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this InstanceDetail.

        公共ip。

        :param public_ip: The public_ip of this InstanceDetail.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def port(self):
        r"""Gets the port of this InstanceDetail.

        端口。

        :return: The port of this InstanceDetail.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this InstanceDetail.

        端口。

        :param port: The port of this InstanceDetail.
        :type port: str
        """
        self._port = port

    @property
    def create_fail_error_code(self):
        r"""Gets the create_fail_error_code of this InstanceDetail.

        创建失败原因编码。

        :return: The create_fail_error_code of this InstanceDetail.
        :rtype: str
        """
        return self._create_fail_error_code

    @create_fail_error_code.setter
    def create_fail_error_code(self, create_fail_error_code):
        r"""Sets the create_fail_error_code of this InstanceDetail.

        创建失败原因编码。

        :param create_fail_error_code: The create_fail_error_code of this InstanceDetail.
        :type create_fail_error_code: str
        """
        self._create_fail_error_code = create_fail_error_code

    @property
    def time_zone(self):
        r"""Gets the time_zone of this InstanceDetail.

        时区。

        :return: The time_zone of this InstanceDetail.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this InstanceDetail.

        时区。

        :param time_zone: The time_zone of this InstanceDetail.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def pay_model(self):
        r"""Gets the pay_model of this InstanceDetail.

        付费模式。

        :return: The pay_model of this InstanceDetail.
        :rtype: str
        """
        return self._pay_model

    @pay_model.setter
    def pay_model(self, pay_model):
        r"""Sets the pay_model of this InstanceDetail.

        付费模式。

        :param pay_model: The pay_model of this InstanceDetail.
        :type pay_model: str
        """
        self._pay_model = pay_model

    @property
    def order_id(self):
        r"""Gets the order_id of this InstanceDetail.

        订单ID。

        :return: The order_id of this InstanceDetail.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this InstanceDetail.

        订单ID。

        :param order_id: The order_id of this InstanceDetail.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def period(self):
        r"""Gets the period of this InstanceDetail.

        周期。

        :return: The period of this InstanceDetail.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this InstanceDetail.

        周期。

        :param period: The period of this InstanceDetail.
        :type period: int
        """
        self._period = period

    @property
    def is_frozen(self):
        r"""Gets the is_frozen of this InstanceDetail.

        是否冻结。

        :return: The is_frozen of this InstanceDetail.
        :rtype: bool
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        r"""Sets the is_frozen of this InstanceDetail.

        是否冻结。

        :param is_frozen: The is_frozen of this InstanceDetail.
        :type is_frozen: bool
        """
        self._is_frozen = is_frozen

    @property
    def frozen_time(self):
        r"""Gets the frozen_time of this InstanceDetail.

        冻结时间。

        :return: The frozen_time of this InstanceDetail.
        :rtype: str
        """
        return self._frozen_time

    @frozen_time.setter
    def frozen_time(self, frozen_time):
        r"""Sets the frozen_time of this InstanceDetail.

        冻结时间。

        :param frozen_time: The frozen_time of this InstanceDetail.
        :type frozen_time: str
        """
        self._frozen_time = frozen_time

    @property
    def actions(self):
        r"""Gets the actions of this InstanceDetail.

        锁状态。

        :return: The actions of this InstanceDetail.
        :rtype: list[:class:`huaweicloudsdkddm.v1.ActionInfo`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this InstanceDetail.

        锁状态。

        :param actions: The actions of this InstanceDetail.
        :type actions: list[:class:`huaweicloudsdkddm.v1.ActionInfo`]
        """
        self._actions = actions

    @property
    def only_default_group(self):
        r"""Gets the only_default_group of this InstanceDetail.

        是否只有默认组。

        :return: The only_default_group of this InstanceDetail.
        :rtype: bool
        """
        return self._only_default_group

    @only_default_group.setter
    def only_default_group(self, only_default_group):
        r"""Sets the only_default_group of this InstanceDetail.

        是否只有默认组。

        :param only_default_group: The only_default_group of this InstanceDetail.
        :type only_default_group: bool
        """
        self._only_default_group = only_default_group

    @property
    def groups(self):
        r"""Gets the groups of this InstanceDetail.

        组信息。

        :return: The groups of this InstanceDetail.
        :rtype: list[:class:`huaweicloudsdkddm.v1.DdmGroupInfo`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this InstanceDetail.

        组信息。

        :param groups: The groups of this InstanceDetail.
        :type groups: list[:class:`huaweicloudsdkddm.v1.DdmGroupInfo`]
        """
        self._groups = groups

    @property
    def extend_map(self):
        r"""Gets the extend_map of this InstanceDetail.

        其他信息。

        :return: The extend_map of this InstanceDetail.
        :rtype: dict(str, str)
        """
        return self._extend_map

    @extend_map.setter
    def extend_map(self, extend_map):
        r"""Sets the extend_map of this InstanceDetail.

        其他信息。

        :param extend_map: The extend_map of this InstanceDetail.
        :type extend_map: dict(str, str)
        """
        self._extend_map = extend_map

    @property
    def tags_info(self):
        r"""Gets the tags_info of this InstanceDetail.

        标签信息。

        :return: The tags_info of this InstanceDetail.
        :rtype: list[:class:`huaweicloudsdkddm.v1.TagsInfo`]
        """
        return self._tags_info

    @tags_info.setter
    def tags_info(self, tags_info):
        r"""Sets the tags_info of this InstanceDetail.

        标签信息。

        :param tags_info: The tags_info of this InstanceDetail.
        :type tags_info: list[:class:`huaweicloudsdkddm.v1.TagsInfo`]
        """
        self._tags_info = tags_info

    @property
    def admin_user_name(self):
        r"""Gets the admin_user_name of this InstanceDetail.

        管理员账号。

        :return: The admin_user_name of this InstanceDetail.
        :rtype: str
        """
        return self._admin_user_name

    @admin_user_name.setter
    def admin_user_name(self, admin_user_name):
        r"""Sets the admin_user_name of this InstanceDetail.

        管理员账号。

        :param admin_user_name: The admin_user_name of this InstanceDetail.
        :type admin_user_name: str
        """
        self._admin_user_name = admin_user_name

    @property
    def eip_binding_info(self):
        r"""Gets the eip_binding_info of this InstanceDetail.

        绑定eip信息。

        :return: The eip_binding_info of this InstanceDetail.
        :rtype: object
        """
        return self._eip_binding_info

    @eip_binding_info.setter
    def eip_binding_info(self, eip_binding_info):
        r"""Sets the eip_binding_info of this InstanceDetail.

        绑定eip信息。

        :param eip_binding_info: The eip_binding_info of this InstanceDetail.
        :type eip_binding_info: object
        """
        self._eip_binding_info = eip_binding_info

    @property
    def enable_ssl(self):
        r"""Gets the enable_ssl of this InstanceDetail.

        是否支持ssl。

        :return: The enable_ssl of this InstanceDetail.
        :rtype: int
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        r"""Sets the enable_ssl of this InstanceDetail.

        是否支持ssl。

        :param enable_ssl: The enable_ssl of this InstanceDetail.
        :type enable_ssl: int
        """
        self._enable_ssl = enable_ssl

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
        if not isinstance(other, InstanceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
