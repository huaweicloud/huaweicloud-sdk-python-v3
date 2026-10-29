# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobBasicInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'executor': 'str',
        'finish_time': 'str',
        'job_result': 'JobResultInfo',
        'job_type': 'str',
        'process': 'ProcessInfo',
        'start_time': 'str',
        'status': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'executor': 'executor',
        'finish_time': 'finishTime',
        'job_result': 'jobResult',
        'job_type': 'jobType',
        'process': 'process',
        'start_time': 'startTime',
        'status': 'status',
        'task_id': 'taskId'
    }

    def __init__(self, executor=None, finish_time=None, job_result=None, job_type=None, process=None, start_time=None, status=None, task_id=None):
        r"""JobBasicInfo

        The model defined in huaweicloud sdk

        :param executor: **参数解释：** 执行人用户名。 **取值范围：** 不涉及。
        :type executor: str
        :param finish_time: **参数解释：** 执行记录的检查完成时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\&quot;2025-11-28T06:55:41Z\&quot;。 **取值范围：** 不涉及。
        :type finish_time: str
        :param job_result: 
        :type job_result: :class:`huaweicloudsdkcodeartscheck.v2.JobResultInfo`
        :param job_type: **参数解释:** 任务类型。 **取值范围:** - FULL：版本级任务。 - INC_GIT：门禁级任务。 [- INC_COMMIT：流水线指定commitId增量检查、代码检查任务设置-检查范围-版本级检查模式的最近一次提交检查。](tag:hws,hws_hk) [- INC_COMMIT：代码检查任务设置-检查范围-版本级检查模式的最近一次提交检查。](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs) [- INC_LAST_SUCCESS_COMMIT：流水线指定commitId以及最后一次门禁成功的commitId间的增量检查。](tag:hws,hws_hk)
        :type job_type: str
        :param process: 
        :type process: :class:`huaweicloudsdkcodeartscheck.v2.ProcessInfo`
        :param start_time: **参数解释：**  执行记录的检查开始时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\&quot;2025-11-28T06:55:41Z\&quot;。 **取值范围：** 不涉及。
        :type start_time: str
        :param status: **参数解释:** 任务执行状态。 **取值范围:** - quering：初始状态。 - running：执行中。 - success：检查成功。 - failed：检查失败。 - aborted：任务中止。
        :type status: str
        :param task_id: **参数解释：**  任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **取值范围：** 长度为[1~32]个字符。
        :type task_id: str
        """
        
        

        self._executor = None
        self._finish_time = None
        self._job_result = None
        self._job_type = None
        self._process = None
        self._start_time = None
        self._status = None
        self._task_id = None
        self.discriminator = None

        if executor is not None:
            self.executor = executor
        if finish_time is not None:
            self.finish_time = finish_time
        if job_result is not None:
            self.job_result = job_result
        if job_type is not None:
            self.job_type = job_type
        if process is not None:
            self.process = process
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if task_id is not None:
            self.task_id = task_id

    @property
    def executor(self):
        r"""Gets the executor of this JobBasicInfo.

        **参数解释：** 执行人用户名。 **取值范围：** 不涉及。

        :return: The executor of this JobBasicInfo.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        r"""Sets the executor of this JobBasicInfo.

        **参数解释：** 执行人用户名。 **取值范围：** 不涉及。

        :param executor: The executor of this JobBasicInfo.
        :type executor: str
        """
        self._executor = executor

    @property
    def finish_time(self):
        r"""Gets the finish_time of this JobBasicInfo.

        **参数解释：** 执行记录的检查完成时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :return: The finish_time of this JobBasicInfo.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this JobBasicInfo.

        **参数解释：** 执行记录的检查完成时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :param finish_time: The finish_time of this JobBasicInfo.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def job_result(self):
        r"""Gets the job_result of this JobBasicInfo.

        :return: The job_result of this JobBasicInfo.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.JobResultInfo`
        """
        return self._job_result

    @job_result.setter
    def job_result(self, job_result):
        r"""Sets the job_result of this JobBasicInfo.

        :param job_result: The job_result of this JobBasicInfo.
        :type job_result: :class:`huaweicloudsdkcodeartscheck.v2.JobResultInfo`
        """
        self._job_result = job_result

    @property
    def job_type(self):
        r"""Gets the job_type of this JobBasicInfo.

        **参数解释:** 任务类型。 **取值范围:** - FULL：版本级任务。 - INC_GIT：门禁级任务。 [- INC_COMMIT：流水线指定commitId增量检查、代码检查任务设置-检查范围-版本级检查模式的最近一次提交检查。](tag:hws,hws_hk) [- INC_COMMIT：代码检查任务设置-检查范围-版本级检查模式的最近一次提交检查。](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs) [- INC_LAST_SUCCESS_COMMIT：流水线指定commitId以及最后一次门禁成功的commitId间的增量检查。](tag:hws,hws_hk)

        :return: The job_type of this JobBasicInfo.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this JobBasicInfo.

        **参数解释:** 任务类型。 **取值范围:** - FULL：版本级任务。 - INC_GIT：门禁级任务。 [- INC_COMMIT：流水线指定commitId增量检查、代码检查任务设置-检查范围-版本级检查模式的最近一次提交检查。](tag:hws,hws_hk) [- INC_COMMIT：代码检查任务设置-检查范围-版本级检查模式的最近一次提交检查。](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs) [- INC_LAST_SUCCESS_COMMIT：流水线指定commitId以及最后一次门禁成功的commitId间的增量检查。](tag:hws,hws_hk)

        :param job_type: The job_type of this JobBasicInfo.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def process(self):
        r"""Gets the process of this JobBasicInfo.

        :return: The process of this JobBasicInfo.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ProcessInfo`
        """
        return self._process

    @process.setter
    def process(self, process):
        r"""Sets the process of this JobBasicInfo.

        :param process: The process of this JobBasicInfo.
        :type process: :class:`huaweicloudsdkcodeartscheck.v2.ProcessInfo`
        """
        self._process = process

    @property
    def start_time(self):
        r"""Gets the start_time of this JobBasicInfo.

        **参数解释：**  执行记录的检查开始时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :return: The start_time of this JobBasicInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this JobBasicInfo.

        **参数解释：**  执行记录的检查开始时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :param start_time: The start_time of this JobBasicInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def status(self):
        r"""Gets the status of this JobBasicInfo.

        **参数解释:** 任务执行状态。 **取值范围:** - quering：初始状态。 - running：执行中。 - success：检查成功。 - failed：检查失败。 - aborted：任务中止。

        :return: The status of this JobBasicInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobBasicInfo.

        **参数解释:** 任务执行状态。 **取值范围:** - quering：初始状态。 - running：执行中。 - success：检查成功。 - failed：检查失败。 - aborted：任务中止。

        :param status: The status of this JobBasicInfo.
        :type status: str
        """
        self._status = status

    @property
    def task_id(self):
        r"""Gets the task_id of this JobBasicInfo.

        **参数解释：**  任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **取值范围：** 长度为[1~32]个字符。

        :return: The task_id of this JobBasicInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this JobBasicInfo.

        **参数解释：**  任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **取值范围：** 长度为[1~32]个字符。

        :param task_id: The task_id of this JobBasicInfo.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, JobBasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
