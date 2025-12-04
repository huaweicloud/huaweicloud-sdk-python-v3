# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NativeReportSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_id': 'str',
        'scan_status': 'str',
        'severity': 'str',
        'duration': 'int',
        'summary': 'VulnerabilitySummary',
        'start_time': 'str',
        'end_time': 'str',
        'complete_percent': 'int',
        'scanner': 'Scanner'
    }

    attribute_map = {
        'report_id': 'report_id',
        'scan_status': 'scan_status',
        'severity': 'severity',
        'duration': 'duration',
        'summary': 'summary',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'complete_percent': 'complete_percent',
        'scanner': 'scanner'
    }

    def __init__(self, report_id=None, scan_status=None, severity=None, duration=None, summary=None, start_time=None, end_time=None, complete_percent=None, scanner=None):
        r"""NativeReportSummary

        The model defined in huaweicloud sdk

        :param report_id: 报告ID
        :type report_id: str
        :param scan_status: 制品扫描状态，Pending(扫描等待中)、Running(扫描中)、Error(扫描失败)、Success(扫描成功)
        :type scan_status: str
        :param severity: 制品扫描报告的总体严重程度，None(无评分), Low(低危), Medium(中危), High(高危), Critical(严重), Security(安全)
        :type severity: str
        :param duration: 生成报告所花费的秒数时间
        :type duration: int
        :param summary: 
        :type summary: :class:`huaweicloudsdkswr.v2.VulnerabilitySummary`
        :param start_time: 生成报告的扫描进程的开始时间
        :type start_time: str
        :param end_time: 生成报告的扫描进程的结束时间
        :type end_time: str
        :param complete_percent: 扫描的完成百分比，该值介于0和100之间
        :type complete_percent: int
        :param scanner: 
        :type scanner: :class:`huaweicloudsdkswr.v2.Scanner`
        """
        
        

        self._report_id = None
        self._scan_status = None
        self._severity = None
        self._duration = None
        self._summary = None
        self._start_time = None
        self._end_time = None
        self._complete_percent = None
        self._scanner = None
        self.discriminator = None

        if report_id is not None:
            self.report_id = report_id
        if scan_status is not None:
            self.scan_status = scan_status
        if severity is not None:
            self.severity = severity
        if duration is not None:
            self.duration = duration
        if summary is not None:
            self.summary = summary
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if complete_percent is not None:
            self.complete_percent = complete_percent
        if scanner is not None:
            self.scanner = scanner

    @property
    def report_id(self):
        r"""Gets the report_id of this NativeReportSummary.

        报告ID

        :return: The report_id of this NativeReportSummary.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this NativeReportSummary.

        报告ID

        :param report_id: The report_id of this NativeReportSummary.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def scan_status(self):
        r"""Gets the scan_status of this NativeReportSummary.

        制品扫描状态，Pending(扫描等待中)、Running(扫描中)、Error(扫描失败)、Success(扫描成功)

        :return: The scan_status of this NativeReportSummary.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this NativeReportSummary.

        制品扫描状态，Pending(扫描等待中)、Running(扫描中)、Error(扫描失败)、Success(扫描成功)

        :param scan_status: The scan_status of this NativeReportSummary.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def severity(self):
        r"""Gets the severity of this NativeReportSummary.

        制品扫描报告的总体严重程度，None(无评分), Low(低危), Medium(中危), High(高危), Critical(严重), Security(安全)

        :return: The severity of this NativeReportSummary.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this NativeReportSummary.

        制品扫描报告的总体严重程度，None(无评分), Low(低危), Medium(中危), High(高危), Critical(严重), Security(安全)

        :param severity: The severity of this NativeReportSummary.
        :type severity: str
        """
        self._severity = severity

    @property
    def duration(self):
        r"""Gets the duration of this NativeReportSummary.

        生成报告所花费的秒数时间

        :return: The duration of this NativeReportSummary.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this NativeReportSummary.

        生成报告所花费的秒数时间

        :param duration: The duration of this NativeReportSummary.
        :type duration: int
        """
        self._duration = duration

    @property
    def summary(self):
        r"""Gets the summary of this NativeReportSummary.

        :return: The summary of this NativeReportSummary.
        :rtype: :class:`huaweicloudsdkswr.v2.VulnerabilitySummary`
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        r"""Sets the summary of this NativeReportSummary.

        :param summary: The summary of this NativeReportSummary.
        :type summary: :class:`huaweicloudsdkswr.v2.VulnerabilitySummary`
        """
        self._summary = summary

    @property
    def start_time(self):
        r"""Gets the start_time of this NativeReportSummary.

        生成报告的扫描进程的开始时间

        :return: The start_time of this NativeReportSummary.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this NativeReportSummary.

        生成报告的扫描进程的开始时间

        :param start_time: The start_time of this NativeReportSummary.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this NativeReportSummary.

        生成报告的扫描进程的结束时间

        :return: The end_time of this NativeReportSummary.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this NativeReportSummary.

        生成报告的扫描进程的结束时间

        :param end_time: The end_time of this NativeReportSummary.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def complete_percent(self):
        r"""Gets the complete_percent of this NativeReportSummary.

        扫描的完成百分比，该值介于0和100之间

        :return: The complete_percent of this NativeReportSummary.
        :rtype: int
        """
        return self._complete_percent

    @complete_percent.setter
    def complete_percent(self, complete_percent):
        r"""Sets the complete_percent of this NativeReportSummary.

        扫描的完成百分比，该值介于0和100之间

        :param complete_percent: The complete_percent of this NativeReportSummary.
        :type complete_percent: int
        """
        self._complete_percent = complete_percent

    @property
    def scanner(self):
        r"""Gets the scanner of this NativeReportSummary.

        :return: The scanner of this NativeReportSummary.
        :rtype: :class:`huaweicloudsdkswr.v2.Scanner`
        """
        return self._scanner

    @scanner.setter
    def scanner(self, scanner):
        r"""Sets the scanner of this NativeReportSummary.

        :param scanner: The scanner of this NativeReportSummary.
        :type scanner: :class:`huaweicloudsdkswr.v2.Scanner`
        """
        self._scanner = scanner

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
        if not isinstance(other, NativeReportSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
