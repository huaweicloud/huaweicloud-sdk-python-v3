# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SnapshotDetail:

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
        'finished': 'str',
        'size': 'float',
        'status': 'str',
        'type': 'str',
        'cluster_id': 'str',
        'datastore': 'Datastore',
        'cluster_name': 'str',
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
        'finished': 'finished',
        'size': 'size',
        'status': 'status',
        'type': 'type',
        'cluster_id': 'cluster_id',
        'datastore': 'datastore',
        'cluster_name': 'cluster_name',
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

    def __init__(self, id=None, name=None, description=None, started=None, finished=None, size=None, status=None, type=None, cluster_id=None, datastore=None, cluster_name=None, bak_expected_start_time=None, bak_keep_day=None, bak_period=None, db_user=None, progress=None, backup_key=None, prior_backup_key=None, base_backup_key=None, backup_device=None, total_backup_size=None, base_backup_name=None, support_inplace_restore=None, fine_grained_backup=None, backup_level=None, fine_grained_backup_detail=None, guest_agent_version=None, cluster_status=None):
        """SnapshotDetail

        The model defined in huaweicloud sdk

        :param id: 快照ID。
        :type id: str
        :param name: 快照名称。
        :type name: str
        :param description: 快照描述。
        :type description: str
        :param started: 快照创建的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。
        :type started: str
        :param finished: 快照完成的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。
        :type finished: str
        :param size: 快照大小，单位GB。
        :type size: float
        :param status: 快照状态： - CREATING：创建中。 - AVAILABLE：可用。 - UNAVAILABLE：不可用。
        :type status: str
        :param type: 快照创建类型。
        :type type: str
        :param cluster_id: 快照对应的集群ID
        :type cluster_id: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkdws.v2.Datastore`
        :param cluster_name: 快照对应的集群名称。
        :type cluster_name: str
        :param bak_expected_start_time: 快照预计开始时间。
        :type bak_expected_start_time: str
        :param bak_keep_day: 快照保留天数。
        :type bak_keep_day: int
        :param bak_period: 快照策略。
        :type bak_period: str
        :param db_user: 数据库用户。
        :type db_user: str
        :param progress: 快照进度。
        :type progress: str
        :param backup_key: 快照BakcupKey。
        :type backup_key: str
        :param prior_backup_key: 增量快照，使用的前一个快照BakcupKey。
        :type prior_backup_key: str
        :param base_backup_key: 对应全量快照BakcupKey。
        :type base_backup_key: str
        :param backup_device: 备份介质。
        :type backup_device: str
        :param total_backup_size: 累计快照大小。
        :type total_backup_size: int
        :param base_backup_name: 对应全量快照名称。
        :type base_backup_name: str
        :param support_inplace_restore: 是否支持就地恢复。
        :type support_inplace_restore: bool
        :param fine_grained_backup: 是否是细粒度备份。
        :type fine_grained_backup: bool
        :param backup_level: 备份级别。
        :type backup_level: str
        :param fine_grained_backup_detail: 
        :type fine_grained_backup_detail: :class:`huaweicloudsdkdws.v2.FineGrainedSnapshotDetail`
        :param guest_agent_version: guestAgent版本。
        :type guest_agent_version: str
        :param cluster_status: 集群状态。
        :type cluster_status: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._started = None
        self._finished = None
        self._size = None
        self._status = None
        self._type = None
        self._cluster_id = None
        self._datastore = None
        self._cluster_name = None
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

        self.id = id
        self.name = name
        self.description = description
        self.started = started
        self.finished = finished
        self.size = size
        self.status = status
        self.type = type
        self.cluster_id = cluster_id
        if datastore is not None:
            self.datastore = datastore
        if cluster_name is not None:
            self.cluster_name = cluster_name
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
        """Gets the id of this SnapshotDetail.

        快照ID。

        :return: The id of this SnapshotDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnapshotDetail.

        快照ID。

        :param id: The id of this SnapshotDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this SnapshotDetail.

        快照名称。

        :return: The name of this SnapshotDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnapshotDetail.

        快照名称。

        :param name: The name of this SnapshotDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this SnapshotDetail.

        快照描述。

        :return: The description of this SnapshotDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SnapshotDetail.

        快照描述。

        :param description: The description of this SnapshotDetail.
        :type description: str
        """
        self._description = description

    @property
    def started(self):
        """Gets the started of this SnapshotDetail.

        快照创建的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。

        :return: The started of this SnapshotDetail.
        :rtype: str
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this SnapshotDetail.

        快照创建的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。

        :param started: The started of this SnapshotDetail.
        :type started: str
        """
        self._started = started

    @property
    def finished(self):
        """Gets the finished of this SnapshotDetail.

        快照完成的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。

        :return: The finished of this SnapshotDetail.
        :rtype: str
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """Sets the finished of this SnapshotDetail.

        快照完成的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。

        :param finished: The finished of this SnapshotDetail.
        :type finished: str
        """
        self._finished = finished

    @property
    def size(self):
        """Gets the size of this SnapshotDetail.

        快照大小，单位GB。

        :return: The size of this SnapshotDetail.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SnapshotDetail.

        快照大小，单位GB。

        :param size: The size of this SnapshotDetail.
        :type size: float
        """
        self._size = size

    @property
    def status(self):
        """Gets the status of this SnapshotDetail.

        快照状态： - CREATING：创建中。 - AVAILABLE：可用。 - UNAVAILABLE：不可用。

        :return: The status of this SnapshotDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SnapshotDetail.

        快照状态： - CREATING：创建中。 - AVAILABLE：可用。 - UNAVAILABLE：不可用。

        :param status: The status of this SnapshotDetail.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this SnapshotDetail.

        快照创建类型。

        :return: The type of this SnapshotDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SnapshotDetail.

        快照创建类型。

        :param type: The type of this SnapshotDetail.
        :type type: str
        """
        self._type = type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this SnapshotDetail.

        快照对应的集群ID

        :return: The cluster_id of this SnapshotDetail.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this SnapshotDetail.

        快照对应的集群ID

        :param cluster_id: The cluster_id of this SnapshotDetail.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def datastore(self):
        """Gets the datastore of this SnapshotDetail.

        :return: The datastore of this SnapshotDetail.
        :rtype: :class:`huaweicloudsdkdws.v2.Datastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this SnapshotDetail.

        :param datastore: The datastore of this SnapshotDetail.
        :type datastore: :class:`huaweicloudsdkdws.v2.Datastore`
        """
        self._datastore = datastore

    @property
    def cluster_name(self):
        """Gets the cluster_name of this SnapshotDetail.

        快照对应的集群名称。

        :return: The cluster_name of this SnapshotDetail.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this SnapshotDetail.

        快照对应的集群名称。

        :param cluster_name: The cluster_name of this SnapshotDetail.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def bak_expected_start_time(self):
        """Gets the bak_expected_start_time of this SnapshotDetail.

        快照预计开始时间。

        :return: The bak_expected_start_time of this SnapshotDetail.
        :rtype: str
        """
        return self._bak_expected_start_time

    @bak_expected_start_time.setter
    def bak_expected_start_time(self, bak_expected_start_time):
        """Sets the bak_expected_start_time of this SnapshotDetail.

        快照预计开始时间。

        :param bak_expected_start_time: The bak_expected_start_time of this SnapshotDetail.
        :type bak_expected_start_time: str
        """
        self._bak_expected_start_time = bak_expected_start_time

    @property
    def bak_keep_day(self):
        """Gets the bak_keep_day of this SnapshotDetail.

        快照保留天数。

        :return: The bak_keep_day of this SnapshotDetail.
        :rtype: int
        """
        return self._bak_keep_day

    @bak_keep_day.setter
    def bak_keep_day(self, bak_keep_day):
        """Sets the bak_keep_day of this SnapshotDetail.

        快照保留天数。

        :param bak_keep_day: The bak_keep_day of this SnapshotDetail.
        :type bak_keep_day: int
        """
        self._bak_keep_day = bak_keep_day

    @property
    def bak_period(self):
        """Gets the bak_period of this SnapshotDetail.

        快照策略。

        :return: The bak_period of this SnapshotDetail.
        :rtype: str
        """
        return self._bak_period

    @bak_period.setter
    def bak_period(self, bak_period):
        """Sets the bak_period of this SnapshotDetail.

        快照策略。

        :param bak_period: The bak_period of this SnapshotDetail.
        :type bak_period: str
        """
        self._bak_period = bak_period

    @property
    def db_user(self):
        """Gets the db_user of this SnapshotDetail.

        数据库用户。

        :return: The db_user of this SnapshotDetail.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        """Sets the db_user of this SnapshotDetail.

        数据库用户。

        :param db_user: The db_user of this SnapshotDetail.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def progress(self):
        """Gets the progress of this SnapshotDetail.

        快照进度。

        :return: The progress of this SnapshotDetail.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this SnapshotDetail.

        快照进度。

        :param progress: The progress of this SnapshotDetail.
        :type progress: str
        """
        self._progress = progress

    @property
    def backup_key(self):
        """Gets the backup_key of this SnapshotDetail.

        快照BakcupKey。

        :return: The backup_key of this SnapshotDetail.
        :rtype: str
        """
        return self._backup_key

    @backup_key.setter
    def backup_key(self, backup_key):
        """Sets the backup_key of this SnapshotDetail.

        快照BakcupKey。

        :param backup_key: The backup_key of this SnapshotDetail.
        :type backup_key: str
        """
        self._backup_key = backup_key

    @property
    def prior_backup_key(self):
        """Gets the prior_backup_key of this SnapshotDetail.

        增量快照，使用的前一个快照BakcupKey。

        :return: The prior_backup_key of this SnapshotDetail.
        :rtype: str
        """
        return self._prior_backup_key

    @prior_backup_key.setter
    def prior_backup_key(self, prior_backup_key):
        """Sets the prior_backup_key of this SnapshotDetail.

        增量快照，使用的前一个快照BakcupKey。

        :param prior_backup_key: The prior_backup_key of this SnapshotDetail.
        :type prior_backup_key: str
        """
        self._prior_backup_key = prior_backup_key

    @property
    def base_backup_key(self):
        """Gets the base_backup_key of this SnapshotDetail.

        对应全量快照BakcupKey。

        :return: The base_backup_key of this SnapshotDetail.
        :rtype: str
        """
        return self._base_backup_key

    @base_backup_key.setter
    def base_backup_key(self, base_backup_key):
        """Sets the base_backup_key of this SnapshotDetail.

        对应全量快照BakcupKey。

        :param base_backup_key: The base_backup_key of this SnapshotDetail.
        :type base_backup_key: str
        """
        self._base_backup_key = base_backup_key

    @property
    def backup_device(self):
        """Gets the backup_device of this SnapshotDetail.

        备份介质。

        :return: The backup_device of this SnapshotDetail.
        :rtype: str
        """
        return self._backup_device

    @backup_device.setter
    def backup_device(self, backup_device):
        """Sets the backup_device of this SnapshotDetail.

        备份介质。

        :param backup_device: The backup_device of this SnapshotDetail.
        :type backup_device: str
        """
        self._backup_device = backup_device

    @property
    def total_backup_size(self):
        """Gets the total_backup_size of this SnapshotDetail.

        累计快照大小。

        :return: The total_backup_size of this SnapshotDetail.
        :rtype: int
        """
        return self._total_backup_size

    @total_backup_size.setter
    def total_backup_size(self, total_backup_size):
        """Sets the total_backup_size of this SnapshotDetail.

        累计快照大小。

        :param total_backup_size: The total_backup_size of this SnapshotDetail.
        :type total_backup_size: int
        """
        self._total_backup_size = total_backup_size

    @property
    def base_backup_name(self):
        """Gets the base_backup_name of this SnapshotDetail.

        对应全量快照名称。

        :return: The base_backup_name of this SnapshotDetail.
        :rtype: str
        """
        return self._base_backup_name

    @base_backup_name.setter
    def base_backup_name(self, base_backup_name):
        """Sets the base_backup_name of this SnapshotDetail.

        对应全量快照名称。

        :param base_backup_name: The base_backup_name of this SnapshotDetail.
        :type base_backup_name: str
        """
        self._base_backup_name = base_backup_name

    @property
    def support_inplace_restore(self):
        """Gets the support_inplace_restore of this SnapshotDetail.

        是否支持就地恢复。

        :return: The support_inplace_restore of this SnapshotDetail.
        :rtype: bool
        """
        return self._support_inplace_restore

    @support_inplace_restore.setter
    def support_inplace_restore(self, support_inplace_restore):
        """Sets the support_inplace_restore of this SnapshotDetail.

        是否支持就地恢复。

        :param support_inplace_restore: The support_inplace_restore of this SnapshotDetail.
        :type support_inplace_restore: bool
        """
        self._support_inplace_restore = support_inplace_restore

    @property
    def fine_grained_backup(self):
        """Gets the fine_grained_backup of this SnapshotDetail.

        是否是细粒度备份。

        :return: The fine_grained_backup of this SnapshotDetail.
        :rtype: bool
        """
        return self._fine_grained_backup

    @fine_grained_backup.setter
    def fine_grained_backup(self, fine_grained_backup):
        """Sets the fine_grained_backup of this SnapshotDetail.

        是否是细粒度备份。

        :param fine_grained_backup: The fine_grained_backup of this SnapshotDetail.
        :type fine_grained_backup: bool
        """
        self._fine_grained_backup = fine_grained_backup

    @property
    def backup_level(self):
        """Gets the backup_level of this SnapshotDetail.

        备份级别。

        :return: The backup_level of this SnapshotDetail.
        :rtype: str
        """
        return self._backup_level

    @backup_level.setter
    def backup_level(self, backup_level):
        """Sets the backup_level of this SnapshotDetail.

        备份级别。

        :param backup_level: The backup_level of this SnapshotDetail.
        :type backup_level: str
        """
        self._backup_level = backup_level

    @property
    def fine_grained_backup_detail(self):
        """Gets the fine_grained_backup_detail of this SnapshotDetail.

        :return: The fine_grained_backup_detail of this SnapshotDetail.
        :rtype: :class:`huaweicloudsdkdws.v2.FineGrainedSnapshotDetail`
        """
        return self._fine_grained_backup_detail

    @fine_grained_backup_detail.setter
    def fine_grained_backup_detail(self, fine_grained_backup_detail):
        """Sets the fine_grained_backup_detail of this SnapshotDetail.

        :param fine_grained_backup_detail: The fine_grained_backup_detail of this SnapshotDetail.
        :type fine_grained_backup_detail: :class:`huaweicloudsdkdws.v2.FineGrainedSnapshotDetail`
        """
        self._fine_grained_backup_detail = fine_grained_backup_detail

    @property
    def guest_agent_version(self):
        """Gets the guest_agent_version of this SnapshotDetail.

        guestAgent版本。

        :return: The guest_agent_version of this SnapshotDetail.
        :rtype: str
        """
        return self._guest_agent_version

    @guest_agent_version.setter
    def guest_agent_version(self, guest_agent_version):
        """Sets the guest_agent_version of this SnapshotDetail.

        guestAgent版本。

        :param guest_agent_version: The guest_agent_version of this SnapshotDetail.
        :type guest_agent_version: str
        """
        self._guest_agent_version = guest_agent_version

    @property
    def cluster_status(self):
        """Gets the cluster_status of this SnapshotDetail.

        集群状态。

        :return: The cluster_status of this SnapshotDetail.
        :rtype: str
        """
        return self._cluster_status

    @cluster_status.setter
    def cluster_status(self, cluster_status):
        """Sets the cluster_status of this SnapshotDetail.

        集群状态。

        :param cluster_status: The cluster_status of this SnapshotDetail.
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
        if not isinstance(other, SnapshotDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
