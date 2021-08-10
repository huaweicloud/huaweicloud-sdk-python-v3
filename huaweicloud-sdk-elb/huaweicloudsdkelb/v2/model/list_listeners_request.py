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
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'default_pool_id': 'str',
        'default_tls_container_ref': 'str',
        'client_ca_tls_container_ref': 'str',
        'protocol': 'str',
        'protocol_port': 'int',
        'tls_ciphers_policy': 'str',
        'member_timeout': 'int',
        'client_timeout': 'int',
        'keepalive_timeout': 'int',
        'tls_container_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'default_pool_id': 'default_pool_id',
        'default_tls_container_ref': 'default_tls_container_ref',
        'client_ca_tls_container_ref': 'client_ca_tls_container_ref',
        'protocol': 'protocol',
        'protocol_port': 'protocol_port',
        'tls_ciphers_policy': 'tls_ciphers_policy',
        'member_timeout': 'member_timeout',
        'client_timeout': 'client_timeout',
        'keepalive_timeout': 'keepalive_timeout',
        'tls_container_id': 'tls_container_id'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, name=None, description=None, default_pool_id=None, default_tls_container_ref=None, client_ca_tls_container_ref=None, protocol=None, protocol_port=None, tls_ciphers_policy=None, member_timeout=None, client_timeout=None, keepalive_timeout=None, tls_container_id=None):
        """ListListenersRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._description = None
        self._default_pool_id = None
        self._default_tls_container_ref = None
        self._client_ca_tls_container_ref = None
        self._protocol = None
        self._protocol_port = None
        self._tls_ciphers_policy = None
        self._member_timeout = None
        self._client_timeout = None
        self._keepalive_timeout = None
        self._tls_container_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if default_pool_id is not None:
            self.default_pool_id = default_pool_id
        if default_tls_container_ref is not None:
            self.default_tls_container_ref = default_tls_container_ref
        if client_ca_tls_container_ref is not None:
            self.client_ca_tls_container_ref = client_ca_tls_container_ref
        if protocol is not None:
            self.protocol = protocol
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if tls_ciphers_policy is not None:
            self.tls_ciphers_policy = tls_ciphers_policy
        if member_timeout is not None:
            self.member_timeout = member_timeout
        if client_timeout is not None:
            self.client_timeout = client_timeout
        if keepalive_timeout is not None:
            self.keepalive_timeout = keepalive_timeout
        if tls_container_id is not None:
            self.tls_container_id = tls_container_id

    @property
    def limit(self):
        """Gets the limit of this ListListenersRequest.

        分页查询中每页的监听器个数

        :return: The limit of this ListListenersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListListenersRequest.

        分页查询中每页的监听器个数

        :param limit: The limit of this ListListenersRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListListenersRequest.

        分页查询的起始的资源id，表示上一页最后一条查询记录的负载均衡器的id。不指定时表示查询第一页。

        :return: The marker of this ListListenersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListListenersRequest.

        分页查询的起始的资源id，表示上一页最后一条查询记录的负载均衡器的id。不指定时表示查询第一页。

        :param marker: The marker of this ListListenersRequest.
        :type: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListListenersRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :return: The page_reverse of this ListListenersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListListenersRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :param page_reverse: The page_reverse of this ListListenersRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListListenersRequest.

        监听器ID。

        :return: The id of this ListListenersRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListListenersRequest.

        监听器ID。

        :param id: The id of this ListListenersRequest.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListListenersRequest.

        监听器名称。

        :return: The name of this ListListenersRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListListenersRequest.

        监听器名称。

        :param name: The name of this ListListenersRequest.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListListenersRequest.

        监听器的描述信息。

        :return: The description of this ListListenersRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListListenersRequest.

        监听器的描述信息。

        :param description: The description of this ListListenersRequest.
        :type: str
        """
        self._description = description

    @property
    def default_pool_id(self):
        """Gets the default_pool_id of this ListListenersRequest.

        监听器的默认后端云服务器组ID。

        :return: The default_pool_id of this ListListenersRequest.
        :rtype: str
        """
        return self._default_pool_id

    @default_pool_id.setter
    def default_pool_id(self, default_pool_id):
        """Sets the default_pool_id of this ListListenersRequest.

        监听器的默认后端云服务器组ID。

        :param default_pool_id: The default_pool_id of this ListListenersRequest.
        :type: str
        """
        self._default_pool_id = default_pool_id

    @property
    def default_tls_container_ref(self):
        """Gets the default_tls_container_ref of this ListListenersRequest.

        监听器使用的服务器证书ID。

        :return: The default_tls_container_ref of this ListListenersRequest.
        :rtype: str
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        """Sets the default_tls_container_ref of this ListListenersRequest.

        监听器使用的服务器证书ID。

        :param default_tls_container_ref: The default_tls_container_ref of this ListListenersRequest.
        :type: str
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def client_ca_tls_container_ref(self):
        """Gets the client_ca_tls_container_ref of this ListListenersRequest.

        监听器使用的CA证书ID。

        :return: The client_ca_tls_container_ref of this ListListenersRequest.
        :rtype: str
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        """Sets the client_ca_tls_container_ref of this ListListenersRequest.

        监听器使用的CA证书ID。

        :param client_ca_tls_container_ref: The client_ca_tls_container_ref of this ListListenersRequest.
        :type: str
        """
        self._client_ca_tls_container_ref = client_ca_tls_container_ref

    @property
    def protocol(self):
        """Gets the protocol of this ListListenersRequest.

        监听器的监听协议。取值范围：TCP、HTTP、UDP、TERMINATED_HTTPS。

        :return: The protocol of this ListListenersRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListListenersRequest.

        监听器的监听协议。取值范围：TCP、HTTP、UDP、TERMINATED_HTTPS。

        :param protocol: The protocol of this ListListenersRequest.
        :type: str
        """
        self._protocol = protocol

    @property
    def protocol_port(self):
        """Gets the protocol_port of this ListListenersRequest.

        监听器的监听端口。

        :return: The protocol_port of this ListListenersRequest.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this ListListenersRequest.

        监听器的监听端口。

        :param protocol_port: The protocol_port of this ListListenersRequest.
        :type: int
        """
        self._protocol_port = protocol_port

    @property
    def tls_ciphers_policy(self):
        """Gets the tls_ciphers_policy of this ListListenersRequest.

        监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效，且默认值为tls-1-0。取值包括：tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict四种安全策略。

        :return: The tls_ciphers_policy of this ListListenersRequest.
        :rtype: str
        """
        return self._tls_ciphers_policy

    @tls_ciphers_policy.setter
    def tls_ciphers_policy(self, tls_ciphers_policy):
        """Sets the tls_ciphers_policy of this ListListenersRequest.

        监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效，且默认值为tls-1-0。取值包括：tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict四种安全策略。

        :param tls_ciphers_policy: The tls_ciphers_policy of this ListListenersRequest.
        :type: str
        """
        self._tls_ciphers_policy = tls_ciphers_policy

    @property
    def member_timeout(self):
        """Gets the member_timeout of this ListListenersRequest.

        等待后端服务器请求超时时间，协议为HTTP， TERMINATED_HTTPS时才有意义。取值范围 1-300

        :return: The member_timeout of this ListListenersRequest.
        :rtype: int
        """
        return self._member_timeout

    @member_timeout.setter
    def member_timeout(self, member_timeout):
        """Sets the member_timeout of this ListListenersRequest.

        等待后端服务器请求超时时间，协议为HTTP， TERMINATED_HTTPS时才有意义。取值范围 1-300

        :param member_timeout: The member_timeout of this ListListenersRequest.
        :type: int
        """
        self._member_timeout = member_timeout

    @property
    def client_timeout(self):
        """Gets the client_timeout of this ListListenersRequest.

        等待客户端请求超时时间，协议为HTTP， TERMINATED_HTTPS的监听器才有意义。取值范围 1-60

        :return: The client_timeout of this ListListenersRequest.
        :rtype: int
        """
        return self._client_timeout

    @client_timeout.setter
    def client_timeout(self, client_timeout):
        """Sets the client_timeout of this ListListenersRequest.

        等待客户端请求超时时间，协议为HTTP， TERMINATED_HTTPS的监听器才有意义。取值范围 1-60

        :param client_timeout: The client_timeout of this ListListenersRequest.
        :type: int
        """
        self._client_timeout = client_timeout

    @property
    def keepalive_timeout(self):
        """Gets the keepalive_timeout of this ListListenersRequest.

        TCP监听器配置空闲超时时间，取值范围为（10-900s）默认值为300s，TCP监听器配置空闲超时时间，取值范围为（10-900s）默认值为300s，HTTP/TERMINATED_HTTPS监听器为客户端连接空闲超时时间，取值范围为（1-300s）默认值为15s。 UDP此字段无意义

        :return: The keepalive_timeout of this ListListenersRequest.
        :rtype: int
        """
        return self._keepalive_timeout

    @keepalive_timeout.setter
    def keepalive_timeout(self, keepalive_timeout):
        """Sets the keepalive_timeout of this ListListenersRequest.

        TCP监听器配置空闲超时时间，取值范围为（10-900s）默认值为300s，TCP监听器配置空闲超时时间，取值范围为（10-900s）默认值为300s，HTTP/TERMINATED_HTTPS监听器为客户端连接空闲超时时间，取值范围为（1-300s）默认值为15s。 UDP此字段无意义

        :param keepalive_timeout: The keepalive_timeout of this ListListenersRequest.
        :type: int
        """
        self._keepalive_timeout = keepalive_timeout

    @property
    def tls_container_id(self):
        """Gets the tls_container_id of this ListListenersRequest.

        查询证书所关联的监听器

        :return: The tls_container_id of this ListListenersRequest.
        :rtype: str
        """
        return self._tls_container_id

    @tls_container_id.setter
    def tls_container_id(self, tls_container_id):
        """Sets the tls_container_id of this ListListenersRequest.

        查询证书所关联的监听器

        :param tls_container_id: The tls_container_id of this ListListenersRequest.
        :type: str
        """
        self._tls_container_id = tls_container_id

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
