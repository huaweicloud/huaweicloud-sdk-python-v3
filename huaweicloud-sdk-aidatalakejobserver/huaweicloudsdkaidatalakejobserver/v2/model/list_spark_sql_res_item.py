# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSparkSqlResItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'statement_id': 'str',
        'client_token': 'str',
        'endpoint_name': 'str',
        'catalog_context': 'SparkSqlCatalogContextResponse',
        'statement': 'str',
        'parameters': 'list[SparkSqlParameter]',
        'state': 'str',
        'statement_type': 'str',
        'error': 'SparkSqlErrorDto',
        'result': 'SparkSqlResultResponse',
        'metric_statistics': 'SparkSqlMetricStatisticsResponse',
        'log_url': 'str',
        'create_time': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'create_user': 'SparkCreateUser'
    }

    attribute_map = {
        'statement_id': 'statement_id',
        'client_token': 'client_token',
        'endpoint_name': 'endpoint_name',
        'catalog_context': 'catalog_context',
        'statement': 'statement',
        'parameters': 'parameters',
        'state': 'state',
        'statement_type': 'statement_type',
        'error': 'error',
        'result': 'result',
        'metric_statistics': 'metric_statistics',
        'log_url': 'log_url',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'create_user': 'create_user'
    }

    def __init__(self, statement_id=None, client_token=None, endpoint_name=None, catalog_context=None, statement=None, parameters=None, state=None, statement_type=None, error=None, result=None, metric_statistics=None, log_url=None, create_time=None, start_time=None, end_time=None, create_user=None):
        r"""ListSparkSqlResItem

        The model defined in huaweicloud sdk

        :param statement_id: **参数解释**：SparkSql作业的ID，用于唯一标识一次SparkSql作业执行。 **取值范围**：采用UUID格式，长度为36个字符，例如：80ceaaff-3cfc-4162-a56f-70031ea4fa91。
        :type statement_id: str
        :param client_token: **参数解释**：SparkSql作业事务ID，用于防止重复提交。 **取值范围**：采用UUID格式，长度为36个字符，例如：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。
        :type client_token: str
        :param endpoint_name: **参数解释**：端点名称，用于指定SparkSql执行环境。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。
        :type endpoint_name: str
        :param catalog_context: 
        :type catalog_context: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlCatalogContextResponse`
        :param statement: **参数解释**：用户SQL语句，用于执行数据查询、数据操作等任务。 **取值范围**：长度不超过500000个字符。
        :type statement: str
        :param parameters: **参数解释**：用户SQL内容的占位符参数列表，用于动态替换SQL中的参数。
        :type parameters: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlParameter`]
        :param state: **参数解释**：SparkSql作业的状态，用于标识作业的执行状态。 **取值范围**： - QUEUED：排队中。 - RUNNING：运行中。 - CANCELING：取消中。 - CANCELED：已取消。 - FAILED：运行失败。 - QUEUED_TIMEOUT：排队超时。 - RUNNING_TIMEOUT：运行超时。 - SUCCEED：运行成功。
        :type state: str
        :param statement_type: **参数解释**：SQL作业类型，用于标识作业的类型。 **取值范围**： - DDL：创建修改删除元数据类型的作业、DESC/SHOW等语句。 - DCL：权限授权与回收类型的作业。 - DQL：查询语句SELECT。 - DML：向表追加、删除、更新新数据类型的作业。
        :type statement_type: str
        :param error: 
        :type error: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlErrorDto`
        :param result: 
        :type result: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlResultResponse`
        :param metric_statistics: 
        :type metric_statistics: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlMetricStatisticsResponse`
        :param log_url: **参数解释**：日志OBS归档路径，用于存储作业执行日志。 **取值范围**：采用OBS路径格式，例如：obs://bucket/aidatalake/workspace_xxx/spark/endpoint_xxx/jobs/logs/2026_04_27/sql-engine-{statement_id}/spark.log。
        :type log_url: str
        :param create_time: **参数解释**：作业创建时间，采用unix时间戳格式。 **取值范围**：单位为毫秒。
        :type create_time: int
        :param start_time: **参数解释**：作业开始运行时间，采用unix时间戳格式。 **取值范围**：单位为毫秒。
        :type start_time: int
        :param end_time: **参数解释**：作业结束时间，采用unix时间戳格式。 **取值范围**：单位为毫秒。
        :type end_time: int
        :param create_user: 
        :type create_user: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkCreateUser`
        """
        
        

        self._statement_id = None
        self._client_token = None
        self._endpoint_name = None
        self._catalog_context = None
        self._statement = None
        self._parameters = None
        self._state = None
        self._statement_type = None
        self._error = None
        self._result = None
        self._metric_statistics = None
        self._log_url = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._create_user = None
        self.discriminator = None

        self.statement_id = statement_id
        if client_token is not None:
            self.client_token = client_token
        self.endpoint_name = endpoint_name
        self.catalog_context = catalog_context
        self.statement = statement
        if parameters is not None:
            self.parameters = parameters
        self.state = state
        self.statement_type = statement_type
        if error is not None:
            self.error = error
        if result is not None:
            self.result = result
        if metric_statistics is not None:
            self.metric_statistics = metric_statistics
        if log_url is not None:
            self.log_url = log_url
        self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.create_user = create_user

    @property
    def statement_id(self):
        r"""Gets the statement_id of this ListSparkSqlResItem.

        **参数解释**：SparkSql作业的ID，用于唯一标识一次SparkSql作业执行。 **取值范围**：采用UUID格式，长度为36个字符，例如：80ceaaff-3cfc-4162-a56f-70031ea4fa91。

        :return: The statement_id of this ListSparkSqlResItem.
        :rtype: str
        """
        return self._statement_id

    @statement_id.setter
    def statement_id(self, statement_id):
        r"""Sets the statement_id of this ListSparkSqlResItem.

        **参数解释**：SparkSql作业的ID，用于唯一标识一次SparkSql作业执行。 **取值范围**：采用UUID格式，长度为36个字符，例如：80ceaaff-3cfc-4162-a56f-70031ea4fa91。

        :param statement_id: The statement_id of this ListSparkSqlResItem.
        :type statement_id: str
        """
        self._statement_id = statement_id

    @property
    def client_token(self):
        r"""Gets the client_token of this ListSparkSqlResItem.

        **参数解释**：SparkSql作业事务ID，用于防止重复提交。 **取值范围**：采用UUID格式，长度为36个字符，例如：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。

        :return: The client_token of this ListSparkSqlResItem.
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        r"""Sets the client_token of this ListSparkSqlResItem.

        **参数解释**：SparkSql作业事务ID，用于防止重复提交。 **取值范围**：采用UUID格式，长度为36个字符，例如：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。

        :param client_token: The client_token of this ListSparkSqlResItem.
        :type client_token: str
        """
        self._client_token = client_token

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this ListSparkSqlResItem.

        **参数解释**：端点名称，用于指定SparkSql执行环境。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。

        :return: The endpoint_name of this ListSparkSqlResItem.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this ListSparkSqlResItem.

        **参数解释**：端点名称，用于指定SparkSql执行环境。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。

        :param endpoint_name: The endpoint_name of this ListSparkSqlResItem.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def catalog_context(self):
        r"""Gets the catalog_context of this ListSparkSqlResItem.

        :return: The catalog_context of this ListSparkSqlResItem.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlCatalogContextResponse`
        """
        return self._catalog_context

    @catalog_context.setter
    def catalog_context(self, catalog_context):
        r"""Sets the catalog_context of this ListSparkSqlResItem.

        :param catalog_context: The catalog_context of this ListSparkSqlResItem.
        :type catalog_context: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlCatalogContextResponse`
        """
        self._catalog_context = catalog_context

    @property
    def statement(self):
        r"""Gets the statement of this ListSparkSqlResItem.

        **参数解释**：用户SQL语句，用于执行数据查询、数据操作等任务。 **取值范围**：长度不超过500000个字符。

        :return: The statement of this ListSparkSqlResItem.
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        r"""Sets the statement of this ListSparkSqlResItem.

        **参数解释**：用户SQL语句，用于执行数据查询、数据操作等任务。 **取值范围**：长度不超过500000个字符。

        :param statement: The statement of this ListSparkSqlResItem.
        :type statement: str
        """
        self._statement = statement

    @property
    def parameters(self):
        r"""Gets the parameters of this ListSparkSqlResItem.

        **参数解释**：用户SQL内容的占位符参数列表，用于动态替换SQL中的参数。

        :return: The parameters of this ListSparkSqlResItem.
        :rtype: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlParameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ListSparkSqlResItem.

        **参数解释**：用户SQL内容的占位符参数列表，用于动态替换SQL中的参数。

        :param parameters: The parameters of this ListSparkSqlResItem.
        :type parameters: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlParameter`]
        """
        self._parameters = parameters

    @property
    def state(self):
        r"""Gets the state of this ListSparkSqlResItem.

        **参数解释**：SparkSql作业的状态，用于标识作业的执行状态。 **取值范围**： - QUEUED：排队中。 - RUNNING：运行中。 - CANCELING：取消中。 - CANCELED：已取消。 - FAILED：运行失败。 - QUEUED_TIMEOUT：排队超时。 - RUNNING_TIMEOUT：运行超时。 - SUCCEED：运行成功。

        :return: The state of this ListSparkSqlResItem.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListSparkSqlResItem.

        **参数解释**：SparkSql作业的状态，用于标识作业的执行状态。 **取值范围**： - QUEUED：排队中。 - RUNNING：运行中。 - CANCELING：取消中。 - CANCELED：已取消。 - FAILED：运行失败。 - QUEUED_TIMEOUT：排队超时。 - RUNNING_TIMEOUT：运行超时。 - SUCCEED：运行成功。

        :param state: The state of this ListSparkSqlResItem.
        :type state: str
        """
        self._state = state

    @property
    def statement_type(self):
        r"""Gets the statement_type of this ListSparkSqlResItem.

        **参数解释**：SQL作业类型，用于标识作业的类型。 **取值范围**： - DDL：创建修改删除元数据类型的作业、DESC/SHOW等语句。 - DCL：权限授权与回收类型的作业。 - DQL：查询语句SELECT。 - DML：向表追加、删除、更新新数据类型的作业。

        :return: The statement_type of this ListSparkSqlResItem.
        :rtype: str
        """
        return self._statement_type

    @statement_type.setter
    def statement_type(self, statement_type):
        r"""Sets the statement_type of this ListSparkSqlResItem.

        **参数解释**：SQL作业类型，用于标识作业的类型。 **取值范围**： - DDL：创建修改删除元数据类型的作业、DESC/SHOW等语句。 - DCL：权限授权与回收类型的作业。 - DQL：查询语句SELECT。 - DML：向表追加、删除、更新新数据类型的作业。

        :param statement_type: The statement_type of this ListSparkSqlResItem.
        :type statement_type: str
        """
        self._statement_type = statement_type

    @property
    def error(self):
        r"""Gets the error of this ListSparkSqlResItem.

        :return: The error of this ListSparkSqlResItem.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlErrorDto`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this ListSparkSqlResItem.

        :param error: The error of this ListSparkSqlResItem.
        :type error: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlErrorDto`
        """
        self._error = error

    @property
    def result(self):
        r"""Gets the result of this ListSparkSqlResItem.

        :return: The result of this ListSparkSqlResItem.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlResultResponse`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ListSparkSqlResItem.

        :param result: The result of this ListSparkSqlResItem.
        :type result: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlResultResponse`
        """
        self._result = result

    @property
    def metric_statistics(self):
        r"""Gets the metric_statistics of this ListSparkSqlResItem.

        :return: The metric_statistics of this ListSparkSqlResItem.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlMetricStatisticsResponse`
        """
        return self._metric_statistics

    @metric_statistics.setter
    def metric_statistics(self, metric_statistics):
        r"""Sets the metric_statistics of this ListSparkSqlResItem.

        :param metric_statistics: The metric_statistics of this ListSparkSqlResItem.
        :type metric_statistics: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkSqlMetricStatisticsResponse`
        """
        self._metric_statistics = metric_statistics

    @property
    def log_url(self):
        r"""Gets the log_url of this ListSparkSqlResItem.

        **参数解释**：日志OBS归档路径，用于存储作业执行日志。 **取值范围**：采用OBS路径格式，例如：obs://bucket/aidatalake/workspace_xxx/spark/endpoint_xxx/jobs/logs/2026_04_27/sql-engine-{statement_id}/spark.log。

        :return: The log_url of this ListSparkSqlResItem.
        :rtype: str
        """
        return self._log_url

    @log_url.setter
    def log_url(self, log_url):
        r"""Sets the log_url of this ListSparkSqlResItem.

        **参数解释**：日志OBS归档路径，用于存储作业执行日志。 **取值范围**：采用OBS路径格式，例如：obs://bucket/aidatalake/workspace_xxx/spark/endpoint_xxx/jobs/logs/2026_04_27/sql-engine-{statement_id}/spark.log。

        :param log_url: The log_url of this ListSparkSqlResItem.
        :type log_url: str
        """
        self._log_url = log_url

    @property
    def create_time(self):
        r"""Gets the create_time of this ListSparkSqlResItem.

        **参数解释**：作业创建时间，采用unix时间戳格式。 **取值范围**：单位为毫秒。

        :return: The create_time of this ListSparkSqlResItem.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListSparkSqlResItem.

        **参数解释**：作业创建时间，采用unix时间戳格式。 **取值范围**：单位为毫秒。

        :param create_time: The create_time of this ListSparkSqlResItem.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ListSparkSqlResItem.

        **参数解释**：作业开始运行时间，采用unix时间戳格式。 **取值范围**：单位为毫秒。

        :return: The start_time of this ListSparkSqlResItem.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListSparkSqlResItem.

        **参数解释**：作业开始运行时间，采用unix时间戳格式。 **取值范围**：单位为毫秒。

        :param start_time: The start_time of this ListSparkSqlResItem.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListSparkSqlResItem.

        **参数解释**：作业结束时间，采用unix时间戳格式。 **取值范围**：单位为毫秒。

        :return: The end_time of this ListSparkSqlResItem.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListSparkSqlResItem.

        **参数解释**：作业结束时间，采用unix时间戳格式。 **取值范围**：单位为毫秒。

        :param end_time: The end_time of this ListSparkSqlResItem.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def create_user(self):
        r"""Gets the create_user of this ListSparkSqlResItem.

        :return: The create_user of this ListSparkSqlResItem.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkCreateUser`
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ListSparkSqlResItem.

        :param create_user: The create_user of this ListSparkSqlResItem.
        :type create_user: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkCreateUser`
        """
        self._create_user = create_user

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
        if not isinstance(other, ListSparkSqlResItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
