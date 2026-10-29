# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlinkSqlGatewayConfigResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host': 'str',
        'sql_gateway_token': 'str'
    }

    attribute_map = {
        'host': 'host',
        'sql_gateway_token': 'sql_gateway_token'
    }

    def __init__(self, host=None, sql_gateway_token=None):
        r"""ShowFlinkSqlGatewayConfigResponseBody

        The model defined in huaweicloud sdk

        :param host: **参数解释**：SQL Gateway的访问Host，格式为sql-gateway-{jobId}。 **取值范围**：长度为1~253个字符。
        :type host: str
        :param sql_gateway_token: **参数解释**：SQL Gateway鉴权Token。 **取值范围**：已配置时固定返回 ******；未配置时不返回该字段。
        :type sql_gateway_token: str
        """
        
        

        self._host = None
        self._sql_gateway_token = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if sql_gateway_token is not None:
            self.sql_gateway_token = sql_gateway_token

    @property
    def host(self):
        r"""Gets the host of this ShowFlinkSqlGatewayConfigResponseBody.

        **参数解释**：SQL Gateway的访问Host，格式为sql-gateway-{jobId}。 **取值范围**：长度为1~253个字符。

        :return: The host of this ShowFlinkSqlGatewayConfigResponseBody.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this ShowFlinkSqlGatewayConfigResponseBody.

        **参数解释**：SQL Gateway的访问Host，格式为sql-gateway-{jobId}。 **取值范围**：长度为1~253个字符。

        :param host: The host of this ShowFlinkSqlGatewayConfigResponseBody.
        :type host: str
        """
        self._host = host

    @property
    def sql_gateway_token(self):
        r"""Gets the sql_gateway_token of this ShowFlinkSqlGatewayConfigResponseBody.

        **参数解释**：SQL Gateway鉴权Token。 **取值范围**：已配置时固定返回 ******；未配置时不返回该字段。

        :return: The sql_gateway_token of this ShowFlinkSqlGatewayConfigResponseBody.
        :rtype: str
        """
        return self._sql_gateway_token

    @sql_gateway_token.setter
    def sql_gateway_token(self, sql_gateway_token):
        r"""Sets the sql_gateway_token of this ShowFlinkSqlGatewayConfigResponseBody.

        **参数解释**：SQL Gateway鉴权Token。 **取值范围**：已配置时固定返回 ******；未配置时不返回该字段。

        :param sql_gateway_token: The sql_gateway_token of this ShowFlinkSqlGatewayConfigResponseBody.
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
        if not isinstance(other, ShowFlinkSqlGatewayConfigResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
