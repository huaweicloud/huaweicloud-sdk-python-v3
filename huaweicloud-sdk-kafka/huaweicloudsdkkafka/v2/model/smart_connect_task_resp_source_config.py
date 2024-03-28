# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartConnectTaskRespSourceConfig:

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
        'sync_mode': 'str',
        'full_sync_wait_ms': 'int',
        'full_sync_max_retry': 'int',
        'ratelimit': 'int',
        'current_cluster_name': 'str',
        'cluster_name': 'str',
        'user_name': 'str',
        'sasl_mechanism': 'str',
        'instance_id': 'str',
        'bootstrap_servers': 'str',
        'security_protocol': 'str',
        'direction': 'str',
        'sync_consumer_offsets_enabled': 'bool',
        'replication_factor': 'int',
        'task_num': 'int',
        'rename_topic_enabled': 'bool',
        'provenance_header_enabled': 'bool',
        'consumer_strategy': 'str',
        'compression_type': 'str',
        'topics_mapping': 'str'
    }

    attribute_map = {
        'redis_address': 'redis_address',
        'redis_type': 'redis_type',
        'dcs_instance_id': 'dcs_instance_id',
        'sync_mode': 'sync_mode',
        'full_sync_wait_ms': 'full_sync_wait_ms',
        'full_sync_max_retry': 'full_sync_max_retry',
        'ratelimit': 'ratelimit',
        'current_cluster_name': 'current_cluster_name',
        'cluster_name': 'cluster_name',
        'user_name': 'user_name',
        'sasl_mechanism': 'sasl_mechanism',
        'instance_id': 'instance_id',
        'bootstrap_servers': 'bootstrap_servers',
        'security_protocol': 'security_protocol',
        'direction': 'direction',
        'sync_consumer_offsets_enabled': 'sync_consumer_offsets_enabled',
        'replication_factor': 'replication_factor',
        'task_num': 'task_num',
        'rename_topic_enabled': 'rename_topic_enabled',
        'provenance_header_enabled': 'provenance_header_enabled',
        'consumer_strategy': 'consumer_strategy',
        'compression_type': 'compression_type',
        'topics_mapping': 'topics_mapping'
    }

    def __init__(self, redis_address=None, redis_type=None, dcs_instance_id=None, sync_mode=None, full_sync_wait_ms=None, full_sync_max_retry=None, ratelimit=None, current_cluster_name=None, cluster_name=None, user_name=None, sasl_mechanism=None, instance_id=None, bootstrap_servers=None, security_protocol=None, direction=None, sync_consumer_offsets_enabled=None, replication_factor=None, task_num=None, rename_topic_enabled=None, provenance_header_enabled=None, consumer_strategy=None, compression_type=None, topics_mapping=None):
        """SmartConnectTaskRespSourceConfig

        The model defined in huaweicloud sdk

        :param redis_address: Redis实例地址。（仅源端类型为Redis时会显示）
        :type redis_address: str
        :param redis_type: Redis实例类型。（仅源端类型为Redis时会显示）
        :type redis_type: str
        :param dcs_instance_id: DCS实例ID。（仅源端类型为Redis时会显示）
        :type dcs_instance_id: str
        :param sync_mode: 同步类型，“RDB_ONLY”为全量同步，“CUSTOM_OFFSET”为全量同步+增量同步。（仅源端类型为Redis时会显示）
        :type sync_mode: str
        :param full_sync_wait_ms: 全量同步重试间隔时间，单位：毫秒。（仅源端类型为Redis时会显示）
        :type full_sync_wait_ms: int
        :param full_sync_max_retry: 全量同步最大重试次数。（仅源端类型为Redis时会显示）
        :type full_sync_max_retry: int
        :param ratelimit: 限速，单位为KB/s。-1表示不限速（仅源端类型为Redis时会显示）
        :type ratelimit: int
        :param current_cluster_name: 当前Kafka实例别名。（仅源端类型为Kafka时会显示）
        :type current_cluster_name: str
        :param cluster_name: 对端Kafka实例别名。（仅源端类型为Kafka时会显示）
        :type cluster_name: str
        :param user_name: 对端Kafka用户名。（仅源端类型为Kafka时会显示）
        :type user_name: str
        :param sasl_mechanism: 对端Kafka认证机制。（仅源端类型为Kafka时会显示）
        :type sasl_mechanism: str
        :param instance_id: 对端Kafka实例ID。（仅源端类型为Kafka时会显示）
        :type instance_id: str
        :param bootstrap_servers: 对端Kafka实例地址。（仅源端类型为Kafka时会显示）
        :type bootstrap_servers: str
        :param security_protocol: 对端Kafka认证方式。（仅源端类型为Kafka时会显示）
        :type security_protocol: str
        :param direction: 同步方向。（仅源端类型为Kafka时会显示）
        :type direction: str
        :param sync_consumer_offsets_enabled: 是否同步消费进度。（仅源端类型为Kafka时会显示）
        :type sync_consumer_offsets_enabled: bool
        :param replication_factor: 副本数。（仅源端类型为Kafka时会显示）
        :type replication_factor: int
        :param task_num: 任务数。（仅源端类型为Kafka时会显示）
        :type task_num: int
        :param rename_topic_enabled: 是否重命名Topic。（仅源端类型为Kafka时会显示）
        :type rename_topic_enabled: bool
        :param provenance_header_enabled: 是否添加来源header。（仅源端类型为Kafka时会显示）
        :type provenance_header_enabled: bool
        :param consumer_strategy: 启动偏移量，latest为获取最新的数据，earliest为获取最早的数据。（仅源端类型为Kafka时会显示）
        :type consumer_strategy: str
        :param compression_type: 压缩算法。（仅源端类型为Kafka时会显示）
        :type compression_type: str
        :param topics_mapping: topic映射。（仅源端类型为Kafka时会显示）
        :type topics_mapping: str
        """
        
        

        self._redis_address = None
        self._redis_type = None
        self._dcs_instance_id = None
        self._sync_mode = None
        self._full_sync_wait_ms = None
        self._full_sync_max_retry = None
        self._ratelimit = None
        self._current_cluster_name = None
        self._cluster_name = None
        self._user_name = None
        self._sasl_mechanism = None
        self._instance_id = None
        self._bootstrap_servers = None
        self._security_protocol = None
        self._direction = None
        self._sync_consumer_offsets_enabled = None
        self._replication_factor = None
        self._task_num = None
        self._rename_topic_enabled = None
        self._provenance_header_enabled = None
        self._consumer_strategy = None
        self._compression_type = None
        self._topics_mapping = None
        self.discriminator = None

        if redis_address is not None:
            self.redis_address = redis_address
        if redis_type is not None:
            self.redis_type = redis_type
        if dcs_instance_id is not None:
            self.dcs_instance_id = dcs_instance_id
        if sync_mode is not None:
            self.sync_mode = sync_mode
        if full_sync_wait_ms is not None:
            self.full_sync_wait_ms = full_sync_wait_ms
        if full_sync_max_retry is not None:
            self.full_sync_max_retry = full_sync_max_retry
        if ratelimit is not None:
            self.ratelimit = ratelimit
        if current_cluster_name is not None:
            self.current_cluster_name = current_cluster_name
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if user_name is not None:
            self.user_name = user_name
        if sasl_mechanism is not None:
            self.sasl_mechanism = sasl_mechanism
        if instance_id is not None:
            self.instance_id = instance_id
        if bootstrap_servers is not None:
            self.bootstrap_servers = bootstrap_servers
        if security_protocol is not None:
            self.security_protocol = security_protocol
        if direction is not None:
            self.direction = direction
        if sync_consumer_offsets_enabled is not None:
            self.sync_consumer_offsets_enabled = sync_consumer_offsets_enabled
        if replication_factor is not None:
            self.replication_factor = replication_factor
        if task_num is not None:
            self.task_num = task_num
        if rename_topic_enabled is not None:
            self.rename_topic_enabled = rename_topic_enabled
        if provenance_header_enabled is not None:
            self.provenance_header_enabled = provenance_header_enabled
        if consumer_strategy is not None:
            self.consumer_strategy = consumer_strategy
        if compression_type is not None:
            self.compression_type = compression_type
        if topics_mapping is not None:
            self.topics_mapping = topics_mapping

    @property
    def redis_address(self):
        """Gets the redis_address of this SmartConnectTaskRespSourceConfig.

        Redis实例地址。（仅源端类型为Redis时会显示）

        :return: The redis_address of this SmartConnectTaskRespSourceConfig.
        :rtype: str
        """
        return self._redis_address

    @redis_address.setter
    def redis_address(self, redis_address):
        """Sets the redis_address of this SmartConnectTaskRespSourceConfig.

        Redis实例地址。（仅源端类型为Redis时会显示）

        :param redis_address: The redis_address of this SmartConnectTaskRespSourceConfig.
        :type redis_address: str
        """
        self._redis_address = redis_address

    @property
    def redis_type(self):
        """Gets the redis_type of this SmartConnectTaskRespSourceConfig.

        Redis实例类型。（仅源端类型为Redis时会显示）

        :return: The redis_type of this SmartConnectTaskRespSourceConfig.
        :rtype: str
        """
        return self._redis_type

    @redis_type.setter
    def redis_type(self, redis_type):
        """Sets the redis_type of this SmartConnectTaskRespSourceConfig.

        Redis实例类型。（仅源端类型为Redis时会显示）

        :param redis_type: The redis_type of this SmartConnectTaskRespSourceConfig.
        :type redis_type: str
        """
        self._redis_type = redis_type

    @property
    def dcs_instance_id(self):
        """Gets the dcs_instance_id of this SmartConnectTaskRespSourceConfig.

        DCS实例ID。（仅源端类型为Redis时会显示）

        :return: The dcs_instance_id of this SmartConnectTaskRespSourceConfig.
        :rtype: str
        """
        return self._dcs_instance_id

    @dcs_instance_id.setter
    def dcs_instance_id(self, dcs_instance_id):
        """Sets the dcs_instance_id of this SmartConnectTaskRespSourceConfig.

        DCS实例ID。（仅源端类型为Redis时会显示）

        :param dcs_instance_id: The dcs_instance_id of this SmartConnectTaskRespSourceConfig.
        :type dcs_instance_id: str
        """
        self._dcs_instance_id = dcs_instance_id

    @property
    def sync_mode(self):
        """Gets the sync_mode of this SmartConnectTaskRespSourceConfig.

        同步类型，“RDB_ONLY”为全量同步，“CUSTOM_OFFSET”为全量同步+增量同步。（仅源端类型为Redis时会显示）

        :return: The sync_mode of this SmartConnectTaskRespSourceConfig.
        :rtype: str
        """
        return self._sync_mode

    @sync_mode.setter
    def sync_mode(self, sync_mode):
        """Sets the sync_mode of this SmartConnectTaskRespSourceConfig.

        同步类型，“RDB_ONLY”为全量同步，“CUSTOM_OFFSET”为全量同步+增量同步。（仅源端类型为Redis时会显示）

        :param sync_mode: The sync_mode of this SmartConnectTaskRespSourceConfig.
        :type sync_mode: str
        """
        self._sync_mode = sync_mode

    @property
    def full_sync_wait_ms(self):
        """Gets the full_sync_wait_ms of this SmartConnectTaskRespSourceConfig.

        全量同步重试间隔时间，单位：毫秒。（仅源端类型为Redis时会显示）

        :return: The full_sync_wait_ms of this SmartConnectTaskRespSourceConfig.
        :rtype: int
        """
        return self._full_sync_wait_ms

    @full_sync_wait_ms.setter
    def full_sync_wait_ms(self, full_sync_wait_ms):
        """Sets the full_sync_wait_ms of this SmartConnectTaskRespSourceConfig.

        全量同步重试间隔时间，单位：毫秒。（仅源端类型为Redis时会显示）

        :param full_sync_wait_ms: The full_sync_wait_ms of this SmartConnectTaskRespSourceConfig.
        :type full_sync_wait_ms: int
        """
        self._full_sync_wait_ms = full_sync_wait_ms

    @property
    def full_sync_max_retry(self):
        """Gets the full_sync_max_retry of this SmartConnectTaskRespSourceConfig.

        全量同步最大重试次数。（仅源端类型为Redis时会显示）

        :return: The full_sync_max_retry of this SmartConnectTaskRespSourceConfig.
        :rtype: int
        """
        return self._full_sync_max_retry

    @full_sync_max_retry.setter
    def full_sync_max_retry(self, full_sync_max_retry):
        """Sets the full_sync_max_retry of this SmartConnectTaskRespSourceConfig.

        全量同步最大重试次数。（仅源端类型为Redis时会显示）

        :param full_sync_max_retry: The full_sync_max_retry of this SmartConnectTaskRespSourceConfig.
        :type full_sync_max_retry: int
        """
        self._full_sync_max_retry = full_sync_max_retry

    @property
    def ratelimit(self):
        """Gets the ratelimit of this SmartConnectTaskRespSourceConfig.

        限速，单位为KB/s。-1表示不限速（仅源端类型为Redis时会显示）

        :return: The ratelimit of this SmartConnectTaskRespSourceConfig.
        :rtype: int
        """
        return self._ratelimit

    @ratelimit.setter
    def ratelimit(self, ratelimit):
        """Sets the ratelimit of this SmartConnectTaskRespSourceConfig.

        限速，单位为KB/s。-1表示不限速（仅源端类型为Redis时会显示）

        :param ratelimit: The ratelimit of this SmartConnectTaskRespSourceConfig.
        :type ratelimit: int
        """
        self._ratelimit = ratelimit

    @property
    def current_cluster_name(self):
        """Gets the current_cluster_name of this SmartConnectTaskRespSourceConfig.

        当前Kafka实例别名。（仅源端类型为Kafka时会显示）

        :return: The current_cluster_name of this SmartConnectTaskRespSourceConfig.
        :rtype: str
        """
        return self._current_cluster_name

    @current_cluster_name.setter
    def current_cluster_name(self, current_cluster_name):
        """Sets the current_cluster_name of this SmartConnectTaskRespSourceConfig.

        当前Kafka实例别名。（仅源端类型为Kafka时会显示）

        :param current_cluster_name: The current_cluster_name of this SmartConnectTaskRespSourceConfig.
        :type current_cluster_name: str
        """
        self._current_cluster_name = current_cluster_name

    @property
    def cluster_name(self):
        """Gets the cluster_name of this SmartConnectTaskRespSourceConfig.

        对端Kafka实例别名。（仅源端类型为Kafka时会显示）

        :return: The cluster_name of this SmartConnectTaskRespSourceConfig.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this SmartConnectTaskRespSourceConfig.

        对端Kafka实例别名。（仅源端类型为Kafka时会显示）

        :param cluster_name: The cluster_name of this SmartConnectTaskRespSourceConfig.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def user_name(self):
        """Gets the user_name of this SmartConnectTaskRespSourceConfig.

        对端Kafka用户名。（仅源端类型为Kafka时会显示）

        :return: The user_name of this SmartConnectTaskRespSourceConfig.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this SmartConnectTaskRespSourceConfig.

        对端Kafka用户名。（仅源端类型为Kafka时会显示）

        :param user_name: The user_name of this SmartConnectTaskRespSourceConfig.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def sasl_mechanism(self):
        """Gets the sasl_mechanism of this SmartConnectTaskRespSourceConfig.

        对端Kafka认证机制。（仅源端类型为Kafka时会显示）

        :return: The sasl_mechanism of this SmartConnectTaskRespSourceConfig.
        :rtype: str
        """
        return self._sasl_mechanism

    @sasl_mechanism.setter
    def sasl_mechanism(self, sasl_mechanism):
        """Sets the sasl_mechanism of this SmartConnectTaskRespSourceConfig.

        对端Kafka认证机制。（仅源端类型为Kafka时会显示）

        :param sasl_mechanism: The sasl_mechanism of this SmartConnectTaskRespSourceConfig.
        :type sasl_mechanism: str
        """
        self._sasl_mechanism = sasl_mechanism

    @property
    def instance_id(self):
        """Gets the instance_id of this SmartConnectTaskRespSourceConfig.

        对端Kafka实例ID。（仅源端类型为Kafka时会显示）

        :return: The instance_id of this SmartConnectTaskRespSourceConfig.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this SmartConnectTaskRespSourceConfig.

        对端Kafka实例ID。（仅源端类型为Kafka时会显示）

        :param instance_id: The instance_id of this SmartConnectTaskRespSourceConfig.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def bootstrap_servers(self):
        """Gets the bootstrap_servers of this SmartConnectTaskRespSourceConfig.

        对端Kafka实例地址。（仅源端类型为Kafka时会显示）

        :return: The bootstrap_servers of this SmartConnectTaskRespSourceConfig.
        :rtype: str
        """
        return self._bootstrap_servers

    @bootstrap_servers.setter
    def bootstrap_servers(self, bootstrap_servers):
        """Sets the bootstrap_servers of this SmartConnectTaskRespSourceConfig.

        对端Kafka实例地址。（仅源端类型为Kafka时会显示）

        :param bootstrap_servers: The bootstrap_servers of this SmartConnectTaskRespSourceConfig.
        :type bootstrap_servers: str
        """
        self._bootstrap_servers = bootstrap_servers

    @property
    def security_protocol(self):
        """Gets the security_protocol of this SmartConnectTaskRespSourceConfig.

        对端Kafka认证方式。（仅源端类型为Kafka时会显示）

        :return: The security_protocol of this SmartConnectTaskRespSourceConfig.
        :rtype: str
        """
        return self._security_protocol

    @security_protocol.setter
    def security_protocol(self, security_protocol):
        """Sets the security_protocol of this SmartConnectTaskRespSourceConfig.

        对端Kafka认证方式。（仅源端类型为Kafka时会显示）

        :param security_protocol: The security_protocol of this SmartConnectTaskRespSourceConfig.
        :type security_protocol: str
        """
        self._security_protocol = security_protocol

    @property
    def direction(self):
        """Gets the direction of this SmartConnectTaskRespSourceConfig.

        同步方向。（仅源端类型为Kafka时会显示）

        :return: The direction of this SmartConnectTaskRespSourceConfig.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this SmartConnectTaskRespSourceConfig.

        同步方向。（仅源端类型为Kafka时会显示）

        :param direction: The direction of this SmartConnectTaskRespSourceConfig.
        :type direction: str
        """
        self._direction = direction

    @property
    def sync_consumer_offsets_enabled(self):
        """Gets the sync_consumer_offsets_enabled of this SmartConnectTaskRespSourceConfig.

        是否同步消费进度。（仅源端类型为Kafka时会显示）

        :return: The sync_consumer_offsets_enabled of this SmartConnectTaskRespSourceConfig.
        :rtype: bool
        """
        return self._sync_consumer_offsets_enabled

    @sync_consumer_offsets_enabled.setter
    def sync_consumer_offsets_enabled(self, sync_consumer_offsets_enabled):
        """Sets the sync_consumer_offsets_enabled of this SmartConnectTaskRespSourceConfig.

        是否同步消费进度。（仅源端类型为Kafka时会显示）

        :param sync_consumer_offsets_enabled: The sync_consumer_offsets_enabled of this SmartConnectTaskRespSourceConfig.
        :type sync_consumer_offsets_enabled: bool
        """
        self._sync_consumer_offsets_enabled = sync_consumer_offsets_enabled

    @property
    def replication_factor(self):
        """Gets the replication_factor of this SmartConnectTaskRespSourceConfig.

        副本数。（仅源端类型为Kafka时会显示）

        :return: The replication_factor of this SmartConnectTaskRespSourceConfig.
        :rtype: int
        """
        return self._replication_factor

    @replication_factor.setter
    def replication_factor(self, replication_factor):
        """Sets the replication_factor of this SmartConnectTaskRespSourceConfig.

        副本数。（仅源端类型为Kafka时会显示）

        :param replication_factor: The replication_factor of this SmartConnectTaskRespSourceConfig.
        :type replication_factor: int
        """
        self._replication_factor = replication_factor

    @property
    def task_num(self):
        """Gets the task_num of this SmartConnectTaskRespSourceConfig.

        任务数。（仅源端类型为Kafka时会显示）

        :return: The task_num of this SmartConnectTaskRespSourceConfig.
        :rtype: int
        """
        return self._task_num

    @task_num.setter
    def task_num(self, task_num):
        """Sets the task_num of this SmartConnectTaskRespSourceConfig.

        任务数。（仅源端类型为Kafka时会显示）

        :param task_num: The task_num of this SmartConnectTaskRespSourceConfig.
        :type task_num: int
        """
        self._task_num = task_num

    @property
    def rename_topic_enabled(self):
        """Gets the rename_topic_enabled of this SmartConnectTaskRespSourceConfig.

        是否重命名Topic。（仅源端类型为Kafka时会显示）

        :return: The rename_topic_enabled of this SmartConnectTaskRespSourceConfig.
        :rtype: bool
        """
        return self._rename_topic_enabled

    @rename_topic_enabled.setter
    def rename_topic_enabled(self, rename_topic_enabled):
        """Sets the rename_topic_enabled of this SmartConnectTaskRespSourceConfig.

        是否重命名Topic。（仅源端类型为Kafka时会显示）

        :param rename_topic_enabled: The rename_topic_enabled of this SmartConnectTaskRespSourceConfig.
        :type rename_topic_enabled: bool
        """
        self._rename_topic_enabled = rename_topic_enabled

    @property
    def provenance_header_enabled(self):
        """Gets the provenance_header_enabled of this SmartConnectTaskRespSourceConfig.

        是否添加来源header。（仅源端类型为Kafka时会显示）

        :return: The provenance_header_enabled of this SmartConnectTaskRespSourceConfig.
        :rtype: bool
        """
        return self._provenance_header_enabled

    @provenance_header_enabled.setter
    def provenance_header_enabled(self, provenance_header_enabled):
        """Sets the provenance_header_enabled of this SmartConnectTaskRespSourceConfig.

        是否添加来源header。（仅源端类型为Kafka时会显示）

        :param provenance_header_enabled: The provenance_header_enabled of this SmartConnectTaskRespSourceConfig.
        :type provenance_header_enabled: bool
        """
        self._provenance_header_enabled = provenance_header_enabled

    @property
    def consumer_strategy(self):
        """Gets the consumer_strategy of this SmartConnectTaskRespSourceConfig.

        启动偏移量，latest为获取最新的数据，earliest为获取最早的数据。（仅源端类型为Kafka时会显示）

        :return: The consumer_strategy of this SmartConnectTaskRespSourceConfig.
        :rtype: str
        """
        return self._consumer_strategy

    @consumer_strategy.setter
    def consumer_strategy(self, consumer_strategy):
        """Sets the consumer_strategy of this SmartConnectTaskRespSourceConfig.

        启动偏移量，latest为获取最新的数据，earliest为获取最早的数据。（仅源端类型为Kafka时会显示）

        :param consumer_strategy: The consumer_strategy of this SmartConnectTaskRespSourceConfig.
        :type consumer_strategy: str
        """
        self._consumer_strategy = consumer_strategy

    @property
    def compression_type(self):
        """Gets the compression_type of this SmartConnectTaskRespSourceConfig.

        压缩算法。（仅源端类型为Kafka时会显示）

        :return: The compression_type of this SmartConnectTaskRespSourceConfig.
        :rtype: str
        """
        return self._compression_type

    @compression_type.setter
    def compression_type(self, compression_type):
        """Sets the compression_type of this SmartConnectTaskRespSourceConfig.

        压缩算法。（仅源端类型为Kafka时会显示）

        :param compression_type: The compression_type of this SmartConnectTaskRespSourceConfig.
        :type compression_type: str
        """
        self._compression_type = compression_type

    @property
    def topics_mapping(self):
        """Gets the topics_mapping of this SmartConnectTaskRespSourceConfig.

        topic映射。（仅源端类型为Kafka时会显示）

        :return: The topics_mapping of this SmartConnectTaskRespSourceConfig.
        :rtype: str
        """
        return self._topics_mapping

    @topics_mapping.setter
    def topics_mapping(self, topics_mapping):
        """Sets the topics_mapping of this SmartConnectTaskRespSourceConfig.

        topic映射。（仅源端类型为Kafka时会显示）

        :param topics_mapping: The topics_mapping of this SmartConnectTaskRespSourceConfig.
        :type topics_mapping: str
        """
        self._topics_mapping = topics_mapping

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
        if not isinstance(other, SmartConnectTaskRespSourceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
