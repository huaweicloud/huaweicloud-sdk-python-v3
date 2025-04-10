# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StarRocksInstanceInfoNodes:

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
        'type': 'str',
        'status': 'str',
        'period': 'str',
        'volume': 'StarRocksInstanceInfoVolume',
        'cpu': 'str',
        'mem': 'str',
        'datastore': 'StarRocksInstanceInfoDatastore',
        'actions': 'list[QueryAction]',
        'priority': 'int',
        'frozen_flag': 'int',
        'db_port': 'int',
        'pay_model': 'str',
        'order_id': 'str',
        'traffic_ip': 'str',
        'traffic_ipv6': 'str',
        'az_code': 'str',
        'az_description': 'str',
        'az_type': 'str',
        'region_code': 'str',
        'create_at': 'int',
        'update_at': 'int',
        'flavor_id': 'str',
        'flavor_ref': 'str',
        'iass_flavor_ref': 'str',
        'max_connections': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'need_restart': 'bool',
        'sg_id': 'str',
        'param_group': 'dict(str, ParamGroup)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'status': 'status',
        'period': 'period',
        'volume': 'volume',
        'cpu': 'cpu',
        'mem': 'mem',
        'datastore': 'datastore',
        'actions': 'actions',
        'priority': 'priority',
        'frozen_flag': 'frozen_flag',
        'db_port': 'db_port',
        'pay_model': 'pay_model',
        'order_id': 'order_id',
        'traffic_ip': 'traffic_ip',
        'traffic_ipv6': 'traffic_ipv6',
        'az_code': 'az_code',
        'az_description': 'az_description',
        'az_type': 'az_type',
        'region_code': 'region_code',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'flavor_id': 'flavor_id',
        'flavor_ref': 'flavor_ref',
        'iass_flavor_ref': 'iass_flavor_ref',
        'max_connections': 'max_connections',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'need_restart': 'need_restart',
        'sg_id': 'sg_id',
        'param_group': 'param_group'
    }

    def __init__(self, id=None, name=None, type=None, status=None, period=None, volume=None, cpu=None, mem=None, datastore=None, actions=None, priority=None, frozen_flag=None, db_port=None, pay_model=None, order_id=None, traffic_ip=None, traffic_ipv6=None, az_code=None, az_description=None, az_type=None, region_code=None, create_at=None, update_at=None, flavor_id=None, flavor_ref=None, iass_flavor_ref=None, max_connections=None, vpc_id=None, subnet_id=None, need_restart=None, sg_id=None, param_group=None):
        r"""StarRocksInstanceInfoNodes

        The model defined in huaweicloud sdk

        :param id: 实例节点ID。
        :type id: str
        :param name: 实例节点名。
        :type name: str
        :param type: 实例节点类型。
        :type type: str
        :param status: 节点状态。  取值：  值为“creating”，表示节点正在创建。  值为“normal”，表示节点正常。  值为“abnormal”，表示节点异常。  值为“createfail”，表示节点创建失败。
        :type status: str
        :param period: 实例节点周期。
        :type period: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoVolume`
        :param cpu: 实例节点cpu数量。
        :type cpu: str
        :param mem: 实例节点内存大小（GB）。
        :type mem: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoDatastore`
        :param actions: 节点动作。
        :type actions: list[:class:`huaweicloudsdkgaussdb.v3.QueryAction`]
        :param priority: 节点优先级。
        :type priority: int
        :param frozen_flag: 冻结标志。
        :type frozen_flag: int
        :param db_port: 数据库端口号。默认3306。
        :type db_port: int
        :param pay_model: 支付模式。
        :type pay_model: str
        :param order_id: 订单号。
        :type order_id: str
        :param traffic_ip: 数据IP。
        :type traffic_ip: str
        :param traffic_ipv6: 数据IPV6。
        :type traffic_ipv6: str
        :param az_code: 可用区代码。
        :type az_code: str
        :param az_description: 可用区描述。
        :type az_description: str
        :param az_type: 可用区类型。
        :type az_type: str
        :param region_code: 实例所在区域。
        :type region_code: str
        :param create_at: 节点创建时间。
        :type create_at: int
        :param update_at: 节点更新时间。
        :type update_at: int
        :param flavor_id: 节点规格ID。
        :type flavor_id: str
        :param flavor_ref: 节点规格码。
        :type flavor_ref: str
        :param iass_flavor_ref: IASS规格码。
        :type iass_flavor_ref: str
        :param max_connections: 公网最大连接数。
        :type max_connections: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param need_restart: 参数更新是否需要重启。
        :type need_restart: bool
        :param sg_id: 安全组。
        :type sg_id: str
        :param param_group: 参数组信息。
        :type param_group: dict(str, ParamGroup)
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._status = None
        self._period = None
        self._volume = None
        self._cpu = None
        self._mem = None
        self._datastore = None
        self._actions = None
        self._priority = None
        self._frozen_flag = None
        self._db_port = None
        self._pay_model = None
        self._order_id = None
        self._traffic_ip = None
        self._traffic_ipv6 = None
        self._az_code = None
        self._az_description = None
        self._az_type = None
        self._region_code = None
        self._create_at = None
        self._update_at = None
        self._flavor_id = None
        self._flavor_ref = None
        self._iass_flavor_ref = None
        self._max_connections = None
        self._vpc_id = None
        self._subnet_id = None
        self._need_restart = None
        self._sg_id = None
        self._param_group = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if period is not None:
            self.period = period
        if volume is not None:
            self.volume = volume
        if cpu is not None:
            self.cpu = cpu
        if mem is not None:
            self.mem = mem
        if datastore is not None:
            self.datastore = datastore
        if actions is not None:
            self.actions = actions
        if priority is not None:
            self.priority = priority
        if frozen_flag is not None:
            self.frozen_flag = frozen_flag
        if db_port is not None:
            self.db_port = db_port
        if pay_model is not None:
            self.pay_model = pay_model
        if order_id is not None:
            self.order_id = order_id
        if traffic_ip is not None:
            self.traffic_ip = traffic_ip
        if traffic_ipv6 is not None:
            self.traffic_ipv6 = traffic_ipv6
        if az_code is not None:
            self.az_code = az_code
        if az_description is not None:
            self.az_description = az_description
        if az_type is not None:
            self.az_type = az_type
        if region_code is not None:
            self.region_code = region_code
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if flavor_ref is not None:
            self.flavor_ref = flavor_ref
        if iass_flavor_ref is not None:
            self.iass_flavor_ref = iass_flavor_ref
        if max_connections is not None:
            self.max_connections = max_connections
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if need_restart is not None:
            self.need_restart = need_restart
        if sg_id is not None:
            self.sg_id = sg_id
        if param_group is not None:
            self.param_group = param_group

    @property
    def id(self):
        r"""Gets the id of this StarRocksInstanceInfoNodes.

        实例节点ID。

        :return: The id of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StarRocksInstanceInfoNodes.

        实例节点ID。

        :param id: The id of this StarRocksInstanceInfoNodes.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this StarRocksInstanceInfoNodes.

        实例节点名。

        :return: The name of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StarRocksInstanceInfoNodes.

        实例节点名。

        :param name: The name of this StarRocksInstanceInfoNodes.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this StarRocksInstanceInfoNodes.

        实例节点类型。

        :return: The type of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this StarRocksInstanceInfoNodes.

        实例节点类型。

        :param type: The type of this StarRocksInstanceInfoNodes.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this StarRocksInstanceInfoNodes.

        节点状态。  取值：  值为“creating”，表示节点正在创建。  值为“normal”，表示节点正常。  值为“abnormal”，表示节点异常。  值为“createfail”，表示节点创建失败。

        :return: The status of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StarRocksInstanceInfoNodes.

        节点状态。  取值：  值为“creating”，表示节点正在创建。  值为“normal”，表示节点正常。  值为“abnormal”，表示节点异常。  值为“createfail”，表示节点创建失败。

        :param status: The status of this StarRocksInstanceInfoNodes.
        :type status: str
        """
        self._status = status

    @property
    def period(self):
        r"""Gets the period of this StarRocksInstanceInfoNodes.

        实例节点周期。

        :return: The period of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this StarRocksInstanceInfoNodes.

        实例节点周期。

        :param period: The period of this StarRocksInstanceInfoNodes.
        :type period: str
        """
        self._period = period

    @property
    def volume(self):
        r"""Gets the volume of this StarRocksInstanceInfoNodes.

        :return: The volume of this StarRocksInstanceInfoNodes.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoVolume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this StarRocksInstanceInfoNodes.

        :param volume: The volume of this StarRocksInstanceInfoNodes.
        :type volume: :class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoVolume`
        """
        self._volume = volume

    @property
    def cpu(self):
        r"""Gets the cpu of this StarRocksInstanceInfoNodes.

        实例节点cpu数量。

        :return: The cpu of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this StarRocksInstanceInfoNodes.

        实例节点cpu数量。

        :param cpu: The cpu of this StarRocksInstanceInfoNodes.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def mem(self):
        r"""Gets the mem of this StarRocksInstanceInfoNodes.

        实例节点内存大小（GB）。

        :return: The mem of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        r"""Sets the mem of this StarRocksInstanceInfoNodes.

        实例节点内存大小（GB）。

        :param mem: The mem of this StarRocksInstanceInfoNodes.
        :type mem: str
        """
        self._mem = mem

    @property
    def datastore(self):
        r"""Gets the datastore of this StarRocksInstanceInfoNodes.

        :return: The datastore of this StarRocksInstanceInfoNodes.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoDatastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this StarRocksInstanceInfoNodes.

        :param datastore: The datastore of this StarRocksInstanceInfoNodes.
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoDatastore`
        """
        self._datastore = datastore

    @property
    def actions(self):
        r"""Gets the actions of this StarRocksInstanceInfoNodes.

        节点动作。

        :return: The actions of this StarRocksInstanceInfoNodes.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.QueryAction`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this StarRocksInstanceInfoNodes.

        节点动作。

        :param actions: The actions of this StarRocksInstanceInfoNodes.
        :type actions: list[:class:`huaweicloudsdkgaussdb.v3.QueryAction`]
        """
        self._actions = actions

    @property
    def priority(self):
        r"""Gets the priority of this StarRocksInstanceInfoNodes.

        节点优先级。

        :return: The priority of this StarRocksInstanceInfoNodes.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this StarRocksInstanceInfoNodes.

        节点优先级。

        :param priority: The priority of this StarRocksInstanceInfoNodes.
        :type priority: int
        """
        self._priority = priority

    @property
    def frozen_flag(self):
        r"""Gets the frozen_flag of this StarRocksInstanceInfoNodes.

        冻结标志。

        :return: The frozen_flag of this StarRocksInstanceInfoNodes.
        :rtype: int
        """
        return self._frozen_flag

    @frozen_flag.setter
    def frozen_flag(self, frozen_flag):
        r"""Sets the frozen_flag of this StarRocksInstanceInfoNodes.

        冻结标志。

        :param frozen_flag: The frozen_flag of this StarRocksInstanceInfoNodes.
        :type frozen_flag: int
        """
        self._frozen_flag = frozen_flag

    @property
    def db_port(self):
        r"""Gets the db_port of this StarRocksInstanceInfoNodes.

        数据库端口号。默认3306。

        :return: The db_port of this StarRocksInstanceInfoNodes.
        :rtype: int
        """
        return self._db_port

    @db_port.setter
    def db_port(self, db_port):
        r"""Sets the db_port of this StarRocksInstanceInfoNodes.

        数据库端口号。默认3306。

        :param db_port: The db_port of this StarRocksInstanceInfoNodes.
        :type db_port: int
        """
        self._db_port = db_port

    @property
    def pay_model(self):
        r"""Gets the pay_model of this StarRocksInstanceInfoNodes.

        支付模式。

        :return: The pay_model of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._pay_model

    @pay_model.setter
    def pay_model(self, pay_model):
        r"""Sets the pay_model of this StarRocksInstanceInfoNodes.

        支付模式。

        :param pay_model: The pay_model of this StarRocksInstanceInfoNodes.
        :type pay_model: str
        """
        self._pay_model = pay_model

    @property
    def order_id(self):
        r"""Gets the order_id of this StarRocksInstanceInfoNodes.

        订单号。

        :return: The order_id of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this StarRocksInstanceInfoNodes.

        订单号。

        :param order_id: The order_id of this StarRocksInstanceInfoNodes.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def traffic_ip(self):
        r"""Gets the traffic_ip of this StarRocksInstanceInfoNodes.

        数据IP。

        :return: The traffic_ip of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._traffic_ip

    @traffic_ip.setter
    def traffic_ip(self, traffic_ip):
        r"""Sets the traffic_ip of this StarRocksInstanceInfoNodes.

        数据IP。

        :param traffic_ip: The traffic_ip of this StarRocksInstanceInfoNodes.
        :type traffic_ip: str
        """
        self._traffic_ip = traffic_ip

    @property
    def traffic_ipv6(self):
        r"""Gets the traffic_ipv6 of this StarRocksInstanceInfoNodes.

        数据IPV6。

        :return: The traffic_ipv6 of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._traffic_ipv6

    @traffic_ipv6.setter
    def traffic_ipv6(self, traffic_ipv6):
        r"""Sets the traffic_ipv6 of this StarRocksInstanceInfoNodes.

        数据IPV6。

        :param traffic_ipv6: The traffic_ipv6 of this StarRocksInstanceInfoNodes.
        :type traffic_ipv6: str
        """
        self._traffic_ipv6 = traffic_ipv6

    @property
    def az_code(self):
        r"""Gets the az_code of this StarRocksInstanceInfoNodes.

        可用区代码。

        :return: The az_code of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this StarRocksInstanceInfoNodes.

        可用区代码。

        :param az_code: The az_code of this StarRocksInstanceInfoNodes.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def az_description(self):
        r"""Gets the az_description of this StarRocksInstanceInfoNodes.

        可用区描述。

        :return: The az_description of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._az_description

    @az_description.setter
    def az_description(self, az_description):
        r"""Sets the az_description of this StarRocksInstanceInfoNodes.

        可用区描述。

        :param az_description: The az_description of this StarRocksInstanceInfoNodes.
        :type az_description: str
        """
        self._az_description = az_description

    @property
    def az_type(self):
        r"""Gets the az_type of this StarRocksInstanceInfoNodes.

        可用区类型。

        :return: The az_type of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._az_type

    @az_type.setter
    def az_type(self, az_type):
        r"""Sets the az_type of this StarRocksInstanceInfoNodes.

        可用区类型。

        :param az_type: The az_type of this StarRocksInstanceInfoNodes.
        :type az_type: str
        """
        self._az_type = az_type

    @property
    def region_code(self):
        r"""Gets the region_code of this StarRocksInstanceInfoNodes.

        实例所在区域。

        :return: The region_code of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        r"""Sets the region_code of this StarRocksInstanceInfoNodes.

        实例所在区域。

        :param region_code: The region_code of this StarRocksInstanceInfoNodes.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def create_at(self):
        r"""Gets the create_at of this StarRocksInstanceInfoNodes.

        节点创建时间。

        :return: The create_at of this StarRocksInstanceInfoNodes.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this StarRocksInstanceInfoNodes.

        节点创建时间。

        :param create_at: The create_at of this StarRocksInstanceInfoNodes.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this StarRocksInstanceInfoNodes.

        节点更新时间。

        :return: The update_at of this StarRocksInstanceInfoNodes.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this StarRocksInstanceInfoNodes.

        节点更新时间。

        :param update_at: The update_at of this StarRocksInstanceInfoNodes.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this StarRocksInstanceInfoNodes.

        节点规格ID。

        :return: The flavor_id of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this StarRocksInstanceInfoNodes.

        节点规格ID。

        :param flavor_id: The flavor_id of this StarRocksInstanceInfoNodes.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this StarRocksInstanceInfoNodes.

        节点规格码。

        :return: The flavor_ref of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this StarRocksInstanceInfoNodes.

        节点规格码。

        :param flavor_ref: The flavor_ref of this StarRocksInstanceInfoNodes.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def iass_flavor_ref(self):
        r"""Gets the iass_flavor_ref of this StarRocksInstanceInfoNodes.

        IASS规格码。

        :return: The iass_flavor_ref of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._iass_flavor_ref

    @iass_flavor_ref.setter
    def iass_flavor_ref(self, iass_flavor_ref):
        r"""Sets the iass_flavor_ref of this StarRocksInstanceInfoNodes.

        IASS规格码。

        :param iass_flavor_ref: The iass_flavor_ref of this StarRocksInstanceInfoNodes.
        :type iass_flavor_ref: str
        """
        self._iass_flavor_ref = iass_flavor_ref

    @property
    def max_connections(self):
        r"""Gets the max_connections of this StarRocksInstanceInfoNodes.

        公网最大连接数。

        :return: The max_connections of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._max_connections

    @max_connections.setter
    def max_connections(self, max_connections):
        r"""Sets the max_connections of this StarRocksInstanceInfoNodes.

        公网最大连接数。

        :param max_connections: The max_connections of this StarRocksInstanceInfoNodes.
        :type max_connections: str
        """
        self._max_connections = max_connections

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this StarRocksInstanceInfoNodes.

        虚拟私有云ID。

        :return: The vpc_id of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this StarRocksInstanceInfoNodes.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this StarRocksInstanceInfoNodes.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this StarRocksInstanceInfoNodes.

        子网ID。

        :return: The subnet_id of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this StarRocksInstanceInfoNodes.

        子网ID。

        :param subnet_id: The subnet_id of this StarRocksInstanceInfoNodes.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def need_restart(self):
        r"""Gets the need_restart of this StarRocksInstanceInfoNodes.

        参数更新是否需要重启。

        :return: The need_restart of this StarRocksInstanceInfoNodes.
        :rtype: bool
        """
        return self._need_restart

    @need_restart.setter
    def need_restart(self, need_restart):
        r"""Sets the need_restart of this StarRocksInstanceInfoNodes.

        参数更新是否需要重启。

        :param need_restart: The need_restart of this StarRocksInstanceInfoNodes.
        :type need_restart: bool
        """
        self._need_restart = need_restart

    @property
    def sg_id(self):
        r"""Gets the sg_id of this StarRocksInstanceInfoNodes.

        安全组。

        :return: The sg_id of this StarRocksInstanceInfoNodes.
        :rtype: str
        """
        return self._sg_id

    @sg_id.setter
    def sg_id(self, sg_id):
        r"""Sets the sg_id of this StarRocksInstanceInfoNodes.

        安全组。

        :param sg_id: The sg_id of this StarRocksInstanceInfoNodes.
        :type sg_id: str
        """
        self._sg_id = sg_id

    @property
    def param_group(self):
        r"""Gets the param_group of this StarRocksInstanceInfoNodes.

        参数组信息。

        :return: The param_group of this StarRocksInstanceInfoNodes.
        :rtype: dict(str, ParamGroup)
        """
        return self._param_group

    @param_group.setter
    def param_group(self, param_group):
        r"""Sets the param_group of this StarRocksInstanceInfoNodes.

        参数组信息。

        :param param_group: The param_group of this StarRocksInstanceInfoNodes.
        :type param_group: dict(str, ParamGroup)
        """
        self._param_group = param_group

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
        if not isinstance(other, StarRocksInstanceInfoNodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
