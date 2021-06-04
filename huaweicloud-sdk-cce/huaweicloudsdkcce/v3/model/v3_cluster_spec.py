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
        'type': 'str',
        'flavor': 'str',
        'version': 'str',
        'description': 'str',
        'ipv6enable': 'bool',
        'offload_cluster': 'bool',
        'host_network': 'HostNetwork',
        'container_network': 'ContainerNetwork',
        'eni_network': 'EniNetwork',
        'authentication': 'Authentication',
        'billing_mode': 'int',
        'masters': 'list[MasterSpec]',
        'kubernetes_svc_ip_range': 'str',
        'cluster_tags': 'list[ResourceTag]',
        'kube_proxy_mode': 'str',
        'az': 'str',
        'extend_param': 'ClusterExtendParam',
        'support_istio': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'flavor': 'flavor',
        'version': 'version',
        'description': 'description',
        'ipv6enable': 'ipv6enable',
        'offload_cluster': 'offloadCluster',
        'host_network': 'hostNetwork',
        'container_network': 'containerNetwork',
        'eni_network': 'eniNetwork',
        'authentication': 'authentication',
        'billing_mode': 'billingMode',
        'masters': 'masters',
        'kubernetes_svc_ip_range': 'kubernetesSvcIpRange',
        'cluster_tags': 'clusterTags',
        'kube_proxy_mode': 'kubeProxyMode',
        'az': 'az',
        'extend_param': 'extendParam',
        'support_istio': 'supportIstio'
    }

    def __init__(self, type=None, flavor=None, version=None, description=None, ipv6enable=None, offload_cluster=None, host_network=None, container_network=None, eni_network=None, authentication=None, billing_mode=None, masters=None, kubernetes_svc_ip_range=None, cluster_tags=None, kube_proxy_mode=None, az=None, extend_param=None, support_istio=None):
        """V3ClusterSpec - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._flavor = None
        self._version = None
        self._description = None
        self._ipv6enable = None
        self._offload_cluster = None
        self._host_network = None
        self._container_network = None
        self._eni_network = None
        self._authentication = None
        self._billing_mode = None
        self._masters = None
        self._kubernetes_svc_ip_range = None
        self._cluster_tags = None
        self._kube_proxy_mode = None
        self._az = None
        self._extend_param = None
        self._support_istio = None
        self.discriminator = None

        self.type = type
        self.flavor = flavor
        if version is not None:
            self.version = version
        if description is not None:
            self.description = description
        if ipv6enable is not None:
            self.ipv6enable = ipv6enable
        if offload_cluster is not None:
            self.offload_cluster = offload_cluster
        self.host_network = host_network
        self.container_network = container_network
        if eni_network is not None:
            self.eni_network = eni_network
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

    @property
    def type(self):
        """Gets the type of this V3ClusterSpec.

        集群类型：  - VirtualMachine：CCE集群  基于Kubernetes来管理一组节点资源，支持虚拟机和裸金属的管理，Kubernetes将自动调度容器运行在可用节点上。在创建容器工作负载前，您需要存在一个可用集群。  - ARM64: 鲲鹏集群  鲲鹏容器集群（ARM指令集）提供了容器在鲲鹏（ARM架构）服务器上的运行能力，提供与X86服务器相同的调度伸缩和快速部署能力。 

        :return: The type of this V3ClusterSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V3ClusterSpec.

        集群类型：  - VirtualMachine：CCE集群  基于Kubernetes来管理一组节点资源，支持虚拟机和裸金属的管理，Kubernetes将自动调度容器运行在可用节点上。在创建容器工作负载前，您需要存在一个可用集群。  - ARM64: 鲲鹏集群  鲲鹏容器集群（ARM指令集）提供了容器在鲲鹏（ARM架构）服务器上的运行能力，提供与X86服务器相同的调度伸缩和快速部署能力。 

        :param type: The type of this V3ClusterSpec.
        :type: str
        """
        self._type = type

    @property
    def flavor(self):
        """Gets the flavor of this V3ClusterSpec.

        字段默认值：创建CCE集群[或鲲鹏集群](tag:hws)时，如果是非专属云为 cce.s1.small，专属云则为 cce.dec.s1.small；   集群规格，集群创建完成后规格不可再变更，请按实际业务需求进行选择：   - cce.s1.small: 小规模单控制节点CCE集群（最大50节点）  - cce.s1.medium: 中等规模单控制节点CCE集群（最大200节点）  - cce.s2.small: 小规模多控制节点CCE集群（最大50节点）  - cce.s2.medium: 中等规模多控制节点CCE集群（最大200节点）  - cce.s2.large: 大规模多控制节点CCE集群（最大1000节点）  - cce.s2.xlarge: 超大规模多控制节点CCE集群（最大2000节点）   >    - s1：单控制节点CCE集群。 >    - s2：多控制节点CCE集群。 >    - dec：专属CCE集群规格。如cce.dec.s1.small为小规模单控制节点专属CCE集群（最大50节点）。 >    - 最大节点数：当前集群支持管理的最大节点规模，请根据业务需求选择。 >    - 单控制节点集群：普通集群是单控制节点，控制节点故障后，集群将不可用，但已运行工作负载不受影响。 >    - 多控制节点集群：即高可用集群，当某个控制节点故障时，集群仍然可用。查看集群模式请参见[[如何排查已创建的集群是否为高可用集群？](https://support.huaweicloud.com/cce_faq/cce_faq_00155.html)](tag:hws)[[如何排查已创建的集群是否为高可用集群？](https://support.huaweicloud.com/intl/zh-cn/cce_faq/cce_faq_00155.html)](tag:hws_hk) 

        :return: The flavor of this V3ClusterSpec.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this V3ClusterSpec.

        字段默认值：创建CCE集群[或鲲鹏集群](tag:hws)时，如果是非专属云为 cce.s1.small，专属云则为 cce.dec.s1.small；   集群规格，集群创建完成后规格不可再变更，请按实际业务需求进行选择：   - cce.s1.small: 小规模单控制节点CCE集群（最大50节点）  - cce.s1.medium: 中等规模单控制节点CCE集群（最大200节点）  - cce.s2.small: 小规模多控制节点CCE集群（最大50节点）  - cce.s2.medium: 中等规模多控制节点CCE集群（最大200节点）  - cce.s2.large: 大规模多控制节点CCE集群（最大1000节点）  - cce.s2.xlarge: 超大规模多控制节点CCE集群（最大2000节点）   >    - s1：单控制节点CCE集群。 >    - s2：多控制节点CCE集群。 >    - dec：专属CCE集群规格。如cce.dec.s1.small为小规模单控制节点专属CCE集群（最大50节点）。 >    - 最大节点数：当前集群支持管理的最大节点规模，请根据业务需求选择。 >    - 单控制节点集群：普通集群是单控制节点，控制节点故障后，集群将不可用，但已运行工作负载不受影响。 >    - 多控制节点集群：即高可用集群，当某个控制节点故障时，集群仍然可用。查看集群模式请参见[[如何排查已创建的集群是否为高可用集群？](https://support.huaweicloud.com/cce_faq/cce_faq_00155.html)](tag:hws)[[如何排查已创建的集群是否为高可用集群？](https://support.huaweicloud.com/intl/zh-cn/cce_faq/cce_faq_00155.html)](tag:hws_hk) 

        :param flavor: The flavor of this V3ClusterSpec.
        :type: str
        """
        self._flavor = flavor

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

    @property
    def description(self):
        """Gets the description of this V3ClusterSpec.

        集群描述，对于集群使用目的的描述，可根据实际情况自定义，默认为空。集群创建成功后可通过接口[[更新指定的集群](https://support.huaweicloud.com/api-cce/cce_02_0240.html)](tag:hws)[[更新指定的集群](https://support.huaweicloud.com/intl/zh-cn/api-cce/cce_02_0240.html)](tag:hws_hk)来做出修改，也可在CCE控制台中对应集群的“集群详情”下的“描述”处进行修改。仅支持utf-8编码。

        :return: The description of this V3ClusterSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V3ClusterSpec.

        集群描述，对于集群使用目的的描述，可根据实际情况自定义，默认为空。集群创建成功后可通过接口[[更新指定的集群](https://support.huaweicloud.com/api-cce/cce_02_0240.html)](tag:hws)[[更新指定的集群](https://support.huaweicloud.com/intl/zh-cn/api-cce/cce_02_0240.html)](tag:hws_hk)来做出修改，也可在CCE控制台中对应集群的“集群详情”下的“描述”处进行修改。仅支持utf-8编码。

        :param description: The description of this V3ClusterSpec.
        :type: str
        """
        self._description = description

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
    def offload_cluster(self):
        """Gets the offload_cluster of this V3ClusterSpec.

        CCE Turbo集群(公测)

        :return: The offload_cluster of this V3ClusterSpec.
        :rtype: bool
        """
        return self._offload_cluster

    @offload_cluster.setter
    def offload_cluster(self, offload_cluster):
        """Sets the offload_cluster of this V3ClusterSpec.

        CCE Turbo集群(公测)

        :param offload_cluster: The offload_cluster of this V3ClusterSpec.
        :type: bool
        """
        self._offload_cluster = offload_cluster

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
    def eni_network(self):
        """Gets the eni_network of this V3ClusterSpec.


        :return: The eni_network of this V3ClusterSpec.
        :rtype: EniNetwork
        """
        return self._eni_network

    @eni_network.setter
    def eni_network(self, eni_network):
        """Sets the eni_network of this V3ClusterSpec.


        :param eni_network: The eni_network of this V3ClusterSpec.
        :type: EniNetwork
        """
        self._eni_network = eni_network

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
    def extend_param(self):
        """Gets the extend_param of this V3ClusterSpec.


        :return: The extend_param of this V3ClusterSpec.
        :rtype: ClusterExtendParam
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this V3ClusterSpec.


        :param extend_param: The extend_param of this V3ClusterSpec.
        :type: ClusterExtendParam
        """
        self._extend_param = extend_param

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
