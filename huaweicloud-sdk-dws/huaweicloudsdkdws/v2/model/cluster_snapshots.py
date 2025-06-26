# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterSnapshots:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'started': 'str',
        'size': 'float',
        'status': 'str',
        'cluster_id': 'str',
        'datastore': 'Datastore',
        'cluster_name': 'str',
        'updated': 'str',
        'type': 'str',
        'bak_expected_start_time': 'str',
        'bak_keep_day': 'int',
        'bak_period': 'str',
        'db_user': 'str',
        'progress': 'str',
        'backup_key': 'str',
        'prior_backup_key': 'str',
        'base_backup_key': 'str',
        'backup_device': 'str',
        'total_backup_size': 'int',
        'base_backup_name': 'str',
        'support_inplace_restore': 'bool',
        'fine_grained_backup': 'bool',
        'backup_level': 'str',
        'fine_grained_backup_detail': 'FineGrainedSnapshotDetail',
        'guest_agent_version': 'str',
        'cluster_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'started': 'started',
        'size': 'size',
        'status': 'status',
        'cluster_id': 'cluster_id',
        'datastore': 'datastore',
        'cluster_name': 'cluster_name',
        'updated': 'updated',
        'type': 'type',
        'bak_expected_start_time': 'bak_expected_start_time',
        'bak_keep_day': 'bak_keep_day',
        'bak_period': 'bak_period',
        'db_user': 'db_user',
        'progress': 'progress',
        'backup_key': 'backup_key',
        'prior_backup_key': 'prior_backup_key',
        'base_backup_key': 'base_backup_key',
        'backup_device': 'backup_device',
        'total_backup_size': 'total_backup_size',
        'base_backup_name': 'base_backup_name',
        'support_inplace_restore': 'support_inplace_restore',
        'fine_grained_backup': 'fine_grained_backup',
        'backup_level': 'backup_level',
        'fine_grained_backup_detail': 'fine_grained_backup_detail',
        'guest_agent_version': 'guest_agent_version',
        'cluster_status': 'cluster_status'
    }

    def __init__(self, id=None, name=None, description=None, started=None, size=None, status=None, cluster_id=None, datastore=None, cluster_name=None, updated=None, type=None, bak_expected_start_time=None, bak_keep_day=None, bak_period=None, db_user=None, progress=None, backup_key=None, prior_backup_key=None, base_backup_key=None, backup_device=None, total_backup_size=None, base_backup_name=None, support_inplace_restore=None, fine_grained_backup=None, backup_level=None, fine_grained_backup_detail=None, guest_agent_version=None, cluster_status=None):
        r"""ClusterSnapshots

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 快照ID。 **取值范围**： 不涉及。
        :type id: str
        :param name: **参数解释**： 快照名称。 **取值范围**： 不涉及。
        :type name: str
        :param description: **参数解释**： 快照描述。 **取值范围**： 不涉及。
        :type description: str
        :param started: **参数解释**： 快照创建的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。 **取值范围**： 不涉及。
        :type started: str
        :param size: **参数解释**： 快照大小，单位 GB。 **取值范围**： 不涉及。
        :type size: float
        :param status: **参数解释**： 快照状态。 **取值范围**： CREATING：创建中。 AVAILABLE：可用。 UNAVAILABLE：不可用。 RESTORING：恢复中。 FROZEN： 普通冻结。 POLICE_FROZEN： 公安冻结。
        :type status: str
        :param cluster_id: **参数解释**： 快照对应的集群ID。 **取值范围**： 不涉及。
        :type cluster_id: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkdws.v2.Datastore`
        :param cluster_name: **参数解释**： 快照对应的集群名称。 **取值范围**： 不涉及。
        :type cluster_name: str
        :param updated: **参数解释**： 快照更新时间。 **取值范围**： 不涉及。
        :type updated: str
        :param type: **参数解释**： 快照类型。 **取值范围**： MANUAL：手动快照。 AUTO：自动快照。
        :type type: str
        :param bak_expected_start_time: **参数解释**： 快照预计开始时间。 **取值范围**： 不涉及。
        :type bak_expected_start_time: str
        :param bak_keep_day: **参数解释**： 快照保留天数。 **取值范围**： 不涉及。
        :type bak_keep_day: int
        :param bak_period: **参数解释**： 快照策略。 **取值范围**： 不涉及。
        :type bak_period: str
        :param db_user: **参数解释**： 数据库用户。 **取值范围**： 不涉及。
        :type db_user: str
        :param progress: **参数解释**： 快照进度。 **取值范围**： 不涉及。
        :type progress: str
        :param backup_key: **参数解释**： 快照备份key。 **取值范围**： 不涉及。
        :type backup_key: str
        :param prior_backup_key: **参数解释**： 增量快照，使用的前一个快照备份key。 **取值范围**： 不涉及。
        :type prior_backup_key: str
        :param base_backup_key: **参数解释**： 对应全量快照备份key。 **取值范围**： 不涉及。
        :type base_backup_key: str
        :param backup_device: **参数解释**： 备份介质。 **取值范围**： 不涉及。
        :type backup_device: str
        :param total_backup_size: **参数解释**： 累计快照大小。 **取值范围**： 不涉及。
        :type total_backup_size: int
        :param base_backup_name: **参数解释**： 对应全量快照名称。 **取值范围**： 不涉及。
        :type base_backup_name: str
        :param support_inplace_restore: **参数解释**： 是否支持就地恢复。 **取值范围**： 不涉及。
        :type support_inplace_restore: bool
        :param fine_grained_backup: **参数解释**： 是否是细粒度备份。 **取值范围**： 不涉及。
        :type fine_grained_backup: bool
        :param backup_level: **参数解释**： 备份级别。 **取值范围**： 不涉及。
        :type backup_level: str
        :param fine_grained_backup_detail: 
        :type fine_grained_backup_detail: :class:`huaweicloudsdkdws.v2.FineGrainedSnapshotDetail`
        :param guest_agent_version: **参数解释**： guestAgent版本。 **取值范围**： 不涉及。
        :type guest_agent_version: str
        :param cluster_status: **参数解释**： 集群状态。 **取值范围**： 不涉及。
        :type cluster_status: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._started = None
        self._size = None
        self._status = None
        self._cluster_id = None
        self._datastore = None
        self._cluster_name = None
        self._updated = None
        self._type = None
        self._bak_expected_start_time = None
        self._bak_keep_day = None
        self._bak_period = None
        self._db_user = None
        self._progress = None
        self._backup_key = None
        self._prior_backup_key = None
        self._base_backup_key = None
        self._backup_device = None
        self._total_backup_size = None
        self._base_backup_name = None
        self._support_inplace_restore = None
        self._fine_grained_backup = None
        self._backup_level = None
        self._fine_grained_backup_detail = None
        self._guest_agent_version = None
        self._cluster_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if started is not None:
            self.started = started
        if size is not None:
            self.size = size
        if status is not None:
            self.status = status
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if datastore is not None:
            self.datastore = datastore
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if updated is not None:
            self.updated = updated
        if type is not None:
            self.type = type
        if bak_expected_start_time is not None:
            self.bak_expected_start_time = bak_expected_start_time
        if bak_keep_day is not None:
            self.bak_keep_day = bak_keep_day
        if bak_period is not None:
            self.bak_period = bak_period
        if db_user is not None:
            self.db_user = db_user
        if progress is not None:
            self.progress = progress
        if backup_key is not None:
            self.backup_key = backup_key
        if prior_backup_key is not None:
            self.prior_backup_key = prior_backup_key
        if base_backup_key is not None:
            self.base_backup_key = base_backup_key
        if backup_device is not None:
            self.backup_device = backup_device
        if total_backup_size is not None:
            self.total_backup_size = total_backup_size
        if base_backup_name is not None:
            self.base_backup_name = base_backup_name
        if support_inplace_restore is not None:
            self.support_inplace_restore = support_inplace_restore
        if fine_grained_backup is not None:
            self.fine_grained_backup = fine_grained_backup
        if backup_level is not None:
            self.backup_level = backup_level
        if fine_grained_backup_detail is not None:
            self.fine_grained_backup_detail = fine_grained_backup_detail
        if guest_agent_version is not None:
            self.guest_agent_version = guest_agent_version
        if cluster_status is not None:
            self.cluster_status = cluster_status

    @property
    def id(self):
        r"""Gets the id of this ClusterSnapshots.

        **参数解释**： 快照ID。 **取值范围**： 不涉及。

        :return: The id of this ClusterSnapshots.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ClusterSnapshots.

        **参数解释**： 快照ID。 **取值范围**： 不涉及。

        :param id: The id of this ClusterSnapshots.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ClusterSnapshots.

        **参数解释**： 快照名称。 **取值范围**： 不涉及。

        :return: The name of this ClusterSnapshots.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ClusterSnapshots.

        **参数解释**： 快照名称。 **取值范围**： 不涉及。

        :param name: The name of this ClusterSnapshots.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ClusterSnapshots.

        **参数解释**： 快照描述。 **取值范围**： 不涉及。

        :return: The description of this ClusterSnapshots.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ClusterSnapshots.

        **参数解释**： 快照描述。 **取值范围**： 不涉及。

        :param description: The description of this ClusterSnapshots.
        :type description: str
        """
        self._description = description

    @property
    def started(self):
        r"""Gets the started of this ClusterSnapshots.

        **参数解释**： 快照创建的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。 **取值范围**： 不涉及。

        :return: The started of this ClusterSnapshots.
        :rtype: str
        """
        return self._started

    @started.setter
    def started(self, started):
        r"""Sets the started of this ClusterSnapshots.

        **参数解释**： 快照创建的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。 **取值范围**： 不涉及。

        :param started: The started of this ClusterSnapshots.
        :type started: str
        """
        self._started = started

    @property
    def size(self):
        r"""Gets the size of this ClusterSnapshots.

        **参数解释**： 快照大小，单位 GB。 **取值范围**： 不涉及。

        :return: The size of this ClusterSnapshots.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ClusterSnapshots.

        **参数解释**： 快照大小，单位 GB。 **取值范围**： 不涉及。

        :param size: The size of this ClusterSnapshots.
        :type size: float
        """
        self._size = size

    @property
    def status(self):
        r"""Gets the status of this ClusterSnapshots.

        **参数解释**： 快照状态。 **取值范围**： CREATING：创建中。 AVAILABLE：可用。 UNAVAILABLE：不可用。 RESTORING：恢复中。 FROZEN： 普通冻结。 POLICE_FROZEN： 公安冻结。

        :return: The status of this ClusterSnapshots.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ClusterSnapshots.

        **参数解释**： 快照状态。 **取值范围**： CREATING：创建中。 AVAILABLE：可用。 UNAVAILABLE：不可用。 RESTORING：恢复中。 FROZEN： 普通冻结。 POLICE_FROZEN： 公安冻结。

        :param status: The status of this ClusterSnapshots.
        :type status: str
        """
        self._status = status

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ClusterSnapshots.

        **参数解释**： 快照对应的集群ID。 **取值范围**： 不涉及。

        :return: The cluster_id of this ClusterSnapshots.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ClusterSnapshots.

        **参数解释**： 快照对应的集群ID。 **取值范围**： 不涉及。

        :param cluster_id: The cluster_id of this ClusterSnapshots.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def datastore(self):
        r"""Gets the datastore of this ClusterSnapshots.

        :return: The datastore of this ClusterSnapshots.
        :rtype: :class:`huaweicloudsdkdws.v2.Datastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this ClusterSnapshots.

        :param datastore: The datastore of this ClusterSnapshots.
        :type datastore: :class:`huaweicloudsdkdws.v2.Datastore`
        """
        self._datastore = datastore

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ClusterSnapshots.

        **参数解释**： 快照对应的集群名称。 **取值范围**： 不涉及。

        :return: The cluster_name of this ClusterSnapshots.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ClusterSnapshots.

        **参数解释**： 快照对应的集群名称。 **取值范围**： 不涉及。

        :param cluster_name: The cluster_name of this ClusterSnapshots.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def updated(self):
        r"""Gets the updated of this ClusterSnapshots.

        **参数解释**： 快照更新时间。 **取值范围**： 不涉及。

        :return: The updated of this ClusterSnapshots.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ClusterSnapshots.

        **参数解释**： 快照更新时间。 **取值范围**： 不涉及。

        :param updated: The updated of this ClusterSnapshots.
        :type updated: str
        """
        self._updated = updated

    @property
    def type(self):
        r"""Gets the type of this ClusterSnapshots.

        **参数解释**： 快照类型。 **取值范围**： MANUAL：手动快照。 AUTO：自动快照。

        :return: The type of this ClusterSnapshots.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ClusterSnapshots.

        **参数解释**： 快照类型。 **取值范围**： MANUAL：手动快照。 AUTO：自动快照。

        :param type: The type of this ClusterSnapshots.
        :type type: str
        """
        self._type = type

    @property
    def bak_expected_start_time(self):
        r"""Gets the bak_expected_start_time of this ClusterSnapshots.

        **参数解释**： 快照预计开始时间。 **取值范围**： 不涉及。

        :return: The bak_expected_start_time of this ClusterSnapshots.
        :rtype: str
        """
        return self._bak_expected_start_time

    @bak_expected_start_time.setter
    def bak_expected_start_time(self, bak_expected_start_time):
        r"""Sets the bak_expected_start_time of this ClusterSnapshots.

        **参数解释**： 快照预计开始时间。 **取值范围**： 不涉及。

        :param bak_expected_start_time: The bak_expected_start_time of this ClusterSnapshots.
        :type bak_expected_start_time: str
        """
        self._bak_expected_start_time = bak_expected_start_time

    @property
    def bak_keep_day(self):
        r"""Gets the bak_keep_day of this ClusterSnapshots.

        **参数解释**： 快照保留天数。 **取值范围**： 不涉及。

        :return: The bak_keep_day of this ClusterSnapshots.
        :rtype: int
        """
        return self._bak_keep_day

    @bak_keep_day.setter
    def bak_keep_day(self, bak_keep_day):
        r"""Sets the bak_keep_day of this ClusterSnapshots.

        **参数解释**： 快照保留天数。 **取值范围**： 不涉及。

        :param bak_keep_day: The bak_keep_day of this ClusterSnapshots.
        :type bak_keep_day: int
        """
        self._bak_keep_day = bak_keep_day

    @property
    def bak_period(self):
        r"""Gets the bak_period of this ClusterSnapshots.

        **参数解释**： 快照策略。 **取值范围**： 不涉及。

        :return: The bak_period of this ClusterSnapshots.
        :rtype: str
        """
        return self._bak_period

    @bak_period.setter
    def bak_period(self, bak_period):
        r"""Sets the bak_period of this ClusterSnapshots.

        **参数解释**： 快照策略。 **取值范围**： 不涉及。

        :param bak_period: The bak_period of this ClusterSnapshots.
        :type bak_period: str
        """
        self._bak_period = bak_period

    @property
    def db_user(self):
        r"""Gets the db_user of this ClusterSnapshots.

        **参数解释**： 数据库用户。 **取值范围**： 不涉及。

        :return: The db_user of this ClusterSnapshots.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        r"""Sets the db_user of this ClusterSnapshots.

        **参数解释**： 数据库用户。 **取值范围**： 不涉及。

        :param db_user: The db_user of this ClusterSnapshots.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def progress(self):
        r"""Gets the progress of this ClusterSnapshots.

        **参数解释**： 快照进度。 **取值范围**： 不涉及。

        :return: The progress of this ClusterSnapshots.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this ClusterSnapshots.

        **参数解释**： 快照进度。 **取值范围**： 不涉及。

        :param progress: The progress of this ClusterSnapshots.
        :type progress: str
        """
        self._progress = progress

    @property
    def backup_key(self):
        r"""Gets the backup_key of this ClusterSnapshots.

        **参数解释**： 快照备份key。 **取值范围**： 不涉及。

        :return: The backup_key of this ClusterSnapshots.
        :rtype: str
        """
        return self._backup_key

    @backup_key.setter
    def backup_key(self, backup_key):
        r"""Sets the backup_key of this ClusterSnapshots.

        **参数解释**： 快照备份key。 **取值范围**： 不涉及。

        :param backup_key: The backup_key of this ClusterSnapshots.
        :type backup_key: str
        """
        self._backup_key = backup_key

    @property
    def prior_backup_key(self):
        r"""Gets the prior_backup_key of this ClusterSnapshots.

        **参数解释**： 增量快照，使用的前一个快照备份key。 **取值范围**： 不涉及。

        :return: The prior_backup_key of this ClusterSnapshots.
        :rtype: str
        """
        return self._prior_backup_key

    @prior_backup_key.setter
    def prior_backup_key(self, prior_backup_key):
        r"""Sets the prior_backup_key of this ClusterSnapshots.

        **参数解释**： 增量快照，使用的前一个快照备份key。 **取值范围**： 不涉及。

        :param prior_backup_key: The prior_backup_key of this ClusterSnapshots.
        :type prior_backup_key: str
        """
        self._prior_backup_key = prior_backup_key

    @property
    def base_backup_key(self):
        r"""Gets the base_backup_key of this ClusterSnapshots.

        **参数解释**： 对应全量快照备份key。 **取值范围**： 不涉及。

        :return: The base_backup_key of this ClusterSnapshots.
        :rtype: str
        """
        return self._base_backup_key

    @base_backup_key.setter
    def base_backup_key(self, base_backup_key):
        r"""Sets the base_backup_key of this ClusterSnapshots.

        **参数解释**： 对应全量快照备份key。 **取值范围**： 不涉及。

        :param base_backup_key: The base_backup_key of this ClusterSnapshots.
        :type base_backup_key: str
        """
        self._base_backup_key = base_backup_key

    @property
    def backup_device(self):
        r"""Gets the backup_device of this ClusterSnapshots.

        **参数解释**： 备份介质。 **取值范围**： 不涉及。

        :return: The backup_device of this ClusterSnapshots.
        :rtype: str
        """
        return self._backup_device

    @backup_device.setter
    def backup_device(self, backup_device):
        r"""Sets the backup_device of this ClusterSnapshots.

        **参数解释**： 备份介质。 **取值范围**： 不涉及。

        :param backup_device: The backup_device of this ClusterSnapshots.
        :type backup_device: str
        """
        self._backup_device = backup_device

    @property
    def total_backup_size(self):
        r"""Gets the total_backup_size of this ClusterSnapshots.

        **参数解释**： 累计快照大小。 **取值范围**： 不涉及。

        :return: The total_backup_size of this ClusterSnapshots.
        :rtype: int
        """
        return self._total_backup_size

    @total_backup_size.setter
    def total_backup_size(self, total_backup_size):
        r"""Sets the total_backup_size of this ClusterSnapshots.

        **参数解释**： 累计快照大小。 **取值范围**： 不涉及。

        :param total_backup_size: The total_backup_size of this ClusterSnapshots.
        :type total_backup_size: int
        """
        self._total_backup_size = total_backup_size

    @property
    def base_backup_name(self):
        r"""Gets the base_backup_name of this ClusterSnapshots.

        **参数解释**： 对应全量快照名称。 **取值范围**： 不涉及。

        :return: The base_backup_name of this ClusterSnapshots.
        :rtype: str
        """
        return self._base_backup_name

    @base_backup_name.setter
    def base_backup_name(self, base_backup_name):
        r"""Sets the base_backup_name of this ClusterSnapshots.

        **参数解释**： 对应全量快照名称。 **取值范围**： 不涉及。

        :param base_backup_name: The base_backup_name of this ClusterSnapshots.
        :type base_backup_name: str
        """
        self._base_backup_name = base_backup_name

    @property
    def support_inplace_restore(self):
        r"""Gets the support_inplace_restore of this ClusterSnapshots.

        **参数解释**： 是否支持就地恢复。 **取值范围**： 不涉及。

        :return: The support_inplace_restore of this ClusterSnapshots.
        :rtype: bool
        """
        return self._support_inplace_restore

    @support_inplace_restore.setter
    def support_inplace_restore(self, support_inplace_restore):
        r"""Sets the support_inplace_restore of this ClusterSnapshots.

        **参数解释**： 是否支持就地恢复。 **取值范围**： 不涉及。

        :param support_inplace_restore: The support_inplace_restore of this ClusterSnapshots.
        :type support_inplace_restore: bool
        """
        self._support_inplace_restore = support_inplace_restore

    @property
    def fine_grained_backup(self):
        r"""Gets the fine_grained_backup of this ClusterSnapshots.

        **参数解释**： 是否是细粒度备份。 **取值范围**： 不涉及。

        :return: The fine_grained_backup of this ClusterSnapshots.
        :rtype: bool
        """
        return self._fine_grained_backup

    @fine_grained_backup.setter
    def fine_grained_backup(self, fine_grained_backup):
        r"""Sets the fine_grained_backup of this ClusterSnapshots.

        **参数解释**： 是否是细粒度备份。 **取值范围**： 不涉及。

        :param fine_grained_backup: The fine_grained_backup of this ClusterSnapshots.
        :type fine_grained_backup: bool
        """
        self._fine_grained_backup = fine_grained_backup

    @property
    def backup_level(self):
        r"""Gets the backup_level of this ClusterSnapshots.

        **参数解释**： 备份级别。 **取值范围**： 不涉及。

        :return: The backup_level of this ClusterSnapshots.
        :rtype: str
        """
        return self._backup_level

    @backup_level.setter
    def backup_level(self, backup_level):
        r"""Sets the backup_level of this ClusterSnapshots.

        **参数解释**： 备份级别。 **取值范围**： 不涉及。

        :param backup_level: The backup_level of this ClusterSnapshots.
        :type backup_level: str
        """
        self._backup_level = backup_level

    @property
    def fine_grained_backup_detail(self):
        r"""Gets the fine_grained_backup_detail of this ClusterSnapshots.

        :return: The fine_grained_backup_detail of this ClusterSnapshots.
        :rtype: :class:`huaweicloudsdkdws.v2.FineGrainedSnapshotDetail`
        """
        return self._fine_grained_backup_detail

    @fine_grained_backup_detail.setter
    def fine_grained_backup_detail(self, fine_grained_backup_detail):
        r"""Sets the fine_grained_backup_detail of this ClusterSnapshots.

        :param fine_grained_backup_detail: The fine_grained_backup_detail of this ClusterSnapshots.
        :type fine_grained_backup_detail: :class:`huaweicloudsdkdws.v2.FineGrainedSnapshotDetail`
        """
        self._fine_grained_backup_detail = fine_grained_backup_detail

    @property
    def guest_agent_version(self):
        r"""Gets the guest_agent_version of this ClusterSnapshots.

        **参数解释**： guestAgent版本。 **取值范围**： 不涉及。

        :return: The guest_agent_version of this ClusterSnapshots.
        :rtype: str
        """
        return self._guest_agent_version

    @guest_agent_version.setter
    def guest_agent_version(self, guest_agent_version):
        r"""Sets the guest_agent_version of this ClusterSnapshots.

        **参数解释**： guestAgent版本。 **取值范围**： 不涉及。

        :param guest_agent_version: The guest_agent_version of this ClusterSnapshots.
        :type guest_agent_version: str
        """
        self._guest_agent_version = guest_agent_version

    @property
    def cluster_status(self):
        r"""Gets the cluster_status of this ClusterSnapshots.

        **参数解释**： 集群状态。 **取值范围**： 不涉及。

        :return: The cluster_status of this ClusterSnapshots.
        :rtype: str
        """
        return self._cluster_status

    @cluster_status.setter
    def cluster_status(self, cluster_status):
        r"""Sets the cluster_status of this ClusterSnapshots.

        **参数解释**： 集群状态。 **取值范围**： 不涉及。

        :param cluster_status: The cluster_status of this ClusterSnapshots.
        :type cluster_status: str
        """
        self._cluster_status = cluster_status

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
        if not isinstance(other, ClusterSnapshots):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
