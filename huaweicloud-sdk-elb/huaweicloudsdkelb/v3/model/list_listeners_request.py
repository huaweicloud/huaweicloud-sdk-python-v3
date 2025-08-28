# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListListenersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'protocol_port': 'list[str]',
        'protocol': 'list[str]',
        'description': 'list[str]',
        'default_tls_container_ref': 'list[str]',
        'client_ca_tls_container_ref': 'list[str]',
        'admin_state_up': 'bool',
        'include_recycle_bin': 'bool',
        'connection_limit': 'list[int]',
        'default_pool_id': 'list[str]',
        'id': 'list[str]',
        'name': 'list[str]',
        'http2_enable': 'bool',
        'loadbalancer_id': 'list[str]',
        'tls_ciphers_policy': 'list[str]',
        'member_address': 'list[str]',
        'member_device_id': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'enable_member_retry': 'bool',
        'member_timeout': 'list[int]',
        'client_timeout': 'list[int]',
        'keepalive_timeout': 'list[int]',
        'transparent_client_ip_enable': 'bool',
        'proxy_protocol_enable': 'bool',
        'enhance_l7policy_enable': 'bool',
        'member_instance_id': 'list[str]',
        'protection_status': 'list[str]',
        'ssl_early_data_enable': 'bool',
        'nat64_enable': 'bool'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'protocol_port': 'protocol_port',
        'protocol': 'protocol',
        'description': 'description',
        'default_tls_container_ref': 'default_tls_container_ref',
        'client_ca_tls_container_ref': 'client_ca_tls_container_ref',
        'admin_state_up': 'admin_state_up',
        'include_recycle_bin': 'include_recycle_bin',
        'connection_limit': 'connection_limit',
        'default_pool_id': 'default_pool_id',
        'id': 'id',
        'name': 'name',
        'http2_enable': 'http2_enable',
        'loadbalancer_id': 'loadbalancer_id',
        'tls_ciphers_policy': 'tls_ciphers_policy',
        'member_address': 'member_address',
        'member_device_id': 'member_device_id',
        'enterprise_project_id': 'enterprise_project_id',
        'enable_member_retry': 'enable_member_retry',
        'member_timeout': 'member_timeout',
        'client_timeout': 'client_timeout',
        'keepalive_timeout': 'keepalive_timeout',
        'transparent_client_ip_enable': 'transparent_client_ip_enable',
        'proxy_protocol_enable': 'proxy_protocol_enable',
        'enhance_l7policy_enable': 'enhance_l7policy_enable',
        'member_instance_id': 'member_instance_id',
        'protection_status': 'protection_status',
        'ssl_early_data_enable': 'ssl_early_data_enable',
        'nat64_enable': 'nat64_enable'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, protocol_port=None, protocol=None, description=None, default_tls_container_ref=None, client_ca_tls_container_ref=None, admin_state_up=None, include_recycle_bin=None, connection_limit=None, default_pool_id=None, id=None, name=None, http2_enable=None, loadbalancer_id=None, tls_ciphers_policy=None, member_address=None, member_device_id=None, enterprise_project_id=None, enable_member_retry=None, member_timeout=None, client_timeout=None, keepalive_timeout=None, transparent_client_ip_enable=None, proxy_protocol_enable=None, enhance_l7policy_enable=None, member_instance_id=None, protection_status=None, ssl_early_data_enable=None, nat64_enable=None):
        r"""ListListenersRequest

        The model defined in huaweicloud sdk

        :param limit: **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000
        :type limit: int
        :param marker: **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及
        :type marker: str
        :param page_reverse: **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false
        :type page_reverse: bool
        :param protocol_port: **参数解释**：监听器的前端监听端口。 支持多值查询，查询条件格式：*protocol_port&#x3D;xxx&amp;protocol_port&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type protocol_port: list[str]
        :param protocol: **参数解释**：监听器的监听协议。 支持多值查询，查询条件格式：*protocol&#x3D;xxx&amp;protocol&#x3D;xxx*。  **约束限制**：不涉及  [取值范围：TCP、UDP、HTTP、HTTPS、TERMINATED_HTTPS、QUIC、TLS。 说明：TERMINATED_HTTPS为共享型LB上的监听器独有的协议。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,srg,fcs,dt)  [取值范围：TCP、UDP、HTTP、HTTPS。](tag:hcso_dt) [取值范围：TCP、UDP、IP、HTTP、HTTPS。IP为网关型LB上的监听器独有的协议。](tag:hws_eu)  **默认取值**：不涉及  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt)
        :type protocol: list[str]
        :param description: **参数解释**：监听器的描述信息。 支持多值查询，查询条件格式：*description&#x3D;xxx&amp;description&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type description: list[str]
        :param default_tls_container_ref: **参数解释**：监听器的服务器证书ID。 支持多值查询，查询条件格式： *default_tls_container_ref&#x3D;xxx&amp;default_tls_container_ref&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type default_tls_container_ref: list[str]
        :param client_ca_tls_container_ref: **参数解释**：监听器的CA证书ID。 支持多值查询，查询条件格式： *client_ca_tls_container_ref&#x3D;xxx&amp;client_ca_tls_container_ref&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type client_ca_tls_container_ref: list[str]
        :param admin_state_up: **参数解释**：监听器的管理状态。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type admin_state_up: bool
        :param include_recycle_bin: **参数解释**：查询结果是否包含回收站负载均衡器的监听器  **约束限制**：不涉及  **取值范围**： - true ：包含回收站elb的监听器。 - false：不包含回收站elb的监听器。  **默认取值**：不涉及
        :type include_recycle_bin: bool
        :param connection_limit: **参数解释**：监听器的最大连接数。 支持多值查询，查询条件格式：*connection_limit&#x3D;xxx&amp;connection_limit&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type connection_limit: list[int]
        :param default_pool_id: **参数解释**：监听器的默认后端服务器组ID。当请求没有匹配的转发策略时，转发到默认后端服务器组上处理。 支持多值查询，查询条件格式：*default_pool_id&#x3D;xxx&amp;default_pool_id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type default_pool_id: list[str]
        :param id: **参数解释**：监听器ID。 支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type id: list[str]
        :param name: **参数解释**：监听器名称。 支持多值查询，查询条件格式：*name&#x3D;xxx&amp;name&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type name: list[str]
        :param http2_enable: **参数解释**：客户端与LB之间的HTTPS请求的HTTP2功能的开启状态。 开启后，可提升客户端与LB间的访问性能，但LB与后端服务器间仍采用HTTP1.X协议。  **约束限制**：不涉及  **取值范围**：true 开启，false 不开启。  **默认取值**：不涉及  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt)
        :type http2_enable: bool
        :param loadbalancer_id: **参数解释**：监听器所属的负载均衡器ID。 支持多值查询，查询条件格式：*loadbalancer_id&#x3D;xxx&amp;loadbalancer_id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type loadbalancer_id: list[str]
        :param tls_ciphers_policy: **参数解释**：监听器使用的安全策略。 支持多值查询，查询条件格式：*tls_ciphers_policy&#x3D;xxx&amp;tls_ciphers_policy&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type tls_ciphers_policy: list[str]
        :param member_address: **参数解释**：后端服务器的IP地址。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_address&#x3D;xxx&amp;member_address&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type member_address: list[str]
        :param member_device_id: **参数解释**：后端服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_device_id&#x3D;xxx&amp;member_device_id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type member_device_id: list[str]
        :param enterprise_project_id: **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  **约束限制**： 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:listeners:list权限。 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type enterprise_project_id: list[str]
        :param enable_member_retry: **参数解释**：是否开启后端服务器的重试。  **约束限制**：不涉及  **取值范围**：true 开启，false 不开启。  **默认取值**：不涉及
        :type enable_member_retry: bool
        :param member_timeout: **参数解释**：等待后端服务器响应超时时间。请求转发后端服务器后，在等待超时member_timeout时长没有响应，负载均衡将终止等待，并返回HTTP504错误码。 支持多值查询，查询条件格式：*member_timeout&#x3D;xxx&amp;member_timeout&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type member_timeout: list[int]
        :param client_timeout: **参数解释**：等待客户端请求超时时间，包括两种情况： - 读取整个客户端请求头的超时时长：如果客户端未在超时时长内发送完整个请求头，则请求将被中断 - 两个连续body体的数据包到达LB的时间间隔，超出client_timeout将会断开连接。 支持多值查询，查询条件格式：*client_timeout&#x3D;xxx&amp;client_timeout&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type client_timeout: list[int]
        :param keepalive_timeout: **参数解释**：客户端连接空闲超时时间。在超过keepalive_timeout时长一直没有请求，负载均衡会暂时中断当前连接，直到下一次请求时重新建立新的连接。 支持多值查询，查询条件格式：*keepalive_timeout&#x3D;xxx&amp;keepalive_timeout&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type keepalive_timeout: list[int]
        :param transparent_client_ip_enable: **参数解释**：是否开启后客户端IP地址将透传到后端服务器。 [仅作用于共享型LB的TCP/UDP监听器。](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)  **约束限制**：不涉及  **取值范围**：true开启，false不开启。  **默认取值**：不涉及
        :type transparent_client_ip_enable: bool
        :param proxy_protocol_enable: **参数解释**：是否开启proxy_protocol。  **约束限制**：不涉及  **取值范围**：true开启，false不开启。  **默认取值**：不涉及
        :type proxy_protocol_enable: bool
        :param enhance_l7policy_enable: **参数解释**：是否开启高级转发策略功能。开启高级转发策略后，支持更灵活的转发策略和转发规则设置。  **约束限制**：不涉及  **取值范围**：true开启，false不开启。  **默认取值**：不涉及  [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type enhance_l7policy_enable: bool
        :param member_instance_id: **参数解释**：后端服务器ID。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_instance_id&#x3D;xxx&amp;member_instance_id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type member_instance_id: list[str]
        :param protection_status: **参数解释**：修改保护状态。 支持多值查询，查询条件格式：*protection_status&#x3D;xxx&amp;protection_status&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护  **默认取值**：不涉及
        :type protection_status: list[str]
        :param ssl_early_data_enable: **参数解释**：是否开启监听器0-RTT功能。  **约束限制**：不涉及  **取值范围**：true开启，false不开启。  **默认取值**：不涉及
        :type ssl_early_data_enable: bool
        :param nat64_enable: **参数解释**：是否开启nat64地址转换功能。  **约束限制**：不涉及  **取值范围**：true开启，false不开启。  **默认取值**：不涉及
        :type nat64_enable: bool
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._protocol_port = None
        self._protocol = None
        self._description = None
        self._default_tls_container_ref = None
        self._client_ca_tls_container_ref = None
        self._admin_state_up = None
        self._include_recycle_bin = None
        self._connection_limit = None
        self._default_pool_id = None
        self._id = None
        self._name = None
        self._http2_enable = None
        self._loadbalancer_id = None
        self._tls_ciphers_policy = None
        self._member_address = None
        self._member_device_id = None
        self._enterprise_project_id = None
        self._enable_member_retry = None
        self._member_timeout = None
        self._client_timeout = None
        self._keepalive_timeout = None
        self._transparent_client_ip_enable = None
        self._proxy_protocol_enable = None
        self._enhance_l7policy_enable = None
        self._member_instance_id = None
        self._protection_status = None
        self._ssl_early_data_enable = None
        self._nat64_enable = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if protocol is not None:
            self.protocol = protocol
        if description is not None:
            self.description = description
        if default_tls_container_ref is not None:
            self.default_tls_container_ref = default_tls_container_ref
        if client_ca_tls_container_ref is not None:
            self.client_ca_tls_container_ref = client_ca_tls_container_ref
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if include_recycle_bin is not None:
            self.include_recycle_bin = include_recycle_bin
        if connection_limit is not None:
            self.connection_limit = connection_limit
        if default_pool_id is not None:
            self.default_pool_id = default_pool_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if http2_enable is not None:
            self.http2_enable = http2_enable
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if tls_ciphers_policy is not None:
            self.tls_ciphers_policy = tls_ciphers_policy
        if member_address is not None:
            self.member_address = member_address
        if member_device_id is not None:
            self.member_device_id = member_device_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enable_member_retry is not None:
            self.enable_member_retry = enable_member_retry
        if member_timeout is not None:
            self.member_timeout = member_timeout
        if client_timeout is not None:
            self.client_timeout = client_timeout
        if keepalive_timeout is not None:
            self.keepalive_timeout = keepalive_timeout
        if transparent_client_ip_enable is not None:
            self.transparent_client_ip_enable = transparent_client_ip_enable
        if proxy_protocol_enable is not None:
            self.proxy_protocol_enable = proxy_protocol_enable
        if enhance_l7policy_enable is not None:
            self.enhance_l7policy_enable = enhance_l7policy_enable
        if member_instance_id is not None:
            self.member_instance_id = member_instance_id
        if protection_status is not None:
            self.protection_status = protection_status
        if ssl_early_data_enable is not None:
            self.ssl_early_data_enable = ssl_early_data_enable
        if nat64_enable is not None:
            self.nat64_enable = nat64_enable

    @property
    def limit(self):
        r"""Gets the limit of this ListListenersRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :return: The limit of this ListListenersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListListenersRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :param limit: The limit of this ListListenersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListListenersRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The marker of this ListListenersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListListenersRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :param marker: The marker of this ListListenersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListListenersRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :return: The page_reverse of this ListListenersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListListenersRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :param page_reverse: The page_reverse of this ListListenersRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this ListListenersRequest.

        **参数解释**：监听器的前端监听端口。 支持多值查询，查询条件格式：*protocol_port=xxx&protocol_port=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The protocol_port of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this ListListenersRequest.

        **参数解释**：监听器的前端监听端口。 支持多值查询，查询条件格式：*protocol_port=xxx&protocol_port=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param protocol_port: The protocol_port of this ListListenersRequest.
        :type protocol_port: list[str]
        """
        self._protocol_port = protocol_port

    @property
    def protocol(self):
        r"""Gets the protocol of this ListListenersRequest.

        **参数解释**：监听器的监听协议。 支持多值查询，查询条件格式：*protocol=xxx&protocol=xxx*。  **约束限制**：不涉及  [取值范围：TCP、UDP、HTTP、HTTPS、TERMINATED_HTTPS、QUIC、TLS。 说明：TERMINATED_HTTPS为共享型LB上的监听器独有的协议。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,srg,fcs,dt)  [取值范围：TCP、UDP、HTTP、HTTPS。](tag:hcso_dt) [取值范围：TCP、UDP、IP、HTTP、HTTPS。IP为网关型LB上的监听器独有的协议。](tag:hws_eu)  **默认取值**：不涉及  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt)

        :return: The protocol of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ListListenersRequest.

        **参数解释**：监听器的监听协议。 支持多值查询，查询条件格式：*protocol=xxx&protocol=xxx*。  **约束限制**：不涉及  [取值范围：TCP、UDP、HTTP、HTTPS、TERMINATED_HTTPS、QUIC、TLS。 说明：TERMINATED_HTTPS为共享型LB上的监听器独有的协议。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,srg,fcs,dt)  [取值范围：TCP、UDP、HTTP、HTTPS。](tag:hcso_dt) [取值范围：TCP、UDP、IP、HTTP、HTTPS。IP为网关型LB上的监听器独有的协议。](tag:hws_eu)  **默认取值**：不涉及  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt)

        :param protocol: The protocol of this ListListenersRequest.
        :type protocol: list[str]
        """
        self._protocol = protocol

    @property
    def description(self):
        r"""Gets the description of this ListListenersRequest.

        **参数解释**：监听器的描述信息。 支持多值查询，查询条件格式：*description=xxx&description=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The description of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListListenersRequest.

        **参数解释**：监听器的描述信息。 支持多值查询，查询条件格式：*description=xxx&description=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param description: The description of this ListListenersRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def default_tls_container_ref(self):
        r"""Gets the default_tls_container_ref of this ListListenersRequest.

        **参数解释**：监听器的服务器证书ID。 支持多值查询，查询条件格式： *default_tls_container_ref=xxx&default_tls_container_ref=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The default_tls_container_ref of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        r"""Sets the default_tls_container_ref of this ListListenersRequest.

        **参数解释**：监听器的服务器证书ID。 支持多值查询，查询条件格式： *default_tls_container_ref=xxx&default_tls_container_ref=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param default_tls_container_ref: The default_tls_container_ref of this ListListenersRequest.
        :type default_tls_container_ref: list[str]
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def client_ca_tls_container_ref(self):
        r"""Gets the client_ca_tls_container_ref of this ListListenersRequest.

        **参数解释**：监听器的CA证书ID。 支持多值查询，查询条件格式： *client_ca_tls_container_ref=xxx&client_ca_tls_container_ref=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The client_ca_tls_container_ref of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        r"""Sets the client_ca_tls_container_ref of this ListListenersRequest.

        **参数解释**：监听器的CA证书ID。 支持多值查询，查询条件格式： *client_ca_tls_container_ref=xxx&client_ca_tls_container_ref=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param client_ca_tls_container_ref: The client_ca_tls_container_ref of this ListListenersRequest.
        :type client_ca_tls_container_ref: list[str]
        """
        self._client_ca_tls_container_ref = client_ca_tls_container_ref

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this ListListenersRequest.

        **参数解释**：监听器的管理状态。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The admin_state_up of this ListListenersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this ListListenersRequest.

        **参数解释**：监听器的管理状态。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param admin_state_up: The admin_state_up of this ListListenersRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def include_recycle_bin(self):
        r"""Gets the include_recycle_bin of this ListListenersRequest.

        **参数解释**：查询结果是否包含回收站负载均衡器的监听器  **约束限制**：不涉及  **取值范围**： - true ：包含回收站elb的监听器。 - false：不包含回收站elb的监听器。  **默认取值**：不涉及

        :return: The include_recycle_bin of this ListListenersRequest.
        :rtype: bool
        """
        return self._include_recycle_bin

    @include_recycle_bin.setter
    def include_recycle_bin(self, include_recycle_bin):
        r"""Sets the include_recycle_bin of this ListListenersRequest.

        **参数解释**：查询结果是否包含回收站负载均衡器的监听器  **约束限制**：不涉及  **取值范围**： - true ：包含回收站elb的监听器。 - false：不包含回收站elb的监听器。  **默认取值**：不涉及

        :param include_recycle_bin: The include_recycle_bin of this ListListenersRequest.
        :type include_recycle_bin: bool
        """
        self._include_recycle_bin = include_recycle_bin

    @property
    def connection_limit(self):
        r"""Gets the connection_limit of this ListListenersRequest.

        **参数解释**：监听器的最大连接数。 支持多值查询，查询条件格式：*connection_limit=xxx&connection_limit=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The connection_limit of this ListListenersRequest.
        :rtype: list[int]
        """
        return self._connection_limit

    @connection_limit.setter
    def connection_limit(self, connection_limit):
        r"""Sets the connection_limit of this ListListenersRequest.

        **参数解释**：监听器的最大连接数。 支持多值查询，查询条件格式：*connection_limit=xxx&connection_limit=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param connection_limit: The connection_limit of this ListListenersRequest.
        :type connection_limit: list[int]
        """
        self._connection_limit = connection_limit

    @property
    def default_pool_id(self):
        r"""Gets the default_pool_id of this ListListenersRequest.

        **参数解释**：监听器的默认后端服务器组ID。当请求没有匹配的转发策略时，转发到默认后端服务器组上处理。 支持多值查询，查询条件格式：*default_pool_id=xxx&default_pool_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The default_pool_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._default_pool_id

    @default_pool_id.setter
    def default_pool_id(self, default_pool_id):
        r"""Sets the default_pool_id of this ListListenersRequest.

        **参数解释**：监听器的默认后端服务器组ID。当请求没有匹配的转发策略时，转发到默认后端服务器组上处理。 支持多值查询，查询条件格式：*default_pool_id=xxx&default_pool_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param default_pool_id: The default_pool_id of this ListListenersRequest.
        :type default_pool_id: list[str]
        """
        self._default_pool_id = default_pool_id

    @property
    def id(self):
        r"""Gets the id of this ListListenersRequest.

        **参数解释**：监听器ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListListenersRequest.

        **参数解释**：监听器ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param id: The id of this ListListenersRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListListenersRequest.

        **参数解释**：监听器名称。 支持多值查询，查询条件格式：*name=xxx&name=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The name of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListListenersRequest.

        **参数解释**：监听器名称。 支持多值查询，查询条件格式：*name=xxx&name=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param name: The name of this ListListenersRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def http2_enable(self):
        r"""Gets the http2_enable of this ListListenersRequest.

        **参数解释**：客户端与LB之间的HTTPS请求的HTTP2功能的开启状态。 开启后，可提升客户端与LB间的访问性能，但LB与后端服务器间仍采用HTTP1.X协议。  **约束限制**：不涉及  **取值范围**：true 开启，false 不开启。  **默认取值**：不涉及  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt)

        :return: The http2_enable of this ListListenersRequest.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        r"""Sets the http2_enable of this ListListenersRequest.

        **参数解释**：客户端与LB之间的HTTPS请求的HTTP2功能的开启状态。 开启后，可提升客户端与LB间的访问性能，但LB与后端服务器间仍采用HTTP1.X协议。  **约束限制**：不涉及  **取值范围**：true 开启，false 不开启。  **默认取值**：不涉及  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt)

        :param http2_enable: The http2_enable of this ListListenersRequest.
        :type http2_enable: bool
        """
        self._http2_enable = http2_enable

    @property
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this ListListenersRequest.

        **参数解释**：监听器所属的负载均衡器ID。 支持多值查询，查询条件格式：*loadbalancer_id=xxx&loadbalancer_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The loadbalancer_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this ListListenersRequest.

        **参数解释**：监听器所属的负载均衡器ID。 支持多值查询，查询条件格式：*loadbalancer_id=xxx&loadbalancer_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param loadbalancer_id: The loadbalancer_id of this ListListenersRequest.
        :type loadbalancer_id: list[str]
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def tls_ciphers_policy(self):
        r"""Gets the tls_ciphers_policy of this ListListenersRequest.

        **参数解释**：监听器使用的安全策略。 支持多值查询，查询条件格式：*tls_ciphers_policy=xxx&tls_ciphers_policy=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The tls_ciphers_policy of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._tls_ciphers_policy

    @tls_ciphers_policy.setter
    def tls_ciphers_policy(self, tls_ciphers_policy):
        r"""Sets the tls_ciphers_policy of this ListListenersRequest.

        **参数解释**：监听器使用的安全策略。 支持多值查询，查询条件格式：*tls_ciphers_policy=xxx&tls_ciphers_policy=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param tls_ciphers_policy: The tls_ciphers_policy of this ListListenersRequest.
        :type tls_ciphers_policy: list[str]
        """
        self._tls_ciphers_policy = tls_ciphers_policy

    @property
    def member_address(self):
        r"""Gets the member_address of this ListListenersRequest.

        **参数解释**：后端服务器的IP地址。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_address=xxx&member_address=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The member_address of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._member_address

    @member_address.setter
    def member_address(self, member_address):
        r"""Sets the member_address of this ListListenersRequest.

        **参数解释**：后端服务器的IP地址。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_address=xxx&member_address=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param member_address: The member_address of this ListListenersRequest.
        :type member_address: list[str]
        """
        self._member_address = member_address

    @property
    def member_device_id(self):
        r"""Gets the member_device_id of this ListListenersRequest.

        **参数解释**：后端服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_device_id=xxx&member_device_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The member_device_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._member_device_id

    @member_device_id.setter
    def member_device_id(self, member_device_id):
        r"""Sets the member_device_id of this ListListenersRequest.

        **参数解释**：后端服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_device_id=xxx&member_device_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param member_device_id: The member_device_id of this ListListenersRequest.
        :type member_device_id: list[str]
        """
        self._member_device_id = member_device_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListListenersRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:listeners:list权限。 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The enterprise_project_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListListenersRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:listeners:list权限。 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this ListListenersRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enable_member_retry(self):
        r"""Gets the enable_member_retry of this ListListenersRequest.

        **参数解释**：是否开启后端服务器的重试。  **约束限制**：不涉及  **取值范围**：true 开启，false 不开启。  **默认取值**：不涉及

        :return: The enable_member_retry of this ListListenersRequest.
        :rtype: bool
        """
        return self._enable_member_retry

    @enable_member_retry.setter
    def enable_member_retry(self, enable_member_retry):
        r"""Sets the enable_member_retry of this ListListenersRequest.

        **参数解释**：是否开启后端服务器的重试。  **约束限制**：不涉及  **取值范围**：true 开启，false 不开启。  **默认取值**：不涉及

        :param enable_member_retry: The enable_member_retry of this ListListenersRequest.
        :type enable_member_retry: bool
        """
        self._enable_member_retry = enable_member_retry

    @property
    def member_timeout(self):
        r"""Gets the member_timeout of this ListListenersRequest.

        **参数解释**：等待后端服务器响应超时时间。请求转发后端服务器后，在等待超时member_timeout时长没有响应，负载均衡将终止等待，并返回HTTP504错误码。 支持多值查询，查询条件格式：*member_timeout=xxx&member_timeout=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The member_timeout of this ListListenersRequest.
        :rtype: list[int]
        """
        return self._member_timeout

    @member_timeout.setter
    def member_timeout(self, member_timeout):
        r"""Sets the member_timeout of this ListListenersRequest.

        **参数解释**：等待后端服务器响应超时时间。请求转发后端服务器后，在等待超时member_timeout时长没有响应，负载均衡将终止等待，并返回HTTP504错误码。 支持多值查询，查询条件格式：*member_timeout=xxx&member_timeout=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param member_timeout: The member_timeout of this ListListenersRequest.
        :type member_timeout: list[int]
        """
        self._member_timeout = member_timeout

    @property
    def client_timeout(self):
        r"""Gets the client_timeout of this ListListenersRequest.

        **参数解释**：等待客户端请求超时时间，包括两种情况： - 读取整个客户端请求头的超时时长：如果客户端未在超时时长内发送完整个请求头，则请求将被中断 - 两个连续body体的数据包到达LB的时间间隔，超出client_timeout将会断开连接。 支持多值查询，查询条件格式：*client_timeout=xxx&client_timeout=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The client_timeout of this ListListenersRequest.
        :rtype: list[int]
        """
        return self._client_timeout

    @client_timeout.setter
    def client_timeout(self, client_timeout):
        r"""Sets the client_timeout of this ListListenersRequest.

        **参数解释**：等待客户端请求超时时间，包括两种情况： - 读取整个客户端请求头的超时时长：如果客户端未在超时时长内发送完整个请求头，则请求将被中断 - 两个连续body体的数据包到达LB的时间间隔，超出client_timeout将会断开连接。 支持多值查询，查询条件格式：*client_timeout=xxx&client_timeout=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param client_timeout: The client_timeout of this ListListenersRequest.
        :type client_timeout: list[int]
        """
        self._client_timeout = client_timeout

    @property
    def keepalive_timeout(self):
        r"""Gets the keepalive_timeout of this ListListenersRequest.

        **参数解释**：客户端连接空闲超时时间。在超过keepalive_timeout时长一直没有请求，负载均衡会暂时中断当前连接，直到下一次请求时重新建立新的连接。 支持多值查询，查询条件格式：*keepalive_timeout=xxx&keepalive_timeout=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The keepalive_timeout of this ListListenersRequest.
        :rtype: list[int]
        """
        return self._keepalive_timeout

    @keepalive_timeout.setter
    def keepalive_timeout(self, keepalive_timeout):
        r"""Sets the keepalive_timeout of this ListListenersRequest.

        **参数解释**：客户端连接空闲超时时间。在超过keepalive_timeout时长一直没有请求，负载均衡会暂时中断当前连接，直到下一次请求时重新建立新的连接。 支持多值查询，查询条件格式：*keepalive_timeout=xxx&keepalive_timeout=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param keepalive_timeout: The keepalive_timeout of this ListListenersRequest.
        :type keepalive_timeout: list[int]
        """
        self._keepalive_timeout = keepalive_timeout

    @property
    def transparent_client_ip_enable(self):
        r"""Gets the transparent_client_ip_enable of this ListListenersRequest.

        **参数解释**：是否开启后客户端IP地址将透传到后端服务器。 [仅作用于共享型LB的TCP/UDP监听器。](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)  **约束限制**：不涉及  **取值范围**：true开启，false不开启。  **默认取值**：不涉及

        :return: The transparent_client_ip_enable of this ListListenersRequest.
        :rtype: bool
        """
        return self._transparent_client_ip_enable

    @transparent_client_ip_enable.setter
    def transparent_client_ip_enable(self, transparent_client_ip_enable):
        r"""Sets the transparent_client_ip_enable of this ListListenersRequest.

        **参数解释**：是否开启后客户端IP地址将透传到后端服务器。 [仅作用于共享型LB的TCP/UDP监听器。](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)  **约束限制**：不涉及  **取值范围**：true开启，false不开启。  **默认取值**：不涉及

        :param transparent_client_ip_enable: The transparent_client_ip_enable of this ListListenersRequest.
        :type transparent_client_ip_enable: bool
        """
        self._transparent_client_ip_enable = transparent_client_ip_enable

    @property
    def proxy_protocol_enable(self):
        r"""Gets the proxy_protocol_enable of this ListListenersRequest.

        **参数解释**：是否开启proxy_protocol。  **约束限制**：不涉及  **取值范围**：true开启，false不开启。  **默认取值**：不涉及

        :return: The proxy_protocol_enable of this ListListenersRequest.
        :rtype: bool
        """
        return self._proxy_protocol_enable

    @proxy_protocol_enable.setter
    def proxy_protocol_enable(self, proxy_protocol_enable):
        r"""Sets the proxy_protocol_enable of this ListListenersRequest.

        **参数解释**：是否开启proxy_protocol。  **约束限制**：不涉及  **取值范围**：true开启，false不开启。  **默认取值**：不涉及

        :param proxy_protocol_enable: The proxy_protocol_enable of this ListListenersRequest.
        :type proxy_protocol_enable: bool
        """
        self._proxy_protocol_enable = proxy_protocol_enable

    @property
    def enhance_l7policy_enable(self):
        r"""Gets the enhance_l7policy_enable of this ListListenersRequest.

        **参数解释**：是否开启高级转发策略功能。开启高级转发策略后，支持更灵活的转发策略和转发规则设置。  **约束限制**：不涉及  **取值范围**：true开启，false不开启。  **默认取值**：不涉及  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The enhance_l7policy_enable of this ListListenersRequest.
        :rtype: bool
        """
        return self._enhance_l7policy_enable

    @enhance_l7policy_enable.setter
    def enhance_l7policy_enable(self, enhance_l7policy_enable):
        r"""Sets the enhance_l7policy_enable of this ListListenersRequest.

        **参数解释**：是否开启高级转发策略功能。开启高级转发策略后，支持更灵活的转发策略和转发规则设置。  **约束限制**：不涉及  **取值范围**：true开启，false不开启。  **默认取值**：不涉及  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param enhance_l7policy_enable: The enhance_l7policy_enable of this ListListenersRequest.
        :type enhance_l7policy_enable: bool
        """
        self._enhance_l7policy_enable = enhance_l7policy_enable

    @property
    def member_instance_id(self):
        r"""Gets the member_instance_id of this ListListenersRequest.

        **参数解释**：后端服务器ID。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_instance_id=xxx&member_instance_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The member_instance_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._member_instance_id

    @member_instance_id.setter
    def member_instance_id(self, member_instance_id):
        r"""Sets the member_instance_id of this ListListenersRequest.

        **参数解释**：后端服务器ID。仅用于查询条件，不作为响应参数字段。 支持多值查询，查询条件格式：*member_instance_id=xxx&member_instance_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param member_instance_id: The member_instance_id of this ListListenersRequest.
        :type member_instance_id: list[str]
        """
        self._member_instance_id = member_instance_id

    @property
    def protection_status(self):
        r"""Gets the protection_status of this ListListenersRequest.

        **参数解释**：修改保护状态。 支持多值查询，查询条件格式：*protection_status=xxx&protection_status=xxx*。  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护  **默认取值**：不涉及

        :return: The protection_status of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this ListListenersRequest.

        **参数解释**：修改保护状态。 支持多值查询，查询条件格式：*protection_status=xxx&protection_status=xxx*。  **约束限制**：不涉及  **取值范围**： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护  **默认取值**：不涉及

        :param protection_status: The protection_status of this ListListenersRequest.
        :type protection_status: list[str]
        """
        self._protection_status = protection_status

    @property
    def ssl_early_data_enable(self):
        r"""Gets the ssl_early_data_enable of this ListListenersRequest.

        **参数解释**：是否开启监听器0-RTT功能。  **约束限制**：不涉及  **取值范围**：true开启，false不开启。  **默认取值**：不涉及

        :return: The ssl_early_data_enable of this ListListenersRequest.
        :rtype: bool
        """
        return self._ssl_early_data_enable

    @ssl_early_data_enable.setter
    def ssl_early_data_enable(self, ssl_early_data_enable):
        r"""Sets the ssl_early_data_enable of this ListListenersRequest.

        **参数解释**：是否开启监听器0-RTT功能。  **约束限制**：不涉及  **取值范围**：true开启，false不开启。  **默认取值**：不涉及

        :param ssl_early_data_enable: The ssl_early_data_enable of this ListListenersRequest.
        :type ssl_early_data_enable: bool
        """
        self._ssl_early_data_enable = ssl_early_data_enable

    @property
    def nat64_enable(self):
        r"""Gets the nat64_enable of this ListListenersRequest.

        **参数解释**：是否开启nat64地址转换功能。  **约束限制**：不涉及  **取值范围**：true开启，false不开启。  **默认取值**：不涉及

        :return: The nat64_enable of this ListListenersRequest.
        :rtype: bool
        """
        return self._nat64_enable

    @nat64_enable.setter
    def nat64_enable(self, nat64_enable):
        r"""Sets the nat64_enable of this ListListenersRequest.

        **参数解释**：是否开启nat64地址转换功能。  **约束限制**：不涉及  **取值范围**：true开启，false不开启。  **默认取值**：不涉及

        :param nat64_enable: The nat64_enable of this ListListenersRequest.
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
        if not isinstance(other, ListListenersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
