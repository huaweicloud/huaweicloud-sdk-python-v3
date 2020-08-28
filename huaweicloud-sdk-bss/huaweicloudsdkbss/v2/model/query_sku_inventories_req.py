# coding: utf-8

import pprint
import re

import six





class QuerySkuInventoriesReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sku_items': 'list[SkuItem]'
    }

    attribute_map = {
        'sku_items': 'sku_items'
    }

    def __init__(self, sku_items=None):
        """QuerySkuInventoriesReq - a model defined in huaweicloud sdk"""
        
        

        self._sku_items = None
        self.discriminator = None

        self.sku_items = sku_items

    @property
    def sku_items(self):
        """Gets the sku_items of this QuerySkuInventoriesReq.

        |参数名称：待查询库存项| |参数约束以及描述：待查询库存项|

        :return: The sku_items of this QuerySkuInventoriesReq.
        :rtype: list[SkuItem]
        """
        return self._sku_items

    @sku_items.setter
    def sku_items(self, sku_items):
        """Sets the sku_items of this QuerySkuInventoriesReq.

        |参数名称：待查询库存项| |参数约束以及描述：待查询库存项|

        :param sku_items: The sku_items of this QuerySkuInventoriesReq.
        :type: list[SkuItem]
        """
        self._sku_items = sku_items

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
        if not isinstance(other, QuerySkuInventoriesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
