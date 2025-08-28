# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberHealthCheckFailedReason:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reason_code': 'str',
        'expected_response': 'str',
        'healthcheck_response': 'str'
    }

    attribute_map = {
        'reason_code': 'reason_code',
        'expected_response': 'expected_response',
        'healthcheck_response': 'healthcheck_response'
    }

    def __init__(self, reason_code=None, expected_response=None, healthcheck_response=None):
        r"""MemberHealthCheckFailedReason

        The model defined in huaweicloud sdk

        :param reason_code: **参数解释**：健康检查异常原因码。  **取值范围**： - CONNECT_TIMEOUT: 负载均衡健康检查时向后端服务器建立连接超时。 - CONNECT_REFUSED: 负载均衡健康检查时向后端服务器拒绝连接。 - CONNECT_FAILED: 负载均衡健康检查时向后端服务器建立连接失败。 - CONNECT_INTERRUPT: 负载均衡健康检查与后端服务器连接中断。 - SSL_HANDSHAKE_ERROR: 负载均衡健康检查时与后端服务器SSL握手失败。 - RECV_RESPONSE_FAILED: 负载均衡健康检查时从后端服务器接收响应失败。 - RECV_RESPONSE_TIMEOUT: 负载均衡健康检查时从后端服务器接收响应超时。 - SEND_REQUEST_FAILED: 负载均衡健康检查时向后端服务器发送请求失败。 - SEND_REQUEST_TIMEOUT: 负载均衡健康检查时向后端服务器发送请求超时。 - RESPONSE_FORMAT_ERROR: 负载均衡健康检查时从后端服务器接收响应格式错误。 - RESPONSE_MISMATCH: 负载均衡健康检查时从后端服务器接收的响应码与预期配置返回码不一致。
        :type reason_code: str
        :param expected_response: **参数解释**：健康检查预期响应状态码。支持HTTP,HTTPS,GRPC健康检查。只有reason_code为RESPONSE_MISMATCH时，支持非null取值。  **取值范围**： - 单值：单个返回码。当type为GRPC时，取值范围为0-99；当type为其他协议时，取值范围为200-599。例如：\&quot;0\&quot;或\&quot;200\&quot;。 - 列表：多个特定返回码，逗号分隔，最多支持5个返回码。例如:\&quot;200,202\&quot;或\&quot;0,1\&quot;。 - 区间：一个返回码区间，区间内\&quot;-\&quot;分隔，区间之间逗号分隔，最多支持5个区间。例如\&quot;200-204,300-399\&quot;或\&quot;0-5,10-12,20-30\&quot;。
        :type expected_response: str
        :param healthcheck_response: **参数解释**：健康检查探测实际响应状态码。支持HTTP,HTTPS,GRPC健康检查。只有reason_code为RESPONSE_MISMATCH时，支持非null取值。  **取值范围**： - 单个返回码。当type为GRPC时，取值范围为0-99；当type为其他协议时，取值范围为200-599。例如：\&quot;0\&quot;或\&quot;200\&quot;。
        :type healthcheck_response: str
        """
        
        

        self._reason_code = None
        self._expected_response = None
        self._healthcheck_response = None
        self.discriminator = None

        self.reason_code = reason_code
        self.expected_response = expected_response
        self.healthcheck_response = healthcheck_response

    @property
    def reason_code(self):
        r"""Gets the reason_code of this MemberHealthCheckFailedReason.

        **参数解释**：健康检查异常原因码。  **取值范围**： - CONNECT_TIMEOUT: 负载均衡健康检查时向后端服务器建立连接超时。 - CONNECT_REFUSED: 负载均衡健康检查时向后端服务器拒绝连接。 - CONNECT_FAILED: 负载均衡健康检查时向后端服务器建立连接失败。 - CONNECT_INTERRUPT: 负载均衡健康检查与后端服务器连接中断。 - SSL_HANDSHAKE_ERROR: 负载均衡健康检查时与后端服务器SSL握手失败。 - RECV_RESPONSE_FAILED: 负载均衡健康检查时从后端服务器接收响应失败。 - RECV_RESPONSE_TIMEOUT: 负载均衡健康检查时从后端服务器接收响应超时。 - SEND_REQUEST_FAILED: 负载均衡健康检查时向后端服务器发送请求失败。 - SEND_REQUEST_TIMEOUT: 负载均衡健康检查时向后端服务器发送请求超时。 - RESPONSE_FORMAT_ERROR: 负载均衡健康检查时从后端服务器接收响应格式错误。 - RESPONSE_MISMATCH: 负载均衡健康检查时从后端服务器接收的响应码与预期配置返回码不一致。

        :return: The reason_code of this MemberHealthCheckFailedReason.
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        r"""Sets the reason_code of this MemberHealthCheckFailedReason.

        **参数解释**：健康检查异常原因码。  **取值范围**： - CONNECT_TIMEOUT: 负载均衡健康检查时向后端服务器建立连接超时。 - CONNECT_REFUSED: 负载均衡健康检查时向后端服务器拒绝连接。 - CONNECT_FAILED: 负载均衡健康检查时向后端服务器建立连接失败。 - CONNECT_INTERRUPT: 负载均衡健康检查与后端服务器连接中断。 - SSL_HANDSHAKE_ERROR: 负载均衡健康检查时与后端服务器SSL握手失败。 - RECV_RESPONSE_FAILED: 负载均衡健康检查时从后端服务器接收响应失败。 - RECV_RESPONSE_TIMEOUT: 负载均衡健康检查时从后端服务器接收响应超时。 - SEND_REQUEST_FAILED: 负载均衡健康检查时向后端服务器发送请求失败。 - SEND_REQUEST_TIMEOUT: 负载均衡健康检查时向后端服务器发送请求超时。 - RESPONSE_FORMAT_ERROR: 负载均衡健康检查时从后端服务器接收响应格式错误。 - RESPONSE_MISMATCH: 负载均衡健康检查时从后端服务器接收的响应码与预期配置返回码不一致。

        :param reason_code: The reason_code of this MemberHealthCheckFailedReason.
        :type reason_code: str
        """
        self._reason_code = reason_code

    @property
    def expected_response(self):
        r"""Gets the expected_response of this MemberHealthCheckFailedReason.

        **参数解释**：健康检查预期响应状态码。支持HTTP,HTTPS,GRPC健康检查。只有reason_code为RESPONSE_MISMATCH时，支持非null取值。  **取值范围**： - 单值：单个返回码。当type为GRPC时，取值范围为0-99；当type为其他协议时，取值范围为200-599。例如：\"0\"或\"200\"。 - 列表：多个特定返回码，逗号分隔，最多支持5个返回码。例如:\"200,202\"或\"0,1\"。 - 区间：一个返回码区间，区间内\"-\"分隔，区间之间逗号分隔，最多支持5个区间。例如\"200-204,300-399\"或\"0-5,10-12,20-30\"。

        :return: The expected_response of this MemberHealthCheckFailedReason.
        :rtype: str
        """
        return self._expected_response

    @expected_response.setter
    def expected_response(self, expected_response):
        r"""Sets the expected_response of this MemberHealthCheckFailedReason.

        **参数解释**：健康检查预期响应状态码。支持HTTP,HTTPS,GRPC健康检查。只有reason_code为RESPONSE_MISMATCH时，支持非null取值。  **取值范围**： - 单值：单个返回码。当type为GRPC时，取值范围为0-99；当type为其他协议时，取值范围为200-599。例如：\"0\"或\"200\"。 - 列表：多个特定返回码，逗号分隔，最多支持5个返回码。例如:\"200,202\"或\"0,1\"。 - 区间：一个返回码区间，区间内\"-\"分隔，区间之间逗号分隔，最多支持5个区间。例如\"200-204,300-399\"或\"0-5,10-12,20-30\"。

        :param expected_response: The expected_response of this MemberHealthCheckFailedReason.
        :type expected_response: str
        """
        self._expected_response = expected_response

    @property
    def healthcheck_response(self):
        r"""Gets the healthcheck_response of this MemberHealthCheckFailedReason.

        **参数解释**：健康检查探测实际响应状态码。支持HTTP,HTTPS,GRPC健康检查。只有reason_code为RESPONSE_MISMATCH时，支持非null取值。  **取值范围**： - 单个返回码。当type为GRPC时，取值范围为0-99；当type为其他协议时，取值范围为200-599。例如：\"0\"或\"200\"。

        :return: The healthcheck_response of this MemberHealthCheckFailedReason.
        :rtype: str
        """
        return self._healthcheck_response

    @healthcheck_response.setter
    def healthcheck_response(self, healthcheck_response):
        r"""Sets the healthcheck_response of this MemberHealthCheckFailedReason.

        **参数解释**：健康检查探测实际响应状态码。支持HTTP,HTTPS,GRPC健康检查。只有reason_code为RESPONSE_MISMATCH时，支持非null取值。  **取值范围**： - 单个返回码。当type为GRPC时，取值范围为0-99；当type为其他协议时，取值范围为200-599。例如：\"0\"或\"200\"。

        :param healthcheck_response: The healthcheck_response of this MemberHealthCheckFailedReason.
        :type healthcheck_response: str
        """
        self._healthcheck_response = healthcheck_response

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
        if not isinstance(other, MemberHealthCheckFailedReason):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
