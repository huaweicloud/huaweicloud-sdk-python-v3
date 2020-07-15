# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListCESMonitoredObjectsResponse(SdkResponse):


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
        """ListCESMonitoredObjectsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

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
        """Gets the router of this ListCESMonitoredObjectsResponse.

        当前查询维度路由。如果是主维度，则数组中是自身ID。

        :return: The router of this ListCESMonitoredObjectsResponse.
        :rtype: list[str]
        """
        return self._router

    @router.setter
    def router(self, router):
        """Sets the router of this ListCESMonitoredObjectsResponse.

        当前查询维度路由。如果是主维度，则数组中是自身ID。

        :param router: The router of this ListCESMonitoredObjectsResponse.
        :type: list[str]
        """
        self._router = router

    @property
    def children(self):
        """Gets the children of this ListCESMonitoredObjectsResponse.

        当前查询维度子维度对象列表。当前只有维度为dcs_instance_id时才有值。 - Proxy集群有两个子维度，分别为dcs_cluster_redis_node和dcs_cluster_proxy_node。 - Cluster集群有一个子维度 dcs_cluster_proxy_node。 

        :return: The children of this ListCESMonitoredObjectsResponse.
        :rtype: list[DimChild]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this ListCESMonitoredObjectsResponse.

        当前查询维度子维度对象列表。当前只有维度为dcs_instance_id时才有值。 - Proxy集群有两个子维度，分别为dcs_cluster_redis_node和dcs_cluster_proxy_node。 - Cluster集群有一个子维度 dcs_cluster_proxy_node。 

        :param children: The children of this ListCESMonitoredObjectsResponse.
        :type: list[DimChild]
        """
        self._children = children

    @property
    def instances(self):
        """Gets the instances of this ListCESMonitoredObjectsResponse.

        当前查询维度监控对象列表。

        :return: The instances of this ListCESMonitoredObjectsResponse.
        :rtype: list[InstancesMonitoredObject]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ListCESMonitoredObjectsResponse.

        当前查询维度监控对象列表。

        :param instances: The instances of this ListCESMonitoredObjectsResponse.
        :type: list[InstancesMonitoredObject]
        """
        self._instances = instances

    @property
    def total(self):
        """Gets the total of this ListCESMonitoredObjectsResponse.

        主维度监控对象的总数。

        :return: The total of this ListCESMonitoredObjectsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListCESMonitoredObjectsResponse.

        主维度监控对象的总数。

        :param total: The total of this ListCESMonitoredObjectsResponse.
        :type: int
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListCESMonitoredObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
