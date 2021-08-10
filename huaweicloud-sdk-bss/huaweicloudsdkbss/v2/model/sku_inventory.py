# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SkuInventory:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'sku_code': 'str',
        'saleable_quantity': 'int'
    }

    attribute_map = {
        'product_id': 'product_id',
        'sku_code': 'sku_code',
        'saleable_quantity': 'saleable_quantity'
    }

    def __init__(self, product_id=None, sku_code=None, saleable_quantity=None):
        """SkuInventory - a model defined in huaweicloud sdk"""
        
        

        self._product_id = None
        self._sku_code = None
        self._saleable_quantity = None
        self.discriminator = None

        self.product_id = product_id
        self.sku_code = sku_code
        self.saleable_quantity = saleable_quantity

    @property
    def product_id(self):
        """Gets the product_id of this SkuInventory.

        产品的ID。

        :return: The product_id of this SkuInventory.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this SkuInventory.

        产品的ID。

        :param product_id: The product_id of this SkuInventory.
        :type: str
        """
        self._product_id = product_id

    @property
    def sku_code(self):
        """Gets the sku_code of this SkuInventory.

        SKU编码，唯一标识一个产品的规格。

        :return: The sku_code of this SkuInventory.
        :rtype: str
        """
        return self._sku_code

    @sku_code.setter
    def sku_code(self, sku_code):
        """Sets the sku_code of this SkuInventory.

        SKU编码，唯一标识一个产品的规格。

        :param sku_code: The sku_code of this SkuInventory.
        :type: str
        """
        self._sku_code = sku_code

    @property
    def saleable_quantity(self):
        """Gets the saleable_quantity of this SkuInventory.

        产品的可售库存数量。

        :return: The saleable_quantity of this SkuInventory.
        :rtype: int
        """
        return self._saleable_quantity

    @saleable_quantity.setter
    def saleable_quantity(self, saleable_quantity):
        """Sets the saleable_quantity of this SkuInventory.

        产品的可售库存数量。

        :param saleable_quantity: The saleable_quantity of this SkuInventory.
        :type: int
        """
        self._saleable_quantity = saleable_quantity

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
        if not isinstance(other, SkuInventory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
