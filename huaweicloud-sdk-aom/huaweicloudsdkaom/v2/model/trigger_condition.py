# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TriggerCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_query_mode': 'str',
        'metric_namespace': 'str',
        'metric_name': 'str',
        'metric_unit': 'str',
        'metric_labels': 'list[str]',
        'promql': 'str',
        'promql_expr': 'list[str]',
        'trigger_times': 'str',
        'trigger_interval': 'str',
        'trigger_type': 'str',
        'promql_for': 'str',
        'aggregation_type': 'str',
        'operator': 'str',
        'thresholds': 'dict(str, str)',
        'aggregation_window': 'str',
        'cmdb': 'CmdbInfo',
        'query_match': 'str',
        'query_param': 'str',
        'aom_monitor_level': 'str',
        'aggregate_type': 'str',
        'metric_statistic_method': 'str',
        'expression': 'str',
        'mix_promql': 'str'
    }

    attribute_map = {
        'metric_query_mode': 'metric_query_mode',
        'metric_namespace': 'metric_namespace',
        'metric_name': 'metric_name',
        'metric_unit': 'metric_unit',
        'metric_labels': 'metric_labels',
        'promql': 'promql',
        'promql_expr': 'promql_expr',
        'trigger_times': 'trigger_times',
        'trigger_interval': 'trigger_interval',
        'trigger_type': 'trigger_type',
        'promql_for': 'promql_for',
        'aggregation_type': 'aggregation_type',
        'operator': 'operator',
        'thresholds': 'thresholds',
        'aggregation_window': 'aggregation_window',
        'cmdb': 'cmdb',
        'query_match': 'query_match',
        'query_param': 'query_param',
        'aom_monitor_level': 'aom_monitor_level',
        'aggregate_type': 'aggregate_type',
        'metric_statistic_method': 'metric_statistic_method',
        'expression': 'expression',
        'mix_promql': 'mix_promql'
    }

    def __init__(self, metric_query_mode=None, metric_namespace=None, metric_name=None, metric_unit=None, metric_labels=None, promql=None, promql_expr=None, trigger_times=None, trigger_interval=None, trigger_type=None, promql_for=None, aggregation_type=None, operator=None, thresholds=None, aggregation_window=None, cmdb=None, query_match=None, query_param=None, aom_monitor_level=None, aggregate_type=None, metric_statistic_method=None, expression=None, mix_promql=None):
        """TriggerCondition

        The model defined in huaweicloud sdk

        :param metric_query_mode: 指标查询模式。 - “AOM”：AOM原生 - “PROM”：AOM Prometheus - “NATIVE_PROM”：原生Prometheus
        :type metric_query_mode: str
        :param metric_namespace: 指标命名空间。
        :type metric_namespace: str
        :param metric_name: 指标名称。
        :type metric_name: str
        :param metric_unit: 指标单位。
        :type metric_unit: str
        :param metric_labels: 指标维度。
        :type metric_labels: list[str]
        :param promql: Prometheus语句。
        :type promql: str
        :param promql_expr: Prometheus语句模板。
        :type promql_expr: list[str]
        :param trigger_times: 连续周期个数。
        :type trigger_times: str
        :param trigger_interval: 检查频率周期。 - 当trigger_type 为“HOURLY”时，填“” - 当trigger_type为“DAILY”时，格式为：“小时” 例如 每天凌晨三点\&quot;03:00\&quot; - 当trigger_type为“WEEKLY”时，格式为：“星期 小时”例如每周一凌晨三点 “1 03:00” - 当trigger_type为“CRON”时，格式为 标准CRON表达式 - 当trigger_type为“FIXED_RATE”时，秒的取值为15s，30s，分钟为 1~59，小时为 1~24。例如：“15s”，“30s”，“1min”，“1h”
        :type trigger_interval: str
        :param trigger_type: 触发频率的类型： - “FIXED_RATE”：固定间隔 - “HOURLY”：每小时 - “DAILY”：每天 - “WEEKLY”：每周 - “CRON”：Cron表达式
        :type trigger_type: str
        :param promql_for: Prometheus原生监控时长。
        :type promql_for: str
        :param aggregation_type: 统计方式： - average - minimum - maximum - sum - sampleCount
        :type aggregation_type: str
        :param operator: 判断条件：“&gt;”,“&lt;”,“&#x3D;”,“&gt;&#x3D;”,“&lt;&#x3D;”
        :type operator: str
        :param thresholds: 键值对形式，键为告警级别，值为告警阈值
        :type thresholds: dict(str, str)
        :param aggregation_window: 统计周期。 - “15s” - “30s” - “1m” - “5m” - “15m” - “1h”
        :type aggregation_window: str
        :param cmdb: 
        :type cmdb: :class:`huaweicloudsdkaom.v2.CmdbInfo`
        :param query_match: 查询筛选条件。
        :type query_match: str
        :param query_param: 查询参数
        :type query_param: str
        :param aom_monitor_level: 监控层级。
        :type aom_monitor_level: str
        :param aggregate_type: 聚合方式。 - “by”：不分组 - “avg” - “max” - “min” - “sum”
        :type aggregate_type: str
        :param metric_statistic_method: 当配置方式为全量指标时可选择的指标运算方式。 - “single”：单个指标进行运算 - “mix”：多个指标进行混合运算
        :type metric_statistic_method: str
        :param expression: 混合运算的表达式。
        :type expression: str
        :param mix_promql: 混合运算的promQL。
        :type mix_promql: str
        """
        
        

        self._metric_query_mode = None
        self._metric_namespace = None
        self._metric_name = None
        self._metric_unit = None
        self._metric_labels = None
        self._promql = None
        self._promql_expr = None
        self._trigger_times = None
        self._trigger_interval = None
        self._trigger_type = None
        self._promql_for = None
        self._aggregation_type = None
        self._operator = None
        self._thresholds = None
        self._aggregation_window = None
        self._cmdb = None
        self._query_match = None
        self._query_param = None
        self._aom_monitor_level = None
        self._aggregate_type = None
        self._metric_statistic_method = None
        self._expression = None
        self._mix_promql = None
        self.discriminator = None

        self.metric_query_mode = metric_query_mode
        self.metric_namespace = metric_namespace
        self.metric_name = metric_name
        self.metric_unit = metric_unit
        self.metric_labels = metric_labels
        self.promql = promql
        if promql_expr is not None:
            self.promql_expr = promql_expr
        if trigger_times is not None:
            self.trigger_times = trigger_times
        if trigger_interval is not None:
            self.trigger_interval = trigger_interval
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if promql_for is not None:
            self.promql_for = promql_for
        if aggregation_type is not None:
            self.aggregation_type = aggregation_type
        if operator is not None:
            self.operator = operator
        if thresholds is not None:
            self.thresholds = thresholds
        if aggregation_window is not None:
            self.aggregation_window = aggregation_window
        if cmdb is not None:
            self.cmdb = cmdb
        if query_match is not None:
            self.query_match = query_match
        self.query_param = query_param
        if aom_monitor_level is not None:
            self.aom_monitor_level = aom_monitor_level
        if aggregate_type is not None:
            self.aggregate_type = aggregate_type
        if metric_statistic_method is not None:
            self.metric_statistic_method = metric_statistic_method
        if expression is not None:
            self.expression = expression
        if mix_promql is not None:
            self.mix_promql = mix_promql

    @property
    def metric_query_mode(self):
        """Gets the metric_query_mode of this TriggerCondition.

        指标查询模式。 - “AOM”：AOM原生 - “PROM”：AOM Prometheus - “NATIVE_PROM”：原生Prometheus

        :return: The metric_query_mode of this TriggerCondition.
        :rtype: str
        """
        return self._metric_query_mode

    @metric_query_mode.setter
    def metric_query_mode(self, metric_query_mode):
        """Sets the metric_query_mode of this TriggerCondition.

        指标查询模式。 - “AOM”：AOM原生 - “PROM”：AOM Prometheus - “NATIVE_PROM”：原生Prometheus

        :param metric_query_mode: The metric_query_mode of this TriggerCondition.
        :type metric_query_mode: str
        """
        self._metric_query_mode = metric_query_mode

    @property
    def metric_namespace(self):
        """Gets the metric_namespace of this TriggerCondition.

        指标命名空间。

        :return: The metric_namespace of this TriggerCondition.
        :rtype: str
        """
        return self._metric_namespace

    @metric_namespace.setter
    def metric_namespace(self, metric_namespace):
        """Sets the metric_namespace of this TriggerCondition.

        指标命名空间。

        :param metric_namespace: The metric_namespace of this TriggerCondition.
        :type metric_namespace: str
        """
        self._metric_namespace = metric_namespace

    @property
    def metric_name(self):
        """Gets the metric_name of this TriggerCondition.

        指标名称。

        :return: The metric_name of this TriggerCondition.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this TriggerCondition.

        指标名称。

        :param metric_name: The metric_name of this TriggerCondition.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def metric_unit(self):
        """Gets the metric_unit of this TriggerCondition.

        指标单位。

        :return: The metric_unit of this TriggerCondition.
        :rtype: str
        """
        return self._metric_unit

    @metric_unit.setter
    def metric_unit(self, metric_unit):
        """Sets the metric_unit of this TriggerCondition.

        指标单位。

        :param metric_unit: The metric_unit of this TriggerCondition.
        :type metric_unit: str
        """
        self._metric_unit = metric_unit

    @property
    def metric_labels(self):
        """Gets the metric_labels of this TriggerCondition.

        指标维度。

        :return: The metric_labels of this TriggerCondition.
        :rtype: list[str]
        """
        return self._metric_labels

    @metric_labels.setter
    def metric_labels(self, metric_labels):
        """Sets the metric_labels of this TriggerCondition.

        指标维度。

        :param metric_labels: The metric_labels of this TriggerCondition.
        :type metric_labels: list[str]
        """
        self._metric_labels = metric_labels

    @property
    def promql(self):
        """Gets the promql of this TriggerCondition.

        Prometheus语句。

        :return: The promql of this TriggerCondition.
        :rtype: str
        """
        return self._promql

    @promql.setter
    def promql(self, promql):
        """Sets the promql of this TriggerCondition.

        Prometheus语句。

        :param promql: The promql of this TriggerCondition.
        :type promql: str
        """
        self._promql = promql

    @property
    def promql_expr(self):
        """Gets the promql_expr of this TriggerCondition.

        Prometheus语句模板。

        :return: The promql_expr of this TriggerCondition.
        :rtype: list[str]
        """
        return self._promql_expr

    @promql_expr.setter
    def promql_expr(self, promql_expr):
        """Sets the promql_expr of this TriggerCondition.

        Prometheus语句模板。

        :param promql_expr: The promql_expr of this TriggerCondition.
        :type promql_expr: list[str]
        """
        self._promql_expr = promql_expr

    @property
    def trigger_times(self):
        """Gets the trigger_times of this TriggerCondition.

        连续周期个数。

        :return: The trigger_times of this TriggerCondition.
        :rtype: str
        """
        return self._trigger_times

    @trigger_times.setter
    def trigger_times(self, trigger_times):
        """Sets the trigger_times of this TriggerCondition.

        连续周期个数。

        :param trigger_times: The trigger_times of this TriggerCondition.
        :type trigger_times: str
        """
        self._trigger_times = trigger_times

    @property
    def trigger_interval(self):
        """Gets the trigger_interval of this TriggerCondition.

        检查频率周期。 - 当trigger_type 为“HOURLY”时，填“” - 当trigger_type为“DAILY”时，格式为：“小时” 例如 每天凌晨三点\"03:00\" - 当trigger_type为“WEEKLY”时，格式为：“星期 小时”例如每周一凌晨三点 “1 03:00” - 当trigger_type为“CRON”时，格式为 标准CRON表达式 - 当trigger_type为“FIXED_RATE”时，秒的取值为15s，30s，分钟为 1~59，小时为 1~24。例如：“15s”，“30s”，“1min”，“1h”

        :return: The trigger_interval of this TriggerCondition.
        :rtype: str
        """
        return self._trigger_interval

    @trigger_interval.setter
    def trigger_interval(self, trigger_interval):
        """Sets the trigger_interval of this TriggerCondition.

        检查频率周期。 - 当trigger_type 为“HOURLY”时，填“” - 当trigger_type为“DAILY”时，格式为：“小时” 例如 每天凌晨三点\"03:00\" - 当trigger_type为“WEEKLY”时，格式为：“星期 小时”例如每周一凌晨三点 “1 03:00” - 当trigger_type为“CRON”时，格式为 标准CRON表达式 - 当trigger_type为“FIXED_RATE”时，秒的取值为15s，30s，分钟为 1~59，小时为 1~24。例如：“15s”，“30s”，“1min”，“1h”

        :param trigger_interval: The trigger_interval of this TriggerCondition.
        :type trigger_interval: str
        """
        self._trigger_interval = trigger_interval

    @property
    def trigger_type(self):
        """Gets the trigger_type of this TriggerCondition.

        触发频率的类型： - “FIXED_RATE”：固定间隔 - “HOURLY”：每小时 - “DAILY”：每天 - “WEEKLY”：每周 - “CRON”：Cron表达式

        :return: The trigger_type of this TriggerCondition.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this TriggerCondition.

        触发频率的类型： - “FIXED_RATE”：固定间隔 - “HOURLY”：每小时 - “DAILY”：每天 - “WEEKLY”：每周 - “CRON”：Cron表达式

        :param trigger_type: The trigger_type of this TriggerCondition.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def promql_for(self):
        """Gets the promql_for of this TriggerCondition.

        Prometheus原生监控时长。

        :return: The promql_for of this TriggerCondition.
        :rtype: str
        """
        return self._promql_for

    @promql_for.setter
    def promql_for(self, promql_for):
        """Sets the promql_for of this TriggerCondition.

        Prometheus原生监控时长。

        :param promql_for: The promql_for of this TriggerCondition.
        :type promql_for: str
        """
        self._promql_for = promql_for

    @property
    def aggregation_type(self):
        """Gets the aggregation_type of this TriggerCondition.

        统计方式： - average - minimum - maximum - sum - sampleCount

        :return: The aggregation_type of this TriggerCondition.
        :rtype: str
        """
        return self._aggregation_type

    @aggregation_type.setter
    def aggregation_type(self, aggregation_type):
        """Sets the aggregation_type of this TriggerCondition.

        统计方式： - average - minimum - maximum - sum - sampleCount

        :param aggregation_type: The aggregation_type of this TriggerCondition.
        :type aggregation_type: str
        """
        self._aggregation_type = aggregation_type

    @property
    def operator(self):
        """Gets the operator of this TriggerCondition.

        判断条件：“>”,“<”,“=”,“>=”,“<=”

        :return: The operator of this TriggerCondition.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this TriggerCondition.

        判断条件：“>”,“<”,“=”,“>=”,“<=”

        :param operator: The operator of this TriggerCondition.
        :type operator: str
        """
        self._operator = operator

    @property
    def thresholds(self):
        """Gets the thresholds of this TriggerCondition.

        键值对形式，键为告警级别，值为告警阈值

        :return: The thresholds of this TriggerCondition.
        :rtype: dict(str, str)
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this TriggerCondition.

        键值对形式，键为告警级别，值为告警阈值

        :param thresholds: The thresholds of this TriggerCondition.
        :type thresholds: dict(str, str)
        """
        self._thresholds = thresholds

    @property
    def aggregation_window(self):
        """Gets the aggregation_window of this TriggerCondition.

        统计周期。 - “15s” - “30s” - “1m” - “5m” - “15m” - “1h”

        :return: The aggregation_window of this TriggerCondition.
        :rtype: str
        """
        return self._aggregation_window

    @aggregation_window.setter
    def aggregation_window(self, aggregation_window):
        """Sets the aggregation_window of this TriggerCondition.

        统计周期。 - “15s” - “30s” - “1m” - “5m” - “15m” - “1h”

        :param aggregation_window: The aggregation_window of this TriggerCondition.
        :type aggregation_window: str
        """
        self._aggregation_window = aggregation_window

    @property
    def cmdb(self):
        """Gets the cmdb of this TriggerCondition.

        :return: The cmdb of this TriggerCondition.
        :rtype: :class:`huaweicloudsdkaom.v2.CmdbInfo`
        """
        return self._cmdb

    @cmdb.setter
    def cmdb(self, cmdb):
        """Sets the cmdb of this TriggerCondition.

        :param cmdb: The cmdb of this TriggerCondition.
        :type cmdb: :class:`huaweicloudsdkaom.v2.CmdbInfo`
        """
        self._cmdb = cmdb

    @property
    def query_match(self):
        """Gets the query_match of this TriggerCondition.

        查询筛选条件。

        :return: The query_match of this TriggerCondition.
        :rtype: str
        """
        return self._query_match

    @query_match.setter
    def query_match(self, query_match):
        """Sets the query_match of this TriggerCondition.

        查询筛选条件。

        :param query_match: The query_match of this TriggerCondition.
        :type query_match: str
        """
        self._query_match = query_match

    @property
    def query_param(self):
        """Gets the query_param of this TriggerCondition.

        查询参数

        :return: The query_param of this TriggerCondition.
        :rtype: str
        """
        return self._query_param

    @query_param.setter
    def query_param(self, query_param):
        """Sets the query_param of this TriggerCondition.

        查询参数

        :param query_param: The query_param of this TriggerCondition.
        :type query_param: str
        """
        self._query_param = query_param

    @property
    def aom_monitor_level(self):
        """Gets the aom_monitor_level of this TriggerCondition.

        监控层级。

        :return: The aom_monitor_level of this TriggerCondition.
        :rtype: str
        """
        return self._aom_monitor_level

    @aom_monitor_level.setter
    def aom_monitor_level(self, aom_monitor_level):
        """Sets the aom_monitor_level of this TriggerCondition.

        监控层级。

        :param aom_monitor_level: The aom_monitor_level of this TriggerCondition.
        :type aom_monitor_level: str
        """
        self._aom_monitor_level = aom_monitor_level

    @property
    def aggregate_type(self):
        """Gets the aggregate_type of this TriggerCondition.

        聚合方式。 - “by”：不分组 - “avg” - “max” - “min” - “sum”

        :return: The aggregate_type of this TriggerCondition.
        :rtype: str
        """
        return self._aggregate_type

    @aggregate_type.setter
    def aggregate_type(self, aggregate_type):
        """Sets the aggregate_type of this TriggerCondition.

        聚合方式。 - “by”：不分组 - “avg” - “max” - “min” - “sum”

        :param aggregate_type: The aggregate_type of this TriggerCondition.
        :type aggregate_type: str
        """
        self._aggregate_type = aggregate_type

    @property
    def metric_statistic_method(self):
        """Gets the metric_statistic_method of this TriggerCondition.

        当配置方式为全量指标时可选择的指标运算方式。 - “single”：单个指标进行运算 - “mix”：多个指标进行混合运算

        :return: The metric_statistic_method of this TriggerCondition.
        :rtype: str
        """
        return self._metric_statistic_method

    @metric_statistic_method.setter
    def metric_statistic_method(self, metric_statistic_method):
        """Sets the metric_statistic_method of this TriggerCondition.

        当配置方式为全量指标时可选择的指标运算方式。 - “single”：单个指标进行运算 - “mix”：多个指标进行混合运算

        :param metric_statistic_method: The metric_statistic_method of this TriggerCondition.
        :type metric_statistic_method: str
        """
        self._metric_statistic_method = metric_statistic_method

    @property
    def expression(self):
        """Gets the expression of this TriggerCondition.

        混合运算的表达式。

        :return: The expression of this TriggerCondition.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this TriggerCondition.

        混合运算的表达式。

        :param expression: The expression of this TriggerCondition.
        :type expression: str
        """
        self._expression = expression

    @property
    def mix_promql(self):
        """Gets the mix_promql of this TriggerCondition.

        混合运算的promQL。

        :return: The mix_promql of this TriggerCondition.
        :rtype: str
        """
        return self._mix_promql

    @mix_promql.setter
    def mix_promql(self, mix_promql):
        """Sets the mix_promql of this TriggerCondition.

        混合运算的promQL。

        :param mix_promql: The mix_promql of this TriggerCondition.
        :type mix_promql: str
        """
        self._mix_promql = mix_promql

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
        if not isinstance(other, TriggerCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
