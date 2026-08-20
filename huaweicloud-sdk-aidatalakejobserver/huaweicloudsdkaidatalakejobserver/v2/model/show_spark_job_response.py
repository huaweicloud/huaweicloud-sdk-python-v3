# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'client_token': 'str',
        'name': 'str',
        'endpoint_name': 'str',
        'catalog_name': 'str',
        'job_agency': 'str',
        'state': 'str',
        'state_message': 'str',
        'job_config': 'object',
        'resource_config': 'ShowSparkResourceConfigResponse',
        'restore_strategy': 'ShowSparkRestoreStrategyResponse',
        'spark_config': 'dict(str, str)',
        'logging_config': 'ShowSparkLoggingConfigResponse',
        'image': 'ShowSparkJobImageConfigResponse',
        'retry_times': 'int',
        'labels': 'list[ShowSparkJobLabelResponse]',
        'create_time': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'create_user': 'SparkCreateUser',
        'log_url': 'str',
        'description': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'client_token': 'client_token',
        'name': 'name',
        'endpoint_name': 'endpoint_name',
        'catalog_name': 'catalog_name',
        'job_agency': 'job_agency',
        'state': 'state',
        'state_message': 'state_message',
        'job_config': 'job_config',
        'resource_config': 'resource_config',
        'restore_strategy': 'restore_strategy',
        'spark_config': 'spark_config',
        'logging_config': 'logging_config',
        'image': 'image',
        'retry_times': 'retry_times',
        'labels': 'labels',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'create_user': 'create_user',
        'log_url': 'log_url',
        'description': 'description'
    }

    def __init__(self, job_id=None, client_token=None, name=None, endpoint_name=None, catalog_name=None, job_agency=None, state=None, state_message=None, job_config=None, resource_config=None, restore_strategy=None, spark_config=None, logging_config=None, image=None, retry_times=None, labels=None, create_time=None, start_time=None, end_time=None, create_user=None, log_url=None, description=None):
        r"""ShowSparkJobResponse

        The model defined in huaweicloud sdk

        :param job_id: **参数解释**：Spark作业ID，用于唯一标识该作业。 **取值范围**：采用UUID格式，长度为36个字符，例如：80ceaaff-3cfc-4162-a56f-70031ea4fa91。
        :type job_id: str
        :param client_token: **参数解释**：Spark作业事务ID，用于防止重复提交。 **取值范围**：采用UUID格式，长度为36个字符，例如：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。
        :type client_token: str
        :param name: **参数解释**：Spark作业名称，用于标识作业。 **取值范围**：长度为1~128个字符。
        :type name: str
        :param endpoint_name: **参数解释**：端点名称，用于指定Spark作业执行环境。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。
        :type endpoint_name: str
        :param catalog_name: **参数解释**：Catalog名称，用于指定作业使用的数据目录。 **取值范围**：长度为1~128个字符。
        :type catalog_name: str
        :param job_agency: **参数解释**：自定义委托的委托名，用于作业操作OBS对象、转储日志、访问DLI元数据等。 **取值范围**：长度为1~64个字符。
        :type job_agency: str
        :param state: **参数解释**：Spark作业状态，用于标识作业当前执行状态。 **取值范围**： - PENDING：启动中。 - QUEUED：排队中。 - RUNNING：运行中。 - CANCELING：取消中。 - CANCELED：已取消。 - FAILED：运行失败。 - QUEUED_TIMEOUT：排队超时。 - RUNNING_TIMEOUT：运行超时。 - SUCCEED：运行成功。
        :type state: str
        :param state_message: **参数解释**：作业状态消息，当作业异常结束时显示相关信息。 **取值范围**：长度为0~512个字符。
        :type state_message: str
        :param job_config: **参数解释**：作业配置信息，包含作业类型、入口参数、依赖包等信息。
        :type job_config: :class:`huaweicloudsdkaidatalakejobserver.v2.object`
        :param resource_config: 
        :type resource_config: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkResourceConfigResponse`
        :param restore_strategy: 
        :type restore_strategy: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkRestoreStrategyResponse`
        :param spark_config: **参数解释**：用户自定义Spark参数配置。 **取值范围**：长度为0~1024个字符。
        :type spark_config: dict(str, str)
        :param logging_config: 
        :type logging_config: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkLoggingConfigResponse`
        :param image: 
        :type image: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkJobImageConfigResponse`
        :param retry_times: **参数解释**：作业重试次数，用于记录作业失败后的重试次数。 **取值范围**：最小值为0。
        :type retry_times: int
        :param labels: **参数解释**：作业标签列表，用于标识和分类作业。
        :type labels: list[:class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkJobLabelResponse`]
        :param create_time: **参数解释**：作业创建时间，用于记录作业提交时间。 **取值范围**：unix时间戳，单位为毫秒。
        :type create_time: int
        :param start_time: **参数解释**：作业开始运行时间，用于记录作业实际开始执行的时间。 **取值范围**：unix时间戳，单位为毫秒。
        :type start_time: int
        :param end_time: **参数解释**：作业结束时间，用于记录作业执行完成的时间。 **取值范围**：unix时间戳，单位为毫秒。
        :type end_time: int
        :param create_user: 
        :type create_user: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkCreateUser`
        :param log_url: **参数解释**：日志归档路径OBS URL，用于查看作业执行日志。 **取值范围**：OBS URL格式，长度为1~1024个字符。
        :type log_url: str
        :param description: **参数解释**：Spark作业描述信息，用于说明作业用途。 **取值范围**：长度为0~512个字符。
        :type description: str
        """
        
        super().__init__()

        self._job_id = None
        self._client_token = None
        self._name = None
        self._endpoint_name = None
        self._catalog_name = None
        self._job_agency = None
        self._state = None
        self._state_message = None
        self._job_config = None
        self._resource_config = None
        self._restore_strategy = None
        self._spark_config = None
        self._logging_config = None
        self._image = None
        self._retry_times = None
        self._labels = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._create_user = None
        self._log_url = None
        self._description = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if client_token is not None:
            self.client_token = client_token
        if name is not None:
            self.name = name
        if endpoint_name is not None:
            self.endpoint_name = endpoint_name
        if catalog_name is not None:
            self.catalog_name = catalog_name
        if job_agency is not None:
            self.job_agency = job_agency
        if state is not None:
            self.state = state
        if state_message is not None:
            self.state_message = state_message
        if job_config is not None:
            self.job_config = job_config
        if resource_config is not None:
            self.resource_config = resource_config
        if restore_strategy is not None:
            self.restore_strategy = restore_strategy
        if spark_config is not None:
            self.spark_config = spark_config
        if logging_config is not None:
            self.logging_config = logging_config
        if image is not None:
            self.image = image
        if retry_times is not None:
            self.retry_times = retry_times
        if labels is not None:
            self.labels = labels
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if create_user is not None:
            self.create_user = create_user
        if log_url is not None:
            self.log_url = log_url
        if description is not None:
            self.description = description

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowSparkJobResponse.

        **参数解释**：Spark作业ID，用于唯一标识该作业。 **取值范围**：采用UUID格式，长度为36个字符，例如：80ceaaff-3cfc-4162-a56f-70031ea4fa91。

        :return: The job_id of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowSparkJobResponse.

        **参数解释**：Spark作业ID，用于唯一标识该作业。 **取值范围**：采用UUID格式，长度为36个字符，例如：80ceaaff-3cfc-4162-a56f-70031ea4fa91。

        :param job_id: The job_id of this ShowSparkJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def client_token(self):
        r"""Gets the client_token of this ShowSparkJobResponse.

        **参数解释**：Spark作业事务ID，用于防止重复提交。 **取值范围**：采用UUID格式，长度为36个字符，例如：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。

        :return: The client_token of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        r"""Sets the client_token of this ShowSparkJobResponse.

        **参数解释**：Spark作业事务ID，用于防止重复提交。 **取值范围**：采用UUID格式，长度为36个字符，例如：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。

        :param client_token: The client_token of this ShowSparkJobResponse.
        :type client_token: str
        """
        self._client_token = client_token

    @property
    def name(self):
        r"""Gets the name of this ShowSparkJobResponse.

        **参数解释**：Spark作业名称，用于标识作业。 **取值范围**：长度为1~128个字符。

        :return: The name of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowSparkJobResponse.

        **参数解释**：Spark作业名称，用于标识作业。 **取值范围**：长度为1~128个字符。

        :param name: The name of this ShowSparkJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this ShowSparkJobResponse.

        **参数解释**：端点名称，用于指定Spark作业执行环境。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。

        :return: The endpoint_name of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this ShowSparkJobResponse.

        **参数解释**：端点名称，用于指定Spark作业执行环境。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。

        :param endpoint_name: The endpoint_name of this ShowSparkJobResponse.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def catalog_name(self):
        r"""Gets the catalog_name of this ShowSparkJobResponse.

        **参数解释**：Catalog名称，用于指定作业使用的数据目录。 **取值范围**：长度为1~128个字符。

        :return: The catalog_name of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this ShowSparkJobResponse.

        **参数解释**：Catalog名称，用于指定作业使用的数据目录。 **取值范围**：长度为1~128个字符。

        :param catalog_name: The catalog_name of this ShowSparkJobResponse.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def job_agency(self):
        r"""Gets the job_agency of this ShowSparkJobResponse.

        **参数解释**：自定义委托的委托名，用于作业操作OBS对象、转储日志、访问DLI元数据等。 **取值范围**：长度为1~64个字符。

        :return: The job_agency of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._job_agency

    @job_agency.setter
    def job_agency(self, job_agency):
        r"""Sets the job_agency of this ShowSparkJobResponse.

        **参数解释**：自定义委托的委托名，用于作业操作OBS对象、转储日志、访问DLI元数据等。 **取值范围**：长度为1~64个字符。

        :param job_agency: The job_agency of this ShowSparkJobResponse.
        :type job_agency: str
        """
        self._job_agency = job_agency

    @property
    def state(self):
        r"""Gets the state of this ShowSparkJobResponse.

        **参数解释**：Spark作业状态，用于标识作业当前执行状态。 **取值范围**： - PENDING：启动中。 - QUEUED：排队中。 - RUNNING：运行中。 - CANCELING：取消中。 - CANCELED：已取消。 - FAILED：运行失败。 - QUEUED_TIMEOUT：排队超时。 - RUNNING_TIMEOUT：运行超时。 - SUCCEED：运行成功。

        :return: The state of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowSparkJobResponse.

        **参数解释**：Spark作业状态，用于标识作业当前执行状态。 **取值范围**： - PENDING：启动中。 - QUEUED：排队中。 - RUNNING：运行中。 - CANCELING：取消中。 - CANCELED：已取消。 - FAILED：运行失败。 - QUEUED_TIMEOUT：排队超时。 - RUNNING_TIMEOUT：运行超时。 - SUCCEED：运行成功。

        :param state: The state of this ShowSparkJobResponse.
        :type state: str
        """
        self._state = state

    @property
    def state_message(self):
        r"""Gets the state_message of this ShowSparkJobResponse.

        **参数解释**：作业状态消息，当作业异常结束时显示相关信息。 **取值范围**：长度为0~512个字符。

        :return: The state_message of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        r"""Sets the state_message of this ShowSparkJobResponse.

        **参数解释**：作业状态消息，当作业异常结束时显示相关信息。 **取值范围**：长度为0~512个字符。

        :param state_message: The state_message of this ShowSparkJobResponse.
        :type state_message: str
        """
        self._state_message = state_message

    @property
    def job_config(self):
        r"""Gets the job_config of this ShowSparkJobResponse.

        **参数解释**：作业配置信息，包含作业类型、入口参数、依赖包等信息。

        :return: The job_config of this ShowSparkJobResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.object`
        """
        return self._job_config

    @job_config.setter
    def job_config(self, job_config):
        r"""Sets the job_config of this ShowSparkJobResponse.

        **参数解释**：作业配置信息，包含作业类型、入口参数、依赖包等信息。

        :param job_config: The job_config of this ShowSparkJobResponse.
        :type job_config: :class:`huaweicloudsdkaidatalakejobserver.v2.object`
        """
        self._job_config = job_config

    @property
    def resource_config(self):
        r"""Gets the resource_config of this ShowSparkJobResponse.

        :return: The resource_config of this ShowSparkJobResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkResourceConfigResponse`
        """
        return self._resource_config

    @resource_config.setter
    def resource_config(self, resource_config):
        r"""Sets the resource_config of this ShowSparkJobResponse.

        :param resource_config: The resource_config of this ShowSparkJobResponse.
        :type resource_config: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkResourceConfigResponse`
        """
        self._resource_config = resource_config

    @property
    def restore_strategy(self):
        r"""Gets the restore_strategy of this ShowSparkJobResponse.

        :return: The restore_strategy of this ShowSparkJobResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkRestoreStrategyResponse`
        """
        return self._restore_strategy

    @restore_strategy.setter
    def restore_strategy(self, restore_strategy):
        r"""Sets the restore_strategy of this ShowSparkJobResponse.

        :param restore_strategy: The restore_strategy of this ShowSparkJobResponse.
        :type restore_strategy: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkRestoreStrategyResponse`
        """
        self._restore_strategy = restore_strategy

    @property
    def spark_config(self):
        r"""Gets the spark_config of this ShowSparkJobResponse.

        **参数解释**：用户自定义Spark参数配置。 **取值范围**：长度为0~1024个字符。

        :return: The spark_config of this ShowSparkJobResponse.
        :rtype: dict(str, str)
        """
        return self._spark_config

    @spark_config.setter
    def spark_config(self, spark_config):
        r"""Sets the spark_config of this ShowSparkJobResponse.

        **参数解释**：用户自定义Spark参数配置。 **取值范围**：长度为0~1024个字符。

        :param spark_config: The spark_config of this ShowSparkJobResponse.
        :type spark_config: dict(str, str)
        """
        self._spark_config = spark_config

    @property
    def logging_config(self):
        r"""Gets the logging_config of this ShowSparkJobResponse.

        :return: The logging_config of this ShowSparkJobResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkLoggingConfigResponse`
        """
        return self._logging_config

    @logging_config.setter
    def logging_config(self, logging_config):
        r"""Sets the logging_config of this ShowSparkJobResponse.

        :param logging_config: The logging_config of this ShowSparkJobResponse.
        :type logging_config: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkLoggingConfigResponse`
        """
        self._logging_config = logging_config

    @property
    def image(self):
        r"""Gets the image of this ShowSparkJobResponse.

        :return: The image of this ShowSparkJobResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkJobImageConfigResponse`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this ShowSparkJobResponse.

        :param image: The image of this ShowSparkJobResponse.
        :type image: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkJobImageConfigResponse`
        """
        self._image = image

    @property
    def retry_times(self):
        r"""Gets the retry_times of this ShowSparkJobResponse.

        **参数解释**：作业重试次数，用于记录作业失败后的重试次数。 **取值范围**：最小值为0。

        :return: The retry_times of this ShowSparkJobResponse.
        :rtype: int
        """
        return self._retry_times

    @retry_times.setter
    def retry_times(self, retry_times):
        r"""Sets the retry_times of this ShowSparkJobResponse.

        **参数解释**：作业重试次数，用于记录作业失败后的重试次数。 **取值范围**：最小值为0。

        :param retry_times: The retry_times of this ShowSparkJobResponse.
        :type retry_times: int
        """
        self._retry_times = retry_times

    @property
    def labels(self):
        r"""Gets the labels of this ShowSparkJobResponse.

        **参数解释**：作业标签列表，用于标识和分类作业。

        :return: The labels of this ShowSparkJobResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkJobLabelResponse`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ShowSparkJobResponse.

        **参数解释**：作业标签列表，用于标识和分类作业。

        :param labels: The labels of this ShowSparkJobResponse.
        :type labels: list[:class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkJobLabelResponse`]
        """
        self._labels = labels

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowSparkJobResponse.

        **参数解释**：作业创建时间，用于记录作业提交时间。 **取值范围**：unix时间戳，单位为毫秒。

        :return: The create_time of this ShowSparkJobResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowSparkJobResponse.

        **参数解释**：作业创建时间，用于记录作业提交时间。 **取值范围**：unix时间戳，单位为毫秒。

        :param create_time: The create_time of this ShowSparkJobResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowSparkJobResponse.

        **参数解释**：作业开始运行时间，用于记录作业实际开始执行的时间。 **取值范围**：unix时间戳，单位为毫秒。

        :return: The start_time of this ShowSparkJobResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowSparkJobResponse.

        **参数解释**：作业开始运行时间，用于记录作业实际开始执行的时间。 **取值范围**：unix时间戳，单位为毫秒。

        :param start_time: The start_time of this ShowSparkJobResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowSparkJobResponse.

        **参数解释**：作业结束时间，用于记录作业执行完成的时间。 **取值范围**：unix时间戳，单位为毫秒。

        :return: The end_time of this ShowSparkJobResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowSparkJobResponse.

        **参数解释**：作业结束时间，用于记录作业执行完成的时间。 **取值范围**：unix时间戳，单位为毫秒。

        :param end_time: The end_time of this ShowSparkJobResponse.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def create_user(self):
        r"""Gets the create_user of this ShowSparkJobResponse.

        :return: The create_user of this ShowSparkJobResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkCreateUser`
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ShowSparkJobResponse.

        :param create_user: The create_user of this ShowSparkJobResponse.
        :type create_user: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkCreateUser`
        """
        self._create_user = create_user

    @property
    def log_url(self):
        r"""Gets the log_url of this ShowSparkJobResponse.

        **参数解释**：日志归档路径OBS URL，用于查看作业执行日志。 **取值范围**：OBS URL格式，长度为1~1024个字符。

        :return: The log_url of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._log_url

    @log_url.setter
    def log_url(self, log_url):
        r"""Sets the log_url of this ShowSparkJobResponse.

        **参数解释**：日志归档路径OBS URL，用于查看作业执行日志。 **取值范围**：OBS URL格式，长度为1~1024个字符。

        :param log_url: The log_url of this ShowSparkJobResponse.
        :type log_url: str
        """
        self._log_url = log_url

    @property
    def description(self):
        r"""Gets the description of this ShowSparkJobResponse.

        **参数解释**：Spark作业描述信息，用于说明作业用途。 **取值范围**：长度为0~512个字符。

        :return: The description of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowSparkJobResponse.

        **参数解释**：Spark作业描述信息，用于说明作业用途。 **取值范围**：长度为0~512个字符。

        :param description: The description of this ShowSparkJobResponse.
        :type description: str
        """
        self._description = description

    def to_dict(self):
        import warnings
        warnings.warn("ShowSparkJobResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSparkJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
