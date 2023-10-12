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
        'parallel_job': 'int'
    }

    attribute_map = {
        'redis_mode': 'redis_mode',
        'schedule_conf': 'schedule_conf',
        'parallel_jobs': 'parallel_jobs',
        'parallel_job': 'parallel_job'
    }

    def __init__(self, redis_mode=None, schedule_conf=None, parallel_jobs=None, parallel_job=None):
        """RedisConf

        The model defined in huaweicloud sdk

        :param redis_mode: 重分布模式
        :type redis_mode: str
        :param schedule_conf: 
        :type schedule_conf: :class:`huaweicloudsdkdws.v2.ScheduleConf`
        :param parallel_jobs: 并行作业数量
        :type parallel_jobs: int
        :param parallel_job: 并行作业数量
        :type parallel_job: int
        """
        
        

        self._redis_mode = None
        self._schedule_conf = None
        self._parallel_jobs = None
        self._parallel_job = None
        self.discriminator = None

        self.redis_mode = redis_mode
        if schedule_conf is not None:
            self.schedule_conf = schedule_conf
        self.parallel_jobs = parallel_jobs
        self.parallel_job = parallel_job

    @property
    def redis_mode(self):
        """Gets the redis_mode of this RedisConf.

        重分布模式

        :return: The redis_mode of this RedisConf.
        :rtype: str
        """
        return self._redis_mode

    @redis_mode.setter
    def redis_mode(self, redis_mode):
        """Sets the redis_mode of this RedisConf.

        重分布模式

        :param redis_mode: The redis_mode of this RedisConf.
        :type redis_mode: str
        """
        self._redis_mode = redis_mode

    @property
    def schedule_conf(self):
        """Gets the schedule_conf of this RedisConf.

        :return: The schedule_conf of this RedisConf.
        :rtype: :class:`huaweicloudsdkdws.v2.ScheduleConf`
        """
        return self._schedule_conf

    @schedule_conf.setter
    def schedule_conf(self, schedule_conf):
        """Sets the schedule_conf of this RedisConf.

        :param schedule_conf: The schedule_conf of this RedisConf.
        :type schedule_conf: :class:`huaweicloudsdkdws.v2.ScheduleConf`
        """
        self._schedule_conf = schedule_conf

    @property
    def parallel_jobs(self):
        """Gets the parallel_jobs of this RedisConf.

        并行作业数量

        :return: The parallel_jobs of this RedisConf.
        :rtype: int
        """
        return self._parallel_jobs

    @parallel_jobs.setter
    def parallel_jobs(self, parallel_jobs):
        """Sets the parallel_jobs of this RedisConf.

        并行作业数量

        :param parallel_jobs: The parallel_jobs of this RedisConf.
        :type parallel_jobs: int
        """
        self._parallel_jobs = parallel_jobs

    @property
    def parallel_job(self):
        """Gets the parallel_job of this RedisConf.

        并行作业数量

        :return: The parallel_job of this RedisConf.
        :rtype: int
        """
        return self._parallel_job

    @parallel_job.setter
    def parallel_job(self, parallel_job):
        """Sets the parallel_job of this RedisConf.

        并行作业数量

        :param parallel_job: The parallel_job of this RedisConf.
        :type parallel_job: int
        """
        self._parallel_job = parallel_job

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
