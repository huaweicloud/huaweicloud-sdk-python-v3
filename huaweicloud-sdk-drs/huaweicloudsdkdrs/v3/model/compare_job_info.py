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
        'options': 'dict(str, str)',
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'export_status': 'str',
        'report_remain_seconds': 'int',
        'compare_job_tag': 'dict(str, str)',
        'proportion_value': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'options': 'options',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'export_status': 'export_status',
        'report_remain_seconds': 'report_remain_seconds',
        'compare_job_tag': 'compare_job_tag',
        'proportion_value': 'proportion_value'
    }

    def __init__(self, id=None, type=None, options=None, start_time=None, end_time=None, status=None, export_status=None, report_remain_seconds=None, compare_job_tag=None, proportion_value=None):
        """CompareJobInfo

        The model defined in huaweicloud sdk

        :param id: 对比任务ID。
        :type id: str
        :param type: 对比类型。 - lines：行数对比 - contents：内容对比 - random：抽样对比，当前仅支持gaussdbv5、gaussdbv5-to-postgresql、gaussdbv5ha-to-postgresql链路。
        :type type: str
        :param options: 对比配置项，key-value形式。 内容对比支持以下配置项： - 对比方式配置，key：contentCompareType，value：dynamic表示动态对比，static表示静态对比。 - lob字段对比类型配置，key：lobCompare，value：ignore表示忽略，length表示长度对比。  行数对比支持以下配置项： - 对比策略配置，多表归一情况下适用，key：comparePolicy，value：normal表示正常对比，manyToOne表示多对一对比。
        :type options: dict(str, str)
        :param start_time: 开始时间，UTC时间，例如：2020-09-01T18:50:20Z。
        :type start_time: str
        :param end_time: 结束时间，UTC时间，例如：2020-09-01T18:50:20Z。
        :type end_time: str
        :param status: 对比任务的状态。 - RUNNING-运行中 - WAITING_FOR_RUNNING-等待启动中 - SUCCESSFUL-完成 - FAILED-失败 - CANCELLED-已取消 - TIMEOUT_INTERRUPT-超时中断 - FULL_DOING-全量校验中 - INCRE_DOING-增量校验中
        :type status: str
        :param export_status: 导出对比结果状态。 - INIT：初始状态 - EXPORTING：对比结果导出中 - EXPORT_COMPLETE：对比结果导出完成 - EXPORT_COMMON_FAILED：对比结果导出失败
        :type export_status: str
        :param report_remain_seconds: 导出比对结果有效期剩余时间。
        :type report_remain_seconds: int
        :param compare_job_tag: 对比任务的标签，当前仅涉及对比策略时返回。
        :type compare_job_tag: dict(str, str)
        :param proportion_value: 抽样比例，对比类型为抽样对比时填写。
        :type proportion_value: str
        """
        
        

        self._id = None
        self._type = None
        self._options = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._export_status = None
        self._report_remain_seconds = None
        self._compare_job_tag = None
        self._proportion_value = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if options is not None:
            self.options = options
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if export_status is not None:
            self.export_status = export_status
        if report_remain_seconds is not None:
            self.report_remain_seconds = report_remain_seconds
        if compare_job_tag is not None:
            self.compare_job_tag = compare_job_tag
        if proportion_value is not None:
            self.proportion_value = proportion_value

    @property
    def id(self):
        """Gets the id of this CompareJobInfo.

        对比任务ID。

        :return: The id of this CompareJobInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompareJobInfo.

        对比任务ID。

        :param id: The id of this CompareJobInfo.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this CompareJobInfo.

        对比类型。 - lines：行数对比 - contents：内容对比 - random：抽样对比，当前仅支持gaussdbv5、gaussdbv5-to-postgresql、gaussdbv5ha-to-postgresql链路。

        :return: The type of this CompareJobInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CompareJobInfo.

        对比类型。 - lines：行数对比 - contents：内容对比 - random：抽样对比，当前仅支持gaussdbv5、gaussdbv5-to-postgresql、gaussdbv5ha-to-postgresql链路。

        :param type: The type of this CompareJobInfo.
        :type type: str
        """
        self._type = type

    @property
    def options(self):
        """Gets the options of this CompareJobInfo.

        对比配置项，key-value形式。 内容对比支持以下配置项： - 对比方式配置，key：contentCompareType，value：dynamic表示动态对比，static表示静态对比。 - lob字段对比类型配置，key：lobCompare，value：ignore表示忽略，length表示长度对比。  行数对比支持以下配置项： - 对比策略配置，多表归一情况下适用，key：comparePolicy，value：normal表示正常对比，manyToOne表示多对一对比。

        :return: The options of this CompareJobInfo.
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this CompareJobInfo.

        对比配置项，key-value形式。 内容对比支持以下配置项： - 对比方式配置，key：contentCompareType，value：dynamic表示动态对比，static表示静态对比。 - lob字段对比类型配置，key：lobCompare，value：ignore表示忽略，length表示长度对比。  行数对比支持以下配置项： - 对比策略配置，多表归一情况下适用，key：comparePolicy，value：normal表示正常对比，manyToOne表示多对一对比。

        :param options: The options of this CompareJobInfo.
        :type options: dict(str, str)
        """
        self._options = options

    @property
    def start_time(self):
        """Gets the start_time of this CompareJobInfo.

        开始时间，UTC时间，例如：2020-09-01T18:50:20Z。

        :return: The start_time of this CompareJobInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CompareJobInfo.

        开始时间，UTC时间，例如：2020-09-01T18:50:20Z。

        :param start_time: The start_time of this CompareJobInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this CompareJobInfo.

        结束时间，UTC时间，例如：2020-09-01T18:50:20Z。

        :return: The end_time of this CompareJobInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CompareJobInfo.

        结束时间，UTC时间，例如：2020-09-01T18:50:20Z。

        :param end_time: The end_time of this CompareJobInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this CompareJobInfo.

        对比任务的状态。 - RUNNING-运行中 - WAITING_FOR_RUNNING-等待启动中 - SUCCESSFUL-完成 - FAILED-失败 - CANCELLED-已取消 - TIMEOUT_INTERRUPT-超时中断 - FULL_DOING-全量校验中 - INCRE_DOING-增量校验中

        :return: The status of this CompareJobInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CompareJobInfo.

        对比任务的状态。 - RUNNING-运行中 - WAITING_FOR_RUNNING-等待启动中 - SUCCESSFUL-完成 - FAILED-失败 - CANCELLED-已取消 - TIMEOUT_INTERRUPT-超时中断 - FULL_DOING-全量校验中 - INCRE_DOING-增量校验中

        :param status: The status of this CompareJobInfo.
        :type status: str
        """
        self._status = status

    @property
    def export_status(self):
        """Gets the export_status of this CompareJobInfo.

        导出对比结果状态。 - INIT：初始状态 - EXPORTING：对比结果导出中 - EXPORT_COMPLETE：对比结果导出完成 - EXPORT_COMMON_FAILED：对比结果导出失败

        :return: The export_status of this CompareJobInfo.
        :rtype: str
        """
        return self._export_status

    @export_status.setter
    def export_status(self, export_status):
        """Sets the export_status of this CompareJobInfo.

        导出对比结果状态。 - INIT：初始状态 - EXPORTING：对比结果导出中 - EXPORT_COMPLETE：对比结果导出完成 - EXPORT_COMMON_FAILED：对比结果导出失败

        :param export_status: The export_status of this CompareJobInfo.
        :type export_status: str
        """
        self._export_status = export_status

    @property
    def report_remain_seconds(self):
        """Gets the report_remain_seconds of this CompareJobInfo.

        导出比对结果有效期剩余时间。

        :return: The report_remain_seconds of this CompareJobInfo.
        :rtype: int
        """
        return self._report_remain_seconds

    @report_remain_seconds.setter
    def report_remain_seconds(self, report_remain_seconds):
        """Sets the report_remain_seconds of this CompareJobInfo.

        导出比对结果有效期剩余时间。

        :param report_remain_seconds: The report_remain_seconds of this CompareJobInfo.
        :type report_remain_seconds: int
        """
        self._report_remain_seconds = report_remain_seconds

    @property
    def compare_job_tag(self):
        """Gets the compare_job_tag of this CompareJobInfo.

        对比任务的标签，当前仅涉及对比策略时返回。

        :return: The compare_job_tag of this CompareJobInfo.
        :rtype: dict(str, str)
        """
        return self._compare_job_tag

    @compare_job_tag.setter
    def compare_job_tag(self, compare_job_tag):
        """Sets the compare_job_tag of this CompareJobInfo.

        对比任务的标签，当前仅涉及对比策略时返回。

        :param compare_job_tag: The compare_job_tag of this CompareJobInfo.
        :type compare_job_tag: dict(str, str)
        """
        self._compare_job_tag = compare_job_tag

    @property
    def proportion_value(self):
        """Gets the proportion_value of this CompareJobInfo.

        抽样比例，对比类型为抽样对比时填写。

        :return: The proportion_value of this CompareJobInfo.
        :rtype: str
        """
        return self._proportion_value

    @proportion_value.setter
    def proportion_value(self, proportion_value):
        """Sets the proportion_value of this CompareJobInfo.

        抽样比例，对比类型为抽样对比时填写。

        :param proportion_value: The proportion_value of this CompareJobInfo.
        :type proportion_value: str
        """
        self._proportion_value = proportion_value

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
