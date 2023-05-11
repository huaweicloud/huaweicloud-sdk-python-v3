# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedistributionReq:

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
        'parallel_jobs': 'int'
    }

    attribute_map = {
        'redis_mode': 'redis_mode',
        'parallel_jobs': 'parallel_jobs'
    }

    def __init__(self, redis_mode=None, parallel_jobs=None):
        """RedistributionReq

        The model defined in huaweicloud sdk

        :param redis_mode: 重分布模式
        :type redis_mode: str
        :param parallel_jobs: 重分布并发数
        :type parallel_jobs: int
        """
        
        

        self._redis_mode = None
        self._parallel_jobs = None
        self.discriminator = None

        self.redis_mode = redis_mode
        self.parallel_jobs = parallel_jobs

    @property
    def redis_mode(self):
        """Gets the redis_mode of this RedistributionReq.

        重分布模式

        :return: The redis_mode of this RedistributionReq.
        :rtype: str
        """
        return self._redis_mode

    @redis_mode.setter
    def redis_mode(self, redis_mode):
        """Sets the redis_mode of this RedistributionReq.

        重分布模式

        :param redis_mode: The redis_mode of this RedistributionReq.
        :type redis_mode: str
        """
        self._redis_mode = redis_mode

    @property
    def parallel_jobs(self):
        """Gets the parallel_jobs of this RedistributionReq.

        重分布并发数

        :return: The parallel_jobs of this RedistributionReq.
        :rtype: int
        """
        return self._parallel_jobs

    @parallel_jobs.setter
    def parallel_jobs(self, parallel_jobs):
        """Sets the parallel_jobs of this RedistributionReq.

        重分布并发数

        :param parallel_jobs: The parallel_jobs of this RedistributionReq.
        :type parallel_jobs: int
        """
        self._parallel_jobs = parallel_jobs

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
        if not isinstance(other, RedistributionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
