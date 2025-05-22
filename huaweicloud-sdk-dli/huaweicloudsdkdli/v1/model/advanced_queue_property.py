# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdvancedQueueProperty:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compute_engine_max_instance': 'int',
        'job_max_concurrent': 'int',
        'compute_engine_max_prefetch_instance': 'int',
        'compute_engine_spark_native_enabled': 'str',
        'network_cidr_in_vpc': 'str',
        'job_save_job_result_to_job_bucket': 'str'
    }

    attribute_map = {
        'compute_engine_max_instance': 'computeEngine.maxInstance',
        'job_max_concurrent': 'job.maxConcurrent',
        'compute_engine_max_prefetch_instance': 'computeEngine.maxPrefetchInstance',
        'compute_engine_spark_native_enabled': 'computeEngine.spark.nativeEnabled',
        'network_cidr_in_vpc': 'network.cidrInVpc',
        'job_save_job_result_to_job_bucket': 'job.saveJobResultToJobBucket'
    }

    def __init__(self, compute_engine_max_instance=None, job_max_concurrent=None, compute_engine_max_prefetch_instance=None, compute_engine_spark_native_enabled=None, network_cidr_in_vpc=None, job_save_job_result_to_job_bucket=None):
        r"""AdvancedQueueProperty

        The model defined in huaweicloud sdk

        :param compute_engine_max_instance: 队列能启动的最大spark driver数量
        :type compute_engine_max_instance: int
        :param job_max_concurrent: 单个spark driver能同时运行的最大任务数量
        :type job_max_concurrent: int
        :param compute_engine_max_prefetch_instance: 队列预先启动的最大spark driver数量
        :type compute_engine_max_prefetch_instance: int
        :param compute_engine_spark_native_enabled: 是否使用DLI Native。当前只涉及开启两种算子：Scan 和 Filter。修改现有队列的本属性，需要重启队列才会生效。
        :type compute_engine_spark_native_enabled: str
        :param network_cidr_in_vpc: 设置队列网段
        :type network_cidr_in_vpc: str
        :param job_save_job_result_to_job_bucket: 是否使用作业桶保存SQL查询结果
        :type job_save_job_result_to_job_bucket: str
        """
        
        

        self._compute_engine_max_instance = None
        self._job_max_concurrent = None
        self._compute_engine_max_prefetch_instance = None
        self._compute_engine_spark_native_enabled = None
        self._network_cidr_in_vpc = None
        self._job_save_job_result_to_job_bucket = None
        self.discriminator = None

        if compute_engine_max_instance is not None:
            self.compute_engine_max_instance = compute_engine_max_instance
        if job_max_concurrent is not None:
            self.job_max_concurrent = job_max_concurrent
        if compute_engine_max_prefetch_instance is not None:
            self.compute_engine_max_prefetch_instance = compute_engine_max_prefetch_instance
        if compute_engine_spark_native_enabled is not None:
            self.compute_engine_spark_native_enabled = compute_engine_spark_native_enabled
        if network_cidr_in_vpc is not None:
            self.network_cidr_in_vpc = network_cidr_in_vpc
        if job_save_job_result_to_job_bucket is not None:
            self.job_save_job_result_to_job_bucket = job_save_job_result_to_job_bucket

    @property
    def compute_engine_max_instance(self):
        r"""Gets the compute_engine_max_instance of this AdvancedQueueProperty.

        队列能启动的最大spark driver数量

        :return: The compute_engine_max_instance of this AdvancedQueueProperty.
        :rtype: int
        """
        return self._compute_engine_max_instance

    @compute_engine_max_instance.setter
    def compute_engine_max_instance(self, compute_engine_max_instance):
        r"""Sets the compute_engine_max_instance of this AdvancedQueueProperty.

        队列能启动的最大spark driver数量

        :param compute_engine_max_instance: The compute_engine_max_instance of this AdvancedQueueProperty.
        :type compute_engine_max_instance: int
        """
        self._compute_engine_max_instance = compute_engine_max_instance

    @property
    def job_max_concurrent(self):
        r"""Gets the job_max_concurrent of this AdvancedQueueProperty.

        单个spark driver能同时运行的最大任务数量

        :return: The job_max_concurrent of this AdvancedQueueProperty.
        :rtype: int
        """
        return self._job_max_concurrent

    @job_max_concurrent.setter
    def job_max_concurrent(self, job_max_concurrent):
        r"""Sets the job_max_concurrent of this AdvancedQueueProperty.

        单个spark driver能同时运行的最大任务数量

        :param job_max_concurrent: The job_max_concurrent of this AdvancedQueueProperty.
        :type job_max_concurrent: int
        """
        self._job_max_concurrent = job_max_concurrent

    @property
    def compute_engine_max_prefetch_instance(self):
        r"""Gets the compute_engine_max_prefetch_instance of this AdvancedQueueProperty.

        队列预先启动的最大spark driver数量

        :return: The compute_engine_max_prefetch_instance of this AdvancedQueueProperty.
        :rtype: int
        """
        return self._compute_engine_max_prefetch_instance

    @compute_engine_max_prefetch_instance.setter
    def compute_engine_max_prefetch_instance(self, compute_engine_max_prefetch_instance):
        r"""Sets the compute_engine_max_prefetch_instance of this AdvancedQueueProperty.

        队列预先启动的最大spark driver数量

        :param compute_engine_max_prefetch_instance: The compute_engine_max_prefetch_instance of this AdvancedQueueProperty.
        :type compute_engine_max_prefetch_instance: int
        """
        self._compute_engine_max_prefetch_instance = compute_engine_max_prefetch_instance

    @property
    def compute_engine_spark_native_enabled(self):
        r"""Gets the compute_engine_spark_native_enabled of this AdvancedQueueProperty.

        是否使用DLI Native。当前只涉及开启两种算子：Scan 和 Filter。修改现有队列的本属性，需要重启队列才会生效。

        :return: The compute_engine_spark_native_enabled of this AdvancedQueueProperty.
        :rtype: str
        """
        return self._compute_engine_spark_native_enabled

    @compute_engine_spark_native_enabled.setter
    def compute_engine_spark_native_enabled(self, compute_engine_spark_native_enabled):
        r"""Sets the compute_engine_spark_native_enabled of this AdvancedQueueProperty.

        是否使用DLI Native。当前只涉及开启两种算子：Scan 和 Filter。修改现有队列的本属性，需要重启队列才会生效。

        :param compute_engine_spark_native_enabled: The compute_engine_spark_native_enabled of this AdvancedQueueProperty.
        :type compute_engine_spark_native_enabled: str
        """
        self._compute_engine_spark_native_enabled = compute_engine_spark_native_enabled

    @property
    def network_cidr_in_vpc(self):
        r"""Gets the network_cidr_in_vpc of this AdvancedQueueProperty.

        设置队列网段

        :return: The network_cidr_in_vpc of this AdvancedQueueProperty.
        :rtype: str
        """
        return self._network_cidr_in_vpc

    @network_cidr_in_vpc.setter
    def network_cidr_in_vpc(self, network_cidr_in_vpc):
        r"""Sets the network_cidr_in_vpc of this AdvancedQueueProperty.

        设置队列网段

        :param network_cidr_in_vpc: The network_cidr_in_vpc of this AdvancedQueueProperty.
        :type network_cidr_in_vpc: str
        """
        self._network_cidr_in_vpc = network_cidr_in_vpc

    @property
    def job_save_job_result_to_job_bucket(self):
        r"""Gets the job_save_job_result_to_job_bucket of this AdvancedQueueProperty.

        是否使用作业桶保存SQL查询结果

        :return: The job_save_job_result_to_job_bucket of this AdvancedQueueProperty.
        :rtype: str
        """
        return self._job_save_job_result_to_job_bucket

    @job_save_job_result_to_job_bucket.setter
    def job_save_job_result_to_job_bucket(self, job_save_job_result_to_job_bucket):
        r"""Sets the job_save_job_result_to_job_bucket of this AdvancedQueueProperty.

        是否使用作业桶保存SQL查询结果

        :param job_save_job_result_to_job_bucket: The job_save_job_result_to_job_bucket of this AdvancedQueueProperty.
        :type job_save_job_result_to_job_bucket: str
        """
        self._job_save_job_result_to_job_bucket = job_save_job_result_to_job_bucket

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
        if not isinstance(other, AdvancedQueueProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
