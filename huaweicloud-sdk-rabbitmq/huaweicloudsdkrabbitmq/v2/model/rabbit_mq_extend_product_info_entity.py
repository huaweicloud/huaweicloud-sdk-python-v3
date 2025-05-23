# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RabbitMQExtendProductInfoEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'product_id': 'str',
        'ecs_flavor_id': 'str',
        'arch_types': 'list[str]',
        'charging_mode': 'list[str]',
        'ios': 'list[RabbitMQExtendProductIosEntity]',
        'properties': 'RabbitMQExtendProductPropertiesEntity',
        'available_zones': 'list[str]',
        'unavailable_zones': 'list[str]',
        'support_features': 'list[RabbitMQProductSupportFeaturesEntity]'
    }

    attribute_map = {
        'type': 'type',
        'product_id': 'product_id',
        'ecs_flavor_id': 'ecs_flavor_id',
        'arch_types': 'arch_types',
        'charging_mode': 'charging_mode',
        'ios': 'ios',
        'properties': 'properties',
        'available_zones': 'available_zones',
        'unavailable_zones': 'unavailable_zones',
        'support_features': 'support_features'
    }

    def __init__(self, type=None, product_id=None, ecs_flavor_id=None, arch_types=None, charging_mode=None, ios=None, properties=None, available_zones=None, unavailable_zones=None, support_features=None):
        r"""RabbitMQExtendProductInfoEntity

        The model defined in huaweicloud sdk

        :param type: 实例类型
        :type type: str
        :param product_id: 产品ID。
        :type product_id: str
        :param ecs_flavor_id: 该产品使用的ECS规格。
        :type ecs_flavor_id: str
        :param arch_types: 支持的CPU架构类型
        :type arch_types: list[str]
        :param charging_mode: 支持的计费模式类型。
        :type charging_mode: list[str]
        :param ios: 磁盘IO信息。
        :type ios: list[:class:`huaweicloudsdkrabbitmq.v2.RabbitMQExtendProductIosEntity`]
        :param properties: 
        :type properties: :class:`huaweicloudsdkrabbitmq.v2.RabbitMQExtendProductPropertiesEntity`
        :param available_zones: 有可用资源的可用区列表。
        :type available_zones: list[str]
        :param unavailable_zones: 资源售罄的可用区列表
        :type unavailable_zones: list[str]
        :param support_features: 支持的特性功能。
        :type support_features: list[:class:`huaweicloudsdkrabbitmq.v2.RabbitMQProductSupportFeaturesEntity`]
        """
        
        

        self._type = None
        self._product_id = None
        self._ecs_flavor_id = None
        self._arch_types = None
        self._charging_mode = None
        self._ios = None
        self._properties = None
        self._available_zones = None
        self._unavailable_zones = None
        self._support_features = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if product_id is not None:
            self.product_id = product_id
        if ecs_flavor_id is not None:
            self.ecs_flavor_id = ecs_flavor_id
        if arch_types is not None:
            self.arch_types = arch_types
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if ios is not None:
            self.ios = ios
        if properties is not None:
            self.properties = properties
        if available_zones is not None:
            self.available_zones = available_zones
        if unavailable_zones is not None:
            self.unavailable_zones = unavailable_zones
        if support_features is not None:
            self.support_features = support_features

    @property
    def type(self):
        r"""Gets the type of this RabbitMQExtendProductInfoEntity.

        实例类型

        :return: The type of this RabbitMQExtendProductInfoEntity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RabbitMQExtendProductInfoEntity.

        实例类型

        :param type: The type of this RabbitMQExtendProductInfoEntity.
        :type type: str
        """
        self._type = type

    @property
    def product_id(self):
        r"""Gets the product_id of this RabbitMQExtendProductInfoEntity.

        产品ID。

        :return: The product_id of this RabbitMQExtendProductInfoEntity.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this RabbitMQExtendProductInfoEntity.

        产品ID。

        :param product_id: The product_id of this RabbitMQExtendProductInfoEntity.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def ecs_flavor_id(self):
        r"""Gets the ecs_flavor_id of this RabbitMQExtendProductInfoEntity.

        该产品使用的ECS规格。

        :return: The ecs_flavor_id of this RabbitMQExtendProductInfoEntity.
        :rtype: str
        """
        return self._ecs_flavor_id

    @ecs_flavor_id.setter
    def ecs_flavor_id(self, ecs_flavor_id):
        r"""Sets the ecs_flavor_id of this RabbitMQExtendProductInfoEntity.

        该产品使用的ECS规格。

        :param ecs_flavor_id: The ecs_flavor_id of this RabbitMQExtendProductInfoEntity.
        :type ecs_flavor_id: str
        """
        self._ecs_flavor_id = ecs_flavor_id

    @property
    def arch_types(self):
        r"""Gets the arch_types of this RabbitMQExtendProductInfoEntity.

        支持的CPU架构类型

        :return: The arch_types of this RabbitMQExtendProductInfoEntity.
        :rtype: list[str]
        """
        return self._arch_types

    @arch_types.setter
    def arch_types(self, arch_types):
        r"""Sets the arch_types of this RabbitMQExtendProductInfoEntity.

        支持的CPU架构类型

        :param arch_types: The arch_types of this RabbitMQExtendProductInfoEntity.
        :type arch_types: list[str]
        """
        self._arch_types = arch_types

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this RabbitMQExtendProductInfoEntity.

        支持的计费模式类型。

        :return: The charging_mode of this RabbitMQExtendProductInfoEntity.
        :rtype: list[str]
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this RabbitMQExtendProductInfoEntity.

        支持的计费模式类型。

        :param charging_mode: The charging_mode of this RabbitMQExtendProductInfoEntity.
        :type charging_mode: list[str]
        """
        self._charging_mode = charging_mode

    @property
    def ios(self):
        r"""Gets the ios of this RabbitMQExtendProductInfoEntity.

        磁盘IO信息。

        :return: The ios of this RabbitMQExtendProductInfoEntity.
        :rtype: list[:class:`huaweicloudsdkrabbitmq.v2.RabbitMQExtendProductIosEntity`]
        """
        return self._ios

    @ios.setter
    def ios(self, ios):
        r"""Sets the ios of this RabbitMQExtendProductInfoEntity.

        磁盘IO信息。

        :param ios: The ios of this RabbitMQExtendProductInfoEntity.
        :type ios: list[:class:`huaweicloudsdkrabbitmq.v2.RabbitMQExtendProductIosEntity`]
        """
        self._ios = ios

    @property
    def properties(self):
        r"""Gets the properties of this RabbitMQExtendProductInfoEntity.

        :return: The properties of this RabbitMQExtendProductInfoEntity.
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.RabbitMQExtendProductPropertiesEntity`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this RabbitMQExtendProductInfoEntity.

        :param properties: The properties of this RabbitMQExtendProductInfoEntity.
        :type properties: :class:`huaweicloudsdkrabbitmq.v2.RabbitMQExtendProductPropertiesEntity`
        """
        self._properties = properties

    @property
    def available_zones(self):
        r"""Gets the available_zones of this RabbitMQExtendProductInfoEntity.

        有可用资源的可用区列表。

        :return: The available_zones of this RabbitMQExtendProductInfoEntity.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this RabbitMQExtendProductInfoEntity.

        有可用资源的可用区列表。

        :param available_zones: The available_zones of this RabbitMQExtendProductInfoEntity.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def unavailable_zones(self):
        r"""Gets the unavailable_zones of this RabbitMQExtendProductInfoEntity.

        资源售罄的可用区列表

        :return: The unavailable_zones of this RabbitMQExtendProductInfoEntity.
        :rtype: list[str]
        """
        return self._unavailable_zones

    @unavailable_zones.setter
    def unavailable_zones(self, unavailable_zones):
        r"""Sets the unavailable_zones of this RabbitMQExtendProductInfoEntity.

        资源售罄的可用区列表

        :param unavailable_zones: The unavailable_zones of this RabbitMQExtendProductInfoEntity.
        :type unavailable_zones: list[str]
        """
        self._unavailable_zones = unavailable_zones

    @property
    def support_features(self):
        r"""Gets the support_features of this RabbitMQExtendProductInfoEntity.

        支持的特性功能。

        :return: The support_features of this RabbitMQExtendProductInfoEntity.
        :rtype: list[:class:`huaweicloudsdkrabbitmq.v2.RabbitMQProductSupportFeaturesEntity`]
        """
        return self._support_features

    @support_features.setter
    def support_features(self, support_features):
        r"""Sets the support_features of this RabbitMQExtendProductInfoEntity.

        支持的特性功能。

        :param support_features: The support_features of this RabbitMQExtendProductInfoEntity.
        :type support_features: list[:class:`huaweicloudsdkrabbitmq.v2.RabbitMQProductSupportFeaturesEntity`]
        """
        self._support_features = support_features

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
        if not isinstance(other, RabbitMQExtendProductInfoEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
