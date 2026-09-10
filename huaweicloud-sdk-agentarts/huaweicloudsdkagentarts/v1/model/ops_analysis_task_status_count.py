# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsAnalysisTaskStatusCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'draft': 'int',
        'scheduled': 'int',
        'running': 'int',
        'paused': 'int',
        'completed': 'int',
        'fail': 'int',
        'stopping': 'int',
        'stopped': 'int'
    }

    attribute_map = {
        'draft': 'draft',
        'scheduled': 'scheduled',
        'running': 'running',
        'paused': 'paused',
        'completed': 'completed',
        'fail': 'fail',
        'stopping': 'stopping',
        'stopped': 'stopped'
    }

    def __init__(self, draft=None, scheduled=None, running=None, paused=None, completed=None, fail=None, stopping=None, stopped=None):
        r"""OpsAnalysisTaskStatusCount

        The model defined in huaweicloud sdk

        :param draft: **参数解释：** 草稿任务个数。  **取值范围：** 0-1000的整数。
        :type draft: int
        :param scheduled: **参数解释：** 待运行的任务个数。  **取值范围：** 0-1000的整数。
        :type scheduled: int
        :param running: **参数解释：** 运行中任务个数。  **取值范围：** 0-1000的整数。
        :type running: int
        :param paused: **参数解释：** 已暂停任务个数。  **取值范围：** 0-1000的整数。
        :type paused: int
        :param completed: **参数解释：** 完成的任务个数。  **取值范围：** 0-1000的整数。
        :type completed: int
        :param fail: **参数解释：** 失败任务个数。  **取值范围：** 0-1000的整数。
        :type fail: int
        :param stopping: **参数解释：** 停止中任务个数。  **取值范围：** 0-1000的整数。
        :type stopping: int
        :param stopped: **参数解释：** 已停止任务个数。  **取值范围：** 0-1000的整数。
        :type stopped: int
        """
        
        

        self._draft = None
        self._scheduled = None
        self._running = None
        self._paused = None
        self._completed = None
        self._fail = None
        self._stopping = None
        self._stopped = None
        self.discriminator = None

        if draft is not None:
            self.draft = draft
        if scheduled is not None:
            self.scheduled = scheduled
        if running is not None:
            self.running = running
        if paused is not None:
            self.paused = paused
        if completed is not None:
            self.completed = completed
        if fail is not None:
            self.fail = fail
        if stopping is not None:
            self.stopping = stopping
        if stopped is not None:
            self.stopped = stopped

    @property
    def draft(self):
        r"""Gets the draft of this OpsAnalysisTaskStatusCount.

        **参数解释：** 草稿任务个数。  **取值范围：** 0-1000的整数。

        :return: The draft of this OpsAnalysisTaskStatusCount.
        :rtype: int
        """
        return self._draft

    @draft.setter
    def draft(self, draft):
        r"""Sets the draft of this OpsAnalysisTaskStatusCount.

        **参数解释：** 草稿任务个数。  **取值范围：** 0-1000的整数。

        :param draft: The draft of this OpsAnalysisTaskStatusCount.
        :type draft: int
        """
        self._draft = draft

    @property
    def scheduled(self):
        r"""Gets the scheduled of this OpsAnalysisTaskStatusCount.

        **参数解释：** 待运行的任务个数。  **取值范围：** 0-1000的整数。

        :return: The scheduled of this OpsAnalysisTaskStatusCount.
        :rtype: int
        """
        return self._scheduled

    @scheduled.setter
    def scheduled(self, scheduled):
        r"""Sets the scheduled of this OpsAnalysisTaskStatusCount.

        **参数解释：** 待运行的任务个数。  **取值范围：** 0-1000的整数。

        :param scheduled: The scheduled of this OpsAnalysisTaskStatusCount.
        :type scheduled: int
        """
        self._scheduled = scheduled

    @property
    def running(self):
        r"""Gets the running of this OpsAnalysisTaskStatusCount.

        **参数解释：** 运行中任务个数。  **取值范围：** 0-1000的整数。

        :return: The running of this OpsAnalysisTaskStatusCount.
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        r"""Sets the running of this OpsAnalysisTaskStatusCount.

        **参数解释：** 运行中任务个数。  **取值范围：** 0-1000的整数。

        :param running: The running of this OpsAnalysisTaskStatusCount.
        :type running: int
        """
        self._running = running

    @property
    def paused(self):
        r"""Gets the paused of this OpsAnalysisTaskStatusCount.

        **参数解释：** 已暂停任务个数。  **取值范围：** 0-1000的整数。

        :return: The paused of this OpsAnalysisTaskStatusCount.
        :rtype: int
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        r"""Sets the paused of this OpsAnalysisTaskStatusCount.

        **参数解释：** 已暂停任务个数。  **取值范围：** 0-1000的整数。

        :param paused: The paused of this OpsAnalysisTaskStatusCount.
        :type paused: int
        """
        self._paused = paused

    @property
    def completed(self):
        r"""Gets the completed of this OpsAnalysisTaskStatusCount.

        **参数解释：** 完成的任务个数。  **取值范围：** 0-1000的整数。

        :return: The completed of this OpsAnalysisTaskStatusCount.
        :rtype: int
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        r"""Sets the completed of this OpsAnalysisTaskStatusCount.

        **参数解释：** 完成的任务个数。  **取值范围：** 0-1000的整数。

        :param completed: The completed of this OpsAnalysisTaskStatusCount.
        :type completed: int
        """
        self._completed = completed

    @property
    def fail(self):
        r"""Gets the fail of this OpsAnalysisTaskStatusCount.

        **参数解释：** 失败任务个数。  **取值范围：** 0-1000的整数。

        :return: The fail of this OpsAnalysisTaskStatusCount.
        :rtype: int
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        r"""Sets the fail of this OpsAnalysisTaskStatusCount.

        **参数解释：** 失败任务个数。  **取值范围：** 0-1000的整数。

        :param fail: The fail of this OpsAnalysisTaskStatusCount.
        :type fail: int
        """
        self._fail = fail

    @property
    def stopping(self):
        r"""Gets the stopping of this OpsAnalysisTaskStatusCount.

        **参数解释：** 停止中任务个数。  **取值范围：** 0-1000的整数。

        :return: The stopping of this OpsAnalysisTaskStatusCount.
        :rtype: int
        """
        return self._stopping

    @stopping.setter
    def stopping(self, stopping):
        r"""Sets the stopping of this OpsAnalysisTaskStatusCount.

        **参数解释：** 停止中任务个数。  **取值范围：** 0-1000的整数。

        :param stopping: The stopping of this OpsAnalysisTaskStatusCount.
        :type stopping: int
        """
        self._stopping = stopping

    @property
    def stopped(self):
        r"""Gets the stopped of this OpsAnalysisTaskStatusCount.

        **参数解释：** 已停止任务个数。  **取值范围：** 0-1000的整数。

        :return: The stopped of this OpsAnalysisTaskStatusCount.
        :rtype: int
        """
        return self._stopped

    @stopped.setter
    def stopped(self, stopped):
        r"""Sets the stopped of this OpsAnalysisTaskStatusCount.

        **参数解释：** 已停止任务个数。  **取值范围：** 0-1000的整数。

        :param stopped: The stopped of this OpsAnalysisTaskStatusCount.
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
        if not isinstance(other, OpsAnalysisTaskStatusCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
