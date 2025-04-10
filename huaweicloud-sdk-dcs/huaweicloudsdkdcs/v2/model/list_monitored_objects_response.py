# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMonitoredObjectsResponse(SdkResponse):

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
        'total': 'int'
    }

    attribute_map = {
        'router': 'router',
        'children': 'children',
        'instances': 'instances',
        'total': 'total'
    }

    def __init__(self, router=None, children=None, instances=None, total=None):
        r"""ListMonitoredObjectsResponse

        The model defined in huaweicloud sdk

        :param router: 当前查询维度路由。如果是主维度，则数组中是自身ID。
        :type router: list[str]
        :param children: 当前查询维度子维度对象列表。当前只有维度为dcs_instance_id时才有值。 - Proxy集群有两个子维度，分别为dcs_cluster_redis_node和dcs_cluster_proxy_node。 - Cluster集群有一个子维度 dcs_cluster_proxy_node。 
        :type children: list[:class:`huaweicloudsdkdcs.v2.DimChild`]
        :param instances: 当前查询维度监控对象列表。
        :type instances: list[:class:`huaweicloudsdkdcs.v2.InstancesMonitoredObject`]
        :param total: 主维度监控对象的总数。
        :type total: int
        """
        
        super(ListMonitoredObjectsResponse, self).__init__()

        self._router = None
        self._children = None
        self._instances = None
        self._total = None
        self.discriminator = None

        if router is not None:
            self.router = router
        if children is not None:
            self.children = children
        if instances is not None:
            self.instances = instances
        if total is not None:
            self.total = total

    @property
    def router(self):
        r"""Gets the router of this ListMonitoredObjectsResponse.

        当前查询维度路由。如果是主维度，则数组中是自身ID。

        :return: The router of this ListMonitoredObjectsResponse.
        :rtype: list[str]
        """
        return self._router

    @router.setter
    def router(self, router):
        r"""Sets the router of this ListMonitoredObjectsResponse.

        当前查询维度路由。如果是主维度，则数组中是自身ID。

        :param router: The router of this ListMonitoredObjectsResponse.
        :type router: list[str]
        """
        self._router = router

    @property
    def children(self):
        r"""Gets the children of this ListMonitoredObjectsResponse.

        当前查询维度子维度对象列表。当前只有维度为dcs_instance_id时才有值。 - Proxy集群有两个子维度，分别为dcs_cluster_redis_node和dcs_cluster_proxy_node。 - Cluster集群有一个子维度 dcs_cluster_proxy_node。 

        :return: The children of this ListMonitoredObjectsResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.DimChild`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this ListMonitoredObjectsResponse.

        当前查询维度子维度对象列表。当前只有维度为dcs_instance_id时才有值。 - Proxy集群有两个子维度，分别为dcs_cluster_redis_node和dcs_cluster_proxy_node。 - Cluster集群有一个子维度 dcs_cluster_proxy_node。 

        :param children: The children of this ListMonitoredObjectsResponse.
        :type children: list[:class:`huaweicloudsdkdcs.v2.DimChild`]
        """
        self._children = children

    @property
    def instances(self):
        r"""Gets the instances of this ListMonitoredObjectsResponse.

        当前查询维度监控对象列表。

        :return: The instances of this ListMonitoredObjectsResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.InstancesMonitoredObject`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ListMonitoredObjectsResponse.

        当前查询维度监控对象列表。

        :param instances: The instances of this ListMonitoredObjectsResponse.
        :type instances: list[:class:`huaweicloudsdkdcs.v2.InstancesMonitoredObject`]
        """
        self._instances = instances

    @property
    def total(self):
        r"""Gets the total of this ListMonitoredObjectsResponse.

        主维度监控对象的总数。

        :return: The total of this ListMonitoredObjectsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListMonitoredObjectsResponse.

        主维度监控对象的总数。

        :param total: The total of this ListMonitoredObjectsResponse.
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
        if not isinstance(other, ListMonitoredObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
