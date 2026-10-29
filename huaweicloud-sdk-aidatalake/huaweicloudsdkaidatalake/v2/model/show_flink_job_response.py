# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlinkJobResponse(SdkResponse):

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
        'deployment_id': 'str',
        'endpoint_id': 'str',
        'endpoint_name': 'str',
        'status': 'FlinkJobStatus',
        'job_agency': 'str',
        'obs_bucket_name': 'str',
        'job_config': 'ShowFlinkJobArtifactResponse',
        'resource_config': 'ShowFlinkResourceConfigResponseBody',
        'image_config': 'ShowFlinkJobImageConfigResponseBody',
        'flink_config': 'dict(str, str)',
        'execution_mode': 'FlinkJobExecutionMode',
        'restore_strategy': 'ShowRestoreStrategyResponseBody',
        'logging_config': 'ShowFlinkLoggingConfigResponseBody',
        'metric': 'FlinkResourceMetric',
        'create_time': 'int',
        'create_user': 'FlinkCreateUser',
        'update_time': 'int',
        'update_user': 'FlinkUpdateUser',
        'log_url': 'str',
        'labels': 'list[FlinkLabel]',
        'description': 'str',
        'alert_enabled': 'bool',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'client_token': 'client_token',
        'name': 'name',
        'deployment_id': 'deployment_id',
        'endpoint_id': 'endpoint_id',
        'endpoint_name': 'endpoint_name',
        'status': 'status',
        'job_agency': 'job_agency',
        'obs_bucket_name': 'obs_bucket_name',
        'job_config': 'job_config',
        'resource_config': 'resource_config',
        'image_config': 'image_config',
        'flink_config': 'flink_config',
        'execution_mode': 'execution_mode',
        'restore_strategy': 'restore_strategy',
        'logging_config': 'logging_config',
        'metric': 'metric',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'update_time': 'update_time',
        'update_user': 'update_user',
        'log_url': 'log_url',
        'labels': 'labels',
        'description': 'description',
        'alert_enabled': 'alert_enabled',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, job_id=None, client_token=None, name=None, deployment_id=None, endpoint_id=None, endpoint_name=None, status=None, job_agency=None, obs_bucket_name=None, job_config=None, resource_config=None, image_config=None, flink_config=None, execution_mode=None, restore_strategy=None, logging_config=None, metric=None, create_time=None, create_user=None, update_time=None, update_user=None, log_url=None, labels=None, description=None, alert_enabled=None, start_time=None, end_time=None):
        r"""ShowFlinkJobResponse

        The model defined in huaweicloud sdk

        :param job_id: **参数解释**：Flink作业ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 
        :type job_id: str
        :param client_token: **参数解释**：客户端Token，用于接口调用幂等校验。 **取值范围**：长度为1~64个字符，只能由英文字母、数字、下划线和中划线组成。 
        :type client_token: str
        :param name: **参数解释**：作业名称。 **取值范围**：1~128个字符，以字母或数字开头和结尾，中间可包含字母、数字、下划线和中划线。 
        :type name: str
        :param deployment_id: **参数解释**：已部署作业ID。 **取值范围**：1~64个字符，支持字母、数字、下划线和中划线。 
        :type deployment_id: str
        :param endpoint_id: **参数解释**：作业运行的端点ID。 **取值范围**：采用UUID格式，固定36个字符。 
        :type endpoint_id: str
        :param endpoint_name: **参数解释**：作业运行的端点名称。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。 
        :type endpoint_name: str
        :param status: 
        :type status: :class:`huaweicloudsdkaidatalake.v2.FlinkJobStatus`
        :param job_agency: **参数解释**：用户自定义委托名称，用于授权作业访问OBS等外部资源，不指定时默认使用端点委托。 **取值范围**：1~64个字符。 
        :type job_agency: str
        :param obs_bucket_name: **参数解释**：OBS桶名称，用于存储作业的Checkpoint、日志等数据。 **取值范围**：1~512个字符。 
        :type obs_bucket_name: str
        :param job_config: 
        :type job_config: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkJobArtifactResponse`
        :param resource_config: 
        :type resource_config: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkResourceConfigResponseBody`
        :param image_config: 
        :type image_config: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkJobImageConfigResponseBody`
        :param flink_config: **参数解释**：Flink配置参数，为键值对形式。key为Flink配置项名称（如taskmanager.numberOfTaskSlots）；value为对应配置值，长度1~1024个字符。除用户配置项外，还包含系统自动补充的保留参数（如execution.checkpointing.dir、execution.checkpointing.savepoint-dir、high-availability.storageDir，由系统根据作业配置自动生成）。 
        :type flink_config: dict(str, str)
        :param execution_mode: 
        :type execution_mode: :class:`huaweicloudsdkaidatalake.v2.FlinkJobExecutionMode`
        :param restore_strategy: 
        :type restore_strategy: :class:`huaweicloudsdkaidatalake.v2.ShowRestoreStrategyResponseBody`
        :param logging_config: 
        :type logging_config: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkLoggingConfigResponseBody`
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
        :param labels: **参数解释**：标签，用于作业分类和筛选。 
        :type labels: list[:class:`huaweicloudsdkaidatalake.v2.FlinkLabel`]
        :param description: **参数解释**：描述信息。 **取值范围**：1~512个字符。 
        :type description: str
        :param alert_enabled: **参数解释**：该作业是否开启失败告警通知。 **取值范围**：   - true：开启。作业运行失败或提交失败时会向客户发送告警通知。   - false：关闭。作业失败时不发送告警通知。 **默认取值**：false，不指定时默认关闭。 
        :type alert_enabled: bool
        :param start_time: **参数解释**：作业开始运行的时间戳（进入RUNNING状态的时间）。 **取值范围**：0 ~ 4102416000000，13位毫秒时间戳。 
        :type start_time: int
        :param end_time: **参数解释**：作业结束时间戳（进入终态 FINISHED/CANCELLED/FAILED的时间）。 **取值范围**：0 ~ 4102416000000，13位毫秒时间戳。 
        :type end_time: int
        """
        
        super().__init__()

        self._job_id = None
        self._client_token = None
        self._name = None
        self._deployment_id = None
        self._endpoint_id = None
        self._endpoint_name = None
        self._status = None
        self._job_agency = None
        self._obs_bucket_name = None
        self._job_config = None
        self._resource_config = None
        self._image_config = None
        self._flink_config = None
        self._execution_mode = None
        self._restore_strategy = None
        self._logging_config = None
        self._metric = None
        self._create_time = None
        self._create_user = None
        self._update_time = None
        self._update_user = None
        self._log_url = None
        self._labels = None
        self._description = None
        self._alert_enabled = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if client_token is not None:
            self.client_token = client_token
        if name is not None:
            self.name = name
        if deployment_id is not None:
            self.deployment_id = deployment_id
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if endpoint_name is not None:
            self.endpoint_name = endpoint_name
        if status is not None:
            self.status = status
        if job_agency is not None:
            self.job_agency = job_agency
        if obs_bucket_name is not None:
            self.obs_bucket_name = obs_bucket_name
        if job_config is not None:
            self.job_config = job_config
        if resource_config is not None:
            self.resource_config = resource_config
        if image_config is not None:
            self.image_config = image_config
        if flink_config is not None:
            self.flink_config = flink_config
        if execution_mode is not None:
            self.execution_mode = execution_mode
        if restore_strategy is not None:
            self.restore_strategy = restore_strategy
        if logging_config is not None:
            self.logging_config = logging_config
        if metric is not None:
            self.metric = metric
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user
        if log_url is not None:
            self.log_url = log_url
        if labels is not None:
            self.labels = labels
        if description is not None:
            self.description = description
        if alert_enabled is not None:
            self.alert_enabled = alert_enabled
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowFlinkJobResponse.

        **参数解释**：Flink作业ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :return: The job_id of this ShowFlinkJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowFlinkJobResponse.

        **参数解释**：Flink作业ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :param job_id: The job_id of this ShowFlinkJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def client_token(self):
        r"""Gets the client_token of this ShowFlinkJobResponse.

        **参数解释**：客户端Token，用于接口调用幂等校验。 **取值范围**：长度为1~64个字符，只能由英文字母、数字、下划线和中划线组成。 

        :return: The client_token of this ShowFlinkJobResponse.
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        r"""Sets the client_token of this ShowFlinkJobResponse.

        **参数解释**：客户端Token，用于接口调用幂等校验。 **取值范围**：长度为1~64个字符，只能由英文字母、数字、下划线和中划线组成。 

        :param client_token: The client_token of this ShowFlinkJobResponse.
        :type client_token: str
        """
        self._client_token = client_token

    @property
    def name(self):
        r"""Gets the name of this ShowFlinkJobResponse.

        **参数解释**：作业名称。 **取值范围**：1~128个字符，以字母或数字开头和结尾，中间可包含字母、数字、下划线和中划线。 

        :return: The name of this ShowFlinkJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowFlinkJobResponse.

        **参数解释**：作业名称。 **取值范围**：1~128个字符，以字母或数字开头和结尾，中间可包含字母、数字、下划线和中划线。 

        :param name: The name of this ShowFlinkJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def deployment_id(self):
        r"""Gets the deployment_id of this ShowFlinkJobResponse.

        **参数解释**：已部署作业ID。 **取值范围**：1~64个字符，支持字母、数字、下划线和中划线。 

        :return: The deployment_id of this ShowFlinkJobResponse.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        r"""Sets the deployment_id of this ShowFlinkJobResponse.

        **参数解释**：已部署作业ID。 **取值范围**：1~64个字符，支持字母、数字、下划线和中划线。 

        :param deployment_id: The deployment_id of this ShowFlinkJobResponse.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this ShowFlinkJobResponse.

        **参数解释**：作业运行的端点ID。 **取值范围**：采用UUID格式，固定36个字符。 

        :return: The endpoint_id of this ShowFlinkJobResponse.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this ShowFlinkJobResponse.

        **参数解释**：作业运行的端点ID。 **取值范围**：采用UUID格式，固定36个字符。 

        :param endpoint_id: The endpoint_id of this ShowFlinkJobResponse.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this ShowFlinkJobResponse.

        **参数解释**：作业运行的端点名称。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。 

        :return: The endpoint_name of this ShowFlinkJobResponse.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this ShowFlinkJobResponse.

        **参数解释**：作业运行的端点名称。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。 

        :param endpoint_name: The endpoint_name of this ShowFlinkJobResponse.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def status(self):
        r"""Gets the status of this ShowFlinkJobResponse.

        :return: The status of this ShowFlinkJobResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkJobStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowFlinkJobResponse.

        :param status: The status of this ShowFlinkJobResponse.
        :type status: :class:`huaweicloudsdkaidatalake.v2.FlinkJobStatus`
        """
        self._status = status

    @property
    def job_agency(self):
        r"""Gets the job_agency of this ShowFlinkJobResponse.

        **参数解释**：用户自定义委托名称，用于授权作业访问OBS等外部资源，不指定时默认使用端点委托。 **取值范围**：1~64个字符。 

        :return: The job_agency of this ShowFlinkJobResponse.
        :rtype: str
        """
        return self._job_agency

    @job_agency.setter
    def job_agency(self, job_agency):
        r"""Sets the job_agency of this ShowFlinkJobResponse.

        **参数解释**：用户自定义委托名称，用于授权作业访问OBS等外部资源，不指定时默认使用端点委托。 **取值范围**：1~64个字符。 

        :param job_agency: The job_agency of this ShowFlinkJobResponse.
        :type job_agency: str
        """
        self._job_agency = job_agency

    @property
    def obs_bucket_name(self):
        r"""Gets the obs_bucket_name of this ShowFlinkJobResponse.

        **参数解释**：OBS桶名称，用于存储作业的Checkpoint、日志等数据。 **取值范围**：1~512个字符。 

        :return: The obs_bucket_name of this ShowFlinkJobResponse.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        r"""Sets the obs_bucket_name of this ShowFlinkJobResponse.

        **参数解释**：OBS桶名称，用于存储作业的Checkpoint、日志等数据。 **取值范围**：1~512个字符。 

        :param obs_bucket_name: The obs_bucket_name of this ShowFlinkJobResponse.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def job_config(self):
        r"""Gets the job_config of this ShowFlinkJobResponse.

        :return: The job_config of this ShowFlinkJobResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkJobArtifactResponse`
        """
        return self._job_config

    @job_config.setter
    def job_config(self, job_config):
        r"""Sets the job_config of this ShowFlinkJobResponse.

        :param job_config: The job_config of this ShowFlinkJobResponse.
        :type job_config: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkJobArtifactResponse`
        """
        self._job_config = job_config

    @property
    def resource_config(self):
        r"""Gets the resource_config of this ShowFlinkJobResponse.

        :return: The resource_config of this ShowFlinkJobResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkResourceConfigResponseBody`
        """
        return self._resource_config

    @resource_config.setter
    def resource_config(self, resource_config):
        r"""Sets the resource_config of this ShowFlinkJobResponse.

        :param resource_config: The resource_config of this ShowFlinkJobResponse.
        :type resource_config: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkResourceConfigResponseBody`
        """
        self._resource_config = resource_config

    @property
    def image_config(self):
        r"""Gets the image_config of this ShowFlinkJobResponse.

        :return: The image_config of this ShowFlinkJobResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkJobImageConfigResponseBody`
        """
        return self._image_config

    @image_config.setter
    def image_config(self, image_config):
        r"""Sets the image_config of this ShowFlinkJobResponse.

        :param image_config: The image_config of this ShowFlinkJobResponse.
        :type image_config: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkJobImageConfigResponseBody`
        """
        self._image_config = image_config

    @property
    def flink_config(self):
        r"""Gets the flink_config of this ShowFlinkJobResponse.

        **参数解释**：Flink配置参数，为键值对形式。key为Flink配置项名称（如taskmanager.numberOfTaskSlots）；value为对应配置值，长度1~1024个字符。除用户配置项外，还包含系统自动补充的保留参数（如execution.checkpointing.dir、execution.checkpointing.savepoint-dir、high-availability.storageDir，由系统根据作业配置自动生成）。 

        :return: The flink_config of this ShowFlinkJobResponse.
        :rtype: dict(str, str)
        """
        return self._flink_config

    @flink_config.setter
    def flink_config(self, flink_config):
        r"""Sets the flink_config of this ShowFlinkJobResponse.

        **参数解释**：Flink配置参数，为键值对形式。key为Flink配置项名称（如taskmanager.numberOfTaskSlots）；value为对应配置值，长度1~1024个字符。除用户配置项外，还包含系统自动补充的保留参数（如execution.checkpointing.dir、execution.checkpointing.savepoint-dir、high-availability.storageDir，由系统根据作业配置自动生成）。 

        :param flink_config: The flink_config of this ShowFlinkJobResponse.
        :type flink_config: dict(str, str)
        """
        self._flink_config = flink_config

    @property
    def execution_mode(self):
        r"""Gets the execution_mode of this ShowFlinkJobResponse.

        :return: The execution_mode of this ShowFlinkJobResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkJobExecutionMode`
        """
        return self._execution_mode

    @execution_mode.setter
    def execution_mode(self, execution_mode):
        r"""Sets the execution_mode of this ShowFlinkJobResponse.

        :param execution_mode: The execution_mode of this ShowFlinkJobResponse.
        :type execution_mode: :class:`huaweicloudsdkaidatalake.v2.FlinkJobExecutionMode`
        """
        self._execution_mode = execution_mode

    @property
    def restore_strategy(self):
        r"""Gets the restore_strategy of this ShowFlinkJobResponse.

        :return: The restore_strategy of this ShowFlinkJobResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowRestoreStrategyResponseBody`
        """
        return self._restore_strategy

    @restore_strategy.setter
    def restore_strategy(self, restore_strategy):
        r"""Sets the restore_strategy of this ShowFlinkJobResponse.

        :param restore_strategy: The restore_strategy of this ShowFlinkJobResponse.
        :type restore_strategy: :class:`huaweicloudsdkaidatalake.v2.ShowRestoreStrategyResponseBody`
        """
        self._restore_strategy = restore_strategy

    @property
    def logging_config(self):
        r"""Gets the logging_config of this ShowFlinkJobResponse.

        :return: The logging_config of this ShowFlinkJobResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkLoggingConfigResponseBody`
        """
        return self._logging_config

    @logging_config.setter
    def logging_config(self, logging_config):
        r"""Sets the logging_config of this ShowFlinkJobResponse.

        :param logging_config: The logging_config of this ShowFlinkJobResponse.
        :type logging_config: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkLoggingConfigResponseBody`
        """
        self._logging_config = logging_config

    @property
    def metric(self):
        r"""Gets the metric of this ShowFlinkJobResponse.

        :return: The metric of this ShowFlinkJobResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkResourceMetric`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this ShowFlinkJobResponse.

        :param metric: The metric of this ShowFlinkJobResponse.
        :type metric: :class:`huaweicloudsdkaidatalake.v2.FlinkResourceMetric`
        """
        self._metric = metric

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowFlinkJobResponse.

        **参数解释**：创建时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :return: The create_time of this ShowFlinkJobResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowFlinkJobResponse.

        **参数解释**：创建时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :param create_time: The create_time of this ShowFlinkJobResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_user(self):
        r"""Gets the create_user of this ShowFlinkJobResponse.

        :return: The create_user of this ShowFlinkJobResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkCreateUser`
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ShowFlinkJobResponse.

        :param create_user: The create_user of this ShowFlinkJobResponse.
        :type create_user: :class:`huaweicloudsdkaidatalake.v2.FlinkCreateUser`
        """
        self._create_user = create_user

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowFlinkJobResponse.

        **参数解释**：更新时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :return: The update_time of this ShowFlinkJobResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowFlinkJobResponse.

        **参数解释**：更新时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :param update_time: The update_time of this ShowFlinkJobResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def update_user(self):
        r"""Gets the update_user of this ShowFlinkJobResponse.

        :return: The update_user of this ShowFlinkJobResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkUpdateUser`
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this ShowFlinkJobResponse.

        :param update_user: The update_user of this ShowFlinkJobResponse.
        :type update_user: :class:`huaweicloudsdkaidatalake.v2.FlinkUpdateUser`
        """
        self._update_user = update_user

    @property
    def log_url(self):
        r"""Gets the log_url of this ShowFlinkJobResponse.

        **参数解释**：日志归档路径OBS URL，用于查看作业执行日志。 **取值范围**：OBS URL格式，长度为1~1024个字符。 

        :return: The log_url of this ShowFlinkJobResponse.
        :rtype: str
        """
        return self._log_url

    @log_url.setter
    def log_url(self, log_url):
        r"""Sets the log_url of this ShowFlinkJobResponse.

        **参数解释**：日志归档路径OBS URL，用于查看作业执行日志。 **取值范围**：OBS URL格式，长度为1~1024个字符。 

        :param log_url: The log_url of this ShowFlinkJobResponse.
        :type log_url: str
        """
        self._log_url = log_url

    @property
    def labels(self):
        r"""Gets the labels of this ShowFlinkJobResponse.

        **参数解释**：标签，用于作业分类和筛选。 

        :return: The labels of this ShowFlinkJobResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.FlinkLabel`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ShowFlinkJobResponse.

        **参数解释**：标签，用于作业分类和筛选。 

        :param labels: The labels of this ShowFlinkJobResponse.
        :type labels: list[:class:`huaweicloudsdkaidatalake.v2.FlinkLabel`]
        """
        self._labels = labels

    @property
    def description(self):
        r"""Gets the description of this ShowFlinkJobResponse.

        **参数解释**：描述信息。 **取值范围**：1~512个字符。 

        :return: The description of this ShowFlinkJobResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowFlinkJobResponse.

        **参数解释**：描述信息。 **取值范围**：1~512个字符。 

        :param description: The description of this ShowFlinkJobResponse.
        :type description: str
        """
        self._description = description

    @property
    def alert_enabled(self):
        r"""Gets the alert_enabled of this ShowFlinkJobResponse.

        **参数解释**：该作业是否开启失败告警通知。 **取值范围**：   - true：开启。作业运行失败或提交失败时会向客户发送告警通知。   - false：关闭。作业失败时不发送告警通知。 **默认取值**：false，不指定时默认关闭。 

        :return: The alert_enabled of this ShowFlinkJobResponse.
        :rtype: bool
        """
        return self._alert_enabled

    @alert_enabled.setter
    def alert_enabled(self, alert_enabled):
        r"""Sets the alert_enabled of this ShowFlinkJobResponse.

        **参数解释**：该作业是否开启失败告警通知。 **取值范围**：   - true：开启。作业运行失败或提交失败时会向客户发送告警通知。   - false：关闭。作业失败时不发送告警通知。 **默认取值**：false，不指定时默认关闭。 

        :param alert_enabled: The alert_enabled of this ShowFlinkJobResponse.
        :type alert_enabled: bool
        """
        self._alert_enabled = alert_enabled

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowFlinkJobResponse.

        **参数解释**：作业开始运行的时间戳（进入RUNNING状态的时间）。 **取值范围**：0 ~ 4102416000000，13位毫秒时间戳。 

        :return: The start_time of this ShowFlinkJobResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowFlinkJobResponse.

        **参数解释**：作业开始运行的时间戳（进入RUNNING状态的时间）。 **取值范围**：0 ~ 4102416000000，13位毫秒时间戳。 

        :param start_time: The start_time of this ShowFlinkJobResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowFlinkJobResponse.

        **参数解释**：作业结束时间戳（进入终态 FINISHED/CANCELLED/FAILED的时间）。 **取值范围**：0 ~ 4102416000000，13位毫秒时间戳。 

        :return: The end_time of this ShowFlinkJobResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowFlinkJobResponse.

        **参数解释**：作业结束时间戳（进入终态 FINISHED/CANCELLED/FAILED的时间）。 **取值范围**：0 ~ 4102416000000，13位毫秒时间戳。 

        :param end_time: The end_time of this ShowFlinkJobResponse.
        :type end_time: int
        """
        self._end_time = end_time

    def to_dict(self):
        import warnings
        warnings.warn("ShowFlinkJobResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowFlinkJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
