# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdvancedConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deploy_timeout_minutes': 'str',
        'upgrade_config': 'UpgradeConfig',
        'service_secret': 'ServiceSecret',
        'dynamic_routing_enable': 'bool',
        'strategy': 'str',
        'ems_enable': 'bool',
        'metric_api_scheme': 'str',
        'metric_api_port': 'str',
        'metric_api_path': 'str',
        'custom_metrics_path': 'str',
        'port': 'int',
        'protocol': 'str'
    }

    attribute_map = {
        'deploy_timeout_minutes': 'deploy_timeout_minutes',
        'upgrade_config': 'upgrade_config',
        'service_secret': 'service_secret',
        'dynamic_routing_enable': 'dynamic_routing_enable',
        'strategy': 'strategy',
        'ems_enable': 'ems_enable',
        'metric_api_scheme': 'metric_api_scheme',
        'metric_api_port': 'metric_api_port',
        'metric_api_path': 'metric_api_path',
        'custom_metrics_path': 'custom_metrics_path',
        'port': 'port',
        'protocol': 'protocol'
    }

    def __init__(self, deploy_timeout_minutes=None, upgrade_config=None, service_secret=None, dynamic_routing_enable=None, strategy=None, ems_enable=None, metric_api_scheme=None, metric_api_port=None, metric_api_path=None, custom_metrics_path=None, port=None, protocol=None):
        r"""AdvancedConfig

        The model defined in huaweicloud sdk

        :param deploy_timeout_minutes: **参数解释：** 部署超时时间
        :type deploy_timeout_minutes: str
        :param upgrade_config: 
        :type upgrade_config: :class:`huaweicloudsdkmodelarts.v1.UpgradeConfig`
        :param service_secret: 
        :type service_secret: :class:`huaweicloudsdkmodelarts.v1.ServiceSecret`
        :param dynamic_routing_enable: **参数解释：** 智能路由开关
        :type dynamic_routing_enable: bool
        :param strategy: **参数解释：** 智能路由策略
        :type strategy: str
        :param ems_enable: **参数解释：** EMS加速开关
        :type ems_enable: bool
        :param metric_api_scheme: **参数解释：** 智能路由指标采集scheme
        :type metric_api_scheme: str
        :param metric_api_port: **参数解释：** 智能路由指标采集端口
        :type metric_api_port: str
        :param metric_api_path: **参数解释：** 智能路由指标采集地址
        :type metric_api_path: str
        :param custom_metrics_path: **参数解释：** 自定义监控采集指标地址
        :type custom_metrics_path: str
        :param port: **参数解释：** 容器端口
        :type port: int
        :param protocol: **参数解释：** 容器请求协议。当选择WSS与WS时，服务接口会升级为WebSocket。开启WebSocket时，不支持同时设置“服务流量限制”。 **取值范围：** - HTTP：HTTP协议。 - HTTPS：HTTPS协议。 - WSS：WebSocket Secure协议。 - WS：WebSocket协议。 - TCP：传输控制协议。 - NA：不使用任何协议。
        :type protocol: str
        """
        
        

        self._deploy_timeout_minutes = None
        self._upgrade_config = None
        self._service_secret = None
        self._dynamic_routing_enable = None
        self._strategy = None
        self._ems_enable = None
        self._metric_api_scheme = None
        self._metric_api_port = None
        self._metric_api_path = None
        self._custom_metrics_path = None
        self._port = None
        self._protocol = None
        self.discriminator = None

        if deploy_timeout_minutes is not None:
            self.deploy_timeout_minutes = deploy_timeout_minutes
        self.upgrade_config = upgrade_config
        if service_secret is not None:
            self.service_secret = service_secret
        if dynamic_routing_enable is not None:
            self.dynamic_routing_enable = dynamic_routing_enable
        if strategy is not None:
            self.strategy = strategy
        if ems_enable is not None:
            self.ems_enable = ems_enable
        if metric_api_scheme is not None:
            self.metric_api_scheme = metric_api_scheme
        if metric_api_port is not None:
            self.metric_api_port = metric_api_port
        if metric_api_path is not None:
            self.metric_api_path = metric_api_path
        if custom_metrics_path is not None:
            self.custom_metrics_path = custom_metrics_path
        self.port = port
        self.protocol = protocol

    @property
    def deploy_timeout_minutes(self):
        r"""Gets the deploy_timeout_minutes of this AdvancedConfig.

        **参数解释：** 部署超时时间

        :return: The deploy_timeout_minutes of this AdvancedConfig.
        :rtype: str
        """
        return self._deploy_timeout_minutes

    @deploy_timeout_minutes.setter
    def deploy_timeout_minutes(self, deploy_timeout_minutes):
        r"""Sets the deploy_timeout_minutes of this AdvancedConfig.

        **参数解释：** 部署超时时间

        :param deploy_timeout_minutes: The deploy_timeout_minutes of this AdvancedConfig.
        :type deploy_timeout_minutes: str
        """
        self._deploy_timeout_minutes = deploy_timeout_minutes

    @property
    def upgrade_config(self):
        r"""Gets the upgrade_config of this AdvancedConfig.

        :return: The upgrade_config of this AdvancedConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpgradeConfig`
        """
        return self._upgrade_config

    @upgrade_config.setter
    def upgrade_config(self, upgrade_config):
        r"""Sets the upgrade_config of this AdvancedConfig.

        :param upgrade_config: The upgrade_config of this AdvancedConfig.
        :type upgrade_config: :class:`huaweicloudsdkmodelarts.v1.UpgradeConfig`
        """
        self._upgrade_config = upgrade_config

    @property
    def service_secret(self):
        r"""Gets the service_secret of this AdvancedConfig.

        :return: The service_secret of this AdvancedConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServiceSecret`
        """
        return self._service_secret

    @service_secret.setter
    def service_secret(self, service_secret):
        r"""Sets the service_secret of this AdvancedConfig.

        :param service_secret: The service_secret of this AdvancedConfig.
        :type service_secret: :class:`huaweicloudsdkmodelarts.v1.ServiceSecret`
        """
        self._service_secret = service_secret

    @property
    def dynamic_routing_enable(self):
        r"""Gets the dynamic_routing_enable of this AdvancedConfig.

        **参数解释：** 智能路由开关

        :return: The dynamic_routing_enable of this AdvancedConfig.
        :rtype: bool
        """
        return self._dynamic_routing_enable

    @dynamic_routing_enable.setter
    def dynamic_routing_enable(self, dynamic_routing_enable):
        r"""Sets the dynamic_routing_enable of this AdvancedConfig.

        **参数解释：** 智能路由开关

        :param dynamic_routing_enable: The dynamic_routing_enable of this AdvancedConfig.
        :type dynamic_routing_enable: bool
        """
        self._dynamic_routing_enable = dynamic_routing_enable

    @property
    def strategy(self):
        r"""Gets the strategy of this AdvancedConfig.

        **参数解释：** 智能路由策略

        :return: The strategy of this AdvancedConfig.
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        r"""Sets the strategy of this AdvancedConfig.

        **参数解释：** 智能路由策略

        :param strategy: The strategy of this AdvancedConfig.
        :type strategy: str
        """
        self._strategy = strategy

    @property
    def ems_enable(self):
        r"""Gets the ems_enable of this AdvancedConfig.

        **参数解释：** EMS加速开关

        :return: The ems_enable of this AdvancedConfig.
        :rtype: bool
        """
        return self._ems_enable

    @ems_enable.setter
    def ems_enable(self, ems_enable):
        r"""Sets the ems_enable of this AdvancedConfig.

        **参数解释：** EMS加速开关

        :param ems_enable: The ems_enable of this AdvancedConfig.
        :type ems_enable: bool
        """
        self._ems_enable = ems_enable

    @property
    def metric_api_scheme(self):
        r"""Gets the metric_api_scheme of this AdvancedConfig.

        **参数解释：** 智能路由指标采集scheme

        :return: The metric_api_scheme of this AdvancedConfig.
        :rtype: str
        """
        return self._metric_api_scheme

    @metric_api_scheme.setter
    def metric_api_scheme(self, metric_api_scheme):
        r"""Sets the metric_api_scheme of this AdvancedConfig.

        **参数解释：** 智能路由指标采集scheme

        :param metric_api_scheme: The metric_api_scheme of this AdvancedConfig.
        :type metric_api_scheme: str
        """
        self._metric_api_scheme = metric_api_scheme

    @property
    def metric_api_port(self):
        r"""Gets the metric_api_port of this AdvancedConfig.

        **参数解释：** 智能路由指标采集端口

        :return: The metric_api_port of this AdvancedConfig.
        :rtype: str
        """
        return self._metric_api_port

    @metric_api_port.setter
    def metric_api_port(self, metric_api_port):
        r"""Sets the metric_api_port of this AdvancedConfig.

        **参数解释：** 智能路由指标采集端口

        :param metric_api_port: The metric_api_port of this AdvancedConfig.
        :type metric_api_port: str
        """
        self._metric_api_port = metric_api_port

    @property
    def metric_api_path(self):
        r"""Gets the metric_api_path of this AdvancedConfig.

        **参数解释：** 智能路由指标采集地址

        :return: The metric_api_path of this AdvancedConfig.
        :rtype: str
        """
        return self._metric_api_path

    @metric_api_path.setter
    def metric_api_path(self, metric_api_path):
        r"""Sets the metric_api_path of this AdvancedConfig.

        **参数解释：** 智能路由指标采集地址

        :param metric_api_path: The metric_api_path of this AdvancedConfig.
        :type metric_api_path: str
        """
        self._metric_api_path = metric_api_path

    @property
    def custom_metrics_path(self):
        r"""Gets the custom_metrics_path of this AdvancedConfig.

        **参数解释：** 自定义监控采集指标地址

        :return: The custom_metrics_path of this AdvancedConfig.
        :rtype: str
        """
        return self._custom_metrics_path

    @custom_metrics_path.setter
    def custom_metrics_path(self, custom_metrics_path):
        r"""Sets the custom_metrics_path of this AdvancedConfig.

        **参数解释：** 自定义监控采集指标地址

        :param custom_metrics_path: The custom_metrics_path of this AdvancedConfig.
        :type custom_metrics_path: str
        """
        self._custom_metrics_path = custom_metrics_path

    @property
    def port(self):
        r"""Gets the port of this AdvancedConfig.

        **参数解释：** 容器端口

        :return: The port of this AdvancedConfig.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this AdvancedConfig.

        **参数解释：** 容器端口

        :param port: The port of this AdvancedConfig.
        :type port: int
        """
        self._port = port

    @property
    def protocol(self):
        r"""Gets the protocol of this AdvancedConfig.

        **参数解释：** 容器请求协议。当选择WSS与WS时，服务接口会升级为WebSocket。开启WebSocket时，不支持同时设置“服务流量限制”。 **取值范围：** - HTTP：HTTP协议。 - HTTPS：HTTPS协议。 - WSS：WebSocket Secure协议。 - WS：WebSocket协议。 - TCP：传输控制协议。 - NA：不使用任何协议。

        :return: The protocol of this AdvancedConfig.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this AdvancedConfig.

        **参数解释：** 容器请求协议。当选择WSS与WS时，服务接口会升级为WebSocket。开启WebSocket时，不支持同时设置“服务流量限制”。 **取值范围：** - HTTP：HTTP协议。 - HTTPS：HTTPS协议。 - WSS：WebSocket Secure协议。 - WS：WebSocket协议。 - TCP：传输控制协议。 - NA：不使用任何协议。

        :param protocol: The protocol of this AdvancedConfig.
        :type protocol: str
        """
        self._protocol = protocol

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
        if not isinstance(other, AdvancedConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
