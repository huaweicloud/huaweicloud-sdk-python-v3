# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'storage': 'str',
        'product_id': 'str',
        'spec_code': 'str',
        'io': 'list[ListProductsRespIo]',
        'unavailable_zones': 'list[str]',
        'available_zones': 'list[str]',
        'ecs_flavor_id': 'str',
        'arch_type': 'str'
    }

    attribute_map = {
        'storage': 'storage',
        'product_id': 'product_id',
        'spec_code': 'spec_code',
        'io': 'io',
        'unavailable_zones': 'unavailable_zones',
        'available_zones': 'available_zones',
        'ecs_flavor_id': 'ecs_flavor_id',
        'arch_type': 'arch_type'
    }

    def __init__(self, storage=None, product_id=None, spec_code=None, io=None, unavailable_zones=None, available_zones=None, ecs_flavor_id=None, arch_type=None):
        r"""ListProductsRespDetail

        The model defined in huaweicloud sdk

        :param storage: 消息存储空间。
        :type storage: str
        :param product_id: 产品ID。
        :type product_id: str
        :param spec_code: 规格ID。
        :type spec_code: str
        :param io: IO信息。
        :type io: list[:class:`huaweicloudsdkrabbitmq.v2.ListProductsRespIo`]
        :param unavailable_zones: 资源售罄的可用区列表。
        :type unavailable_zones: list[str]
        :param available_zones: 有可用资源的可用区列表。
        :type available_zones: list[str]
        :param ecs_flavor_id: 该产品规格对应的虚拟机规格。
        :type ecs_flavor_id: str
        :param arch_type: 实例规格架构类型。当前仅支持X86。
        :type arch_type: str
        """
        
        

        self._storage = None
        self._product_id = None
        self._spec_code = None
        self._io = None
        self._unavailable_zones = None
        self._available_zones = None
        self._ecs_flavor_id = None
        self._arch_type = None
        self.discriminator = None

        if storage is not None:
            self.storage = storage
        if product_id is not None:
            self.product_id = product_id
        if spec_code is not None:
            self.spec_code = spec_code
        if io is not None:
            self.io = io
        if unavailable_zones is not None:
            self.unavailable_zones = unavailable_zones
        if available_zones is not None:
            self.available_zones = available_zones
        if ecs_flavor_id is not None:
            self.ecs_flavor_id = ecs_flavor_id
        if arch_type is not None:
            self.arch_type = arch_type

    @property
    def storage(self):
        r"""Gets the storage of this ListProductsRespDetail.

        消息存储空间。

        :return: The storage of this ListProductsRespDetail.
        :rtype: str
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        r"""Sets the storage of this ListProductsRespDetail.

        消息存储空间。

        :param storage: The storage of this ListProductsRespDetail.
        :type storage: str
        """
        self._storage = storage

    @property
    def product_id(self):
        r"""Gets the product_id of this ListProductsRespDetail.

        产品ID。

        :return: The product_id of this ListProductsRespDetail.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ListProductsRespDetail.

        产品ID。

        :param product_id: The product_id of this ListProductsRespDetail.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ListProductsRespDetail.

        规格ID。

        :return: The spec_code of this ListProductsRespDetail.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ListProductsRespDetail.

        规格ID。

        :param spec_code: The spec_code of this ListProductsRespDetail.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def io(self):
        r"""Gets the io of this ListProductsRespDetail.

        IO信息。

        :return: The io of this ListProductsRespDetail.
        :rtype: list[:class:`huaweicloudsdkrabbitmq.v2.ListProductsRespIo`]
        """
        return self._io

    @io.setter
    def io(self, io):
        r"""Sets the io of this ListProductsRespDetail.

        IO信息。

        :param io: The io of this ListProductsRespDetail.
        :type io: list[:class:`huaweicloudsdkrabbitmq.v2.ListProductsRespIo`]
        """
        self._io = io

    @property
    def unavailable_zones(self):
        r"""Gets the unavailable_zones of this ListProductsRespDetail.

        资源售罄的可用区列表。

        :return: The unavailable_zones of this ListProductsRespDetail.
        :rtype: list[str]
        """
        return self._unavailable_zones

    @unavailable_zones.setter
    def unavailable_zones(self, unavailable_zones):
        r"""Sets the unavailable_zones of this ListProductsRespDetail.

        资源售罄的可用区列表。

        :param unavailable_zones: The unavailable_zones of this ListProductsRespDetail.
        :type unavailable_zones: list[str]
        """
        self._unavailable_zones = unavailable_zones

    @property
    def available_zones(self):
        r"""Gets the available_zones of this ListProductsRespDetail.

        有可用资源的可用区列表。

        :return: The available_zones of this ListProductsRespDetail.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this ListProductsRespDetail.

        有可用资源的可用区列表。

        :param available_zones: The available_zones of this ListProductsRespDetail.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def ecs_flavor_id(self):
        r"""Gets the ecs_flavor_id of this ListProductsRespDetail.

        该产品规格对应的虚拟机规格。

        :return: The ecs_flavor_id of this ListProductsRespDetail.
        :rtype: str
        """
        return self._ecs_flavor_id

    @ecs_flavor_id.setter
    def ecs_flavor_id(self, ecs_flavor_id):
        r"""Sets the ecs_flavor_id of this ListProductsRespDetail.

        该产品规格对应的虚拟机规格。

        :param ecs_flavor_id: The ecs_flavor_id of this ListProductsRespDetail.
        :type ecs_flavor_id: str
        """
        self._ecs_flavor_id = ecs_flavor_id

    @property
    def arch_type(self):
        r"""Gets the arch_type of this ListProductsRespDetail.

        实例规格架构类型。当前仅支持X86。

        :return: The arch_type of this ListProductsRespDetail.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        r"""Sets the arch_type of this ListProductsRespDetail.

        实例规格架构类型。当前仅支持X86。

        :param arch_type: The arch_type of this ListProductsRespDetail.
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
        if not isinstance(other, ListProductsRespDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
