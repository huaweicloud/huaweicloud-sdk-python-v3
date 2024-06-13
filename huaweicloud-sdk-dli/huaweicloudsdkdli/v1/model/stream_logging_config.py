# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StreamLoggingConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_enabled': 'bool',
        'obs_bucket': 'str',
        'root_logger_level': 'str',
        'loggers_level_of_class': 'list[StreamClassLoggerLevel]'
    }

    attribute_map = {
        'log_enabled': 'log_enabled',
        'obs_bucket': 'obs_bucket',
        'root_logger_level': 'root_logger_level',
        'loggers_level_of_class': 'loggers_level_of_class'
    }

    def __init__(self, log_enabled=None, obs_bucket=None, root_logger_level=None, loggers_level_of_class=None):
        """StreamLoggingConfig

        The model defined in huaweicloud sdk

        :param log_enabled: 是否开启作业的日志上传到用户的 OBS 功能。默认为 false。
        :type log_enabled: bool
        :param obs_bucket: 用户授权保存作业日志的 OBS 桶名。
        :type obs_bucket: str
        :param root_logger_level: 根目录日志级别配置，DEBUG\\TRACE\\WARNNING\\INFO\\ERROR
        :type root_logger_level: str
        :param loggers_level_of_class: 输出日志的类名称对应的日志级别配置。
        :type loggers_level_of_class: list[:class:`huaweicloudsdkdli.v1.StreamClassLoggerLevel`]
        """
        
        

        self._log_enabled = None
        self._obs_bucket = None
        self._root_logger_level = None
        self._loggers_level_of_class = None
        self.discriminator = None

        if log_enabled is not None:
            self.log_enabled = log_enabled
        if obs_bucket is not None:
            self.obs_bucket = obs_bucket
        if root_logger_level is not None:
            self.root_logger_level = root_logger_level
        if loggers_level_of_class is not None:
            self.loggers_level_of_class = loggers_level_of_class

    @property
    def log_enabled(self):
        """Gets the log_enabled of this StreamLoggingConfig.

        是否开启作业的日志上传到用户的 OBS 功能。默认为 false。

        :return: The log_enabled of this StreamLoggingConfig.
        :rtype: bool
        """
        return self._log_enabled

    @log_enabled.setter
    def log_enabled(self, log_enabled):
        """Sets the log_enabled of this StreamLoggingConfig.

        是否开启作业的日志上传到用户的 OBS 功能。默认为 false。

        :param log_enabled: The log_enabled of this StreamLoggingConfig.
        :type log_enabled: bool
        """
        self._log_enabled = log_enabled

    @property
    def obs_bucket(self):
        """Gets the obs_bucket of this StreamLoggingConfig.

        用户授权保存作业日志的 OBS 桶名。

        :return: The obs_bucket of this StreamLoggingConfig.
        :rtype: str
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        """Sets the obs_bucket of this StreamLoggingConfig.

        用户授权保存作业日志的 OBS 桶名。

        :param obs_bucket: The obs_bucket of this StreamLoggingConfig.
        :type obs_bucket: str
        """
        self._obs_bucket = obs_bucket

    @property
    def root_logger_level(self):
        """Gets the root_logger_level of this StreamLoggingConfig.

        根目录日志级别配置，DEBUG\\TRACE\\WARNNING\\INFO\\ERROR

        :return: The root_logger_level of this StreamLoggingConfig.
        :rtype: str
        """
        return self._root_logger_level

    @root_logger_level.setter
    def root_logger_level(self, root_logger_level):
        """Sets the root_logger_level of this StreamLoggingConfig.

        根目录日志级别配置，DEBUG\\TRACE\\WARNNING\\INFO\\ERROR

        :param root_logger_level: The root_logger_level of this StreamLoggingConfig.
        :type root_logger_level: str
        """
        self._root_logger_level = root_logger_level

    @property
    def loggers_level_of_class(self):
        """Gets the loggers_level_of_class of this StreamLoggingConfig.

        输出日志的类名称对应的日志级别配置。

        :return: The loggers_level_of_class of this StreamLoggingConfig.
        :rtype: list[:class:`huaweicloudsdkdli.v1.StreamClassLoggerLevel`]
        """
        return self._loggers_level_of_class

    @loggers_level_of_class.setter
    def loggers_level_of_class(self, loggers_level_of_class):
        """Sets the loggers_level_of_class of this StreamLoggingConfig.

        输出日志的类名称对应的日志级别配置。

        :param loggers_level_of_class: The loggers_level_of_class of this StreamLoggingConfig.
        :type loggers_level_of_class: list[:class:`huaweicloudsdkdli.v1.StreamClassLoggerLevel`]
        """
        self._loggers_level_of_class = loggers_level_of_class

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
        if not isinstance(other, StreamLoggingConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
