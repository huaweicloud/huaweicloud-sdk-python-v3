# coding: utf-8

import re
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
        'admin_state_up': 'bool',
        'client_ca_tls_container_ref': 'list[str]',
        'client_timeout': 'list[int]',
        'connection_limit': 'list[int]',
        'default_pool_id': 'list[str]',
        'default_tls_container_ref': 'list[str]',
        'description': 'list[str]',
        'enable_member_retry': 'bool',
        'enterprise_project_id': 'list[str]',
        'http2_enable': 'bool',
        'id': 'list[str]',
        'keepalive_timeout': 'list[int]',
        'limit': 'int',
        'loadbalancer_id': 'list[str]',
        'marker': 'str',
        'member_address': 'list[str]',
        'member_device_id': 'list[str]',
        'member_timeout': 'list[int]',
        'name': 'list[str]',
        'page_reverse': 'bool',
        'protocol': 'list[str]',
        'protocol_port': 'list[str]',
        'tls_ciphers_policy': 'list[str]',
        'transparent_client_ip_enable': 'bool'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'client_ca_tls_container_ref': 'client_ca_tls_container_ref',
        'client_timeout': 'client_timeout',
        'connection_limit': 'connection_limit',
        'default_pool_id': 'default_pool_id',
        'default_tls_container_ref': 'default_tls_container_ref',
        'description': 'description',
        'enable_member_retry': 'enable_member_retry',
        'enterprise_project_id': 'enterprise_project_id',
        'http2_enable': 'http2_enable',
        'id': 'id',
        'keepalive_timeout': 'keepalive_timeout',
        'limit': 'limit',
        'loadbalancer_id': 'loadbalancer_id',
        'marker': 'marker',
        'member_address': 'member_address',
        'member_device_id': 'member_device_id',
        'member_timeout': 'member_timeout',
        'name': 'name',
        'page_reverse': 'page_reverse',
        'protocol': 'protocol',
        'protocol_port': 'protocol_port',
        'tls_ciphers_policy': 'tls_ciphers_policy',
        'transparent_client_ip_enable': 'transparent_client_ip_enable'
    }

    def __init__(self, admin_state_up=None, client_ca_tls_container_ref=None, client_timeout=None, connection_limit=None, default_pool_id=None, default_tls_container_ref=None, description=None, enable_member_retry=None, enterprise_project_id=None, http2_enable=None, id=None, keepalive_timeout=None, limit=None, loadbalancer_id=None, marker=None, member_address=None, member_device_id=None, member_timeout=None, name=None, page_reverse=None, protocol=None, protocol_port=None, tls_ciphers_policy=None, transparent_client_ip_enable=None):
        """ListListenersRequest - a model defined in huaweicloud sdk"""
        
        

        self._admin_state_up = None
        self._client_ca_tls_container_ref = None
        self._client_timeout = None
        self._connection_limit = None
        self._default_pool_id = None
        self._default_tls_container_ref = None
        self._description = None
        self._enable_member_retry = None
        self._enterprise_project_id = None
        self._http2_enable = None
        self._id = None
        self._keepalive_timeout = None
        self._limit = None
        self._loadbalancer_id = None
        self._marker = None
        self._member_address = None
        self._member_device_id = None
        self._member_timeout = None
        self._name = None
        self._page_reverse = None
        self._protocol = None
        self._protocol_port = None
        self._tls_ciphers_policy = None
        self._transparent_client_ip_enable = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if client_ca_tls_container_ref is not None:
            self.client_ca_tls_container_ref = client_ca_tls_container_ref
        if client_timeout is not None:
            self.client_timeout = client_timeout
        if connection_limit is not None:
            self.connection_limit = connection_limit
        if default_pool_id is not None:
            self.default_pool_id = default_pool_id
        if default_tls_container_ref is not None:
            self.default_tls_container_ref = default_tls_container_ref
        if description is not None:
            self.description = description
        if enable_member_retry is not None:
            self.enable_member_retry = enable_member_retry
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if http2_enable is not None:
            self.http2_enable = http2_enable
        if id is not None:
            self.id = id
        if keepalive_timeout is not None:
            self.keepalive_timeout = keepalive_timeout
        if limit is not None:
            self.limit = limit
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if marker is not None:
            self.marker = marker
        if member_address is not None:
            self.member_address = member_address
        if member_device_id is not None:
            self.member_device_id = member_device_id
        if member_timeout is not None:
            self.member_timeout = member_timeout
        if name is not None:
            self.name = name
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if protocol is not None:
            self.protocol = protocol
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if tls_ciphers_policy is not None:
            self.tls_ciphers_policy = tls_ciphers_policy
        if transparent_client_ip_enable is not None:
            self.transparent_client_ip_enable = transparent_client_ip_enable

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListListenersRequest.

        监听器的管理状态。只支持设定为true，该字段的值无实际意义。

        :return: The admin_state_up of this ListListenersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListListenersRequest.

        监听器的管理状态。只支持设定为true，该字段的值无实际意义。

        :param admin_state_up: The admin_state_up of this ListListenersRequest.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def client_ca_tls_container_ref(self):
        """Gets the client_ca_tls_container_ref of this ListListenersRequest.

        监听器使用的CA证书ID。

        :return: The client_ca_tls_container_ref of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        """Sets the client_ca_tls_container_ref of this ListListenersRequest.

        监听器使用的CA证书ID。

        :param client_ca_tls_container_ref: The client_ca_tls_container_ref of this ListListenersRequest.
        :type: list[str]
        """
        self._client_ca_tls_container_ref = client_ca_tls_container_ref

    @property
    def client_timeout(self):
        """Gets the client_timeout of this ListListenersRequest.

        等待客户端请求超时时间，协议为HTTP， TERMINATED_HTTPS的监听器才有意义。取值范围 1-60

        :return: The client_timeout of this ListListenersRequest.
        :rtype: list[int]
        """
        return self._client_timeout

    @client_timeout.setter
    def client_timeout(self, client_timeout):
        """Sets the client_timeout of this ListListenersRequest.

        等待客户端请求超时时间，协议为HTTP， TERMINATED_HTTPS的监听器才有意义。取值范围 1-60

        :param client_timeout: The client_timeout of this ListListenersRequest.
        :type: list[int]
        """
        self._client_timeout = client_timeout

    @property
    def connection_limit(self):
        """Gets the connection_limit of this ListListenersRequest.

        监听器的最大连接数。该字段为预留字段，暂未启用。默认为-1。

        :return: The connection_limit of this ListListenersRequest.
        :rtype: list[int]
        """
        return self._connection_limit

    @connection_limit.setter
    def connection_limit(self, connection_limit):
        """Sets the connection_limit of this ListListenersRequest.

        监听器的最大连接数。该字段为预留字段，暂未启用。默认为-1。

        :param connection_limit: The connection_limit of this ListListenersRequest.
        :type: list[int]
        """
        self._connection_limit = connection_limit

    @property
    def default_pool_id(self):
        """Gets the default_pool_id of this ListListenersRequest.

        监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。

        :return: The default_pool_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._default_pool_id

    @default_pool_id.setter
    def default_pool_id(self, default_pool_id):
        """Sets the default_pool_id of this ListListenersRequest.

        监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。

        :param default_pool_id: The default_pool_id of this ListListenersRequest.
        :type: list[str]
        """
        self._default_pool_id = default_pool_id

    @property
    def default_tls_container_ref(self):
        """Gets the default_tls_container_ref of this ListListenersRequest.

        监听器使用的服务器证书ID。

        :return: The default_tls_container_ref of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        """Sets the default_tls_container_ref of this ListListenersRequest.

        监听器使用的服务器证书ID。

        :param default_tls_container_ref: The default_tls_container_ref of this ListListenersRequest.
        :type: list[str]
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def description(self):
        """Gets the description of this ListListenersRequest.

        监听器的描述信息。

        :return: The description of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListListenersRequest.

        监听器的描述信息。

        :param description: The description of this ListListenersRequest.
        :type: list[str]
        """
        self._description = description

    @property
    def enable_member_retry(self):
        """Gets the enable_member_retry of this ListListenersRequest.

        后端重试探测的开关

        :return: The enable_member_retry of this ListListenersRequest.
        :rtype: bool
        """
        return self._enable_member_retry

    @enable_member_retry.setter
    def enable_member_retry(self, enable_member_retry):
        """Sets the enable_member_retry of this ListListenersRequest.

        后端重试探测的开关

        :param enable_member_retry: The enable_member_retry of this ListListenersRequest.
        :type: bool
        """
        self._enable_member_retry = enable_member_retry

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListListenersRequest.

        企业项目ID。

        :return: The enterprise_project_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListListenersRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListListenersRequest.
        :type: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def http2_enable(self):
        """Gets the http2_enable of this ListListenersRequest.

        HTTP2功能的开启状态。该字段只有当监听器的协议是TERMINATED_HTTPS时生效。

        :return: The http2_enable of this ListListenersRequest.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this ListListenersRequest.

        HTTP2功能的开启状态。该字段只有当监听器的协议是TERMINATED_HTTPS时生效。

        :param http2_enable: The http2_enable of this ListListenersRequest.
        :type: bool
        """
        self._http2_enable = http2_enable

    @property
    def id(self):
        """Gets the id of this ListListenersRequest.

        监听器ID。

        :return: The id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListListenersRequest.

        监听器ID。

        :param id: The id of this ListListenersRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def keepalive_timeout(self):
        """Gets the keepalive_timeout of this ListListenersRequest.

        TCP监听器配置空闲超时时间，取值范围为（10-900s）默认值为300s，TCP监听器配置空闲超时时间，取值范围为（10-900s）默认值为300s，HTTP/TERMINATED_HTTPS监听器为客户端连接空闲超时时间，取值范围为（1-300s）默认值为15s。 UDP此字段无意义

        :return: The keepalive_timeout of this ListListenersRequest.
        :rtype: list[int]
        """
        return self._keepalive_timeout

    @keepalive_timeout.setter
    def keepalive_timeout(self, keepalive_timeout):
        """Sets the keepalive_timeout of this ListListenersRequest.

        TCP监听器配置空闲超时时间，取值范围为（10-900s）默认值为300s，TCP监听器配置空闲超时时间，取值范围为（10-900s）默认值为300s，HTTP/TERMINATED_HTTPS监听器为客户端连接空闲超时时间，取值范围为（1-300s）默认值为15s。 UDP此字段无意义

        :param keepalive_timeout: The keepalive_timeout of this ListListenersRequest.
        :type: list[int]
        """
        self._keepalive_timeout = keepalive_timeout

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
        :type: int
        """
        self._limit = limit

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this ListListenersRequest.

        监听器绑定的负载均衡器ID。

        :return: The loadbalancer_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this ListListenersRequest.

        监听器绑定的负载均衡器ID。

        :param loadbalancer_id: The loadbalancer_id of this ListListenersRequest.
        :type: list[str]
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def marker(self):
        """Gets the marker of this ListListenersRequest.

        上一页最后一条记录的ID。  使用说明：  - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :return: The marker of this ListListenersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListListenersRequest.

        上一页最后一条记录的ID。  使用说明：  - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :param marker: The marker of this ListListenersRequest.
        :type: str
        """
        self._marker = marker

    @property
    def member_address(self):
        """Gets the member_address of this ListListenersRequest.

        后端云服务器的IP地址。

        :return: The member_address of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._member_address

    @member_address.setter
    def member_address(self, member_address):
        """Sets the member_address of this ListListenersRequest.

        后端云服务器的IP地址。

        :param member_address: The member_address of this ListListenersRequest.
        :type: list[str]
        """
        self._member_address = member_address

    @property
    def member_device_id(self):
        """Gets the member_device_id of this ListListenersRequest.

        后端云服务器对应的弹性云服务器的ID。

        :return: The member_device_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._member_device_id

    @member_device_id.setter
    def member_device_id(self, member_device_id):
        """Sets the member_device_id of this ListListenersRequest.

        后端云服务器对应的弹性云服务器的ID。

        :param member_device_id: The member_device_id of this ListListenersRequest.
        :type: list[str]
        """
        self._member_device_id = member_device_id

    @property
    def member_timeout(self):
        """Gets the member_timeout of this ListListenersRequest.

        等待后端服务器请求超时时间，协议为HTTP， TERMINATED_HTTPS时才有意义。取值范围 1-300

        :return: The member_timeout of this ListListenersRequest.
        :rtype: list[int]
        """
        return self._member_timeout

    @member_timeout.setter
    def member_timeout(self, member_timeout):
        """Sets the member_timeout of this ListListenersRequest.

        等待后端服务器请求超时时间，协议为HTTP， TERMINATED_HTTPS时才有意义。取值范围 1-300

        :param member_timeout: The member_timeout of this ListListenersRequest.
        :type: list[int]
        """
        self._member_timeout = member_timeout

    @property
    def name(self):
        """Gets the name of this ListListenersRequest.

        监听器名称。

        :return: The name of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListListenersRequest.

        监听器名称。

        :param name: The name of this ListListenersRequest.
        :type: list[str]
        """
        self._name = name

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListListenersRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。 使用说明：必须与limit一起使用。

        :return: The page_reverse of this ListListenersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListListenersRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。 使用说明：必须与limit一起使用。

        :param page_reverse: The page_reverse of this ListListenersRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def protocol(self):
        """Gets the protocol of this ListListenersRequest.

        监听器的监听协议。 取值：UDP,TCP,HTTP,TERMINATED_HTTPS。

        :return: The protocol of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListListenersRequest.

        监听器的监听协议。 取值：UDP,TCP,HTTP,TERMINATED_HTTPS。

        :param protocol: The protocol of this ListListenersRequest.
        :type: list[str]
        """
        self._protocol = protocol

    @property
    def protocol_port(self):
        """Gets the protocol_port of this ListListenersRequest.

        监听器的监听端口。

        :return: The protocol_port of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this ListListenersRequest.

        监听器的监听端口。

        :param protocol_port: The protocol_port of this ListListenersRequest.
        :type: list[str]
        """
        self._protocol_port = protocol_port

    @property
    def tls_ciphers_policy(self):
        """Gets the tls_ciphers_policy of this ListListenersRequest.

        监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效，且默认值为tls-1-0。 取值包括：tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict四种安全策略。

        :return: The tls_ciphers_policy of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._tls_ciphers_policy

    @tls_ciphers_policy.setter
    def tls_ciphers_policy(self, tls_ciphers_policy):
        """Sets the tls_ciphers_policy of this ListListenersRequest.

        监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效，且默认值为tls-1-0。 取值包括：tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict四种安全策略。

        :param tls_ciphers_policy: The tls_ciphers_policy of this ListListenersRequest.
        :type: list[str]
        """
        self._tls_ciphers_policy = tls_ciphers_policy

    @property
    def transparent_client_ip_enable(self):
        """Gets the transparent_client_ip_enable of this ListListenersRequest.

        获取客户端真实IP

        :return: The transparent_client_ip_enable of this ListListenersRequest.
        :rtype: bool
        """
        return self._transparent_client_ip_enable

    @transparent_client_ip_enable.setter
    def transparent_client_ip_enable(self, transparent_client_ip_enable):
        """Sets the transparent_client_ip_enable of this ListListenersRequest.

        获取客户端真实IP

        :param transparent_client_ip_enable: The transparent_client_ip_enable of this ListListenersRequest.
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
