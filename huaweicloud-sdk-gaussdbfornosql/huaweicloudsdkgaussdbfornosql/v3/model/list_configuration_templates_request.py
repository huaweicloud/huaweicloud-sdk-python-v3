# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigurationTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'datastore_name': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'datastore_name': 'datastore_name',
        'mode': 'mode'
    }

    def __init__(self, offset=None, limit=None, datastore_name=None, mode=None):
        r"""ListConfigurationTemplatesRequest

        The model defined in huaweicloud sdk

        :param offset: 索引位置，偏移量。   - 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。   - 取值必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询个数上限值。 - 取值范围: 1~100。 - 不传该参数时，默认查询前100条信息。
        :type limit: int
        :param datastore_name: 【参数解释】 数据库名称。 【约束限制】 不限制。 【取值范围】 cassandra：表示支持GeminiDB Cassandra实例。 redis：表示支持GeminiDB Redis实例。 influxdb：表示支持GeminiDB Influx实例。 mongodb： 表示支持GeminiDB Mongo实例。 【默认取值】 不传该参数，则表示查询所有数据库类型。
        :type datastore_name: str
        :param mode: 【参数解释】 数据库实例类型。 【约束限制】 不限制。 【取值范围】 * 取值为“CloudNativeCluster”, 表示查询支持GeminiDB Cassandra云原生部署模式实例的参数模板。 * 取值为“Cluster”, 表示查询GeminiDB Cassandra经典部署模式实例、GeminiDB Influx经典部署模式实例、GeminiDB Redis Proxy集群经典部署模式实例支持的参数模板。 * 取值为“Replication”, 表示查询支持GeminiDB Redis经典部署模式主备类型实例的参数组。 * 取值为“InfluxdbSingle”, 表示查询支持GeminiDB Influx经典部署模式单节点类型实例的参数组。 * 取值为“ReplicaSet”, 表示查询支持GeminiDB Mongo副本集类型实例的参数组。 * 取值为“All”， 表示查询所有部署模式的参数模板。 【默认取值】 不传该参数，则表示查询经典部署模式实例支持的参数组。
        :type mode: str
        """
        
        

        self._offset = None
        self._limit = None
        self._datastore_name = None
        self._mode = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if datastore_name is not None:
            self.datastore_name = datastore_name
        if mode is not None:
            self.mode = mode

    @property
    def offset(self):
        r"""Gets the offset of this ListConfigurationTemplatesRequest.

        索引位置，偏移量。   - 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。   - 取值必须为数字，不能为负数。

        :return: The offset of this ListConfigurationTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListConfigurationTemplatesRequest.

        索引位置，偏移量。   - 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。   - 取值必须为数字，不能为负数。

        :param offset: The offset of this ListConfigurationTemplatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListConfigurationTemplatesRequest.

        查询个数上限值。 - 取值范围: 1~100。 - 不传该参数时，默认查询前100条信息。

        :return: The limit of this ListConfigurationTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListConfigurationTemplatesRequest.

        查询个数上限值。 - 取值范围: 1~100。 - 不传该参数时，默认查询前100条信息。

        :param limit: The limit of this ListConfigurationTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def datastore_name(self):
        r"""Gets the datastore_name of this ListConfigurationTemplatesRequest.

        【参数解释】 数据库名称。 【约束限制】 不限制。 【取值范围】 cassandra：表示支持GeminiDB Cassandra实例。 redis：表示支持GeminiDB Redis实例。 influxdb：表示支持GeminiDB Influx实例。 mongodb： 表示支持GeminiDB Mongo实例。 【默认取值】 不传该参数，则表示查询所有数据库类型。

        :return: The datastore_name of this ListConfigurationTemplatesRequest.
        :rtype: str
        """
        return self._datastore_name

    @datastore_name.setter
    def datastore_name(self, datastore_name):
        r"""Sets the datastore_name of this ListConfigurationTemplatesRequest.

        【参数解释】 数据库名称。 【约束限制】 不限制。 【取值范围】 cassandra：表示支持GeminiDB Cassandra实例。 redis：表示支持GeminiDB Redis实例。 influxdb：表示支持GeminiDB Influx实例。 mongodb： 表示支持GeminiDB Mongo实例。 【默认取值】 不传该参数，则表示查询所有数据库类型。

        :param datastore_name: The datastore_name of this ListConfigurationTemplatesRequest.
        :type datastore_name: str
        """
        self._datastore_name = datastore_name

    @property
    def mode(self):
        r"""Gets the mode of this ListConfigurationTemplatesRequest.

        【参数解释】 数据库实例类型。 【约束限制】 不限制。 【取值范围】 * 取值为“CloudNativeCluster”, 表示查询支持GeminiDB Cassandra云原生部署模式实例的参数模板。 * 取值为“Cluster”, 表示查询GeminiDB Cassandra经典部署模式实例、GeminiDB Influx经典部署模式实例、GeminiDB Redis Proxy集群经典部署模式实例支持的参数模板。 * 取值为“Replication”, 表示查询支持GeminiDB Redis经典部署模式主备类型实例的参数组。 * 取值为“InfluxdbSingle”, 表示查询支持GeminiDB Influx经典部署模式单节点类型实例的参数组。 * 取值为“ReplicaSet”, 表示查询支持GeminiDB Mongo副本集类型实例的参数组。 * 取值为“All”， 表示查询所有部署模式的参数模板。 【默认取值】 不传该参数，则表示查询经典部署模式实例支持的参数组。

        :return: The mode of this ListConfigurationTemplatesRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ListConfigurationTemplatesRequest.

        【参数解释】 数据库实例类型。 【约束限制】 不限制。 【取值范围】 * 取值为“CloudNativeCluster”, 表示查询支持GeminiDB Cassandra云原生部署模式实例的参数模板。 * 取值为“Cluster”, 表示查询GeminiDB Cassandra经典部署模式实例、GeminiDB Influx经典部署模式实例、GeminiDB Redis Proxy集群经典部署模式实例支持的参数模板。 * 取值为“Replication”, 表示查询支持GeminiDB Redis经典部署模式主备类型实例的参数组。 * 取值为“InfluxdbSingle”, 表示查询支持GeminiDB Influx经典部署模式单节点类型实例的参数组。 * 取值为“ReplicaSet”, 表示查询支持GeminiDB Mongo副本集类型实例的参数组。 * 取值为“All”， 表示查询所有部署模式的参数模板。 【默认取值】 不传该参数，则表示查询经典部署模式实例支持的参数组。

        :param mode: The mode of this ListConfigurationTemplatesRequest.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, ListConfigurationTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
