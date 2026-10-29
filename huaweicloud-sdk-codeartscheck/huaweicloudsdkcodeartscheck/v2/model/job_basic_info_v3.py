# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobBasicInfoV3:

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
        'id': 'str',
        'job_result': 'JobResultInfo',
        'job_type': 'str',
        'process': 'ProcessInfo',
        'review_result': 'str',
        'rule_sets': 'list[ConfigTemplateRuleSetInfo]',
        'source': 'str',
        'source_repo_url': 'str',
        'start_time': 'str',
        'status': 'str',
        'sub_job_ids': 'list[str]',
        'sub_job_statuses': 'list[str]',
        'target_repo_url': 'str',
        'task_id': 'str',
        'total_execute_time': 'str'
    }

    attribute_map = {
        'executor': 'executor',
        'finish_time': 'finishTime',
        'id': 'id',
        'job_result': 'jobResult',
        'job_type': 'jobType',
        'process': 'process',
        'review_result': 'reviewResult',
        'rule_sets': 'ruleSets',
        'source': 'source',
        'source_repo_url': 'sourceRepoUrl',
        'start_time': 'startTime',
        'status': 'status',
        'sub_job_ids': 'subJobIds',
        'sub_job_statuses': 'subJobStatuses',
        'target_repo_url': 'targetRepoUrl',
        'task_id': 'taskId',
        'total_execute_time': 'totalExecuteTime'
    }

    def __init__(self, executor=None, finish_time=None, id=None, job_result=None, job_type=None, process=None, review_result=None, rule_sets=None, source=None, source_repo_url=None, start_time=None, status=None, sub_job_ids=None, sub_job_statuses=None, target_repo_url=None, task_id=None, total_execute_time=None):
        r"""JobBasicInfoV3

        The model defined in huaweicloud sdk

        :param executor: **参数解释：** 执行人用户名。 **取值范围：** 长度为[1~255]个字符。
        :type executor: str
        :param finish_time: **参数解释：** 执行记录的检查完成时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\&quot;2025-11-28T06:55:41Z\&quot;。 **取值范围：** 不涉及。
        :type finish_time: str
        :param id: **参数解释：** 执行ID，来自代码检查执行任务接口的返回值，每次执行代码检查任务都有唯一的执行ID。 **取值范围：** 长度为[1~32]个字符。
        :type id: str
        :param job_result: 
        :type job_result: :class:`huaweicloudsdkcodeartscheck.v2.JobResultInfo`
        :param job_type: **参数解释:** 任务类型。 **取值范围:** - FULL：版本级任务。 - INC_GIT：门禁级任务。 [- INC_COMMIT：流水线指定commitId增量检查、代码检查任务设置-检查范围-版本级检查模式的最近一次提交检查。](tag:hws,hws_hk) [- INC_COMMIT：代码检查任务设置-检查范围-版本级检查模式的最近一次提交检查。](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs) [- INC_LAST_SUCCESS_COMMIT：流水线指定commitId以及最后一次门禁成功的commitId间的增量检查。](tag:hws,hws_hk)
        :type job_type: str
        :param process: 
        :type process: :class:`huaweicloudsdkcodeartscheck.v2.ProcessInfo`
        :param review_result: **参数解释：** 门禁结果。 **取值范围：** - success：门禁通过。 - error：门禁未通过。
        :type review_result: str
        :param rule_sets: **参数解释：** 规则集配置列表。
        :type rule_sets: list[:class:`huaweicloudsdkcodeartscheck.v2.ConfigTemplateRuleSetInfo`]
        :param source: **参数解释：** 执行来源。 **取值范围：** - customer：来自页面点击。 - Scheduled：来自定时任务。 - CodeCheckEdge：来自Edge服务。 - CodeArtsPipeline：来自流水线。 - DevCloudWebhook：来自CodeArtsRepo的Webhook。 - GitCodeActionPipeline：来自流水线的GitCodeAction插件。
        :type source: str
        :param source_repo_url: **参数解释：** 源分支的代码仓地址。 **取值范围：** 长度为[1~1024]个字符。
        :type source_repo_url: str
        :param start_time: **参数解释：**  执行记录的检查开始时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\&quot;2025-11-28T06:55:41Z\&quot;。 **取值范围：** 不涉及。
        :type start_time: str
        :param status: **参数解释:** 任务执行状态。 **取值范围:** - quering：初始状态。 - running：执行中。 - success：检查成功。 - failed：检查失败。 - aborted：任务中止。
        :type status: str
        :param sub_job_ids: **参数解释：** 子任务ID，该字段一般返回空数组[]。
        :type sub_job_ids: list[str]
        :param sub_job_statuses: **参数解释：** 子任务状态，该字段一般返回空数组[]。
        :type sub_job_statuses: list[str]
        :param target_repo_url: **参数解释：** 目标分支的代码仓地址。 **取值范围：** 长度为[1~1024]个字符。
        :type target_repo_url: str
        :param task_id: **参数解释：** 任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **取值范围：** 长度为[1~32]个字符。
        :type task_id: str
        :param total_execute_time: **参数解释：** 任务总执行时长，格式为%dm%ds，例如\&quot;6m6s\&quot;。 **取值范围：** 不涉及。
        :type total_execute_time: str
        """
        
        

        self._executor = None
        self._finish_time = None
        self._id = None
        self._job_result = None
        self._job_type = None
        self._process = None
        self._review_result = None
        self._rule_sets = None
        self._source = None
        self._source_repo_url = None
        self._start_time = None
        self._status = None
        self._sub_job_ids = None
        self._sub_job_statuses = None
        self._target_repo_url = None
        self._task_id = None
        self._total_execute_time = None
        self.discriminator = None

        if executor is not None:
            self.executor = executor
        if finish_time is not None:
            self.finish_time = finish_time
        if id is not None:
            self.id = id
        if job_result is not None:
            self.job_result = job_result
        if job_type is not None:
            self.job_type = job_type
        if process is not None:
            self.process = process
        if review_result is not None:
            self.review_result = review_result
        if rule_sets is not None:
            self.rule_sets = rule_sets
        if source is not None:
            self.source = source
        if source_repo_url is not None:
            self.source_repo_url = source_repo_url
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if sub_job_ids is not None:
            self.sub_job_ids = sub_job_ids
        if sub_job_statuses is not None:
            self.sub_job_statuses = sub_job_statuses
        if target_repo_url is not None:
            self.target_repo_url = target_repo_url
        if task_id is not None:
            self.task_id = task_id
        if total_execute_time is not None:
            self.total_execute_time = total_execute_time

    @property
    def executor(self):
        r"""Gets the executor of this JobBasicInfoV3.

        **参数解释：** 执行人用户名。 **取值范围：** 长度为[1~255]个字符。

        :return: The executor of this JobBasicInfoV3.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        r"""Sets the executor of this JobBasicInfoV3.

        **参数解释：** 执行人用户名。 **取值范围：** 长度为[1~255]个字符。

        :param executor: The executor of this JobBasicInfoV3.
        :type executor: str
        """
        self._executor = executor

    @property
    def finish_time(self):
        r"""Gets the finish_time of this JobBasicInfoV3.

        **参数解释：** 执行记录的检查完成时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :return: The finish_time of this JobBasicInfoV3.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this JobBasicInfoV3.

        **参数解释：** 执行记录的检查完成时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :param finish_time: The finish_time of this JobBasicInfoV3.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def id(self):
        r"""Gets the id of this JobBasicInfoV3.

        **参数解释：** 执行ID，来自代码检查执行任务接口的返回值，每次执行代码检查任务都有唯一的执行ID。 **取值范围：** 长度为[1~32]个字符。

        :return: The id of this JobBasicInfoV3.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this JobBasicInfoV3.

        **参数解释：** 执行ID，来自代码检查执行任务接口的返回值，每次执行代码检查任务都有唯一的执行ID。 **取值范围：** 长度为[1~32]个字符。

        :param id: The id of this JobBasicInfoV3.
        :type id: str
        """
        self._id = id

    @property
    def job_result(self):
        r"""Gets the job_result of this JobBasicInfoV3.

        :return: The job_result of this JobBasicInfoV3.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.JobResultInfo`
        """
        return self._job_result

    @job_result.setter
    def job_result(self, job_result):
        r"""Sets the job_result of this JobBasicInfoV3.

        :param job_result: The job_result of this JobBasicInfoV3.
        :type job_result: :class:`huaweicloudsdkcodeartscheck.v2.JobResultInfo`
        """
        self._job_result = job_result

    @property
    def job_type(self):
        r"""Gets the job_type of this JobBasicInfoV3.

        **参数解释:** 任务类型。 **取值范围:** - FULL：版本级任务。 - INC_GIT：门禁级任务。 [- INC_COMMIT：流水线指定commitId增量检查、代码检查任务设置-检查范围-版本级检查模式的最近一次提交检查。](tag:hws,hws_hk) [- INC_COMMIT：代码检查任务设置-检查范围-版本级检查模式的最近一次提交检查。](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs) [- INC_LAST_SUCCESS_COMMIT：流水线指定commitId以及最后一次门禁成功的commitId间的增量检查。](tag:hws,hws_hk)

        :return: The job_type of this JobBasicInfoV3.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this JobBasicInfoV3.

        **参数解释:** 任务类型。 **取值范围:** - FULL：版本级任务。 - INC_GIT：门禁级任务。 [- INC_COMMIT：流水线指定commitId增量检查、代码检查任务设置-检查范围-版本级检查模式的最近一次提交检查。](tag:hws,hws_hk) [- INC_COMMIT：代码检查任务设置-检查范围-版本级检查模式的最近一次提交检查。](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs) [- INC_LAST_SUCCESS_COMMIT：流水线指定commitId以及最后一次门禁成功的commitId间的增量检查。](tag:hws,hws_hk)

        :param job_type: The job_type of this JobBasicInfoV3.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def process(self):
        r"""Gets the process of this JobBasicInfoV3.

        :return: The process of this JobBasicInfoV3.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ProcessInfo`
        """
        return self._process

    @process.setter
    def process(self, process):
        r"""Sets the process of this JobBasicInfoV3.

        :param process: The process of this JobBasicInfoV3.
        :type process: :class:`huaweicloudsdkcodeartscheck.v2.ProcessInfo`
        """
        self._process = process

    @property
    def review_result(self):
        r"""Gets the review_result of this JobBasicInfoV3.

        **参数解释：** 门禁结果。 **取值范围：** - success：门禁通过。 - error：门禁未通过。

        :return: The review_result of this JobBasicInfoV3.
        :rtype: str
        """
        return self._review_result

    @review_result.setter
    def review_result(self, review_result):
        r"""Sets the review_result of this JobBasicInfoV3.

        **参数解释：** 门禁结果。 **取值范围：** - success：门禁通过。 - error：门禁未通过。

        :param review_result: The review_result of this JobBasicInfoV3.
        :type review_result: str
        """
        self._review_result = review_result

    @property
    def rule_sets(self):
        r"""Gets the rule_sets of this JobBasicInfoV3.

        **参数解释：** 规则集配置列表。

        :return: The rule_sets of this JobBasicInfoV3.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.ConfigTemplateRuleSetInfo`]
        """
        return self._rule_sets

    @rule_sets.setter
    def rule_sets(self, rule_sets):
        r"""Sets the rule_sets of this JobBasicInfoV3.

        **参数解释：** 规则集配置列表。

        :param rule_sets: The rule_sets of this JobBasicInfoV3.
        :type rule_sets: list[:class:`huaweicloudsdkcodeartscheck.v2.ConfigTemplateRuleSetInfo`]
        """
        self._rule_sets = rule_sets

    @property
    def source(self):
        r"""Gets the source of this JobBasicInfoV3.

        **参数解释：** 执行来源。 **取值范围：** - customer：来自页面点击。 - Scheduled：来自定时任务。 - CodeCheckEdge：来自Edge服务。 - CodeArtsPipeline：来自流水线。 - DevCloudWebhook：来自CodeArtsRepo的Webhook。 - GitCodeActionPipeline：来自流水线的GitCodeAction插件。

        :return: The source of this JobBasicInfoV3.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this JobBasicInfoV3.

        **参数解释：** 执行来源。 **取值范围：** - customer：来自页面点击。 - Scheduled：来自定时任务。 - CodeCheckEdge：来自Edge服务。 - CodeArtsPipeline：来自流水线。 - DevCloudWebhook：来自CodeArtsRepo的Webhook。 - GitCodeActionPipeline：来自流水线的GitCodeAction插件。

        :param source: The source of this JobBasicInfoV3.
        :type source: str
        """
        self._source = source

    @property
    def source_repo_url(self):
        r"""Gets the source_repo_url of this JobBasicInfoV3.

        **参数解释：** 源分支的代码仓地址。 **取值范围：** 长度为[1~1024]个字符。

        :return: The source_repo_url of this JobBasicInfoV3.
        :rtype: str
        """
        return self._source_repo_url

    @source_repo_url.setter
    def source_repo_url(self, source_repo_url):
        r"""Sets the source_repo_url of this JobBasicInfoV3.

        **参数解释：** 源分支的代码仓地址。 **取值范围：** 长度为[1~1024]个字符。

        :param source_repo_url: The source_repo_url of this JobBasicInfoV3.
        :type source_repo_url: str
        """
        self._source_repo_url = source_repo_url

    @property
    def start_time(self):
        r"""Gets the start_time of this JobBasicInfoV3.

        **参数解释：**  执行记录的检查开始时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :return: The start_time of this JobBasicInfoV3.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this JobBasicInfoV3.

        **参数解释：**  执行记录的检查开始时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :param start_time: The start_time of this JobBasicInfoV3.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def status(self):
        r"""Gets the status of this JobBasicInfoV3.

        **参数解释:** 任务执行状态。 **取值范围:** - quering：初始状态。 - running：执行中。 - success：检查成功。 - failed：检查失败。 - aborted：任务中止。

        :return: The status of this JobBasicInfoV3.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobBasicInfoV3.

        **参数解释:** 任务执行状态。 **取值范围:** - quering：初始状态。 - running：执行中。 - success：检查成功。 - failed：检查失败。 - aborted：任务中止。

        :param status: The status of this JobBasicInfoV3.
        :type status: str
        """
        self._status = status

    @property
    def sub_job_ids(self):
        r"""Gets the sub_job_ids of this JobBasicInfoV3.

        **参数解释：** 子任务ID，该字段一般返回空数组[]。

        :return: The sub_job_ids of this JobBasicInfoV3.
        :rtype: list[str]
        """
        return self._sub_job_ids

    @sub_job_ids.setter
    def sub_job_ids(self, sub_job_ids):
        r"""Sets the sub_job_ids of this JobBasicInfoV3.

        **参数解释：** 子任务ID，该字段一般返回空数组[]。

        :param sub_job_ids: The sub_job_ids of this JobBasicInfoV3.
        :type sub_job_ids: list[str]
        """
        self._sub_job_ids = sub_job_ids

    @property
    def sub_job_statuses(self):
        r"""Gets the sub_job_statuses of this JobBasicInfoV3.

        **参数解释：** 子任务状态，该字段一般返回空数组[]。

        :return: The sub_job_statuses of this JobBasicInfoV3.
        :rtype: list[str]
        """
        return self._sub_job_statuses

    @sub_job_statuses.setter
    def sub_job_statuses(self, sub_job_statuses):
        r"""Sets the sub_job_statuses of this JobBasicInfoV3.

        **参数解释：** 子任务状态，该字段一般返回空数组[]。

        :param sub_job_statuses: The sub_job_statuses of this JobBasicInfoV3.
        :type sub_job_statuses: list[str]
        """
        self._sub_job_statuses = sub_job_statuses

    @property
    def target_repo_url(self):
        r"""Gets the target_repo_url of this JobBasicInfoV3.

        **参数解释：** 目标分支的代码仓地址。 **取值范围：** 长度为[1~1024]个字符。

        :return: The target_repo_url of this JobBasicInfoV3.
        :rtype: str
        """
        return self._target_repo_url

    @target_repo_url.setter
    def target_repo_url(self, target_repo_url):
        r"""Sets the target_repo_url of this JobBasicInfoV3.

        **参数解释：** 目标分支的代码仓地址。 **取值范围：** 长度为[1~1024]个字符。

        :param target_repo_url: The target_repo_url of this JobBasicInfoV3.
        :type target_repo_url: str
        """
        self._target_repo_url = target_repo_url

    @property
    def task_id(self):
        r"""Gets the task_id of this JobBasicInfoV3.

        **参数解释：** 任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **取值范围：** 长度为[1~32]个字符。

        :return: The task_id of this JobBasicInfoV3.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this JobBasicInfoV3.

        **参数解释：** 任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **取值范围：** 长度为[1~32]个字符。

        :param task_id: The task_id of this JobBasicInfoV3.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def total_execute_time(self):
        r"""Gets the total_execute_time of this JobBasicInfoV3.

        **参数解释：** 任务总执行时长，格式为%dm%ds，例如\"6m6s\"。 **取值范围：** 不涉及。

        :return: The total_execute_time of this JobBasicInfoV3.
        :rtype: str
        """
        return self._total_execute_time

    @total_execute_time.setter
    def total_execute_time(self, total_execute_time):
        r"""Sets the total_execute_time of this JobBasicInfoV3.

        **参数解释：** 任务总执行时长，格式为%dm%ds，例如\"6m6s\"。 **取值范围：** 不涉及。

        :param total_execute_time: The total_execute_time of this JobBasicInfoV3.
        :type total_execute_time: str
        """
        self._total_execute_time = total_execute_time

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
        if not isinstance(other, JobBasicInfoV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
