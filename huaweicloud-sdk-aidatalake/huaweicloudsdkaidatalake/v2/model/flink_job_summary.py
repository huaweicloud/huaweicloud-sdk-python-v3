# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkJobSummary:

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
        'name': 'str',
        'endpoint_id': 'str',
        'endpoint_name': 'str',
        'job_type': 'str',
        'status': 'FlinkJobStatus',
        'execution_mode': 'FlinkJobExecutionMode',
        'metric': 'FlinkResourceMetric',
        'create_time': 'int',
        'create_user': 'FlinkCreateUser',
        'update_time': 'int',
        'update_user': 'FlinkUpdateUser',
        'log_url': 'str',
        'description': 'str',
        'alert_enabled': 'bool',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'name': 'name',
        'endpoint_id': 'endpoint_id',
        'endpoint_name': 'endpoint_name',
        'job_type': 'job_type',
        'status': 'status',
        'execution_mode': 'execution_mode',
        'metric': 'metric',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'update_time': 'update_time',
        'update_user': 'update_user',
        'log_url': 'log_url',
        'description': 'description',
        'alert_enabled': 'alert_enabled',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, job_id=None, name=None, endpoint_id=None, endpoint_name=None, job_type=None, status=None, execution_mode=None, metric=None, create_time=None, create_user=None, update_time=None, update_user=None, log_url=None, description=None, alert_enabled=None, start_time=None, end_time=None):
        r"""FlinkJobSummary

        The model defined in huaweicloud sdk

        :param job_id: **参数解释**：Flink作业ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 
        :type job_id: str
        :param name: **参数解释**：作业名称。 **取值范围**：1~128个字符，以字母或数字开头和结尾，中间可包含字母、数字、下划线和中划线。 
        :type name: str
        :param endpoint_id: **参数解释**：作业运行的端点ID。 **取值范围**：采用UUID格式，固定36个字符。 
        :type endpoint_id: str
        :param endpoint_name: **参数解释**：作业运行的端点名称。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。 
        :type endpoint_name: str
        :param job_type: **参数解释**：作业类型。 **取值范围**：   - FLINK_JAR_JOB：JAR作业。   - FLINK_SQL_JOB：SQL作业。   - FLINK_SQL_GATEWAY：SQL Gateway作业。   - FLINK_PYTHON_JOB：Python作业。 
        :type job_type: str
        :param status: 
        :type status: :class:`huaweicloudsdkaidatalake.v2.FlinkJobStatus`
        :param execution_mode: 
        :type execution_mode: :class:`huaweicloudsdkaidatalake.v2.FlinkJobExecutionMode`
        :param metric: 
        :type metric: :class:`huaweicloudsdkaidatalake.v2.FlinkResourceMetric`
        :param create_time: **参数解释**：创建时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 
        :type create_time: int
        :param create_user: 
        :type create_user: :class:`huaweicloudsdkaidatalake.v2.FlinkCreateUser`
        :param update_time: **参数解释**：更新时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 
        :type update_time: int
        :param update_user: 
        :type update_user: :class:`huaweicloudsdkaidatalake.v2.FlinkUpdateUser`
        :param log_url: **参数解释**：日志归档路径OBS URL，用于查看作业执行日志。 **取值范围**：OBS URL格式，长度为1~1024个字符。 
        :type log_url: str
        :param description: **参数解释**：作业描述信息。 **取值范围**：1~512个字符。 
        :type description: str
        :param alert_enabled: **参数解释**：该作业是否开启失败告警通知。 **取值范围**：   - true：开启。作业运行失败或提交失败时会向客户发送告警通知。   - false：关闭。作业失败时不发送告警通知。 **默认取值**：false，不指定时默认关闭。 
        :type alert_enabled: bool
        :param start_time: **参数解释**：作业开始运行的时间戳（进入RUNNING状态的时间）。 **取值范围**：0 ~ 4102416000000，13位毫秒时间戳。 
        :type start_time: int
        :param end_time: **参数解释**：作业结束时间戳（进入终态 FINISHED/CANCELLED/FAILED的时间）。 **取值范围**：0 ~ 4102416000000，13位毫秒时间戳。 
        :type end_time: int
        """
        
        

        self._job_id = None
        self._name = None
        self._endpoint_id = None
        self._endpoint_name = None
        self._job_type = None
        self._status = None
        self._execution_mode = None
        self._metric = None
        self._create_time = None
        self._create_user = None
        self._update_time = None
        self._update_user = None
        self._log_url = None
        self._description = None
        self._alert_enabled = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.job_id = job_id
        self.name = name
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if endpoint_name is not None:
            self.endpoint_name = endpoint_name
        if job_type is not None:
            self.job_type = job_type
        self.status = status
        self.execution_mode = execution_mode
        self.metric = metric
        self.create_time = create_time
        self.create_user = create_user
        self.update_time = update_time
        self.update_user = update_user
        if log_url is not None:
            self.log_url = log_url
        self.description = description
        if alert_enabled is not None:
            self.alert_enabled = alert_enabled
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def job_id(self):
        r"""Gets the job_id of this FlinkJobSummary.

        **参数解释**：Flink作业ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :return: The job_id of this FlinkJobSummary.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this FlinkJobSummary.

        **参数解释**：Flink作业ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :param job_id: The job_id of this FlinkJobSummary.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def name(self):
        r"""Gets the name of this FlinkJobSummary.

        **参数解释**：作业名称。 **取值范围**：1~128个字符，以字母或数字开头和结尾，中间可包含字母、数字、下划线和中划线。 

        :return: The name of this FlinkJobSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FlinkJobSummary.

        **参数解释**：作业名称。 **取值范围**：1~128个字符，以字母或数字开头和结尾，中间可包含字母、数字、下划线和中划线。 

        :param name: The name of this FlinkJobSummary.
        :type name: str
        """
        self._name = name

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this FlinkJobSummary.

        **参数解释**：作业运行的端点ID。 **取值范围**：采用UUID格式，固定36个字符。 

        :return: The endpoint_id of this FlinkJobSummary.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this FlinkJobSummary.

        **参数解释**：作业运行的端点ID。 **取值范围**：采用UUID格式，固定36个字符。 

        :param endpoint_id: The endpoint_id of this FlinkJobSummary.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this FlinkJobSummary.

        **参数解释**：作业运行的端点名称。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。 

        :return: The endpoint_name of this FlinkJobSummary.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this FlinkJobSummary.

        **参数解释**：作业运行的端点名称。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。 

        :param endpoint_name: The endpoint_name of this FlinkJobSummary.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def job_type(self):
        r"""Gets the job_type of this FlinkJobSummary.

        **参数解释**：作业类型。 **取值范围**：   - FLINK_JAR_JOB：JAR作业。   - FLINK_SQL_JOB：SQL作业。   - FLINK_SQL_GATEWAY：SQL Gateway作业。   - FLINK_PYTHON_JOB：Python作业。 

        :return: The job_type of this FlinkJobSummary.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this FlinkJobSummary.

        **参数解释**：作业类型。 **取值范围**：   - FLINK_JAR_JOB：JAR作业。   - FLINK_SQL_JOB：SQL作业。   - FLINK_SQL_GATEWAY：SQL Gateway作业。   - FLINK_PYTHON_JOB：Python作业。 

        :param job_type: The job_type of this FlinkJobSummary.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def status(self):
        r"""Gets the status of this FlinkJobSummary.

        :return: The status of this FlinkJobSummary.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkJobStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this FlinkJobSummary.

        :param status: The status of this FlinkJobSummary.
        :type status: :class:`huaweicloudsdkaidatalake.v2.FlinkJobStatus`
        """
        self._status = status

    @property
    def execution_mode(self):
        r"""Gets the execution_mode of this FlinkJobSummary.

        :return: The execution_mode of this FlinkJobSummary.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkJobExecutionMode`
        """
        return self._execution_mode

    @execution_mode.setter
    def execution_mode(self, execution_mode):
        r"""Sets the execution_mode of this FlinkJobSummary.

        :param execution_mode: The execution_mode of this FlinkJobSummary.
        :type execution_mode: :class:`huaweicloudsdkaidatalake.v2.FlinkJobExecutionMode`
        """
        self._execution_mode = execution_mode

    @property
    def metric(self):
        r"""Gets the metric of this FlinkJobSummary.

        :return: The metric of this FlinkJobSummary.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkResourceMetric`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this FlinkJobSummary.

        :param metric: The metric of this FlinkJobSummary.
        :type metric: :class:`huaweicloudsdkaidatalake.v2.FlinkResourceMetric`
        """
        self._metric = metric

    @property
    def create_time(self):
        r"""Gets the create_time of this FlinkJobSummary.

        **参数解释**：创建时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :return: The create_time of this FlinkJobSummary.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this FlinkJobSummary.

        **参数解释**：创建时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :param create_time: The create_time of this FlinkJobSummary.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_user(self):
        r"""Gets the create_user of this FlinkJobSummary.

        :return: The create_user of this FlinkJobSummary.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkCreateUser`
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this FlinkJobSummary.

        :param create_user: The create_user of this FlinkJobSummary.
        :type create_user: :class:`huaweicloudsdkaidatalake.v2.FlinkCreateUser`
        """
        self._create_user = create_user

    @property
    def update_time(self):
        r"""Gets the update_time of this FlinkJobSummary.

        **参数解释**：更新时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :return: The update_time of this FlinkJobSummary.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this FlinkJobSummary.

        **参数解释**：更新时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :param update_time: The update_time of this FlinkJobSummary.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def update_user(self):
        r"""Gets the update_user of this FlinkJobSummary.

        :return: The update_user of this FlinkJobSummary.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkUpdateUser`
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this FlinkJobSummary.

        :param update_user: The update_user of this FlinkJobSummary.
        :type update_user: :class:`huaweicloudsdkaidatalake.v2.FlinkUpdateUser`
        """
        self._update_user = update_user

    @property
    def log_url(self):
        r"""Gets the log_url of this FlinkJobSummary.

        **参数解释**：日志归档路径OBS URL，用于查看作业执行日志。 **取值范围**：OBS URL格式，长度为1~1024个字符。 

        :return: The log_url of this FlinkJobSummary.
        :rtype: str
        """
        return self._log_url

    @log_url.setter
    def log_url(self, log_url):
        r"""Sets the log_url of this FlinkJobSummary.

        **参数解释**：日志归档路径OBS URL，用于查看作业执行日志。 **取值范围**：OBS URL格式，长度为1~1024个字符。 

        :param log_url: The log_url of this FlinkJobSummary.
        :type log_url: str
        """
        self._log_url = log_url

    @property
    def description(self):
        r"""Gets the description of this FlinkJobSummary.

        **参数解释**：作业描述信息。 **取值范围**：1~512个字符。 

        :return: The description of this FlinkJobSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this FlinkJobSummary.

        **参数解释**：作业描述信息。 **取值范围**：1~512个字符。 

        :param description: The description of this FlinkJobSummary.
        :type description: str
        """
        self._description = description

    @property
    def alert_enabled(self):
        r"""Gets the alert_enabled of this FlinkJobSummary.

        **参数解释**：该作业是否开启失败告警通知。 **取值范围**：   - true：开启。作业运行失败或提交失败时会向客户发送告警通知。   - false：关闭。作业失败时不发送告警通知。 **默认取值**：false，不指定时默认关闭。 

        :return: The alert_enabled of this FlinkJobSummary.
        :rtype: bool
        """
        return self._alert_enabled

    @alert_enabled.setter
    def alert_enabled(self, alert_enabled):
        r"""Sets the alert_enabled of this FlinkJobSummary.

        **参数解释**：该作业是否开启失败告警通知。 **取值范围**：   - true：开启。作业运行失败或提交失败时会向客户发送告警通知。   - false：关闭。作业失败时不发送告警通知。 **默认取值**：false，不指定时默认关闭。 

        :param alert_enabled: The alert_enabled of this FlinkJobSummary.
        :type alert_enabled: bool
        """
        self._alert_enabled = alert_enabled

    @property
    def start_time(self):
        r"""Gets the start_time of this FlinkJobSummary.

        **参数解释**：作业开始运行的时间戳（进入RUNNING状态的时间）。 **取值范围**：0 ~ 4102416000000，13位毫秒时间戳。 

        :return: The start_time of this FlinkJobSummary.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this FlinkJobSummary.

        **参数解释**：作业开始运行的时间戳（进入RUNNING状态的时间）。 **取值范围**：0 ~ 4102416000000，13位毫秒时间戳。 

        :param start_time: The start_time of this FlinkJobSummary.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this FlinkJobSummary.

        **参数解释**：作业结束时间戳（进入终态 FINISHED/CANCELLED/FAILED的时间）。 **取值范围**：0 ~ 4102416000000，13位毫秒时间戳。 

        :return: The end_time of this FlinkJobSummary.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this FlinkJobSummary.

        **参数解释**：作业结束时间戳（进入终态 FINISHED/CANCELLED/FAILED的时间）。 **取值范围**：0 ~ 4102416000000，13位毫秒时间戳。 

        :param end_time: The end_time of this FlinkJobSummary.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, FlinkJobSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
