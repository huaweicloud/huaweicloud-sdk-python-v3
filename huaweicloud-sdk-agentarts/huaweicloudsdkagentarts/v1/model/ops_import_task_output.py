# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsImportTaskOutput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'status': 'str',
        'progress': 'str',
        'success_count': 'str',
        'total_count': 'str',
        'error_detail': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'progress': 'progress',
        'success_count': 'success_count',
        'total_count': 'total_count',
        'error_detail': 'error_detail',
        'created_at': 'created_at'
    }

    def __init__(self, task_id=None, status=None, progress=None, success_count=None, total_count=None, error_detail=None, created_at=None):
        r"""OpsImportTaskOutput

        The model defined in huaweicloud sdk

        :param task_id: **参数解释：** 导入任务的唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 
        :type task_id: str
        :param status: **参数解释：** 导入任务的当前运行状态。 **取值范围：** - PENDING: 等待中 - RUNNING: 运行中 - SUCCESS: 成功 - FAILED: 失败 
        :type status: str
        :param progress: **参数解释：** 任务执行的百分比进度。 **取值范围：** 0%到100%。 
        :type progress: str
        :param success_count: **参数解释：** 导入成功的条目数量。 **取值范围：** 大于等于0的整数字符串。 
        :type success_count: str
        :param total_count: **参数解释：** 本次导入任务涉及的总数据条目数量。 **取值范围：** 0-100的整数字符串。 
        :type total_count: str
        :param error_detail: **参数解释：** 当任务状态为 FAILED 时，记录的详细错误信息或异常堆栈。 **取值范围：** 任意描述性字符串。 
        :type error_detail: str
        :param created_at: **参数解释：** 导入任务的发起时间。 **取值范围：** UTC时间格式字符串。 
        :type created_at: datetime
        """
        
        

        self._task_id = None
        self._status = None
        self._progress = None
        self._success_count = None
        self._total_count = None
        self._error_detail = None
        self._created_at = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if success_count is not None:
            self.success_count = success_count
        if total_count is not None:
            self.total_count = total_count
        if error_detail is not None:
            self.error_detail = error_detail
        if created_at is not None:
            self.created_at = created_at

    @property
    def task_id(self):
        r"""Gets the task_id of this OpsImportTaskOutput.

        **参数解释：** 导入任务的唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 

        :return: The task_id of this OpsImportTaskOutput.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this OpsImportTaskOutput.

        **参数解释：** 导入任务的唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 

        :param task_id: The task_id of this OpsImportTaskOutput.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        r"""Gets the status of this OpsImportTaskOutput.

        **参数解释：** 导入任务的当前运行状态。 **取值范围：** - PENDING: 等待中 - RUNNING: 运行中 - SUCCESS: 成功 - FAILED: 失败 

        :return: The status of this OpsImportTaskOutput.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OpsImportTaskOutput.

        **参数解释：** 导入任务的当前运行状态。 **取值范围：** - PENDING: 等待中 - RUNNING: 运行中 - SUCCESS: 成功 - FAILED: 失败 

        :param status: The status of this OpsImportTaskOutput.
        :type status: str
        """
        self._status = status

    @property
    def progress(self):
        r"""Gets the progress of this OpsImportTaskOutput.

        **参数解释：** 任务执行的百分比进度。 **取值范围：** 0%到100%。 

        :return: The progress of this OpsImportTaskOutput.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this OpsImportTaskOutput.

        **参数解释：** 任务执行的百分比进度。 **取值范围：** 0%到100%。 

        :param progress: The progress of this OpsImportTaskOutput.
        :type progress: str
        """
        self._progress = progress

    @property
    def success_count(self):
        r"""Gets the success_count of this OpsImportTaskOutput.

        **参数解释：** 导入成功的条目数量。 **取值范围：** 大于等于0的整数字符串。 

        :return: The success_count of this OpsImportTaskOutput.
        :rtype: str
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this OpsImportTaskOutput.

        **参数解释：** 导入成功的条目数量。 **取值范围：** 大于等于0的整数字符串。 

        :param success_count: The success_count of this OpsImportTaskOutput.
        :type success_count: str
        """
        self._success_count = success_count

    @property
    def total_count(self):
        r"""Gets the total_count of this OpsImportTaskOutput.

        **参数解释：** 本次导入任务涉及的总数据条目数量。 **取值范围：** 0-100的整数字符串。 

        :return: The total_count of this OpsImportTaskOutput.
        :rtype: str
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this OpsImportTaskOutput.

        **参数解释：** 本次导入任务涉及的总数据条目数量。 **取值范围：** 0-100的整数字符串。 

        :param total_count: The total_count of this OpsImportTaskOutput.
        :type total_count: str
        """
        self._total_count = total_count

    @property
    def error_detail(self):
        r"""Gets the error_detail of this OpsImportTaskOutput.

        **参数解释：** 当任务状态为 FAILED 时，记录的详细错误信息或异常堆栈。 **取值范围：** 任意描述性字符串。 

        :return: The error_detail of this OpsImportTaskOutput.
        :rtype: str
        """
        return self._error_detail

    @error_detail.setter
    def error_detail(self, error_detail):
        r"""Sets the error_detail of this OpsImportTaskOutput.

        **参数解释：** 当任务状态为 FAILED 时，记录的详细错误信息或异常堆栈。 **取值范围：** 任意描述性字符串。 

        :param error_detail: The error_detail of this OpsImportTaskOutput.
        :type error_detail: str
        """
        self._error_detail = error_detail

    @property
    def created_at(self):
        r"""Gets the created_at of this OpsImportTaskOutput.

        **参数解释：** 导入任务的发起时间。 **取值范围：** UTC时间格式字符串。 

        :return: The created_at of this OpsImportTaskOutput.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this OpsImportTaskOutput.

        **参数解释：** 导入任务的发起时间。 **取值范围：** UTC时间格式字符串。 

        :param created_at: The created_at of this OpsImportTaskOutput.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, OpsImportTaskOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
