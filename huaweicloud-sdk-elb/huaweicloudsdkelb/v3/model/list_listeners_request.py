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
        'protection_status': 'list[str]'
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
        'protection_status': 'protection_status'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, protocol_port=None, protocol=None, description=None, default_tls_container_ref=None, client_ca_tls_container_ref=None, admin_state_up=None, connection_limit=None, default_pool_id=None, id=None, name=None, http2_enable=None, loadbalancer_id=None, tls_ciphers_policy=None, member_address=None, member_device_id=None, enterprise_project_id=None, enable_member_retry=None, member_timeout=None, client_timeout=None, keepalive_timeout=None, transparent_client_ip_enable=None, proxy_protocol_enable=None, enhance_l7policy_enable=None, member_instance_id=None, protection_status=None):
        """ListListenersRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。
        :type limit: int
        :param marker: 上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。
        :type marker: str
        :param page_reverse: 是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。
        :type page_reverse: bool
        :param protocol_port: 监听器的前端监听端口。  支持多值查询，查询条件格式：*protocol_port&#x3D;xxx&amp;protocol_port&#x3D;xxx*。
        :type protocol_port: list[str]
        :param protocol: 监听器的监听协议。  [取值：TCP、UDP、HTTP、HTTPS、TERMINATED_HTTPS、QUIC。  说明：TERMINATED_HTTPS为共享型LB上的监听器独有的协议。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt)  [取值：TCP、UDP、HTTP、HTTPS。](tag:hws_eu,hcso_dt)  支持多值查询，查询条件格式：*protocol&#x3D;xxx&amp;protocol&#x3D;xxx*。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt,dt_test)
        :type protocol: list[str]
        :param description: 监听器的描述信息。  支持多值查询，查询条件格式：*description&#x3D;xxx&amp;description&#x3D;xxx*。
        :type description: list[str]
        :param default_tls_container_ref: 监听器的服务器证书ID。  支持多值查询，查询条件格式： *default_tls_container_ref&#x3D;xxx&amp;default_tls_container_ref&#x3D;xxx*。
        :type default_tls_container_ref: list[str]
        :param client_ca_tls_container_ref: 监听器的CA证书ID。  支持多值查询，查询条件格式： *client_ca_tls_container_ref&#x3D;xxx&amp;client_ca_tls_container_ref&#x3D;xxx*。
        :type client_ca_tls_container_ref: list[str]
        :param admin_state_up: 监听器的管理状态，只能设置为true。  不支持该字段，请勿使用。
        :type admin_state_up: bool
        :param connection_limit: ​监听器的最大连接数。  取值：-1表示不限制连接数。  支持多值查询，查询条件格式：*connection_limit&#x3D;xxx&amp;connection_limit&#x3D;xxx*。  不支持该字段，请勿使用。
        :type connection_limit: list[int]
        :param default_pool_id: 监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。  支持多值查询，查询条件格式：*default_pool_id&#x3D;xxx&amp;default_pool_id&#x3D;xxx*。
        :type default_pool_id: list[str]
        :param id: 监听器ID。  支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx*。
        :type id: list[str]
        :param name: 监听器名称。  支持多值查询，查询条件格式：*name&#x3D;xxx&amp;name&#x3D;xxx*。
        :type name: list[str]
        :param http2_enable: 客户端与LB之间的HTTPS请求的HTTP2功能的开启状态。 开启后，可提升客户端与LB间的访问性能，但LB与后端服务器间仍采用HTTP1.X协议。  使用说明： - 仅HTTPS协议监听器有效。 - QUIC监听器不能设置该字段，固定返回为true。 - 其他协议的监听器可设置该字段但无效，无论取值如何都不影响监听器正常运行。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt,dt_test)
        :type http2_enable: bool
        :param loadbalancer_id: 监听器所属的负载均衡器ID。  支持多值查询，查询条件格式：*loadbalancer_id&#x3D;xxx&amp;loadbalancer_id&#x3D;xxx*。
        :type loadbalancer_id: list[str]
        :param tls_ciphers_policy: 监听器使用的安全策略。  支持多值查询，查询条件格式：*tls_ciphers_policy&#x3D;xxx&amp;tls_ciphers_policy&#x3D;xxx*。
        :type tls_ciphers_policy: list[str]
        :param member_address: 后端云服务器的IP地址。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_address&#x3D;xxx&amp;member_address&#x3D;xxx*。
        :type member_address: list[str]
        :param member_device_id: 后端云服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_device_id&#x3D;xxx&amp;member_device_id&#x3D;xxx*。
        :type member_device_id: list[str]
        :param enterprise_project_id: 企业项目ID。不传时查询default企业项目\&quot;0\&quot;下的资源，鉴权按照default企业项目鉴权； 如果传值，则传已存在的企业项目ID或all_granted_eps（表示查询所有企业项目）进行查询。  支持多值查询，查询条件格式：*enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)
        :type enterprise_project_id: list[str]
        :param enable_member_retry: 是否开启后端服务器的重试。  取值：true 开启重试，false 不开启重试。
        :type enable_member_retry: bool
        :param member_timeout: 等待后端服务器响应超时时间。请求转发后端服务器后，在等待超时member_timeout时长没有响应，负载均衡将终止等待，并返回 HTTP504错误码。  取值：1-300s。  支持多值查询，查询条件格式：*member_timeout&#x3D;xxx&amp;member_timeout&#x3D;xxx*。
        :type member_timeout: list[int]
        :param client_timeout: 等待客户端请求超时时间，包括两种情况： - 读取整个客户端请求头的超时时长：如果客户端未在超时时长内发送完整个请求头，则请求将被中断 - 两个连续body体的数据包到达LB的时间间隔，超出client_timeout将会断开连接。  取值：1-300s。  支持多值查询，查询条件格式：*client_timeout&#x3D;xxx&amp;client_timeout&#x3D;xxx*。
        :type client_timeout: list[int]
        :param keepalive_timeout: 客户端连接空闲超时时间。在超过keepalive_timeout时长一直没有请求， 负载均衡会暂时中断当前连接，直到下一次请求时重新建立新的连接。  取值： - TCP监听器：10-4000s。 - HTTP/HTTPS/TERMINATED_HTTPS监听器：0-4000s。 - 共享型实例的UDP监听器不支持此字段。  支持多值查询，查询条件格式：*keepalive_timeout&#x3D;xxx&amp;keepalive_timeout&#x3D;xxx*。
        :type keepalive_timeout: list[int]
        :param transparent_client_ip_enable: 是否透传客户端IP地址。开启后客户端IP地址将透传到后端服务器。  [仅作用于共享型LB的TCP/UDP监听器。取值：true开启，false不开启。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)
        :type transparent_client_ip_enable: bool
        :param proxy_protocol_enable: 是否开启proxy_protocol。仅tcpssl监听器可指定，其他协议的监听器该字段不生效，proxy_protocol不开启。
        :type proxy_protocol_enable: bool
        :param enhance_l7policy_enable: 是否开启高级转发策略功能。开启高级转发策略后，支持更灵活的转发策略和转发规则设置。  取值：true开启，false不开启。  [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type enhance_l7policy_enable: bool
        :param member_instance_id: 后端云服务器ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_instance_id&#x3D;xxx&amp;member_instance_id&#x3D;xxx*。
        :type member_instance_id: list[str]
        :param protection_status: 修改保护状态, 取值： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护
        :type protection_status: list[str]
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

    @property
    def limit(self):
        """Gets the limit of this ListListenersRequest.

        每页返回的个数。

        :return: The limit of this ListListenersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListListenersRequest.

        每页返回的个数。

        :param limit: The limit of this ListListenersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListListenersRequest.

        上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :return: The marker of this ListListenersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListListenersRequest.

        上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :param marker: The marker of this ListListenersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListListenersRequest.

        是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。

        :return: The page_reverse of this ListListenersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListListenersRequest.

        是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。

        :param page_reverse: The page_reverse of this ListListenersRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def protocol_port(self):
        """Gets the protocol_port of this ListListenersRequest.

        监听器的前端监听端口。  支持多值查询，查询条件格式：*protocol_port=xxx&protocol_port=xxx*。

        :return: The protocol_port of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this ListListenersRequest.

        监听器的前端监听端口。  支持多值查询，查询条件格式：*protocol_port=xxx&protocol_port=xxx*。

        :param protocol_port: The protocol_port of this ListListenersRequest.
        :type protocol_port: list[str]
        """
        self._protocol_port = protocol_port

    @property
    def protocol(self):
        """Gets the protocol of this ListListenersRequest.

        监听器的监听协议。  [取值：TCP、UDP、HTTP、HTTPS、TERMINATED_HTTPS、QUIC。  说明：TERMINATED_HTTPS为共享型LB上的监听器独有的协议。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt)  [取值：TCP、UDP、HTTP、HTTPS。](tag:hws_eu,hcso_dt)  支持多值查询，查询条件格式：*protocol=xxx&protocol=xxx*。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt,dt_test)

        :return: The protocol of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListListenersRequest.

        监听器的监听协议。  [取值：TCP、UDP、HTTP、HTTPS、TERMINATED_HTTPS、QUIC。  说明：TERMINATED_HTTPS为共享型LB上的监听器独有的协议。 ](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt)  [取值：TCP、UDP、HTTP、HTTPS。](tag:hws_eu,hcso_dt)  支持多值查询，查询条件格式：*protocol=xxx&protocol=xxx*。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt,dt_test)

        :param protocol: The protocol of this ListListenersRequest.
        :type protocol: list[str]
        """
        self._protocol = protocol

    @property
    def description(self):
        """Gets the description of this ListListenersRequest.

        监听器的描述信息。  支持多值查询，查询条件格式：*description=xxx&description=xxx*。

        :return: The description of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListListenersRequest.

        监听器的描述信息。  支持多值查询，查询条件格式：*description=xxx&description=xxx*。

        :param description: The description of this ListListenersRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def default_tls_container_ref(self):
        """Gets the default_tls_container_ref of this ListListenersRequest.

        监听器的服务器证书ID。  支持多值查询，查询条件格式： *default_tls_container_ref=xxx&default_tls_container_ref=xxx*。

        :return: The default_tls_container_ref of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        """Sets the default_tls_container_ref of this ListListenersRequest.

        监听器的服务器证书ID。  支持多值查询，查询条件格式： *default_tls_container_ref=xxx&default_tls_container_ref=xxx*。

        :param default_tls_container_ref: The default_tls_container_ref of this ListListenersRequest.
        :type default_tls_container_ref: list[str]
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def client_ca_tls_container_ref(self):
        """Gets the client_ca_tls_container_ref of this ListListenersRequest.

        监听器的CA证书ID。  支持多值查询，查询条件格式： *client_ca_tls_container_ref=xxx&client_ca_tls_container_ref=xxx*。

        :return: The client_ca_tls_container_ref of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        """Sets the client_ca_tls_container_ref of this ListListenersRequest.

        监听器的CA证书ID。  支持多值查询，查询条件格式： *client_ca_tls_container_ref=xxx&client_ca_tls_container_ref=xxx*。

        :param client_ca_tls_container_ref: The client_ca_tls_container_ref of this ListListenersRequest.
        :type client_ca_tls_container_ref: list[str]
        """
        self._client_ca_tls_container_ref = client_ca_tls_container_ref

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListListenersRequest.

        监听器的管理状态，只能设置为true。  不支持该字段，请勿使用。

        :return: The admin_state_up of this ListListenersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListListenersRequest.

        监听器的管理状态，只能设置为true。  不支持该字段，请勿使用。

        :param admin_state_up: The admin_state_up of this ListListenersRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def connection_limit(self):
        """Gets the connection_limit of this ListListenersRequest.

        ​监听器的最大连接数。  取值：-1表示不限制连接数。  支持多值查询，查询条件格式：*connection_limit=xxx&connection_limit=xxx*。  不支持该字段，请勿使用。

        :return: The connection_limit of this ListListenersRequest.
        :rtype: list[int]
        """
        return self._connection_limit

    @connection_limit.setter
    def connection_limit(self, connection_limit):
        """Sets the connection_limit of this ListListenersRequest.

        ​监听器的最大连接数。  取值：-1表示不限制连接数。  支持多值查询，查询条件格式：*connection_limit=xxx&connection_limit=xxx*。  不支持该字段，请勿使用。

        :param connection_limit: The connection_limit of this ListListenersRequest.
        :type connection_limit: list[int]
        """
        self._connection_limit = connection_limit

    @property
    def default_pool_id(self):
        """Gets the default_pool_id of this ListListenersRequest.

        监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。  支持多值查询，查询条件格式：*default_pool_id=xxx&default_pool_id=xxx*。

        :return: The default_pool_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._default_pool_id

    @default_pool_id.setter
    def default_pool_id(self, default_pool_id):
        """Sets the default_pool_id of this ListListenersRequest.

        监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。  支持多值查询，查询条件格式：*default_pool_id=xxx&default_pool_id=xxx*。

        :param default_pool_id: The default_pool_id of this ListListenersRequest.
        :type default_pool_id: list[str]
        """
        self._default_pool_id = default_pool_id

    @property
    def id(self):
        """Gets the id of this ListListenersRequest.

        监听器ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx*。

        :return: The id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListListenersRequest.

        监听器ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx*。

        :param id: The id of this ListListenersRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListListenersRequest.

        监听器名称。  支持多值查询，查询条件格式：*name=xxx&name=xxx*。

        :return: The name of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListListenersRequest.

        监听器名称。  支持多值查询，查询条件格式：*name=xxx&name=xxx*。

        :param name: The name of this ListListenersRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def http2_enable(self):
        """Gets the http2_enable of this ListListenersRequest.

        客户端与LB之间的HTTPS请求的HTTP2功能的开启状态。 开启后，可提升客户端与LB间的访问性能，但LB与后端服务器间仍采用HTTP1.X协议。  使用说明： - 仅HTTPS协议监听器有效。 - QUIC监听器不能设置该字段，固定返回为true。 - 其他协议的监听器可设置该字段但无效，无论取值如何都不影响监听器正常运行。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt,dt_test)

        :return: The http2_enable of this ListListenersRequest.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this ListListenersRequest.

        客户端与LB之间的HTTPS请求的HTTP2功能的开启状态。 开启后，可提升客户端与LB间的访问性能，但LB与后端服务器间仍采用HTTP1.X协议。  使用说明： - 仅HTTPS协议监听器有效。 - QUIC监听器不能设置该字段，固定返回为true。 - 其他协议的监听器可设置该字段但无效，无论取值如何都不影响监听器正常运行。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt,dt,dt_test)

        :param http2_enable: The http2_enable of this ListListenersRequest.
        :type http2_enable: bool
        """
        self._http2_enable = http2_enable

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this ListListenersRequest.

        监听器所属的负载均衡器ID。  支持多值查询，查询条件格式：*loadbalancer_id=xxx&loadbalancer_id=xxx*。

        :return: The loadbalancer_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this ListListenersRequest.

        监听器所属的负载均衡器ID。  支持多值查询，查询条件格式：*loadbalancer_id=xxx&loadbalancer_id=xxx*。

        :param loadbalancer_id: The loadbalancer_id of this ListListenersRequest.
        :type loadbalancer_id: list[str]
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def tls_ciphers_policy(self):
        """Gets the tls_ciphers_policy of this ListListenersRequest.

        监听器使用的安全策略。  支持多值查询，查询条件格式：*tls_ciphers_policy=xxx&tls_ciphers_policy=xxx*。

        :return: The tls_ciphers_policy of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._tls_ciphers_policy

    @tls_ciphers_policy.setter
    def tls_ciphers_policy(self, tls_ciphers_policy):
        """Sets the tls_ciphers_policy of this ListListenersRequest.

        监听器使用的安全策略。  支持多值查询，查询条件格式：*tls_ciphers_policy=xxx&tls_ciphers_policy=xxx*。

        :param tls_ciphers_policy: The tls_ciphers_policy of this ListListenersRequest.
        :type tls_ciphers_policy: list[str]
        """
        self._tls_ciphers_policy = tls_ciphers_policy

    @property
    def member_address(self):
        """Gets the member_address of this ListListenersRequest.

        后端云服务器的IP地址。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_address=xxx&member_address=xxx*。

        :return: The member_address of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._member_address

    @member_address.setter
    def member_address(self, member_address):
        """Sets the member_address of this ListListenersRequest.

        后端云服务器的IP地址。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_address=xxx&member_address=xxx*。

        :param member_address: The member_address of this ListListenersRequest.
        :type member_address: list[str]
        """
        self._member_address = member_address

    @property
    def member_device_id(self):
        """Gets the member_device_id of this ListListenersRequest.

        后端云服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_device_id=xxx&member_device_id=xxx*。

        :return: The member_device_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._member_device_id

    @member_device_id.setter
    def member_device_id(self, member_device_id):
        """Sets the member_device_id of this ListListenersRequest.

        后端云服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_device_id=xxx&member_device_id=xxx*。

        :param member_device_id: The member_device_id of this ListListenersRequest.
        :type member_device_id: list[str]
        """
        self._member_device_id = member_device_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListListenersRequest.

        企业项目ID。不传时查询default企业项目\"0\"下的资源，鉴权按照default企业项目鉴权； 如果传值，则传已存在的企业项目ID或all_granted_eps（表示查询所有企业项目）进行查询。  支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :return: The enterprise_project_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListListenersRequest.

        企业项目ID。不传时查询default企业项目\"0\"下的资源，鉴权按照default企业项目鉴权； 如果传值，则传已存在的企业项目ID或all_granted_eps（表示查询所有企业项目）进行查询。  支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this ListListenersRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enable_member_retry(self):
        """Gets the enable_member_retry of this ListListenersRequest.

        是否开启后端服务器的重试。  取值：true 开启重试，false 不开启重试。

        :return: The enable_member_retry of this ListListenersRequest.
        :rtype: bool
        """
        return self._enable_member_retry

    @enable_member_retry.setter
    def enable_member_retry(self, enable_member_retry):
        """Sets the enable_member_retry of this ListListenersRequest.

        是否开启后端服务器的重试。  取值：true 开启重试，false 不开启重试。

        :param enable_member_retry: The enable_member_retry of this ListListenersRequest.
        :type enable_member_retry: bool
        """
        self._enable_member_retry = enable_member_retry

    @property
    def member_timeout(self):
        """Gets the member_timeout of this ListListenersRequest.

        等待后端服务器响应超时时间。请求转发后端服务器后，在等待超时member_timeout时长没有响应，负载均衡将终止等待，并返回 HTTP504错误码。  取值：1-300s。  支持多值查询，查询条件格式：*member_timeout=xxx&member_timeout=xxx*。

        :return: The member_timeout of this ListListenersRequest.
        :rtype: list[int]
        """
        return self._member_timeout

    @member_timeout.setter
    def member_timeout(self, member_timeout):
        """Sets the member_timeout of this ListListenersRequest.

        等待后端服务器响应超时时间。请求转发后端服务器后，在等待超时member_timeout时长没有响应，负载均衡将终止等待，并返回 HTTP504错误码。  取值：1-300s。  支持多值查询，查询条件格式：*member_timeout=xxx&member_timeout=xxx*。

        :param member_timeout: The member_timeout of this ListListenersRequest.
        :type member_timeout: list[int]
        """
        self._member_timeout = member_timeout

    @property
    def client_timeout(self):
        """Gets the client_timeout of this ListListenersRequest.

        等待客户端请求超时时间，包括两种情况： - 读取整个客户端请求头的超时时长：如果客户端未在超时时长内发送完整个请求头，则请求将被中断 - 两个连续body体的数据包到达LB的时间间隔，超出client_timeout将会断开连接。  取值：1-300s。  支持多值查询，查询条件格式：*client_timeout=xxx&client_timeout=xxx*。

        :return: The client_timeout of this ListListenersRequest.
        :rtype: list[int]
        """
        return self._client_timeout

    @client_timeout.setter
    def client_timeout(self, client_timeout):
        """Sets the client_timeout of this ListListenersRequest.

        等待客户端请求超时时间，包括两种情况： - 读取整个客户端请求头的超时时长：如果客户端未在超时时长内发送完整个请求头，则请求将被中断 - 两个连续body体的数据包到达LB的时间间隔，超出client_timeout将会断开连接。  取值：1-300s。  支持多值查询，查询条件格式：*client_timeout=xxx&client_timeout=xxx*。

        :param client_timeout: The client_timeout of this ListListenersRequest.
        :type client_timeout: list[int]
        """
        self._client_timeout = client_timeout

    @property
    def keepalive_timeout(self):
        """Gets the keepalive_timeout of this ListListenersRequest.

        客户端连接空闲超时时间。在超过keepalive_timeout时长一直没有请求， 负载均衡会暂时中断当前连接，直到下一次请求时重新建立新的连接。  取值： - TCP监听器：10-4000s。 - HTTP/HTTPS/TERMINATED_HTTPS监听器：0-4000s。 - 共享型实例的UDP监听器不支持此字段。  支持多值查询，查询条件格式：*keepalive_timeout=xxx&keepalive_timeout=xxx*。

        :return: The keepalive_timeout of this ListListenersRequest.
        :rtype: list[int]
        """
        return self._keepalive_timeout

    @keepalive_timeout.setter
    def keepalive_timeout(self, keepalive_timeout):
        """Sets the keepalive_timeout of this ListListenersRequest.

        客户端连接空闲超时时间。在超过keepalive_timeout时长一直没有请求， 负载均衡会暂时中断当前连接，直到下一次请求时重新建立新的连接。  取值： - TCP监听器：10-4000s。 - HTTP/HTTPS/TERMINATED_HTTPS监听器：0-4000s。 - 共享型实例的UDP监听器不支持此字段。  支持多值查询，查询条件格式：*keepalive_timeout=xxx&keepalive_timeout=xxx*。

        :param keepalive_timeout: The keepalive_timeout of this ListListenersRequest.
        :type keepalive_timeout: list[int]
        """
        self._keepalive_timeout = keepalive_timeout

    @property
    def transparent_client_ip_enable(self):
        """Gets the transparent_client_ip_enable of this ListListenersRequest.

        是否透传客户端IP地址。开启后客户端IP地址将透传到后端服务器。  [仅作用于共享型LB的TCP/UDP监听器。取值：true开启，false不开启。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)

        :return: The transparent_client_ip_enable of this ListListenersRequest.
        :rtype: bool
        """
        return self._transparent_client_ip_enable

    @transparent_client_ip_enable.setter
    def transparent_client_ip_enable(self, transparent_client_ip_enable):
        """Sets the transparent_client_ip_enable of this ListListenersRequest.

        是否透传客户端IP地址。开启后客户端IP地址将透传到后端服务器。  [仅作用于共享型LB的TCP/UDP监听器。取值：true开启，false不开启。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)

        :param transparent_client_ip_enable: The transparent_client_ip_enable of this ListListenersRequest.
        :type transparent_client_ip_enable: bool
        """
        self._transparent_client_ip_enable = transparent_client_ip_enable

    @property
    def proxy_protocol_enable(self):
        """Gets the proxy_protocol_enable of this ListListenersRequest.

        是否开启proxy_protocol。仅tcpssl监听器可指定，其他协议的监听器该字段不生效，proxy_protocol不开启。

        :return: The proxy_protocol_enable of this ListListenersRequest.
        :rtype: bool
        """
        return self._proxy_protocol_enable

    @proxy_protocol_enable.setter
    def proxy_protocol_enable(self, proxy_protocol_enable):
        """Sets the proxy_protocol_enable of this ListListenersRequest.

        是否开启proxy_protocol。仅tcpssl监听器可指定，其他协议的监听器该字段不生效，proxy_protocol不开启。

        :param proxy_protocol_enable: The proxy_protocol_enable of this ListListenersRequest.
        :type proxy_protocol_enable: bool
        """
        self._proxy_protocol_enable = proxy_protocol_enable

    @property
    def enhance_l7policy_enable(self):
        """Gets the enhance_l7policy_enable of this ListListenersRequest.

        是否开启高级转发策略功能。开启高级转发策略后，支持更灵活的转发策略和转发规则设置。  取值：true开启，false不开启。  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The enhance_l7policy_enable of this ListListenersRequest.
        :rtype: bool
        """
        return self._enhance_l7policy_enable

    @enhance_l7policy_enable.setter
    def enhance_l7policy_enable(self, enhance_l7policy_enable):
        """Sets the enhance_l7policy_enable of this ListListenersRequest.

        是否开启高级转发策略功能。开启高级转发策略后，支持更灵活的转发策略和转发规则设置。  取值：true开启，false不开启。  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param enhance_l7policy_enable: The enhance_l7policy_enable of this ListListenersRequest.
        :type enhance_l7policy_enable: bool
        """
        self._enhance_l7policy_enable = enhance_l7policy_enable

    @property
    def member_instance_id(self):
        """Gets the member_instance_id of this ListListenersRequest.

        后端云服务器ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_instance_id=xxx&member_instance_id=xxx*。

        :return: The member_instance_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._member_instance_id

    @member_instance_id.setter
    def member_instance_id(self, member_instance_id):
        """Sets the member_instance_id of this ListListenersRequest.

        后端云服务器ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_instance_id=xxx&member_instance_id=xxx*。

        :param member_instance_id: The member_instance_id of this ListListenersRequest.
        :type member_instance_id: list[str]
        """
        self._member_instance_id = member_instance_id

    @property
    def protection_status(self):
        """Gets the protection_status of this ListListenersRequest.

        修改保护状态, 取值： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护

        :return: The protection_status of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        """Sets the protection_status of this ListListenersRequest.

        修改保护状态, 取值： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护

        :param protection_status: The protection_status of this ListListenersRequest.
        :type protection_status: list[str]
        """
        self._protection_status = protection_status

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
