# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProPricePlansResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'count': 'int',
        'price_plans': 'list[ProPricePlanVo]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'count': 'count',
        'price_plans': 'price_plans'
    }

    def __init__(self, limit=None, offset=None, count=None, price_plans=None):
        """ListProPricePlansResponse

        The model defined in huaweicloud sdk

        :param limit: 每页的记录数
        :type limit: int
        :param offset: 页码，最小值是1，最大值为1000000。默认值是1.
        :type offset: int
        :param count: 记录总数
        :type count: int
        :param price_plans: 套餐列表
        :type price_plans: list[:class:`huaweicloudsdkgsl.v3.ProPricePlanVo`]
        """
        
        super(ListProPricePlansResponse, self).__init__()

        self._limit = None
        self._offset = None
        self._count = None
        self._price_plans = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if count is not None:
            self.count = count
        if price_plans is not None:
            self.price_plans = price_plans

    @property
    def limit(self):
        """Gets the limit of this ListProPricePlansResponse.

        每页的记录数

        :return: The limit of this ListProPricePlansResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProPricePlansResponse.

        每页的记录数

        :param limit: The limit of this ListProPricePlansResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListProPricePlansResponse.

        页码，最小值是1，最大值为1000000。默认值是1.

        :return: The offset of this ListProPricePlansResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProPricePlansResponse.

        页码，最小值是1，最大值为1000000。默认值是1.

        :param offset: The offset of this ListProPricePlansResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def count(self):
        """Gets the count of this ListProPricePlansResponse.

        记录总数

        :return: The count of this ListProPricePlansResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListProPricePlansResponse.

        记录总数

        :param count: The count of this ListProPricePlansResponse.
        :type count: int
        """
        self._count = count

    @property
    def price_plans(self):
        """Gets the price_plans of this ListProPricePlansResponse.

        套餐列表

        :return: The price_plans of this ListProPricePlansResponse.
        :rtype: list[:class:`huaweicloudsdkgsl.v3.ProPricePlanVo`]
        """
        return self._price_plans

    @price_plans.setter
    def price_plans(self, price_plans):
        """Sets the price_plans of this ListProPricePlansResponse.

        套餐列表

        :param price_plans: The price_plans of this ListProPricePlansResponse.
        :type price_plans: list[:class:`huaweicloudsdkgsl.v3.ProPricePlanVo`]
        """
        self._price_plans = price_plans

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
        if not isinstance(other, ListProPricePlansResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
