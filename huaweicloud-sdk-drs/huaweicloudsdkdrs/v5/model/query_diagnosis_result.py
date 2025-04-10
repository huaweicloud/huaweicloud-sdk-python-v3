# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDiagnosisResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'score': 'int',
        'status': 'str',
        'progress': 'int',
        'error_msg': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'total': 'int',
        'normal_count': 'int',
        'abnormal_count': 'int',
        'alarm_count': 'int',
        'failure_count': 'int',
        'timeout_count': 'int',
        'diagnosis_results': 'list[QueryDiagnosisResultDiagnosisResults]'
    }

    attribute_map = {
        'score': 'score',
        'status': 'status',
        'progress': 'progress',
        'error_msg': 'error_msg',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'total': 'total',
        'normal_count': 'normal_count',
        'abnormal_count': 'abnormal_count',
        'alarm_count': 'alarm_count',
        'failure_count': 'failure_count',
        'timeout_count': 'timeout_count',
        'diagnosis_results': 'diagnosis_results'
    }

    def __init__(self, score=None, status=None, progress=None, error_msg=None, start_time=None, end_time=None, total=None, normal_count=None, abnormal_count=None, alarm_count=None, failure_count=None, timeout_count=None, diagnosis_results=None):
        r"""QueryDiagnosisResult

        The model defined in huaweicloud sdk

        :param score: 得分。
        :type score: int
        :param status: 状态。
        :type status: str
        :param progress: 进度。
        :type progress: int
        :param error_msg: 失败原因。
        :type error_msg: str
        :param start_time: 开始时间。
        :type start_time: str
        :param end_time: 结束时间。
        :type end_time: str
        :param total: 诊断项总数。
        :type total: int
        :param normal_count: 正常数量。
        :type normal_count: int
        :param abnormal_count: 异常数量。
        :type abnormal_count: int
        :param alarm_count: 告警数量。
        :type alarm_count: int
        :param failure_count: 失败数量。
        :type failure_count: int
        :param timeout_count: 超时数量。
        :type timeout_count: int
        :param diagnosis_results: 诊断结果。
        :type diagnosis_results: list[:class:`huaweicloudsdkdrs.v5.QueryDiagnosisResultDiagnosisResults`]
        """
        
        

        self._score = None
        self._status = None
        self._progress = None
        self._error_msg = None
        self._start_time = None
        self._end_time = None
        self._total = None
        self._normal_count = None
        self._abnormal_count = None
        self._alarm_count = None
        self._failure_count = None
        self._timeout_count = None
        self._diagnosis_results = None
        self.discriminator = None

        if score is not None:
            self.score = score
        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if error_msg is not None:
            self.error_msg = error_msg
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if total is not None:
            self.total = total
        if normal_count is not None:
            self.normal_count = normal_count
        if abnormal_count is not None:
            self.abnormal_count = abnormal_count
        if alarm_count is not None:
            self.alarm_count = alarm_count
        if failure_count is not None:
            self.failure_count = failure_count
        if timeout_count is not None:
            self.timeout_count = timeout_count
        if diagnosis_results is not None:
            self.diagnosis_results = diagnosis_results

    @property
    def score(self):
        r"""Gets the score of this QueryDiagnosisResult.

        得分。

        :return: The score of this QueryDiagnosisResult.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this QueryDiagnosisResult.

        得分。

        :param score: The score of this QueryDiagnosisResult.
        :type score: int
        """
        self._score = score

    @property
    def status(self):
        r"""Gets the status of this QueryDiagnosisResult.

        状态。

        :return: The status of this QueryDiagnosisResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this QueryDiagnosisResult.

        状态。

        :param status: The status of this QueryDiagnosisResult.
        :type status: str
        """
        self._status = status

    @property
    def progress(self):
        r"""Gets the progress of this QueryDiagnosisResult.

        进度。

        :return: The progress of this QueryDiagnosisResult.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this QueryDiagnosisResult.

        进度。

        :param progress: The progress of this QueryDiagnosisResult.
        :type progress: int
        """
        self._progress = progress

    @property
    def error_msg(self):
        r"""Gets the error_msg of this QueryDiagnosisResult.

        失败原因。

        :return: The error_msg of this QueryDiagnosisResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this QueryDiagnosisResult.

        失败原因。

        :param error_msg: The error_msg of this QueryDiagnosisResult.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def start_time(self):
        r"""Gets the start_time of this QueryDiagnosisResult.

        开始时间。

        :return: The start_time of this QueryDiagnosisResult.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this QueryDiagnosisResult.

        开始时间。

        :param start_time: The start_time of this QueryDiagnosisResult.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this QueryDiagnosisResult.

        结束时间。

        :return: The end_time of this QueryDiagnosisResult.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this QueryDiagnosisResult.

        结束时间。

        :param end_time: The end_time of this QueryDiagnosisResult.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def total(self):
        r"""Gets the total of this QueryDiagnosisResult.

        诊断项总数。

        :return: The total of this QueryDiagnosisResult.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this QueryDiagnosisResult.

        诊断项总数。

        :param total: The total of this QueryDiagnosisResult.
        :type total: int
        """
        self._total = total

    @property
    def normal_count(self):
        r"""Gets the normal_count of this QueryDiagnosisResult.

        正常数量。

        :return: The normal_count of this QueryDiagnosisResult.
        :rtype: int
        """
        return self._normal_count

    @normal_count.setter
    def normal_count(self, normal_count):
        r"""Sets the normal_count of this QueryDiagnosisResult.

        正常数量。

        :param normal_count: The normal_count of this QueryDiagnosisResult.
        :type normal_count: int
        """
        self._normal_count = normal_count

    @property
    def abnormal_count(self):
        r"""Gets the abnormal_count of this QueryDiagnosisResult.

        异常数量。

        :return: The abnormal_count of this QueryDiagnosisResult.
        :rtype: int
        """
        return self._abnormal_count

    @abnormal_count.setter
    def abnormal_count(self, abnormal_count):
        r"""Sets the abnormal_count of this QueryDiagnosisResult.

        异常数量。

        :param abnormal_count: The abnormal_count of this QueryDiagnosisResult.
        :type abnormal_count: int
        """
        self._abnormal_count = abnormal_count

    @property
    def alarm_count(self):
        r"""Gets the alarm_count of this QueryDiagnosisResult.

        告警数量。

        :return: The alarm_count of this QueryDiagnosisResult.
        :rtype: int
        """
        return self._alarm_count

    @alarm_count.setter
    def alarm_count(self, alarm_count):
        r"""Sets the alarm_count of this QueryDiagnosisResult.

        告警数量。

        :param alarm_count: The alarm_count of this QueryDiagnosisResult.
        :type alarm_count: int
        """
        self._alarm_count = alarm_count

    @property
    def failure_count(self):
        r"""Gets the failure_count of this QueryDiagnosisResult.

        失败数量。

        :return: The failure_count of this QueryDiagnosisResult.
        :rtype: int
        """
        return self._failure_count

    @failure_count.setter
    def failure_count(self, failure_count):
        r"""Sets the failure_count of this QueryDiagnosisResult.

        失败数量。

        :param failure_count: The failure_count of this QueryDiagnosisResult.
        :type failure_count: int
        """
        self._failure_count = failure_count

    @property
    def timeout_count(self):
        r"""Gets the timeout_count of this QueryDiagnosisResult.

        超时数量。

        :return: The timeout_count of this QueryDiagnosisResult.
        :rtype: int
        """
        return self._timeout_count

    @timeout_count.setter
    def timeout_count(self, timeout_count):
        r"""Sets the timeout_count of this QueryDiagnosisResult.

        超时数量。

        :param timeout_count: The timeout_count of this QueryDiagnosisResult.
        :type timeout_count: int
        """
        self._timeout_count = timeout_count

    @property
    def diagnosis_results(self):
        r"""Gets the diagnosis_results of this QueryDiagnosisResult.

        诊断结果。

        :return: The diagnosis_results of this QueryDiagnosisResult.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.QueryDiagnosisResultDiagnosisResults`]
        """
        return self._diagnosis_results

    @diagnosis_results.setter
    def diagnosis_results(self, diagnosis_results):
        r"""Sets the diagnosis_results of this QueryDiagnosisResult.

        诊断结果。

        :param diagnosis_results: The diagnosis_results of this QueryDiagnosisResult.
        :type diagnosis_results: list[:class:`huaweicloudsdkdrs.v5.QueryDiagnosisResultDiagnosisResults`]
        """
        self._diagnosis_results = diagnosis_results

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
        if not isinstance(other, QueryDiagnosisResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
