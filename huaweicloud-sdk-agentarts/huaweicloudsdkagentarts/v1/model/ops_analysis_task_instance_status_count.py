# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsAnalysisTaskInstanceStatusCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scheduled': 'int',
        'running': 'int',
        'skipped': 'int',
        'success': 'int',
        'fail': 'int',
        'stopped': 'int'
    }

    attribute_map = {
        'scheduled': 'scheduled',
        'running': 'running',
        'skipped': 'skipped',
        'success': 'success',
        'fail': 'fail',
        'stopped': 'stopped'
    }

    def __init__(self, scheduled=None, running=None, skipped=None, success=None, fail=None, stopped=None):
        r"""OpsAnalysisTaskInstanceStatusCount

        The model defined in huaweicloud sdk

        :param scheduled: **参数解释：** 待运行task_instance个数。 **取值范围：** 0-30的整数。
        :type scheduled: int
        :param running: **参数解释：** 运行中task_instance个数。 **取值范围：** 0-30的整数。
        :type running: int
        :param skipped: **参数解释：** 跳过task_instance个数。 **取值范围：** 0-30的整数。
        :type skipped: int
        :param success: **参数解释：** 成功完成task_instance个数。 **取值范围：** 0-30的整数。
        :type success: int
        :param fail: **参数解释：** 运行失败task_instance个数。 **取值范围：** 0-30的整数。
        :type fail: int
        :param stopped: **参数解释：** 已停止task_instance个数。 **取值范围：** 0-30的整数。
        :type stopped: int
        """
        
        

        self._scheduled = None
        self._running = None
        self._skipped = None
        self._success = None
        self._fail = None
        self._stopped = None
        self.discriminator = None

        if scheduled is not None:
            self.scheduled = scheduled
        if running is not None:
            self.running = running
        if skipped is not None:
            self.skipped = skipped
        if success is not None:
            self.success = success
        if fail is not None:
            self.fail = fail
        if stopped is not None:
            self.stopped = stopped

    @property
    def scheduled(self):
        r"""Gets the scheduled of this OpsAnalysisTaskInstanceStatusCount.

        **参数解释：** 待运行task_instance个数。 **取值范围：** 0-30的整数。

        :return: The scheduled of this OpsAnalysisTaskInstanceStatusCount.
        :rtype: int
        """
        return self._scheduled

    @scheduled.setter
    def scheduled(self, scheduled):
        r"""Sets the scheduled of this OpsAnalysisTaskInstanceStatusCount.

        **参数解释：** 待运行task_instance个数。 **取值范围：** 0-30的整数。

        :param scheduled: The scheduled of this OpsAnalysisTaskInstanceStatusCount.
        :type scheduled: int
        """
        self._scheduled = scheduled

    @property
    def running(self):
        r"""Gets the running of this OpsAnalysisTaskInstanceStatusCount.

        **参数解释：** 运行中task_instance个数。 **取值范围：** 0-30的整数。

        :return: The running of this OpsAnalysisTaskInstanceStatusCount.
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        r"""Sets the running of this OpsAnalysisTaskInstanceStatusCount.

        **参数解释：** 运行中task_instance个数。 **取值范围：** 0-30的整数。

        :param running: The running of this OpsAnalysisTaskInstanceStatusCount.
        :type running: int
        """
        self._running = running

    @property
    def skipped(self):
        r"""Gets the skipped of this OpsAnalysisTaskInstanceStatusCount.

        **参数解释：** 跳过task_instance个数。 **取值范围：** 0-30的整数。

        :return: The skipped of this OpsAnalysisTaskInstanceStatusCount.
        :rtype: int
        """
        return self._skipped

    @skipped.setter
    def skipped(self, skipped):
        r"""Sets the skipped of this OpsAnalysisTaskInstanceStatusCount.

        **参数解释：** 跳过task_instance个数。 **取值范围：** 0-30的整数。

        :param skipped: The skipped of this OpsAnalysisTaskInstanceStatusCount.
        :type skipped: int
        """
        self._skipped = skipped

    @property
    def success(self):
        r"""Gets the success of this OpsAnalysisTaskInstanceStatusCount.

        **参数解释：** 成功完成task_instance个数。 **取值范围：** 0-30的整数。

        :return: The success of this OpsAnalysisTaskInstanceStatusCount.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this OpsAnalysisTaskInstanceStatusCount.

        **参数解释：** 成功完成task_instance个数。 **取值范围：** 0-30的整数。

        :param success: The success of this OpsAnalysisTaskInstanceStatusCount.
        :type success: int
        """
        self._success = success

    @property
    def fail(self):
        r"""Gets the fail of this OpsAnalysisTaskInstanceStatusCount.

        **参数解释：** 运行失败task_instance个数。 **取值范围：** 0-30的整数。

        :return: The fail of this OpsAnalysisTaskInstanceStatusCount.
        :rtype: int
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        r"""Sets the fail of this OpsAnalysisTaskInstanceStatusCount.

        **参数解释：** 运行失败task_instance个数。 **取值范围：** 0-30的整数。

        :param fail: The fail of this OpsAnalysisTaskInstanceStatusCount.
        :type fail: int
        """
        self._fail = fail

    @property
    def stopped(self):
        r"""Gets the stopped of this OpsAnalysisTaskInstanceStatusCount.

        **参数解释：** 已停止task_instance个数。 **取值范围：** 0-30的整数。

        :return: The stopped of this OpsAnalysisTaskInstanceStatusCount.
        :rtype: int
        """
        return self._stopped

    @stopped.setter
    def stopped(self, stopped):
        r"""Sets the stopped of this OpsAnalysisTaskInstanceStatusCount.

        **参数解释：** 已停止task_instance个数。 **取值范围：** 0-30的整数。

        :param stopped: The stopped of this OpsAnalysisTaskInstanceStatusCount.
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
        if not isinstance(other, OpsAnalysisTaskInstanceStatusCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
