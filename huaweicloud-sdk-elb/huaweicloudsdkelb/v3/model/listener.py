# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'enterprise_project_id': 'str',
        'protocol': 'str',
        'protocol_port': 'int',
        'sni_container_refs': 'list[str]',
        'sni_match_algo': 'str',
        'tags': 'list[Tag]',
        'updated_at': 'str',
        'tls_ciphers_policy': 'str',
        'security_policy_id': 'str',
        'enable_member_retry': 'bool',
        'keepalive_timeout': 'int',
        'client_timeout': 'int',
        'member_timeout': 'int',
        'ipgroup': 'ListenerIpGroup',
        'transparent_client_ip_enable': 'bool',
        'proxy_protocol_enable': 'bool',
        'enhance_l7policy_enable': 'bool',
        'quic_config': 'ListenerQuicConfig',
        'protection_status': 'str',
        'protection_reason': 'str',
        'gzip_enable': 'bool',
        'port_ranges': 'list[PortRange]',
        'ssl_early_data_enable': 'bool',
        'cps': 'int',
        'connection': 'int',
        'nat64_enable': 'bool'
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
        'enterprise_project_id': 'enterprise_project_id',
        'protocol': 'protocol',
        'protocol_port': 'protocol_port',
        'sni_container_refs': 'sni_container_refs',
        'sni_match_algo': 'sni_match_algo',
        'tags': 'tags',
        'updated_at': 'updated_at',
        'tls_ciphers_policy': 'tls_ciphers_policy',
        'security_policy_id': 'security_policy_id',
        'enable_member_retry': 'enable_member_retry',
        'keepalive_timeout': 'keepalive_timeout',
        'client_timeout': 'client_timeout',
        'member_timeout': 'member_timeout',
        'ipgroup': 'ipgroup',
        'transparent_client_ip_enable': 'transparent_client_ip_enable',
        'proxy_protocol_enable': 'proxy_protocol_enable',
        'enhance_l7policy_enable': 'enhance_l7policy_enable',
        'quic_config': 'quic_config',
        'protection_status': 'protection_status',
        'protection_reason': 'protection_reason',
        'gzip_enable': 'gzip_enable',
        'port_ranges': 'port_ranges',
        'ssl_early_data_enable': 'ssl_early_data_enable',
        'cps': 'cps',
        'connection': 'connection',
        'nat64_enable': 'nat64_enable'
    }

    def __init__(self, admin_state_up=None, client_ca_tls_container_ref=None, connection_limit=None, created_at=None, default_pool_id=None, default_tls_container_ref=None, description=None, http2_enable=None, id=None, insert_headers=None, loadbalancers=None, name=None, project_id=None, enterprise_project_id=None, protocol=None, protocol_port=None, sni_container_refs=None, sni_match_algo=None, tags=None, updated_at=None, tls_ciphers_policy=None, security_policy_id=None, enable_member_retry=None, keepalive_timeout=None, client_timeout=None, member_timeout=None, ipgroup=None, transparent_client_ip_enable=None, proxy_protocol_enable=None, enhance_l7policy_enable=None, quic_config=None, protection_status=None, protection_reason=None, gzip_enable=None, port_ranges=None, ssl_early_data_enable=None, cps=None, connection=None, nat64_enable=None):
        r"""Listener

        The model defined in huaweicloud sdk

        :param admin_state_up: 参数解释：监听器的管理状态。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type admin_state_up: bool
        :param client_ca_tls_container_ref: 参数解释：监听器使用的CA证书ID。  约束限制：当且仅当type&#x3D;client时，才会使用该字段对应的证书。
        :type client_ca_tls_container_ref: str
        :param connection_limit: 参数解释：监听器的最大连接数。  取值范围：-1表示不限制。  默认取值：-1。  不支持该字段，请勿使用。
        :type connection_limit: int
        :param created_at: 参数解释：监听器的创建时间。  取值范围：  格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如：2021-07-30T12:03:44Z
        :type created_at: str
        :param default_pool_id: 参数解释：监听器的默认后端服务器组ID。当请求没有匹配的转发策略时，转发到默认后端服务器上处理。
        :type default_pool_id: str
        :param default_tls_container_ref: 参数解释：监听器使用的服务器证书ID。
        :type default_tls_container_ref: str
        :param description: 参数解释：监听器的描述信息。
        :type description: str
        :param http2_enable: 参数解释：客户端与LB之间的HTTPS请求的HTTP2功能的开启状态。 开启后，可提升客户端与LB间的访问性能，但LB与后端服务器间仍采用HTTP1.X协议。  约束限制： - 仅HTTPS协议监听器有效。 - QUIC监听器不能设置该字段，固定返回为true。 - 其他协议的监听器可设置该字段但无效，无论取值如何都不影响监听器正常运行。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt)
        :type http2_enable: bool
        :param id: 参数解释：监听器ID。
        :type id: str
        :param insert_headers: 
        :type insert_headers: :class:`huaweicloudsdkelb.v3.ListenerInsertHeaders`
        :param loadbalancers: 参数解释：监听器所属的负载均衡器的ID列表。  约束限制：一个监听器只支持关联到一个LB。
        :type loadbalancers: list[:class:`huaweicloudsdkelb.v3.LoadBalancerRef`]
        :param name: 参数解释：监听器的名称。  约束限制：若名称为空，则在控制台的监听器列表无法选择并查看监听器详情。
        :type name: str
        :param project_id: 参数解释：监听器所在的项目ID。
        :type project_id: str
        :param enterprise_project_id: 参数解释：企业项目ID。
        :type enterprise_project_id: str
        :param protocol: 参数解释：监听器的监听协议。  [取值范围：TCP、UDP、HTTP、HTTPS、TERMINATED_HTTPS、QUIC、TLS。  约束限制： - 共享型LB上的HTTPS监听器只支持设置为TERMINATED_HTTPS， 创建时传入HTTPS将会自动转为TERMINATED_HTTPS。 - 独享型LB上的HTTPS监听器只支持设置为HTTPS，创建时传入TERMINATED_HTTPS将会自动转为HTTPS。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt)  [取值：TCP、UDP、HTTP、HTTPS。](tag:hcso_dt) [取值：TCP、UDP、IP、HTTP、HTTPS。IP为网关型LB上的监听器独有的协议。](tag:hws_eu)  [不支持QUIC。](tag:tm,g42,hk_g42,dt)
        :type protocol: str
        :param protocol_port: 参数解释：监听器的监听端口。  约束限制： - QUIC监听器端口不能是4789，且不能和UDP监听器端口重复。 - 传0表示开启监听端口范围的能力，此时port_ranges为必填字段。 [-不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt)
        :type protocol_port: int
        :param sni_container_refs: 参数解释：监听器使用的SNI证书（带域名的服务器证书）ID列表。  约束限制： - QUIC监听器仅支持RSA证书。 - 列表对应的所有SNI证书的域名不允许存在重复。 - 列表对应的所有SNI证书的域名总数不超过200。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt)
        :type sni_container_refs: list[str]
        :param sni_match_algo: 参数解释：监听器使用的SNI证书泛域名匹配方式。  取值范围：longest_suffix表示最长尾缀匹配；wildcard表示标准域名分级匹配。  默认取值：wildcard
        :type sni_match_algo: str
        :param tags: 参数解释：标签列表。
        :type tags: list[:class:`huaweicloudsdkelb.v3.Tag`]
        :param updated_at: 参数解释：监听器的更新时间。  取值范围：  格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如：2021-07-30T12:03:44Z
        :type updated_at: str
        :param tls_ciphers_policy: 参数解释：监听器使用的安全策略。  [取值范围：tls-1-0-inherit、tls-1-0、tls-1-1、 tls-1-2、tls-1-2-strict、tls-1-2-fs、tls-1-0-with-1-3、 tls-1-2-fs-with-1-3、 hybrid-policy-1-0、tls-1-2-strict-no-cbc，默认：tls-1-2。 ](tag:hws,hws_hk,ocb,tlf,ctc,hcso,ct,sbc,tm,cmcc,dt)  [取值范围：tls-1-0、tls-1-1、tls-1-2、 tls-1-2-strict，默认：tls-1-2。](tag:hws_eu,g42,hk_g42,hcso_dt)  [约束限制： - 仅对HTTPS协议类型的监听器且关联LB为独享型时有效。 - QUIC监听器不支持该字段。 - 若同时设置了security_policy_id和tls_ciphers_policy，则仅security_policy_id生效。 - 加密套件的优先顺序为ecc套件、rsa套件、tls1.3协议的套件（即支持ecc又支持rsa） ](tag:hws,hws_hk,hws_eu,ocb,tlf,ctc,hcso,ct,sbc,g42,tm,cmcc,hk_g42,dt)  [约束限制： - 仅对HTTPS协议类型的监听器有效](tag:hcso_dt)  [不支持tls1.3协议的套件。](tag:tm,hws_eu,g42,hk_g42)
        :type tls_ciphers_policy: str
        :param security_policy_id: 参数解释：自定义安全策略的ID。  [约束限制： - 仅对HTTPS协议类型的监听器且关联LB为独享型时有效。 - 若同时设置了security_policy_id和tls_ciphers_policy，则仅security_policy_id生效。 - 加密套件的优先顺序为ecc套件、rsa套件、tls1.3协议的套件（即支持ecc又支持rsa） ](tag:hws,hws_hk,hws_eu,ocb,ctc,hcso,g42,tm,cmcc,hk_g42,dt)  [约束限制： - 仅对HTTPS协议类型的监听器有效](tag:hcso_dt)  [不支持tls1.3协议的套件。](tag:tm,hws_eu,g42,hk_g42)
        :type security_policy_id: str
        :param enable_member_retry: 参数解释：是否开启后端服务器的重试。  [约束限制： - 若关联是共享型LB，仅在protocol为HTTP、TERMINATED_HTTPS时才能传入该字段。 - 若关联是独享型LB，仅在protocol为HTTP、HTTPS和QUIC时才能传入该字段。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt)  [约束限制： - 仅在protocol为HTTP、HTTPS时才能传入该字段。](tag:hws_eu,hcso_dt)  取值范围：true 开启重试，false 不开启重试。  默认取值：true。  [不支持QUIC。](tag:tm,dt)
        :type enable_member_retry: bool
        :param keepalive_timeout: 参数解释：客户端连接空闲超时时间。在超过keepalive_timeout时长一直没有请求，负载均衡会暂时中断当前连接，直到下一次请求时重新建立新的连接。  约束限制：共享型实例的UDP监听器不支持此字段。  取值范围： - TCP监听器[和IP监听器](tag:hws_eu)：10-4000s，默认值为300s。 - 若为HTTP/HTTPS/TERMINATED_HTTPS监听器，取值范围为（0-4000s）默认值为60s。
        :type keepalive_timeout: int
        :param client_timeout: 参数解释：等待客户端请求超时时间，包括两种情况： - 读取整个客户端请求头的超时时长：如果客户端未在超时时长内发送完整个请求头，则请求将被中断 - 两个连续body体的数据包到达LB的时间间隔，超出client_timeout将会断开连接。  约束限制：仅协议为HTTP/HTTPS的监听器支持该字段。  取值范围：1-300s  默认取值：60s。
        :type client_timeout: int
        :param member_timeout: 参数解释：等待后端服务器响应超时时间。请求转发后端服务器后，在等待超时member_timeout时长没有响应，负载均衡将终止等待，并返回HTTP504错误码。  约束限制：仅支持协议为HTTP/HTTPS的监听器。  取值范围：1-300s  默认取值：60s。
        :type member_timeout: int
        :param ipgroup: 
        :type ipgroup: :class:`huaweicloudsdkelb.v3.ListenerIpGroup`
        :param transparent_client_ip_enable: 参数解释：是否透传客户端IP地址。开启后客户端IP地址将透传到后端服务器。 [仅作用于共享型LB的TCP/UDP监听器。  约束限制： - 开启特性后，ELB和后端服务器之间直接使用真实的IP访问，需要确保已正确设置服务器的安全组以及访问控制策略。 - 开启特性后，不支持同一台服务器既作为后端服务器又作为客户端的场景。 - 开启特性后，不支持变更后端服务器规格。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt)   取值范围： - 共享型LB的TCP/UDP监听器可设置为true或false，不传默认为false。 - 共享型LB的HTTP/HTTPS监听器只支持设置为true，不传默认为true。 - 独享型负载均衡器所有协议的监听器只支持设置为true，不传默认为true。  [只设支持置为true，不传默认为true。](tag:hws_eu,hcso_dt)
        :type transparent_client_ip_enable: bool
        :param proxy_protocol_enable: 参数解释：是否开启proxy_protocol。仅TLS监听器可指定，其他协议的监听器该字段不生效，proxy_protocol不开启。
        :type proxy_protocol_enable: bool
        :param enhance_l7policy_enable: 参数解释：是否开启高级转发策略功能。开启高级转发策略后，支持更灵活的转发策略和转发规则设置。  开启后支持如下场景： - 转发策略的action字段支持指定为REDIRECT_TO_URL, FIXED_RESPONSE，即支持URL重定向和响应固定的内容给客户端。 - 转发策略支持指定priority、redirect_url_config、fixed_response_config字段。 - 转发规则rule的type可以指定METHOD, HEADER, QUERY_STRING, SOURCE_IP这几种取值。 - 转发规则rule的type为HOST_NAME时，转发规则rule的value支持通配符*。 - 转发规则支持指定conditions字段。  约束限制： - 开启后不支持关闭。 - 开启高级转发策略后，监听器关联的转发策略的匹配优先级由转发策略的priority字段来决定，不再自动排序。具体说明详见转发策略的priority字段的说明。  取值范围：true开启，false不开启。  默认取值：false。[西南-贵阳一和华南-广州局点，该配置默认true。](tag:hws)  [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type enhance_l7policy_enable: bool
        :param quic_config: 
        :type quic_config: :class:`huaweicloudsdkelb.v3.ListenerQuicConfig`
        :param protection_status: 参数解释：修改保护状态,   取值范围： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护
        :type protection_status: str
        :param protection_reason: 参数解释：设置保护的原因。作为protection_status的转态设置的原因。  约束限制：仅当protection_status为consoleProtection时有效。  取值范围：除&#39;&lt;&#39;和&#39;&gt;&#39;外通用Unicode字符集字符，最大255个字符。
        :type protection_reason: str
        :param gzip_enable: 参数解释：ELB是否开启gzip压缩。  [约束限制：仅HTTP/HTTPS类型监听器支持配置。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt) [约束限制：仅HTTP/HTTPS/QUIC类型监听器支持配置。](tag:hws,hws_hk,hws_test,hcs,hcs_sm,hcso,hk_vdf,srg,fcs,fcs_vm,mix,ocb,ctc,cmcc,ct,sbc,hws_ocb,hk_sbc)  默认取值：false  [不支持该字段，请勿使用。](tag:hws_eu,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)
        :type gzip_enable: bool
        :param port_ranges: 参数解释：端口监听范围（闭区间)。  约束限制： - 最多指定10个端口组，每个组范围不可有重叠部分 - 仅当protocol_port为0时可以传入。  [不支持该字段，请勿使用。](tag:hws_eu,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)
        :type port_ranges: list[:class:`huaweicloudsdkelb.v3.PortRange`]
        :param ssl_early_data_enable: 参数解释：监听器0-RTT能力开关  约束限制：仅HTTPS类型监听器支持配置，需要依赖TLSv1.3安全策略协议。  默认取值：false。
        :type ssl_early_data_enable: bool
        :param cps: 参数解释：监听器新建限速  约束限制：当该限速值大于LB的限速值时，以LB的限速值生效  取值范围：0-1000000  默认取值：0，表示不限速
        :type cps: int
        :param connection: 参数解释：监听器并发限速  约束限制：当该限速值大于LB的限速值时，以LB的限速值生效  取值范围：0-1000000  默认取值：0，表示不限速
        :type connection: int
        :param nat64_enable: 参数解释： 监听器地址族转换能力开关，可以实现客户端通过访问LB的IPv4或者IPv6地址，来访问IPv4后端和IPv6后端。  约束限制： 仅对于TCP、UDP协议类型的监听器生效，与transparent_client_ip_enable，获取客户端ip功能开关互斥，开启地址族转换同时需要保证获取客户端ip功能关闭。  取值范围： - true：开启地址族转换功能 - false：关闭地址族转换功能  默认取值：false
        :type nat64_enable: bool
        """
        
        

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
        self._enterprise_project_id = None
        self._protocol = None
        self._protocol_port = None
        self._sni_container_refs = None
        self._sni_match_algo = None
        self._tags = None
        self._updated_at = None
        self._tls_ciphers_policy = None
        self._security_policy_id = None
        self._enable_member_retry = None
        self._keepalive_timeout = None
        self._client_timeout = None
        self._member_timeout = None
        self._ipgroup = None
        self._transparent_client_ip_enable = None
        self._proxy_protocol_enable = None
        self._enhance_l7policy_enable = None
        self._quic_config = None
        self._protection_status = None
        self._protection_reason = None
        self._gzip_enable = None
        self._port_ranges = None
        self._ssl_early_data_enable = None
        self._cps = None
        self._connection = None
        self._nat64_enable = None
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
        self.enterprise_project_id = enterprise_project_id
        self.protocol = protocol
        self.protocol_port = protocol_port
        self.sni_container_refs = sni_container_refs
        self.sni_match_algo = sni_match_algo
        self.tags = tags
        self.updated_at = updated_at
        self.tls_ciphers_policy = tls_ciphers_policy
        self.security_policy_id = security_policy_id
        self.enable_member_retry = enable_member_retry
        self.keepalive_timeout = keepalive_timeout
        self.client_timeout = client_timeout
        self.member_timeout = member_timeout
        self.ipgroup = ipgroup
        self.transparent_client_ip_enable = transparent_client_ip_enable
        if proxy_protocol_enable is not None:
            self.proxy_protocol_enable = proxy_protocol_enable
        self.enhance_l7policy_enable = enhance_l7policy_enable
        if quic_config is not None:
            self.quic_config = quic_config
        if protection_status is not None:
            self.protection_status = protection_status
        if protection_reason is not None:
            self.protection_reason = protection_reason
        if gzip_enable is not None:
            self.gzip_enable = gzip_enable
        if port_ranges is not None:
            self.port_ranges = port_ranges
        if ssl_early_data_enable is not None:
            self.ssl_early_data_enable = ssl_early_data_enable
        if cps is not None:
            self.cps = cps
        if connection is not None:
            self.connection = connection
        if nat64_enable is not None:
            self.nat64_enable = nat64_enable

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this Listener.

        参数解释：监听器的管理状态。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The admin_state_up of this Listener.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this Listener.

        参数解释：监听器的管理状态。  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param admin_state_up: The admin_state_up of this Listener.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def client_ca_tls_container_ref(self):
        r"""Gets the client_ca_tls_container_ref of this Listener.

        参数解释：监听器使用的CA证书ID。  约束限制：当且仅当type=client时，才会使用该字段对应的证书。

        :return: The client_ca_tls_container_ref of this Listener.
        :rtype: str
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        r"""Sets the client_ca_tls_container_ref of this Listener.

        参数解释：监听器使用的CA证书ID。  约束限制：当且仅当type=client时，才会使用该字段对应的证书。

        :param client_ca_tls_container_ref: The client_ca_tls_container_ref of this Listener.
        :type client_ca_tls_container_ref: str
        """
        self._client_ca_tls_container_ref = client_ca_tls_container_ref

    @property
    def connection_limit(self):
        r"""Gets the connection_limit of this Listener.

        参数解释：监听器的最大连接数。  取值范围：-1表示不限制。  默认取值：-1。  不支持该字段，请勿使用。

        :return: The connection_limit of this Listener.
        :rtype: int
        """
        return self._connection_limit

    @connection_limit.setter
    def connection_limit(self, connection_limit):
        r"""Sets the connection_limit of this Listener.

        参数解释：监听器的最大连接数。  取值范围：-1表示不限制。  默认取值：-1。  不支持该字段，请勿使用。

        :param connection_limit: The connection_limit of this Listener.
        :type connection_limit: int
        """
        self._connection_limit = connection_limit

    @property
    def created_at(self):
        r"""Gets the created_at of this Listener.

        参数解释：监听器的创建时间。  取值范围：  格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如：2021-07-30T12:03:44Z

        :return: The created_at of this Listener.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Listener.

        参数解释：监听器的创建时间。  取值范围：  格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如：2021-07-30T12:03:44Z

        :param created_at: The created_at of this Listener.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def default_pool_id(self):
        r"""Gets the default_pool_id of this Listener.

        参数解释：监听器的默认后端服务器组ID。当请求没有匹配的转发策略时，转发到默认后端服务器上处理。

        :return: The default_pool_id of this Listener.
        :rtype: str
        """
        return self._default_pool_id

    @default_pool_id.setter
    def default_pool_id(self, default_pool_id):
        r"""Sets the default_pool_id of this Listener.

        参数解释：监听器的默认后端服务器组ID。当请求没有匹配的转发策略时，转发到默认后端服务器上处理。

        :param default_pool_id: The default_pool_id of this Listener.
        :type default_pool_id: str
        """
        self._default_pool_id = default_pool_id

    @property
    def default_tls_container_ref(self):
        r"""Gets the default_tls_container_ref of this Listener.

        参数解释：监听器使用的服务器证书ID。

        :return: The default_tls_container_ref of this Listener.
        :rtype: str
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        r"""Sets the default_tls_container_ref of this Listener.

        参数解释：监听器使用的服务器证书ID。

        :param default_tls_container_ref: The default_tls_container_ref of this Listener.
        :type default_tls_container_ref: str
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def description(self):
        r"""Gets the description of this Listener.

        参数解释：监听器的描述信息。

        :return: The description of this Listener.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Listener.

        参数解释：监听器的描述信息。

        :param description: The description of this Listener.
        :type description: str
        """
        self._description = description

    @property
    def http2_enable(self):
        r"""Gets the http2_enable of this Listener.

        参数解释：客户端与LB之间的HTTPS请求的HTTP2功能的开启状态。 开启后，可提升客户端与LB间的访问性能，但LB与后端服务器间仍采用HTTP1.X协议。  约束限制： - 仅HTTPS协议监听器有效。 - QUIC监听器不能设置该字段，固定返回为true。 - 其他协议的监听器可设置该字段但无效，无论取值如何都不影响监听器正常运行。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt)

        :return: The http2_enable of this Listener.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        r"""Sets the http2_enable of this Listener.

        参数解释：客户端与LB之间的HTTPS请求的HTTP2功能的开启状态。 开启后，可提升客户端与LB间的访问性能，但LB与后端服务器间仍采用HTTP1.X协议。  约束限制： - 仅HTTPS协议监听器有效。 - QUIC监听器不能设置该字段，固定返回为true。 - 其他协议的监听器可设置该字段但无效，无论取值如何都不影响监听器正常运行。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt)

        :param http2_enable: The http2_enable of this Listener.
        :type http2_enable: bool
        """
        self._http2_enable = http2_enable

    @property
    def id(self):
        r"""Gets the id of this Listener.

        参数解释：监听器ID。

        :return: The id of this Listener.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Listener.

        参数解释：监听器ID。

        :param id: The id of this Listener.
        :type id: str
        """
        self._id = id

    @property
    def insert_headers(self):
        r"""Gets the insert_headers of this Listener.

        :return: The insert_headers of this Listener.
        :rtype: :class:`huaweicloudsdkelb.v3.ListenerInsertHeaders`
        """
        return self._insert_headers

    @insert_headers.setter
    def insert_headers(self, insert_headers):
        r"""Sets the insert_headers of this Listener.

        :param insert_headers: The insert_headers of this Listener.
        :type insert_headers: :class:`huaweicloudsdkelb.v3.ListenerInsertHeaders`
        """
        self._insert_headers = insert_headers

    @property
    def loadbalancers(self):
        r"""Gets the loadbalancers of this Listener.

        参数解释：监听器所属的负载均衡器的ID列表。  约束限制：一个监听器只支持关联到一个LB。

        :return: The loadbalancers of this Listener.
        :rtype: list[:class:`huaweicloudsdkelb.v3.LoadBalancerRef`]
        """
        return self._loadbalancers

    @loadbalancers.setter
    def loadbalancers(self, loadbalancers):
        r"""Sets the loadbalancers of this Listener.

        参数解释：监听器所属的负载均衡器的ID列表。  约束限制：一个监听器只支持关联到一个LB。

        :param loadbalancers: The loadbalancers of this Listener.
        :type loadbalancers: list[:class:`huaweicloudsdkelb.v3.LoadBalancerRef`]
        """
        self._loadbalancers = loadbalancers

    @property
    def name(self):
        r"""Gets the name of this Listener.

        参数解释：监听器的名称。  约束限制：若名称为空，则在控制台的监听器列表无法选择并查看监听器详情。

        :return: The name of this Listener.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Listener.

        参数解释：监听器的名称。  约束限制：若名称为空，则在控制台的监听器列表无法选择并查看监听器详情。

        :param name: The name of this Listener.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this Listener.

        参数解释：监听器所在的项目ID。

        :return: The project_id of this Listener.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Listener.

        参数解释：监听器所在的项目ID。

        :param project_id: The project_id of this Listener.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this Listener.

        参数解释：企业项目ID。

        :return: The enterprise_project_id of this Listener.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this Listener.

        参数解释：企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this Listener.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def protocol(self):
        r"""Gets the protocol of this Listener.

        参数解释：监听器的监听协议。  [取值范围：TCP、UDP、HTTP、HTTPS、TERMINATED_HTTPS、QUIC、TLS。  约束限制： - 共享型LB上的HTTPS监听器只支持设置为TERMINATED_HTTPS， 创建时传入HTTPS将会自动转为TERMINATED_HTTPS。 - 独享型LB上的HTTPS监听器只支持设置为HTTPS，创建时传入TERMINATED_HTTPS将会自动转为HTTPS。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt)  [取值：TCP、UDP、HTTP、HTTPS。](tag:hcso_dt) [取值：TCP、UDP、IP、HTTP、HTTPS。IP为网关型LB上的监听器独有的协议。](tag:hws_eu)  [不支持QUIC。](tag:tm,g42,hk_g42,dt)

        :return: The protocol of this Listener.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this Listener.

        参数解释：监听器的监听协议。  [取值范围：TCP、UDP、HTTP、HTTPS、TERMINATED_HTTPS、QUIC、TLS。  约束限制： - 共享型LB上的HTTPS监听器只支持设置为TERMINATED_HTTPS， 创建时传入HTTPS将会自动转为TERMINATED_HTTPS。 - 独享型LB上的HTTPS监听器只支持设置为HTTPS，创建时传入TERMINATED_HTTPS将会自动转为HTTPS。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt)  [取值：TCP、UDP、HTTP、HTTPS。](tag:hcso_dt) [取值：TCP、UDP、IP、HTTP、HTTPS。IP为网关型LB上的监听器独有的协议。](tag:hws_eu)  [不支持QUIC。](tag:tm,g42,hk_g42,dt)

        :param protocol: The protocol of this Listener.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this Listener.

        参数解释：监听器的监听端口。  约束限制： - QUIC监听器端口不能是4789，且不能和UDP监听器端口重复。 - 传0表示开启监听端口范围的能力，此时port_ranges为必填字段。 [-不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt)

        :return: The protocol_port of this Listener.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this Listener.

        参数解释：监听器的监听端口。  约束限制： - QUIC监听器端口不能是4789，且不能和UDP监听器端口重复。 - 传0表示开启监听端口范围的能力，此时port_ranges为必填字段。 [-不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt)

        :param protocol_port: The protocol_port of this Listener.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def sni_container_refs(self):
        r"""Gets the sni_container_refs of this Listener.

        参数解释：监听器使用的SNI证书（带域名的服务器证书）ID列表。  约束限制： - QUIC监听器仅支持RSA证书。 - 列表对应的所有SNI证书的域名不允许存在重复。 - 列表对应的所有SNI证书的域名总数不超过200。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt)

        :return: The sni_container_refs of this Listener.
        :rtype: list[str]
        """
        return self._sni_container_refs

    @sni_container_refs.setter
    def sni_container_refs(self, sni_container_refs):
        r"""Sets the sni_container_refs of this Listener.

        参数解释：监听器使用的SNI证书（带域名的服务器证书）ID列表。  约束限制： - QUIC监听器仅支持RSA证书。 - 列表对应的所有SNI证书的域名不允许存在重复。 - 列表对应的所有SNI证书的域名总数不超过200。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt)

        :param sni_container_refs: The sni_container_refs of this Listener.
        :type sni_container_refs: list[str]
        """
        self._sni_container_refs = sni_container_refs

    @property
    def sni_match_algo(self):
        r"""Gets the sni_match_algo of this Listener.

        参数解释：监听器使用的SNI证书泛域名匹配方式。  取值范围：longest_suffix表示最长尾缀匹配；wildcard表示标准域名分级匹配。  默认取值：wildcard

        :return: The sni_match_algo of this Listener.
        :rtype: str
        """
        return self._sni_match_algo

    @sni_match_algo.setter
    def sni_match_algo(self, sni_match_algo):
        r"""Sets the sni_match_algo of this Listener.

        参数解释：监听器使用的SNI证书泛域名匹配方式。  取值范围：longest_suffix表示最长尾缀匹配；wildcard表示标准域名分级匹配。  默认取值：wildcard

        :param sni_match_algo: The sni_match_algo of this Listener.
        :type sni_match_algo: str
        """
        self._sni_match_algo = sni_match_algo

    @property
    def tags(self):
        r"""Gets the tags of this Listener.

        参数解释：标签列表。

        :return: The tags of this Listener.
        :rtype: list[:class:`huaweicloudsdkelb.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this Listener.

        参数解释：标签列表。

        :param tags: The tags of this Listener.
        :type tags: list[:class:`huaweicloudsdkelb.v3.Tag`]
        """
        self._tags = tags

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Listener.

        参数解释：监听器的更新时间。  取值范围：  格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如：2021-07-30T12:03:44Z

        :return: The updated_at of this Listener.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Listener.

        参数解释：监听器的更新时间。  取值范围：  格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如：2021-07-30T12:03:44Z

        :param updated_at: The updated_at of this Listener.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def tls_ciphers_policy(self):
        r"""Gets the tls_ciphers_policy of this Listener.

        参数解释：监听器使用的安全策略。  [取值范围：tls-1-0-inherit、tls-1-0、tls-1-1、 tls-1-2、tls-1-2-strict、tls-1-2-fs、tls-1-0-with-1-3、 tls-1-2-fs-with-1-3、 hybrid-policy-1-0、tls-1-2-strict-no-cbc，默认：tls-1-2。 ](tag:hws,hws_hk,ocb,tlf,ctc,hcso,ct,sbc,tm,cmcc,dt)  [取值范围：tls-1-0、tls-1-1、tls-1-2、 tls-1-2-strict，默认：tls-1-2。](tag:hws_eu,g42,hk_g42,hcso_dt)  [约束限制： - 仅对HTTPS协议类型的监听器且关联LB为独享型时有效。 - QUIC监听器不支持该字段。 - 若同时设置了security_policy_id和tls_ciphers_policy，则仅security_policy_id生效。 - 加密套件的优先顺序为ecc套件、rsa套件、tls1.3协议的套件（即支持ecc又支持rsa） ](tag:hws,hws_hk,hws_eu,ocb,tlf,ctc,hcso,ct,sbc,g42,tm,cmcc,hk_g42,dt)  [约束限制： - 仅对HTTPS协议类型的监听器有效](tag:hcso_dt)  [不支持tls1.3协议的套件。](tag:tm,hws_eu,g42,hk_g42)

        :return: The tls_ciphers_policy of this Listener.
        :rtype: str
        """
        return self._tls_ciphers_policy

    @tls_ciphers_policy.setter
    def tls_ciphers_policy(self, tls_ciphers_policy):
        r"""Sets the tls_ciphers_policy of this Listener.

        参数解释：监听器使用的安全策略。  [取值范围：tls-1-0-inherit、tls-1-0、tls-1-1、 tls-1-2、tls-1-2-strict、tls-1-2-fs、tls-1-0-with-1-3、 tls-1-2-fs-with-1-3、 hybrid-policy-1-0、tls-1-2-strict-no-cbc，默认：tls-1-2。 ](tag:hws,hws_hk,ocb,tlf,ctc,hcso,ct,sbc,tm,cmcc,dt)  [取值范围：tls-1-0、tls-1-1、tls-1-2、 tls-1-2-strict，默认：tls-1-2。](tag:hws_eu,g42,hk_g42,hcso_dt)  [约束限制： - 仅对HTTPS协议类型的监听器且关联LB为独享型时有效。 - QUIC监听器不支持该字段。 - 若同时设置了security_policy_id和tls_ciphers_policy，则仅security_policy_id生效。 - 加密套件的优先顺序为ecc套件、rsa套件、tls1.3协议的套件（即支持ecc又支持rsa） ](tag:hws,hws_hk,hws_eu,ocb,tlf,ctc,hcso,ct,sbc,g42,tm,cmcc,hk_g42,dt)  [约束限制： - 仅对HTTPS协议类型的监听器有效](tag:hcso_dt)  [不支持tls1.3协议的套件。](tag:tm,hws_eu,g42,hk_g42)

        :param tls_ciphers_policy: The tls_ciphers_policy of this Listener.
        :type tls_ciphers_policy: str
        """
        self._tls_ciphers_policy = tls_ciphers_policy

    @property
    def security_policy_id(self):
        r"""Gets the security_policy_id of this Listener.

        参数解释：自定义安全策略的ID。  [约束限制： - 仅对HTTPS协议类型的监听器且关联LB为独享型时有效。 - 若同时设置了security_policy_id和tls_ciphers_policy，则仅security_policy_id生效。 - 加密套件的优先顺序为ecc套件、rsa套件、tls1.3协议的套件（即支持ecc又支持rsa） ](tag:hws,hws_hk,hws_eu,ocb,ctc,hcso,g42,tm,cmcc,hk_g42,dt)  [约束限制： - 仅对HTTPS协议类型的监听器有效](tag:hcso_dt)  [不支持tls1.3协议的套件。](tag:tm,hws_eu,g42,hk_g42)

        :return: The security_policy_id of this Listener.
        :rtype: str
        """
        return self._security_policy_id

    @security_policy_id.setter
    def security_policy_id(self, security_policy_id):
        r"""Sets the security_policy_id of this Listener.

        参数解释：自定义安全策略的ID。  [约束限制： - 仅对HTTPS协议类型的监听器且关联LB为独享型时有效。 - 若同时设置了security_policy_id和tls_ciphers_policy，则仅security_policy_id生效。 - 加密套件的优先顺序为ecc套件、rsa套件、tls1.3协议的套件（即支持ecc又支持rsa） ](tag:hws,hws_hk,hws_eu,ocb,ctc,hcso,g42,tm,cmcc,hk_g42,dt)  [约束限制： - 仅对HTTPS协议类型的监听器有效](tag:hcso_dt)  [不支持tls1.3协议的套件。](tag:tm,hws_eu,g42,hk_g42)

        :param security_policy_id: The security_policy_id of this Listener.
        :type security_policy_id: str
        """
        self._security_policy_id = security_policy_id

    @property
    def enable_member_retry(self):
        r"""Gets the enable_member_retry of this Listener.

        参数解释：是否开启后端服务器的重试。  [约束限制： - 若关联是共享型LB，仅在protocol为HTTP、TERMINATED_HTTPS时才能传入该字段。 - 若关联是独享型LB，仅在protocol为HTTP、HTTPS和QUIC时才能传入该字段。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt)  [约束限制： - 仅在protocol为HTTP、HTTPS时才能传入该字段。](tag:hws_eu,hcso_dt)  取值范围：true 开启重试，false 不开启重试。  默认取值：true。  [不支持QUIC。](tag:tm,dt)

        :return: The enable_member_retry of this Listener.
        :rtype: bool
        """
        return self._enable_member_retry

    @enable_member_retry.setter
    def enable_member_retry(self, enable_member_retry):
        r"""Sets the enable_member_retry of this Listener.

        参数解释：是否开启后端服务器的重试。  [约束限制： - 若关联是共享型LB，仅在protocol为HTTP、TERMINATED_HTTPS时才能传入该字段。 - 若关联是独享型LB，仅在protocol为HTTP、HTTPS和QUIC时才能传入该字段。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt)  [约束限制： - 仅在protocol为HTTP、HTTPS时才能传入该字段。](tag:hws_eu,hcso_dt)  取值范围：true 开启重试，false 不开启重试。  默认取值：true。  [不支持QUIC。](tag:tm,dt)

        :param enable_member_retry: The enable_member_retry of this Listener.
        :type enable_member_retry: bool
        """
        self._enable_member_retry = enable_member_retry

    @property
    def keepalive_timeout(self):
        r"""Gets the keepalive_timeout of this Listener.

        参数解释：客户端连接空闲超时时间。在超过keepalive_timeout时长一直没有请求，负载均衡会暂时中断当前连接，直到下一次请求时重新建立新的连接。  约束限制：共享型实例的UDP监听器不支持此字段。  取值范围： - TCP监听器[和IP监听器](tag:hws_eu)：10-4000s，默认值为300s。 - 若为HTTP/HTTPS/TERMINATED_HTTPS监听器，取值范围为（0-4000s）默认值为60s。

        :return: The keepalive_timeout of this Listener.
        :rtype: int
        """
        return self._keepalive_timeout

    @keepalive_timeout.setter
    def keepalive_timeout(self, keepalive_timeout):
        r"""Sets the keepalive_timeout of this Listener.

        参数解释：客户端连接空闲超时时间。在超过keepalive_timeout时长一直没有请求，负载均衡会暂时中断当前连接，直到下一次请求时重新建立新的连接。  约束限制：共享型实例的UDP监听器不支持此字段。  取值范围： - TCP监听器[和IP监听器](tag:hws_eu)：10-4000s，默认值为300s。 - 若为HTTP/HTTPS/TERMINATED_HTTPS监听器，取值范围为（0-4000s）默认值为60s。

        :param keepalive_timeout: The keepalive_timeout of this Listener.
        :type keepalive_timeout: int
        """
        self._keepalive_timeout = keepalive_timeout

    @property
    def client_timeout(self):
        r"""Gets the client_timeout of this Listener.

        参数解释：等待客户端请求超时时间，包括两种情况： - 读取整个客户端请求头的超时时长：如果客户端未在超时时长内发送完整个请求头，则请求将被中断 - 两个连续body体的数据包到达LB的时间间隔，超出client_timeout将会断开连接。  约束限制：仅协议为HTTP/HTTPS的监听器支持该字段。  取值范围：1-300s  默认取值：60s。

        :return: The client_timeout of this Listener.
        :rtype: int
        """
        return self._client_timeout

    @client_timeout.setter
    def client_timeout(self, client_timeout):
        r"""Sets the client_timeout of this Listener.

        参数解释：等待客户端请求超时时间，包括两种情况： - 读取整个客户端请求头的超时时长：如果客户端未在超时时长内发送完整个请求头，则请求将被中断 - 两个连续body体的数据包到达LB的时间间隔，超出client_timeout将会断开连接。  约束限制：仅协议为HTTP/HTTPS的监听器支持该字段。  取值范围：1-300s  默认取值：60s。

        :param client_timeout: The client_timeout of this Listener.
        :type client_timeout: int
        """
        self._client_timeout = client_timeout

    @property
    def member_timeout(self):
        r"""Gets the member_timeout of this Listener.

        参数解释：等待后端服务器响应超时时间。请求转发后端服务器后，在等待超时member_timeout时长没有响应，负载均衡将终止等待，并返回HTTP504错误码。  约束限制：仅支持协议为HTTP/HTTPS的监听器。  取值范围：1-300s  默认取值：60s。

        :return: The member_timeout of this Listener.
        :rtype: int
        """
        return self._member_timeout

    @member_timeout.setter
    def member_timeout(self, member_timeout):
        r"""Sets the member_timeout of this Listener.

        参数解释：等待后端服务器响应超时时间。请求转发后端服务器后，在等待超时member_timeout时长没有响应，负载均衡将终止等待，并返回HTTP504错误码。  约束限制：仅支持协议为HTTP/HTTPS的监听器。  取值范围：1-300s  默认取值：60s。

        :param member_timeout: The member_timeout of this Listener.
        :type member_timeout: int
        """
        self._member_timeout = member_timeout

    @property
    def ipgroup(self):
        r"""Gets the ipgroup of this Listener.

        :return: The ipgroup of this Listener.
        :rtype: :class:`huaweicloudsdkelb.v3.ListenerIpGroup`
        """
        return self._ipgroup

    @ipgroup.setter
    def ipgroup(self, ipgroup):
        r"""Sets the ipgroup of this Listener.

        :param ipgroup: The ipgroup of this Listener.
        :type ipgroup: :class:`huaweicloudsdkelb.v3.ListenerIpGroup`
        """
        self._ipgroup = ipgroup

    @property
    def transparent_client_ip_enable(self):
        r"""Gets the transparent_client_ip_enable of this Listener.

        参数解释：是否透传客户端IP地址。开启后客户端IP地址将透传到后端服务器。 [仅作用于共享型LB的TCP/UDP监听器。  约束限制： - 开启特性后，ELB和后端服务器之间直接使用真实的IP访问，需要确保已正确设置服务器的安全组以及访问控制策略。 - 开启特性后，不支持同一台服务器既作为后端服务器又作为客户端的场景。 - 开启特性后，不支持变更后端服务器规格。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt)   取值范围： - 共享型LB的TCP/UDP监听器可设置为true或false，不传默认为false。 - 共享型LB的HTTP/HTTPS监听器只支持设置为true，不传默认为true。 - 独享型负载均衡器所有协议的监听器只支持设置为true，不传默认为true。  [只设支持置为true，不传默认为true。](tag:hws_eu,hcso_dt)

        :return: The transparent_client_ip_enable of this Listener.
        :rtype: bool
        """
        return self._transparent_client_ip_enable

    @transparent_client_ip_enable.setter
    def transparent_client_ip_enable(self, transparent_client_ip_enable):
        r"""Sets the transparent_client_ip_enable of this Listener.

        参数解释：是否透传客户端IP地址。开启后客户端IP地址将透传到后端服务器。 [仅作用于共享型LB的TCP/UDP监听器。  约束限制： - 开启特性后，ELB和后端服务器之间直接使用真实的IP访问，需要确保已正确设置服务器的安全组以及访问控制策略。 - 开启特性后，不支持同一台服务器既作为后端服务器又作为客户端的场景。 - 开启特性后，不支持变更后端服务器规格。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt)   取值范围： - 共享型LB的TCP/UDP监听器可设置为true或false，不传默认为false。 - 共享型LB的HTTP/HTTPS监听器只支持设置为true，不传默认为true。 - 独享型负载均衡器所有协议的监听器只支持设置为true，不传默认为true。  [只设支持置为true，不传默认为true。](tag:hws_eu,hcso_dt)

        :param transparent_client_ip_enable: The transparent_client_ip_enable of this Listener.
        :type transparent_client_ip_enable: bool
        """
        self._transparent_client_ip_enable = transparent_client_ip_enable

    @property
    def proxy_protocol_enable(self):
        r"""Gets the proxy_protocol_enable of this Listener.

        参数解释：是否开启proxy_protocol。仅TLS监听器可指定，其他协议的监听器该字段不生效，proxy_protocol不开启。

        :return: The proxy_protocol_enable of this Listener.
        :rtype: bool
        """
        return self._proxy_protocol_enable

    @proxy_protocol_enable.setter
    def proxy_protocol_enable(self, proxy_protocol_enable):
        r"""Sets the proxy_protocol_enable of this Listener.

        参数解释：是否开启proxy_protocol。仅TLS监听器可指定，其他协议的监听器该字段不生效，proxy_protocol不开启。

        :param proxy_protocol_enable: The proxy_protocol_enable of this Listener.
        :type proxy_protocol_enable: bool
        """
        self._proxy_protocol_enable = proxy_protocol_enable

    @property
    def enhance_l7policy_enable(self):
        r"""Gets the enhance_l7policy_enable of this Listener.

        参数解释：是否开启高级转发策略功能。开启高级转发策略后，支持更灵活的转发策略和转发规则设置。  开启后支持如下场景： - 转发策略的action字段支持指定为REDIRECT_TO_URL, FIXED_RESPONSE，即支持URL重定向和响应固定的内容给客户端。 - 转发策略支持指定priority、redirect_url_config、fixed_response_config字段。 - 转发规则rule的type可以指定METHOD, HEADER, QUERY_STRING, SOURCE_IP这几种取值。 - 转发规则rule的type为HOST_NAME时，转发规则rule的value支持通配符*。 - 转发规则支持指定conditions字段。  约束限制： - 开启后不支持关闭。 - 开启高级转发策略后，监听器关联的转发策略的匹配优先级由转发策略的priority字段来决定，不再自动排序。具体说明详见转发策略的priority字段的说明。  取值范围：true开启，false不开启。  默认取值：false。[西南-贵阳一和华南-广州局点，该配置默认true。](tag:hws)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The enhance_l7policy_enable of this Listener.
        :rtype: bool
        """
        return self._enhance_l7policy_enable

    @enhance_l7policy_enable.setter
    def enhance_l7policy_enable(self, enhance_l7policy_enable):
        r"""Sets the enhance_l7policy_enable of this Listener.

        参数解释：是否开启高级转发策略功能。开启高级转发策略后，支持更灵活的转发策略和转发规则设置。  开启后支持如下场景： - 转发策略的action字段支持指定为REDIRECT_TO_URL, FIXED_RESPONSE，即支持URL重定向和响应固定的内容给客户端。 - 转发策略支持指定priority、redirect_url_config、fixed_response_config字段。 - 转发规则rule的type可以指定METHOD, HEADER, QUERY_STRING, SOURCE_IP这几种取值。 - 转发规则rule的type为HOST_NAME时，转发规则rule的value支持通配符*。 - 转发规则支持指定conditions字段。  约束限制： - 开启后不支持关闭。 - 开启高级转发策略后，监听器关联的转发策略的匹配优先级由转发策略的priority字段来决定，不再自动排序。具体说明详见转发策略的priority字段的说明。  取值范围：true开启，false不开启。  默认取值：false。[西南-贵阳一和华南-广州局点，该配置默认true。](tag:hws)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param enhance_l7policy_enable: The enhance_l7policy_enable of this Listener.
        :type enhance_l7policy_enable: bool
        """
        self._enhance_l7policy_enable = enhance_l7policy_enable

    @property
    def quic_config(self):
        r"""Gets the quic_config of this Listener.

        :return: The quic_config of this Listener.
        :rtype: :class:`huaweicloudsdkelb.v3.ListenerQuicConfig`
        """
        return self._quic_config

    @quic_config.setter
    def quic_config(self, quic_config):
        r"""Sets the quic_config of this Listener.

        :param quic_config: The quic_config of this Listener.
        :type quic_config: :class:`huaweicloudsdkelb.v3.ListenerQuicConfig`
        """
        self._quic_config = quic_config

    @property
    def protection_status(self):
        r"""Gets the protection_status of this Listener.

        参数解释：修改保护状态,   取值范围： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护

        :return: The protection_status of this Listener.
        :rtype: str
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this Listener.

        参数解释：修改保护状态,   取值范围： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护

        :param protection_status: The protection_status of this Listener.
        :type protection_status: str
        """
        self._protection_status = protection_status

    @property
    def protection_reason(self):
        r"""Gets the protection_reason of this Listener.

        参数解释：设置保护的原因。作为protection_status的转态设置的原因。  约束限制：仅当protection_status为consoleProtection时有效。  取值范围：除'<'和'>'外通用Unicode字符集字符，最大255个字符。

        :return: The protection_reason of this Listener.
        :rtype: str
        """
        return self._protection_reason

    @protection_reason.setter
    def protection_reason(self, protection_reason):
        r"""Sets the protection_reason of this Listener.

        参数解释：设置保护的原因。作为protection_status的转态设置的原因。  约束限制：仅当protection_status为consoleProtection时有效。  取值范围：除'<'和'>'外通用Unicode字符集字符，最大255个字符。

        :param protection_reason: The protection_reason of this Listener.
        :type protection_reason: str
        """
        self._protection_reason = protection_reason

    @property
    def gzip_enable(self):
        r"""Gets the gzip_enable of this Listener.

        参数解释：ELB是否开启gzip压缩。  [约束限制：仅HTTP/HTTPS类型监听器支持配置。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt) [约束限制：仅HTTP/HTTPS/QUIC类型监听器支持配置。](tag:hws,hws_hk,hws_test,hcs,hcs_sm,hcso,hk_vdf,srg,fcs,fcs_vm,mix,ocb,ctc,cmcc,ct,sbc,hws_ocb,hk_sbc)  默认取值：false  [不支持该字段，请勿使用。](tag:hws_eu,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)

        :return: The gzip_enable of this Listener.
        :rtype: bool
        """
        return self._gzip_enable

    @gzip_enable.setter
    def gzip_enable(self, gzip_enable):
        r"""Sets the gzip_enable of this Listener.

        参数解释：ELB是否开启gzip压缩。  [约束限制：仅HTTP/HTTPS类型监听器支持配置。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt) [约束限制：仅HTTP/HTTPS/QUIC类型监听器支持配置。](tag:hws,hws_hk,hws_test,hcs,hcs_sm,hcso,hk_vdf,srg,fcs,fcs_vm,mix,ocb,ctc,cmcc,ct,sbc,hws_ocb,hk_sbc)  默认取值：false  [不支持该字段，请勿使用。](tag:hws_eu,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)

        :param gzip_enable: The gzip_enable of this Listener.
        :type gzip_enable: bool
        """
        self._gzip_enable = gzip_enable

    @property
    def port_ranges(self):
        r"""Gets the port_ranges of this Listener.

        参数解释：端口监听范围（闭区间)。  约束限制： - 最多指定10个端口组，每个组范围不可有重叠部分 - 仅当protocol_port为0时可以传入。  [不支持该字段，请勿使用。](tag:hws_eu,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)

        :return: The port_ranges of this Listener.
        :rtype: list[:class:`huaweicloudsdkelb.v3.PortRange`]
        """
        return self._port_ranges

    @port_ranges.setter
    def port_ranges(self, port_ranges):
        r"""Sets the port_ranges of this Listener.

        参数解释：端口监听范围（闭区间)。  约束限制： - 最多指定10个端口组，每个组范围不可有重叠部分 - 仅当protocol_port为0时可以传入。  [不支持该字段，请勿使用。](tag:hws_eu,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42)

        :param port_ranges: The port_ranges of this Listener.
        :type port_ranges: list[:class:`huaweicloudsdkelb.v3.PortRange`]
        """
        self._port_ranges = port_ranges

    @property
    def ssl_early_data_enable(self):
        r"""Gets the ssl_early_data_enable of this Listener.

        参数解释：监听器0-RTT能力开关  约束限制：仅HTTPS类型监听器支持配置，需要依赖TLSv1.3安全策略协议。  默认取值：false。

        :return: The ssl_early_data_enable of this Listener.
        :rtype: bool
        """
        return self._ssl_early_data_enable

    @ssl_early_data_enable.setter
    def ssl_early_data_enable(self, ssl_early_data_enable):
        r"""Sets the ssl_early_data_enable of this Listener.

        参数解释：监听器0-RTT能力开关  约束限制：仅HTTPS类型监听器支持配置，需要依赖TLSv1.3安全策略协议。  默认取值：false。

        :param ssl_early_data_enable: The ssl_early_data_enable of this Listener.
        :type ssl_early_data_enable: bool
        """
        self._ssl_early_data_enable = ssl_early_data_enable

    @property
    def cps(self):
        r"""Gets the cps of this Listener.

        参数解释：监听器新建限速  约束限制：当该限速值大于LB的限速值时，以LB的限速值生效  取值范围：0-1000000  默认取值：0，表示不限速

        :return: The cps of this Listener.
        :rtype: int
        """
        return self._cps

    @cps.setter
    def cps(self, cps):
        r"""Sets the cps of this Listener.

        参数解释：监听器新建限速  约束限制：当该限速值大于LB的限速值时，以LB的限速值生效  取值范围：0-1000000  默认取值：0，表示不限速

        :param cps: The cps of this Listener.
        :type cps: int
        """
        self._cps = cps

    @property
    def connection(self):
        r"""Gets the connection of this Listener.

        参数解释：监听器并发限速  约束限制：当该限速值大于LB的限速值时，以LB的限速值生效  取值范围：0-1000000  默认取值：0，表示不限速

        :return: The connection of this Listener.
        :rtype: int
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this Listener.

        参数解释：监听器并发限速  约束限制：当该限速值大于LB的限速值时，以LB的限速值生效  取值范围：0-1000000  默认取值：0，表示不限速

        :param connection: The connection of this Listener.
        :type connection: int
        """
        self._connection = connection

    @property
    def nat64_enable(self):
        r"""Gets the nat64_enable of this Listener.

        参数解释： 监听器地址族转换能力开关，可以实现客户端通过访问LB的IPv4或者IPv6地址，来访问IPv4后端和IPv6后端。  约束限制： 仅对于TCP、UDP协议类型的监听器生效，与transparent_client_ip_enable，获取客户端ip功能开关互斥，开启地址族转换同时需要保证获取客户端ip功能关闭。  取值范围： - true：开启地址族转换功能 - false：关闭地址族转换功能  默认取值：false

        :return: The nat64_enable of this Listener.
        :rtype: bool
        """
        return self._nat64_enable

    @nat64_enable.setter
    def nat64_enable(self, nat64_enable):
        r"""Sets the nat64_enable of this Listener.

        参数解释： 监听器地址族转换能力开关，可以实现客户端通过访问LB的IPv4或者IPv6地址，来访问IPv4后端和IPv6后端。  约束限制： 仅对于TCP、UDP协议类型的监听器生效，与transparent_client_ip_enable，获取客户端ip功能开关互斥，开启地址族转换同时需要保证获取客户端ip功能关闭。  取值范围： - true：开启地址族转换功能 - false：关闭地址族转换功能  默认取值：false

        :param nat64_enable: The nat64_enable of this Listener.
        :type nat64_enable: bool
        """
        self._nat64_enable = nat64_enable

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
        if not isinstance(other, Listener):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
