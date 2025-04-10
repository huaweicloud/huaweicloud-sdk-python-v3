# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportFullSqlStat:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'collect_full_sql': 'bool',
        'execute_top_templates': 'list[HealthReportSqlTemplate]',
        'sum_rows_examined_top_templates': 'list[HealthReportSqlTemplate]',
        'avg_cost_top_templates': 'list[HealthReportSqlTemplate]',
        'analyze_success': 'bool',
        'error_message': 'str'
    }

    attribute_map = {
        'collect_full_sql': 'collect_full_sql',
        'execute_top_templates': 'execute_top_templates',
        'sum_rows_examined_top_templates': 'sum_rows_examined_top_templates',
        'avg_cost_top_templates': 'avg_cost_top_templates',
        'analyze_success': 'analyze_success',
        'error_message': 'error_message'
    }

    def __init__(self, collect_full_sql=None, execute_top_templates=None, sum_rows_examined_top_templates=None, avg_cost_top_templates=None, analyze_success=None, error_message=None):
        r"""HealthReportFullSqlStat

        The model defined in huaweicloud sdk

        :param collect_full_sql: 是否收集全量SQL。
        :type collect_full_sql: bool
        :param execute_top_templates: 全量SQL Top总执行次数列表。
        :type execute_top_templates: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        :param sum_rows_examined_top_templates: 全量SQL Top总扫描行数列表。
        :type sum_rows_examined_top_templates: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        :param avg_cost_top_templates: 全量SQL Top平均执行耗时列表。
        :type avg_cost_top_templates: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        :param analyze_success: 统计分析是否成功。
        :type analyze_success: bool
        :param error_message: 错误信息。
        :type error_message: str
        """
        
        

        self._collect_full_sql = None
        self._execute_top_templates = None
        self._sum_rows_examined_top_templates = None
        self._avg_cost_top_templates = None
        self._analyze_success = None
        self._error_message = None
        self.discriminator = None

        self.collect_full_sql = collect_full_sql
        self.execute_top_templates = execute_top_templates
        self.sum_rows_examined_top_templates = sum_rows_examined_top_templates
        self.avg_cost_top_templates = avg_cost_top_templates
        self.analyze_success = analyze_success
        self.error_message = error_message

    @property
    def collect_full_sql(self):
        r"""Gets the collect_full_sql of this HealthReportFullSqlStat.

        是否收集全量SQL。

        :return: The collect_full_sql of this HealthReportFullSqlStat.
        :rtype: bool
        """
        return self._collect_full_sql

    @collect_full_sql.setter
    def collect_full_sql(self, collect_full_sql):
        r"""Sets the collect_full_sql of this HealthReportFullSqlStat.

        是否收集全量SQL。

        :param collect_full_sql: The collect_full_sql of this HealthReportFullSqlStat.
        :type collect_full_sql: bool
        """
        self._collect_full_sql = collect_full_sql

    @property
    def execute_top_templates(self):
        r"""Gets the execute_top_templates of this HealthReportFullSqlStat.

        全量SQL Top总执行次数列表。

        :return: The execute_top_templates of this HealthReportFullSqlStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        """
        return self._execute_top_templates

    @execute_top_templates.setter
    def execute_top_templates(self, execute_top_templates):
        r"""Sets the execute_top_templates of this HealthReportFullSqlStat.

        全量SQL Top总执行次数列表。

        :param execute_top_templates: The execute_top_templates of this HealthReportFullSqlStat.
        :type execute_top_templates: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        """
        self._execute_top_templates = execute_top_templates

    @property
    def sum_rows_examined_top_templates(self):
        r"""Gets the sum_rows_examined_top_templates of this HealthReportFullSqlStat.

        全量SQL Top总扫描行数列表。

        :return: The sum_rows_examined_top_templates of this HealthReportFullSqlStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        """
        return self._sum_rows_examined_top_templates

    @sum_rows_examined_top_templates.setter
    def sum_rows_examined_top_templates(self, sum_rows_examined_top_templates):
        r"""Sets the sum_rows_examined_top_templates of this HealthReportFullSqlStat.

        全量SQL Top总扫描行数列表。

        :param sum_rows_examined_top_templates: The sum_rows_examined_top_templates of this HealthReportFullSqlStat.
        :type sum_rows_examined_top_templates: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        """
        self._sum_rows_examined_top_templates = sum_rows_examined_top_templates

    @property
    def avg_cost_top_templates(self):
        r"""Gets the avg_cost_top_templates of this HealthReportFullSqlStat.

        全量SQL Top平均执行耗时列表。

        :return: The avg_cost_top_templates of this HealthReportFullSqlStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        """
        return self._avg_cost_top_templates

    @avg_cost_top_templates.setter
    def avg_cost_top_templates(self, avg_cost_top_templates):
        r"""Sets the avg_cost_top_templates of this HealthReportFullSqlStat.

        全量SQL Top平均执行耗时列表。

        :param avg_cost_top_templates: The avg_cost_top_templates of this HealthReportFullSqlStat.
        :type avg_cost_top_templates: list[:class:`huaweicloudsdkdas.v3.HealthReportSqlTemplate`]
        """
        self._avg_cost_top_templates = avg_cost_top_templates

    @property
    def analyze_success(self):
        r"""Gets the analyze_success of this HealthReportFullSqlStat.

        统计分析是否成功。

        :return: The analyze_success of this HealthReportFullSqlStat.
        :rtype: bool
        """
        return self._analyze_success

    @analyze_success.setter
    def analyze_success(self, analyze_success):
        r"""Sets the analyze_success of this HealthReportFullSqlStat.

        统计分析是否成功。

        :param analyze_success: The analyze_success of this HealthReportFullSqlStat.
        :type analyze_success: bool
        """
        self._analyze_success = analyze_success

    @property
    def error_message(self):
        r"""Gets the error_message of this HealthReportFullSqlStat.

        错误信息。

        :return: The error_message of this HealthReportFullSqlStat.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this HealthReportFullSqlStat.

        错误信息。

        :param error_message: The error_message of this HealthReportFullSqlStat.
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
        if not isinstance(other, HealthReportFullSqlStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
