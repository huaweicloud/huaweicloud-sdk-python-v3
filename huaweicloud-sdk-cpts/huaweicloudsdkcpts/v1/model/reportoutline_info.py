# coding: utf-8

import re
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
        'case_retry': 'int',
        'complete_num': 'int',
        'duration': 'int',
        'end_time': 'str',
        'executed_num': 'int',
        'iteration_uri': 'str',
        'kpi_case_count': 'int',
        'kpi_case_execute_count': 'int',
        'kpi_case_pass_count': 'int',
        'max_users': 'int',
        'pass_num': 'int',
        'progress_state': 'str',
        'stage': 'int',
        'stage_name': 'str',
        'start_time': 'str',
        'status_value': 'str',
        'success_rate': 'int',
        'task_status': 'int',
        'total_num': 'int',
        'tps': 'float',
        'version_uri': 'str'
    }

    attribute_map = {
        'avg_response_time': 'avgResponseTime',
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
        'progress_state': 'progressState',
        'stage': 'stage',
        'stage_name': 'stageName',
        'start_time': 'startTime',
        'status_value': 'statusValue',
        'success_rate': 'successRate',
        'task_status': 'taskStatus',
        'total_num': 'totalNum',
        'tps': 'tps',
        'version_uri': 'versionUri'
    }

    def __init__(self, avg_response_time=None, case_retry=None, complete_num=None, duration=None, end_time=None, executed_num=None, iteration_uri=None, kpi_case_count=None, kpi_case_execute_count=None, kpi_case_pass_count=None, max_users=None, pass_num=None, progress_state=None, stage=None, stage_name=None, start_time=None, status_value=None, success_rate=None, task_status=None, total_num=None, tps=None, version_uri=None):
        """ReportoutlineInfo - a model defined in huaweicloud sdk"""
        
        

        self._avg_response_time = None
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
        self._progress_state = None
        self._stage = None
        self._stage_name = None
        self._start_time = None
        self._status_value = None
        self._success_rate = None
        self._task_status = None
        self._total_num = None
        self._tps = None
        self._version_uri = None
        self.discriminator = None

        if avg_response_time is not None:
            self.avg_response_time = avg_response_time
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
        if progress_state is not None:
            self.progress_state = progress_state
        if stage is not None:
            self.stage = stage
        if stage_name is not None:
            self.stage_name = stage_name
        if start_time is not None:
            self.start_time = start_time
        if status_value is not None:
            self.status_value = status_value
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

    @property
    def avg_response_time(self):
        """Gets the avg_response_time of this ReportoutlineInfo.

        avgResponseTime

        :return: The avg_response_time of this ReportoutlineInfo.
        :rtype: float
        """
        return self._avg_response_time

    @avg_response_time.setter
    def avg_response_time(self, avg_response_time):
        """Sets the avg_response_time of this ReportoutlineInfo.

        avgResponseTime

        :param avg_response_time: The avg_response_time of this ReportoutlineInfo.
        :type: float
        """
        self._avg_response_time = avg_response_time

    @property
    def case_retry(self):
        """Gets the case_retry of this ReportoutlineInfo.

        caseRetry

        :return: The case_retry of this ReportoutlineInfo.
        :rtype: int
        """
        return self._case_retry

    @case_retry.setter
    def case_retry(self, case_retry):
        """Sets the case_retry of this ReportoutlineInfo.

        caseRetry

        :param case_retry: The case_retry of this ReportoutlineInfo.
        :type: int
        """
        self._case_retry = case_retry

    @property
    def complete_num(self):
        """Gets the complete_num of this ReportoutlineInfo.

        completeNum

        :return: The complete_num of this ReportoutlineInfo.
        :rtype: int
        """
        return self._complete_num

    @complete_num.setter
    def complete_num(self, complete_num):
        """Sets the complete_num of this ReportoutlineInfo.

        completeNum

        :param complete_num: The complete_num of this ReportoutlineInfo.
        :type: int
        """
        self._complete_num = complete_num

    @property
    def duration(self):
        """Gets the duration of this ReportoutlineInfo.

        duration

        :return: The duration of this ReportoutlineInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ReportoutlineInfo.

        duration

        :param duration: The duration of this ReportoutlineInfo.
        :type: int
        """
        self._duration = duration

    @property
    def end_time(self):
        """Gets the end_time of this ReportoutlineInfo.

        endTime

        :return: The end_time of this ReportoutlineInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ReportoutlineInfo.

        endTime

        :param end_time: The end_time of this ReportoutlineInfo.
        :type: str
        """
        self._end_time = end_time

    @property
    def executed_num(self):
        """Gets the executed_num of this ReportoutlineInfo.

        executedNum

        :return: The executed_num of this ReportoutlineInfo.
        :rtype: int
        """
        return self._executed_num

    @executed_num.setter
    def executed_num(self, executed_num):
        """Sets the executed_num of this ReportoutlineInfo.

        executedNum

        :param executed_num: The executed_num of this ReportoutlineInfo.
        :type: int
        """
        self._executed_num = executed_num

    @property
    def iteration_uri(self):
        """Gets the iteration_uri of this ReportoutlineInfo.

        iterationUri

        :return: The iteration_uri of this ReportoutlineInfo.
        :rtype: str
        """
        return self._iteration_uri

    @iteration_uri.setter
    def iteration_uri(self, iteration_uri):
        """Sets the iteration_uri of this ReportoutlineInfo.

        iterationUri

        :param iteration_uri: The iteration_uri of this ReportoutlineInfo.
        :type: str
        """
        self._iteration_uri = iteration_uri

    @property
    def kpi_case_count(self):
        """Gets the kpi_case_count of this ReportoutlineInfo.

        kpiCaseCount

        :return: The kpi_case_count of this ReportoutlineInfo.
        :rtype: int
        """
        return self._kpi_case_count

    @kpi_case_count.setter
    def kpi_case_count(self, kpi_case_count):
        """Sets the kpi_case_count of this ReportoutlineInfo.

        kpiCaseCount

        :param kpi_case_count: The kpi_case_count of this ReportoutlineInfo.
        :type: int
        """
        self._kpi_case_count = kpi_case_count

    @property
    def kpi_case_execute_count(self):
        """Gets the kpi_case_execute_count of this ReportoutlineInfo.

        kpiCaseExecuteCount

        :return: The kpi_case_execute_count of this ReportoutlineInfo.
        :rtype: int
        """
        return self._kpi_case_execute_count

    @kpi_case_execute_count.setter
    def kpi_case_execute_count(self, kpi_case_execute_count):
        """Sets the kpi_case_execute_count of this ReportoutlineInfo.

        kpiCaseExecuteCount

        :param kpi_case_execute_count: The kpi_case_execute_count of this ReportoutlineInfo.
        :type: int
        """
        self._kpi_case_execute_count = kpi_case_execute_count

    @property
    def kpi_case_pass_count(self):
        """Gets the kpi_case_pass_count of this ReportoutlineInfo.

        kpiCasePassCount

        :return: The kpi_case_pass_count of this ReportoutlineInfo.
        :rtype: int
        """
        return self._kpi_case_pass_count

    @kpi_case_pass_count.setter
    def kpi_case_pass_count(self, kpi_case_pass_count):
        """Sets the kpi_case_pass_count of this ReportoutlineInfo.

        kpiCasePassCount

        :param kpi_case_pass_count: The kpi_case_pass_count of this ReportoutlineInfo.
        :type: int
        """
        self._kpi_case_pass_count = kpi_case_pass_count

    @property
    def max_users(self):
        """Gets the max_users of this ReportoutlineInfo.

        maxUsers

        :return: The max_users of this ReportoutlineInfo.
        :rtype: int
        """
        return self._max_users

    @max_users.setter
    def max_users(self, max_users):
        """Sets the max_users of this ReportoutlineInfo.

        maxUsers

        :param max_users: The max_users of this ReportoutlineInfo.
        :type: int
        """
        self._max_users = max_users

    @property
    def pass_num(self):
        """Gets the pass_num of this ReportoutlineInfo.

        passNum

        :return: The pass_num of this ReportoutlineInfo.
        :rtype: int
        """
        return self._pass_num

    @pass_num.setter
    def pass_num(self, pass_num):
        """Sets the pass_num of this ReportoutlineInfo.

        passNum

        :param pass_num: The pass_num of this ReportoutlineInfo.
        :type: int
        """
        self._pass_num = pass_num

    @property
    def progress_state(self):
        """Gets the progress_state of this ReportoutlineInfo.

        progressState

        :return: The progress_state of this ReportoutlineInfo.
        :rtype: str
        """
        return self._progress_state

    @progress_state.setter
    def progress_state(self, progress_state):
        """Sets the progress_state of this ReportoutlineInfo.

        progressState

        :param progress_state: The progress_state of this ReportoutlineInfo.
        :type: str
        """
        self._progress_state = progress_state

    @property
    def stage(self):
        """Gets the stage of this ReportoutlineInfo.

        stage

        :return: The stage of this ReportoutlineInfo.
        :rtype: int
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this ReportoutlineInfo.

        stage

        :param stage: The stage of this ReportoutlineInfo.
        :type: int
        """
        self._stage = stage

    @property
    def stage_name(self):
        """Gets the stage_name of this ReportoutlineInfo.

        stageName

        :return: The stage_name of this ReportoutlineInfo.
        :rtype: str
        """
        return self._stage_name

    @stage_name.setter
    def stage_name(self, stage_name):
        """Sets the stage_name of this ReportoutlineInfo.

        stageName

        :param stage_name: The stage_name of this ReportoutlineInfo.
        :type: str
        """
        self._stage_name = stage_name

    @property
    def start_time(self):
        """Gets the start_time of this ReportoutlineInfo.

        startTime

        :return: The start_time of this ReportoutlineInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ReportoutlineInfo.

        startTime

        :param start_time: The start_time of this ReportoutlineInfo.
        :type: str
        """
        self._start_time = start_time

    @property
    def status_value(self):
        """Gets the status_value of this ReportoutlineInfo.

        statusValue

        :return: The status_value of this ReportoutlineInfo.
        :rtype: str
        """
        return self._status_value

    @status_value.setter
    def status_value(self, status_value):
        """Sets the status_value of this ReportoutlineInfo.

        statusValue

        :param status_value: The status_value of this ReportoutlineInfo.
        :type: str
        """
        self._status_value = status_value

    @property
    def success_rate(self):
        """Gets the success_rate of this ReportoutlineInfo.

        successRate

        :return: The success_rate of this ReportoutlineInfo.
        :rtype: int
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this ReportoutlineInfo.

        successRate

        :param success_rate: The success_rate of this ReportoutlineInfo.
        :type: int
        """
        self._success_rate = success_rate

    @property
    def task_status(self):
        """Gets the task_status of this ReportoutlineInfo.

        taskStatus

        :return: The task_status of this ReportoutlineInfo.
        :rtype: int
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this ReportoutlineInfo.

        taskStatus

        :param task_status: The task_status of this ReportoutlineInfo.
        :type: int
        """
        self._task_status = task_status

    @property
    def total_num(self):
        """Gets the total_num of this ReportoutlineInfo.

        totalNum

        :return: The total_num of this ReportoutlineInfo.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this ReportoutlineInfo.

        totalNum

        :param total_num: The total_num of this ReportoutlineInfo.
        :type: int
        """
        self._total_num = total_num

    @property
    def tps(self):
        """Gets the tps of this ReportoutlineInfo.

        tps

        :return: The tps of this ReportoutlineInfo.
        :rtype: float
        """
        return self._tps

    @tps.setter
    def tps(self, tps):
        """Sets the tps of this ReportoutlineInfo.

        tps

        :param tps: The tps of this ReportoutlineInfo.
        :type: float
        """
        self._tps = tps

    @property
    def version_uri(self):
        """Gets the version_uri of this ReportoutlineInfo.

        versionUri

        :return: The version_uri of this ReportoutlineInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        """Sets the version_uri of this ReportoutlineInfo.

        versionUri

        :param version_uri: The version_uri of this ReportoutlineInfo.
        :type: str
        """
        self._version_uri = version_uri

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
