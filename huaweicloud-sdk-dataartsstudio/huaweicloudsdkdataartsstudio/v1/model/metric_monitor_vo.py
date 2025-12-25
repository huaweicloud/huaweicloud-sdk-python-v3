# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricMonitorVO:

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
        'other_metric_ids': 'list[str]',
        'other_metric_names': 'list[str]',
        'other_compound_metric_ids': 'list[str]',
        'other_compound_metric_names': 'list[str]',
        'expression': 'str',
        'metric_id': 'str',
        'front_configs': 'str',
        'metric_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'other_metric_ids': 'other_metric_ids',
        'other_metric_names': 'other_metric_names',
        'other_compound_metric_ids': 'other_compound_metric_ids',
        'other_compound_metric_names': 'other_compound_metric_names',
        'expression': 'expression',
        'metric_id': 'metric_id',
        'front_configs': 'front_configs',
        'metric_type': 'metric_type'
    }

    def __init__(self, id=None, other_metric_ids=None, other_metric_names=None, other_compound_metric_ids=None, other_compound_metric_names=None, expression=None, metric_id=None, front_configs=None, metric_type=None):
        r"""MetricMonitorVO

        The model defined in huaweicloud sdk

        :param id: 编码，ID字符串。
        :type id: str
        :param other_metric_ids: 其他指标ID，ID字符串。
        :type other_metric_ids: list[str]
        :param other_metric_names: 其他指标名称，只读。
        :type other_metric_names: list[str]
        :param other_compound_metric_ids: 其他复合指标ID。
        :type other_compound_metric_ids: list[str]
        :param other_compound_metric_names: 其他复合指标名称。
        :type other_compound_metric_names: list[str]
        :param expression: 告警表达式。
        :type expression: str
        :param metric_id: 挂载指ID，ID字符串。
        :type metric_id: str
        :param front_configs: 前端表达式配置，用于前端数据恢复。
        :type front_configs: str
        :param metric_type: 业务实体类型。 枚举值：  - AGGREGATION_LOGIC_TABLE: 汇总表  - ATOMIC_INDEX: 原子指标  - ATOMIC_METRIC: 原子指标（新）  - BIZ_CATALOG: 流程架构目录  - BIZ_METRIC: 业务指标  - CODE_TABLE: 码表  - COMMON_CONDITION: 通用限定  - COMPOSITE_METRIC: 复合指标（新）  - COMPOUND_METRIC: 复合指标  - CONDITION_GROUP: 限定分组  - DEGENERATE_DIMENSION: 退化维度  - DERIVATIVE_INDEX: 衍生指标  - DERIVED_METRIC: 衍生指标（新）  - DIMENSION: 维度  - DIMENSION_ATTRIBUTE: 维度属性  - DIMENSION_HIERARCHIES: 维度层级  - DIMENSION_LOGIC_TABLE: 维度表  - DIMENSION_TABLE_ATTRIBUTE: 维度属性  - DIRECTORY: 目录  - FACT_ATTRIBUTE: 事实表属性  - FACT_DIMENSION: 事实表维度  - FACT_LOGIC_TABLE: 事实表  - FACT_MEASURE: 事实表度量  - FUNCTION: 函数  - INFO_ARCH: 信息架构（批量修改主题使用）  - MODEL: 模型  - QUALITY_RULE: 质量规则  - SECRECY_LEVEL: 密级  - STANDARD_ELEMENT: 数据标准  - STANDARD_ELEMENT_TEMPLATE: 数据标准模板  - SUBJECT: 主题  - SUMMARY_DIMENSION_ATTRIBUTE: 汇总表维度属性  - SUMMARY_INDEX: 汇总表指标属性  - SUMMARY_TIME: 汇总表时间周期属性  - TABLE_MODEL: 关系模型（逻辑模型/物理模型）  - TABLE_MODEL_ATTRIBUTE: 关系模型属性（逻辑模型/物理模型）  - TABLE_MODEL_LOGIC: 逻辑实体  - TABLE_TYPE: 表类型  - TAG: 标签  - TIME_CONDITION: 时间限定 
        :type metric_type: str
        """
        
        

        self._id = None
        self._other_metric_ids = None
        self._other_metric_names = None
        self._other_compound_metric_ids = None
        self._other_compound_metric_names = None
        self._expression = None
        self._metric_id = None
        self._front_configs = None
        self._metric_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if other_metric_ids is not None:
            self.other_metric_ids = other_metric_ids
        if other_metric_names is not None:
            self.other_metric_names = other_metric_names
        if other_compound_metric_ids is not None:
            self.other_compound_metric_ids = other_compound_metric_ids
        if other_compound_metric_names is not None:
            self.other_compound_metric_names = other_compound_metric_names
        if expression is not None:
            self.expression = expression
        if metric_id is not None:
            self.metric_id = metric_id
        if front_configs is not None:
            self.front_configs = front_configs
        if metric_type is not None:
            self.metric_type = metric_type

    @property
    def id(self):
        r"""Gets the id of this MetricMonitorVO.

        编码，ID字符串。

        :return: The id of this MetricMonitorVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MetricMonitorVO.

        编码，ID字符串。

        :param id: The id of this MetricMonitorVO.
        :type id: str
        """
        self._id = id

    @property
    def other_metric_ids(self):
        r"""Gets the other_metric_ids of this MetricMonitorVO.

        其他指标ID，ID字符串。

        :return: The other_metric_ids of this MetricMonitorVO.
        :rtype: list[str]
        """
        return self._other_metric_ids

    @other_metric_ids.setter
    def other_metric_ids(self, other_metric_ids):
        r"""Sets the other_metric_ids of this MetricMonitorVO.

        其他指标ID，ID字符串。

        :param other_metric_ids: The other_metric_ids of this MetricMonitorVO.
        :type other_metric_ids: list[str]
        """
        self._other_metric_ids = other_metric_ids

    @property
    def other_metric_names(self):
        r"""Gets the other_metric_names of this MetricMonitorVO.

        其他指标名称，只读。

        :return: The other_metric_names of this MetricMonitorVO.
        :rtype: list[str]
        """
        return self._other_metric_names

    @other_metric_names.setter
    def other_metric_names(self, other_metric_names):
        r"""Sets the other_metric_names of this MetricMonitorVO.

        其他指标名称，只读。

        :param other_metric_names: The other_metric_names of this MetricMonitorVO.
        :type other_metric_names: list[str]
        """
        self._other_metric_names = other_metric_names

    @property
    def other_compound_metric_ids(self):
        r"""Gets the other_compound_metric_ids of this MetricMonitorVO.

        其他复合指标ID。

        :return: The other_compound_metric_ids of this MetricMonitorVO.
        :rtype: list[str]
        """
        return self._other_compound_metric_ids

    @other_compound_metric_ids.setter
    def other_compound_metric_ids(self, other_compound_metric_ids):
        r"""Sets the other_compound_metric_ids of this MetricMonitorVO.

        其他复合指标ID。

        :param other_compound_metric_ids: The other_compound_metric_ids of this MetricMonitorVO.
        :type other_compound_metric_ids: list[str]
        """
        self._other_compound_metric_ids = other_compound_metric_ids

    @property
    def other_compound_metric_names(self):
        r"""Gets the other_compound_metric_names of this MetricMonitorVO.

        其他复合指标名称。

        :return: The other_compound_metric_names of this MetricMonitorVO.
        :rtype: list[str]
        """
        return self._other_compound_metric_names

    @other_compound_metric_names.setter
    def other_compound_metric_names(self, other_compound_metric_names):
        r"""Sets the other_compound_metric_names of this MetricMonitorVO.

        其他复合指标名称。

        :param other_compound_metric_names: The other_compound_metric_names of this MetricMonitorVO.
        :type other_compound_metric_names: list[str]
        """
        self._other_compound_metric_names = other_compound_metric_names

    @property
    def expression(self):
        r"""Gets the expression of this MetricMonitorVO.

        告警表达式。

        :return: The expression of this MetricMonitorVO.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        r"""Sets the expression of this MetricMonitorVO.

        告警表达式。

        :param expression: The expression of this MetricMonitorVO.
        :type expression: str
        """
        self._expression = expression

    @property
    def metric_id(self):
        r"""Gets the metric_id of this MetricMonitorVO.

        挂载指ID，ID字符串。

        :return: The metric_id of this MetricMonitorVO.
        :rtype: str
        """
        return self._metric_id

    @metric_id.setter
    def metric_id(self, metric_id):
        r"""Sets the metric_id of this MetricMonitorVO.

        挂载指ID，ID字符串。

        :param metric_id: The metric_id of this MetricMonitorVO.
        :type metric_id: str
        """
        self._metric_id = metric_id

    @property
    def front_configs(self):
        r"""Gets the front_configs of this MetricMonitorVO.

        前端表达式配置，用于前端数据恢复。

        :return: The front_configs of this MetricMonitorVO.
        :rtype: str
        """
        return self._front_configs

    @front_configs.setter
    def front_configs(self, front_configs):
        r"""Sets the front_configs of this MetricMonitorVO.

        前端表达式配置，用于前端数据恢复。

        :param front_configs: The front_configs of this MetricMonitorVO.
        :type front_configs: str
        """
        self._front_configs = front_configs

    @property
    def metric_type(self):
        r"""Gets the metric_type of this MetricMonitorVO.

        业务实体类型。 枚举值：  - AGGREGATION_LOGIC_TABLE: 汇总表  - ATOMIC_INDEX: 原子指标  - ATOMIC_METRIC: 原子指标（新）  - BIZ_CATALOG: 流程架构目录  - BIZ_METRIC: 业务指标  - CODE_TABLE: 码表  - COMMON_CONDITION: 通用限定  - COMPOSITE_METRIC: 复合指标（新）  - COMPOUND_METRIC: 复合指标  - CONDITION_GROUP: 限定分组  - DEGENERATE_DIMENSION: 退化维度  - DERIVATIVE_INDEX: 衍生指标  - DERIVED_METRIC: 衍生指标（新）  - DIMENSION: 维度  - DIMENSION_ATTRIBUTE: 维度属性  - DIMENSION_HIERARCHIES: 维度层级  - DIMENSION_LOGIC_TABLE: 维度表  - DIMENSION_TABLE_ATTRIBUTE: 维度属性  - DIRECTORY: 目录  - FACT_ATTRIBUTE: 事实表属性  - FACT_DIMENSION: 事实表维度  - FACT_LOGIC_TABLE: 事实表  - FACT_MEASURE: 事实表度量  - FUNCTION: 函数  - INFO_ARCH: 信息架构（批量修改主题使用）  - MODEL: 模型  - QUALITY_RULE: 质量规则  - SECRECY_LEVEL: 密级  - STANDARD_ELEMENT: 数据标准  - STANDARD_ELEMENT_TEMPLATE: 数据标准模板  - SUBJECT: 主题  - SUMMARY_DIMENSION_ATTRIBUTE: 汇总表维度属性  - SUMMARY_INDEX: 汇总表指标属性  - SUMMARY_TIME: 汇总表时间周期属性  - TABLE_MODEL: 关系模型（逻辑模型/物理模型）  - TABLE_MODEL_ATTRIBUTE: 关系模型属性（逻辑模型/物理模型）  - TABLE_MODEL_LOGIC: 逻辑实体  - TABLE_TYPE: 表类型  - TAG: 标签  - TIME_CONDITION: 时间限定 

        :return: The metric_type of this MetricMonitorVO.
        :rtype: str
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        r"""Sets the metric_type of this MetricMonitorVO.

        业务实体类型。 枚举值：  - AGGREGATION_LOGIC_TABLE: 汇总表  - ATOMIC_INDEX: 原子指标  - ATOMIC_METRIC: 原子指标（新）  - BIZ_CATALOG: 流程架构目录  - BIZ_METRIC: 业务指标  - CODE_TABLE: 码表  - COMMON_CONDITION: 通用限定  - COMPOSITE_METRIC: 复合指标（新）  - COMPOUND_METRIC: 复合指标  - CONDITION_GROUP: 限定分组  - DEGENERATE_DIMENSION: 退化维度  - DERIVATIVE_INDEX: 衍生指标  - DERIVED_METRIC: 衍生指标（新）  - DIMENSION: 维度  - DIMENSION_ATTRIBUTE: 维度属性  - DIMENSION_HIERARCHIES: 维度层级  - DIMENSION_LOGIC_TABLE: 维度表  - DIMENSION_TABLE_ATTRIBUTE: 维度属性  - DIRECTORY: 目录  - FACT_ATTRIBUTE: 事实表属性  - FACT_DIMENSION: 事实表维度  - FACT_LOGIC_TABLE: 事实表  - FACT_MEASURE: 事实表度量  - FUNCTION: 函数  - INFO_ARCH: 信息架构（批量修改主题使用）  - MODEL: 模型  - QUALITY_RULE: 质量规则  - SECRECY_LEVEL: 密级  - STANDARD_ELEMENT: 数据标准  - STANDARD_ELEMENT_TEMPLATE: 数据标准模板  - SUBJECT: 主题  - SUMMARY_DIMENSION_ATTRIBUTE: 汇总表维度属性  - SUMMARY_INDEX: 汇总表指标属性  - SUMMARY_TIME: 汇总表时间周期属性  - TABLE_MODEL: 关系模型（逻辑模型/物理模型）  - TABLE_MODEL_ATTRIBUTE: 关系模型属性（逻辑模型/物理模型）  - TABLE_MODEL_LOGIC: 逻辑实体  - TABLE_TYPE: 表类型  - TAG: 标签  - TIME_CONDITION: 时间限定 

        :param metric_type: The metric_type of this MetricMonitorVO.
        :type metric_type: str
        """
        self._metric_type = metric_type

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
        if not isinstance(other, MetricMonitorVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
