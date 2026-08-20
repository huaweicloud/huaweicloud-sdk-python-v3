# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunSparkJobRequestBody:

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
        'endpoint_name': 'str',
        'job_config': 'object',
        'catalog_name': 'str',
        'job_agency': 'str',
        'resource_config': 'SparkResourceConfig',
        'spark_config': 'dict(str, str)',
        'image': 'SparkJobImageConfig',
        'logging_config': 'SparkLoggingConfig',
        'restore_strategy': 'SparkRestoreStrategy',
        'labels': 'list[SparkJobLabel]',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'endpoint_name': 'endpoint_name',
        'job_config': 'job_config',
        'catalog_name': 'catalog_name',
        'job_agency': 'job_agency',
        'resource_config': 'resource_config',
        'spark_config': 'spark_config',
        'image': 'image',
        'logging_config': 'logging_config',
        'restore_strategy': 'restore_strategy',
        'labels': 'labels',
        'description': 'description'
    }

    def __init__(self, name=None, endpoint_name=None, job_config=None, catalog_name=None, job_agency=None, resource_config=None, spark_config=None, image=None, logging_config=None, restore_strategy=None, labels=None, description=None):
        r"""RunSparkJobRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释**：Spark作业名称，用于标识作业。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符。 **默认取值**：不涉及。
        :type name: str
        :param endpoint_name: **参数解释**：端点名称，用于指定Spark作业执行环境。 **约束限制**：不涉及。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。 **默认取值**：不涉及。
        :type endpoint_name: str
        :param job_config: **参数解释**：作业配置参数，用于指定Spark作业的类型和执行参数。根据作业类型自动选择对应的参数结构：spark_jar_job对应SparkJarParameter，spark_python_job对应SparkPyParameter，spark_sql_scripting_job对应SparkSqlScriptParameter。 **约束限制**：不涉及。
        :type job_config: :class:`huaweicloudsdkaidatalakejobserver.v2.object`
        :param catalog_name: **参数解释**：Catalog名称，用于指定作业使用的数据目录。 **约束限制**：不涉及。 **取值范围**：长度不超过128个字符。 **默认取值**：不涉及。
        :type catalog_name: str
        :param job_agency: **参数解释**：自定义委托名称，用于作业操作OBS对象、转储日志、访问DLI元数据等。 **约束限制**：不涉及。 **取值范围**：长度为1~64个字符。 **默认取值**：不涉及。
        :type job_agency: str
        :param resource_config: 
        :type resource_config: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkResourceConfig`
        :param spark_config: **参数解释**：用户自定义Spark参数配置，用于优化Spark作业性能。 **约束限制**：最多支持100个参数。
        :type spark_config: dict(str, str)
        :param image: 
        :type image: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkJobImageConfig`
        :param logging_config: 
        :type logging_config: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkLoggingConfig`
        :param restore_strategy: 
        :type restore_strategy: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkRestoreStrategy`
        :param labels: **参数解释**：作业标签列表，用于标识和分类作业。 **约束限制**：标签数量不能超过16条。
        :type labels: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkJobLabel`]
        :param description: **参数解释**：Spark作业描述信息，用于说明作业用途。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符。 **默认取值**：不涉及。
        :type description: str
        """
        
        

        self._name = None
        self._endpoint_name = None
        self._job_config = None
        self._catalog_name = None
        self._job_agency = None
        self._resource_config = None
        self._spark_config = None
        self._image = None
        self._logging_config = None
        self._restore_strategy = None
        self._labels = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.endpoint_name = endpoint_name
        self.job_config = job_config
        if catalog_name is not None:
            self.catalog_name = catalog_name
        if job_agency is not None:
            self.job_agency = job_agency
        if resource_config is not None:
            self.resource_config = resource_config
        if spark_config is not None:
            self.spark_config = spark_config
        if image is not None:
            self.image = image
        if logging_config is not None:
            self.logging_config = logging_config
        if restore_strategy is not None:
            self.restore_strategy = restore_strategy
        if labels is not None:
            self.labels = labels
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this RunSparkJobRequestBody.

        **参数解释**：Spark作业名称，用于标识作业。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符。 **默认取值**：不涉及。

        :return: The name of this RunSparkJobRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RunSparkJobRequestBody.

        **参数解释**：Spark作业名称，用于标识作业。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符。 **默认取值**：不涉及。

        :param name: The name of this RunSparkJobRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this RunSparkJobRequestBody.

        **参数解释**：端点名称，用于指定Spark作业执行环境。 **约束限制**：不涉及。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。 **默认取值**：不涉及。

        :return: The endpoint_name of this RunSparkJobRequestBody.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this RunSparkJobRequestBody.

        **参数解释**：端点名称，用于指定Spark作业执行环境。 **约束限制**：不涉及。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。 **默认取值**：不涉及。

        :param endpoint_name: The endpoint_name of this RunSparkJobRequestBody.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def job_config(self):
        r"""Gets the job_config of this RunSparkJobRequestBody.

        **参数解释**：作业配置参数，用于指定Spark作业的类型和执行参数。根据作业类型自动选择对应的参数结构：spark_jar_job对应SparkJarParameter，spark_python_job对应SparkPyParameter，spark_sql_scripting_job对应SparkSqlScriptParameter。 **约束限制**：不涉及。

        :return: The job_config of this RunSparkJobRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.object`
        """
        return self._job_config

    @job_config.setter
    def job_config(self, job_config):
        r"""Sets the job_config of this RunSparkJobRequestBody.

        **参数解释**：作业配置参数，用于指定Spark作业的类型和执行参数。根据作业类型自动选择对应的参数结构：spark_jar_job对应SparkJarParameter，spark_python_job对应SparkPyParameter，spark_sql_scripting_job对应SparkSqlScriptParameter。 **约束限制**：不涉及。

        :param job_config: The job_config of this RunSparkJobRequestBody.
        :type job_config: :class:`huaweicloudsdkaidatalakejobserver.v2.object`
        """
        self._job_config = job_config

    @property
    def catalog_name(self):
        r"""Gets the catalog_name of this RunSparkJobRequestBody.

        **参数解释**：Catalog名称，用于指定作业使用的数据目录。 **约束限制**：不涉及。 **取值范围**：长度不超过128个字符。 **默认取值**：不涉及。

        :return: The catalog_name of this RunSparkJobRequestBody.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this RunSparkJobRequestBody.

        **参数解释**：Catalog名称，用于指定作业使用的数据目录。 **约束限制**：不涉及。 **取值范围**：长度不超过128个字符。 **默认取值**：不涉及。

        :param catalog_name: The catalog_name of this RunSparkJobRequestBody.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def job_agency(self):
        r"""Gets the job_agency of this RunSparkJobRequestBody.

        **参数解释**：自定义委托名称，用于作业操作OBS对象、转储日志、访问DLI元数据等。 **约束限制**：不涉及。 **取值范围**：长度为1~64个字符。 **默认取值**：不涉及。

        :return: The job_agency of this RunSparkJobRequestBody.
        :rtype: str
        """
        return self._job_agency

    @job_agency.setter
    def job_agency(self, job_agency):
        r"""Sets the job_agency of this RunSparkJobRequestBody.

        **参数解释**：自定义委托名称，用于作业操作OBS对象、转储日志、访问DLI元数据等。 **约束限制**：不涉及。 **取值范围**：长度为1~64个字符。 **默认取值**：不涉及。

        :param job_agency: The job_agency of this RunSparkJobRequestBody.
        :type job_agency: str
        """
        self._job_agency = job_agency

    @property
    def resource_config(self):
        r"""Gets the resource_config of this RunSparkJobRequestBody.

        :return: The resource_config of this RunSparkJobRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkResourceConfig`
        """
        return self._resource_config

    @resource_config.setter
    def resource_config(self, resource_config):
        r"""Sets the resource_config of this RunSparkJobRequestBody.

        :param resource_config: The resource_config of this RunSparkJobRequestBody.
        :type resource_config: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkResourceConfig`
        """
        self._resource_config = resource_config

    @property
    def spark_config(self):
        r"""Gets the spark_config of this RunSparkJobRequestBody.

        **参数解释**：用户自定义Spark参数配置，用于优化Spark作业性能。 **约束限制**：最多支持100个参数。

        :return: The spark_config of this RunSparkJobRequestBody.
        :rtype: dict(str, str)
        """
        return self._spark_config

    @spark_config.setter
    def spark_config(self, spark_config):
        r"""Sets the spark_config of this RunSparkJobRequestBody.

        **参数解释**：用户自定义Spark参数配置，用于优化Spark作业性能。 **约束限制**：最多支持100个参数。

        :param spark_config: The spark_config of this RunSparkJobRequestBody.
        :type spark_config: dict(str, str)
        """
        self._spark_config = spark_config

    @property
    def image(self):
        r"""Gets the image of this RunSparkJobRequestBody.

        :return: The image of this RunSparkJobRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkJobImageConfig`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this RunSparkJobRequestBody.

        :param image: The image of this RunSparkJobRequestBody.
        :type image: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkJobImageConfig`
        """
        self._image = image

    @property
    def logging_config(self):
        r"""Gets the logging_config of this RunSparkJobRequestBody.

        :return: The logging_config of this RunSparkJobRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkLoggingConfig`
        """
        return self._logging_config

    @logging_config.setter
    def logging_config(self, logging_config):
        r"""Sets the logging_config of this RunSparkJobRequestBody.

        :param logging_config: The logging_config of this RunSparkJobRequestBody.
        :type logging_config: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkLoggingConfig`
        """
        self._logging_config = logging_config

    @property
    def restore_strategy(self):
        r"""Gets the restore_strategy of this RunSparkJobRequestBody.

        :return: The restore_strategy of this RunSparkJobRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkRestoreStrategy`
        """
        return self._restore_strategy

    @restore_strategy.setter
    def restore_strategy(self, restore_strategy):
        r"""Sets the restore_strategy of this RunSparkJobRequestBody.

        :param restore_strategy: The restore_strategy of this RunSparkJobRequestBody.
        :type restore_strategy: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkRestoreStrategy`
        """
        self._restore_strategy = restore_strategy

    @property
    def labels(self):
        r"""Gets the labels of this RunSparkJobRequestBody.

        **参数解释**：作业标签列表，用于标识和分类作业。 **约束限制**：标签数量不能超过16条。

        :return: The labels of this RunSparkJobRequestBody.
        :rtype: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkJobLabel`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this RunSparkJobRequestBody.

        **参数解释**：作业标签列表，用于标识和分类作业。 **约束限制**：标签数量不能超过16条。

        :param labels: The labels of this RunSparkJobRequestBody.
        :type labels: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkJobLabel`]
        """
        self._labels = labels

    @property
    def description(self):
        r"""Gets the description of this RunSparkJobRequestBody.

        **参数解释**：Spark作业描述信息，用于说明作业用途。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符。 **默认取值**：不涉及。

        :return: The description of this RunSparkJobRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RunSparkJobRequestBody.

        **参数解释**：Spark作业描述信息，用于说明作业用途。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符。 **默认取值**：不涉及。

        :param description: The description of this RunSparkJobRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, RunSparkJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
