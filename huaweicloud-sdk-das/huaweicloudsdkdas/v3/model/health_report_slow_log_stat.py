# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportSlowLogStat:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'collect_slow_log': 'bool',
        'top_execute_slow_logs': 'list[HealthReportSqlTemplate]',
        'top_avg_query_time_slow_logs': 'list[HealthReportSqlTemplate]',
        'top_max_query_time_slow_logs': 'list[HealthReportSqlTemplate]',
        'rows_examined_exceeding': 'list[HealthReportSqlTemplate]',
        'analyze_success': 'bool',
        'error_message': 'str'
    }

    attribute_map = {
        'collect_slow_log': 'collect_slow_log',
        'top_execute_slow_logs': 'top_execute_slow_logs',
        'top_avg_query_time_slow_logs': 'top_avg_query_time_slow_logs',
        'top_max_query_time_slow_logs': 'top_max_query_time_slow_logs',
        'rows_examined_exceeding': 'rows_examined_exceeding',
        'analyze_success': 'analyze_success',
        'error_message': 'error_message'
    }

    def __init__(self, collect_slow_log=None, top_execute_slow_logs=None, top_avg_query_time_slow_logs=None, top_max_query_time_slow_logs=None, rows_examined_exceeding=None, analyze_success=None, error_message=None):
        r"""HealthReportSlowLogStat

        The model defined in huaweicloud sdk

        :param collect_slow_log: 是否收集慢SQL。
        :type collect_slow_log: bool
        :param top_execute_slow_logs: 慢SQL Top执行次数列表。
        :type top_execute_slow_logs: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        :param top_avg_query_time_slow_logs: 慢SQL Top平均执行时间列表。
        :type top_avg_query_time_slow_logs: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        :param top_max_query_time_slow_logs: 慢SQL Top最大执行时间列表。
        :type top_max_query_time_slow_logs: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        :param rows_examined_exceeding: 慢SQL Top扫描返回比列表。
        :type rows_examined_exceeding: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        :param analyze_success: 统计分析是否成功。
        :type analyze_success: bool
        :param error_message: 错误信息。
        :type error_message: str
        """
        
        

        self._collect_slow_log = None
        self._top_execute_slow_logs = None
        self._top_avg_query_time_slow_logs = None
        self._top_max_query_time_slow_logs = None
        self._rows_examined_exceeding = None
        self._analyze_success = None
        self._error_message = None
        self.discriminator = None

        self.collect_slow_log = collect_slow_log
        self.top_execute_slow_logs = top_execute_slow_logs
        self.top_avg_query_time_slow_logs = top_avg_query_time_slow_logs
        self.top_max_query_time_slow_logs = top_max_query_time_slow_logs
        self.rows_examined_exceeding = rows_examined_exceeding
        self.analyze_success = analyze_success
        self.error_message = error_message

    @property
    def collect_slow_log(self):
        r"""Gets the collect_slow_log of this HealthReportSlowLogStat.

        是否收集慢SQL。

        :return: The collect_slow_log of this HealthReportSlowLogStat.
        :rtype: bool
        """
        return self._collect_slow_log

    @collect_slow_log.setter
    def collect_slow_log(self, collect_slow_log):
        r"""Sets the collect_slow_log of this HealthReportSlowLogStat.

        是否收集慢SQL。

        :param collect_slow_log: The collect_slow_log of this HealthReportSlowLogStat.
        :type collect_slow_log: bool
        """
        self._collect_slow_log = collect_slow_log

    @property
    def top_execute_slow_logs(self):
        r"""Gets the top_execute_slow_logs of this HealthReportSlowLogStat.

        慢SQL Top执行次数列表。

        :return: The top_execute_slow_logs of this HealthReportSlowLogStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        """
        return self._top_execute_slow_logs

    @top_execute_slow_logs.setter
    def top_execute_slow_logs(self, top_execute_slow_logs):
        r"""Sets the top_execute_slow_logs of this HealthReportSlowLogStat.

        慢SQL Top执行次数列表。

        :param top_execute_slow_logs: The top_execute_slow_logs of this HealthReportSlowLogStat.
        :type top_execute_slow_logs: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        """
        self._top_execute_slow_logs = top_execute_slow_logs

    @property
    def top_avg_query_time_slow_logs(self):
        r"""Gets the top_avg_query_time_slow_logs of this HealthReportSlowLogStat.

        慢SQL Top平均执行时间列表。

        :return: The top_avg_query_time_slow_logs of this HealthReportSlowLogStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        """
        return self._top_avg_query_time_slow_logs

    @top_avg_query_time_slow_logs.setter
    def top_avg_query_time_slow_logs(self, top_avg_query_time_slow_logs):
        r"""Sets the top_avg_query_time_slow_logs of this HealthReportSlowLogStat.

        慢SQL Top平均执行时间列表。

        :param top_avg_query_time_slow_logs: The top_avg_query_time_slow_logs of this HealthReportSlowLogStat.
        :type top_avg_query_time_slow_logs: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        """
        self._top_avg_query_time_slow_logs = top_avg_query_time_slow_logs

    @property
    def top_max_query_time_slow_logs(self):
        r"""Gets the top_max_query_time_slow_logs of this HealthReportSlowLogStat.

        慢SQL Top最大执行时间列表。

        :return: The top_max_query_time_slow_logs of this HealthReportSlowLogStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        """
        return self._top_max_query_time_slow_logs

    @top_max_query_time_slow_logs.setter
    def top_max_query_time_slow_logs(self, top_max_query_time_slow_logs):
        r"""Sets the top_max_query_time_slow_logs of this HealthReportSlowLogStat.

        慢SQL Top最大执行时间列表。

        :param top_max_query_time_slow_logs: The top_max_query_time_slow_logs of this HealthReportSlowLogStat.
        :type top_max_query_time_slow_logs: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        """
        self._top_max_query_time_slow_logs = top_max_query_time_slow_logs

    @property
    def rows_examined_exceeding(self):
        r"""Gets the rows_examined_exceeding of this HealthReportSlowLogStat.

        慢SQL Top扫描返回比列表。

        :return: The rows_examined_exceeding of this HealthReportSlowLogStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        """
        return self._rows_examined_exceeding

    @rows_examined_exceeding.setter
    def rows_examined_exceeding(self, rows_examined_exceeding):
        r"""Sets the rows_examined_exceeding of this HealthReportSlowLogStat.

        慢SQL Top扫描返回比列表。

        :param rows_examined_exceeding: The rows_examined_exceeding of this HealthReportSlowLogStat.
        :type rows_examined_exceeding: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        """
        self._rows_examined_exceeding = rows_examined_exceeding

    @property
    def analyze_success(self):
        r"""Gets the analyze_success of this HealthReportSlowLogStat.

        统计分析是否成功。

        :return: The analyze_success of this HealthReportSlowLogStat.
        :rtype: bool
        """
        return self._analyze_success

    @analyze_success.setter
    def analyze_success(self, analyze_success):
        r"""Sets the analyze_success of this HealthReportSlowLogStat.

        统计分析是否成功。

        :param analyze_success: The analyze_success of this HealthReportSlowLogStat.
        :type analyze_success: bool
        """
        self._analyze_success = analyze_success

    @property
    def error_message(self):
        r"""Gets the error_message of this HealthReportSlowLogStat.

        错误信息。

        :return: The error_message of this HealthReportSlowLogStat.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this HealthReportSlowLogStat.

        错误信息。

        :param error_message: The error_message of this HealthReportSlowLogStat.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, HealthReportSlowLogStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
