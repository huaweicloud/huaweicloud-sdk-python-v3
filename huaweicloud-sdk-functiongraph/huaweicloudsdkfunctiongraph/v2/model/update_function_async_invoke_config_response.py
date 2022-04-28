# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFunctionAsyncInvokeConfigResponse(SdkResponse):

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
        'last_modified': 'str',
        'enable_async_status_log': 'bool'
    }

    attribute_map = {
        'func_urn': 'func_urn',
        'max_async_event_age_in_seconds': 'max_async_event_age_in_seconds',
        'max_async_retry_attempts': 'max_async_retry_attempts',
        'destination_config': 'destination_config',
        'created_time': 'created_time',
        'last_modified': 'last_modified',
        'enable_async_status_log': 'enable_async_status_log'
    }

    def __init__(self, func_urn=None, max_async_event_age_in_seconds=None, max_async_retry_attempts=None, destination_config=None, created_time=None, last_modified=None, enable_async_status_log=None):
        """UpdateFunctionAsyncInvokeConfigResponse

        The model defined in huaweicloud sdk

        :param func_urn: 函数URN。
        :type func_urn: str
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
        :param enable_async_status_log: 开启异步调用状态持久化
        :type enable_async_status_log: bool
        """
        
        super(UpdateFunctionAsyncInvokeConfigResponse, self).__init__()

        self._func_urn = None
        self._max_async_event_age_in_seconds = None
        self._max_async_retry_attempts = None
        self._destination_config = None
        self._created_time = None
        self._last_modified = None
        self._enable_async_status_log = None
        self.discriminator = None

        if func_urn is not None:
            self.func_urn = func_urn
        if max_async_event_age_in_seconds is not None:
            self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        if max_async_retry_attempts is not None:
            self.max_async_retry_attempts = max_async_retry_attempts
        if destination_config is not None:
            self.destination_config = destination_config
        if created_time is not None:
            self.created_time = created_time
        if last_modified is not None:
            self.last_modified = last_modified
        if enable_async_status_log is not None:
            self.enable_async_status_log = enable_async_status_log

    @property
    def func_urn(self):
        """Gets the func_urn of this UpdateFunctionAsyncInvokeConfigResponse.

        函数URN。

        :return: The func_urn of this UpdateFunctionAsyncInvokeConfigResponse.
        :rtype: str
        """
        return self._func_urn

    @func_urn.setter
    def func_urn(self, func_urn):
        """Sets the func_urn of this UpdateFunctionAsyncInvokeConfigResponse.

        函数URN。

        :param func_urn: The func_urn of this UpdateFunctionAsyncInvokeConfigResponse.
        :type func_urn: str
        """
        self._func_urn = func_urn

    @property
    def max_async_event_age_in_seconds(self):
        """Gets the max_async_event_age_in_seconds of this UpdateFunctionAsyncInvokeConfigResponse.

        消息最大存活时长，取值范围[60，86400]。单位：秒。

        :return: The max_async_event_age_in_seconds of this UpdateFunctionAsyncInvokeConfigResponse.
        :rtype: int
        """
        return self._max_async_event_age_in_seconds

    @max_async_event_age_in_seconds.setter
    def max_async_event_age_in_seconds(self, max_async_event_age_in_seconds):
        """Sets the max_async_event_age_in_seconds of this UpdateFunctionAsyncInvokeConfigResponse.

        消息最大存活时长，取值范围[60，86400]。单位：秒。

        :param max_async_event_age_in_seconds: The max_async_event_age_in_seconds of this UpdateFunctionAsyncInvokeConfigResponse.
        :type max_async_event_age_in_seconds: int
        """
        self._max_async_event_age_in_seconds = max_async_event_age_in_seconds

    @property
    def max_async_retry_attempts(self):
        """Gets the max_async_retry_attempts of this UpdateFunctionAsyncInvokeConfigResponse.

        异步调用失败后的最大重试次数，默认值为3。取值范围[0，8]。

        :return: The max_async_retry_attempts of this UpdateFunctionAsyncInvokeConfigResponse.
        :rtype: int
        """
        return self._max_async_retry_attempts

    @max_async_retry_attempts.setter
    def max_async_retry_attempts(self, max_async_retry_attempts):
        """Sets the max_async_retry_attempts of this UpdateFunctionAsyncInvokeConfigResponse.

        异步调用失败后的最大重试次数，默认值为3。取值范围[0，8]。

        :param max_async_retry_attempts: The max_async_retry_attempts of this UpdateFunctionAsyncInvokeConfigResponse.
        :type max_async_retry_attempts: int
        """
        self._max_async_retry_attempts = max_async_retry_attempts

    @property
    def destination_config(self):
        """Gets the destination_config of this UpdateFunctionAsyncInvokeConfigResponse.


        :return: The destination_config of this UpdateFunctionAsyncInvokeConfigResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FuncAsyncDestinationConfig`
        """
        return self._destination_config

    @destination_config.setter
    def destination_config(self, destination_config):
        """Sets the destination_config of this UpdateFunctionAsyncInvokeConfigResponse.


        :param destination_config: The destination_config of this UpdateFunctionAsyncInvokeConfigResponse.
        :type destination_config: :class:`huaweicloudsdkfunctiongraph.v2.FuncAsyncDestinationConfig`
        """
        self._destination_config = destination_config

    @property
    def created_time(self):
        """Gets the created_time of this UpdateFunctionAsyncInvokeConfigResponse.

        异步调用配置的创建时间。

        :return: The created_time of this UpdateFunctionAsyncInvokeConfigResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this UpdateFunctionAsyncInvokeConfigResponse.

        异步调用配置的创建时间。

        :param created_time: The created_time of this UpdateFunctionAsyncInvokeConfigResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def last_modified(self):
        """Gets the last_modified of this UpdateFunctionAsyncInvokeConfigResponse.

        异步调用配置的最后更改时间。

        :return: The last_modified of this UpdateFunctionAsyncInvokeConfigResponse.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this UpdateFunctionAsyncInvokeConfigResponse.

        异步调用配置的最后更改时间。

        :param last_modified: The last_modified of this UpdateFunctionAsyncInvokeConfigResponse.
        :type last_modified: str
        """
        self._last_modified = last_modified

    @property
    def enable_async_status_log(self):
        """Gets the enable_async_status_log of this UpdateFunctionAsyncInvokeConfigResponse.

        开启异步调用状态持久化

        :return: The enable_async_status_log of this UpdateFunctionAsyncInvokeConfigResponse.
        :rtype: bool
        """
        return self._enable_async_status_log

    @enable_async_status_log.setter
    def enable_async_status_log(self, enable_async_status_log):
        """Sets the enable_async_status_log of this UpdateFunctionAsyncInvokeConfigResponse.

        开启异步调用状态持久化

        :param enable_async_status_log: The enable_async_status_log of this UpdateFunctionAsyncInvokeConfigResponse.
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
        if not isinstance(other, UpdateFunctionAsyncInvokeConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
