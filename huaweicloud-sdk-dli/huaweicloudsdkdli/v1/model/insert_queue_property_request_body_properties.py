# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InsertQueuePropertyRequestBodyProperties:

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
        'compute_engine_max_prefetch_instance': 'int'
    }

    attribute_map = {
        'compute_engine_max_instance': 'computeEngine.maxInstance',
        'job_max_concurrent': 'job.maxConcurrent',
        'compute_engine_max_prefetch_instance': 'computeEngine.maxPrefetchInstance'
    }

    def __init__(self, compute_engine_max_instance=None, job_max_concurrent=None, compute_engine_max_prefetch_instance=None):
        """InsertQueuePropertyRequestBodyProperties

        The model defined in huaweicloud sdk

        :param compute_engine_max_instance: 队列能启动的最大spark driver数量
        :type compute_engine_max_instance: int
        :param job_max_concurrent: 单个spark driver能同时运行的最大任务数量
        :type job_max_concurrent: int
        :param compute_engine_max_prefetch_instance: 队列预先启动的最大spark driver数量
        :type compute_engine_max_prefetch_instance: int
        """
        
        

        self._compute_engine_max_instance = None
        self._job_max_concurrent = None
        self._compute_engine_max_prefetch_instance = None
        self.discriminator = None

        if compute_engine_max_instance is not None:
            self.compute_engine_max_instance = compute_engine_max_instance
        if job_max_concurrent is not None:
            self.job_max_concurrent = job_max_concurrent
        if compute_engine_max_prefetch_instance is not None:
            self.compute_engine_max_prefetch_instance = compute_engine_max_prefetch_instance

    @property
    def compute_engine_max_instance(self):
        """Gets the compute_engine_max_instance of this InsertQueuePropertyRequestBodyProperties.

        队列能启动的最大spark driver数量

        :return: The compute_engine_max_instance of this InsertQueuePropertyRequestBodyProperties.
        :rtype: int
        """
        return self._compute_engine_max_instance

    @compute_engine_max_instance.setter
    def compute_engine_max_instance(self, compute_engine_max_instance):
        """Sets the compute_engine_max_instance of this InsertQueuePropertyRequestBodyProperties.

        队列能启动的最大spark driver数量

        :param compute_engine_max_instance: The compute_engine_max_instance of this InsertQueuePropertyRequestBodyProperties.
        :type compute_engine_max_instance: int
        """
        self._compute_engine_max_instance = compute_engine_max_instance

    @property
    def job_max_concurrent(self):
        """Gets the job_max_concurrent of this InsertQueuePropertyRequestBodyProperties.

        单个spark driver能同时运行的最大任务数量

        :return: The job_max_concurrent of this InsertQueuePropertyRequestBodyProperties.
        :rtype: int
        """
        return self._job_max_concurrent

    @job_max_concurrent.setter
    def job_max_concurrent(self, job_max_concurrent):
        """Sets the job_max_concurrent of this InsertQueuePropertyRequestBodyProperties.

        单个spark driver能同时运行的最大任务数量

        :param job_max_concurrent: The job_max_concurrent of this InsertQueuePropertyRequestBodyProperties.
        :type job_max_concurrent: int
        """
        self._job_max_concurrent = job_max_concurrent

    @property
    def compute_engine_max_prefetch_instance(self):
        """Gets the compute_engine_max_prefetch_instance of this InsertQueuePropertyRequestBodyProperties.

        队列预先启动的最大spark driver数量

        :return: The compute_engine_max_prefetch_instance of this InsertQueuePropertyRequestBodyProperties.
        :rtype: int
        """
        return self._compute_engine_max_prefetch_instance

    @compute_engine_max_prefetch_instance.setter
    def compute_engine_max_prefetch_instance(self, compute_engine_max_prefetch_instance):
        """Sets the compute_engine_max_prefetch_instance of this InsertQueuePropertyRequestBodyProperties.

        队列预先启动的最大spark driver数量

        :param compute_engine_max_prefetch_instance: The compute_engine_max_prefetch_instance of this InsertQueuePropertyRequestBodyProperties.
        :type compute_engine_max_prefetch_instance: int
        """
        self._compute_engine_max_prefetch_instance = compute_engine_max_prefetch_instance

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
        if not isinstance(other, InsertQueuePropertyRequestBodyProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
