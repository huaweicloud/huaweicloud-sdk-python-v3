# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StreamClassLoggerLevel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logger_name': 'str',
        'logger_level': 'str'
    }

    attribute_map = {
        'logger_name': 'logger_name',
        'logger_level': 'logger_level'
    }

    def __init__(self, logger_name=None, logger_level=None):
        """StreamClassLoggerLevel

        The model defined in huaweicloud sdk

        :param logger_name: 输出日志的类的名称。
        :type logger_name: str
        :param logger_level: 输出日志的级别，DEBUG\\TRACE\\WARNNING\\INFO\\ERROR。
        :type logger_level: str
        """
        
        

        self._logger_name = None
        self._logger_level = None
        self.discriminator = None

        if logger_name is not None:
            self.logger_name = logger_name
        if logger_level is not None:
            self.logger_level = logger_level

    @property
    def logger_name(self):
        """Gets the logger_name of this StreamClassLoggerLevel.

        输出日志的类的名称。

        :return: The logger_name of this StreamClassLoggerLevel.
        :rtype: str
        """
        return self._logger_name

    @logger_name.setter
    def logger_name(self, logger_name):
        """Sets the logger_name of this StreamClassLoggerLevel.

        输出日志的类的名称。

        :param logger_name: The logger_name of this StreamClassLoggerLevel.
        :type logger_name: str
        """
        self._logger_name = logger_name

    @property
    def logger_level(self):
        """Gets the logger_level of this StreamClassLoggerLevel.

        输出日志的级别，DEBUG\\TRACE\\WARNNING\\INFO\\ERROR。

        :return: The logger_level of this StreamClassLoggerLevel.
        :rtype: str
        """
        return self._logger_level

    @logger_level.setter
    def logger_level(self, logger_level):
        """Sets the logger_level of this StreamClassLoggerLevel.

        输出日志的级别，DEBUG\\TRACE\\WARNNING\\INFO\\ERROR。

        :param logger_level: The logger_level of this StreamClassLoggerLevel.
        :type logger_level: str
        """
        self._logger_level = logger_level

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
        if not isinstance(other, StreamClassLoggerLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
