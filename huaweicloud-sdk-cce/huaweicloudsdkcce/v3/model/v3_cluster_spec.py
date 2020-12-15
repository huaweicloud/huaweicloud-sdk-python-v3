# coding: utf-8

import pprint
import re

import six





class V3ClusterSpec:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'authentication': 'Authentication',
        'az': 'str',
        'billing_mode': 'int',
        'cluster_tags': 'list[ResourceTag]',
        'container_network': 'ContainerNetwork',
        'description': 'str',
        'eni_network': 'ENINetwork',
        'extend_param': 'dict(str, str)',
        'flavor': 'str',
        'host_network': 'HostNetwork',
        'ipv6enable': 'bool',
        'kube_proxy_mode': 'str',
        'kubernetes_svc_ip_range': 'str',
        'masters': 'list[MasterSpec]',
        'support_istio': 'bool',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'authentication': 'authentication',
        'az': 'az',
        'billing_mode': 'billingMode',
        'cluster_tags': 'clusterTags',
        'container_network': 'containerNetwork',
        'description': 'description',
        'eni_network': 'eniNetwork',
        'extend_param': 'extendParam',
        'flavor': 'flavor',
        'host_network': 'hostNetwork',
        'ipv6enable': 'ipv6enable',
        'kube_proxy_mode': 'kubeProxyMode',
        'kubernetes_svc_ip_range': 'kubernetesSvcIpRange',
        'masters': 'masters',
        'support_istio': 'supportIstio',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, authentication=None, az=None, billing_mode=0, cluster_tags=None, container_network=None, description=None, eni_network=None, extend_param=None, flavor=None, host_network=None, ipv6enable=None, kube_proxy_mode=None, kubernetes_svc_ip_range=None, masters=None, support_istio=None, type=None, version=None):
        """V3ClusterSpec - a model defined in huaweicloud sdk"""
        
        

        self._authentication = None
        self._az = None
        self._billing_mode = None
        self._cluster_tags = None
        self._container_network = None
        self._description = None
        self._eni_network = None
        self._extend_param = None
        self._flavor = None
        self._host_network = None
        self._ipv6enable = None
        self._kube_proxy_mode = None
        self._kubernetes_svc_ip_range = None
        self._masters = None
        self._support_istio = None
        self._type = None
        self._version = None
        self.discriminator = None

        if authentication is not None:
            self.authentication = authentication
        if az is not None:
            self.az = az
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if cluster_tags is not None:
            self.cluster_tags = cluster_tags
        self.container_network = container_network
        if description is not None:
            self.description = description
        if eni_network is not None:
            self.eni_network = eni_network
        if extend_param is not None:
            self.extend_param = extend_param
        self.flavor = flavor
        self.host_network = host_network
        if ipv6enable is not None:
            self.ipv6enable = ipv6enable
        if kube_proxy_mode is not None:
            self.kube_proxy_mode = kube_proxy_mode
        if kubernetes_svc_ip_range is not None:
            self.kubernetes_svc_ip_range = kubernetes_svc_ip_range
        if masters is not None:
            self.masters = masters
        if support_istio is not None:
            self.support_istio = support_istio
        self.type = type
        if version is not None:
            self.version = version

    @property
    def authentication(self):
        """Gets the authentication of this V3ClusterSpec.


        :return: The authentication of this V3ClusterSpec.
        :rtype: Authentication
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this V3ClusterSpec.


        :param authentication: The authentication of this V3ClusterSpec.
        :type: Authentication
        """
        self._authentication = authentication

    @property
    def az(self):
        """Gets the az of this V3ClusterSpec.

        可用区（仅查询返回字段）

        :return: The az of this V3ClusterSpec.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        """Sets the az of this V3ClusterSpec.

        可用区（仅查询返回字段）

        :param az: The az of this V3ClusterSpec.
        :type: str
        """
        self._az = az

    @property
    def billing_mode(self):
        """Gets the billing_mode of this V3ClusterSpec.

        集群的计费方式，当前接口只支持创建“按需计费”的集群。计费方式为“按需计费”时，取值为“0”。若不填，则默认为“0”。

        :return: The billing_mode of this V3ClusterSpec.
        :rtype: int
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        """Sets the billing_mode of this V3ClusterSpec.

        集群的计费方式，当前接口只支持创建“按需计费”的集群。计费方式为“按需计费”时，取值为“0”。若不填，则默认为“0”。

        :param billing_mode: The billing_mode of this V3ClusterSpec.
        :type: int
        """
        self._billing_mode = billing_mode

    @property
    def cluster_tags(self):
        """Gets the cluster_tags of this V3ClusterSpec.

        集群资源标签

        :return: The cluster_tags of this V3ClusterSpec.
        :rtype: list[ResourceTag]
        """
        return self._cluster_tags

    @cluster_tags.setter
    def cluster_tags(self, cluster_tags):
        """Sets the cluster_tags of this V3ClusterSpec.

        集群资源标签

        :param cluster_tags: The cluster_tags of this V3ClusterSpec.
        :type: list[ResourceTag]
        """
        self._cluster_tags = cluster_tags

    @property
    def container_network(self):
        """Gets the container_network of this V3ClusterSpec.


        :return: The container_network of this V3ClusterSpec.
        :rtype: ContainerNetwork
        """
        return self._container_network

    @container_network.setter
    def container_network(self, container_network):
        """Sets the container_network of this V3ClusterSpec.


        :param container_network: The container_network of this V3ClusterSpec.
        :type: ContainerNetwork
        """
        self._container_network = container_network

    @property
    def description(self):
        """Gets the description of this V3ClusterSpec.

        集群描述，对于集群使用目的的描述，可根据实际情况自定义，默认为空。集群创建成功后可通过接口[更新指定的集群](https://support.huaweicloud.com/api-cce/cce_02_0240.html)来做出修改，也可在CCE控制台中对应集群的“集群详情”下的“描述”处进行修改。仅支持utf-8编码。

        :return: The description of this V3ClusterSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V3ClusterSpec.

        集群描述，对于集群使用目的的描述，可根据实际情况自定义，默认为空。集群创建成功后可通过接口[更新指定的集群](https://support.huaweicloud.com/api-cce/cce_02_0240.html)来做出修改，也可在CCE控制台中对应集群的“集群详情”下的“描述”处进行修改。仅支持utf-8编码。

        :param description: The description of this V3ClusterSpec.
        :type: str
        """
        self._description = description

    @property
    def eni_network(self):
        """Gets the eni_network of this V3ClusterSpec.


        :return: The eni_network of this V3ClusterSpec.
        :rtype: ENINetwork
        """
        return self._eni_network

    @eni_network.setter
    def eni_network(self, eni_network):
        """Sets the eni_network of this V3ClusterSpec.


        :param eni_network: The eni_network of this V3ClusterSpec.
        :type: ENINetwork
        """
        self._eni_network = eni_network

    @property
    def extend_param(self):
        """Gets the extend_param of this V3ClusterSpec.

        扩展字段，key/value对格式。可配置多可用区集群、专属混合集群，以及将集群创建在特定的企业项目下。可配置的key/value对如下： - clusterAZ: 集群控制节点可用区配置。   - multi_az：多可用区，可选。仅使用高可用集群时才可以配置多可用区。   - 专属云计算池可用区：用于指定专属云可用区部署集群控制节点。   如果需配置专属混合集群，该字段为必选。例如“华北四-可用区一”取值为：cn-north-4a。更多信息请参见[什么是专属计算集群？](https://support.huaweicloud.com/productdesc-dcc/zh-cn_topic_0016310838.html) - dssMasterVolumes: 用于指定控制节点的系统盘和数据盘使用专属分布式存储，未指定或者值为空时，默认使用EVS云硬盘。   如果配置专属混合集群，该字段为必选，请按照如下格式设置：   ```   <rootVol.dssPoolID>.<rootVol.volType>;<dataVol.dssPoolID>.<dataVol.volType>   ```   字段说明：   rootVol为系统盘；dataVol为数据盘；   dssPoolID为专属分布式存储池ID；   volType为专属分布式存储池的存储类型，如SAS、SSD。   样例：c950ee97-587c-4f24-8a74-3367e3da570f.sas;6edbc2f4-1507-44f8-ac0d-eed1d2608d38.ssd   非专属混合集群不支持配置该字段。 - enterpriseProjectId:   如果需要将集群创建在特定的企业项目下，请设置{\"enterpriseProjectId\":\"xxx\"}的key/value对。   >   - 需要开通企业项目功能后才可配置企业项目，详情请参见 [如何进入企业管理页面](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0108763975.html)。   >   - 集群所属的企业项目与集群下所关联的其他云服务资源所属的企业项目必须保持一致。 - kubeProxyMode:   服务转发模式，支持以下两种实现：   - iptables：社区传统的kube-proxy模式，完全以iptables规则的方式来实现service负载均衡。该方式最主要的问题是在服务多的时候产生太多的iptables规则，非增量式更新会引入一定的时延，大规模情况下有明显的性能问题   - ipvs：主导开发并在社区获得广泛支持的kube-proxy模式，采用增量式更新，吞吐更高，速度更快，并可以保证service更新期间连接保持不断开，适用于大规模场景。 - clusterExternalIP: master 弹性公网IP - alpha.cce/fixPoolMask:    容器网络固定IP池掩码位数，仅vpc-router支持。   整数字符传取值范围: 24 ~ 28 - decMasterFlavor: 专属混合集群指定可控制节点的规格。最大长度255。 - dockerUmaskMode: 集群默认Docker的UmaskMode配置，可取值为secure或normal，不指定时默认为normal。 - kubernetes.io/cpuManagerPolicy:    集群CPU管理策略。取值为none或static，默认为none。   - none：关闭工作负载实例独占CPU核的功能，优点是CPU共享池的可分配核数较多   - static：支持给工作负载实例配置CPU独占，适用于对CPU缓存和调度延迟敏感的工作负载。 

        :return: The extend_param of this V3ClusterSpec.
        :rtype: dict(str, str)
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this V3ClusterSpec.

        扩展字段，key/value对格式。可配置多可用区集群、专属混合集群，以及将集群创建在特定的企业项目下。可配置的key/value对如下： - clusterAZ: 集群控制节点可用区配置。   - multi_az：多可用区，可选。仅使用高可用集群时才可以配置多可用区。   - 专属云计算池可用区：用于指定专属云可用区部署集群控制节点。   如果需配置专属混合集群，该字段为必选。例如“华北四-可用区一”取值为：cn-north-4a。更多信息请参见[什么是专属计算集群？](https://support.huaweicloud.com/productdesc-dcc/zh-cn_topic_0016310838.html) - dssMasterVolumes: 用于指定控制节点的系统盘和数据盘使用专属分布式存储，未指定或者值为空时，默认使用EVS云硬盘。   如果配置专属混合集群，该字段为必选，请按照如下格式设置：   ```   <rootVol.dssPoolID>.<rootVol.volType>;<dataVol.dssPoolID>.<dataVol.volType>   ```   字段说明：   rootVol为系统盘；dataVol为数据盘；   dssPoolID为专属分布式存储池ID；   volType为专属分布式存储池的存储类型，如SAS、SSD。   样例：c950ee97-587c-4f24-8a74-3367e3da570f.sas;6edbc2f4-1507-44f8-ac0d-eed1d2608d38.ssd   非专属混合集群不支持配置该字段。 - enterpriseProjectId:   如果需要将集群创建在特定的企业项目下，请设置{\"enterpriseProjectId\":\"xxx\"}的key/value对。   >   - 需要开通企业项目功能后才可配置企业项目，详情请参见 [如何进入企业管理页面](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0108763975.html)。   >   - 集群所属的企业项目与集群下所关联的其他云服务资源所属的企业项目必须保持一致。 - kubeProxyMode:   服务转发模式，支持以下两种实现：   - iptables：社区传统的kube-proxy模式，完全以iptables规则的方式来实现service负载均衡。该方式最主要的问题是在服务多的时候产生太多的iptables规则，非增量式更新会引入一定的时延，大规模情况下有明显的性能问题   - ipvs：主导开发并在社区获得广泛支持的kube-proxy模式，采用增量式更新，吞吐更高，速度更快，并可以保证service更新期间连接保持不断开，适用于大规模场景。 - clusterExternalIP: master 弹性公网IP - alpha.cce/fixPoolMask:    容器网络固定IP池掩码位数，仅vpc-router支持。   整数字符传取值范围: 24 ~ 28 - decMasterFlavor: 专属混合集群指定可控制节点的规格。最大长度255。 - dockerUmaskMode: 集群默认Docker的UmaskMode配置，可取值为secure或normal，不指定时默认为normal。 - kubernetes.io/cpuManagerPolicy:    集群CPU管理策略。取值为none或static，默认为none。   - none：关闭工作负载实例独占CPU核的功能，优点是CPU共享池的可分配核数较多   - static：支持给工作负载实例配置CPU独占，适用于对CPU缓存和调度延迟敏感的工作负载。 

        :param extend_param: The extend_param of this V3ClusterSpec.
        :type: dict(str, str)
        """
        self._extend_param = extend_param

    @property
    def flavor(self):
        """Gets the flavor of this V3ClusterSpec.

        字段默认值：创建混合集群或鲲鹏集群时，如果是非专属云为 cce.s1.small，专属云则为 cce.dec.s1.small；  集群规格，集群创建完成后规格不可再变更，请按实际业务需求进行选择：  - cce.s1.small: 小规模单控制节点混合集群（最大50节点） - cce.s1.medium: 中等规模单控制节点混合集群（最大200节点） - cce.s2.small: 小规模多控制节点混合集群（最大50节点） - cce.s2.medium: 中等规模多控制节点混合集群（最大200节点） - cce.s2.large: 大规模多控制节点混合集群（最大1000节点） - cce.s2.xlarge: 超大规模多控制节点混合集群（最大2000节点）  > s1：单控制节点混合集群。 >  > s2：多控制节点混合集群。 >  > dec：专属混合集群规格。如cce.dec.s1.small为小规模单控制节点专属混合集群（最大50节点）。 >  > 最大节点数：当前集群支持管理的最大节点规模，请根据业务需求选择。 >  > 单控制节点集群：普通集群是单控制节点，控制节点故障后，集群将不可用，但已运行工作负载不受影响。 >  > 多控制节点集群：即高可用集群，当某个控制节点故障时，集群仍然可用。查看集群模式请参见[如何排查已创建的集群是否为高可用集群？](https://support.huaweicloud.com/cce_faq/cce_faq_00155.html)

        :return: The flavor of this V3ClusterSpec.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this V3ClusterSpec.

        字段默认值：创建混合集群或鲲鹏集群时，如果是非专属云为 cce.s1.small，专属云则为 cce.dec.s1.small；  集群规格，集群创建完成后规格不可再变更，请按实际业务需求进行选择：  - cce.s1.small: 小规模单控制节点混合集群（最大50节点） - cce.s1.medium: 中等规模单控制节点混合集群（最大200节点） - cce.s2.small: 小规模多控制节点混合集群（最大50节点） - cce.s2.medium: 中等规模多控制节点混合集群（最大200节点） - cce.s2.large: 大规模多控制节点混合集群（最大1000节点） - cce.s2.xlarge: 超大规模多控制节点混合集群（最大2000节点）  > s1：单控制节点混合集群。 >  > s2：多控制节点混合集群。 >  > dec：专属混合集群规格。如cce.dec.s1.small为小规模单控制节点专属混合集群（最大50节点）。 >  > 最大节点数：当前集群支持管理的最大节点规模，请根据业务需求选择。 >  > 单控制节点集群：普通集群是单控制节点，控制节点故障后，集群将不可用，但已运行工作负载不受影响。 >  > 多控制节点集群：即高可用集群，当某个控制节点故障时，集群仍然可用。查看集群模式请参见[如何排查已创建的集群是否为高可用集群？](https://support.huaweicloud.com/cce_faq/cce_faq_00155.html)

        :param flavor: The flavor of this V3ClusterSpec.
        :type: str
        """
        self._flavor = flavor

    @property
    def host_network(self):
        """Gets the host_network of this V3ClusterSpec.


        :return: The host_network of this V3ClusterSpec.
        :rtype: HostNetwork
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """Sets the host_network of this V3ClusterSpec.


        :param host_network: The host_network of this V3ClusterSpec.
        :type: HostNetwork
        """
        self._host_network = host_network

    @property
    def ipv6enable(self):
        """Gets the ipv6enable of this V3ClusterSpec.

        集群是否使用IPv6模式，1.15版本及以上支持。

        :return: The ipv6enable of this V3ClusterSpec.
        :rtype: bool
        """
        return self._ipv6enable

    @ipv6enable.setter
    def ipv6enable(self, ipv6enable):
        """Sets the ipv6enable of this V3ClusterSpec.

        集群是否使用IPv6模式，1.15版本及以上支持。

        :param ipv6enable: The ipv6enable of this V3ClusterSpec.
        :type: bool
        """
        self._ipv6enable = ipv6enable

    @property
    def kube_proxy_mode(self):
        """Gets the kube_proxy_mode of this V3ClusterSpec.

        服务转发模式，支持以下两种实现：  iptables：社区传统的kube-proxy模式，完全以iptables规则的方式来实现service负载均衡。该方式最主要的问题是在服务多的时候产生太多的iptables规则，非增量式更新会引入一定的时延，大规模情况下有明显的性能问题。  ipvs：主导开发并在社区获得广泛支持的kube-proxy模式，采用增量式更新，吞吐更高，速度更快，并可以保证service更新期间连接保持不断开，适用于大规模场景。   >此参数目前仅在响应中体现，创建集群时请在**extendParam**中配置此参数。 

        :return: The kube_proxy_mode of this V3ClusterSpec.
        :rtype: str
        """
        return self._kube_proxy_mode

    @kube_proxy_mode.setter
    def kube_proxy_mode(self, kube_proxy_mode):
        """Sets the kube_proxy_mode of this V3ClusterSpec.

        服务转发模式，支持以下两种实现：  iptables：社区传统的kube-proxy模式，完全以iptables规则的方式来实现service负载均衡。该方式最主要的问题是在服务多的时候产生太多的iptables规则，非增量式更新会引入一定的时延，大规模情况下有明显的性能问题。  ipvs：主导开发并在社区获得广泛支持的kube-proxy模式，采用增量式更新，吞吐更高，速度更快，并可以保证service更新期间连接保持不断开，适用于大规模场景。   >此参数目前仅在响应中体现，创建集群时请在**extendParam**中配置此参数。 

        :param kube_proxy_mode: The kube_proxy_mode of this V3ClusterSpec.
        :type: str
        """
        self._kube_proxy_mode = kube_proxy_mode

    @property
    def kubernetes_svc_ip_range(self):
        """Gets the kubernetes_svc_ip_range of this V3ClusterSpec.

        服务网段参数，kubernetes clusterIp取值范围，1.11.7版本及以上支持。 

        :return: The kubernetes_svc_ip_range of this V3ClusterSpec.
        :rtype: str
        """
        return self._kubernetes_svc_ip_range

    @kubernetes_svc_ip_range.setter
    def kubernetes_svc_ip_range(self, kubernetes_svc_ip_range):
        """Sets the kubernetes_svc_ip_range of this V3ClusterSpec.

        服务网段参数，kubernetes clusterIp取值范围，1.11.7版本及以上支持。 

        :param kubernetes_svc_ip_range: The kubernetes_svc_ip_range of this V3ClusterSpec.
        :type: str
        """
        self._kubernetes_svc_ip_range = kubernetes_svc_ip_range

    @property
    def masters(self):
        """Gets the masters of this V3ClusterSpec.

        控制节点的高级配置

        :return: The masters of this V3ClusterSpec.
        :rtype: list[MasterSpec]
        """
        return self._masters

    @masters.setter
    def masters(self, masters):
        """Sets the masters of this V3ClusterSpec.

        控制节点的高级配置

        :param masters: The masters of this V3ClusterSpec.
        :type: list[MasterSpec]
        """
        self._masters = masters

    @property
    def support_istio(self):
        """Gets the support_istio of this V3ClusterSpec.

        支持Istio

        :return: The support_istio of this V3ClusterSpec.
        :rtype: bool
        """
        return self._support_istio

    @support_istio.setter
    def support_istio(self, support_istio):
        """Sets the support_istio of this V3ClusterSpec.

        支持Istio

        :param support_istio: The support_istio of this V3ClusterSpec.
        :type: bool
        """
        self._support_istio = support_istio

    @property
    def type(self):
        """Gets the type of this V3ClusterSpec.

        集群类型：  - VirtualMachine：混合集群  基于Kubernetes来管理一组节点资源，支持虚拟机和裸金属的管理，Kubernetes将自动调度容器运行在可用节点上。在创建容器工作负载前，您需要存在一个可用集群。  - BareMetal：裸金属集群  基于裸金属服务提供高计算和高网络性能的kubernetes容器集群，如需使用，请[创建裸金属服务器](https://support.huaweicloud.com/usermanual-bms/zh-cn_topic_0035100414.html)。裸金属集群为保证高速的容器网络性能，要求您在创建裸金属服务器时，添加一块高速网卡。添加步骤请参见[管理高速网络](https://support.huaweicloud.com/usermanual-bms/zh-cn_topic_0053537013.html)。  - ARM64: 鲲鹏集群  鲲鹏容器集群（ARM指令集）提供了容器在鲲鹏（ARM架构）服务器上的运行能力，提供与X86服务器相同的调度伸缩和快速部署能力。 

        :return: The type of this V3ClusterSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V3ClusterSpec.

        集群类型：  - VirtualMachine：混合集群  基于Kubernetes来管理一组节点资源，支持虚拟机和裸金属的管理，Kubernetes将自动调度容器运行在可用节点上。在创建容器工作负载前，您需要存在一个可用集群。  - BareMetal：裸金属集群  基于裸金属服务提供高计算和高网络性能的kubernetes容器集群，如需使用，请[创建裸金属服务器](https://support.huaweicloud.com/usermanual-bms/zh-cn_topic_0035100414.html)。裸金属集群为保证高速的容器网络性能，要求您在创建裸金属服务器时，添加一块高速网卡。添加步骤请参见[管理高速网络](https://support.huaweicloud.com/usermanual-bms/zh-cn_topic_0053537013.html)。  - ARM64: 鲲鹏集群  鲲鹏容器集群（ARM指令集）提供了容器在鲲鹏（ARM架构）服务器上的运行能力，提供与X86服务器相同的调度伸缩和快速部署能力。 

        :param type: The type of this V3ClusterSpec.
        :type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this V3ClusterSpec.

        集群版本，与Kubernetes社区基线版本保持一致，建议选择最新版本。  在CCE控制台中支持创建两种最新版本的集群。可登录CCE控制台，单击“总览 > 购买Kubernetes集群”，在“版本”处获取到集群版本。 其它集群版本，当前仍可通过api创建，但后续会逐渐下线，具体下线策略请关注CCE官方公告。  >    - 若不配置，默认创建最新版本的集群。 >    - 若指定集群基线版本但是不指定具体r版本，则系统默认选择对应集群版本的最新r版本。建议不指定具体r版本由系统选择最新版本。

        :return: The version of this V3ClusterSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V3ClusterSpec.

        集群版本，与Kubernetes社区基线版本保持一致，建议选择最新版本。  在CCE控制台中支持创建两种最新版本的集群。可登录CCE控制台，单击“总览 > 购买Kubernetes集群”，在“版本”处获取到集群版本。 其它集群版本，当前仍可通过api创建，但后续会逐渐下线，具体下线策略请关注CCE官方公告。  >    - 若不配置，默认创建最新版本的集群。 >    - 若指定集群基线版本但是不指定具体r版本，则系统默认选择对应集群版本的最新r版本。建议不指定具体r版本由系统选择最新版本。

        :param version: The version of this V3ClusterSpec.
        :type: str
        """
        self._version = version

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V3ClusterSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
