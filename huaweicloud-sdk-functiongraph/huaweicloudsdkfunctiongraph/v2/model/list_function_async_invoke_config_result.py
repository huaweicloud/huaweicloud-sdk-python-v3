# coding: utf-8

import pprint
import re

import six





class ListFunctionAsyncInvokeConfigResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'func_urn': 'str',
        'max_async_event_age_in_seconds': 'int',
        'max_async_retry_attempts': 'int',
        'destination_config': 'FuncAsyncDestinationConfig',
        'created_time': 'str',
        'last_modified': 'str'
    }

    attribute_map = {
        'func_urn': 'func_urn',
        'max_async_event_age_in_seconds': 'max_async_event_age_in_seconds',
        'max_async_retry_attempts': 'max_async_retry_attempts',
        'destination_config': 'destination_config',
        'created_time': 'created_time',
        'last_modified': 'last_modified'
    }

    def __init__(self, func_urn=None, max_async_event_age_in_seconds=None, max_async_retry_attempts=None, destination_config=None, created_time=None, last_modified=None):
        """ListFunctionAsyncInvokeConfigResult - a model defined in huaweicloud sdk"""
        
        

        self._func_urn = None
        self._max_async_event_age_in_seconds = None
        self._max_async_retry_attempts = None
        self._destination_config = None
        self._created_time = None
        self._last_modified = None
        self.discriminator = None

        self.func_urn = func_urn
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        self.max_async_retry_attempts = max_async_retry_attempts
        self.destination_config = destination_config
        if created_time is not None:
            self.created_time = created_time
        if last_modified is not None:
            self.last_modified = last_modified

    @property
    def func_urn(self):
        """Gets the func_urn of this ListFunctionAsyncInvokeConfigResult.

        函数URN。

        :return: The func_urn of this ListFunctionAsyncInvokeConfigResult.
        :rtype: str
        """
        return self._func_urn

    @func_urn.setter
    def func_urn(self, func_urn):
        """Sets the func_urn of this ListFunctionAsyncInvokeConfigResult.

        函数URN。

        :param func_urn: The func_urn of this ListFunctionAsyncInvokeConfigResult.
        :type: str
        """
        self._func_urn = func_urn

    @property
    def max_async_event_age_in_seconds(self):
        """Gets the max_async_event_age_in_seconds of this ListFunctionAsyncInvokeConfigResult.

        消息最大存活时长，取值范围[60，86400]。单位：秒。

        :return: The max_async_event_age_in_seconds of this ListFunctionAsyncInvokeConfigResult.
        :rtype: int
        """
        return self._max_async_event_age_in_seconds

    @max_async_event_age_in_seconds.setter
    def max_async_event_age_in_seconds(self, max_async_event_age_in_seconds):
        """Sets the max_async_event_age_in_seconds of this ListFunctionAsyncInvokeConfigResult.

        消息最大存活时长，取值范围[60，86400]。单位：秒。

        :param max_async_event_age_in_seconds: The max_async_event_age_in_seconds of this ListFunctionAsyncInvokeConfigResult.
        :type: int
        """
        self._max_async_event_age_in_seconds = max_async_event_age_in_seconds

    @property
    def max_async_retry_attempts(self):
        """Gets the max_async_retry_attempts of this ListFunctionAsyncInvokeConfigResult.

        异步调用失败后的最大重试次数，默认值为3。取值范围[0，8]。

        :return: The max_async_retry_attempts of this ListFunctionAsyncInvokeConfigResult.
        :rtype: int
        """
        return self._max_async_retry_attempts

    @max_async_retry_attempts.setter
    def max_async_retry_attempts(self, max_async_retry_attempts):
        """Sets the max_async_retry_attempts of this ListFunctionAsyncInvokeConfigResult.

        异步调用失败后的最大重试次数，默认值为3。取值范围[0，8]。

        :param max_async_retry_attempts: The max_async_retry_attempts of this ListFunctionAsyncInvokeConfigResult.
        :type: int
        """
        self._max_async_retry_attempts = max_async_retry_attempts

    @property
    def destination_config(self):
        """Gets the destination_config of this ListFunctionAsyncInvokeConfigResult.


        :return: The destination_config of this ListFunctionAsyncInvokeConfigResult.
        :rtype: FuncAsyncDestinationConfig
        """
        return self._destination_config

    @destination_config.setter
    def destination_config(self, destination_config):
        """Sets the destination_config of this ListFunctionAsyncInvokeConfigResult.


        :param destination_config: The destination_config of this ListFunctionAsyncInvokeConfigResult.
        :type: FuncAsyncDestinationConfig
        """
        self._destination_config = destination_config

    @property
    def created_time(self):
        """Gets the created_time of this ListFunctionAsyncInvokeConfigResult.

        异步调用配置的创建时间。

        :return: The created_time of this ListFunctionAsyncInvokeConfigResult.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ListFunctionAsyncInvokeConfigResult.

        异步调用配置的创建时间。

        :param created_time: The created_time of this ListFunctionAsyncInvokeConfigResult.
        :type: str
        """
        self._created_time = created_time

    @property
    def last_modified(self):
        """Gets the last_modified of this ListFunctionAsyncInvokeConfigResult.

        异步调用配置的最后更改时间。

        :return: The last_modified of this ListFunctionAsyncInvokeConfigResult.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this ListFunctionAsyncInvokeConfigResult.

        异步调用配置的最后更改时间。

        :param last_modified: The last_modified of this ListFunctionAsyncInvokeConfigResult.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListFunctionAsyncInvokeConfigResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other