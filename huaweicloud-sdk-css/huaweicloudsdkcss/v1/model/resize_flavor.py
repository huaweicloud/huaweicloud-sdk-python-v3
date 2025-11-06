# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeFlavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'str_id': 'str',
        'cpu': 'int',
        'ram': 'int',
        'name': 'str',
        'region': 'str',
        'diskrange': 'str',
        'typename': 'str',
        'cond_operation_status': 'str',
        'localdisk': 'str',
        'edge': 'bool'
    }

    attribute_map = {
        'str_id': 'str_id',
        'cpu': 'cpu',
        'ram': 'ram',
        'name': 'name',
        'region': 'region',
        'diskrange': 'diskrange',
        'typename': 'typename',
        'cond_operation_status': 'condOperationStatus',
        'localdisk': 'localdisk',
        'edge': 'edge'
    }

    def __init__(self, str_id=None, cpu=None, ram=None, name=None, region=None, diskrange=None, typename=None, cond_operation_status=None, localdisk=None, edge=None):
        r"""ResizeFlavor

        The model defined in huaweicloud sdk

        :param str_id: **参数解释**： 规格id。 **取值范围**： 不涉及
        :type str_id: str
        :param cpu: **参数解释**： 实例的CPU核数。 **取值范围**： 不涉及
        :type cpu: int
        :param ram: **参数解释**： 实例的内存大小。单位GB。 **取值范围**： 不涉及
        :type ram: int
        :param name: **参数解释**： 规格名称。 **取值范围**： 不涉及
        :type name: str
        :param region: **参数解释**： 节点规格支持的Region。 **取值范围**： 不涉及
        :type region: str
        :param diskrange: **参数解释**： 实例的硬盘容量范围，单位GB。 **取值范围**： 不涉及
        :type diskrange: str
        :param typename: **参数解释**： 节点类型。 **取值范围**： - ess：数据节点。 - ess-cold：冷数据节点。 - ess-client：Client节点。 - ess-master：Master节点。 - lgs：LogStash节点。
        :type typename: str
        :param cond_operation_status: **参数解释**： 规格售卖状态。 **取值范围**： - normal：正常商用。 - sellout：售罄。
        :type cond_operation_status: str
        :param localdisk: **参数解释**： 是否本地盘。 **取值范围**： - false：非本地盘规格。 - true：本地盘规格。
        :type localdisk: str
        :param edge: **参数解释**： 是否边缘区规格。 **取值范围**： - false：中心可用区规格。 - true：边缘可用区规格。
        :type edge: bool
        """
        
        

        self._str_id = None
        self._cpu = None
        self._ram = None
        self._name = None
        self._region = None
        self._diskrange = None
        self._typename = None
        self._cond_operation_status = None
        self._localdisk = None
        self._edge = None
        self.discriminator = None

        if str_id is not None:
            self.str_id = str_id
        if cpu is not None:
            self.cpu = cpu
        if ram is not None:
            self.ram = ram
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if diskrange is not None:
            self.diskrange = diskrange
        if typename is not None:
            self.typename = typename
        if cond_operation_status is not None:
            self.cond_operation_status = cond_operation_status
        if localdisk is not None:
            self.localdisk = localdisk
        if edge is not None:
            self.edge = edge

    @property
    def str_id(self):
        r"""Gets the str_id of this ResizeFlavor.

        **参数解释**： 规格id。 **取值范围**： 不涉及

        :return: The str_id of this ResizeFlavor.
        :rtype: str
        """
        return self._str_id

    @str_id.setter
    def str_id(self, str_id):
        r"""Sets the str_id of this ResizeFlavor.

        **参数解释**： 规格id。 **取值范围**： 不涉及

        :param str_id: The str_id of this ResizeFlavor.
        :type str_id: str
        """
        self._str_id = str_id

    @property
    def cpu(self):
        r"""Gets the cpu of this ResizeFlavor.

        **参数解释**： 实例的CPU核数。 **取值范围**： 不涉及

        :return: The cpu of this ResizeFlavor.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ResizeFlavor.

        **参数解释**： 实例的CPU核数。 **取值范围**： 不涉及

        :param cpu: The cpu of this ResizeFlavor.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def ram(self):
        r"""Gets the ram of this ResizeFlavor.

        **参数解释**： 实例的内存大小。单位GB。 **取值范围**： 不涉及

        :return: The ram of this ResizeFlavor.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this ResizeFlavor.

        **参数解释**： 实例的内存大小。单位GB。 **取值范围**： 不涉及

        :param ram: The ram of this ResizeFlavor.
        :type ram: int
        """
        self._ram = ram

    @property
    def name(self):
        r"""Gets the name of this ResizeFlavor.

        **参数解释**： 规格名称。 **取值范围**： 不涉及

        :return: The name of this ResizeFlavor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ResizeFlavor.

        **参数解释**： 规格名称。 **取值范围**： 不涉及

        :param name: The name of this ResizeFlavor.
        :type name: str
        """
        self._name = name

    @property
    def region(self):
        r"""Gets the region of this ResizeFlavor.

        **参数解释**： 节点规格支持的Region。 **取值范围**： 不涉及

        :return: The region of this ResizeFlavor.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ResizeFlavor.

        **参数解释**： 节点规格支持的Region。 **取值范围**： 不涉及

        :param region: The region of this ResizeFlavor.
        :type region: str
        """
        self._region = region

    @property
    def diskrange(self):
        r"""Gets the diskrange of this ResizeFlavor.

        **参数解释**： 实例的硬盘容量范围，单位GB。 **取值范围**： 不涉及

        :return: The diskrange of this ResizeFlavor.
        :rtype: str
        """
        return self._diskrange

    @diskrange.setter
    def diskrange(self, diskrange):
        r"""Sets the diskrange of this ResizeFlavor.

        **参数解释**： 实例的硬盘容量范围，单位GB。 **取值范围**： 不涉及

        :param diskrange: The diskrange of this ResizeFlavor.
        :type diskrange: str
        """
        self._diskrange = diskrange

    @property
    def typename(self):
        r"""Gets the typename of this ResizeFlavor.

        **参数解释**： 节点类型。 **取值范围**： - ess：数据节点。 - ess-cold：冷数据节点。 - ess-client：Client节点。 - ess-master：Master节点。 - lgs：LogStash节点。

        :return: The typename of this ResizeFlavor.
        :rtype: str
        """
        return self._typename

    @typename.setter
    def typename(self, typename):
        r"""Sets the typename of this ResizeFlavor.

        **参数解释**： 节点类型。 **取值范围**： - ess：数据节点。 - ess-cold：冷数据节点。 - ess-client：Client节点。 - ess-master：Master节点。 - lgs：LogStash节点。

        :param typename: The typename of this ResizeFlavor.
        :type typename: str
        """
        self._typename = typename

    @property
    def cond_operation_status(self):
        r"""Gets the cond_operation_status of this ResizeFlavor.

        **参数解释**： 规格售卖状态。 **取值范围**： - normal：正常商用。 - sellout：售罄。

        :return: The cond_operation_status of this ResizeFlavor.
        :rtype: str
        """
        return self._cond_operation_status

    @cond_operation_status.setter
    def cond_operation_status(self, cond_operation_status):
        r"""Sets the cond_operation_status of this ResizeFlavor.

        **参数解释**： 规格售卖状态。 **取值范围**： - normal：正常商用。 - sellout：售罄。

        :param cond_operation_status: The cond_operation_status of this ResizeFlavor.
        :type cond_operation_status: str
        """
        self._cond_operation_status = cond_operation_status

    @property
    def localdisk(self):
        r"""Gets the localdisk of this ResizeFlavor.

        **参数解释**： 是否本地盘。 **取值范围**： - false：非本地盘规格。 - true：本地盘规格。

        :return: The localdisk of this ResizeFlavor.
        :rtype: str
        """
        return self._localdisk

    @localdisk.setter
    def localdisk(self, localdisk):
        r"""Sets the localdisk of this ResizeFlavor.

        **参数解释**： 是否本地盘。 **取值范围**： - false：非本地盘规格。 - true：本地盘规格。

        :param localdisk: The localdisk of this ResizeFlavor.
        :type localdisk: str
        """
        self._localdisk = localdisk

    @property
    def edge(self):
        r"""Gets the edge of this ResizeFlavor.

        **参数解释**： 是否边缘区规格。 **取值范围**： - false：中心可用区规格。 - true：边缘可用区规格。

        :return: The edge of this ResizeFlavor.
        :rtype: bool
        """
        return self._edge

    @edge.setter
    def edge(self, edge):
        r"""Sets the edge of this ResizeFlavor.

        **参数解释**： 是否边缘区规格。 **取值范围**： - false：中心可用区规格。 - true：边缘可用区规格。

        :param edge: The edge of this ResizeFlavor.
        :type edge: bool
        """
        self._edge = edge

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
        if not isinstance(other, ResizeFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
