# coding: utf-8

import pprint
import re

import six





class UpdateListenerOption:


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
        'name': 'str',
        'sni_container_refs': 'list[str]',
        'tls_ciphers_policy': 'str',
        'enable_member_retry': 'bool',
        'member_timeout': 'int',
        'client_timeout': 'int',
        'keepalive_timeout': 'int',
        'ipgroup': 'UpdateListenerIpGroupOption',
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
        'name': 'name',
        'sni_container_refs': 'sni_container_refs',
        'tls_ciphers_policy': 'tls_ciphers_policy',
        'enable_member_retry': 'enable_member_retry',
        'member_timeout': 'member_timeout',
        'client_timeout': 'client_timeout',
        'keepalive_timeout': 'keepalive_timeout',
        'ipgroup': 'ipgroup',
        'transparent_client_ip_enable': 'transparent_client_ip_enable'
    }

    def __init__(self, admin_state_up=None, client_ca_tls_container_ref=None, default_pool_id=None, default_tls_container_ref=None, description=None, http2_enable=None, insert_headers=None, name=None, sni_container_refs=None, tls_ciphers_policy=None, enable_member_retry=None, member_timeout=None, client_timeout=None, keepalive_timeout=None, ipgroup=None, transparent_client_ip_enable=None):
        """UpdateListenerOption - a model defined in huaweicloud sdk"""
        
        

        self._admin_state_up = None
        self._client_ca_tls_container_ref = None
        self._default_pool_id = None
        self._default_tls_container_ref = None
        self._description = None
        self._http2_enable = None
        self._insert_headers = None
        self._name = None
        self._sni_container_refs = None
        self._tls_ciphers_policy = None
        self._enable_member_retry = None
        self._member_timeout = None
        self._client_timeout = None
        self._keepalive_timeout = None
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
        if name is not None:
            self.name = name
        if sni_container_refs is not None:
            self.sni_container_refs = sni_container_refs
        if tls_ciphers_policy is not None:
            self.tls_ciphers_policy = tls_ciphers_policy
        if enable_member_retry is not None:
            self.enable_member_retry = enable_member_retry
        if member_timeout is not None:
            self.member_timeout = member_timeout
        if client_timeout is not None:
            self.client_timeout = client_timeout
        if keepalive_timeout is not None:
            self.keepalive_timeout = keepalive_timeout
        if ipgroup is not None:
            self.ipgroup = ipgroup
        if transparent_client_ip_enable is not None:
            self.transparent_client_ip_enable = transparent_client_ip_enable

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateListenerOption.

        监听器的管理状态。只支持设定为true，该字段的值无实际意义。

        :return: The admin_state_up of this UpdateListenerOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateListenerOption.

        监听器的管理状态。只支持设定为true，该字段的值无实际意义。

        :param admin_state_up: The admin_state_up of this UpdateListenerOption.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def client_ca_tls_container_ref(self):
        """Gets the client_ca_tls_container_ref of this UpdateListenerOption.

        监听器使用的CA证书ID。

        :return: The client_ca_tls_container_ref of this UpdateListenerOption.
        :rtype: str
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        """Sets the client_ca_tls_container_ref of this UpdateListenerOption.

        监听器使用的CA证书ID。

        :param client_ca_tls_container_ref: The client_ca_tls_container_ref of this UpdateListenerOption.
        :type: str
        """
        self._client_ca_tls_container_ref = client_ca_tls_container_ref

    @property
    def default_pool_id(self):
        """Gets the default_pool_id of this UpdateListenerOption.

        监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。

        :return: The default_pool_id of this UpdateListenerOption.
        :rtype: str
        """
        return self._default_pool_id

    @default_pool_id.setter
    def default_pool_id(self, default_pool_id):
        """Sets the default_pool_id of this UpdateListenerOption.

        监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。

        :param default_pool_id: The default_pool_id of this UpdateListenerOption.
        :type: str
        """
        self._default_pool_id = default_pool_id

    @property
    def default_tls_container_ref(self):
        """Gets the default_tls_container_ref of this UpdateListenerOption.

        监听器使用的服务器证书ID。

        :return: The default_tls_container_ref of this UpdateListenerOption.
        :rtype: str
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        """Sets the default_tls_container_ref of this UpdateListenerOption.

        监听器使用的服务器证书ID。

        :param default_tls_container_ref: The default_tls_container_ref of this UpdateListenerOption.
        :type: str
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def description(self):
        """Gets the description of this UpdateListenerOption.

        监听器的描述信息

        :return: The description of this UpdateListenerOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateListenerOption.

        监听器的描述信息

        :param description: The description of this UpdateListenerOption.
        :type: str
        """
        self._description = description

    @property
    def http2_enable(self):
        """Gets the http2_enable of this UpdateListenerOption.

        HTTP2功能的开启状态。该字段只有当监听器的协议是TERMINATED_HTTPS时生效。

        :return: The http2_enable of this UpdateListenerOption.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this UpdateListenerOption.

        HTTP2功能的开启状态。该字段只有当监听器的协议是TERMINATED_HTTPS时生效。

        :param http2_enable: The http2_enable of this UpdateListenerOption.
        :type: bool
        """
        self._http2_enable = http2_enable

    @property
    def insert_headers(self):
        """Gets the insert_headers of this UpdateListenerOption.


        :return: The insert_headers of this UpdateListenerOption.
        :rtype: ListenerInsertHeaders
        """
        return self._insert_headers

    @insert_headers.setter
    def insert_headers(self, insert_headers):
        """Sets the insert_headers of this UpdateListenerOption.


        :param insert_headers: The insert_headers of this UpdateListenerOption.
        :type: ListenerInsertHeaders
        """
        self._insert_headers = insert_headers

    @property
    def name(self):
        """Gets the name of this UpdateListenerOption.

        监听器名称

        :return: The name of this UpdateListenerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateListenerOption.

        监听器名称

        :param name: The name of this UpdateListenerOption.
        :type: str
        """
        self._name = name

    @property
    def sni_container_refs(self):
        """Gets the sni_container_refs of this UpdateListenerOption.

        监听器使用的SNI证书（带域名的服务器证书）ID的列表。 各SNI证书的域名不允许重复。 各SNI证书域名总数不超过30。

        :return: The sni_container_refs of this UpdateListenerOption.
        :rtype: list[str]
        """
        return self._sni_container_refs

    @sni_container_refs.setter
    def sni_container_refs(self, sni_container_refs):
        """Sets the sni_container_refs of this UpdateListenerOption.

        监听器使用的SNI证书（带域名的服务器证书）ID的列表。 各SNI证书的域名不允许重复。 各SNI证书域名总数不超过30。

        :param sni_container_refs: The sni_container_refs of this UpdateListenerOption.
        :type: list[str]
        """
        self._sni_container_refs = sni_container_refs

    @property
    def tls_ciphers_policy(self):
        """Gets the tls_ciphers_policy of this UpdateListenerOption.

        监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效，且默认值为tls-1-0。 取值包括：tls-1-0-inherit,tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict, tls-1-2-fst 六种安全策略

        :return: The tls_ciphers_policy of this UpdateListenerOption.
        :rtype: str
        """
        return self._tls_ciphers_policy

    @tls_ciphers_policy.setter
    def tls_ciphers_policy(self, tls_ciphers_policy):
        """Sets the tls_ciphers_policy of this UpdateListenerOption.

        监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效，且默认值为tls-1-0。 取值包括：tls-1-0-inherit,tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict, tls-1-2-fst 六种安全策略

        :param tls_ciphers_policy: The tls_ciphers_policy of this UpdateListenerOption.
        :type: str
        """
        self._tls_ciphers_policy = tls_ciphers_policy

    @property
    def enable_member_retry(self):
        """Gets the enable_member_retry of this UpdateListenerOption.

        是否关闭后端服务器的重试。 当前仅七层的性能共享型实例支持指定该字段。

        :return: The enable_member_retry of this UpdateListenerOption.
        :rtype: bool
        """
        return self._enable_member_retry

    @enable_member_retry.setter
    def enable_member_retry(self, enable_member_retry):
        """Sets the enable_member_retry of this UpdateListenerOption.

        是否关闭后端服务器的重试。 当前仅七层的性能共享型实例支持指定该字段。

        :param enable_member_retry: The enable_member_retry of this UpdateListenerOption.
        :type: bool
        """
        self._enable_member_retry = enable_member_retry

    @property
    def member_timeout(self):
        """Gets the member_timeout of this UpdateListenerOption.

        等待后端服务器请求超时时间，仅限协议为HTTP， TERMINATED_HTTPS的监听器配置。取值范围为1-300s，默认为60s TCP，UDP协议的监听器不支持此字段

        :return: The member_timeout of this UpdateListenerOption.
        :rtype: int
        """
        return self._member_timeout

    @member_timeout.setter
    def member_timeout(self, member_timeout):
        """Sets the member_timeout of this UpdateListenerOption.

        等待后端服务器请求超时时间，仅限协议为HTTP， TERMINATED_HTTPS的监听器配置。取值范围为1-300s，默认为60s TCP，UDP协议的监听器不支持此字段

        :param member_timeout: The member_timeout of this UpdateListenerOption.
        :type: int
        """
        self._member_timeout = member_timeout

    @property
    def client_timeout(self):
        """Gets the client_timeout of this UpdateListenerOption.

        等待客户端请求超时时间，仅限协议为HTTP， TERMINATED_HTTPS的监听器配置。取值范围为1-60s, 默认值为60s TCP，UDP协议的监听器不支持此字段

        :return: The client_timeout of this UpdateListenerOption.
        :rtype: int
        """
        return self._client_timeout

    @client_timeout.setter
    def client_timeout(self, client_timeout):
        """Sets the client_timeout of this UpdateListenerOption.

        等待客户端请求超时时间，仅限协议为HTTP， TERMINATED_HTTPS的监听器配置。取值范围为1-60s, 默认值为60s TCP，UDP协议的监听器不支持此字段

        :param client_timeout: The client_timeout of this UpdateListenerOption.
        :type: int
        """
        self._client_timeout = client_timeout

    @property
    def keepalive_timeout(self):
        """Gets the keepalive_timeout of this UpdateListenerOption.

        TCP监听器配置空闲超时时间，取值范围为（10-900s）默认值为300s，HTTP/TERMINATED_HTTPS监听器为客户端连接空闲超时时间，取值范围为（1-300s）默认值为15s。 UDP监听器不支持此字段

        :return: The keepalive_timeout of this UpdateListenerOption.
        :rtype: int
        """
        return self._keepalive_timeout

    @keepalive_timeout.setter
    def keepalive_timeout(self, keepalive_timeout):
        """Sets the keepalive_timeout of this UpdateListenerOption.

        TCP监听器配置空闲超时时间，取值范围为（10-900s）默认值为300s，HTTP/TERMINATED_HTTPS监听器为客户端连接空闲超时时间，取值范围为（1-300s）默认值为15s。 UDP监听器不支持此字段

        :param keepalive_timeout: The keepalive_timeout of this UpdateListenerOption.
        :type: int
        """
        self._keepalive_timeout = keepalive_timeout

    @property
    def ipgroup(self):
        """Gets the ipgroup of this UpdateListenerOption.


        :return: The ipgroup of this UpdateListenerOption.
        :rtype: UpdateListenerIpGroupOption
        """
        return self._ipgroup

    @ipgroup.setter
    def ipgroup(self, ipgroup):
        """Sets the ipgroup of this UpdateListenerOption.


        :param ipgroup: The ipgroup of this UpdateListenerOption.
        :type: UpdateListenerIpGroupOption
        """
        self._ipgroup = ipgroup

    @property
    def transparent_client_ip_enable(self):
        """Gets the transparent_client_ip_enable of this UpdateListenerOption.

        获取客户端真实IP 共享型实例的TCP/UDP监听器支持修改，共享型实例的HTTP/TERMINATED_HTTPS监听器和独享型实例的所有类型监听器都不支持修改

        :return: The transparent_client_ip_enable of this UpdateListenerOption.
        :rtype: bool
        """
        return self._transparent_client_ip_enable

    @transparent_client_ip_enable.setter
    def transparent_client_ip_enable(self, transparent_client_ip_enable):
        """Sets the transparent_client_ip_enable of this UpdateListenerOption.

        获取客户端真实IP 共享型实例的TCP/UDP监听器支持修改，共享型实例的HTTP/TERMINATED_HTTPS监听器和独享型实例的所有类型监听器都不支持修改

        :param transparent_client_ip_enable: The transparent_client_ip_enable of this UpdateListenerOption.
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
        if not isinstance(other, UpdateListenerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
