# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisasterRecoveryCluster:

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
        'cluster_az': 'str',
        'role': 'str',
        'region': 'str',
        'status': 'str',
        'progress': 'str',
        'last_success_time': 'str',
        'obs_bucket_name': 'str',
        'datastore_version': 'str',
        'datastore_type': 'str',
        'disk_capacity': 'str',
        'disk_used': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'cluster_az': 'cluster_az',
        'role': 'role',
        'region': 'region',
        'status': 'status',
        'progress': 'progress',
        'last_success_time': 'last_success_time',
        'obs_bucket_name': 'obs_bucket_name',
        'datastore_version': 'datastore_version',
        'datastore_type': 'datastore_type',
        'disk_capacity': 'disk_capacity',
        'disk_used': 'disk_used'
    }

    def __init__(self, id=None, name=None, cluster_az=None, role=None, region=None, status=None, progress=None, last_success_time=None, obs_bucket_name=None, datastore_version=None, datastore_type=None, disk_capacity=None, disk_used=None):
        r"""DisasterRecoveryCluster

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 容灾集群信息ID。 **取值范围**： 不涉及。
        :type id: str
        :param name: **参数解释**： 容灾集群名称。 **取值范围**： 不涉及。
        :type name: str
        :param cluster_az: **参数解释**： 容灾集群所在可用区。 **取值范围**： 不涉及。
        :type cluster_az: str
        :param role: **参数解释**： 容灾集群角色。 **取值范围**： 不涉及。
        :type role: str
        :param region: **参数解释**： 容灾集群所在region。 **取值范围**： 不涉及。
        :type region: str
        :param status: **参数解释**： 容灾集群状态。 **取值范围**： - backuping，备份运行中。 - restoring，恢复运行中。 - stopped，集群已停止。 - waiting，容灾运行中。 - abnormal，容灾异常。 - drDeleted，容灾已删除。
        :type status: str
        :param progress: **参数解释**： 容灾进度。 **取值范围**： 不涉及。
        :type progress: str
        :param last_success_time: **参数解释**： 上一次容灾时间。 **取值范围**： 不涉及。
        :type last_success_time: str
        :param obs_bucket_name: **参数解释**： OBS桶名称。 **取值范围**： 不涉及。
        :type obs_bucket_name: str
        :param datastore_version: **参数解释**： 数据库版本。 **取值范围**： 不涉及。
        :type datastore_version: str
        :param datastore_type: **参数解释**： 数据库类型。 **取值范围**： 不涉及。
        :type datastore_type: str
        :param disk_capacity: **参数解释**： 磁盘容量。 **取值范围**： 不涉及。
        :type disk_capacity: str
        :param disk_used: **参数解释**： 磁盘使用率。 **取值范围**： 不涉及。
        :type disk_used: str
        """
        
        

        self._id = None
        self._name = None
        self._cluster_az = None
        self._role = None
        self._region = None
        self._status = None
        self._progress = None
        self._last_success_time = None
        self._obs_bucket_name = None
        self._datastore_version = None
        self._datastore_type = None
        self._disk_capacity = None
        self._disk_used = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if cluster_az is not None:
            self.cluster_az = cluster_az
        if role is not None:
            self.role = role
        if region is not None:
            self.region = region
        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if last_success_time is not None:
            self.last_success_time = last_success_time
        if obs_bucket_name is not None:
            self.obs_bucket_name = obs_bucket_name
        if datastore_version is not None:
            self.datastore_version = datastore_version
        if datastore_type is not None:
            self.datastore_type = datastore_type
        if disk_capacity is not None:
            self.disk_capacity = disk_capacity
        if disk_used is not None:
            self.disk_used = disk_used

    @property
    def id(self):
        r"""Gets the id of this DisasterRecoveryCluster.

        **参数解释**： 容灾集群信息ID。 **取值范围**： 不涉及。

        :return: The id of this DisasterRecoveryCluster.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DisasterRecoveryCluster.

        **参数解释**： 容灾集群信息ID。 **取值范围**： 不涉及。

        :param id: The id of this DisasterRecoveryCluster.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DisasterRecoveryCluster.

        **参数解释**： 容灾集群名称。 **取值范围**： 不涉及。

        :return: The name of this DisasterRecoveryCluster.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DisasterRecoveryCluster.

        **参数解释**： 容灾集群名称。 **取值范围**： 不涉及。

        :param name: The name of this DisasterRecoveryCluster.
        :type name: str
        """
        self._name = name

    @property
    def cluster_az(self):
        r"""Gets the cluster_az of this DisasterRecoveryCluster.

        **参数解释**： 容灾集群所在可用区。 **取值范围**： 不涉及。

        :return: The cluster_az of this DisasterRecoveryCluster.
        :rtype: str
        """
        return self._cluster_az

    @cluster_az.setter
    def cluster_az(self, cluster_az):
        r"""Sets the cluster_az of this DisasterRecoveryCluster.

        **参数解释**： 容灾集群所在可用区。 **取值范围**： 不涉及。

        :param cluster_az: The cluster_az of this DisasterRecoveryCluster.
        :type cluster_az: str
        """
        self._cluster_az = cluster_az

    @property
    def role(self):
        r"""Gets the role of this DisasterRecoveryCluster.

        **参数解释**： 容灾集群角色。 **取值范围**： 不涉及。

        :return: The role of this DisasterRecoveryCluster.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this DisasterRecoveryCluster.

        **参数解释**： 容灾集群角色。 **取值范围**： 不涉及。

        :param role: The role of this DisasterRecoveryCluster.
        :type role: str
        """
        self._role = role

    @property
    def region(self):
        r"""Gets the region of this DisasterRecoveryCluster.

        **参数解释**： 容灾集群所在region。 **取值范围**： 不涉及。

        :return: The region of this DisasterRecoveryCluster.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this DisasterRecoveryCluster.

        **参数解释**： 容灾集群所在region。 **取值范围**： 不涉及。

        :param region: The region of this DisasterRecoveryCluster.
        :type region: str
        """
        self._region = region

    @property
    def status(self):
        r"""Gets the status of this DisasterRecoveryCluster.

        **参数解释**： 容灾集群状态。 **取值范围**： - backuping，备份运行中。 - restoring，恢复运行中。 - stopped，集群已停止。 - waiting，容灾运行中。 - abnormal，容灾异常。 - drDeleted，容灾已删除。

        :return: The status of this DisasterRecoveryCluster.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DisasterRecoveryCluster.

        **参数解释**： 容灾集群状态。 **取值范围**： - backuping，备份运行中。 - restoring，恢复运行中。 - stopped，集群已停止。 - waiting，容灾运行中。 - abnormal，容灾异常。 - drDeleted，容灾已删除。

        :param status: The status of this DisasterRecoveryCluster.
        :type status: str
        """
        self._status = status

    @property
    def progress(self):
        r"""Gets the progress of this DisasterRecoveryCluster.

        **参数解释**： 容灾进度。 **取值范围**： 不涉及。

        :return: The progress of this DisasterRecoveryCluster.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this DisasterRecoveryCluster.

        **参数解释**： 容灾进度。 **取值范围**： 不涉及。

        :param progress: The progress of this DisasterRecoveryCluster.
        :type progress: str
        """
        self._progress = progress

    @property
    def last_success_time(self):
        r"""Gets the last_success_time of this DisasterRecoveryCluster.

        **参数解释**： 上一次容灾时间。 **取值范围**： 不涉及。

        :return: The last_success_time of this DisasterRecoveryCluster.
        :rtype: str
        """
        return self._last_success_time

    @last_success_time.setter
    def last_success_time(self, last_success_time):
        r"""Sets the last_success_time of this DisasterRecoveryCluster.

        **参数解释**： 上一次容灾时间。 **取值范围**： 不涉及。

        :param last_success_time: The last_success_time of this DisasterRecoveryCluster.
        :type last_success_time: str
        """
        self._last_success_time = last_success_time

    @property
    def obs_bucket_name(self):
        r"""Gets the obs_bucket_name of this DisasterRecoveryCluster.

        **参数解释**： OBS桶名称。 **取值范围**： 不涉及。

        :return: The obs_bucket_name of this DisasterRecoveryCluster.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        r"""Sets the obs_bucket_name of this DisasterRecoveryCluster.

        **参数解释**： OBS桶名称。 **取值范围**： 不涉及。

        :param obs_bucket_name: The obs_bucket_name of this DisasterRecoveryCluster.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def datastore_version(self):
        r"""Gets the datastore_version of this DisasterRecoveryCluster.

        **参数解释**： 数据库版本。 **取值范围**： 不涉及。

        :return: The datastore_version of this DisasterRecoveryCluster.
        :rtype: str
        """
        return self._datastore_version

    @datastore_version.setter
    def datastore_version(self, datastore_version):
        r"""Sets the datastore_version of this DisasterRecoveryCluster.

        **参数解释**： 数据库版本。 **取值范围**： 不涉及。

        :param datastore_version: The datastore_version of this DisasterRecoveryCluster.
        :type datastore_version: str
        """
        self._datastore_version = datastore_version

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this DisasterRecoveryCluster.

        **参数解释**： 数据库类型。 **取值范围**： 不涉及。

        :return: The datastore_type of this DisasterRecoveryCluster.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this DisasterRecoveryCluster.

        **参数解释**： 数据库类型。 **取值范围**： 不涉及。

        :param datastore_type: The datastore_type of this DisasterRecoveryCluster.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def disk_capacity(self):
        r"""Gets the disk_capacity of this DisasterRecoveryCluster.

        **参数解释**： 磁盘容量。 **取值范围**： 不涉及。

        :return: The disk_capacity of this DisasterRecoveryCluster.
        :rtype: str
        """
        return self._disk_capacity

    @disk_capacity.setter
    def disk_capacity(self, disk_capacity):
        r"""Sets the disk_capacity of this DisasterRecoveryCluster.

        **参数解释**： 磁盘容量。 **取值范围**： 不涉及。

        :param disk_capacity: The disk_capacity of this DisasterRecoveryCluster.
        :type disk_capacity: str
        """
        self._disk_capacity = disk_capacity

    @property
    def disk_used(self):
        r"""Gets the disk_used of this DisasterRecoveryCluster.

        **参数解释**： 磁盘使用率。 **取值范围**： 不涉及。

        :return: The disk_used of this DisasterRecoveryCluster.
        :rtype: str
        """
        return self._disk_used

    @disk_used.setter
    def disk_used(self, disk_used):
        r"""Sets the disk_used of this DisasterRecoveryCluster.

        **参数解释**： 磁盘使用率。 **取值范围**： 不涉及。

        :param disk_used: The disk_used of this DisasterRecoveryCluster.
        :type disk_used: str
        """
        self._disk_used = disk_used

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DisasterRecoveryCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
