# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkSqlResponse(SdkResponse):

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
        'client_token': 'str',
        'catalog_context': 'SparkSqlCatalogContextResponse',
        'statement': 'str',
        'parameters': 'list[SparkSqlParameter]',
        'statement_type': 'str',
        'statement_id': 'str',
        'state': 'str',
        'error': 'SparkSqlErrorDto',
        'spark_config': 'dict(str, str)',
        'image': 'ShowSparkSqlImageConfigResponse',
        'result': 'SparkSqlResultResponse',
        'metric_statistics': 'SparkSqlMetricStatisticsResponse',
        'timeout': 'SparkSqlTimeout',
        'log_url': 'str',
        'create_time': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'create_user': 'SparkCreateUser',
        'labels': 'list[SparkSqlLabelRes]'
    }

    attribute_map = {
        'endpoint_name': 'endpoint_name',
        'client_token': 'client_token',
        'catalog_context': 'catalog_context',
        'statement': 'statement',
        'parameters': 'parameters',
        'statement_type': 'statement_type',
        'statement_id': 'statement_id',
        'state': 'state',
        'error': 'error',
        'spark_config': 'spark_config',
        'image': 'image',
        'result': 'result',
        'metric_statistics': 'metric_statistics',
        'timeout': 'timeout',
        'log_url': 'log_url',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'create_user': 'create_user',
        'labels': 'labels'
    }

    def __init__(self, endpoint_name=None, client_token=None, catalog_context=None, statement=None, parameters=None, statement_type=None, statement_id=None, state=None, error=None, spark_config=None, image=None, result=None, metric_statistics=None, timeout=None, log_url=None, create_time=None, start_time=None, end_time=None, create_user=None, labels=None):
        r"""ShowSparkSqlResponse

        The model defined in huaweicloud sdk

        :param endpoint_name: **参数解释**：端点名称，用于指定SparkSql执行环境。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。
        :type endpoint_name: str
        :param client_token: **参数解释**：SparkSql作业事务ID，用于防止重复提交。 **取值范围**：采用UUID格式，长度为36个字符，例如：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。
        :type client_token: str
        :param catalog_context: 
        :type catalog_context: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlCatalogContextResponse`
        :param statement: **参数解释**：用户SQL语句，用于执行数据查询、数据操作等任务。 **取值范围**：长度不超过500000个字符。
        :type statement: str
        :param parameters: **参数解释**：用户SQL内容的占位符参数列表，用于动态替换SQL中的参数。数组中的每个元素为SparkSqlParameter对象，包含占位符的键和值。
        :type parameters: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlParameter`]
        :param statement_type: **参数解释**：SQL作业类型，用于标识作业的类型。 **取值范围**： - DDL：创建修改删除元数据类型的作业、DESC/SHOW等语句。 - DCL：权限授权与回收类型的作业。 - DQL：查询语句SELECT。 - DML：向表追加、删除、更新新数据类型的作业。
        :type statement_type: str
        :param statement_id: **参数解释**：SparkSql作业的ID，用于唯一标识一次SparkSql作业执行。 **取值范围**：采用UUID格式，长度为36个字符，例如：80ceaaff-3cfc-4162-a56f-70031ea4fa91。
        :type statement_id: str
        :param state: **参数解释**：SparkSql作业的状态，用于标识作业的执行状态。 **取值范围**： - QUEUED：排队中。 - RUNNING：运行中。 - CANCELING：取消中。 - CANCELED：已取消。 - FAILED：运行失败。 - QUEUED_TIMEOUT：排队超时。 - RUNNING_TIMEOUT：运行超时。 - SUCCEED：运行成功。
        :type state: str
        :param error: 
        :type error: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlErrorDto`
        :param spark_config: **参数解释**：用户自定义Spark参数配置，用于配置作业执行时的Spark参数。
        :type spark_config: dict(str, str)
        :param image: 
        :type image: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkSqlImageConfigResponse`
        :param result: 
        :type result: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlResultResponse`
        :param metric_statistics: 
        :type metric_statistics: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlMetricStatisticsResponse`
        :param timeout: 
        :type timeout: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlTimeout`
        :param log_url: **参数解释**：日志OBS归档路径，用于存储作业执行的日志信息。包括：result（sql运行结果）、metric_statistics（SQL运行指标统计）、timeout（sql超时时间）、error（错误信息）。 **取值范围**：采用OBS路径格式，例如：obs://bucket/aidatalake/workspace_xxx/spark/endpoint_xxx/jobs/logs/2026_04_27/{job_id}/spark.log。
        :type log_url: str
        :param create_time: **参数解释**：作业创建时间，用于标识作业的创建时间戳。 **取值范围**：大于等于0的整数，单位为毫秒。
        :type create_time: int
        :param start_time: **参数解释**：作业开始运行时间，用于标识作业开始执行的时间戳。 **取值范围**：大于等于0的整数，单位为毫秒。
        :type start_time: int
        :param end_time: **参数解释**：作业结束时间，用于标识作业完成执行的时间戳。 **取值范围**：大于等于0的整数，单位为毫秒。
        :type end_time: int
        :param create_user: 
        :type create_user: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkCreateUser`
        :param labels: **参数解释**：作业标签列表，用于标识和分类作业。数组中的每个元素为SparkSqlLabelRes对象，包含标签的键和值。
        :type labels: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlLabelRes`]
        """
        
        super().__init__()

        self._endpoint_name = None
        self._client_token = None
        self._catalog_context = None
        self._statement = None
        self._parameters = None
        self._statement_type = None
        self._statement_id = None
        self._state = None
        self._error = None
        self._spark_config = None
        self._image = None
        self._result = None
        self._metric_statistics = None
        self._timeout = None
        self._log_url = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._create_user = None
        self._labels = None
        self.discriminator = None

        if endpoint_name is not None:
            self.endpoint_name = endpoint_name
        if client_token is not None:
            self.client_token = client_token
        if catalog_context is not None:
            self.catalog_context = catalog_context
        if statement is not None:
            self.statement = statement
        if parameters is not None:
            self.parameters = parameters
        if statement_type is not None:
            self.statement_type = statement_type
        if statement_id is not None:
            self.statement_id = statement_id
        if state is not None:
            self.state = state
        if error is not None:
            self.error = error
        if spark_config is not None:
            self.spark_config = spark_config
        if image is not None:
            self.image = image
        if result is not None:
            self.result = result
        if metric_statistics is not None:
            self.metric_statistics = metric_statistics
        if timeout is not None:
            self.timeout = timeout
        if log_url is not None:
            self.log_url = log_url
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if create_user is not None:
            self.create_user = create_user
        if labels is not None:
            self.labels = labels

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this ShowSparkSqlResponse.

        **参数解释**：端点名称，用于指定SparkSql执行环境。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。

        :return: The endpoint_name of this ShowSparkSqlResponse.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this ShowSparkSqlResponse.

        **参数解释**：端点名称，用于指定SparkSql执行环境。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。

        :param endpoint_name: The endpoint_name of this ShowSparkSqlResponse.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def client_token(self):
        r"""Gets the client_token of this ShowSparkSqlResponse.

        **参数解释**：SparkSql作业事务ID，用于防止重复提交。 **取值范围**：采用UUID格式，长度为36个字符，例如：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。

        :return: The client_token of this ShowSparkSqlResponse.
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        r"""Sets the client_token of this ShowSparkSqlResponse.

        **参数解释**：SparkSql作业事务ID，用于防止重复提交。 **取值范围**：采用UUID格式，长度为36个字符，例如：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。

        :param client_token: The client_token of this ShowSparkSqlResponse.
        :type client_token: str
        """
        self._client_token = client_token

    @property
    def catalog_context(self):
        r"""Gets the catalog_context of this ShowSparkSqlResponse.

        :return: The catalog_context of this ShowSparkSqlResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlCatalogContextResponse`
        """
        return self._catalog_context

    @catalog_context.setter
    def catalog_context(self, catalog_context):
        r"""Sets the catalog_context of this ShowSparkSqlResponse.

        :param catalog_context: The catalog_context of this ShowSparkSqlResponse.
        :type catalog_context: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlCatalogContextResponse`
        """
        self._catalog_context = catalog_context

    @property
    def statement(self):
        r"""Gets the statement of this ShowSparkSqlResponse.

        **参数解释**：用户SQL语句，用于执行数据查询、数据操作等任务。 **取值范围**：长度不超过500000个字符。

        :return: The statement of this ShowSparkSqlResponse.
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        r"""Sets the statement of this ShowSparkSqlResponse.

        **参数解释**：用户SQL语句，用于执行数据查询、数据操作等任务。 **取值范围**：长度不超过500000个字符。

        :param statement: The statement of this ShowSparkSqlResponse.
        :type statement: str
        """
        self._statement = statement

    @property
    def parameters(self):
        r"""Gets the parameters of this ShowSparkSqlResponse.

        **参数解释**：用户SQL内容的占位符参数列表，用于动态替换SQL中的参数。数组中的每个元素为SparkSqlParameter对象，包含占位符的键和值。

        :return: The parameters of this ShowSparkSqlResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlParameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ShowSparkSqlResponse.

        **参数解释**：用户SQL内容的占位符参数列表，用于动态替换SQL中的参数。数组中的每个元素为SparkSqlParameter对象，包含占位符的键和值。

        :param parameters: The parameters of this ShowSparkSqlResponse.
        :type parameters: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlParameter`]
        """
        self._parameters = parameters

    @property
    def statement_type(self):
        r"""Gets the statement_type of this ShowSparkSqlResponse.

        **参数解释**：SQL作业类型，用于标识作业的类型。 **取值范围**： - DDL：创建修改删除元数据类型的作业、DESC/SHOW等语句。 - DCL：权限授权与回收类型的作业。 - DQL：查询语句SELECT。 - DML：向表追加、删除、更新新数据类型的作业。

        :return: The statement_type of this ShowSparkSqlResponse.
        :rtype: str
        """
        return self._statement_type

    @statement_type.setter
    def statement_type(self, statement_type):
        r"""Sets the statement_type of this ShowSparkSqlResponse.

        **参数解释**：SQL作业类型，用于标识作业的类型。 **取值范围**： - DDL：创建修改删除元数据类型的作业、DESC/SHOW等语句。 - DCL：权限授权与回收类型的作业。 - DQL：查询语句SELECT。 - DML：向表追加、删除、更新新数据类型的作业。

        :param statement_type: The statement_type of this ShowSparkSqlResponse.
        :type statement_type: str
        """
        self._statement_type = statement_type

    @property
    def statement_id(self):
        r"""Gets the statement_id of this ShowSparkSqlResponse.

        **参数解释**：SparkSql作业的ID，用于唯一标识一次SparkSql作业执行。 **取值范围**：采用UUID格式，长度为36个字符，例如：80ceaaff-3cfc-4162-a56f-70031ea4fa91。

        :return: The statement_id of this ShowSparkSqlResponse.
        :rtype: str
        """
        return self._statement_id

    @statement_id.setter
    def statement_id(self, statement_id):
        r"""Sets the statement_id of this ShowSparkSqlResponse.

        **参数解释**：SparkSql作业的ID，用于唯一标识一次SparkSql作业执行。 **取值范围**：采用UUID格式，长度为36个字符，例如：80ceaaff-3cfc-4162-a56f-70031ea4fa91。

        :param statement_id: The statement_id of this ShowSparkSqlResponse.
        :type statement_id: str
        """
        self._statement_id = statement_id

    @property
    def state(self):
        r"""Gets the state of this ShowSparkSqlResponse.

        **参数解释**：SparkSql作业的状态，用于标识作业的执行状态。 **取值范围**： - QUEUED：排队中。 - RUNNING：运行中。 - CANCELING：取消中。 - CANCELED：已取消。 - FAILED：运行失败。 - QUEUED_TIMEOUT：排队超时。 - RUNNING_TIMEOUT：运行超时。 - SUCCEED：运行成功。

        :return: The state of this ShowSparkSqlResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowSparkSqlResponse.

        **参数解释**：SparkSql作业的状态，用于标识作业的执行状态。 **取值范围**： - QUEUED：排队中。 - RUNNING：运行中。 - CANCELING：取消中。 - CANCELED：已取消。 - FAILED：运行失败。 - QUEUED_TIMEOUT：排队超时。 - RUNNING_TIMEOUT：运行超时。 - SUCCEED：运行成功。

        :param state: The state of this ShowSparkSqlResponse.
        :type state: str
        """
        self._state = state

    @property
    def error(self):
        r"""Gets the error of this ShowSparkSqlResponse.

        :return: The error of this ShowSparkSqlResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlErrorDto`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this ShowSparkSqlResponse.

        :param error: The error of this ShowSparkSqlResponse.
        :type error: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlErrorDto`
        """
        self._error = error

    @property
    def spark_config(self):
        r"""Gets the spark_config of this ShowSparkSqlResponse.

        **参数解释**：用户自定义Spark参数配置，用于配置作业执行时的Spark参数。

        :return: The spark_config of this ShowSparkSqlResponse.
        :rtype: dict(str, str)
        """
        return self._spark_config

    @spark_config.setter
    def spark_config(self, spark_config):
        r"""Sets the spark_config of this ShowSparkSqlResponse.

        **参数解释**：用户自定义Spark参数配置，用于配置作业执行时的Spark参数。

        :param spark_config: The spark_config of this ShowSparkSqlResponse.
        :type spark_config: dict(str, str)
        """
        self._spark_config = spark_config

    @property
    def image(self):
        r"""Gets the image of this ShowSparkSqlResponse.

        :return: The image of this ShowSparkSqlResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkSqlImageConfigResponse`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this ShowSparkSqlResponse.

        :param image: The image of this ShowSparkSqlResponse.
        :type image: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkSqlImageConfigResponse`
        """
        self._image = image

    @property
    def result(self):
        r"""Gets the result of this ShowSparkSqlResponse.

        :return: The result of this ShowSparkSqlResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlResultResponse`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowSparkSqlResponse.

        :param result: The result of this ShowSparkSqlResponse.
        :type result: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlResultResponse`
        """
        self._result = result

    @property
    def metric_statistics(self):
        r"""Gets the metric_statistics of this ShowSparkSqlResponse.

        :return: The metric_statistics of this ShowSparkSqlResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlMetricStatisticsResponse`
        """
        return self._metric_statistics

    @metric_statistics.setter
    def metric_statistics(self, metric_statistics):
        r"""Sets the metric_statistics of this ShowSparkSqlResponse.

        :param metric_statistics: The metric_statistics of this ShowSparkSqlResponse.
        :type metric_statistics: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlMetricStatisticsResponse`
        """
        self._metric_statistics = metric_statistics

    @property
    def timeout(self):
        r"""Gets the timeout of this ShowSparkSqlResponse.

        :return: The timeout of this ShowSparkSqlResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlTimeout`
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this ShowSparkSqlResponse.

        :param timeout: The timeout of this ShowSparkSqlResponse.
        :type timeout: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlTimeout`
        """
        self._timeout = timeout

    @property
    def log_url(self):
        r"""Gets the log_url of this ShowSparkSqlResponse.

        **参数解释**：日志OBS归档路径，用于存储作业执行的日志信息。包括：result（sql运行结果）、metric_statistics（SQL运行指标统计）、timeout（sql超时时间）、error（错误信息）。 **取值范围**：采用OBS路径格式，例如：obs://bucket/aidatalake/workspace_xxx/spark/endpoint_xxx/jobs/logs/2026_04_27/{job_id}/spark.log。

        :return: The log_url of this ShowSparkSqlResponse.
        :rtype: str
        """
        return self._log_url

    @log_url.setter
    def log_url(self, log_url):
        r"""Sets the log_url of this ShowSparkSqlResponse.

        **参数解释**：日志OBS归档路径，用于存储作业执行的日志信息。包括：result（sql运行结果）、metric_statistics（SQL运行指标统计）、timeout（sql超时时间）、error（错误信息）。 **取值范围**：采用OBS路径格式，例如：obs://bucket/aidatalake/workspace_xxx/spark/endpoint_xxx/jobs/logs/2026_04_27/{job_id}/spark.log。

        :param log_url: The log_url of this ShowSparkSqlResponse.
        :type log_url: str
        """
        self._log_url = log_url

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowSparkSqlResponse.

        **参数解释**：作业创建时间，用于标识作业的创建时间戳。 **取值范围**：大于等于0的整数，单位为毫秒。

        :return: The create_time of this ShowSparkSqlResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowSparkSqlResponse.

        **参数解释**：作业创建时间，用于标识作业的创建时间戳。 **取值范围**：大于等于0的整数，单位为毫秒。

        :param create_time: The create_time of this ShowSparkSqlResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowSparkSqlResponse.

        **参数解释**：作业开始运行时间，用于标识作业开始执行的时间戳。 **取值范围**：大于等于0的整数，单位为毫秒。

        :return: The start_time of this ShowSparkSqlResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowSparkSqlResponse.

        **参数解释**：作业开始运行时间，用于标识作业开始执行的时间戳。 **取值范围**：大于等于0的整数，单位为毫秒。

        :param start_time: The start_time of this ShowSparkSqlResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowSparkSqlResponse.

        **参数解释**：作业结束时间，用于标识作业完成执行的时间戳。 **取值范围**：大于等于0的整数，单位为毫秒。

        :return: The end_time of this ShowSparkSqlResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowSparkSqlResponse.

        **参数解释**：作业结束时间，用于标识作业完成执行的时间戳。 **取值范围**：大于等于0的整数，单位为毫秒。

        :param end_time: The end_time of this ShowSparkSqlResponse.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def create_user(self):
        r"""Gets the create_user of this ShowSparkSqlResponse.

        :return: The create_user of this ShowSparkSqlResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkCreateUser`
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ShowSparkSqlResponse.

        :param create_user: The create_user of this ShowSparkSqlResponse.
        :type create_user: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkCreateUser`
        """
        self._create_user = create_user

    @property
    def labels(self):
        r"""Gets the labels of this ShowSparkSqlResponse.

        **参数解释**：作业标签列表，用于标识和分类作业。数组中的每个元素为SparkSqlLabelRes对象，包含标签的键和值。

        :return: The labels of this ShowSparkSqlResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlLabelRes`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ShowSparkSqlResponse.

        **参数解释**：作业标签列表，用于标识和分类作业。数组中的每个元素为SparkSqlLabelRes对象，包含标签的键和值。

        :param labels: The labels of this ShowSparkSqlResponse.
        :type labels: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlLabelRes`]
        """
        self._labels = labels

    def to_dict(self):
        import warnings
        warnings.warn("ShowSparkSqlResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowSparkSqlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
