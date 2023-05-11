# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobQueryBean:

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
        'user': 'str',
        'job_name': 'str',
        'job_result': 'str',
        'job_state': 'str',
        'job_progress': 'float',
        'job_type': 'str',
        'started_time': 'int',
        'submitted_time': 'int',
        'finished_time': 'int',
        'elapsed_time': 'int',
        'arguments': 'str',
        'launcher_id': 'str',
        'properties': 'str',
        'app_id': 'str',
        'tracking_url': 'str',
        'queue': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'user': 'user',
        'job_name': 'job_name',
        'job_result': 'job_result',
        'job_state': 'job_state',
        'job_progress': 'job_progress',
        'job_type': 'job_type',
        'started_time': 'started_time',
        'submitted_time': 'submitted_time',
        'finished_time': 'finished_time',
        'elapsed_time': 'elapsed_time',
        'arguments': 'arguments',
        'launcher_id': 'launcher_id',
        'properties': 'properties',
        'app_id': 'app_id',
        'tracking_url': 'tracking_url',
        'queue': 'queue'
    }

    def __init__(self, job_id=None, user=None, job_name=None, job_result=None, job_state=None, job_progress=None, job_type=None, started_time=None, submitted_time=None, finished_time=None, elapsed_time=None, arguments=None, launcher_id=None, properties=None, app_id=None, tracking_url=None, queue=None):
        """JobQueryBean

        The model defined in huaweicloud sdk

        :param job_id: 作业ID。
        :type job_id: str
        :param user: 提交作业的用户名称。
        :type user: str
        :param job_name: 作业名称。
        :type job_name: str
        :param job_result: 作业最终结果。 - FAILED：执行失败的作业 - KILLED：执行中被手动终止的作业。 - UNDEFINED：正在执行的作业。 - SUCCEEDED：执行成功的作业。
        :type job_result: str
        :param job_state: 作业执行状态。  - FAILED：失败 - KILLED：已终止 - NEW：已创建 - NEW_SAVING：已创建保存中 - SUBMITTED：已提交 - ACCEPTED：已接受 - RUNNING：运行中 - FINISHED：已完成
        :type job_state: str
        :param job_progress: 作业执行进度。
        :type job_progress: float
        :param job_type: 作业类型。 - MapReduce - SparkSubmit：SparkPython类型的作业在查询时作业类型请选择SparkSubmit。 - HiveScript - HiveSql - DistCp，导入、导出数据。 - SparkScript - SparkSql - Flink
        :type job_type: str
        :param started_time: 作业开始执行时间。单位：毫秒。
        :type started_time: int
        :param submitted_time: 作业提交时间。单位：毫秒。
        :type submitted_time: int
        :param finished_time: 作业完成时间。单位：毫秒。
        :type finished_time: int
        :param elapsed_time: 作业执行时长。单位：毫秒。
        :type elapsed_time: int
        :param arguments: 运行参数。
        :type arguments: str
        :param launcher_id: 实际作业编号。
        :type launcher_id: str
        :param properties: 配置参数，用于传-d参数。最多为2048字符，不能包含&gt;&lt;|&#39;&#x60;&amp;!\\特殊字符，可为空。
        :type properties: str
        :param app_id: 实际作业编号。
        :type app_id: str
        :param tracking_url:  日志链接地址。当前仅SparkSubmit作业支持该参数。 该参数基于集群的EIP访问集群中的YARN WebUI页面，用户如果在VPC界面解绑EIP，MRS服务侧数据会因为未更新导致该参数引用旧EIP导致访问失败，可通过对集群重新进行EIP的绑定来修复该问题。
        :type tracking_url: str
        :param queue: 作业的资源对列类型。
        :type queue: str
        """
        
        

        self._job_id = None
        self._user = None
        self._job_name = None
        self._job_result = None
        self._job_state = None
        self._job_progress = None
        self._job_type = None
        self._started_time = None
        self._submitted_time = None
        self._finished_time = None
        self._elapsed_time = None
        self._arguments = None
        self._launcher_id = None
        self._properties = None
        self._app_id = None
        self._tracking_url = None
        self._queue = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if user is not None:
            self.user = user
        if job_name is not None:
            self.job_name = job_name
        if job_result is not None:
            self.job_result = job_result
        if job_state is not None:
            self.job_state = job_state
        if job_progress is not None:
            self.job_progress = job_progress
        if job_type is not None:
            self.job_type = job_type
        if started_time is not None:
            self.started_time = started_time
        if submitted_time is not None:
            self.submitted_time = submitted_time
        if finished_time is not None:
            self.finished_time = finished_time
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time
        if arguments is not None:
            self.arguments = arguments
        if launcher_id is not None:
            self.launcher_id = launcher_id
        if properties is not None:
            self.properties = properties
        if app_id is not None:
            self.app_id = app_id
        if tracking_url is not None:
            self.tracking_url = tracking_url
        if queue is not None:
            self.queue = queue

    @property
    def job_id(self):
        """Gets the job_id of this JobQueryBean.

        作业ID。

        :return: The job_id of this JobQueryBean.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobQueryBean.

        作业ID。

        :param job_id: The job_id of this JobQueryBean.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def user(self):
        """Gets the user of this JobQueryBean.

        提交作业的用户名称。

        :return: The user of this JobQueryBean.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this JobQueryBean.

        提交作业的用户名称。

        :param user: The user of this JobQueryBean.
        :type user: str
        """
        self._user = user

    @property
    def job_name(self):
        """Gets the job_name of this JobQueryBean.

        作业名称。

        :return: The job_name of this JobQueryBean.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this JobQueryBean.

        作业名称。

        :param job_name: The job_name of this JobQueryBean.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_result(self):
        """Gets the job_result of this JobQueryBean.

        作业最终结果。 - FAILED：执行失败的作业 - KILLED：执行中被手动终止的作业。 - UNDEFINED：正在执行的作业。 - SUCCEEDED：执行成功的作业。

        :return: The job_result of this JobQueryBean.
        :rtype: str
        """
        return self._job_result

    @job_result.setter
    def job_result(self, job_result):
        """Sets the job_result of this JobQueryBean.

        作业最终结果。 - FAILED：执行失败的作业 - KILLED：执行中被手动终止的作业。 - UNDEFINED：正在执行的作业。 - SUCCEEDED：执行成功的作业。

        :param job_result: The job_result of this JobQueryBean.
        :type job_result: str
        """
        self._job_result = job_result

    @property
    def job_state(self):
        """Gets the job_state of this JobQueryBean.

        作业执行状态。  - FAILED：失败 - KILLED：已终止 - NEW：已创建 - NEW_SAVING：已创建保存中 - SUBMITTED：已提交 - ACCEPTED：已接受 - RUNNING：运行中 - FINISHED：已完成

        :return: The job_state of this JobQueryBean.
        :rtype: str
        """
        return self._job_state

    @job_state.setter
    def job_state(self, job_state):
        """Sets the job_state of this JobQueryBean.

        作业执行状态。  - FAILED：失败 - KILLED：已终止 - NEW：已创建 - NEW_SAVING：已创建保存中 - SUBMITTED：已提交 - ACCEPTED：已接受 - RUNNING：运行中 - FINISHED：已完成

        :param job_state: The job_state of this JobQueryBean.
        :type job_state: str
        """
        self._job_state = job_state

    @property
    def job_progress(self):
        """Gets the job_progress of this JobQueryBean.

        作业执行进度。

        :return: The job_progress of this JobQueryBean.
        :rtype: float
        """
        return self._job_progress

    @job_progress.setter
    def job_progress(self, job_progress):
        """Sets the job_progress of this JobQueryBean.

        作业执行进度。

        :param job_progress: The job_progress of this JobQueryBean.
        :type job_progress: float
        """
        self._job_progress = job_progress

    @property
    def job_type(self):
        """Gets the job_type of this JobQueryBean.

        作业类型。 - MapReduce - SparkSubmit：SparkPython类型的作业在查询时作业类型请选择SparkSubmit。 - HiveScript - HiveSql - DistCp，导入、导出数据。 - SparkScript - SparkSql - Flink

        :return: The job_type of this JobQueryBean.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this JobQueryBean.

        作业类型。 - MapReduce - SparkSubmit：SparkPython类型的作业在查询时作业类型请选择SparkSubmit。 - HiveScript - HiveSql - DistCp，导入、导出数据。 - SparkScript - SparkSql - Flink

        :param job_type: The job_type of this JobQueryBean.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def started_time(self):
        """Gets the started_time of this JobQueryBean.

        作业开始执行时间。单位：毫秒。

        :return: The started_time of this JobQueryBean.
        :rtype: int
        """
        return self._started_time

    @started_time.setter
    def started_time(self, started_time):
        """Sets the started_time of this JobQueryBean.

        作业开始执行时间。单位：毫秒。

        :param started_time: The started_time of this JobQueryBean.
        :type started_time: int
        """
        self._started_time = started_time

    @property
    def submitted_time(self):
        """Gets the submitted_time of this JobQueryBean.

        作业提交时间。单位：毫秒。

        :return: The submitted_time of this JobQueryBean.
        :rtype: int
        """
        return self._submitted_time

    @submitted_time.setter
    def submitted_time(self, submitted_time):
        """Sets the submitted_time of this JobQueryBean.

        作业提交时间。单位：毫秒。

        :param submitted_time: The submitted_time of this JobQueryBean.
        :type submitted_time: int
        """
        self._submitted_time = submitted_time

    @property
    def finished_time(self):
        """Gets the finished_time of this JobQueryBean.

        作业完成时间。单位：毫秒。

        :return: The finished_time of this JobQueryBean.
        :rtype: int
        """
        return self._finished_time

    @finished_time.setter
    def finished_time(self, finished_time):
        """Sets the finished_time of this JobQueryBean.

        作业完成时间。单位：毫秒。

        :param finished_time: The finished_time of this JobQueryBean.
        :type finished_time: int
        """
        self._finished_time = finished_time

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this JobQueryBean.

        作业执行时长。单位：毫秒。

        :return: The elapsed_time of this JobQueryBean.
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this JobQueryBean.

        作业执行时长。单位：毫秒。

        :param elapsed_time: The elapsed_time of this JobQueryBean.
        :type elapsed_time: int
        """
        self._elapsed_time = elapsed_time

    @property
    def arguments(self):
        """Gets the arguments of this JobQueryBean.

        运行参数。

        :return: The arguments of this JobQueryBean.
        :rtype: str
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this JobQueryBean.

        运行参数。

        :param arguments: The arguments of this JobQueryBean.
        :type arguments: str
        """
        self._arguments = arguments

    @property
    def launcher_id(self):
        """Gets the launcher_id of this JobQueryBean.

        实际作业编号。

        :return: The launcher_id of this JobQueryBean.
        :rtype: str
        """
        return self._launcher_id

    @launcher_id.setter
    def launcher_id(self, launcher_id):
        """Sets the launcher_id of this JobQueryBean.

        实际作业编号。

        :param launcher_id: The launcher_id of this JobQueryBean.
        :type launcher_id: str
        """
        self._launcher_id = launcher_id

    @property
    def properties(self):
        """Gets the properties of this JobQueryBean.

        配置参数，用于传-d参数。最多为2048字符，不能包含><|'`&!\\特殊字符，可为空。

        :return: The properties of this JobQueryBean.
        :rtype: str
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this JobQueryBean.

        配置参数，用于传-d参数。最多为2048字符，不能包含><|'`&!\\特殊字符，可为空。

        :param properties: The properties of this JobQueryBean.
        :type properties: str
        """
        self._properties = properties

    @property
    def app_id(self):
        """Gets the app_id of this JobQueryBean.

        实际作业编号。

        :return: The app_id of this JobQueryBean.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this JobQueryBean.

        实际作业编号。

        :param app_id: The app_id of this JobQueryBean.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def tracking_url(self):
        """Gets the tracking_url of this JobQueryBean.

         日志链接地址。当前仅SparkSubmit作业支持该参数。 该参数基于集群的EIP访问集群中的YARN WebUI页面，用户如果在VPC界面解绑EIP，MRS服务侧数据会因为未更新导致该参数引用旧EIP导致访问失败，可通过对集群重新进行EIP的绑定来修复该问题。

        :return: The tracking_url of this JobQueryBean.
        :rtype: str
        """
        return self._tracking_url

    @tracking_url.setter
    def tracking_url(self, tracking_url):
        """Sets the tracking_url of this JobQueryBean.

         日志链接地址。当前仅SparkSubmit作业支持该参数。 该参数基于集群的EIP访问集群中的YARN WebUI页面，用户如果在VPC界面解绑EIP，MRS服务侧数据会因为未更新导致该参数引用旧EIP导致访问失败，可通过对集群重新进行EIP的绑定来修复该问题。

        :param tracking_url: The tracking_url of this JobQueryBean.
        :type tracking_url: str
        """
        self._tracking_url = tracking_url

    @property
    def queue(self):
        """Gets the queue of this JobQueryBean.

        作业的资源对列类型。

        :return: The queue of this JobQueryBean.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this JobQueryBean.

        作业的资源对列类型。

        :param queue: The queue of this JobQueryBean.
        :type queue: str
        """
        self._queue = queue

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobQueryBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
