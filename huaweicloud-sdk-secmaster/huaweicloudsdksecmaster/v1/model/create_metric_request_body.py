# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMetricRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'metric_type': 'str',
        'data_type': 'str',
        'metric_dimension': 'int',
        'cache_ttl': 'int',
        'report_period': 'int',
        'is_built_in': 'bool',
        'effective_column': 'str',
        'max_query_range': 'int',
        'derived_metrics': 'list[MetricMetaDataDerivedMetrics]',
        'compound_expression': 'str',
        'metric_format': 'list[LayoutMetricFormat]',
        'metric_expand_dim': 'MetricDimensionExpandParam',
        'version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'metric_type': 'metric_type',
        'data_type': 'data_type',
        'metric_dimension': 'metric_dimension',
        'cache_ttl': 'cache_ttl',
        'report_period': 'report_period',
        'is_built_in': 'is_built_in',
        'effective_column': 'effective_column',
        'max_query_range': 'max_query_range',
        'derived_metrics': 'derived_metrics',
        'compound_expression': 'compound_expression',
        'metric_format': 'metric_format',
        'metric_expand_dim': 'metric_expand_dim',
        'version': 'version'
    }

    def __init__(self, name=None, id=None, metric_type=None, data_type=None, metric_dimension=None, cache_ttl=None, report_period=None, is_built_in=None, effective_column=None, max_query_range=None, derived_metrics=None, compound_expression=None, metric_format=None, metric_expand_dim=None, version=None):
        r"""CreateMetricRequestBody

        The model defined in huaweicloud sdk

        :param name: 指标名称
        :type name: str
        :param id: 指标Id
        :type id: str
        :param metric_type: 指标类型， 当前仅支持创建日志类型指标
        :type metric_type: str
        :param data_type: 数据类型, 当前仅支持创建统计指标
        :type data_type: str
        :param metric_dimension: 指标结果维度，0维：单个数字，2维：图表或表格，3+维：多标签图表, metric_type为DERIVED必填，其他类型选填（COMPOUND时必为0）
        :type metric_dimension: int
        :param cache_ttl: 缓存生命周期，单位s
        :type cache_ttl: int
        :param report_period: 上报周期，埋点指标时必填，单位s
        :type report_period: int
        :param is_built_in: 是否为系统指标
        :type is_built_in: bool
        :param effective_column: 生效的列, 当有该参数时，使用指定列作为指标数据结果
        :type effective_column: str
        :param max_query_range: 指标支持的最大检索范围，单位：天；复合指标时，数值为derived_metrics列表元素中最小值
        :type max_query_range: int
        :param derived_metrics: 衍生指标列表，非复合指标时只有一个元素，复合指标时，为各衍生指标的定义
        :type derived_metrics: list[:class:`huaweicloudsdksecmaster.v1.MetricMetaDataDerivedMetrics`]
        :param compound_expression: metric_type为DERIVED时填写, 复合指标的表达式
        :type compound_expression: str
        :param metric_format: 指标格式
        :type metric_format: list[:class:`huaweicloudsdksecmaster.v1.LayoutMetricFormat`]
        :param metric_expand_dim: 
        :type metric_expand_dim: :class:`huaweicloudsdksecmaster.v1.MetricDimensionExpandParam`
        :param version: 安全云脑版本
        :type version: str
        """
        
        

        self._name = None
        self._id = None
        self._metric_type = None
        self._data_type = None
        self._metric_dimension = None
        self._cache_ttl = None
        self._report_period = None
        self._is_built_in = None
        self._effective_column = None
        self._max_query_range = None
        self._derived_metrics = None
        self._compound_expression = None
        self._metric_format = None
        self._metric_expand_dim = None
        self._version = None
        self.discriminator = None

        self.name = name
        if id is not None:
            self.id = id
        self.metric_type = metric_type
        self.data_type = data_type
        if metric_dimension is not None:
            self.metric_dimension = metric_dimension
        self.cache_ttl = cache_ttl
        if report_period is not None:
            self.report_period = report_period
        if is_built_in is not None:
            self.is_built_in = is_built_in
        if effective_column is not None:
            self.effective_column = effective_column
        if max_query_range is not None:
            self.max_query_range = max_query_range
        if derived_metrics is not None:
            self.derived_metrics = derived_metrics
        if compound_expression is not None:
            self.compound_expression = compound_expression
        if metric_format is not None:
            self.metric_format = metric_format
        if metric_expand_dim is not None:
            self.metric_expand_dim = metric_expand_dim
        if version is not None:
            self.version = version

    @property
    def name(self):
        r"""Gets the name of this CreateMetricRequestBody.

        指标名称

        :return: The name of this CreateMetricRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateMetricRequestBody.

        指标名称

        :param name: The name of this CreateMetricRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this CreateMetricRequestBody.

        指标Id

        :return: The id of this CreateMetricRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateMetricRequestBody.

        指标Id

        :param id: The id of this CreateMetricRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def metric_type(self):
        r"""Gets the metric_type of this CreateMetricRequestBody.

        指标类型， 当前仅支持创建日志类型指标

        :return: The metric_type of this CreateMetricRequestBody.
        :rtype: str
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        r"""Sets the metric_type of this CreateMetricRequestBody.

        指标类型， 当前仅支持创建日志类型指标

        :param metric_type: The metric_type of this CreateMetricRequestBody.
        :type metric_type: str
        """
        self._metric_type = metric_type

    @property
    def data_type(self):
        r"""Gets the data_type of this CreateMetricRequestBody.

        数据类型, 当前仅支持创建统计指标

        :return: The data_type of this CreateMetricRequestBody.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this CreateMetricRequestBody.

        数据类型, 当前仅支持创建统计指标

        :param data_type: The data_type of this CreateMetricRequestBody.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def metric_dimension(self):
        r"""Gets the metric_dimension of this CreateMetricRequestBody.

        指标结果维度，0维：单个数字，2维：图表或表格，3+维：多标签图表, metric_type为DERIVED必填，其他类型选填（COMPOUND时必为0）

        :return: The metric_dimension of this CreateMetricRequestBody.
        :rtype: int
        """
        return self._metric_dimension

    @metric_dimension.setter
    def metric_dimension(self, metric_dimension):
        r"""Sets the metric_dimension of this CreateMetricRequestBody.

        指标结果维度，0维：单个数字，2维：图表或表格，3+维：多标签图表, metric_type为DERIVED必填，其他类型选填（COMPOUND时必为0）

        :param metric_dimension: The metric_dimension of this CreateMetricRequestBody.
        :type metric_dimension: int
        """
        self._metric_dimension = metric_dimension

    @property
    def cache_ttl(self):
        r"""Gets the cache_ttl of this CreateMetricRequestBody.

        缓存生命周期，单位s

        :return: The cache_ttl of this CreateMetricRequestBody.
        :rtype: int
        """
        return self._cache_ttl

    @cache_ttl.setter
    def cache_ttl(self, cache_ttl):
        r"""Sets the cache_ttl of this CreateMetricRequestBody.

        缓存生命周期，单位s

        :param cache_ttl: The cache_ttl of this CreateMetricRequestBody.
        :type cache_ttl: int
        """
        self._cache_ttl = cache_ttl

    @property
    def report_period(self):
        r"""Gets the report_period of this CreateMetricRequestBody.

        上报周期，埋点指标时必填，单位s

        :return: The report_period of this CreateMetricRequestBody.
        :rtype: int
        """
        return self._report_period

    @report_period.setter
    def report_period(self, report_period):
        r"""Sets the report_period of this CreateMetricRequestBody.

        上报周期，埋点指标时必填，单位s

        :param report_period: The report_period of this CreateMetricRequestBody.
        :type report_period: int
        """
        self._report_period = report_period

    @property
    def is_built_in(self):
        r"""Gets the is_built_in of this CreateMetricRequestBody.

        是否为系统指标

        :return: The is_built_in of this CreateMetricRequestBody.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        r"""Sets the is_built_in of this CreateMetricRequestBody.

        是否为系统指标

        :param is_built_in: The is_built_in of this CreateMetricRequestBody.
        :type is_built_in: bool
        """
        self._is_built_in = is_built_in

    @property
    def effective_column(self):
        r"""Gets the effective_column of this CreateMetricRequestBody.

        生效的列, 当有该参数时，使用指定列作为指标数据结果

        :return: The effective_column of this CreateMetricRequestBody.
        :rtype: str
        """
        return self._effective_column

    @effective_column.setter
    def effective_column(self, effective_column):
        r"""Sets the effective_column of this CreateMetricRequestBody.

        生效的列, 当有该参数时，使用指定列作为指标数据结果

        :param effective_column: The effective_column of this CreateMetricRequestBody.
        :type effective_column: str
        """
        self._effective_column = effective_column

    @property
    def max_query_range(self):
        r"""Gets the max_query_range of this CreateMetricRequestBody.

        指标支持的最大检索范围，单位：天；复合指标时，数值为derived_metrics列表元素中最小值

        :return: The max_query_range of this CreateMetricRequestBody.
        :rtype: int
        """
        return self._max_query_range

    @max_query_range.setter
    def max_query_range(self, max_query_range):
        r"""Sets the max_query_range of this CreateMetricRequestBody.

        指标支持的最大检索范围，单位：天；复合指标时，数值为derived_metrics列表元素中最小值

        :param max_query_range: The max_query_range of this CreateMetricRequestBody.
        :type max_query_range: int
        """
        self._max_query_range = max_query_range

    @property
    def derived_metrics(self):
        r"""Gets the derived_metrics of this CreateMetricRequestBody.

        衍生指标列表，非复合指标时只有一个元素，复合指标时，为各衍生指标的定义

        :return: The derived_metrics of this CreateMetricRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.MetricMetaDataDerivedMetrics`]
        """
        return self._derived_metrics

    @derived_metrics.setter
    def derived_metrics(self, derived_metrics):
        r"""Sets the derived_metrics of this CreateMetricRequestBody.

        衍生指标列表，非复合指标时只有一个元素，复合指标时，为各衍生指标的定义

        :param derived_metrics: The derived_metrics of this CreateMetricRequestBody.
        :type derived_metrics: list[:class:`huaweicloudsdksecmaster.v1.MetricMetaDataDerivedMetrics`]
        """
        self._derived_metrics = derived_metrics

    @property
    def compound_expression(self):
        r"""Gets the compound_expression of this CreateMetricRequestBody.

        metric_type为DERIVED时填写, 复合指标的表达式

        :return: The compound_expression of this CreateMetricRequestBody.
        :rtype: str
        """
        return self._compound_expression

    @compound_expression.setter
    def compound_expression(self, compound_expression):
        r"""Sets the compound_expression of this CreateMetricRequestBody.

        metric_type为DERIVED时填写, 复合指标的表达式

        :param compound_expression: The compound_expression of this CreateMetricRequestBody.
        :type compound_expression: str
        """
        self._compound_expression = compound_expression

    @property
    def metric_format(self):
        r"""Gets the metric_format of this CreateMetricRequestBody.

        指标格式

        :return: The metric_format of this CreateMetricRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.LayoutMetricFormat`]
        """
        return self._metric_format

    @metric_format.setter
    def metric_format(self, metric_format):
        r"""Sets the metric_format of this CreateMetricRequestBody.

        指标格式

        :param metric_format: The metric_format of this CreateMetricRequestBody.
        :type metric_format: list[:class:`huaweicloudsdksecmaster.v1.LayoutMetricFormat`]
        """
        self._metric_format = metric_format

    @property
    def metric_expand_dim(self):
        r"""Gets the metric_expand_dim of this CreateMetricRequestBody.

        :return: The metric_expand_dim of this CreateMetricRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v1.MetricDimensionExpandParam`
        """
        return self._metric_expand_dim

    @metric_expand_dim.setter
    def metric_expand_dim(self, metric_expand_dim):
        r"""Sets the metric_expand_dim of this CreateMetricRequestBody.

        :param metric_expand_dim: The metric_expand_dim of this CreateMetricRequestBody.
        :type metric_expand_dim: :class:`huaweicloudsdksecmaster.v1.MetricDimensionExpandParam`
        """
        self._metric_expand_dim = metric_expand_dim

    @property
    def version(self):
        r"""Gets the version of this CreateMetricRequestBody.

        安全云脑版本

        :return: The version of this CreateMetricRequestBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateMetricRequestBody.

        安全云脑版本

        :param version: The version of this CreateMetricRequestBody.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, CreateMetricRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
