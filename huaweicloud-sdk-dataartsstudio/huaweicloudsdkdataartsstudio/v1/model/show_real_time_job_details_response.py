# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRealTimeJobDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'job_id': 'str',
        'state': 'str',
        'migration_type': 'str',
        'startup_timestamp': 'str',
        'job_engine_version': 'str',
        'cluster_engine_version': 'str',
        'cluster_type': 'str',
        'tracking_url': 'str',
        'metric_info': 'str',
        'task_details': 'list[TaskDetailInfo]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'job_id': 'job_id',
        'state': 'state',
        'migration_type': 'migration_type',
        'startup_timestamp': 'startup_timestamp',
        'job_engine_version': 'job_engine_version',
        'cluster_engine_version': 'cluster_engine_version',
        'cluster_type': 'cluster_type',
        'tracking_url': 'tracking_url',
        'metric_info': 'metric_info',
        'task_details': 'task_details'
    }

    def __init__(self, is_success=None, message=None, job_id=None, state=None, migration_type=None, startup_timestamp=None, job_engine_version=None, cluster_engine_version=None, cluster_type=None, tracking_url=None, metric_info=None, task_details=None):
        r"""ShowRealTimeJobDetailsResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param job_id: 作业ID。
        :type job_id: str
        :param state: 作业状态。 - EXCEPTION：异常 - STOPPING：停止中 - SUBMITTING：提交中 - RUNNING：运行中 - STOPPED：已停止 - SUCCESS：成功
        :type state: str
        :param migration_type: 作业迁移类型。 - INCREMENTAL_DATA：增量数据 - HISTORY_DATA：历史数据
        :type migration_type: str
        :param startup_timestamp: INCREMENTAL_DATA作业启动的时间位点。
        :type startup_timestamp: str
        :param job_engine_version: 运行作业时的引擎版本。
        :type job_engine_version: str
        :param cluster_engine_version: 作业关联资源组的引擎版本。
        :type cluster_engine_version: str
        :param cluster_type: 资源组类型。
        :type cluster_type: str
        :param tracking_url: MRS Flink作业trackingUrl。
        :type tracking_url: str
        :param metric_info: 作业指标信息。
        :type metric_info: str
        :param task_details: 任务详情列表。
        :type task_details: list[:class:`huaweicloudsdkdataartsstudio.v1.TaskDetailInfo`]
        """
        
        super().__init__()

        self._is_success = None
        self._message = None
        self._job_id = None
        self._state = None
        self._migration_type = None
        self._startup_timestamp = None
        self._job_engine_version = None
        self._cluster_engine_version = None
        self._cluster_type = None
        self._tracking_url = None
        self._metric_info = None
        self._task_details = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if job_id is not None:
            self.job_id = job_id
        if state is not None:
            self.state = state
        if migration_type is not None:
            self.migration_type = migration_type
        if startup_timestamp is not None:
            self.startup_timestamp = startup_timestamp
        if job_engine_version is not None:
            self.job_engine_version = job_engine_version
        if cluster_engine_version is not None:
            self.cluster_engine_version = cluster_engine_version
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if tracking_url is not None:
            self.tracking_url = tracking_url
        if metric_info is not None:
            self.metric_info = metric_info
        if task_details is not None:
            self.task_details = task_details

    @property
    def is_success(self):
        r"""Gets the is_success of this ShowRealTimeJobDetailsResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this ShowRealTimeJobDetailsResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ShowRealTimeJobDetailsResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ShowRealTimeJobDetailsResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this ShowRealTimeJobDetailsResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ShowRealTimeJobDetailsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowRealTimeJobDetailsResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ShowRealTimeJobDetailsResponse.
        :type message: str
        """
        self._message = message

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowRealTimeJobDetailsResponse.

        作业ID。

        :return: The job_id of this ShowRealTimeJobDetailsResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowRealTimeJobDetailsResponse.

        作业ID。

        :param job_id: The job_id of this ShowRealTimeJobDetailsResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def state(self):
        r"""Gets the state of this ShowRealTimeJobDetailsResponse.

        作业状态。 - EXCEPTION：异常 - STOPPING：停止中 - SUBMITTING：提交中 - RUNNING：运行中 - STOPPED：已停止 - SUCCESS：成功

        :return: The state of this ShowRealTimeJobDetailsResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowRealTimeJobDetailsResponse.

        作业状态。 - EXCEPTION：异常 - STOPPING：停止中 - SUBMITTING：提交中 - RUNNING：运行中 - STOPPED：已停止 - SUCCESS：成功

        :param state: The state of this ShowRealTimeJobDetailsResponse.
        :type state: str
        """
        self._state = state

    @property
    def migration_type(self):
        r"""Gets the migration_type of this ShowRealTimeJobDetailsResponse.

        作业迁移类型。 - INCREMENTAL_DATA：增量数据 - HISTORY_DATA：历史数据

        :return: The migration_type of this ShowRealTimeJobDetailsResponse.
        :rtype: str
        """
        return self._migration_type

    @migration_type.setter
    def migration_type(self, migration_type):
        r"""Sets the migration_type of this ShowRealTimeJobDetailsResponse.

        作业迁移类型。 - INCREMENTAL_DATA：增量数据 - HISTORY_DATA：历史数据

        :param migration_type: The migration_type of this ShowRealTimeJobDetailsResponse.
        :type migration_type: str
        """
        self._migration_type = migration_type

    @property
    def startup_timestamp(self):
        r"""Gets the startup_timestamp of this ShowRealTimeJobDetailsResponse.

        INCREMENTAL_DATA作业启动的时间位点。

        :return: The startup_timestamp of this ShowRealTimeJobDetailsResponse.
        :rtype: str
        """
        return self._startup_timestamp

    @startup_timestamp.setter
    def startup_timestamp(self, startup_timestamp):
        r"""Sets the startup_timestamp of this ShowRealTimeJobDetailsResponse.

        INCREMENTAL_DATA作业启动的时间位点。

        :param startup_timestamp: The startup_timestamp of this ShowRealTimeJobDetailsResponse.
        :type startup_timestamp: str
        """
        self._startup_timestamp = startup_timestamp

    @property
    def job_engine_version(self):
        r"""Gets the job_engine_version of this ShowRealTimeJobDetailsResponse.

        运行作业时的引擎版本。

        :return: The job_engine_version of this ShowRealTimeJobDetailsResponse.
        :rtype: str
        """
        return self._job_engine_version

    @job_engine_version.setter
    def job_engine_version(self, job_engine_version):
        r"""Sets the job_engine_version of this ShowRealTimeJobDetailsResponse.

        运行作业时的引擎版本。

        :param job_engine_version: The job_engine_version of this ShowRealTimeJobDetailsResponse.
        :type job_engine_version: str
        """
        self._job_engine_version = job_engine_version

    @property
    def cluster_engine_version(self):
        r"""Gets the cluster_engine_version of this ShowRealTimeJobDetailsResponse.

        作业关联资源组的引擎版本。

        :return: The cluster_engine_version of this ShowRealTimeJobDetailsResponse.
        :rtype: str
        """
        return self._cluster_engine_version

    @cluster_engine_version.setter
    def cluster_engine_version(self, cluster_engine_version):
        r"""Sets the cluster_engine_version of this ShowRealTimeJobDetailsResponse.

        作业关联资源组的引擎版本。

        :param cluster_engine_version: The cluster_engine_version of this ShowRealTimeJobDetailsResponse.
        :type cluster_engine_version: str
        """
        self._cluster_engine_version = cluster_engine_version

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ShowRealTimeJobDetailsResponse.

        资源组类型。

        :return: The cluster_type of this ShowRealTimeJobDetailsResponse.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ShowRealTimeJobDetailsResponse.

        资源组类型。

        :param cluster_type: The cluster_type of this ShowRealTimeJobDetailsResponse.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def tracking_url(self):
        r"""Gets the tracking_url of this ShowRealTimeJobDetailsResponse.

        MRS Flink作业trackingUrl。

        :return: The tracking_url of this ShowRealTimeJobDetailsResponse.
        :rtype: str
        """
        return self._tracking_url

    @tracking_url.setter
    def tracking_url(self, tracking_url):
        r"""Sets the tracking_url of this ShowRealTimeJobDetailsResponse.

        MRS Flink作业trackingUrl。

        :param tracking_url: The tracking_url of this ShowRealTimeJobDetailsResponse.
        :type tracking_url: str
        """
        self._tracking_url = tracking_url

    @property
    def metric_info(self):
        r"""Gets the metric_info of this ShowRealTimeJobDetailsResponse.

        作业指标信息。

        :return: The metric_info of this ShowRealTimeJobDetailsResponse.
        :rtype: str
        """
        return self._metric_info

    @metric_info.setter
    def metric_info(self, metric_info):
        r"""Sets the metric_info of this ShowRealTimeJobDetailsResponse.

        作业指标信息。

        :param metric_info: The metric_info of this ShowRealTimeJobDetailsResponse.
        :type metric_info: str
        """
        self._metric_info = metric_info

    @property
    def task_details(self):
        r"""Gets the task_details of this ShowRealTimeJobDetailsResponse.

        任务详情列表。

        :return: The task_details of this ShowRealTimeJobDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TaskDetailInfo`]
        """
        return self._task_details

    @task_details.setter
    def task_details(self, task_details):
        r"""Sets the task_details of this ShowRealTimeJobDetailsResponse.

        任务详情列表。

        :param task_details: The task_details of this ShowRealTimeJobDetailsResponse.
        :type task_details: list[:class:`huaweicloudsdkdataartsstudio.v1.TaskDetailInfo`]
        """
        self._task_details = task_details

    def to_dict(self):
        import warnings
        warnings.warn("ShowRealTimeJobDetailsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowRealTimeJobDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
