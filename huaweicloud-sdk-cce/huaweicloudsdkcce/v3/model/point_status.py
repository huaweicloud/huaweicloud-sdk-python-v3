# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PointStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_type': 'str',
        'task_id': 'str',
        'status': 'str',
        'start_time_stamp': 'str',
        'end_time_stamp': 'str',
        'expire_time_stamp': 'str'
    }

    attribute_map = {
        'task_type': 'taskType',
        'task_id': 'taskID',
        'status': 'status',
        'start_time_stamp': 'startTimeStamp',
        'end_time_stamp': 'endTimeStamp',
        'expire_time_stamp': 'expireTimeStamp'
    }

    def __init__(self, task_type=None, task_id=None, status=None, start_time_stamp=None, end_time_stamp=None, expire_time_stamp=None):
        r"""PointStatus

        The model defined in huaweicloud sdk

        :param task_type: 集群升级任务类型： Cluster: 集群升级任务 PreCheck: 集群升级预检查任务 Rollback: 集群升级回归任务 Snapshot: 集群升级快照任务 PostCheck: 集群升级后检查任务 
        :type task_type: str
        :param task_id: 升级任务项ID
        :type task_id: str
        :param status: 集群升级状态： Init: 任务初始状态 Queuing: 任务已进入执行队列 Running: 任务开始执行 Success: 任务执行成功 Failed: 任务执行失败 
        :type status: str
        :param start_time_stamp: 升级任务开始时间
        :type start_time_stamp: str
        :param end_time_stamp: 升级任务结束时间
        :type end_time_stamp: str
        :param expire_time_stamp: 升级任务过期时间（当前仅升级前检查任务适用）
        :type expire_time_stamp: str
        """
        
        

        self._task_type = None
        self._task_id = None
        self._status = None
        self._start_time_stamp = None
        self._end_time_stamp = None
        self._expire_time_stamp = None
        self.discriminator = None

        if task_type is not None:
            self.task_type = task_type
        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if start_time_stamp is not None:
            self.start_time_stamp = start_time_stamp
        if end_time_stamp is not None:
            self.end_time_stamp = end_time_stamp
        if expire_time_stamp is not None:
            self.expire_time_stamp = expire_time_stamp

    @property
    def task_type(self):
        r"""Gets the task_type of this PointStatus.

        集群升级任务类型： Cluster: 集群升级任务 PreCheck: 集群升级预检查任务 Rollback: 集群升级回归任务 Snapshot: 集群升级快照任务 PostCheck: 集群升级后检查任务 

        :return: The task_type of this PointStatus.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this PointStatus.

        集群升级任务类型： Cluster: 集群升级任务 PreCheck: 集群升级预检查任务 Rollback: 集群升级回归任务 Snapshot: 集群升级快照任务 PostCheck: 集群升级后检查任务 

        :param task_type: The task_type of this PointStatus.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def task_id(self):
        r"""Gets the task_id of this PointStatus.

        升级任务项ID

        :return: The task_id of this PointStatus.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this PointStatus.

        升级任务项ID

        :param task_id: The task_id of this PointStatus.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        r"""Gets the status of this PointStatus.

        集群升级状态： Init: 任务初始状态 Queuing: 任务已进入执行队列 Running: 任务开始执行 Success: 任务执行成功 Failed: 任务执行失败 

        :return: The status of this PointStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PointStatus.

        集群升级状态： Init: 任务初始状态 Queuing: 任务已进入执行队列 Running: 任务开始执行 Success: 任务执行成功 Failed: 任务执行失败 

        :param status: The status of this PointStatus.
        :type status: str
        """
        self._status = status

    @property
    def start_time_stamp(self):
        r"""Gets the start_time_stamp of this PointStatus.

        升级任务开始时间

        :return: The start_time_stamp of this PointStatus.
        :rtype: str
        """
        return self._start_time_stamp

    @start_time_stamp.setter
    def start_time_stamp(self, start_time_stamp):
        r"""Sets the start_time_stamp of this PointStatus.

        升级任务开始时间

        :param start_time_stamp: The start_time_stamp of this PointStatus.
        :type start_time_stamp: str
        """
        self._start_time_stamp = start_time_stamp

    @property
    def end_time_stamp(self):
        r"""Gets the end_time_stamp of this PointStatus.

        升级任务结束时间

        :return: The end_time_stamp of this PointStatus.
        :rtype: str
        """
        return self._end_time_stamp

    @end_time_stamp.setter
    def end_time_stamp(self, end_time_stamp):
        r"""Sets the end_time_stamp of this PointStatus.

        升级任务结束时间

        :param end_time_stamp: The end_time_stamp of this PointStatus.
        :type end_time_stamp: str
        """
        self._end_time_stamp = end_time_stamp

    @property
    def expire_time_stamp(self):
        r"""Gets the expire_time_stamp of this PointStatus.

        升级任务过期时间（当前仅升级前检查任务适用）

        :return: The expire_time_stamp of this PointStatus.
        :rtype: str
        """
        return self._expire_time_stamp

    @expire_time_stamp.setter
    def expire_time_stamp(self, expire_time_stamp):
        r"""Sets the expire_time_stamp of this PointStatus.

        升级任务过期时间（当前仅升级前检查任务适用）

        :param expire_time_stamp: The expire_time_stamp of this PointStatus.
        :type expire_time_stamp: str
        """
        self._expire_time_stamp = expire_time_stamp

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
        if not isinstance(other, PointStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
