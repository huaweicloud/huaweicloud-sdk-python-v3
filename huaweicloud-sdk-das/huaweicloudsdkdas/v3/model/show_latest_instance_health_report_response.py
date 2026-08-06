# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLatestInstanceHealthReportResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'bool',
        'start_at': 'float',
        'end_at': 'float',
        'task_id': 'str',
        'summary_info': 'HealthReportSummaryInfo',
        'instance_info': 'HealthReportInstanceInfo',
        'performance_stat': 'HealthReportPerformanceStat',
        'disk_stat': 'HealthReportDiskStat',
        'table_space_stat': 'HealthReportTableSpaceNewStat',
        'slow_log_stat': 'HealthReportSlowLogStat',
        'full_sql_stat': 'HealthReportFullSqlStat',
        'inspection_stat': 'HealthReportInspectionStat'
    }

    attribute_map = {
        'success': 'success',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'task_id': 'task_id',
        'summary_info': 'summary_info',
        'instance_info': 'instance_info',
        'performance_stat': 'performance_stat',
        'disk_stat': 'disk_stat',
        'table_space_stat': 'table_space_stat',
        'slow_log_stat': 'slow_log_stat',
        'full_sql_stat': 'full_sql_stat',
        'inspection_stat': 'inspection_stat'
    }

    def __init__(self, success=None, start_at=None, end_at=None, task_id=None, summary_info=None, instance_info=None, performance_stat=None, disk_stat=None, table_space_stat=None, slow_log_stat=None, full_sql_stat=None, inspection_stat=None):
        r"""ShowLatestInstanceHealthReportResponse

        The model defined in huaweicloud sdk

        :param success: 日报诊断是否成功
        :type success: bool
        :param start_at: 日报诊断区间的起始时间（Unix timestamp），单位：毫秒
        :type start_at: float
        :param end_at: 日报诊断区间的结束时间（Unix timestamp），单位：毫秒
        :type end_at: float
        :param task_id: 报告ID
        :type task_id: str
        :param summary_info: 
        :type summary_info: :class:`huaweicloudsdkdas.v3.HealthReportSummaryInfo`
        :param instance_info: 
        :type instance_info: :class:`huaweicloudsdkdas.v3.HealthReportInstanceInfo`
        :param performance_stat: 
        :type performance_stat: :class:`huaweicloudsdkdas.v3.HealthReportPerformanceStat`
        :param disk_stat: 
        :type disk_stat: :class:`huaweicloudsdkdas.v3.HealthReportDiskStat`
        :param table_space_stat: 
        :type table_space_stat: :class:`huaweicloudsdkdas.v3.HealthReportTableSpaceNewStat`
        :param slow_log_stat: 
        :type slow_log_stat: :class:`huaweicloudsdkdas.v3.HealthReportSlowLogStat`
        :param full_sql_stat: 
        :type full_sql_stat: :class:`huaweicloudsdkdas.v3.HealthReportFullSqlStat`
        :param inspection_stat: 
        :type inspection_stat: :class:`huaweicloudsdkdas.v3.HealthReportInspectionStat`
        """
        
        super().__init__()

        self._success = None
        self._start_at = None
        self._end_at = None
        self._task_id = None
        self._summary_info = None
        self._instance_info = None
        self._performance_stat = None
        self._disk_stat = None
        self._table_space_stat = None
        self._slow_log_stat = None
        self._full_sql_stat = None
        self._inspection_stat = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if start_at is not None:
            self.start_at = start_at
        if end_at is not None:
            self.end_at = end_at
        if task_id is not None:
            self.task_id = task_id
        if summary_info is not None:
            self.summary_info = summary_info
        if instance_info is not None:
            self.instance_info = instance_info
        if performance_stat is not None:
            self.performance_stat = performance_stat
        if disk_stat is not None:
            self.disk_stat = disk_stat
        if table_space_stat is not None:
            self.table_space_stat = table_space_stat
        if slow_log_stat is not None:
            self.slow_log_stat = slow_log_stat
        if full_sql_stat is not None:
            self.full_sql_stat = full_sql_stat
        if inspection_stat is not None:
            self.inspection_stat = inspection_stat

    @property
    def success(self):
        r"""Gets the success of this ShowLatestInstanceHealthReportResponse.

        日报诊断是否成功

        :return: The success of this ShowLatestInstanceHealthReportResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ShowLatestInstanceHealthReportResponse.

        日报诊断是否成功

        :param success: The success of this ShowLatestInstanceHealthReportResponse.
        :type success: bool
        """
        self._success = success

    @property
    def start_at(self):
        r"""Gets the start_at of this ShowLatestInstanceHealthReportResponse.

        日报诊断区间的起始时间（Unix timestamp），单位：毫秒

        :return: The start_at of this ShowLatestInstanceHealthReportResponse.
        :rtype: float
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ShowLatestInstanceHealthReportResponse.

        日报诊断区间的起始时间（Unix timestamp），单位：毫秒

        :param start_at: The start_at of this ShowLatestInstanceHealthReportResponse.
        :type start_at: float
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ShowLatestInstanceHealthReportResponse.

        日报诊断区间的结束时间（Unix timestamp），单位：毫秒

        :return: The end_at of this ShowLatestInstanceHealthReportResponse.
        :rtype: float
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ShowLatestInstanceHealthReportResponse.

        日报诊断区间的结束时间（Unix timestamp），单位：毫秒

        :param end_at: The end_at of this ShowLatestInstanceHealthReportResponse.
        :type end_at: float
        """
        self._end_at = end_at

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowLatestInstanceHealthReportResponse.

        报告ID

        :return: The task_id of this ShowLatestInstanceHealthReportResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowLatestInstanceHealthReportResponse.

        报告ID

        :param task_id: The task_id of this ShowLatestInstanceHealthReportResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def summary_info(self):
        r"""Gets the summary_info of this ShowLatestInstanceHealthReportResponse.

        :return: The summary_info of this ShowLatestInstanceHealthReportResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.HealthReportSummaryInfo`
        """
        return self._summary_info

    @summary_info.setter
    def summary_info(self, summary_info):
        r"""Sets the summary_info of this ShowLatestInstanceHealthReportResponse.

        :param summary_info: The summary_info of this ShowLatestInstanceHealthReportResponse.
        :type summary_info: :class:`huaweicloudsdkdas.v3.HealthReportSummaryInfo`
        """
        self._summary_info = summary_info

    @property
    def instance_info(self):
        r"""Gets the instance_info of this ShowLatestInstanceHealthReportResponse.

        :return: The instance_info of this ShowLatestInstanceHealthReportResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.HealthReportInstanceInfo`
        """
        return self._instance_info

    @instance_info.setter
    def instance_info(self, instance_info):
        r"""Sets the instance_info of this ShowLatestInstanceHealthReportResponse.

        :param instance_info: The instance_info of this ShowLatestInstanceHealthReportResponse.
        :type instance_info: :class:`huaweicloudsdkdas.v3.HealthReportInstanceInfo`
        """
        self._instance_info = instance_info

    @property
    def performance_stat(self):
        r"""Gets the performance_stat of this ShowLatestInstanceHealthReportResponse.

        :return: The performance_stat of this ShowLatestInstanceHealthReportResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.HealthReportPerformanceStat`
        """
        return self._performance_stat

    @performance_stat.setter
    def performance_stat(self, performance_stat):
        r"""Sets the performance_stat of this ShowLatestInstanceHealthReportResponse.

        :param performance_stat: The performance_stat of this ShowLatestInstanceHealthReportResponse.
        :type performance_stat: :class:`huaweicloudsdkdas.v3.HealthReportPerformanceStat`
        """
        self._performance_stat = performance_stat

    @property
    def disk_stat(self):
        r"""Gets the disk_stat of this ShowLatestInstanceHealthReportResponse.

        :return: The disk_stat of this ShowLatestInstanceHealthReportResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.HealthReportDiskStat`
        """
        return self._disk_stat

    @disk_stat.setter
    def disk_stat(self, disk_stat):
        r"""Sets the disk_stat of this ShowLatestInstanceHealthReportResponse.

        :param disk_stat: The disk_stat of this ShowLatestInstanceHealthReportResponse.
        :type disk_stat: :class:`huaweicloudsdkdas.v3.HealthReportDiskStat`
        """
        self._disk_stat = disk_stat

    @property
    def table_space_stat(self):
        r"""Gets the table_space_stat of this ShowLatestInstanceHealthReportResponse.

        :return: The table_space_stat of this ShowLatestInstanceHealthReportResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.HealthReportTableSpaceNewStat`
        """
        return self._table_space_stat

    @table_space_stat.setter
    def table_space_stat(self, table_space_stat):
        r"""Sets the table_space_stat of this ShowLatestInstanceHealthReportResponse.

        :param table_space_stat: The table_space_stat of this ShowLatestInstanceHealthReportResponse.
        :type table_space_stat: :class:`huaweicloudsdkdas.v3.HealthReportTableSpaceNewStat`
        """
        self._table_space_stat = table_space_stat

    @property
    def slow_log_stat(self):
        r"""Gets the slow_log_stat of this ShowLatestInstanceHealthReportResponse.

        :return: The slow_log_stat of this ShowLatestInstanceHealthReportResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.HealthReportSlowLogStat`
        """
        return self._slow_log_stat

    @slow_log_stat.setter
    def slow_log_stat(self, slow_log_stat):
        r"""Sets the slow_log_stat of this ShowLatestInstanceHealthReportResponse.

        :param slow_log_stat: The slow_log_stat of this ShowLatestInstanceHealthReportResponse.
        :type slow_log_stat: :class:`huaweicloudsdkdas.v3.HealthReportSlowLogStat`
        """
        self._slow_log_stat = slow_log_stat

    @property
    def full_sql_stat(self):
        r"""Gets the full_sql_stat of this ShowLatestInstanceHealthReportResponse.

        :return: The full_sql_stat of this ShowLatestInstanceHealthReportResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.HealthReportFullSqlStat`
        """
        return self._full_sql_stat

    @full_sql_stat.setter
    def full_sql_stat(self, full_sql_stat):
        r"""Sets the full_sql_stat of this ShowLatestInstanceHealthReportResponse.

        :param full_sql_stat: The full_sql_stat of this ShowLatestInstanceHealthReportResponse.
        :type full_sql_stat: :class:`huaweicloudsdkdas.v3.HealthReportFullSqlStat`
        """
        self._full_sql_stat = full_sql_stat

    @property
    def inspection_stat(self):
        r"""Gets the inspection_stat of this ShowLatestInstanceHealthReportResponse.

        :return: The inspection_stat of this ShowLatestInstanceHealthReportResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.HealthReportInspectionStat`
        """
        return self._inspection_stat

    @inspection_stat.setter
    def inspection_stat(self, inspection_stat):
        r"""Sets the inspection_stat of this ShowLatestInstanceHealthReportResponse.

        :param inspection_stat: The inspection_stat of this ShowLatestInstanceHealthReportResponse.
        :type inspection_stat: :class:`huaweicloudsdkdas.v3.HealthReportInspectionStat`
        """
        self._inspection_stat = inspection_stat

    def to_dict(self):
        import warnings
        warnings.warn("ShowLatestInstanceHealthReportResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowLatestInstanceHealthReportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
