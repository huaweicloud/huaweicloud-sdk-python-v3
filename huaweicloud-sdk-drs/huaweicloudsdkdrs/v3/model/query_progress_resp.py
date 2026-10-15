# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryProgressResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'progress': 'str',
        'incre_trans_delay': 'str',
        'incre_trans_delay_millis': 'str',
        'task_mode': 'str',
        'transfer_status': 'str',
        'process_time': 'str',
        'remaining_time': 'str',
        'progress_map': 'dict(str, ProgressInfo)',
        'error_code': 'str',
        'error_msg': 'str',
        'apply_rows_rate': 'int',
        'apply_bytes_rate': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'progress': 'progress',
        'incre_trans_delay': 'incre_trans_delay',
        'incre_trans_delay_millis': 'incre_trans_delay_millis',
        'task_mode': 'task_mode',
        'transfer_status': 'transfer_status',
        'process_time': 'process_time',
        'remaining_time': 'remaining_time',
        'progress_map': 'progress_map',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'apply_rows_rate': 'apply_rows_rate',
        'apply_bytes_rate': 'apply_bytes_rate'
    }

    def __init__(self, job_id=None, progress=None, incre_trans_delay=None, incre_trans_delay_millis=None, task_mode=None, transfer_status=None, process_time=None, remaining_time=None, progress_map=None, error_code=None, error_msg=None, apply_rows_rate=None, apply_bytes_rate=None):
        r"""QueryProgressResp

        The model defined in huaweicloud sdk

        :param job_id: **参数解释**：  迁移任务ID，用于唯一标识一个数据复制任务，在查询、修改、删除等操作中作为任务的识别凭证。  **约束限制**：  不涉及。  **取值范围**：  UUID格式字符串。  **默认取值**：  不涉及
        :type job_id: str
        :param progress: **参数解释**：  迁移百分比，表示当前任务的数据迁移完成进度。  **约束限制**：  不涉及。  **取值范围**：  0-100。  **默认取值**：  不涉及
        :type progress: str
        :param incre_trans_delay: **参数解释**：  增量迁移时延。当任务处于增量阶段时，该值表示源库与目标库之间的数据同步延迟。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type incre_trans_delay: str
        :param incre_trans_delay_millis: **参数解释**：  增量迁移时延，与incre_trans_delay含义相同，但以毫秒为单位提供更精确的时延信息。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type incre_trans_delay_millis: str
        :param task_mode: **参数解释**：  任务迁移模式，指定数据复制任务的执行方式。  **约束限制**：  单主灾备场景仅支持选择FULL_INCR_TRANS（全量+增量）。  **取值范围**：  - FULL_TRANS：全量迁移，仅迁移历史数据，迁移完成后任务结束 - INCR_TRANS：增量迁移，仅同步新增数据变更，适用于持续同步场景 - FULL_INCR_TRANS：全量+增量迁移，先迁移历史数据再持续同步增量，适用于平滑切换场景  **默认取值**：  不涉及
        :type task_mode: str
        :param transfer_status: **参数解释**：  任务当前传输状态，表示数据迁移任务所处的运行阶段，可用于判断任务是否正常推进。  **约束限制**：  不涉及。  **取值范围**：  - CREATING：创建中 - CREATE_FAILED：创建失败 - CONFIGURATION：配置中 - WAITING_FOR_START：等待启动中 - RELEASE_RESOURCE_COMPLETE：已结束 - DELETED：已删除 - INCRE_TRANSFER_STARTED：增量迁移中 - INCRE_TRANSFER_FAILED：增量迁移失败 - FULL_TRANSFER_STARTED：全量迁移中 - FULL_TRANSFER_COMPLETE：全量迁移完成 - PAUSING：暂停中 - FULL_TRANSFER_FAILED：全量迁移失败  **默认取值**：  不涉及
        :type transfer_status: str
        :param process_time: **参数解释**：  迁移时间，格式为毫秒级Unix时间戳，表示任务最近一次进度更新时间。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type process_time: str
        :param remaining_time: **参数解释**：  预计剩余完成时间，单位为秒。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type remaining_time: str
        :param progress_map: **参数解释**：  数据、结构、索引迁移进度信息体，详情请参见ProgressInfo定义。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type progress_map: dict(str, ProgressInfo)
        :param error_code: **参数解释**：  错误码，当任务报错时返回的错误代码。  **约束限制**：  不涉及。  **取值范围**：  格式为DRS.XXXXXX。  **默认取值**：  不涉及
        :type error_code: str
        :param error_msg: **参数解释**：  错误详细信息，当任务执行失败时返回的具体错误描述。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type error_msg: str
        :param apply_rows_rate: **参数解释**：  增量迁移RPS。  **约束限制**：  值为-1时代表任务尚未进入到增量状态。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type apply_rows_rate: int
        :param apply_bytes_rate: **参数解释**：  增量迁移网络流量。  **约束限制**：  值为-1时代表任务尚未进入到增量状态。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type apply_bytes_rate: int
        """
        
        

        self._job_id = None
        self._progress = None
        self._incre_trans_delay = None
        self._incre_trans_delay_millis = None
        self._task_mode = None
        self._transfer_status = None
        self._process_time = None
        self._remaining_time = None
        self._progress_map = None
        self._error_code = None
        self._error_msg = None
        self._apply_rows_rate = None
        self._apply_bytes_rate = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if progress is not None:
            self.progress = progress
        if incre_trans_delay is not None:
            self.incre_trans_delay = incre_trans_delay
        if incre_trans_delay_millis is not None:
            self.incre_trans_delay_millis = incre_trans_delay_millis
        if task_mode is not None:
            self.task_mode = task_mode
        if transfer_status is not None:
            self.transfer_status = transfer_status
        if process_time is not None:
            self.process_time = process_time
        if remaining_time is not None:
            self.remaining_time = remaining_time
        if progress_map is not None:
            self.progress_map = progress_map
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if apply_rows_rate is not None:
            self.apply_rows_rate = apply_rows_rate
        if apply_bytes_rate is not None:
            self.apply_bytes_rate = apply_bytes_rate

    @property
    def job_id(self):
        r"""Gets the job_id of this QueryProgressResp.

        **参数解释**：  迁移任务ID，用于唯一标识一个数据复制任务，在查询、修改、删除等操作中作为任务的识别凭证。  **约束限制**：  不涉及。  **取值范围**：  UUID格式字符串。  **默认取值**：  不涉及

        :return: The job_id of this QueryProgressResp.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this QueryProgressResp.

        **参数解释**：  迁移任务ID，用于唯一标识一个数据复制任务，在查询、修改、删除等操作中作为任务的识别凭证。  **约束限制**：  不涉及。  **取值范围**：  UUID格式字符串。  **默认取值**：  不涉及

        :param job_id: The job_id of this QueryProgressResp.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def progress(self):
        r"""Gets the progress of this QueryProgressResp.

        **参数解释**：  迁移百分比，表示当前任务的数据迁移完成进度。  **约束限制**：  不涉及。  **取值范围**：  0-100。  **默认取值**：  不涉及

        :return: The progress of this QueryProgressResp.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this QueryProgressResp.

        **参数解释**：  迁移百分比，表示当前任务的数据迁移完成进度。  **约束限制**：  不涉及。  **取值范围**：  0-100。  **默认取值**：  不涉及

        :param progress: The progress of this QueryProgressResp.
        :type progress: str
        """
        self._progress = progress

    @property
    def incre_trans_delay(self):
        r"""Gets the incre_trans_delay of this QueryProgressResp.

        **参数解释**：  增量迁移时延。当任务处于增量阶段时，该值表示源库与目标库之间的数据同步延迟。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The incre_trans_delay of this QueryProgressResp.
        :rtype: str
        """
        return self._incre_trans_delay

    @incre_trans_delay.setter
    def incre_trans_delay(self, incre_trans_delay):
        r"""Sets the incre_trans_delay of this QueryProgressResp.

        **参数解释**：  增量迁移时延。当任务处于增量阶段时，该值表示源库与目标库之间的数据同步延迟。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param incre_trans_delay: The incre_trans_delay of this QueryProgressResp.
        :type incre_trans_delay: str
        """
        self._incre_trans_delay = incre_trans_delay

    @property
    def incre_trans_delay_millis(self):
        r"""Gets the incre_trans_delay_millis of this QueryProgressResp.

        **参数解释**：  增量迁移时延，与incre_trans_delay含义相同，但以毫秒为单位提供更精确的时延信息。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The incre_trans_delay_millis of this QueryProgressResp.
        :rtype: str
        """
        return self._incre_trans_delay_millis

    @incre_trans_delay_millis.setter
    def incre_trans_delay_millis(self, incre_trans_delay_millis):
        r"""Sets the incre_trans_delay_millis of this QueryProgressResp.

        **参数解释**：  增量迁移时延，与incre_trans_delay含义相同，但以毫秒为单位提供更精确的时延信息。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param incre_trans_delay_millis: The incre_trans_delay_millis of this QueryProgressResp.
        :type incre_trans_delay_millis: str
        """
        self._incre_trans_delay_millis = incre_trans_delay_millis

    @property
    def task_mode(self):
        r"""Gets the task_mode of this QueryProgressResp.

        **参数解释**：  任务迁移模式，指定数据复制任务的执行方式。  **约束限制**：  单主灾备场景仅支持选择FULL_INCR_TRANS（全量+增量）。  **取值范围**：  - FULL_TRANS：全量迁移，仅迁移历史数据，迁移完成后任务结束 - INCR_TRANS：增量迁移，仅同步新增数据变更，适用于持续同步场景 - FULL_INCR_TRANS：全量+增量迁移，先迁移历史数据再持续同步增量，适用于平滑切换场景  **默认取值**：  不涉及

        :return: The task_mode of this QueryProgressResp.
        :rtype: str
        """
        return self._task_mode

    @task_mode.setter
    def task_mode(self, task_mode):
        r"""Sets the task_mode of this QueryProgressResp.

        **参数解释**：  任务迁移模式，指定数据复制任务的执行方式。  **约束限制**：  单主灾备场景仅支持选择FULL_INCR_TRANS（全量+增量）。  **取值范围**：  - FULL_TRANS：全量迁移，仅迁移历史数据，迁移完成后任务结束 - INCR_TRANS：增量迁移，仅同步新增数据变更，适用于持续同步场景 - FULL_INCR_TRANS：全量+增量迁移，先迁移历史数据再持续同步增量，适用于平滑切换场景  **默认取值**：  不涉及

        :param task_mode: The task_mode of this QueryProgressResp.
        :type task_mode: str
        """
        self._task_mode = task_mode

    @property
    def transfer_status(self):
        r"""Gets the transfer_status of this QueryProgressResp.

        **参数解释**：  任务当前传输状态，表示数据迁移任务所处的运行阶段，可用于判断任务是否正常推进。  **约束限制**：  不涉及。  **取值范围**：  - CREATING：创建中 - CREATE_FAILED：创建失败 - CONFIGURATION：配置中 - WAITING_FOR_START：等待启动中 - RELEASE_RESOURCE_COMPLETE：已结束 - DELETED：已删除 - INCRE_TRANSFER_STARTED：增量迁移中 - INCRE_TRANSFER_FAILED：增量迁移失败 - FULL_TRANSFER_STARTED：全量迁移中 - FULL_TRANSFER_COMPLETE：全量迁移完成 - PAUSING：暂停中 - FULL_TRANSFER_FAILED：全量迁移失败  **默认取值**：  不涉及

        :return: The transfer_status of this QueryProgressResp.
        :rtype: str
        """
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, transfer_status):
        r"""Sets the transfer_status of this QueryProgressResp.

        **参数解释**：  任务当前传输状态，表示数据迁移任务所处的运行阶段，可用于判断任务是否正常推进。  **约束限制**：  不涉及。  **取值范围**：  - CREATING：创建中 - CREATE_FAILED：创建失败 - CONFIGURATION：配置中 - WAITING_FOR_START：等待启动中 - RELEASE_RESOURCE_COMPLETE：已结束 - DELETED：已删除 - INCRE_TRANSFER_STARTED：增量迁移中 - INCRE_TRANSFER_FAILED：增量迁移失败 - FULL_TRANSFER_STARTED：全量迁移中 - FULL_TRANSFER_COMPLETE：全量迁移完成 - PAUSING：暂停中 - FULL_TRANSFER_FAILED：全量迁移失败  **默认取值**：  不涉及

        :param transfer_status: The transfer_status of this QueryProgressResp.
        :type transfer_status: str
        """
        self._transfer_status = transfer_status

    @property
    def process_time(self):
        r"""Gets the process_time of this QueryProgressResp.

        **参数解释**：  迁移时间，格式为毫秒级Unix时间戳，表示任务最近一次进度更新时间。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The process_time of this QueryProgressResp.
        :rtype: str
        """
        return self._process_time

    @process_time.setter
    def process_time(self, process_time):
        r"""Sets the process_time of this QueryProgressResp.

        **参数解释**：  迁移时间，格式为毫秒级Unix时间戳，表示任务最近一次进度更新时间。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param process_time: The process_time of this QueryProgressResp.
        :type process_time: str
        """
        self._process_time = process_time

    @property
    def remaining_time(self):
        r"""Gets the remaining_time of this QueryProgressResp.

        **参数解释**：  预计剩余完成时间，单位为秒。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The remaining_time of this QueryProgressResp.
        :rtype: str
        """
        return self._remaining_time

    @remaining_time.setter
    def remaining_time(self, remaining_time):
        r"""Sets the remaining_time of this QueryProgressResp.

        **参数解释**：  预计剩余完成时间，单位为秒。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param remaining_time: The remaining_time of this QueryProgressResp.
        :type remaining_time: str
        """
        self._remaining_time = remaining_time

    @property
    def progress_map(self):
        r"""Gets the progress_map of this QueryProgressResp.

        **参数解释**：  数据、结构、索引迁移进度信息体，详情请参见ProgressInfo定义。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The progress_map of this QueryProgressResp.
        :rtype: dict(str, ProgressInfo)
        """
        return self._progress_map

    @progress_map.setter
    def progress_map(self, progress_map):
        r"""Sets the progress_map of this QueryProgressResp.

        **参数解释**：  数据、结构、索引迁移进度信息体，详情请参见ProgressInfo定义。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param progress_map: The progress_map of this QueryProgressResp.
        :type progress_map: dict(str, ProgressInfo)
        """
        self._progress_map = progress_map

    @property
    def error_code(self):
        r"""Gets the error_code of this QueryProgressResp.

        **参数解释**：  错误码，当任务报错时返回的错误代码。  **约束限制**：  不涉及。  **取值范围**：  格式为DRS.XXXXXX。  **默认取值**：  不涉及

        :return: The error_code of this QueryProgressResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this QueryProgressResp.

        **参数解释**：  错误码，当任务报错时返回的错误代码。  **约束限制**：  不涉及。  **取值范围**：  格式为DRS.XXXXXX。  **默认取值**：  不涉及

        :param error_code: The error_code of this QueryProgressResp.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this QueryProgressResp.

        **参数解释**：  错误详细信息，当任务执行失败时返回的具体错误描述。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The error_msg of this QueryProgressResp.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this QueryProgressResp.

        **参数解释**：  错误详细信息，当任务执行失败时返回的具体错误描述。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param error_msg: The error_msg of this QueryProgressResp.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def apply_rows_rate(self):
        r"""Gets the apply_rows_rate of this QueryProgressResp.

        **参数解释**：  增量迁移RPS。  **约束限制**：  值为-1时代表任务尚未进入到增量状态。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The apply_rows_rate of this QueryProgressResp.
        :rtype: int
        """
        return self._apply_rows_rate

    @apply_rows_rate.setter
    def apply_rows_rate(self, apply_rows_rate):
        r"""Sets the apply_rows_rate of this QueryProgressResp.

        **参数解释**：  增量迁移RPS。  **约束限制**：  值为-1时代表任务尚未进入到增量状态。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param apply_rows_rate: The apply_rows_rate of this QueryProgressResp.
        :type apply_rows_rate: int
        """
        self._apply_rows_rate = apply_rows_rate

    @property
    def apply_bytes_rate(self):
        r"""Gets the apply_bytes_rate of this QueryProgressResp.

        **参数解释**：  增量迁移网络流量。  **约束限制**：  值为-1时代表任务尚未进入到增量状态。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The apply_bytes_rate of this QueryProgressResp.
        :rtype: int
        """
        return self._apply_bytes_rate

    @apply_bytes_rate.setter
    def apply_bytes_rate(self, apply_bytes_rate):
        r"""Sets the apply_bytes_rate of this QueryProgressResp.

        **参数解释**：  增量迁移网络流量。  **约束限制**：  值为-1时代表任务尚未进入到增量状态。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param apply_bytes_rate: The apply_bytes_rate of this QueryProgressResp.
        :type apply_bytes_rate: int
        """
        self._apply_bytes_rate = apply_bytes_rate

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
        if not isinstance(other, QueryProgressResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
