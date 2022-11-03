# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'items': 'list[ListInstance]'
    }

    attribute_map = {
        'total': 'total',
        'purchased': 'purchased',
        'items': 'items'
    }

    def __init__(self, total=None, purchased=None, items=None):
        """ListInstanceResponse

        The model defined in huaweicloud sdk

        :param total: 独享引擎实例数量
        :type total: int
        :param purchased: 是否曾经购买过独享引擎
        :type purchased: bool
        :param items: 详细的独享引擎信息列表
        :type items: list[:class:`huaweicloudsdkwaf.v1.ListInstance`]
        """
        
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

        独享引擎实例数量

        :return: The total of this ListInstanceResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListInstanceResponse.

        独享引擎实例数量

        :param total: The total of this ListInstanceResponse.
        :type total: int
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
        :type purchased: bool
        """
        self._purchased = purchased

    @property
    def items(self):
        """Gets the items of this ListInstanceResponse.

        详细的独享引擎信息列表

        :return: The items of this ListInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.ListInstance`]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ListInstanceResponse.

        详细的独享引擎信息列表

        :param items: The items of this ListInstanceResponse.
        :type items: list[:class:`huaweicloudsdkwaf.v1.ListInstance`]
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
        if not isinstance(other, ListInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
