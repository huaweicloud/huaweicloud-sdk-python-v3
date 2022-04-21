# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterRedisNodeMonitoredObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dcs_instance_id': 'str',
        'name': 'str',
        'dcs_cluster_redis_node': 'str',
        'status': 'str'
    }

    attribute_map = {
        'dcs_instance_id': 'dcs_instance_id',
        'name': 'name',
        'dcs_cluster_redis_node': 'dcs_cluster_redis_node',
        'status': 'status'
    }

    def __init__(self, dcs_instance_id=None, name=None, dcs_cluster_redis_node=None, status=None):
        """ClusterRedisNodeMonitoredObject

        The model defined in huaweicloud sdk

        :param dcs_instance_id: 测量对象ID，即节点的ID。
        :type dcs_instance_id: str
        :param name: 测量对象名称，即节点IP。
        :type name: str
        :param dcs_cluster_redis_node: 维度dcs_cluster_redis_node的测量对象的ID。
        :type dcs_cluster_redis_node: str
        :param status: 测量对象状态，即节点状态。
        :type status: str
        """
        
        

        self._dcs_instance_id = None
        self._name = None
        self._dcs_cluster_redis_node = None
        self._status = None
        self.discriminator = None

        if dcs_instance_id is not None:
            self.dcs_instance_id = dcs_instance_id
        if name is not None:
            self.name = name
        if dcs_cluster_redis_node is not None:
            self.dcs_cluster_redis_node = dcs_cluster_redis_node
        if status is not None:
            self.status = status

    @property
    def dcs_instance_id(self):
        """Gets the dcs_instance_id of this ClusterRedisNodeMonitoredObject.

        测量对象ID，即节点的ID。

        :return: The dcs_instance_id of this ClusterRedisNodeMonitoredObject.
        :rtype: str
        """
        return self._dcs_instance_id

    @dcs_instance_id.setter
    def dcs_instance_id(self, dcs_instance_id):
        """Sets the dcs_instance_id of this ClusterRedisNodeMonitoredObject.

        测量对象ID，即节点的ID。

        :param dcs_instance_id: The dcs_instance_id of this ClusterRedisNodeMonitoredObject.
        :type dcs_instance_id: str
        """
        self._dcs_instance_id = dcs_instance_id

    @property
    def name(self):
        """Gets the name of this ClusterRedisNodeMonitoredObject.

        测量对象名称，即节点IP。

        :return: The name of this ClusterRedisNodeMonitoredObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterRedisNodeMonitoredObject.

        测量对象名称，即节点IP。

        :param name: The name of this ClusterRedisNodeMonitoredObject.
        :type name: str
        """
        self._name = name

    @property
    def dcs_cluster_redis_node(self):
        """Gets the dcs_cluster_redis_node of this ClusterRedisNodeMonitoredObject.

        维度dcs_cluster_redis_node的测量对象的ID。

        :return: The dcs_cluster_redis_node of this ClusterRedisNodeMonitoredObject.
        :rtype: str
        """
        return self._dcs_cluster_redis_node

    @dcs_cluster_redis_node.setter
    def dcs_cluster_redis_node(self, dcs_cluster_redis_node):
        """Sets the dcs_cluster_redis_node of this ClusterRedisNodeMonitoredObject.

        维度dcs_cluster_redis_node的测量对象的ID。

        :param dcs_cluster_redis_node: The dcs_cluster_redis_node of this ClusterRedisNodeMonitoredObject.
        :type dcs_cluster_redis_node: str
        """
        self._dcs_cluster_redis_node = dcs_cluster_redis_node

    @property
    def status(self):
        """Gets the status of this ClusterRedisNodeMonitoredObject.

        测量对象状态，即节点状态。

        :return: The status of this ClusterRedisNodeMonitoredObject.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterRedisNodeMonitoredObject.

        测量对象状态，即节点状态。

        :param status: The status of this ClusterRedisNodeMonitoredObject.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ClusterRedisNodeMonitoredObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
