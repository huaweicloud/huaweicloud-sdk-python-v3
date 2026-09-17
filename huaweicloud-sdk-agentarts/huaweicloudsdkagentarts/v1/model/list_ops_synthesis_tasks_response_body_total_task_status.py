# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsSynthesisTasksResponseBodyTotalTaskStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'int',
        'partial_success': 'int',
        'running': 'int',
        'pending': 'int',
        'failed': 'int',
        'stopped': 'int'
    }

    attribute_map = {
        'success': 'success',
        'partial_success': 'partial_success',
        'running': 'running',
        'pending': 'pending',
        'failed': 'failed',
        'stopped': 'stopped'
    }

    def __init__(self, success=None, partial_success=None, running=None, pending=None, failed=None, stopped=None):
        r"""ListOpsSynthesisTasksResponseBodyTotalTaskStatus

        The model defined in huaweicloud sdk

        :param success: 成功任务数
        :type success: int
        :param partial_success: 部分成功任务数
        :type partial_success: int
        :param running: 运行中任务数
        :type running: int
        :param pending: 待执行任务数
        :type pending: int
        :param failed: 失败任务数
        :type failed: int
        :param stopped: 已停止任务数
        :type stopped: int
        """
        
        

        self._success = None
        self._partial_success = None
        self._running = None
        self._pending = None
        self._failed = None
        self._stopped = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if partial_success is not None:
            self.partial_success = partial_success
        if running is not None:
            self.running = running
        if pending is not None:
            self.pending = pending
        if failed is not None:
            self.failed = failed
        if stopped is not None:
            self.stopped = stopped

    @property
    def success(self):
        r"""Gets the success of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.

        成功任务数

        :return: The success of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.

        成功任务数

        :param success: The success of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.
        :type success: int
        """
        self._success = success

    @property
    def partial_success(self):
        r"""Gets the partial_success of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.

        部分成功任务数

        :return: The partial_success of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.
        :rtype: int
        """
        return self._partial_success

    @partial_success.setter
    def partial_success(self, partial_success):
        r"""Sets the partial_success of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.

        部分成功任务数

        :param partial_success: The partial_success of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.
        :type partial_success: int
        """
        self._partial_success = partial_success

    @property
    def running(self):
        r"""Gets the running of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.

        运行中任务数

        :return: The running of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        r"""Sets the running of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.

        运行中任务数

        :param running: The running of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.
        :type running: int
        """
        self._running = running

    @property
    def pending(self):
        r"""Gets the pending of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.

        待执行任务数

        :return: The pending of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.
        :rtype: int
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        r"""Sets the pending of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.

        待执行任务数

        :param pending: The pending of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.
        :type pending: int
        """
        self._pending = pending

    @property
    def failed(self):
        r"""Gets the failed of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.

        失败任务数

        :return: The failed of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        r"""Sets the failed of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.

        失败任务数

        :param failed: The failed of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.
        :type failed: int
        """
        self._failed = failed

    @property
    def stopped(self):
        r"""Gets the stopped of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.

        已停止任务数

        :return: The stopped of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.
        :rtype: int
        """
        return self._stopped

    @stopped.setter
    def stopped(self, stopped):
        r"""Sets the stopped of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.

        已停止任务数

        :param stopped: The stopped of this ListOpsSynthesisTasksResponseBodyTotalTaskStatus.
        :type stopped: int
        """
        self._stopped = stopped

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
        if not isinstance(other, ListOpsSynthesisTasksResponseBodyTotalTaskStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
