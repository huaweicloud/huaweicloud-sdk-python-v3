# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterSpec:

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
        'ipv6enable': 'bool',
        'host_network': 'HostNetwork',
        'container_network': 'ContainerNetwork',
        'eni_network': 'EniNetwork',
        'service_network': 'ServiceNetwork',
        'authentication': 'Authentication',
        'billing_mode': 'int',
        'masters': 'list[MasterSpec]',
        'kubernetes_svc_ip_range': 'str',
        'cluster_tags': 'list[ResourceTag]',
        'kube_proxy_mode': 'str',
        'az': 'str',
        'extend_param': 'ClusterExtendParam',
        'support_istio': 'bool',
        'enable_master_volume_encryption': 'bool',
        'enable_dist_mgt': 'bool',
        'deletion_protection': 'bool',
        'configurations_override': 'list[PackageConfiguration]',
        'cluster_ops': 'ClusterOps',
        'encryption_config': 'EncryptionConfig'
    }

    attribute_map = {
        'category': 'category',
        'type': 'type',
        'flavor': 'flavor',
        'version': 'version',
        'platform_version': 'platformVersion',
        'description': 'description',
        'custom_san': 'customSan',
        'ipv6enable': 'ipv6enable',
        'host_network': 'hostNetwork',
        'container_network': 'containerNetwork',
        'eni_network': 'eniNetwork',
        'service_network': 'serviceNetwork',
        'authentication': 'authentication',
        'billing_mode': 'billingMode',
        'masters': 'masters',
        'kubernetes_svc_ip_range': 'kubernetesSvcIpRange',
        'cluster_tags': 'clusterTags',
        'kube_proxy_mode': 'kubeProxyMode',
        'az': 'az',
        'extend_param': 'extendParam',
        'support_istio': 'supportIstio',
        'enable_master_volume_encryption': 'enableMasterVolumeEncryption',
        'enable_dist_mgt': 'enableDistMgt',
        'deletion_protection': 'deletionProtection',
        'configurations_override': 'configurationsOverride',
        'cluster_ops': 'clusterOps',
        'encryption_config': 'encryptionConfig'
    }

    def __init__(self, category=None, type=None, flavor=None, version=None, platform_version=None, description=None, custom_san=None, ipv6enable=None, host_network=None, container_network=None, eni_network=None, service_network=None, authentication=None, billing_mode=None, masters=None, kubernetes_svc_ip_range=None, cluster_tags=None, kube_proxy_mode=None, az=None, extend_param=None, support_istio=None, enable_master_volume_encryption=None, enable_dist_mgt=None, deletion_protection=None, configurations_override=None, cluster_ops=None, encryption_config=None):
        r"""ClusterSpec

        The model defined in huaweicloud sdk

        :param category: 集群类别： - CCE：CCE集群   CCE集群支持虚拟机与裸金属服务器混合、GPU、NPU等异构节点的混合部署，基于高性能网络模型提供全方位、多场景、安全稳定的容器运行环境。 [- Turbo: CCE Turbo集群。   全面基于云原生基础设施构建的云原生2.0的容器引擎服务，具备软硬协同、网络无损、安全可靠、调度智能的优势，为用户提供一站式、高性价比的全新容器服务体验。](tag:hws,hws_hk,dt,hcs,g42,sbc) 
        :type category: str
        :param type: 集群Master节点架构：  - VirtualMachine：Master节点为x86架构服务器 [- ARM64: Master节点为鲲鹏（ARM架构）服务器](tag:hws,hws_hk,hcs) 
        :type type: str
        :param flavor: 集群规格，当集群为v1.15及以上版本时支持创建后变更，详情请参见[变更集群规格](ResizeCluster.xml)。请按实际业务需求进行选择： - cce.s1.small: 小规模单控制节点CCE集群（最大50节点） - cce.s1.medium: 中等规模单控制节点CCE集群（最大200节点） - cce.s2.small: 小规模多控制节点CCE集群（最大50节点） - cce.s2.medium: 中等规模多控制节点CCE集群（最大200节点） - cce.s2.large: 大规模多控制节点CCE集群（最大1000节点） - cce.s2.xlarge: 超大规模多控制节点CCE集群（最大2000节点）  &gt;    关于规格参数中的字段说明如下： &gt;    - s1：单控制节点的集群，控制节点数为1。单控制节点故障后，集群将不可用，但已运行工作负载不受影响。 &gt;    - s2：多控制节点的集群，即高可用集群，控制节点数为3。当某个控制节点故障时，集群仍然可用。 &gt;    [- dec：表示专属云的CCE集群规格。例如cce.dec.s1.small表示小规模单控制节点的专属云CCE集群（最大50节点）。](tag:hws,hws_hk) &gt;    - small：表示集群支持管理的最大节点规模为50节点。 &gt;    - medium：表示集群支持管理的最大节点规模为200节点。 &gt;    - large：表示集群支持管理的最大节点规模为1000节点。 &gt;    - xlarge：表示集群支持管理的最大节点规模为2000节点。 
        :type flavor: str
        :param version: 集群版本，与Kubernetes社区基线版本保持一致，建议选择最新版本。  在CCE控制台支持创建两种最新版本的集群。可登录CCE控制台创建集群，在“版本”处获取到集群版本。 其它集群版本，当前仍可通过api创建，但后续会逐渐下线，具体下线策略请关注CCE官方公告。  &gt;    - 若不配置，默认创建最新版本的集群。 &gt;    - 若指定集群基线版本但是不指定具体r版本，则系统默认选择对应集群版本的最新r版本。建议不指定具体r版本由系统选择最新版本。 [&gt;    - Turbo集群支持1.19及以上版本商用。](tag:hws,hws_hk,dt) [&gt;    - Turbo集群支持1.23及以上版本商用。](tag:hcs,g42,sbc)
        :type version: str
        :param platform_version: CCE集群平台版本号，表示集群版本(version)下的内部版本。用于跟踪某一集群版本内的迭代，集群版本内唯一，跨集群版本重新计数。不支持用户指定，集群创建时自动选择对应集群版本的最新平台版本。  platformVersion格式为：cce.X.Y - X: 表示内部特性版本。集群版本中特性或者补丁修复，或者OS支持等变更场景。其值从1开始单调递增。 - Y: 表示内部特性版本的补丁版本。仅用于特性版本上线后的软件包更新，不涉及其他修改。其值从0开始单调递增。 
        :type platform_version: str
        :param description: 集群描述，对于集群使用目的的描述，可根据实际情况自定义，默认为空。集群创建成功后可通过接口[更新指定的集群](cce_02_0240.xml)来做出修改，也可在CCE控制台中对应集群的“集群详情”下的“描述”处进行修改。仅支持utf-8编码。 
        :type description: str
        :param custom_san: 集群的API Server服务端证书中的自定义SAN（Subject Alternative Name）字段，遵从SSL标准X509定义的格式规范。  1. 不允许出现同名重复。 2. 格式符合IP和域名格式。  示例: &#x60;&#x60;&#x60; SAN 1: DNS Name&#x3D;example.com SAN 2: DNS Name&#x3D;www.example.com SAN 3: DNS Name&#x3D;example.net SAN 4: IP Address&#x3D;93.184.216.34 &#x60;&#x60;&#x60;
        :type custom_san: list[str]
        :param ipv6enable: 集群是否使用IPv6模式，1.15版本及以上支持。
        :type ipv6enable: bool
        :param host_network: 
        :type host_network: :class:`huaweicloudsdkcce.v3.HostNetwork`
        :param container_network: 
        :type container_network: :class:`huaweicloudsdkcce.v3.ContainerNetwork`
        :param eni_network: 
        :type eni_network: :class:`huaweicloudsdkcce.v3.EniNetwork`
        :param service_network: 
        :type service_network: :class:`huaweicloudsdkcce.v3.ServiceNetwork`
        :param authentication: 
        :type authentication: :class:`huaweicloudsdkcce.v3.Authentication`
        :param billing_mode: 集群的计费方式。 - 0: 按需计费 [- 1: 包周期](tag:hws,hws_hk)  默认为“按需计费”。 
        :type billing_mode: int
        :param masters: 控制节点的高级配置
        :type masters: list[:class:`huaweicloudsdkcce.v3.MasterSpec`]
        :param kubernetes_svc_ip_range: 服务网段参数，kubernetes clusterIP取值范围，1.11.7版本及以上支持。创建集群时如若未传参，默认为\&quot;10.247.0.0/16\&quot;。该参数废弃中，推荐使用新字段serviceNetwork，包含IPv4服务网段。 
        :type kubernetes_svc_ip_range: str
        :param cluster_tags: 集群资源标签
        :type cluster_tags: list[:class:`huaweicloudsdkcce.v3.ResourceTag`]
        :param kube_proxy_mode: 服务转发模式，支持以下两种实现：  - iptables：社区传统的kube-proxy模式，完全以iptables规则的方式来实现service负载均衡。该方式最主要的问题是在服务多的时候产生太多的iptables规则，非增量式更新会引入一定的时延，大规模情况下有明显的性能问题。 - ipvs：主导开发并在社区获得广泛支持的kube-proxy模式，采用增量式更新，吞吐更高，速度更快，并可以保证service更新期间连接保持不断开，适用于大规模场景。  &gt; 默认使用iptables转发模式。 
        :type kube_proxy_mode: str
        :param az: 可用区（仅查询返回字段）。  [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint?CCE)](tag:hws)  [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/intl/zh-cn/endpoint?CCE)](tag:hws_hk) 
        :type az: str
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcce.v3.ClusterExtendParam`
        :param support_istio: 支持Istio
        :type support_istio: bool
        :param enable_master_volume_encryption: 集群控制节点系统盘、数据盘加密。默认使用AES_256加密算法。CCE、Turbo集群1.25及以上版本开始支持。集群创建后不支持修改。开启后存在一定的磁盘读写性能损耗。
        :type enable_master_volume_encryption: bool
        :param enable_dist_mgt: 集群开启对分布式云支持。创建CCE Turbo集群时，可在创建集群过程中，开启对分布式云(cloudpond)支持。
        :type enable_dist_mgt: bool
        :param deletion_protection: 集群删除保护，默认为false关闭，如果开启后用户将无法删除该集群。
        :type deletion_protection: bool
        :param configurations_override: 覆盖集群默认组件配置  若指定了不支持的组件或组件不支持的参数，该配置项将被忽略。  当前支持的可配置组件及其参数详见 [[配置管理](https://support.huaweicloud.com/usermanual-cce/cce_10_0213.html)](tag:hws) [[配置管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0213.html)](tag:hws_hk) 
        :type configurations_override: list[:class:`huaweicloudsdkcce.v3.PackageConfiguration`]
        :param cluster_ops: 
        :type cluster_ops: :class:`huaweicloudsdkcce.v3.ClusterOps`
        :param encryption_config: 
        :type encryption_config: :class:`huaweicloudsdkcce.v3.EncryptionConfig`
        """
        
        

        self._category = None
        self._type = None
        self._flavor = None
        self._version = None
        self._platform_version = None
        self._description = None
        self._custom_san = None
        self._ipv6enable = None
        self._host_network = None
        self._container_network = None
        self._eni_network = None
        self._service_network = None
        self._authentication = None
        self._billing_mode = None
        self._masters = None
        self._kubernetes_svc_ip_range = None
        self._cluster_tags = None
        self._kube_proxy_mode = None
        self._az = None
        self._extend_param = None
        self._support_istio = None
        self._enable_master_volume_encryption = None
        self._enable_dist_mgt = None
        self._deletion_protection = None
        self._configurations_override = None
        self._cluster_ops = None
        self._encryption_config = None
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
        if ipv6enable is not None:
            self.ipv6enable = ipv6enable
        self.host_network = host_network
        self.container_network = container_network
        self.eni_network = eni_network
        if service_network is not None:
            self.service_network = service_network
        if authentication is not None:
            self.authentication = authentication
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if masters is not None:
            self.masters = masters
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
        if support_istio is not None:
            self.support_istio = support_istio
        if enable_master_volume_encryption is not None:
            self.enable_master_volume_encryption = enable_master_volume_encryption
        if enable_dist_mgt is not None:
            self.enable_dist_mgt = enable_dist_mgt
        if deletion_protection is not None:
            self.deletion_protection = deletion_protection
        if configurations_override is not None:
            self.configurations_override = configurations_override
        if cluster_ops is not None:
            self.cluster_ops = cluster_ops
        if encryption_config is not None:
            self.encryption_config = encryption_config

    @property
    def category(self):
        r"""Gets the category of this ClusterSpec.

        集群类别： - CCE：CCE集群   CCE集群支持虚拟机与裸金属服务器混合、GPU、NPU等异构节点的混合部署，基于高性能网络模型提供全方位、多场景、安全稳定的容器运行环境。 [- Turbo: CCE Turbo集群。   全面基于云原生基础设施构建的云原生2.0的容器引擎服务，具备软硬协同、网络无损、安全可靠、调度智能的优势，为用户提供一站式、高性价比的全新容器服务体验。](tag:hws,hws_hk,dt,hcs,g42,sbc) 

        :return: The category of this ClusterSpec.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ClusterSpec.

        集群类别： - CCE：CCE集群   CCE集群支持虚拟机与裸金属服务器混合、GPU、NPU等异构节点的混合部署，基于高性能网络模型提供全方位、多场景、安全稳定的容器运行环境。 [- Turbo: CCE Turbo集群。   全面基于云原生基础设施构建的云原生2.0的容器引擎服务，具备软硬协同、网络无损、安全可靠、调度智能的优势，为用户提供一站式、高性价比的全新容器服务体验。](tag:hws,hws_hk,dt,hcs,g42,sbc) 

        :param category: The category of this ClusterSpec.
        :type category: str
        """
        self._category = category

    @property
    def type(self):
        r"""Gets the type of this ClusterSpec.

        集群Master节点架构：  - VirtualMachine：Master节点为x86架构服务器 [- ARM64: Master节点为鲲鹏（ARM架构）服务器](tag:hws,hws_hk,hcs) 

        :return: The type of this ClusterSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ClusterSpec.

        集群Master节点架构：  - VirtualMachine：Master节点为x86架构服务器 [- ARM64: Master节点为鲲鹏（ARM架构）服务器](tag:hws,hws_hk,hcs) 

        :param type: The type of this ClusterSpec.
        :type type: str
        """
        self._type = type

    @property
    def flavor(self):
        r"""Gets the flavor of this ClusterSpec.

        集群规格，当集群为v1.15及以上版本时支持创建后变更，详情请参见[变更集群规格](ResizeCluster.xml)。请按实际业务需求进行选择： - cce.s1.small: 小规模单控制节点CCE集群（最大50节点） - cce.s1.medium: 中等规模单控制节点CCE集群（最大200节点） - cce.s2.small: 小规模多控制节点CCE集群（最大50节点） - cce.s2.medium: 中等规模多控制节点CCE集群（最大200节点） - cce.s2.large: 大规模多控制节点CCE集群（最大1000节点） - cce.s2.xlarge: 超大规模多控制节点CCE集群（最大2000节点）  >    关于规格参数中的字段说明如下： >    - s1：单控制节点的集群，控制节点数为1。单控制节点故障后，集群将不可用，但已运行工作负载不受影响。 >    - s2：多控制节点的集群，即高可用集群，控制节点数为3。当某个控制节点故障时，集群仍然可用。 >    [- dec：表示专属云的CCE集群规格。例如cce.dec.s1.small表示小规模单控制节点的专属云CCE集群（最大50节点）。](tag:hws,hws_hk) >    - small：表示集群支持管理的最大节点规模为50节点。 >    - medium：表示集群支持管理的最大节点规模为200节点。 >    - large：表示集群支持管理的最大节点规模为1000节点。 >    - xlarge：表示集群支持管理的最大节点规模为2000节点。 

        :return: The flavor of this ClusterSpec.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ClusterSpec.

        集群规格，当集群为v1.15及以上版本时支持创建后变更，详情请参见[变更集群规格](ResizeCluster.xml)。请按实际业务需求进行选择： - cce.s1.small: 小规模单控制节点CCE集群（最大50节点） - cce.s1.medium: 中等规模单控制节点CCE集群（最大200节点） - cce.s2.small: 小规模多控制节点CCE集群（最大50节点） - cce.s2.medium: 中等规模多控制节点CCE集群（最大200节点） - cce.s2.large: 大规模多控制节点CCE集群（最大1000节点） - cce.s2.xlarge: 超大规模多控制节点CCE集群（最大2000节点）  >    关于规格参数中的字段说明如下： >    - s1：单控制节点的集群，控制节点数为1。单控制节点故障后，集群将不可用，但已运行工作负载不受影响。 >    - s2：多控制节点的集群，即高可用集群，控制节点数为3。当某个控制节点故障时，集群仍然可用。 >    [- dec：表示专属云的CCE集群规格。例如cce.dec.s1.small表示小规模单控制节点的专属云CCE集群（最大50节点）。](tag:hws,hws_hk) >    - small：表示集群支持管理的最大节点规模为50节点。 >    - medium：表示集群支持管理的最大节点规模为200节点。 >    - large：表示集群支持管理的最大节点规模为1000节点。 >    - xlarge：表示集群支持管理的最大节点规模为2000节点。 

        :param flavor: The flavor of this ClusterSpec.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def version(self):
        r"""Gets the version of this ClusterSpec.

        集群版本，与Kubernetes社区基线版本保持一致，建议选择最新版本。  在CCE控制台支持创建两种最新版本的集群。可登录CCE控制台创建集群，在“版本”处获取到集群版本。 其它集群版本，当前仍可通过api创建，但后续会逐渐下线，具体下线策略请关注CCE官方公告。  >    - 若不配置，默认创建最新版本的集群。 >    - 若指定集群基线版本但是不指定具体r版本，则系统默认选择对应集群版本的最新r版本。建议不指定具体r版本由系统选择最新版本。 [>    - Turbo集群支持1.19及以上版本商用。](tag:hws,hws_hk,dt) [>    - Turbo集群支持1.23及以上版本商用。](tag:hcs,g42,sbc)

        :return: The version of this ClusterSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ClusterSpec.

        集群版本，与Kubernetes社区基线版本保持一致，建议选择最新版本。  在CCE控制台支持创建两种最新版本的集群。可登录CCE控制台创建集群，在“版本”处获取到集群版本。 其它集群版本，当前仍可通过api创建，但后续会逐渐下线，具体下线策略请关注CCE官方公告。  >    - 若不配置，默认创建最新版本的集群。 >    - 若指定集群基线版本但是不指定具体r版本，则系统默认选择对应集群版本的最新r版本。建议不指定具体r版本由系统选择最新版本。 [>    - Turbo集群支持1.19及以上版本商用。](tag:hws,hws_hk,dt) [>    - Turbo集群支持1.23及以上版本商用。](tag:hcs,g42,sbc)

        :param version: The version of this ClusterSpec.
        :type version: str
        """
        self._version = version

    @property
    def platform_version(self):
        r"""Gets the platform_version of this ClusterSpec.

        CCE集群平台版本号，表示集群版本(version)下的内部版本。用于跟踪某一集群版本内的迭代，集群版本内唯一，跨集群版本重新计数。不支持用户指定，集群创建时自动选择对应集群版本的最新平台版本。  platformVersion格式为：cce.X.Y - X: 表示内部特性版本。集群版本中特性或者补丁修复，或者OS支持等变更场景。其值从1开始单调递增。 - Y: 表示内部特性版本的补丁版本。仅用于特性版本上线后的软件包更新，不涉及其他修改。其值从0开始单调递增。 

        :return: The platform_version of this ClusterSpec.
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        r"""Sets the platform_version of this ClusterSpec.

        CCE集群平台版本号，表示集群版本(version)下的内部版本。用于跟踪某一集群版本内的迭代，集群版本内唯一，跨集群版本重新计数。不支持用户指定，集群创建时自动选择对应集群版本的最新平台版本。  platformVersion格式为：cce.X.Y - X: 表示内部特性版本。集群版本中特性或者补丁修复，或者OS支持等变更场景。其值从1开始单调递增。 - Y: 表示内部特性版本的补丁版本。仅用于特性版本上线后的软件包更新，不涉及其他修改。其值从0开始单调递增。 

        :param platform_version: The platform_version of this ClusterSpec.
        :type platform_version: str
        """
        self._platform_version = platform_version

    @property
    def description(self):
        r"""Gets the description of this ClusterSpec.

        集群描述，对于集群使用目的的描述，可根据实际情况自定义，默认为空。集群创建成功后可通过接口[更新指定的集群](cce_02_0240.xml)来做出修改，也可在CCE控制台中对应集群的“集群详情”下的“描述”处进行修改。仅支持utf-8编码。 

        :return: The description of this ClusterSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ClusterSpec.

        集群描述，对于集群使用目的的描述，可根据实际情况自定义，默认为空。集群创建成功后可通过接口[更新指定的集群](cce_02_0240.xml)来做出修改，也可在CCE控制台中对应集群的“集群详情”下的“描述”处进行修改。仅支持utf-8编码。 

        :param description: The description of this ClusterSpec.
        :type description: str
        """
        self._description = description

    @property
    def custom_san(self):
        r"""Gets the custom_san of this ClusterSpec.

        集群的API Server服务端证书中的自定义SAN（Subject Alternative Name）字段，遵从SSL标准X509定义的格式规范。  1. 不允许出现同名重复。 2. 格式符合IP和域名格式。  示例: ``` SAN 1: DNS Name=example.com SAN 2: DNS Name=www.example.com SAN 3: DNS Name=example.net SAN 4: IP Address=93.184.216.34 ```

        :return: The custom_san of this ClusterSpec.
        :rtype: list[str]
        """
        return self._custom_san

    @custom_san.setter
    def custom_san(self, custom_san):
        r"""Sets the custom_san of this ClusterSpec.

        集群的API Server服务端证书中的自定义SAN（Subject Alternative Name）字段，遵从SSL标准X509定义的格式规范。  1. 不允许出现同名重复。 2. 格式符合IP和域名格式。  示例: ``` SAN 1: DNS Name=example.com SAN 2: DNS Name=www.example.com SAN 3: DNS Name=example.net SAN 4: IP Address=93.184.216.34 ```

        :param custom_san: The custom_san of this ClusterSpec.
        :type custom_san: list[str]
        """
        self._custom_san = custom_san

    @property
    def ipv6enable(self):
        r"""Gets the ipv6enable of this ClusterSpec.

        集群是否使用IPv6模式，1.15版本及以上支持。

        :return: The ipv6enable of this ClusterSpec.
        :rtype: bool
        """
        return self._ipv6enable

    @ipv6enable.setter
    def ipv6enable(self, ipv6enable):
        r"""Sets the ipv6enable of this ClusterSpec.

        集群是否使用IPv6模式，1.15版本及以上支持。

        :param ipv6enable: The ipv6enable of this ClusterSpec.
        :type ipv6enable: bool
        """
        self._ipv6enable = ipv6enable

    @property
    def host_network(self):
        r"""Gets the host_network of this ClusterSpec.

        :return: The host_network of this ClusterSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.HostNetwork`
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        r"""Sets the host_network of this ClusterSpec.

        :param host_network: The host_network of this ClusterSpec.
        :type host_network: :class:`huaweicloudsdkcce.v3.HostNetwork`
        """
        self._host_network = host_network

    @property
    def container_network(self):
        r"""Gets the container_network of this ClusterSpec.

        :return: The container_network of this ClusterSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.ContainerNetwork`
        """
        return self._container_network

    @container_network.setter
    def container_network(self, container_network):
        r"""Sets the container_network of this ClusterSpec.

        :param container_network: The container_network of this ClusterSpec.
        :type container_network: :class:`huaweicloudsdkcce.v3.ContainerNetwork`
        """
        self._container_network = container_network

    @property
    def eni_network(self):
        r"""Gets the eni_network of this ClusterSpec.

        :return: The eni_network of this ClusterSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.EniNetwork`
        """
        return self._eni_network

    @eni_network.setter
    def eni_network(self, eni_network):
        r"""Sets the eni_network of this ClusterSpec.

        :param eni_network: The eni_network of this ClusterSpec.
        :type eni_network: :class:`huaweicloudsdkcce.v3.EniNetwork`
        """
        self._eni_network = eni_network

    @property
    def service_network(self):
        r"""Gets the service_network of this ClusterSpec.

        :return: The service_network of this ClusterSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.ServiceNetwork`
        """
        return self._service_network

    @service_network.setter
    def service_network(self, service_network):
        r"""Sets the service_network of this ClusterSpec.

        :param service_network: The service_network of this ClusterSpec.
        :type service_network: :class:`huaweicloudsdkcce.v3.ServiceNetwork`
        """
        self._service_network = service_network

    @property
    def authentication(self):
        r"""Gets the authentication of this ClusterSpec.

        :return: The authentication of this ClusterSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.Authentication`
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        r"""Sets the authentication of this ClusterSpec.

        :param authentication: The authentication of this ClusterSpec.
        :type authentication: :class:`huaweicloudsdkcce.v3.Authentication`
        """
        self._authentication = authentication

    @property
    def billing_mode(self):
        r"""Gets the billing_mode of this ClusterSpec.

        集群的计费方式。 - 0: 按需计费 [- 1: 包周期](tag:hws,hws_hk)  默认为“按需计费”。 

        :return: The billing_mode of this ClusterSpec.
        :rtype: int
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        r"""Sets the billing_mode of this ClusterSpec.

        集群的计费方式。 - 0: 按需计费 [- 1: 包周期](tag:hws,hws_hk)  默认为“按需计费”。 

        :param billing_mode: The billing_mode of this ClusterSpec.
        :type billing_mode: int
        """
        self._billing_mode = billing_mode

    @property
    def masters(self):
        r"""Gets the masters of this ClusterSpec.

        控制节点的高级配置

        :return: The masters of this ClusterSpec.
        :rtype: list[:class:`huaweicloudsdkcce.v3.MasterSpec`]
        """
        return self._masters

    @masters.setter
    def masters(self, masters):
        r"""Sets the masters of this ClusterSpec.

        控制节点的高级配置

        :param masters: The masters of this ClusterSpec.
        :type masters: list[:class:`huaweicloudsdkcce.v3.MasterSpec`]
        """
        self._masters = masters

    @property
    def kubernetes_svc_ip_range(self):
        r"""Gets the kubernetes_svc_ip_range of this ClusterSpec.

        服务网段参数，kubernetes clusterIP取值范围，1.11.7版本及以上支持。创建集群时如若未传参，默认为\"10.247.0.0/16\"。该参数废弃中，推荐使用新字段serviceNetwork，包含IPv4服务网段。 

        :return: The kubernetes_svc_ip_range of this ClusterSpec.
        :rtype: str
        """
        return self._kubernetes_svc_ip_range

    @kubernetes_svc_ip_range.setter
    def kubernetes_svc_ip_range(self, kubernetes_svc_ip_range):
        r"""Sets the kubernetes_svc_ip_range of this ClusterSpec.

        服务网段参数，kubernetes clusterIP取值范围，1.11.7版本及以上支持。创建集群时如若未传参，默认为\"10.247.0.0/16\"。该参数废弃中，推荐使用新字段serviceNetwork，包含IPv4服务网段。 

        :param kubernetes_svc_ip_range: The kubernetes_svc_ip_range of this ClusterSpec.
        :type kubernetes_svc_ip_range: str
        """
        self._kubernetes_svc_ip_range = kubernetes_svc_ip_range

    @property
    def cluster_tags(self):
        r"""Gets the cluster_tags of this ClusterSpec.

        集群资源标签

        :return: The cluster_tags of this ClusterSpec.
        :rtype: list[:class:`huaweicloudsdkcce.v3.ResourceTag`]
        """
        return self._cluster_tags

    @cluster_tags.setter
    def cluster_tags(self, cluster_tags):
        r"""Sets the cluster_tags of this ClusterSpec.

        集群资源标签

        :param cluster_tags: The cluster_tags of this ClusterSpec.
        :type cluster_tags: list[:class:`huaweicloudsdkcce.v3.ResourceTag`]
        """
        self._cluster_tags = cluster_tags

    @property
    def kube_proxy_mode(self):
        r"""Gets the kube_proxy_mode of this ClusterSpec.

        服务转发模式，支持以下两种实现：  - iptables：社区传统的kube-proxy模式，完全以iptables规则的方式来实现service负载均衡。该方式最主要的问题是在服务多的时候产生太多的iptables规则，非增量式更新会引入一定的时延，大规模情况下有明显的性能问题。 - ipvs：主导开发并在社区获得广泛支持的kube-proxy模式，采用增量式更新，吞吐更高，速度更快，并可以保证service更新期间连接保持不断开，适用于大规模场景。  > 默认使用iptables转发模式。 

        :return: The kube_proxy_mode of this ClusterSpec.
        :rtype: str
        """
        return self._kube_proxy_mode

    @kube_proxy_mode.setter
    def kube_proxy_mode(self, kube_proxy_mode):
        r"""Sets the kube_proxy_mode of this ClusterSpec.

        服务转发模式，支持以下两种实现：  - iptables：社区传统的kube-proxy模式，完全以iptables规则的方式来实现service负载均衡。该方式最主要的问题是在服务多的时候产生太多的iptables规则，非增量式更新会引入一定的时延，大规模情况下有明显的性能问题。 - ipvs：主导开发并在社区获得广泛支持的kube-proxy模式，采用增量式更新，吞吐更高，速度更快，并可以保证service更新期间连接保持不断开，适用于大规模场景。  > 默认使用iptables转发模式。 

        :param kube_proxy_mode: The kube_proxy_mode of this ClusterSpec.
        :type kube_proxy_mode: str
        """
        self._kube_proxy_mode = kube_proxy_mode

    @property
    def az(self):
        r"""Gets the az of this ClusterSpec.

        可用区（仅查询返回字段）。  [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint?CCE)](tag:hws)  [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/intl/zh-cn/endpoint?CCE)](tag:hws_hk) 

        :return: The az of this ClusterSpec.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        r"""Sets the az of this ClusterSpec.

        可用区（仅查询返回字段）。  [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint?CCE)](tag:hws)  [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/intl/zh-cn/endpoint?CCE)](tag:hws_hk) 

        :param az: The az of this ClusterSpec.
        :type az: str
        """
        self._az = az

    @property
    def extend_param(self):
        r"""Gets the extend_param of this ClusterSpec.

        :return: The extend_param of this ClusterSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.ClusterExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this ClusterSpec.

        :param extend_param: The extend_param of this ClusterSpec.
        :type extend_param: :class:`huaweicloudsdkcce.v3.ClusterExtendParam`
        """
        self._extend_param = extend_param

    @property
    def support_istio(self):
        r"""Gets the support_istio of this ClusterSpec.

        支持Istio

        :return: The support_istio of this ClusterSpec.
        :rtype: bool
        """
        return self._support_istio

    @support_istio.setter
    def support_istio(self, support_istio):
        r"""Sets the support_istio of this ClusterSpec.

        支持Istio

        :param support_istio: The support_istio of this ClusterSpec.
        :type support_istio: bool
        """
        self._support_istio = support_istio

    @property
    def enable_master_volume_encryption(self):
        r"""Gets the enable_master_volume_encryption of this ClusterSpec.

        集群控制节点系统盘、数据盘加密。默认使用AES_256加密算法。CCE、Turbo集群1.25及以上版本开始支持。集群创建后不支持修改。开启后存在一定的磁盘读写性能损耗。

        :return: The enable_master_volume_encryption of this ClusterSpec.
        :rtype: bool
        """
        return self._enable_master_volume_encryption

    @enable_master_volume_encryption.setter
    def enable_master_volume_encryption(self, enable_master_volume_encryption):
        r"""Sets the enable_master_volume_encryption of this ClusterSpec.

        集群控制节点系统盘、数据盘加密。默认使用AES_256加密算法。CCE、Turbo集群1.25及以上版本开始支持。集群创建后不支持修改。开启后存在一定的磁盘读写性能损耗。

        :param enable_master_volume_encryption: The enable_master_volume_encryption of this ClusterSpec.
        :type enable_master_volume_encryption: bool
        """
        self._enable_master_volume_encryption = enable_master_volume_encryption

    @property
    def enable_dist_mgt(self):
        r"""Gets the enable_dist_mgt of this ClusterSpec.

        集群开启对分布式云支持。创建CCE Turbo集群时，可在创建集群过程中，开启对分布式云(cloudpond)支持。

        :return: The enable_dist_mgt of this ClusterSpec.
        :rtype: bool
        """
        return self._enable_dist_mgt

    @enable_dist_mgt.setter
    def enable_dist_mgt(self, enable_dist_mgt):
        r"""Sets the enable_dist_mgt of this ClusterSpec.

        集群开启对分布式云支持。创建CCE Turbo集群时，可在创建集群过程中，开启对分布式云(cloudpond)支持。

        :param enable_dist_mgt: The enable_dist_mgt of this ClusterSpec.
        :type enable_dist_mgt: bool
        """
        self._enable_dist_mgt = enable_dist_mgt

    @property
    def deletion_protection(self):
        r"""Gets the deletion_protection of this ClusterSpec.

        集群删除保护，默认为false关闭，如果开启后用户将无法删除该集群。

        :return: The deletion_protection of this ClusterSpec.
        :rtype: bool
        """
        return self._deletion_protection

    @deletion_protection.setter
    def deletion_protection(self, deletion_protection):
        r"""Sets the deletion_protection of this ClusterSpec.

        集群删除保护，默认为false关闭，如果开启后用户将无法删除该集群。

        :param deletion_protection: The deletion_protection of this ClusterSpec.
        :type deletion_protection: bool
        """
        self._deletion_protection = deletion_protection

    @property
    def configurations_override(self):
        r"""Gets the configurations_override of this ClusterSpec.

        覆盖集群默认组件配置  若指定了不支持的组件或组件不支持的参数，该配置项将被忽略。  当前支持的可配置组件及其参数详见 [[配置管理](https://support.huaweicloud.com/usermanual-cce/cce_10_0213.html)](tag:hws) [[配置管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0213.html)](tag:hws_hk) 

        :return: The configurations_override of this ClusterSpec.
        :rtype: list[:class:`huaweicloudsdkcce.v3.PackageConfiguration`]
        """
        return self._configurations_override

    @configurations_override.setter
    def configurations_override(self, configurations_override):
        r"""Sets the configurations_override of this ClusterSpec.

        覆盖集群默认组件配置  若指定了不支持的组件或组件不支持的参数，该配置项将被忽略。  当前支持的可配置组件及其参数详见 [[配置管理](https://support.huaweicloud.com/usermanual-cce/cce_10_0213.html)](tag:hws) [[配置管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0213.html)](tag:hws_hk) 

        :param configurations_override: The configurations_override of this ClusterSpec.
        :type configurations_override: list[:class:`huaweicloudsdkcce.v3.PackageConfiguration`]
        """
        self._configurations_override = configurations_override

    @property
    def cluster_ops(self):
        r"""Gets the cluster_ops of this ClusterSpec.

        :return: The cluster_ops of this ClusterSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.ClusterOps`
        """
        return self._cluster_ops

    @cluster_ops.setter
    def cluster_ops(self, cluster_ops):
        r"""Sets the cluster_ops of this ClusterSpec.

        :param cluster_ops: The cluster_ops of this ClusterSpec.
        :type cluster_ops: :class:`huaweicloudsdkcce.v3.ClusterOps`
        """
        self._cluster_ops = cluster_ops

    @property
    def encryption_config(self):
        r"""Gets the encryption_config of this ClusterSpec.

        :return: The encryption_config of this ClusterSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.EncryptionConfig`
        """
        return self._encryption_config

    @encryption_config.setter
    def encryption_config(self, encryption_config):
        r"""Sets the encryption_config of this ClusterSpec.

        :param encryption_config: The encryption_config of this ClusterSpec.
        :type encryption_config: :class:`huaweicloudsdkcce.v3.EncryptionConfig`
        """
        self._encryption_config = encryption_config

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
        if not isinstance(other, ClusterSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
