# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClickHouseNodeInfo:

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
        'volume': 'ClickHouseNodeInfoVolume',
        'cpu': 'str',
        'mem': 'str',
        'datastore': 'ClickHouseNodeInfoDatastore',
        'priority': 'int',
        'frozen_flag': 'int',
        'db_port': 'int',
        'pay_model': 'str',
        'order_id': 'str',
        'traffic_ip': 'str',
        'traffic_ipv6': 'str',
        'traffic_vip': 'str',
        'traffic_vipv6': 'str',
        'az_code': 'str',
        'az_description': 'str',
        'az_type': 'str',
        'region': 'str',
        'create_at': 'int',
        'update_at': 'int',
        'flavor_id': 'str',
        'flavor_ref': 'str',
        'iass_flavor_ref': 'str',
        'max_connections': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'need_restart': 'bool',
        'sg_id': 'str'
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
        'priority': 'priority',
        'frozen_flag': 'frozen_flag',
        'db_port': 'db_port',
        'pay_model': 'pay_model',
        'order_id': 'order_id',
        'traffic_ip': 'traffic_ip',
        'traffic_ipv6': 'traffic_ipv6',
        'traffic_vip': 'traffic_vip',
        'traffic_vipv6': 'traffic_vipv6',
        'az_code': 'az_code',
        'az_description': 'az_description',
        'az_type': 'az_type',
        'region': 'region',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'flavor_id': 'flavor_id',
        'flavor_ref': 'flavor_ref',
        'iass_flavor_ref': 'iass_flavor_ref',
        'max_connections': 'max_connections',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'need_restart': 'need_restart',
        'sg_id': 'sg_id'
    }

    def __init__(self, id=None, name=None, type=None, status=None, period=None, volume=None, cpu=None, mem=None, datastore=None, priority=None, frozen_flag=None, db_port=None, pay_model=None, order_id=None, traffic_ip=None, traffic_ipv6=None, traffic_vip=None, traffic_vipv6=None, az_code=None, az_description=None, az_type=None, region=None, create_at=None, update_at=None, flavor_id=None, flavor_ref=None, iass_flavor_ref=None, max_connections=None, vpc_id=None, subnet_id=None, need_restart=None, sg_id=None):
        """ClickHouseNodeInfo

        The model defined in huaweicloud sdk

        :param id: 实例节点ID。
        :type id: str
        :param name: 实例节点名。
        :type name: str
        :param type: 实例节点类型。 取值范围： - master：主节点 - slave：备节点
        :type type: str
        :param status: 实例节点状态。
        :type status: str
        :param period: 实例节点周期。
        :type period: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkgaussdb.v3.ClickHouseNodeInfoVolume`
        :param cpu: 实例节点cpu数量。
        :type cpu: str
        :param mem: 实例节点内存大小（GB）。
        :type mem: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.ClickHouseNodeInfoDatastore`
        :param priority: 节点优先级。
        :type priority: int
        :param frozen_flag: 冻结标志。 取值范围： - 0：不冻结 - 1：冻结
        :type frozen_flag: int
        :param db_port: 数据库端口号。取值范围：0~65535。
        :type db_port: int
        :param pay_model: 支付模式。 取值范围： - 0：按需计费 - 1：包周期
        :type pay_model: str
        :param order_id: 包周期订单ID。
        :type order_id: str
        :param traffic_ip: 节点数据ip。
        :type traffic_ip: str
        :param traffic_ipv6: 节点数据ipv6。
        :type traffic_ipv6: str
        :param traffic_vip: 节点数据vip。
        :type traffic_vip: str
        :param traffic_vipv6: 节点数据vipV6。
        :type traffic_vipv6: str
        :param az_code: 可用区。
        :type az_code: str
        :param az_description: 可用区描述。
        :type az_description: str
        :param az_type: 可用区类型。
        :type az_type: str
        :param region: 节点所在区。
        :type region: str
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
        :param sg_id: 安全组
        :type sg_id: str
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
        self._priority = None
        self._frozen_flag = None
        self._db_port = None
        self._pay_model = None
        self._order_id = None
        self._traffic_ip = None
        self._traffic_ipv6 = None
        self._traffic_vip = None
        self._traffic_vipv6 = None
        self._az_code = None
        self._az_description = None
        self._az_type = None
        self._region = None
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
        self.discriminator = None

        self.id = id
        self.name = name
        self.type = type
        self.status = status
        if period is not None:
            self.period = period
        self.volume = volume
        self.cpu = cpu
        self.mem = mem
        self.datastore = datastore
        self.priority = priority
        self.frozen_flag = frozen_flag
        self.db_port = db_port
        self.pay_model = pay_model
        if order_id is not None:
            self.order_id = order_id
        self.traffic_ip = traffic_ip
        if traffic_ipv6 is not None:
            self.traffic_ipv6 = traffic_ipv6
        if traffic_vip is not None:
            self.traffic_vip = traffic_vip
        if traffic_vipv6 is not None:
            self.traffic_vipv6 = traffic_vipv6
        self.az_code = az_code
        self.az_description = az_description
        self.az_type = az_type
        self.region = region
        self.create_at = create_at
        self.update_at = update_at
        self.flavor_id = flavor_id
        self.flavor_ref = flavor_ref
        self.iass_flavor_ref = iass_flavor_ref
        self.max_connections = max_connections
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.need_restart = need_restart
        self.sg_id = sg_id

    @property
    def id(self):
        """Gets the id of this ClickHouseNodeInfo.

        实例节点ID。

        :return: The id of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClickHouseNodeInfo.

        实例节点ID。

        :param id: The id of this ClickHouseNodeInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ClickHouseNodeInfo.

        实例节点名。

        :return: The name of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClickHouseNodeInfo.

        实例节点名。

        :param name: The name of this ClickHouseNodeInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ClickHouseNodeInfo.

        实例节点类型。 取值范围： - master：主节点 - slave：备节点

        :return: The type of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClickHouseNodeInfo.

        实例节点类型。 取值范围： - master：主节点 - slave：备节点

        :param type: The type of this ClickHouseNodeInfo.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this ClickHouseNodeInfo.

        实例节点状态。

        :return: The status of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClickHouseNodeInfo.

        实例节点状态。

        :param status: The status of this ClickHouseNodeInfo.
        :type status: str
        """
        self._status = status

    @property
    def period(self):
        """Gets the period of this ClickHouseNodeInfo.

        实例节点周期。

        :return: The period of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ClickHouseNodeInfo.

        实例节点周期。

        :param period: The period of this ClickHouseNodeInfo.
        :type period: str
        """
        self._period = period

    @property
    def volume(self):
        """Gets the volume of this ClickHouseNodeInfo.

        :return: The volume of this ClickHouseNodeInfo.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ClickHouseNodeInfoVolume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this ClickHouseNodeInfo.

        :param volume: The volume of this ClickHouseNodeInfo.
        :type volume: :class:`huaweicloudsdkgaussdb.v3.ClickHouseNodeInfoVolume`
        """
        self._volume = volume

    @property
    def cpu(self):
        """Gets the cpu of this ClickHouseNodeInfo.

        实例节点cpu数量。

        :return: The cpu of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ClickHouseNodeInfo.

        实例节点cpu数量。

        :param cpu: The cpu of this ClickHouseNodeInfo.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def mem(self):
        """Gets the mem of this ClickHouseNodeInfo.

        实例节点内存大小（GB）。

        :return: The mem of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        """Sets the mem of this ClickHouseNodeInfo.

        实例节点内存大小（GB）。

        :param mem: The mem of this ClickHouseNodeInfo.
        :type mem: str
        """
        self._mem = mem

    @property
    def datastore(self):
        """Gets the datastore of this ClickHouseNodeInfo.

        :return: The datastore of this ClickHouseNodeInfo.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ClickHouseNodeInfoDatastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this ClickHouseNodeInfo.

        :param datastore: The datastore of this ClickHouseNodeInfo.
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.ClickHouseNodeInfoDatastore`
        """
        self._datastore = datastore

    @property
    def priority(self):
        """Gets the priority of this ClickHouseNodeInfo.

        节点优先级。

        :return: The priority of this ClickHouseNodeInfo.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ClickHouseNodeInfo.

        节点优先级。

        :param priority: The priority of this ClickHouseNodeInfo.
        :type priority: int
        """
        self._priority = priority

    @property
    def frozen_flag(self):
        """Gets the frozen_flag of this ClickHouseNodeInfo.

        冻结标志。 取值范围： - 0：不冻结 - 1：冻结

        :return: The frozen_flag of this ClickHouseNodeInfo.
        :rtype: int
        """
        return self._frozen_flag

    @frozen_flag.setter
    def frozen_flag(self, frozen_flag):
        """Sets the frozen_flag of this ClickHouseNodeInfo.

        冻结标志。 取值范围： - 0：不冻结 - 1：冻结

        :param frozen_flag: The frozen_flag of this ClickHouseNodeInfo.
        :type frozen_flag: int
        """
        self._frozen_flag = frozen_flag

    @property
    def db_port(self):
        """Gets the db_port of this ClickHouseNodeInfo.

        数据库端口号。取值范围：0~65535。

        :return: The db_port of this ClickHouseNodeInfo.
        :rtype: int
        """
        return self._db_port

    @db_port.setter
    def db_port(self, db_port):
        """Sets the db_port of this ClickHouseNodeInfo.

        数据库端口号。取值范围：0~65535。

        :param db_port: The db_port of this ClickHouseNodeInfo.
        :type db_port: int
        """
        self._db_port = db_port

    @property
    def pay_model(self):
        """Gets the pay_model of this ClickHouseNodeInfo.

        支付模式。 取值范围： - 0：按需计费 - 1：包周期

        :return: The pay_model of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._pay_model

    @pay_model.setter
    def pay_model(self, pay_model):
        """Sets the pay_model of this ClickHouseNodeInfo.

        支付模式。 取值范围： - 0：按需计费 - 1：包周期

        :param pay_model: The pay_model of this ClickHouseNodeInfo.
        :type pay_model: str
        """
        self._pay_model = pay_model

    @property
    def order_id(self):
        """Gets the order_id of this ClickHouseNodeInfo.

        包周期订单ID。

        :return: The order_id of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ClickHouseNodeInfo.

        包周期订单ID。

        :param order_id: The order_id of this ClickHouseNodeInfo.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def traffic_ip(self):
        """Gets the traffic_ip of this ClickHouseNodeInfo.

        节点数据ip。

        :return: The traffic_ip of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._traffic_ip

    @traffic_ip.setter
    def traffic_ip(self, traffic_ip):
        """Sets the traffic_ip of this ClickHouseNodeInfo.

        节点数据ip。

        :param traffic_ip: The traffic_ip of this ClickHouseNodeInfo.
        :type traffic_ip: str
        """
        self._traffic_ip = traffic_ip

    @property
    def traffic_ipv6(self):
        """Gets the traffic_ipv6 of this ClickHouseNodeInfo.

        节点数据ipv6。

        :return: The traffic_ipv6 of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._traffic_ipv6

    @traffic_ipv6.setter
    def traffic_ipv6(self, traffic_ipv6):
        """Sets the traffic_ipv6 of this ClickHouseNodeInfo.

        节点数据ipv6。

        :param traffic_ipv6: The traffic_ipv6 of this ClickHouseNodeInfo.
        :type traffic_ipv6: str
        """
        self._traffic_ipv6 = traffic_ipv6

    @property
    def traffic_vip(self):
        """Gets the traffic_vip of this ClickHouseNodeInfo.

        节点数据vip。

        :return: The traffic_vip of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._traffic_vip

    @traffic_vip.setter
    def traffic_vip(self, traffic_vip):
        """Sets the traffic_vip of this ClickHouseNodeInfo.

        节点数据vip。

        :param traffic_vip: The traffic_vip of this ClickHouseNodeInfo.
        :type traffic_vip: str
        """
        self._traffic_vip = traffic_vip

    @property
    def traffic_vipv6(self):
        """Gets the traffic_vipv6 of this ClickHouseNodeInfo.

        节点数据vipV6。

        :return: The traffic_vipv6 of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._traffic_vipv6

    @traffic_vipv6.setter
    def traffic_vipv6(self, traffic_vipv6):
        """Sets the traffic_vipv6 of this ClickHouseNodeInfo.

        节点数据vipV6。

        :param traffic_vipv6: The traffic_vipv6 of this ClickHouseNodeInfo.
        :type traffic_vipv6: str
        """
        self._traffic_vipv6 = traffic_vipv6

    @property
    def az_code(self):
        """Gets the az_code of this ClickHouseNodeInfo.

        可用区。

        :return: The az_code of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this ClickHouseNodeInfo.

        可用区。

        :param az_code: The az_code of this ClickHouseNodeInfo.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def az_description(self):
        """Gets the az_description of this ClickHouseNodeInfo.

        可用区描述。

        :return: The az_description of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._az_description

    @az_description.setter
    def az_description(self, az_description):
        """Sets the az_description of this ClickHouseNodeInfo.

        可用区描述。

        :param az_description: The az_description of this ClickHouseNodeInfo.
        :type az_description: str
        """
        self._az_description = az_description

    @property
    def az_type(self):
        """Gets the az_type of this ClickHouseNodeInfo.

        可用区类型。

        :return: The az_type of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._az_type

    @az_type.setter
    def az_type(self, az_type):
        """Sets the az_type of this ClickHouseNodeInfo.

        可用区类型。

        :param az_type: The az_type of this ClickHouseNodeInfo.
        :type az_type: str
        """
        self._az_type = az_type

    @property
    def region(self):
        """Gets the region of this ClickHouseNodeInfo.

        节点所在区。

        :return: The region of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ClickHouseNodeInfo.

        节点所在区。

        :param region: The region of this ClickHouseNodeInfo.
        :type region: str
        """
        self._region = region

    @property
    def create_at(self):
        """Gets the create_at of this ClickHouseNodeInfo.

        节点创建时间。

        :return: The create_at of this ClickHouseNodeInfo.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this ClickHouseNodeInfo.

        节点创建时间。

        :param create_at: The create_at of this ClickHouseNodeInfo.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def update_at(self):
        """Gets the update_at of this ClickHouseNodeInfo.

        节点更新时间。

        :return: The update_at of this ClickHouseNodeInfo.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this ClickHouseNodeInfo.

        节点更新时间。

        :param update_at: The update_at of this ClickHouseNodeInfo.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def flavor_id(self):
        """Gets the flavor_id of this ClickHouseNodeInfo.

        节点规格ID。

        :return: The flavor_id of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this ClickHouseNodeInfo.

        节点规格ID。

        :param flavor_id: The flavor_id of this ClickHouseNodeInfo.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this ClickHouseNodeInfo.

        节点规格码。

        :return: The flavor_ref of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this ClickHouseNodeInfo.

        节点规格码。

        :param flavor_ref: The flavor_ref of this ClickHouseNodeInfo.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def iass_flavor_ref(self):
        """Gets the iass_flavor_ref of this ClickHouseNodeInfo.

        IASS规格码。

        :return: The iass_flavor_ref of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._iass_flavor_ref

    @iass_flavor_ref.setter
    def iass_flavor_ref(self, iass_flavor_ref):
        """Sets the iass_flavor_ref of this ClickHouseNodeInfo.

        IASS规格码。

        :param iass_flavor_ref: The iass_flavor_ref of this ClickHouseNodeInfo.
        :type iass_flavor_ref: str
        """
        self._iass_flavor_ref = iass_flavor_ref

    @property
    def max_connections(self):
        """Gets the max_connections of this ClickHouseNodeInfo.

        公网最大连接数。

        :return: The max_connections of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._max_connections

    @max_connections.setter
    def max_connections(self, max_connections):
        """Sets the max_connections of this ClickHouseNodeInfo.

        公网最大连接数。

        :param max_connections: The max_connections of this ClickHouseNodeInfo.
        :type max_connections: str
        """
        self._max_connections = max_connections

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ClickHouseNodeInfo.

        虚拟私有云ID。

        :return: The vpc_id of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ClickHouseNodeInfo.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this ClickHouseNodeInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ClickHouseNodeInfo.

        子网ID。

        :return: The subnet_id of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ClickHouseNodeInfo.

        子网ID。

        :param subnet_id: The subnet_id of this ClickHouseNodeInfo.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def need_restart(self):
        """Gets the need_restart of this ClickHouseNodeInfo.

        参数更新是否需要重启。

        :return: The need_restart of this ClickHouseNodeInfo.
        :rtype: bool
        """
        return self._need_restart

    @need_restart.setter
    def need_restart(self, need_restart):
        """Sets the need_restart of this ClickHouseNodeInfo.

        参数更新是否需要重启。

        :param need_restart: The need_restart of this ClickHouseNodeInfo.
        :type need_restart: bool
        """
        self._need_restart = need_restart

    @property
    def sg_id(self):
        """Gets the sg_id of this ClickHouseNodeInfo.

        安全组

        :return: The sg_id of this ClickHouseNodeInfo.
        :rtype: str
        """
        return self._sg_id

    @sg_id.setter
    def sg_id(self, sg_id):
        """Sets the sg_id of this ClickHouseNodeInfo.

        安全组

        :param sg_id: The sg_id of this ClickHouseNodeInfo.
        :type sg_id: str
        """
        self._sg_id = sg_id

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
        if not isinstance(other, ClickHouseNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
