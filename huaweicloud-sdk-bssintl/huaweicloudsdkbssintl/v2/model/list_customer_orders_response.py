# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomerOrdersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'order_infos': 'list[CustomerOrderV2]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'order_infos': 'order_infos'
    }

    def __init__(self, total_count=None, order_infos=None):
        r"""ListCustomerOrdersResponse

        The model defined in huaweicloud sdk

        :param total_count: 大于等于0的整数。 符合条件的记录总数。
        :type total_count: int
        :param order_infos: - 客户订单详情信息。 具体请参见表2
        :type order_infos: list[:class:`huaweicloudsdkbssintl.v2.CustomerOrderV2`]
        """
        
        super(ListCustomerOrdersResponse, self).__init__()

        self._total_count = None
        self._order_infos = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if order_infos is not None:
            self.order_infos = order_infos

    @property
    def total_count(self):
        r"""Gets the total_count of this ListCustomerOrdersResponse.

        大于等于0的整数。 符合条件的记录总数。

        :return: The total_count of this ListCustomerOrdersResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListCustomerOrdersResponse.

        大于等于0的整数。 符合条件的记录总数。

        :param total_count: The total_count of this ListCustomerOrdersResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def order_infos(self):
        r"""Gets the order_infos of this ListCustomerOrdersResponse.

        - 客户订单详情信息。 具体请参见表2

        :return: The order_infos of this ListCustomerOrdersResponse.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.CustomerOrderV2`]
        """
        return self._order_infos

    @order_infos.setter
    def order_infos(self, order_infos):
        r"""Sets the order_infos of this ListCustomerOrdersResponse.

        - 客户订单详情信息。 具体请参见表2

        :param order_infos: The order_infos of this ListCustomerOrdersResponse.
        :type order_infos: list[:class:`huaweicloudsdkbssintl.v2.CustomerOrderV2`]
        """
        self._order_infos = order_infos

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
        if not isinstance(other, ListCustomerOrdersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
