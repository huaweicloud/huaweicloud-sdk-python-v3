# coding: utf-8

import pprint
import re

import six





class Listener:


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
        'connection_limit': 'int',
        'created_at': 'str',
        'default_pool_id': 'str',
        'default_tls_container_ref': 'str',
        'description': 'str',
        'http2_enable': 'bool',
        'id': 'str',
        'insert_headers': 'ListenerInsertHeaders',
        'loadbalancers': 'list[LoadBalancerRef]',
        'name': 'str',
        'project_id': 'str',
        'protocol': 'str',
        'protocol_port': 'int',
        'sni_container_refs': 'list[str]',
        'tags': 'list[Tag]',
        'updated_at': 'str',
        'tls_ciphers_policy': 'str',
        'enable_member_retry': 'bool',
        'keepalive_timeout': 'int',
        'client_timeout': 'int',
        'member_timeout': 'int',
        'ipgroup': 'ListenerIpGroup'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'client_ca_tls_container_ref': 'client_ca_tls_container_ref',
        'connection_limit': 'connection_limit',
        'created_at': 'created_at',
        'default_pool_id': 'default_pool_id',
        'default_tls_container_ref': 'default_tls_container_ref',
        'description': 'description',
        'http2_enable': 'http2_enable',
        'id': 'id',
        'insert_headers': 'insert_headers',
        'loadbalancers': 'loadbalancers',
        'name': 'name',
        'project_id': 'project_id',
        'protocol': 'protocol',
        'protocol_port': 'protocol_port',
        'sni_container_refs': 'sni_container_refs',
        'tags': 'tags',
        'updated_at': 'updated_at',
        'tls_ciphers_policy': 'tls_ciphers_policy',
        'enable_member_retry': 'enable_member_retry',
        'keepalive_timeout': 'keepalive_timeout',
        'client_timeout': 'client_timeout',
        'member_timeout': 'member_timeout',
        'ipgroup': 'ipgroup'
    }

    def __init__(self, admin_state_up=None, client_ca_tls_container_ref=None, connection_limit=None, created_at=None, default_pool_id=None, default_tls_container_ref=None, description=None, http2_enable=None, id=None, insert_headers=None, loadbalancers=None, name=None, project_id=None, protocol=None, protocol_port=None, sni_container_refs=None, tags=None, updated_at=None, tls_ciphers_policy=None, enable_member_retry=None, keepalive_timeout=None, client_timeout=None, member_timeout=None, ipgroup=None):
        """Listener - a model defined in huaweicloud sdk"""
        
        

        self._admin_state_up = None
        self._client_ca_tls_container_ref = None
        self._connection_limit = None
        self._created_at = None
        self._default_pool_id = None
        self._default_tls_container_ref = None
        self._description = None
        self._http2_enable = None
        self._id = None
        self._insert_headers = None
        self._loadbalancers = None
        self._name = None
        self._project_id = None
        self._protocol = None
        self._protocol_port = None
        self._sni_container_refs = None
        self._tags = None
        self._updated_at = None
        self._tls_ciphers_policy = None
        self._enable_member_retry = None
        self._keepalive_timeout = None
        self._client_timeout = None
        self._member_timeout = None
        self._ipgroup = None
        self.discriminator = None

        self.admin_state_up = admin_state_up
        self.client_ca_tls_container_ref = client_ca_tls_container_ref
        self.connection_limit = connection_limit
        self.created_at = created_at
        self.default_pool_id = default_pool_id
        self.default_tls_container_ref = default_tls_container_ref
        self.description = description
        self.http2_enable = http2_enable
        self.id = id
        self.insert_headers = insert_headers
        self.loadbalancers = loadbalancers
        self.name = name
        self.project_id = project_id
        self.protocol = protocol
        self.protocol_port = protocol_port
        self.sni_container_refs = sni_container_refs
        self.tags = tags
        self.updated_at = updated_at
        self.tls_ciphers_policy = tls_ciphers_policy
        self.enable_member_retry = enable_member_retry
        if keepalive_timeout is not None:
            self.keepalive_timeout = keepalive_timeout
        if client_timeout is not None:
            self.client_timeout = client_timeout
        if member_timeout is not None:
            self.member_timeout = member_timeout
        self.ipgroup = ipgroup

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this Listener.

        监听器的管理状态。只支持设定为true，该字段的值无实际意义。

        :return: The admin_state_up of this Listener.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this Listener.

        监听器的管理状态。只支持设定为true，该字段的值无实际意义。

        :param admin_state_up: The admin_state_up of this Listener.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def client_ca_tls_container_ref(self):
        """Gets the client_ca_tls_container_ref of this Listener.

        监听器使用的CA证书ID。

        :return: The client_ca_tls_container_ref of this Listener.
        :rtype: str
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        """Sets the client_ca_tls_container_ref of this Listener.

        监听器使用的CA证书ID。

        :param client_ca_tls_container_ref: The client_ca_tls_container_ref of this Listener.
        :type: str
        """
        self._client_ca_tls_container_ref = client_ca_tls_container_ref

    @property
    def connection_limit(self):
        """Gets the connection_limit of this Listener.

        监听器的最大连接数。该字段为预留字段，暂未启用。默认为-1。

        :return: The connection_limit of this Listener.
        :rtype: int
        """
        return self._connection_limit

    @connection_limit.setter
    def connection_limit(self, connection_limit):
        """Sets the connection_limit of this Listener.

        监听器的最大连接数。该字段为预留字段，暂未启用。默认为-1。

        :param connection_limit: The connection_limit of this Listener.
        :type: int
        """
        self._connection_limit = connection_limit

    @property
    def created_at(self):
        """Gets the created_at of this Listener.

        监听器的创建时间。

        :return: The created_at of this Listener.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Listener.

        监听器的创建时间。

        :param created_at: The created_at of this Listener.
        :type: str
        """
        self._created_at = created_at

    @property
    def default_pool_id(self):
        """Gets the default_pool_id of this Listener.

        监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。

        :return: The default_pool_id of this Listener.
        :rtype: str
        """
        return self._default_pool_id

    @default_pool_id.setter
    def default_pool_id(self, default_pool_id):
        """Sets the default_pool_id of this Listener.

        监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。

        :param default_pool_id: The default_pool_id of this Listener.
        :type: str
        """
        self._default_pool_id = default_pool_id

    @property
    def default_tls_container_ref(self):
        """Gets the default_tls_container_ref of this Listener.

        监听器使用的服务器证书ID。

        :return: The default_tls_container_ref of this Listener.
        :rtype: str
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        """Sets the default_tls_container_ref of this Listener.

        监听器使用的服务器证书ID。

        :param default_tls_container_ref: The default_tls_container_ref of this Listener.
        :type: str
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def description(self):
        """Gets the description of this Listener.

        监听器的描述信息

        :return: The description of this Listener.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Listener.

        监听器的描述信息

        :param description: The description of this Listener.
        :type: str
        """
        self._description = description

    @property
    def http2_enable(self):
        """Gets the http2_enable of this Listener.

        HTTP2功能的开启状态。该字段只有当监听器的协议是TERMINATED_HTTPS时生效。

        :return: The http2_enable of this Listener.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this Listener.

        HTTP2功能的开启状态。该字段只有当监听器的协议是TERMINATED_HTTPS时生效。

        :param http2_enable: The http2_enable of this Listener.
        :type: bool
        """
        self._http2_enable = http2_enable

    @property
    def id(self):
        """Gets the id of this Listener.

        监听器ID

        :return: The id of this Listener.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Listener.

        监听器ID

        :param id: The id of this Listener.
        :type: str
        """
        self._id = id

    @property
    def insert_headers(self):
        """Gets the insert_headers of this Listener.


        :return: The insert_headers of this Listener.
        :rtype: ListenerInsertHeaders
        """
        return self._insert_headers

    @insert_headers.setter
    def insert_headers(self, insert_headers):
        """Sets the insert_headers of this Listener.


        :param insert_headers: The insert_headers of this Listener.
        :type: ListenerInsertHeaders
        """
        self._insert_headers = insert_headers

    @property
    def loadbalancers(self):
        """Gets the loadbalancers of this Listener.

        监听器绑定的负载均衡器ID的列表。

        :return: The loadbalancers of this Listener.
        :rtype: list[LoadBalancerRef]
        """
        return self._loadbalancers

    @loadbalancers.setter
    def loadbalancers(self, loadbalancers):
        """Sets the loadbalancers of this Listener.

        监听器绑定的负载均衡器ID的列表。

        :param loadbalancers: The loadbalancers of this Listener.
        :type: list[LoadBalancerRef]
        """
        self._loadbalancers = loadbalancers

    @property
    def name(self):
        """Gets the name of this Listener.

        监听器名称

        :return: The name of this Listener.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Listener.

        监听器名称

        :param name: The name of this Listener.
        :type: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this Listener.

        监听器所在的项目ID。

        :return: The project_id of this Listener.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Listener.

        监听器所在的项目ID。

        :param project_id: The project_id of this Listener.
        :type: str
        """
        self._project_id = project_id

    @property
    def protocol(self):
        """Gets the protocol of this Listener.

        监听器的监听协议

        :return: The protocol of this Listener.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this Listener.

        监听器的监听协议

        :param protocol: The protocol of this Listener.
        :type: str
        """
        self._protocol = protocol

    @property
    def protocol_port(self):
        """Gets the protocol_port of this Listener.

        监听器的监听端口。

        :return: The protocol_port of this Listener.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this Listener.

        监听器的监听端口。

        :param protocol_port: The protocol_port of this Listener.
        :type: int
        """
        self._protocol_port = protocol_port

    @property
    def sni_container_refs(self):
        """Gets the sni_container_refs of this Listener.

        监听器使用的SNI证书（带域名的服务器证书）ID的列表。

        :return: The sni_container_refs of this Listener.
        :rtype: list[str]
        """
        return self._sni_container_refs

    @sni_container_refs.setter
    def sni_container_refs(self, sni_container_refs):
        """Sets the sni_container_refs of this Listener.

        监听器使用的SNI证书（带域名的服务器证书）ID的列表。

        :param sni_container_refs: The sni_container_refs of this Listener.
        :type: list[str]
        """
        self._sni_container_refs = sni_container_refs

    @property
    def tags(self):
        """Gets the tags of this Listener.

        标签列表

        :return: The tags of this Listener.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Listener.

        标签列表

        :param tags: The tags of this Listener.
        :type: list[Tag]
        """
        self._tags = tags

    @property
    def updated_at(self):
        """Gets the updated_at of this Listener.

        监听器的更新时间。

        :return: The updated_at of this Listener.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Listener.

        监听器的更新时间。

        :param updated_at: The updated_at of this Listener.
        :type: str
        """
        self._updated_at = updated_at

    @property
    def tls_ciphers_policy(self):
        """Gets the tls_ciphers_policy of this Listener.

        监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效，且默认值为tls-1-0。 取值包括：tls-1-0-inherit,tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict，tls-1-2-fs六种安全策略

        :return: The tls_ciphers_policy of this Listener.
        :rtype: str
        """
        return self._tls_ciphers_policy

    @tls_ciphers_policy.setter
    def tls_ciphers_policy(self, tls_ciphers_policy):
        """Sets the tls_ciphers_policy of this Listener.

        监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效，且默认值为tls-1-0。 取值包括：tls-1-0-inherit,tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict，tls-1-2-fs六种安全策略

        :param tls_ciphers_policy: The tls_ciphers_policy of this Listener.
        :type: str
        """
        self._tls_ciphers_policy = tls_ciphers_policy

    @property
    def enable_member_retry(self):
        """Gets the enable_member_retry of this Listener.

        是否关闭后端服务器的重试。 该字段只在protocol为HTTP、HTTPS时有意义。

        :return: The enable_member_retry of this Listener.
        :rtype: bool
        """
        return self._enable_member_retry

    @enable_member_retry.setter
    def enable_member_retry(self, enable_member_retry):
        """Sets the enable_member_retry of this Listener.

        是否关闭后端服务器的重试。 该字段只在protocol为HTTP、HTTPS时有意义。

        :param enable_member_retry: The enable_member_retry of this Listener.
        :type: bool
        """
        self._enable_member_retry = enable_member_retry

    @property
    def keepalive_timeout(self):
        """Gets the keepalive_timeout of this Listener.

        TCP监听器配置空闲超时时间，取值范围为（10-900s）默认值为300s，TCP监听器配置空闲超时时间，取值范围为（10-900s）默认值为300s，HTTP/TERMINATED_HTTPS监听器为客户端连接空闲超时时间，取值范围为（1-300s）默认值为15s。 UDP此字段无意义

        :return: The keepalive_timeout of this Listener.
        :rtype: int
        """
        return self._keepalive_timeout

    @keepalive_timeout.setter
    def keepalive_timeout(self, keepalive_timeout):
        """Sets the keepalive_timeout of this Listener.

        TCP监听器配置空闲超时时间，取值范围为（10-900s）默认值为300s，TCP监听器配置空闲超时时间，取值范围为（10-900s）默认值为300s，HTTP/TERMINATED_HTTPS监听器为客户端连接空闲超时时间，取值范围为（1-300s）默认值为15s。 UDP此字段无意义

        :param keepalive_timeout: The keepalive_timeout of this Listener.
        :type: int
        """
        self._keepalive_timeout = keepalive_timeout

    @property
    def client_timeout(self):
        """Gets the client_timeout of this Listener.

        等待客户端请求超时时间，协议为HTTP， TERMINATED_HTTPS的监听器才有意义。取值范围 1-60

        :return: The client_timeout of this Listener.
        :rtype: int
        """
        return self._client_timeout

    @client_timeout.setter
    def client_timeout(self, client_timeout):
        """Sets the client_timeout of this Listener.

        等待客户端请求超时时间，协议为HTTP， TERMINATED_HTTPS的监听器才有意义。取值范围 1-60

        :param client_timeout: The client_timeout of this Listener.
        :type: int
        """
        self._client_timeout = client_timeout

    @property
    def member_timeout(self):
        """Gets the member_timeout of this Listener.

        等待后端服务器请求超时时间，协议为HTTP， TERMINATED_HTTPS时才有意义。取值范围 1-300

        :return: The member_timeout of this Listener.
        :rtype: int
        """
        return self._member_timeout

    @member_timeout.setter
    def member_timeout(self, member_timeout):
        """Sets the member_timeout of this Listener.

        等待后端服务器请求超时时间，协议为HTTP， TERMINATED_HTTPS时才有意义。取值范围 1-300

        :param member_timeout: The member_timeout of this Listener.
        :type: int
        """
        self._member_timeout = member_timeout

    @property
    def ipgroup(self):
        """Gets the ipgroup of this Listener.


        :return: The ipgroup of this Listener.
        :rtype: ListenerIpGroup
        """
        return self._ipgroup

    @ipgroup.setter
    def ipgroup(self, ipgroup):
        """Sets the ipgroup of this Listener.


        :param ipgroup: The ipgroup of this Listener.
        :type: ListenerIpGroup
        """
        self._ipgroup = ipgroup

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
        if not isinstance(other, Listener):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
