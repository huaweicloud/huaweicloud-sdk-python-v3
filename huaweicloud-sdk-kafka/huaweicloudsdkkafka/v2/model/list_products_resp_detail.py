# coding: utf-8

import pprint
import re

import six





class ListProductsRespDetail:


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
        """ListProductsRespDetail - a model defined in huaweicloud sdk"""
        
        

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
        """Gets the tps of this ListProductsRespDetail.

        单位时间内的消息量最大值。

        :return: The tps of this ListProductsRespDetail.
        :rtype: str
        """
        return self._tps

    @tps.setter
    def tps(self, tps):
        """Sets the tps of this ListProductsRespDetail.

        单位时间内的消息量最大值。

        :param tps: The tps of this ListProductsRespDetail.
        :type: str
        """
        self._tps = tps

    @property
    def storage(self):
        """Gets the storage of this ListProductsRespDetail.

        消息存储空间。

        :return: The storage of this ListProductsRespDetail.
        :rtype: str
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this ListProductsRespDetail.

        消息存储空间。

        :param storage: The storage of this ListProductsRespDetail.
        :type: str
        """
        self._storage = storage

    @property
    def partition_num(self):
        """Gets the partition_num of this ListProductsRespDetail.

        Kafka实例的最大Topic数。

        :return: The partition_num of this ListProductsRespDetail.
        :rtype: str
        """
        return self._partition_num

    @partition_num.setter
    def partition_num(self, partition_num):
        """Sets the partition_num of this ListProductsRespDetail.

        Kafka实例的最大Topic数。

        :param partition_num: The partition_num of this ListProductsRespDetail.
        :type: str
        """
        self._partition_num = partition_num

    @property
    def product_id(self):
        """Gets the product_id of this ListProductsRespDetail.

        产品ID。

        :return: The product_id of this ListProductsRespDetail.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ListProductsRespDetail.

        产品ID。

        :param product_id: The product_id of this ListProductsRespDetail.
        :type: str
        """
        self._product_id = product_id

    @property
    def spec_code(self):
        """Gets the spec_code of this ListProductsRespDetail.

        规格ID。

        :return: The spec_code of this ListProductsRespDetail.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this ListProductsRespDetail.

        规格ID。

        :param spec_code: The spec_code of this ListProductsRespDetail.
        :type: str
        """
        self._spec_code = spec_code

    @property
    def io(self):
        """Gets the io of this ListProductsRespDetail.

        IO信息。

        :return: The io of this ListProductsRespDetail.
        :rtype: list[ListProductsRespIo]
        """
        return self._io

    @io.setter
    def io(self, io):
        """Sets the io of this ListProductsRespDetail.

        IO信息。

        :param io: The io of this ListProductsRespDetail.
        :type: list[ListProductsRespIo]
        """
        self._io = io

    @property
    def bandwidth(self):
        """Gets the bandwidth of this ListProductsRespDetail.

        Kafka实例的基准带宽。

        :return: The bandwidth of this ListProductsRespDetail.
        :rtype: str
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this ListProductsRespDetail.

        Kafka实例的基准带宽。

        :param bandwidth: The bandwidth of this ListProductsRespDetail.
        :type: str
        """
        self._bandwidth = bandwidth

    @property
    def unavailable_zones(self):
        """Gets the unavailable_zones of this ListProductsRespDetail.

        资源售罄的可用区列表。

        :return: The unavailable_zones of this ListProductsRespDetail.
        :rtype: list[str]
        """
        return self._unavailable_zones

    @unavailable_zones.setter
    def unavailable_zones(self, unavailable_zones):
        """Sets the unavailable_zones of this ListProductsRespDetail.

        资源售罄的可用区列表。

        :param unavailable_zones: The unavailable_zones of this ListProductsRespDetail.
        :type: list[str]
        """
        self._unavailable_zones = unavailable_zones

    @property
    def available_zones(self):
        """Gets the available_zones of this ListProductsRespDetail.

        有可用资源的可用区列表。

        :return: The available_zones of this ListProductsRespDetail.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this ListProductsRespDetail.

        有可用资源的可用区列表。

        :param available_zones: The available_zones of this ListProductsRespDetail.
        :type: list[str]
        """
        self._available_zones = available_zones

    @property
    def ecs_flavor_id(self):
        """Gets the ecs_flavor_id of this ListProductsRespDetail.

        该产品规格对应的虚拟机规格。

        :return: The ecs_flavor_id of this ListProductsRespDetail.
        :rtype: str
        """
        return self._ecs_flavor_id

    @ecs_flavor_id.setter
    def ecs_flavor_id(self, ecs_flavor_id):
        """Sets the ecs_flavor_id of this ListProductsRespDetail.

        该产品规格对应的虚拟机规格。

        :param ecs_flavor_id: The ecs_flavor_id of this ListProductsRespDetail.
        :type: str
        """
        self._ecs_flavor_id = ecs_flavor_id

    @property
    def arch_type(self):
        """Gets the arch_type of this ListProductsRespDetail.

        实例规格架构类型。当前仅支持X86。

        :return: The arch_type of this ListProductsRespDetail.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """Sets the arch_type of this ListProductsRespDetail.

        实例规格架构类型。当前仅支持X86。

        :param arch_type: The arch_type of this ListProductsRespDetail.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListProductsRespDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
