# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateTriggerCondition:

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
        'promql_expr': 'str',
        'trigger_times': 'int',
        'trigger_interval': 'str',
        'trigger_type': 'str',
        'promql_for': 'str',
        'aggregation_type': 'str',
        'operator': 'str',
        'thresholds': 'dict(str, str)',
        'aggregation_window': 'str',
        'cmdb': 'CmdbInfo',
        'query_match': 'str',
        'aom_monitor_level': 'str',
        'aggregate_type': 'str',
        'metric_statistic_method': 'str',
        'expression': 'str',
        'mix_promql': 'str',
        'alarm_message_template': 'str',
        'promql_monitor_templates': 'list[str]',
        'query_param': 'object'
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
        'aom_monitor_level': 'aom_monitor_level',
        'aggregate_type': 'aggregate_type',
        'metric_statistic_method': 'metric_statistic_method',
        'expression': 'expression',
        'mix_promql': 'mix_promql',
        'alarm_message_template': 'alarm_message_template',
        'promql_monitor_templates': 'promql_monitor_templates',
        'query_param': 'query_param'
    }

    def __init__(self, metric_query_mode=None, metric_namespace=None, metric_name=None, metric_unit=None, metric_labels=None, promql=None, promql_expr=None, trigger_times=None, trigger_interval=None, trigger_type=None, promql_for=None, aggregation_type=None, operator=None, thresholds=None, aggregation_window=None, cmdb=None, query_match=None, aom_monitor_level=None, aggregate_type=None, metric_statistic_method=None, expression=None, mix_promql=None, alarm_message_template=None, promql_monitor_templates=None, query_param=None):
        r"""TemplateTriggerCondition

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
        :type promql_expr: str
        :param trigger_times: 连续周期个数。
        :type trigger_times: int
        :param trigger_interval: 检查频率周期。 - 当trigger_type 为“HOURLY”时，填“” - 当trigger_type为“DAILY”时，格式为：“小时” 。例如每天凌晨三点\&quot;03:00\&quot;。 - 当trigger_type为“WEEKLY”时，格式为：“星期 小时”。例如每周一凌晨三点 “1 03:00”。 - 当trigger_type为“CRON”时，格式为标准CRON表达式。 - 当trigger_type为“FIXED_RATE”时，秒的取值为15s，30s，分钟为 1~59，小时为 1~24。例如“15s”，“30s”，“1min”，“1h”。
        :type trigger_interval: str
        :param trigger_type: 触发频率的类型： - “FIXED_RATE”：固定间隔 - “HOURLY”：每小时 - “DAILY”：每天 - “WEEKLY”：每周 - “CRON”：Cron表达式
        :type trigger_type: str
        :param promql_for: 持续时间。 持续时间范围： - “0”：立即 - “15s”：15秒 - “30s”：30秒 - “1m”：1分钟
        :type promql_for: str
        :param aggregation_type: 检测规则： - average：平均值 - minimum：最小值 - maximum：最大值 - sum：总计 - sampleCount：样本
        :type aggregation_type: str
        :param operator: 判断条件：“&gt;”,“&lt;”,“&#x3D;”,“&gt;&#x3D;”,“&lt;&#x3D;”
        :type operator: str
        :param thresholds: 键值对形式，键为告警级别，值为告警阈值
        :type thresholds: dict(str, str)
        :param aggregation_window: 统计周期。 - “15s”：15秒 - “30s”：30秒 - “1m”：1分钟 - “5m”：5分钟 - “15m”：15分钟 - “1h”：1小时
        :type aggregation_window: str
        :param cmdb: 
        :type cmdb: :class:`huaweicloudsdkaom.v2.CmdbInfo`
        :param query_match: 查询筛选条件。
        :type query_match: str
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
        :param alarm_message_template: 通知内容。
        :type alarm_message_template: str
        :param promql_monitor_templates: Prometheus监控模板。默认为cluster。
        :type promql_monitor_templates: list[str]
        :param query_param: - PromQL告警规则，该参数为\&quot;{\\\&quot;defaultRule\\\&quot;:{\\\&quot;label\\\&quot;:\\\&quot;自定义\\\&quot;,\\\&quot;id\\\&quot;:\\\&quot;custom\\\&quot;},\\\&quot;templateSelectd\\\&quot;:null,\\\&quot;dimensionsList\\\&quot;:[]}\&quot; - 阈值告警规则，该参数为空。
        :type query_param: object
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
        self._aom_monitor_level = None
        self._aggregate_type = None
        self._metric_statistic_method = None
        self._expression = None
        self._mix_promql = None
        self._alarm_message_template = None
        self._promql_monitor_templates = None
        self._query_param = None
        self.discriminator = None

        if metric_query_mode is not None:
            self.metric_query_mode = metric_query_mode
        if metric_namespace is not None:
            self.metric_namespace = metric_namespace
        if metric_name is not None:
            self.metric_name = metric_name
        if metric_unit is not None:
            self.metric_unit = metric_unit
        if metric_labels is not None:
            self.metric_labels = metric_labels
        if promql is not None:
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
        if alarm_message_template is not None:
            self.alarm_message_template = alarm_message_template
        if promql_monitor_templates is not None:
            self.promql_monitor_templates = promql_monitor_templates
        if query_param is not None:
            self.query_param = query_param

    @property
    def metric_query_mode(self):
        r"""Gets the metric_query_mode of this TemplateTriggerCondition.

        指标查询模式。 - “AOM”：AOM原生 - “PROM”：AOM Prometheus - “NATIVE_PROM”：原生Prometheus

        :return: The metric_query_mode of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._metric_query_mode

    @metric_query_mode.setter
    def metric_query_mode(self, metric_query_mode):
        r"""Sets the metric_query_mode of this TemplateTriggerCondition.

        指标查询模式。 - “AOM”：AOM原生 - “PROM”：AOM Prometheus - “NATIVE_PROM”：原生Prometheus

        :param metric_query_mode: The metric_query_mode of this TemplateTriggerCondition.
        :type metric_query_mode: str
        """
        self._metric_query_mode = metric_query_mode

    @property
    def metric_namespace(self):
        r"""Gets the metric_namespace of this TemplateTriggerCondition.

        指标命名空间。

        :return: The metric_namespace of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._metric_namespace

    @metric_namespace.setter
    def metric_namespace(self, metric_namespace):
        r"""Sets the metric_namespace of this TemplateTriggerCondition.

        指标命名空间。

        :param metric_namespace: The metric_namespace of this TemplateTriggerCondition.
        :type metric_namespace: str
        """
        self._metric_namespace = metric_namespace

    @property
    def metric_name(self):
        r"""Gets the metric_name of this TemplateTriggerCondition.

        指标名称。

        :return: The metric_name of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this TemplateTriggerCondition.

        指标名称。

        :param metric_name: The metric_name of this TemplateTriggerCondition.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def metric_unit(self):
        r"""Gets the metric_unit of this TemplateTriggerCondition.

        指标单位。

        :return: The metric_unit of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._metric_unit

    @metric_unit.setter
    def metric_unit(self, metric_unit):
        r"""Sets the metric_unit of this TemplateTriggerCondition.

        指标单位。

        :param metric_unit: The metric_unit of this TemplateTriggerCondition.
        :type metric_unit: str
        """
        self._metric_unit = metric_unit

    @property
    def metric_labels(self):
        r"""Gets the metric_labels of this TemplateTriggerCondition.

        指标维度。

        :return: The metric_labels of this TemplateTriggerCondition.
        :rtype: list[str]
        """
        return self._metric_labels

    @metric_labels.setter
    def metric_labels(self, metric_labels):
        r"""Sets the metric_labels of this TemplateTriggerCondition.

        指标维度。

        :param metric_labels: The metric_labels of this TemplateTriggerCondition.
        :type metric_labels: list[str]
        """
        self._metric_labels = metric_labels

    @property
    def promql(self):
        r"""Gets the promql of this TemplateTriggerCondition.

        Prometheus语句。

        :return: The promql of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._promql

    @promql.setter
    def promql(self, promql):
        r"""Sets the promql of this TemplateTriggerCondition.

        Prometheus语句。

        :param promql: The promql of this TemplateTriggerCondition.
        :type promql: str
        """
        self._promql = promql

    @property
    def promql_expr(self):
        r"""Gets the promql_expr of this TemplateTriggerCondition.

        Prometheus语句模板。

        :return: The promql_expr of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._promql_expr

    @promql_expr.setter
    def promql_expr(self, promql_expr):
        r"""Sets the promql_expr of this TemplateTriggerCondition.

        Prometheus语句模板。

        :param promql_expr: The promql_expr of this TemplateTriggerCondition.
        :type promql_expr: str
        """
        self._promql_expr = promql_expr

    @property
    def trigger_times(self):
        r"""Gets the trigger_times of this TemplateTriggerCondition.

        连续周期个数。

        :return: The trigger_times of this TemplateTriggerCondition.
        :rtype: int
        """
        return self._trigger_times

    @trigger_times.setter
    def trigger_times(self, trigger_times):
        r"""Sets the trigger_times of this TemplateTriggerCondition.

        连续周期个数。

        :param trigger_times: The trigger_times of this TemplateTriggerCondition.
        :type trigger_times: int
        """
        self._trigger_times = trigger_times

    @property
    def trigger_interval(self):
        r"""Gets the trigger_interval of this TemplateTriggerCondition.

        检查频率周期。 - 当trigger_type 为“HOURLY”时，填“” - 当trigger_type为“DAILY”时，格式为：“小时” 。例如每天凌晨三点\"03:00\"。 - 当trigger_type为“WEEKLY”时，格式为：“星期 小时”。例如每周一凌晨三点 “1 03:00”。 - 当trigger_type为“CRON”时，格式为标准CRON表达式。 - 当trigger_type为“FIXED_RATE”时，秒的取值为15s，30s，分钟为 1~59，小时为 1~24。例如“15s”，“30s”，“1min”，“1h”。

        :return: The trigger_interval of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._trigger_interval

    @trigger_interval.setter
    def trigger_interval(self, trigger_interval):
        r"""Sets the trigger_interval of this TemplateTriggerCondition.

        检查频率周期。 - 当trigger_type 为“HOURLY”时，填“” - 当trigger_type为“DAILY”时，格式为：“小时” 。例如每天凌晨三点\"03:00\"。 - 当trigger_type为“WEEKLY”时，格式为：“星期 小时”。例如每周一凌晨三点 “1 03:00”。 - 当trigger_type为“CRON”时，格式为标准CRON表达式。 - 当trigger_type为“FIXED_RATE”时，秒的取值为15s，30s，分钟为 1~59，小时为 1~24。例如“15s”，“30s”，“1min”，“1h”。

        :param trigger_interval: The trigger_interval of this TemplateTriggerCondition.
        :type trigger_interval: str
        """
        self._trigger_interval = trigger_interval

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this TemplateTriggerCondition.

        触发频率的类型： - “FIXED_RATE”：固定间隔 - “HOURLY”：每小时 - “DAILY”：每天 - “WEEKLY”：每周 - “CRON”：Cron表达式

        :return: The trigger_type of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this TemplateTriggerCondition.

        触发频率的类型： - “FIXED_RATE”：固定间隔 - “HOURLY”：每小时 - “DAILY”：每天 - “WEEKLY”：每周 - “CRON”：Cron表达式

        :param trigger_type: The trigger_type of this TemplateTriggerCondition.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def promql_for(self):
        r"""Gets the promql_for of this TemplateTriggerCondition.

        持续时间。 持续时间范围： - “0”：立即 - “15s”：15秒 - “30s”：30秒 - “1m”：1分钟

        :return: The promql_for of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._promql_for

    @promql_for.setter
    def promql_for(self, promql_for):
        r"""Sets the promql_for of this TemplateTriggerCondition.

        持续时间。 持续时间范围： - “0”：立即 - “15s”：15秒 - “30s”：30秒 - “1m”：1分钟

        :param promql_for: The promql_for of this TemplateTriggerCondition.
        :type promql_for: str
        """
        self._promql_for = promql_for

    @property
    def aggregation_type(self):
        r"""Gets the aggregation_type of this TemplateTriggerCondition.

        检测规则： - average：平均值 - minimum：最小值 - maximum：最大值 - sum：总计 - sampleCount：样本

        :return: The aggregation_type of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._aggregation_type

    @aggregation_type.setter
    def aggregation_type(self, aggregation_type):
        r"""Sets the aggregation_type of this TemplateTriggerCondition.

        检测规则： - average：平均值 - minimum：最小值 - maximum：最大值 - sum：总计 - sampleCount：样本

        :param aggregation_type: The aggregation_type of this TemplateTriggerCondition.
        :type aggregation_type: str
        """
        self._aggregation_type = aggregation_type

    @property
    def operator(self):
        r"""Gets the operator of this TemplateTriggerCondition.

        判断条件：“>”,“<”,“=”,“>=”,“<=”

        :return: The operator of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this TemplateTriggerCondition.

        判断条件：“>”,“<”,“=”,“>=”,“<=”

        :param operator: The operator of this TemplateTriggerCondition.
        :type operator: str
        """
        self._operator = operator

    @property
    def thresholds(self):
        r"""Gets the thresholds of this TemplateTriggerCondition.

        键值对形式，键为告警级别，值为告警阈值

        :return: The thresholds of this TemplateTriggerCondition.
        :rtype: dict(str, str)
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        r"""Sets the thresholds of this TemplateTriggerCondition.

        键值对形式，键为告警级别，值为告警阈值

        :param thresholds: The thresholds of this TemplateTriggerCondition.
        :type thresholds: dict(str, str)
        """
        self._thresholds = thresholds

    @property
    def aggregation_window(self):
        r"""Gets the aggregation_window of this TemplateTriggerCondition.

        统计周期。 - “15s”：15秒 - “30s”：30秒 - “1m”：1分钟 - “5m”：5分钟 - “15m”：15分钟 - “1h”：1小时

        :return: The aggregation_window of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._aggregation_window

    @aggregation_window.setter
    def aggregation_window(self, aggregation_window):
        r"""Sets the aggregation_window of this TemplateTriggerCondition.

        统计周期。 - “15s”：15秒 - “30s”：30秒 - “1m”：1分钟 - “5m”：5分钟 - “15m”：15分钟 - “1h”：1小时

        :param aggregation_window: The aggregation_window of this TemplateTriggerCondition.
        :type aggregation_window: str
        """
        self._aggregation_window = aggregation_window

    @property
    def cmdb(self):
        r"""Gets the cmdb of this TemplateTriggerCondition.

        :return: The cmdb of this TemplateTriggerCondition.
        :rtype: :class:`huaweicloudsdkaom.v2.CmdbInfo`
        """
        return self._cmdb

    @cmdb.setter
    def cmdb(self, cmdb):
        r"""Sets the cmdb of this TemplateTriggerCondition.

        :param cmdb: The cmdb of this TemplateTriggerCondition.
        :type cmdb: :class:`huaweicloudsdkaom.v2.CmdbInfo`
        """
        self._cmdb = cmdb

    @property
    def query_match(self):
        r"""Gets the query_match of this TemplateTriggerCondition.

        查询筛选条件。

        :return: The query_match of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._query_match

    @query_match.setter
    def query_match(self, query_match):
        r"""Sets the query_match of this TemplateTriggerCondition.

        查询筛选条件。

        :param query_match: The query_match of this TemplateTriggerCondition.
        :type query_match: str
        """
        self._query_match = query_match

    @property
    def aom_monitor_level(self):
        r"""Gets the aom_monitor_level of this TemplateTriggerCondition.

        监控层级。

        :return: The aom_monitor_level of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._aom_monitor_level

    @aom_monitor_level.setter
    def aom_monitor_level(self, aom_monitor_level):
        r"""Sets the aom_monitor_level of this TemplateTriggerCondition.

        监控层级。

        :param aom_monitor_level: The aom_monitor_level of this TemplateTriggerCondition.
        :type aom_monitor_level: str
        """
        self._aom_monitor_level = aom_monitor_level

    @property
    def aggregate_type(self):
        r"""Gets the aggregate_type of this TemplateTriggerCondition.

        聚合方式。 - “by”：不分组 - “avg” - “max” - “min” - “sum”

        :return: The aggregate_type of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._aggregate_type

    @aggregate_type.setter
    def aggregate_type(self, aggregate_type):
        r"""Sets the aggregate_type of this TemplateTriggerCondition.

        聚合方式。 - “by”：不分组 - “avg” - “max” - “min” - “sum”

        :param aggregate_type: The aggregate_type of this TemplateTriggerCondition.
        :type aggregate_type: str
        """
        self._aggregate_type = aggregate_type

    @property
    def metric_statistic_method(self):
        r"""Gets the metric_statistic_method of this TemplateTriggerCondition.

        当配置方式为全量指标时可选择的指标运算方式。 - “single”：单个指标进行运算 - “mix”：多个指标进行混合运算

        :return: The metric_statistic_method of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._metric_statistic_method

    @metric_statistic_method.setter
    def metric_statistic_method(self, metric_statistic_method):
        r"""Sets the metric_statistic_method of this TemplateTriggerCondition.

        当配置方式为全量指标时可选择的指标运算方式。 - “single”：单个指标进行运算 - “mix”：多个指标进行混合运算

        :param metric_statistic_method: The metric_statistic_method of this TemplateTriggerCondition.
        :type metric_statistic_method: str
        """
        self._metric_statistic_method = metric_statistic_method

    @property
    def expression(self):
        r"""Gets the expression of this TemplateTriggerCondition.

        混合运算的表达式。

        :return: The expression of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        r"""Sets the expression of this TemplateTriggerCondition.

        混合运算的表达式。

        :param expression: The expression of this TemplateTriggerCondition.
        :type expression: str
        """
        self._expression = expression

    @property
    def mix_promql(self):
        r"""Gets the mix_promql of this TemplateTriggerCondition.

        混合运算的promQL。

        :return: The mix_promql of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._mix_promql

    @mix_promql.setter
    def mix_promql(self, mix_promql):
        r"""Sets the mix_promql of this TemplateTriggerCondition.

        混合运算的promQL。

        :param mix_promql: The mix_promql of this TemplateTriggerCondition.
        :type mix_promql: str
        """
        self._mix_promql = mix_promql

    @property
    def alarm_message_template(self):
        r"""Gets the alarm_message_template of this TemplateTriggerCondition.

        通知内容。

        :return: The alarm_message_template of this TemplateTriggerCondition.
        :rtype: str
        """
        return self._alarm_message_template

    @alarm_message_template.setter
    def alarm_message_template(self, alarm_message_template):
        r"""Sets the alarm_message_template of this TemplateTriggerCondition.

        通知内容。

        :param alarm_message_template: The alarm_message_template of this TemplateTriggerCondition.
        :type alarm_message_template: str
        """
        self._alarm_message_template = alarm_message_template

    @property
    def promql_monitor_templates(self):
        r"""Gets the promql_monitor_templates of this TemplateTriggerCondition.

        Prometheus监控模板。默认为cluster。

        :return: The promql_monitor_templates of this TemplateTriggerCondition.
        :rtype: list[str]
        """
        return self._promql_monitor_templates

    @promql_monitor_templates.setter
    def promql_monitor_templates(self, promql_monitor_templates):
        r"""Sets the promql_monitor_templates of this TemplateTriggerCondition.

        Prometheus监控模板。默认为cluster。

        :param promql_monitor_templates: The promql_monitor_templates of this TemplateTriggerCondition.
        :type promql_monitor_templates: list[str]
        """
        self._promql_monitor_templates = promql_monitor_templates

    @property
    def query_param(self):
        r"""Gets the query_param of this TemplateTriggerCondition.

        - PromQL告警规则，该参数为\"{\\\"defaultRule\\\":{\\\"label\\\":\\\"自定义\\\",\\\"id\\\":\\\"custom\\\"},\\\"templateSelectd\\\":null,\\\"dimensionsList\\\":[]}\" - 阈值告警规则，该参数为空。

        :return: The query_param of this TemplateTriggerCondition.
        :rtype: object
        """
        return self._query_param

    @query_param.setter
    def query_param(self, query_param):
        r"""Sets the query_param of this TemplateTriggerCondition.

        - PromQL告警规则，该参数为\"{\\\"defaultRule\\\":{\\\"label\\\":\\\"自定义\\\",\\\"id\\\":\\\"custom\\\"},\\\"templateSelectd\\\":null,\\\"dimensionsList\\\":[]}\" - 阈值告警规则，该参数为空。

        :param query_param: The query_param of this TemplateTriggerCondition.
        :type query_param: object
        """
        self._query_param = query_param

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
        if not isinstance(other, TemplateTriggerCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
