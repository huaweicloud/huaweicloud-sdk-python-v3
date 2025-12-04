# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProductsRespDetail1:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tps': 'str',
        'storage': 'str',
        'partition_num': 'str',
        'product_id': 'str',
        'spec_code': 'str',
        'io': 'list[ListProductsRespIo1]',
        'bandwidth': 'str',
        'unavailable_zones': 'list[str]',
        'available_zones': 'list[str]',
        'ecs_flavor_id': 'str',
        'arch_type': 'str'
    }

    attribute_map = {
        'tps': 'tps',
        'storage': 'storage',
        'partition_num': 'partition_num',
        'product_id': 'product_id',
        'spec_code': 'spec_code',
        'io': 'io',
        'bandwidth': 'bandwidth',
        'unavailable_zones': 'unavailable_zones',
        'available_zones': 'available_zones',
        'ecs_flavor_id': 'ecs_flavor_id',
        'arch_type': 'arch_type'
    }

    def __init__(self, tps=None, storage=None, partition_num=None, product_id=None, spec_code=None, io=None, bandwidth=None, unavailable_zones=None, available_zones=None, ecs_flavor_id=None, arch_type=None):
        r"""ListProductsRespDetail1

        The model defined in huaweicloud sdk

        :param tps: **参数解释**： 单位时间内的消息量最大值。 **取值范围**： 不涉及。
        :type tps: str
        :param storage: **参数解释**： 消息存储空间。 **取值范围**： 不涉及。
        :type storage: str
        :param partition_num: **参数解释**： Kafka实例的分区数量。 **取值范围**： 不涉及。
        :type partition_num: str
        :param product_id: **参数解释**： 产品ID。 **取值范围**： 不涉及。
        :type product_id: str
        :param spec_code: **参数解释**： 规格ID。 **取值范围**： 不涉及。
        :type spec_code: str
        :param io: **参数解释**： IO信息。 **取值范围**： 不涉及。
        :type io: list[:class:`huaweicloudsdkkafka.v2.ListProductsRespIo1`]
        :param bandwidth: **参数解释**： Kafka实例的基准带宽。 **取值范围**： 不涉及。
        :type bandwidth: str
        :param unavailable_zones: **参数解释**： 资源售罄的可用区列表。 **取值范围**： 不涉及。
        :type unavailable_zones: list[str]
        :param available_zones: **参数解释**： 有可用资源的可用区列表。 **取值范围**： 不涉及。
        :type available_zones: list[str]
        :param ecs_flavor_id: **参数解释**： 该产品规格对应的虚拟机规格。 **取值范围**： 不涉及。
        :type ecs_flavor_id: str
        :param arch_type: **参数解释**： 实例规格架构类型。当前仅支持X86。 **取值范围**： 不涉及。
        :type arch_type: str
        """
        
        

        self._tps = None
        self._storage = None
        self._partition_num = None
        self._product_id = None
        self._spec_code = None
        self._io = None
        self._bandwidth = None
        self._unavailable_zones = None
        self._available_zones = None
        self._ecs_flavor_id = None
        self._arch_type = None
        self.discriminator = None

        if tps is not None:
            self.tps = tps
        if storage is not None:
            self.storage = storage
        if partition_num is not None:
            self.partition_num = partition_num
        if product_id is not None:
            self.product_id = product_id
        if spec_code is not None:
            self.spec_code = spec_code
        if io is not None:
            self.io = io
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if unavailable_zones is not None:
            self.unavailable_zones = unavailable_zones
        if available_zones is not None:
            self.available_zones = available_zones
        if ecs_flavor_id is not None:
            self.ecs_flavor_id = ecs_flavor_id
        if arch_type is not None:
            self.arch_type = arch_type

    @property
    def tps(self):
        r"""Gets the tps of this ListProductsRespDetail1.

        **参数解释**： 单位时间内的消息量最大值。 **取值范围**： 不涉及。

        :return: The tps of this ListProductsRespDetail1.
        :rtype: str
        """
        return self._tps

    @tps.setter
    def tps(self, tps):
        r"""Sets the tps of this ListProductsRespDetail1.

        **参数解释**： 单位时间内的消息量最大值。 **取值范围**： 不涉及。

        :param tps: The tps of this ListProductsRespDetail1.
        :type tps: str
        """
        self._tps = tps

    @property
    def storage(self):
        r"""Gets the storage of this ListProductsRespDetail1.

        **参数解释**： 消息存储空间。 **取值范围**： 不涉及。

        :return: The storage of this ListProductsRespDetail1.
        :rtype: str
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        r"""Sets the storage of this ListProductsRespDetail1.

        **参数解释**： 消息存储空间。 **取值范围**： 不涉及。

        :param storage: The storage of this ListProductsRespDetail1.
        :type storage: str
        """
        self._storage = storage

    @property
    def partition_num(self):
        r"""Gets the partition_num of this ListProductsRespDetail1.

        **参数解释**： Kafka实例的分区数量。 **取值范围**： 不涉及。

        :return: The partition_num of this ListProductsRespDetail1.
        :rtype: str
        """
        return self._partition_num

    @partition_num.setter
    def partition_num(self, partition_num):
        r"""Sets the partition_num of this ListProductsRespDetail1.

        **参数解释**： Kafka实例的分区数量。 **取值范围**： 不涉及。

        :param partition_num: The partition_num of this ListProductsRespDetail1.
        :type partition_num: str
        """
        self._partition_num = partition_num

    @property
    def product_id(self):
        r"""Gets the product_id of this ListProductsRespDetail1.

        **参数解释**： 产品ID。 **取值范围**： 不涉及。

        :return: The product_id of this ListProductsRespDetail1.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ListProductsRespDetail1.

        **参数解释**： 产品ID。 **取值范围**： 不涉及。

        :param product_id: The product_id of this ListProductsRespDetail1.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ListProductsRespDetail1.

        **参数解释**： 规格ID。 **取值范围**： 不涉及。

        :return: The spec_code of this ListProductsRespDetail1.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ListProductsRespDetail1.

        **参数解释**： 规格ID。 **取值范围**： 不涉及。

        :param spec_code: The spec_code of this ListProductsRespDetail1.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def io(self):
        r"""Gets the io of this ListProductsRespDetail1.

        **参数解释**： IO信息。 **取值范围**： 不涉及。

        :return: The io of this ListProductsRespDetail1.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ListProductsRespIo1`]
        """
        return self._io

    @io.setter
    def io(self, io):
        r"""Sets the io of this ListProductsRespDetail1.

        **参数解释**： IO信息。 **取值范围**： 不涉及。

        :param io: The io of this ListProductsRespDetail1.
        :type io: list[:class:`huaweicloudsdkkafka.v2.ListProductsRespIo1`]
        """
        self._io = io

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this ListProductsRespDetail1.

        **参数解释**： Kafka实例的基准带宽。 **取值范围**： 不涉及。

        :return: The bandwidth of this ListProductsRespDetail1.
        :rtype: str
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this ListProductsRespDetail1.

        **参数解释**： Kafka实例的基准带宽。 **取值范围**： 不涉及。

        :param bandwidth: The bandwidth of this ListProductsRespDetail1.
        :type bandwidth: str
        """
        self._bandwidth = bandwidth

    @property
    def unavailable_zones(self):
        r"""Gets the unavailable_zones of this ListProductsRespDetail1.

        **参数解释**： 资源售罄的可用区列表。 **取值范围**： 不涉及。

        :return: The unavailable_zones of this ListProductsRespDetail1.
        :rtype: list[str]
        """
        return self._unavailable_zones

    @unavailable_zones.setter
    def unavailable_zones(self, unavailable_zones):
        r"""Sets the unavailable_zones of this ListProductsRespDetail1.

        **参数解释**： 资源售罄的可用区列表。 **取值范围**： 不涉及。

        :param unavailable_zones: The unavailable_zones of this ListProductsRespDetail1.
        :type unavailable_zones: list[str]
        """
        self._unavailable_zones = unavailable_zones

    @property
    def available_zones(self):
        r"""Gets the available_zones of this ListProductsRespDetail1.

        **参数解释**： 有可用资源的可用区列表。 **取值范围**： 不涉及。

        :return: The available_zones of this ListProductsRespDetail1.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this ListProductsRespDetail1.

        **参数解释**： 有可用资源的可用区列表。 **取值范围**： 不涉及。

        :param available_zones: The available_zones of this ListProductsRespDetail1.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def ecs_flavor_id(self):
        r"""Gets the ecs_flavor_id of this ListProductsRespDetail1.

        **参数解释**： 该产品规格对应的虚拟机规格。 **取值范围**： 不涉及。

        :return: The ecs_flavor_id of this ListProductsRespDetail1.
        :rtype: str
        """
        return self._ecs_flavor_id

    @ecs_flavor_id.setter
    def ecs_flavor_id(self, ecs_flavor_id):
        r"""Sets the ecs_flavor_id of this ListProductsRespDetail1.

        **参数解释**： 该产品规格对应的虚拟机规格。 **取值范围**： 不涉及。

        :param ecs_flavor_id: The ecs_flavor_id of this ListProductsRespDetail1.
        :type ecs_flavor_id: str
        """
        self._ecs_flavor_id = ecs_flavor_id

    @property
    def arch_type(self):
        r"""Gets the arch_type of this ListProductsRespDetail1.

        **参数解释**： 实例规格架构类型。当前仅支持X86。 **取值范围**： 不涉及。

        :return: The arch_type of this ListProductsRespDetail1.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        r"""Sets the arch_type of this ListProductsRespDetail1.

        **参数解释**： 实例规格架构类型。当前仅支持X86。 **取值范围**： 不涉及。

        :param arch_type: The arch_type of this ListProductsRespDetail1.
        :type arch_type: str
        """
        self._arch_type = arch_type

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
        if not isinstance(other, ListProductsRespDetail1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
