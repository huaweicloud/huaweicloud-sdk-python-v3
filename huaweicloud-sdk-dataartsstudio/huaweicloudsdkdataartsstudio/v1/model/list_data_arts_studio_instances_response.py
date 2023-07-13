# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataArtsStudioInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'billing_check': 'bool',
        'count': 'int',
        'commodity_order_lists': 'list[ApigCommodityOrder]'
    }

    attribute_map = {
        'billing_check': 'billing_check',
        'count': 'count',
        'commodity_order_lists': 'commodity_order_lists'
    }

    def __init__(self, billing_check=None, count=None, commodity_order_lists=None):
        """ListDataArtsStudioInstancesResponse

        The model defined in huaweicloud sdk

        :param billing_check: 是否需要账单
        :type billing_check: bool
        :param count: 返回记录总数
        :type count: int
        :param commodity_order_lists: 返回实例列表
        :type commodity_order_lists: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigCommodityOrder`]
        """
        
        super(ListDataArtsStudioInstancesResponse, self).__init__()

        self._billing_check = None
        self._count = None
        self._commodity_order_lists = None
        self.discriminator = None

        if billing_check is not None:
            self.billing_check = billing_check
        if count is not None:
            self.count = count
        if commodity_order_lists is not None:
            self.commodity_order_lists = commodity_order_lists

    @property
    def billing_check(self):
        """Gets the billing_check of this ListDataArtsStudioInstancesResponse.

        是否需要账单

        :return: The billing_check of this ListDataArtsStudioInstancesResponse.
        :rtype: bool
        """
        return self._billing_check

    @billing_check.setter
    def billing_check(self, billing_check):
        """Sets the billing_check of this ListDataArtsStudioInstancesResponse.

        是否需要账单

        :param billing_check: The billing_check of this ListDataArtsStudioInstancesResponse.
        :type billing_check: bool
        """
        self._billing_check = billing_check

    @property
    def count(self):
        """Gets the count of this ListDataArtsStudioInstancesResponse.

        返回记录总数

        :return: The count of this ListDataArtsStudioInstancesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListDataArtsStudioInstancesResponse.

        返回记录总数

        :param count: The count of this ListDataArtsStudioInstancesResponse.
        :type count: int
        """
        self._count = count

    @property
    def commodity_order_lists(self):
        """Gets the commodity_order_lists of this ListDataArtsStudioInstancesResponse.

        返回实例列表

        :return: The commodity_order_lists of this ListDataArtsStudioInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigCommodityOrder`]
        """
        return self._commodity_order_lists

    @commodity_order_lists.setter
    def commodity_order_lists(self, commodity_order_lists):
        """Sets the commodity_order_lists of this ListDataArtsStudioInstancesResponse.

        返回实例列表

        :param commodity_order_lists: The commodity_order_lists of this ListDataArtsStudioInstancesResponse.
        :type commodity_order_lists: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigCommodityOrder`]
        """
        self._commodity_order_lists = commodity_order_lists

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
        if not isinstance(other, ListDataArtsStudioInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
