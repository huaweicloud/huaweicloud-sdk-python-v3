# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportoutlineInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'avg_response_time': 'float',
        'branch_id': 'str',
        'branch_name': 'str',
        'case_retry': 'float',
        'complete_num': 'float',
        'duration': 'float',
        'end_time': 'str',
        'executed_num': 'float',
        'iteration_uri': 'str',
        'kpi_case_count': 'float',
        'kpi_case_execute_count': 'float',
        'kpi_case_pass_count': 'float',
        'max_users': 'float',
        'pass_num': 'float',
        'stage': 'float',
        'stage_name': 'str',
        'start_time': 'str',
        'success_rate': 'float',
        'task_status': 'float',
        'total_num': 'float',
        'tps': 'float',
        'version_uri': 'str',
        'project_id': 'str',
        'service_id': 'str',
        'progress_state': 'str',
        'create_by': 'str',
        'status_value': 'str'
    }

    attribute_map = {
        'avg_response_time': 'avgResponseTime',
        'branch_id': 'branchId',
        'branch_name': 'branchName',
        'case_retry': 'caseRetry',
        'complete_num': 'completeNum',
        'duration': 'duration',
        'end_time': 'endTime',
        'executed_num': 'executedNum',
        'iteration_uri': 'iterationUri',
        'kpi_case_count': 'kpiCaseCount',
        'kpi_case_execute_count': 'kpiCaseExecuteCount',
        'kpi_case_pass_count': 'kpiCasePassCount',
        'max_users': 'maxUsers',
        'pass_num': 'passNum',
        'stage': 'stage',
        'stage_name': 'stageName',
        'start_time': 'startTime',
        'success_rate': 'successRate',
        'task_status': 'taskStatus',
        'total_num': 'totalNum',
        'tps': 'tps',
        'version_uri': 'versionUri',
        'project_id': 'projectId',
        'service_id': 'serviceId',
        'progress_state': 'progressState',
        'create_by': 'createBy',
        'status_value': 'statusValue'
    }

    def __init__(self, avg_response_time=None, branch_id=None, branch_name=None, case_retry=None, complete_num=None, duration=None, end_time=None, executed_num=None, iteration_uri=None, kpi_case_count=None, kpi_case_execute_count=None, kpi_case_pass_count=None, max_users=None, pass_num=None, stage=None, stage_name=None, start_time=None, success_rate=None, task_status=None, total_num=None, tps=None, version_uri=None, project_id=None, service_id=None, progress_state=None, create_by=None, status_value=None):
        r"""ReportoutlineInfo

        The model defined in huaweicloud sdk

        :param avg_response_time: 平均响应时间
        :type avg_response_time: float
        :param branch_id: 分支id
        :type branch_id: str
        :param branch_name: 分支名称
        :type branch_name: str
        :param case_retry: 用例重试次数
        :type case_retry: float
        :param complete_num: 已完成的用例数
        :type complete_num: float
        :param duration: 持续时间
        :type duration: float
        :param end_time: 结束时间
        :type end_time: str
        :param executed_num: 已执行用例数
        :type executed_num: float
        :param iteration_uri: 迭代id
        :type iteration_uri: str
        :param kpi_case_count: kpi用例数
        :type kpi_case_count: float
        :param kpi_case_execute_count: kpi用例执行次数
        :type kpi_case_execute_count: float
        :param kpi_case_pass_count: kpi用例通过次数
        :type kpi_case_pass_count: float
        :param max_users: 最大并发数
        :type max_users: float
        :param pass_num: 结果为pass的用例数
        :type pass_num: float
        :param stage: 阶段id
        :type stage: float
        :param stage_name: 阶段名称
        :type stage_name: str
        :param start_time: 开始时间
        :type start_time: str
        :param success_rate: 成功率
        :type success_rate: float
        :param task_status: 任务状态
        :type task_status: float
        :param total_num: 总用例数
        :type total_num: float
        :param tps: 性能tps指标
        :type tps: float
        :param version_uri: 分支uri
        :type version_uri: str
        :param project_id: 工程id
        :type project_id: str
        :param service_id: 服务id
        :type service_id: str
        :param progress_state: 内部版本字段，已弃用，待删除
        :type progress_state: str
        :param create_by: 报告执行人
        :type create_by: str
        :param status_value: 内部版本字段，已弃用，待删除
        :type status_value: str
        """
        
        

        self._avg_response_time = None
        self._branch_id = None
        self._branch_name = None
        self._case_retry = None
        self._complete_num = None
        self._duration = None
        self._end_time = None
        self._executed_num = None
        self._iteration_uri = None
        self._kpi_case_count = None
        self._kpi_case_execute_count = None
        self._kpi_case_pass_count = None
        self._max_users = None
        self._pass_num = None
        self._stage = None
        self._stage_name = None
        self._start_time = None
        self._success_rate = None
        self._task_status = None
        self._total_num = None
        self._tps = None
        self._version_uri = None
        self._project_id = None
        self._service_id = None
        self._progress_state = None
        self._create_by = None
        self._status_value = None
        self.discriminator = None

        if avg_response_time is not None:
            self.avg_response_time = avg_response_time
        if branch_id is not None:
            self.branch_id = branch_id
        if branch_name is not None:
            self.branch_name = branch_name
        if case_retry is not None:
            self.case_retry = case_retry
        if complete_num is not None:
            self.complete_num = complete_num
        if duration is not None:
            self.duration = duration
        if end_time is not None:
            self.end_time = end_time
        if executed_num is not None:
            self.executed_num = executed_num
        if iteration_uri is not None:
            self.iteration_uri = iteration_uri
        if kpi_case_count is not None:
            self.kpi_case_count = kpi_case_count
        if kpi_case_execute_count is not None:
            self.kpi_case_execute_count = kpi_case_execute_count
        if kpi_case_pass_count is not None:
            self.kpi_case_pass_count = kpi_case_pass_count
        if max_users is not None:
            self.max_users = max_users
        if pass_num is not None:
            self.pass_num = pass_num
        if stage is not None:
            self.stage = stage
        if stage_name is not None:
            self.stage_name = stage_name
        if start_time is not None:
            self.start_time = start_time
        if success_rate is not None:
            self.success_rate = success_rate
        if task_status is not None:
            self.task_status = task_status
        if total_num is not None:
            self.total_num = total_num
        if tps is not None:
            self.tps = tps
        if version_uri is not None:
            self.version_uri = version_uri
        if project_id is not None:
            self.project_id = project_id
        if service_id is not None:
            self.service_id = service_id
        if progress_state is not None:
            self.progress_state = progress_state
        if create_by is not None:
            self.create_by = create_by
        if status_value is not None:
            self.status_value = status_value

    @property
    def avg_response_time(self):
        r"""Gets the avg_response_time of this ReportoutlineInfo.

        平均响应时间

        :return: The avg_response_time of this ReportoutlineInfo.
        :rtype: float
        """
        return self._avg_response_time

    @avg_response_time.setter
    def avg_response_time(self, avg_response_time):
        r"""Sets the avg_response_time of this ReportoutlineInfo.

        平均响应时间

        :param avg_response_time: The avg_response_time of this ReportoutlineInfo.
        :type avg_response_time: float
        """
        self._avg_response_time = avg_response_time

    @property
    def branch_id(self):
        r"""Gets the branch_id of this ReportoutlineInfo.

        分支id

        :return: The branch_id of this ReportoutlineInfo.
        :rtype: str
        """
        return self._branch_id

    @branch_id.setter
    def branch_id(self, branch_id):
        r"""Sets the branch_id of this ReportoutlineInfo.

        分支id

        :param branch_id: The branch_id of this ReportoutlineInfo.
        :type branch_id: str
        """
        self._branch_id = branch_id

    @property
    def branch_name(self):
        r"""Gets the branch_name of this ReportoutlineInfo.

        分支名称

        :return: The branch_name of this ReportoutlineInfo.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        r"""Sets the branch_name of this ReportoutlineInfo.

        分支名称

        :param branch_name: The branch_name of this ReportoutlineInfo.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def case_retry(self):
        r"""Gets the case_retry of this ReportoutlineInfo.

        用例重试次数

        :return: The case_retry of this ReportoutlineInfo.
        :rtype: float
        """
        return self._case_retry

    @case_retry.setter
    def case_retry(self, case_retry):
        r"""Sets the case_retry of this ReportoutlineInfo.

        用例重试次数

        :param case_retry: The case_retry of this ReportoutlineInfo.
        :type case_retry: float
        """
        self._case_retry = case_retry

    @property
    def complete_num(self):
        r"""Gets the complete_num of this ReportoutlineInfo.

        已完成的用例数

        :return: The complete_num of this ReportoutlineInfo.
        :rtype: float
        """
        return self._complete_num

    @complete_num.setter
    def complete_num(self, complete_num):
        r"""Sets the complete_num of this ReportoutlineInfo.

        已完成的用例数

        :param complete_num: The complete_num of this ReportoutlineInfo.
        :type complete_num: float
        """
        self._complete_num = complete_num

    @property
    def duration(self):
        r"""Gets the duration of this ReportoutlineInfo.

        持续时间

        :return: The duration of this ReportoutlineInfo.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ReportoutlineInfo.

        持续时间

        :param duration: The duration of this ReportoutlineInfo.
        :type duration: float
        """
        self._duration = duration

    @property
    def end_time(self):
        r"""Gets the end_time of this ReportoutlineInfo.

        结束时间

        :return: The end_time of this ReportoutlineInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ReportoutlineInfo.

        结束时间

        :param end_time: The end_time of this ReportoutlineInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def executed_num(self):
        r"""Gets the executed_num of this ReportoutlineInfo.

        已执行用例数

        :return: The executed_num of this ReportoutlineInfo.
        :rtype: float
        """
        return self._executed_num

    @executed_num.setter
    def executed_num(self, executed_num):
        r"""Sets the executed_num of this ReportoutlineInfo.

        已执行用例数

        :param executed_num: The executed_num of this ReportoutlineInfo.
        :type executed_num: float
        """
        self._executed_num = executed_num

    @property
    def iteration_uri(self):
        r"""Gets the iteration_uri of this ReportoutlineInfo.

        迭代id

        :return: The iteration_uri of this ReportoutlineInfo.
        :rtype: str
        """
        return self._iteration_uri

    @iteration_uri.setter
    def iteration_uri(self, iteration_uri):
        r"""Sets the iteration_uri of this ReportoutlineInfo.

        迭代id

        :param iteration_uri: The iteration_uri of this ReportoutlineInfo.
        :type iteration_uri: str
        """
        self._iteration_uri = iteration_uri

    @property
    def kpi_case_count(self):
        r"""Gets the kpi_case_count of this ReportoutlineInfo.

        kpi用例数

        :return: The kpi_case_count of this ReportoutlineInfo.
        :rtype: float
        """
        return self._kpi_case_count

    @kpi_case_count.setter
    def kpi_case_count(self, kpi_case_count):
        r"""Sets the kpi_case_count of this ReportoutlineInfo.

        kpi用例数

        :param kpi_case_count: The kpi_case_count of this ReportoutlineInfo.
        :type kpi_case_count: float
        """
        self._kpi_case_count = kpi_case_count

    @property
    def kpi_case_execute_count(self):
        r"""Gets the kpi_case_execute_count of this ReportoutlineInfo.

        kpi用例执行次数

        :return: The kpi_case_execute_count of this ReportoutlineInfo.
        :rtype: float
        """
        return self._kpi_case_execute_count

    @kpi_case_execute_count.setter
    def kpi_case_execute_count(self, kpi_case_execute_count):
        r"""Sets the kpi_case_execute_count of this ReportoutlineInfo.

        kpi用例执行次数

        :param kpi_case_execute_count: The kpi_case_execute_count of this ReportoutlineInfo.
        :type kpi_case_execute_count: float
        """
        self._kpi_case_execute_count = kpi_case_execute_count

    @property
    def kpi_case_pass_count(self):
        r"""Gets the kpi_case_pass_count of this ReportoutlineInfo.

        kpi用例通过次数

        :return: The kpi_case_pass_count of this ReportoutlineInfo.
        :rtype: float
        """
        return self._kpi_case_pass_count

    @kpi_case_pass_count.setter
    def kpi_case_pass_count(self, kpi_case_pass_count):
        r"""Sets the kpi_case_pass_count of this ReportoutlineInfo.

        kpi用例通过次数

        :param kpi_case_pass_count: The kpi_case_pass_count of this ReportoutlineInfo.
        :type kpi_case_pass_count: float
        """
        self._kpi_case_pass_count = kpi_case_pass_count

    @property
    def max_users(self):
        r"""Gets the max_users of this ReportoutlineInfo.

        最大并发数

        :return: The max_users of this ReportoutlineInfo.
        :rtype: float
        """
        return self._max_users

    @max_users.setter
    def max_users(self, max_users):
        r"""Sets the max_users of this ReportoutlineInfo.

        最大并发数

        :param max_users: The max_users of this ReportoutlineInfo.
        :type max_users: float
        """
        self._max_users = max_users

    @property
    def pass_num(self):
        r"""Gets the pass_num of this ReportoutlineInfo.

        结果为pass的用例数

        :return: The pass_num of this ReportoutlineInfo.
        :rtype: float
        """
        return self._pass_num

    @pass_num.setter
    def pass_num(self, pass_num):
        r"""Sets the pass_num of this ReportoutlineInfo.

        结果为pass的用例数

        :param pass_num: The pass_num of this ReportoutlineInfo.
        :type pass_num: float
        """
        self._pass_num = pass_num

    @property
    def stage(self):
        r"""Gets the stage of this ReportoutlineInfo.

        阶段id

        :return: The stage of this ReportoutlineInfo.
        :rtype: float
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        r"""Sets the stage of this ReportoutlineInfo.

        阶段id

        :param stage: The stage of this ReportoutlineInfo.
        :type stage: float
        """
        self._stage = stage

    @property
    def stage_name(self):
        r"""Gets the stage_name of this ReportoutlineInfo.

        阶段名称

        :return: The stage_name of this ReportoutlineInfo.
        :rtype: str
        """
        return self._stage_name

    @stage_name.setter
    def stage_name(self, stage_name):
        r"""Sets the stage_name of this ReportoutlineInfo.

        阶段名称

        :param stage_name: The stage_name of this ReportoutlineInfo.
        :type stage_name: str
        """
        self._stage_name = stage_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ReportoutlineInfo.

        开始时间

        :return: The start_time of this ReportoutlineInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ReportoutlineInfo.

        开始时间

        :param start_time: The start_time of this ReportoutlineInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def success_rate(self):
        r"""Gets the success_rate of this ReportoutlineInfo.

        成功率

        :return: The success_rate of this ReportoutlineInfo.
        :rtype: float
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        r"""Sets the success_rate of this ReportoutlineInfo.

        成功率

        :param success_rate: The success_rate of this ReportoutlineInfo.
        :type success_rate: float
        """
        self._success_rate = success_rate

    @property
    def task_status(self):
        r"""Gets the task_status of this ReportoutlineInfo.

        任务状态

        :return: The task_status of this ReportoutlineInfo.
        :rtype: float
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this ReportoutlineInfo.

        任务状态

        :param task_status: The task_status of this ReportoutlineInfo.
        :type task_status: float
        """
        self._task_status = task_status

    @property
    def total_num(self):
        r"""Gets the total_num of this ReportoutlineInfo.

        总用例数

        :return: The total_num of this ReportoutlineInfo.
        :rtype: float
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ReportoutlineInfo.

        总用例数

        :param total_num: The total_num of this ReportoutlineInfo.
        :type total_num: float
        """
        self._total_num = total_num

    @property
    def tps(self):
        r"""Gets the tps of this ReportoutlineInfo.

        性能tps指标

        :return: The tps of this ReportoutlineInfo.
        :rtype: float
        """
        return self._tps

    @tps.setter
    def tps(self, tps):
        r"""Sets the tps of this ReportoutlineInfo.

        性能tps指标

        :param tps: The tps of this ReportoutlineInfo.
        :type tps: float
        """
        self._tps = tps

    @property
    def version_uri(self):
        r"""Gets the version_uri of this ReportoutlineInfo.

        分支uri

        :return: The version_uri of this ReportoutlineInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this ReportoutlineInfo.

        分支uri

        :param version_uri: The version_uri of this ReportoutlineInfo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def project_id(self):
        r"""Gets the project_id of this ReportoutlineInfo.

        工程id

        :return: The project_id of this ReportoutlineInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ReportoutlineInfo.

        工程id

        :param project_id: The project_id of this ReportoutlineInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def service_id(self):
        r"""Gets the service_id of this ReportoutlineInfo.

        服务id

        :return: The service_id of this ReportoutlineInfo.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this ReportoutlineInfo.

        服务id

        :param service_id: The service_id of this ReportoutlineInfo.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def progress_state(self):
        r"""Gets the progress_state of this ReportoutlineInfo.

        内部版本字段，已弃用，待删除

        :return: The progress_state of this ReportoutlineInfo.
        :rtype: str
        """
        return self._progress_state

    @progress_state.setter
    def progress_state(self, progress_state):
        r"""Sets the progress_state of this ReportoutlineInfo.

        内部版本字段，已弃用，待删除

        :param progress_state: The progress_state of this ReportoutlineInfo.
        :type progress_state: str
        """
        self._progress_state = progress_state

    @property
    def create_by(self):
        r"""Gets the create_by of this ReportoutlineInfo.

        报告执行人

        :return: The create_by of this ReportoutlineInfo.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this ReportoutlineInfo.

        报告执行人

        :param create_by: The create_by of this ReportoutlineInfo.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def status_value(self):
        r"""Gets the status_value of this ReportoutlineInfo.

        内部版本字段，已弃用，待删除

        :return: The status_value of this ReportoutlineInfo.
        :rtype: str
        """
        return self._status_value

    @status_value.setter
    def status_value(self, status_value):
        r"""Sets the status_value of this ReportoutlineInfo.

        内部版本字段，已弃用，待删除

        :param status_value: The status_value of this ReportoutlineInfo.
        :type status_value: str
        """
        self._status_value = status_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReportoutlineInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
