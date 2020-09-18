# coding: utf-8

import pprint
import re

import six





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
        'resource_type': 'str',
        'quotalocal_disk': 'str',
        'quotanvme_ssd': 'str',
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
        'condoperationcharge': 'str'
    }

    attribute_map = {
        'ecsperformancetype': 'ecs:performancetype',
        'resource_type': 'resource_type',
        'quotalocal_disk': 'quota:local_disk',
        'quotanvme_ssd': 'quota:nvme_ssd',
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
        'condoperationcharge': 'cond:operation:charge'
    }

    def __init__(self, ecsperformancetype=None, resource_type=None, quotalocal_disk=None, quotanvme_ssd=None, ecsgeneration=None, ecsvirtualization_env_types=None, pci_passthroughenable_gpu=None, pci_passthroughgpu_specs=None, pci_passthroughalias=None, condoperationstatus=None, condoperationaz=None, quotamax_rate=None, quotamin_rate=None, quotamax_pps=None, condoperationcharge=None):
        """FlavorExtraSpec - a model defined in huaweicloud sdk"""
        
        

        self._ecsperformancetype = None
        self._resource_type = None
        self._quotalocal_disk = None
        self._quotanvme_ssd = None
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
        self.discriminator = None

        self.ecsperformancetype = ecsperformancetype
        self.resource_type = resource_type
        if quotalocal_disk is not None:
            self.quotalocal_disk = quotalocal_disk
        if quotanvme_ssd is not None:
            self.quotanvme_ssd = quotanvme_ssd
        if ecsgeneration is not None:
            self.ecsgeneration = ecsgeneration
        if ecsvirtualization_env_types is not None:
            self.ecsvirtualization_env_types = ecsvirtualization_env_types
        self.pci_passthroughenable_gpu = pci_passthroughenable_gpu
        self.pci_passthroughgpu_specs = pci_passthroughgpu_specs
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

    @property
    def ecsperformancetype(self):
        """Gets the ecsperformancetype of this FlavorExtraSpec.

        云服务器规格的分类：  - normal：通用型 - cpuv1：计算I型 - cpuv2：计算II型 - highmem：内存优化型 - gpu：GPU加速型 - entry：通用入门型 - saphana：大内存型 - ultracpu：超高性能计算型 - diskintensive：磁盘增强型 - highio：超高I/O型 - fpga：FPGA加速型  > 说明：  - 早期注册的规格该字段为hws:performancetype。

        :return: The ecsperformancetype of this FlavorExtraSpec.
        :rtype: str
        """
        return self._ecsperformancetype

    @ecsperformancetype.setter
    def ecsperformancetype(self, ecsperformancetype):
        """Sets the ecsperformancetype of this FlavorExtraSpec.

        云服务器规格的分类：  - normal：通用型 - cpuv1：计算I型 - cpuv2：计算II型 - highmem：内存优化型 - gpu：GPU加速型 - entry：通用入门型 - saphana：大内存型 - ultracpu：超高性能计算型 - diskintensive：磁盘增强型 - highio：超高I/O型 - fpga：FPGA加速型  > 说明：  - 早期注册的规格该字段为hws:performancetype。

        :param ecsperformancetype: The ecsperformancetype of this FlavorExtraSpec.
        :type: str
        """
        self._ecsperformancetype = ecsperformancetype

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
        :type: str
        """
        self._resource_type = resource_type

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
        :type: str
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
        :type: str
        """
        self._quotanvme_ssd = quotanvme_ssd

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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
        """
        self._condoperationcharge = condoperationcharge

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
        if not isinstance(other, FlavorExtraSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
