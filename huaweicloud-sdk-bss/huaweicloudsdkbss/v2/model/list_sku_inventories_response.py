# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListSkuInventoriesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sku_inventories': 'list[SkuInventory]'
    }

    attribute_map = {
        'sku_inventories': 'sku_inventories'
    }

    def __init__(self, sku_inventories=None):
        """ListSkuInventoriesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._sku_inventories = None
        self.discriminator = None

        if sku_inventories is not None:
            self.sku_inventories = sku_inventories

    @property
    def sku_inventories(self):
        """Gets the sku_inventories of this ListSkuInventoriesResponse.

        |参数名称：总记录数| |参数约束以及描述：总记录数|

        :return: The sku_inventories of this ListSkuInventoriesResponse.
        :rtype: list[SkuInventory]
        """
        return self._sku_inventories

    @sku_inventories.setter
    def sku_inventories(self, sku_inventories):
        """Sets the sku_inventories of this ListSkuInventoriesResponse.

        |参数名称：总记录数| |参数约束以及描述：总记录数|

        :param sku_inventories: The sku_inventories of this ListSkuInventoriesResponse.
        :type: list[SkuInventory]
        """
        self._sku_inventories = sku_inventories

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
        if not isinstance(other, ListSkuInventoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
