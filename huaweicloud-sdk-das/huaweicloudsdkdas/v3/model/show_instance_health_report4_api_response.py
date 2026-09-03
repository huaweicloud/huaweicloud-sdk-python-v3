# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceHealthReport4ApiResponse(SdkResponse):

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
        'start_at': 'int',
        'end_at': 'int',
        'task_id': 'str',
        'summary_info': 'SummaryInfo',
        'instance_info': 'HealthReportInstanceInfo',
        'performance_stat': 'PerformanceStat',
        'disk_stat': 'DiskStat',
        'table_space_stat': 'TableSpaceStat',
        'slow_log_stat': 'SlowLogStat',
        'full_sql_stat': 'FullSqlStat',
        'inspection_stat': 'InspectionStat',
        'error_message': 'str',
        'suffix_uri': 'str'
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
        'inspection_stat': 'inspection_stat',
        'error_message': 'error_message',
        'suffix_uri': 'suffix_uri'
    }

    def __init__(self, success=None, start_at=None, end_at=None, task_id=None, summary_info=None, instance_info=None, performance_stat=None, disk_stat=None, table_space_stat=None, slow_log_stat=None, full_sql_stat=None, inspection_stat=None, error_message=None, suffix_uri=None):
        r"""ShowInstanceHealthReport4ApiResponse

        The model defined in huaweicloud sdk

        :param success: 日报诊断是否成功
        :type success: bool
        :param start_at: 日报诊断区间的起始时间（Unix timestamp），单位：毫秒
        :type start_at: int
        :param end_at: 日报诊断区间的结束时间（Unix timestamp），单位：毫秒
        :type end_at: int
        :param task_id: 报告ID
        :type task_id: str
        :param summary_info: 
        :type summary_info: :class:`huaweicloudsdkdas.v3.SummaryInfo`
        :param instance_info: 
        :type instance_info: :class:`huaweicloudsdkdas.v3.HealthReportInstanceInfo`
        :param performance_stat: 
        :type performance_stat: :class:`huaweicloudsdkdas.v3.PerformanceStat`
        :param disk_stat: 
        :type disk_stat: :class:`huaweicloudsdkdas.v3.DiskStat`
        :param table_space_stat: 
        :type table_space_stat: :class:`huaweicloudsdkdas.v3.TableSpaceStat`
        :param slow_log_stat: 
        :type slow_log_stat: :class:`huaweicloudsdkdas.v3.SlowLogStat`
        :param full_sql_stat: 
        :type full_sql_stat: :class:`huaweicloudsdkdas.v3.FullSqlStat`
        :param inspection_stat: 
        :type inspection_stat: :class:`huaweicloudsdkdas.v3.InspectionStat`
        :param error_message: 错误信息
        :type error_message: str
        :param suffix_uri: 报告链接
        :type suffix_uri: str
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
        self._error_message = None
        self._suffix_uri = None
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
        if error_message is not None:
            self.error_message = error_message
        if suffix_uri is not None:
            self.suffix_uri = suffix_uri

    @property
    def success(self):
        r"""Gets the success of this ShowInstanceHealthReport4ApiResponse.

        日报诊断是否成功

        :return: The success of this ShowInstanceHealthReport4ApiResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ShowInstanceHealthReport4ApiResponse.

        日报诊断是否成功

        :param success: The success of this ShowInstanceHealthReport4ApiResponse.
        :type success: bool
        """
        self._success = success

    @property
    def start_at(self):
        r"""Gets the start_at of this ShowInstanceHealthReport4ApiResponse.

        日报诊断区间的起始时间（Unix timestamp），单位：毫秒

        :return: The start_at of this ShowInstanceHealthReport4ApiResponse.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ShowInstanceHealthReport4ApiResponse.

        日报诊断区间的起始时间（Unix timestamp），单位：毫秒

        :param start_at: The start_at of this ShowInstanceHealthReport4ApiResponse.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ShowInstanceHealthReport4ApiResponse.

        日报诊断区间的结束时间（Unix timestamp），单位：毫秒

        :return: The end_at of this ShowInstanceHealthReport4ApiResponse.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ShowInstanceHealthReport4ApiResponse.

        日报诊断区间的结束时间（Unix timestamp），单位：毫秒

        :param end_at: The end_at of this ShowInstanceHealthReport4ApiResponse.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowInstanceHealthReport4ApiResponse.

        报告ID

        :return: The task_id of this ShowInstanceHealthReport4ApiResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowInstanceHealthReport4ApiResponse.

        报告ID

        :param task_id: The task_id of this ShowInstanceHealthReport4ApiResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def summary_info(self):
        r"""Gets the summary_info of this ShowInstanceHealthReport4ApiResponse.

        :return: The summary_info of this ShowInstanceHealthReport4ApiResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.SummaryInfo`
        """
        return self._summary_info

    @summary_info.setter
    def summary_info(self, summary_info):
        r"""Sets the summary_info of this ShowInstanceHealthReport4ApiResponse.

        :param summary_info: The summary_info of this ShowInstanceHealthReport4ApiResponse.
        :type summary_info: :class:`huaweicloudsdkdas.v3.SummaryInfo`
        """
        self._summary_info = summary_info

    @property
    def instance_info(self):
        r"""Gets the instance_info of this ShowInstanceHealthReport4ApiResponse.

        :return: The instance_info of this ShowInstanceHealthReport4ApiResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.HealthReportInstanceInfo`
        """
        return self._instance_info

    @instance_info.setter
    def instance_info(self, instance_info):
        r"""Sets the instance_info of this ShowInstanceHealthReport4ApiResponse.

        :param instance_info: The instance_info of this ShowInstanceHealthReport4ApiResponse.
        :type instance_info: :class:`huaweicloudsdkdas.v3.HealthReportInstanceInfo`
        """
        self._instance_info = instance_info

    @property
    def performance_stat(self):
        r"""Gets the performance_stat of this ShowInstanceHealthReport4ApiResponse.

        :return: The performance_stat of this ShowInstanceHealthReport4ApiResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.PerformanceStat`
        """
        return self._performance_stat

    @performance_stat.setter
    def performance_stat(self, performance_stat):
        r"""Sets the performance_stat of this ShowInstanceHealthReport4ApiResponse.

        :param performance_stat: The performance_stat of this ShowInstanceHealthReport4ApiResponse.
        :type performance_stat: :class:`huaweicloudsdkdas.v3.PerformanceStat`
        """
        self._performance_stat = performance_stat

    @property
    def disk_stat(self):
        r"""Gets the disk_stat of this ShowInstanceHealthReport4ApiResponse.

        :return: The disk_stat of this ShowInstanceHealthReport4ApiResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.DiskStat`
        """
        return self._disk_stat

    @disk_stat.setter
    def disk_stat(self, disk_stat):
        r"""Sets the disk_stat of this ShowInstanceHealthReport4ApiResponse.

        :param disk_stat: The disk_stat of this ShowInstanceHealthReport4ApiResponse.
        :type disk_stat: :class:`huaweicloudsdkdas.v3.DiskStat`
        """
        self._disk_stat = disk_stat

    @property
    def table_space_stat(self):
        r"""Gets the table_space_stat of this ShowInstanceHealthReport4ApiResponse.

        :return: The table_space_stat of this ShowInstanceHealthReport4ApiResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.TableSpaceStat`
        """
        return self._table_space_stat

    @table_space_stat.setter
    def table_space_stat(self, table_space_stat):
        r"""Sets the table_space_stat of this ShowInstanceHealthReport4ApiResponse.

        :param table_space_stat: The table_space_stat of this ShowInstanceHealthReport4ApiResponse.
        :type table_space_stat: :class:`huaweicloudsdkdas.v3.TableSpaceStat`
        """
        self._table_space_stat = table_space_stat

    @property
    def slow_log_stat(self):
        r"""Gets the slow_log_stat of this ShowInstanceHealthReport4ApiResponse.

        :return: The slow_log_stat of this ShowInstanceHealthReport4ApiResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.SlowLogStat`
        """
        return self._slow_log_stat

    @slow_log_stat.setter
    def slow_log_stat(self, slow_log_stat):
        r"""Sets the slow_log_stat of this ShowInstanceHealthReport4ApiResponse.

        :param slow_log_stat: The slow_log_stat of this ShowInstanceHealthReport4ApiResponse.
        :type slow_log_stat: :class:`huaweicloudsdkdas.v3.SlowLogStat`
        """
        self._slow_log_stat = slow_log_stat

    @property
    def full_sql_stat(self):
        r"""Gets the full_sql_stat of this ShowInstanceHealthReport4ApiResponse.

        :return: The full_sql_stat of this ShowInstanceHealthReport4ApiResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.FullSqlStat`
        """
        return self._full_sql_stat

    @full_sql_stat.setter
    def full_sql_stat(self, full_sql_stat):
        r"""Sets the full_sql_stat of this ShowInstanceHealthReport4ApiResponse.

        :param full_sql_stat: The full_sql_stat of this ShowInstanceHealthReport4ApiResponse.
        :type full_sql_stat: :class:`huaweicloudsdkdas.v3.FullSqlStat`
        """
        self._full_sql_stat = full_sql_stat

    @property
    def inspection_stat(self):
        r"""Gets the inspection_stat of this ShowInstanceHealthReport4ApiResponse.

        :return: The inspection_stat of this ShowInstanceHealthReport4ApiResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.InspectionStat`
        """
        return self._inspection_stat

    @inspection_stat.setter
    def inspection_stat(self, inspection_stat):
        r"""Sets the inspection_stat of this ShowInstanceHealthReport4ApiResponse.

        :param inspection_stat: The inspection_stat of this ShowInstanceHealthReport4ApiResponse.
        :type inspection_stat: :class:`huaweicloudsdkdas.v3.InspectionStat`
        """
        self._inspection_stat = inspection_stat

    @property
    def error_message(self):
        r"""Gets the error_message of this ShowInstanceHealthReport4ApiResponse.

        错误信息

        :return: The error_message of this ShowInstanceHealthReport4ApiResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this ShowInstanceHealthReport4ApiResponse.

        错误信息

        :param error_message: The error_message of this ShowInstanceHealthReport4ApiResponse.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def suffix_uri(self):
        r"""Gets the suffix_uri of this ShowInstanceHealthReport4ApiResponse.

        报告链接

        :return: The suffix_uri of this ShowInstanceHealthReport4ApiResponse.
        :rtype: str
        """
        return self._suffix_uri

    @suffix_uri.setter
    def suffix_uri(self, suffix_uri):
        r"""Sets the suffix_uri of this ShowInstanceHealthReport4ApiResponse.

        报告链接

        :param suffix_uri: The suffix_uri of this ShowInstanceHealthReport4ApiResponse.
        :type suffix_uri: str
        """
        self._suffix_uri = suffix_uri

    def to_dict(self):
        import warnings
        warnings.warn("ShowInstanceHealthReport4ApiResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowInstanceHealthReport4ApiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
