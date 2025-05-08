# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductEntity:

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
        'billing_code': 'str',
        'arch_types': 'list[str]',
        'charging_mode': 'object',
        'ios': 'object',
        'support_features': 'object',
        'properties': 'object',
        'available_zones': 'list[str]',
        'unavailable_zones': 'list[str]',
        'qingtian_incompatible': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'product_id': 'product_id',
        'ecs_flavor_id': 'ecs_flavor_id',
        'billing_code': 'billing_code',
        'arch_types': 'arch_types',
        'charging_mode': 'charging_mode',
        'ios': 'ios',
        'support_features': 'support_features',
        'properties': 'properties',
        'available_zones': 'available_zones',
        'unavailable_zones': 'unavailable_zones',
        'qingtian_incompatible': 'qingtian_incompatible'
    }

    def __init__(self, type=None, product_id=None, ecs_flavor_id=None, billing_code=None, arch_types=None, charging_mode=None, ios=None, support_features=None, properties=None, available_zones=None, unavailable_zones=None, qingtian_incompatible=None):
        r"""ProductEntity

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 产品类型。 **取值范围**： - single：单机。 - cluster：集群。
        :type type: str
        :param product_id: **参数解释**： 产品ID。 **取值范围**： 不涉及。
        :type product_id: str
        :param ecs_flavor_id: **参数解释**： ECS的Flavor ID。 **取值范围**： 不涉及。
        :type ecs_flavor_id: str
        :param billing_code: **参数解释**： CBC的规格码。 **取值范围**： 不涉及。
        :type billing_code: str
        :param arch_types: **参数解释**： 架构类型。
        :type arch_types: list[str]
        :param charging_mode: **参数解释**： 计费模式。 **取值范围**： 不涉及。
        :type charging_mode: object
        :param ios: **参数解释**： 支持的io类型。 **取值范围**： 不涉及。
        :type ios: object
        :param support_features: **参数解释**： 支持的特性。 **取值范围**： 不涉及。
        :type support_features: object
        :param properties: **参数解释**： 产品特性。 **取值范围**： 不涉及。
        :type properties: object
        :param available_zones: **参数解释**： 可用分区。
        :type available_zones: list[str]
        :param unavailable_zones: **参数解释**： 不可用分区。
        :type unavailable_zones: list[str]
        :param qingtian_incompatible: **参数解释**： 是否为擎天实例。 **取值范围**： - true：是 - false：否
        :type qingtian_incompatible: bool
        """
        
        

        self._type = None
        self._product_id = None
        self._ecs_flavor_id = None
        self._billing_code = None
        self._arch_types = None
        self._charging_mode = None
        self._ios = None
        self._support_features = None
        self._properties = None
        self._available_zones = None
        self._unavailable_zones = None
        self._qingtian_incompatible = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if product_id is not None:
            self.product_id = product_id
        if ecs_flavor_id is not None:
            self.ecs_flavor_id = ecs_flavor_id
        if billing_code is not None:
            self.billing_code = billing_code
        if arch_types is not None:
            self.arch_types = arch_types
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if ios is not None:
            self.ios = ios
        if support_features is not None:
            self.support_features = support_features
        if properties is not None:
            self.properties = properties
        if available_zones is not None:
            self.available_zones = available_zones
        if unavailable_zones is not None:
            self.unavailable_zones = unavailable_zones
        if qingtian_incompatible is not None:
            self.qingtian_incompatible = qingtian_incompatible

    @property
    def type(self):
        r"""Gets the type of this ProductEntity.

        **参数解释**： 产品类型。 **取值范围**： - single：单机。 - cluster：集群。

        :return: The type of this ProductEntity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ProductEntity.

        **参数解释**： 产品类型。 **取值范围**： - single：单机。 - cluster：集群。

        :param type: The type of this ProductEntity.
        :type type: str
        """
        self._type = type

    @property
    def product_id(self):
        r"""Gets the product_id of this ProductEntity.

        **参数解释**： 产品ID。 **取值范围**： 不涉及。

        :return: The product_id of this ProductEntity.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ProductEntity.

        **参数解释**： 产品ID。 **取值范围**： 不涉及。

        :param product_id: The product_id of this ProductEntity.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def ecs_flavor_id(self):
        r"""Gets the ecs_flavor_id of this ProductEntity.

        **参数解释**： ECS的Flavor ID。 **取值范围**： 不涉及。

        :return: The ecs_flavor_id of this ProductEntity.
        :rtype: str
        """
        return self._ecs_flavor_id

    @ecs_flavor_id.setter
    def ecs_flavor_id(self, ecs_flavor_id):
        r"""Sets the ecs_flavor_id of this ProductEntity.

        **参数解释**： ECS的Flavor ID。 **取值范围**： 不涉及。

        :param ecs_flavor_id: The ecs_flavor_id of this ProductEntity.
        :type ecs_flavor_id: str
        """
        self._ecs_flavor_id = ecs_flavor_id

    @property
    def billing_code(self):
        r"""Gets the billing_code of this ProductEntity.

        **参数解释**： CBC的规格码。 **取值范围**： 不涉及。

        :return: The billing_code of this ProductEntity.
        :rtype: str
        """
        return self._billing_code

    @billing_code.setter
    def billing_code(self, billing_code):
        r"""Sets the billing_code of this ProductEntity.

        **参数解释**： CBC的规格码。 **取值范围**： 不涉及。

        :param billing_code: The billing_code of this ProductEntity.
        :type billing_code: str
        """
        self._billing_code = billing_code

    @property
    def arch_types(self):
        r"""Gets the arch_types of this ProductEntity.

        **参数解释**： 架构类型。

        :return: The arch_types of this ProductEntity.
        :rtype: list[str]
        """
        return self._arch_types

    @arch_types.setter
    def arch_types(self, arch_types):
        r"""Sets the arch_types of this ProductEntity.

        **参数解释**： 架构类型。

        :param arch_types: The arch_types of this ProductEntity.
        :type arch_types: list[str]
        """
        self._arch_types = arch_types

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ProductEntity.

        **参数解释**： 计费模式。 **取值范围**： 不涉及。

        :return: The charging_mode of this ProductEntity.
        :rtype: object
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ProductEntity.

        **参数解释**： 计费模式。 **取值范围**： 不涉及。

        :param charging_mode: The charging_mode of this ProductEntity.
        :type charging_mode: object
        """
        self._charging_mode = charging_mode

    @property
    def ios(self):
        r"""Gets the ios of this ProductEntity.

        **参数解释**： 支持的io类型。 **取值范围**： 不涉及。

        :return: The ios of this ProductEntity.
        :rtype: object
        """
        return self._ios

    @ios.setter
    def ios(self, ios):
        r"""Sets the ios of this ProductEntity.

        **参数解释**： 支持的io类型。 **取值范围**： 不涉及。

        :param ios: The ios of this ProductEntity.
        :type ios: object
        """
        self._ios = ios

    @property
    def support_features(self):
        r"""Gets the support_features of this ProductEntity.

        **参数解释**： 支持的特性。 **取值范围**： 不涉及。

        :return: The support_features of this ProductEntity.
        :rtype: object
        """
        return self._support_features

    @support_features.setter
    def support_features(self, support_features):
        r"""Sets the support_features of this ProductEntity.

        **参数解释**： 支持的特性。 **取值范围**： 不涉及。

        :param support_features: The support_features of this ProductEntity.
        :type support_features: object
        """
        self._support_features = support_features

    @property
    def properties(self):
        r"""Gets the properties of this ProductEntity.

        **参数解释**： 产品特性。 **取值范围**： 不涉及。

        :return: The properties of this ProductEntity.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ProductEntity.

        **参数解释**： 产品特性。 **取值范围**： 不涉及。

        :param properties: The properties of this ProductEntity.
        :type properties: object
        """
        self._properties = properties

    @property
    def available_zones(self):
        r"""Gets the available_zones of this ProductEntity.

        **参数解释**： 可用分区。

        :return: The available_zones of this ProductEntity.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this ProductEntity.

        **参数解释**： 可用分区。

        :param available_zones: The available_zones of this ProductEntity.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def unavailable_zones(self):
        r"""Gets the unavailable_zones of this ProductEntity.

        **参数解释**： 不可用分区。

        :return: The unavailable_zones of this ProductEntity.
        :rtype: list[str]
        """
        return self._unavailable_zones

    @unavailable_zones.setter
    def unavailable_zones(self, unavailable_zones):
        r"""Sets the unavailable_zones of this ProductEntity.

        **参数解释**： 不可用分区。

        :param unavailable_zones: The unavailable_zones of this ProductEntity.
        :type unavailable_zones: list[str]
        """
        self._unavailable_zones = unavailable_zones

    @property
    def qingtian_incompatible(self):
        r"""Gets the qingtian_incompatible of this ProductEntity.

        **参数解释**： 是否为擎天实例。 **取值范围**： - true：是 - false：否

        :return: The qingtian_incompatible of this ProductEntity.
        :rtype: bool
        """
        return self._qingtian_incompatible

    @qingtian_incompatible.setter
    def qingtian_incompatible(self, qingtian_incompatible):
        r"""Sets the qingtian_incompatible of this ProductEntity.

        **参数解释**： 是否为擎天实例。 **取值范围**： - true：是 - false：否

        :param qingtian_incompatible: The qingtian_incompatible of this ProductEntity.
        :type qingtian_incompatible: bool
        """
        self._qingtian_incompatible = qingtian_incompatible

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
        if not isinstance(other, ProductEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
