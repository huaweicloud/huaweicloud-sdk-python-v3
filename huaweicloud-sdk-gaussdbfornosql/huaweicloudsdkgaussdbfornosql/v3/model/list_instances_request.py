# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'mode': 'str',
        'datastore_type': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'mode': 'mode',
        'datastore_type': 'datastore_type',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, id=None, name=None, mode=None, datastore_type=None, vpc_id=None, subnet_id=None, offset=None, limit=None):
        """ListInstancesRequest

        The model defined in huaweicloud sdk

        :param id: 实例ID。 如果id以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的id精确匹配查询。
        :type id: str
        :param name: 实例名称。 如果name以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的name精确匹配查询。
        :type name: str
        :param mode: 实例类型。   - 取值为“Cluster”，表示GaussDB(for Cassandra)、GaussDB(for Influx)、GaussDB(for Redis)集群实例类型。   - 取值为“Sharding”，表示GaussDB(for Mongo)集群实例类型。   - 取值为“ReplicaSet”，表示GaussDB(for Mongo)副本集实例类型。   - 取值为“InfluxdbCluster”，表示GaussDB(for Influx)集群实例类型。   - 取值为“InfluxdbSingle”，表示GaussDB(for Influx)单节点实例类型。   - 取值为“RedisReplica”，表示GaussDB(for Redis)性能版实例类型。   - 取值为“Replication”，表示GaussDB(for Redis)主备版实例类型。
        :type mode: str
        :param datastore_type: 数据库类型。   - 取值为“cassandra”，表示查询GaussDB(for Cassandra)数据库实例。   - 取值为“mongodb”，表示查询GaussDB(for Mongo)数据库实例。   - 取值为“influxdb”，表示查询GaussDB(for Influx)数据库实例。   - 取值为“redis”，表示查询GaussDB(for Redis)数据库实例。   - 如果不传该参数，表示查询所有数据库实例。
        :type datastore_type: str
        :param vpc_id: 虚拟私有云ID，获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询VPC列表。
        :type vpc_id: str
        :param subnet_id: 子网的网络ID，获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询子网列表。
        :type subnet_id: str
        :param offset: 索引位置偏移量，表示从指定project ID下最新的实例创建时间开始，按时间的先后顺序偏移offset条数据后查询对应的实例信息。 取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从最新的实例创建时间对应的实例开始查询。
        :type offset: int
        :param limit: 查询实例个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条实例信息。
        :type limit: int
        """
        
        

        self._id = None
        self._name = None
        self._mode = None
        self._datastore_type = None
        self._vpc_id = None
        self._subnet_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if mode is not None:
            self.mode = mode
        if datastore_type is not None:
            self.datastore_type = datastore_type
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def id(self):
        """Gets the id of this ListInstancesRequest.

        实例ID。 如果id以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的id精确匹配查询。

        :return: The id of this ListInstancesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListInstancesRequest.

        实例ID。 如果id以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的id精确匹配查询。

        :param id: The id of this ListInstancesRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListInstancesRequest.

        实例名称。 如果name以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的name精确匹配查询。

        :return: The name of this ListInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListInstancesRequest.

        实例名称。 如果name以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的name精确匹配查询。

        :param name: The name of this ListInstancesRequest.
        :type name: str
        """
        self._name = name

    @property
    def mode(self):
        """Gets the mode of this ListInstancesRequest.

        实例类型。   - 取值为“Cluster”，表示GaussDB(for Cassandra)、GaussDB(for Influx)、GaussDB(for Redis)集群实例类型。   - 取值为“Sharding”，表示GaussDB(for Mongo)集群实例类型。   - 取值为“ReplicaSet”，表示GaussDB(for Mongo)副本集实例类型。   - 取值为“InfluxdbCluster”，表示GaussDB(for Influx)集群实例类型。   - 取值为“InfluxdbSingle”，表示GaussDB(for Influx)单节点实例类型。   - 取值为“RedisReplica”，表示GaussDB(for Redis)性能版实例类型。   - 取值为“Replication”，表示GaussDB(for Redis)主备版实例类型。

        :return: The mode of this ListInstancesRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ListInstancesRequest.

        实例类型。   - 取值为“Cluster”，表示GaussDB(for Cassandra)、GaussDB(for Influx)、GaussDB(for Redis)集群实例类型。   - 取值为“Sharding”，表示GaussDB(for Mongo)集群实例类型。   - 取值为“ReplicaSet”，表示GaussDB(for Mongo)副本集实例类型。   - 取值为“InfluxdbCluster”，表示GaussDB(for Influx)集群实例类型。   - 取值为“InfluxdbSingle”，表示GaussDB(for Influx)单节点实例类型。   - 取值为“RedisReplica”，表示GaussDB(for Redis)性能版实例类型。   - 取值为“Replication”，表示GaussDB(for Redis)主备版实例类型。

        :param mode: The mode of this ListInstancesRequest.
        :type mode: str
        """
        self._mode = mode

    @property
    def datastore_type(self):
        """Gets the datastore_type of this ListInstancesRequest.

        数据库类型。   - 取值为“cassandra”，表示查询GaussDB(for Cassandra)数据库实例。   - 取值为“mongodb”，表示查询GaussDB(for Mongo)数据库实例。   - 取值为“influxdb”，表示查询GaussDB(for Influx)数据库实例。   - 取值为“redis”，表示查询GaussDB(for Redis)数据库实例。   - 如果不传该参数，表示查询所有数据库实例。

        :return: The datastore_type of this ListInstancesRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this ListInstancesRequest.

        数据库类型。   - 取值为“cassandra”，表示查询GaussDB(for Cassandra)数据库实例。   - 取值为“mongodb”，表示查询GaussDB(for Mongo)数据库实例。   - 取值为“influxdb”，表示查询GaussDB(for Influx)数据库实例。   - 取值为“redis”，表示查询GaussDB(for Redis)数据库实例。   - 如果不传该参数，表示查询所有数据库实例。

        :param datastore_type: The datastore_type of this ListInstancesRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListInstancesRequest.

        虚拟私有云ID，获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询VPC列表。

        :return: The vpc_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListInstancesRequest.

        虚拟私有云ID，获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询VPC列表。

        :param vpc_id: The vpc_id of this ListInstancesRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ListInstancesRequest.

        子网的网络ID，获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询子网列表。

        :return: The subnet_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ListInstancesRequest.

        子网的网络ID，获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询子网列表。

        :param subnet_id: The subnet_id of this ListInstancesRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def offset(self):
        """Gets the offset of this ListInstancesRequest.

        索引位置偏移量，表示从指定project ID下最新的实例创建时间开始，按时间的先后顺序偏移offset条数据后查询对应的实例信息。 取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从最新的实例创建时间对应的实例开始查询。

        :return: The offset of this ListInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListInstancesRequest.

        索引位置偏移量，表示从指定project ID下最新的实例创建时间开始，按时间的先后顺序偏移offset条数据后查询对应的实例信息。 取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从最新的实例创建时间对应的实例开始查询。

        :param offset: The offset of this ListInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListInstancesRequest.

        查询实例个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条实例信息。

        :return: The limit of this ListInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListInstancesRequest.

        查询实例个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条实例信息。

        :param limit: The limit of this ListInstancesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
