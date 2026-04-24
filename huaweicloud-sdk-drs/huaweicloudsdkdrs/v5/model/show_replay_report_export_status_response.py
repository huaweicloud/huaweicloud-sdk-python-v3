# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReplayReportExportStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'export_status': 'str',
        'job_id': 'str',
        'file_type': 'str',
        'failed_reason': 'str',
        'total_count': 'int',
        'current_count': 'int',
        'progress_percentage': 'int',
        'uploaded_file_names': 'list[str]'
    }

    attribute_map = {
        'export_status': 'export_status',
        'job_id': 'job_id',
        'file_type': 'file_type',
        'failed_reason': 'failed_reason',
        'total_count': 'total_count',
        'current_count': 'current_count',
        'progress_percentage': 'progress_percentage',
        'uploaded_file_names': 'uploaded_file_names'
    }

    def __init__(self, export_status=None, job_id=None, file_type=None, failed_reason=None, total_count=None, current_count=None, progress_percentage=None, uploaded_file_names=None):
        r"""ShowReplayReportExportStatusResponse

        The model defined in huaweicloud sdk

        :param export_status: 导出状态。取值范围： - EXPORTING ：导出中 - EXPORT_COMPLETE ：导出完成 - EXPORT_COMMON_FAILED ：导出失败
        :type export_status: str
        :param job_id: 任务id
        :type job_id: str
        :param file_type: 导出的sql文件类型。取值范围： - abnormal_sql ：异常sql列表 - error_sql_detail ：异常sql详情 - slow_sql ：慢sql列表 - slow_sql_detail ： 慢sql详情
        :type file_type: str
        :param failed_reason: 失败原因
        :type failed_reason: str
        :param total_count: 导出的数据总量
        :type total_count: int
        :param current_count: 当前已经处理数据量
        :type current_count: int
        :param progress_percentage: 任务进度百分数
        :type progress_percentage: int
        :param uploaded_file_names: 已经上传到obs的文件名称
        :type uploaded_file_names: list[str]
        """
        
        super().__init__()

        self._export_status = None
        self._job_id = None
        self._file_type = None
        self._failed_reason = None
        self._total_count = None
        self._current_count = None
        self._progress_percentage = None
        self._uploaded_file_names = None
        self.discriminator = None

        if export_status is not None:
            self.export_status = export_status
        if job_id is not None:
            self.job_id = job_id
        if file_type is not None:
            self.file_type = file_type
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if total_count is not None:
            self.total_count = total_count
        if current_count is not None:
            self.current_count = current_count
        if progress_percentage is not None:
            self.progress_percentage = progress_percentage
        if uploaded_file_names is not None:
            self.uploaded_file_names = uploaded_file_names

    @property
    def export_status(self):
        r"""Gets the export_status of this ShowReplayReportExportStatusResponse.

        导出状态。取值范围： - EXPORTING ：导出中 - EXPORT_COMPLETE ：导出完成 - EXPORT_COMMON_FAILED ：导出失败

        :return: The export_status of this ShowReplayReportExportStatusResponse.
        :rtype: str
        """
        return self._export_status

    @export_status.setter
    def export_status(self, export_status):
        r"""Sets the export_status of this ShowReplayReportExportStatusResponse.

        导出状态。取值范围： - EXPORTING ：导出中 - EXPORT_COMPLETE ：导出完成 - EXPORT_COMMON_FAILED ：导出失败

        :param export_status: The export_status of this ShowReplayReportExportStatusResponse.
        :type export_status: str
        """
        self._export_status = export_status

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowReplayReportExportStatusResponse.

        任务id

        :return: The job_id of this ShowReplayReportExportStatusResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowReplayReportExportStatusResponse.

        任务id

        :param job_id: The job_id of this ShowReplayReportExportStatusResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def file_type(self):
        r"""Gets the file_type of this ShowReplayReportExportStatusResponse.

        导出的sql文件类型。取值范围： - abnormal_sql ：异常sql列表 - error_sql_detail ：异常sql详情 - slow_sql ：慢sql列表 - slow_sql_detail ： 慢sql详情

        :return: The file_type of this ShowReplayReportExportStatusResponse.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this ShowReplayReportExportStatusResponse.

        导出的sql文件类型。取值范围： - abnormal_sql ：异常sql列表 - error_sql_detail ：异常sql详情 - slow_sql ：慢sql列表 - slow_sql_detail ： 慢sql详情

        :param file_type: The file_type of this ShowReplayReportExportStatusResponse.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this ShowReplayReportExportStatusResponse.

        失败原因

        :return: The failed_reason of this ShowReplayReportExportStatusResponse.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this ShowReplayReportExportStatusResponse.

        失败原因

        :param failed_reason: The failed_reason of this ShowReplayReportExportStatusResponse.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowReplayReportExportStatusResponse.

        导出的数据总量

        :return: The total_count of this ShowReplayReportExportStatusResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowReplayReportExportStatusResponse.

        导出的数据总量

        :param total_count: The total_count of this ShowReplayReportExportStatusResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def current_count(self):
        r"""Gets the current_count of this ShowReplayReportExportStatusResponse.

        当前已经处理数据量

        :return: The current_count of this ShowReplayReportExportStatusResponse.
        :rtype: int
        """
        return self._current_count

    @current_count.setter
    def current_count(self, current_count):
        r"""Sets the current_count of this ShowReplayReportExportStatusResponse.

        当前已经处理数据量

        :param current_count: The current_count of this ShowReplayReportExportStatusResponse.
        :type current_count: int
        """
        self._current_count = current_count

    @property
    def progress_percentage(self):
        r"""Gets the progress_percentage of this ShowReplayReportExportStatusResponse.

        任务进度百分数

        :return: The progress_percentage of this ShowReplayReportExportStatusResponse.
        :rtype: int
        """
        return self._progress_percentage

    @progress_percentage.setter
    def progress_percentage(self, progress_percentage):
        r"""Sets the progress_percentage of this ShowReplayReportExportStatusResponse.

        任务进度百分数

        :param progress_percentage: The progress_percentage of this ShowReplayReportExportStatusResponse.
        :type progress_percentage: int
        """
        self._progress_percentage = progress_percentage

    @property
    def uploaded_file_names(self):
        r"""Gets the uploaded_file_names of this ShowReplayReportExportStatusResponse.

        已经上传到obs的文件名称

        :return: The uploaded_file_names of this ShowReplayReportExportStatusResponse.
        :rtype: list[str]
        """
        return self._uploaded_file_names

    @uploaded_file_names.setter
    def uploaded_file_names(self, uploaded_file_names):
        r"""Sets the uploaded_file_names of this ShowReplayReportExportStatusResponse.

        已经上传到obs的文件名称

        :param uploaded_file_names: The uploaded_file_names of this ShowReplayReportExportStatusResponse.
        :type uploaded_file_names: list[str]
        """
        self._uploaded_file_names = uploaded_file_names

    def to_dict(self):
        import warnings
        warnings.warn("ShowReplayReportExportStatusResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowReplayReportExportStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
