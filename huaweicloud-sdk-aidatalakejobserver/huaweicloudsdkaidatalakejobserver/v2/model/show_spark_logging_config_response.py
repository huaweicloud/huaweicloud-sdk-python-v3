# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkLoggingConfigResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'driver_root_logger_level': 'LogLevel',
        'driver_loggers_level_of_class': 'list[ShowSparkClassLoggerLevelResponse]',
        'executor_root_logger_level': 'LogLevel',
        'executor_loggers_level_of_class': 'list[ShowSparkClassLoggerLevelResponse]'
    }

    attribute_map = {
        'driver_root_logger_level': 'driver_root_logger_level',
        'driver_loggers_level_of_class': 'driver_loggers_level_of_class',
        'executor_root_logger_level': 'executor_root_logger_level',
        'executor_loggers_level_of_class': 'executor_loggers_level_of_class'
    }

    def __init__(self, driver_root_logger_level=None, driver_loggers_level_of_class=None, executor_root_logger_level=None, executor_loggers_level_of_class=None):
        r"""ShowSparkLoggingConfigResponse

        The model defined in huaweicloud sdk

        :param driver_root_logger_level: 
        :type driver_root_logger_level: :class:`huaweicloudsdkaidatalakejobserver.v2.LogLevel`
        :param driver_loggers_level_of_class: **参数解释**：Driver类日志级别配置列表，用于为指定类设置特定的日志级别。 
        :type driver_loggers_level_of_class: list[:class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkClassLoggerLevelResponse`]
        :param executor_root_logger_level: 
        :type executor_root_logger_level: :class:`huaweicloudsdkaidatalakejobserver.v2.LogLevel`
        :param executor_loggers_level_of_class: **参数解释**：Executor类日志级别配置列表，用于为指定类设置特定的日志级别。 
        :type executor_loggers_level_of_class: list[:class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkClassLoggerLevelResponse`]
        """
        
        

        self._driver_root_logger_level = None
        self._driver_loggers_level_of_class = None
        self._executor_root_logger_level = None
        self._executor_loggers_level_of_class = None
        self.discriminator = None

        if driver_root_logger_level is not None:
            self.driver_root_logger_level = driver_root_logger_level
        if driver_loggers_level_of_class is not None:
            self.driver_loggers_level_of_class = driver_loggers_level_of_class
        if executor_root_logger_level is not None:
            self.executor_root_logger_level = executor_root_logger_level
        if executor_loggers_level_of_class is not None:
            self.executor_loggers_level_of_class = executor_loggers_level_of_class

    @property
    def driver_root_logger_level(self):
        r"""Gets the driver_root_logger_level of this ShowSparkLoggingConfigResponse.

        :return: The driver_root_logger_level of this ShowSparkLoggingConfigResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.LogLevel`
        """
        return self._driver_root_logger_level

    @driver_root_logger_level.setter
    def driver_root_logger_level(self, driver_root_logger_level):
        r"""Sets the driver_root_logger_level of this ShowSparkLoggingConfigResponse.

        :param driver_root_logger_level: The driver_root_logger_level of this ShowSparkLoggingConfigResponse.
        :type driver_root_logger_level: :class:`huaweicloudsdkaidatalakejobserver.v2.LogLevel`
        """
        self._driver_root_logger_level = driver_root_logger_level

    @property
    def driver_loggers_level_of_class(self):
        r"""Gets the driver_loggers_level_of_class of this ShowSparkLoggingConfigResponse.

        **参数解释**：Driver类日志级别配置列表，用于为指定类设置特定的日志级别。 

        :return: The driver_loggers_level_of_class of this ShowSparkLoggingConfigResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkClassLoggerLevelResponse`]
        """
        return self._driver_loggers_level_of_class

    @driver_loggers_level_of_class.setter
    def driver_loggers_level_of_class(self, driver_loggers_level_of_class):
        r"""Sets the driver_loggers_level_of_class of this ShowSparkLoggingConfigResponse.

        **参数解释**：Driver类日志级别配置列表，用于为指定类设置特定的日志级别。 

        :param driver_loggers_level_of_class: The driver_loggers_level_of_class of this ShowSparkLoggingConfigResponse.
        :type driver_loggers_level_of_class: list[:class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkClassLoggerLevelResponse`]
        """
        self._driver_loggers_level_of_class = driver_loggers_level_of_class

    @property
    def executor_root_logger_level(self):
        r"""Gets the executor_root_logger_level of this ShowSparkLoggingConfigResponse.

        :return: The executor_root_logger_level of this ShowSparkLoggingConfigResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.LogLevel`
        """
        return self._executor_root_logger_level

    @executor_root_logger_level.setter
    def executor_root_logger_level(self, executor_root_logger_level):
        r"""Sets the executor_root_logger_level of this ShowSparkLoggingConfigResponse.

        :param executor_root_logger_level: The executor_root_logger_level of this ShowSparkLoggingConfigResponse.
        :type executor_root_logger_level: :class:`huaweicloudsdkaidatalakejobserver.v2.LogLevel`
        """
        self._executor_root_logger_level = executor_root_logger_level

    @property
    def executor_loggers_level_of_class(self):
        r"""Gets the executor_loggers_level_of_class of this ShowSparkLoggingConfigResponse.

        **参数解释**：Executor类日志级别配置列表，用于为指定类设置特定的日志级别。 

        :return: The executor_loggers_level_of_class of this ShowSparkLoggingConfigResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkClassLoggerLevelResponse`]
        """
        return self._executor_loggers_level_of_class

    @executor_loggers_level_of_class.setter
    def executor_loggers_level_of_class(self, executor_loggers_level_of_class):
        r"""Sets the executor_loggers_level_of_class of this ShowSparkLoggingConfigResponse.

        **参数解释**：Executor类日志级别配置列表，用于为指定类设置特定的日志级别。 

        :param executor_loggers_level_of_class: The executor_loggers_level_of_class of this ShowSparkLoggingConfigResponse.
        :type executor_loggers_level_of_class: list[:class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkClassLoggerLevelResponse`]
        """
        self._executor_loggers_level_of_class = executor_loggers_level_of_class

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowSparkLoggingConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
