# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetryFactoryJobInstanceBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'retry_location': 'str',
        'node_name': 'str',
        'retry_task_version': 'str',
        'ignore_obs_monitor': 'bool',
        'task_retrys': 'list[RetryFactoryJobInstanceBodyTaskRetrys]',
        'begin_time': 'int',
        'end_time': 'int',
        'jobs': 'list[RetryFactoryJobInstanceBodyJobs]',
        'concurrent': 'int'
    }

    attribute_map = {
        'retry_location': 'retry_location',
        'node_name': 'node_name',
        'retry_task_version': 'retry_task_version',
        'ignore_obs_monitor': 'ignore_obs_monitor',
        'task_retrys': 'task_retrys',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'jobs': 'jobs',
        'concurrent': 'concurrent'
    }

    def __init__(self, retry_location=None, node_name=None, retry_task_version=None, ignore_obs_monitor=None, task_retrys=None, begin_time=None, end_time=None, jobs=None, concurrent=None):
        r"""RetryFactoryJobInstanceBody

        The model defined in huaweicloud sdk

        :param retry_location: 重跑开始位置，取值有firstNode、errorNode和specifiedNode。
        :type retry_location: str
        :param node_name: 节点名称。
        :type node_name: str
        :param retry_task_version: 使用的作业参数，取值有original_version和current_version。
        :type retry_task_version: str
        :param ignore_obs_monitor: 是否忽略obs监听，默认为true。
        :type ignore_obs_monitor: bool
        :param task_retrys: 作业实例重跑参数，当重跑当前实例类型时，需要指定该参数的重跑信息，重跑当前作业及其上下游作业实例类型不需要指定该参数。
        :type task_retrys: list[:class:`huaweicloudsdkdataartsstudio.v1.RetryFactoryJobInstanceBodyTaskRetrys`]
        :param begin_time: 实例开始时间，当重跑当前作业及其上下游作业实例类型时，该参数有效。
        :type begin_time: int
        :param end_time: 实例结束时间，当重跑当前作业及其上下游作业实例类型时，该参数有效。
        :type end_time: int
        :param jobs: 作业实例重跑参数，当重跑当前作业及其上下游作业实例类型时，需要指定该参数的重跑信息，重跑当前实例类型不需要指定该参数。
        :type jobs: list[:class:`huaweicloudsdkdataartsstudio.v1.RetryFactoryJobInstanceBodyJobs`]
        :param concurrent: 并行度，当重跑当前作业及其上下游作业实例类型时，该参数有效，默认值为1，取值范围为1到128。
        :type concurrent: int
        """
        
        

        self._retry_location = None
        self._node_name = None
        self._retry_task_version = None
        self._ignore_obs_monitor = None
        self._task_retrys = None
        self._begin_time = None
        self._end_time = None
        self._jobs = None
        self._concurrent = None
        self.discriminator = None

        self.retry_location = retry_location
        if node_name is not None:
            self.node_name = node_name
        self.retry_task_version = retry_task_version
        if ignore_obs_monitor is not None:
            self.ignore_obs_monitor = ignore_obs_monitor
        if task_retrys is not None:
            self.task_retrys = task_retrys
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if jobs is not None:
            self.jobs = jobs
        if concurrent is not None:
            self.concurrent = concurrent

    @property
    def retry_location(self):
        r"""Gets the retry_location of this RetryFactoryJobInstanceBody.

        重跑开始位置，取值有firstNode、errorNode和specifiedNode。

        :return: The retry_location of this RetryFactoryJobInstanceBody.
        :rtype: str
        """
        return self._retry_location

    @retry_location.setter
    def retry_location(self, retry_location):
        r"""Sets the retry_location of this RetryFactoryJobInstanceBody.

        重跑开始位置，取值有firstNode、errorNode和specifiedNode。

        :param retry_location: The retry_location of this RetryFactoryJobInstanceBody.
        :type retry_location: str
        """
        self._retry_location = retry_location

    @property
    def node_name(self):
        r"""Gets the node_name of this RetryFactoryJobInstanceBody.

        节点名称。

        :return: The node_name of this RetryFactoryJobInstanceBody.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this RetryFactoryJobInstanceBody.

        节点名称。

        :param node_name: The node_name of this RetryFactoryJobInstanceBody.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def retry_task_version(self):
        r"""Gets the retry_task_version of this RetryFactoryJobInstanceBody.

        使用的作业参数，取值有original_version和current_version。

        :return: The retry_task_version of this RetryFactoryJobInstanceBody.
        :rtype: str
        """
        return self._retry_task_version

    @retry_task_version.setter
    def retry_task_version(self, retry_task_version):
        r"""Sets the retry_task_version of this RetryFactoryJobInstanceBody.

        使用的作业参数，取值有original_version和current_version。

        :param retry_task_version: The retry_task_version of this RetryFactoryJobInstanceBody.
        :type retry_task_version: str
        """
        self._retry_task_version = retry_task_version

    @property
    def ignore_obs_monitor(self):
        r"""Gets the ignore_obs_monitor of this RetryFactoryJobInstanceBody.

        是否忽略obs监听，默认为true。

        :return: The ignore_obs_monitor of this RetryFactoryJobInstanceBody.
        :rtype: bool
        """
        return self._ignore_obs_monitor

    @ignore_obs_monitor.setter
    def ignore_obs_monitor(self, ignore_obs_monitor):
        r"""Sets the ignore_obs_monitor of this RetryFactoryJobInstanceBody.

        是否忽略obs监听，默认为true。

        :param ignore_obs_monitor: The ignore_obs_monitor of this RetryFactoryJobInstanceBody.
        :type ignore_obs_monitor: bool
        """
        self._ignore_obs_monitor = ignore_obs_monitor

    @property
    def task_retrys(self):
        r"""Gets the task_retrys of this RetryFactoryJobInstanceBody.

        作业实例重跑参数，当重跑当前实例类型时，需要指定该参数的重跑信息，重跑当前作业及其上下游作业实例类型不需要指定该参数。

        :return: The task_retrys of this RetryFactoryJobInstanceBody.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.RetryFactoryJobInstanceBodyTaskRetrys`]
        """
        return self._task_retrys

    @task_retrys.setter
    def task_retrys(self, task_retrys):
        r"""Sets the task_retrys of this RetryFactoryJobInstanceBody.

        作业实例重跑参数，当重跑当前实例类型时，需要指定该参数的重跑信息，重跑当前作业及其上下游作业实例类型不需要指定该参数。

        :param task_retrys: The task_retrys of this RetryFactoryJobInstanceBody.
        :type task_retrys: list[:class:`huaweicloudsdkdataartsstudio.v1.RetryFactoryJobInstanceBodyTaskRetrys`]
        """
        self._task_retrys = task_retrys

    @property
    def begin_time(self):
        r"""Gets the begin_time of this RetryFactoryJobInstanceBody.

        实例开始时间，当重跑当前作业及其上下游作业实例类型时，该参数有效。

        :return: The begin_time of this RetryFactoryJobInstanceBody.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this RetryFactoryJobInstanceBody.

        实例开始时间，当重跑当前作业及其上下游作业实例类型时，该参数有效。

        :param begin_time: The begin_time of this RetryFactoryJobInstanceBody.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this RetryFactoryJobInstanceBody.

        实例结束时间，当重跑当前作业及其上下游作业实例类型时，该参数有效。

        :return: The end_time of this RetryFactoryJobInstanceBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this RetryFactoryJobInstanceBody.

        实例结束时间，当重跑当前作业及其上下游作业实例类型时，该参数有效。

        :param end_time: The end_time of this RetryFactoryJobInstanceBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def jobs(self):
        r"""Gets the jobs of this RetryFactoryJobInstanceBody.

        作业实例重跑参数，当重跑当前作业及其上下游作业实例类型时，需要指定该参数的重跑信息，重跑当前实例类型不需要指定该参数。

        :return: The jobs of this RetryFactoryJobInstanceBody.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.RetryFactoryJobInstanceBodyJobs`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        r"""Sets the jobs of this RetryFactoryJobInstanceBody.

        作业实例重跑参数，当重跑当前作业及其上下游作业实例类型时，需要指定该参数的重跑信息，重跑当前实例类型不需要指定该参数。

        :param jobs: The jobs of this RetryFactoryJobInstanceBody.
        :type jobs: list[:class:`huaweicloudsdkdataartsstudio.v1.RetryFactoryJobInstanceBodyJobs`]
        """
        self._jobs = jobs

    @property
    def concurrent(self):
        r"""Gets the concurrent of this RetryFactoryJobInstanceBody.

        并行度，当重跑当前作业及其上下游作业实例类型时，该参数有效，默认值为1，取值范围为1到128。

        :return: The concurrent of this RetryFactoryJobInstanceBody.
        :rtype: int
        """
        return self._concurrent

    @concurrent.setter
    def concurrent(self, concurrent):
        r"""Sets the concurrent of this RetryFactoryJobInstanceBody.

        并行度，当重跑当前作业及其上下游作业实例类型时，该参数有效，默认值为1，取值范围为1到128。

        :param concurrent: The concurrent of this RetryFactoryJobInstanceBody.
        :type concurrent: int
        """
        self._concurrent = concurrent

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
        if not isinstance(other, RetryFactoryJobInstanceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
