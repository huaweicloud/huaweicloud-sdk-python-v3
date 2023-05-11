# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceExtendProductInfoRespDetail:

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
        'io': 'list[ListProductsRespIo]',
        'bandwidth': 'str',
        'recommend_max_cons_groups': 'str',
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
        'recommend_max_cons_groups': 'recommend_max_consGroups',
        'unavailable_zones': 'unavailable_zones',
        'available_zones': 'available_zones',
        'ecs_flavor_id': 'ecs_flavor_id',
        'arch_type': 'arch_type'
    }

    def __init__(self, tps=None, storage=None, partition_num=None, product_id=None, spec_code=None, io=None, bandwidth=None, recommend_max_cons_groups=None, unavailable_zones=None, available_zones=None, ecs_flavor_id=None, arch_type=None):
        """ShowInstanceExtendProductInfoRespDetail

        The model defined in huaweicloud sdk

        :param tps: 单位时间内的消息量最大值。
        :type tps: str
        :param storage: 消息存储空间。
        :type storage: str
        :param partition_num: Kafka实例的分区数量。
        :type partition_num: str
        :param product_id: 产品ID。
        :type product_id: str
        :param spec_code: 规格ID。
        :type spec_code: str
        :param io: IO信息。
        :type io: list[:class:`huaweicloudsdkkafka.v2.ListProductsRespIo`]
        :param bandwidth: Kafka实例的基准带宽。
        :type bandwidth: str
        :param recommend_max_cons_groups: Kafka实例最大消费组数参考值。
        :type recommend_max_cons_groups: str
        :param unavailable_zones: 资源售罄的可用区列表。
        :type unavailable_zones: list[str]
        :param available_zones: 有可用资源的可用区列表。
        :type available_zones: list[str]
        :param ecs_flavor_id: 该产品规格对应的虚拟机规格。
        :type ecs_flavor_id: str
        :param arch_type: 实例规格架构类型。当前仅支持X86。
        :type arch_type: str
        """
        
        

        self._tps = None
        self._storage = None
        self._partition_num = None
        self._product_id = None
        self._spec_code = None
        self._io = None
        self._bandwidth = None
        self._recommend_max_cons_groups = None
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
        if recommend_max_cons_groups is not None:
            self.recommend_max_cons_groups = recommend_max_cons_groups
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
        """Gets the tps of this ShowInstanceExtendProductInfoRespDetail.

        单位时间内的消息量最大值。

        :return: The tps of this ShowInstanceExtendProductInfoRespDetail.
        :rtype: str
        """
        return self._tps

    @tps.setter
    def tps(self, tps):
        """Sets the tps of this ShowInstanceExtendProductInfoRespDetail.

        单位时间内的消息量最大值。

        :param tps: The tps of this ShowInstanceExtendProductInfoRespDetail.
        :type tps: str
        """
        self._tps = tps

    @property
    def storage(self):
        """Gets the storage of this ShowInstanceExtendProductInfoRespDetail.

        消息存储空间。

        :return: The storage of this ShowInstanceExtendProductInfoRespDetail.
        :rtype: str
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this ShowInstanceExtendProductInfoRespDetail.

        消息存储空间。

        :param storage: The storage of this ShowInstanceExtendProductInfoRespDetail.
        :type storage: str
        """
        self._storage = storage

    @property
    def partition_num(self):
        """Gets the partition_num of this ShowInstanceExtendProductInfoRespDetail.

        Kafka实例的分区数量。

        :return: The partition_num of this ShowInstanceExtendProductInfoRespDetail.
        :rtype: str
        """
        return self._partition_num

    @partition_num.setter
    def partition_num(self, partition_num):
        """Sets the partition_num of this ShowInstanceExtendProductInfoRespDetail.

        Kafka实例的分区数量。

        :param partition_num: The partition_num of this ShowInstanceExtendProductInfoRespDetail.
        :type partition_num: str
        """
        self._partition_num = partition_num

    @property
    def product_id(self):
        """Gets the product_id of this ShowInstanceExtendProductInfoRespDetail.

        产品ID。

        :return: The product_id of this ShowInstanceExtendProductInfoRespDetail.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ShowInstanceExtendProductInfoRespDetail.

        产品ID。

        :param product_id: The product_id of this ShowInstanceExtendProductInfoRespDetail.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def spec_code(self):
        """Gets the spec_code of this ShowInstanceExtendProductInfoRespDetail.

        规格ID。

        :return: The spec_code of this ShowInstanceExtendProductInfoRespDetail.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this ShowInstanceExtendProductInfoRespDetail.

        规格ID。

        :param spec_code: The spec_code of this ShowInstanceExtendProductInfoRespDetail.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def io(self):
        """Gets the io of this ShowInstanceExtendProductInfoRespDetail.

        IO信息。

        :return: The io of this ShowInstanceExtendProductInfoRespDetail.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ListProductsRespIo`]
        """
        return self._io

    @io.setter
    def io(self, io):
        """Sets the io of this ShowInstanceExtendProductInfoRespDetail.

        IO信息。

        :param io: The io of this ShowInstanceExtendProductInfoRespDetail.
        :type io: list[:class:`huaweicloudsdkkafka.v2.ListProductsRespIo`]
        """
        self._io = io

    @property
    def bandwidth(self):
        """Gets the bandwidth of this ShowInstanceExtendProductInfoRespDetail.

        Kafka实例的基准带宽。

        :return: The bandwidth of this ShowInstanceExtendProductInfoRespDetail.
        :rtype: str
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this ShowInstanceExtendProductInfoRespDetail.

        Kafka实例的基准带宽。

        :param bandwidth: The bandwidth of this ShowInstanceExtendProductInfoRespDetail.
        :type bandwidth: str
        """
        self._bandwidth = bandwidth

    @property
    def recommend_max_cons_groups(self):
        """Gets the recommend_max_cons_groups of this ShowInstanceExtendProductInfoRespDetail.

        Kafka实例最大消费组数参考值。

        :return: The recommend_max_cons_groups of this ShowInstanceExtendProductInfoRespDetail.
        :rtype: str
        """
        return self._recommend_max_cons_groups

    @recommend_max_cons_groups.setter
    def recommend_max_cons_groups(self, recommend_max_cons_groups):
        """Sets the recommend_max_cons_groups of this ShowInstanceExtendProductInfoRespDetail.

        Kafka实例最大消费组数参考值。

        :param recommend_max_cons_groups: The recommend_max_cons_groups of this ShowInstanceExtendProductInfoRespDetail.
        :type recommend_max_cons_groups: str
        """
        self._recommend_max_cons_groups = recommend_max_cons_groups

    @property
    def unavailable_zones(self):
        """Gets the unavailable_zones of this ShowInstanceExtendProductInfoRespDetail.

        资源售罄的可用区列表。

        :return: The unavailable_zones of this ShowInstanceExtendProductInfoRespDetail.
        :rtype: list[str]
        """
        return self._unavailable_zones

    @unavailable_zones.setter
    def unavailable_zones(self, unavailable_zones):
        """Sets the unavailable_zones of this ShowInstanceExtendProductInfoRespDetail.

        资源售罄的可用区列表。

        :param unavailable_zones: The unavailable_zones of this ShowInstanceExtendProductInfoRespDetail.
        :type unavailable_zones: list[str]
        """
        self._unavailable_zones = unavailable_zones

    @property
    def available_zones(self):
        """Gets the available_zones of this ShowInstanceExtendProductInfoRespDetail.

        有可用资源的可用区列表。

        :return: The available_zones of this ShowInstanceExtendProductInfoRespDetail.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this ShowInstanceExtendProductInfoRespDetail.

        有可用资源的可用区列表。

        :param available_zones: The available_zones of this ShowInstanceExtendProductInfoRespDetail.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def ecs_flavor_id(self):
        """Gets the ecs_flavor_id of this ShowInstanceExtendProductInfoRespDetail.

        该产品规格对应的虚拟机规格。

        :return: The ecs_flavor_id of this ShowInstanceExtendProductInfoRespDetail.
        :rtype: str
        """
        return self._ecs_flavor_id

    @ecs_flavor_id.setter
    def ecs_flavor_id(self, ecs_flavor_id):
        """Sets the ecs_flavor_id of this ShowInstanceExtendProductInfoRespDetail.

        该产品规格对应的虚拟机规格。

        :param ecs_flavor_id: The ecs_flavor_id of this ShowInstanceExtendProductInfoRespDetail.
        :type ecs_flavor_id: str
        """
        self._ecs_flavor_id = ecs_flavor_id

    @property
    def arch_type(self):
        """Gets the arch_type of this ShowInstanceExtendProductInfoRespDetail.

        实例规格架构类型。当前仅支持X86。

        :return: The arch_type of this ShowInstanceExtendProductInfoRespDetail.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """Sets the arch_type of this ShowInstanceExtendProductInfoRespDetail.

        实例规格架构类型。当前仅支持X86。

        :param arch_type: The arch_type of this ShowInstanceExtendProductInfoRespDetail.
        :type arch_type: str
        """
        self._arch_type = arch_type

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
        if not isinstance(other, ShowInstanceExtendProductInfoRespDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
