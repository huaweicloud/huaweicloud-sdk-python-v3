# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEngineProductsEntity:

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
        'charging_mode': 'list[str]',
        'ios': 'list[ListEngineIosEntity]',
        'support_features': 'list[object]',
        'properties': 'ListEnginePropertiesEntity'
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
        'properties': 'properties'
    }

    def __init__(self, type=None, product_id=None, ecs_flavor_id=None, billing_code=None, arch_types=None, charging_mode=None, ios=None, support_features=None, properties=None):
        r"""ListEngineProductsEntity

        The model defined in huaweicloud sdk

        :param type: 产品类型。当前产品类型有单机和集群。
        :type type: str
        :param product_id: 产品ID。
        :type product_id: str
        :param ecs_flavor_id: 底层资源类型。
        :type ecs_flavor_id: str
        :param billing_code: 账单计费类型。
        :type billing_code: str
        :param arch_types: CPU架构。
        :type arch_types: list[str]
        :param charging_mode: 计费模式。   - monthly：包年/包月类型。   - hourly：按需类型。
        :type charging_mode: list[str]
        :param ios: 支持的磁盘IO类型列表。
        :type ios: list[:class:`huaweicloudsdkrabbitmq.v2.ListEngineIosEntity`]
        :param support_features: 当前规格实例支持的功能特性列表。
        :type support_features: list[object]
        :param properties: 
        :type properties: :class:`huaweicloudsdkrabbitmq.v2.ListEnginePropertiesEntity`
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

    @property
    def type(self):
        r"""Gets the type of this ListEngineProductsEntity.

        产品类型。当前产品类型有单机和集群。

        :return: The type of this ListEngineProductsEntity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListEngineProductsEntity.

        产品类型。当前产品类型有单机和集群。

        :param type: The type of this ListEngineProductsEntity.
        :type type: str
        """
        self._type = type

    @property
    def product_id(self):
        r"""Gets the product_id of this ListEngineProductsEntity.

        产品ID。

        :return: The product_id of this ListEngineProductsEntity.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ListEngineProductsEntity.

        产品ID。

        :param product_id: The product_id of this ListEngineProductsEntity.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def ecs_flavor_id(self):
        r"""Gets the ecs_flavor_id of this ListEngineProductsEntity.

        底层资源类型。

        :return: The ecs_flavor_id of this ListEngineProductsEntity.
        :rtype: str
        """
        return self._ecs_flavor_id

    @ecs_flavor_id.setter
    def ecs_flavor_id(self, ecs_flavor_id):
        r"""Sets the ecs_flavor_id of this ListEngineProductsEntity.

        底层资源类型。

        :param ecs_flavor_id: The ecs_flavor_id of this ListEngineProductsEntity.
        :type ecs_flavor_id: str
        """
        self._ecs_flavor_id = ecs_flavor_id

    @property
    def billing_code(self):
        r"""Gets the billing_code of this ListEngineProductsEntity.

        账单计费类型。

        :return: The billing_code of this ListEngineProductsEntity.
        :rtype: str
        """
        return self._billing_code

    @billing_code.setter
    def billing_code(self, billing_code):
        r"""Sets the billing_code of this ListEngineProductsEntity.

        账单计费类型。

        :param billing_code: The billing_code of this ListEngineProductsEntity.
        :type billing_code: str
        """
        self._billing_code = billing_code

    @property
    def arch_types(self):
        r"""Gets the arch_types of this ListEngineProductsEntity.

        CPU架构。

        :return: The arch_types of this ListEngineProductsEntity.
        :rtype: list[str]
        """
        return self._arch_types

    @arch_types.setter
    def arch_types(self, arch_types):
        r"""Sets the arch_types of this ListEngineProductsEntity.

        CPU架构。

        :param arch_types: The arch_types of this ListEngineProductsEntity.
        :type arch_types: list[str]
        """
        self._arch_types = arch_types

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ListEngineProductsEntity.

        计费模式。   - monthly：包年/包月类型。   - hourly：按需类型。

        :return: The charging_mode of this ListEngineProductsEntity.
        :rtype: list[str]
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ListEngineProductsEntity.

        计费模式。   - monthly：包年/包月类型。   - hourly：按需类型。

        :param charging_mode: The charging_mode of this ListEngineProductsEntity.
        :type charging_mode: list[str]
        """
        self._charging_mode = charging_mode

    @property
    def ios(self):
        r"""Gets the ios of this ListEngineProductsEntity.

        支持的磁盘IO类型列表。

        :return: The ios of this ListEngineProductsEntity.
        :rtype: list[:class:`huaweicloudsdkrabbitmq.v2.ListEngineIosEntity`]
        """
        return self._ios

    @ios.setter
    def ios(self, ios):
        r"""Sets the ios of this ListEngineProductsEntity.

        支持的磁盘IO类型列表。

        :param ios: The ios of this ListEngineProductsEntity.
        :type ios: list[:class:`huaweicloudsdkrabbitmq.v2.ListEngineIosEntity`]
        """
        self._ios = ios

    @property
    def support_features(self):
        r"""Gets the support_features of this ListEngineProductsEntity.

        当前规格实例支持的功能特性列表。

        :return: The support_features of this ListEngineProductsEntity.
        :rtype: list[object]
        """
        return self._support_features

    @support_features.setter
    def support_features(self, support_features):
        r"""Sets the support_features of this ListEngineProductsEntity.

        当前规格实例支持的功能特性列表。

        :param support_features: The support_features of this ListEngineProductsEntity.
        :type support_features: list[object]
        """
        self._support_features = support_features

    @property
    def properties(self):
        r"""Gets the properties of this ListEngineProductsEntity.

        :return: The properties of this ListEngineProductsEntity.
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ListEnginePropertiesEntity`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ListEngineProductsEntity.

        :param properties: The properties of this ListEngineProductsEntity.
        :type properties: :class:`huaweicloudsdkrabbitmq.v2.ListEnginePropertiesEntity`
        """
        self._properties = properties

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
        if not isinstance(other, ListEngineProductsEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
