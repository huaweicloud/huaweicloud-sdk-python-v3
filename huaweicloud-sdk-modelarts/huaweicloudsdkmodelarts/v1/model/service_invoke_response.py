# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceInvokeResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'int',
        'protocol': 'str',
        'auth_type': 'str',
        'internet_access_enable': 'bool',
        'intranet_approval_enable': 'bool',
        'dynamic_routing_enable': 'bool',
        'strategy': 'str',
        'metric_api_scheme': 'str',
        'metric_api_port': 'str',
        'metric_api_path': 'str',
        'ems_enable': 'bool',
        'request_retry_enable': 'bool',
        'request_retry_cnt_max': 'int',
        'request_retry_interval_ms': 'int',
        'fuse_configs': 'FuseConfig'
    }

    attribute_map = {
        'port': 'port',
        'protocol': 'protocol',
        'auth_type': 'auth_type',
        'internet_access_enable': 'internet_access_enable',
        'intranet_approval_enable': 'intranet_approval_enable',
        'dynamic_routing_enable': 'dynamic_routing_enable',
        'strategy': 'strategy',
        'metric_api_scheme': 'metric_api_scheme',
        'metric_api_port': 'metric_api_port',
        'metric_api_path': 'metric_api_path',
        'ems_enable': 'ems_enable',
        'request_retry_enable': 'request_retry_enable',
        'request_retry_cnt_max': 'request_retry_cnt_max',
        'request_retry_interval_ms': 'request_retry_interval_ms',
        'fuse_configs': 'fuse_configs'
    }

    def __init__(self, port=None, protocol=None, auth_type=None, internet_access_enable=None, intranet_approval_enable=None, dynamic_routing_enable=None, strategy=None, metric_api_scheme=None, metric_api_port=None, metric_api_path=None, ems_enable=None, request_retry_enable=None, request_retry_cnt_max=None, request_retry_interval_ms=None, fuse_configs=None):
        r"""ServiceInvokeResponse

        The model defined in huaweicloud sdk

        :param port: **参数解释：** 服务端口号。 **取值范围：** [1, 65535]。
        :type port: int
        :param protocol: **参数解释：** 服务请求协议。当选择WSS与WS时，服务接口会升级为WebSocket。开启WebSocket时，不支持同时设置“服务流量限制”。 **取值范围：** - HTTP：HTTP协议。 - HTTPS：HTTPS协议。 - WSS：WebSocket Secure协议。 - WS：WebSocket协议。
        :type protocol: str
        :param auth_type: **参数解释：** 认证类型。 **取值范围：** - TOKEN：IAM Token认证。 - API_KEY：API Key认证。 - NONE：无认证。
        :type auth_type: str
        :param internet_access_enable: **参数解释：** 外网访问。 **取值范围：** - TRUE：要外网访问。 - FALSE：不要外网访问。
        :type internet_access_enable: bool
        :param intranet_approval_enable: **参数解释：** 内网审批。 **取值范围：** - TRUE：要内网审批。 - FALSE：不要内网审批。
        :type intranet_approval_enable: bool
        :param dynamic_routing_enable: **参数解释：** 动态路由开关。 **取值范围：** - TRUE：开启动态路由。 - FALSE：不开启动态路由。
        :type dynamic_routing_enable: bool
        :param strategy: **参数解释：** 智能路由策略。 **取值范围：** - ROUND_ROBIN：轮询。 - ORIGIN_IP_HASH：源IP哈希。 - MIN_CONN：最小连接数。 - MIN_FIRST_TOKEN_TIME：最小首token时延。 - COMPOSITE：综合负载。 - SLO_BASED：SLO优先级。
        :type strategy: str
        :param metric_api_scheme: **参数解释：** 指标接口服务请求协议。 **取值范围：** - HTTP：HTTP协议。 - HTTPS：HTTPS协议。
        :type metric_api_scheme: str
        :param metric_api_port: **参数解释：** 指标接口端口号。 **取值范围：** [1, 65535]。
        :type metric_api_port: str
        :param metric_api_path: **参数解释：** 指标接口path。 **取值范围：** 不涉及。
        :type metric_api_path: str
        :param ems_enable: **参数解释：** 是否开启EMS加速。 **取值范围：** - TRUE：开启EMS加速。 - FALSE：不开启EMS加速。
        :type ems_enable: bool
        :param request_retry_enable: **参数解释：** proxy支持请求重调度开关。 **取值范围：** - true：开启proxy支持请求重调度。 - false：不开启proxy支持请求重调度。
        :type request_retry_enable: bool
        :param request_retry_cnt_max: **参数解释：** proxy支持请求重调度的重试次数 **取值范围：** [1, 10]。
        :type request_retry_cnt_max: int
        :param request_retry_interval_ms: **参数解释：** proxy支持请求重调度的重试间隔，单位ms **取值范围：** [1, 10000]。
        :type request_retry_interval_ms: int
        :param fuse_configs: 
        :type fuse_configs: :class:`huaweicloudsdkmodelarts.v1.FuseConfig`
        """
        
        

        self._port = None
        self._protocol = None
        self._auth_type = None
        self._internet_access_enable = None
        self._intranet_approval_enable = None
        self._dynamic_routing_enable = None
        self._strategy = None
        self._metric_api_scheme = None
        self._metric_api_port = None
        self._metric_api_path = None
        self._ems_enable = None
        self._request_retry_enable = None
        self._request_retry_cnt_max = None
        self._request_retry_interval_ms = None
        self._fuse_configs = None
        self.discriminator = None

        self.port = port
        self.protocol = protocol
        self.auth_type = auth_type
        if internet_access_enable is not None:
            self.internet_access_enable = internet_access_enable
        if intranet_approval_enable is not None:
            self.intranet_approval_enable = intranet_approval_enable
        if dynamic_routing_enable is not None:
            self.dynamic_routing_enable = dynamic_routing_enable
        if strategy is not None:
            self.strategy = strategy
        if metric_api_scheme is not None:
            self.metric_api_scheme = metric_api_scheme
        if metric_api_port is not None:
            self.metric_api_port = metric_api_port
        if metric_api_path is not None:
            self.metric_api_path = metric_api_path
        if ems_enable is not None:
            self.ems_enable = ems_enable
        if request_retry_enable is not None:
            self.request_retry_enable = request_retry_enable
        if request_retry_cnt_max is not None:
            self.request_retry_cnt_max = request_retry_cnt_max
        if request_retry_interval_ms is not None:
            self.request_retry_interval_ms = request_retry_interval_ms
        if fuse_configs is not None:
            self.fuse_configs = fuse_configs

    @property
    def port(self):
        r"""Gets the port of this ServiceInvokeResponse.

        **参数解释：** 服务端口号。 **取值范围：** [1, 65535]。

        :return: The port of this ServiceInvokeResponse.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ServiceInvokeResponse.

        **参数解释：** 服务端口号。 **取值范围：** [1, 65535]。

        :param port: The port of this ServiceInvokeResponse.
        :type port: int
        """
        self._port = port

    @property
    def protocol(self):
        r"""Gets the protocol of this ServiceInvokeResponse.

        **参数解释：** 服务请求协议。当选择WSS与WS时，服务接口会升级为WebSocket。开启WebSocket时，不支持同时设置“服务流量限制”。 **取值范围：** - HTTP：HTTP协议。 - HTTPS：HTTPS协议。 - WSS：WebSocket Secure协议。 - WS：WebSocket协议。

        :return: The protocol of this ServiceInvokeResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ServiceInvokeResponse.

        **参数解释：** 服务请求协议。当选择WSS与WS时，服务接口会升级为WebSocket。开启WebSocket时，不支持同时设置“服务流量限制”。 **取值范围：** - HTTP：HTTP协议。 - HTTPS：HTTPS协议。 - WSS：WebSocket Secure协议。 - WS：WebSocket协议。

        :param protocol: The protocol of this ServiceInvokeResponse.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def auth_type(self):
        r"""Gets the auth_type of this ServiceInvokeResponse.

        **参数解释：** 认证类型。 **取值范围：** - TOKEN：IAM Token认证。 - API_KEY：API Key认证。 - NONE：无认证。

        :return: The auth_type of this ServiceInvokeResponse.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this ServiceInvokeResponse.

        **参数解释：** 认证类型。 **取值范围：** - TOKEN：IAM Token认证。 - API_KEY：API Key认证。 - NONE：无认证。

        :param auth_type: The auth_type of this ServiceInvokeResponse.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def internet_access_enable(self):
        r"""Gets the internet_access_enable of this ServiceInvokeResponse.

        **参数解释：** 外网访问。 **取值范围：** - TRUE：要外网访问。 - FALSE：不要外网访问。

        :return: The internet_access_enable of this ServiceInvokeResponse.
        :rtype: bool
        """
        return self._internet_access_enable

    @internet_access_enable.setter
    def internet_access_enable(self, internet_access_enable):
        r"""Sets the internet_access_enable of this ServiceInvokeResponse.

        **参数解释：** 外网访问。 **取值范围：** - TRUE：要外网访问。 - FALSE：不要外网访问。

        :param internet_access_enable: The internet_access_enable of this ServiceInvokeResponse.
        :type internet_access_enable: bool
        """
        self._internet_access_enable = internet_access_enable

    @property
    def intranet_approval_enable(self):
        r"""Gets the intranet_approval_enable of this ServiceInvokeResponse.

        **参数解释：** 内网审批。 **取值范围：** - TRUE：要内网审批。 - FALSE：不要内网审批。

        :return: The intranet_approval_enable of this ServiceInvokeResponse.
        :rtype: bool
        """
        return self._intranet_approval_enable

    @intranet_approval_enable.setter
    def intranet_approval_enable(self, intranet_approval_enable):
        r"""Sets the intranet_approval_enable of this ServiceInvokeResponse.

        **参数解释：** 内网审批。 **取值范围：** - TRUE：要内网审批。 - FALSE：不要内网审批。

        :param intranet_approval_enable: The intranet_approval_enable of this ServiceInvokeResponse.
        :type intranet_approval_enable: bool
        """
        self._intranet_approval_enable = intranet_approval_enable

    @property
    def dynamic_routing_enable(self):
        r"""Gets the dynamic_routing_enable of this ServiceInvokeResponse.

        **参数解释：** 动态路由开关。 **取值范围：** - TRUE：开启动态路由。 - FALSE：不开启动态路由。

        :return: The dynamic_routing_enable of this ServiceInvokeResponse.
        :rtype: bool
        """
        return self._dynamic_routing_enable

    @dynamic_routing_enable.setter
    def dynamic_routing_enable(self, dynamic_routing_enable):
        r"""Sets the dynamic_routing_enable of this ServiceInvokeResponse.

        **参数解释：** 动态路由开关。 **取值范围：** - TRUE：开启动态路由。 - FALSE：不开启动态路由。

        :param dynamic_routing_enable: The dynamic_routing_enable of this ServiceInvokeResponse.
        :type dynamic_routing_enable: bool
        """
        self._dynamic_routing_enable = dynamic_routing_enable

    @property
    def strategy(self):
        r"""Gets the strategy of this ServiceInvokeResponse.

        **参数解释：** 智能路由策略。 **取值范围：** - ROUND_ROBIN：轮询。 - ORIGIN_IP_HASH：源IP哈希。 - MIN_CONN：最小连接数。 - MIN_FIRST_TOKEN_TIME：最小首token时延。 - COMPOSITE：综合负载。 - SLO_BASED：SLO优先级。

        :return: The strategy of this ServiceInvokeResponse.
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        r"""Sets the strategy of this ServiceInvokeResponse.

        **参数解释：** 智能路由策略。 **取值范围：** - ROUND_ROBIN：轮询。 - ORIGIN_IP_HASH：源IP哈希。 - MIN_CONN：最小连接数。 - MIN_FIRST_TOKEN_TIME：最小首token时延。 - COMPOSITE：综合负载。 - SLO_BASED：SLO优先级。

        :param strategy: The strategy of this ServiceInvokeResponse.
        :type strategy: str
        """
        self._strategy = strategy

    @property
    def metric_api_scheme(self):
        r"""Gets the metric_api_scheme of this ServiceInvokeResponse.

        **参数解释：** 指标接口服务请求协议。 **取值范围：** - HTTP：HTTP协议。 - HTTPS：HTTPS协议。

        :return: The metric_api_scheme of this ServiceInvokeResponse.
        :rtype: str
        """
        return self._metric_api_scheme

    @metric_api_scheme.setter
    def metric_api_scheme(self, metric_api_scheme):
        r"""Sets the metric_api_scheme of this ServiceInvokeResponse.

        **参数解释：** 指标接口服务请求协议。 **取值范围：** - HTTP：HTTP协议。 - HTTPS：HTTPS协议。

        :param metric_api_scheme: The metric_api_scheme of this ServiceInvokeResponse.
        :type metric_api_scheme: str
        """
        self._metric_api_scheme = metric_api_scheme

    @property
    def metric_api_port(self):
        r"""Gets the metric_api_port of this ServiceInvokeResponse.

        **参数解释：** 指标接口端口号。 **取值范围：** [1, 65535]。

        :return: The metric_api_port of this ServiceInvokeResponse.
        :rtype: str
        """
        return self._metric_api_port

    @metric_api_port.setter
    def metric_api_port(self, metric_api_port):
        r"""Sets the metric_api_port of this ServiceInvokeResponse.

        **参数解释：** 指标接口端口号。 **取值范围：** [1, 65535]。

        :param metric_api_port: The metric_api_port of this ServiceInvokeResponse.
        :type metric_api_port: str
        """
        self._metric_api_port = metric_api_port

    @property
    def metric_api_path(self):
        r"""Gets the metric_api_path of this ServiceInvokeResponse.

        **参数解释：** 指标接口path。 **取值范围：** 不涉及。

        :return: The metric_api_path of this ServiceInvokeResponse.
        :rtype: str
        """
        return self._metric_api_path

    @metric_api_path.setter
    def metric_api_path(self, metric_api_path):
        r"""Sets the metric_api_path of this ServiceInvokeResponse.

        **参数解释：** 指标接口path。 **取值范围：** 不涉及。

        :param metric_api_path: The metric_api_path of this ServiceInvokeResponse.
        :type metric_api_path: str
        """
        self._metric_api_path = metric_api_path

    @property
    def ems_enable(self):
        r"""Gets the ems_enable of this ServiceInvokeResponse.

        **参数解释：** 是否开启EMS加速。 **取值范围：** - TRUE：开启EMS加速。 - FALSE：不开启EMS加速。

        :return: The ems_enable of this ServiceInvokeResponse.
        :rtype: bool
        """
        return self._ems_enable

    @ems_enable.setter
    def ems_enable(self, ems_enable):
        r"""Sets the ems_enable of this ServiceInvokeResponse.

        **参数解释：** 是否开启EMS加速。 **取值范围：** - TRUE：开启EMS加速。 - FALSE：不开启EMS加速。

        :param ems_enable: The ems_enable of this ServiceInvokeResponse.
        :type ems_enable: bool
        """
        self._ems_enable = ems_enable

    @property
    def request_retry_enable(self):
        r"""Gets the request_retry_enable of this ServiceInvokeResponse.

        **参数解释：** proxy支持请求重调度开关。 **取值范围：** - true：开启proxy支持请求重调度。 - false：不开启proxy支持请求重调度。

        :return: The request_retry_enable of this ServiceInvokeResponse.
        :rtype: bool
        """
        return self._request_retry_enable

    @request_retry_enable.setter
    def request_retry_enable(self, request_retry_enable):
        r"""Sets the request_retry_enable of this ServiceInvokeResponse.

        **参数解释：** proxy支持请求重调度开关。 **取值范围：** - true：开启proxy支持请求重调度。 - false：不开启proxy支持请求重调度。

        :param request_retry_enable: The request_retry_enable of this ServiceInvokeResponse.
        :type request_retry_enable: bool
        """
        self._request_retry_enable = request_retry_enable

    @property
    def request_retry_cnt_max(self):
        r"""Gets the request_retry_cnt_max of this ServiceInvokeResponse.

        **参数解释：** proxy支持请求重调度的重试次数 **取值范围：** [1, 10]。

        :return: The request_retry_cnt_max of this ServiceInvokeResponse.
        :rtype: int
        """
        return self._request_retry_cnt_max

    @request_retry_cnt_max.setter
    def request_retry_cnt_max(self, request_retry_cnt_max):
        r"""Sets the request_retry_cnt_max of this ServiceInvokeResponse.

        **参数解释：** proxy支持请求重调度的重试次数 **取值范围：** [1, 10]。

        :param request_retry_cnt_max: The request_retry_cnt_max of this ServiceInvokeResponse.
        :type request_retry_cnt_max: int
        """
        self._request_retry_cnt_max = request_retry_cnt_max

    @property
    def request_retry_interval_ms(self):
        r"""Gets the request_retry_interval_ms of this ServiceInvokeResponse.

        **参数解释：** proxy支持请求重调度的重试间隔，单位ms **取值范围：** [1, 10000]。

        :return: The request_retry_interval_ms of this ServiceInvokeResponse.
        :rtype: int
        """
        return self._request_retry_interval_ms

    @request_retry_interval_ms.setter
    def request_retry_interval_ms(self, request_retry_interval_ms):
        r"""Sets the request_retry_interval_ms of this ServiceInvokeResponse.

        **参数解释：** proxy支持请求重调度的重试间隔，单位ms **取值范围：** [1, 10000]。

        :param request_retry_interval_ms: The request_retry_interval_ms of this ServiceInvokeResponse.
        :type request_retry_interval_ms: int
        """
        self._request_retry_interval_ms = request_retry_interval_ms

    @property
    def fuse_configs(self):
        r"""Gets the fuse_configs of this ServiceInvokeResponse.

        :return: The fuse_configs of this ServiceInvokeResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.FuseConfig`
        """
        return self._fuse_configs

    @fuse_configs.setter
    def fuse_configs(self, fuse_configs):
        r"""Sets the fuse_configs of this ServiceInvokeResponse.

        :param fuse_configs: The fuse_configs of this ServiceInvokeResponse.
        :type fuse_configs: :class:`huaweicloudsdkmodelarts.v1.FuseConfig`
        """
        self._fuse_configs = fuse_configs

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServiceInvokeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
