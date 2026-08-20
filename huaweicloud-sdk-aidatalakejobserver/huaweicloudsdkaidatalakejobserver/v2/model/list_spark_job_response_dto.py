# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSparkJobResponseDto:

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
        'job_type': 'str',
        'state': 'str',
        'state_message': 'str',
        'retry_times': 'int',
        'create_time': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'create_user': 'SparkCreateUser',
        'log_url': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'client_token': 'client_token',
        'name': 'name',
        'endpoint_name': 'endpoint_name',
        'job_type': 'job_type',
        'state': 'state',
        'state_message': 'state_message',
        'retry_times': 'retry_times',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'create_user': 'create_user',
        'log_url': 'log_url'
    }

    def __init__(self, job_id=None, client_token=None, name=None, endpoint_name=None, job_type=None, state=None, state_message=None, retry_times=None, create_time=None, start_time=None, end_time=None, create_user=None, log_url=None):
        r"""ListSparkJobResponseDto

        The model defined in huaweicloud sdk

        :param job_id: **参数解释**：Spark作业ID，用于唯一标识该作业。 **取值范围**：采用UUID格式，长度为36个字符，例如：80ceaaff-3cfc-4162-a56f-70031ea4fa91。
        :type job_id: str
        :param client_token: **参数解释**：Spark作业事务ID，用于防止重复提交。 **取值范围**：采用UUID格式，长度为36个字符，例如：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。
        :type client_token: str
        :param name: **参数解释**：Spark作业名称，用于标识作业。 **取值范围**：长度为1~128个字符。
        :type name: str
        :param endpoint_name: **参数解释**：端点名称，用于指定Spark作业执行环境。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。
        :type endpoint_name: str
        :param job_type: **参数解释**：作业类型，用于标识作业的类型。 **取值范围**： - spark_jar_job：Spark jar作业。 - spark_python_job：Python Spark作业。 - spark_sql_scripting_job：SQL脚本作业（预留类型）。
        :type job_type: str
        :param state: **参数解释**：Spark作业状态，用于标识作业当前执行状态。 **取值范围**： - PENDING：启动中。 - QUEUED：排队中。 - RUNNING：运行中。 - CANCELING：取消中。 - CANCELED：已取消。 - FAILED：运行失败。 - SUCCEED：运行成功。 - QUEUED_TIMEOUT：排队超时。 - RUNNING_TIMEOUT：运行超时。
        :type state: str
        :param state_message: **参数解释**：作业状态消息，当作业异常结束时显示相关信息。 **取值范围**：长度为0~512个字符。
        :type state_message: str
        :param retry_times: **参数解释**：作业重试次数，用于记录作业失败后的重试次数。 **取值范围**：最小值为0。
        :type retry_times: int
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
        """
        
        

        self._job_id = None
        self._client_token = None
        self._name = None
        self._endpoint_name = None
        self._job_type = None
        self._state = None
        self._state_message = None
        self._retry_times = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._create_user = None
        self._log_url = None
        self.discriminator = None

        self.job_id = job_id
        if client_token is not None:
            self.client_token = client_token
        self.name = name
        self.endpoint_name = endpoint_name
        self.job_type = job_type
        self.state = state
        if state_message is not None:
            self.state_message = state_message
        if retry_times is not None:
            self.retry_times = retry_times
        self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.create_user = create_user
        if log_url is not None:
            self.log_url = log_url

    @property
    def job_id(self):
        r"""Gets the job_id of this ListSparkJobResponseDto.

        **参数解释**：Spark作业ID，用于唯一标识该作业。 **取值范围**：采用UUID格式，长度为36个字符，例如：80ceaaff-3cfc-4162-a56f-70031ea4fa91。

        :return: The job_id of this ListSparkJobResponseDto.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListSparkJobResponseDto.

        **参数解释**：Spark作业ID，用于唯一标识该作业。 **取值范围**：采用UUID格式，长度为36个字符，例如：80ceaaff-3cfc-4162-a56f-70031ea4fa91。

        :param job_id: The job_id of this ListSparkJobResponseDto.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def client_token(self):
        r"""Gets the client_token of this ListSparkJobResponseDto.

        **参数解释**：Spark作业事务ID，用于防止重复提交。 **取值范围**：采用UUID格式，长度为36个字符，例如：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。

        :return: The client_token of this ListSparkJobResponseDto.
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        r"""Sets the client_token of this ListSparkJobResponseDto.

        **参数解释**：Spark作业事务ID，用于防止重复提交。 **取值范围**：采用UUID格式，长度为36个字符，例如：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。

        :param client_token: The client_token of this ListSparkJobResponseDto.
        :type client_token: str
        """
        self._client_token = client_token

    @property
    def name(self):
        r"""Gets the name of this ListSparkJobResponseDto.

        **参数解释**：Spark作业名称，用于标识作业。 **取值范围**：长度为1~128个字符。

        :return: The name of this ListSparkJobResponseDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSparkJobResponseDto.

        **参数解释**：Spark作业名称，用于标识作业。 **取值范围**：长度为1~128个字符。

        :param name: The name of this ListSparkJobResponseDto.
        :type name: str
        """
        self._name = name

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this ListSparkJobResponseDto.

        **参数解释**：端点名称，用于指定Spark作业执行环境。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。

        :return: The endpoint_name of this ListSparkJobResponseDto.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this ListSparkJobResponseDto.

        **参数解释**：端点名称，用于指定Spark作业执行环境。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。

        :param endpoint_name: The endpoint_name of this ListSparkJobResponseDto.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def job_type(self):
        r"""Gets the job_type of this ListSparkJobResponseDto.

        **参数解释**：作业类型，用于标识作业的类型。 **取值范围**： - spark_jar_job：Spark jar作业。 - spark_python_job：Python Spark作业。 - spark_sql_scripting_job：SQL脚本作业（预留类型）。

        :return: The job_type of this ListSparkJobResponseDto.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ListSparkJobResponseDto.

        **参数解释**：作业类型，用于标识作业的类型。 **取值范围**： - spark_jar_job：Spark jar作业。 - spark_python_job：Python Spark作业。 - spark_sql_scripting_job：SQL脚本作业（预留类型）。

        :param job_type: The job_type of this ListSparkJobResponseDto.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def state(self):
        r"""Gets the state of this ListSparkJobResponseDto.

        **参数解释**：Spark作业状态，用于标识作业当前执行状态。 **取值范围**： - PENDING：启动中。 - QUEUED：排队中。 - RUNNING：运行中。 - CANCELING：取消中。 - CANCELED：已取消。 - FAILED：运行失败。 - SUCCEED：运行成功。 - QUEUED_TIMEOUT：排队超时。 - RUNNING_TIMEOUT：运行超时。

        :return: The state of this ListSparkJobResponseDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListSparkJobResponseDto.

        **参数解释**：Spark作业状态，用于标识作业当前执行状态。 **取值范围**： - PENDING：启动中。 - QUEUED：排队中。 - RUNNING：运行中。 - CANCELING：取消中。 - CANCELED：已取消。 - FAILED：运行失败。 - SUCCEED：运行成功。 - QUEUED_TIMEOUT：排队超时。 - RUNNING_TIMEOUT：运行超时。

        :param state: The state of this ListSparkJobResponseDto.
        :type state: str
        """
        self._state = state

    @property
    def state_message(self):
        r"""Gets the state_message of this ListSparkJobResponseDto.

        **参数解释**：作业状态消息，当作业异常结束时显示相关信息。 **取值范围**：长度为0~512个字符。

        :return: The state_message of this ListSparkJobResponseDto.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        r"""Sets the state_message of this ListSparkJobResponseDto.

        **参数解释**：作业状态消息，当作业异常结束时显示相关信息。 **取值范围**：长度为0~512个字符。

        :param state_message: The state_message of this ListSparkJobResponseDto.
        :type state_message: str
        """
        self._state_message = state_message

    @property
    def retry_times(self):
        r"""Gets the retry_times of this ListSparkJobResponseDto.

        **参数解释**：作业重试次数，用于记录作业失败后的重试次数。 **取值范围**：最小值为0。

        :return: The retry_times of this ListSparkJobResponseDto.
        :rtype: int
        """
        return self._retry_times

    @retry_times.setter
    def retry_times(self, retry_times):
        r"""Sets the retry_times of this ListSparkJobResponseDto.

        **参数解释**：作业重试次数，用于记录作业失败后的重试次数。 **取值范围**：最小值为0。

        :param retry_times: The retry_times of this ListSparkJobResponseDto.
        :type retry_times: int
        """
        self._retry_times = retry_times

    @property
    def create_time(self):
        r"""Gets the create_time of this ListSparkJobResponseDto.

        **参数解释**：作业创建时间，用于记录作业提交时间。 **取值范围**：unix时间戳，单位为毫秒。

        :return: The create_time of this ListSparkJobResponseDto.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListSparkJobResponseDto.

        **参数解释**：作业创建时间，用于记录作业提交时间。 **取值范围**：unix时间戳，单位为毫秒。

        :param create_time: The create_time of this ListSparkJobResponseDto.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ListSparkJobResponseDto.

        **参数解释**：作业开始运行时间，用于记录作业实际开始执行的时间。 **取值范围**：unix时间戳，单位为毫秒。

        :return: The start_time of this ListSparkJobResponseDto.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListSparkJobResponseDto.

        **参数解释**：作业开始运行时间，用于记录作业实际开始执行的时间。 **取值范围**：unix时间戳，单位为毫秒。

        :param start_time: The start_time of this ListSparkJobResponseDto.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListSparkJobResponseDto.

        **参数解释**：作业结束时间，用于记录作业执行完成的时间。 **取值范围**：unix时间戳，单位为毫秒。

        :return: The end_time of this ListSparkJobResponseDto.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListSparkJobResponseDto.

        **参数解释**：作业结束时间，用于记录作业执行完成的时间。 **取值范围**：unix时间戳，单位为毫秒。

        :param end_time: The end_time of this ListSparkJobResponseDto.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def create_user(self):
        r"""Gets the create_user of this ListSparkJobResponseDto.

        :return: The create_user of this ListSparkJobResponseDto.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkCreateUser`
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ListSparkJobResponseDto.

        :param create_user: The create_user of this ListSparkJobResponseDto.
        :type create_user: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkCreateUser`
        """
        self._create_user = create_user

    @property
    def log_url(self):
        r"""Gets the log_url of this ListSparkJobResponseDto.

        **参数解释**：日志归档路径OBS URL，用于查看作业执行日志。 **取值范围**：OBS URL格式，长度为1~1024个字符。

        :return: The log_url of this ListSparkJobResponseDto.
        :rtype: str
        """
        return self._log_url

    @log_url.setter
    def log_url(self, log_url):
        r"""Sets the log_url of this ListSparkJobResponseDto.

        **参数解释**：日志归档路径OBS URL，用于查看作业执行日志。 **取值范围**：OBS URL格式，长度为1~1024个字符。

        :param log_url: The log_url of this ListSparkJobResponseDto.
        :type log_url: str
        """
        self._log_url = log_url

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
        if not isinstance(other, ListSparkJobResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
