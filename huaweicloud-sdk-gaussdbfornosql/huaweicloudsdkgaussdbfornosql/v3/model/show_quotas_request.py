# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQuotasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_type': 'str',
        'mode': 'str',
        'product_type': 'str'
    }

    attribute_map = {
        'datastore_type': 'datastore_type',
        'mode': 'mode',
        'product_type': 'product_type'
    }

    def __init__(self, datastore_type=None, mode=None, product_type=None):
        r"""ShowQuotasRequest

        The model defined in huaweicloud sdk

        :param datastore_type: 数据库类型。 取值为“cassandra”，表示查询GeminiDB Cassandra数据库实例配额。 取值为“mongodb”，表示GeminiDB Mongo查询数据库实例配额。 取值为“influxdb”，表示查询GeminiDB Influx数据库实例配额。 取值为“redis”，表示查询GeminiDB Redis数据库实例配额。 如果不传该参数，表示查询所有数据库实例配额。
        :type datastore_type: str
        :param mode: 实例类型。   - 取值为“Cluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis Proxy经典部署模式集群实例类型。   - 取值为“CloudNativeCluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis云原生部署模式集群实例类型。   - 取值为“RedisCluster”，表示GeminiDB Redis Cluster经典部署模式集群实例类型。   - 取值为“Replication”，表示GeminiDB Redis经典部署模式主备实例类型。   - 取值为“InfluxdbSingle”，表示GeminiDB Influx经典部署模式单节点实例类型。   - 取值为“ReplicaSet”，表示GeminiDB Mongo副本集实例类型。   - 如果不传datastore_type参数，自动忽略该参数设置。
        :type mode: str
        :param product_type: 产品类型。   -  Capacity 容量型   -  Standard 标准型 当查询GeminiDB redis云原生部署模式集群类型配额必传此参数。
        :type product_type: str
        """
        
        

        self._datastore_type = None
        self._mode = None
        self._product_type = None
        self.discriminator = None

        if datastore_type is not None:
            self.datastore_type = datastore_type
        if mode is not None:
            self.mode = mode
        if product_type is not None:
            self.product_type = product_type

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ShowQuotasRequest.

        数据库类型。 取值为“cassandra”，表示查询GeminiDB Cassandra数据库实例配额。 取值为“mongodb”，表示GeminiDB Mongo查询数据库实例配额。 取值为“influxdb”，表示查询GeminiDB Influx数据库实例配额。 取值为“redis”，表示查询GeminiDB Redis数据库实例配额。 如果不传该参数，表示查询所有数据库实例配额。

        :return: The datastore_type of this ShowQuotasRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ShowQuotasRequest.

        数据库类型。 取值为“cassandra”，表示查询GeminiDB Cassandra数据库实例配额。 取值为“mongodb”，表示GeminiDB Mongo查询数据库实例配额。 取值为“influxdb”，表示查询GeminiDB Influx数据库实例配额。 取值为“redis”，表示查询GeminiDB Redis数据库实例配额。 如果不传该参数，表示查询所有数据库实例配额。

        :param datastore_type: The datastore_type of this ShowQuotasRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def mode(self):
        r"""Gets the mode of this ShowQuotasRequest.

        实例类型。   - 取值为“Cluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis Proxy经典部署模式集群实例类型。   - 取值为“CloudNativeCluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis云原生部署模式集群实例类型。   - 取值为“RedisCluster”，表示GeminiDB Redis Cluster经典部署模式集群实例类型。   - 取值为“Replication”，表示GeminiDB Redis经典部署模式主备实例类型。   - 取值为“InfluxdbSingle”，表示GeminiDB Influx经典部署模式单节点实例类型。   - 取值为“ReplicaSet”，表示GeminiDB Mongo副本集实例类型。   - 如果不传datastore_type参数，自动忽略该参数设置。

        :return: The mode of this ShowQuotasRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ShowQuotasRequest.

        实例类型。   - 取值为“Cluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis Proxy经典部署模式集群实例类型。   - 取值为“CloudNativeCluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis云原生部署模式集群实例类型。   - 取值为“RedisCluster”，表示GeminiDB Redis Cluster经典部署模式集群实例类型。   - 取值为“Replication”，表示GeminiDB Redis经典部署模式主备实例类型。   - 取值为“InfluxdbSingle”，表示GeminiDB Influx经典部署模式单节点实例类型。   - 取值为“ReplicaSet”，表示GeminiDB Mongo副本集实例类型。   - 如果不传datastore_type参数，自动忽略该参数设置。

        :param mode: The mode of this ShowQuotasRequest.
        :type mode: str
        """
        self._mode = mode

    @property
    def product_type(self):
        r"""Gets the product_type of this ShowQuotasRequest.

        产品类型。   -  Capacity 容量型   -  Standard 标准型 当查询GeminiDB redis云原生部署模式集群类型配额必传此参数。

        :return: The product_type of this ShowQuotasRequest.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        r"""Sets the product_type of this ShowQuotasRequest.

        产品类型。   -  Capacity 容量型   -  Standard 标准型 当查询GeminiDB redis云原生部署模式集群类型配额必传此参数。

        :param product_type: The product_type of this ShowQuotasRequest.
        :type product_type: str
        """
        self._product_type = product_type

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
        if not isinstance(other, ShowQuotasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
