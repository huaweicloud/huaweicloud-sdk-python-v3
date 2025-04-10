# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSharerProductsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'products': 'list[SharerProductInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'products': 'products',
        'total_count': 'total_count'
    }

    def __init__(self, products=None, total_count=None):
        r"""ListSharerProductsResponse

        The model defined in huaweicloud sdk

        :param products: 产品列表。
        :type products: list[:class:`huaweicloudsdkworkspace.v2.SharerProductInfo`]
        :param total_count: 对象总数。
        :type total_count: int
        """
        
        super(ListSharerProductsResponse, self).__init__()

        self._products = None
        self._total_count = None
        self.discriminator = None

        if products is not None:
            self.products = products
        if total_count is not None:
            self.total_count = total_count

    @property
    def products(self):
        r"""Gets the products of this ListSharerProductsResponse.

        产品列表。

        :return: The products of this ListSharerProductsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SharerProductInfo`]
        """
        return self._products

    @products.setter
    def products(self, products):
        r"""Sets the products of this ListSharerProductsResponse.

        产品列表。

        :param products: The products of this ListSharerProductsResponse.
        :type products: list[:class:`huaweicloudsdkworkspace.v2.SharerProductInfo`]
        """
        self._products = products

    @property
    def total_count(self):
        r"""Gets the total_count of this ListSharerProductsResponse.

        对象总数。

        :return: The total_count of this ListSharerProductsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListSharerProductsResponse.

        对象总数。

        :param total_count: The total_count of this ListSharerProductsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListSharerProductsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
