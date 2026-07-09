# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseAuditV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'binding_db_type': 'str',
        'charge_model': 'str',
        'comment': 'str',
        'config_num': 'int',
        'connect_ipv6': 'str',
        'connect_ip': 'str',
        'cpu': 'int',
        'created': 'str',
        'database_limit': 'int',
        'effect': 'int',
        'enterprise_project_id': 'str',
        'expired': 'str',
        'failed_reason': 'str',
        'instance_id': 'str',
        'keep_days': 'str',
        'name': 'str',
        'new_version': 'str',
        'port_id': 'str',
        'ram': 'int',
        'region': 'str',
        'remain_days': 'str',
        'resource_id': 'str',
        'resource_spec_code': 'str',
        'scene': 'str',
        'security_group_id': 'str',
        'specification': 'str',
        'status': 'str',
        'subnet_id': 'str',
        'supported_feature': 'list[str]',
        'task': 'str',
        'timezone': 'str',
        'upgrade_log': 'str',
        'version': 'str',
        'vpc_id': 'str',
        'zone': 'str'
    }

    attribute_map = {
        'binding_db_type': 'binding_db_type',
        'charge_model': 'charge_model',
        'comment': 'comment',
        'config_num': 'config_num',
        'connect_ipv6': 'connectIpv6',
        'connect_ip': 'connect_ip',
        'cpu': 'cpu',
        'created': 'created',
        'database_limit': 'database_limit',
        'effect': 'effect',
        'enterprise_project_id': 'enterprise_project_id',
        'expired': 'expired',
        'failed_reason': 'failed_reason',
        'instance_id': 'instance_id',
        'keep_days': 'keep_days',
        'name': 'name',
        'new_version': 'new_version',
        'port_id': 'port_id',
        'ram': 'ram',
        'region': 'region',
        'remain_days': 'remain_days',
        'resource_id': 'resource_id',
        'resource_spec_code': 'resource_spec_code',
        'scene': 'scene',
        'security_group_id': 'security_group_id',
        'specification': 'specification',
        'status': 'status',
        'subnet_id': 'subnet_id',
        'supported_feature': 'supported_feature',
        'task': 'task',
        'timezone': 'timezone',
        'upgrade_log': 'upgrade_log',
        'version': 'version',
        'vpc_id': 'vpc_id',
        'zone': 'zone'
    }

    def __init__(self, binding_db_type=None, charge_model=None, comment=None, config_num=None, connect_ipv6=None, connect_ip=None, cpu=None, created=None, database_limit=None, effect=None, enterprise_project_id=None, expired=None, failed_reason=None, instance_id=None, keep_days=None, name=None, new_version=None, port_id=None, ram=None, region=None, remain_days=None, resource_id=None, resource_spec_code=None, scene=None, security_group_id=None, specification=None, status=None, subnet_id=None, supported_feature=None, task=None, timezone=None, upgrade_log=None, version=None, vpc_id=None, zone=None):
        r"""ResponseAuditV2

        The model defined in huaweicloud sdk

        :param binding_db_type: 绑定数据库类型
        :type binding_db_type: str
        :param charge_model: 付费模式  - Period：包周期 - Demand：按需。
        :type charge_model: str
        :param comment: 备注
        :type comment: str
        :param config_num: 已配置数据库数量
        :type config_num: int
        :param connect_ipv6: IPV6
        :type connect_ipv6: str
        :param connect_ip: IPV4
        :type connect_ip: str
        :param cpu: CPU数量
        :type cpu: int
        :param created: 创建时间
        :type created: str
        :param database_limit: 数据库数量限额
        :type database_limit: int
        :param effect: 实例结果状态 - 1：冻结可释放  - 2：冻结不可释放 - 3：冻结后不可续费
        :type effect: int
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param expired: 过期时间
        :type expired: str
        :param failed_reason: 失败原因
        :type failed_reason: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param keep_days: 在线天数
        :type keep_days: str
        :param name: 实例名称
        :type name: str
        :param new_version: 最新版本
        :type new_version: str
        :param port_id: 端口ID
        :type port_id: str
        :param ram: 内存大小
        :type ram: int
        :param region: 所属区域
        :type region: str
        :param remain_days: 剩余天数
        :type remain_days: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_spec_code: 资源规格编码
        :type resource_spec_code: str
        :param scene: 冻结场景  - POLICE: 公安冻结  - ILLEGAL: 违规冻结  - VERIFY: 未实名认证冻结  - PARTNER: 合作伙伴冻结 - ARREARS: 普通冻结（普通）
        :type scene: str
        :param security_group_id: 安全组ID
        :type security_group_id: str
        :param specification: 规格
        :type specification: str
        :param status: 实例状态  - SHUTOFF: 已关闭  - ACTIVE: 运行中，允许任何操作   - DELETING: 删除中，不允许任何操作  - BUILD: 创建中，不允许任何操作  - DELETED: 已删除，不需要展示  - ERROR: 故障，只允许删除  - HAWAIT: 等待备机创建成功，不允许任何操作  - FROZEN: 已冻结，只允许续费、绑定/解绑  - UPGRADING: 升级中，不允许升级操作
        :type status: str
        :param subnet_id: 子网ID
        :type subnet_id: str
        :param supported_feature: 功能列表
        :type supported_feature: list[str]
        :param task: 任务状态  - powering-on: 正在开启，实例可以绑定、解绑  - powering-off: 正在关闭，实例可以绑定、解绑  - rebooting: 正在重启，实例可以绑定、解绑  - delete_wait: 等待删除，集群与实例不允许任何操作  - NO_TASK: 不展示
        :type task: str
        :param timezone: 时区
        :type timezone: str
        :param upgrade_log: 升级日志
        :type upgrade_log: str
        :param version: 实例版本
        :type version: str
        :param vpc_id: VPC私有云ID
        :type vpc_id: str
        :param zone: 可用区
        :type zone: str
        """
        
        

        self._binding_db_type = None
        self._charge_model = None
        self._comment = None
        self._config_num = None
        self._connect_ipv6 = None
        self._connect_ip = None
        self._cpu = None
        self._created = None
        self._database_limit = None
        self._effect = None
        self._enterprise_project_id = None
        self._expired = None
        self._failed_reason = None
        self._instance_id = None
        self._keep_days = None
        self._name = None
        self._new_version = None
        self._port_id = None
        self._ram = None
        self._region = None
        self._remain_days = None
        self._resource_id = None
        self._resource_spec_code = None
        self._scene = None
        self._security_group_id = None
        self._specification = None
        self._status = None
        self._subnet_id = None
        self._supported_feature = None
        self._task = None
        self._timezone = None
        self._upgrade_log = None
        self._version = None
        self._vpc_id = None
        self._zone = None
        self.discriminator = None

        if binding_db_type is not None:
            self.binding_db_type = binding_db_type
        self.charge_model = charge_model
        self.comment = comment
        self.config_num = config_num
        if connect_ipv6 is not None:
            self.connect_ipv6 = connect_ipv6
        self.connect_ip = connect_ip
        self.cpu = cpu
        self.created = created
        self.database_limit = database_limit
        self.effect = effect
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.expired = expired
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if instance_id is not None:
            self.instance_id = instance_id
        self.keep_days = keep_days
        self.name = name
        self.new_version = new_version
        self.port_id = port_id
        self.ram = ram
        self.region = region
        self.remain_days = remain_days
        self.resource_id = resource_id
        self.resource_spec_code = resource_spec_code
        self.scene = scene
        self.security_group_id = security_group_id
        self.specification = specification
        self.status = status
        self.subnet_id = subnet_id
        if supported_feature is not None:
            self.supported_feature = supported_feature
        self.task = task
        if timezone is not None:
            self.timezone = timezone
        if upgrade_log is not None:
            self.upgrade_log = upgrade_log
        self.version = version
        self.vpc_id = vpc_id
        self.zone = zone

    @property
    def binding_db_type(self):
        r"""Gets the binding_db_type of this ResponseAuditV2.

        绑定数据库类型

        :return: The binding_db_type of this ResponseAuditV2.
        :rtype: str
        """
        return self._binding_db_type

    @binding_db_type.setter
    def binding_db_type(self, binding_db_type):
        r"""Sets the binding_db_type of this ResponseAuditV2.

        绑定数据库类型

        :param binding_db_type: The binding_db_type of this ResponseAuditV2.
        :type binding_db_type: str
        """
        self._binding_db_type = binding_db_type

    @property
    def charge_model(self):
        r"""Gets the charge_model of this ResponseAuditV2.

        付费模式  - Period：包周期 - Demand：按需。

        :return: The charge_model of this ResponseAuditV2.
        :rtype: str
        """
        return self._charge_model

    @charge_model.setter
    def charge_model(self, charge_model):
        r"""Sets the charge_model of this ResponseAuditV2.

        付费模式  - Period：包周期 - Demand：按需。

        :param charge_model: The charge_model of this ResponseAuditV2.
        :type charge_model: str
        """
        self._charge_model = charge_model

    @property
    def comment(self):
        r"""Gets the comment of this ResponseAuditV2.

        备注

        :return: The comment of this ResponseAuditV2.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this ResponseAuditV2.

        备注

        :param comment: The comment of this ResponseAuditV2.
        :type comment: str
        """
        self._comment = comment

    @property
    def config_num(self):
        r"""Gets the config_num of this ResponseAuditV2.

        已配置数据库数量

        :return: The config_num of this ResponseAuditV2.
        :rtype: int
        """
        return self._config_num

    @config_num.setter
    def config_num(self, config_num):
        r"""Sets the config_num of this ResponseAuditV2.

        已配置数据库数量

        :param config_num: The config_num of this ResponseAuditV2.
        :type config_num: int
        """
        self._config_num = config_num

    @property
    def connect_ipv6(self):
        r"""Gets the connect_ipv6 of this ResponseAuditV2.

        IPV6

        :return: The connect_ipv6 of this ResponseAuditV2.
        :rtype: str
        """
        return self._connect_ipv6

    @connect_ipv6.setter
    def connect_ipv6(self, connect_ipv6):
        r"""Sets the connect_ipv6 of this ResponseAuditV2.

        IPV6

        :param connect_ipv6: The connect_ipv6 of this ResponseAuditV2.
        :type connect_ipv6: str
        """
        self._connect_ipv6 = connect_ipv6

    @property
    def connect_ip(self):
        r"""Gets the connect_ip of this ResponseAuditV2.

        IPV4

        :return: The connect_ip of this ResponseAuditV2.
        :rtype: str
        """
        return self._connect_ip

    @connect_ip.setter
    def connect_ip(self, connect_ip):
        r"""Sets the connect_ip of this ResponseAuditV2.

        IPV4

        :param connect_ip: The connect_ip of this ResponseAuditV2.
        :type connect_ip: str
        """
        self._connect_ip = connect_ip

    @property
    def cpu(self):
        r"""Gets the cpu of this ResponseAuditV2.

        CPU数量

        :return: The cpu of this ResponseAuditV2.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ResponseAuditV2.

        CPU数量

        :param cpu: The cpu of this ResponseAuditV2.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def created(self):
        r"""Gets the created of this ResponseAuditV2.

        创建时间

        :return: The created of this ResponseAuditV2.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ResponseAuditV2.

        创建时间

        :param created: The created of this ResponseAuditV2.
        :type created: str
        """
        self._created = created

    @property
    def database_limit(self):
        r"""Gets the database_limit of this ResponseAuditV2.

        数据库数量限额

        :return: The database_limit of this ResponseAuditV2.
        :rtype: int
        """
        return self._database_limit

    @database_limit.setter
    def database_limit(self, database_limit):
        r"""Sets the database_limit of this ResponseAuditV2.

        数据库数量限额

        :param database_limit: The database_limit of this ResponseAuditV2.
        :type database_limit: int
        """
        self._database_limit = database_limit

    @property
    def effect(self):
        r"""Gets the effect of this ResponseAuditV2.

        实例结果状态 - 1：冻结可释放  - 2：冻结不可释放 - 3：冻结后不可续费

        :return: The effect of this ResponseAuditV2.
        :rtype: int
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        r"""Sets the effect of this ResponseAuditV2.

        实例结果状态 - 1：冻结可释放  - 2：冻结不可释放 - 3：冻结后不可续费

        :param effect: The effect of this ResponseAuditV2.
        :type effect: int
        """
        self._effect = effect

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ResponseAuditV2.

        企业项目ID

        :return: The enterprise_project_id of this ResponseAuditV2.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ResponseAuditV2.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ResponseAuditV2.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def expired(self):
        r"""Gets the expired of this ResponseAuditV2.

        过期时间

        :return: The expired of this ResponseAuditV2.
        :rtype: str
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        r"""Sets the expired of this ResponseAuditV2.

        过期时间

        :param expired: The expired of this ResponseAuditV2.
        :type expired: str
        """
        self._expired = expired

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this ResponseAuditV2.

        失败原因

        :return: The failed_reason of this ResponseAuditV2.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this ResponseAuditV2.

        失败原因

        :param failed_reason: The failed_reason of this ResponseAuditV2.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ResponseAuditV2.

        实例ID

        :return: The instance_id of this ResponseAuditV2.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ResponseAuditV2.

        实例ID

        :param instance_id: The instance_id of this ResponseAuditV2.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def keep_days(self):
        r"""Gets the keep_days of this ResponseAuditV2.

        在线天数

        :return: The keep_days of this ResponseAuditV2.
        :rtype: str
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this ResponseAuditV2.

        在线天数

        :param keep_days: The keep_days of this ResponseAuditV2.
        :type keep_days: str
        """
        self._keep_days = keep_days

    @property
    def name(self):
        r"""Gets the name of this ResponseAuditV2.

        实例名称

        :return: The name of this ResponseAuditV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ResponseAuditV2.

        实例名称

        :param name: The name of this ResponseAuditV2.
        :type name: str
        """
        self._name = name

    @property
    def new_version(self):
        r"""Gets the new_version of this ResponseAuditV2.

        最新版本

        :return: The new_version of this ResponseAuditV2.
        :rtype: str
        """
        return self._new_version

    @new_version.setter
    def new_version(self, new_version):
        r"""Sets the new_version of this ResponseAuditV2.

        最新版本

        :param new_version: The new_version of this ResponseAuditV2.
        :type new_version: str
        """
        self._new_version = new_version

    @property
    def port_id(self):
        r"""Gets the port_id of this ResponseAuditV2.

        端口ID

        :return: The port_id of this ResponseAuditV2.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this ResponseAuditV2.

        端口ID

        :param port_id: The port_id of this ResponseAuditV2.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def ram(self):
        r"""Gets the ram of this ResponseAuditV2.

        内存大小

        :return: The ram of this ResponseAuditV2.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this ResponseAuditV2.

        内存大小

        :param ram: The ram of this ResponseAuditV2.
        :type ram: int
        """
        self._ram = ram

    @property
    def region(self):
        r"""Gets the region of this ResponseAuditV2.

        所属区域

        :return: The region of this ResponseAuditV2.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ResponseAuditV2.

        所属区域

        :param region: The region of this ResponseAuditV2.
        :type region: str
        """
        self._region = region

    @property
    def remain_days(self):
        r"""Gets the remain_days of this ResponseAuditV2.

        剩余天数

        :return: The remain_days of this ResponseAuditV2.
        :rtype: str
        """
        return self._remain_days

    @remain_days.setter
    def remain_days(self, remain_days):
        r"""Sets the remain_days of this ResponseAuditV2.

        剩余天数

        :param remain_days: The remain_days of this ResponseAuditV2.
        :type remain_days: str
        """
        self._remain_days = remain_days

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ResponseAuditV2.

        资源ID

        :return: The resource_id of this ResponseAuditV2.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ResponseAuditV2.

        资源ID

        :param resource_id: The resource_id of this ResponseAuditV2.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ResponseAuditV2.

        资源规格编码

        :return: The resource_spec_code of this ResponseAuditV2.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ResponseAuditV2.

        资源规格编码

        :param resource_spec_code: The resource_spec_code of this ResponseAuditV2.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def scene(self):
        r"""Gets the scene of this ResponseAuditV2.

        冻结场景  - POLICE: 公安冻结  - ILLEGAL: 违规冻结  - VERIFY: 未实名认证冻结  - PARTNER: 合作伙伴冻结 - ARREARS: 普通冻结（普通）

        :return: The scene of this ResponseAuditV2.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this ResponseAuditV2.

        冻结场景  - POLICE: 公安冻结  - ILLEGAL: 违规冻结  - VERIFY: 未实名认证冻结  - PARTNER: 合作伙伴冻结 - ARREARS: 普通冻结（普通）

        :param scene: The scene of this ResponseAuditV2.
        :type scene: str
        """
        self._scene = scene

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this ResponseAuditV2.

        安全组ID

        :return: The security_group_id of this ResponseAuditV2.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this ResponseAuditV2.

        安全组ID

        :param security_group_id: The security_group_id of this ResponseAuditV2.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def specification(self):
        r"""Gets the specification of this ResponseAuditV2.

        规格

        :return: The specification of this ResponseAuditV2.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this ResponseAuditV2.

        规格

        :param specification: The specification of this ResponseAuditV2.
        :type specification: str
        """
        self._specification = specification

    @property
    def status(self):
        r"""Gets the status of this ResponseAuditV2.

        实例状态  - SHUTOFF: 已关闭  - ACTIVE: 运行中，允许任何操作   - DELETING: 删除中，不允许任何操作  - BUILD: 创建中，不允许任何操作  - DELETED: 已删除，不需要展示  - ERROR: 故障，只允许删除  - HAWAIT: 等待备机创建成功，不允许任何操作  - FROZEN: 已冻结，只允许续费、绑定/解绑  - UPGRADING: 升级中，不允许升级操作

        :return: The status of this ResponseAuditV2.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ResponseAuditV2.

        实例状态  - SHUTOFF: 已关闭  - ACTIVE: 运行中，允许任何操作   - DELETING: 删除中，不允许任何操作  - BUILD: 创建中，不允许任何操作  - DELETED: 已删除，不需要展示  - ERROR: 故障，只允许删除  - HAWAIT: 等待备机创建成功，不允许任何操作  - FROZEN: 已冻结，只允许续费、绑定/解绑  - UPGRADING: 升级中，不允许升级操作

        :param status: The status of this ResponseAuditV2.
        :type status: str
        """
        self._status = status

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ResponseAuditV2.

        子网ID

        :return: The subnet_id of this ResponseAuditV2.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ResponseAuditV2.

        子网ID

        :param subnet_id: The subnet_id of this ResponseAuditV2.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def supported_feature(self):
        r"""Gets the supported_feature of this ResponseAuditV2.

        功能列表

        :return: The supported_feature of this ResponseAuditV2.
        :rtype: list[str]
        """
        return self._supported_feature

    @supported_feature.setter
    def supported_feature(self, supported_feature):
        r"""Sets the supported_feature of this ResponseAuditV2.

        功能列表

        :param supported_feature: The supported_feature of this ResponseAuditV2.
        :type supported_feature: list[str]
        """
        self._supported_feature = supported_feature

    @property
    def task(self):
        r"""Gets the task of this ResponseAuditV2.

        任务状态  - powering-on: 正在开启，实例可以绑定、解绑  - powering-off: 正在关闭，实例可以绑定、解绑  - rebooting: 正在重启，实例可以绑定、解绑  - delete_wait: 等待删除，集群与实例不允许任何操作  - NO_TASK: 不展示

        :return: The task of this ResponseAuditV2.
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        r"""Sets the task of this ResponseAuditV2.

        任务状态  - powering-on: 正在开启，实例可以绑定、解绑  - powering-off: 正在关闭，实例可以绑定、解绑  - rebooting: 正在重启，实例可以绑定、解绑  - delete_wait: 等待删除，集群与实例不允许任何操作  - NO_TASK: 不展示

        :param task: The task of this ResponseAuditV2.
        :type task: str
        """
        self._task = task

    @property
    def timezone(self):
        r"""Gets the timezone of this ResponseAuditV2.

        时区

        :return: The timezone of this ResponseAuditV2.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        r"""Sets the timezone of this ResponseAuditV2.

        时区

        :param timezone: The timezone of this ResponseAuditV2.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def upgrade_log(self):
        r"""Gets the upgrade_log of this ResponseAuditV2.

        升级日志

        :return: The upgrade_log of this ResponseAuditV2.
        :rtype: str
        """
        return self._upgrade_log

    @upgrade_log.setter
    def upgrade_log(self, upgrade_log):
        r"""Sets the upgrade_log of this ResponseAuditV2.

        升级日志

        :param upgrade_log: The upgrade_log of this ResponseAuditV2.
        :type upgrade_log: str
        """
        self._upgrade_log = upgrade_log

    @property
    def version(self):
        r"""Gets the version of this ResponseAuditV2.

        实例版本

        :return: The version of this ResponseAuditV2.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ResponseAuditV2.

        实例版本

        :param version: The version of this ResponseAuditV2.
        :type version: str
        """
        self._version = version

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ResponseAuditV2.

        VPC私有云ID

        :return: The vpc_id of this ResponseAuditV2.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ResponseAuditV2.

        VPC私有云ID

        :param vpc_id: The vpc_id of this ResponseAuditV2.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def zone(self):
        r"""Gets the zone of this ResponseAuditV2.

        可用区

        :return: The zone of this ResponseAuditV2.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        r"""Sets the zone of this ResponseAuditV2.

        可用区

        :param zone: The zone of this ResponseAuditV2.
        :type zone: str
        """
        self._zone = zone

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
        if not isinstance(other, ResponseAuditV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
