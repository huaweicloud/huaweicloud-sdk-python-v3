# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FunctionAsyncConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_async_event_age_in_seconds': 'int',
        'max_async_retry_attempts': 'int',
        'destination_config': 'FuncAsyncDestinationConfig',
        'created_time': 'str',
        'last_modified': 'str'
    }

    attribute_map = {
        'max_async_event_age_in_seconds': 'max_async_event_age_in_seconds',
        'max_async_retry_attempts': 'max_async_retry_attempts',
        'destination_config': 'destination_config',
        'created_time': 'created_time',
        'last_modified': 'last_modified'
    }

    def __init__(self, max_async_event_age_in_seconds=None, max_async_retry_attempts=None, destination_config=None, created_time=None, last_modified=None):
        """FunctionAsyncConfig

        The model defined in huaweicloud sdk

        :param max_async_event_age_in_seconds: 消息最大存活时长，取值范围[60，86400]。单位：秒。
        :type max_async_event_age_in_seconds: int
        :param max_async_retry_attempts: 异步调用失败后的最大重试次数，默认值为3。取值范围[0，8]。
        :type max_async_retry_attempts: int
        :param destination_config: 
        :type destination_config: :class:`huaweicloudsdkfunctiongraph.v2.FuncAsyncDestinationConfig`
        :param created_time: 异步调用配置的创建时间。
        :type created_time: str
        :param last_modified: 异步调用配置的最后更改时间。
        :type last_modified: str
        """
        
        

        self._max_async_event_age_in_seconds = None
        self._max_async_retry_attempts = None
        self._destination_config = None
        self._created_time = None
        self._last_modified = None
        self.discriminator = None

        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        self.max_async_retry_attempts = max_async_retry_attempts
        self.destination_config = destination_config
        if created_time is not None:
            self.created_time = created_time
        if last_modified is not None:
            self.last_modified = last_modified

    @property
    def max_async_event_age_in_seconds(self):
        """Gets the max_async_event_age_in_seconds of this FunctionAsyncConfig.

        消息最大存活时长，取值范围[60，86400]。单位：秒。

        :return: The max_async_event_age_in_seconds of this FunctionAsyncConfig.
        :rtype: int
        """
        return self._max_async_event_age_in_seconds

    @max_async_event_age_in_seconds.setter
    def max_async_event_age_in_seconds(self, max_async_event_age_in_seconds):
        """Sets the max_async_event_age_in_seconds of this FunctionAsyncConfig.

        消息最大存活时长，取值范围[60，86400]。单位：秒。

        :param max_async_event_age_in_seconds: The max_async_event_age_in_seconds of this FunctionAsyncConfig.
        :type max_async_event_age_in_seconds: int
        """
        self._max_async_event_age_in_seconds = max_async_event_age_in_seconds

    @property
    def max_async_retry_attempts(self):
        """Gets the max_async_retry_attempts of this FunctionAsyncConfig.

        异步调用失败后的最大重试次数，默认值为3。取值范围[0，8]。

        :return: The max_async_retry_attempts of this FunctionAsyncConfig.
        :rtype: int
        """
        return self._max_async_retry_attempts

    @max_async_retry_attempts.setter
    def max_async_retry_attempts(self, max_async_retry_attempts):
        """Sets the max_async_retry_attempts of this FunctionAsyncConfig.

        异步调用失败后的最大重试次数，默认值为3。取值范围[0，8]。

        :param max_async_retry_attempts: The max_async_retry_attempts of this FunctionAsyncConfig.
        :type max_async_retry_attempts: int
        """
        self._max_async_retry_attempts = max_async_retry_attempts

    @property
    def destination_config(self):
        """Gets the destination_config of this FunctionAsyncConfig.

        :return: The destination_config of this FunctionAsyncConfig.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FuncAsyncDestinationConfig`
        """
        return self._destination_config

    @destination_config.setter
    def destination_config(self, destination_config):
        """Sets the destination_config of this FunctionAsyncConfig.

        :param destination_config: The destination_config of this FunctionAsyncConfig.
        :type destination_config: :class:`huaweicloudsdkfunctiongraph.v2.FuncAsyncDestinationConfig`
        """
        self._destination_config = destination_config

    @property
    def created_time(self):
        """Gets the created_time of this FunctionAsyncConfig.

        异步调用配置的创建时间。

        :return: The created_time of this FunctionAsyncConfig.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this FunctionAsyncConfig.

        异步调用配置的创建时间。

        :param created_time: The created_time of this FunctionAsyncConfig.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def last_modified(self):
        """Gets the last_modified of this FunctionAsyncConfig.

        异步调用配置的最后更改时间。

        :return: The last_modified of this FunctionAsyncConfig.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this FunctionAsyncConfig.

        异步调用配置的最后更改时间。

        :param last_modified: The last_modified of this FunctionAsyncConfig.
        :type last_modified: str
        """
        self._last_modified = last_modified

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
        if not isinstance(other, FunctionAsyncConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
