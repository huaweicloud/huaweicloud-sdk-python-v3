# coding: utf-8

import pprint
import re

import six





class CreateListenerOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'client_ca_tls_container_ref': 'str',
        'default_pool_id': 'str',
        'default_tls_container_ref': 'str',
        'description': 'str',
        'http2_enable': 'bool',
        'insert_headers': 'ListenerInsertHeaders',
        'loadbalancer_id': 'str',
        'name': 'str',
        'project_id': 'str',
        'protocol': 'str',
        'protocol_port': 'int',
        'sni_container_refs': 'list[str]',
        'tags': 'list[Tag]',
        'tls_ciphers_policy': 'str',
        'enable_member_retry': 'bool',
        'keepalive_timeout': 'int',
        'client_timeout': 'int',
        'member_timeout': 'int',
        'ipgroup': 'CreateListenerIpGroupOption',
        'transparent_client_ip_enable': 'bool'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'client_ca_tls_container_ref': 'client_ca_tls_container_ref',
        'default_pool_id': 'default_pool_id',
        'default_tls_container_ref': 'default_tls_container_ref',
        'description': 'description',
        'http2_enable': 'http2_enable',
        'insert_headers': 'insert_headers',
        'loadbalancer_id': 'loadbalancer_id',
        'name': 'name',
        'project_id': 'project_id',
        'protocol': 'protocol',
        'protocol_port': 'protocol_port',
        'sni_container_refs': 'sni_container_refs',
        'tags': 'tags',
        'tls_ciphers_policy': 'tls_ciphers_policy',
        'enable_member_retry': 'enable_member_retry',
        'keepalive_timeout': 'keepalive_timeout',
        'client_timeout': 'client_timeout',
        'member_timeout': 'member_timeout',
        'ipgroup': 'ipgroup',
        'transparent_client_ip_enable': 'transparent_client_ip_enable'
    }

    def __init__(self, admin_state_up=None, client_ca_tls_container_ref=None, default_pool_id=None, default_tls_container_ref=None, description=None, http2_enable=None, insert_headers=None, loadbalancer_id=None, name=None, project_id=None, protocol=None, protocol_port=None, sni_container_refs=None, tags=None, tls_ciphers_policy=None, enable_member_retry=True, keepalive_timeout=None, client_timeout=60, member_timeout=60, ipgroup=None, transparent_client_ip_enable=False):
        """CreateListenerOption - a model defined in huaweicloud sdk"""
        
        

        self._admin_state_up = None
        self._client_ca_tls_container_ref = None
        self._default_pool_id = None
        self._default_tls_container_ref = None
        self._description = None
        self._http2_enable = None
        self._insert_headers = None
        self._loadbalancer_id = None
        self._name = None
        self._project_id = None
        self._protocol = None
        self._protocol_port = None
        self._sni_container_refs = None
        self._tags = None
        self._tls_ciphers_policy = None
        self._enable_member_retry = None
        self._keepalive_timeout = None
        self._client_timeout = None
        self._member_timeout = None
        self._ipgroup = None
        self._transparent_client_ip_enable = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if client_ca_tls_container_ref is not None:
            self.client_ca_tls_container_ref = client_ca_tls_container_ref
        if default_pool_id is not None:
            self.default_pool_id = default_pool_id
        if default_tls_container_ref is not None:
            self.default_tls_container_ref = default_tls_container_ref
        if description is not None:
            self.description = description
        if http2_enable is not None:
            self.http2_enable = http2_enable
        if insert_headers is not None:
            self.insert_headers = insert_headers
        self.loadbalancer_id = loadbalancer_id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        self.protocol = protocol
        self.protocol_port = protocol_port
        if sni_container_refs is not None:
            self.sni_container_refs = sni_container_refs
        if tags is not None:
            self.tags = tags
        if tls_ciphers_policy is not None:
            self.tls_ciphers_policy = tls_ciphers_policy
        if enable_member_retry is not None:
            self.enable_member_retry = enable_member_retry
        if keepalive_timeout is not None:
            self.keepalive_timeout = keepalive_timeout
        if client_timeout is not None:
            self.client_timeout = client_timeout
        if member_timeout is not None:
            self.member_timeout = member_timeout
        if ipgroup is not None:
            self.ipgroup = ipgroup
        if transparent_client_ip_enable is not None:
            self.transparent_client_ip_enable = transparent_client_ip_enable

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateListenerOption.

        监听器的管理状态。只支持设定为true，该字段的值无实际意义。

        :return: The admin_state_up of this CreateListenerOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateListenerOption.

        监听器的管理状态。只支持设定为true，该字段的值无实际意义。

        :param admin_state_up: The admin_state_up of this CreateListenerOption.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def client_ca_tls_container_ref(self):
        """Gets the client_ca_tls_container_ref of this CreateListenerOption.

        监听器使用的CA证书ID。

        :return: The client_ca_tls_container_ref of this CreateListenerOption.
        :rtype: str
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        """Sets the client_ca_tls_container_ref of this CreateListenerOption.

        监听器使用的CA证书ID。

        :param client_ca_tls_container_ref: The client_ca_tls_container_ref of this CreateListenerOption.
        :type: str
        """
        self._client_ca_tls_container_ref = client_ca_tls_container_ref

    @property
    def default_pool_id(self):
        """Gets the default_pool_id of this CreateListenerOption.

        监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。

        :return: The default_pool_id of this CreateListenerOption.
        :rtype: str
        """
        return self._default_pool_id

    @default_pool_id.setter
    def default_pool_id(self, default_pool_id):
        """Sets the default_pool_id of this CreateListenerOption.

        监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。

        :param default_pool_id: The default_pool_id of this CreateListenerOption.
        :type: str
        """
        self._default_pool_id = default_pool_id

    @property
    def default_tls_container_ref(self):
        """Gets the default_tls_container_ref of this CreateListenerOption.

        监听器使用的服务器证书ID。

        :return: The default_tls_container_ref of this CreateListenerOption.
        :rtype: str
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        """Sets the default_tls_container_ref of this CreateListenerOption.

        监听器使用的服务器证书ID。

        :param default_tls_container_ref: The default_tls_container_ref of this CreateListenerOption.
        :type: str
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def description(self):
        """Gets the description of this CreateListenerOption.

        监听器的描述信息

        :return: The description of this CreateListenerOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateListenerOption.

        监听器的描述信息

        :param description: The description of this CreateListenerOption.
        :type: str
        """
        self._description = description

    @property
    def http2_enable(self):
        """Gets the http2_enable of this CreateListenerOption.

        HTTP2功能的开启状态。该字段只有当监听器的协议是TERMINATED_HTTPS时生效。

        :return: The http2_enable of this CreateListenerOption.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this CreateListenerOption.

        HTTP2功能的开启状态。该字段只有当监听器的协议是TERMINATED_HTTPS时生效。

        :param http2_enable: The http2_enable of this CreateListenerOption.
        :type: bool
        """
        self._http2_enable = http2_enable

    @property
    def insert_headers(self):
        """Gets the insert_headers of this CreateListenerOption.


        :return: The insert_headers of this CreateListenerOption.
        :rtype: ListenerInsertHeaders
        """
        return self._insert_headers

    @insert_headers.setter
    def insert_headers(self, insert_headers):
        """Sets the insert_headers of this CreateListenerOption.


        :param insert_headers: The insert_headers of this CreateListenerOption.
        :type: ListenerInsertHeaders
        """
        self._insert_headers = insert_headers

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this CreateListenerOption.

        监听器关联的负载均衡器 ID

        :return: The loadbalancer_id of this CreateListenerOption.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this CreateListenerOption.

        监听器关联的负载均衡器 ID

        :param loadbalancer_id: The loadbalancer_id of this CreateListenerOption.
        :type: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def name(self):
        """Gets the name of this CreateListenerOption.

        监听器名称

        :return: The name of this CreateListenerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateListenerOption.

        监听器名称

        :param name: The name of this CreateListenerOption.
        :type: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this CreateListenerOption.

        监听器所在的项目ID。

        :return: The project_id of this CreateListenerOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateListenerOption.

        监听器所在的项目ID。

        :param project_id: The project_id of this CreateListenerOption.
        :type: str
        """
        self._project_id = project_id

    @property
    def protocol(self):
        """Gets the protocol of this CreateListenerOption.

        监听器的监听协议。 支持TCP、HTTP、UDP、TERMINATED_HTTPS。

        :return: The protocol of this CreateListenerOption.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateListenerOption.

        监听器的监听协议。 支持TCP、HTTP、UDP、TERMINATED_HTTPS。

        :param protocol: The protocol of this CreateListenerOption.
        :type: str
        """
        self._protocol = protocol

    @property
    def protocol_port(self):
        """Gets the protocol_port of this CreateListenerOption.

        监听器的监听端口。

        :return: The protocol_port of this CreateListenerOption.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this CreateListenerOption.

        监听器的监听端口。

        :param protocol_port: The protocol_port of this CreateListenerOption.
        :type: int
        """
        self._protocol_port = protocol_port

    @property
    def sni_container_refs(self):
        """Gets the sni_container_refs of this CreateListenerOption.

        监听器使用的SNI证书（带域名的服务器证书）ID的列表。 各SNI证书的域名不允许重复。 各SNI证书域名总数不超过30。

        :return: The sni_container_refs of this CreateListenerOption.
        :rtype: list[str]
        """
        return self._sni_container_refs

    @sni_container_refs.setter
    def sni_container_refs(self, sni_container_refs):
        """Sets the sni_container_refs of this CreateListenerOption.

        监听器使用的SNI证书（带域名的服务器证书）ID的列表。 各SNI证书的域名不允许重复。 各SNI证书域名总数不超过30。

        :param sni_container_refs: The sni_container_refs of this CreateListenerOption.
        :type: list[str]
        """
        self._sni_container_refs = sni_container_refs

    @property
    def tags(self):
        """Gets the tags of this CreateListenerOption.

        标签列表

        :return: The tags of this CreateListenerOption.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateListenerOption.

        标签列表

        :param tags: The tags of this CreateListenerOption.
        :type: list[Tag]
        """
        self._tags = tags

    @property
    def tls_ciphers_policy(self):
        """Gets the tls_ciphers_policy of this CreateListenerOption.

        监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效，且默认值为tls-1-0。 取值包括：tls-1-0-inherit,tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict，tls-1-2-fs六种安全策略

        :return: The tls_ciphers_policy of this CreateListenerOption.
        :rtype: str
        """
        return self._tls_ciphers_policy

    @tls_ciphers_policy.setter
    def tls_ciphers_policy(self, tls_ciphers_policy):
        """Sets the tls_ciphers_policy of this CreateListenerOption.

        监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效，且默认值为tls-1-0。 取值包括：tls-1-0-inherit,tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict，tls-1-2-fs六种安全策略

        :param tls_ciphers_policy: The tls_ciphers_policy of this CreateListenerOption.
        :type: str
        """
        self._tls_ciphers_policy = tls_ciphers_policy

    @property
    def enable_member_retry(self):
        """Gets the enable_member_retry of this CreateListenerOption.

        是否关闭后端服务器的重试。 仅protocol为HTTP、HTTPS时支持指定该字段。

        :return: The enable_member_retry of this CreateListenerOption.
        :rtype: bool
        """
        return self._enable_member_retry

    @enable_member_retry.setter
    def enable_member_retry(self, enable_member_retry):
        """Sets the enable_member_retry of this CreateListenerOption.

        是否关闭后端服务器的重试。 仅protocol为HTTP、HTTPS时支持指定该字段。

        :param enable_member_retry: The enable_member_retry of this CreateListenerOption.
        :type: bool
        """
        self._enable_member_retry = enable_member_retry

    @property
    def keepalive_timeout(self):
        """Gets the keepalive_timeout of this CreateListenerOption.

        TCP监听器配置空闲超时时间，取值范围为（10-900s）默认值为300s，HTTP/TERMINATED_HTTPS监听器为客户端连接空闲超时时间，取值范围为（1-300s）默认值为15s。 UDP监听器不支持此字段

        :return: The keepalive_timeout of this CreateListenerOption.
        :rtype: int
        """
        return self._keepalive_timeout

    @keepalive_timeout.setter
    def keepalive_timeout(self, keepalive_timeout):
        """Sets the keepalive_timeout of this CreateListenerOption.

        TCP监听器配置空闲超时时间，取值范围为（10-900s）默认值为300s，HTTP/TERMINATED_HTTPS监听器为客户端连接空闲超时时间，取值范围为（1-300s）默认值为15s。 UDP监听器不支持此字段

        :param keepalive_timeout: The keepalive_timeout of this CreateListenerOption.
        :type: int
        """
        self._keepalive_timeout = keepalive_timeout

    @property
    def client_timeout(self):
        """Gets the client_timeout of this CreateListenerOption.

        等待客户端请求超时时间，仅限协议为HTTP， TERMINATED_HTTPS的监听器配置。取值范围为1-60s, 默认值为60s TCP，UDP协议的监听器不支持此字段

        :return: The client_timeout of this CreateListenerOption.
        :rtype: int
        """
        return self._client_timeout

    @client_timeout.setter
    def client_timeout(self, client_timeout):
        """Sets the client_timeout of this CreateListenerOption.

        等待客户端请求超时时间，仅限协议为HTTP， TERMINATED_HTTPS的监听器配置。取值范围为1-60s, 默认值为60s TCP，UDP协议的监听器不支持此字段

        :param client_timeout: The client_timeout of this CreateListenerOption.
        :type: int
        """
        self._client_timeout = client_timeout

    @property
    def member_timeout(self):
        """Gets the member_timeout of this CreateListenerOption.

        等待后端服务器请求超时时间，仅限协议为HTTP， TERMINATED_HTTPS的监听器配置。取值范围为1-300s，默认为60s TCP，UDP协议的监听器不支持此字段

        :return: The member_timeout of this CreateListenerOption.
        :rtype: int
        """
        return self._member_timeout

    @member_timeout.setter
    def member_timeout(self, member_timeout):
        """Sets the member_timeout of this CreateListenerOption.

        等待后端服务器请求超时时间，仅限协议为HTTP， TERMINATED_HTTPS的监听器配置。取值范围为1-300s，默认为60s TCP，UDP协议的监听器不支持此字段

        :param member_timeout: The member_timeout of this CreateListenerOption.
        :type: int
        """
        self._member_timeout = member_timeout

    @property
    def ipgroup(self):
        """Gets the ipgroup of this CreateListenerOption.


        :return: The ipgroup of this CreateListenerOption.
        :rtype: CreateListenerIpGroupOption
        """
        return self._ipgroup

    @ipgroup.setter
    def ipgroup(self, ipgroup):
        """Sets the ipgroup of this CreateListenerOption.


        :param ipgroup: The ipgroup of this CreateListenerOption.
        :type: CreateListenerIpGroupOption
        """
        self._ipgroup = ipgroup

    @property
    def transparent_client_ip_enable(self):
        """Gets the transparent_client_ip_enable of this CreateListenerOption.

        获取客户端真实IP

        :return: The transparent_client_ip_enable of this CreateListenerOption.
        :rtype: bool
        """
        return self._transparent_client_ip_enable

    @transparent_client_ip_enable.setter
    def transparent_client_ip_enable(self, transparent_client_ip_enable):
        """Sets the transparent_client_ip_enable of this CreateListenerOption.

        获取客户端真实IP

        :param transparent_client_ip_enable: The transparent_client_ip_enable of this CreateListenerOption.
        :type: bool
        """
        self._transparent_client_ip_enable = transparent_client_ip_enable

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateListenerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
