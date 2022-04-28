# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'destination_config': 'FuncAsyncDestinationConfig',
        'enable_async_status_log': 'bool'
    }

    attribute_map = {
        'max_async_event_age_in_seconds': 'max_async_event_age_in_seconds',
        'max_async_retry_attempts': 'max_async_retry_attempts',
        'destination_config': 'destination_config',
        'enable_async_status_log': 'enable_async_status_log'
    }

    def __init__(self, max_async_event_age_in_seconds=None, max_async_retry_attempts=None, destination_config=None, enable_async_status_log=None):
        """UpdateFunctionAsyncInvokeConfigRequestBody

        The model defined in huaweicloud sdk

        :param max_async_event_age_in_seconds: 消息最大存活时长，取值范围[1，86400]，单位：秒，默认值为3600。
        :type max_async_event_age_in_seconds: int
        :param max_async_retry_attempts: 异步调用失败后的最大重试次数，默认值为1。取值范围[0，3]。
        :type max_async_retry_attempts: int
        :param destination_config: 
        :type destination_config: :class:`huaweicloudsdkfunctiongraph.v2.FuncAsyncDestinationConfig`
        :param enable_async_status_log: 开启异步调用状态持久化
        :type enable_async_status_log: bool
        """
        
        

        self._max_async_event_age_in_seconds = None
        self._max_async_retry_attempts = None
        self._destination_config = None
        self._enable_async_status_log = None
        self.discriminator = None

        if max_async_event_age_in_seconds is not None:
            self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        if max_async_retry_attempts is not None:
            self.max_async_retry_attempts = max_async_retry_attempts
        if destination_config is not None:
            self.destination_config = destination_config
        if enable_async_status_log is not None:
            self.enable_async_status_log = enable_async_status_log

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
        :type max_async_event_age_in_seconds: int
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
        :type max_async_retry_attempts: int
        """
        self._max_async_retry_attempts = max_async_retry_attempts

    @property
    def destination_config(self):
        """Gets the destination_config of this UpdateFunctionAsyncInvokeConfigRequestBody.


        :return: The destination_config of this UpdateFunctionAsyncInvokeConfigRequestBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FuncAsyncDestinationConfig`
        """
        return self._destination_config

    @destination_config.setter
    def destination_config(self, destination_config):
        """Sets the destination_config of this UpdateFunctionAsyncInvokeConfigRequestBody.


        :param destination_config: The destination_config of this UpdateFunctionAsyncInvokeConfigRequestBody.
        :type destination_config: :class:`huaweicloudsdkfunctiongraph.v2.FuncAsyncDestinationConfig`
        """
        self._destination_config = destination_config

    @property
    def enable_async_status_log(self):
        """Gets the enable_async_status_log of this UpdateFunctionAsyncInvokeConfigRequestBody.

        开启异步调用状态持久化

        :return: The enable_async_status_log of this UpdateFunctionAsyncInvokeConfigRequestBody.
        :rtype: bool
        """
        return self._enable_async_status_log

    @enable_async_status_log.setter
    def enable_async_status_log(self, enable_async_status_log):
        """Sets the enable_async_status_log of this UpdateFunctionAsyncInvokeConfigRequestBody.

        开启异步调用状态持久化

        :param enable_async_status_log: The enable_async_status_log of this UpdateFunctionAsyncInvokeConfigRequestBody.
        :type enable_async_status_log: bool
        """
        self._enable_async_status_log = enable_async_status_log

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
        if not isinstance(other, UpdateFunctionAsyncInvokeConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
