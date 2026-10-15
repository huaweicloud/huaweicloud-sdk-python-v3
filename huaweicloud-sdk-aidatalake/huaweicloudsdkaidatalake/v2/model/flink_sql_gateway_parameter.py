# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkSqlGatewayParameter:

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
        'sql_gateway_token': 'str'
    }

    attribute_map = {
        'type': 'type',
        'sql_gateway_token': 'sql_gateway_token'
    }

    def __init__(self, type=None, sql_gateway_token=None):
        r"""FlinkSqlGatewayParameter

        The model defined in huaweicloud sdk

        :param type: **参数解释**：作业类型。 **约束限制**：固定值为 FLINK_SQL_GATEWAY。 **取值范围**：不涉及。 **默认取值**：FLINK_SQL_GATEWAY。
        :type type: str
        :param sql_gateway_token: **参数解释**：用户自定义的SQL Gateway访问鉴权Token，调用方通过HTTP请求头 Authorization: Bearer {token} 携带。 **约束限制**：不涉及。 **取值范围**：长度为1~256个字符。 **默认取值**：不涉及。
        :type sql_gateway_token: str
        """
        
        

        self._type = None
        self._sql_gateway_token = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if sql_gateway_token is not None:
            self.sql_gateway_token = sql_gateway_token

    @property
    def type(self):
        r"""Gets the type of this FlinkSqlGatewayParameter.

        **参数解释**：作业类型。 **约束限制**：固定值为 FLINK_SQL_GATEWAY。 **取值范围**：不涉及。 **默认取值**：FLINK_SQL_GATEWAY。

        :return: The type of this FlinkSqlGatewayParameter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this FlinkSqlGatewayParameter.

        **参数解释**：作业类型。 **约束限制**：固定值为 FLINK_SQL_GATEWAY。 **取值范围**：不涉及。 **默认取值**：FLINK_SQL_GATEWAY。

        :param type: The type of this FlinkSqlGatewayParameter.
        :type type: str
        """
        self._type = type

    @property
    def sql_gateway_token(self):
        r"""Gets the sql_gateway_token of this FlinkSqlGatewayParameter.

        **参数解释**：用户自定义的SQL Gateway访问鉴权Token，调用方通过HTTP请求头 Authorization: Bearer {token} 携带。 **约束限制**：不涉及。 **取值范围**：长度为1~256个字符。 **默认取值**：不涉及。

        :return: The sql_gateway_token of this FlinkSqlGatewayParameter.
        :rtype: str
        """
        return self._sql_gateway_token

    @sql_gateway_token.setter
    def sql_gateway_token(self, sql_gateway_token):
        r"""Sets the sql_gateway_token of this FlinkSqlGatewayParameter.

        **参数解释**：用户自定义的SQL Gateway访问鉴权Token，调用方通过HTTP请求头 Authorization: Bearer {token} 携带。 **约束限制**：不涉及。 **取值范围**：长度为1~256个字符。 **默认取值**：不涉及。

        :param sql_gateway_token: The sql_gateway_token of this FlinkSqlGatewayParameter.
        :type sql_gateway_token: str
        """
        self._sql_gateway_token = sql_gateway_token

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
        if not isinstance(other, FlinkSqlGatewayParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
