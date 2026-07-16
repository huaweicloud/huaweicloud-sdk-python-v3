# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotebookFlavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'arch': 'str',
        'ascend': 'AscendInfo',
        'billing': 'BillingInfo',
        'category': 'str',
        'description': 'str',
        'feature': 'str',
        'free': 'bool',
        'gpu': 'GPUInfo',
        'id': 'str',
        'memory': 'int',
        'name': 'str',
        'sold_out': 'bool',
        'storages': 'list[str]',
        'vcpus': 'int',
        'evs_max_size': 'str',
        'evs_sku_code': 'str',
        'grow_support_type': 'str'
    }

    attribute_map = {
        'arch': 'arch',
        'ascend': 'ascend',
        'billing': 'billing',
        'category': 'category',
        'description': 'description',
        'feature': 'feature',
        'free': 'free',
        'gpu': 'gpu',
        'id': 'id',
        'memory': 'memory',
        'name': 'name',
        'sold_out': 'sold_out',
        'storages': 'storages',
        'vcpus': 'vcpus',
        'evs_max_size': 'evs_max_size',
        'evs_sku_code': 'evs_sku_code',
        'grow_support_type': 'grow_support_type'
    }

    def __init__(self, arch=None, ascend=None, billing=None, category=None, description=None, feature=None, free=None, gpu=None, id=None, memory=None, name=None, sold_out=None, storages=None, vcpus=None, evs_max_size=None, evs_sku_code=None, grow_support_type=None):
        r"""NotebookFlavor

        The model defined in huaweicloud sdk

        :param arch: **参数解释**：架构类型。 **取值范围**：枚举类型，取值如下： - x86_64 - aarch64
        :type arch: str
        :param ascend: 
        :type ascend: :class:`huaweicloudsdkmodelarts.v1.AscendInfo`
        :param billing: 
        :type billing: :class:`huaweicloudsdkmodelarts.v1.BillingInfo`
        :param category: **参数解释**：规格处理器类型。 **取值范围**：枚举类型，取值如下： - CPU - GPU - [ASCEND](tag:hc,hk,fcs_super)
        :type category: str
        :param description: **参数解释**：规格描述信息。 **取值范围**：不涉及。
        :type description: str
        :param feature: **参数解释**：实例类别。 **取值范围**：枚举类型，取值如下： - DEFAULT：CodeLab免费规格实例，每个用户最多只能创建一个。 - NOTEBOOK：计费规格实例。
        :type feature: str
        :param free: **参数解释**：是否为免费规格。 **取值范围**：布尔类型： - true：免费规格。 - false：不是免费规格。
        :type free: bool
        :param gpu: 
        :type gpu: :class:`huaweicloudsdkmodelarts.v1.GPUInfo`
        :param id: **参数解释**：规格ID。 **取值范围**：不涉及。
        :type id: str
        :param memory: **参数解释**：内存大小。 **取值范围**：不涉及。
        :type memory: int
        :param name: **参数解释**：规格名称。 **取值范围**：不涉及。
        :type name: str
        :param sold_out: **参数解释**：资源是否充足。 **取值范围**：布尔类型： - true 资源不足 - false 资源充足
        :type sold_out: bool
        :param storages: **参数解释**：规格支持的存储类型。枚举类型，取值如下： - EFS - EVS
        :type storages: list[str]
        :param vcpus: **参数解释**：CPU核数。 **取值范围**：不涉及。
        :type vcpus: int
        :param evs_max_size: **参数解释**：规格包含EVS时，EVS存储创建的最大上限(单位：GB)。 **取值范围**：不涉及。
        :type evs_max_size: str
        :param evs_sku_code: **参数解释**：规格包含EVS时，EVS存储的sku编码。 **取值范围**：不涉及。
        :type evs_sku_code: str
        :param grow_support_type: **参数解释**：支持站点类型。 **取值范围**：枚举类型，取值如下： - COMMON：国内与国际站都支持。 - NATIONAL：仅在国内站支持。 - INTERNATIONAL：仅在国际站支持。 - NONE：国内与国际站都不支持。
        :type grow_support_type: str
        """
        
        

        self._arch = None
        self._ascend = None
        self._billing = None
        self._category = None
        self._description = None
        self._feature = None
        self._free = None
        self._gpu = None
        self._id = None
        self._memory = None
        self._name = None
        self._sold_out = None
        self._storages = None
        self._vcpus = None
        self._evs_max_size = None
        self._evs_sku_code = None
        self._grow_support_type = None
        self.discriminator = None

        if arch is not None:
            self.arch = arch
        if ascend is not None:
            self.ascend = ascend
        if billing is not None:
            self.billing = billing
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if feature is not None:
            self.feature = feature
        if free is not None:
            self.free = free
        if gpu is not None:
            self.gpu = gpu
        if id is not None:
            self.id = id
        if memory is not None:
            self.memory = memory
        if name is not None:
            self.name = name
        if sold_out is not None:
            self.sold_out = sold_out
        if storages is not None:
            self.storages = storages
        if vcpus is not None:
            self.vcpus = vcpus
        if evs_max_size is not None:
            self.evs_max_size = evs_max_size
        if evs_sku_code is not None:
            self.evs_sku_code = evs_sku_code
        if grow_support_type is not None:
            self.grow_support_type = grow_support_type

    @property
    def arch(self):
        r"""Gets the arch of this NotebookFlavor.

        **参数解释**：架构类型。 **取值范围**：枚举类型，取值如下： - x86_64 - aarch64

        :return: The arch of this NotebookFlavor.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this NotebookFlavor.

        **参数解释**：架构类型。 **取值范围**：枚举类型，取值如下： - x86_64 - aarch64

        :param arch: The arch of this NotebookFlavor.
        :type arch: str
        """
        self._arch = arch

    @property
    def ascend(self):
        r"""Gets the ascend of this NotebookFlavor.

        :return: The ascend of this NotebookFlavor.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AscendInfo`
        """
        return self._ascend

    @ascend.setter
    def ascend(self, ascend):
        r"""Sets the ascend of this NotebookFlavor.

        :param ascend: The ascend of this NotebookFlavor.
        :type ascend: :class:`huaweicloudsdkmodelarts.v1.AscendInfo`
        """
        self._ascend = ascend

    @property
    def billing(self):
        r"""Gets the billing of this NotebookFlavor.

        :return: The billing of this NotebookFlavor.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BillingInfo`
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        r"""Sets the billing of this NotebookFlavor.

        :param billing: The billing of this NotebookFlavor.
        :type billing: :class:`huaweicloudsdkmodelarts.v1.BillingInfo`
        """
        self._billing = billing

    @property
    def category(self):
        r"""Gets the category of this NotebookFlavor.

        **参数解释**：规格处理器类型。 **取值范围**：枚举类型，取值如下： - CPU - GPU - [ASCEND](tag:hc,hk,fcs_super)

        :return: The category of this NotebookFlavor.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this NotebookFlavor.

        **参数解释**：规格处理器类型。 **取值范围**：枚举类型，取值如下： - CPU - GPU - [ASCEND](tag:hc,hk,fcs_super)

        :param category: The category of this NotebookFlavor.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        r"""Gets the description of this NotebookFlavor.

        **参数解释**：规格描述信息。 **取值范围**：不涉及。

        :return: The description of this NotebookFlavor.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this NotebookFlavor.

        **参数解释**：规格描述信息。 **取值范围**：不涉及。

        :param description: The description of this NotebookFlavor.
        :type description: str
        """
        self._description = description

    @property
    def feature(self):
        r"""Gets the feature of this NotebookFlavor.

        **参数解释**：实例类别。 **取值范围**：枚举类型，取值如下： - DEFAULT：CodeLab免费规格实例，每个用户最多只能创建一个。 - NOTEBOOK：计费规格实例。

        :return: The feature of this NotebookFlavor.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this NotebookFlavor.

        **参数解释**：实例类别。 **取值范围**：枚举类型，取值如下： - DEFAULT：CodeLab免费规格实例，每个用户最多只能创建一个。 - NOTEBOOK：计费规格实例。

        :param feature: The feature of this NotebookFlavor.
        :type feature: str
        """
        self._feature = feature

    @property
    def free(self):
        r"""Gets the free of this NotebookFlavor.

        **参数解释**：是否为免费规格。 **取值范围**：布尔类型： - true：免费规格。 - false：不是免费规格。

        :return: The free of this NotebookFlavor.
        :rtype: bool
        """
        return self._free

    @free.setter
    def free(self, free):
        r"""Sets the free of this NotebookFlavor.

        **参数解释**：是否为免费规格。 **取值范围**：布尔类型： - true：免费规格。 - false：不是免费规格。

        :param free: The free of this NotebookFlavor.
        :type free: bool
        """
        self._free = free

    @property
    def gpu(self):
        r"""Gets the gpu of this NotebookFlavor.

        :return: The gpu of this NotebookFlavor.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.GPUInfo`
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this NotebookFlavor.

        :param gpu: The gpu of this NotebookFlavor.
        :type gpu: :class:`huaweicloudsdkmodelarts.v1.GPUInfo`
        """
        self._gpu = gpu

    @property
    def id(self):
        r"""Gets the id of this NotebookFlavor.

        **参数解释**：规格ID。 **取值范围**：不涉及。

        :return: The id of this NotebookFlavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NotebookFlavor.

        **参数解释**：规格ID。 **取值范围**：不涉及。

        :param id: The id of this NotebookFlavor.
        :type id: str
        """
        self._id = id

    @property
    def memory(self):
        r"""Gets the memory of this NotebookFlavor.

        **参数解释**：内存大小。 **取值范围**：不涉及。

        :return: The memory of this NotebookFlavor.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this NotebookFlavor.

        **参数解释**：内存大小。 **取值范围**：不涉及。

        :param memory: The memory of this NotebookFlavor.
        :type memory: int
        """
        self._memory = memory

    @property
    def name(self):
        r"""Gets the name of this NotebookFlavor.

        **参数解释**：规格名称。 **取值范围**：不涉及。

        :return: The name of this NotebookFlavor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NotebookFlavor.

        **参数解释**：规格名称。 **取值范围**：不涉及。

        :param name: The name of this NotebookFlavor.
        :type name: str
        """
        self._name = name

    @property
    def sold_out(self):
        r"""Gets the sold_out of this NotebookFlavor.

        **参数解释**：资源是否充足。 **取值范围**：布尔类型： - true 资源不足 - false 资源充足

        :return: The sold_out of this NotebookFlavor.
        :rtype: bool
        """
        return self._sold_out

    @sold_out.setter
    def sold_out(self, sold_out):
        r"""Sets the sold_out of this NotebookFlavor.

        **参数解释**：资源是否充足。 **取值范围**：布尔类型： - true 资源不足 - false 资源充足

        :param sold_out: The sold_out of this NotebookFlavor.
        :type sold_out: bool
        """
        self._sold_out = sold_out

    @property
    def storages(self):
        r"""Gets the storages of this NotebookFlavor.

        **参数解释**：规格支持的存储类型。枚举类型，取值如下： - EFS - EVS

        :return: The storages of this NotebookFlavor.
        :rtype: list[str]
        """
        return self._storages

    @storages.setter
    def storages(self, storages):
        r"""Sets the storages of this NotebookFlavor.

        **参数解释**：规格支持的存储类型。枚举类型，取值如下： - EFS - EVS

        :param storages: The storages of this NotebookFlavor.
        :type storages: list[str]
        """
        self._storages = storages

    @property
    def vcpus(self):
        r"""Gets the vcpus of this NotebookFlavor.

        **参数解释**：CPU核数。 **取值范围**：不涉及。

        :return: The vcpus of this NotebookFlavor.
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this NotebookFlavor.

        **参数解释**：CPU核数。 **取值范围**：不涉及。

        :param vcpus: The vcpus of this NotebookFlavor.
        :type vcpus: int
        """
        self._vcpus = vcpus

    @property
    def evs_max_size(self):
        r"""Gets the evs_max_size of this NotebookFlavor.

        **参数解释**：规格包含EVS时，EVS存储创建的最大上限(单位：GB)。 **取值范围**：不涉及。

        :return: The evs_max_size of this NotebookFlavor.
        :rtype: str
        """
        return self._evs_max_size

    @evs_max_size.setter
    def evs_max_size(self, evs_max_size):
        r"""Sets the evs_max_size of this NotebookFlavor.

        **参数解释**：规格包含EVS时，EVS存储创建的最大上限(单位：GB)。 **取值范围**：不涉及。

        :param evs_max_size: The evs_max_size of this NotebookFlavor.
        :type evs_max_size: str
        """
        self._evs_max_size = evs_max_size

    @property
    def evs_sku_code(self):
        r"""Gets the evs_sku_code of this NotebookFlavor.

        **参数解释**：规格包含EVS时，EVS存储的sku编码。 **取值范围**：不涉及。

        :return: The evs_sku_code of this NotebookFlavor.
        :rtype: str
        """
        return self._evs_sku_code

    @evs_sku_code.setter
    def evs_sku_code(self, evs_sku_code):
        r"""Sets the evs_sku_code of this NotebookFlavor.

        **参数解释**：规格包含EVS时，EVS存储的sku编码。 **取值范围**：不涉及。

        :param evs_sku_code: The evs_sku_code of this NotebookFlavor.
        :type evs_sku_code: str
        """
        self._evs_sku_code = evs_sku_code

    @property
    def grow_support_type(self):
        r"""Gets the grow_support_type of this NotebookFlavor.

        **参数解释**：支持站点类型。 **取值范围**：枚举类型，取值如下： - COMMON：国内与国际站都支持。 - NATIONAL：仅在国内站支持。 - INTERNATIONAL：仅在国际站支持。 - NONE：国内与国际站都不支持。

        :return: The grow_support_type of this NotebookFlavor.
        :rtype: str
        """
        return self._grow_support_type

    @grow_support_type.setter
    def grow_support_type(self, grow_support_type):
        r"""Sets the grow_support_type of this NotebookFlavor.

        **参数解释**：支持站点类型。 **取值范围**：枚举类型，取值如下： - COMMON：国内与国际站都支持。 - NATIONAL：仅在国内站支持。 - INTERNATIONAL：仅在国际站支持。 - NONE：国内与国际站都不支持。

        :param grow_support_type: The grow_support_type of this NotebookFlavor.
        :type grow_support_type: str
        """
        self._grow_support_type = grow_support_type

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
        if not isinstance(other, NotebookFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
