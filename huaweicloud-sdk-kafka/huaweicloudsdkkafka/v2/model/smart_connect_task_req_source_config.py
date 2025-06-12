# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartConnectTaskReqSourceConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_cluster_name': 'str',
        'cluster_name': 'str',
        'user_name': 'str',
        'password': 'str',
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
        'current_cluster_name': 'current_cluster_name',
        'cluster_name': 'cluster_name',
        'user_name': 'user_name',
        'password': 'password',
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

    def __init__(self, current_cluster_name=None, cluster_name=None, user_name=None, password=None, sasl_mechanism=None, instance_id=None, bootstrap_servers=None, security_protocol=None, direction=None, sync_consumer_offsets_enabled=None, replication_factor=None, task_num=None, rename_topic_enabled=None, provenance_header_enabled=None, consumer_strategy=None, compression_type=None, topics_mapping=None):
        r"""SmartConnectTaskReqSourceConfig

        The model defined in huaweicloud sdk

        :param current_cluster_name: 当前Kafka实例别名。（仅源端类型为Kafka时需要填写）
        :type current_cluster_name: str
        :param cluster_name: 对端Kafka实例别名。（仅源端类型为Kafka时需要填写）
        :type cluster_name: str
        :param user_name: 对端Kafka开启SASL_SSL时设置的用户名，或者创建SASL_SSL用户时设置的用户名。（仅源端类型为Kafka且对端Kafka认证方式为“SASL_SSL”时需要填写）
        :type user_name: str
        :param password: 对端Kafka开启SASL_SSL时设置的密码，或者创建SASL_SSL用户时设置的密码。（仅源端类型为Kafka且对端Kafka认证方式为“SASL_SSL”时需要填写）
        :type password: str
        :param sasl_mechanism: 对端Kafka认证机制。（仅源端类型为Kafka且“认证方式”为“SASL_SSL”时需要填写）
        :type sasl_mechanism: str
        :param instance_id: 对端Kafka实例ID。（仅源端类型为Kafka时需要填写，instance_id和bootstrap_servers仅需要填写其中一个）
        :type instance_id: str
        :param bootstrap_servers: 对端Kafka实例地址。（仅源端类型为Kafka时需要填写，instance_id和bootstrap_servers仅需要填写其中一个）
        :type bootstrap_servers: str
        :param security_protocol: 对端Kafka认证方式。（仅源端类型为Kafka需要填写） 支持以下两种认证方式：   - SASL_SSL：表示实例已开启SASL_SSL。   - PLAINTEXT：表示实例未开启SASL_SSL。 
        :type security_protocol: str
        :param direction: 同步方向；pull为把对端Kafka实例数据复制到当前Kafka实例中，push为把当前Kafka实例数据复制到对端Kafka实例中，two-way为对两端Kafka实例数据进行双向复制。（仅源端类型为Kafka时需要填写）
        :type direction: str
        :param sync_consumer_offsets_enabled: 是否同步消费进度。（仅源端类型为Kafka时需要填写）
        :type sync_consumer_offsets_enabled: bool
        :param replication_factor: 在对端实例中自动创建Topic时，指定Topic的副本数，此参数值不能超过对端实例的代理数。如果对端实例中设置了“default.replication.factor”，此参数的优先级高于“default.replication.factor”。（仅源端类型为Kafka时需要填写）
        :type replication_factor: int
        :param task_num: 数据复制的任务数。默认值为2，建议保持默认值。如果“同步方式”为“双向”，实际任务数&#x3D;设置的任务数*2。（仅源端类型为Kafka时需要填写）
        :type task_num: int
        :param rename_topic_enabled: 是否重命名Topic，在目标Topic名称前添加源端Kafka实例的别名，形成目标Topic新的名称。（仅源端类型为Kafka时需要填写）
        :type rename_topic_enabled: bool
        :param provenance_header_enabled: 目标Topic接收复制的消息，此消息header中包含消息来源。两端实例数据双向复制时，请开启“添加来源header”，防止循环复制。（仅源端类型为Kafka时需要填写）
        :type provenance_header_enabled: bool
        :param consumer_strategy: 启动偏移量，latest为获取最新的数据，earliest为获取最早的数据。（仅源端类型为Kafka时需要填写）
        :type consumer_strategy: str
        :param compression_type: 复制消息所使用的压缩算法。（仅源端类型为Kafka时需要填写） - none - gzip - snappy - lz4 - zstd 
        :type compression_type: str
        :param topics_mapping: Topic映射，用于自定义目标端Topic名称。不能同时设置“重命名Topic”和“Topic映射”。Topic映射请按照“源端Topic:目的端Topic”的格式填写，如涉及多个Topic映射，请用“,”分隔开，例如：topic-sc-1:topic-sc-2,topic-sc-3:topic-sc-4。（仅源端类型为Kafka时需要填写）
        :type topics_mapping: str
        """
        
        

        self._current_cluster_name = None
        self._cluster_name = None
        self._user_name = None
        self._password = None
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

        if current_cluster_name is not None:
            self.current_cluster_name = current_cluster_name
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password
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
    def current_cluster_name(self):
        r"""Gets the current_cluster_name of this SmartConnectTaskReqSourceConfig.

        当前Kafka实例别名。（仅源端类型为Kafka时需要填写）

        :return: The current_cluster_name of this SmartConnectTaskReqSourceConfig.
        :rtype: str
        """
        return self._current_cluster_name

    @current_cluster_name.setter
    def current_cluster_name(self, current_cluster_name):
        r"""Sets the current_cluster_name of this SmartConnectTaskReqSourceConfig.

        当前Kafka实例别名。（仅源端类型为Kafka时需要填写）

        :param current_cluster_name: The current_cluster_name of this SmartConnectTaskReqSourceConfig.
        :type current_cluster_name: str
        """
        self._current_cluster_name = current_cluster_name

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this SmartConnectTaskReqSourceConfig.

        对端Kafka实例别名。（仅源端类型为Kafka时需要填写）

        :return: The cluster_name of this SmartConnectTaskReqSourceConfig.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this SmartConnectTaskReqSourceConfig.

        对端Kafka实例别名。（仅源端类型为Kafka时需要填写）

        :param cluster_name: The cluster_name of this SmartConnectTaskReqSourceConfig.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def user_name(self):
        r"""Gets the user_name of this SmartConnectTaskReqSourceConfig.

        对端Kafka开启SASL_SSL时设置的用户名，或者创建SASL_SSL用户时设置的用户名。（仅源端类型为Kafka且对端Kafka认证方式为“SASL_SSL”时需要填写）

        :return: The user_name of this SmartConnectTaskReqSourceConfig.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this SmartConnectTaskReqSourceConfig.

        对端Kafka开启SASL_SSL时设置的用户名，或者创建SASL_SSL用户时设置的用户名。（仅源端类型为Kafka且对端Kafka认证方式为“SASL_SSL”时需要填写）

        :param user_name: The user_name of this SmartConnectTaskReqSourceConfig.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def password(self):
        r"""Gets the password of this SmartConnectTaskReqSourceConfig.

        对端Kafka开启SASL_SSL时设置的密码，或者创建SASL_SSL用户时设置的密码。（仅源端类型为Kafka且对端Kafka认证方式为“SASL_SSL”时需要填写）

        :return: The password of this SmartConnectTaskReqSourceConfig.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this SmartConnectTaskReqSourceConfig.

        对端Kafka开启SASL_SSL时设置的密码，或者创建SASL_SSL用户时设置的密码。（仅源端类型为Kafka且对端Kafka认证方式为“SASL_SSL”时需要填写）

        :param password: The password of this SmartConnectTaskReqSourceConfig.
        :type password: str
        """
        self._password = password

    @property
    def sasl_mechanism(self):
        r"""Gets the sasl_mechanism of this SmartConnectTaskReqSourceConfig.

        对端Kafka认证机制。（仅源端类型为Kafka且“认证方式”为“SASL_SSL”时需要填写）

        :return: The sasl_mechanism of this SmartConnectTaskReqSourceConfig.
        :rtype: str
        """
        return self._sasl_mechanism

    @sasl_mechanism.setter
    def sasl_mechanism(self, sasl_mechanism):
        r"""Sets the sasl_mechanism of this SmartConnectTaskReqSourceConfig.

        对端Kafka认证机制。（仅源端类型为Kafka且“认证方式”为“SASL_SSL”时需要填写）

        :param sasl_mechanism: The sasl_mechanism of this SmartConnectTaskReqSourceConfig.
        :type sasl_mechanism: str
        """
        self._sasl_mechanism = sasl_mechanism

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SmartConnectTaskReqSourceConfig.

        对端Kafka实例ID。（仅源端类型为Kafka时需要填写，instance_id和bootstrap_servers仅需要填写其中一个）

        :return: The instance_id of this SmartConnectTaskReqSourceConfig.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SmartConnectTaskReqSourceConfig.

        对端Kafka实例ID。（仅源端类型为Kafka时需要填写，instance_id和bootstrap_servers仅需要填写其中一个）

        :param instance_id: The instance_id of this SmartConnectTaskReqSourceConfig.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def bootstrap_servers(self):
        r"""Gets the bootstrap_servers of this SmartConnectTaskReqSourceConfig.

        对端Kafka实例地址。（仅源端类型为Kafka时需要填写，instance_id和bootstrap_servers仅需要填写其中一个）

        :return: The bootstrap_servers of this SmartConnectTaskReqSourceConfig.
        :rtype: str
        """
        return self._bootstrap_servers

    @bootstrap_servers.setter
    def bootstrap_servers(self, bootstrap_servers):
        r"""Sets the bootstrap_servers of this SmartConnectTaskReqSourceConfig.

        对端Kafka实例地址。（仅源端类型为Kafka时需要填写，instance_id和bootstrap_servers仅需要填写其中一个）

        :param bootstrap_servers: The bootstrap_servers of this SmartConnectTaskReqSourceConfig.
        :type bootstrap_servers: str
        """
        self._bootstrap_servers = bootstrap_servers

    @property
    def security_protocol(self):
        r"""Gets the security_protocol of this SmartConnectTaskReqSourceConfig.

        对端Kafka认证方式。（仅源端类型为Kafka需要填写） 支持以下两种认证方式：   - SASL_SSL：表示实例已开启SASL_SSL。   - PLAINTEXT：表示实例未开启SASL_SSL。 

        :return: The security_protocol of this SmartConnectTaskReqSourceConfig.
        :rtype: str
        """
        return self._security_protocol

    @security_protocol.setter
    def security_protocol(self, security_protocol):
        r"""Sets the security_protocol of this SmartConnectTaskReqSourceConfig.

        对端Kafka认证方式。（仅源端类型为Kafka需要填写） 支持以下两种认证方式：   - SASL_SSL：表示实例已开启SASL_SSL。   - PLAINTEXT：表示实例未开启SASL_SSL。 

        :param security_protocol: The security_protocol of this SmartConnectTaskReqSourceConfig.
        :type security_protocol: str
        """
        self._security_protocol = security_protocol

    @property
    def direction(self):
        r"""Gets the direction of this SmartConnectTaskReqSourceConfig.

        同步方向；pull为把对端Kafka实例数据复制到当前Kafka实例中，push为把当前Kafka实例数据复制到对端Kafka实例中，two-way为对两端Kafka实例数据进行双向复制。（仅源端类型为Kafka时需要填写）

        :return: The direction of this SmartConnectTaskReqSourceConfig.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this SmartConnectTaskReqSourceConfig.

        同步方向；pull为把对端Kafka实例数据复制到当前Kafka实例中，push为把当前Kafka实例数据复制到对端Kafka实例中，two-way为对两端Kafka实例数据进行双向复制。（仅源端类型为Kafka时需要填写）

        :param direction: The direction of this SmartConnectTaskReqSourceConfig.
        :type direction: str
        """
        self._direction = direction

    @property
    def sync_consumer_offsets_enabled(self):
        r"""Gets the sync_consumer_offsets_enabled of this SmartConnectTaskReqSourceConfig.

        是否同步消费进度。（仅源端类型为Kafka时需要填写）

        :return: The sync_consumer_offsets_enabled of this SmartConnectTaskReqSourceConfig.
        :rtype: bool
        """
        return self._sync_consumer_offsets_enabled

    @sync_consumer_offsets_enabled.setter
    def sync_consumer_offsets_enabled(self, sync_consumer_offsets_enabled):
        r"""Sets the sync_consumer_offsets_enabled of this SmartConnectTaskReqSourceConfig.

        是否同步消费进度。（仅源端类型为Kafka时需要填写）

        :param sync_consumer_offsets_enabled: The sync_consumer_offsets_enabled of this SmartConnectTaskReqSourceConfig.
        :type sync_consumer_offsets_enabled: bool
        """
        self._sync_consumer_offsets_enabled = sync_consumer_offsets_enabled

    @property
    def replication_factor(self):
        r"""Gets the replication_factor of this SmartConnectTaskReqSourceConfig.

        在对端实例中自动创建Topic时，指定Topic的副本数，此参数值不能超过对端实例的代理数。如果对端实例中设置了“default.replication.factor”，此参数的优先级高于“default.replication.factor”。（仅源端类型为Kafka时需要填写）

        :return: The replication_factor of this SmartConnectTaskReqSourceConfig.
        :rtype: int
        """
        return self._replication_factor

    @replication_factor.setter
    def replication_factor(self, replication_factor):
        r"""Sets the replication_factor of this SmartConnectTaskReqSourceConfig.

        在对端实例中自动创建Topic时，指定Topic的副本数，此参数值不能超过对端实例的代理数。如果对端实例中设置了“default.replication.factor”，此参数的优先级高于“default.replication.factor”。（仅源端类型为Kafka时需要填写）

        :param replication_factor: The replication_factor of this SmartConnectTaskReqSourceConfig.
        :type replication_factor: int
        """
        self._replication_factor = replication_factor

    @property
    def task_num(self):
        r"""Gets the task_num of this SmartConnectTaskReqSourceConfig.

        数据复制的任务数。默认值为2，建议保持默认值。如果“同步方式”为“双向”，实际任务数=设置的任务数*2。（仅源端类型为Kafka时需要填写）

        :return: The task_num of this SmartConnectTaskReqSourceConfig.
        :rtype: int
        """
        return self._task_num

    @task_num.setter
    def task_num(self, task_num):
        r"""Sets the task_num of this SmartConnectTaskReqSourceConfig.

        数据复制的任务数。默认值为2，建议保持默认值。如果“同步方式”为“双向”，实际任务数=设置的任务数*2。（仅源端类型为Kafka时需要填写）

        :param task_num: The task_num of this SmartConnectTaskReqSourceConfig.
        :type task_num: int
        """
        self._task_num = task_num

    @property
    def rename_topic_enabled(self):
        r"""Gets the rename_topic_enabled of this SmartConnectTaskReqSourceConfig.

        是否重命名Topic，在目标Topic名称前添加源端Kafka实例的别名，形成目标Topic新的名称。（仅源端类型为Kafka时需要填写）

        :return: The rename_topic_enabled of this SmartConnectTaskReqSourceConfig.
        :rtype: bool
        """
        return self._rename_topic_enabled

    @rename_topic_enabled.setter
    def rename_topic_enabled(self, rename_topic_enabled):
        r"""Sets the rename_topic_enabled of this SmartConnectTaskReqSourceConfig.

        是否重命名Topic，在目标Topic名称前添加源端Kafka实例的别名，形成目标Topic新的名称。（仅源端类型为Kafka时需要填写）

        :param rename_topic_enabled: The rename_topic_enabled of this SmartConnectTaskReqSourceConfig.
        :type rename_topic_enabled: bool
        """
        self._rename_topic_enabled = rename_topic_enabled

    @property
    def provenance_header_enabled(self):
        r"""Gets the provenance_header_enabled of this SmartConnectTaskReqSourceConfig.

        目标Topic接收复制的消息，此消息header中包含消息来源。两端实例数据双向复制时，请开启“添加来源header”，防止循环复制。（仅源端类型为Kafka时需要填写）

        :return: The provenance_header_enabled of this SmartConnectTaskReqSourceConfig.
        :rtype: bool
        """
        return self._provenance_header_enabled

    @provenance_header_enabled.setter
    def provenance_header_enabled(self, provenance_header_enabled):
        r"""Sets the provenance_header_enabled of this SmartConnectTaskReqSourceConfig.

        目标Topic接收复制的消息，此消息header中包含消息来源。两端实例数据双向复制时，请开启“添加来源header”，防止循环复制。（仅源端类型为Kafka时需要填写）

        :param provenance_header_enabled: The provenance_header_enabled of this SmartConnectTaskReqSourceConfig.
        :type provenance_header_enabled: bool
        """
        self._provenance_header_enabled = provenance_header_enabled

    @property
    def consumer_strategy(self):
        r"""Gets the consumer_strategy of this SmartConnectTaskReqSourceConfig.

        启动偏移量，latest为获取最新的数据，earliest为获取最早的数据。（仅源端类型为Kafka时需要填写）

        :return: The consumer_strategy of this SmartConnectTaskReqSourceConfig.
        :rtype: str
        """
        return self._consumer_strategy

    @consumer_strategy.setter
    def consumer_strategy(self, consumer_strategy):
        r"""Sets the consumer_strategy of this SmartConnectTaskReqSourceConfig.

        启动偏移量，latest为获取最新的数据，earliest为获取最早的数据。（仅源端类型为Kafka时需要填写）

        :param consumer_strategy: The consumer_strategy of this SmartConnectTaskReqSourceConfig.
        :type consumer_strategy: str
        """
        self._consumer_strategy = consumer_strategy

    @property
    def compression_type(self):
        r"""Gets the compression_type of this SmartConnectTaskReqSourceConfig.

        复制消息所使用的压缩算法。（仅源端类型为Kafka时需要填写） - none - gzip - snappy - lz4 - zstd 

        :return: The compression_type of this SmartConnectTaskReqSourceConfig.
        :rtype: str
        """
        return self._compression_type

    @compression_type.setter
    def compression_type(self, compression_type):
        r"""Sets the compression_type of this SmartConnectTaskReqSourceConfig.

        复制消息所使用的压缩算法。（仅源端类型为Kafka时需要填写） - none - gzip - snappy - lz4 - zstd 

        :param compression_type: The compression_type of this SmartConnectTaskReqSourceConfig.
        :type compression_type: str
        """
        self._compression_type = compression_type

    @property
    def topics_mapping(self):
        r"""Gets the topics_mapping of this SmartConnectTaskReqSourceConfig.

        Topic映射，用于自定义目标端Topic名称。不能同时设置“重命名Topic”和“Topic映射”。Topic映射请按照“源端Topic:目的端Topic”的格式填写，如涉及多个Topic映射，请用“,”分隔开，例如：topic-sc-1:topic-sc-2,topic-sc-3:topic-sc-4。（仅源端类型为Kafka时需要填写）

        :return: The topics_mapping of this SmartConnectTaskReqSourceConfig.
        :rtype: str
        """
        return self._topics_mapping

    @topics_mapping.setter
    def topics_mapping(self, topics_mapping):
        r"""Sets the topics_mapping of this SmartConnectTaskReqSourceConfig.

        Topic映射，用于自定义目标端Topic名称。不能同时设置“重命名Topic”和“Topic映射”。Topic映射请按照“源端Topic:目的端Topic”的格式填写，如涉及多个Topic映射，请用“,”分隔开，例如：topic-sc-1:topic-sc-2,topic-sc-3:topic-sc-4。（仅源端类型为Kafka时需要填写）

        :param topics_mapping: The topics_mapping of this SmartConnectTaskReqSourceConfig.
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
        if not isinstance(other, SmartConnectTaskReqSourceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
