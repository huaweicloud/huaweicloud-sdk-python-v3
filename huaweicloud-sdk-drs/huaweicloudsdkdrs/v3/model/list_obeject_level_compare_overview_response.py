# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListObejectLevelCompareOverviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'start_time': 'str',
        'status': 'str',
        'export_status': 'str',
        'report_remain_seconds': 'int',
        'compare_job_id': 'str',
        'error_msg': 'str',
        'compare_result': 'list[ObjectsCompareOverviewInfo]'
    }

    attribute_map = {
        'create_time': 'create_time',
        'start_time': 'start_time',
        'status': 'status',
        'export_status': 'export_status',
        'report_remain_seconds': 'report_remain_seconds',
        'compare_job_id': 'compare_job_id',
        'error_msg': 'error_msg',
        'compare_result': 'compare_result'
    }

    def __init__(self, create_time=None, start_time=None, status=None, export_status=None, report_remain_seconds=None, compare_job_id=None, error_msg=None, compare_result=None):
        r"""ListObejectLevelCompareOverviewResponse

        The model defined in huaweicloud sdk

        :param create_time: 对比任务创建时间，UTC时间，例如：2024-04-09T07:00:57Z。
        :type create_time: str
        :param start_time: 对比任务开始时间，UTC时间，例如：2024-04-09T07:00:57Z。
        :type start_time: str
        :param status: 对比任务状态。 取值： - RUNNING：运行中。 - WAITING_FOR_RUNNING：等待启动中。 - SUCCESSFUL：完成。 - FAILED：失败。 - CANCELLED：已取消。 - TIMEOUT_INTERRUPT：超时中断。 - FULL_DOING：全量校验中。 - INCRE_DOING：增量校验中。
        :type status: str
        :param export_status: 生成对比结果报告文件的状态：  - INIT：初始状态。  - EXPORTING：对比结果导出中。  - EXPORT_COMPLETE：对比结果导出完成。  - EXPORT_COMMON_FAILED：对比结果导出失败。
        :type export_status: str
        :param report_remain_seconds: 对比结果报告文件有效期剩余时间，单位秒，报告未生成时返回-1。
        :type report_remain_seconds: int
        :param compare_job_id: 对比任务ID。
        :type compare_job_id: str
        :param error_msg: 失败原因。
        :type error_msg: str
        :param compare_result: 对比结果。
        :type compare_result: list[:class:`huaweicloudsdkdrs.v3.ObjectsCompareOverviewInfo`]
        """
        
        super(ListObejectLevelCompareOverviewResponse, self).__init__()

        self._create_time = None
        self._start_time = None
        self._status = None
        self._export_status = None
        self._report_remain_seconds = None
        self._compare_job_id = None
        self._error_msg = None
        self._compare_result = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if export_status is not None:
            self.export_status = export_status
        if report_remain_seconds is not None:
            self.report_remain_seconds = report_remain_seconds
        if compare_job_id is not None:
            self.compare_job_id = compare_job_id
        if error_msg is not None:
            self.error_msg = error_msg
        if compare_result is not None:
            self.compare_result = compare_result

    @property
    def create_time(self):
        r"""Gets the create_time of this ListObejectLevelCompareOverviewResponse.

        对比任务创建时间，UTC时间，例如：2024-04-09T07:00:57Z。

        :return: The create_time of this ListObejectLevelCompareOverviewResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListObejectLevelCompareOverviewResponse.

        对比任务创建时间，UTC时间，例如：2024-04-09T07:00:57Z。

        :param create_time: The create_time of this ListObejectLevelCompareOverviewResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ListObejectLevelCompareOverviewResponse.

        对比任务开始时间，UTC时间，例如：2024-04-09T07:00:57Z。

        :return: The start_time of this ListObejectLevelCompareOverviewResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListObejectLevelCompareOverviewResponse.

        对比任务开始时间，UTC时间，例如：2024-04-09T07:00:57Z。

        :param start_time: The start_time of this ListObejectLevelCompareOverviewResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def status(self):
        r"""Gets the status of this ListObejectLevelCompareOverviewResponse.

        对比任务状态。 取值： - RUNNING：运行中。 - WAITING_FOR_RUNNING：等待启动中。 - SUCCESSFUL：完成。 - FAILED：失败。 - CANCELLED：已取消。 - TIMEOUT_INTERRUPT：超时中断。 - FULL_DOING：全量校验中。 - INCRE_DOING：增量校验中。

        :return: The status of this ListObejectLevelCompareOverviewResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListObejectLevelCompareOverviewResponse.

        对比任务状态。 取值： - RUNNING：运行中。 - WAITING_FOR_RUNNING：等待启动中。 - SUCCESSFUL：完成。 - FAILED：失败。 - CANCELLED：已取消。 - TIMEOUT_INTERRUPT：超时中断。 - FULL_DOING：全量校验中。 - INCRE_DOING：增量校验中。

        :param status: The status of this ListObejectLevelCompareOverviewResponse.
        :type status: str
        """
        self._status = status

    @property
    def export_status(self):
        r"""Gets the export_status of this ListObejectLevelCompareOverviewResponse.

        生成对比结果报告文件的状态：  - INIT：初始状态。  - EXPORTING：对比结果导出中。  - EXPORT_COMPLETE：对比结果导出完成。  - EXPORT_COMMON_FAILED：对比结果导出失败。

        :return: The export_status of this ListObejectLevelCompareOverviewResponse.
        :rtype: str
        """
        return self._export_status

    @export_status.setter
    def export_status(self, export_status):
        r"""Sets the export_status of this ListObejectLevelCompareOverviewResponse.

        生成对比结果报告文件的状态：  - INIT：初始状态。  - EXPORTING：对比结果导出中。  - EXPORT_COMPLETE：对比结果导出完成。  - EXPORT_COMMON_FAILED：对比结果导出失败。

        :param export_status: The export_status of this ListObejectLevelCompareOverviewResponse.
        :type export_status: str
        """
        self._export_status = export_status

    @property
    def report_remain_seconds(self):
        r"""Gets the report_remain_seconds of this ListObejectLevelCompareOverviewResponse.

        对比结果报告文件有效期剩余时间，单位秒，报告未生成时返回-1。

        :return: The report_remain_seconds of this ListObejectLevelCompareOverviewResponse.
        :rtype: int
        """
        return self._report_remain_seconds

    @report_remain_seconds.setter
    def report_remain_seconds(self, report_remain_seconds):
        r"""Sets the report_remain_seconds of this ListObejectLevelCompareOverviewResponse.

        对比结果报告文件有效期剩余时间，单位秒，报告未生成时返回-1。

        :param report_remain_seconds: The report_remain_seconds of this ListObejectLevelCompareOverviewResponse.
        :type report_remain_seconds: int
        """
        self._report_remain_seconds = report_remain_seconds

    @property
    def compare_job_id(self):
        r"""Gets the compare_job_id of this ListObejectLevelCompareOverviewResponse.

        对比任务ID。

        :return: The compare_job_id of this ListObejectLevelCompareOverviewResponse.
        :rtype: str
        """
        return self._compare_job_id

    @compare_job_id.setter
    def compare_job_id(self, compare_job_id):
        r"""Sets the compare_job_id of this ListObejectLevelCompareOverviewResponse.

        对比任务ID。

        :param compare_job_id: The compare_job_id of this ListObejectLevelCompareOverviewResponse.
        :type compare_job_id: str
        """
        self._compare_job_id = compare_job_id

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ListObejectLevelCompareOverviewResponse.

        失败原因。

        :return: The error_msg of this ListObejectLevelCompareOverviewResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ListObejectLevelCompareOverviewResponse.

        失败原因。

        :param error_msg: The error_msg of this ListObejectLevelCompareOverviewResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def compare_result(self):
        r"""Gets the compare_result of this ListObejectLevelCompareOverviewResponse.

        对比结果。

        :return: The compare_result of this ListObejectLevelCompareOverviewResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.ObjectsCompareOverviewInfo`]
        """
        return self._compare_result

    @compare_result.setter
    def compare_result(self, compare_result):
        r"""Sets the compare_result of this ListObejectLevelCompareOverviewResponse.

        对比结果。

        :param compare_result: The compare_result of this ListObejectLevelCompareOverviewResponse.
        :type compare_result: list[:class:`huaweicloudsdkdrs.v3.ObjectsCompareOverviewInfo`]
        """
        self._compare_result = compare_result

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
        if not isinstance(other, ListObejectLevelCompareOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
