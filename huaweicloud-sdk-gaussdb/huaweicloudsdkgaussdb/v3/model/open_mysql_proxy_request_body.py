# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenMysqlProxyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_ref': 'str',
        'node_num': 'int',
        'proxy_name': 'str',
        'proxy_mode': 'str',
        'route_mode': 'int',
        'nodes_read_weight': 'list[NodesWeight]',
        'subnet_id': 'str',
        'new_node_auto_add_status': 'str',
        'new_node_weight': 'int'
    }

    attribute_map = {
        'flavor_ref': 'flavor_ref',
        'node_num': 'node_num',
        'proxy_name': 'proxy_name',
        'proxy_mode': 'proxy_mode',
        'route_mode': 'route_mode',
        'nodes_read_weight': 'nodes_read_weight',
        'subnet_id': 'subnet_id',
        'new_node_auto_add_status': 'new_node_auto_add_status',
        'new_node_weight': 'new_node_weight'
    }

    def __init__(self, flavor_ref=None, node_num=None, proxy_name=None, proxy_mode=None, route_mode=None, nodes_read_weight=None, subnet_id=None, new_node_auto_add_status=None, new_node_weight=None):
        r"""OpenMysqlProxyRequestBody

        The model defined in huaweicloud sdk

        :param flavor_ref: 代理规格码。
        :type flavor_ref: str
        :param node_num: 代理实例节点数，取值整数2-32。
        :type node_num: int
        :param proxy_name: 代理实例名称。用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：最小为4个字符，最大为64个字符且不超过64个字节（注意：一个中文字符占用3个字节），必须以字母或中文开头，区分大小写，可以包含字母、数字、中划线、下划线或中文，不能包含其他特殊字符。
        :type proxy_name: str
        :param proxy_mode: 代理实例类型。默认类型为readwrite。
        :type proxy_mode: str
        :param route_mode: 数据库代理路由模式，默认为权重负载模式。  取值范围: - 0，表示权重负载模式; - 1，表示负载均衡模式（数据库主节点不接受读请求）； - 2，表示负载均衡模式（数据库主节点接受读请求）。
        :type route_mode: int
        :param nodes_read_weight: 数据库节点的读权重设置。  在proxy_mode为readonly时，只能为只读节点选择权重。
        :type nodes_read_weight: list[:class:`huaweicloudsdkgaussdb.v3.NodesWeight`]
        :param subnet_id: 数据库VPC下的子网ID。
        :type subnet_id: str
        :param new_node_auto_add_status: 是否开启新增节点自动加入该Proxy。如果需要设置是否开启新增节点自动加入该Proxy，请联系客服人员添加白名单，加入白名单后，方可输入该字段。  取值范围： - ON：开启。 - OFF：关闭。
        :type new_node_auto_add_status: str
        :param new_node_weight: 新增节点的读权重：    - 如果路由模式为0，新增节点自动加入为ON，取值为0~1000。 - 如果路由模式不为0或新增节点自动加入为OFF，则可不输入读权重。
        :type new_node_weight: int
        """
        
        

        self._flavor_ref = None
        self._node_num = None
        self._proxy_name = None
        self._proxy_mode = None
        self._route_mode = None
        self._nodes_read_weight = None
        self._subnet_id = None
        self._new_node_auto_add_status = None
        self._new_node_weight = None
        self.discriminator = None

        self.flavor_ref = flavor_ref
        self.node_num = node_num
        if proxy_name is not None:
            self.proxy_name = proxy_name
        if proxy_mode is not None:
            self.proxy_mode = proxy_mode
        if route_mode is not None:
            self.route_mode = route_mode
        if nodes_read_weight is not None:
            self.nodes_read_weight = nodes_read_weight
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if new_node_auto_add_status is not None:
            self.new_node_auto_add_status = new_node_auto_add_status
        if new_node_weight is not None:
            self.new_node_weight = new_node_weight

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this OpenMysqlProxyRequestBody.

        代理规格码。

        :return: The flavor_ref of this OpenMysqlProxyRequestBody.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this OpenMysqlProxyRequestBody.

        代理规格码。

        :param flavor_ref: The flavor_ref of this OpenMysqlProxyRequestBody.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def node_num(self):
        r"""Gets the node_num of this OpenMysqlProxyRequestBody.

        代理实例节点数，取值整数2-32。

        :return: The node_num of this OpenMysqlProxyRequestBody.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this OpenMysqlProxyRequestBody.

        代理实例节点数，取值整数2-32。

        :param node_num: The node_num of this OpenMysqlProxyRequestBody.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def proxy_name(self):
        r"""Gets the proxy_name of this OpenMysqlProxyRequestBody.

        代理实例名称。用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：最小为4个字符，最大为64个字符且不超过64个字节（注意：一个中文字符占用3个字节），必须以字母或中文开头，区分大小写，可以包含字母、数字、中划线、下划线或中文，不能包含其他特殊字符。

        :return: The proxy_name of this OpenMysqlProxyRequestBody.
        :rtype: str
        """
        return self._proxy_name

    @proxy_name.setter
    def proxy_name(self, proxy_name):
        r"""Sets the proxy_name of this OpenMysqlProxyRequestBody.

        代理实例名称。用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：最小为4个字符，最大为64个字符且不超过64个字节（注意：一个中文字符占用3个字节），必须以字母或中文开头，区分大小写，可以包含字母、数字、中划线、下划线或中文，不能包含其他特殊字符。

        :param proxy_name: The proxy_name of this OpenMysqlProxyRequestBody.
        :type proxy_name: str
        """
        self._proxy_name = proxy_name

    @property
    def proxy_mode(self):
        r"""Gets the proxy_mode of this OpenMysqlProxyRequestBody.

        代理实例类型。默认类型为readwrite。

        :return: The proxy_mode of this OpenMysqlProxyRequestBody.
        :rtype: str
        """
        return self._proxy_mode

    @proxy_mode.setter
    def proxy_mode(self, proxy_mode):
        r"""Sets the proxy_mode of this OpenMysqlProxyRequestBody.

        代理实例类型。默认类型为readwrite。

        :param proxy_mode: The proxy_mode of this OpenMysqlProxyRequestBody.
        :type proxy_mode: str
        """
        self._proxy_mode = proxy_mode

    @property
    def route_mode(self):
        r"""Gets the route_mode of this OpenMysqlProxyRequestBody.

        数据库代理路由模式，默认为权重负载模式。  取值范围: - 0，表示权重负载模式; - 1，表示负载均衡模式（数据库主节点不接受读请求）； - 2，表示负载均衡模式（数据库主节点接受读请求）。

        :return: The route_mode of this OpenMysqlProxyRequestBody.
        :rtype: int
        """
        return self._route_mode

    @route_mode.setter
    def route_mode(self, route_mode):
        r"""Sets the route_mode of this OpenMysqlProxyRequestBody.

        数据库代理路由模式，默认为权重负载模式。  取值范围: - 0，表示权重负载模式; - 1，表示负载均衡模式（数据库主节点不接受读请求）； - 2，表示负载均衡模式（数据库主节点接受读请求）。

        :param route_mode: The route_mode of this OpenMysqlProxyRequestBody.
        :type route_mode: int
        """
        self._route_mode = route_mode

    @property
    def nodes_read_weight(self):
        r"""Gets the nodes_read_weight of this OpenMysqlProxyRequestBody.

        数据库节点的读权重设置。  在proxy_mode为readonly时，只能为只读节点选择权重。

        :return: The nodes_read_weight of this OpenMysqlProxyRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.NodesWeight`]
        """
        return self._nodes_read_weight

    @nodes_read_weight.setter
    def nodes_read_weight(self, nodes_read_weight):
        r"""Sets the nodes_read_weight of this OpenMysqlProxyRequestBody.

        数据库节点的读权重设置。  在proxy_mode为readonly时，只能为只读节点选择权重。

        :param nodes_read_weight: The nodes_read_weight of this OpenMysqlProxyRequestBody.
        :type nodes_read_weight: list[:class:`huaweicloudsdkgaussdb.v3.NodesWeight`]
        """
        self._nodes_read_weight = nodes_read_weight

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this OpenMysqlProxyRequestBody.

        数据库VPC下的子网ID。

        :return: The subnet_id of this OpenMysqlProxyRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this OpenMysqlProxyRequestBody.

        数据库VPC下的子网ID。

        :param subnet_id: The subnet_id of this OpenMysqlProxyRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def new_node_auto_add_status(self):
        r"""Gets the new_node_auto_add_status of this OpenMysqlProxyRequestBody.

        是否开启新增节点自动加入该Proxy。如果需要设置是否开启新增节点自动加入该Proxy，请联系客服人员添加白名单，加入白名单后，方可输入该字段。  取值范围： - ON：开启。 - OFF：关闭。

        :return: The new_node_auto_add_status of this OpenMysqlProxyRequestBody.
        :rtype: str
        """
        return self._new_node_auto_add_status

    @new_node_auto_add_status.setter
    def new_node_auto_add_status(self, new_node_auto_add_status):
        r"""Sets the new_node_auto_add_status of this OpenMysqlProxyRequestBody.

        是否开启新增节点自动加入该Proxy。如果需要设置是否开启新增节点自动加入该Proxy，请联系客服人员添加白名单，加入白名单后，方可输入该字段。  取值范围： - ON：开启。 - OFF：关闭。

        :param new_node_auto_add_status: The new_node_auto_add_status of this OpenMysqlProxyRequestBody.
        :type new_node_auto_add_status: str
        """
        self._new_node_auto_add_status = new_node_auto_add_status

    @property
    def new_node_weight(self):
        r"""Gets the new_node_weight of this OpenMysqlProxyRequestBody.

        新增节点的读权重：    - 如果路由模式为0，新增节点自动加入为ON，取值为0~1000。 - 如果路由模式不为0或新增节点自动加入为OFF，则可不输入读权重。

        :return: The new_node_weight of this OpenMysqlProxyRequestBody.
        :rtype: int
        """
        return self._new_node_weight

    @new_node_weight.setter
    def new_node_weight(self, new_node_weight):
        r"""Sets the new_node_weight of this OpenMysqlProxyRequestBody.

        新增节点的读权重：    - 如果路由模式为0，新增节点自动加入为ON，取值为0~1000。 - 如果路由模式不为0或新增节点自动加入为OFF，则可不输入读权重。

        :param new_node_weight: The new_node_weight of this OpenMysqlProxyRequestBody.
        :type new_node_weight: int
        """
        self._new_node_weight = new_node_weight

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
        if not isinstance(other, OpenMysqlProxyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
