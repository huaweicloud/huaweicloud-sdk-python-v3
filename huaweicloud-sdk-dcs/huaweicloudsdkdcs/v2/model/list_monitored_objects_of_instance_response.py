# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMonitoredObjectsOfInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'router': 'list[str]',
        'children': 'list[DimChild]',
        'instances': 'list[InstancesMonitoredObject]',
        'dcs_cluster_redis_node': 'list[ClusterRedisNodeMonitoredObject]',
        'dcs_cluster_proxy_node': 'list[ProxyNodeMonitoredObject]',
        'dcs_cluster_proxy2_node': 'list[Proxy2NodeMonitoredObject]',
        'total': 'int'
    }

    attribute_map = {
        'router': 'router',
        'children': 'children',
        'instances': 'instances',
        'dcs_cluster_redis_node': 'dcs_cluster_redis_node',
        'dcs_cluster_proxy_node': 'dcs_cluster_proxy_node',
        'dcs_cluster_proxy2_node': 'dcs_cluster_proxy2_node',
        'total': 'total'
    }

    def __init__(self, router=None, children=None, instances=None, dcs_cluster_redis_node=None, dcs_cluster_proxy_node=None, dcs_cluster_proxy2_node=None, total=None):
        """ListMonitoredObjectsOfInstanceResponse

        The model defined in huaweicloud sdk

        :param router: 当前查询维度路由。如果是主维度，则数组中是自身ID。
        :type router: list[str]
        :param children: 当前查询维度子维度对象列表。当前只有维度为dcs_instance_id时才有值。 - Proxy集群有两个子维度，分别为dcs_cluster_redis_node和dcs_cluster_proxy_node。 - Cluster集群有一个子维度 dcs_cluster_proxy_node。 
        :type children: list[:class:`huaweicloudsdkdcs.v2.DimChild`]
        :param instances: 当前查询维度监控对象列表。
        :type instances: list[:class:`huaweicloudsdkdcs.v2.InstancesMonitoredObject`]
        :param dcs_cluster_redis_node: Proxy集群或Cluster集群时才存在，表示集群数据节点维度的监控对象列表。字段名称与children的子维度对象名称相同。
        :type dcs_cluster_redis_node: list[:class:`huaweicloudsdkdcs.v2.ClusterRedisNodeMonitoredObject`]
        :param dcs_cluster_proxy_node: Proxy集群时才存在，表示集群Proxy节点维度的监控对象列表。字段名称与children的子维度对象名称相同。
        :type dcs_cluster_proxy_node: list[:class:`huaweicloudsdkdcs.v2.ProxyNodeMonitoredObject`]
        :param dcs_cluster_proxy2_node: Redis 4.0和5.0的Proxy集群时才存在，表示集群Proxy节点维度的监控对象列表。字段名称与children的子维度对象名称相同。 
        :type dcs_cluster_proxy2_node: list[:class:`huaweicloudsdkdcs.v2.Proxy2NodeMonitoredObject`]
        :param total: 主维度监控对象的总数。
        :type total: int
        """
        
        super(ListMonitoredObjectsOfInstanceResponse, self).__init__()

        self._router = None
        self._children = None
        self._instances = None
        self._dcs_cluster_redis_node = None
        self._dcs_cluster_proxy_node = None
        self._dcs_cluster_proxy2_node = None
        self._total = None
        self.discriminator = None

        if router is not None:
            self.router = router
        if children is not None:
            self.children = children
        if instances is not None:
            self.instances = instances
        if dcs_cluster_redis_node is not None:
            self.dcs_cluster_redis_node = dcs_cluster_redis_node
        if dcs_cluster_proxy_node is not None:
            self.dcs_cluster_proxy_node = dcs_cluster_proxy_node
        if dcs_cluster_proxy2_node is not None:
            self.dcs_cluster_proxy2_node = dcs_cluster_proxy2_node
        if total is not None:
            self.total = total

    @property
    def router(self):
        """Gets the router of this ListMonitoredObjectsOfInstanceResponse.

        当前查询维度路由。如果是主维度，则数组中是自身ID。

        :return: The router of this ListMonitoredObjectsOfInstanceResponse.
        :rtype: list[str]
        """
        return self._router

    @router.setter
    def router(self, router):
        """Sets the router of this ListMonitoredObjectsOfInstanceResponse.

        当前查询维度路由。如果是主维度，则数组中是自身ID。

        :param router: The router of this ListMonitoredObjectsOfInstanceResponse.
        :type router: list[str]
        """
        self._router = router

    @property
    def children(self):
        """Gets the children of this ListMonitoredObjectsOfInstanceResponse.

        当前查询维度子维度对象列表。当前只有维度为dcs_instance_id时才有值。 - Proxy集群有两个子维度，分别为dcs_cluster_redis_node和dcs_cluster_proxy_node。 - Cluster集群有一个子维度 dcs_cluster_proxy_node。 

        :return: The children of this ListMonitoredObjectsOfInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.DimChild`]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this ListMonitoredObjectsOfInstanceResponse.

        当前查询维度子维度对象列表。当前只有维度为dcs_instance_id时才有值。 - Proxy集群有两个子维度，分别为dcs_cluster_redis_node和dcs_cluster_proxy_node。 - Cluster集群有一个子维度 dcs_cluster_proxy_node。 

        :param children: The children of this ListMonitoredObjectsOfInstanceResponse.
        :type children: list[:class:`huaweicloudsdkdcs.v2.DimChild`]
        """
        self._children = children

    @property
    def instances(self):
        """Gets the instances of this ListMonitoredObjectsOfInstanceResponse.

        当前查询维度监控对象列表。

        :return: The instances of this ListMonitoredObjectsOfInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.InstancesMonitoredObject`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ListMonitoredObjectsOfInstanceResponse.

        当前查询维度监控对象列表。

        :param instances: The instances of this ListMonitoredObjectsOfInstanceResponse.
        :type instances: list[:class:`huaweicloudsdkdcs.v2.InstancesMonitoredObject`]
        """
        self._instances = instances

    @property
    def dcs_cluster_redis_node(self):
        """Gets the dcs_cluster_redis_node of this ListMonitoredObjectsOfInstanceResponse.

        Proxy集群或Cluster集群时才存在，表示集群数据节点维度的监控对象列表。字段名称与children的子维度对象名称相同。

        :return: The dcs_cluster_redis_node of this ListMonitoredObjectsOfInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.ClusterRedisNodeMonitoredObject`]
        """
        return self._dcs_cluster_redis_node

    @dcs_cluster_redis_node.setter
    def dcs_cluster_redis_node(self, dcs_cluster_redis_node):
        """Sets the dcs_cluster_redis_node of this ListMonitoredObjectsOfInstanceResponse.

        Proxy集群或Cluster集群时才存在，表示集群数据节点维度的监控对象列表。字段名称与children的子维度对象名称相同。

        :param dcs_cluster_redis_node: The dcs_cluster_redis_node of this ListMonitoredObjectsOfInstanceResponse.
        :type dcs_cluster_redis_node: list[:class:`huaweicloudsdkdcs.v2.ClusterRedisNodeMonitoredObject`]
        """
        self._dcs_cluster_redis_node = dcs_cluster_redis_node

    @property
    def dcs_cluster_proxy_node(self):
        """Gets the dcs_cluster_proxy_node of this ListMonitoredObjectsOfInstanceResponse.

        Proxy集群时才存在，表示集群Proxy节点维度的监控对象列表。字段名称与children的子维度对象名称相同。

        :return: The dcs_cluster_proxy_node of this ListMonitoredObjectsOfInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.ProxyNodeMonitoredObject`]
        """
        return self._dcs_cluster_proxy_node

    @dcs_cluster_proxy_node.setter
    def dcs_cluster_proxy_node(self, dcs_cluster_proxy_node):
        """Sets the dcs_cluster_proxy_node of this ListMonitoredObjectsOfInstanceResponse.

        Proxy集群时才存在，表示集群Proxy节点维度的监控对象列表。字段名称与children的子维度对象名称相同。

        :param dcs_cluster_proxy_node: The dcs_cluster_proxy_node of this ListMonitoredObjectsOfInstanceResponse.
        :type dcs_cluster_proxy_node: list[:class:`huaweicloudsdkdcs.v2.ProxyNodeMonitoredObject`]
        """
        self._dcs_cluster_proxy_node = dcs_cluster_proxy_node

    @property
    def dcs_cluster_proxy2_node(self):
        """Gets the dcs_cluster_proxy2_node of this ListMonitoredObjectsOfInstanceResponse.

        Redis 4.0和5.0的Proxy集群时才存在，表示集群Proxy节点维度的监控对象列表。字段名称与children的子维度对象名称相同。 

        :return: The dcs_cluster_proxy2_node of this ListMonitoredObjectsOfInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.Proxy2NodeMonitoredObject`]
        """
        return self._dcs_cluster_proxy2_node

    @dcs_cluster_proxy2_node.setter
    def dcs_cluster_proxy2_node(self, dcs_cluster_proxy2_node):
        """Sets the dcs_cluster_proxy2_node of this ListMonitoredObjectsOfInstanceResponse.

        Redis 4.0和5.0的Proxy集群时才存在，表示集群Proxy节点维度的监控对象列表。字段名称与children的子维度对象名称相同。 

        :param dcs_cluster_proxy2_node: The dcs_cluster_proxy2_node of this ListMonitoredObjectsOfInstanceResponse.
        :type dcs_cluster_proxy2_node: list[:class:`huaweicloudsdkdcs.v2.Proxy2NodeMonitoredObject`]
        """
        self._dcs_cluster_proxy2_node = dcs_cluster_proxy2_node

    @property
    def total(self):
        """Gets the total of this ListMonitoredObjectsOfInstanceResponse.

        主维度监控对象的总数。

        :return: The total of this ListMonitoredObjectsOfInstanceResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListMonitoredObjectsOfInstanceResponse.

        主维度监控对象的总数。

        :param total: The total of this ListMonitoredObjectsOfInstanceResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListMonitoredObjectsOfInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
