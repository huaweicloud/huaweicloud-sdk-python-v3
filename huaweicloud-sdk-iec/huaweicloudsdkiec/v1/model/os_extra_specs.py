# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OsExtraSpecs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condoperationstatus': 'str',
        'ecsgeneration': 'str',
        'ecsperformancetype': 'str',
        'ecsvirtualization_env_types': 'str',
        'infocpuname': 'str',
        'infogpuname': 'str',
        'pci_passthroughalias': 'str',
        'pci_passthroughenable_gpu': 'str',
        'pci_passthroughgpu_specs': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'condoperationstatus': 'cond:operation:status',
        'ecsgeneration': 'ecs:generation',
        'ecsperformancetype': 'ecs:performancetype',
        'ecsvirtualization_env_types': 'ecs:virtualization_env_types',
        'infocpuname': 'info:cpu:name',
        'infogpuname': 'info:gpu:name',
        'pci_passthroughalias': 'pci_passthrough:alias',
        'pci_passthroughenable_gpu': 'pci_passthrough:enable_gpu',
        'pci_passthroughgpu_specs': 'pci_passthrough:gpu_specs',
        'resource_type': 'resource_type'
    }

    def __init__(self, condoperationstatus=None, ecsgeneration=None, ecsperformancetype=None, ecsvirtualization_env_types=None, infocpuname=None, infogpuname=None, pci_passthroughalias=None, pci_passthroughenable_gpu=None, pci_passthroughgpu_specs=None, resource_type=None):
        """OsExtraSpecs

        The model defined in huaweicloud sdk

        :param condoperationstatus: 此参数是Region级配置，某个AZ没有在cond:operation:az参数中配置时默认使用此参数的取值。不配置或无此参数时等同于“normal”。
        :type condoperationstatus: str
        :param ecsgeneration: 边缘实例类型的代数。
        :type ecsgeneration: str
        :param ecsperformancetype: 边缘实例规格的分类。
        :type ecsperformancetype: str
        :param ecsvirtualization_env_types: 虚拟化类型。
        :type ecsvirtualization_env_types: str
        :param infocpuname: 此参数是规格的CPU详细信息。
        :type infocpuname: str
        :param infogpuname: 此参数是规格的GPU详细信息。
        :type infogpuname: str
        :param pci_passthroughalias: P1型本地直通GPU的型号和数量，参数值可设置为“nvidia-p100:1”，表示使用该规格创建的边缘实例将占用1张NVIDIA P100显卡。
        :type pci_passthroughalias: str
        :param pci_passthroughenable_gpu: 显卡是否直通。 值为“true”，表示GPU直通。
        :type pci_passthroughenable_gpu: str
        :param pci_passthroughgpu_specs: G1型和G2型边缘实例应用的技术，包括GPU虚拟化和GPU直通。
        :type pci_passthroughgpu_specs: str
        :param resource_type: 资源类型，resource_type是为了区分边缘实例的物理主机类型。
        :type resource_type: str
        """
        
        

        self._condoperationstatus = None
        self._ecsgeneration = None
        self._ecsperformancetype = None
        self._ecsvirtualization_env_types = None
        self._infocpuname = None
        self._infogpuname = None
        self._pci_passthroughalias = None
        self._pci_passthroughenable_gpu = None
        self._pci_passthroughgpu_specs = None
        self._resource_type = None
        self.discriminator = None

        if condoperationstatus is not None:
            self.condoperationstatus = condoperationstatus
        if ecsgeneration is not None:
            self.ecsgeneration = ecsgeneration
        if ecsperformancetype is not None:
            self.ecsperformancetype = ecsperformancetype
        if ecsvirtualization_env_types is not None:
            self.ecsvirtualization_env_types = ecsvirtualization_env_types
        if infocpuname is not None:
            self.infocpuname = infocpuname
        if infogpuname is not None:
            self.infogpuname = infogpuname
        if pci_passthroughalias is not None:
            self.pci_passthroughalias = pci_passthroughalias
        if pci_passthroughenable_gpu is not None:
            self.pci_passthroughenable_gpu = pci_passthroughenable_gpu
        if pci_passthroughgpu_specs is not None:
            self.pci_passthroughgpu_specs = pci_passthroughgpu_specs
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def condoperationstatus(self):
        """Gets the condoperationstatus of this OsExtraSpecs.

        此参数是Region级配置，某个AZ没有在cond:operation:az参数中配置时默认使用此参数的取值。不配置或无此参数时等同于“normal”。

        :return: The condoperationstatus of this OsExtraSpecs.
        :rtype: str
        """
        return self._condoperationstatus

    @condoperationstatus.setter
    def condoperationstatus(self, condoperationstatus):
        """Sets the condoperationstatus of this OsExtraSpecs.

        此参数是Region级配置，某个AZ没有在cond:operation:az参数中配置时默认使用此参数的取值。不配置或无此参数时等同于“normal”。

        :param condoperationstatus: The condoperationstatus of this OsExtraSpecs.
        :type condoperationstatus: str
        """
        self._condoperationstatus = condoperationstatus

    @property
    def ecsgeneration(self):
        """Gets the ecsgeneration of this OsExtraSpecs.

        边缘实例类型的代数。

        :return: The ecsgeneration of this OsExtraSpecs.
        :rtype: str
        """
        return self._ecsgeneration

    @ecsgeneration.setter
    def ecsgeneration(self, ecsgeneration):
        """Sets the ecsgeneration of this OsExtraSpecs.

        边缘实例类型的代数。

        :param ecsgeneration: The ecsgeneration of this OsExtraSpecs.
        :type ecsgeneration: str
        """
        self._ecsgeneration = ecsgeneration

    @property
    def ecsperformancetype(self):
        """Gets the ecsperformancetype of this OsExtraSpecs.

        边缘实例规格的分类。

        :return: The ecsperformancetype of this OsExtraSpecs.
        :rtype: str
        """
        return self._ecsperformancetype

    @ecsperformancetype.setter
    def ecsperformancetype(self, ecsperformancetype):
        """Sets the ecsperformancetype of this OsExtraSpecs.

        边缘实例规格的分类。

        :param ecsperformancetype: The ecsperformancetype of this OsExtraSpecs.
        :type ecsperformancetype: str
        """
        self._ecsperformancetype = ecsperformancetype

    @property
    def ecsvirtualization_env_types(self):
        """Gets the ecsvirtualization_env_types of this OsExtraSpecs.

        虚拟化类型。

        :return: The ecsvirtualization_env_types of this OsExtraSpecs.
        :rtype: str
        """
        return self._ecsvirtualization_env_types

    @ecsvirtualization_env_types.setter
    def ecsvirtualization_env_types(self, ecsvirtualization_env_types):
        """Sets the ecsvirtualization_env_types of this OsExtraSpecs.

        虚拟化类型。

        :param ecsvirtualization_env_types: The ecsvirtualization_env_types of this OsExtraSpecs.
        :type ecsvirtualization_env_types: str
        """
        self._ecsvirtualization_env_types = ecsvirtualization_env_types

    @property
    def infocpuname(self):
        """Gets the infocpuname of this OsExtraSpecs.

        此参数是规格的CPU详细信息。

        :return: The infocpuname of this OsExtraSpecs.
        :rtype: str
        """
        return self._infocpuname

    @infocpuname.setter
    def infocpuname(self, infocpuname):
        """Sets the infocpuname of this OsExtraSpecs.

        此参数是规格的CPU详细信息。

        :param infocpuname: The infocpuname of this OsExtraSpecs.
        :type infocpuname: str
        """
        self._infocpuname = infocpuname

    @property
    def infogpuname(self):
        """Gets the infogpuname of this OsExtraSpecs.

        此参数是规格的GPU详细信息。

        :return: The infogpuname of this OsExtraSpecs.
        :rtype: str
        """
        return self._infogpuname

    @infogpuname.setter
    def infogpuname(self, infogpuname):
        """Sets the infogpuname of this OsExtraSpecs.

        此参数是规格的GPU详细信息。

        :param infogpuname: The infogpuname of this OsExtraSpecs.
        :type infogpuname: str
        """
        self._infogpuname = infogpuname

    @property
    def pci_passthroughalias(self):
        """Gets the pci_passthroughalias of this OsExtraSpecs.

        P1型本地直通GPU的型号和数量，参数值可设置为“nvidia-p100:1”，表示使用该规格创建的边缘实例将占用1张NVIDIA P100显卡。

        :return: The pci_passthroughalias of this OsExtraSpecs.
        :rtype: str
        """
        return self._pci_passthroughalias

    @pci_passthroughalias.setter
    def pci_passthroughalias(self, pci_passthroughalias):
        """Sets the pci_passthroughalias of this OsExtraSpecs.

        P1型本地直通GPU的型号和数量，参数值可设置为“nvidia-p100:1”，表示使用该规格创建的边缘实例将占用1张NVIDIA P100显卡。

        :param pci_passthroughalias: The pci_passthroughalias of this OsExtraSpecs.
        :type pci_passthroughalias: str
        """
        self._pci_passthroughalias = pci_passthroughalias

    @property
    def pci_passthroughenable_gpu(self):
        """Gets the pci_passthroughenable_gpu of this OsExtraSpecs.

        显卡是否直通。 值为“true”，表示GPU直通。

        :return: The pci_passthroughenable_gpu of this OsExtraSpecs.
        :rtype: str
        """
        return self._pci_passthroughenable_gpu

    @pci_passthroughenable_gpu.setter
    def pci_passthroughenable_gpu(self, pci_passthroughenable_gpu):
        """Sets the pci_passthroughenable_gpu of this OsExtraSpecs.

        显卡是否直通。 值为“true”，表示GPU直通。

        :param pci_passthroughenable_gpu: The pci_passthroughenable_gpu of this OsExtraSpecs.
        :type pci_passthroughenable_gpu: str
        """
        self._pci_passthroughenable_gpu = pci_passthroughenable_gpu

    @property
    def pci_passthroughgpu_specs(self):
        """Gets the pci_passthroughgpu_specs of this OsExtraSpecs.

        G1型和G2型边缘实例应用的技术，包括GPU虚拟化和GPU直通。

        :return: The pci_passthroughgpu_specs of this OsExtraSpecs.
        :rtype: str
        """
        return self._pci_passthroughgpu_specs

    @pci_passthroughgpu_specs.setter
    def pci_passthroughgpu_specs(self, pci_passthroughgpu_specs):
        """Sets the pci_passthroughgpu_specs of this OsExtraSpecs.

        G1型和G2型边缘实例应用的技术，包括GPU虚拟化和GPU直通。

        :param pci_passthroughgpu_specs: The pci_passthroughgpu_specs of this OsExtraSpecs.
        :type pci_passthroughgpu_specs: str
        """
        self._pci_passthroughgpu_specs = pci_passthroughgpu_specs

    @property
    def resource_type(self):
        """Gets the resource_type of this OsExtraSpecs.

        资源类型，resource_type是为了区分边缘实例的物理主机类型。

        :return: The resource_type of this OsExtraSpecs.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this OsExtraSpecs.

        资源类型，resource_type是为了区分边缘实例的物理主机类型。

        :param resource_type: The resource_type of this OsExtraSpecs.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, OsExtraSpecs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
