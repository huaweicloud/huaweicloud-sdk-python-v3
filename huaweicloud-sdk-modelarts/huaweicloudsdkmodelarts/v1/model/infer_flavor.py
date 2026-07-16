# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InferFlavor:

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
        'ascend': 'AscendResource',
        'billing': 'BillingResource',
        'category': 'str',
        'description': 'str',
        'feature': 'str',
        'free': 'bool',
        'gpu': 'GPUResource',
        'id': 'str',
        'memory': 'int',
        'name': 'str',
        'sold_out': 'bool',
        'storages': 'list[str]',
        'vcpus': 'int',
        'evs_max_size': 'str'
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
        'evs_max_size': 'evs_max_size'
    }

    def __init__(self, arch=None, ascend=None, billing=None, category=None, description=None, feature=None, free=None, gpu=None, id=None, memory=None, name=None, sold_out=None, storages=None, vcpus=None, evs_max_size=None):
        r"""InferFlavor

        The model defined in huaweicloud sdk

        :param arch: **参数解释：** 架构类型。 **取值范围：** - X86_64 - arm64
        :type arch: str
        :param ascend: 
        :type ascend: :class:`huaweicloudsdkmodelarts.v1.AscendResource`
        :param billing: 
        :type billing: :class:`huaweicloudsdkmodelarts.v1.BillingResource`
        :param category: **参数解释：** 规格处理器类型。 **取值范围：** - CPU - GPU - [ASCEND](tag:hws,hws_hk,hk,fcs_super)
        :type category: str
        :param description: **参数解释：** 规格描述信息。 **取值范围：** 不涉及。
        :type description: str
        :param feature: **参数解释：** 规格类别。 **取值范围：** - DEFAULT：CodeLab规格。 - NOTEBOOK：Notebook规格。
        :type feature: str
        :param free: **参数解释：** 是否为免费规格。 **取值范围：** - true: 免费规格。 - false: 付费规格。
        :type free: bool
        :param gpu: 
        :type gpu: :class:`huaweicloudsdkmodelarts.v1.GPUResource`
        :param id: **参数解释：** 规格ID。 **取值范围：** 不涉及。
        :type id: str
        :param memory: **参数解释：** 内存大小。 **取值范围：** 不涉及。
        :type memory: int
        :param name: **参数解释：** 规格名称。 **取值范围：** 不涉及。
        :type name: str
        :param sold_out: **参数解释：** 资源是否充足。 **取值范围：** - true 资源不足。 - false 资源充足。
        :type sold_out: bool
        :param storages: **参数解释：** 规格支持的存储类型。
        :type storages: list[str]
        :param vcpus: **参数解释：** CPU核数。 **取值范围：** 不涉及。
        :type vcpus: int
        :param evs_max_size: **参数解释：** EVS磁盘最大容量。 **取值范围：** 不涉及。
        :type evs_max_size: str
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

    @property
    def arch(self):
        r"""Gets the arch of this InferFlavor.

        **参数解释：** 架构类型。 **取值范围：** - X86_64 - arm64

        :return: The arch of this InferFlavor.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this InferFlavor.

        **参数解释：** 架构类型。 **取值范围：** - X86_64 - arm64

        :param arch: The arch of this InferFlavor.
        :type arch: str
        """
        self._arch = arch

    @property
    def ascend(self):
        r"""Gets the ascend of this InferFlavor.

        :return: The ascend of this InferFlavor.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AscendResource`
        """
        return self._ascend

    @ascend.setter
    def ascend(self, ascend):
        r"""Sets the ascend of this InferFlavor.

        :param ascend: The ascend of this InferFlavor.
        :type ascend: :class:`huaweicloudsdkmodelarts.v1.AscendResource`
        """
        self._ascend = ascend

    @property
    def billing(self):
        r"""Gets the billing of this InferFlavor.

        :return: The billing of this InferFlavor.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BillingResource`
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        r"""Sets the billing of this InferFlavor.

        :param billing: The billing of this InferFlavor.
        :type billing: :class:`huaweicloudsdkmodelarts.v1.BillingResource`
        """
        self._billing = billing

    @property
    def category(self):
        r"""Gets the category of this InferFlavor.

        **参数解释：** 规格处理器类型。 **取值范围：** - CPU - GPU - [ASCEND](tag:hws,hws_hk,hk,fcs_super)

        :return: The category of this InferFlavor.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this InferFlavor.

        **参数解释：** 规格处理器类型。 **取值范围：** - CPU - GPU - [ASCEND](tag:hws,hws_hk,hk,fcs_super)

        :param category: The category of this InferFlavor.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        r"""Gets the description of this InferFlavor.

        **参数解释：** 规格描述信息。 **取值范围：** 不涉及。

        :return: The description of this InferFlavor.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this InferFlavor.

        **参数解释：** 规格描述信息。 **取值范围：** 不涉及。

        :param description: The description of this InferFlavor.
        :type description: str
        """
        self._description = description

    @property
    def feature(self):
        r"""Gets the feature of this InferFlavor.

        **参数解释：** 规格类别。 **取值范围：** - DEFAULT：CodeLab规格。 - NOTEBOOK：Notebook规格。

        :return: The feature of this InferFlavor.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this InferFlavor.

        **参数解释：** 规格类别。 **取值范围：** - DEFAULT：CodeLab规格。 - NOTEBOOK：Notebook规格。

        :param feature: The feature of this InferFlavor.
        :type feature: str
        """
        self._feature = feature

    @property
    def free(self):
        r"""Gets the free of this InferFlavor.

        **参数解释：** 是否为免费规格。 **取值范围：** - true: 免费规格。 - false: 付费规格。

        :return: The free of this InferFlavor.
        :rtype: bool
        """
        return self._free

    @free.setter
    def free(self, free):
        r"""Sets the free of this InferFlavor.

        **参数解释：** 是否为免费规格。 **取值范围：** - true: 免费规格。 - false: 付费规格。

        :param free: The free of this InferFlavor.
        :type free: bool
        """
        self._free = free

    @property
    def gpu(self):
        r"""Gets the gpu of this InferFlavor.

        :return: The gpu of this InferFlavor.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.GPUResource`
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this InferFlavor.

        :param gpu: The gpu of this InferFlavor.
        :type gpu: :class:`huaweicloudsdkmodelarts.v1.GPUResource`
        """
        self._gpu = gpu

    @property
    def id(self):
        r"""Gets the id of this InferFlavor.

        **参数解释：** 规格ID。 **取值范围：** 不涉及。

        :return: The id of this InferFlavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InferFlavor.

        **参数解释：** 规格ID。 **取值范围：** 不涉及。

        :param id: The id of this InferFlavor.
        :type id: str
        """
        self._id = id

    @property
    def memory(self):
        r"""Gets the memory of this InferFlavor.

        **参数解释：** 内存大小。 **取值范围：** 不涉及。

        :return: The memory of this InferFlavor.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this InferFlavor.

        **参数解释：** 内存大小。 **取值范围：** 不涉及。

        :param memory: The memory of this InferFlavor.
        :type memory: int
        """
        self._memory = memory

    @property
    def name(self):
        r"""Gets the name of this InferFlavor.

        **参数解释：** 规格名称。 **取值范围：** 不涉及。

        :return: The name of this InferFlavor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InferFlavor.

        **参数解释：** 规格名称。 **取值范围：** 不涉及。

        :param name: The name of this InferFlavor.
        :type name: str
        """
        self._name = name

    @property
    def sold_out(self):
        r"""Gets the sold_out of this InferFlavor.

        **参数解释：** 资源是否充足。 **取值范围：** - true 资源不足。 - false 资源充足。

        :return: The sold_out of this InferFlavor.
        :rtype: bool
        """
        return self._sold_out

    @sold_out.setter
    def sold_out(self, sold_out):
        r"""Sets the sold_out of this InferFlavor.

        **参数解释：** 资源是否充足。 **取值范围：** - true 资源不足。 - false 资源充足。

        :param sold_out: The sold_out of this InferFlavor.
        :type sold_out: bool
        """
        self._sold_out = sold_out

    @property
    def storages(self):
        r"""Gets the storages of this InferFlavor.

        **参数解释：** 规格支持的存储类型。

        :return: The storages of this InferFlavor.
        :rtype: list[str]
        """
        return self._storages

    @storages.setter
    def storages(self, storages):
        r"""Sets the storages of this InferFlavor.

        **参数解释：** 规格支持的存储类型。

        :param storages: The storages of this InferFlavor.
        :type storages: list[str]
        """
        self._storages = storages

    @property
    def vcpus(self):
        r"""Gets the vcpus of this InferFlavor.

        **参数解释：** CPU核数。 **取值范围：** 不涉及。

        :return: The vcpus of this InferFlavor.
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this InferFlavor.

        **参数解释：** CPU核数。 **取值范围：** 不涉及。

        :param vcpus: The vcpus of this InferFlavor.
        :type vcpus: int
        """
        self._vcpus = vcpus

    @property
    def evs_max_size(self):
        r"""Gets the evs_max_size of this InferFlavor.

        **参数解释：** EVS磁盘最大容量。 **取值范围：** 不涉及。

        :return: The evs_max_size of this InferFlavor.
        :rtype: str
        """
        return self._evs_max_size

    @evs_max_size.setter
    def evs_max_size(self, evs_max_size):
        r"""Sets the evs_max_size of this InferFlavor.

        **参数解释：** EVS磁盘最大容量。 **取值范围：** 不涉及。

        :param evs_max_size: The evs_max_size of this InferFlavor.
        :type evs_max_size: str
        """
        self._evs_max_size = evs_max_size

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
        if not isinstance(other, InferFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
