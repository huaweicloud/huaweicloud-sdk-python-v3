# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecoverRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recover_start_at': 'int',
        'recover_end_at': 'int',
        'recover': 'str',
        'fault_scenario': 'str',
        'reason': 'str',
        'related_task': 'str',
        'recover_result': 'str'
    }

    attribute_map = {
        'recover_start_at': 'recover_start_at',
        'recover_end_at': 'recover_end_at',
        'recover': 'recover',
        'fault_scenario': 'fault_scenario',
        'reason': 'reason',
        'related_task': 'related_task',
        'recover_result': 'recover_result'
    }

    def __init__(self, recover_start_at=None, recover_end_at=None, recover=None, fault_scenario=None, reason=None, related_task=None, recover_result=None):
        r"""RecoverRecord

        The model defined in huaweicloud sdk

        :param recover_start_at: **参数描述**：本次故障容忍策略开始执行时间的unix时间戳，单位为秒(s)，同时也是故障发生时间。 **取值范围**：不涉及。
        :type recover_start_at: int
        :param recover_end_at: **参数描述**：本次故障容忍策略结束时间的unix时间戳，单位为秒(s)。 **取值范围**：不涉及。
        :type recover_end_at: int
        :param recover: **参数描述**：本次故障容忍策略。 **取值范围**：枚举值如下： - npu_step_retry: Step重计算 - npu_proc_restart: NPU原地热恢复 - proc_restart: 进程原地重启 - pod_reschedule: Pod级重调度 - job_reschedule: Job级重调度 - job_reschedule_with_taint: 隔离式Job重调度
        :type recover: str
        :param fault_scenario: **参数描述**：本次故障场景。 **取值范围**：枚举值如下： - chip_fault: 芯片故障 - node_fault: 节点故障 - job_failed: 作业失败退出 - job_hanged: 作业卡死 - job_subhealth: 作业亚健康 - error_in_log: 日志异常
        :type fault_scenario: str
        :param reason: **参数描述**：本次故障原因。 **取值范围**：不涉及。
        :type reason: str
        :param related_task: **参数描述**：引发本次运行结束的task worker ID(如worker-0)。 **取值范围**：不涉及。
        :type related_task: str
        :param recover_result: **参数描述**：本次故障执行结果。 **取值范围**：枚举值如下： - recovering: 执行中 - success: 成功 - failed: 失败 - downgrade: 策略降级 - terminated: 策略被终止 - quotaExceeded: 策略执行次数超限制
        :type recover_result: str
        """
        
        

        self._recover_start_at = None
        self._recover_end_at = None
        self._recover = None
        self._fault_scenario = None
        self._reason = None
        self._related_task = None
        self._recover_result = None
        self.discriminator = None

        if recover_start_at is not None:
            self.recover_start_at = recover_start_at
        if recover_end_at is not None:
            self.recover_end_at = recover_end_at
        if recover is not None:
            self.recover = recover
        if fault_scenario is not None:
            self.fault_scenario = fault_scenario
        if reason is not None:
            self.reason = reason
        if related_task is not None:
            self.related_task = related_task
        if recover_result is not None:
            self.recover_result = recover_result

    @property
    def recover_start_at(self):
        r"""Gets the recover_start_at of this RecoverRecord.

        **参数描述**：本次故障容忍策略开始执行时间的unix时间戳，单位为秒(s)，同时也是故障发生时间。 **取值范围**：不涉及。

        :return: The recover_start_at of this RecoverRecord.
        :rtype: int
        """
        return self._recover_start_at

    @recover_start_at.setter
    def recover_start_at(self, recover_start_at):
        r"""Sets the recover_start_at of this RecoverRecord.

        **参数描述**：本次故障容忍策略开始执行时间的unix时间戳，单位为秒(s)，同时也是故障发生时间。 **取值范围**：不涉及。

        :param recover_start_at: The recover_start_at of this RecoverRecord.
        :type recover_start_at: int
        """
        self._recover_start_at = recover_start_at

    @property
    def recover_end_at(self):
        r"""Gets the recover_end_at of this RecoverRecord.

        **参数描述**：本次故障容忍策略结束时间的unix时间戳，单位为秒(s)。 **取值范围**：不涉及。

        :return: The recover_end_at of this RecoverRecord.
        :rtype: int
        """
        return self._recover_end_at

    @recover_end_at.setter
    def recover_end_at(self, recover_end_at):
        r"""Sets the recover_end_at of this RecoverRecord.

        **参数描述**：本次故障容忍策略结束时间的unix时间戳，单位为秒(s)。 **取值范围**：不涉及。

        :param recover_end_at: The recover_end_at of this RecoverRecord.
        :type recover_end_at: int
        """
        self._recover_end_at = recover_end_at

    @property
    def recover(self):
        r"""Gets the recover of this RecoverRecord.

        **参数描述**：本次故障容忍策略。 **取值范围**：枚举值如下： - npu_step_retry: Step重计算 - npu_proc_restart: NPU原地热恢复 - proc_restart: 进程原地重启 - pod_reschedule: Pod级重调度 - job_reschedule: Job级重调度 - job_reschedule_with_taint: 隔离式Job重调度

        :return: The recover of this RecoverRecord.
        :rtype: str
        """
        return self._recover

    @recover.setter
    def recover(self, recover):
        r"""Sets the recover of this RecoverRecord.

        **参数描述**：本次故障容忍策略。 **取值范围**：枚举值如下： - npu_step_retry: Step重计算 - npu_proc_restart: NPU原地热恢复 - proc_restart: 进程原地重启 - pod_reschedule: Pod级重调度 - job_reschedule: Job级重调度 - job_reschedule_with_taint: 隔离式Job重调度

        :param recover: The recover of this RecoverRecord.
        :type recover: str
        """
        self._recover = recover

    @property
    def fault_scenario(self):
        r"""Gets the fault_scenario of this RecoverRecord.

        **参数描述**：本次故障场景。 **取值范围**：枚举值如下： - chip_fault: 芯片故障 - node_fault: 节点故障 - job_failed: 作业失败退出 - job_hanged: 作业卡死 - job_subhealth: 作业亚健康 - error_in_log: 日志异常

        :return: The fault_scenario of this RecoverRecord.
        :rtype: str
        """
        return self._fault_scenario

    @fault_scenario.setter
    def fault_scenario(self, fault_scenario):
        r"""Sets the fault_scenario of this RecoverRecord.

        **参数描述**：本次故障场景。 **取值范围**：枚举值如下： - chip_fault: 芯片故障 - node_fault: 节点故障 - job_failed: 作业失败退出 - job_hanged: 作业卡死 - job_subhealth: 作业亚健康 - error_in_log: 日志异常

        :param fault_scenario: The fault_scenario of this RecoverRecord.
        :type fault_scenario: str
        """
        self._fault_scenario = fault_scenario

    @property
    def reason(self):
        r"""Gets the reason of this RecoverRecord.

        **参数描述**：本次故障原因。 **取值范围**：不涉及。

        :return: The reason of this RecoverRecord.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this RecoverRecord.

        **参数描述**：本次故障原因。 **取值范围**：不涉及。

        :param reason: The reason of this RecoverRecord.
        :type reason: str
        """
        self._reason = reason

    @property
    def related_task(self):
        r"""Gets the related_task of this RecoverRecord.

        **参数描述**：引发本次运行结束的task worker ID(如worker-0)。 **取值范围**：不涉及。

        :return: The related_task of this RecoverRecord.
        :rtype: str
        """
        return self._related_task

    @related_task.setter
    def related_task(self, related_task):
        r"""Sets the related_task of this RecoverRecord.

        **参数描述**：引发本次运行结束的task worker ID(如worker-0)。 **取值范围**：不涉及。

        :param related_task: The related_task of this RecoverRecord.
        :type related_task: str
        """
        self._related_task = related_task

    @property
    def recover_result(self):
        r"""Gets the recover_result of this RecoverRecord.

        **参数描述**：本次故障执行结果。 **取值范围**：枚举值如下： - recovering: 执行中 - success: 成功 - failed: 失败 - downgrade: 策略降级 - terminated: 策略被终止 - quotaExceeded: 策略执行次数超限制

        :return: The recover_result of this RecoverRecord.
        :rtype: str
        """
        return self._recover_result

    @recover_result.setter
    def recover_result(self, recover_result):
        r"""Sets the recover_result of this RecoverRecord.

        **参数描述**：本次故障执行结果。 **取值范围**：枚举值如下： - recovering: 执行中 - success: 成功 - failed: 失败 - downgrade: 策略降级 - terminated: 策略被终止 - quotaExceeded: 策略执行次数超限制

        :param recover_result: The recover_result of this RecoverRecord.
        :type recover_result: str
        """
        self._recover_result = recover_result

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
        if not isinstance(other, RecoverRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
