# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareJobInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'type': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'compute_type': 'str',
        'export_status': 'str',
        'report_remain_seconds': 'int',
        'compare_job_tag': 'dict(str, str)',
        'options': 'dict(str, str)',
        'error_msg': 'str',
        'dynamic_compare_delay': 'int'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'compute_type': 'compute_type',
        'export_status': 'export_status',
        'report_remain_seconds': 'report_remain_seconds',
        'compare_job_tag': 'compare_job_tag',
        'options': 'options',
        'error_msg': 'error_msg',
        'dynamic_compare_delay': 'dynamic_compare_delay'
    }

    def __init__(self, id=None, type=None, start_time=None, end_time=None, status=None, compute_type=None, export_status=None, report_remain_seconds=None, compare_job_tag=None, options=None, error_msg=None, dynamic_compare_delay=None):
        r"""CompareJobInfo

        The model defined in huaweicloud sdk

        :param id: 对比任务ID。
        :type id: str
        :param type: 对比类型。
        :type type: str
        :param start_time: 开始时间。
        :type start_time: str
        :param end_time: 结束时间。
        :type end_time: str
        :param status: 对比任务的状态。取值： - RUNNING：运行中。 - WAITING_FOR_RUNNING：等待启动中。 - SUCCESSFUL：完成。 - FAILED：失败。 - CANCELLED：已取消。 - TIMEOUT_INTERRUPT：超时中断。 - FULL_DOING：全量校验中。 - INCRE_DOING：增量校验中。
        :type status: str
        :param compute_type: 对比计算资源。
        :type compute_type: str
        :param export_status: 导出比对结果状态。
        :type export_status: str
        :param report_remain_seconds: 导出比对结果有效期剩余时间。
        :type report_remain_seconds: int
        :param compare_job_tag: 对比任务的标签。
        :type compare_job_tag: dict(str, str)
        :param options: 对比任务选项。
        :type options: dict(str, str)
        :param error_msg: 失败原因。
        :type error_msg: str
        :param dynamic_compare_delay: 动态比对时延。
        :type dynamic_compare_delay: int
        """
        
        

        self._id = None
        self._type = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._compute_type = None
        self._export_status = None
        self._report_remain_seconds = None
        self._compare_job_tag = None
        self._options = None
        self._error_msg = None
        self._dynamic_compare_delay = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if compute_type is not None:
            self.compute_type = compute_type
        if export_status is not None:
            self.export_status = export_status
        if report_remain_seconds is not None:
            self.report_remain_seconds = report_remain_seconds
        if compare_job_tag is not None:
            self.compare_job_tag = compare_job_tag
        if options is not None:
            self.options = options
        if error_msg is not None:
            self.error_msg = error_msg
        if dynamic_compare_delay is not None:
            self.dynamic_compare_delay = dynamic_compare_delay

    @property
    def id(self):
        r"""Gets the id of this CompareJobInfo.

        对比任务ID。

        :return: The id of this CompareJobInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CompareJobInfo.

        对比任务ID。

        :param id: The id of this CompareJobInfo.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this CompareJobInfo.

        对比类型。

        :return: The type of this CompareJobInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CompareJobInfo.

        对比类型。

        :param type: The type of this CompareJobInfo.
        :type type: str
        """
        self._type = type

    @property
    def start_time(self):
        r"""Gets the start_time of this CompareJobInfo.

        开始时间。

        :return: The start_time of this CompareJobInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CompareJobInfo.

        开始时间。

        :param start_time: The start_time of this CompareJobInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this CompareJobInfo.

        结束时间。

        :return: The end_time of this CompareJobInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this CompareJobInfo.

        结束时间。

        :param end_time: The end_time of this CompareJobInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this CompareJobInfo.

        对比任务的状态。取值： - RUNNING：运行中。 - WAITING_FOR_RUNNING：等待启动中。 - SUCCESSFUL：完成。 - FAILED：失败。 - CANCELLED：已取消。 - TIMEOUT_INTERRUPT：超时中断。 - FULL_DOING：全量校验中。 - INCRE_DOING：增量校验中。

        :return: The status of this CompareJobInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CompareJobInfo.

        对比任务的状态。取值： - RUNNING：运行中。 - WAITING_FOR_RUNNING：等待启动中。 - SUCCESSFUL：完成。 - FAILED：失败。 - CANCELLED：已取消。 - TIMEOUT_INTERRUPT：超时中断。 - FULL_DOING：全量校验中。 - INCRE_DOING：增量校验中。

        :param status: The status of this CompareJobInfo.
        :type status: str
        """
        self._status = status

    @property
    def compute_type(self):
        r"""Gets the compute_type of this CompareJobInfo.

        对比计算资源。

        :return: The compute_type of this CompareJobInfo.
        :rtype: str
        """
        return self._compute_type

    @compute_type.setter
    def compute_type(self, compute_type):
        r"""Sets the compute_type of this CompareJobInfo.

        对比计算资源。

        :param compute_type: The compute_type of this CompareJobInfo.
        :type compute_type: str
        """
        self._compute_type = compute_type

    @property
    def export_status(self):
        r"""Gets the export_status of this CompareJobInfo.

        导出比对结果状态。

        :return: The export_status of this CompareJobInfo.
        :rtype: str
        """
        return self._export_status

    @export_status.setter
    def export_status(self, export_status):
        r"""Sets the export_status of this CompareJobInfo.

        导出比对结果状态。

        :param export_status: The export_status of this CompareJobInfo.
        :type export_status: str
        """
        self._export_status = export_status

    @property
    def report_remain_seconds(self):
        r"""Gets the report_remain_seconds of this CompareJobInfo.

        导出比对结果有效期剩余时间。

        :return: The report_remain_seconds of this CompareJobInfo.
        :rtype: int
        """
        return self._report_remain_seconds

    @report_remain_seconds.setter
    def report_remain_seconds(self, report_remain_seconds):
        r"""Sets the report_remain_seconds of this CompareJobInfo.

        导出比对结果有效期剩余时间。

        :param report_remain_seconds: The report_remain_seconds of this CompareJobInfo.
        :type report_remain_seconds: int
        """
        self._report_remain_seconds = report_remain_seconds

    @property
    def compare_job_tag(self):
        r"""Gets the compare_job_tag of this CompareJobInfo.

        对比任务的标签。

        :return: The compare_job_tag of this CompareJobInfo.
        :rtype: dict(str, str)
        """
        return self._compare_job_tag

    @compare_job_tag.setter
    def compare_job_tag(self, compare_job_tag):
        r"""Sets the compare_job_tag of this CompareJobInfo.

        对比任务的标签。

        :param compare_job_tag: The compare_job_tag of this CompareJobInfo.
        :type compare_job_tag: dict(str, str)
        """
        self._compare_job_tag = compare_job_tag

    @property
    def options(self):
        r"""Gets the options of this CompareJobInfo.

        对比任务选项。

        :return: The options of this CompareJobInfo.
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this CompareJobInfo.

        对比任务选项。

        :param options: The options of this CompareJobInfo.
        :type options: dict(str, str)
        """
        self._options = options

    @property
    def error_msg(self):
        r"""Gets the error_msg of this CompareJobInfo.

        失败原因。

        :return: The error_msg of this CompareJobInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this CompareJobInfo.

        失败原因。

        :param error_msg: The error_msg of this CompareJobInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def dynamic_compare_delay(self):
        r"""Gets the dynamic_compare_delay of this CompareJobInfo.

        动态比对时延。

        :return: The dynamic_compare_delay of this CompareJobInfo.
        :rtype: int
        """
        return self._dynamic_compare_delay

    @dynamic_compare_delay.setter
    def dynamic_compare_delay(self, dynamic_compare_delay):
        r"""Sets the dynamic_compare_delay of this CompareJobInfo.

        动态比对时延。

        :param dynamic_compare_delay: The dynamic_compare_delay of this CompareJobInfo.
        :type dynamic_compare_delay: int
        """
        self._dynamic_compare_delay = dynamic_compare_delay

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
        if not isinstance(other, CompareJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
