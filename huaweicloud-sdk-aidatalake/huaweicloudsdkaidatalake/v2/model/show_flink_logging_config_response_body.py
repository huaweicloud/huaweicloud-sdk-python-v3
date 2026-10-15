# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlinkLoggingConfigResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'root_logger_level': 'FlinkLoggerLevel',
        'log4j_loggers': 'list[ShowFlinkLog4jLoggersResponseBody]'
    }

    attribute_map = {
        'root_logger_level': 'root_logger_level',
        'log4j_loggers': 'log4j_loggers'
    }

    def __init__(self, root_logger_level=None, log4j_loggers=None):
        r"""ShowFlinkLoggingConfigResponseBody

        The model defined in huaweicloud sdk

        :param root_logger_level: 
        :type root_logger_level: :class:`huaweicloudsdkaidatalake.v2.FlinkLoggerLevel`
        :param log4j_loggers: **参数解释**：自定义日志类配置列表。
        :type log4j_loggers: list[:class:`huaweicloudsdkaidatalake.v2.ShowFlinkLog4jLoggersResponseBody`]
        """
        
        

        self._root_logger_level = None
        self._log4j_loggers = None
        self.discriminator = None

        if root_logger_level is not None:
            self.root_logger_level = root_logger_level
        if log4j_loggers is not None:
            self.log4j_loggers = log4j_loggers

    @property
    def root_logger_level(self):
        r"""Gets the root_logger_level of this ShowFlinkLoggingConfigResponseBody.

        :return: The root_logger_level of this ShowFlinkLoggingConfigResponseBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkLoggerLevel`
        """
        return self._root_logger_level

    @root_logger_level.setter
    def root_logger_level(self, root_logger_level):
        r"""Sets the root_logger_level of this ShowFlinkLoggingConfigResponseBody.

        :param root_logger_level: The root_logger_level of this ShowFlinkLoggingConfigResponseBody.
        :type root_logger_level: :class:`huaweicloudsdkaidatalake.v2.FlinkLoggerLevel`
        """
        self._root_logger_level = root_logger_level

    @property
    def log4j_loggers(self):
        r"""Gets the log4j_loggers of this ShowFlinkLoggingConfigResponseBody.

        **参数解释**：自定义日志类配置列表。

        :return: The log4j_loggers of this ShowFlinkLoggingConfigResponseBody.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.ShowFlinkLog4jLoggersResponseBody`]
        """
        return self._log4j_loggers

    @log4j_loggers.setter
    def log4j_loggers(self, log4j_loggers):
        r"""Sets the log4j_loggers of this ShowFlinkLoggingConfigResponseBody.

        **参数解释**：自定义日志类配置列表。

        :param log4j_loggers: The log4j_loggers of this ShowFlinkLoggingConfigResponseBody.
        :type log4j_loggers: list[:class:`huaweicloudsdkaidatalake.v2.ShowFlinkLog4jLoggersResponseBody`]
        """
        self._log4j_loggers = log4j_loggers

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
        if not isinstance(other, ShowFlinkLoggingConfigResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
