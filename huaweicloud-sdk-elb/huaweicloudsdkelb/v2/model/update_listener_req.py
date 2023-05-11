# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateListenerReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'connection_limit': 'int',
        'http2_enable': 'bool',
        'default_pool_id': 'str',
        'default_tls_container_ref': 'str',
        'client_ca_tls_container_ref': 'str',
        'sni_container_refs': 'list[str]',
        'insert_headers': 'InsertHeader',
        'tls_ciphers_policy': 'str',
        'admin_state_up': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'connection_limit': 'connection_limit',
        'http2_enable': 'http2_enable',
        'default_pool_id': 'default_pool_id',
        'default_tls_container_ref': 'default_tls_container_ref',
        'client_ca_tls_container_ref': 'client_ca_tls_container_ref',
        'sni_container_refs': 'sni_container_refs',
        'insert_headers': 'insert_headers',
        'tls_ciphers_policy': 'tls_ciphers_policy',
        'admin_state_up': 'admin_state_up'
    }

    def __init__(self, name=None, description=None, connection_limit=None, http2_enable=None, default_pool_id=None, default_tls_container_ref=None, client_ca_tls_container_ref=None, sni_container_refs=None, insert_headers=None, tls_ciphers_policy=None, admin_state_up=None):
        """UpdateListenerReq

        The model defined in huaweicloud sdk

        :param name: 监听器名称。
        :type name: str
        :param description: 监听器的描述信息
        :type description: str
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
        :param sni_container_refs: 监听器使用的SNI证书（带域名的服务器证书）ID的列表。
        :type sni_container_refs: list[str]
        :param insert_headers: 
        :type insert_headers: :class:`huaweicloudsdkelb.v2.InsertHeader`
        :param tls_ciphers_policy: 监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效。  取值包括：tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict多种安全策略。  加密套件的排序为国密套件、ecc套件、rsa套件、tls1.3协议的套件（即支持ecc又支持rsa）
        :type tls_ciphers_policy: str
        :param admin_state_up: 监听器的管理状态。  该字段为预留字段，暂未启动。只支持设定为true
        :type admin_state_up: bool
        """
        
        

        self._name = None
        self._description = None
        self._connection_limit = None
        self._http2_enable = None
        self._default_pool_id = None
        self._default_tls_container_ref = None
        self._client_ca_tls_container_ref = None
        self._sni_container_refs = None
        self._insert_headers = None
        self._tls_ciphers_policy = None
        self._admin_state_up = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
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
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up

    @property
    def name(self):
        """Gets the name of this UpdateListenerReq.

        监听器名称。

        :return: The name of this UpdateListenerReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateListenerReq.

        监听器名称。

        :param name: The name of this UpdateListenerReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateListenerReq.

        监听器的描述信息

        :return: The description of this UpdateListenerReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateListenerReq.

        监听器的描述信息

        :param description: The description of this UpdateListenerReq.
        :type description: str
        """
        self._description = description

    @property
    def connection_limit(self):
        """Gets the connection_limit of this UpdateListenerReq.

        监听器的最大连接数。该字段为预留字段，暂未启用。默认为-1。

        :return: The connection_limit of this UpdateListenerReq.
        :rtype: int
        """
        return self._connection_limit

    @connection_limit.setter
    def connection_limit(self, connection_limit):
        """Sets the connection_limit of this UpdateListenerReq.

        监听器的最大连接数。该字段为预留字段，暂未启用。默认为-1。

        :param connection_limit: The connection_limit of this UpdateListenerReq.
        :type connection_limit: int
        """
        self._connection_limit = connection_limit

    @property
    def http2_enable(self):
        """Gets the http2_enable of this UpdateListenerReq.

        HTTP2功能的开启状态。该字段只有当监听器的协议是TERMINATED_HTTPS时才有意义。

        :return: The http2_enable of this UpdateListenerReq.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this UpdateListenerReq.

        HTTP2功能的开启状态。该字段只有当监听器的协议是TERMINATED_HTTPS时才有意义。

        :param http2_enable: The http2_enable of this UpdateListenerReq.
        :type http2_enable: bool
        """
        self._http2_enable = http2_enable

    @property
    def default_pool_id(self):
        """Gets the default_pool_id of this UpdateListenerReq.

        监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。当该字段为null时，表示监听器无默认的后端云服务器组。

        :return: The default_pool_id of this UpdateListenerReq.
        :rtype: str
        """
        return self._default_pool_id

    @default_pool_id.setter
    def default_pool_id(self, default_pool_id):
        """Sets the default_pool_id of this UpdateListenerReq.

        监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。当该字段为null时，表示监听器无默认的后端云服务器组。

        :param default_pool_id: The default_pool_id of this UpdateListenerReq.
        :type default_pool_id: str
        """
        self._default_pool_id = default_pool_id

    @property
    def default_tls_container_ref(self):
        """Gets the default_tls_container_ref of this UpdateListenerReq.

        监听器使用的服务器证书ID。当protocol参数为TERMINATED_HTTPS时，为必选字段

        :return: The default_tls_container_ref of this UpdateListenerReq.
        :rtype: str
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        """Sets the default_tls_container_ref of this UpdateListenerReq.

        监听器使用的服务器证书ID。当protocol参数为TERMINATED_HTTPS时，为必选字段

        :param default_tls_container_ref: The default_tls_container_ref of this UpdateListenerReq.
        :type default_tls_container_ref: str
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def client_ca_tls_container_ref(self):
        """Gets the client_ca_tls_container_ref of this UpdateListenerReq.

        监听器使用的CA证书ID。

        :return: The client_ca_tls_container_ref of this UpdateListenerReq.
        :rtype: str
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        """Sets the client_ca_tls_container_ref of this UpdateListenerReq.

        监听器使用的CA证书ID。

        :param client_ca_tls_container_ref: The client_ca_tls_container_ref of this UpdateListenerReq.
        :type client_ca_tls_container_ref: str
        """
        self._client_ca_tls_container_ref = client_ca_tls_container_ref

    @property
    def sni_container_refs(self):
        """Gets the sni_container_refs of this UpdateListenerReq.

        监听器使用的SNI证书（带域名的服务器证书）ID的列表。

        :return: The sni_container_refs of this UpdateListenerReq.
        :rtype: list[str]
        """
        return self._sni_container_refs

    @sni_container_refs.setter
    def sni_container_refs(self, sni_container_refs):
        """Sets the sni_container_refs of this UpdateListenerReq.

        监听器使用的SNI证书（带域名的服务器证书）ID的列表。

        :param sni_container_refs: The sni_container_refs of this UpdateListenerReq.
        :type sni_container_refs: list[str]
        """
        self._sni_container_refs = sni_container_refs

    @property
    def insert_headers(self):
        """Gets the insert_headers of this UpdateListenerReq.

        :return: The insert_headers of this UpdateListenerReq.
        :rtype: :class:`huaweicloudsdkelb.v2.InsertHeader`
        """
        return self._insert_headers

    @insert_headers.setter
    def insert_headers(self, insert_headers):
        """Sets the insert_headers of this UpdateListenerReq.

        :param insert_headers: The insert_headers of this UpdateListenerReq.
        :type insert_headers: :class:`huaweicloudsdkelb.v2.InsertHeader`
        """
        self._insert_headers = insert_headers

    @property
    def tls_ciphers_policy(self):
        """Gets the tls_ciphers_policy of this UpdateListenerReq.

        监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效。  取值包括：tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict多种安全策略。  加密套件的排序为国密套件、ecc套件、rsa套件、tls1.3协议的套件（即支持ecc又支持rsa）

        :return: The tls_ciphers_policy of this UpdateListenerReq.
        :rtype: str
        """
        return self._tls_ciphers_policy

    @tls_ciphers_policy.setter
    def tls_ciphers_policy(self, tls_ciphers_policy):
        """Sets the tls_ciphers_policy of this UpdateListenerReq.

        监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效。  取值包括：tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict多种安全策略。  加密套件的排序为国密套件、ecc套件、rsa套件、tls1.3协议的套件（即支持ecc又支持rsa）

        :param tls_ciphers_policy: The tls_ciphers_policy of this UpdateListenerReq.
        :type tls_ciphers_policy: str
        """
        self._tls_ciphers_policy = tls_ciphers_policy

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateListenerReq.

        监听器的管理状态。  该字段为预留字段，暂未启动。只支持设定为true

        :return: The admin_state_up of this UpdateListenerReq.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateListenerReq.

        监听器的管理状态。  该字段为预留字段，暂未启动。只支持设定为true

        :param admin_state_up: The admin_state_up of this UpdateListenerReq.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

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
        if not isinstance(other, UpdateListenerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
