# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConfigurationDatastoreOption:

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
        'mode': 'str'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version',
        'mode': 'mode'
    }

    def __init__(self, type=None, version=None, mode=None):
        r"""CreateConfigurationDatastoreOption

        The model defined in huaweicloud sdk

        :param type: 数据库类型。 - GeminiDB Cassandra实例取值为“cassandra”。 - GeminiDB Mongo实例取值为\&quot;mongodb\&quot;。 - GeminiDB Influx实例取值为\&quot;influxdb\&quot;。 - GeminiDB Redis实例取值为\&quot;redis\&quot;。 - GeminiDB DynamoDB实例取值为\&quot;dynamodb\&quot;。 - GeminiDB HBase实例取值为\&quot;hbase\&quot;。
        :type type: str
        :param version: 数据库版本。 - GeminiDB Cassandra实例支持3.11版本，取值为“3.11”。 - GeminiDB Mongo实例支持4.0版本，取值为\&quot;4.0\&quot;。 - GeminiDB Influx实例支持1.8版本，取值\&quot;1.8\&quot;。 - GeminiDB Redis实例支持5.0版本，取值\&quot;5.0\&quot;。
        :type version: str
        :param mode: 数据库实例类型当创建支持GeminiDB Mongo、GeminiDB Cassandra云原生部署模式实例的参数模板， 该参数必选。 取值范围: *  GeminiDB Mongo 副本集实例取值为\&quot;ReplicaSet\&quot;。 *  GeminiDB Influx 单节点实例取值为\&quot;InfluxdbSingle\&quot;。 *  GeminiDB Cassandra云原生部署模式实例取值为\&quot;CloudNativeCluster\&quot;。 不传该参数，对GeminiDB Cassandra实例默认创建支持经典部署模式集群实例的参数模板。
        :type mode: str
        """
        
        

        self._type = None
        self._version = None
        self._mode = None
        self.discriminator = None

        self.type = type
        self.version = version
        if mode is not None:
            self.mode = mode

    @property
    def type(self):
        r"""Gets the type of this CreateConfigurationDatastoreOption.

        数据库类型。 - GeminiDB Cassandra实例取值为“cassandra”。 - GeminiDB Mongo实例取值为\"mongodb\"。 - GeminiDB Influx实例取值为\"influxdb\"。 - GeminiDB Redis实例取值为\"redis\"。 - GeminiDB DynamoDB实例取值为\"dynamodb\"。 - GeminiDB HBase实例取值为\"hbase\"。

        :return: The type of this CreateConfigurationDatastoreOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateConfigurationDatastoreOption.

        数据库类型。 - GeminiDB Cassandra实例取值为“cassandra”。 - GeminiDB Mongo实例取值为\"mongodb\"。 - GeminiDB Influx实例取值为\"influxdb\"。 - GeminiDB Redis实例取值为\"redis\"。 - GeminiDB DynamoDB实例取值为\"dynamodb\"。 - GeminiDB HBase实例取值为\"hbase\"。

        :param type: The type of this CreateConfigurationDatastoreOption.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this CreateConfigurationDatastoreOption.

        数据库版本。 - GeminiDB Cassandra实例支持3.11版本，取值为“3.11”。 - GeminiDB Mongo实例支持4.0版本，取值为\"4.0\"。 - GeminiDB Influx实例支持1.8版本，取值\"1.8\"。 - GeminiDB Redis实例支持5.0版本，取值\"5.0\"。

        :return: The version of this CreateConfigurationDatastoreOption.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateConfigurationDatastoreOption.

        数据库版本。 - GeminiDB Cassandra实例支持3.11版本，取值为“3.11”。 - GeminiDB Mongo实例支持4.0版本，取值为\"4.0\"。 - GeminiDB Influx实例支持1.8版本，取值\"1.8\"。 - GeminiDB Redis实例支持5.0版本，取值\"5.0\"。

        :param version: The version of this CreateConfigurationDatastoreOption.
        :type version: str
        """
        self._version = version

    @property
    def mode(self):
        r"""Gets the mode of this CreateConfigurationDatastoreOption.

        数据库实例类型当创建支持GeminiDB Mongo、GeminiDB Cassandra云原生部署模式实例的参数模板， 该参数必选。 取值范围: *  GeminiDB Mongo 副本集实例取值为\"ReplicaSet\"。 *  GeminiDB Influx 单节点实例取值为\"InfluxdbSingle\"。 *  GeminiDB Cassandra云原生部署模式实例取值为\"CloudNativeCluster\"。 不传该参数，对GeminiDB Cassandra实例默认创建支持经典部署模式集群实例的参数模板。

        :return: The mode of this CreateConfigurationDatastoreOption.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this CreateConfigurationDatastoreOption.

        数据库实例类型当创建支持GeminiDB Mongo、GeminiDB Cassandra云原生部署模式实例的参数模板， 该参数必选。 取值范围: *  GeminiDB Mongo 副本集实例取值为\"ReplicaSet\"。 *  GeminiDB Influx 单节点实例取值为\"InfluxdbSingle\"。 *  GeminiDB Cassandra云原生部署模式实例取值为\"CloudNativeCluster\"。 不传该参数，对GeminiDB Cassandra实例默认创建支持经典部署模式集群实例的参数模板。

        :param mode: The mode of this CreateConfigurationDatastoreOption.
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
        if not isinstance(other, CreateConfigurationDatastoreOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
