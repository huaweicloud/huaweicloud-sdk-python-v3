# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_az': 'str',
        'dss_master_volumes': 'str',
        'enterprise_project_id': 'str',
        'kube_proxy_mode': 'str',
        'cluster_external_ip': 'str',
        'alpha_cce_fix_pool_mask': 'str',
        'dec_master_flavor': 'str',
        'docker_umask_mode': 'str',
        'kubernetes_io_cpu_manager_policy': 'str',
        'order_id': 'str',
        'period_type': 'str',
        'period_num': 'int',
        'is_auto_renew': 'str',
        'is_auto_pay': 'str',
        'upgradefrom': 'str'
    }

    attribute_map = {
        'cluster_az': 'clusterAZ',
        'dss_master_volumes': 'dssMasterVolumes',
        'enterprise_project_id': 'enterpriseProjectId',
        'kube_proxy_mode': 'kubeProxyMode',
        'cluster_external_ip': 'clusterExternalIP',
        'alpha_cce_fix_pool_mask': 'alpha.cce/fixPoolMask',
        'dec_master_flavor': 'decMasterFlavor',
        'docker_umask_mode': 'dockerUmaskMode',
        'kubernetes_io_cpu_manager_policy': 'kubernetes.io/cpuManagerPolicy',
        'order_id': 'orderID',
        'period_type': 'periodType',
        'period_num': 'periodNum',
        'is_auto_renew': 'isAutoRenew',
        'is_auto_pay': 'isAutoPay',
        'upgradefrom': 'upgradefrom'
    }

    def __init__(self, cluster_az=None, dss_master_volumes=None, enterprise_project_id=None, kube_proxy_mode=None, cluster_external_ip=None, alpha_cce_fix_pool_mask=None, dec_master_flavor=None, docker_umask_mode=None, kubernetes_io_cpu_manager_policy=None, order_id=None, period_type=None, period_num=None, is_auto_renew=None, is_auto_pay=None, upgradefrom=None):
        r"""ClusterExtendParam

        The model defined in huaweicloud sdk

        :param cluster_az: 集群控制节点可用区配置。  [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint?CCE)](tag:hws) [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/intl/zh-cn/endpoint?CCE)](tag:hws_hk)    - multi_az：多可用区，可选。仅使用高可用集群时才可以配置多可用区。 - 专属云计算池可用区：用于指定专属云可用区部署集群控制节点。如果需配置专属CCE集群，该字段为必选。 
        :type cluster_az: str
        :param dss_master_volumes: 用于指定控制节点的系统盘和数据盘使用专属分布式存储，未指定或者值为空时，默认使用EVS云硬盘。  如果配置专属CCE集群，该字段为必选，请按照如下格式设置：  &#x60;&#x60;&#x60; &lt;rootVol.dssPoolID&gt;.&lt;rootVol.volType&gt;;&lt;dataVol.dssPoolID&gt;.&lt;dataVol.volType&gt; &#x60;&#x60;&#x60;  字段说明： - rootVol为系统盘；dataVol为数据盘； - dssPoolID为专属分布式存储池ID； - volType为专属分布式存储池的存储类型，如SAS、SSD。  样例：c950ee97-587c-4f24-8a74-3367e3da570f.sas;6edbc2f4-1507-44f8-ac0d-eed1d2608d38.ssd  &gt; 非专属CCE集群不支持配置该字段。 
        :type dss_master_volumes: str
        :param enterprise_project_id: 集群所属的企业项目ID。 &gt;   - 需要开通企业项目功能后才可配置企业项目。 &gt;   - 集群所属的企业项目与集群下所关联的其他云服务资源所属的企业项目必须保持一致。 
        :type enterprise_project_id: str
        :param kube_proxy_mode: 服务转发模式，支持以下两种实现：  - iptables：社区传统的kube-proxy模式，完全以iptables规则的方式来实现service负载均衡。该方式最主要的问题是在服务多的时候产生太多的iptables规则，非增量式更新会引入一定的时延，大规模情况下有明显的性能问题 - ipvs：主导开发并在社区获得广泛支持的kube-proxy模式，采用增量式更新，吞吐更高，速度更快，并可以保证service更新期间连接保持不断开，适用于大规模场景。  &gt; 此参数已废弃，若同时指定此参数和ClusterSpec下的kubeProxyMode，以ClusterSpec下的为准。 
        :type kube_proxy_mode: str
        :param cluster_external_ip: master 弹性公网IP
        :type cluster_external_ip: str
        :param alpha_cce_fix_pool_mask: 容器网络固定IP池掩码位数，仅vpc-router网络支持。  该参数决定节点可分配容器IP数量，与创建节点时设置的maxPods参数共同决定节点最多可以创建多少个Pod， 具体请参见[节点最多可以创建多少Pod](maxPods.xml)。   整数字符传取值范围: 24 ~ 28 
        :type alpha_cce_fix_pool_mask: str
        :param dec_master_flavor: 专属CCE集群指定可控制节点的规格。
        :type dec_master_flavor: str
        :param docker_umask_mode: 集群默认Docker的UmaskMode配置，可取值为secure或normal，不指定时默认为normal。 
        :type docker_umask_mode: str
        :param kubernetes_io_cpu_manager_policy: 集群CPU管理策略。取值为none（或空值）或static，默认为none（或空值）。 - none(或空值)：关闭工作负载实例独占CPU核的功能，优点是CPU共享池的可分配核数较多 - static：支持给节点上的工作负载实例配置CPU独占，适用于对CPU缓存和调度延迟敏感的工作负载[，Turbo集群下仅对普通容器节点有效，安全容器节点无效](tag:hws,hws_hk,dt,g42,sbc)。 
        :type kubernetes_io_cpu_manager_policy: str
        :param order_id: 订单ID，集群付费类型为自动付费包周期类型时，响应中会返回此字段(仅创建场景涉及)。
        :type order_id: str
        :param period_type: - month：月 - year：年 &gt; 作为请求参数，billingMode为1（包周期）时生效，且为必选。 &gt; 作为响应参数，仅在创建包周期集群时返回。 
        :type period_type: str
        :param period_num: 订购周期数，取值范围： - periodType&#x3D;month（周期类型为月）时，取值为[1-9]。 - periodType&#x3D;year（周期类型为年）时，取值为1-3。 &gt; 作为请求参数，billingMode为1时生效，且为必选。 &gt; 作为响应参数，仅在创建包周期集群时返回。 
        :type period_num: int
        :param is_auto_renew: 是否自动续订 - “true”：自动续订 - “false”：不自动续订 &gt; billingMode为1时生效，不填写此参数时默认不会自动续费。 
        :type is_auto_renew: str
        :param is_auto_pay: 是否自动扣款 - “true”：自动扣款 - “false”：不自动扣款 &gt; billingMode为1时生效，不填写此参数时默认不会自动扣款。 
        :type is_auto_pay: str
        :param upgradefrom: 记录集群通过何种升级方式升级到当前版本。 
        :type upgradefrom: str
        """
        
        

        self._cluster_az = None
        self._dss_master_volumes = None
        self._enterprise_project_id = None
        self._kube_proxy_mode = None
        self._cluster_external_ip = None
        self._alpha_cce_fix_pool_mask = None
        self._dec_master_flavor = None
        self._docker_umask_mode = None
        self._kubernetes_io_cpu_manager_policy = None
        self._order_id = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self._upgradefrom = None
        self.discriminator = None

        if cluster_az is not None:
            self.cluster_az = cluster_az
        if dss_master_volumes is not None:
            self.dss_master_volumes = dss_master_volumes
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if kube_proxy_mode is not None:
            self.kube_proxy_mode = kube_proxy_mode
        if cluster_external_ip is not None:
            self.cluster_external_ip = cluster_external_ip
        if alpha_cce_fix_pool_mask is not None:
            self.alpha_cce_fix_pool_mask = alpha_cce_fix_pool_mask
        if dec_master_flavor is not None:
            self.dec_master_flavor = dec_master_flavor
        if docker_umask_mode is not None:
            self.docker_umask_mode = docker_umask_mode
        if kubernetes_io_cpu_manager_policy is not None:
            self.kubernetes_io_cpu_manager_policy = kubernetes_io_cpu_manager_policy
        if order_id is not None:
            self.order_id = order_id
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if upgradefrom is not None:
            self.upgradefrom = upgradefrom

    @property
    def cluster_az(self):
        r"""Gets the cluster_az of this ClusterExtendParam.

        集群控制节点可用区配置。  [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint?CCE)](tag:hws) [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/intl/zh-cn/endpoint?CCE)](tag:hws_hk)    - multi_az：多可用区，可选。仅使用高可用集群时才可以配置多可用区。 - 专属云计算池可用区：用于指定专属云可用区部署集群控制节点。如果需配置专属CCE集群，该字段为必选。 

        :return: The cluster_az of this ClusterExtendParam.
        :rtype: str
        """
        return self._cluster_az

    @cluster_az.setter
    def cluster_az(self, cluster_az):
        r"""Sets the cluster_az of this ClusterExtendParam.

        集群控制节点可用区配置。  [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint?CCE)](tag:hws) [CCE支持的可用区请参考[地区和终端节点](https://developer.huaweicloud.com/intl/zh-cn/endpoint?CCE)](tag:hws_hk)    - multi_az：多可用区，可选。仅使用高可用集群时才可以配置多可用区。 - 专属云计算池可用区：用于指定专属云可用区部署集群控制节点。如果需配置专属CCE集群，该字段为必选。 

        :param cluster_az: The cluster_az of this ClusterExtendParam.
        :type cluster_az: str
        """
        self._cluster_az = cluster_az

    @property
    def dss_master_volumes(self):
        r"""Gets the dss_master_volumes of this ClusterExtendParam.

        用于指定控制节点的系统盘和数据盘使用专属分布式存储，未指定或者值为空时，默认使用EVS云硬盘。  如果配置专属CCE集群，该字段为必选，请按照如下格式设置：  ``` <rootVol.dssPoolID>.<rootVol.volType>;<dataVol.dssPoolID>.<dataVol.volType> ```  字段说明： - rootVol为系统盘；dataVol为数据盘； - dssPoolID为专属分布式存储池ID； - volType为专属分布式存储池的存储类型，如SAS、SSD。  样例：c950ee97-587c-4f24-8a74-3367e3da570f.sas;6edbc2f4-1507-44f8-ac0d-eed1d2608d38.ssd  > 非专属CCE集群不支持配置该字段。 

        :return: The dss_master_volumes of this ClusterExtendParam.
        :rtype: str
        """
        return self._dss_master_volumes

    @dss_master_volumes.setter
    def dss_master_volumes(self, dss_master_volumes):
        r"""Sets the dss_master_volumes of this ClusterExtendParam.

        用于指定控制节点的系统盘和数据盘使用专属分布式存储，未指定或者值为空时，默认使用EVS云硬盘。  如果配置专属CCE集群，该字段为必选，请按照如下格式设置：  ``` <rootVol.dssPoolID>.<rootVol.volType>;<dataVol.dssPoolID>.<dataVol.volType> ```  字段说明： - rootVol为系统盘；dataVol为数据盘； - dssPoolID为专属分布式存储池ID； - volType为专属分布式存储池的存储类型，如SAS、SSD。  样例：c950ee97-587c-4f24-8a74-3367e3da570f.sas;6edbc2f4-1507-44f8-ac0d-eed1d2608d38.ssd  > 非专属CCE集群不支持配置该字段。 

        :param dss_master_volumes: The dss_master_volumes of this ClusterExtendParam.
        :type dss_master_volumes: str
        """
        self._dss_master_volumes = dss_master_volumes

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ClusterExtendParam.

        集群所属的企业项目ID。 >   - 需要开通企业项目功能后才可配置企业项目。 >   - 集群所属的企业项目与集群下所关联的其他云服务资源所属的企业项目必须保持一致。 

        :return: The enterprise_project_id of this ClusterExtendParam.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ClusterExtendParam.

        集群所属的企业项目ID。 >   - 需要开通企业项目功能后才可配置企业项目。 >   - 集群所属的企业项目与集群下所关联的其他云服务资源所属的企业项目必须保持一致。 

        :param enterprise_project_id: The enterprise_project_id of this ClusterExtendParam.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def kube_proxy_mode(self):
        r"""Gets the kube_proxy_mode of this ClusterExtendParam.

        服务转发模式，支持以下两种实现：  - iptables：社区传统的kube-proxy模式，完全以iptables规则的方式来实现service负载均衡。该方式最主要的问题是在服务多的时候产生太多的iptables规则，非增量式更新会引入一定的时延，大规模情况下有明显的性能问题 - ipvs：主导开发并在社区获得广泛支持的kube-proxy模式，采用增量式更新，吞吐更高，速度更快，并可以保证service更新期间连接保持不断开，适用于大规模场景。  > 此参数已废弃，若同时指定此参数和ClusterSpec下的kubeProxyMode，以ClusterSpec下的为准。 

        :return: The kube_proxy_mode of this ClusterExtendParam.
        :rtype: str
        """
        return self._kube_proxy_mode

    @kube_proxy_mode.setter
    def kube_proxy_mode(self, kube_proxy_mode):
        r"""Sets the kube_proxy_mode of this ClusterExtendParam.

        服务转发模式，支持以下两种实现：  - iptables：社区传统的kube-proxy模式，完全以iptables规则的方式来实现service负载均衡。该方式最主要的问题是在服务多的时候产生太多的iptables规则，非增量式更新会引入一定的时延，大规模情况下有明显的性能问题 - ipvs：主导开发并在社区获得广泛支持的kube-proxy模式，采用增量式更新，吞吐更高，速度更快，并可以保证service更新期间连接保持不断开，适用于大规模场景。  > 此参数已废弃，若同时指定此参数和ClusterSpec下的kubeProxyMode，以ClusterSpec下的为准。 

        :param kube_proxy_mode: The kube_proxy_mode of this ClusterExtendParam.
        :type kube_proxy_mode: str
        """
        self._kube_proxy_mode = kube_proxy_mode

    @property
    def cluster_external_ip(self):
        r"""Gets the cluster_external_ip of this ClusterExtendParam.

        master 弹性公网IP

        :return: The cluster_external_ip of this ClusterExtendParam.
        :rtype: str
        """
        return self._cluster_external_ip

    @cluster_external_ip.setter
    def cluster_external_ip(self, cluster_external_ip):
        r"""Sets the cluster_external_ip of this ClusterExtendParam.

        master 弹性公网IP

        :param cluster_external_ip: The cluster_external_ip of this ClusterExtendParam.
        :type cluster_external_ip: str
        """
        self._cluster_external_ip = cluster_external_ip

    @property
    def alpha_cce_fix_pool_mask(self):
        r"""Gets the alpha_cce_fix_pool_mask of this ClusterExtendParam.

        容器网络固定IP池掩码位数，仅vpc-router网络支持。  该参数决定节点可分配容器IP数量，与创建节点时设置的maxPods参数共同决定节点最多可以创建多少个Pod， 具体请参见[节点最多可以创建多少Pod](maxPods.xml)。   整数字符传取值范围: 24 ~ 28 

        :return: The alpha_cce_fix_pool_mask of this ClusterExtendParam.
        :rtype: str
        """
        return self._alpha_cce_fix_pool_mask

    @alpha_cce_fix_pool_mask.setter
    def alpha_cce_fix_pool_mask(self, alpha_cce_fix_pool_mask):
        r"""Sets the alpha_cce_fix_pool_mask of this ClusterExtendParam.

        容器网络固定IP池掩码位数，仅vpc-router网络支持。  该参数决定节点可分配容器IP数量，与创建节点时设置的maxPods参数共同决定节点最多可以创建多少个Pod， 具体请参见[节点最多可以创建多少Pod](maxPods.xml)。   整数字符传取值范围: 24 ~ 28 

        :param alpha_cce_fix_pool_mask: The alpha_cce_fix_pool_mask of this ClusterExtendParam.
        :type alpha_cce_fix_pool_mask: str
        """
        self._alpha_cce_fix_pool_mask = alpha_cce_fix_pool_mask

    @property
    def dec_master_flavor(self):
        r"""Gets the dec_master_flavor of this ClusterExtendParam.

        专属CCE集群指定可控制节点的规格。

        :return: The dec_master_flavor of this ClusterExtendParam.
        :rtype: str
        """
        return self._dec_master_flavor

    @dec_master_flavor.setter
    def dec_master_flavor(self, dec_master_flavor):
        r"""Sets the dec_master_flavor of this ClusterExtendParam.

        专属CCE集群指定可控制节点的规格。

        :param dec_master_flavor: The dec_master_flavor of this ClusterExtendParam.
        :type dec_master_flavor: str
        """
        self._dec_master_flavor = dec_master_flavor

    @property
    def docker_umask_mode(self):
        r"""Gets the docker_umask_mode of this ClusterExtendParam.

        集群默认Docker的UmaskMode配置，可取值为secure或normal，不指定时默认为normal。 

        :return: The docker_umask_mode of this ClusterExtendParam.
        :rtype: str
        """
        return self._docker_umask_mode

    @docker_umask_mode.setter
    def docker_umask_mode(self, docker_umask_mode):
        r"""Sets the docker_umask_mode of this ClusterExtendParam.

        集群默认Docker的UmaskMode配置，可取值为secure或normal，不指定时默认为normal。 

        :param docker_umask_mode: The docker_umask_mode of this ClusterExtendParam.
        :type docker_umask_mode: str
        """
        self._docker_umask_mode = docker_umask_mode

    @property
    def kubernetes_io_cpu_manager_policy(self):
        r"""Gets the kubernetes_io_cpu_manager_policy of this ClusterExtendParam.

        集群CPU管理策略。取值为none（或空值）或static，默认为none（或空值）。 - none(或空值)：关闭工作负载实例独占CPU核的功能，优点是CPU共享池的可分配核数较多 - static：支持给节点上的工作负载实例配置CPU独占，适用于对CPU缓存和调度延迟敏感的工作负载[，Turbo集群下仅对普通容器节点有效，安全容器节点无效](tag:hws,hws_hk,dt,g42,sbc)。 

        :return: The kubernetes_io_cpu_manager_policy of this ClusterExtendParam.
        :rtype: str
        """
        return self._kubernetes_io_cpu_manager_policy

    @kubernetes_io_cpu_manager_policy.setter
    def kubernetes_io_cpu_manager_policy(self, kubernetes_io_cpu_manager_policy):
        r"""Sets the kubernetes_io_cpu_manager_policy of this ClusterExtendParam.

        集群CPU管理策略。取值为none（或空值）或static，默认为none（或空值）。 - none(或空值)：关闭工作负载实例独占CPU核的功能，优点是CPU共享池的可分配核数较多 - static：支持给节点上的工作负载实例配置CPU独占，适用于对CPU缓存和调度延迟敏感的工作负载[，Turbo集群下仅对普通容器节点有效，安全容器节点无效](tag:hws,hws_hk,dt,g42,sbc)。 

        :param kubernetes_io_cpu_manager_policy: The kubernetes_io_cpu_manager_policy of this ClusterExtendParam.
        :type kubernetes_io_cpu_manager_policy: str
        """
        self._kubernetes_io_cpu_manager_policy = kubernetes_io_cpu_manager_policy

    @property
    def order_id(self):
        r"""Gets the order_id of this ClusterExtendParam.

        订单ID，集群付费类型为自动付费包周期类型时，响应中会返回此字段(仅创建场景涉及)。

        :return: The order_id of this ClusterExtendParam.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ClusterExtendParam.

        订单ID，集群付费类型为自动付费包周期类型时，响应中会返回此字段(仅创建场景涉及)。

        :param order_id: The order_id of this ClusterExtendParam.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def period_type(self):
        r"""Gets the period_type of this ClusterExtendParam.

        - month：月 - year：年 > 作为请求参数，billingMode为1（包周期）时生效，且为必选。 > 作为响应参数，仅在创建包周期集群时返回。 

        :return: The period_type of this ClusterExtendParam.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this ClusterExtendParam.

        - month：月 - year：年 > 作为请求参数，billingMode为1（包周期）时生效，且为必选。 > 作为响应参数，仅在创建包周期集群时返回。 

        :param period_type: The period_type of this ClusterExtendParam.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this ClusterExtendParam.

        订购周期数，取值范围： - periodType=month（周期类型为月）时，取值为[1-9]。 - periodType=year（周期类型为年）时，取值为1-3。 > 作为请求参数，billingMode为1时生效，且为必选。 > 作为响应参数，仅在创建包周期集群时返回。 

        :return: The period_num of this ClusterExtendParam.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this ClusterExtendParam.

        订购周期数，取值范围： - periodType=month（周期类型为月）时，取值为[1-9]。 - periodType=year（周期类型为年）时，取值为1-3。 > 作为请求参数，billingMode为1时生效，且为必选。 > 作为响应参数，仅在创建包周期集群时返回。 

        :param period_num: The period_num of this ClusterExtendParam.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this ClusterExtendParam.

        是否自动续订 - “true”：自动续订 - “false”：不自动续订 > billingMode为1时生效，不填写此参数时默认不会自动续费。 

        :return: The is_auto_renew of this ClusterExtendParam.
        :rtype: str
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this ClusterExtendParam.

        是否自动续订 - “true”：自动续订 - “false”：不自动续订 > billingMode为1时生效，不填写此参数时默认不会自动续费。 

        :param is_auto_renew: The is_auto_renew of this ClusterExtendParam.
        :type is_auto_renew: str
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this ClusterExtendParam.

        是否自动扣款 - “true”：自动扣款 - “false”：不自动扣款 > billingMode为1时生效，不填写此参数时默认不会自动扣款。 

        :return: The is_auto_pay of this ClusterExtendParam.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this ClusterExtendParam.

        是否自动扣款 - “true”：自动扣款 - “false”：不自动扣款 > billingMode为1时生效，不填写此参数时默认不会自动扣款。 

        :param is_auto_pay: The is_auto_pay of this ClusterExtendParam.
        :type is_auto_pay: str
        """
        self._is_auto_pay = is_auto_pay

    @property
    def upgradefrom(self):
        r"""Gets the upgradefrom of this ClusterExtendParam.

        记录集群通过何种升级方式升级到当前版本。 

        :return: The upgradefrom of this ClusterExtendParam.
        :rtype: str
        """
        return self._upgradefrom

    @upgradefrom.setter
    def upgradefrom(self, upgradefrom):
        r"""Sets the upgradefrom of this ClusterExtendParam.

        记录集群通过何种升级方式升级到当前版本。 

        :param upgradefrom: The upgradefrom of this ClusterExtendParam.
        :type upgradefrom: str
        """
        self._upgradefrom = upgradefrom

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
        if not isinstance(other, ClusterExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
