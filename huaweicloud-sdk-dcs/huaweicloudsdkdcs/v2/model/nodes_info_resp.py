# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodesInfoResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logical_node_id': 'str',
        'name': 'str',
        'status': 'str',
        'az_code': 'str',
        'node_role': 'str',
        'node_type': 'str',
        'node_ip': 'str',
        'node_port': 'str',
        'node_id': 'str',
        'priority_weight': 'int',
        'is_access': 'bool',
        'group_id': 'str',
        'group_name': 'str',
        'is_remove_ip': 'bool',
        'replication_id': 'str',
        'dimensions': 'list[InstanceReplicationDimensionsInfo]'
    }

    attribute_map = {
        'logical_node_id': 'logical_node_id',
        'name': 'name',
        'status': 'status',
        'az_code': 'az_code',
        'node_role': 'node_role',
        'node_type': 'node_type',
        'node_ip': 'node_ip',
        'node_port': 'node_port',
        'node_id': 'node_id',
        'priority_weight': 'priority_weight',
        'is_access': 'is_access',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'is_remove_ip': 'is_remove_ip',
        'replication_id': 'replication_id',
        'dimensions': 'dimensions'
    }

    def __init__(self, logical_node_id=None, name=None, status=None, az_code=None, node_role=None, node_type=None, node_ip=None, node_port=None, node_id=None, priority_weight=None, is_access=None, group_id=None, group_name=None, is_remove_ip=None, replication_id=None, dimensions=None):
        """NodesInfoResp

        The model defined in huaweicloud sdk

        :param logical_node_id: 逻辑节点ID
        :type logical_node_id: str
        :param name: 节点名称
        :type name: str
        :param status: 节点状态，所有值如下: - Creating：创建中。 - Active：运行中。 - Inactive：故障。 - Deleting：删除中。 - AddSharding：添加分片中。 
        :type status: str
        :param az_code: 可用区code
        :type az_code: str
        :param node_role: 节点角色，所有值如下: - redis-server：Redis server节点。 - redis-proxy：proxy节点。 
        :type node_role: str
        :param node_type: 节点主从角色: - master：主 - slave：从 - proxy: proxy实例节点角色为\&quot;proxy\&quot; 
        :type node_type: str
        :param node_ip: 节点的IP
        :type node_ip: str
        :param node_port: 节点的port
        :type node_port: str
        :param node_id: 节点ID
        :type node_id: str
        :param priority_weight: 节点权重
        :type priority_weight: int
        :param is_access: 节点的IP是否可直接访问
        :type is_access: bool
        :param group_id: 分片ID
        :type group_id: str
        :param group_name: 分片名称
        :type group_name: str
        :param is_remove_ip: 是否从只读域名中摘除IP
        :type is_remove_ip: bool
        :param replication_id: 副本id
        :type replication_id: str
        :param dimensions: 副本对应的监控指标维度信息。可用于调用云监控服务的查询监控数据指标相关接口 - 副本的监控维度为多维度，返回数组中包含两个维度信息。从云监控查询监控数据时，要按多维度传递指标维度参数，才能查询到监控指标值 - 第一个维度为副本父维度信息 维度名称为dcs_instance_id，维度值对应副本所在的实例ID - 第二个维度，维度名称为dcs_cluster_redis_node,维度值为副本的监控对象ID，与副本ID和节点ID不同。 
        :type dimensions: list[:class:`huaweicloudsdkdcs.v2.InstanceReplicationDimensionsInfo`]
        """
        
        

        self._logical_node_id = None
        self._name = None
        self._status = None
        self._az_code = None
        self._node_role = None
        self._node_type = None
        self._node_ip = None
        self._node_port = None
        self._node_id = None
        self._priority_weight = None
        self._is_access = None
        self._group_id = None
        self._group_name = None
        self._is_remove_ip = None
        self._replication_id = None
        self._dimensions = None
        self.discriminator = None

        if logical_node_id is not None:
            self.logical_node_id = logical_node_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if az_code is not None:
            self.az_code = az_code
        if node_role is not None:
            self.node_role = node_role
        if node_type is not None:
            self.node_type = node_type
        if node_ip is not None:
            self.node_ip = node_ip
        if node_port is not None:
            self.node_port = node_port
        if node_id is not None:
            self.node_id = node_id
        if priority_weight is not None:
            self.priority_weight = priority_weight
        if is_access is not None:
            self.is_access = is_access
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if is_remove_ip is not None:
            self.is_remove_ip = is_remove_ip
        if replication_id is not None:
            self.replication_id = replication_id
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def logical_node_id(self):
        """Gets the logical_node_id of this NodesInfoResp.

        逻辑节点ID

        :return: The logical_node_id of this NodesInfoResp.
        :rtype: str
        """
        return self._logical_node_id

    @logical_node_id.setter
    def logical_node_id(self, logical_node_id):
        """Sets the logical_node_id of this NodesInfoResp.

        逻辑节点ID

        :param logical_node_id: The logical_node_id of this NodesInfoResp.
        :type logical_node_id: str
        """
        self._logical_node_id = logical_node_id

    @property
    def name(self):
        """Gets the name of this NodesInfoResp.

        节点名称

        :return: The name of this NodesInfoResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodesInfoResp.

        节点名称

        :param name: The name of this NodesInfoResp.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this NodesInfoResp.

        节点状态，所有值如下: - Creating：创建中。 - Active：运行中。 - Inactive：故障。 - Deleting：删除中。 - AddSharding：添加分片中。 

        :return: The status of this NodesInfoResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodesInfoResp.

        节点状态，所有值如下: - Creating：创建中。 - Active：运行中。 - Inactive：故障。 - Deleting：删除中。 - AddSharding：添加分片中。 

        :param status: The status of this NodesInfoResp.
        :type status: str
        """
        self._status = status

    @property
    def az_code(self):
        """Gets the az_code of this NodesInfoResp.

        可用区code

        :return: The az_code of this NodesInfoResp.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this NodesInfoResp.

        可用区code

        :param az_code: The az_code of this NodesInfoResp.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def node_role(self):
        """Gets the node_role of this NodesInfoResp.

        节点角色，所有值如下: - redis-server：Redis server节点。 - redis-proxy：proxy节点。 

        :return: The node_role of this NodesInfoResp.
        :rtype: str
        """
        return self._node_role

    @node_role.setter
    def node_role(self, node_role):
        """Sets the node_role of this NodesInfoResp.

        节点角色，所有值如下: - redis-server：Redis server节点。 - redis-proxy：proxy节点。 

        :param node_role: The node_role of this NodesInfoResp.
        :type node_role: str
        """
        self._node_role = node_role

    @property
    def node_type(self):
        """Gets the node_type of this NodesInfoResp.

        节点主从角色: - master：主 - slave：从 - proxy: proxy实例节点角色为\"proxy\" 

        :return: The node_type of this NodesInfoResp.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this NodesInfoResp.

        节点主从角色: - master：主 - slave：从 - proxy: proxy实例节点角色为\"proxy\" 

        :param node_type: The node_type of this NodesInfoResp.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def node_ip(self):
        """Gets the node_ip of this NodesInfoResp.

        节点的IP

        :return: The node_ip of this NodesInfoResp.
        :rtype: str
        """
        return self._node_ip

    @node_ip.setter
    def node_ip(self, node_ip):
        """Sets the node_ip of this NodesInfoResp.

        节点的IP

        :param node_ip: The node_ip of this NodesInfoResp.
        :type node_ip: str
        """
        self._node_ip = node_ip

    @property
    def node_port(self):
        """Gets the node_port of this NodesInfoResp.

        节点的port

        :return: The node_port of this NodesInfoResp.
        :rtype: str
        """
        return self._node_port

    @node_port.setter
    def node_port(self, node_port):
        """Sets the node_port of this NodesInfoResp.

        节点的port

        :param node_port: The node_port of this NodesInfoResp.
        :type node_port: str
        """
        self._node_port = node_port

    @property
    def node_id(self):
        """Gets the node_id of this NodesInfoResp.

        节点ID

        :return: The node_id of this NodesInfoResp.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this NodesInfoResp.

        节点ID

        :param node_id: The node_id of this NodesInfoResp.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def priority_weight(self):
        """Gets the priority_weight of this NodesInfoResp.

        节点权重

        :return: The priority_weight of this NodesInfoResp.
        :rtype: int
        """
        return self._priority_weight

    @priority_weight.setter
    def priority_weight(self, priority_weight):
        """Sets the priority_weight of this NodesInfoResp.

        节点权重

        :param priority_weight: The priority_weight of this NodesInfoResp.
        :type priority_weight: int
        """
        self._priority_weight = priority_weight

    @property
    def is_access(self):
        """Gets the is_access of this NodesInfoResp.

        节点的IP是否可直接访问

        :return: The is_access of this NodesInfoResp.
        :rtype: bool
        """
        return self._is_access

    @is_access.setter
    def is_access(self, is_access):
        """Sets the is_access of this NodesInfoResp.

        节点的IP是否可直接访问

        :param is_access: The is_access of this NodesInfoResp.
        :type is_access: bool
        """
        self._is_access = is_access

    @property
    def group_id(self):
        """Gets the group_id of this NodesInfoResp.

        分片ID

        :return: The group_id of this NodesInfoResp.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this NodesInfoResp.

        分片ID

        :param group_id: The group_id of this NodesInfoResp.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this NodesInfoResp.

        分片名称

        :return: The group_name of this NodesInfoResp.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this NodesInfoResp.

        分片名称

        :param group_name: The group_name of this NodesInfoResp.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def is_remove_ip(self):
        """Gets the is_remove_ip of this NodesInfoResp.

        是否从只读域名中摘除IP

        :return: The is_remove_ip of this NodesInfoResp.
        :rtype: bool
        """
        return self._is_remove_ip

    @is_remove_ip.setter
    def is_remove_ip(self, is_remove_ip):
        """Sets the is_remove_ip of this NodesInfoResp.

        是否从只读域名中摘除IP

        :param is_remove_ip: The is_remove_ip of this NodesInfoResp.
        :type is_remove_ip: bool
        """
        self._is_remove_ip = is_remove_ip

    @property
    def replication_id(self):
        """Gets the replication_id of this NodesInfoResp.

        副本id

        :return: The replication_id of this NodesInfoResp.
        :rtype: str
        """
        return self._replication_id

    @replication_id.setter
    def replication_id(self, replication_id):
        """Sets the replication_id of this NodesInfoResp.

        副本id

        :param replication_id: The replication_id of this NodesInfoResp.
        :type replication_id: str
        """
        self._replication_id = replication_id

    @property
    def dimensions(self):
        """Gets the dimensions of this NodesInfoResp.

        副本对应的监控指标维度信息。可用于调用云监控服务的查询监控数据指标相关接口 - 副本的监控维度为多维度，返回数组中包含两个维度信息。从云监控查询监控数据时，要按多维度传递指标维度参数，才能查询到监控指标值 - 第一个维度为副本父维度信息 维度名称为dcs_instance_id，维度值对应副本所在的实例ID - 第二个维度，维度名称为dcs_cluster_redis_node,维度值为副本的监控对象ID，与副本ID和节点ID不同。 

        :return: The dimensions of this NodesInfoResp.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.InstanceReplicationDimensionsInfo`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this NodesInfoResp.

        副本对应的监控指标维度信息。可用于调用云监控服务的查询监控数据指标相关接口 - 副本的监控维度为多维度，返回数组中包含两个维度信息。从云监控查询监控数据时，要按多维度传递指标维度参数，才能查询到监控指标值 - 第一个维度为副本父维度信息 维度名称为dcs_instance_id，维度值对应副本所在的实例ID - 第二个维度，维度名称为dcs_cluster_redis_node,维度值为副本的监控对象ID，与副本ID和节点ID不同。 

        :param dimensions: The dimensions of this NodesInfoResp.
        :type dimensions: list[:class:`huaweicloudsdkdcs.v2.InstanceReplicationDimensionsInfo`]
        """
        self._dimensions = dimensions

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
        if not isinstance(other, NodesInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
