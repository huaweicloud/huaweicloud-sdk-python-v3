# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ElbConnectionUpdateRequest:

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
        'm_tls': 'bool',
        'ca_cert_id': 'str',
        'server_cert_id': 'str',
        'sni_cert_ids': 'list[str]',
        'action': 'str'
    }

    attribute_map = {
        'elb_id': 'elb_id',
        'm_tls': 'm_tls',
        'ca_cert_id': 'ca_cert_id',
        'server_cert_id': 'server_cert_id',
        'sni_cert_ids': 'sni_cert_ids',
        'action': 'action'
    }

    def __init__(self, elb_id=None, m_tls=None, ca_cert_id=None, server_cert_id=None, sni_cert_ids=None, action=None):
        r"""ElbConnectionUpdateRequest

        The model defined in huaweicloud sdk

        :param elb_id: **参数解释：** 负载均衡器ID。 **约束限制：**  不涉及。 **取值范围：** 不涉及。 **默认取值：**  不涉及。
        :type elb_id: str
        :param m_tls: **参数解释：** 负载均衡器的HTTPS监听器是否开启双向认证。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置为true，否则忽略该配置 **取值范围：** 不涉及。 **默认取值：** false
        :type m_tls: bool
        :param ca_cert_id: **参数解释：** 负载均衡器的HTTPS监听器配置的客户端证书ID。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置 **取值范围：** 不涉及。 **默认取值：**  不涉及。
        :type ca_cert_id: str
        :param server_cert_id: **参数解释：** 负载均衡器的HTTPS监听器配置的服务端证书ID。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type server_cert_id: str
        :param sni_cert_ids: **参数解释：** 负载均衡器的HTTPS监听器配置的SNI（服务器名称指示）证书ID列表。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type sni_cert_ids: list[str]
        :param action: **参数解释：** ELB接入操作。 **约束限制：** 不涉及。 **取值范围：** - RETRY：重试连接（仅当连接状态为CONNECT_FAILED时可用）。 - SYNC_ADDR：同步ELB地址（仅当连接状态为CONNECTED时可用）。 **默认取值：** 不涉及。
        :type action: str
        """
        
        

        self._elb_id = None
        self._m_tls = None
        self._ca_cert_id = None
        self._server_cert_id = None
        self._sni_cert_ids = None
        self._action = None
        self.discriminator = None

        self.elb_id = elb_id
        if m_tls is not None:
            self.m_tls = m_tls
        if ca_cert_id is not None:
            self.ca_cert_id = ca_cert_id
        if server_cert_id is not None:
            self.server_cert_id = server_cert_id
        if sni_cert_ids is not None:
            self.sni_cert_ids = sni_cert_ids
        if action is not None:
            self.action = action

    @property
    def elb_id(self):
        r"""Gets the elb_id of this ElbConnectionUpdateRequest.

        **参数解释：** 负载均衡器ID。 **约束限制：**  不涉及。 **取值范围：** 不涉及。 **默认取值：**  不涉及。

        :return: The elb_id of this ElbConnectionUpdateRequest.
        :rtype: str
        """
        return self._elb_id

    @elb_id.setter
    def elb_id(self, elb_id):
        r"""Sets the elb_id of this ElbConnectionUpdateRequest.

        **参数解释：** 负载均衡器ID。 **约束限制：**  不涉及。 **取值范围：** 不涉及。 **默认取值：**  不涉及。

        :param elb_id: The elb_id of this ElbConnectionUpdateRequest.
        :type elb_id: str
        """
        self._elb_id = elb_id

    @property
    def m_tls(self):
        r"""Gets the m_tls of this ElbConnectionUpdateRequest.

        **参数解释：** 负载均衡器的HTTPS监听器是否开启双向认证。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置为true，否则忽略该配置 **取值范围：** 不涉及。 **默认取值：** false

        :return: The m_tls of this ElbConnectionUpdateRequest.
        :rtype: bool
        """
        return self._m_tls

    @m_tls.setter
    def m_tls(self, m_tls):
        r"""Sets the m_tls of this ElbConnectionUpdateRequest.

        **参数解释：** 负载均衡器的HTTPS监听器是否开启双向认证。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置为true，否则忽略该配置 **取值范围：** 不涉及。 **默认取值：** false

        :param m_tls: The m_tls of this ElbConnectionUpdateRequest.
        :type m_tls: bool
        """
        self._m_tls = m_tls

    @property
    def ca_cert_id(self):
        r"""Gets the ca_cert_id of this ElbConnectionUpdateRequest.

        **参数解释：** 负载均衡器的HTTPS监听器配置的客户端证书ID。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置 **取值范围：** 不涉及。 **默认取值：**  不涉及。

        :return: The ca_cert_id of this ElbConnectionUpdateRequest.
        :rtype: str
        """
        return self._ca_cert_id

    @ca_cert_id.setter
    def ca_cert_id(self, ca_cert_id):
        r"""Sets the ca_cert_id of this ElbConnectionUpdateRequest.

        **参数解释：** 负载均衡器的HTTPS监听器配置的客户端证书ID。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置 **取值范围：** 不涉及。 **默认取值：**  不涉及。

        :param ca_cert_id: The ca_cert_id of this ElbConnectionUpdateRequest.
        :type ca_cert_id: str
        """
        self._ca_cert_id = ca_cert_id

    @property
    def server_cert_id(self):
        r"""Gets the server_cert_id of this ElbConnectionUpdateRequest.

        **参数解释：** 负载均衡器的HTTPS监听器配置的服务端证书ID。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The server_cert_id of this ElbConnectionUpdateRequest.
        :rtype: str
        """
        return self._server_cert_id

    @server_cert_id.setter
    def server_cert_id(self, server_cert_id):
        r"""Sets the server_cert_id of this ElbConnectionUpdateRequest.

        **参数解释：** 负载均衡器的HTTPS监听器配置的服务端证书ID。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param server_cert_id: The server_cert_id of this ElbConnectionUpdateRequest.
        :type server_cert_id: str
        """
        self._server_cert_id = server_cert_id

    @property
    def sni_cert_ids(self):
        r"""Gets the sni_cert_ids of this ElbConnectionUpdateRequest.

        **参数解释：** 负载均衡器的HTTPS监听器配置的SNI（服务器名称指示）证书ID列表。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The sni_cert_ids of this ElbConnectionUpdateRequest.
        :rtype: list[str]
        """
        return self._sni_cert_ids

    @sni_cert_ids.setter
    def sni_cert_ids(self, sni_cert_ids):
        r"""Sets the sni_cert_ids of this ElbConnectionUpdateRequest.

        **参数解释：** 负载均衡器的HTTPS监听器配置的SNI（服务器名称指示）证书ID列表。 **约束限制：** 仅推理服务协议为HTTPS或WSS时可配置，否则忽略该配置。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param sni_cert_ids: The sni_cert_ids of this ElbConnectionUpdateRequest.
        :type sni_cert_ids: list[str]
        """
        self._sni_cert_ids = sni_cert_ids

    @property
    def action(self):
        r"""Gets the action of this ElbConnectionUpdateRequest.

        **参数解释：** ELB接入操作。 **约束限制：** 不涉及。 **取值范围：** - RETRY：重试连接（仅当连接状态为CONNECT_FAILED时可用）。 - SYNC_ADDR：同步ELB地址（仅当连接状态为CONNECTED时可用）。 **默认取值：** 不涉及。

        :return: The action of this ElbConnectionUpdateRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ElbConnectionUpdateRequest.

        **参数解释：** ELB接入操作。 **约束限制：** 不涉及。 **取值范围：** - RETRY：重试连接（仅当连接状态为CONNECT_FAILED时可用）。 - SYNC_ADDR：同步ELB地址（仅当连接状态为CONNECTED时可用）。 **默认取值：** 不涉及。

        :param action: The action of this ElbConnectionUpdateRequest.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, ElbConnectionUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
