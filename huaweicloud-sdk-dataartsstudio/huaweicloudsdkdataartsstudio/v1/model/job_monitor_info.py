# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobMonitorInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'update_time': 'int',
        'node_id': 'str',
        'consume_position': 'str',
        'origin_position': 'str',
        'running_status': 'str',
        'total_task_props': 'object',
        'task_info': 'list[MonitorTaskInfo]',
        'snapshot_progress': 'SnapshotProgressInfo'
    }

    attribute_map = {
        'update_time': 'update_time',
        'node_id': 'node_id',
        'consume_position': 'consume_position',
        'origin_position': 'origin_position',
        'running_status': 'running_status',
        'total_task_props': 'total_task_props',
        'task_info': 'task_info',
        'snapshot_progress': 'snapshot_progress'
    }

    def __init__(self, update_time=None, node_id=None, consume_position=None, origin_position=None, running_status=None, total_task_props=None, task_info=None, snapshot_progress=None):
        r"""JobMonitorInfo

        The model defined in huaweicloud sdk

        :param update_time: 任务更新时间，毫秒时间戳。
        :type update_time: int
        :param node_id: 作业源信息。
        :type node_id: str
        :param consume_position: 作业消费位点。
        :type consume_position: str
        :param origin_position: 起始位点。
        :type origin_position: str
        :param running_status: 作业全量增量运行状态。 - INITIALIZING：初始化 - BINLOG：增量同步 - SNAPSHOT：全量同步
        :type running_status: str
        :param total_task_props: 单节点聚合后的监控指标。
        :type total_task_props: object
        :param task_info: 连接列表。
        :type task_info: list[:class:`huaweicloudsdkdataartsstudio.v1.MonitorTaskInfo`]
        :param snapshot_progress: 
        :type snapshot_progress: :class:`huaweicloudsdkdataartsstudio.v1.SnapshotProgressInfo`
        """
        
        

        self._update_time = None
        self._node_id = None
        self._consume_position = None
        self._origin_position = None
        self._running_status = None
        self._total_task_props = None
        self._task_info = None
        self._snapshot_progress = None
        self.discriminator = None

        if update_time is not None:
            self.update_time = update_time
        if node_id is not None:
            self.node_id = node_id
        if consume_position is not None:
            self.consume_position = consume_position
        if origin_position is not None:
            self.origin_position = origin_position
        if running_status is not None:
            self.running_status = running_status
        if total_task_props is not None:
            self.total_task_props = total_task_props
        if task_info is not None:
            self.task_info = task_info
        if snapshot_progress is not None:
            self.snapshot_progress = snapshot_progress

    @property
    def update_time(self):
        r"""Gets the update_time of this JobMonitorInfo.

        任务更新时间，毫秒时间戳。

        :return: The update_time of this JobMonitorInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this JobMonitorInfo.

        任务更新时间，毫秒时间戳。

        :param update_time: The update_time of this JobMonitorInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def node_id(self):
        r"""Gets the node_id of this JobMonitorInfo.

        作业源信息。

        :return: The node_id of this JobMonitorInfo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this JobMonitorInfo.

        作业源信息。

        :param node_id: The node_id of this JobMonitorInfo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def consume_position(self):
        r"""Gets the consume_position of this JobMonitorInfo.

        作业消费位点。

        :return: The consume_position of this JobMonitorInfo.
        :rtype: str
        """
        return self._consume_position

    @consume_position.setter
    def consume_position(self, consume_position):
        r"""Sets the consume_position of this JobMonitorInfo.

        作业消费位点。

        :param consume_position: The consume_position of this JobMonitorInfo.
        :type consume_position: str
        """
        self._consume_position = consume_position

    @property
    def origin_position(self):
        r"""Gets the origin_position of this JobMonitorInfo.

        起始位点。

        :return: The origin_position of this JobMonitorInfo.
        :rtype: str
        """
        return self._origin_position

    @origin_position.setter
    def origin_position(self, origin_position):
        r"""Sets the origin_position of this JobMonitorInfo.

        起始位点。

        :param origin_position: The origin_position of this JobMonitorInfo.
        :type origin_position: str
        """
        self._origin_position = origin_position

    @property
    def running_status(self):
        r"""Gets the running_status of this JobMonitorInfo.

        作业全量增量运行状态。 - INITIALIZING：初始化 - BINLOG：增量同步 - SNAPSHOT：全量同步

        :return: The running_status of this JobMonitorInfo.
        :rtype: str
        """
        return self._running_status

    @running_status.setter
    def running_status(self, running_status):
        r"""Sets the running_status of this JobMonitorInfo.

        作业全量增量运行状态。 - INITIALIZING：初始化 - BINLOG：增量同步 - SNAPSHOT：全量同步

        :param running_status: The running_status of this JobMonitorInfo.
        :type running_status: str
        """
        self._running_status = running_status

    @property
    def total_task_props(self):
        r"""Gets the total_task_props of this JobMonitorInfo.

        单节点聚合后的监控指标。

        :return: The total_task_props of this JobMonitorInfo.
        :rtype: object
        """
        return self._total_task_props

    @total_task_props.setter
    def total_task_props(self, total_task_props):
        r"""Sets the total_task_props of this JobMonitorInfo.

        单节点聚合后的监控指标。

        :param total_task_props: The total_task_props of this JobMonitorInfo.
        :type total_task_props: object
        """
        self._total_task_props = total_task_props

    @property
    def task_info(self):
        r"""Gets the task_info of this JobMonitorInfo.

        连接列表。

        :return: The task_info of this JobMonitorInfo.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.MonitorTaskInfo`]
        """
        return self._task_info

    @task_info.setter
    def task_info(self, task_info):
        r"""Sets the task_info of this JobMonitorInfo.

        连接列表。

        :param task_info: The task_info of this JobMonitorInfo.
        :type task_info: list[:class:`huaweicloudsdkdataartsstudio.v1.MonitorTaskInfo`]
        """
        self._task_info = task_info

    @property
    def snapshot_progress(self):
        r"""Gets the snapshot_progress of this JobMonitorInfo.

        :return: The snapshot_progress of this JobMonitorInfo.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SnapshotProgressInfo`
        """
        return self._snapshot_progress

    @snapshot_progress.setter
    def snapshot_progress(self, snapshot_progress):
        r"""Sets the snapshot_progress of this JobMonitorInfo.

        :param snapshot_progress: The snapshot_progress of this JobMonitorInfo.
        :type snapshot_progress: :class:`huaweicloudsdkdataartsstudio.v1.SnapshotProgressInfo`
        """
        self._snapshot_progress = snapshot_progress

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
        if not isinstance(other, JobMonitorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
