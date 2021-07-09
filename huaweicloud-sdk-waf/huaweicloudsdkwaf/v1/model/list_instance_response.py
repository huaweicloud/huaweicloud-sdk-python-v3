# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListInstanceResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'purchased': 'bool',
        'items': 'list[PremiumWafInstance]'
    }

    attribute_map = {
        'total': 'total',
        'purchased': 'purchased',
        'items': 'items'
    }

    def __init__(self, total=None, purchased=None, items=None):
        """ListInstanceResponse - a model defined in huaweicloud sdk"""
        
        super(ListInstanceResponse, self).__init__()

        self._total = None
        self._purchased = None
        self._items = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if purchased is not None:
            self.purchased = purchased
        if items is not None:
            self.items = items

    @property
    def total(self):
        """Gets the total of this ListInstanceResponse.

        全部独享引擎的数量

        :return: The total of this ListInstanceResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListInstanceResponse.

        全部独享引擎的数量

        :param total: The total of this ListInstanceResponse.
        :type: int
        """
        self._total = total

    @property
    def purchased(self):
        """Gets the purchased of this ListInstanceResponse.

        是否曾经购买过独享引擎

        :return: The purchased of this ListInstanceResponse.
        :rtype: bool
        """
        return self._purchased

    @purchased.setter
    def purchased(self, purchased):
        """Sets the purchased of this ListInstanceResponse.

        是否曾经购买过独享引擎

        :param purchased: The purchased of this ListInstanceResponse.
        :type: bool
        """
        self._purchased = purchased

    @property
    def items(self):
        """Gets the items of this ListInstanceResponse.

        详细的独享引擎信息

        :return: The items of this ListInstanceResponse.
        :rtype: list[PremiumWafInstance]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ListInstanceResponse.

        详细的独享引擎信息

        :param items: The items of this ListInstanceResponse.
        :type: list[PremiumWafInstance]
        """
        self._items = items

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
