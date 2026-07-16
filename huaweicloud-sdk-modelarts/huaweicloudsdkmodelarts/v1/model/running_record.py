# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunningRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_at': 'int',
        'end_at': 'int',
        'xpu_start_at': 'int',
        'start_type': 'str',
        'end_reason': 'str',
        'end_related_task': 'str',
        'end_recover': 'str',
        'end_recover_before_downgrade': 'str',
        'recover_records': 'list[RecoverRecord]'
    }

    attribute_map = {
        'start_at': 'start_at',
        'end_at': 'end_at',
        'xpu_start_at': 'xpu_start_at',
        'start_type': 'start_type',
        'end_reason': 'end_reason',
        'end_related_task': 'end_related_task',
        'end_recover': 'end_recover',
        'end_recover_before_downgrade': 'end_recover_before_downgrade',
        'recover_records': 'recover_records'
    }

    def __init__(self, start_at=None, end_at=None, xpu_start_at=None, start_type=None, end_reason=None, end_related_task=None, end_recover=None, end_recover_before_downgrade=None, recover_records=None):
        r"""RunningRecord

        The model defined in huaweicloud sdk

        :param start_at: 本次运行开始时间的unix时间戳，单位为秒(s)。
        :type start_at: int
        :param end_at: 本次运行结束时间的unix时间戳，单位为秒(s)。
        :type end_at: int
        :param xpu_start_at: **参数解释**：本次运行加速卡启动时间的unix时间戳，单位为秒(s)。 **取值范围**：不涉及。
        :type xpu_start_at: int
        :param start_type: 本地运行的启动方式： - init_or_rescheduled：代表本次启动为被调度后的首次运行，包括初次启动及调度恢复后的运行。 - restarted：代表本次启动非被调度后的首次运行，为进程重启后的运行。
        :type start_type: str
        :param end_reason: 本次运行结束原因。
        :type end_reason: str
        :param end_related_task: 引发本次运行结束的task worker ID(如worker-0)。
        :type end_related_task: str
        :param end_recover: 本次运行结束后所采取的故障容忍策略，枚举值如下： - npu_proc_restart: NPU原地热恢复 - gpu_proc_restart: GPU原地热恢复 - proc_restart: 进程原地重启 - pod_reschedule: Pod级重调度 - job_reschedule: Job级重调度 - job_reschedule_with_taint: 隔离式Job重调度
        :type end_recover: str
        :param end_recover_before_downgrade: 本次运行结束后在故障容忍策略降级前所采取的容忍策略，取值范围同end_recover。
        :type end_recover_before_downgrade: str
        :param recover_records: **参数解释**：本次运行异常结束时采取的所有故障容忍策略详情。
        :type recover_records: list[:class:`huaweicloudsdkmodelarts.v1.RecoverRecord`]
        """
        
        

        self._start_at = None
        self._end_at = None
        self._xpu_start_at = None
        self._start_type = None
        self._end_reason = None
        self._end_related_task = None
        self._end_recover = None
        self._end_recover_before_downgrade = None
        self._recover_records = None
        self.discriminator = None

        if start_at is not None:
            self.start_at = start_at
        if end_at is not None:
            self.end_at = end_at
        if xpu_start_at is not None:
            self.xpu_start_at = xpu_start_at
        if start_type is not None:
            self.start_type = start_type
        if end_reason is not None:
            self.end_reason = end_reason
        if end_related_task is not None:
            self.end_related_task = end_related_task
        if end_recover is not None:
            self.end_recover = end_recover
        if end_recover_before_downgrade is not None:
            self.end_recover_before_downgrade = end_recover_before_downgrade
        if recover_records is not None:
            self.recover_records = recover_records

    @property
    def start_at(self):
        r"""Gets the start_at of this RunningRecord.

        本次运行开始时间的unix时间戳，单位为秒(s)。

        :return: The start_at of this RunningRecord.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this RunningRecord.

        本次运行开始时间的unix时间戳，单位为秒(s)。

        :param start_at: The start_at of this RunningRecord.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this RunningRecord.

        本次运行结束时间的unix时间戳，单位为秒(s)。

        :return: The end_at of this RunningRecord.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this RunningRecord.

        本次运行结束时间的unix时间戳，单位为秒(s)。

        :param end_at: The end_at of this RunningRecord.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def xpu_start_at(self):
        r"""Gets the xpu_start_at of this RunningRecord.

        **参数解释**：本次运行加速卡启动时间的unix时间戳，单位为秒(s)。 **取值范围**：不涉及。

        :return: The xpu_start_at of this RunningRecord.
        :rtype: int
        """
        return self._xpu_start_at

    @xpu_start_at.setter
    def xpu_start_at(self, xpu_start_at):
        r"""Sets the xpu_start_at of this RunningRecord.

        **参数解释**：本次运行加速卡启动时间的unix时间戳，单位为秒(s)。 **取值范围**：不涉及。

        :param xpu_start_at: The xpu_start_at of this RunningRecord.
        :type xpu_start_at: int
        """
        self._xpu_start_at = xpu_start_at

    @property
    def start_type(self):
        r"""Gets the start_type of this RunningRecord.

        本地运行的启动方式： - init_or_rescheduled：代表本次启动为被调度后的首次运行，包括初次启动及调度恢复后的运行。 - restarted：代表本次启动非被调度后的首次运行，为进程重启后的运行。

        :return: The start_type of this RunningRecord.
        :rtype: str
        """
        return self._start_type

    @start_type.setter
    def start_type(self, start_type):
        r"""Sets the start_type of this RunningRecord.

        本地运行的启动方式： - init_or_rescheduled：代表本次启动为被调度后的首次运行，包括初次启动及调度恢复后的运行。 - restarted：代表本次启动非被调度后的首次运行，为进程重启后的运行。

        :param start_type: The start_type of this RunningRecord.
        :type start_type: str
        """
        self._start_type = start_type

    @property
    def end_reason(self):
        r"""Gets the end_reason of this RunningRecord.

        本次运行结束原因。

        :return: The end_reason of this RunningRecord.
        :rtype: str
        """
        return self._end_reason

    @end_reason.setter
    def end_reason(self, end_reason):
        r"""Sets the end_reason of this RunningRecord.

        本次运行结束原因。

        :param end_reason: The end_reason of this RunningRecord.
        :type end_reason: str
        """
        self._end_reason = end_reason

    @property
    def end_related_task(self):
        r"""Gets the end_related_task of this RunningRecord.

        引发本次运行结束的task worker ID(如worker-0)。

        :return: The end_related_task of this RunningRecord.
        :rtype: str
        """
        return self._end_related_task

    @end_related_task.setter
    def end_related_task(self, end_related_task):
        r"""Sets the end_related_task of this RunningRecord.

        引发本次运行结束的task worker ID(如worker-0)。

        :param end_related_task: The end_related_task of this RunningRecord.
        :type end_related_task: str
        """
        self._end_related_task = end_related_task

    @property
    def end_recover(self):
        r"""Gets the end_recover of this RunningRecord.

        本次运行结束后所采取的故障容忍策略，枚举值如下： - npu_proc_restart: NPU原地热恢复 - gpu_proc_restart: GPU原地热恢复 - proc_restart: 进程原地重启 - pod_reschedule: Pod级重调度 - job_reschedule: Job级重调度 - job_reschedule_with_taint: 隔离式Job重调度

        :return: The end_recover of this RunningRecord.
        :rtype: str
        """
        return self._end_recover

    @end_recover.setter
    def end_recover(self, end_recover):
        r"""Sets the end_recover of this RunningRecord.

        本次运行结束后所采取的故障容忍策略，枚举值如下： - npu_proc_restart: NPU原地热恢复 - gpu_proc_restart: GPU原地热恢复 - proc_restart: 进程原地重启 - pod_reschedule: Pod级重调度 - job_reschedule: Job级重调度 - job_reschedule_with_taint: 隔离式Job重调度

        :param end_recover: The end_recover of this RunningRecord.
        :type end_recover: str
        """
        self._end_recover = end_recover

    @property
    def end_recover_before_downgrade(self):
        r"""Gets the end_recover_before_downgrade of this RunningRecord.

        本次运行结束后在故障容忍策略降级前所采取的容忍策略，取值范围同end_recover。

        :return: The end_recover_before_downgrade of this RunningRecord.
        :rtype: str
        """
        return self._end_recover_before_downgrade

    @end_recover_before_downgrade.setter
    def end_recover_before_downgrade(self, end_recover_before_downgrade):
        r"""Sets the end_recover_before_downgrade of this RunningRecord.

        本次运行结束后在故障容忍策略降级前所采取的容忍策略，取值范围同end_recover。

        :param end_recover_before_downgrade: The end_recover_before_downgrade of this RunningRecord.
        :type end_recover_before_downgrade: str
        """
        self._end_recover_before_downgrade = end_recover_before_downgrade

    @property
    def recover_records(self):
        r"""Gets the recover_records of this RunningRecord.

        **参数解释**：本次运行异常结束时采取的所有故障容忍策略详情。

        :return: The recover_records of this RunningRecord.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.RecoverRecord`]
        """
        return self._recover_records

    @recover_records.setter
    def recover_records(self, recover_records):
        r"""Sets the recover_records of this RunningRecord.

        **参数解释**：本次运行异常结束时采取的所有故障容忍策略详情。

        :param recover_records: The recover_records of this RunningRecord.
        :type recover_records: list[:class:`huaweicloudsdkmodelarts.v1.RecoverRecord`]
        """
        self._recover_records = recover_records

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
        if not isinstance(other, RunningRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
