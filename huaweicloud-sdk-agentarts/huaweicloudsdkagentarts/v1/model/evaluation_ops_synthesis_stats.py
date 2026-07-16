# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationOpsSynthesisStats:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'progress': 'int',
        'success': 'int',
        'failed': 'int',
        'running': 'int',
        'pending': 'int'
    }

    attribute_map = {
        'total': 'total',
        'progress': 'progress',
        'success': 'success',
        'failed': 'failed',
        'running': 'running',
        'pending': 'pending'
    }

    def __init__(self, total=None, progress=None, success=None, failed=None, running=None, pending=None):
        r"""EvaluationOpsSynthesisStats

        The model defined in huaweicloud sdk

        :param total: **参数解释：**   任务计划生成的总样本条数。 **取值范围：**   0-500。 
        :type total: int
        :param progress: **参数解释：**   当前任务执行的百分比进度。 **取值范围：**   0-100。 
        :type progress: int
        :param success: **参数解释：**   当前已成功生成的样本总数。 **取值范围：**   0-500。 
        :type success: int
        :param failed: **参数解释：**   在合成过程中失败的样本总数。 **取值范围：**   0-500。 
        :type failed: int
        :param running: **参数解释：**   当前正处于活跃生成阶段的样本条数。 **取值范围：**   0-500。 
        :type running: int
        :param pending: **参数解释：**   尚未开始执行、在队列中等待的样本条数。 **取值范围：**   0-500。 
        :type pending: int
        """
        
        

        self._total = None
        self._progress = None
        self._success = None
        self._failed = None
        self._running = None
        self._pending = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if progress is not None:
            self.progress = progress
        if success is not None:
            self.success = success
        if failed is not None:
            self.failed = failed
        if running is not None:
            self.running = running
        if pending is not None:
            self.pending = pending

    @property
    def total(self):
        r"""Gets the total of this EvaluationOpsSynthesisStats.

        **参数解释：**   任务计划生成的总样本条数。 **取值范围：**   0-500。 

        :return: The total of this EvaluationOpsSynthesisStats.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this EvaluationOpsSynthesisStats.

        **参数解释：**   任务计划生成的总样本条数。 **取值范围：**   0-500。 

        :param total: The total of this EvaluationOpsSynthesisStats.
        :type total: int
        """
        self._total = total

    @property
    def progress(self):
        r"""Gets the progress of this EvaluationOpsSynthesisStats.

        **参数解释：**   当前任务执行的百分比进度。 **取值范围：**   0-100。 

        :return: The progress of this EvaluationOpsSynthesisStats.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this EvaluationOpsSynthesisStats.

        **参数解释：**   当前任务执行的百分比进度。 **取值范围：**   0-100。 

        :param progress: The progress of this EvaluationOpsSynthesisStats.
        :type progress: int
        """
        self._progress = progress

    @property
    def success(self):
        r"""Gets the success of this EvaluationOpsSynthesisStats.

        **参数解释：**   当前已成功生成的样本总数。 **取值范围：**   0-500。 

        :return: The success of this EvaluationOpsSynthesisStats.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this EvaluationOpsSynthesisStats.

        **参数解释：**   当前已成功生成的样本总数。 **取值范围：**   0-500。 

        :param success: The success of this EvaluationOpsSynthesisStats.
        :type success: int
        """
        self._success = success

    @property
    def failed(self):
        r"""Gets the failed of this EvaluationOpsSynthesisStats.

        **参数解释：**   在合成过程中失败的样本总数。 **取值范围：**   0-500。 

        :return: The failed of this EvaluationOpsSynthesisStats.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        r"""Sets the failed of this EvaluationOpsSynthesisStats.

        **参数解释：**   在合成过程中失败的样本总数。 **取值范围：**   0-500。 

        :param failed: The failed of this EvaluationOpsSynthesisStats.
        :type failed: int
        """
        self._failed = failed

    @property
    def running(self):
        r"""Gets the running of this EvaluationOpsSynthesisStats.

        **参数解释：**   当前正处于活跃生成阶段的样本条数。 **取值范围：**   0-500。 

        :return: The running of this EvaluationOpsSynthesisStats.
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        r"""Sets the running of this EvaluationOpsSynthesisStats.

        **参数解释：**   当前正处于活跃生成阶段的样本条数。 **取值范围：**   0-500。 

        :param running: The running of this EvaluationOpsSynthesisStats.
        :type running: int
        """
        self._running = running

    @property
    def pending(self):
        r"""Gets the pending of this EvaluationOpsSynthesisStats.

        **参数解释：**   尚未开始执行、在队列中等待的样本条数。 **取值范围：**   0-500。 

        :return: The pending of this EvaluationOpsSynthesisStats.
        :rtype: int
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        r"""Sets the pending of this EvaluationOpsSynthesisStats.

        **参数解释：**   尚未开始执行、在队列中等待的样本条数。 **取值范围：**   0-500。 

        :param pending: The pending of this EvaluationOpsSynthesisStats.
        :type pending: int
        """
        self._pending = pending

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
        if not isinstance(other, EvaluationOpsSynthesisStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
