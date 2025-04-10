# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutopilotClusterSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'type': 'str',
        'flavor': 'str',
        'version': 'str',
        'platform_version': 'str',
        'description': 'str',
        'custom_san': 'list[str]',
        'enable_snat': 'bool',
        'enable_swr_image_access': 'bool',
        'ipv6enable': 'bool',
        'host_network': 'AutopilotHostNetwork',
        'container_network': 'AutopilotContainerNetwork',
        'eni_network': 'AutopilotEniNetwork',
        'service_network': 'AutopilotServiceNetwork',
        'authentication': 'AutopilotAuthentication',
        'billing_mode': 'int',
        'kubernetes_svc_ip_range': 'str',
        'cluster_tags': 'list[AutopilotResourceTag]',
        'kube_proxy_mode': 'str',
        'az': 'str',
        'extend_param': 'AutopilotClusterExtendParam',
        'configurations_override': 'list[AutopilotPackageConfiguration]'
    }

    attribute_map = {
        'category': 'category',
        'type': 'type',
        'flavor': 'flavor',
        'version': 'version',
        'platform_version': 'platformVersion',
        'description': 'description',
        'custom_san': 'customSan',
        'enable_snat': 'enableSnat',
        'enable_swr_image_access': 'enableSWRImageAccess',
        'ipv6enable': 'ipv6enable',
        'host_network': 'hostNetwork',
        'container_network': 'containerNetwork',
        'eni_network': 'eniNetwork',
        'service_network': 'serviceNetwork',
        'authentication': 'authentication',
        'billing_mode': 'billingMode',
        'kubernetes_svc_ip_range': 'kubernetesSvcIpRange',
        'cluster_tags': 'clusterTags',
        'kube_proxy_mode': 'kubeProxyMode',
        'az': 'az',
        'extend_param': 'extendParam',
        'configurations_override': 'configurationsOverride'
    }

    def __init__(self, category=None, type=None, flavor=None, version=None, platform_version=None, description=None, custom_san=None, enable_snat=None, enable_swr_image_access=None, ipv6enable=None, host_network=None, container_network=None, eni_network=None, service_network=None, authentication=None, billing_mode=None, kubernetes_svc_ip_range=None, cluster_tags=None, kube_proxy_mode=None, az=None, extend_param=None, configurations_override=None):
        r"""AutopilotClusterSpec

        The model defined in huaweicloud sdk

        :param category: 集群类别。 
        :type category: str
        :param type: 集群Master节点架构：  - VirtualMachine：Master节点为x86架构服务器 
        :type type: str
        :param flavor: 集群规格，cce.autopilot.cluster 
        :type flavor: str
        :param version: 集群版本，与Kubernetes社区基线版本保持一致，建议选择最新版本。  在CCE控制台支持创建两种最新版本的集群。可登录CCE控制台创建集群，在“版本”处获取到集群版本。 其它集群版本，当前仍可通过api创建，但后续会逐渐下线，具体下线策略请关注CCE官方公告。  &gt;    - 若不配置，默认创建最新版本的集群。
        :type version: str
        :param platform_version: CCE集群平台版本号，表示集群版本(version)下的内部版本。用于跟踪某一集群版本内的迭代，集群版本内唯一，跨集群版本重新计数。不支持用户指定，集群创建时自动选择对应集群版本的最新平台版本。  platformVersion格式为：cce.X.Y - X: 表示内部特性版本。集群版本中特性或者补丁修复，或者OS支持等变更场景。其值从1开始单调递增。 - Y: 表示内部特性版本的补丁版本。仅用于特性版本上线后的软件包更新，不涉及其他修改。其值从0开始单调递增。 
        :type platform_version: str
        :param description: 集群描述，对于集群使用目的的描述，可根据实际情况自定义，默认为空。集群创建成功后可通过接口[更新指定的集群](cce_02_0240.xml)来做出修改，也可在CCE控制台中对应集群的“集群详情”下的“描述”处进行修改。仅支持utf-8编码。 
        :type description: str
        :param custom_san: 集群的API Server服务端证书中的自定义SAN（Subject Alternative Name）字段，遵从SSL标准X509定义的格式规范。  1. 不允许出现同名重复。 2. 格式符合IP和域名格式。  示例: &#x60;&#x60;&#x60; SAN 1: DNS Name&#x3D;example.com SAN 2: DNS Name&#x3D;www.example.com SAN 3: DNS Name&#x3D;example.net SAN 4: IP Address&#x3D;93.184.216.34 &#x60;&#x60;&#x60;
        :type custom_san: list[str]
        :param enable_snat: 集群是否配置SNAT。开启后您的集群可以通过NAT网关访问公网，默认使用所选的VPC中已有的NAT网关，否则系统将会为您自动创建一个默认规格的NAT网关并绑定弹性公网IP，自动配置SNAT规则。
        :type enable_snat: bool
        :param enable_swr_image_access: 集群是否配置镜像访问。为确保您的集群节点可以从容器镜像服务中拉取镜像，默认使用所选VPC中已有的SWR和OBS终端节点，否则将会为您自动新建SWR和OBS终端节点。
        :type enable_swr_image_access: bool
        :param ipv6enable: 集群是否使用IPv6模式。
        :type ipv6enable: bool
        :param host_network: 
        :type host_network: :class:`huaweicloudsdkcce.v3.AutopilotHostNetwork`
        :param container_network: 
        :type container_network: :class:`huaweicloudsdkcce.v3.AutopilotContainerNetwork`
        :param eni_network: 
        :type eni_network: :class:`huaweicloudsdkcce.v3.AutopilotEniNetwork`
        :param service_network: 
        :type service_network: :class:`huaweicloudsdkcce.v3.AutopilotServiceNetwork`
        :param authentication: 
        :type authentication: :class:`huaweicloudsdkcce.v3.AutopilotAuthentication`
        :param billing_mode: 集群的计费方式。 - 0: 按需计费  默认为“按需计费”。 
        :type billing_mode: int
        :param kubernetes_svc_ip_range: 服务网段参数，kubernetes clusterIP取值范围。创建集群时如若未传参，默认为\&quot;10.247.0.0/16\&quot;。该参数废弃中，推荐使用新字段serviceNetwork，包含IPv4服务网段。 
        :type kubernetes_svc_ip_range: str
        :param cluster_tags: 集群资源标签
        :type cluster_tags: list[:class:`huaweicloudsdkcce.v3.AutopilotResourceTag`]
        :param kube_proxy_mode: 服务转发模式：  - iptables：社区传统的kube-proxy模式，完全以iptables规则的方式来实现service负载均衡。该方式最主要的问题是在服务多的时候产生太多的iptables规则，非增量式更新会引入一定的时延，大规模情况下有明显的性能问题。  &gt; 默认使用iptables转发模式。 
        :type kube_proxy_mode: str
        :param az: 可用区（仅查询返回字段）。  [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint?CCE)](tag:hws)  [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/intl/zh-cn/endpoint?CCE)](tag:hws_hk) 
        :type az: str
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcce.v3.AutopilotClusterExtendParam`
        :param configurations_override: 覆盖集群默认组件配置  若指定了不支持的组件或组件不支持的参数，该配置项将被忽略。  当前支持的可配置组件及其参数详见 [[配置管理](https://support.huaweicloud.com/usermanual-cce/cce_10_0213.html)](tag:hws) [[配置管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0213.html)](tag:hws_hk) 
        :type configurations_override: list[:class:`huaweicloudsdkcce.v3.AutopilotPackageConfiguration`]
        """
        
        

        self._category = None
        self._type = None
        self._flavor = None
        self._version = None
        self._platform_version = None
        self._description = None
        self._custom_san = None
        self._enable_snat = None
        self._enable_swr_image_access = None
        self._ipv6enable = None
        self._host_network = None
        self._container_network = None
        self._eni_network = None
        self._service_network = None
        self._authentication = None
        self._billing_mode = None
        self._kubernetes_svc_ip_range = None
        self._cluster_tags = None
        self._kube_proxy_mode = None
        self._az = None
        self._extend_param = None
        self._configurations_override = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if type is not None:
            self.type = type
        self.flavor = flavor
        if version is not None:
            self.version = version
        if platform_version is not None:
            self.platform_version = platform_version
        if description is not None:
            self.description = description
        if custom_san is not None:
            self.custom_san = custom_san
        if enable_snat is not None:
            self.enable_snat = enable_snat
        if enable_swr_image_access is not None:
            self.enable_swr_image_access = enable_swr_image_access
        if ipv6enable is not None:
            self.ipv6enable = ipv6enable
        self.host_network = host_network
        self.container_network = container_network
        if eni_network is not None:
            self.eni_network = eni_network
        if service_network is not None:
            self.service_network = service_network
        if authentication is not None:
            self.authentication = authentication
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if kubernetes_svc_ip_range is not None:
            self.kubernetes_svc_ip_range = kubernetes_svc_ip_range
        if cluster_tags is not None:
            self.cluster_tags = cluster_tags
        if kube_proxy_mode is not None:
            self.kube_proxy_mode = kube_proxy_mode
        if az is not None:
            self.az = az
        if extend_param is not None:
            self.extend_param = extend_param
        if configurations_override is not None:
            self.configurations_override = configurations_override

    @property
    def category(self):
        r"""Gets the category of this AutopilotClusterSpec.

        集群类别。 

        :return: The category of this AutopilotClusterSpec.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this AutopilotClusterSpec.

        集群类别。 

        :param category: The category of this AutopilotClusterSpec.
        :type category: str
        """
        self._category = category

    @property
    def type(self):
        r"""Gets the type of this AutopilotClusterSpec.

        集群Master节点架构：  - VirtualMachine：Master节点为x86架构服务器 

        :return: The type of this AutopilotClusterSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AutopilotClusterSpec.

        集群Master节点架构：  - VirtualMachine：Master节点为x86架构服务器 

        :param type: The type of this AutopilotClusterSpec.
        :type type: str
        """
        self._type = type

    @property
    def flavor(self):
        r"""Gets the flavor of this AutopilotClusterSpec.

        集群规格，cce.autopilot.cluster 

        :return: The flavor of this AutopilotClusterSpec.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this AutopilotClusterSpec.

        集群规格，cce.autopilot.cluster 

        :param flavor: The flavor of this AutopilotClusterSpec.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def version(self):
        r"""Gets the version of this AutopilotClusterSpec.

        集群版本，与Kubernetes社区基线版本保持一致，建议选择最新版本。  在CCE控制台支持创建两种最新版本的集群。可登录CCE控制台创建集群，在“版本”处获取到集群版本。 其它集群版本，当前仍可通过api创建，但后续会逐渐下线，具体下线策略请关注CCE官方公告。  >    - 若不配置，默认创建最新版本的集群。

        :return: The version of this AutopilotClusterSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AutopilotClusterSpec.

        集群版本，与Kubernetes社区基线版本保持一致，建议选择最新版本。  在CCE控制台支持创建两种最新版本的集群。可登录CCE控制台创建集群，在“版本”处获取到集群版本。 其它集群版本，当前仍可通过api创建，但后续会逐渐下线，具体下线策略请关注CCE官方公告。  >    - 若不配置，默认创建最新版本的集群。

        :param version: The version of this AutopilotClusterSpec.
        :type version: str
        """
        self._version = version

    @property
    def platform_version(self):
        r"""Gets the platform_version of this AutopilotClusterSpec.

        CCE集群平台版本号，表示集群版本(version)下的内部版本。用于跟踪某一集群版本内的迭代，集群版本内唯一，跨集群版本重新计数。不支持用户指定，集群创建时自动选择对应集群版本的最新平台版本。  platformVersion格式为：cce.X.Y - X: 表示内部特性版本。集群版本中特性或者补丁修复，或者OS支持等变更场景。其值从1开始单调递增。 - Y: 表示内部特性版本的补丁版本。仅用于特性版本上线后的软件包更新，不涉及其他修改。其值从0开始单调递增。 

        :return: The platform_version of this AutopilotClusterSpec.
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        r"""Sets the platform_version of this AutopilotClusterSpec.

        CCE集群平台版本号，表示集群版本(version)下的内部版本。用于跟踪某一集群版本内的迭代，集群版本内唯一，跨集群版本重新计数。不支持用户指定，集群创建时自动选择对应集群版本的最新平台版本。  platformVersion格式为：cce.X.Y - X: 表示内部特性版本。集群版本中特性或者补丁修复，或者OS支持等变更场景。其值从1开始单调递增。 - Y: 表示内部特性版本的补丁版本。仅用于特性版本上线后的软件包更新，不涉及其他修改。其值从0开始单调递增。 

        :param platform_version: The platform_version of this AutopilotClusterSpec.
        :type platform_version: str
        """
        self._platform_version = platform_version

    @property
    def description(self):
        r"""Gets the description of this AutopilotClusterSpec.

        集群描述，对于集群使用目的的描述，可根据实际情况自定义，默认为空。集群创建成功后可通过接口[更新指定的集群](cce_02_0240.xml)来做出修改，也可在CCE控制台中对应集群的“集群详情”下的“描述”处进行修改。仅支持utf-8编码。 

        :return: The description of this AutopilotClusterSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AutopilotClusterSpec.

        集群描述，对于集群使用目的的描述，可根据实际情况自定义，默认为空。集群创建成功后可通过接口[更新指定的集群](cce_02_0240.xml)来做出修改，也可在CCE控制台中对应集群的“集群详情”下的“描述”处进行修改。仅支持utf-8编码。 

        :param description: The description of this AutopilotClusterSpec.
        :type description: str
        """
        self._description = description

    @property
    def custom_san(self):
        r"""Gets the custom_san of this AutopilotClusterSpec.

        集群的API Server服务端证书中的自定义SAN（Subject Alternative Name）字段，遵从SSL标准X509定义的格式规范。  1. 不允许出现同名重复。 2. 格式符合IP和域名格式。  示例: ``` SAN 1: DNS Name=example.com SAN 2: DNS Name=www.example.com SAN 3: DNS Name=example.net SAN 4: IP Address=93.184.216.34 ```

        :return: The custom_san of this AutopilotClusterSpec.
        :rtype: list[str]
        """
        return self._custom_san

    @custom_san.setter
    def custom_san(self, custom_san):
        r"""Sets the custom_san of this AutopilotClusterSpec.

        集群的API Server服务端证书中的自定义SAN（Subject Alternative Name）字段，遵从SSL标准X509定义的格式规范。  1. 不允许出现同名重复。 2. 格式符合IP和域名格式。  示例: ``` SAN 1: DNS Name=example.com SAN 2: DNS Name=www.example.com SAN 3: DNS Name=example.net SAN 4: IP Address=93.184.216.34 ```

        :param custom_san: The custom_san of this AutopilotClusterSpec.
        :type custom_san: list[str]
        """
        self._custom_san = custom_san

    @property
    def enable_snat(self):
        r"""Gets the enable_snat of this AutopilotClusterSpec.

        集群是否配置SNAT。开启后您的集群可以通过NAT网关访问公网，默认使用所选的VPC中已有的NAT网关，否则系统将会为您自动创建一个默认规格的NAT网关并绑定弹性公网IP，自动配置SNAT规则。

        :return: The enable_snat of this AutopilotClusterSpec.
        :rtype: bool
        """
        return self._enable_snat

    @enable_snat.setter
    def enable_snat(self, enable_snat):
        r"""Sets the enable_snat of this AutopilotClusterSpec.

        集群是否配置SNAT。开启后您的集群可以通过NAT网关访问公网，默认使用所选的VPC中已有的NAT网关，否则系统将会为您自动创建一个默认规格的NAT网关并绑定弹性公网IP，自动配置SNAT规则。

        :param enable_snat: The enable_snat of this AutopilotClusterSpec.
        :type enable_snat: bool
        """
        self._enable_snat = enable_snat

    @property
    def enable_swr_image_access(self):
        r"""Gets the enable_swr_image_access of this AutopilotClusterSpec.

        集群是否配置镜像访问。为确保您的集群节点可以从容器镜像服务中拉取镜像，默认使用所选VPC中已有的SWR和OBS终端节点，否则将会为您自动新建SWR和OBS终端节点。

        :return: The enable_swr_image_access of this AutopilotClusterSpec.
        :rtype: bool
        """
        return self._enable_swr_image_access

    @enable_swr_image_access.setter
    def enable_swr_image_access(self, enable_swr_image_access):
        r"""Sets the enable_swr_image_access of this AutopilotClusterSpec.

        集群是否配置镜像访问。为确保您的集群节点可以从容器镜像服务中拉取镜像，默认使用所选VPC中已有的SWR和OBS终端节点，否则将会为您自动新建SWR和OBS终端节点。

        :param enable_swr_image_access: The enable_swr_image_access of this AutopilotClusterSpec.
        :type enable_swr_image_access: bool
        """
        self._enable_swr_image_access = enable_swr_image_access

    @property
    def ipv6enable(self):
        r"""Gets the ipv6enable of this AutopilotClusterSpec.

        集群是否使用IPv6模式。

        :return: The ipv6enable of this AutopilotClusterSpec.
        :rtype: bool
        """
        return self._ipv6enable

    @ipv6enable.setter
    def ipv6enable(self, ipv6enable):
        r"""Sets the ipv6enable of this AutopilotClusterSpec.

        集群是否使用IPv6模式。

        :param ipv6enable: The ipv6enable of this AutopilotClusterSpec.
        :type ipv6enable: bool
        """
        self._ipv6enable = ipv6enable

    @property
    def host_network(self):
        r"""Gets the host_network of this AutopilotClusterSpec.

        :return: The host_network of this AutopilotClusterSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.AutopilotHostNetwork`
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        r"""Sets the host_network of this AutopilotClusterSpec.

        :param host_network: The host_network of this AutopilotClusterSpec.
        :type host_network: :class:`huaweicloudsdkcce.v3.AutopilotHostNetwork`
        """
        self._host_network = host_network

    @property
    def container_network(self):
        r"""Gets the container_network of this AutopilotClusterSpec.

        :return: The container_network of this AutopilotClusterSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.AutopilotContainerNetwork`
        """
        return self._container_network

    @container_network.setter
    def container_network(self, container_network):
        r"""Sets the container_network of this AutopilotClusterSpec.

        :param container_network: The container_network of this AutopilotClusterSpec.
        :type container_network: :class:`huaweicloudsdkcce.v3.AutopilotContainerNetwork`
        """
        self._container_network = container_network

    @property
    def eni_network(self):
        r"""Gets the eni_network of this AutopilotClusterSpec.

        :return: The eni_network of this AutopilotClusterSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.AutopilotEniNetwork`
        """
        return self._eni_network

    @eni_network.setter
    def eni_network(self, eni_network):
        r"""Sets the eni_network of this AutopilotClusterSpec.

        :param eni_network: The eni_network of this AutopilotClusterSpec.
        :type eni_network: :class:`huaweicloudsdkcce.v3.AutopilotEniNetwork`
        """
        self._eni_network = eni_network

    @property
    def service_network(self):
        r"""Gets the service_network of this AutopilotClusterSpec.

        :return: The service_network of this AutopilotClusterSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.AutopilotServiceNetwork`
        """
        return self._service_network

    @service_network.setter
    def service_network(self, service_network):
        r"""Sets the service_network of this AutopilotClusterSpec.

        :param service_network: The service_network of this AutopilotClusterSpec.
        :type service_network: :class:`huaweicloudsdkcce.v3.AutopilotServiceNetwork`
        """
        self._service_network = service_network

    @property
    def authentication(self):
        r"""Gets the authentication of this AutopilotClusterSpec.

        :return: The authentication of this AutopilotClusterSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.AutopilotAuthentication`
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        r"""Sets the authentication of this AutopilotClusterSpec.

        :param authentication: The authentication of this AutopilotClusterSpec.
        :type authentication: :class:`huaweicloudsdkcce.v3.AutopilotAuthentication`
        """
        self._authentication = authentication

    @property
    def billing_mode(self):
        r"""Gets the billing_mode of this AutopilotClusterSpec.

        集群的计费方式。 - 0: 按需计费  默认为“按需计费”。 

        :return: The billing_mode of this AutopilotClusterSpec.
        :rtype: int
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        r"""Sets the billing_mode of this AutopilotClusterSpec.

        集群的计费方式。 - 0: 按需计费  默认为“按需计费”。 

        :param billing_mode: The billing_mode of this AutopilotClusterSpec.
        :type billing_mode: int
        """
        self._billing_mode = billing_mode

    @property
    def kubernetes_svc_ip_range(self):
        r"""Gets the kubernetes_svc_ip_range of this AutopilotClusterSpec.

        服务网段参数，kubernetes clusterIP取值范围。创建集群时如若未传参，默认为\"10.247.0.0/16\"。该参数废弃中，推荐使用新字段serviceNetwork，包含IPv4服务网段。 

        :return: The kubernetes_svc_ip_range of this AutopilotClusterSpec.
        :rtype: str
        """
        return self._kubernetes_svc_ip_range

    @kubernetes_svc_ip_range.setter
    def kubernetes_svc_ip_range(self, kubernetes_svc_ip_range):
        r"""Sets the kubernetes_svc_ip_range of this AutopilotClusterSpec.

        服务网段参数，kubernetes clusterIP取值范围。创建集群时如若未传参，默认为\"10.247.0.0/16\"。该参数废弃中，推荐使用新字段serviceNetwork，包含IPv4服务网段。 

        :param kubernetes_svc_ip_range: The kubernetes_svc_ip_range of this AutopilotClusterSpec.
        :type kubernetes_svc_ip_range: str
        """
        self._kubernetes_svc_ip_range = kubernetes_svc_ip_range

    @property
    def cluster_tags(self):
        r"""Gets the cluster_tags of this AutopilotClusterSpec.

        集群资源标签

        :return: The cluster_tags of this AutopilotClusterSpec.
        :rtype: list[:class:`huaweicloudsdkcce.v3.AutopilotResourceTag`]
        """
        return self._cluster_tags

    @cluster_tags.setter
    def cluster_tags(self, cluster_tags):
        r"""Sets the cluster_tags of this AutopilotClusterSpec.

        集群资源标签

        :param cluster_tags: The cluster_tags of this AutopilotClusterSpec.
        :type cluster_tags: list[:class:`huaweicloudsdkcce.v3.AutopilotResourceTag`]
        """
        self._cluster_tags = cluster_tags

    @property
    def kube_proxy_mode(self):
        r"""Gets the kube_proxy_mode of this AutopilotClusterSpec.

        服务转发模式：  - iptables：社区传统的kube-proxy模式，完全以iptables规则的方式来实现service负载均衡。该方式最主要的问题是在服务多的时候产生太多的iptables规则，非增量式更新会引入一定的时延，大规模情况下有明显的性能问题。  > 默认使用iptables转发模式。 

        :return: The kube_proxy_mode of this AutopilotClusterSpec.
        :rtype: str
        """
        return self._kube_proxy_mode

    @kube_proxy_mode.setter
    def kube_proxy_mode(self, kube_proxy_mode):
        r"""Sets the kube_proxy_mode of this AutopilotClusterSpec.

        服务转发模式：  - iptables：社区传统的kube-proxy模式，完全以iptables规则的方式来实现service负载均衡。该方式最主要的问题是在服务多的时候产生太多的iptables规则，非增量式更新会引入一定的时延，大规模情况下有明显的性能问题。  > 默认使用iptables转发模式。 

        :param kube_proxy_mode: The kube_proxy_mode of this AutopilotClusterSpec.
        :type kube_proxy_mode: str
        """
        self._kube_proxy_mode = kube_proxy_mode

    @property
    def az(self):
        r"""Gets the az of this AutopilotClusterSpec.

        可用区（仅查询返回字段）。  [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint?CCE)](tag:hws)  [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/intl/zh-cn/endpoint?CCE)](tag:hws_hk) 

        :return: The az of this AutopilotClusterSpec.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        r"""Sets the az of this AutopilotClusterSpec.

        可用区（仅查询返回字段）。  [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint?CCE)](tag:hws)  [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/intl/zh-cn/endpoint?CCE)](tag:hws_hk) 

        :param az: The az of this AutopilotClusterSpec.
        :type az: str
        """
        self._az = az

    @property
    def extend_param(self):
        r"""Gets the extend_param of this AutopilotClusterSpec.

        :return: The extend_param of this AutopilotClusterSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.AutopilotClusterExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this AutopilotClusterSpec.

        :param extend_param: The extend_param of this AutopilotClusterSpec.
        :type extend_param: :class:`huaweicloudsdkcce.v3.AutopilotClusterExtendParam`
        """
        self._extend_param = extend_param

    @property
    def configurations_override(self):
        r"""Gets the configurations_override of this AutopilotClusterSpec.

        覆盖集群默认组件配置  若指定了不支持的组件或组件不支持的参数，该配置项将被忽略。  当前支持的可配置组件及其参数详见 [[配置管理](https://support.huaweicloud.com/usermanual-cce/cce_10_0213.html)](tag:hws) [[配置管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0213.html)](tag:hws_hk) 

        :return: The configurations_override of this AutopilotClusterSpec.
        :rtype: list[:class:`huaweicloudsdkcce.v3.AutopilotPackageConfiguration`]
        """
        return self._configurations_override

    @configurations_override.setter
    def configurations_override(self, configurations_override):
        r"""Sets the configurations_override of this AutopilotClusterSpec.

        覆盖集群默认组件配置  若指定了不支持的组件或组件不支持的参数，该配置项将被忽略。  当前支持的可配置组件及其参数详见 [[配置管理](https://support.huaweicloud.com/usermanual-cce/cce_10_0213.html)](tag:hws) [[配置管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0213.html)](tag:hws_hk) 

        :param configurations_override: The configurations_override of this AutopilotClusterSpec.
        :type configurations_override: list[:class:`huaweicloudsdkcce.v3.AutopilotPackageConfiguration`]
        """
        self._configurations_override = configurations_override

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
        if not isinstance(other, AutopilotClusterSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
