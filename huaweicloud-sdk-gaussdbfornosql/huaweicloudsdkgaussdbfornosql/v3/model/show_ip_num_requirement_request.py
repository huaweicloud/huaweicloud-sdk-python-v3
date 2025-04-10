# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIpNumRequirementRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_num': 'int',
        'engine_name': 'str',
        'instance_mode': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'node_num': 'node_num',
        'engine_name': 'engine_name',
        'instance_mode': 'instance_mode',
        'instance_id': 'instance_id'
    }

    def __init__(self, node_num=None, engine_name=None, instance_mode=None, instance_id=None):
        r"""ShowIpNumRequirementRequest

        The model defined in huaweicloud sdk

        :param node_num: 创建实例或扩容节点的个数。最大支持输入200。
        :type node_num: int
        :param engine_name: 数据库引擎名称。没有传入实例ID的时候该字段为必传。   - 取值为“cassandra”，表示GeminiDB Cassandra数据库引擎。   - 取值为“mongodb”，表示GeminiDB Mongo数据库引擎。   - 取值为“influxdb”，表示GeminiDB Influx数据库引擎。   - 取值为“redis”，表示GeminiDB Redis数据库引擎。
        :type engine_name: str
        :param instance_mode: 实例类型。没有传入实例ID的时候该字段为必传。   -  取值为“Cluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis Proxy经典部署模式集群实例类型。   -  取值为“CloudNativeCluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis云原生部署模式集群实例类型。   -  取值为“RedisCluster”，表示GeminiDB Redis Cluster经典部署模式集群实例类型。   -  取值为“Replication”，表示GeminiDB Redis经典部署模式主备实例类型。   -  取值为“InfluxdbSingle”，表示GeminiDB Influx经典部署模式单节点实例类型。   -  取值为“ReplicaSet”，表示GeminiDB Mongo副本集实例类型。
        :type instance_mode: str
        :param instance_id: 实例Id，可以调用5.3.3 查询实例列表和详情接口获取。如果未申请实例，可以调用5.3.1 创建实例接口创建。
        :type instance_id: str
        """
        
        

        self._node_num = None
        self._engine_name = None
        self._instance_mode = None
        self._instance_id = None
        self.discriminator = None

        self.node_num = node_num
        if engine_name is not None:
            self.engine_name = engine_name
        if instance_mode is not None:
            self.instance_mode = instance_mode
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def node_num(self):
        r"""Gets the node_num of this ShowIpNumRequirementRequest.

        创建实例或扩容节点的个数。最大支持输入200。

        :return: The node_num of this ShowIpNumRequirementRequest.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this ShowIpNumRequirementRequest.

        创建实例或扩容节点的个数。最大支持输入200。

        :param node_num: The node_num of this ShowIpNumRequirementRequest.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def engine_name(self):
        r"""Gets the engine_name of this ShowIpNumRequirementRequest.

        数据库引擎名称。没有传入实例ID的时候该字段为必传。   - 取值为“cassandra”，表示GeminiDB Cassandra数据库引擎。   - 取值为“mongodb”，表示GeminiDB Mongo数据库引擎。   - 取值为“influxdb”，表示GeminiDB Influx数据库引擎。   - 取值为“redis”，表示GeminiDB Redis数据库引擎。

        :return: The engine_name of this ShowIpNumRequirementRequest.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this ShowIpNumRequirementRequest.

        数据库引擎名称。没有传入实例ID的时候该字段为必传。   - 取值为“cassandra”，表示GeminiDB Cassandra数据库引擎。   - 取值为“mongodb”，表示GeminiDB Mongo数据库引擎。   - 取值为“influxdb”，表示GeminiDB Influx数据库引擎。   - 取值为“redis”，表示GeminiDB Redis数据库引擎。

        :param engine_name: The engine_name of this ShowIpNumRequirementRequest.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def instance_mode(self):
        r"""Gets the instance_mode of this ShowIpNumRequirementRequest.

        实例类型。没有传入实例ID的时候该字段为必传。   -  取值为“Cluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis Proxy经典部署模式集群实例类型。   -  取值为“CloudNativeCluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis云原生部署模式集群实例类型。   -  取值为“RedisCluster”，表示GeminiDB Redis Cluster经典部署模式集群实例类型。   -  取值为“Replication”，表示GeminiDB Redis经典部署模式主备实例类型。   -  取值为“InfluxdbSingle”，表示GeminiDB Influx经典部署模式单节点实例类型。   -  取值为“ReplicaSet”，表示GeminiDB Mongo副本集实例类型。

        :return: The instance_mode of this ShowIpNumRequirementRequest.
        :rtype: str
        """
        return self._instance_mode

    @instance_mode.setter
    def instance_mode(self, instance_mode):
        r"""Sets the instance_mode of this ShowIpNumRequirementRequest.

        实例类型。没有传入实例ID的时候该字段为必传。   -  取值为“Cluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis Proxy经典部署模式集群实例类型。   -  取值为“CloudNativeCluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis云原生部署模式集群实例类型。   -  取值为“RedisCluster”，表示GeminiDB Redis Cluster经典部署模式集群实例类型。   -  取值为“Replication”，表示GeminiDB Redis经典部署模式主备实例类型。   -  取值为“InfluxdbSingle”，表示GeminiDB Influx经典部署模式单节点实例类型。   -  取值为“ReplicaSet”，表示GeminiDB Mongo副本集实例类型。

        :param instance_mode: The instance_mode of this ShowIpNumRequirementRequest.
        :type instance_mode: str
        """
        self._instance_mode = instance_mode

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowIpNumRequirementRequest.

        实例Id，可以调用5.3.3 查询实例列表和详情接口获取。如果未申请实例，可以调用5.3.1 创建实例接口创建。

        :return: The instance_id of this ShowIpNumRequirementRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowIpNumRequirementRequest.

        实例Id，可以调用5.3.3 查询实例列表和详情接口获取。如果未申请实例，可以调用5.3.1 创建实例接口创建。

        :param instance_id: The instance_id of this ShowIpNumRequirementRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ShowIpNumRequirementRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
