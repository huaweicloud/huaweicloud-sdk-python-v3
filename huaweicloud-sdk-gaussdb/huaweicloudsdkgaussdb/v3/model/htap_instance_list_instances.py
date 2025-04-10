# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HtapInstanceListInstances:

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
        'engine_name': 'str',
        'engine_version': 'str',
        'project_id': 'str',
        'instance_state': 'HtapInstanceListInstanceState',
        'create_at': 'int',
        'is_frozen': 'bool',
        'ha_mode': 'str',
        'pay_model': 'str',
        'order_id': 'str',
        'alter_order_id': 'str',
        'data_vip': 'str',
        'readable_node_infos': 'list[ReadableNodeInfos]',
        'proxy_ips': 'list[str]',
        'data_vip_v6': 'str',
        'port': 'int',
        'available_zones': 'list[HtapInstanceListAvailableZones]',
        'current_actions': 'list[QueryAction]',
        'volume_type': 'str',
        'server_type': 'str',
        'enterprise_project_id': 'str',
        'dedicated_resource_id': 'str',
        'network': 'HtapInstanceListNetwork',
        'ch_master_node_id': 'str',
        'node_num': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'project_id': 'project_id',
        'instance_state': 'instance_state',
        'create_at': 'create_at',
        'is_frozen': 'is_frozen',
        'ha_mode': 'ha_mode',
        'pay_model': 'pay_model',
        'order_id': 'order_id',
        'alter_order_id': 'alter_order_id',
        'data_vip': 'data_vip',
        'readable_node_infos': 'readable_node_infos',
        'proxy_ips': 'proxy_ips',
        'data_vip_v6': 'data_vip_v6',
        'port': 'port',
        'available_zones': 'available_zones',
        'current_actions': 'current_actions',
        'volume_type': 'volume_type',
        'server_type': 'server_type',
        'enterprise_project_id': 'enterprise_project_id',
        'dedicated_resource_id': 'dedicated_resource_id',
        'network': 'network',
        'ch_master_node_id': 'ch_master_node_id',
        'node_num': 'node_num'
    }

    def __init__(self, id=None, name=None, engine_name=None, engine_version=None, project_id=None, instance_state=None, create_at=None, is_frozen=None, ha_mode=None, pay_model=None, order_id=None, alter_order_id=None, data_vip=None, readable_node_infos=None, proxy_ips=None, data_vip_v6=None, port=None, available_zones=None, current_actions=None, volume_type=None, server_type=None, enterprise_project_id=None, dedicated_resource_id=None, network=None, ch_master_node_id=None, node_num=None):
        r"""HtapInstanceListInstances

        The model defined in huaweicloud sdk

        :param id: HTAP实例ID，严格匹配UUID规则。
        :type id: str
        :param name: HTAP实例名。
        :type name: str
        :param engine_name: HTAP数据库引擎名。
        :type engine_name: str
        :param engine_version: HTAP数据库引擎版本。
        :type engine_version: str
        :param project_id: 租户在某一region下的project ID
        :type project_id: str
        :param instance_state: 
        :type instance_state: :class:`huaweicloudsdkgaussdb.v3.HtapInstanceListInstanceState`
        :param create_at: HTAP实例创建时间。
        :type create_at: int
        :param is_frozen: HTAP实例是否冻结。
        :type is_frozen: bool
        :param ha_mode: HTAP实例部署模式。
        :type ha_mode: str
        :param pay_model: 计费模式。当前仅支持按需计费。 0：按需计费 1：包周期
        :type pay_model: str
        :param order_id: 包周期计费订单ID。
        :type order_id: str
        :param alter_order_id: 包周期计费备用订单ID。
        :type alter_order_id: str
        :param data_vip: 读写内网地址。
        :type data_vip: str
        :param readable_node_infos: 可读节点信息
        :type readable_node_infos: list[:class:`huaweicloudsdkgaussdb.v3.ReadableNodeInfos`]
        :param proxy_ips: 代理IP。
        :type proxy_ips: list[str]
        :param data_vip_v6: 读写内网地址IPV6。
        :type data_vip_v6: str
        :param port: 数据库访问端口。
        :type port: int
        :param available_zones: 可用区信息。
        :type available_zones: list[:class:`huaweicloudsdkgaussdb.v3.HtapInstanceListAvailableZones`]
        :param current_actions: 实例动作。
        :type current_actions: list[:class:`huaweicloudsdkgaussdb.v3.QueryAction`]
        :param volume_type: 存储类型。
        :type volume_type: str
        :param server_type: 服务器类型。
        :type server_type: str
        :param enterprise_project_id: 企业项目ID。如果帐户开通企业项目服务则该参数必选，未开启该参数不可选。
        :type enterprise_project_id: str
        :param dedicated_resource_id: 专属资源池ID，只有开通专属资源池后才支持此参数。
        :type dedicated_resource_id: str
        :param network: 
        :type network: :class:`huaweicloudsdkgaussdb.v3.HtapInstanceListNetwork`
        :param ch_master_node_id: ClickHouse主节点ID。
        :type ch_master_node_id: str
        :param node_num: 节点个数。
        :type node_num: int
        """
        
        

        self._id = None
        self._name = None
        self._engine_name = None
        self._engine_version = None
        self._project_id = None
        self._instance_state = None
        self._create_at = None
        self._is_frozen = None
        self._ha_mode = None
        self._pay_model = None
        self._order_id = None
        self._alter_order_id = None
        self._data_vip = None
        self._readable_node_infos = None
        self._proxy_ips = None
        self._data_vip_v6 = None
        self._port = None
        self._available_zones = None
        self._current_actions = None
        self._volume_type = None
        self._server_type = None
        self._enterprise_project_id = None
        self._dedicated_resource_id = None
        self._network = None
        self._ch_master_node_id = None
        self._node_num = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if engine_name is not None:
            self.engine_name = engine_name
        if engine_version is not None:
            self.engine_version = engine_version
        if project_id is not None:
            self.project_id = project_id
        if instance_state is not None:
            self.instance_state = instance_state
        if create_at is not None:
            self.create_at = create_at
        if is_frozen is not None:
            self.is_frozen = is_frozen
        if ha_mode is not None:
            self.ha_mode = ha_mode
        if pay_model is not None:
            self.pay_model = pay_model
        if order_id is not None:
            self.order_id = order_id
        if alter_order_id is not None:
            self.alter_order_id = alter_order_id
        if data_vip is not None:
            self.data_vip = data_vip
        if readable_node_infos is not None:
            self.readable_node_infos = readable_node_infos
        if proxy_ips is not None:
            self.proxy_ips = proxy_ips
        if data_vip_v6 is not None:
            self.data_vip_v6 = data_vip_v6
        if port is not None:
            self.port = port
        if available_zones is not None:
            self.available_zones = available_zones
        if current_actions is not None:
            self.current_actions = current_actions
        if volume_type is not None:
            self.volume_type = volume_type
        if server_type is not None:
            self.server_type = server_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if dedicated_resource_id is not None:
            self.dedicated_resource_id = dedicated_resource_id
        if network is not None:
            self.network = network
        if ch_master_node_id is not None:
            self.ch_master_node_id = ch_master_node_id
        if node_num is not None:
            self.node_num = node_num

    @property
    def id(self):
        r"""Gets the id of this HtapInstanceListInstances.

        HTAP实例ID，严格匹配UUID规则。

        :return: The id of this HtapInstanceListInstances.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HtapInstanceListInstances.

        HTAP实例ID，严格匹配UUID规则。

        :param id: The id of this HtapInstanceListInstances.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this HtapInstanceListInstances.

        HTAP实例名。

        :return: The name of this HtapInstanceListInstances.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HtapInstanceListInstances.

        HTAP实例名。

        :param name: The name of this HtapInstanceListInstances.
        :type name: str
        """
        self._name = name

    @property
    def engine_name(self):
        r"""Gets the engine_name of this HtapInstanceListInstances.

        HTAP数据库引擎名。

        :return: The engine_name of this HtapInstanceListInstances.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this HtapInstanceListInstances.

        HTAP数据库引擎名。

        :param engine_name: The engine_name of this HtapInstanceListInstances.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        r"""Gets the engine_version of this HtapInstanceListInstances.

        HTAP数据库引擎版本。

        :return: The engine_version of this HtapInstanceListInstances.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this HtapInstanceListInstances.

        HTAP数据库引擎版本。

        :param engine_version: The engine_version of this HtapInstanceListInstances.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def project_id(self):
        r"""Gets the project_id of this HtapInstanceListInstances.

        租户在某一region下的project ID

        :return: The project_id of this HtapInstanceListInstances.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this HtapInstanceListInstances.

        租户在某一region下的project ID

        :param project_id: The project_id of this HtapInstanceListInstances.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def instance_state(self):
        r"""Gets the instance_state of this HtapInstanceListInstances.

        :return: The instance_state of this HtapInstanceListInstances.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.HtapInstanceListInstanceState`
        """
        return self._instance_state

    @instance_state.setter
    def instance_state(self, instance_state):
        r"""Sets the instance_state of this HtapInstanceListInstances.

        :param instance_state: The instance_state of this HtapInstanceListInstances.
        :type instance_state: :class:`huaweicloudsdkgaussdb.v3.HtapInstanceListInstanceState`
        """
        self._instance_state = instance_state

    @property
    def create_at(self):
        r"""Gets the create_at of this HtapInstanceListInstances.

        HTAP实例创建时间。

        :return: The create_at of this HtapInstanceListInstances.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this HtapInstanceListInstances.

        HTAP实例创建时间。

        :param create_at: The create_at of this HtapInstanceListInstances.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def is_frozen(self):
        r"""Gets the is_frozen of this HtapInstanceListInstances.

        HTAP实例是否冻结。

        :return: The is_frozen of this HtapInstanceListInstances.
        :rtype: bool
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        r"""Sets the is_frozen of this HtapInstanceListInstances.

        HTAP实例是否冻结。

        :param is_frozen: The is_frozen of this HtapInstanceListInstances.
        :type is_frozen: bool
        """
        self._is_frozen = is_frozen

    @property
    def ha_mode(self):
        r"""Gets the ha_mode of this HtapInstanceListInstances.

        HTAP实例部署模式。

        :return: The ha_mode of this HtapInstanceListInstances.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        r"""Sets the ha_mode of this HtapInstanceListInstances.

        HTAP实例部署模式。

        :param ha_mode: The ha_mode of this HtapInstanceListInstances.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def pay_model(self):
        r"""Gets the pay_model of this HtapInstanceListInstances.

        计费模式。当前仅支持按需计费。 0：按需计费 1：包周期

        :return: The pay_model of this HtapInstanceListInstances.
        :rtype: str
        """
        return self._pay_model

    @pay_model.setter
    def pay_model(self, pay_model):
        r"""Sets the pay_model of this HtapInstanceListInstances.

        计费模式。当前仅支持按需计费。 0：按需计费 1：包周期

        :param pay_model: The pay_model of this HtapInstanceListInstances.
        :type pay_model: str
        """
        self._pay_model = pay_model

    @property
    def order_id(self):
        r"""Gets the order_id of this HtapInstanceListInstances.

        包周期计费订单ID。

        :return: The order_id of this HtapInstanceListInstances.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this HtapInstanceListInstances.

        包周期计费订单ID。

        :param order_id: The order_id of this HtapInstanceListInstances.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def alter_order_id(self):
        r"""Gets the alter_order_id of this HtapInstanceListInstances.

        包周期计费备用订单ID。

        :return: The alter_order_id of this HtapInstanceListInstances.
        :rtype: str
        """
        return self._alter_order_id

    @alter_order_id.setter
    def alter_order_id(self, alter_order_id):
        r"""Sets the alter_order_id of this HtapInstanceListInstances.

        包周期计费备用订单ID。

        :param alter_order_id: The alter_order_id of this HtapInstanceListInstances.
        :type alter_order_id: str
        """
        self._alter_order_id = alter_order_id

    @property
    def data_vip(self):
        r"""Gets the data_vip of this HtapInstanceListInstances.

        读写内网地址。

        :return: The data_vip of this HtapInstanceListInstances.
        :rtype: str
        """
        return self._data_vip

    @data_vip.setter
    def data_vip(self, data_vip):
        r"""Sets the data_vip of this HtapInstanceListInstances.

        读写内网地址。

        :param data_vip: The data_vip of this HtapInstanceListInstances.
        :type data_vip: str
        """
        self._data_vip = data_vip

    @property
    def readable_node_infos(self):
        r"""Gets the readable_node_infos of this HtapInstanceListInstances.

        可读节点信息

        :return: The readable_node_infos of this HtapInstanceListInstances.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ReadableNodeInfos`]
        """
        return self._readable_node_infos

    @readable_node_infos.setter
    def readable_node_infos(self, readable_node_infos):
        r"""Sets the readable_node_infos of this HtapInstanceListInstances.

        可读节点信息

        :param readable_node_infos: The readable_node_infos of this HtapInstanceListInstances.
        :type readable_node_infos: list[:class:`huaweicloudsdkgaussdb.v3.ReadableNodeInfos`]
        """
        self._readable_node_infos = readable_node_infos

    @property
    def proxy_ips(self):
        r"""Gets the proxy_ips of this HtapInstanceListInstances.

        代理IP。

        :return: The proxy_ips of this HtapInstanceListInstances.
        :rtype: list[str]
        """
        return self._proxy_ips

    @proxy_ips.setter
    def proxy_ips(self, proxy_ips):
        r"""Sets the proxy_ips of this HtapInstanceListInstances.

        代理IP。

        :param proxy_ips: The proxy_ips of this HtapInstanceListInstances.
        :type proxy_ips: list[str]
        """
        self._proxy_ips = proxy_ips

    @property
    def data_vip_v6(self):
        r"""Gets the data_vip_v6 of this HtapInstanceListInstances.

        读写内网地址IPV6。

        :return: The data_vip_v6 of this HtapInstanceListInstances.
        :rtype: str
        """
        return self._data_vip_v6

    @data_vip_v6.setter
    def data_vip_v6(self, data_vip_v6):
        r"""Sets the data_vip_v6 of this HtapInstanceListInstances.

        读写内网地址IPV6。

        :param data_vip_v6: The data_vip_v6 of this HtapInstanceListInstances.
        :type data_vip_v6: str
        """
        self._data_vip_v6 = data_vip_v6

    @property
    def port(self):
        r"""Gets the port of this HtapInstanceListInstances.

        数据库访问端口。

        :return: The port of this HtapInstanceListInstances.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this HtapInstanceListInstances.

        数据库访问端口。

        :param port: The port of this HtapInstanceListInstances.
        :type port: int
        """
        self._port = port

    @property
    def available_zones(self):
        r"""Gets the available_zones of this HtapInstanceListInstances.

        可用区信息。

        :return: The available_zones of this HtapInstanceListInstances.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.HtapInstanceListAvailableZones`]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this HtapInstanceListInstances.

        可用区信息。

        :param available_zones: The available_zones of this HtapInstanceListInstances.
        :type available_zones: list[:class:`huaweicloudsdkgaussdb.v3.HtapInstanceListAvailableZones`]
        """
        self._available_zones = available_zones

    @property
    def current_actions(self):
        r"""Gets the current_actions of this HtapInstanceListInstances.

        实例动作。

        :return: The current_actions of this HtapInstanceListInstances.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.QueryAction`]
        """
        return self._current_actions

    @current_actions.setter
    def current_actions(self, current_actions):
        r"""Sets the current_actions of this HtapInstanceListInstances.

        实例动作。

        :param current_actions: The current_actions of this HtapInstanceListInstances.
        :type current_actions: list[:class:`huaweicloudsdkgaussdb.v3.QueryAction`]
        """
        self._current_actions = current_actions

    @property
    def volume_type(self):
        r"""Gets the volume_type of this HtapInstanceListInstances.

        存储类型。

        :return: The volume_type of this HtapInstanceListInstances.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this HtapInstanceListInstances.

        存储类型。

        :param volume_type: The volume_type of this HtapInstanceListInstances.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def server_type(self):
        r"""Gets the server_type of this HtapInstanceListInstances.

        服务器类型。

        :return: The server_type of this HtapInstanceListInstances.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this HtapInstanceListInstances.

        服务器类型。

        :param server_type: The server_type of this HtapInstanceListInstances.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this HtapInstanceListInstances.

        企业项目ID。如果帐户开通企业项目服务则该参数必选，未开启该参数不可选。

        :return: The enterprise_project_id of this HtapInstanceListInstances.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this HtapInstanceListInstances.

        企业项目ID。如果帐户开通企业项目服务则该参数必选，未开启该参数不可选。

        :param enterprise_project_id: The enterprise_project_id of this HtapInstanceListInstances.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def dedicated_resource_id(self):
        r"""Gets the dedicated_resource_id of this HtapInstanceListInstances.

        专属资源池ID，只有开通专属资源池后才支持此参数。

        :return: The dedicated_resource_id of this HtapInstanceListInstances.
        :rtype: str
        """
        return self._dedicated_resource_id

    @dedicated_resource_id.setter
    def dedicated_resource_id(self, dedicated_resource_id):
        r"""Sets the dedicated_resource_id of this HtapInstanceListInstances.

        专属资源池ID，只有开通专属资源池后才支持此参数。

        :param dedicated_resource_id: The dedicated_resource_id of this HtapInstanceListInstances.
        :type dedicated_resource_id: str
        """
        self._dedicated_resource_id = dedicated_resource_id

    @property
    def network(self):
        r"""Gets the network of this HtapInstanceListInstances.

        :return: The network of this HtapInstanceListInstances.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.HtapInstanceListNetwork`
        """
        return self._network

    @network.setter
    def network(self, network):
        r"""Sets the network of this HtapInstanceListInstances.

        :param network: The network of this HtapInstanceListInstances.
        :type network: :class:`huaweicloudsdkgaussdb.v3.HtapInstanceListNetwork`
        """
        self._network = network

    @property
    def ch_master_node_id(self):
        r"""Gets the ch_master_node_id of this HtapInstanceListInstances.

        ClickHouse主节点ID。

        :return: The ch_master_node_id of this HtapInstanceListInstances.
        :rtype: str
        """
        return self._ch_master_node_id

    @ch_master_node_id.setter
    def ch_master_node_id(self, ch_master_node_id):
        r"""Sets the ch_master_node_id of this HtapInstanceListInstances.

        ClickHouse主节点ID。

        :param ch_master_node_id: The ch_master_node_id of this HtapInstanceListInstances.
        :type ch_master_node_id: str
        """
        self._ch_master_node_id = ch_master_node_id

    @property
    def node_num(self):
        r"""Gets the node_num of this HtapInstanceListInstances.

        节点个数。

        :return: The node_num of this HtapInstanceListInstances.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this HtapInstanceListInstances.

        节点个数。

        :param node_num: The node_num of this HtapInstanceListInstances.
        :type node_num: int
        """
        self._node_num = node_num

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
        if not isinstance(other, HtapInstanceListInstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
