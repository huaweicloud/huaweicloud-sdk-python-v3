# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ray_job_config': 'RayJobConfig',
        'python_job_config': 'PythonJobConfig',
        'spark_job_config': 'SparkJobConfig',
        'timeout_seconds': 'int',
        'max_retries': 'int',
        'queue': 'bool',
        'max_concurrent_runs': 'int'
    }

    attribute_map = {
        'ray_job_config': 'ray_job_config',
        'python_job_config': 'python_job_config',
        'spark_job_config': 'spark_job_config',
        'timeout_seconds': 'timeout_seconds',
        'max_retries': 'max_retries',
        'queue': 'queue',
        'max_concurrent_runs': 'max_concurrent_runs'
    }

    def __init__(self, ray_job_config=None, python_job_config=None, spark_job_config=None, timeout_seconds=None, max_retries=None, queue=None, max_concurrent_runs=None):
        r"""JobConfig

        The model defined in huaweicloud sdk

        :param ray_job_config: 
        :type ray_job_config: :class:`huaweicloudsdkdataartsfabric.v1.RayJobConfig`
        :param python_job_config: 
        :type python_job_config: :class:`huaweicloudsdkdataartsfabric.v1.PythonJobConfig`
        :param spark_job_config: 
        :type spark_job_config: :class:`huaweicloudsdkdataartsfabric.v1.SparkJobConfig`
        :param timeout_seconds: 超时时间，即最长运行时间,超过该事件则终止。   可选，默认值为0，值0表示没有超时。
        :type timeout_seconds: int
        :param max_retries: 运行重试次数
        :type max_retries: int
        :param queue: 作业是否排队。 true: 排队 false：不排队
        :type queue: bool
        :param max_concurrent_runs: 作业允许的最大并发运行数可选。 Default: 1
        :type max_concurrent_runs: int
        """
        
        

        self._ray_job_config = None
        self._python_job_config = None
        self._spark_job_config = None
        self._timeout_seconds = None
        self._max_retries = None
        self._queue = None
        self._max_concurrent_runs = None
        self.discriminator = None

        if ray_job_config is not None:
            self.ray_job_config = ray_job_config
        if python_job_config is not None:
            self.python_job_config = python_job_config
        if spark_job_config is not None:
            self.spark_job_config = spark_job_config
        if timeout_seconds is not None:
            self.timeout_seconds = timeout_seconds
        if max_retries is not None:
            self.max_retries = max_retries
        if queue is not None:
            self.queue = queue
        if max_concurrent_runs is not None:
            self.max_concurrent_runs = max_concurrent_runs

    @property
    def ray_job_config(self):
        r"""Gets the ray_job_config of this JobConfig.

        :return: The ray_job_config of this JobConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.RayJobConfig`
        """
        return self._ray_job_config

    @ray_job_config.setter
    def ray_job_config(self, ray_job_config):
        r"""Sets the ray_job_config of this JobConfig.

        :param ray_job_config: The ray_job_config of this JobConfig.
        :type ray_job_config: :class:`huaweicloudsdkdataartsfabric.v1.RayJobConfig`
        """
        self._ray_job_config = ray_job_config

    @property
    def python_job_config(self):
        r"""Gets the python_job_config of this JobConfig.

        :return: The python_job_config of this JobConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.PythonJobConfig`
        """
        return self._python_job_config

    @python_job_config.setter
    def python_job_config(self, python_job_config):
        r"""Sets the python_job_config of this JobConfig.

        :param python_job_config: The python_job_config of this JobConfig.
        :type python_job_config: :class:`huaweicloudsdkdataartsfabric.v1.PythonJobConfig`
        """
        self._python_job_config = python_job_config

    @property
    def spark_job_config(self):
        r"""Gets the spark_job_config of this JobConfig.

        :return: The spark_job_config of this JobConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.SparkJobConfig`
        """
        return self._spark_job_config

    @spark_job_config.setter
    def spark_job_config(self, spark_job_config):
        r"""Sets the spark_job_config of this JobConfig.

        :param spark_job_config: The spark_job_config of this JobConfig.
        :type spark_job_config: :class:`huaweicloudsdkdataartsfabric.v1.SparkJobConfig`
        """
        self._spark_job_config = spark_job_config

    @property
    def timeout_seconds(self):
        r"""Gets the timeout_seconds of this JobConfig.

        超时时间，即最长运行时间,超过该事件则终止。   可选，默认值为0，值0表示没有超时。

        :return: The timeout_seconds of this JobConfig.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        r"""Sets the timeout_seconds of this JobConfig.

        超时时间，即最长运行时间,超过该事件则终止。   可选，默认值为0，值0表示没有超时。

        :param timeout_seconds: The timeout_seconds of this JobConfig.
        :type timeout_seconds: int
        """
        self._timeout_seconds = timeout_seconds

    @property
    def max_retries(self):
        r"""Gets the max_retries of this JobConfig.

        运行重试次数

        :return: The max_retries of this JobConfig.
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        r"""Sets the max_retries of this JobConfig.

        运行重试次数

        :param max_retries: The max_retries of this JobConfig.
        :type max_retries: int
        """
        self._max_retries = max_retries

    @property
    def queue(self):
        r"""Gets the queue of this JobConfig.

        作业是否排队。 true: 排队 false：不排队

        :return: The queue of this JobConfig.
        :rtype: bool
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        r"""Sets the queue of this JobConfig.

        作业是否排队。 true: 排队 false：不排队

        :param queue: The queue of this JobConfig.
        :type queue: bool
        """
        self._queue = queue

    @property
    def max_concurrent_runs(self):
        r"""Gets the max_concurrent_runs of this JobConfig.

        作业允许的最大并发运行数可选。 Default: 1

        :return: The max_concurrent_runs of this JobConfig.
        :rtype: int
        """
        return self._max_concurrent_runs

    @max_concurrent_runs.setter
    def max_concurrent_runs(self, max_concurrent_runs):
        r"""Sets the max_concurrent_runs of this JobConfig.

        作业允许的最大并发运行数可选。 Default: 1

        :param max_concurrent_runs: The max_concurrent_runs of this JobConfig.
        :type max_concurrent_runs: int
        """
        self._max_concurrent_runs = max_concurrent_runs

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
        if not isinstance(other, JobConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
