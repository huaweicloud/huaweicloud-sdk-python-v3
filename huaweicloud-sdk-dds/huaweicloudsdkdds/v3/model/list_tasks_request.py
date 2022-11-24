# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'name': 'name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, start_time=None, end_time=None, status=None, name=None, offset=None, limit=None):
        """ListTasksRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始，Z指时区偏移量
        :type start_time: str
        :param end_time: 查询结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于查询开始时间，时间跨度不超过30天。 其中，T指某个时间的开始，Z指时区偏移量。
        :type end_time: str
        :param status: 任务状态： 取值为“Running”为执行中； 取值为“Completed”为完成； 取值为“Failed” 为失败。
        :type status: str
        :param name: 任务名称。对应取值如下： - \&quot;CreateMongoDB\&quot;：创建集群实例 - \&quot;CreateMongoDBReplica\&quot;：创建副本集实例 - \&quot;CreateMongoDBReplicaSingle\&quot;：创建单节点实例 - \&quot;EnlargeMongoDBVolume\&quot;：磁盘扩容 - \&quot;ResizeMongoDBInstance\&quot;：社区版实例规格变更 - \&quot;ResizeDfvMongoDBInstance\&quot;：社区增强版实例规格变更 - \&quot;EnlargeMongoDBGroup\&quot;：添加节点 - \&quot;ReplicaSetEnlargeNode\&quot;：副本集添加备节点 - \&quot;AddReadonlyNode\&quot;：添加只读节点 - \&quot;RestartInstance\&quot;：重启集群实例 - \&quot;RestartGroup\&quot;：重启集群节点组 - \&quot;RestartNode\&quot;：重启集群节点 - \&quot;RestartReplicaSetInstance\&quot;：重启副本集实例 - \&quot;RestartReplicaSingleInstance\&quot;：重启单节点实例 - \&quot;SwitchPrimary\&quot;：主备切换 - \&quot;ModifyIp\&quot;：修改内网地址 - \&quot;ModifySecurityGroup\&quot;：修改安全组 - \&quot;ModifyPort\&quot;：修改数据库端口 - \&quot;BindPublicIP\&quot;：绑定弹性IP - \&quot;UnbindPublicIP\&quot;：解绑弹性IP - \&quot;SwitchInstanceSSL\&quot;：切换SSL - \&quot;AzMigrate\&quot;：迁移可用区 - \&quot;CreateIp\&quot;：显示shard/config IP - \&quot;ModifyOpLogSize\&quot;：修改oplog大小 - \&quot;RestoreMongoDB\&quot;：集群恢复到新实例 - \&quot;RestoreMongoDB_Replica\&quot;：副本集恢复到新实例 - \&quot;RestoreMongoDB_Replica_Single\&quot;：单节点恢复到新实例 - \&quot;RestoreMongoDB_Replica_PITR\&quot;：副本集恢复到指定时间点 - \&quot;MongodbSnapshotBackup\&quot;：创建物理备份 - \&quot;MongodbSnapshotEBackup\&quot;：创建快照备份 - \&quot;MongodbRestoreData2CurrentInstance\&quot;：备份恢复到当前实例 - \&quot;MongodbRestoreData2NewInstance\&quot;：备份恢复到新实例 - \&quot;MongodbPitr2CurrentInstance\&quot;：备份恢复到当前实例指定时间点 - \&quot;MongodbPitr2NewInstance\&quot;：备份恢复到新实例指定时间点 - \&quot;MongodbRecycleBackup\&quot;：备份回收 - \&quot;MongodbRestoreTable\&quot;：库表级时间点恢复 - \&quot;UpgradeDatabaseVersion\&quot;：升级数据库补丁
        :type name: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为100，不能为负数，最小值为1，最大值为100。
        :type limit: int
        """
        
        

        self._start_time = None
        self._end_time = None
        self._status = None
        self._name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def start_time(self):
        """Gets the start_time of this ListTasksRequest.

        查询开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始，Z指时区偏移量

        :return: The start_time of this ListTasksRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListTasksRequest.

        查询开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始，Z指时区偏移量

        :param start_time: The start_time of this ListTasksRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListTasksRequest.

        查询结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于查询开始时间，时间跨度不超过30天。 其中，T指某个时间的开始，Z指时区偏移量。

        :return: The end_time of this ListTasksRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListTasksRequest.

        查询结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于查询开始时间，时间跨度不超过30天。 其中，T指某个时间的开始，Z指时区偏移量。

        :param end_time: The end_time of this ListTasksRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this ListTasksRequest.

        任务状态： 取值为“Running”为执行中； 取值为“Completed”为完成； 取值为“Failed” 为失败。

        :return: The status of this ListTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListTasksRequest.

        任务状态： 取值为“Running”为执行中； 取值为“Completed”为完成； 取值为“Failed” 为失败。

        :param status: The status of this ListTasksRequest.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this ListTasksRequest.

        任务名称。对应取值如下： - \"CreateMongoDB\"：创建集群实例 - \"CreateMongoDBReplica\"：创建副本集实例 - \"CreateMongoDBReplicaSingle\"：创建单节点实例 - \"EnlargeMongoDBVolume\"：磁盘扩容 - \"ResizeMongoDBInstance\"：社区版实例规格变更 - \"ResizeDfvMongoDBInstance\"：社区增强版实例规格变更 - \"EnlargeMongoDBGroup\"：添加节点 - \"ReplicaSetEnlargeNode\"：副本集添加备节点 - \"AddReadonlyNode\"：添加只读节点 - \"RestartInstance\"：重启集群实例 - \"RestartGroup\"：重启集群节点组 - \"RestartNode\"：重启集群节点 - \"RestartReplicaSetInstance\"：重启副本集实例 - \"RestartReplicaSingleInstance\"：重启单节点实例 - \"SwitchPrimary\"：主备切换 - \"ModifyIp\"：修改内网地址 - \"ModifySecurityGroup\"：修改安全组 - \"ModifyPort\"：修改数据库端口 - \"BindPublicIP\"：绑定弹性IP - \"UnbindPublicIP\"：解绑弹性IP - \"SwitchInstanceSSL\"：切换SSL - \"AzMigrate\"：迁移可用区 - \"CreateIp\"：显示shard/config IP - \"ModifyOpLogSize\"：修改oplog大小 - \"RestoreMongoDB\"：集群恢复到新实例 - \"RestoreMongoDB_Replica\"：副本集恢复到新实例 - \"RestoreMongoDB_Replica_Single\"：单节点恢复到新实例 - \"RestoreMongoDB_Replica_PITR\"：副本集恢复到指定时间点 - \"MongodbSnapshotBackup\"：创建物理备份 - \"MongodbSnapshotEBackup\"：创建快照备份 - \"MongodbRestoreData2CurrentInstance\"：备份恢复到当前实例 - \"MongodbRestoreData2NewInstance\"：备份恢复到新实例 - \"MongodbPitr2CurrentInstance\"：备份恢复到当前实例指定时间点 - \"MongodbPitr2NewInstance\"：备份恢复到新实例指定时间点 - \"MongodbRecycleBackup\"：备份回收 - \"MongodbRestoreTable\"：库表级时间点恢复 - \"UpgradeDatabaseVersion\"：升级数据库补丁

        :return: The name of this ListTasksRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListTasksRequest.

        任务名称。对应取值如下： - \"CreateMongoDB\"：创建集群实例 - \"CreateMongoDBReplica\"：创建副本集实例 - \"CreateMongoDBReplicaSingle\"：创建单节点实例 - \"EnlargeMongoDBVolume\"：磁盘扩容 - \"ResizeMongoDBInstance\"：社区版实例规格变更 - \"ResizeDfvMongoDBInstance\"：社区增强版实例规格变更 - \"EnlargeMongoDBGroup\"：添加节点 - \"ReplicaSetEnlargeNode\"：副本集添加备节点 - \"AddReadonlyNode\"：添加只读节点 - \"RestartInstance\"：重启集群实例 - \"RestartGroup\"：重启集群节点组 - \"RestartNode\"：重启集群节点 - \"RestartReplicaSetInstance\"：重启副本集实例 - \"RestartReplicaSingleInstance\"：重启单节点实例 - \"SwitchPrimary\"：主备切换 - \"ModifyIp\"：修改内网地址 - \"ModifySecurityGroup\"：修改安全组 - \"ModifyPort\"：修改数据库端口 - \"BindPublicIP\"：绑定弹性IP - \"UnbindPublicIP\"：解绑弹性IP - \"SwitchInstanceSSL\"：切换SSL - \"AzMigrate\"：迁移可用区 - \"CreateIp\"：显示shard/config IP - \"ModifyOpLogSize\"：修改oplog大小 - \"RestoreMongoDB\"：集群恢复到新实例 - \"RestoreMongoDB_Replica\"：副本集恢复到新实例 - \"RestoreMongoDB_Replica_Single\"：单节点恢复到新实例 - \"RestoreMongoDB_Replica_PITR\"：副本集恢复到指定时间点 - \"MongodbSnapshotBackup\"：创建物理备份 - \"MongodbSnapshotEBackup\"：创建快照备份 - \"MongodbRestoreData2CurrentInstance\"：备份恢复到当前实例 - \"MongodbRestoreData2NewInstance\"：备份恢复到新实例 - \"MongodbPitr2CurrentInstance\"：备份恢复到当前实例指定时间点 - \"MongodbPitr2NewInstance\"：备份恢复到新实例指定时间点 - \"MongodbRecycleBackup\"：备份回收 - \"MongodbRestoreTable\"：库表级时间点恢复 - \"UpgradeDatabaseVersion\"：升级数据库补丁

        :param name: The name of this ListTasksRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListTasksRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTasksRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListTasksRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTasksRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListTasksRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
