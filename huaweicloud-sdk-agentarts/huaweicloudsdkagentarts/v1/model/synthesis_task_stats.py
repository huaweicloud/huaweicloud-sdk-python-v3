# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SynthesisTaskStats:

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
        'change_uncommitted': 'int',
        'success': 'int',
        'failed': 'int',
        'running': 'int',
        'pending': 'int',
        'progress': 'str'
    }

    attribute_map = {
        'total': 'total',
        'change_uncommitted': 'change_uncommitted',
        'success': 'success',
        'failed': 'failed',
        'running': 'running',
        'pending': 'pending',
        'progress': 'progress'
    }

    def __init__(self, total=None, change_uncommitted=None, success=None, failed=None, running=None, pending=None, progress=None):
        r"""SynthesisTaskStats

        The model defined in huaweicloud sdk

        :param total: **参数解释：** 合成数据总条数。 **取值范围：** 0-10000。 
        :type total: int
        :param change_uncommitted: **参数解释：** 标识当前草稿态相对于最新发布版本是否有尚未提交的变更。 **约束限制：** 不涉及。 **取值范围：** 0-10000。 
        :type change_uncommitted: int
        :param success: **参数解释：** 合成数据success状态总条数。 **取值范围：** 0-10000。 
        :type success: int
        :param failed: **参数解释：** 合成数据failed状态总条数。 **取值范围：** 0-10000。 
        :type failed: int
        :param running: **参数解释：** 合成数据running状态总条数。 **取值范围：** 0-10000。 
        :type running: int
        :param pending: **参数解释：** 合成数据pending状态总条数。 **取值范围：** 0-10000。 
        :type pending: int
        :param progress: **参数解释：** 任务执行的百分比进度。 **取值范围：** 0%到100%。 
        :type progress: str
        """
        
        

        self._total = None
        self._change_uncommitted = None
        self._success = None
        self._failed = None
        self._running = None
        self._pending = None
        self._progress = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if change_uncommitted is not None:
            self.change_uncommitted = change_uncommitted
        if success is not None:
            self.success = success
        if failed is not None:
            self.failed = failed
        if running is not None:
            self.running = running
        if pending is not None:
            self.pending = pending
        if progress is not None:
            self.progress = progress

    @property
    def total(self):
        r"""Gets the total of this SynthesisTaskStats.

        **参数解释：** 合成数据总条数。 **取值范围：** 0-10000。 

        :return: The total of this SynthesisTaskStats.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this SynthesisTaskStats.

        **参数解释：** 合成数据总条数。 **取值范围：** 0-10000。 

        :param total: The total of this SynthesisTaskStats.
        :type total: int
        """
        self._total = total

    @property
    def change_uncommitted(self):
        r"""Gets the change_uncommitted of this SynthesisTaskStats.

        **参数解释：** 标识当前草稿态相对于最新发布版本是否有尚未提交的变更。 **约束限制：** 不涉及。 **取值范围：** 0-10000。 

        :return: The change_uncommitted of this SynthesisTaskStats.
        :rtype: int
        """
        return self._change_uncommitted

    @change_uncommitted.setter
    def change_uncommitted(self, change_uncommitted):
        r"""Sets the change_uncommitted of this SynthesisTaskStats.

        **参数解释：** 标识当前草稿态相对于最新发布版本是否有尚未提交的变更。 **约束限制：** 不涉及。 **取值范围：** 0-10000。 

        :param change_uncommitted: The change_uncommitted of this SynthesisTaskStats.
        :type change_uncommitted: int
        """
        self._change_uncommitted = change_uncommitted

    @property
    def success(self):
        r"""Gets the success of this SynthesisTaskStats.

        **参数解释：** 合成数据success状态总条数。 **取值范围：** 0-10000。 

        :return: The success of this SynthesisTaskStats.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this SynthesisTaskStats.

        **参数解释：** 合成数据success状态总条数。 **取值范围：** 0-10000。 

        :param success: The success of this SynthesisTaskStats.
        :type success: int
        """
        self._success = success

    @property
    def failed(self):
        r"""Gets the failed of this SynthesisTaskStats.

        **参数解释：** 合成数据failed状态总条数。 **取值范围：** 0-10000。 

        :return: The failed of this SynthesisTaskStats.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        r"""Sets the failed of this SynthesisTaskStats.

        **参数解释：** 合成数据failed状态总条数。 **取值范围：** 0-10000。 

        :param failed: The failed of this SynthesisTaskStats.
        :type failed: int
        """
        self._failed = failed

    @property
    def running(self):
        r"""Gets the running of this SynthesisTaskStats.

        **参数解释：** 合成数据running状态总条数。 **取值范围：** 0-10000。 

        :return: The running of this SynthesisTaskStats.
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        r"""Sets the running of this SynthesisTaskStats.

        **参数解释：** 合成数据running状态总条数。 **取值范围：** 0-10000。 

        :param running: The running of this SynthesisTaskStats.
        :type running: int
        """
        self._running = running

    @property
    def pending(self):
        r"""Gets the pending of this SynthesisTaskStats.

        **参数解释：** 合成数据pending状态总条数。 **取值范围：** 0-10000。 

        :return: The pending of this SynthesisTaskStats.
        :rtype: int
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        r"""Sets the pending of this SynthesisTaskStats.

        **参数解释：** 合成数据pending状态总条数。 **取值范围：** 0-10000。 

        :param pending: The pending of this SynthesisTaskStats.
        :type pending: int
        """
        self._pending = pending

    @property
    def progress(self):
        r"""Gets the progress of this SynthesisTaskStats.

        **参数解释：** 任务执行的百分比进度。 **取值范围：** 0%到100%。 

        :return: The progress of this SynthesisTaskStats.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this SynthesisTaskStats.

        **参数解释：** 任务执行的百分比进度。 **取值范围：** 0%到100%。 

        :param progress: The progress of this SynthesisTaskStats.
        :type progress: str
        """
        self._progress = progress

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
        if not isinstance(other, SynthesisTaskStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
