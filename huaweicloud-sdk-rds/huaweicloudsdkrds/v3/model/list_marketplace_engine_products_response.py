# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMarketplaceEngineProductsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marketplace_engine_products': 'list[MarketplaceEngineProduct]',
        'total_count': 'int'
    }

    attribute_map = {
        'marketplace_engine_products': 'marketplace_engine_products',
        'total_count': 'total_count'
    }

    def __init__(self, marketplace_engine_products=None, total_count=None):
        r"""ListMarketplaceEngineProductsResponse

        The model defined in huaweicloud sdk

        :param marketplace_engine_products: 云市场引擎商品列表。
        :type marketplace_engine_products: list[:class:`huaweicloudsdkrds.v3.MarketplaceEngineProduct`]
        :param total_count: 云市场引擎商品总数。
        :type total_count: int
        """
        
        super(ListMarketplaceEngineProductsResponse, self).__init__()

        self._marketplace_engine_products = None
        self._total_count = None
        self.discriminator = None

        if marketplace_engine_products is not None:
            self.marketplace_engine_products = marketplace_engine_products
        if total_count is not None:
            self.total_count = total_count

    @property
    def marketplace_engine_products(self):
        r"""Gets the marketplace_engine_products of this ListMarketplaceEngineProductsResponse.

        云市场引擎商品列表。

        :return: The marketplace_engine_products of this ListMarketplaceEngineProductsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.MarketplaceEngineProduct`]
        """
        return self._marketplace_engine_products

    @marketplace_engine_products.setter
    def marketplace_engine_products(self, marketplace_engine_products):
        r"""Sets the marketplace_engine_products of this ListMarketplaceEngineProductsResponse.

        云市场引擎商品列表。

        :param marketplace_engine_products: The marketplace_engine_products of this ListMarketplaceEngineProductsResponse.
        :type marketplace_engine_products: list[:class:`huaweicloudsdkrds.v3.MarketplaceEngineProduct`]
        """
        self._marketplace_engine_products = marketplace_engine_products

    @property
    def total_count(self):
        r"""Gets the total_count of this ListMarketplaceEngineProductsResponse.

        云市场引擎商品总数。

        :return: The total_count of this ListMarketplaceEngineProductsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListMarketplaceEngineProductsResponse.

        云市场引擎商品总数。

        :param total_count: The total_count of this ListMarketplaceEngineProductsResponse.
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
        if not isinstance(other, ListMarketplaceEngineProductsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
