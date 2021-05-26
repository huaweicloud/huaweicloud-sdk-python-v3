# coding: utf-8

import pprint
import re

import six





class UpdateFunctionAsyncInvokeConfigRequestBody:


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
        'destination_config': 'FuncAsyncDestinationConfig'
    }

    attribute_map = {
        'max_async_event_age_in_seconds': 'max_async_event_age_in_seconds',
        'max_async_retry_attempts': 'max_async_retry_attempts',
        'destination_config': 'destination_config'
    }

    def __init__(self, max_async_event_age_in_seconds=None, max_async_retry_attempts=None, destination_config=None):
        """UpdateFunctionAsyncInvokeConfigRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._max_async_event_age_in_seconds = None
        self._max_async_retry_attempts = None
        self._destination_config = None
        self.discriminator = None

        if max_async_event_age_in_seconds is not None:
            self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        if max_async_retry_attempts is not None:
            self.max_async_retry_attempts = max_async_retry_attempts
        if destination_config is not None:
            self.destination_config = destination_config

    @property
    def max_async_event_age_in_seconds(self):
        """Gets the max_async_event_age_in_seconds of this UpdateFunctionAsyncInvokeConfigRequestBody.

        消息最大存活时长，取值范围[1，86400]，单位：秒，默认值为3600。

        :return: The max_async_event_age_in_seconds of this UpdateFunctionAsyncInvokeConfigRequestBody.
        :rtype: int
        """
        return self._max_async_event_age_in_seconds

    @max_async_event_age_in_seconds.setter
    def max_async_event_age_in_seconds(self, max_async_event_age_in_seconds):
        """Sets the max_async_event_age_in_seconds of this UpdateFunctionAsyncInvokeConfigRequestBody.

        消息最大存活时长，取值范围[1，86400]，单位：秒，默认值为3600。

        :param max_async_event_age_in_seconds: The max_async_event_age_in_seconds of this UpdateFunctionAsyncInvokeConfigRequestBody.
        :type: int
        """
        self._max_async_event_age_in_seconds = max_async_event_age_in_seconds

    @property
    def max_async_retry_attempts(self):
        """Gets the max_async_retry_attempts of this UpdateFunctionAsyncInvokeConfigRequestBody.

        异步调用失败后的最大重试次数，默认值为1。取值范围[0，3]。

        :return: The max_async_retry_attempts of this UpdateFunctionAsyncInvokeConfigRequestBody.
        :rtype: int
        """
        return self._max_async_retry_attempts

    @max_async_retry_attempts.setter
    def max_async_retry_attempts(self, max_async_retry_attempts):
        """Sets the max_async_retry_attempts of this UpdateFunctionAsyncInvokeConfigRequestBody.

        异步调用失败后的最大重试次数，默认值为1。取值范围[0，3]。

        :param max_async_retry_attempts: The max_async_retry_attempts of this UpdateFunctionAsyncInvokeConfigRequestBody.
        :type: int
        """
        self._max_async_retry_attempts = max_async_retry_attempts

    @property
    def destination_config(self):
        """Gets the destination_config of this UpdateFunctionAsyncInvokeConfigRequestBody.


        :return: The destination_config of this UpdateFunctionAsyncInvokeConfigRequestBody.
        :rtype: FuncAsyncDestinationConfig
        """
        return self._destination_config

    @destination_config.setter
    def destination_config(self, destination_config):
        """Sets the destination_config of this UpdateFunctionAsyncInvokeConfigRequestBody.


        :param destination_config: The destination_config of this UpdateFunctionAsyncInvokeConfigRequestBody.
        :type: FuncAsyncDestinationConfig
        """
        self._destination_config = destination_config

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
        if not isinstance(other, UpdateFunctionAsyncInvokeConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
