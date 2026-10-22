# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkSchedulingConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_concurrent_jobs': 'int',
        'scheduling_policy': 'str',
        'fifo_tolerance_seconds': 'int'
    }

    attribute_map = {
        'max_concurrent_jobs': 'max_concurrent_jobs',
        'scheduling_policy': 'scheduling_policy',
        'fifo_tolerance_seconds': 'fifo_tolerance_seconds'
    }

    def __init__(self, max_concurrent_jobs=None, scheduling_policy=None, fifo_tolerance_seconds=None):
        r"""SparkSchedulingConfig

        The model defined in huaweicloud sdk

        :param max_concurrent_jobs: **参数解释**：端点最大并发作业数量。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：200。 
        :type max_concurrent_jobs: int
        :param scheduling_policy: **参数解释**：作业调度策略，支持随机和先进先出。 **约束限制**：不涉及。 **取值范围**： - RANDOM：随机。 - FIFO：先进先出。 **默认取值**：RANDOM。 
        :type scheduling_policy: str
        :param fifo_tolerance_seconds: **参数解释**：FIFO允许并发时间（秒）。 **约束限制**：不涉及。 **取值范围**：0~3600。 **默认取值**：300。 
        :type fifo_tolerance_seconds: int
        """
        
        

        self._max_concurrent_jobs = None
        self._scheduling_policy = None
        self._fifo_tolerance_seconds = None
        self.discriminator = None

        if max_concurrent_jobs is not None:
            self.max_concurrent_jobs = max_concurrent_jobs
        if scheduling_policy is not None:
            self.scheduling_policy = scheduling_policy
        if fifo_tolerance_seconds is not None:
            self.fifo_tolerance_seconds = fifo_tolerance_seconds

    @property
    def max_concurrent_jobs(self):
        r"""Gets the max_concurrent_jobs of this SparkSchedulingConfig.

        **参数解释**：端点最大并发作业数量。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：200。 

        :return: The max_concurrent_jobs of this SparkSchedulingConfig.
        :rtype: int
        """
        return self._max_concurrent_jobs

    @max_concurrent_jobs.setter
    def max_concurrent_jobs(self, max_concurrent_jobs):
        r"""Sets the max_concurrent_jobs of this SparkSchedulingConfig.

        **参数解释**：端点最大并发作业数量。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：200。 

        :param max_concurrent_jobs: The max_concurrent_jobs of this SparkSchedulingConfig.
        :type max_concurrent_jobs: int
        """
        self._max_concurrent_jobs = max_concurrent_jobs

    @property
    def scheduling_policy(self):
        r"""Gets the scheduling_policy of this SparkSchedulingConfig.

        **参数解释**：作业调度策略，支持随机和先进先出。 **约束限制**：不涉及。 **取值范围**： - RANDOM：随机。 - FIFO：先进先出。 **默认取值**：RANDOM。 

        :return: The scheduling_policy of this SparkSchedulingConfig.
        :rtype: str
        """
        return self._scheduling_policy

    @scheduling_policy.setter
    def scheduling_policy(self, scheduling_policy):
        r"""Sets the scheduling_policy of this SparkSchedulingConfig.

        **参数解释**：作业调度策略，支持随机和先进先出。 **约束限制**：不涉及。 **取值范围**： - RANDOM：随机。 - FIFO：先进先出。 **默认取值**：RANDOM。 

        :param scheduling_policy: The scheduling_policy of this SparkSchedulingConfig.
        :type scheduling_policy: str
        """
        self._scheduling_policy = scheduling_policy

    @property
    def fifo_tolerance_seconds(self):
        r"""Gets the fifo_tolerance_seconds of this SparkSchedulingConfig.

        **参数解释**：FIFO允许并发时间（秒）。 **约束限制**：不涉及。 **取值范围**：0~3600。 **默认取值**：300。 

        :return: The fifo_tolerance_seconds of this SparkSchedulingConfig.
        :rtype: int
        """
        return self._fifo_tolerance_seconds

    @fifo_tolerance_seconds.setter
    def fifo_tolerance_seconds(self, fifo_tolerance_seconds):
        r"""Sets the fifo_tolerance_seconds of this SparkSchedulingConfig.

        **参数解释**：FIFO允许并发时间（秒）。 **约束限制**：不涉及。 **取值范围**：0~3600。 **默认取值**：300。 

        :param fifo_tolerance_seconds: The fifo_tolerance_seconds of this SparkSchedulingConfig.
        :type fifo_tolerance_seconds: int
        """
        self._fifo_tolerance_seconds = fifo_tolerance_seconds

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
        if not isinstance(other, SparkSchedulingConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
