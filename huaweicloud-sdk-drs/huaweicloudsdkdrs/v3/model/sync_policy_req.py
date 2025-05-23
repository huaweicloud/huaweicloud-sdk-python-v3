# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncPolicyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'conflict_policy': 'str',
        'filter_ddl_policy': 'str',
        'ddl_trans': 'bool',
        'index_trans': 'bool',
        'topic_policy': 'str',
        'topic': 'str',
        'partition_policy': 'str',
        'kafka_data_format': 'str',
        'topic_name_format': 'str',
        'partitions_num': 'str',
        'replication_factor': 'str',
        'is_fill_materialized_view': 'bool',
        'export_snapshot': 'bool',
        'slot_name': 'str',
        'file_and_position': 'str',
        'gtid_set': 'str',
        'ddl_topic': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'conflict_policy': 'conflict_policy',
        'filter_ddl_policy': 'filter_ddl_policy',
        'ddl_trans': 'ddl_trans',
        'index_trans': 'index_trans',
        'topic_policy': 'topic_policy',
        'topic': 'topic',
        'partition_policy': 'partition_policy',
        'kafka_data_format': 'kafka_data_format',
        'topic_name_format': 'topic_name_format',
        'partitions_num': 'partitions_num',
        'replication_factor': 'replication_factor',
        'is_fill_materialized_view': 'is_fill_materialized_view',
        'export_snapshot': 'export_snapshot',
        'slot_name': 'slot_name',
        'file_and_position': 'file_and_position',
        'gtid_set': 'gtid_set',
        'ddl_topic': 'ddl_topic'
    }

    def __init__(self, job_id=None, conflict_policy=None, filter_ddl_policy=None, ddl_trans=None, index_trans=None, topic_policy=None, topic=None, partition_policy=None, kafka_data_format=None, topic_name_format=None, partitions_num=None, replication_factor=None, is_fill_materialized_view=None, export_snapshot=None, slot_name=None, file_and_position=None, gtid_set=None, ddl_topic=None):
        r"""SyncPolicyReq

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param conflict_policy: 冲突策略。 - ignore：忽略 - overwrite：覆盖 - stop：报错
        :type conflict_policy: str
        :param filter_ddl_policy: 过滤DDL策略。
        :type filter_ddl_policy: str
        :param ddl_trans: 同步增量是否同步DDL。
        :type ddl_trans: bool
        :param index_trans: 同步增量是否同步索引。
        :type index_trans: bool
        :param topic_policy: 同步Topic策略，目标库为kafka时必填，取值： - 0：集中投递到一个Topic - 1：按库名-schema-表名自动生成Topic名字 - 2：按库名自动生成Topic名字 - 3：按库名-schema自动生成Topic名字
        :type topic_policy: str
        :param topic: Topic名称，topic_policy为0时必填，确保topic已存在。
        :type topic: str
        :param partition_policy: 同步到kafka partition策略，取值： - 0：按库名.schema.表名的hash值投递到不同Partition - 1：全部投递到Partition 0 - 2：按主键的hash值投递到不同Partition - 3：按库名.schema的hash值投递到不同Partition **当topic_policy取0时，可以取0,1,2,3；当topic_policy取1时，可以取1,2；当topic_policy取2时，可以取0,1,3；当topic_policy取3时，可以取0,1；**
        :type partition_policy: str
        :param kafka_data_format: 投送到kafka的数据格式，不填默认为json：
        :type kafka_data_format: str
        :param topic_name_format: Topic名字格式，topic_policy为1,2,3,时需要 - 当topic_policy取1时，Topic名字格式支持database、schema两个变量，其他字符当做常量。分别用$database$代替数据库名，$schema$代替模式名，不填默认为$database$-$schema$ - 当topic_policy取2时，Topic名字格式支持database一个变量，其他字符都当做常量，不填默认为$database$ - 当topic_policy取3时，Topic名字格式支持database、schema和tablename三个变量，其他字符当做常量。分别用$database$代替数据库名，$schema$代替模式名，$tablename$代替表名，不填默认为$database$-$schema$-$tablename$
        :type topic_name_format: str
        :param partitions_num: Partition个数，取值1-2147483647之间，topic_policy为1,2,3,时需要，不填默认为1
        :type partitions_num: str
        :param replication_factor: 副本个数，取值1-32767之间，topic_policy为1,2,3,时需要，不填默认为1
        :type replication_factor: str
        :param is_fill_materialized_view: PostgreSQL同步全量阶段是否填充物化视图，不填默认为false
        :type is_fill_materialized_view: bool
        :param export_snapshot: PostgreSQL同步全量阶段是否使用快照模式导出，不填默认为false
        :type export_snapshot: bool
        :param slot_name: 复制槽名称，gaussdbv5ha-to-kafka主备任务必填
        :type slot_name: str
        :param file_and_position: - MySQL为源通过show master status命令获取源库位点，根据提示分别填写File:Position。例如：mysql-bin.000277:805 文件名只能为1-60个字符且不能包含&lt; &gt; &amp; : \&quot; \\&#39; / \\\\\\\\ 特殊字符，文件编号只能为3-20个数字，binlog事件位置只能为1-20个数字，且总长度不能超过100个字符。格式为：文件名.文件编号:事件位点 - MongoDB为源的任务，任务的源库日志从位点开始获取（含当前启动位点），位点需设置在oplog范围以内。非集群通过db.getReplicationInfo()直接获得oplog范围，集群通过db.watch([], {startAtOperationTime: Timestamp(xx, xx)})命令，将启动位点填在xx处，校验位点是否在oplog范围以内。格式为：timestamp:incre。timestamp和incre均为范围在1~2,147,483,647之间的整数。
        :type file_and_position: str
        :param gtid_set: - MySQL为源的任务需要，通过show master status命令获取源库位点，根据提示填写Executed_Gtid_Set（如果源库为MySQL 5.5版本，则不支持使用同步任务）。  - 不能包含&lt; &gt; &amp; \&quot; \\&#39; / \\\\\\\\ 特殊字符和中文。且不能超过2048个字符
        :type gtid_set: str
        :param ddl_topic: 存储DDL的topic。Kafka为目标且ddl_trans为true时必填，取值：目标库已存在的topic名称，确保topic已存在。
        :type ddl_topic: str
        """
        
        

        self._job_id = None
        self._conflict_policy = None
        self._filter_ddl_policy = None
        self._ddl_trans = None
        self._index_trans = None
        self._topic_policy = None
        self._topic = None
        self._partition_policy = None
        self._kafka_data_format = None
        self._topic_name_format = None
        self._partitions_num = None
        self._replication_factor = None
        self._is_fill_materialized_view = None
        self._export_snapshot = None
        self._slot_name = None
        self._file_and_position = None
        self._gtid_set = None
        self._ddl_topic = None
        self.discriminator = None

        self.job_id = job_id
        if conflict_policy is not None:
            self.conflict_policy = conflict_policy
        if filter_ddl_policy is not None:
            self.filter_ddl_policy = filter_ddl_policy
        if ddl_trans is not None:
            self.ddl_trans = ddl_trans
        if index_trans is not None:
            self.index_trans = index_trans
        if topic_policy is not None:
            self.topic_policy = topic_policy
        if topic is not None:
            self.topic = topic
        if partition_policy is not None:
            self.partition_policy = partition_policy
        if kafka_data_format is not None:
            self.kafka_data_format = kafka_data_format
        if topic_name_format is not None:
            self.topic_name_format = topic_name_format
        if partitions_num is not None:
            self.partitions_num = partitions_num
        if replication_factor is not None:
            self.replication_factor = replication_factor
        if is_fill_materialized_view is not None:
            self.is_fill_materialized_view = is_fill_materialized_view
        if export_snapshot is not None:
            self.export_snapshot = export_snapshot
        if slot_name is not None:
            self.slot_name = slot_name
        if file_and_position is not None:
            self.file_and_position = file_and_position
        if gtid_set is not None:
            self.gtid_set = gtid_set
        if ddl_topic is not None:
            self.ddl_topic = ddl_topic

    @property
    def job_id(self):
        r"""Gets the job_id of this SyncPolicyReq.

        任务ID。

        :return: The job_id of this SyncPolicyReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this SyncPolicyReq.

        任务ID。

        :param job_id: The job_id of this SyncPolicyReq.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def conflict_policy(self):
        r"""Gets the conflict_policy of this SyncPolicyReq.

        冲突策略。 - ignore：忽略 - overwrite：覆盖 - stop：报错

        :return: The conflict_policy of this SyncPolicyReq.
        :rtype: str
        """
        return self._conflict_policy

    @conflict_policy.setter
    def conflict_policy(self, conflict_policy):
        r"""Sets the conflict_policy of this SyncPolicyReq.

        冲突策略。 - ignore：忽略 - overwrite：覆盖 - stop：报错

        :param conflict_policy: The conflict_policy of this SyncPolicyReq.
        :type conflict_policy: str
        """
        self._conflict_policy = conflict_policy

    @property
    def filter_ddl_policy(self):
        r"""Gets the filter_ddl_policy of this SyncPolicyReq.

        过滤DDL策略。

        :return: The filter_ddl_policy of this SyncPolicyReq.
        :rtype: str
        """
        return self._filter_ddl_policy

    @filter_ddl_policy.setter
    def filter_ddl_policy(self, filter_ddl_policy):
        r"""Sets the filter_ddl_policy of this SyncPolicyReq.

        过滤DDL策略。

        :param filter_ddl_policy: The filter_ddl_policy of this SyncPolicyReq.
        :type filter_ddl_policy: str
        """
        self._filter_ddl_policy = filter_ddl_policy

    @property
    def ddl_trans(self):
        r"""Gets the ddl_trans of this SyncPolicyReq.

        同步增量是否同步DDL。

        :return: The ddl_trans of this SyncPolicyReq.
        :rtype: bool
        """
        return self._ddl_trans

    @ddl_trans.setter
    def ddl_trans(self, ddl_trans):
        r"""Sets the ddl_trans of this SyncPolicyReq.

        同步增量是否同步DDL。

        :param ddl_trans: The ddl_trans of this SyncPolicyReq.
        :type ddl_trans: bool
        """
        self._ddl_trans = ddl_trans

    @property
    def index_trans(self):
        r"""Gets the index_trans of this SyncPolicyReq.

        同步增量是否同步索引。

        :return: The index_trans of this SyncPolicyReq.
        :rtype: bool
        """
        return self._index_trans

    @index_trans.setter
    def index_trans(self, index_trans):
        r"""Sets the index_trans of this SyncPolicyReq.

        同步增量是否同步索引。

        :param index_trans: The index_trans of this SyncPolicyReq.
        :type index_trans: bool
        """
        self._index_trans = index_trans

    @property
    def topic_policy(self):
        r"""Gets the topic_policy of this SyncPolicyReq.

        同步Topic策略，目标库为kafka时必填，取值： - 0：集中投递到一个Topic - 1：按库名-schema-表名自动生成Topic名字 - 2：按库名自动生成Topic名字 - 3：按库名-schema自动生成Topic名字

        :return: The topic_policy of this SyncPolicyReq.
        :rtype: str
        """
        return self._topic_policy

    @topic_policy.setter
    def topic_policy(self, topic_policy):
        r"""Sets the topic_policy of this SyncPolicyReq.

        同步Topic策略，目标库为kafka时必填，取值： - 0：集中投递到一个Topic - 1：按库名-schema-表名自动生成Topic名字 - 2：按库名自动生成Topic名字 - 3：按库名-schema自动生成Topic名字

        :param topic_policy: The topic_policy of this SyncPolicyReq.
        :type topic_policy: str
        """
        self._topic_policy = topic_policy

    @property
    def topic(self):
        r"""Gets the topic of this SyncPolicyReq.

        Topic名称，topic_policy为0时必填，确保topic已存在。

        :return: The topic of this SyncPolicyReq.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this SyncPolicyReq.

        Topic名称，topic_policy为0时必填，确保topic已存在。

        :param topic: The topic of this SyncPolicyReq.
        :type topic: str
        """
        self._topic = topic

    @property
    def partition_policy(self):
        r"""Gets the partition_policy of this SyncPolicyReq.

        同步到kafka partition策略，取值： - 0：按库名.schema.表名的hash值投递到不同Partition - 1：全部投递到Partition 0 - 2：按主键的hash值投递到不同Partition - 3：按库名.schema的hash值投递到不同Partition **当topic_policy取0时，可以取0,1,2,3；当topic_policy取1时，可以取1,2；当topic_policy取2时，可以取0,1,3；当topic_policy取3时，可以取0,1；**

        :return: The partition_policy of this SyncPolicyReq.
        :rtype: str
        """
        return self._partition_policy

    @partition_policy.setter
    def partition_policy(self, partition_policy):
        r"""Sets the partition_policy of this SyncPolicyReq.

        同步到kafka partition策略，取值： - 0：按库名.schema.表名的hash值投递到不同Partition - 1：全部投递到Partition 0 - 2：按主键的hash值投递到不同Partition - 3：按库名.schema的hash值投递到不同Partition **当topic_policy取0时，可以取0,1,2,3；当topic_policy取1时，可以取1,2；当topic_policy取2时，可以取0,1,3；当topic_policy取3时，可以取0,1；**

        :param partition_policy: The partition_policy of this SyncPolicyReq.
        :type partition_policy: str
        """
        self._partition_policy = partition_policy

    @property
    def kafka_data_format(self):
        r"""Gets the kafka_data_format of this SyncPolicyReq.

        投送到kafka的数据格式，不填默认为json：

        :return: The kafka_data_format of this SyncPolicyReq.
        :rtype: str
        """
        return self._kafka_data_format

    @kafka_data_format.setter
    def kafka_data_format(self, kafka_data_format):
        r"""Sets the kafka_data_format of this SyncPolicyReq.

        投送到kafka的数据格式，不填默认为json：

        :param kafka_data_format: The kafka_data_format of this SyncPolicyReq.
        :type kafka_data_format: str
        """
        self._kafka_data_format = kafka_data_format

    @property
    def topic_name_format(self):
        r"""Gets the topic_name_format of this SyncPolicyReq.

        Topic名字格式，topic_policy为1,2,3,时需要 - 当topic_policy取1时，Topic名字格式支持database、schema两个变量，其他字符当做常量。分别用$database$代替数据库名，$schema$代替模式名，不填默认为$database$-$schema$ - 当topic_policy取2时，Topic名字格式支持database一个变量，其他字符都当做常量，不填默认为$database$ - 当topic_policy取3时，Topic名字格式支持database、schema和tablename三个变量，其他字符当做常量。分别用$database$代替数据库名，$schema$代替模式名，$tablename$代替表名，不填默认为$database$-$schema$-$tablename$

        :return: The topic_name_format of this SyncPolicyReq.
        :rtype: str
        """
        return self._topic_name_format

    @topic_name_format.setter
    def topic_name_format(self, topic_name_format):
        r"""Sets the topic_name_format of this SyncPolicyReq.

        Topic名字格式，topic_policy为1,2,3,时需要 - 当topic_policy取1时，Topic名字格式支持database、schema两个变量，其他字符当做常量。分别用$database$代替数据库名，$schema$代替模式名，不填默认为$database$-$schema$ - 当topic_policy取2时，Topic名字格式支持database一个变量，其他字符都当做常量，不填默认为$database$ - 当topic_policy取3时，Topic名字格式支持database、schema和tablename三个变量，其他字符当做常量。分别用$database$代替数据库名，$schema$代替模式名，$tablename$代替表名，不填默认为$database$-$schema$-$tablename$

        :param topic_name_format: The topic_name_format of this SyncPolicyReq.
        :type topic_name_format: str
        """
        self._topic_name_format = topic_name_format

    @property
    def partitions_num(self):
        r"""Gets the partitions_num of this SyncPolicyReq.

        Partition个数，取值1-2147483647之间，topic_policy为1,2,3,时需要，不填默认为1

        :return: The partitions_num of this SyncPolicyReq.
        :rtype: str
        """
        return self._partitions_num

    @partitions_num.setter
    def partitions_num(self, partitions_num):
        r"""Sets the partitions_num of this SyncPolicyReq.

        Partition个数，取值1-2147483647之间，topic_policy为1,2,3,时需要，不填默认为1

        :param partitions_num: The partitions_num of this SyncPolicyReq.
        :type partitions_num: str
        """
        self._partitions_num = partitions_num

    @property
    def replication_factor(self):
        r"""Gets the replication_factor of this SyncPolicyReq.

        副本个数，取值1-32767之间，topic_policy为1,2,3,时需要，不填默认为1

        :return: The replication_factor of this SyncPolicyReq.
        :rtype: str
        """
        return self._replication_factor

    @replication_factor.setter
    def replication_factor(self, replication_factor):
        r"""Sets the replication_factor of this SyncPolicyReq.

        副本个数，取值1-32767之间，topic_policy为1,2,3,时需要，不填默认为1

        :param replication_factor: The replication_factor of this SyncPolicyReq.
        :type replication_factor: str
        """
        self._replication_factor = replication_factor

    @property
    def is_fill_materialized_view(self):
        r"""Gets the is_fill_materialized_view of this SyncPolicyReq.

        PostgreSQL同步全量阶段是否填充物化视图，不填默认为false

        :return: The is_fill_materialized_view of this SyncPolicyReq.
        :rtype: bool
        """
        return self._is_fill_materialized_view

    @is_fill_materialized_view.setter
    def is_fill_materialized_view(self, is_fill_materialized_view):
        r"""Sets the is_fill_materialized_view of this SyncPolicyReq.

        PostgreSQL同步全量阶段是否填充物化视图，不填默认为false

        :param is_fill_materialized_view: The is_fill_materialized_view of this SyncPolicyReq.
        :type is_fill_materialized_view: bool
        """
        self._is_fill_materialized_view = is_fill_materialized_view

    @property
    def export_snapshot(self):
        r"""Gets the export_snapshot of this SyncPolicyReq.

        PostgreSQL同步全量阶段是否使用快照模式导出，不填默认为false

        :return: The export_snapshot of this SyncPolicyReq.
        :rtype: bool
        """
        return self._export_snapshot

    @export_snapshot.setter
    def export_snapshot(self, export_snapshot):
        r"""Sets the export_snapshot of this SyncPolicyReq.

        PostgreSQL同步全量阶段是否使用快照模式导出，不填默认为false

        :param export_snapshot: The export_snapshot of this SyncPolicyReq.
        :type export_snapshot: bool
        """
        self._export_snapshot = export_snapshot

    @property
    def slot_name(self):
        r"""Gets the slot_name of this SyncPolicyReq.

        复制槽名称，gaussdbv5ha-to-kafka主备任务必填

        :return: The slot_name of this SyncPolicyReq.
        :rtype: str
        """
        return self._slot_name

    @slot_name.setter
    def slot_name(self, slot_name):
        r"""Sets the slot_name of this SyncPolicyReq.

        复制槽名称，gaussdbv5ha-to-kafka主备任务必填

        :param slot_name: The slot_name of this SyncPolicyReq.
        :type slot_name: str
        """
        self._slot_name = slot_name

    @property
    def file_and_position(self):
        r"""Gets the file_and_position of this SyncPolicyReq.

        - MySQL为源通过show master status命令获取源库位点，根据提示分别填写File:Position。例如：mysql-bin.000277:805 文件名只能为1-60个字符且不能包含< > & : \" \\' / \\\\\\\\ 特殊字符，文件编号只能为3-20个数字，binlog事件位置只能为1-20个数字，且总长度不能超过100个字符。格式为：文件名.文件编号:事件位点 - MongoDB为源的任务，任务的源库日志从位点开始获取（含当前启动位点），位点需设置在oplog范围以内。非集群通过db.getReplicationInfo()直接获得oplog范围，集群通过db.watch([], {startAtOperationTime: Timestamp(xx, xx)})命令，将启动位点填在xx处，校验位点是否在oplog范围以内。格式为：timestamp:incre。timestamp和incre均为范围在1~2,147,483,647之间的整数。

        :return: The file_and_position of this SyncPolicyReq.
        :rtype: str
        """
        return self._file_and_position

    @file_and_position.setter
    def file_and_position(self, file_and_position):
        r"""Sets the file_and_position of this SyncPolicyReq.

        - MySQL为源通过show master status命令获取源库位点，根据提示分别填写File:Position。例如：mysql-bin.000277:805 文件名只能为1-60个字符且不能包含< > & : \" \\' / \\\\\\\\ 特殊字符，文件编号只能为3-20个数字，binlog事件位置只能为1-20个数字，且总长度不能超过100个字符。格式为：文件名.文件编号:事件位点 - MongoDB为源的任务，任务的源库日志从位点开始获取（含当前启动位点），位点需设置在oplog范围以内。非集群通过db.getReplicationInfo()直接获得oplog范围，集群通过db.watch([], {startAtOperationTime: Timestamp(xx, xx)})命令，将启动位点填在xx处，校验位点是否在oplog范围以内。格式为：timestamp:incre。timestamp和incre均为范围在1~2,147,483,647之间的整数。

        :param file_and_position: The file_and_position of this SyncPolicyReq.
        :type file_and_position: str
        """
        self._file_and_position = file_and_position

    @property
    def gtid_set(self):
        r"""Gets the gtid_set of this SyncPolicyReq.

        - MySQL为源的任务需要，通过show master status命令获取源库位点，根据提示填写Executed_Gtid_Set（如果源库为MySQL 5.5版本，则不支持使用同步任务）。  - 不能包含< > & \" \\' / \\\\\\\\ 特殊字符和中文。且不能超过2048个字符

        :return: The gtid_set of this SyncPolicyReq.
        :rtype: str
        """
        return self._gtid_set

    @gtid_set.setter
    def gtid_set(self, gtid_set):
        r"""Sets the gtid_set of this SyncPolicyReq.

        - MySQL为源的任务需要，通过show master status命令获取源库位点，根据提示填写Executed_Gtid_Set（如果源库为MySQL 5.5版本，则不支持使用同步任务）。  - 不能包含< > & \" \\' / \\\\\\\\ 特殊字符和中文。且不能超过2048个字符

        :param gtid_set: The gtid_set of this SyncPolicyReq.
        :type gtid_set: str
        """
        self._gtid_set = gtid_set

    @property
    def ddl_topic(self):
        r"""Gets the ddl_topic of this SyncPolicyReq.

        存储DDL的topic。Kafka为目标且ddl_trans为true时必填，取值：目标库已存在的topic名称，确保topic已存在。

        :return: The ddl_topic of this SyncPolicyReq.
        :rtype: str
        """
        return self._ddl_topic

    @ddl_topic.setter
    def ddl_topic(self, ddl_topic):
        r"""Sets the ddl_topic of this SyncPolicyReq.

        存储DDL的topic。Kafka为目标且ddl_trans为true时必填，取值：目标库已存在的topic名称，确保topic已存在。

        :param ddl_topic: The ddl_topic of this SyncPolicyReq.
        :type ddl_topic: str
        """
        self._ddl_topic = ddl_topic

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
        if not isinstance(other, SyncPolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
