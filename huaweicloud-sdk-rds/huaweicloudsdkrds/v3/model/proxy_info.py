# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProxyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_id': 'str',
        'status': 'str',
        'address': 'str',
        'port': 'int',
        'delay_threshold_in_seconds': 'int',
        'cpu': 'str',
        'mem': 'str',
        'node_num': 'int',
        'nodes': 'list[ProxyInfoNodes]',
        'mode': 'str',
        'flavor_info': 'ProxyInfoFlavorInfo',
        'transaction_split': 'str',
        'connection_pool_type': 'str',
        'pay_mode': 'str',
        'name': 'str',
        'proxy_mode': 'str',
        'dns_name': 'str',
        'subnet_id': 'str',
        'seconds_level_monitor_fun_status': 'str',
        'alt_flag': 'bool',
        'force_read_only': 'bool',
        'route_mode': 'int',
        'ssl_option': 'bool',
        'support_balance_route_mode': 'bool',
        'support_proxy_ssl': 'bool',
        'support_switch_connection_pool_type': 'bool',
        'support_transaction_split': 'bool'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'status': 'status',
        'address': 'address',
        'port': 'port',
        'delay_threshold_in_seconds': 'delay_threshold_in_seconds',
        'cpu': 'cpu',
        'mem': 'mem',
        'node_num': 'node_num',
        'nodes': 'nodes',
        'mode': 'mode',
        'flavor_info': 'flavor_info',
        'transaction_split': 'transaction_split',
        'connection_pool_type': 'connection_pool_type',
        'pay_mode': 'pay_mode',
        'name': 'name',
        'proxy_mode': 'proxy_mode',
        'dns_name': 'dns_name',
        'subnet_id': 'subnet_id',
        'seconds_level_monitor_fun_status': 'seconds_level_monitor_fun_status',
        'alt_flag': 'alt_flag',
        'force_read_only': 'force_read_only',
        'route_mode': 'route_mode',
        'ssl_option': 'ssl_option',
        'support_balance_route_mode': 'support_balance_route_mode',
        'support_proxy_ssl': 'support_proxy_ssl',
        'support_switch_connection_pool_type': 'support_switch_connection_pool_type',
        'support_transaction_split': 'support_transaction_split'
    }

    def __init__(self, pool_id=None, status=None, address=None, port=None, delay_threshold_in_seconds=None, cpu=None, mem=None, node_num=None, nodes=None, mode=None, flavor_info=None, transaction_split=None, connection_pool_type=None, pay_mode=None, name=None, proxy_mode=None, dns_name=None, subnet_id=None, seconds_level_monitor_fun_status=None, alt_flag=None, force_read_only=None, route_mode=None, ssl_option=None, support_balance_route_mode=None, support_proxy_ssl=None, support_switch_connection_pool_type=None, support_transaction_split=None):
        r"""ProxyInfo

        The model defined in huaweicloud sdk

        :param pool_id: 数据库代理实例ID。
        :type pool_id: str
        :param status: 数据库代理状态。  取值: NORMAL：表示数据库代理正常。 ENABLING：表示数据库代理正在开启。 DISABLING：表示数据库代理正在关闭。 CHANGING_NODE_NUM：表示数据库代理正在调整节点数量。 SCALING: 表示数据库代理正在规格变更。 UPGRADING: 表示数据库代理正在升级内核版本。 IPMODIFYING: 表示数据库代理正在修改读写分离地址。 RESTARTING: 表示数据库代理正在重启进程。 TRANSACTION_SPLITTING: 表示数据库代理正在变更事务拆分功能状态。 CONNECTION_POOL_SWITCH_OPERATING: 表示数据库代理正在变更会话连接池类型。 PORT_MODIFYING: 表示数据库代理正在修改端口。 PROXY_SSL_SWITCHING: 表示数据库代理正在变更SSL状态。 ALT_SWITCH_OPERATING: 表示数据库代理正在变更ALT状态。 CHANGING_RESOURCES: 表示数据库代理正在进行资源变更。 NORMAL: 表示数据库代理正常。 ABNORMAL: 表示数据库代理异常。 FAILED: 表示数据库代理创建失败。 FROZEN: 表示数据库代理已冻结。
        :type status: str
        :param address: 读写分离地址。
        :type address: str
        :param port: 端口号。
        :type port: int
        :param delay_threshold_in_seconds: 延时阈值，单位：秒。
        :type delay_threshold_in_seconds: int
        :param cpu: 数据库代理规格的CPU大小。
        :type cpu: str
        :param mem: 数据库代理规格的内存大小。
        :type mem: str
        :param node_num: 数据库代理节点个数。
        :type node_num: int
        :param nodes: 数据库代理节点信息列表。
        :type nodes: list[:class:`huaweicloudsdkrds.v3.ProxyInfoNodes`]
        :param mode: 数据库代理集群模式。 取值：     Cluster：集群模式     Ha：主备模式
        :type mode: str
        :param flavor_info: 
        :type flavor_info: :class:`huaweicloudsdkrds.v3.ProxyInfoFlavorInfo`
        :param transaction_split: 数据库代理事务拆分开关状态。  true：开启。  false：关闭。
        :type transaction_split: str
        :param connection_pool_type: 连接池类型。  取值范围:  CLOSED: 关闭连接池。  SESSION: 开启会话级连接池。
        :type connection_pool_type: str
        :param pay_mode: 数据库代理计费模式。  取值范围： 0:按需计费 1:包周期计费
        :type pay_mode: str
        :param name: 数据库代理名称。
        :type name: str
        :param proxy_mode: 数据库代理读写模式。 取值范围：     readwrite 读写模式     readonly 只读模式
        :type proxy_mode: str
        :param dns_name: 数据库代理读写分离地址内网域名。 该字段为空表示未申请读写内网域名。
        :type dns_name: str
        :param subnet_id: 数据库代理实例所属子网ID。
        :type subnet_id: str
        :param seconds_level_monitor_fun_status: 数据库代理秒级监控状态。
        :type seconds_level_monitor_fun_status: str
        :param alt_flag: ALT开关状态。
        :type alt_flag: bool
        :param force_read_only: 是否强制读路由到只读。
        :type force_read_only: bool
        :param route_mode: 数据库代理路由模式。 取值范围:     0：表示权重负载模式。     1：表示负载均衡模式（数据库主实例不接受读请求）。     2：表示负载均衡模式（数据库主实例接受读请求）。
        :type route_mode: int
        :param ssl_option: ssl开关状态。
        :type ssl_option: bool
        :param support_balance_route_mode: 数据库代理是否支持开启负载均衡路由模式。
        :type support_balance_route_mode: bool
        :param support_proxy_ssl: 数据库代理是否支持开启ssl功能。
        :type support_proxy_ssl: bool
        :param support_switch_connection_pool_type: 数据库代理是否支持切换会话连接池类型。
        :type support_switch_connection_pool_type: bool
        :param support_transaction_split: 数据库代理是否支持开启事务拆分。
        :type support_transaction_split: bool
        """
        
        

        self._pool_id = None
        self._status = None
        self._address = None
        self._port = None
        self._delay_threshold_in_seconds = None
        self._cpu = None
        self._mem = None
        self._node_num = None
        self._nodes = None
        self._mode = None
        self._flavor_info = None
        self._transaction_split = None
        self._connection_pool_type = None
        self._pay_mode = None
        self._name = None
        self._proxy_mode = None
        self._dns_name = None
        self._subnet_id = None
        self._seconds_level_monitor_fun_status = None
        self._alt_flag = None
        self._force_read_only = None
        self._route_mode = None
        self._ssl_option = None
        self._support_balance_route_mode = None
        self._support_proxy_ssl = None
        self._support_switch_connection_pool_type = None
        self._support_transaction_split = None
        self.discriminator = None

        if pool_id is not None:
            self.pool_id = pool_id
        if status is not None:
            self.status = status
        if address is not None:
            self.address = address
        if port is not None:
            self.port = port
        if delay_threshold_in_seconds is not None:
            self.delay_threshold_in_seconds = delay_threshold_in_seconds
        if cpu is not None:
            self.cpu = cpu
        if mem is not None:
            self.mem = mem
        if node_num is not None:
            self.node_num = node_num
        if nodes is not None:
            self.nodes = nodes
        if mode is not None:
            self.mode = mode
        if flavor_info is not None:
            self.flavor_info = flavor_info
        if transaction_split is not None:
            self.transaction_split = transaction_split
        if connection_pool_type is not None:
            self.connection_pool_type = connection_pool_type
        if pay_mode is not None:
            self.pay_mode = pay_mode
        if name is not None:
            self.name = name
        if proxy_mode is not None:
            self.proxy_mode = proxy_mode
        if dns_name is not None:
            self.dns_name = dns_name
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if seconds_level_monitor_fun_status is not None:
            self.seconds_level_monitor_fun_status = seconds_level_monitor_fun_status
        if alt_flag is not None:
            self.alt_flag = alt_flag
        if force_read_only is not None:
            self.force_read_only = force_read_only
        if route_mode is not None:
            self.route_mode = route_mode
        if ssl_option is not None:
            self.ssl_option = ssl_option
        if support_balance_route_mode is not None:
            self.support_balance_route_mode = support_balance_route_mode
        if support_proxy_ssl is not None:
            self.support_proxy_ssl = support_proxy_ssl
        if support_switch_connection_pool_type is not None:
            self.support_switch_connection_pool_type = support_switch_connection_pool_type
        if support_transaction_split is not None:
            self.support_transaction_split = support_transaction_split

    @property
    def pool_id(self):
        r"""Gets the pool_id of this ProxyInfo.

        数据库代理实例ID。

        :return: The pool_id of this ProxyInfo.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this ProxyInfo.

        数据库代理实例ID。

        :param pool_id: The pool_id of this ProxyInfo.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def status(self):
        r"""Gets the status of this ProxyInfo.

        数据库代理状态。  取值: NORMAL：表示数据库代理正常。 ENABLING：表示数据库代理正在开启。 DISABLING：表示数据库代理正在关闭。 CHANGING_NODE_NUM：表示数据库代理正在调整节点数量。 SCALING: 表示数据库代理正在规格变更。 UPGRADING: 表示数据库代理正在升级内核版本。 IPMODIFYING: 表示数据库代理正在修改读写分离地址。 RESTARTING: 表示数据库代理正在重启进程。 TRANSACTION_SPLITTING: 表示数据库代理正在变更事务拆分功能状态。 CONNECTION_POOL_SWITCH_OPERATING: 表示数据库代理正在变更会话连接池类型。 PORT_MODIFYING: 表示数据库代理正在修改端口。 PROXY_SSL_SWITCHING: 表示数据库代理正在变更SSL状态。 ALT_SWITCH_OPERATING: 表示数据库代理正在变更ALT状态。 CHANGING_RESOURCES: 表示数据库代理正在进行资源变更。 NORMAL: 表示数据库代理正常。 ABNORMAL: 表示数据库代理异常。 FAILED: 表示数据库代理创建失败。 FROZEN: 表示数据库代理已冻结。

        :return: The status of this ProxyInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ProxyInfo.

        数据库代理状态。  取值: NORMAL：表示数据库代理正常。 ENABLING：表示数据库代理正在开启。 DISABLING：表示数据库代理正在关闭。 CHANGING_NODE_NUM：表示数据库代理正在调整节点数量。 SCALING: 表示数据库代理正在规格变更。 UPGRADING: 表示数据库代理正在升级内核版本。 IPMODIFYING: 表示数据库代理正在修改读写分离地址。 RESTARTING: 表示数据库代理正在重启进程。 TRANSACTION_SPLITTING: 表示数据库代理正在变更事务拆分功能状态。 CONNECTION_POOL_SWITCH_OPERATING: 表示数据库代理正在变更会话连接池类型。 PORT_MODIFYING: 表示数据库代理正在修改端口。 PROXY_SSL_SWITCHING: 表示数据库代理正在变更SSL状态。 ALT_SWITCH_OPERATING: 表示数据库代理正在变更ALT状态。 CHANGING_RESOURCES: 表示数据库代理正在进行资源变更。 NORMAL: 表示数据库代理正常。 ABNORMAL: 表示数据库代理异常。 FAILED: 表示数据库代理创建失败。 FROZEN: 表示数据库代理已冻结。

        :param status: The status of this ProxyInfo.
        :type status: str
        """
        self._status = status

    @property
    def address(self):
        r"""Gets the address of this ProxyInfo.

        读写分离地址。

        :return: The address of this ProxyInfo.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this ProxyInfo.

        读写分离地址。

        :param address: The address of this ProxyInfo.
        :type address: str
        """
        self._address = address

    @property
    def port(self):
        r"""Gets the port of this ProxyInfo.

        端口号。

        :return: The port of this ProxyInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ProxyInfo.

        端口号。

        :param port: The port of this ProxyInfo.
        :type port: int
        """
        self._port = port

    @property
    def delay_threshold_in_seconds(self):
        r"""Gets the delay_threshold_in_seconds of this ProxyInfo.

        延时阈值，单位：秒。

        :return: The delay_threshold_in_seconds of this ProxyInfo.
        :rtype: int
        """
        return self._delay_threshold_in_seconds

    @delay_threshold_in_seconds.setter
    def delay_threshold_in_seconds(self, delay_threshold_in_seconds):
        r"""Sets the delay_threshold_in_seconds of this ProxyInfo.

        延时阈值，单位：秒。

        :param delay_threshold_in_seconds: The delay_threshold_in_seconds of this ProxyInfo.
        :type delay_threshold_in_seconds: int
        """
        self._delay_threshold_in_seconds = delay_threshold_in_seconds

    @property
    def cpu(self):
        r"""Gets the cpu of this ProxyInfo.

        数据库代理规格的CPU大小。

        :return: The cpu of this ProxyInfo.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ProxyInfo.

        数据库代理规格的CPU大小。

        :param cpu: The cpu of this ProxyInfo.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def mem(self):
        r"""Gets the mem of this ProxyInfo.

        数据库代理规格的内存大小。

        :return: The mem of this ProxyInfo.
        :rtype: str
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        r"""Sets the mem of this ProxyInfo.

        数据库代理规格的内存大小。

        :param mem: The mem of this ProxyInfo.
        :type mem: str
        """
        self._mem = mem

    @property
    def node_num(self):
        r"""Gets the node_num of this ProxyInfo.

        数据库代理节点个数。

        :return: The node_num of this ProxyInfo.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this ProxyInfo.

        数据库代理节点个数。

        :param node_num: The node_num of this ProxyInfo.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def nodes(self):
        r"""Gets the nodes of this ProxyInfo.

        数据库代理节点信息列表。

        :return: The nodes of this ProxyInfo.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ProxyInfoNodes`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this ProxyInfo.

        数据库代理节点信息列表。

        :param nodes: The nodes of this ProxyInfo.
        :type nodes: list[:class:`huaweicloudsdkrds.v3.ProxyInfoNodes`]
        """
        self._nodes = nodes

    @property
    def mode(self):
        r"""Gets the mode of this ProxyInfo.

        数据库代理集群模式。 取值：     Cluster：集群模式     Ha：主备模式

        :return: The mode of this ProxyInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ProxyInfo.

        数据库代理集群模式。 取值：     Cluster：集群模式     Ha：主备模式

        :param mode: The mode of this ProxyInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def flavor_info(self):
        r"""Gets the flavor_info of this ProxyInfo.

        :return: The flavor_info of this ProxyInfo.
        :rtype: :class:`huaweicloudsdkrds.v3.ProxyInfoFlavorInfo`
        """
        return self._flavor_info

    @flavor_info.setter
    def flavor_info(self, flavor_info):
        r"""Sets the flavor_info of this ProxyInfo.

        :param flavor_info: The flavor_info of this ProxyInfo.
        :type flavor_info: :class:`huaweicloudsdkrds.v3.ProxyInfoFlavorInfo`
        """
        self._flavor_info = flavor_info

    @property
    def transaction_split(self):
        r"""Gets the transaction_split of this ProxyInfo.

        数据库代理事务拆分开关状态。  true：开启。  false：关闭。

        :return: The transaction_split of this ProxyInfo.
        :rtype: str
        """
        return self._transaction_split

    @transaction_split.setter
    def transaction_split(self, transaction_split):
        r"""Sets the transaction_split of this ProxyInfo.

        数据库代理事务拆分开关状态。  true：开启。  false：关闭。

        :param transaction_split: The transaction_split of this ProxyInfo.
        :type transaction_split: str
        """
        self._transaction_split = transaction_split

    @property
    def connection_pool_type(self):
        r"""Gets the connection_pool_type of this ProxyInfo.

        连接池类型。  取值范围:  CLOSED: 关闭连接池。  SESSION: 开启会话级连接池。

        :return: The connection_pool_type of this ProxyInfo.
        :rtype: str
        """
        return self._connection_pool_type

    @connection_pool_type.setter
    def connection_pool_type(self, connection_pool_type):
        r"""Sets the connection_pool_type of this ProxyInfo.

        连接池类型。  取值范围:  CLOSED: 关闭连接池。  SESSION: 开启会话级连接池。

        :param connection_pool_type: The connection_pool_type of this ProxyInfo.
        :type connection_pool_type: str
        """
        self._connection_pool_type = connection_pool_type

    @property
    def pay_mode(self):
        r"""Gets the pay_mode of this ProxyInfo.

        数据库代理计费模式。  取值范围： 0:按需计费 1:包周期计费

        :return: The pay_mode of this ProxyInfo.
        :rtype: str
        """
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, pay_mode):
        r"""Sets the pay_mode of this ProxyInfo.

        数据库代理计费模式。  取值范围： 0:按需计费 1:包周期计费

        :param pay_mode: The pay_mode of this ProxyInfo.
        :type pay_mode: str
        """
        self._pay_mode = pay_mode

    @property
    def name(self):
        r"""Gets the name of this ProxyInfo.

        数据库代理名称。

        :return: The name of this ProxyInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ProxyInfo.

        数据库代理名称。

        :param name: The name of this ProxyInfo.
        :type name: str
        """
        self._name = name

    @property
    def proxy_mode(self):
        r"""Gets the proxy_mode of this ProxyInfo.

        数据库代理读写模式。 取值范围：     readwrite 读写模式     readonly 只读模式

        :return: The proxy_mode of this ProxyInfo.
        :rtype: str
        """
        return self._proxy_mode

    @proxy_mode.setter
    def proxy_mode(self, proxy_mode):
        r"""Sets the proxy_mode of this ProxyInfo.

        数据库代理读写模式。 取值范围：     readwrite 读写模式     readonly 只读模式

        :param proxy_mode: The proxy_mode of this ProxyInfo.
        :type proxy_mode: str
        """
        self._proxy_mode = proxy_mode

    @property
    def dns_name(self):
        r"""Gets the dns_name of this ProxyInfo.

        数据库代理读写分离地址内网域名。 该字段为空表示未申请读写内网域名。

        :return: The dns_name of this ProxyInfo.
        :rtype: str
        """
        return self._dns_name

    @dns_name.setter
    def dns_name(self, dns_name):
        r"""Sets the dns_name of this ProxyInfo.

        数据库代理读写分离地址内网域名。 该字段为空表示未申请读写内网域名。

        :param dns_name: The dns_name of this ProxyInfo.
        :type dns_name: str
        """
        self._dns_name = dns_name

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ProxyInfo.

        数据库代理实例所属子网ID。

        :return: The subnet_id of this ProxyInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ProxyInfo.

        数据库代理实例所属子网ID。

        :param subnet_id: The subnet_id of this ProxyInfo.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def seconds_level_monitor_fun_status(self):
        r"""Gets the seconds_level_monitor_fun_status of this ProxyInfo.

        数据库代理秒级监控状态。

        :return: The seconds_level_monitor_fun_status of this ProxyInfo.
        :rtype: str
        """
        return self._seconds_level_monitor_fun_status

    @seconds_level_monitor_fun_status.setter
    def seconds_level_monitor_fun_status(self, seconds_level_monitor_fun_status):
        r"""Sets the seconds_level_monitor_fun_status of this ProxyInfo.

        数据库代理秒级监控状态。

        :param seconds_level_monitor_fun_status: The seconds_level_monitor_fun_status of this ProxyInfo.
        :type seconds_level_monitor_fun_status: str
        """
        self._seconds_level_monitor_fun_status = seconds_level_monitor_fun_status

    @property
    def alt_flag(self):
        r"""Gets the alt_flag of this ProxyInfo.

        ALT开关状态。

        :return: The alt_flag of this ProxyInfo.
        :rtype: bool
        """
        return self._alt_flag

    @alt_flag.setter
    def alt_flag(self, alt_flag):
        r"""Sets the alt_flag of this ProxyInfo.

        ALT开关状态。

        :param alt_flag: The alt_flag of this ProxyInfo.
        :type alt_flag: bool
        """
        self._alt_flag = alt_flag

    @property
    def force_read_only(self):
        r"""Gets the force_read_only of this ProxyInfo.

        是否强制读路由到只读。

        :return: The force_read_only of this ProxyInfo.
        :rtype: bool
        """
        return self._force_read_only

    @force_read_only.setter
    def force_read_only(self, force_read_only):
        r"""Sets the force_read_only of this ProxyInfo.

        是否强制读路由到只读。

        :param force_read_only: The force_read_only of this ProxyInfo.
        :type force_read_only: bool
        """
        self._force_read_only = force_read_only

    @property
    def route_mode(self):
        r"""Gets the route_mode of this ProxyInfo.

        数据库代理路由模式。 取值范围:     0：表示权重负载模式。     1：表示负载均衡模式（数据库主实例不接受读请求）。     2：表示负载均衡模式（数据库主实例接受读请求）。

        :return: The route_mode of this ProxyInfo.
        :rtype: int
        """
        return self._route_mode

    @route_mode.setter
    def route_mode(self, route_mode):
        r"""Sets the route_mode of this ProxyInfo.

        数据库代理路由模式。 取值范围:     0：表示权重负载模式。     1：表示负载均衡模式（数据库主实例不接受读请求）。     2：表示负载均衡模式（数据库主实例接受读请求）。

        :param route_mode: The route_mode of this ProxyInfo.
        :type route_mode: int
        """
        self._route_mode = route_mode

    @property
    def ssl_option(self):
        r"""Gets the ssl_option of this ProxyInfo.

        ssl开关状态。

        :return: The ssl_option of this ProxyInfo.
        :rtype: bool
        """
        return self._ssl_option

    @ssl_option.setter
    def ssl_option(self, ssl_option):
        r"""Sets the ssl_option of this ProxyInfo.

        ssl开关状态。

        :param ssl_option: The ssl_option of this ProxyInfo.
        :type ssl_option: bool
        """
        self._ssl_option = ssl_option

    @property
    def support_balance_route_mode(self):
        r"""Gets the support_balance_route_mode of this ProxyInfo.

        数据库代理是否支持开启负载均衡路由模式。

        :return: The support_balance_route_mode of this ProxyInfo.
        :rtype: bool
        """
        return self._support_balance_route_mode

    @support_balance_route_mode.setter
    def support_balance_route_mode(self, support_balance_route_mode):
        r"""Sets the support_balance_route_mode of this ProxyInfo.

        数据库代理是否支持开启负载均衡路由模式。

        :param support_balance_route_mode: The support_balance_route_mode of this ProxyInfo.
        :type support_balance_route_mode: bool
        """
        self._support_balance_route_mode = support_balance_route_mode

    @property
    def support_proxy_ssl(self):
        r"""Gets the support_proxy_ssl of this ProxyInfo.

        数据库代理是否支持开启ssl功能。

        :return: The support_proxy_ssl of this ProxyInfo.
        :rtype: bool
        """
        return self._support_proxy_ssl

    @support_proxy_ssl.setter
    def support_proxy_ssl(self, support_proxy_ssl):
        r"""Sets the support_proxy_ssl of this ProxyInfo.

        数据库代理是否支持开启ssl功能。

        :param support_proxy_ssl: The support_proxy_ssl of this ProxyInfo.
        :type support_proxy_ssl: bool
        """
        self._support_proxy_ssl = support_proxy_ssl

    @property
    def support_switch_connection_pool_type(self):
        r"""Gets the support_switch_connection_pool_type of this ProxyInfo.

        数据库代理是否支持切换会话连接池类型。

        :return: The support_switch_connection_pool_type of this ProxyInfo.
        :rtype: bool
        """
        return self._support_switch_connection_pool_type

    @support_switch_connection_pool_type.setter
    def support_switch_connection_pool_type(self, support_switch_connection_pool_type):
        r"""Sets the support_switch_connection_pool_type of this ProxyInfo.

        数据库代理是否支持切换会话连接池类型。

        :param support_switch_connection_pool_type: The support_switch_connection_pool_type of this ProxyInfo.
        :type support_switch_connection_pool_type: bool
        """
        self._support_switch_connection_pool_type = support_switch_connection_pool_type

    @property
    def support_transaction_split(self):
        r"""Gets the support_transaction_split of this ProxyInfo.

        数据库代理是否支持开启事务拆分。

        :return: The support_transaction_split of this ProxyInfo.
        :rtype: bool
        """
        return self._support_transaction_split

    @support_transaction_split.setter
    def support_transaction_split(self, support_transaction_split):
        r"""Sets the support_transaction_split of this ProxyInfo.

        数据库代理是否支持开启事务拆分。

        :param support_transaction_split: The support_transaction_split of this ProxyInfo.
        :type support_transaction_split: bool
        """
        self._support_transaction_split = support_transaction_split

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
        if not isinstance(other, ProxyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
