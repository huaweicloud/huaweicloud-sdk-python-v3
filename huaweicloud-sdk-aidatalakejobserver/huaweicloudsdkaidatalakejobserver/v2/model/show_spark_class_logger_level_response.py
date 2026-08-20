# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkClassLoggerLevelResponse:

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
        'logger_level': 'LogLevel'
    }

    attribute_map = {
        'logger_name': 'logger_name',
        'logger_level': 'logger_level'
    }

    def __init__(self, logger_name=None, logger_level=None):
        r"""ShowSparkClassLoggerLevelResponse

        The model defined in huaweicloud sdk

        :param logger_name: **参数解释**：输出日志类的名称，用于指定需要配置日志级别的类。 **取值范围**：完整的类路径格式，例如：com.aaa.bbb.ccc。长度为1~512个字符。 
        :type logger_name: str
        :param logger_level: 
        :type logger_level: :class:`huaweicloudsdkaidatalakejobserver.v2.LogLevel`
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
        r"""Gets the logger_name of this ShowSparkClassLoggerLevelResponse.

        **参数解释**：输出日志类的名称，用于指定需要配置日志级别的类。 **取值范围**：完整的类路径格式，例如：com.aaa.bbb.ccc。长度为1~512个字符。 

        :return: The logger_name of this ShowSparkClassLoggerLevelResponse.
        :rtype: str
        """
        return self._logger_name

    @logger_name.setter
    def logger_name(self, logger_name):
        r"""Sets the logger_name of this ShowSparkClassLoggerLevelResponse.

        **参数解释**：输出日志类的名称，用于指定需要配置日志级别的类。 **取值范围**：完整的类路径格式，例如：com.aaa.bbb.ccc。长度为1~512个字符。 

        :param logger_name: The logger_name of this ShowSparkClassLoggerLevelResponse.
        :type logger_name: str
        """
        self._logger_name = logger_name

    @property
    def logger_level(self):
        r"""Gets the logger_level of this ShowSparkClassLoggerLevelResponse.

        :return: The logger_level of this ShowSparkClassLoggerLevelResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.LogLevel`
        """
        return self._logger_level

    @logger_level.setter
    def logger_level(self, logger_level):
        r"""Sets the logger_level of this ShowSparkClassLoggerLevelResponse.

        :param logger_level: The logger_level of this ShowSparkClassLoggerLevelResponse.
        :type logger_level: :class:`huaweicloudsdkaidatalakejobserver.v2.LogLevel`
        """
        self._logger_level = logger_level

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
        if not isinstance(other, ShowSparkClassLoggerLevelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
