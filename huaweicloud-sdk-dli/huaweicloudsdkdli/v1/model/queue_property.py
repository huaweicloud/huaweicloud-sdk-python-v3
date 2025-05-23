# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueueProperty:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, key=None, value=None):
        r"""QueueProperty

        The model defined in huaweicloud sdk

        :param key: 返回属性值对应的key值: computeEngine.maxInstances, 队列能启动的最大spark driver数量; computeEngine.maxPrefetchInstance, 队列预先启动的最大spark driver数量; job.maxConcurrent,单个spark driver能同时运行的最大任务数量; multipleSc.support,是否支持设置多个spark driver; job.saveJobResultToJobBucket, 是否使用作业桶保存SQL查询结果，true代表开启; computeEngine.spark.nativeEnabled, 是否使用DLI Native;
        :type key: str
        :param value: 
        :type value: str
        """
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value = value

    @property
    def key(self):
        r"""Gets the key of this QueueProperty.

        返回属性值对应的key值: computeEngine.maxInstances, 队列能启动的最大spark driver数量; computeEngine.maxPrefetchInstance, 队列预先启动的最大spark driver数量; job.maxConcurrent,单个spark driver能同时运行的最大任务数量; multipleSc.support,是否支持设置多个spark driver; job.saveJobResultToJobBucket, 是否使用作业桶保存SQL查询结果，true代表开启; computeEngine.spark.nativeEnabled, 是否使用DLI Native;

        :return: The key of this QueueProperty.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this QueueProperty.

        返回属性值对应的key值: computeEngine.maxInstances, 队列能启动的最大spark driver数量; computeEngine.maxPrefetchInstance, 队列预先启动的最大spark driver数量; job.maxConcurrent,单个spark driver能同时运行的最大任务数量; multipleSc.support,是否支持设置多个spark driver; job.saveJobResultToJobBucket, 是否使用作业桶保存SQL查询结果，true代表开启; computeEngine.spark.nativeEnabled, 是否使用DLI Native;

        :param key: The key of this QueueProperty.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this QueueProperty.

        :return: The value of this QueueProperty.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this QueueProperty.

        :param value: The value of this QueueProperty.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, QueueProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
