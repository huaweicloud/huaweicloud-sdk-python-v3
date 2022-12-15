# coding: utf-8

import re
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
        'nodes_read_weight': 'list[NodesWeight]'
    }

    attribute_map = {
        'flavor_ref': 'flavor_ref',
        'node_num': 'node_num',
        'proxy_name': 'proxy_name',
        'proxy_mode': 'proxy_mode',
        'nodes_read_weight': 'nodes_read_weight'
    }

    def __init__(self, flavor_ref=None, node_num=None, proxy_name=None, proxy_mode=None, nodes_read_weight=None):
        """OpenMysqlProxyRequestBody

        The model defined in huaweicloud sdk

        :param flavor_ref: 代理规格码。
        :type flavor_ref: str
        :param node_num: 代理实例节点数，取值整数2-32。
        :type node_num: int
        :param proxy_name: 代理实例名称。用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。
        :type proxy_name: str
        :param proxy_mode: 代理实例类型。默认类型为readwrite。
        :type proxy_mode: str
        :param nodes_read_weight: 数据库节点的读权重设置。
        :type nodes_read_weight: list[:class:`huaweicloudsdkgaussdb.v3.NodesWeight`]
        """
        
        

        self._flavor_ref = None
        self._node_num = None
        self._proxy_name = None
        self._proxy_mode = None
        self._nodes_read_weight = None
        self.discriminator = None

        self.flavor_ref = flavor_ref
        self.node_num = node_num
        if proxy_name is not None:
            self.proxy_name = proxy_name
        if proxy_mode is not None:
            self.proxy_mode = proxy_mode
        if nodes_read_weight is not None:
            self.nodes_read_weight = nodes_read_weight

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this OpenMysqlProxyRequestBody.

        代理规格码。

        :return: The flavor_ref of this OpenMysqlProxyRequestBody.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this OpenMysqlProxyRequestBody.

        代理规格码。

        :param flavor_ref: The flavor_ref of this OpenMysqlProxyRequestBody.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def node_num(self):
        """Gets the node_num of this OpenMysqlProxyRequestBody.

        代理实例节点数，取值整数2-32。

        :return: The node_num of this OpenMysqlProxyRequestBody.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this OpenMysqlProxyRequestBody.

        代理实例节点数，取值整数2-32。

        :param node_num: The node_num of this OpenMysqlProxyRequestBody.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def proxy_name(self):
        """Gets the proxy_name of this OpenMysqlProxyRequestBody.

        代理实例名称。用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :return: The proxy_name of this OpenMysqlProxyRequestBody.
        :rtype: str
        """
        return self._proxy_name

    @proxy_name.setter
    def proxy_name(self, proxy_name):
        """Sets the proxy_name of this OpenMysqlProxyRequestBody.

        代理实例名称。用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :param proxy_name: The proxy_name of this OpenMysqlProxyRequestBody.
        :type proxy_name: str
        """
        self._proxy_name = proxy_name

    @property
    def proxy_mode(self):
        """Gets the proxy_mode of this OpenMysqlProxyRequestBody.

        代理实例类型。默认类型为readwrite。

        :return: The proxy_mode of this OpenMysqlProxyRequestBody.
        :rtype: str
        """
        return self._proxy_mode

    @proxy_mode.setter
    def proxy_mode(self, proxy_mode):
        """Sets the proxy_mode of this OpenMysqlProxyRequestBody.

        代理实例类型。默认类型为readwrite。

        :param proxy_mode: The proxy_mode of this OpenMysqlProxyRequestBody.
        :type proxy_mode: str
        """
        self._proxy_mode = proxy_mode

    @property
    def nodes_read_weight(self):
        """Gets the nodes_read_weight of this OpenMysqlProxyRequestBody.

        数据库节点的读权重设置。

        :return: The nodes_read_weight of this OpenMysqlProxyRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.NodesWeight`]
        """
        return self._nodes_read_weight

    @nodes_read_weight.setter
    def nodes_read_weight(self, nodes_read_weight):
        """Sets the nodes_read_weight of this OpenMysqlProxyRequestBody.

        数据库节点的读权重设置。

        :param nodes_read_weight: The nodes_read_weight of this OpenMysqlProxyRequestBody.
        :type nodes_read_weight: list[:class:`huaweicloudsdkgaussdb.v3.NodesWeight`]
        """
        self._nodes_read_weight = nodes_read_weight

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
