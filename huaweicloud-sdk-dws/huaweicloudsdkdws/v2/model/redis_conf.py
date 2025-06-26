# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedisConf:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'redis_mode': 'str',
        'schedule_conf': 'ScheduleConf',
        'parallel_jobs': 'int',
        'parallel_job': 'int',
        'priority_policy': 'str',
        'bucket_split_info': 'BucketSplitInfo'
    }

    attribute_map = {
        'redis_mode': 'redis_mode',
        'schedule_conf': 'schedule_conf',
        'parallel_jobs': 'parallel_jobs',
        'parallel_job': 'parallel_job',
        'priority_policy': 'priority_policy',
        'bucket_split_info': 'bucket_split_info'
    }

    def __init__(self, redis_mode=None, schedule_conf=None, parallel_jobs=None, parallel_job=None, priority_policy=None, bucket_split_info=None):
        r"""RedisConf

        The model defined in huaweicloud sdk

        :param redis_mode: **参数解释**： 重分布模式。 **取值范围**： online|offline。
        :type redis_mode: str
        :param schedule_conf: 
        :type schedule_conf: :class:`huaweicloudsdkdws.v2.ScheduleConf`
        :param parallel_jobs: **参数解释**： 重分布并发数。 **取值范围**： 1~200。
        :type parallel_jobs: int
        :param parallel_job: **参数解释**： 重分布并发数，已经废弃。 **取值范围**： 1~200。
        :type parallel_job: int
        :param priority_policy: **参数解释**： 优先级策略。 **取值范围**： large：优先对大表进行重分布。 small：优先对小表进行重分布 default：默认顺序进行重分布。
        :type priority_policy: str
        :param bucket_split_info: 
        :type bucket_split_info: :class:`huaweicloudsdkdws.v2.BucketSplitInfo`
        """
        
        

        self._redis_mode = None
        self._schedule_conf = None
        self._parallel_jobs = None
        self._parallel_job = None
        self._priority_policy = None
        self._bucket_split_info = None
        self.discriminator = None

        self.redis_mode = redis_mode
        if schedule_conf is not None:
            self.schedule_conf = schedule_conf
        self.parallel_jobs = parallel_jobs
        self.parallel_job = parallel_job
        if priority_policy is not None:
            self.priority_policy = priority_policy
        if bucket_split_info is not None:
            self.bucket_split_info = bucket_split_info

    @property
    def redis_mode(self):
        r"""Gets the redis_mode of this RedisConf.

        **参数解释**： 重分布模式。 **取值范围**： online|offline。

        :return: The redis_mode of this RedisConf.
        :rtype: str
        """
        return self._redis_mode

    @redis_mode.setter
    def redis_mode(self, redis_mode):
        r"""Sets the redis_mode of this RedisConf.

        **参数解释**： 重分布模式。 **取值范围**： online|offline。

        :param redis_mode: The redis_mode of this RedisConf.
        :type redis_mode: str
        """
        self._redis_mode = redis_mode

    @property
    def schedule_conf(self):
        r"""Gets the schedule_conf of this RedisConf.

        :return: The schedule_conf of this RedisConf.
        :rtype: :class:`huaweicloudsdkdws.v2.ScheduleConf`
        """
        return self._schedule_conf

    @schedule_conf.setter
    def schedule_conf(self, schedule_conf):
        r"""Sets the schedule_conf of this RedisConf.

        :param schedule_conf: The schedule_conf of this RedisConf.
        :type schedule_conf: :class:`huaweicloudsdkdws.v2.ScheduleConf`
        """
        self._schedule_conf = schedule_conf

    @property
    def parallel_jobs(self):
        r"""Gets the parallel_jobs of this RedisConf.

        **参数解释**： 重分布并发数。 **取值范围**： 1~200。

        :return: The parallel_jobs of this RedisConf.
        :rtype: int
        """
        return self._parallel_jobs

    @parallel_jobs.setter
    def parallel_jobs(self, parallel_jobs):
        r"""Sets the parallel_jobs of this RedisConf.

        **参数解释**： 重分布并发数。 **取值范围**： 1~200。

        :param parallel_jobs: The parallel_jobs of this RedisConf.
        :type parallel_jobs: int
        """
        self._parallel_jobs = parallel_jobs

    @property
    def parallel_job(self):
        r"""Gets the parallel_job of this RedisConf.

        **参数解释**： 重分布并发数，已经废弃。 **取值范围**： 1~200。

        :return: The parallel_job of this RedisConf.
        :rtype: int
        """
        return self._parallel_job

    @parallel_job.setter
    def parallel_job(self, parallel_job):
        r"""Sets the parallel_job of this RedisConf.

        **参数解释**： 重分布并发数，已经废弃。 **取值范围**： 1~200。

        :param parallel_job: The parallel_job of this RedisConf.
        :type parallel_job: int
        """
        self._parallel_job = parallel_job

    @property
    def priority_policy(self):
        r"""Gets the priority_policy of this RedisConf.

        **参数解释**： 优先级策略。 **取值范围**： large：优先对大表进行重分布。 small：优先对小表进行重分布 default：默认顺序进行重分布。

        :return: The priority_policy of this RedisConf.
        :rtype: str
        """
        return self._priority_policy

    @priority_policy.setter
    def priority_policy(self, priority_policy):
        r"""Sets the priority_policy of this RedisConf.

        **参数解释**： 优先级策略。 **取值范围**： large：优先对大表进行重分布。 small：优先对小表进行重分布 default：默认顺序进行重分布。

        :param priority_policy: The priority_policy of this RedisConf.
        :type priority_policy: str
        """
        self._priority_policy = priority_policy

    @property
    def bucket_split_info(self):
        r"""Gets the bucket_split_info of this RedisConf.

        :return: The bucket_split_info of this RedisConf.
        :rtype: :class:`huaweicloudsdkdws.v2.BucketSplitInfo`
        """
        return self._bucket_split_info

    @bucket_split_info.setter
    def bucket_split_info(self, bucket_split_info):
        r"""Sets the bucket_split_info of this RedisConf.

        :param bucket_split_info: The bucket_split_info of this RedisConf.
        :type bucket_split_info: :class:`huaweicloudsdkdws.v2.BucketSplitInfo`
        """
        self._bucket_split_info = bucket_split_info

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
        if not isinstance(other, RedisConf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
