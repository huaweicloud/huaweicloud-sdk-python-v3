# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskInstanceMetricDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eihealth_project_id': 'str',
        'job_id': 'str',
        'task_name': 'str',
        'task_index': 'str',
        'instance_name': 'str',
        'from_time': 'int',
        'to_time': 'int',
        'method': 'str',
        'metric_name': 'str'
    }

    attribute_map = {
        'eihealth_project_id': 'eihealth_project_id',
        'job_id': 'job_id',
        'task_name': 'task_name',
        'task_index': 'task_index',
        'instance_name': 'instance_name',
        'from_time': 'from_time',
        'to_time': 'to_time',
        'method': 'method',
        'metric_name': 'metric_name'
    }

    def __init__(self, eihealth_project_id=None, job_id=None, task_name=None, task_index=None, instance_name=None, from_time=None, to_time=None, method=None, metric_name=None):
        r"""ShowTaskInstanceMetricDataRequest

        The model defined in huaweicloud sdk

        :param eihealth_project_id: 平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param job_id: 作业id
        :type job_id: str
        :param task_name: 子任务名称
        :type task_name: str
        :param task_index: 子任务的并发序号
        :type task_index: str
        :param instance_name: 子任务实例名称
        :type instance_name: str
        :param from_time: 查询监控数据起始时间，UNIX时间戳，单位毫秒，不填时默认为当前时间
        :type from_time: int
        :param to_time: 查询监控数据截止时间，UNIX时间戳，单位毫秒，不填时默认为当前时间
        :type to_time: int
        :param method: 统计方法。枚举值，取值范围：maximum（最大值）、minimum（最小值）、average（平均值），不填时默认为maximum
        :type method: str
        :param metric_name: 查询的监控指标名称
        :type metric_name: str
        """
        
        

        self._eihealth_project_id = None
        self._job_id = None
        self._task_name = None
        self._task_index = None
        self._instance_name = None
        self._from_time = None
        self._to_time = None
        self._method = None
        self._metric_name = None
        self.discriminator = None

        self.eihealth_project_id = eihealth_project_id
        self.job_id = job_id
        self.task_name = task_name
        if task_index is not None:
            self.task_index = task_index
        self.instance_name = instance_name
        if from_time is not None:
            self.from_time = from_time
        if to_time is not None:
            self.to_time = to_time
        if method is not None:
            self.method = method
        self.metric_name = metric_name

    @property
    def eihealth_project_id(self):
        r"""Gets the eihealth_project_id of this ShowTaskInstanceMetricDataRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this ShowTaskInstanceMetricDataRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        r"""Sets the eihealth_project_id of this ShowTaskInstanceMetricDataRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this ShowTaskInstanceMetricDataRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowTaskInstanceMetricDataRequest.

        作业id

        :return: The job_id of this ShowTaskInstanceMetricDataRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowTaskInstanceMetricDataRequest.

        作业id

        :param job_id: The job_id of this ShowTaskInstanceMetricDataRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ShowTaskInstanceMetricDataRequest.

        子任务名称

        :return: The task_name of this ShowTaskInstanceMetricDataRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ShowTaskInstanceMetricDataRequest.

        子任务名称

        :param task_name: The task_name of this ShowTaskInstanceMetricDataRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_index(self):
        r"""Gets the task_index of this ShowTaskInstanceMetricDataRequest.

        子任务的并发序号

        :return: The task_index of this ShowTaskInstanceMetricDataRequest.
        :rtype: str
        """
        return self._task_index

    @task_index.setter
    def task_index(self, task_index):
        r"""Sets the task_index of this ShowTaskInstanceMetricDataRequest.

        子任务的并发序号

        :param task_index: The task_index of this ShowTaskInstanceMetricDataRequest.
        :type task_index: str
        """
        self._task_index = task_index

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ShowTaskInstanceMetricDataRequest.

        子任务实例名称

        :return: The instance_name of this ShowTaskInstanceMetricDataRequest.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ShowTaskInstanceMetricDataRequest.

        子任务实例名称

        :param instance_name: The instance_name of this ShowTaskInstanceMetricDataRequest.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def from_time(self):
        r"""Gets the from_time of this ShowTaskInstanceMetricDataRequest.

        查询监控数据起始时间，UNIX时间戳，单位毫秒，不填时默认为当前时间

        :return: The from_time of this ShowTaskInstanceMetricDataRequest.
        :rtype: int
        """
        return self._from_time

    @from_time.setter
    def from_time(self, from_time):
        r"""Sets the from_time of this ShowTaskInstanceMetricDataRequest.

        查询监控数据起始时间，UNIX时间戳，单位毫秒，不填时默认为当前时间

        :param from_time: The from_time of this ShowTaskInstanceMetricDataRequest.
        :type from_time: int
        """
        self._from_time = from_time

    @property
    def to_time(self):
        r"""Gets the to_time of this ShowTaskInstanceMetricDataRequest.

        查询监控数据截止时间，UNIX时间戳，单位毫秒，不填时默认为当前时间

        :return: The to_time of this ShowTaskInstanceMetricDataRequest.
        :rtype: int
        """
        return self._to_time

    @to_time.setter
    def to_time(self, to_time):
        r"""Sets the to_time of this ShowTaskInstanceMetricDataRequest.

        查询监控数据截止时间，UNIX时间戳，单位毫秒，不填时默认为当前时间

        :param to_time: The to_time of this ShowTaskInstanceMetricDataRequest.
        :type to_time: int
        """
        self._to_time = to_time

    @property
    def method(self):
        r"""Gets the method of this ShowTaskInstanceMetricDataRequest.

        统计方法。枚举值，取值范围：maximum（最大值）、minimum（最小值）、average（平均值），不填时默认为maximum

        :return: The method of this ShowTaskInstanceMetricDataRequest.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        r"""Sets the method of this ShowTaskInstanceMetricDataRequest.

        统计方法。枚举值，取值范围：maximum（最大值）、minimum（最小值）、average（平均值），不填时默认为maximum

        :param method: The method of this ShowTaskInstanceMetricDataRequest.
        :type method: str
        """
        self._method = method

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowTaskInstanceMetricDataRequest.

        查询的监控指标名称

        :return: The metric_name of this ShowTaskInstanceMetricDataRequest.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowTaskInstanceMetricDataRequest.

        查询的监控指标名称

        :param metric_name: The metric_name of this ShowTaskInstanceMetricDataRequest.
        :type metric_name: str
        """
        self._metric_name = metric_name

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
        if not isinstance(other, ShowTaskInstanceMetricDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
