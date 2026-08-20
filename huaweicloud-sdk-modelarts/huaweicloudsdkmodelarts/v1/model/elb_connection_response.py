# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ElbConnectionResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'elb_id': 'str',
        'listener_id': 'str',
        'm_tls': 'bool',
        'ca_cert_id': 'str',
        'server_cert_id': 'str',
        'sni_cert_ids': 'list[str]',
        'status': 'str',
        'message': 'str',
        'residual_resources': 'ResidualResources'
    }

    attribute_map = {
        'elb_id': 'elb_id',
        'listener_id': 'listener_id',
        'm_tls': 'm_tls',
        'ca_cert_id': 'ca_cert_id',
        'server_cert_id': 'server_cert_id',
        'sni_cert_ids': 'sni_cert_ids',
        'status': 'status',
        'message': 'message',
        'residual_resources': 'residual_resources'
    }

    def __init__(self, elb_id=None, listener_id=None, m_tls=None, ca_cert_id=None, server_cert_id=None, sni_cert_ids=None, status=None, message=None, residual_resources=None):
        r"""ElbConnectionResponse

        The model defined in huaweicloud sdk

        :param elb_id: **参数解释：** 负载均衡器ID。 **约束限制：**  不涉及。 **取值范围：** 不涉及。 **默认取值：**  不涉及。
        :type elb_id: str
        :param listener_id: **参数解释：** 负载均衡器的监听器ID。 **约束限制：**  不涉及。 **取值范围：** 不涉及。 **默认取值：**  不涉及。
        :type listener_id: str
        :param m_tls: **参数解释：** 负载均衡器的HTTPS监听器是否开启双向认证。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置为true，否则忽略该配置 **取值范围：** 不涉及。 **默认取值：** false
        :type m_tls: bool
        :param ca_cert_id: **参数解释：** 负载均衡器的HTTPS监听器配置的客户端证书ID。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置 **取值范围：** 不涉及。 **默认取值：**  不涉及。
        :type ca_cert_id: str
        :param server_cert_id: **参数解释：** 负载均衡器的HTTPS监听器配置的服务端证书ID。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type server_cert_id: str
        :param sni_cert_ids: **参数解释：** 负载均衡器的HTTPS监听器配置的SNI（服务器名称指示）证书ID列表。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type sni_cert_ids: list[str]
        :param status: **参数解释：** ELB连接状态。 **约束限制：** 仅在响应中返回，请求中传入不生效。 **取值范围：** - CONNECTING：连接中。 - CONNECTED：已连接。 - CONNECT_FAILED：连接失败。 - DISCONNECTING：断开中 - DISCONNET_FAILED：断开失败 **默认取值：** 不涉及。
        :type status: str
        :param message: **参数解释：** ELB连接失败时的错误信息。 **约束限制：** 仅在响应中返回，请求中传入不生效；仅当ELB连接状态为CONNECT_FAILED时返回。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type message: str
        :param residual_resources: 
        :type residual_resources: :class:`huaweicloudsdkmodelarts.v1.ResidualResources`
        """
        
        

        self._elb_id = None
        self._listener_id = None
        self._m_tls = None
        self._ca_cert_id = None
        self._server_cert_id = None
        self._sni_cert_ids = None
        self._status = None
        self._message = None
        self._residual_resources = None
        self.discriminator = None

        self.elb_id = elb_id
        if listener_id is not None:
            self.listener_id = listener_id
        if m_tls is not None:
            self.m_tls = m_tls
        if ca_cert_id is not None:
            self.ca_cert_id = ca_cert_id
        if server_cert_id is not None:
            self.server_cert_id = server_cert_id
        if sni_cert_ids is not None:
            self.sni_cert_ids = sni_cert_ids
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if residual_resources is not None:
            self.residual_resources = residual_resources

    @property
    def elb_id(self):
        r"""Gets the elb_id of this ElbConnectionResponse.

        **参数解释：** 负载均衡器ID。 **约束限制：**  不涉及。 **取值范围：** 不涉及。 **默认取值：**  不涉及。

        :return: The elb_id of this ElbConnectionResponse.
        :rtype: str
        """
        return self._elb_id

    @elb_id.setter
    def elb_id(self, elb_id):
        r"""Sets the elb_id of this ElbConnectionResponse.

        **参数解释：** 负载均衡器ID。 **约束限制：**  不涉及。 **取值范围：** 不涉及。 **默认取值：**  不涉及。

        :param elb_id: The elb_id of this ElbConnectionResponse.
        :type elb_id: str
        """
        self._elb_id = elb_id

    @property
    def listener_id(self):
        r"""Gets the listener_id of this ElbConnectionResponse.

        **参数解释：** 负载均衡器的监听器ID。 **约束限制：**  不涉及。 **取值范围：** 不涉及。 **默认取值：**  不涉及。

        :return: The listener_id of this ElbConnectionResponse.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this ElbConnectionResponse.

        **参数解释：** 负载均衡器的监听器ID。 **约束限制：**  不涉及。 **取值范围：** 不涉及。 **默认取值：**  不涉及。

        :param listener_id: The listener_id of this ElbConnectionResponse.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def m_tls(self):
        r"""Gets the m_tls of this ElbConnectionResponse.

        **参数解释：** 负载均衡器的HTTPS监听器是否开启双向认证。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置为true，否则忽略该配置 **取值范围：** 不涉及。 **默认取值：** false

        :return: The m_tls of this ElbConnectionResponse.
        :rtype: bool
        """
        return self._m_tls

    @m_tls.setter
    def m_tls(self, m_tls):
        r"""Sets the m_tls of this ElbConnectionResponse.

        **参数解释：** 负载均衡器的HTTPS监听器是否开启双向认证。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置为true，否则忽略该配置 **取值范围：** 不涉及。 **默认取值：** false

        :param m_tls: The m_tls of this ElbConnectionResponse.
        :type m_tls: bool
        """
        self._m_tls = m_tls

    @property
    def ca_cert_id(self):
        r"""Gets the ca_cert_id of this ElbConnectionResponse.

        **参数解释：** 负载均衡器的HTTPS监听器配置的客户端证书ID。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置 **取值范围：** 不涉及。 **默认取值：**  不涉及。

        :return: The ca_cert_id of this ElbConnectionResponse.
        :rtype: str
        """
        return self._ca_cert_id

    @ca_cert_id.setter
    def ca_cert_id(self, ca_cert_id):
        r"""Sets the ca_cert_id of this ElbConnectionResponse.

        **参数解释：** 负载均衡器的HTTPS监听器配置的客户端证书ID。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置 **取值范围：** 不涉及。 **默认取值：**  不涉及。

        :param ca_cert_id: The ca_cert_id of this ElbConnectionResponse.
        :type ca_cert_id: str
        """
        self._ca_cert_id = ca_cert_id

    @property
    def server_cert_id(self):
        r"""Gets the server_cert_id of this ElbConnectionResponse.

        **参数解释：** 负载均衡器的HTTPS监听器配置的服务端证书ID。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The server_cert_id of this ElbConnectionResponse.
        :rtype: str
        """
        return self._server_cert_id

    @server_cert_id.setter
    def server_cert_id(self, server_cert_id):
        r"""Sets the server_cert_id of this ElbConnectionResponse.

        **参数解释：** 负载均衡器的HTTPS监听器配置的服务端证书ID。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param server_cert_id: The server_cert_id of this ElbConnectionResponse.
        :type server_cert_id: str
        """
        self._server_cert_id = server_cert_id

    @property
    def sni_cert_ids(self):
        r"""Gets the sni_cert_ids of this ElbConnectionResponse.

        **参数解释：** 负载均衡器的HTTPS监听器配置的SNI（服务器名称指示）证书ID列表。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The sni_cert_ids of this ElbConnectionResponse.
        :rtype: list[str]
        """
        return self._sni_cert_ids

    @sni_cert_ids.setter
    def sni_cert_ids(self, sni_cert_ids):
        r"""Sets the sni_cert_ids of this ElbConnectionResponse.

        **参数解释：** 负载均衡器的HTTPS监听器配置的SNI（服务器名称指示）证书ID列表。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param sni_cert_ids: The sni_cert_ids of this ElbConnectionResponse.
        :type sni_cert_ids: list[str]
        """
        self._sni_cert_ids = sni_cert_ids

    @property
    def status(self):
        r"""Gets the status of this ElbConnectionResponse.

        **参数解释：** ELB连接状态。 **约束限制：** 仅在响应中返回，请求中传入不生效。 **取值范围：** - CONNECTING：连接中。 - CONNECTED：已连接。 - CONNECT_FAILED：连接失败。 - DISCONNECTING：断开中 - DISCONNET_FAILED：断开失败 **默认取值：** 不涉及。

        :return: The status of this ElbConnectionResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ElbConnectionResponse.

        **参数解释：** ELB连接状态。 **约束限制：** 仅在响应中返回，请求中传入不生效。 **取值范围：** - CONNECTING：连接中。 - CONNECTED：已连接。 - CONNECT_FAILED：连接失败。 - DISCONNECTING：断开中 - DISCONNET_FAILED：断开失败 **默认取值：** 不涉及。

        :param status: The status of this ElbConnectionResponse.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this ElbConnectionResponse.

        **参数解释：** ELB连接失败时的错误信息。 **约束限制：** 仅在响应中返回，请求中传入不生效；仅当ELB连接状态为CONNECT_FAILED时返回。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The message of this ElbConnectionResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ElbConnectionResponse.

        **参数解释：** ELB连接失败时的错误信息。 **约束限制：** 仅在响应中返回，请求中传入不生效；仅当ELB连接状态为CONNECT_FAILED时返回。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param message: The message of this ElbConnectionResponse.
        :type message: str
        """
        self._message = message

    @property
    def residual_resources(self):
        r"""Gets the residual_resources of this ElbConnectionResponse.

        :return: The residual_resources of this ElbConnectionResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ResidualResources`
        """
        return self._residual_resources

    @residual_resources.setter
    def residual_resources(self, residual_resources):
        r"""Sets the residual_resources of this ElbConnectionResponse.

        :param residual_resources: The residual_resources of this ElbConnectionResponse.
        :type residual_resources: :class:`huaweicloudsdkmodelarts.v1.ResidualResources`
        """
        self._residual_resources = residual_resources

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
        if not isinstance(other, ElbConnectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
