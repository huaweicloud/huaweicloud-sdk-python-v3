# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Elbv3Listener:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'protocol': 'str',
        'protocol_port': 'int',
        'default_tls_container_ref': 'str',
        'client_ca_tls_container_ref': 'str',
        'ipgroup': 'ListenerIpGroup'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'protocol': 'protocol',
        'protocol_port': 'protocol_port',
        'default_tls_container_ref': 'default_tls_container_ref',
        'client_ca_tls_container_ref': 'client_ca_tls_container_ref',
        'ipgroup': 'ipgroup'
    }

    def __init__(self, id=None, name=None, protocol=None, protocol_port=None, default_tls_container_ref=None, client_ca_tls_container_ref=None, ipgroup=None):
        r"""Elbv3Listener

        The model defined in huaweicloud sdk

        :param id: 监听器ID。
        :type id: str
        :param name: 监听器的名称。
        :type name: str
        :param protocol: 监听器的监听协议。
        :type protocol: str
        :param protocol_port: 监听器的前端监听端口。
        :type protocol_port: int
        :param default_tls_container_ref: **参数解释**： 负载均衡器监听器的服务端证书。 **取值范围**： 不涉及
        :type default_tls_container_ref: str
        :param client_ca_tls_container_ref: **参数解释**： 负载均衡器监听器的ca证书。 **取值范围**： 不涉及
        :type client_ca_tls_container_ref: str
        :param ipgroup: 
        :type ipgroup: :class:`huaweicloudsdkcss.v1.ListenerIpGroup`
        """
        
        

        self._id = None
        self._name = None
        self._protocol = None
        self._protocol_port = None
        self._default_tls_container_ref = None
        self._client_ca_tls_container_ref = None
        self._ipgroup = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if protocol is not None:
            self.protocol = protocol
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if default_tls_container_ref is not None:
            self.default_tls_container_ref = default_tls_container_ref
        if client_ca_tls_container_ref is not None:
            self.client_ca_tls_container_ref = client_ca_tls_container_ref
        if ipgroup is not None:
            self.ipgroup = ipgroup

    @property
    def id(self):
        r"""Gets the id of this Elbv3Listener.

        监听器ID。

        :return: The id of this Elbv3Listener.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Elbv3Listener.

        监听器ID。

        :param id: The id of this Elbv3Listener.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Elbv3Listener.

        监听器的名称。

        :return: The name of this Elbv3Listener.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Elbv3Listener.

        监听器的名称。

        :param name: The name of this Elbv3Listener.
        :type name: str
        """
        self._name = name

    @property
    def protocol(self):
        r"""Gets the protocol of this Elbv3Listener.

        监听器的监听协议。

        :return: The protocol of this Elbv3Listener.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this Elbv3Listener.

        监听器的监听协议。

        :param protocol: The protocol of this Elbv3Listener.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this Elbv3Listener.

        监听器的前端监听端口。

        :return: The protocol_port of this Elbv3Listener.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this Elbv3Listener.

        监听器的前端监听端口。

        :param protocol_port: The protocol_port of this Elbv3Listener.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def default_tls_container_ref(self):
        r"""Gets the default_tls_container_ref of this Elbv3Listener.

        **参数解释**： 负载均衡器监听器的服务端证书。 **取值范围**： 不涉及

        :return: The default_tls_container_ref of this Elbv3Listener.
        :rtype: str
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        r"""Sets the default_tls_container_ref of this Elbv3Listener.

        **参数解释**： 负载均衡器监听器的服务端证书。 **取值范围**： 不涉及

        :param default_tls_container_ref: The default_tls_container_ref of this Elbv3Listener.
        :type default_tls_container_ref: str
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def client_ca_tls_container_ref(self):
        r"""Gets the client_ca_tls_container_ref of this Elbv3Listener.

        **参数解释**： 负载均衡器监听器的ca证书。 **取值范围**： 不涉及

        :return: The client_ca_tls_container_ref of this Elbv3Listener.
        :rtype: str
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        r"""Sets the client_ca_tls_container_ref of this Elbv3Listener.

        **参数解释**： 负载均衡器监听器的ca证书。 **取值范围**： 不涉及

        :param client_ca_tls_container_ref: The client_ca_tls_container_ref of this Elbv3Listener.
        :type client_ca_tls_container_ref: str
        """
        self._client_ca_tls_container_ref = client_ca_tls_container_ref

    @property
    def ipgroup(self):
        r"""Gets the ipgroup of this Elbv3Listener.

        :return: The ipgroup of this Elbv3Listener.
        :rtype: :class:`huaweicloudsdkcss.v1.ListenerIpGroup`
        """
        return self._ipgroup

    @ipgroup.setter
    def ipgroup(self, ipgroup):
        r"""Sets the ipgroup of this Elbv3Listener.

        :param ipgroup: The ipgroup of this Elbv3Listener.
        :type ipgroup: :class:`huaweicloudsdkcss.v1.ListenerIpGroup`
        """
        self._ipgroup = ipgroup

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
        if not isinstance(other, Elbv3Listener):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
