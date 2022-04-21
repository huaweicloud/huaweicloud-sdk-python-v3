# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateListenerReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'loadbalancer_id': 'str',
        'protocol': 'str',
        'protocol_port': 'int',
        'tenant_id': 'str',
        'name': 'str',
        'description': 'str',
        'admin_state_up': 'bool',
        'connection_limit': 'int',
        'http2_enable': 'bool',
        'default_pool_id': 'str',
        'default_tls_container_ref': 'str',
        'client_ca_tls_container_ref': 'str',
        'sni_container_refs': 'list[str]',
        'insert_headers': 'InsertHeader',
        'tls_ciphers_policy': 'str'
    }

    attribute_map = {
        'loadbalancer_id': 'loadbalancer_id',
        'protocol': 'protocol',
        'protocol_port': 'protocol_port',
        'tenant_id': 'tenant_id',
        'name': 'name',
        'description': 'description',
        'admin_state_up': 'admin_state_up',
        'connection_limit': 'connection_limit',
        'http2_enable': 'http2_enable',
        'default_pool_id': 'default_pool_id',
        'default_tls_container_ref': 'default_tls_container_ref',
        'client_ca_tls_container_ref': 'client_ca_tls_container_ref',
        'sni_container_refs': 'sni_container_refs',
        'insert_headers': 'insert_headers',
        'tls_ciphers_policy': 'tls_ciphers_policy'
    }

    def __init__(self, loadbalancer_id=None, protocol=None, protocol_port=None, tenant_id=None, name=None, description=None, admin_state_up=None, connection_limit=None, http2_enable=None, default_pool_id=None, default_tls_container_ref=None, client_ca_tls_container_ref=None, sni_container_refs=None, insert_headers=None, tls_ciphers_policy=None):
        """CreateListenerReq

        The model defined in huaweicloud sdk

        :param loadbalancer_id: 监听器关联的负载均衡器 ID
        :type loadbalancer_id: str
        :param protocol: 监听器的监听协议
        :type protocol: str
        :param protocol_port: 监听器的监听端口。如果监听协议为UDP，端口号不支持4789。
        :type protocol_port: int
        :param tenant_id: 监听器所在的项目ID。
        :type tenant_id: str
        :param name: 监听器名称。
        :type name: str
        :param description: 监听器的描述信息
        :type description: str
        :param admin_state_up: 监听器器的管理状态。只支持设定为true，该字段的值无实际意义。
        :type admin_state_up: bool
        :param connection_limit: 监听器的最大连接数。该字段为预留字段，暂未启用。默认为-1。
        :type connection_limit: int
        :param http2_enable: HTTP2功能的开启状态。该字段只有当监听器的协议是TERMINATED_HTTPS时才有意义。
        :type http2_enable: bool
        :param default_pool_id: 监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。当该字段为null时，表示监听器无默认的后端云服务器组。
        :type default_pool_id: str
        :param default_tls_container_ref: 监听器使用的服务器证书ID。当protocol参数为TERMINATED_HTTPS时，为必选字段
        :type default_tls_container_ref: str
        :param client_ca_tls_container_ref: 监听器使用的CA证书ID。
        :type client_ca_tls_container_ref: str
        :param sni_container_refs: 监听器使用的SNI证书（带域名的服务器证书）ID的列表。 该字段不为空列表时，SNI特性开启。该字段为空列表时，SNI特性关闭。
        :type sni_container_refs: list[str]
        :param insert_headers: 
        :type insert_headers: :class:`huaweicloudsdkelb.v2.InsertHeader`
        :param tls_ciphers_policy: 监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效，且默认值为tls-1-0。  取值包括：tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict多种安全策略。
        :type tls_ciphers_policy: str
        """
        
        

        self._loadbalancer_id = None
        self._protocol = None
        self._protocol_port = None
        self._tenant_id = None
        self._name = None
        self._description = None
        self._admin_state_up = None
        self._connection_limit = None
        self._http2_enable = None
        self._default_pool_id = None
        self._default_tls_container_ref = None
        self._client_ca_tls_container_ref = None
        self._sni_container_refs = None
        self._insert_headers = None
        self._tls_ciphers_policy = None
        self.discriminator = None

        self.loadbalancer_id = loadbalancer_id
        self.protocol = protocol
        self.protocol_port = protocol_port
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if connection_limit is not None:
            self.connection_limit = connection_limit
        if http2_enable is not None:
            self.http2_enable = http2_enable
        if default_pool_id is not None:
            self.default_pool_id = default_pool_id
        if default_tls_container_ref is not None:
            self.default_tls_container_ref = default_tls_container_ref
        if client_ca_tls_container_ref is not None:
            self.client_ca_tls_container_ref = client_ca_tls_container_ref
        if sni_container_refs is not None:
            self.sni_container_refs = sni_container_refs
        if insert_headers is not None:
            self.insert_headers = insert_headers
        if tls_ciphers_policy is not None:
            self.tls_ciphers_policy = tls_ciphers_policy

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this CreateListenerReq.

        监听器关联的负载均衡器 ID

        :return: The loadbalancer_id of this CreateListenerReq.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this CreateListenerReq.

        监听器关联的负载均衡器 ID

        :param loadbalancer_id: The loadbalancer_id of this CreateListenerReq.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def protocol(self):
        """Gets the protocol of this CreateListenerReq.

        监听器的监听协议

        :return: The protocol of this CreateListenerReq.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateListenerReq.

        监听器的监听协议

        :param protocol: The protocol of this CreateListenerReq.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def protocol_port(self):
        """Gets the protocol_port of this CreateListenerReq.

        监听器的监听端口。如果监听协议为UDP，端口号不支持4789。

        :return: The protocol_port of this CreateListenerReq.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this CreateListenerReq.

        监听器的监听端口。如果监听协议为UDP，端口号不支持4789。

        :param protocol_port: The protocol_port of this CreateListenerReq.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CreateListenerReq.

        监听器所在的项目ID。

        :return: The tenant_id of this CreateListenerReq.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CreateListenerReq.

        监听器所在的项目ID。

        :param tenant_id: The tenant_id of this CreateListenerReq.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this CreateListenerReq.

        监听器名称。

        :return: The name of this CreateListenerReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateListenerReq.

        监听器名称。

        :param name: The name of this CreateListenerReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateListenerReq.

        监听器的描述信息

        :return: The description of this CreateListenerReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateListenerReq.

        监听器的描述信息

        :param description: The description of this CreateListenerReq.
        :type description: str
        """
        self._description = description

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateListenerReq.

        监听器器的管理状态。只支持设定为true，该字段的值无实际意义。

        :return: The admin_state_up of this CreateListenerReq.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateListenerReq.

        监听器器的管理状态。只支持设定为true，该字段的值无实际意义。

        :param admin_state_up: The admin_state_up of this CreateListenerReq.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def connection_limit(self):
        """Gets the connection_limit of this CreateListenerReq.

        监听器的最大连接数。该字段为预留字段，暂未启用。默认为-1。

        :return: The connection_limit of this CreateListenerReq.
        :rtype: int
        """
        return self._connection_limit

    @connection_limit.setter
    def connection_limit(self, connection_limit):
        """Sets the connection_limit of this CreateListenerReq.

        监听器的最大连接数。该字段为预留字段，暂未启用。默认为-1。

        :param connection_limit: The connection_limit of this CreateListenerReq.
        :type connection_limit: int
        """
        self._connection_limit = connection_limit

    @property
    def http2_enable(self):
        """Gets the http2_enable of this CreateListenerReq.

        HTTP2功能的开启状态。该字段只有当监听器的协议是TERMINATED_HTTPS时才有意义。

        :return: The http2_enable of this CreateListenerReq.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this CreateListenerReq.

        HTTP2功能的开启状态。该字段只有当监听器的协议是TERMINATED_HTTPS时才有意义。

        :param http2_enable: The http2_enable of this CreateListenerReq.
        :type http2_enable: bool
        """
        self._http2_enable = http2_enable

    @property
    def default_pool_id(self):
        """Gets the default_pool_id of this CreateListenerReq.

        监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。当该字段为null时，表示监听器无默认的后端云服务器组。

        :return: The default_pool_id of this CreateListenerReq.
        :rtype: str
        """
        return self._default_pool_id

    @default_pool_id.setter
    def default_pool_id(self, default_pool_id):
        """Sets the default_pool_id of this CreateListenerReq.

        监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。当该字段为null时，表示监听器无默认的后端云服务器组。

        :param default_pool_id: The default_pool_id of this CreateListenerReq.
        :type default_pool_id: str
        """
        self._default_pool_id = default_pool_id

    @property
    def default_tls_container_ref(self):
        """Gets the default_tls_container_ref of this CreateListenerReq.

        监听器使用的服务器证书ID。当protocol参数为TERMINATED_HTTPS时，为必选字段

        :return: The default_tls_container_ref of this CreateListenerReq.
        :rtype: str
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        """Sets the default_tls_container_ref of this CreateListenerReq.

        监听器使用的服务器证书ID。当protocol参数为TERMINATED_HTTPS时，为必选字段

        :param default_tls_container_ref: The default_tls_container_ref of this CreateListenerReq.
        :type default_tls_container_ref: str
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def client_ca_tls_container_ref(self):
        """Gets the client_ca_tls_container_ref of this CreateListenerReq.

        监听器使用的CA证书ID。

        :return: The client_ca_tls_container_ref of this CreateListenerReq.
        :rtype: str
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        """Sets the client_ca_tls_container_ref of this CreateListenerReq.

        监听器使用的CA证书ID。

        :param client_ca_tls_container_ref: The client_ca_tls_container_ref of this CreateListenerReq.
        :type client_ca_tls_container_ref: str
        """
        self._client_ca_tls_container_ref = client_ca_tls_container_ref

    @property
    def sni_container_refs(self):
        """Gets the sni_container_refs of this CreateListenerReq.

        监听器使用的SNI证书（带域名的服务器证书）ID的列表。 该字段不为空列表时，SNI特性开启。该字段为空列表时，SNI特性关闭。

        :return: The sni_container_refs of this CreateListenerReq.
        :rtype: list[str]
        """
        return self._sni_container_refs

    @sni_container_refs.setter
    def sni_container_refs(self, sni_container_refs):
        """Sets the sni_container_refs of this CreateListenerReq.

        监听器使用的SNI证书（带域名的服务器证书）ID的列表。 该字段不为空列表时，SNI特性开启。该字段为空列表时，SNI特性关闭。

        :param sni_container_refs: The sni_container_refs of this CreateListenerReq.
        :type sni_container_refs: list[str]
        """
        self._sni_container_refs = sni_container_refs

    @property
    def insert_headers(self):
        """Gets the insert_headers of this CreateListenerReq.


        :return: The insert_headers of this CreateListenerReq.
        :rtype: :class:`huaweicloudsdkelb.v2.InsertHeader`
        """
        return self._insert_headers

    @insert_headers.setter
    def insert_headers(self, insert_headers):
        """Sets the insert_headers of this CreateListenerReq.


        :param insert_headers: The insert_headers of this CreateListenerReq.
        :type insert_headers: :class:`huaweicloudsdkelb.v2.InsertHeader`
        """
        self._insert_headers = insert_headers

    @property
    def tls_ciphers_policy(self):
        """Gets the tls_ciphers_policy of this CreateListenerReq.

        监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效，且默认值为tls-1-0。  取值包括：tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict多种安全策略。

        :return: The tls_ciphers_policy of this CreateListenerReq.
        :rtype: str
        """
        return self._tls_ciphers_policy

    @tls_ciphers_policy.setter
    def tls_ciphers_policy(self, tls_ciphers_policy):
        """Sets the tls_ciphers_policy of this CreateListenerReq.

        监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效，且默认值为tls-1-0。  取值包括：tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict多种安全策略。

        :param tls_ciphers_policy: The tls_ciphers_policy of this CreateListenerReq.
        :type tls_ciphers_policy: str
        """
        self._tls_ciphers_policy = tls_ciphers_policy

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
        if not isinstance(other, CreateListenerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
