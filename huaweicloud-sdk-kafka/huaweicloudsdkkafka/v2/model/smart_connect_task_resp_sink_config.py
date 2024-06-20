# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartConnectTaskRespSinkConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'redis_address': 'str',
        'redis_type': 'str',
        'dcs_instance_id': 'str',
        'target_db': 'int',
        'consumer_strategy': 'str',
        'destination_file_type': 'str',
        'deliver_time_interval': 'int',
        'obs_bucket_name': 'str',
        'obs_path': 'str',
        'partition_format': 'str',
        'record_delimiter': 'str',
        'store_keys': 'bool',
        'obs_part_size': 'int',
        'flush_size': 'int',
        'timezone': 'str',
        'schema_generator_class': 'str',
        'partitioner_class': 'str',
        'value_converter': 'str',
        'key_converter': 'str',
        'kv_delimiter': 'str'
    }

    attribute_map = {
        'redis_address': 'redis_address',
        'redis_type': 'redis_type',
        'dcs_instance_id': 'dcs_instance_id',
        'target_db': 'target_db',
        'consumer_strategy': 'consumer_strategy',
        'destination_file_type': 'destination_file_type',
        'deliver_time_interval': 'deliver_time_interval',
        'obs_bucket_name': 'obs_bucket_name',
        'obs_path': 'obs_path',
        'partition_format': 'partition_format',
        'record_delimiter': 'record_delimiter',
        'store_keys': 'store_keys',
        'obs_part_size': 'obs_part_size',
        'flush_size': 'flush_size',
        'timezone': 'timezone',
        'schema_generator_class': 'schema_generator_class',
        'partitioner_class': 'partitioner_class',
        'value_converter': 'value_converter',
        'key_converter': 'key_converter',
        'kv_delimiter': 'kv_delimiter'
    }

    def __init__(self, redis_address=None, redis_type=None, dcs_instance_id=None, target_db=None, consumer_strategy=None, destination_file_type=None, deliver_time_interval=None, obs_bucket_name=None, obs_path=None, partition_format=None, record_delimiter=None, store_keys=None, obs_part_size=None, flush_size=None, timezone=None, schema_generator_class=None, partitioner_class=None, value_converter=None, key_converter=None, kv_delimiter=None):
        """SmartConnectTaskRespSinkConfig

        The model defined in huaweicloud sdk

        :param redis_address: Redis实例地址。（仅目标端类型为Redis时会显示）
        :type redis_address: str
        :param redis_type: Redis实例类型。（仅目标端类型为Redis时会显示）
        :type redis_type: str
        :param dcs_instance_id: DCS实例ID。（仅目标端类型为Redis时会显示）
        :type dcs_instance_id: str
        :param target_db: 目标数据库，默认为-1。（仅目标端类型为Redis时会显示）
        :type target_db: int
        :param consumer_strategy: 转储启动偏移量，latest为获取最新的数据，earliest为获取最早的数据。（仅目标端类型为OBS时会显示）
        :type consumer_strategy: str
        :param destination_file_type: 转储文件格式。当前只支持TEXT。（仅目标端类型为OBS时会显示）
        :type destination_file_type: str
        :param deliver_time_interval: 记数据转储周期（秒）。（仅目标端类型为OBS时会显示）
        :type deliver_time_interval: int
        :param obs_bucket_name: 转储地址。（仅目标端类型为OBS时会显示）
        :type obs_bucket_name: str
        :param obs_path: 转储目录。（仅目标端类型为OBS时会显示）
        :type obs_path: str
        :param partition_format: 时间目录格式。（仅目标端类型为OBS时会显示）
        :type partition_format: str
        :param record_delimiter: 记录分行符。（仅目标端类型为OBS时会显示）
        :type record_delimiter: str
        :param store_keys: 存储Key。（仅目标端类型为OBS时会显示）
        :type store_keys: bool
        :param obs_part_size: 每个传输文件多大后就开始上传，单位为byte；默认值5242880。（仅目标端类型为OBS时会显示）
        :type obs_part_size: int
        :param flush_size: flush_size。（仅目标端类型为OBS时会显示）
        :type flush_size: int
        :param timezone: 时区。（仅目标端类型为OBS时会显示）
        :type timezone: str
        :param schema_generator_class: schema_generator类，默认为\&quot;io.confluent.connect.storage.hive.schema.DefaultSchemaGenerator\&quot;。（仅目标端类型为OBS时会显示）
        :type schema_generator_class: str
        :param partitioner_class: partitioner类，默认\&quot;io.confluent.connect.storage.partitioner.TimeBasedPartitioner\&quot;。（仅目标端类型为OBS时会显示）
        :type partitioner_class: str
        :param value_converter: value_converter，默认为\&quot;org.apache.kafka.connect.converters.ByteArrayConverter\&quot;。（仅目标端类型为OBS时会显示）
        :type value_converter: str
        :param key_converter: key_converter，默认为\&quot;org.apache.kafka.connect.converters.ByteArrayConverter\&quot;。（仅目标端类型为OBS时会显示）
        :type key_converter: str
        :param kv_delimiter: kv_delimiter，默认为\&quot;:\&quot;。（仅目标端类型为OBS时会显示）
        :type kv_delimiter: str
        """
        
        

        self._redis_address = None
        self._redis_type = None
        self._dcs_instance_id = None
        self._target_db = None
        self._consumer_strategy = None
        self._destination_file_type = None
        self._deliver_time_interval = None
        self._obs_bucket_name = None
        self._obs_path = None
        self._partition_format = None
        self._record_delimiter = None
        self._store_keys = None
        self._obs_part_size = None
        self._flush_size = None
        self._timezone = None
        self._schema_generator_class = None
        self._partitioner_class = None
        self._value_converter = None
        self._key_converter = None
        self._kv_delimiter = None
        self.discriminator = None

        if redis_address is not None:
            self.redis_address = redis_address
        if redis_type is not None:
            self.redis_type = redis_type
        if dcs_instance_id is not None:
            self.dcs_instance_id = dcs_instance_id
        if target_db is not None:
            self.target_db = target_db
        if consumer_strategy is not None:
            self.consumer_strategy = consumer_strategy
        if destination_file_type is not None:
            self.destination_file_type = destination_file_type
        if deliver_time_interval is not None:
            self.deliver_time_interval = deliver_time_interval
        if obs_bucket_name is not None:
            self.obs_bucket_name = obs_bucket_name
        if obs_path is not None:
            self.obs_path = obs_path
        if partition_format is not None:
            self.partition_format = partition_format
        if record_delimiter is not None:
            self.record_delimiter = record_delimiter
        if store_keys is not None:
            self.store_keys = store_keys
        if obs_part_size is not None:
            self.obs_part_size = obs_part_size
        if flush_size is not None:
            self.flush_size = flush_size
        if timezone is not None:
            self.timezone = timezone
        if schema_generator_class is not None:
            self.schema_generator_class = schema_generator_class
        if partitioner_class is not None:
            self.partitioner_class = partitioner_class
        if value_converter is not None:
            self.value_converter = value_converter
        if key_converter is not None:
            self.key_converter = key_converter
        if kv_delimiter is not None:
            self.kv_delimiter = kv_delimiter

    @property
    def redis_address(self):
        """Gets the redis_address of this SmartConnectTaskRespSinkConfig.

        Redis实例地址。（仅目标端类型为Redis时会显示）

        :return: The redis_address of this SmartConnectTaskRespSinkConfig.
        :rtype: str
        """
        return self._redis_address

    @redis_address.setter
    def redis_address(self, redis_address):
        """Sets the redis_address of this SmartConnectTaskRespSinkConfig.

        Redis实例地址。（仅目标端类型为Redis时会显示）

        :param redis_address: The redis_address of this SmartConnectTaskRespSinkConfig.
        :type redis_address: str
        """
        self._redis_address = redis_address

    @property
    def redis_type(self):
        """Gets the redis_type of this SmartConnectTaskRespSinkConfig.

        Redis实例类型。（仅目标端类型为Redis时会显示）

        :return: The redis_type of this SmartConnectTaskRespSinkConfig.
        :rtype: str
        """
        return self._redis_type

    @redis_type.setter
    def redis_type(self, redis_type):
        """Sets the redis_type of this SmartConnectTaskRespSinkConfig.

        Redis实例类型。（仅目标端类型为Redis时会显示）

        :param redis_type: The redis_type of this SmartConnectTaskRespSinkConfig.
        :type redis_type: str
        """
        self._redis_type = redis_type

    @property
    def dcs_instance_id(self):
        """Gets the dcs_instance_id of this SmartConnectTaskRespSinkConfig.

        DCS实例ID。（仅目标端类型为Redis时会显示）

        :return: The dcs_instance_id of this SmartConnectTaskRespSinkConfig.
        :rtype: str
        """
        return self._dcs_instance_id

    @dcs_instance_id.setter
    def dcs_instance_id(self, dcs_instance_id):
        """Sets the dcs_instance_id of this SmartConnectTaskRespSinkConfig.

        DCS实例ID。（仅目标端类型为Redis时会显示）

        :param dcs_instance_id: The dcs_instance_id of this SmartConnectTaskRespSinkConfig.
        :type dcs_instance_id: str
        """
        self._dcs_instance_id = dcs_instance_id

    @property
    def target_db(self):
        """Gets the target_db of this SmartConnectTaskRespSinkConfig.

        目标数据库，默认为-1。（仅目标端类型为Redis时会显示）

        :return: The target_db of this SmartConnectTaskRespSinkConfig.
        :rtype: int
        """
        return self._target_db

    @target_db.setter
    def target_db(self, target_db):
        """Sets the target_db of this SmartConnectTaskRespSinkConfig.

        目标数据库，默认为-1。（仅目标端类型为Redis时会显示）

        :param target_db: The target_db of this SmartConnectTaskRespSinkConfig.
        :type target_db: int
        """
        self._target_db = target_db

    @property
    def consumer_strategy(self):
        """Gets the consumer_strategy of this SmartConnectTaskRespSinkConfig.

        转储启动偏移量，latest为获取最新的数据，earliest为获取最早的数据。（仅目标端类型为OBS时会显示）

        :return: The consumer_strategy of this SmartConnectTaskRespSinkConfig.
        :rtype: str
        """
        return self._consumer_strategy

    @consumer_strategy.setter
    def consumer_strategy(self, consumer_strategy):
        """Sets the consumer_strategy of this SmartConnectTaskRespSinkConfig.

        转储启动偏移量，latest为获取最新的数据，earliest为获取最早的数据。（仅目标端类型为OBS时会显示）

        :param consumer_strategy: The consumer_strategy of this SmartConnectTaskRespSinkConfig.
        :type consumer_strategy: str
        """
        self._consumer_strategy = consumer_strategy

    @property
    def destination_file_type(self):
        """Gets the destination_file_type of this SmartConnectTaskRespSinkConfig.

        转储文件格式。当前只支持TEXT。（仅目标端类型为OBS时会显示）

        :return: The destination_file_type of this SmartConnectTaskRespSinkConfig.
        :rtype: str
        """
        return self._destination_file_type

    @destination_file_type.setter
    def destination_file_type(self, destination_file_type):
        """Sets the destination_file_type of this SmartConnectTaskRespSinkConfig.

        转储文件格式。当前只支持TEXT。（仅目标端类型为OBS时会显示）

        :param destination_file_type: The destination_file_type of this SmartConnectTaskRespSinkConfig.
        :type destination_file_type: str
        """
        self._destination_file_type = destination_file_type

    @property
    def deliver_time_interval(self):
        """Gets the deliver_time_interval of this SmartConnectTaskRespSinkConfig.

        记数据转储周期（秒）。（仅目标端类型为OBS时会显示）

        :return: The deliver_time_interval of this SmartConnectTaskRespSinkConfig.
        :rtype: int
        """
        return self._deliver_time_interval

    @deliver_time_interval.setter
    def deliver_time_interval(self, deliver_time_interval):
        """Sets the deliver_time_interval of this SmartConnectTaskRespSinkConfig.

        记数据转储周期（秒）。（仅目标端类型为OBS时会显示）

        :param deliver_time_interval: The deliver_time_interval of this SmartConnectTaskRespSinkConfig.
        :type deliver_time_interval: int
        """
        self._deliver_time_interval = deliver_time_interval

    @property
    def obs_bucket_name(self):
        """Gets the obs_bucket_name of this SmartConnectTaskRespSinkConfig.

        转储地址。（仅目标端类型为OBS时会显示）

        :return: The obs_bucket_name of this SmartConnectTaskRespSinkConfig.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        """Sets the obs_bucket_name of this SmartConnectTaskRespSinkConfig.

        转储地址。（仅目标端类型为OBS时会显示）

        :param obs_bucket_name: The obs_bucket_name of this SmartConnectTaskRespSinkConfig.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def obs_path(self):
        """Gets the obs_path of this SmartConnectTaskRespSinkConfig.

        转储目录。（仅目标端类型为OBS时会显示）

        :return: The obs_path of this SmartConnectTaskRespSinkConfig.
        :rtype: str
        """
        return self._obs_path

    @obs_path.setter
    def obs_path(self, obs_path):
        """Sets the obs_path of this SmartConnectTaskRespSinkConfig.

        转储目录。（仅目标端类型为OBS时会显示）

        :param obs_path: The obs_path of this SmartConnectTaskRespSinkConfig.
        :type obs_path: str
        """
        self._obs_path = obs_path

    @property
    def partition_format(self):
        """Gets the partition_format of this SmartConnectTaskRespSinkConfig.

        时间目录格式。（仅目标端类型为OBS时会显示）

        :return: The partition_format of this SmartConnectTaskRespSinkConfig.
        :rtype: str
        """
        return self._partition_format

    @partition_format.setter
    def partition_format(self, partition_format):
        """Sets the partition_format of this SmartConnectTaskRespSinkConfig.

        时间目录格式。（仅目标端类型为OBS时会显示）

        :param partition_format: The partition_format of this SmartConnectTaskRespSinkConfig.
        :type partition_format: str
        """
        self._partition_format = partition_format

    @property
    def record_delimiter(self):
        """Gets the record_delimiter of this SmartConnectTaskRespSinkConfig.

        记录分行符。（仅目标端类型为OBS时会显示）

        :return: The record_delimiter of this SmartConnectTaskRespSinkConfig.
        :rtype: str
        """
        return self._record_delimiter

    @record_delimiter.setter
    def record_delimiter(self, record_delimiter):
        """Sets the record_delimiter of this SmartConnectTaskRespSinkConfig.

        记录分行符。（仅目标端类型为OBS时会显示）

        :param record_delimiter: The record_delimiter of this SmartConnectTaskRespSinkConfig.
        :type record_delimiter: str
        """
        self._record_delimiter = record_delimiter

    @property
    def store_keys(self):
        """Gets the store_keys of this SmartConnectTaskRespSinkConfig.

        存储Key。（仅目标端类型为OBS时会显示）

        :return: The store_keys of this SmartConnectTaskRespSinkConfig.
        :rtype: bool
        """
        return self._store_keys

    @store_keys.setter
    def store_keys(self, store_keys):
        """Sets the store_keys of this SmartConnectTaskRespSinkConfig.

        存储Key。（仅目标端类型为OBS时会显示）

        :param store_keys: The store_keys of this SmartConnectTaskRespSinkConfig.
        :type store_keys: bool
        """
        self._store_keys = store_keys

    @property
    def obs_part_size(self):
        """Gets the obs_part_size of this SmartConnectTaskRespSinkConfig.

        每个传输文件多大后就开始上传，单位为byte；默认值5242880。（仅目标端类型为OBS时会显示）

        :return: The obs_part_size of this SmartConnectTaskRespSinkConfig.
        :rtype: int
        """
        return self._obs_part_size

    @obs_part_size.setter
    def obs_part_size(self, obs_part_size):
        """Sets the obs_part_size of this SmartConnectTaskRespSinkConfig.

        每个传输文件多大后就开始上传，单位为byte；默认值5242880。（仅目标端类型为OBS时会显示）

        :param obs_part_size: The obs_part_size of this SmartConnectTaskRespSinkConfig.
        :type obs_part_size: int
        """
        self._obs_part_size = obs_part_size

    @property
    def flush_size(self):
        """Gets the flush_size of this SmartConnectTaskRespSinkConfig.

        flush_size。（仅目标端类型为OBS时会显示）

        :return: The flush_size of this SmartConnectTaskRespSinkConfig.
        :rtype: int
        """
        return self._flush_size

    @flush_size.setter
    def flush_size(self, flush_size):
        """Sets the flush_size of this SmartConnectTaskRespSinkConfig.

        flush_size。（仅目标端类型为OBS时会显示）

        :param flush_size: The flush_size of this SmartConnectTaskRespSinkConfig.
        :type flush_size: int
        """
        self._flush_size = flush_size

    @property
    def timezone(self):
        """Gets the timezone of this SmartConnectTaskRespSinkConfig.

        时区。（仅目标端类型为OBS时会显示）

        :return: The timezone of this SmartConnectTaskRespSinkConfig.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this SmartConnectTaskRespSinkConfig.

        时区。（仅目标端类型为OBS时会显示）

        :param timezone: The timezone of this SmartConnectTaskRespSinkConfig.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def schema_generator_class(self):
        """Gets the schema_generator_class of this SmartConnectTaskRespSinkConfig.

        schema_generator类，默认为\"io.confluent.connect.storage.hive.schema.DefaultSchemaGenerator\"。（仅目标端类型为OBS时会显示）

        :return: The schema_generator_class of this SmartConnectTaskRespSinkConfig.
        :rtype: str
        """
        return self._schema_generator_class

    @schema_generator_class.setter
    def schema_generator_class(self, schema_generator_class):
        """Sets the schema_generator_class of this SmartConnectTaskRespSinkConfig.

        schema_generator类，默认为\"io.confluent.connect.storage.hive.schema.DefaultSchemaGenerator\"。（仅目标端类型为OBS时会显示）

        :param schema_generator_class: The schema_generator_class of this SmartConnectTaskRespSinkConfig.
        :type schema_generator_class: str
        """
        self._schema_generator_class = schema_generator_class

    @property
    def partitioner_class(self):
        """Gets the partitioner_class of this SmartConnectTaskRespSinkConfig.

        partitioner类，默认\"io.confluent.connect.storage.partitioner.TimeBasedPartitioner\"。（仅目标端类型为OBS时会显示）

        :return: The partitioner_class of this SmartConnectTaskRespSinkConfig.
        :rtype: str
        """
        return self._partitioner_class

    @partitioner_class.setter
    def partitioner_class(self, partitioner_class):
        """Sets the partitioner_class of this SmartConnectTaskRespSinkConfig.

        partitioner类，默认\"io.confluent.connect.storage.partitioner.TimeBasedPartitioner\"。（仅目标端类型为OBS时会显示）

        :param partitioner_class: The partitioner_class of this SmartConnectTaskRespSinkConfig.
        :type partitioner_class: str
        """
        self._partitioner_class = partitioner_class

    @property
    def value_converter(self):
        """Gets the value_converter of this SmartConnectTaskRespSinkConfig.

        value_converter，默认为\"org.apache.kafka.connect.converters.ByteArrayConverter\"。（仅目标端类型为OBS时会显示）

        :return: The value_converter of this SmartConnectTaskRespSinkConfig.
        :rtype: str
        """
        return self._value_converter

    @value_converter.setter
    def value_converter(self, value_converter):
        """Sets the value_converter of this SmartConnectTaskRespSinkConfig.

        value_converter，默认为\"org.apache.kafka.connect.converters.ByteArrayConverter\"。（仅目标端类型为OBS时会显示）

        :param value_converter: The value_converter of this SmartConnectTaskRespSinkConfig.
        :type value_converter: str
        """
        self._value_converter = value_converter

    @property
    def key_converter(self):
        """Gets the key_converter of this SmartConnectTaskRespSinkConfig.

        key_converter，默认为\"org.apache.kafka.connect.converters.ByteArrayConverter\"。（仅目标端类型为OBS时会显示）

        :return: The key_converter of this SmartConnectTaskRespSinkConfig.
        :rtype: str
        """
        return self._key_converter

    @key_converter.setter
    def key_converter(self, key_converter):
        """Sets the key_converter of this SmartConnectTaskRespSinkConfig.

        key_converter，默认为\"org.apache.kafka.connect.converters.ByteArrayConverter\"。（仅目标端类型为OBS时会显示）

        :param key_converter: The key_converter of this SmartConnectTaskRespSinkConfig.
        :type key_converter: str
        """
        self._key_converter = key_converter

    @property
    def kv_delimiter(self):
        """Gets the kv_delimiter of this SmartConnectTaskRespSinkConfig.

        kv_delimiter，默认为\":\"。（仅目标端类型为OBS时会显示）

        :return: The kv_delimiter of this SmartConnectTaskRespSinkConfig.
        :rtype: str
        """
        return self._kv_delimiter

    @kv_delimiter.setter
    def kv_delimiter(self, kv_delimiter):
        """Sets the kv_delimiter of this SmartConnectTaskRespSinkConfig.

        kv_delimiter，默认为\":\"。（仅目标端类型为OBS时会显示）

        :param kv_delimiter: The kv_delimiter of this SmartConnectTaskRespSinkConfig.
        :type kv_delimiter: str
        """
        self._kv_delimiter = kv_delimiter

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
        if not isinstance(other, SmartConnectTaskRespSinkConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
