# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadStatisticsStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queue': 'int',
        'pending': 'int',
        'abnormal': 'int',
        'terminating': 'int',
        'creating': 'int',
        'running': 'int',
        'completed': 'int',
        'terminated': 'int',
        'failed': 'int'
    }

    attribute_map = {
        'queue': 'Queue',
        'pending': 'Pending',
        'abnormal': 'Abnormal',
        'terminating': 'Terminating',
        'creating': 'Creating',
        'running': 'Running',
        'completed': 'Completed',
        'terminated': 'Terminated',
        'failed': 'Failed'
    }

    def __init__(self, queue=None, pending=None, abnormal=None, terminating=None, creating=None, running=None, completed=None, terminated=None, failed=None):
        r"""WorkloadStatisticsStatus

        The model defined in huaweicloud sdk

        :param queue: **参数描述**： 排队中的作业个数。 **取值范围**： 不涉及。
        :type queue: int
        :param pending: **参数描述**： 等待中的作业个数。 **取值范围**： 不涉及。
        :type pending: int
        :param abnormal: **参数描述**： 异常的作业个数。 **取值范围**： 不涉及。
        :type abnormal: int
        :param terminating: **参数描述**： 终止中的作业个数。 **取值范围**： 不涉及。
        :type terminating: int
        :param creating: **参数描述**： 创建中的作业个数。 **取值范围**： 不涉及。
        :type creating: int
        :param running: **参数描述**： 运行中的作业个数。 **取值范围**： 不涉及。
        :type running: int
        :param completed: **参数描述**： 已完成的作业个数。 **取值范围**： 不涉及。
        :type completed: int
        :param terminated: **参数描述**： 已终止的作业个数。 **取值范围**： 不涉及。
        :type terminated: int
        :param failed: **参数描述**：运行失败的作业个数。 **取值范围**： 不涉及。
        :type failed: int
        """
        
        

        self._queue = None
        self._pending = None
        self._abnormal = None
        self._terminating = None
        self._creating = None
        self._running = None
        self._completed = None
        self._terminated = None
        self._failed = None
        self.discriminator = None

        if queue is not None:
            self.queue = queue
        if pending is not None:
            self.pending = pending
        if abnormal is not None:
            self.abnormal = abnormal
        if terminating is not None:
            self.terminating = terminating
        if creating is not None:
            self.creating = creating
        if running is not None:
            self.running = running
        if completed is not None:
            self.completed = completed
        if terminated is not None:
            self.terminated = terminated
        if failed is not None:
            self.failed = failed

    @property
    def queue(self):
        r"""Gets the queue of this WorkloadStatisticsStatus.

        **参数描述**： 排队中的作业个数。 **取值范围**： 不涉及。

        :return: The queue of this WorkloadStatisticsStatus.
        :rtype: int
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        r"""Sets the queue of this WorkloadStatisticsStatus.

        **参数描述**： 排队中的作业个数。 **取值范围**： 不涉及。

        :param queue: The queue of this WorkloadStatisticsStatus.
        :type queue: int
        """
        self._queue = queue

    @property
    def pending(self):
        r"""Gets the pending of this WorkloadStatisticsStatus.

        **参数描述**： 等待中的作业个数。 **取值范围**： 不涉及。

        :return: The pending of this WorkloadStatisticsStatus.
        :rtype: int
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        r"""Sets the pending of this WorkloadStatisticsStatus.

        **参数描述**： 等待中的作业个数。 **取值范围**： 不涉及。

        :param pending: The pending of this WorkloadStatisticsStatus.
        :type pending: int
        """
        self._pending = pending

    @property
    def abnormal(self):
        r"""Gets the abnormal of this WorkloadStatisticsStatus.

        **参数描述**： 异常的作业个数。 **取值范围**： 不涉及。

        :return: The abnormal of this WorkloadStatisticsStatus.
        :rtype: int
        """
        return self._abnormal

    @abnormal.setter
    def abnormal(self, abnormal):
        r"""Sets the abnormal of this WorkloadStatisticsStatus.

        **参数描述**： 异常的作业个数。 **取值范围**： 不涉及。

        :param abnormal: The abnormal of this WorkloadStatisticsStatus.
        :type abnormal: int
        """
        self._abnormal = abnormal

    @property
    def terminating(self):
        r"""Gets the terminating of this WorkloadStatisticsStatus.

        **参数描述**： 终止中的作业个数。 **取值范围**： 不涉及。

        :return: The terminating of this WorkloadStatisticsStatus.
        :rtype: int
        """
        return self._terminating

    @terminating.setter
    def terminating(self, terminating):
        r"""Sets the terminating of this WorkloadStatisticsStatus.

        **参数描述**： 终止中的作业个数。 **取值范围**： 不涉及。

        :param terminating: The terminating of this WorkloadStatisticsStatus.
        :type terminating: int
        """
        self._terminating = terminating

    @property
    def creating(self):
        r"""Gets the creating of this WorkloadStatisticsStatus.

        **参数描述**： 创建中的作业个数。 **取值范围**： 不涉及。

        :return: The creating of this WorkloadStatisticsStatus.
        :rtype: int
        """
        return self._creating

    @creating.setter
    def creating(self, creating):
        r"""Sets the creating of this WorkloadStatisticsStatus.

        **参数描述**： 创建中的作业个数。 **取值范围**： 不涉及。

        :param creating: The creating of this WorkloadStatisticsStatus.
        :type creating: int
        """
        self._creating = creating

    @property
    def running(self):
        r"""Gets the running of this WorkloadStatisticsStatus.

        **参数描述**： 运行中的作业个数。 **取值范围**： 不涉及。

        :return: The running of this WorkloadStatisticsStatus.
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        r"""Sets the running of this WorkloadStatisticsStatus.

        **参数描述**： 运行中的作业个数。 **取值范围**： 不涉及。

        :param running: The running of this WorkloadStatisticsStatus.
        :type running: int
        """
        self._running = running

    @property
    def completed(self):
        r"""Gets the completed of this WorkloadStatisticsStatus.

        **参数描述**： 已完成的作业个数。 **取值范围**： 不涉及。

        :return: The completed of this WorkloadStatisticsStatus.
        :rtype: int
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        r"""Sets the completed of this WorkloadStatisticsStatus.

        **参数描述**： 已完成的作业个数。 **取值范围**： 不涉及。

        :param completed: The completed of this WorkloadStatisticsStatus.
        :type completed: int
        """
        self._completed = completed

    @property
    def terminated(self):
        r"""Gets the terminated of this WorkloadStatisticsStatus.

        **参数描述**： 已终止的作业个数。 **取值范围**： 不涉及。

        :return: The terminated of this WorkloadStatisticsStatus.
        :rtype: int
        """
        return self._terminated

    @terminated.setter
    def terminated(self, terminated):
        r"""Sets the terminated of this WorkloadStatisticsStatus.

        **参数描述**： 已终止的作业个数。 **取值范围**： 不涉及。

        :param terminated: The terminated of this WorkloadStatisticsStatus.
        :type terminated: int
        """
        self._terminated = terminated

    @property
    def failed(self):
        r"""Gets the failed of this WorkloadStatisticsStatus.

        **参数描述**：运行失败的作业个数。 **取值范围**： 不涉及。

        :return: The failed of this WorkloadStatisticsStatus.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        r"""Sets the failed of this WorkloadStatisticsStatus.

        **参数描述**：运行失败的作业个数。 **取值范围**： 不涉及。

        :param failed: The failed of this WorkloadStatisticsStatus.
        :type failed: int
        """
        self._failed = failed

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
        if not isinstance(other, WorkloadStatisticsStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
