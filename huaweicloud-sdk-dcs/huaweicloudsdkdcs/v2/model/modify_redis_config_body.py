# coding: utf-8

import pprint
import re

import six





class ModifyRedisConfigBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'redis_config': 'list[RedisConfig]'
    }

    attribute_map = {
        'redis_config': 'redis_config'
    }

    def __init__(self, redis_config=None):
        """ModifyRedisConfigBody - a model defined in huaweicloud sdk"""
        
        

        self._redis_config = None
        self.discriminator = None

        if redis_config is not None:
            self.redis_config = redis_config

    @property
    def redis_config(self):
        """Gets the redis_config of this ModifyRedisConfigBody.

        实例配置项数组。

        :return: The redis_config of this ModifyRedisConfigBody.
        :rtype: list[RedisConfig]
        """
        return self._redis_config

    @redis_config.setter
    def redis_config(self, redis_config):
        """Sets the redis_config of this ModifyRedisConfigBody.

        实例配置项数组。

        :param redis_config: The redis_config of this ModifyRedisConfigBody.
        :type: list[RedisConfig]
        """
        self._redis_config = redis_config

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModifyRedisConfigBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
