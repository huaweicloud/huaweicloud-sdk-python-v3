# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlinkSqlGatewayParameterResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'sql_gateway_config': 'ShowFlinkSqlGatewayConfigResponseBody',
        'idle_enabled': 'bool',
        'idle_timeout': 'int'
    }

    attribute_map = {
        'type': 'type',
        'sql_gateway_config': 'sql_gateway_config',
        'idle_enabled': 'idle_enabled',
        'idle_timeout': 'idle_timeout'
    }

    def __init__(self, type=None, sql_gateway_config=None, idle_enabled=None, idle_timeout=None):
        r"""ShowFlinkSqlGatewayParameterResponse

        The model defined in huaweicloud sdk

        :param type: **参数解释**：作业类型。 **约束限制**：不涉及。 **取值范围**：   - FLINK_SQL_GATEWAY：SQL Gateway作业。
        :type type: str
        :param sql_gateway_config: 
        :type sql_gateway_config: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkSqlGatewayConfigResponseBody`
        :param idle_enabled: **参数解释**：是否开启空闲自动释放。 **取值范围**：   - true：开启空闲自动释放。   - false：关闭空闲自动释放。
        :type idle_enabled: bool
        :param idle_timeout: **参数解释**：最大空闲时长，单位为分钟。空闲指会话内没有正在运行的作业，创建会话等其他操作不计为非空闲。 **取值范围**：10~1440。
        :type idle_timeout: int
        """
        
        

        self._type = None
        self._sql_gateway_config = None
        self._idle_enabled = None
        self._idle_timeout = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if sql_gateway_config is not None:
            self.sql_gateway_config = sql_gateway_config
        if idle_enabled is not None:
            self.idle_enabled = idle_enabled
        if idle_timeout is not None:
            self.idle_timeout = idle_timeout

    @property
    def type(self):
        r"""Gets the type of this ShowFlinkSqlGatewayParameterResponse.

        **参数解释**：作业类型。 **约束限制**：不涉及。 **取值范围**：   - FLINK_SQL_GATEWAY：SQL Gateway作业。

        :return: The type of this ShowFlinkSqlGatewayParameterResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowFlinkSqlGatewayParameterResponse.

        **参数解释**：作业类型。 **约束限制**：不涉及。 **取值范围**：   - FLINK_SQL_GATEWAY：SQL Gateway作业。

        :param type: The type of this ShowFlinkSqlGatewayParameterResponse.
        :type type: str
        """
        self._type = type

    @property
    def sql_gateway_config(self):
        r"""Gets the sql_gateway_config of this ShowFlinkSqlGatewayParameterResponse.

        :return: The sql_gateway_config of this ShowFlinkSqlGatewayParameterResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkSqlGatewayConfigResponseBody`
        """
        return self._sql_gateway_config

    @sql_gateway_config.setter
    def sql_gateway_config(self, sql_gateway_config):
        r"""Sets the sql_gateway_config of this ShowFlinkSqlGatewayParameterResponse.

        :param sql_gateway_config: The sql_gateway_config of this ShowFlinkSqlGatewayParameterResponse.
        :type sql_gateway_config: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkSqlGatewayConfigResponseBody`
        """
        self._sql_gateway_config = sql_gateway_config

    @property
    def idle_enabled(self):
        r"""Gets the idle_enabled of this ShowFlinkSqlGatewayParameterResponse.

        **参数解释**：是否开启空闲自动释放。 **取值范围**：   - true：开启空闲自动释放。   - false：关闭空闲自动释放。

        :return: The idle_enabled of this ShowFlinkSqlGatewayParameterResponse.
        :rtype: bool
        """
        return self._idle_enabled

    @idle_enabled.setter
    def idle_enabled(self, idle_enabled):
        r"""Sets the idle_enabled of this ShowFlinkSqlGatewayParameterResponse.

        **参数解释**：是否开启空闲自动释放。 **取值范围**：   - true：开启空闲自动释放。   - false：关闭空闲自动释放。

        :param idle_enabled: The idle_enabled of this ShowFlinkSqlGatewayParameterResponse.
        :type idle_enabled: bool
        """
        self._idle_enabled = idle_enabled

    @property
    def idle_timeout(self):
        r"""Gets the idle_timeout of this ShowFlinkSqlGatewayParameterResponse.

        **参数解释**：最大空闲时长，单位为分钟。空闲指会话内没有正在运行的作业，创建会话等其他操作不计为非空闲。 **取值范围**：10~1440。

        :return: The idle_timeout of this ShowFlinkSqlGatewayParameterResponse.
        :rtype: int
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, idle_timeout):
        r"""Sets the idle_timeout of this ShowFlinkSqlGatewayParameterResponse.

        **参数解释**：最大空闲时长，单位为分钟。空闲指会话内没有正在运行的作业，创建会话等其他操作不计为非空闲。 **取值范围**：10~1440。

        :param idle_timeout: The idle_timeout of this ShowFlinkSqlGatewayParameterResponse.
        :type idle_timeout: int
        """
        self._idle_timeout = idle_timeout

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
        if not isinstance(other, ShowFlinkSqlGatewayParameterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
