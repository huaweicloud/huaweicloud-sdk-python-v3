# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'security_policy_id': 'str',
        'enable_member_retry': 'bool',
        'member_timeout': 'int',
        'client_timeout': 'int',
        'keepalive_timeout': 'int',
        'ipgroup': 'UpdateListenerIpGroupOption',
        'transparent_client_ip_enable': 'bool',
        'enhance_l7policy_enable': 'bool'
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
        'security_policy_id': 'security_policy_id',
        'enable_member_retry': 'enable_member_retry',
        'member_timeout': 'member_timeout',
        'client_timeout': 'client_timeout',
        'keepalive_timeout': 'keepalive_timeout',
        'ipgroup': 'ipgroup',
        'transparent_client_ip_enable': 'transparent_client_ip_enable',
        'enhance_l7policy_enable': 'enhance_l7policy_enable'
    }

    def __init__(self, admin_state_up=None, client_ca_tls_container_ref=None, default_pool_id=None, default_tls_container_ref=None, description=None, http2_enable=None, insert_headers=None, name=None, sni_container_refs=None, tls_ciphers_policy=None, security_policy_id=None, enable_member_retry=None, member_timeout=None, client_timeout=None, keepalive_timeout=None, ipgroup=None, transparent_client_ip_enable=None, enhance_l7policy_enable=None):
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
        self._security_policy_id = None
        self._enable_member_retry = None
        self._member_timeout = None
        self._client_timeout = None
        self._keepalive_timeout = None
        self._ipgroup = None
        self._transparent_client_ip_enable = None
        self._enhance_l7policy_enable = None
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
        if security_policy_id is not None:
            self.security_policy_id = security_policy_id
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
        if enhance_l7policy_enable is not None:
            self.enhance_l7policy_enable = enhance_l7policy_enable

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateListenerOption.

        监听器的管理状态。只能设置为true。  不支持该字段，请勿使用。

        :return: The admin_state_up of this UpdateListenerOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateListenerOption.

        监听器的管理状态。只能设置为true。  不支持该字段，请勿使用。

        :param admin_state_up: The admin_state_up of this UpdateListenerOption.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def client_ca_tls_container_ref(self):
        """Gets the client_ca_tls_container_ref of this UpdateListenerOption.

        监听器使用的CA证书ID。仅客户端证书有效，其他类型证书无效。

        :return: The client_ca_tls_container_ref of this UpdateListenerOption.
        :rtype: str
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        """Sets the client_ca_tls_container_ref of this UpdateListenerOption.

        监听器使用的CA证书ID。仅客户端证书有效，其他类型证书无效。

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

        监听器使用的服务器证书ID。  使用说明： - 当监听器协议为HTTPS时，该字段必传，且对应的证书的type必须是server类型。

        :return: The default_tls_container_ref of this UpdateListenerOption.
        :rtype: str
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        """Sets the default_tls_container_ref of this UpdateListenerOption.

        监听器使用的服务器证书ID。  使用说明： - 当监听器协议为HTTPS时，该字段必传，且对应的证书的type必须是server类型。

        :param default_tls_container_ref: The default_tls_container_ref of this UpdateListenerOption.
        :type: str
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def description(self):
        """Gets the description of this UpdateListenerOption.

        监听器的描述信息。

        :return: The description of this UpdateListenerOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateListenerOption.

        监听器的描述信息。

        :param description: The description of this UpdateListenerOption.
        :type: str
        """
        self._description = description

    @property
    def http2_enable(self):
        """Gets the http2_enable of this UpdateListenerOption.

        客户端与LB之间的HTTPS请求的HTTP2功能的开启状态。开启后，可提升客户端与LB间的访问性能，但LB与后端服务器间仍采用HTTP1.X协议。 非HTTPS协议的监听器该字段无效，无论取值如何都不影响监听器正常运行。

        :return: The http2_enable of this UpdateListenerOption.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this UpdateListenerOption.

        客户端与LB之间的HTTPS请求的HTTP2功能的开启状态。开启后，可提升客户端与LB间的访问性能，但LB与后端服务器间仍采用HTTP1.X协议。 非HTTPS协议的监听器该字段无效，无论取值如何都不影响监听器正常运行。

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

        监听器的名称。

        :return: The name of this UpdateListenerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateListenerOption.

        监听器的名称。

        :param name: The name of this UpdateListenerOption.
        :type: str
        """
        self._name = name

    @property
    def sni_container_refs(self):
        """Gets the sni_container_refs of this UpdateListenerOption.

        监听器使用的SNI证书（带域名的服务器证书）ID列表。  使用说明： - 列表对应的所有SNI证书的域名不允许存在重复。 - 列表对应的所有SNI证书的域名总数不超过30。

        :return: The sni_container_refs of this UpdateListenerOption.
        :rtype: list[str]
        """
        return self._sni_container_refs

    @sni_container_refs.setter
    def sni_container_refs(self, sni_container_refs):
        """Sets the sni_container_refs of this UpdateListenerOption.

        监听器使用的SNI证书（带域名的服务器证书）ID列表。  使用说明： - 列表对应的所有SNI证书的域名不允许存在重复。 - 列表对应的所有SNI证书的域名总数不超过30。

        :param sni_container_refs: The sni_container_refs of this UpdateListenerOption.
        :type: list[str]
        """
        self._sni_container_refs = sni_container_refs

    @property
    def tls_ciphers_policy(self):
        """Gets the tls_ciphers_policy of this UpdateListenerOption.

        监听器使用的安全策略，仅对HTTPS协议类型的监听器有效。 [取值：tls-1-0-inherit, tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict，tls-1-2-fs, tls-1-0-with-1-3, tls-1-2-fs-with-1-3, hybrid-policy-1-0。](tag:hws,hk,ocb,tlf,ctc,hcso,sbc,g42,tm,cmcc,hk-g42) [取值：tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict。](tag:dt,dt_test) 使用说明： - 若同时设置了security_policy_id和tls_ciphers_policy，则仅security_policy_id生效。

        :return: The tls_ciphers_policy of this UpdateListenerOption.
        :rtype: str
        """
        return self._tls_ciphers_policy

    @tls_ciphers_policy.setter
    def tls_ciphers_policy(self, tls_ciphers_policy):
        """Sets the tls_ciphers_policy of this UpdateListenerOption.

        监听器使用的安全策略，仅对HTTPS协议类型的监听器有效。 [取值：tls-1-0-inherit, tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict，tls-1-2-fs, tls-1-0-with-1-3, tls-1-2-fs-with-1-3, hybrid-policy-1-0。](tag:hws,hk,ocb,tlf,ctc,hcso,sbc,g42,tm,cmcc,hk-g42) [取值：tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict。](tag:dt,dt_test) 使用说明： - 若同时设置了security_policy_id和tls_ciphers_policy，则仅security_policy_id生效。

        :param tls_ciphers_policy: The tls_ciphers_policy of this UpdateListenerOption.
        :type: str
        """
        self._tls_ciphers_policy = tls_ciphers_policy

    @property
    def security_policy_id(self):
        """Gets the security_policy_id of this UpdateListenerOption.

        自定义安全策略的ID。仅关联LB为独享型时有效。 使用说明： - 若同时设置了security_policy_id和tls_ciphers_policy，则仅security_policy_id生效。

        :return: The security_policy_id of this UpdateListenerOption.
        :rtype: str
        """
        return self._security_policy_id

    @security_policy_id.setter
    def security_policy_id(self, security_policy_id):
        """Sets the security_policy_id of this UpdateListenerOption.

        自定义安全策略的ID。仅关联LB为独享型时有效。 使用说明： - 若同时设置了security_policy_id和tls_ciphers_policy，则仅security_policy_id生效。

        :param security_policy_id: The security_policy_id of this UpdateListenerOption.
        :type: str
        """
        self._security_policy_id = security_policy_id

    @property
    def enable_member_retry(self):
        """Gets the enable_member_retry of this UpdateListenerOption.

        是否开启后端服务器的重试。取值：true 开启重试，false 不开启重试。  使用说明： - 若关联是共享型LB，仅在protocol为HTTP、TERMINATED_HTTPS时才能传入该字段。 - 若关联是独享型LB，仅在protocol为HTTP、HTTPS时才能传入该字段。

        :return: The enable_member_retry of this UpdateListenerOption.
        :rtype: bool
        """
        return self._enable_member_retry

    @enable_member_retry.setter
    def enable_member_retry(self, enable_member_retry):
        """Sets the enable_member_retry of this UpdateListenerOption.

        是否开启后端服务器的重试。取值：true 开启重试，false 不开启重试。  使用说明： - 若关联是共享型LB，仅在protocol为HTTP、TERMINATED_HTTPS时才能传入该字段。 - 若关联是独享型LB，仅在protocol为HTTP、HTTPS时才能传入该字段。

        :param enable_member_retry: The enable_member_retry of this UpdateListenerOption.
        :type: bool
        """
        self._enable_member_retry = enable_member_retry

    @property
    def member_timeout(self):
        """Gets the member_timeout of this UpdateListenerOption.

        等待后端服务器响应超时时间。请求转发后端服务器后，在等待超时member_timeout时长没有响应，负载均衡将终止等待，并返回 HTTP504错误码。  取值：1-300s。  使用说明： - 仅支持协议为HTTP/HTTPS的监听器。

        :return: The member_timeout of this UpdateListenerOption.
        :rtype: int
        """
        return self._member_timeout

    @member_timeout.setter
    def member_timeout(self, member_timeout):
        """Sets the member_timeout of this UpdateListenerOption.

        等待后端服务器响应超时时间。请求转发后端服务器后，在等待超时member_timeout时长没有响应，负载均衡将终止等待，并返回 HTTP504错误码。  取值：1-300s。  使用说明： - 仅支持协议为HTTP/HTTPS的监听器。

        :param member_timeout: The member_timeout of this UpdateListenerOption.
        :type: int
        """
        self._member_timeout = member_timeout

    @property
    def client_timeout(self):
        """Gets the client_timeout of this UpdateListenerOption.

        等待客户端请求超时时间，仅限协议为HTTP，HTTPS的监听器配置。取值范围为1-300s, 默认值为60s TCP，UDP协议的监听器不支持此字段

        :return: The client_timeout of this UpdateListenerOption.
        :rtype: int
        """
        return self._client_timeout

    @client_timeout.setter
    def client_timeout(self, client_timeout):
        """Sets the client_timeout of this UpdateListenerOption.

        等待客户端请求超时时间，仅限协议为HTTP，HTTPS的监听器配置。取值范围为1-300s, 默认值为60s TCP，UDP协议的监听器不支持此字段

        :param client_timeout: The client_timeout of this UpdateListenerOption.
        :type: int
        """
        self._client_timeout = client_timeout

    @property
    def keepalive_timeout(self):
        """Gets the keepalive_timeout of this UpdateListenerOption.

        客户端连接空闲超时时间。在超过keepalive_timeout时长一直没有请求，负载均衡会暂时中断当前连接，直到一下次请求时重新建立新的连接。取值： - TCP监听器：10-4000s。 - HTTP/HTTPS/TERMINATED_HTTPS监听器：0-4000s。 - UDP监听器不支持此字段。

        :return: The keepalive_timeout of this UpdateListenerOption.
        :rtype: int
        """
        return self._keepalive_timeout

    @keepalive_timeout.setter
    def keepalive_timeout(self, keepalive_timeout):
        """Sets the keepalive_timeout of this UpdateListenerOption.

        客户端连接空闲超时时间。在超过keepalive_timeout时长一直没有请求，负载均衡会暂时中断当前连接，直到一下次请求时重新建立新的连接。取值： - TCP监听器：10-4000s。 - HTTP/HTTPS/TERMINATED_HTTPS监听器：0-4000s。 - UDP监听器不支持此字段。

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

        是否透传客户端IP地址。开启后客户端IP地址将透传到后端服务器。仅作用于共享型LB的TCP/UDP监听器。取值： - 共享型LB的TCP/UDP监听器可设置为true或false。 - 共享型LB的HTTP/TERMINATED_HTTPS监听器只支持设置为true。 - 独享型负载均衡器所有协议的监听器只支持设置为true。  使用说明： - 开启特性后，ELB和后端服务器之间直接使用真实的IP访问，需要确保已正确设置服务器的安全组以及访问控制策略。 - 开启特性后，不支持同一台服务器既作为后端服务器又作为客户端的场景。 - 开启特性后，不支持变更后端服务器规格。

        :return: The transparent_client_ip_enable of this UpdateListenerOption.
        :rtype: bool
        """
        return self._transparent_client_ip_enable

    @transparent_client_ip_enable.setter
    def transparent_client_ip_enable(self, transparent_client_ip_enable):
        """Sets the transparent_client_ip_enable of this UpdateListenerOption.

        是否透传客户端IP地址。开启后客户端IP地址将透传到后端服务器。仅作用于共享型LB的TCP/UDP监听器。取值： - 共享型LB的TCP/UDP监听器可设置为true或false。 - 共享型LB的HTTP/TERMINATED_HTTPS监听器只支持设置为true。 - 独享型负载均衡器所有协议的监听器只支持设置为true。  使用说明： - 开启特性后，ELB和后端服务器之间直接使用真实的IP访问，需要确保已正确设置服务器的安全组以及访问控制策略。 - 开启特性后，不支持同一台服务器既作为后端服务器又作为客户端的场景。 - 开启特性后，不支持变更后端服务器规格。

        :param transparent_client_ip_enable: The transparent_client_ip_enable of this UpdateListenerOption.
        :type: bool
        """
        self._transparent_client_ip_enable = transparent_client_ip_enable

    @property
    def enhance_l7policy_enable(self):
        """Gets the enhance_l7policy_enable of this UpdateListenerOption.

        是否开启高级转发策略功能。开启高级转发策略后，支持更灵活的转发策略和转发规则设置。取值：true开启，false不开启。 开启后支持如下场景：  - 转发策略的action字段支持指定为REDIRECT_TO_URL, FIXED_RESPONSE，即支持URL重定向和响应固定的内容给客户端。  - 转发策略支持指定priority、redirect_url_config、fixed_response_config字段。  - 转发规则rule的type可以指定METHOD, HEADER, QUERY_STRING, SOURCE_IP这几种取值。  - 转发规则rule的type为HOST_NAME时，转发规则rule的value支持通配符*。  - 转发规则支持指定conditions字段。

        :return: The enhance_l7policy_enable of this UpdateListenerOption.
        :rtype: bool
        """
        return self._enhance_l7policy_enable

    @enhance_l7policy_enable.setter
    def enhance_l7policy_enable(self, enhance_l7policy_enable):
        """Sets the enhance_l7policy_enable of this UpdateListenerOption.

        是否开启高级转发策略功能。开启高级转发策略后，支持更灵活的转发策略和转发规则设置。取值：true开启，false不开启。 开启后支持如下场景：  - 转发策略的action字段支持指定为REDIRECT_TO_URL, FIXED_RESPONSE，即支持URL重定向和响应固定的内容给客户端。  - 转发策略支持指定priority、redirect_url_config、fixed_response_config字段。  - 转发规则rule的type可以指定METHOD, HEADER, QUERY_STRING, SOURCE_IP这几种取值。  - 转发规则rule的type为HOST_NAME时，转发规则rule的value支持通配符*。  - 转发规则支持指定conditions字段。

        :param enhance_l7policy_enable: The enhance_l7policy_enable of this UpdateListenerOption.
        :type: bool
        """
        self._enhance_l7policy_enable = enhance_l7policy_enable

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
        if not isinstance(other, UpdateListenerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
