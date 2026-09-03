# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunSparkSqlRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint_name': 'str',
        'catalog_context': 'SparkSqlCatalogContext',
        'statement': 'str',
        'parameters': 'list[SparkSqlParameter]',
        'spark_config': 'dict(str, str)',
        'timeout': 'SparkSqlTimeout',
        'labels': 'list[SparkSqlLabel]'
    }

    attribute_map = {
        'endpoint_name': 'endpoint_name',
        'catalog_context': 'catalog_context',
        'statement': 'statement',
        'parameters': 'parameters',
        'spark_config': 'spark_config',
        'timeout': 'timeout',
        'labels': 'labels'
    }

    def __init__(self, endpoint_name=None, catalog_context=None, statement=None, parameters=None, spark_config=None, timeout=None, labels=None):
        r"""RunSparkSqlRequestBody

        The model defined in huaweicloud sdk

        :param endpoint_name: **参数解释**：端点名称，用于指定SparkSql作业运行的计算引擎。可在控制台的端点管理页面查看，或通过查询端点列表接口获取。 **约束限制**：不涉及。 **取值范围**：只能以英文小写字母开头，由英文小写字母、数字及中划线组成，以英文小写字母或数字结尾，且长度为1~63个字符。 **默认取值**：不涉及。 
        :type endpoint_name: str
        :param catalog_context: 
        :type catalog_context: :class:`huaweicloudsdkaidatalake.v2.SparkSqlCatalogContext`
        :param statement: **参数解释**：用户SQL语句，用于执行SparkSql作业。支持DDL、DCL、DQL、DML等多种SQL类型。 **约束限制**：不涉及。 **取值范围**：不超过500000个字符。 **默认取值**：不涉及。 
        :type statement: str
        :param parameters: **参数解释**：用户SQL语句中的占位符参数列表，用于SQL参数化执行。数组中的每个元素为SparkSqlParameter对象，包含占位符的键、值和类型信息。 **约束限制**：占位符参数数量不能超过16条。 
        :type parameters: list[:class:`huaweicloudsdkaidatalake.v2.SparkSqlParameter`]
        :param spark_config: **参数解释**：用户自定义Spark参数配置，用于优化作业性能。格式为key/value键值对，Key为参数名称，Value为参数值。例如：spark.executor.memory&#x3D;4g。 **约束限制**：参数配置项数量不能超过100条，每个参数值的长度不超过1024个字符。 
        :type spark_config: dict(str, str)
        :param timeout: 
        :type timeout: :class:`huaweicloudsdkaidatalake.v2.SparkSqlTimeout`
        :param labels: **参数解释**：作业标签列表，用于标识和分类作业。数组中的每个元素为SparkSqlLabel对象，包含标签的键和值。 **约束限制**：标签数量不能超过16条。 
        :type labels: list[:class:`huaweicloudsdkaidatalake.v2.SparkSqlLabel`]
        """
        
        

        self._endpoint_name = None
        self._catalog_context = None
        self._statement = None
        self._parameters = None
        self._spark_config = None
        self._timeout = None
        self._labels = None
        self.discriminator = None

        self.endpoint_name = endpoint_name
        self.catalog_context = catalog_context
        self.statement = statement
        if parameters is not None:
            self.parameters = parameters
        if spark_config is not None:
            self.spark_config = spark_config
        if timeout is not None:
            self.timeout = timeout
        if labels is not None:
            self.labels = labels

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this RunSparkSqlRequestBody.

        **参数解释**：端点名称，用于指定SparkSql作业运行的计算引擎。可在控制台的端点管理页面查看，或通过查询端点列表接口获取。 **约束限制**：不涉及。 **取值范围**：只能以英文小写字母开头，由英文小写字母、数字及中划线组成，以英文小写字母或数字结尾，且长度为1~63个字符。 **默认取值**：不涉及。 

        :return: The endpoint_name of this RunSparkSqlRequestBody.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this RunSparkSqlRequestBody.

        **参数解释**：端点名称，用于指定SparkSql作业运行的计算引擎。可在控制台的端点管理页面查看，或通过查询端点列表接口获取。 **约束限制**：不涉及。 **取值范围**：只能以英文小写字母开头，由英文小写字母、数字及中划线组成，以英文小写字母或数字结尾，且长度为1~63个字符。 **默认取值**：不涉及。 

        :param endpoint_name: The endpoint_name of this RunSparkSqlRequestBody.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def catalog_context(self):
        r"""Gets the catalog_context of this RunSparkSqlRequestBody.

        :return: The catalog_context of this RunSparkSqlRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.SparkSqlCatalogContext`
        """
        return self._catalog_context

    @catalog_context.setter
    def catalog_context(self, catalog_context):
        r"""Sets the catalog_context of this RunSparkSqlRequestBody.

        :param catalog_context: The catalog_context of this RunSparkSqlRequestBody.
        :type catalog_context: :class:`huaweicloudsdkaidatalake.v2.SparkSqlCatalogContext`
        """
        self._catalog_context = catalog_context

    @property
    def statement(self):
        r"""Gets the statement of this RunSparkSqlRequestBody.

        **参数解释**：用户SQL语句，用于执行SparkSql作业。支持DDL、DCL、DQL、DML等多种SQL类型。 **约束限制**：不涉及。 **取值范围**：不超过500000个字符。 **默认取值**：不涉及。 

        :return: The statement of this RunSparkSqlRequestBody.
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        r"""Sets the statement of this RunSparkSqlRequestBody.

        **参数解释**：用户SQL语句，用于执行SparkSql作业。支持DDL、DCL、DQL、DML等多种SQL类型。 **约束限制**：不涉及。 **取值范围**：不超过500000个字符。 **默认取值**：不涉及。 

        :param statement: The statement of this RunSparkSqlRequestBody.
        :type statement: str
        """
        self._statement = statement

    @property
    def parameters(self):
        r"""Gets the parameters of this RunSparkSqlRequestBody.

        **参数解释**：用户SQL语句中的占位符参数列表，用于SQL参数化执行。数组中的每个元素为SparkSqlParameter对象，包含占位符的键、值和类型信息。 **约束限制**：占位符参数数量不能超过16条。 

        :return: The parameters of this RunSparkSqlRequestBody.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.SparkSqlParameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this RunSparkSqlRequestBody.

        **参数解释**：用户SQL语句中的占位符参数列表，用于SQL参数化执行。数组中的每个元素为SparkSqlParameter对象，包含占位符的键、值和类型信息。 **约束限制**：占位符参数数量不能超过16条。 

        :param parameters: The parameters of this RunSparkSqlRequestBody.
        :type parameters: list[:class:`huaweicloudsdkaidatalake.v2.SparkSqlParameter`]
        """
        self._parameters = parameters

    @property
    def spark_config(self):
        r"""Gets the spark_config of this RunSparkSqlRequestBody.

        **参数解释**：用户自定义Spark参数配置，用于优化作业性能。格式为key/value键值对，Key为参数名称，Value为参数值。例如：spark.executor.memory=4g。 **约束限制**：参数配置项数量不能超过100条，每个参数值的长度不超过1024个字符。 

        :return: The spark_config of this RunSparkSqlRequestBody.
        :rtype: dict(str, str)
        """
        return self._spark_config

    @spark_config.setter
    def spark_config(self, spark_config):
        r"""Sets the spark_config of this RunSparkSqlRequestBody.

        **参数解释**：用户自定义Spark参数配置，用于优化作业性能。格式为key/value键值对，Key为参数名称，Value为参数值。例如：spark.executor.memory=4g。 **约束限制**：参数配置项数量不能超过100条，每个参数值的长度不超过1024个字符。 

        :param spark_config: The spark_config of this RunSparkSqlRequestBody.
        :type spark_config: dict(str, str)
        """
        self._spark_config = spark_config

    @property
    def timeout(self):
        r"""Gets the timeout of this RunSparkSqlRequestBody.

        :return: The timeout of this RunSparkSqlRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.SparkSqlTimeout`
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this RunSparkSqlRequestBody.

        :param timeout: The timeout of this RunSparkSqlRequestBody.
        :type timeout: :class:`huaweicloudsdkaidatalake.v2.SparkSqlTimeout`
        """
        self._timeout = timeout

    @property
    def labels(self):
        r"""Gets the labels of this RunSparkSqlRequestBody.

        **参数解释**：作业标签列表，用于标识和分类作业。数组中的每个元素为SparkSqlLabel对象，包含标签的键和值。 **约束限制**：标签数量不能超过16条。 

        :return: The labels of this RunSparkSqlRequestBody.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.SparkSqlLabel`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this RunSparkSqlRequestBody.

        **参数解释**：作业标签列表，用于标识和分类作业。数组中的每个元素为SparkSqlLabel对象，包含标签的键和值。 **约束限制**：标签数量不能超过16条。 

        :param labels: The labels of this RunSparkSqlRequestBody.
        :type labels: list[:class:`huaweicloudsdkaidatalake.v2.SparkSqlLabel`]
        """
        self._labels = labels

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
        if not isinstance(other, RunSparkSqlRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
