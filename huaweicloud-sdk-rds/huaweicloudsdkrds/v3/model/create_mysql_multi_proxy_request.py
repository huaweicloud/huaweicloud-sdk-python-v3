# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMysqlMultiProxyRequest:

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
        'nodes_read_weight': 'list[InstancesWeight]',
        'subnet_id': 'str'
    }

    attribute_map = {
        'flavor_ref': 'flavor_ref',
        'node_num': 'node_num',
        'proxy_name': 'proxy_name',
        'proxy_mode': 'proxy_mode',
        'route_mode': 'route_mode',
        'nodes_read_weight': 'nodes_read_weight',
        'subnet_id': 'subnet_id'
    }

    def __init__(self, flavor_ref=None, node_num=None, proxy_name=None, proxy_mode=None, route_mode=None, nodes_read_weight=None, subnet_id=None):
        r"""CreateMysqlMultiProxyRequest

        The model defined in huaweicloud sdk

        :param flavor_ref: 数据库代理规格码。      - 当局点支持主备模式数据库代理时，该字段不生效。     - 当局点支持集群模式数据库代理时，该字段请参考查询数据库代理规格信息接口返回体中，[规格信息]中的code字段。
        :type flavor_ref: str
        :param node_num: 数据库代理节点数量。      - 当局点支持主备模式数据库代理时，请设置该字段为固定值2。     - 当局点支持集群模式数据库代理时，该字段最小值为2，最大值请参考查询数据库代理信息列表接口返回体中，[数据库代理信息列表]中的max_proxy_node_num字段值。
        :type node_num: int
        :param proxy_name: 数据库代理名称。用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：最小长度为4个字符，最大不超过64个字节，以字母或中文字符开头，只能包含字母、数字、中划线、下划线、英文句号和中文。  当不选择该参数或局点仅支持主备模式数据库代理时，将随机生成名称。
        :type proxy_name: str
        :param proxy_mode: 数据库代理读写模式。 取值范围:     readwrite：读写模式。     readonly：只读模式。
        :type proxy_mode: str
        :param route_mode: 数据库代理路由模式。 取值范围:     0：表示权重负载模式。     1：表示负载均衡模式（数据库主节点不接受读请求）。     2：表示负载均衡模式（数据库主节点接受读请求）。      - 如需使用负载均衡模式，请联系客服申请
        :type route_mode: int
        :param nodes_read_weight: 数据库节点的读权重设置。      - 在proxy_mode（数据库代理读写模式）为readonly（只读模式）或者在route_mode（路由模式）&gt;0时，只能为只读节点选择权重。     - 在proxy_mode（数据库代理读写模式）为readonly（只读模式）时，需要至少为一个只读实例配置权重。     - 在route_mode（路由模式）&gt;0时，为主实例配置的权重将不生效。     - 该列表可以为空列表。
        :type nodes_read_weight: list[:class:`huaweicloudsdkrds.v3.InstancesWeight`]
        :param subnet_id: 数据库VPC下的子网ID。 取值范围为该实例所在VPC下的所有子网ID。      - 如需使用该参数，请联系客服申请。     - 获取子网ID请参考[创建VPC和子网](https://support.huaweicloud.com/api-cce/cce_02_0100.html)
        :type subnet_id: str
        """
        
        

        self._flavor_ref = None
        self._node_num = None
        self._proxy_name = None
        self._proxy_mode = None
        self._route_mode = None
        self._nodes_read_weight = None
        self._subnet_id = None
        self.discriminator = None

        self.flavor_ref = flavor_ref
        self.node_num = node_num
        if proxy_name is not None:
            self.proxy_name = proxy_name
        if proxy_mode is not None:
            self.proxy_mode = proxy_mode
        if route_mode is not None:
            self.route_mode = route_mode
        self.nodes_read_weight = nodes_read_weight
        if subnet_id is not None:
            self.subnet_id = subnet_id

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this CreateMysqlMultiProxyRequest.

        数据库代理规格码。      - 当局点支持主备模式数据库代理时，该字段不生效。     - 当局点支持集群模式数据库代理时，该字段请参考查询数据库代理规格信息接口返回体中，[规格信息]中的code字段。

        :return: The flavor_ref of this CreateMysqlMultiProxyRequest.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this CreateMysqlMultiProxyRequest.

        数据库代理规格码。      - 当局点支持主备模式数据库代理时，该字段不生效。     - 当局点支持集群模式数据库代理时，该字段请参考查询数据库代理规格信息接口返回体中，[规格信息]中的code字段。

        :param flavor_ref: The flavor_ref of this CreateMysqlMultiProxyRequest.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def node_num(self):
        r"""Gets the node_num of this CreateMysqlMultiProxyRequest.

        数据库代理节点数量。      - 当局点支持主备模式数据库代理时，请设置该字段为固定值2。     - 当局点支持集群模式数据库代理时，该字段最小值为2，最大值请参考查询数据库代理信息列表接口返回体中，[数据库代理信息列表]中的max_proxy_node_num字段值。

        :return: The node_num of this CreateMysqlMultiProxyRequest.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this CreateMysqlMultiProxyRequest.

        数据库代理节点数量。      - 当局点支持主备模式数据库代理时，请设置该字段为固定值2。     - 当局点支持集群模式数据库代理时，该字段最小值为2，最大值请参考查询数据库代理信息列表接口返回体中，[数据库代理信息列表]中的max_proxy_node_num字段值。

        :param node_num: The node_num of this CreateMysqlMultiProxyRequest.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def proxy_name(self):
        r"""Gets the proxy_name of this CreateMysqlMultiProxyRequest.

        数据库代理名称。用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：最小长度为4个字符，最大不超过64个字节，以字母或中文字符开头，只能包含字母、数字、中划线、下划线、英文句号和中文。  当不选择该参数或局点仅支持主备模式数据库代理时，将随机生成名称。

        :return: The proxy_name of this CreateMysqlMultiProxyRequest.
        :rtype: str
        """
        return self._proxy_name

    @proxy_name.setter
    def proxy_name(self, proxy_name):
        r"""Sets the proxy_name of this CreateMysqlMultiProxyRequest.

        数据库代理名称。用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：最小长度为4个字符，最大不超过64个字节，以字母或中文字符开头，只能包含字母、数字、中划线、下划线、英文句号和中文。  当不选择该参数或局点仅支持主备模式数据库代理时，将随机生成名称。

        :param proxy_name: The proxy_name of this CreateMysqlMultiProxyRequest.
        :type proxy_name: str
        """
        self._proxy_name = proxy_name

    @property
    def proxy_mode(self):
        r"""Gets the proxy_mode of this CreateMysqlMultiProxyRequest.

        数据库代理读写模式。 取值范围:     readwrite：读写模式。     readonly：只读模式。

        :return: The proxy_mode of this CreateMysqlMultiProxyRequest.
        :rtype: str
        """
        return self._proxy_mode

    @proxy_mode.setter
    def proxy_mode(self, proxy_mode):
        r"""Sets the proxy_mode of this CreateMysqlMultiProxyRequest.

        数据库代理读写模式。 取值范围:     readwrite：读写模式。     readonly：只读模式。

        :param proxy_mode: The proxy_mode of this CreateMysqlMultiProxyRequest.
        :type proxy_mode: str
        """
        self._proxy_mode = proxy_mode

    @property
    def route_mode(self):
        r"""Gets the route_mode of this CreateMysqlMultiProxyRequest.

        数据库代理路由模式。 取值范围:     0：表示权重负载模式。     1：表示负载均衡模式（数据库主节点不接受读请求）。     2：表示负载均衡模式（数据库主节点接受读请求）。      - 如需使用负载均衡模式，请联系客服申请

        :return: The route_mode of this CreateMysqlMultiProxyRequest.
        :rtype: int
        """
        return self._route_mode

    @route_mode.setter
    def route_mode(self, route_mode):
        r"""Sets the route_mode of this CreateMysqlMultiProxyRequest.

        数据库代理路由模式。 取值范围:     0：表示权重负载模式。     1：表示负载均衡模式（数据库主节点不接受读请求）。     2：表示负载均衡模式（数据库主节点接受读请求）。      - 如需使用负载均衡模式，请联系客服申请

        :param route_mode: The route_mode of this CreateMysqlMultiProxyRequest.
        :type route_mode: int
        """
        self._route_mode = route_mode

    @property
    def nodes_read_weight(self):
        r"""Gets the nodes_read_weight of this CreateMysqlMultiProxyRequest.

        数据库节点的读权重设置。      - 在proxy_mode（数据库代理读写模式）为readonly（只读模式）或者在route_mode（路由模式）>0时，只能为只读节点选择权重。     - 在proxy_mode（数据库代理读写模式）为readonly（只读模式）时，需要至少为一个只读实例配置权重。     - 在route_mode（路由模式）>0时，为主实例配置的权重将不生效。     - 该列表可以为空列表。

        :return: The nodes_read_weight of this CreateMysqlMultiProxyRequest.
        :rtype: list[:class:`huaweicloudsdkrds.v3.InstancesWeight`]
        """
        return self._nodes_read_weight

    @nodes_read_weight.setter
    def nodes_read_weight(self, nodes_read_weight):
        r"""Sets the nodes_read_weight of this CreateMysqlMultiProxyRequest.

        数据库节点的读权重设置。      - 在proxy_mode（数据库代理读写模式）为readonly（只读模式）或者在route_mode（路由模式）>0时，只能为只读节点选择权重。     - 在proxy_mode（数据库代理读写模式）为readonly（只读模式）时，需要至少为一个只读实例配置权重。     - 在route_mode（路由模式）>0时，为主实例配置的权重将不生效。     - 该列表可以为空列表。

        :param nodes_read_weight: The nodes_read_weight of this CreateMysqlMultiProxyRequest.
        :type nodes_read_weight: list[:class:`huaweicloudsdkrds.v3.InstancesWeight`]
        """
        self._nodes_read_weight = nodes_read_weight

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateMysqlMultiProxyRequest.

        数据库VPC下的子网ID。 取值范围为该实例所在VPC下的所有子网ID。      - 如需使用该参数，请联系客服申请。     - 获取子网ID请参考[创建VPC和子网](https://support.huaweicloud.com/api-cce/cce_02_0100.html)

        :return: The subnet_id of this CreateMysqlMultiProxyRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateMysqlMultiProxyRequest.

        数据库VPC下的子网ID。 取值范围为该实例所在VPC下的所有子网ID。      - 如需使用该参数，请联系客服申请。     - 获取子网ID请参考[创建VPC和子网](https://support.huaweicloud.com/api-cce/cce_02_0100.html)

        :param subnet_id: The subnet_id of this CreateMysqlMultiProxyRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

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
        if not isinstance(other, CreateMysqlMultiProxyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
