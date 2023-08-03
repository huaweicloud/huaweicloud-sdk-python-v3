# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyGaussMySqlProxyRouteModeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'route_mode': 'int',
        'master_weight': 'int',
        'readonly_nodes': 'list[ModifyProxyRouteWeightReadonlyNode]'
    }

    attribute_map = {
        'route_mode': 'route_mode',
        'master_weight': 'master_weight',
        'readonly_nodes': 'readonly_nodes'
    }

    def __init__(self, route_mode=None, master_weight=None, readonly_nodes=None):
        """ModifyGaussMySqlProxyRouteModeRequestBody

        The model defined in huaweicloud sdk

        :param route_mode: 数据库代理路由模式。  取值范围： - 0，表示权重负载模式。 - 1，表示负载均衡模式（数据库主节点不接受读请求）。 - 2，表示负载均衡模式（数据库主节点接受读请求）。
        :type route_mode: int
        :param master_weight: 主节点权重： - 如果路由模式为0，取值为0~1000。 - 如果路由模式为1，取值为0。 - 如果路由模式为2，取值为1。
        :type master_weight: int
        :param readonly_nodes: 只读节点权重配置信息。
        :type readonly_nodes: list[:class:`huaweicloudsdkgaussdb.v3.ModifyProxyRouteWeightReadonlyNode`]
        """
        
        

        self._route_mode = None
        self._master_weight = None
        self._readonly_nodes = None
        self.discriminator = None

        self.route_mode = route_mode
        if master_weight is not None:
            self.master_weight = master_weight
        if readonly_nodes is not None:
            self.readonly_nodes = readonly_nodes

    @property
    def route_mode(self):
        """Gets the route_mode of this ModifyGaussMySqlProxyRouteModeRequestBody.

        数据库代理路由模式。  取值范围： - 0，表示权重负载模式。 - 1，表示负载均衡模式（数据库主节点不接受读请求）。 - 2，表示负载均衡模式（数据库主节点接受读请求）。

        :return: The route_mode of this ModifyGaussMySqlProxyRouteModeRequestBody.
        :rtype: int
        """
        return self._route_mode

    @route_mode.setter
    def route_mode(self, route_mode):
        """Sets the route_mode of this ModifyGaussMySqlProxyRouteModeRequestBody.

        数据库代理路由模式。  取值范围： - 0，表示权重负载模式。 - 1，表示负载均衡模式（数据库主节点不接受读请求）。 - 2，表示负载均衡模式（数据库主节点接受读请求）。

        :param route_mode: The route_mode of this ModifyGaussMySqlProxyRouteModeRequestBody.
        :type route_mode: int
        """
        self._route_mode = route_mode

    @property
    def master_weight(self):
        """Gets the master_weight of this ModifyGaussMySqlProxyRouteModeRequestBody.

        主节点权重： - 如果路由模式为0，取值为0~1000。 - 如果路由模式为1，取值为0。 - 如果路由模式为2，取值为1。

        :return: The master_weight of this ModifyGaussMySqlProxyRouteModeRequestBody.
        :rtype: int
        """
        return self._master_weight

    @master_weight.setter
    def master_weight(self, master_weight):
        """Sets the master_weight of this ModifyGaussMySqlProxyRouteModeRequestBody.

        主节点权重： - 如果路由模式为0，取值为0~1000。 - 如果路由模式为1，取值为0。 - 如果路由模式为2，取值为1。

        :param master_weight: The master_weight of this ModifyGaussMySqlProxyRouteModeRequestBody.
        :type master_weight: int
        """
        self._master_weight = master_weight

    @property
    def readonly_nodes(self):
        """Gets the readonly_nodes of this ModifyGaussMySqlProxyRouteModeRequestBody.

        只读节点权重配置信息。

        :return: The readonly_nodes of this ModifyGaussMySqlProxyRouteModeRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ModifyProxyRouteWeightReadonlyNode`]
        """
        return self._readonly_nodes

    @readonly_nodes.setter
    def readonly_nodes(self, readonly_nodes):
        """Sets the readonly_nodes of this ModifyGaussMySqlProxyRouteModeRequestBody.

        只读节点权重配置信息。

        :param readonly_nodes: The readonly_nodes of this ModifyGaussMySqlProxyRouteModeRequestBody.
        :type readonly_nodes: list[:class:`huaweicloudsdkgaussdb.v3.ModifyProxyRouteWeightReadonlyNode`]
        """
        self._readonly_nodes = readonly_nodes

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
        if not isinstance(other, ModifyGaussMySqlProxyRouteModeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
