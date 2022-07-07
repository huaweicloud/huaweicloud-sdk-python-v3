# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotBackupsResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'created': 'str',
        'datastore': 'ListSnapshotBackupsDatastoreResp',
        'description': 'str',
        'id': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'name': 'str',
        'status': 'str',
        'updated': 'str',
        'backup_type': 'str',
        'backup_method': 'str',
        'backup_expected_start_time': 'str',
        'backup_keep_day': 'int',
        'backup_period': 'str',
        'indices': 'str',
        'total_shards': 'int',
        'failed_shards': 'int',
        'version': 'str',
        'restore_status': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'bucket_name': 'str'
    }

    attribute_map = {
        'created': 'created',
        'datastore': 'datastore',
        'description': 'description',
        'id': 'id',
        'cluster_id': 'clusterId',
        'cluster_name': 'clusterName',
        'name': 'name',
        'status': 'status',
        'updated': 'updated',
        'backup_type': 'backupType',
        'backup_method': 'backupMethod',
        'backup_expected_start_time': 'backupExpectedStartTime',
        'backup_keep_day': 'backupKeepDay',
        'backup_period': 'backupPeriod',
        'indices': 'indices',
        'total_shards': 'totalShards',
        'failed_shards': 'failedShards',
        'version': 'version',
        'restore_status': 'restoreStatus',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'bucket_name': 'bucketName'
    }

    def __init__(self, created=None, datastore=None, description=None, id=None, cluster_id=None, cluster_name=None, name=None, status=None, updated=None, backup_type=None, backup_method=None, backup_expected_start_time=None, backup_keep_day=None, backup_period=None, indices=None, total_shards=None, failed_shards=None, version=None, restore_status=None, start_time=None, end_time=None, bucket_name=None):
        """ListSnapshotBackupsResp

        The model defined in huaweicloud sdk

        :param created: 快照创建时间。
        :type created: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkcss.v1.ListSnapshotBackupsDatastoreResp`
        :param description: 快照描述信息。
        :type description: str
        :param id: 快照ID。
        :type id: str
        :param cluster_id: 集群ID。
        :type cluster_id: str
        :param cluster_name: 集群名字。
        :type cluster_name: str
        :param name: 快照名称。
        :type name: str
        :param status: 快照状态。
        :type status: str
        :param updated: 快照更新时间，格式为ISO8601：CCYY-MM-DDThh:mm:ss。
        :type updated: str
        :param backup_type: 快照创建类型： - 0：表示自动创建。 - 1：表示手动创建。
        :type backup_type: str
        :param backup_method: 创建快照方式。
        :type backup_method: str
        :param backup_expected_start_time: 快照开始执行时间。
        :type backup_expected_start_time: str
        :param backup_keep_day: 快照保留时间。
        :type backup_keep_day: int
        :param backup_period: 快照每天执行的时间点。
        :type backup_period: str
        :param indices: 要备份的索引。
        :type indices: str
        :param total_shards: 要备份的索引的总shard数。
        :type total_shards: int
        :param failed_shards: 备份失败的shard数。
        :type failed_shards: int
        :param version: 快照的版本。
        :type version: str
        :param restore_status: 快照恢复的状态。
        :type restore_status: str
        :param start_time: 快照开始执行的时间戳。
        :type start_time: int
        :param end_time: 快照执行结束的时间戳。
        :type end_time: int
        :param bucket_name: 保存快照数据的桶名。
        :type bucket_name: str
        """
        
        

        self._created = None
        self._datastore = None
        self._description = None
        self._id = None
        self._cluster_id = None
        self._cluster_name = None
        self._name = None
        self._status = None
        self._updated = None
        self._backup_type = None
        self._backup_method = None
        self._backup_expected_start_time = None
        self._backup_keep_day = None
        self._backup_period = None
        self._indices = None
        self._total_shards = None
        self._failed_shards = None
        self._version = None
        self._restore_status = None
        self._start_time = None
        self._end_time = None
        self._bucket_name = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if datastore is not None:
            self.datastore = datastore
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if updated is not None:
            self.updated = updated
        if backup_type is not None:
            self.backup_type = backup_type
        if backup_method is not None:
            self.backup_method = backup_method
        if backup_expected_start_time is not None:
            self.backup_expected_start_time = backup_expected_start_time
        if backup_keep_day is not None:
            self.backup_keep_day = backup_keep_day
        if backup_period is not None:
            self.backup_period = backup_period
        if indices is not None:
            self.indices = indices
        if total_shards is not None:
            self.total_shards = total_shards
        if failed_shards is not None:
            self.failed_shards = failed_shards
        if version is not None:
            self.version = version
        if restore_status is not None:
            self.restore_status = restore_status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if bucket_name is not None:
            self.bucket_name = bucket_name

    @property
    def created(self):
        """Gets the created of this ListSnapshotBackupsResp.

        快照创建时间。

        :return: The created of this ListSnapshotBackupsResp.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ListSnapshotBackupsResp.

        快照创建时间。

        :param created: The created of this ListSnapshotBackupsResp.
        :type created: str
        """
        self._created = created

    @property
    def datastore(self):
        """Gets the datastore of this ListSnapshotBackupsResp.


        :return: The datastore of this ListSnapshotBackupsResp.
        :rtype: :class:`huaweicloudsdkcss.v1.ListSnapshotBackupsDatastoreResp`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this ListSnapshotBackupsResp.


        :param datastore: The datastore of this ListSnapshotBackupsResp.
        :type datastore: :class:`huaweicloudsdkcss.v1.ListSnapshotBackupsDatastoreResp`
        """
        self._datastore = datastore

    @property
    def description(self):
        """Gets the description of this ListSnapshotBackupsResp.

        快照描述信息。

        :return: The description of this ListSnapshotBackupsResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListSnapshotBackupsResp.

        快照描述信息。

        :param description: The description of this ListSnapshotBackupsResp.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this ListSnapshotBackupsResp.

        快照ID。

        :return: The id of this ListSnapshotBackupsResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListSnapshotBackupsResp.

        快照ID。

        :param id: The id of this ListSnapshotBackupsResp.
        :type id: str
        """
        self._id = id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListSnapshotBackupsResp.

        集群ID。

        :return: The cluster_id of this ListSnapshotBackupsResp.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListSnapshotBackupsResp.

        集群ID。

        :param cluster_id: The cluster_id of this ListSnapshotBackupsResp.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ListSnapshotBackupsResp.

        集群名字。

        :return: The cluster_name of this ListSnapshotBackupsResp.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ListSnapshotBackupsResp.

        集群名字。

        :param cluster_name: The cluster_name of this ListSnapshotBackupsResp.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def name(self):
        """Gets the name of this ListSnapshotBackupsResp.

        快照名称。

        :return: The name of this ListSnapshotBackupsResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListSnapshotBackupsResp.

        快照名称。

        :param name: The name of this ListSnapshotBackupsResp.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListSnapshotBackupsResp.

        快照状态。

        :return: The status of this ListSnapshotBackupsResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListSnapshotBackupsResp.

        快照状态。

        :param status: The status of this ListSnapshotBackupsResp.
        :type status: str
        """
        self._status = status

    @property
    def updated(self):
        """Gets the updated of this ListSnapshotBackupsResp.

        快照更新时间，格式为ISO8601：CCYY-MM-DDThh:mm:ss。

        :return: The updated of this ListSnapshotBackupsResp.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ListSnapshotBackupsResp.

        快照更新时间，格式为ISO8601：CCYY-MM-DDThh:mm:ss。

        :param updated: The updated of this ListSnapshotBackupsResp.
        :type updated: str
        """
        self._updated = updated

    @property
    def backup_type(self):
        """Gets the backup_type of this ListSnapshotBackupsResp.

        快照创建类型： - 0：表示自动创建。 - 1：表示手动创建。

        :return: The backup_type of this ListSnapshotBackupsResp.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this ListSnapshotBackupsResp.

        快照创建类型： - 0：表示自动创建。 - 1：表示手动创建。

        :param backup_type: The backup_type of this ListSnapshotBackupsResp.
        :type backup_type: str
        """
        self._backup_type = backup_type

    @property
    def backup_method(self):
        """Gets the backup_method of this ListSnapshotBackupsResp.

        创建快照方式。

        :return: The backup_method of this ListSnapshotBackupsResp.
        :rtype: str
        """
        return self._backup_method

    @backup_method.setter
    def backup_method(self, backup_method):
        """Sets the backup_method of this ListSnapshotBackupsResp.

        创建快照方式。

        :param backup_method: The backup_method of this ListSnapshotBackupsResp.
        :type backup_method: str
        """
        self._backup_method = backup_method

    @property
    def backup_expected_start_time(self):
        """Gets the backup_expected_start_time of this ListSnapshotBackupsResp.

        快照开始执行时间。

        :return: The backup_expected_start_time of this ListSnapshotBackupsResp.
        :rtype: str
        """
        return self._backup_expected_start_time

    @backup_expected_start_time.setter
    def backup_expected_start_time(self, backup_expected_start_time):
        """Sets the backup_expected_start_time of this ListSnapshotBackupsResp.

        快照开始执行时间。

        :param backup_expected_start_time: The backup_expected_start_time of this ListSnapshotBackupsResp.
        :type backup_expected_start_time: str
        """
        self._backup_expected_start_time = backup_expected_start_time

    @property
    def backup_keep_day(self):
        """Gets the backup_keep_day of this ListSnapshotBackupsResp.

        快照保留时间。

        :return: The backup_keep_day of this ListSnapshotBackupsResp.
        :rtype: int
        """
        return self._backup_keep_day

    @backup_keep_day.setter
    def backup_keep_day(self, backup_keep_day):
        """Sets the backup_keep_day of this ListSnapshotBackupsResp.

        快照保留时间。

        :param backup_keep_day: The backup_keep_day of this ListSnapshotBackupsResp.
        :type backup_keep_day: int
        """
        self._backup_keep_day = backup_keep_day

    @property
    def backup_period(self):
        """Gets the backup_period of this ListSnapshotBackupsResp.

        快照每天执行的时间点。

        :return: The backup_period of this ListSnapshotBackupsResp.
        :rtype: str
        """
        return self._backup_period

    @backup_period.setter
    def backup_period(self, backup_period):
        """Sets the backup_period of this ListSnapshotBackupsResp.

        快照每天执行的时间点。

        :param backup_period: The backup_period of this ListSnapshotBackupsResp.
        :type backup_period: str
        """
        self._backup_period = backup_period

    @property
    def indices(self):
        """Gets the indices of this ListSnapshotBackupsResp.

        要备份的索引。

        :return: The indices of this ListSnapshotBackupsResp.
        :rtype: str
        """
        return self._indices

    @indices.setter
    def indices(self, indices):
        """Sets the indices of this ListSnapshotBackupsResp.

        要备份的索引。

        :param indices: The indices of this ListSnapshotBackupsResp.
        :type indices: str
        """
        self._indices = indices

    @property
    def total_shards(self):
        """Gets the total_shards of this ListSnapshotBackupsResp.

        要备份的索引的总shard数。

        :return: The total_shards of this ListSnapshotBackupsResp.
        :rtype: int
        """
        return self._total_shards

    @total_shards.setter
    def total_shards(self, total_shards):
        """Sets the total_shards of this ListSnapshotBackupsResp.

        要备份的索引的总shard数。

        :param total_shards: The total_shards of this ListSnapshotBackupsResp.
        :type total_shards: int
        """
        self._total_shards = total_shards

    @property
    def failed_shards(self):
        """Gets the failed_shards of this ListSnapshotBackupsResp.

        备份失败的shard数。

        :return: The failed_shards of this ListSnapshotBackupsResp.
        :rtype: int
        """
        return self._failed_shards

    @failed_shards.setter
    def failed_shards(self, failed_shards):
        """Sets the failed_shards of this ListSnapshotBackupsResp.

        备份失败的shard数。

        :param failed_shards: The failed_shards of this ListSnapshotBackupsResp.
        :type failed_shards: int
        """
        self._failed_shards = failed_shards

    @property
    def version(self):
        """Gets the version of this ListSnapshotBackupsResp.

        快照的版本。

        :return: The version of this ListSnapshotBackupsResp.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListSnapshotBackupsResp.

        快照的版本。

        :param version: The version of this ListSnapshotBackupsResp.
        :type version: str
        """
        self._version = version

    @property
    def restore_status(self):
        """Gets the restore_status of this ListSnapshotBackupsResp.

        快照恢复的状态。

        :return: The restore_status of this ListSnapshotBackupsResp.
        :rtype: str
        """
        return self._restore_status

    @restore_status.setter
    def restore_status(self, restore_status):
        """Sets the restore_status of this ListSnapshotBackupsResp.

        快照恢复的状态。

        :param restore_status: The restore_status of this ListSnapshotBackupsResp.
        :type restore_status: str
        """
        self._restore_status = restore_status

    @property
    def start_time(self):
        """Gets the start_time of this ListSnapshotBackupsResp.

        快照开始执行的时间戳。

        :return: The start_time of this ListSnapshotBackupsResp.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListSnapshotBackupsResp.

        快照开始执行的时间戳。

        :param start_time: The start_time of this ListSnapshotBackupsResp.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListSnapshotBackupsResp.

        快照执行结束的时间戳。

        :return: The end_time of this ListSnapshotBackupsResp.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListSnapshotBackupsResp.

        快照执行结束的时间戳。

        :param end_time: The end_time of this ListSnapshotBackupsResp.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def bucket_name(self):
        """Gets the bucket_name of this ListSnapshotBackupsResp.

        保存快照数据的桶名。

        :return: The bucket_name of this ListSnapshotBackupsResp.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this ListSnapshotBackupsResp.

        保存快照数据的桶名。

        :param bucket_name: The bucket_name of this ListSnapshotBackupsResp.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

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
        if not isinstance(other, ListSnapshotBackupsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
