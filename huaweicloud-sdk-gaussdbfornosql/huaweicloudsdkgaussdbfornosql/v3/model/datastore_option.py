# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatastoreOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'version': 'str',
        'storage_engine': 'str'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version',
        'storage_engine': 'storage_engine'
    }

    def __init__(self, type=None, version=None, storage_engine=None):
        r"""DatastoreOption

        The model defined in huaweicloud sdk

        :param type: 数据库类型。 - 支持GeminiDB Cassandra，GeminiDB Mongo，GeminiDB Influx数据库实例。 - 取值为“cassandra”，表示创建GeminiDB Cassandra数据库实例。 - 取值为“mongodb”，表示创建GeminiDB Mongo数据库实例。 - 取值为“influxdb”，表示创建GeminiDB Influx数据库实例。 - 取值为“redis”，表示创建GeminiDB Redis数据库实例。 - 取值为“dynamodb”，表示创建GeminiDB DynamoDB数据库实例。 - 取值为“hbase”，表示创建GeminiDB HBase数据库实例。
        :type type: str
        :param version: 数据库版本。 - GeminiDB Cassandra实例支持3.11版本，取值为“3.11”。 - GeminiDB Mongo实例支持4.0版本，取值为4.0\&quot;。 - GeminiDB Influ经典部署模式集群类型实例支持1.8版本，取值为“1.8”。 - GeminiDB Influx云原生部署模式集群类型实例支持1.7版本，取值为“1.7”。 - GeminiDB Redis实例支持5.0版本，取值为“5.0”。 - GeminiDB DynamoDB实例取值为“”。 - GeminiDB HBase实例取值为“”。
        :type version: str
        :param storage_engine: 存储引擎。 - GeminiDB Cassandra实例支持RocksDB存储引擎，取值为“rocksDB”。 - GeminiDB Mongo实例支持RocksDB存储引擎，取值为“rocksDB”。 - GeminiDB Influx实例支持RocksDB存储引擎，取值为“rocksDB”。 - GeminiDB Redis实例支持RocksDB存储引擎，取值为“rocksDB”。
        :type storage_engine: str
        """
        
        

        self._type = None
        self._version = None
        self._storage_engine = None
        self.discriminator = None

        self.type = type
        self.version = version
        self.storage_engine = storage_engine

    @property
    def type(self):
        r"""Gets the type of this DatastoreOption.

        数据库类型。 - 支持GeminiDB Cassandra，GeminiDB Mongo，GeminiDB Influx数据库实例。 - 取值为“cassandra”，表示创建GeminiDB Cassandra数据库实例。 - 取值为“mongodb”，表示创建GeminiDB Mongo数据库实例。 - 取值为“influxdb”，表示创建GeminiDB Influx数据库实例。 - 取值为“redis”，表示创建GeminiDB Redis数据库实例。 - 取值为“dynamodb”，表示创建GeminiDB DynamoDB数据库实例。 - 取值为“hbase”，表示创建GeminiDB HBase数据库实例。

        :return: The type of this DatastoreOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DatastoreOption.

        数据库类型。 - 支持GeminiDB Cassandra，GeminiDB Mongo，GeminiDB Influx数据库实例。 - 取值为“cassandra”，表示创建GeminiDB Cassandra数据库实例。 - 取值为“mongodb”，表示创建GeminiDB Mongo数据库实例。 - 取值为“influxdb”，表示创建GeminiDB Influx数据库实例。 - 取值为“redis”，表示创建GeminiDB Redis数据库实例。 - 取值为“dynamodb”，表示创建GeminiDB DynamoDB数据库实例。 - 取值为“hbase”，表示创建GeminiDB HBase数据库实例。

        :param type: The type of this DatastoreOption.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this DatastoreOption.

        数据库版本。 - GeminiDB Cassandra实例支持3.11版本，取值为“3.11”。 - GeminiDB Mongo实例支持4.0版本，取值为4.0\"。 - GeminiDB Influ经典部署模式集群类型实例支持1.8版本，取值为“1.8”。 - GeminiDB Influx云原生部署模式集群类型实例支持1.7版本，取值为“1.7”。 - GeminiDB Redis实例支持5.0版本，取值为“5.0”。 - GeminiDB DynamoDB实例取值为“”。 - GeminiDB HBase实例取值为“”。

        :return: The version of this DatastoreOption.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this DatastoreOption.

        数据库版本。 - GeminiDB Cassandra实例支持3.11版本，取值为“3.11”。 - GeminiDB Mongo实例支持4.0版本，取值为4.0\"。 - GeminiDB Influ经典部署模式集群类型实例支持1.8版本，取值为“1.8”。 - GeminiDB Influx云原生部署模式集群类型实例支持1.7版本，取值为“1.7”。 - GeminiDB Redis实例支持5.0版本，取值为“5.0”。 - GeminiDB DynamoDB实例取值为“”。 - GeminiDB HBase实例取值为“”。

        :param version: The version of this DatastoreOption.
        :type version: str
        """
        self._version = version

    @property
    def storage_engine(self):
        r"""Gets the storage_engine of this DatastoreOption.

        存储引擎。 - GeminiDB Cassandra实例支持RocksDB存储引擎，取值为“rocksDB”。 - GeminiDB Mongo实例支持RocksDB存储引擎，取值为“rocksDB”。 - GeminiDB Influx实例支持RocksDB存储引擎，取值为“rocksDB”。 - GeminiDB Redis实例支持RocksDB存储引擎，取值为“rocksDB”。

        :return: The storage_engine of this DatastoreOption.
        :rtype: str
        """
        return self._storage_engine

    @storage_engine.setter
    def storage_engine(self, storage_engine):
        r"""Sets the storage_engine of this DatastoreOption.

        存储引擎。 - GeminiDB Cassandra实例支持RocksDB存储引擎，取值为“rocksDB”。 - GeminiDB Mongo实例支持RocksDB存储引擎，取值为“rocksDB”。 - GeminiDB Influx实例支持RocksDB存储引擎，取值为“rocksDB”。 - GeminiDB Redis实例支持RocksDB存储引擎，取值为“rocksDB”。

        :param storage_engine: The storage_engine of this DatastoreOption.
        :type storage_engine: str
        """
        self._storage_engine = storage_engine

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
        if not isinstance(other, DatastoreOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
