# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectsCompareTaskInfo:

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
        'compare_results': 'list[ObjectsCompareOverviewInfo]',
        'start_time': 'str',
        'status': 'str',
        'export_status': 'str',
        'report_remain_seconds': 'int',
        'compare_job_id': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'compare_results': 'compare_results',
        'start_time': 'start_time',
        'status': 'status',
        'export_status': 'export_status',
        'report_remain_seconds': 'report_remain_seconds',
        'compare_job_id': 'compare_job_id',
        'error_msg': 'error_msg'
    }

    def __init__(self, create_time=None, compare_results=None, start_time=None, status=None, export_status=None, report_remain_seconds=None, compare_job_id=None, error_msg=None):
        """ObjectsCompareTaskInfo

        The model defined in huaweicloud sdk

        :param create_time: 对比任务创建时间。
        :type create_time: str
        :param compare_results: 对比结果。
        :type compare_results: list[:class:`huaweicloudsdkdrs.v5.ObjectsCompareOverviewInfo`]
        :param start_time: 对比任务开始时间。
        :type start_time: str
        :param status: 对比任务状态。取值： - RUNNING：运行中。 - WAITING_FOR_RUNNING：等待启动中。 - SUCCESSFUL：完成。 - FAILED：失败。 - CANCELLED：已取消。
        :type status: str
        :param export_status: 导出比对结果状态。
        :type export_status: str
        :param report_remain_seconds: 导出比对结果有效期剩余时间。
        :type report_remain_seconds: int
        :param compare_job_id: 对比任务ID。
        :type compare_job_id: str
        :param error_msg: 失败原因。
        :type error_msg: str
        """
        
        

        self._create_time = None
        self._compare_results = None
        self._start_time = None
        self._status = None
        self._export_status = None
        self._report_remain_seconds = None
        self._compare_job_id = None
        self._error_msg = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if compare_results is not None:
            self.compare_results = compare_results
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

    @property
    def create_time(self):
        """Gets the create_time of this ObjectsCompareTaskInfo.

        对比任务创建时间。

        :return: The create_time of this ObjectsCompareTaskInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ObjectsCompareTaskInfo.

        对比任务创建时间。

        :param create_time: The create_time of this ObjectsCompareTaskInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def compare_results(self):
        """Gets the compare_results of this ObjectsCompareTaskInfo.

        对比结果。

        :return: The compare_results of this ObjectsCompareTaskInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ObjectsCompareOverviewInfo`]
        """
        return self._compare_results

    @compare_results.setter
    def compare_results(self, compare_results):
        """Sets the compare_results of this ObjectsCompareTaskInfo.

        对比结果。

        :param compare_results: The compare_results of this ObjectsCompareTaskInfo.
        :type compare_results: list[:class:`huaweicloudsdkdrs.v5.ObjectsCompareOverviewInfo`]
        """
        self._compare_results = compare_results

    @property
    def start_time(self):
        """Gets the start_time of this ObjectsCompareTaskInfo.

        对比任务开始时间。

        :return: The start_time of this ObjectsCompareTaskInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ObjectsCompareTaskInfo.

        对比任务开始时间。

        :param start_time: The start_time of this ObjectsCompareTaskInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this ObjectsCompareTaskInfo.

        对比任务状态。取值： - RUNNING：运行中。 - WAITING_FOR_RUNNING：等待启动中。 - SUCCESSFUL：完成。 - FAILED：失败。 - CANCELLED：已取消。

        :return: The status of this ObjectsCompareTaskInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ObjectsCompareTaskInfo.

        对比任务状态。取值： - RUNNING：运行中。 - WAITING_FOR_RUNNING：等待启动中。 - SUCCESSFUL：完成。 - FAILED：失败。 - CANCELLED：已取消。

        :param status: The status of this ObjectsCompareTaskInfo.
        :type status: str
        """
        self._status = status

    @property
    def export_status(self):
        """Gets the export_status of this ObjectsCompareTaskInfo.

        导出比对结果状态。

        :return: The export_status of this ObjectsCompareTaskInfo.
        :rtype: str
        """
        return self._export_status

    @export_status.setter
    def export_status(self, export_status):
        """Sets the export_status of this ObjectsCompareTaskInfo.

        导出比对结果状态。

        :param export_status: The export_status of this ObjectsCompareTaskInfo.
        :type export_status: str
        """
        self._export_status = export_status

    @property
    def report_remain_seconds(self):
        """Gets the report_remain_seconds of this ObjectsCompareTaskInfo.

        导出比对结果有效期剩余时间。

        :return: The report_remain_seconds of this ObjectsCompareTaskInfo.
        :rtype: int
        """
        return self._report_remain_seconds

    @report_remain_seconds.setter
    def report_remain_seconds(self, report_remain_seconds):
        """Sets the report_remain_seconds of this ObjectsCompareTaskInfo.

        导出比对结果有效期剩余时间。

        :param report_remain_seconds: The report_remain_seconds of this ObjectsCompareTaskInfo.
        :type report_remain_seconds: int
        """
        self._report_remain_seconds = report_remain_seconds

    @property
    def compare_job_id(self):
        """Gets the compare_job_id of this ObjectsCompareTaskInfo.

        对比任务ID。

        :return: The compare_job_id of this ObjectsCompareTaskInfo.
        :rtype: str
        """
        return self._compare_job_id

    @compare_job_id.setter
    def compare_job_id(self, compare_job_id):
        """Sets the compare_job_id of this ObjectsCompareTaskInfo.

        对比任务ID。

        :param compare_job_id: The compare_job_id of this ObjectsCompareTaskInfo.
        :type compare_job_id: str
        """
        self._compare_job_id = compare_job_id

    @property
    def error_msg(self):
        """Gets the error_msg of this ObjectsCompareTaskInfo.

        失败原因。

        :return: The error_msg of this ObjectsCompareTaskInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ObjectsCompareTaskInfo.

        失败原因。

        :param error_msg: The error_msg of this ObjectsCompareTaskInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, ObjectsCompareTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
