# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatastoreResult:

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
        """DatastoreResult

        The model defined in huaweicloud sdk

        :param type: 数据库类型。 - 支持GaussDB(for Cassandra)，GaussDB(for Mongo)，GaussDB(for Influx)数据库实例。 - 取值为“cassandra”，表示创建GaussDB(for Cassandra)数据库实例。 - 取值为“mongodb”，表示创建GaussDB(for Mongo)数据库实例。 - 取值为“influxdb”，表示创建GaussDB(for Influx)数据库实例。
        :type type: str
        :param version: 数据库版本。 - GaussDB(for Cassandra)实例支持3.11版本，取值为“3.11”。 - GaussDB(for Mongo)实例支持3.4，4.0版本，取值为\&quot;3.4\&quot;或\&quot;4.0\&quot;。 - GaussDB(for Influx)实例支持1.7版本，取值为“1.7”。
        :type version: str
        :param storage_engine: 存储引擎。 - GaussDB(for Cassandra)实例支持RocksDB存储引擎，取值为“rocksDB”。 - GaussDB(for Mongo)实例支持RocksDB存储引擎，取值为“rocksDB”。 - GaussDB(for Influx)实例支持RocksDB存储引擎，取值为“rocksDB”。
        :type storage_engine: str
        """
        
        

        self._type = None
        self._version = None
        self._storage_engine = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if storage_engine is not None:
            self.storage_engine = storage_engine

    @property
    def type(self):
        """Gets the type of this DatastoreResult.

        数据库类型。 - 支持GaussDB(for Cassandra)，GaussDB(for Mongo)，GaussDB(for Influx)数据库实例。 - 取值为“cassandra”，表示创建GaussDB(for Cassandra)数据库实例。 - 取值为“mongodb”，表示创建GaussDB(for Mongo)数据库实例。 - 取值为“influxdb”，表示创建GaussDB(for Influx)数据库实例。

        :return: The type of this DatastoreResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DatastoreResult.

        数据库类型。 - 支持GaussDB(for Cassandra)，GaussDB(for Mongo)，GaussDB(for Influx)数据库实例。 - 取值为“cassandra”，表示创建GaussDB(for Cassandra)数据库实例。 - 取值为“mongodb”，表示创建GaussDB(for Mongo)数据库实例。 - 取值为“influxdb”，表示创建GaussDB(for Influx)数据库实例。

        :param type: The type of this DatastoreResult.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this DatastoreResult.

        数据库版本。 - GaussDB(for Cassandra)实例支持3.11版本，取值为“3.11”。 - GaussDB(for Mongo)实例支持3.4，4.0版本，取值为\"3.4\"或\"4.0\"。 - GaussDB(for Influx)实例支持1.7版本，取值为“1.7”。

        :return: The version of this DatastoreResult.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DatastoreResult.

        数据库版本。 - GaussDB(for Cassandra)实例支持3.11版本，取值为“3.11”。 - GaussDB(for Mongo)实例支持3.4，4.0版本，取值为\"3.4\"或\"4.0\"。 - GaussDB(for Influx)实例支持1.7版本，取值为“1.7”。

        :param version: The version of this DatastoreResult.
        :type version: str
        """
        self._version = version

    @property
    def storage_engine(self):
        """Gets the storage_engine of this DatastoreResult.

        存储引擎。 - GaussDB(for Cassandra)实例支持RocksDB存储引擎，取值为“rocksDB”。 - GaussDB(for Mongo)实例支持RocksDB存储引擎，取值为“rocksDB”。 - GaussDB(for Influx)实例支持RocksDB存储引擎，取值为“rocksDB”。

        :return: The storage_engine of this DatastoreResult.
        :rtype: str
        """
        return self._storage_engine

    @storage_engine.setter
    def storage_engine(self, storage_engine):
        """Sets the storage_engine of this DatastoreResult.

        存储引擎。 - GaussDB(for Cassandra)实例支持RocksDB存储引擎，取值为“rocksDB”。 - GaussDB(for Mongo)实例支持RocksDB存储引擎，取值为“rocksDB”。 - GaussDB(for Influx)实例支持RocksDB存储引擎，取值为“rocksDB”。

        :param storage_engine: The storage_engine of this DatastoreResult.
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
        if not isinstance(other, DatastoreResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
