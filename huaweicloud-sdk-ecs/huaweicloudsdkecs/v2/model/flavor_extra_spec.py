# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorExtraSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ecsperformancetype': 'str',
        'hwnuma_nodes': 'str',
        'resource_type': 'str',
        'hpet_support': 'str',
        'instance_vnictype': 'str',
        'instance_vnicinstance_bandwidth': 'str',
        'instance_vnicmax_count': 'str',
        'quotalocal_disk': 'str',
        'quotanvme_ssd': 'str',
        'extra_speciopersistent_grant': 'str',
        'ecsgeneration': 'str',
        'ecsvirtualization_env_types': 'str',
        'pci_passthroughenable_gpu': 'str',
        'pci_passthroughgpu_specs': 'str',
        'pci_passthroughalias': 'str',
        'condoperationstatus': 'str',
        'condoperationaz': 'str',
        'quotamax_rate': 'str',
        'quotamin_rate': 'str',
        'quotamax_pps': 'str',
        'condoperationcharge': 'str',
        'condoperationchargestop': 'str',
        'condspotoperationaz': 'str',
        'condoperationroles': 'str',
        'condspotoperationstatus': 'str',
        'condnetwork': 'str',
        'condstorage': 'str',
        'condcomputelive_resizable': 'str',
        'condcompute': 'str',
        'infogpuname': 'str',
        'infocpuname': 'str',
        'quotagpu': 'str',
        'quotavif_max_num': 'str',
        'quotasub_network_interface_max_num': 'str',
        'ecsinstance_architecture': 'str'
    }

    attribute_map = {
        'ecsperformancetype': 'ecs:performancetype',
        'hwnuma_nodes': 'hw:numa_nodes',
        'resource_type': 'resource_type',
        'hpet_support': 'hpet_support',
        'instance_vnictype': 'instance_vnic:type',
        'instance_vnicinstance_bandwidth': 'instance_vnic:instance_bandwidth',
        'instance_vnicmax_count': 'instance_vnic:max_count',
        'quotalocal_disk': 'quota:local_disk',
        'quotanvme_ssd': 'quota:nvme_ssd',
        'extra_speciopersistent_grant': 'extra_spec:io:persistent_grant',
        'ecsgeneration': 'ecs:generation',
        'ecsvirtualization_env_types': 'ecs:virtualization_env_types',
        'pci_passthroughenable_gpu': 'pci_passthrough:enable_gpu',
        'pci_passthroughgpu_specs': 'pci_passthrough:gpu_specs',
        'pci_passthroughalias': 'pci_passthrough:alias',
        'condoperationstatus': 'cond:operation:status',
        'condoperationaz': 'cond:operation:az',
        'quotamax_rate': 'quota:max_rate',
        'quotamin_rate': 'quota:min_rate',
        'quotamax_pps': 'quota:max_pps',
        'condoperationcharge': 'cond:operation:charge',
        'condoperationchargestop': 'cond:operation:charge:stop',
        'condspotoperationaz': 'cond:spot:operation:az',
        'condoperationroles': 'cond:operation:roles',
        'condspotoperationstatus': 'cond:spot:operation:status',
        'condnetwork': 'cond:network',
        'condstorage': 'cond:storage',
        'condcomputelive_resizable': 'cond:compute:live_resizable',
        'condcompute': 'cond:compute',
        'infogpuname': 'info:gpu:name',
        'infocpuname': 'info:cpu:name',
        'quotagpu': 'quota:gpu',
        'quotavif_max_num': 'quota:vif_max_num',
        'quotasub_network_interface_max_num': 'quota:sub_network_interface_max_num',
        'ecsinstance_architecture': 'ecs:instance_architecture'
    }

    def __init__(self, ecsperformancetype=None, hwnuma_nodes=None, resource_type=None, hpet_support=None, instance_vnictype=None, instance_vnicinstance_bandwidth=None, instance_vnicmax_count=None, quotalocal_disk=None, quotanvme_ssd=None, extra_speciopersistent_grant=None, ecsgeneration=None, ecsvirtualization_env_types=None, pci_passthroughenable_gpu=None, pci_passthroughgpu_specs=None, pci_passthroughalias=None, condoperationstatus=None, condoperationaz=None, quotamax_rate=None, quotamin_rate=None, quotamax_pps=None, condoperationcharge=None, condoperationchargestop=None, condspotoperationaz=None, condoperationroles=None, condspotoperationstatus=None, condnetwork=None, condstorage=None, condcomputelive_resizable=None, condcompute=None, infogpuname=None, infocpuname=None, quotagpu=None, quotavif_max_num=None, quotasub_network_interface_max_num=None, ecsinstance_architecture=None):
        """FlavorExtraSpec

        The model defined in huaweicloud sdk

        :param ecsperformancetype: 云服务器规格的分类：  - normal：通用型 - entry：通用入门型 - cpuv1：计算I型 - cpuv2：计算II型 - computingv3：通用计算增强型 - kunpeng_computing：鲲鹏通用计算增强型 - kunpeng_highmem：鲲鹏内存优化型 - highmem：内存优化型 - saphana：大内存型 - diskintensive：磁盘增强型 - highio：超高I/O型 - ultracpu：超高性能计算型 - gpu：GPU加速型 - fpga：FPGA加速型 - ascend：AI加速型  &gt; 说明：  - 早期注册的规格该字段为hws:performancetype。
        :type ecsperformancetype: str
        :param hwnuma_nodes: 主机的物理cpu数量。
        :type hwnuma_nodes: str
        :param resource_type: 资源类型。resource_type是为了区分云服务器的物理主机类型。
        :type resource_type: str
        :param hpet_support: 弹性运服务器高精度时钟是否开启，开启为true，否则为false。（该字段是否返回根据云服务器规格而定）
        :type hpet_support: str
        :param instance_vnictype: 网卡类型，值固定为“enhanced”，表示使用增强型网络的资源创建云服务器。
        :type instance_vnictype: str
        :param instance_vnicinstance_bandwidth: 最大带宽，单位Mbps，最大值为10000。
        :type instance_vnicinstance_bandwidth: str
        :param instance_vnicmax_count: 最大网卡个数，最大为4。
        :type instance_vnicmax_count: str
        :param quotalocal_disk: 值格式为{type}:{count}:{size}:{safeFormat}，其中：  - type指磁盘类型，当前只支持hdd。 - count指本地磁盘数量，目前支持d1类型：3/6/12/24，d2类型：2/4/8/12/16/24，d3类型：2/4/8/12/16/24/28。 - size指单个磁盘容量，单位GB，目前只支持1675（实际磁盘大小为1800，格式化后可用大小为1675）。 - safeFormat指云服务器本地磁盘是否安全格式化，目前仅支持d1类型：FALSE，d2/d3类型：True。  &gt; 说明：  - 磁盘增强型特有字段。
        :type quotalocal_disk: str
        :param quotanvme_ssd: 值格式为{type}:{spec}:{size}:{safeFormat}，其中：  - type指主机上配备的nvme ssd的单卡容量大小，当前只支持1.6T/3.2T。 - spec指nvme ssd的规格，包括large/small。large表示大规格，small表示小规格。目前仅支持i3类型：large。 - size指guest使用的盘的容量大小，单位为GB。在spec值为large的情况下，此项即为host单卡大小。在spec值为small的情况下，此为1/4规格或者1/2规格。 - safeFormat指云服务器本地磁盘是否安全格式化，目前仅支持i3类型：True。  &gt; 说明：  - 超高I/O型特有字段。
        :type quotanvme_ssd: str
        :param extra_speciopersistent_grant: 是否支持持久化，值为true。  代表云服务器访问存储的方式为持久化授权。   &gt; 说明：  - 密集存储D1型特有字段。
        :type extra_speciopersistent_grant: str
        :param ecsgeneration: 弹性云服务器类型的代数。  - s1：通用型I代 - s2：通用型II代 - s3：通用型 - m1：内存优化型I代 - m2：内存优化型II代 - m3：内存优化型 - h1：高性能计算型I代 - h2：高性能计算型II代 - h3：高性能计算型 - hi3：超高性能计算型 - d1：密集存储型I代 - d2：密集存储型II代 - d3：磁盘增强型 - g1：GPU加速型I代 - g2：GPU加速型II代 - f1：FPGA高性能型 - f2：FPGA通用型 - c3：通用计算增强型 - e3：大内存型 - i3：超高I/O型
        :type ecsgeneration: str
        :param ecsvirtualization_env_types: 虚拟化类型。  - 如果值为“FusionCompute”，表示弹性云服务器使用基于XEN的虚拟化技术。 - 如果值为“CloudCompute”，表示弹性云服务器使用基于KVM的虚拟化技术。
        :type ecsvirtualization_env_types: str
        :param pci_passthroughenable_gpu: 显卡是否直通。  值为“true”，表示GPU直通。
        :type pci_passthroughenable_gpu: str
        :param pci_passthroughgpu_specs: G1型和G2型云服务器应用的技术，包括GPU虚拟化和GPU直通。  - 如果该规格的云服务器使用GPU虚拟化技术，且GPU卡的型号为M60-1Q，参数值可设置为“m60_1q:virt:1”。 - 如果该规格的云服务器使用GPU直通技术，且GPU卡的型号为M60，参数值可设置为“m60:direct_graphics:1”。
        :type pci_passthroughgpu_specs: str
        :param pci_passthroughalias: P1型v本地直通GPU的型号和数量，参数值可设置为“nvidia-p100:1”，表示使用该规格创建的弹性云服务器将占用1张NVIDIA P100显卡。
        :type pci_passthroughalias: str
        :param condoperationstatus: 此参数是Region级配置，某个AZ没有在cond:operation:az参数中配置时默认使用此参数的取值。不配置或无此参数时等同于“normal”。取值范围：  - normal：正常商用 - abandon：下线（即不显示） - sellout：售罄 - obt：公测 - promotion：推荐(等同normal，也是商用)
        :type condoperationstatus: str
        :param condoperationaz: 此参数是AZ级配置，某个AZ没有在此参数中配置时默认使用cond:operation:status参数的取值。此参数的配置格式“az(xx)”。()内为某个AZ的flavor状态，()内必须要填有状态，不填为无效配置。状态的取值范围与cond:operation:status参数相同。  例如：flavor在某个region的az0正常商用，az1售罄，az2公测，az3正常商用，其他az显示下线，可配置为：  - “cond:operation:status”设置为“abandon” - “cond:operation:az”设置为“az0(normal), az1(sellout), az2(obt), az3(normal)”  &gt; 说明：  - 如果flavor在某个AZ下的状态与cond:operation:status配置状态不同，必须配置该参数。
        :type condoperationaz: str
        :param quotamax_rate: 最大带宽  - 单位Mbps，显示为Gbps时除以1000
        :type quotamax_rate: str
        :param quotamin_rate: 基准带宽  - 单位Mbps，显示为Gbps时除以1000
        :type quotamin_rate: str
        :param quotamax_pps: 内网最大收发包能力  - 单位个，显示为xx万时除以10000
        :type quotamax_pps: str
        :param condoperationcharge: 计费类型  - 计费场景，不配置时都支持 - period，包周期 - demand，按需
        :type condoperationcharge: str
        :param condoperationchargestop: 关机是否收费  - 关机是否计费，默认免费： - charge - free
        :type condoperationchargestop: str
        :param condspotoperationaz: 计费类型  - 计费场景，不配置时都支持 - period，包周期 - demand，按需
        :type condspotoperationaz: str
        :param condoperationroles: 允许的角色 匹配的用户标签（roles的op_gatexxx标签）。不设置时所有用户可见
        :type condoperationroles: str
        :param condspotoperationstatus: Flavor在竞价销售模式下的状态  - 不配置时等同abandon - normal，正常商用 - abandon，下线 - sellout，售罄 - obt，公测，未申请时提示申请（暂不支持） - private，私有，只给特定用户显示（暂不支持） - test，试用/免费（暂不支持） - promotion，推荐
        :type condspotoperationstatus: str
        :param condnetwork: 网络约束 支持网络特性，不配置时以UI配置为准。
        :type condnetwork: str
        :param condstorage: 存储约束  - 支持磁盘特性，不配置时以UI配置为准。 - scsi，支持scsi - localdisk，支持本地盘 - ib，支持ib
        :type condstorage: str
        :param condcomputelive_resizable: 计算约束  - true，支持在线扩容。 - false或不存在该字段，不支持在线扩容。
        :type condcomputelive_resizable: str
        :param condcompute: 计算约束  - autorecovery，自动恢复特性。 - 不存在该字段，不支持自动恢复。
        :type condcompute: str
        :param infogpuname: 
        :type infogpuname: str
        :param infocpuname: 
        :type infocpuname: str
        :param quotagpu: 
        :type quotagpu: str
        :param quotavif_max_num: 最多支持的弹性网卡个数
        :type quotavif_max_num: str
        :param quotasub_network_interface_max_num: 最多支持的辅助弹性网卡个数
        :type quotasub_network_interface_max_num: str
        :param ecsinstance_architecture: 该规格对应的CPU架构，且仅鲲鹏实例架构规格返回该字段  - 取值为arm64表示CPU架构为鲲鹏计算。
        :type ecsinstance_architecture: str
        """
        
        

        self._ecsperformancetype = None
        self._hwnuma_nodes = None
        self._resource_type = None
        self._hpet_support = None
        self._instance_vnictype = None
        self._instance_vnicinstance_bandwidth = None
        self._instance_vnicmax_count = None
        self._quotalocal_disk = None
        self._quotanvme_ssd = None
        self._extra_speciopersistent_grant = None
        self._ecsgeneration = None
        self._ecsvirtualization_env_types = None
        self._pci_passthroughenable_gpu = None
        self._pci_passthroughgpu_specs = None
        self._pci_passthroughalias = None
        self._condoperationstatus = None
        self._condoperationaz = None
        self._quotamax_rate = None
        self._quotamin_rate = None
        self._quotamax_pps = None
        self._condoperationcharge = None
        self._condoperationchargestop = None
        self._condspotoperationaz = None
        self._condoperationroles = None
        self._condspotoperationstatus = None
        self._condnetwork = None
        self._condstorage = None
        self._condcomputelive_resizable = None
        self._condcompute = None
        self._infogpuname = None
        self._infocpuname = None
        self._quotagpu = None
        self._quotavif_max_num = None
        self._quotasub_network_interface_max_num = None
        self._ecsinstance_architecture = None
        self.discriminator = None

        if ecsperformancetype is not None:
            self.ecsperformancetype = ecsperformancetype
        if hwnuma_nodes is not None:
            self.hwnuma_nodes = hwnuma_nodes
        if resource_type is not None:
            self.resource_type = resource_type
        if hpet_support is not None:
            self.hpet_support = hpet_support
        if instance_vnictype is not None:
            self.instance_vnictype = instance_vnictype
        if instance_vnicinstance_bandwidth is not None:
            self.instance_vnicinstance_bandwidth = instance_vnicinstance_bandwidth
        if instance_vnicmax_count is not None:
            self.instance_vnicmax_count = instance_vnicmax_count
        if quotalocal_disk is not None:
            self.quotalocal_disk = quotalocal_disk
        if quotanvme_ssd is not None:
            self.quotanvme_ssd = quotanvme_ssd
        if extra_speciopersistent_grant is not None:
            self.extra_speciopersistent_grant = extra_speciopersistent_grant
        if ecsgeneration is not None:
            self.ecsgeneration = ecsgeneration
        if ecsvirtualization_env_types is not None:
            self.ecsvirtualization_env_types = ecsvirtualization_env_types
        if pci_passthroughenable_gpu is not None:
            self.pci_passthroughenable_gpu = pci_passthroughenable_gpu
        if pci_passthroughgpu_specs is not None:
            self.pci_passthroughgpu_specs = pci_passthroughgpu_specs
        if pci_passthroughalias is not None:
            self.pci_passthroughalias = pci_passthroughalias
        if condoperationstatus is not None:
            self.condoperationstatus = condoperationstatus
        if condoperationaz is not None:
            self.condoperationaz = condoperationaz
        if quotamax_rate is not None:
            self.quotamax_rate = quotamax_rate
        if quotamin_rate is not None:
            self.quotamin_rate = quotamin_rate
        if quotamax_pps is not None:
            self.quotamax_pps = quotamax_pps
        if condoperationcharge is not None:
            self.condoperationcharge = condoperationcharge
        if condoperationchargestop is not None:
            self.condoperationchargestop = condoperationchargestop
        if condspotoperationaz is not None:
            self.condspotoperationaz = condspotoperationaz
        if condoperationroles is not None:
            self.condoperationroles = condoperationroles
        if condspotoperationstatus is not None:
            self.condspotoperationstatus = condspotoperationstatus
        if condnetwork is not None:
            self.condnetwork = condnetwork
        if condstorage is not None:
            self.condstorage = condstorage
        if condcomputelive_resizable is not None:
            self.condcomputelive_resizable = condcomputelive_resizable
        if condcompute is not None:
            self.condcompute = condcompute
        if infogpuname is not None:
            self.infogpuname = infogpuname
        if infocpuname is not None:
            self.infocpuname = infocpuname
        if quotagpu is not None:
            self.quotagpu = quotagpu
        if quotavif_max_num is not None:
            self.quotavif_max_num = quotavif_max_num
        if quotasub_network_interface_max_num is not None:
            self.quotasub_network_interface_max_num = quotasub_network_interface_max_num
        if ecsinstance_architecture is not None:
            self.ecsinstance_architecture = ecsinstance_architecture

    @property
    def ecsperformancetype(self):
        """Gets the ecsperformancetype of this FlavorExtraSpec.

        云服务器规格的分类：  - normal：通用型 - entry：通用入门型 - cpuv1：计算I型 - cpuv2：计算II型 - computingv3：通用计算增强型 - kunpeng_computing：鲲鹏通用计算增强型 - kunpeng_highmem：鲲鹏内存优化型 - highmem：内存优化型 - saphana：大内存型 - diskintensive：磁盘增强型 - highio：超高I/O型 - ultracpu：超高性能计算型 - gpu：GPU加速型 - fpga：FPGA加速型 - ascend：AI加速型  > 说明：  - 早期注册的规格该字段为hws:performancetype。

        :return: The ecsperformancetype of this FlavorExtraSpec.
        :rtype: str
        """
        return self._ecsperformancetype

    @ecsperformancetype.setter
    def ecsperformancetype(self, ecsperformancetype):
        """Sets the ecsperformancetype of this FlavorExtraSpec.

        云服务器规格的分类：  - normal：通用型 - entry：通用入门型 - cpuv1：计算I型 - cpuv2：计算II型 - computingv3：通用计算增强型 - kunpeng_computing：鲲鹏通用计算增强型 - kunpeng_highmem：鲲鹏内存优化型 - highmem：内存优化型 - saphana：大内存型 - diskintensive：磁盘增强型 - highio：超高I/O型 - ultracpu：超高性能计算型 - gpu：GPU加速型 - fpga：FPGA加速型 - ascend：AI加速型  > 说明：  - 早期注册的规格该字段为hws:performancetype。

        :param ecsperformancetype: The ecsperformancetype of this FlavorExtraSpec.
        :type ecsperformancetype: str
        """
        self._ecsperformancetype = ecsperformancetype

    @property
    def hwnuma_nodes(self):
        """Gets the hwnuma_nodes of this FlavorExtraSpec.

        主机的物理cpu数量。

        :return: The hwnuma_nodes of this FlavorExtraSpec.
        :rtype: str
        """
        return self._hwnuma_nodes

    @hwnuma_nodes.setter
    def hwnuma_nodes(self, hwnuma_nodes):
        """Sets the hwnuma_nodes of this FlavorExtraSpec.

        主机的物理cpu数量。

        :param hwnuma_nodes: The hwnuma_nodes of this FlavorExtraSpec.
        :type hwnuma_nodes: str
        """
        self._hwnuma_nodes = hwnuma_nodes

    @property
    def resource_type(self):
        """Gets the resource_type of this FlavorExtraSpec.

        资源类型。resource_type是为了区分云服务器的物理主机类型。

        :return: The resource_type of this FlavorExtraSpec.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this FlavorExtraSpec.

        资源类型。resource_type是为了区分云服务器的物理主机类型。

        :param resource_type: The resource_type of this FlavorExtraSpec.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def hpet_support(self):
        """Gets the hpet_support of this FlavorExtraSpec.

        弹性运服务器高精度时钟是否开启，开启为true，否则为false。（该字段是否返回根据云服务器规格而定）

        :return: The hpet_support of this FlavorExtraSpec.
        :rtype: str
        """
        return self._hpet_support

    @hpet_support.setter
    def hpet_support(self, hpet_support):
        """Sets the hpet_support of this FlavorExtraSpec.

        弹性运服务器高精度时钟是否开启，开启为true，否则为false。（该字段是否返回根据云服务器规格而定）

        :param hpet_support: The hpet_support of this FlavorExtraSpec.
        :type hpet_support: str
        """
        self._hpet_support = hpet_support

    @property
    def instance_vnictype(self):
        """Gets the instance_vnictype of this FlavorExtraSpec.

        网卡类型，值固定为“enhanced”，表示使用增强型网络的资源创建云服务器。

        :return: The instance_vnictype of this FlavorExtraSpec.
        :rtype: str
        """
        return self._instance_vnictype

    @instance_vnictype.setter
    def instance_vnictype(self, instance_vnictype):
        """Sets the instance_vnictype of this FlavorExtraSpec.

        网卡类型，值固定为“enhanced”，表示使用增强型网络的资源创建云服务器。

        :param instance_vnictype: The instance_vnictype of this FlavorExtraSpec.
        :type instance_vnictype: str
        """
        self._instance_vnictype = instance_vnictype

    @property
    def instance_vnicinstance_bandwidth(self):
        """Gets the instance_vnicinstance_bandwidth of this FlavorExtraSpec.

        最大带宽，单位Mbps，最大值为10000。

        :return: The instance_vnicinstance_bandwidth of this FlavorExtraSpec.
        :rtype: str
        """
        return self._instance_vnicinstance_bandwidth

    @instance_vnicinstance_bandwidth.setter
    def instance_vnicinstance_bandwidth(self, instance_vnicinstance_bandwidth):
        """Sets the instance_vnicinstance_bandwidth of this FlavorExtraSpec.

        最大带宽，单位Mbps，最大值为10000。

        :param instance_vnicinstance_bandwidth: The instance_vnicinstance_bandwidth of this FlavorExtraSpec.
        :type instance_vnicinstance_bandwidth: str
        """
        self._instance_vnicinstance_bandwidth = instance_vnicinstance_bandwidth

    @property
    def instance_vnicmax_count(self):
        """Gets the instance_vnicmax_count of this FlavorExtraSpec.

        最大网卡个数，最大为4。

        :return: The instance_vnicmax_count of this FlavorExtraSpec.
        :rtype: str
        """
        return self._instance_vnicmax_count

    @instance_vnicmax_count.setter
    def instance_vnicmax_count(self, instance_vnicmax_count):
        """Sets the instance_vnicmax_count of this FlavorExtraSpec.

        最大网卡个数，最大为4。

        :param instance_vnicmax_count: The instance_vnicmax_count of this FlavorExtraSpec.
        :type instance_vnicmax_count: str
        """
        self._instance_vnicmax_count = instance_vnicmax_count

    @property
    def quotalocal_disk(self):
        """Gets the quotalocal_disk of this FlavorExtraSpec.

        值格式为{type}:{count}:{size}:{safeFormat}，其中：  - type指磁盘类型，当前只支持hdd。 - count指本地磁盘数量，目前支持d1类型：3/6/12/24，d2类型：2/4/8/12/16/24，d3类型：2/4/8/12/16/24/28。 - size指单个磁盘容量，单位GB，目前只支持1675（实际磁盘大小为1800，格式化后可用大小为1675）。 - safeFormat指云服务器本地磁盘是否安全格式化，目前仅支持d1类型：FALSE，d2/d3类型：True。  > 说明：  - 磁盘增强型特有字段。

        :return: The quotalocal_disk of this FlavorExtraSpec.
        :rtype: str
        """
        return self._quotalocal_disk

    @quotalocal_disk.setter
    def quotalocal_disk(self, quotalocal_disk):
        """Sets the quotalocal_disk of this FlavorExtraSpec.

        值格式为{type}:{count}:{size}:{safeFormat}，其中：  - type指磁盘类型，当前只支持hdd。 - count指本地磁盘数量，目前支持d1类型：3/6/12/24，d2类型：2/4/8/12/16/24，d3类型：2/4/8/12/16/24/28。 - size指单个磁盘容量，单位GB，目前只支持1675（实际磁盘大小为1800，格式化后可用大小为1675）。 - safeFormat指云服务器本地磁盘是否安全格式化，目前仅支持d1类型：FALSE，d2/d3类型：True。  > 说明：  - 磁盘增强型特有字段。

        :param quotalocal_disk: The quotalocal_disk of this FlavorExtraSpec.
        :type quotalocal_disk: str
        """
        self._quotalocal_disk = quotalocal_disk

    @property
    def quotanvme_ssd(self):
        """Gets the quotanvme_ssd of this FlavorExtraSpec.

        值格式为{type}:{spec}:{size}:{safeFormat}，其中：  - type指主机上配备的nvme ssd的单卡容量大小，当前只支持1.6T/3.2T。 - spec指nvme ssd的规格，包括large/small。large表示大规格，small表示小规格。目前仅支持i3类型：large。 - size指guest使用的盘的容量大小，单位为GB。在spec值为large的情况下，此项即为host单卡大小。在spec值为small的情况下，此为1/4规格或者1/2规格。 - safeFormat指云服务器本地磁盘是否安全格式化，目前仅支持i3类型：True。  > 说明：  - 超高I/O型特有字段。

        :return: The quotanvme_ssd of this FlavorExtraSpec.
        :rtype: str
        """
        return self._quotanvme_ssd

    @quotanvme_ssd.setter
    def quotanvme_ssd(self, quotanvme_ssd):
        """Sets the quotanvme_ssd of this FlavorExtraSpec.

        值格式为{type}:{spec}:{size}:{safeFormat}，其中：  - type指主机上配备的nvme ssd的单卡容量大小，当前只支持1.6T/3.2T。 - spec指nvme ssd的规格，包括large/small。large表示大规格，small表示小规格。目前仅支持i3类型：large。 - size指guest使用的盘的容量大小，单位为GB。在spec值为large的情况下，此项即为host单卡大小。在spec值为small的情况下，此为1/4规格或者1/2规格。 - safeFormat指云服务器本地磁盘是否安全格式化，目前仅支持i3类型：True。  > 说明：  - 超高I/O型特有字段。

        :param quotanvme_ssd: The quotanvme_ssd of this FlavorExtraSpec.
        :type quotanvme_ssd: str
        """
        self._quotanvme_ssd = quotanvme_ssd

    @property
    def extra_speciopersistent_grant(self):
        """Gets the extra_speciopersistent_grant of this FlavorExtraSpec.

        是否支持持久化，值为true。  代表云服务器访问存储的方式为持久化授权。   > 说明：  - 密集存储D1型特有字段。

        :return: The extra_speciopersistent_grant of this FlavorExtraSpec.
        :rtype: str
        """
        return self._extra_speciopersistent_grant

    @extra_speciopersistent_grant.setter
    def extra_speciopersistent_grant(self, extra_speciopersistent_grant):
        """Sets the extra_speciopersistent_grant of this FlavorExtraSpec.

        是否支持持久化，值为true。  代表云服务器访问存储的方式为持久化授权。   > 说明：  - 密集存储D1型特有字段。

        :param extra_speciopersistent_grant: The extra_speciopersistent_grant of this FlavorExtraSpec.
        :type extra_speciopersistent_grant: str
        """
        self._extra_speciopersistent_grant = extra_speciopersistent_grant

    @property
    def ecsgeneration(self):
        """Gets the ecsgeneration of this FlavorExtraSpec.

        弹性云服务器类型的代数。  - s1：通用型I代 - s2：通用型II代 - s3：通用型 - m1：内存优化型I代 - m2：内存优化型II代 - m3：内存优化型 - h1：高性能计算型I代 - h2：高性能计算型II代 - h3：高性能计算型 - hi3：超高性能计算型 - d1：密集存储型I代 - d2：密集存储型II代 - d3：磁盘增强型 - g1：GPU加速型I代 - g2：GPU加速型II代 - f1：FPGA高性能型 - f2：FPGA通用型 - c3：通用计算增强型 - e3：大内存型 - i3：超高I/O型

        :return: The ecsgeneration of this FlavorExtraSpec.
        :rtype: str
        """
        return self._ecsgeneration

    @ecsgeneration.setter
    def ecsgeneration(self, ecsgeneration):
        """Sets the ecsgeneration of this FlavorExtraSpec.

        弹性云服务器类型的代数。  - s1：通用型I代 - s2：通用型II代 - s3：通用型 - m1：内存优化型I代 - m2：内存优化型II代 - m3：内存优化型 - h1：高性能计算型I代 - h2：高性能计算型II代 - h3：高性能计算型 - hi3：超高性能计算型 - d1：密集存储型I代 - d2：密集存储型II代 - d3：磁盘增强型 - g1：GPU加速型I代 - g2：GPU加速型II代 - f1：FPGA高性能型 - f2：FPGA通用型 - c3：通用计算增强型 - e3：大内存型 - i3：超高I/O型

        :param ecsgeneration: The ecsgeneration of this FlavorExtraSpec.
        :type ecsgeneration: str
        """
        self._ecsgeneration = ecsgeneration

    @property
    def ecsvirtualization_env_types(self):
        """Gets the ecsvirtualization_env_types of this FlavorExtraSpec.

        虚拟化类型。  - 如果值为“FusionCompute”，表示弹性云服务器使用基于XEN的虚拟化技术。 - 如果值为“CloudCompute”，表示弹性云服务器使用基于KVM的虚拟化技术。

        :return: The ecsvirtualization_env_types of this FlavorExtraSpec.
        :rtype: str
        """
        return self._ecsvirtualization_env_types

    @ecsvirtualization_env_types.setter
    def ecsvirtualization_env_types(self, ecsvirtualization_env_types):
        """Sets the ecsvirtualization_env_types of this FlavorExtraSpec.

        虚拟化类型。  - 如果值为“FusionCompute”，表示弹性云服务器使用基于XEN的虚拟化技术。 - 如果值为“CloudCompute”，表示弹性云服务器使用基于KVM的虚拟化技术。

        :param ecsvirtualization_env_types: The ecsvirtualization_env_types of this FlavorExtraSpec.
        :type ecsvirtualization_env_types: str
        """
        self._ecsvirtualization_env_types = ecsvirtualization_env_types

    @property
    def pci_passthroughenable_gpu(self):
        """Gets the pci_passthroughenable_gpu of this FlavorExtraSpec.

        显卡是否直通。  值为“true”，表示GPU直通。

        :return: The pci_passthroughenable_gpu of this FlavorExtraSpec.
        :rtype: str
        """
        return self._pci_passthroughenable_gpu

    @pci_passthroughenable_gpu.setter
    def pci_passthroughenable_gpu(self, pci_passthroughenable_gpu):
        """Sets the pci_passthroughenable_gpu of this FlavorExtraSpec.

        显卡是否直通。  值为“true”，表示GPU直通。

        :param pci_passthroughenable_gpu: The pci_passthroughenable_gpu of this FlavorExtraSpec.
        :type pci_passthroughenable_gpu: str
        """
        self._pci_passthroughenable_gpu = pci_passthroughenable_gpu

    @property
    def pci_passthroughgpu_specs(self):
        """Gets the pci_passthroughgpu_specs of this FlavorExtraSpec.

        G1型和G2型云服务器应用的技术，包括GPU虚拟化和GPU直通。  - 如果该规格的云服务器使用GPU虚拟化技术，且GPU卡的型号为M60-1Q，参数值可设置为“m60_1q:virt:1”。 - 如果该规格的云服务器使用GPU直通技术，且GPU卡的型号为M60，参数值可设置为“m60:direct_graphics:1”。

        :return: The pci_passthroughgpu_specs of this FlavorExtraSpec.
        :rtype: str
        """
        return self._pci_passthroughgpu_specs

    @pci_passthroughgpu_specs.setter
    def pci_passthroughgpu_specs(self, pci_passthroughgpu_specs):
        """Sets the pci_passthroughgpu_specs of this FlavorExtraSpec.

        G1型和G2型云服务器应用的技术，包括GPU虚拟化和GPU直通。  - 如果该规格的云服务器使用GPU虚拟化技术，且GPU卡的型号为M60-1Q，参数值可设置为“m60_1q:virt:1”。 - 如果该规格的云服务器使用GPU直通技术，且GPU卡的型号为M60，参数值可设置为“m60:direct_graphics:1”。

        :param pci_passthroughgpu_specs: The pci_passthroughgpu_specs of this FlavorExtraSpec.
        :type pci_passthroughgpu_specs: str
        """
        self._pci_passthroughgpu_specs = pci_passthroughgpu_specs

    @property
    def pci_passthroughalias(self):
        """Gets the pci_passthroughalias of this FlavorExtraSpec.

        P1型v本地直通GPU的型号和数量，参数值可设置为“nvidia-p100:1”，表示使用该规格创建的弹性云服务器将占用1张NVIDIA P100显卡。

        :return: The pci_passthroughalias of this FlavorExtraSpec.
        :rtype: str
        """
        return self._pci_passthroughalias

    @pci_passthroughalias.setter
    def pci_passthroughalias(self, pci_passthroughalias):
        """Sets the pci_passthroughalias of this FlavorExtraSpec.

        P1型v本地直通GPU的型号和数量，参数值可设置为“nvidia-p100:1”，表示使用该规格创建的弹性云服务器将占用1张NVIDIA P100显卡。

        :param pci_passthroughalias: The pci_passthroughalias of this FlavorExtraSpec.
        :type pci_passthroughalias: str
        """
        self._pci_passthroughalias = pci_passthroughalias

    @property
    def condoperationstatus(self):
        """Gets the condoperationstatus of this FlavorExtraSpec.

        此参数是Region级配置，某个AZ没有在cond:operation:az参数中配置时默认使用此参数的取值。不配置或无此参数时等同于“normal”。取值范围：  - normal：正常商用 - abandon：下线（即不显示） - sellout：售罄 - obt：公测 - promotion：推荐(等同normal，也是商用)

        :return: The condoperationstatus of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condoperationstatus

    @condoperationstatus.setter
    def condoperationstatus(self, condoperationstatus):
        """Sets the condoperationstatus of this FlavorExtraSpec.

        此参数是Region级配置，某个AZ没有在cond:operation:az参数中配置时默认使用此参数的取值。不配置或无此参数时等同于“normal”。取值范围：  - normal：正常商用 - abandon：下线（即不显示） - sellout：售罄 - obt：公测 - promotion：推荐(等同normal，也是商用)

        :param condoperationstatus: The condoperationstatus of this FlavorExtraSpec.
        :type condoperationstatus: str
        """
        self._condoperationstatus = condoperationstatus

    @property
    def condoperationaz(self):
        """Gets the condoperationaz of this FlavorExtraSpec.

        此参数是AZ级配置，某个AZ没有在此参数中配置时默认使用cond:operation:status参数的取值。此参数的配置格式“az(xx)”。()内为某个AZ的flavor状态，()内必须要填有状态，不填为无效配置。状态的取值范围与cond:operation:status参数相同。  例如：flavor在某个region的az0正常商用，az1售罄，az2公测，az3正常商用，其他az显示下线，可配置为：  - “cond:operation:status”设置为“abandon” - “cond:operation:az”设置为“az0(normal), az1(sellout), az2(obt), az3(normal)”  > 说明：  - 如果flavor在某个AZ下的状态与cond:operation:status配置状态不同，必须配置该参数。

        :return: The condoperationaz of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condoperationaz

    @condoperationaz.setter
    def condoperationaz(self, condoperationaz):
        """Sets the condoperationaz of this FlavorExtraSpec.

        此参数是AZ级配置，某个AZ没有在此参数中配置时默认使用cond:operation:status参数的取值。此参数的配置格式“az(xx)”。()内为某个AZ的flavor状态，()内必须要填有状态，不填为无效配置。状态的取值范围与cond:operation:status参数相同。  例如：flavor在某个region的az0正常商用，az1售罄，az2公测，az3正常商用，其他az显示下线，可配置为：  - “cond:operation:status”设置为“abandon” - “cond:operation:az”设置为“az0(normal), az1(sellout), az2(obt), az3(normal)”  > 说明：  - 如果flavor在某个AZ下的状态与cond:operation:status配置状态不同，必须配置该参数。

        :param condoperationaz: The condoperationaz of this FlavorExtraSpec.
        :type condoperationaz: str
        """
        self._condoperationaz = condoperationaz

    @property
    def quotamax_rate(self):
        """Gets the quotamax_rate of this FlavorExtraSpec.

        最大带宽  - 单位Mbps，显示为Gbps时除以1000

        :return: The quotamax_rate of this FlavorExtraSpec.
        :rtype: str
        """
        return self._quotamax_rate

    @quotamax_rate.setter
    def quotamax_rate(self, quotamax_rate):
        """Sets the quotamax_rate of this FlavorExtraSpec.

        最大带宽  - 单位Mbps，显示为Gbps时除以1000

        :param quotamax_rate: The quotamax_rate of this FlavorExtraSpec.
        :type quotamax_rate: str
        """
        self._quotamax_rate = quotamax_rate

    @property
    def quotamin_rate(self):
        """Gets the quotamin_rate of this FlavorExtraSpec.

        基准带宽  - 单位Mbps，显示为Gbps时除以1000

        :return: The quotamin_rate of this FlavorExtraSpec.
        :rtype: str
        """
        return self._quotamin_rate

    @quotamin_rate.setter
    def quotamin_rate(self, quotamin_rate):
        """Sets the quotamin_rate of this FlavorExtraSpec.

        基准带宽  - 单位Mbps，显示为Gbps时除以1000

        :param quotamin_rate: The quotamin_rate of this FlavorExtraSpec.
        :type quotamin_rate: str
        """
        self._quotamin_rate = quotamin_rate

    @property
    def quotamax_pps(self):
        """Gets the quotamax_pps of this FlavorExtraSpec.

        内网最大收发包能力  - 单位个，显示为xx万时除以10000

        :return: The quotamax_pps of this FlavorExtraSpec.
        :rtype: str
        """
        return self._quotamax_pps

    @quotamax_pps.setter
    def quotamax_pps(self, quotamax_pps):
        """Sets the quotamax_pps of this FlavorExtraSpec.

        内网最大收发包能力  - 单位个，显示为xx万时除以10000

        :param quotamax_pps: The quotamax_pps of this FlavorExtraSpec.
        :type quotamax_pps: str
        """
        self._quotamax_pps = quotamax_pps

    @property
    def condoperationcharge(self):
        """Gets the condoperationcharge of this FlavorExtraSpec.

        计费类型  - 计费场景，不配置时都支持 - period，包周期 - demand，按需

        :return: The condoperationcharge of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condoperationcharge

    @condoperationcharge.setter
    def condoperationcharge(self, condoperationcharge):
        """Sets the condoperationcharge of this FlavorExtraSpec.

        计费类型  - 计费场景，不配置时都支持 - period，包周期 - demand，按需

        :param condoperationcharge: The condoperationcharge of this FlavorExtraSpec.
        :type condoperationcharge: str
        """
        self._condoperationcharge = condoperationcharge

    @property
    def condoperationchargestop(self):
        """Gets the condoperationchargestop of this FlavorExtraSpec.

        关机是否收费  - 关机是否计费，默认免费： - charge - free

        :return: The condoperationchargestop of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condoperationchargestop

    @condoperationchargestop.setter
    def condoperationchargestop(self, condoperationchargestop):
        """Sets the condoperationchargestop of this FlavorExtraSpec.

        关机是否收费  - 关机是否计费，默认免费： - charge - free

        :param condoperationchargestop: The condoperationchargestop of this FlavorExtraSpec.
        :type condoperationchargestop: str
        """
        self._condoperationchargestop = condoperationchargestop

    @property
    def condspotoperationaz(self):
        """Gets the condspotoperationaz of this FlavorExtraSpec.

        计费类型  - 计费场景，不配置时都支持 - period，包周期 - demand，按需

        :return: The condspotoperationaz of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condspotoperationaz

    @condspotoperationaz.setter
    def condspotoperationaz(self, condspotoperationaz):
        """Sets the condspotoperationaz of this FlavorExtraSpec.

        计费类型  - 计费场景，不配置时都支持 - period，包周期 - demand，按需

        :param condspotoperationaz: The condspotoperationaz of this FlavorExtraSpec.
        :type condspotoperationaz: str
        """
        self._condspotoperationaz = condspotoperationaz

    @property
    def condoperationroles(self):
        """Gets the condoperationroles of this FlavorExtraSpec.

        允许的角色 匹配的用户标签（roles的op_gatexxx标签）。不设置时所有用户可见

        :return: The condoperationroles of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condoperationroles

    @condoperationroles.setter
    def condoperationroles(self, condoperationroles):
        """Sets the condoperationroles of this FlavorExtraSpec.

        允许的角色 匹配的用户标签（roles的op_gatexxx标签）。不设置时所有用户可见

        :param condoperationroles: The condoperationroles of this FlavorExtraSpec.
        :type condoperationroles: str
        """
        self._condoperationroles = condoperationroles

    @property
    def condspotoperationstatus(self):
        """Gets the condspotoperationstatus of this FlavorExtraSpec.

        Flavor在竞价销售模式下的状态  - 不配置时等同abandon - normal，正常商用 - abandon，下线 - sellout，售罄 - obt，公测，未申请时提示申请（暂不支持） - private，私有，只给特定用户显示（暂不支持） - test，试用/免费（暂不支持） - promotion，推荐

        :return: The condspotoperationstatus of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condspotoperationstatus

    @condspotoperationstatus.setter
    def condspotoperationstatus(self, condspotoperationstatus):
        """Sets the condspotoperationstatus of this FlavorExtraSpec.

        Flavor在竞价销售模式下的状态  - 不配置时等同abandon - normal，正常商用 - abandon，下线 - sellout，售罄 - obt，公测，未申请时提示申请（暂不支持） - private，私有，只给特定用户显示（暂不支持） - test，试用/免费（暂不支持） - promotion，推荐

        :param condspotoperationstatus: The condspotoperationstatus of this FlavorExtraSpec.
        :type condspotoperationstatus: str
        """
        self._condspotoperationstatus = condspotoperationstatus

    @property
    def condnetwork(self):
        """Gets the condnetwork of this FlavorExtraSpec.

        网络约束 支持网络特性，不配置时以UI配置为准。

        :return: The condnetwork of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condnetwork

    @condnetwork.setter
    def condnetwork(self, condnetwork):
        """Sets the condnetwork of this FlavorExtraSpec.

        网络约束 支持网络特性，不配置时以UI配置为准。

        :param condnetwork: The condnetwork of this FlavorExtraSpec.
        :type condnetwork: str
        """
        self._condnetwork = condnetwork

    @property
    def condstorage(self):
        """Gets the condstorage of this FlavorExtraSpec.

        存储约束  - 支持磁盘特性，不配置时以UI配置为准。 - scsi，支持scsi - localdisk，支持本地盘 - ib，支持ib

        :return: The condstorage of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condstorage

    @condstorage.setter
    def condstorage(self, condstorage):
        """Sets the condstorage of this FlavorExtraSpec.

        存储约束  - 支持磁盘特性，不配置时以UI配置为准。 - scsi，支持scsi - localdisk，支持本地盘 - ib，支持ib

        :param condstorage: The condstorage of this FlavorExtraSpec.
        :type condstorage: str
        """
        self._condstorage = condstorage

    @property
    def condcomputelive_resizable(self):
        """Gets the condcomputelive_resizable of this FlavorExtraSpec.

        计算约束  - true，支持在线扩容。 - false或不存在该字段，不支持在线扩容。

        :return: The condcomputelive_resizable of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condcomputelive_resizable

    @condcomputelive_resizable.setter
    def condcomputelive_resizable(self, condcomputelive_resizable):
        """Sets the condcomputelive_resizable of this FlavorExtraSpec.

        计算约束  - true，支持在线扩容。 - false或不存在该字段，不支持在线扩容。

        :param condcomputelive_resizable: The condcomputelive_resizable of this FlavorExtraSpec.
        :type condcomputelive_resizable: str
        """
        self._condcomputelive_resizable = condcomputelive_resizable

    @property
    def condcompute(self):
        """Gets the condcompute of this FlavorExtraSpec.

        计算约束  - autorecovery，自动恢复特性。 - 不存在该字段，不支持自动恢复。

        :return: The condcompute of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condcompute

    @condcompute.setter
    def condcompute(self, condcompute):
        """Sets the condcompute of this FlavorExtraSpec.

        计算约束  - autorecovery，自动恢复特性。 - 不存在该字段，不支持自动恢复。

        :param condcompute: The condcompute of this FlavorExtraSpec.
        :type condcompute: str
        """
        self._condcompute = condcompute

    @property
    def infogpuname(self):
        """Gets the infogpuname of this FlavorExtraSpec.

        

        :return: The infogpuname of this FlavorExtraSpec.
        :rtype: str
        """
        return self._infogpuname

    @infogpuname.setter
    def infogpuname(self, infogpuname):
        """Sets the infogpuname of this FlavorExtraSpec.

        

        :param infogpuname: The infogpuname of this FlavorExtraSpec.
        :type infogpuname: str
        """
        self._infogpuname = infogpuname

    @property
    def infocpuname(self):
        """Gets the infocpuname of this FlavorExtraSpec.

        

        :return: The infocpuname of this FlavorExtraSpec.
        :rtype: str
        """
        return self._infocpuname

    @infocpuname.setter
    def infocpuname(self, infocpuname):
        """Sets the infocpuname of this FlavorExtraSpec.

        

        :param infocpuname: The infocpuname of this FlavorExtraSpec.
        :type infocpuname: str
        """
        self._infocpuname = infocpuname

    @property
    def quotagpu(self):
        """Gets the quotagpu of this FlavorExtraSpec.

        

        :return: The quotagpu of this FlavorExtraSpec.
        :rtype: str
        """
        return self._quotagpu

    @quotagpu.setter
    def quotagpu(self, quotagpu):
        """Sets the quotagpu of this FlavorExtraSpec.

        

        :param quotagpu: The quotagpu of this FlavorExtraSpec.
        :type quotagpu: str
        """
        self._quotagpu = quotagpu

    @property
    def quotavif_max_num(self):
        """Gets the quotavif_max_num of this FlavorExtraSpec.

        最多支持的弹性网卡个数

        :return: The quotavif_max_num of this FlavorExtraSpec.
        :rtype: str
        """
        return self._quotavif_max_num

    @quotavif_max_num.setter
    def quotavif_max_num(self, quotavif_max_num):
        """Sets the quotavif_max_num of this FlavorExtraSpec.

        最多支持的弹性网卡个数

        :param quotavif_max_num: The quotavif_max_num of this FlavorExtraSpec.
        :type quotavif_max_num: str
        """
        self._quotavif_max_num = quotavif_max_num

    @property
    def quotasub_network_interface_max_num(self):
        """Gets the quotasub_network_interface_max_num of this FlavorExtraSpec.

        最多支持的辅助弹性网卡个数

        :return: The quotasub_network_interface_max_num of this FlavorExtraSpec.
        :rtype: str
        """
        return self._quotasub_network_interface_max_num

    @quotasub_network_interface_max_num.setter
    def quotasub_network_interface_max_num(self, quotasub_network_interface_max_num):
        """Sets the quotasub_network_interface_max_num of this FlavorExtraSpec.

        最多支持的辅助弹性网卡个数

        :param quotasub_network_interface_max_num: The quotasub_network_interface_max_num of this FlavorExtraSpec.
        :type quotasub_network_interface_max_num: str
        """
        self._quotasub_network_interface_max_num = quotasub_network_interface_max_num

    @property
    def ecsinstance_architecture(self):
        """Gets the ecsinstance_architecture of this FlavorExtraSpec.

        该规格对应的CPU架构，且仅鲲鹏实例架构规格返回该字段  - 取值为arm64表示CPU架构为鲲鹏计算。

        :return: The ecsinstance_architecture of this FlavorExtraSpec.
        :rtype: str
        """
        return self._ecsinstance_architecture

    @ecsinstance_architecture.setter
    def ecsinstance_architecture(self, ecsinstance_architecture):
        """Sets the ecsinstance_architecture of this FlavorExtraSpec.

        该规格对应的CPU架构，且仅鲲鹏实例架构规格返回该字段  - 取值为arm64表示CPU架构为鲲鹏计算。

        :param ecsinstance_architecture: The ecsinstance_architecture of this FlavorExtraSpec.
        :type ecsinstance_architecture: str
        """
        self._ecsinstance_architecture = ecsinstance_architecture

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
        if not isinstance(other, FlavorExtraSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
