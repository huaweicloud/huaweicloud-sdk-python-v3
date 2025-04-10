# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProductsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'products': 'list[ProductDetailInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'products': 'products',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, count=None, products=None, x_request_id=None):
        r"""ListProductsResponse

        The model defined in huaweicloud sdk

        :param count: **参数解释**： 商品信息总数
        :type count: int
        :param products: 商品信息列表
        :type products: list[:class:`huaweicloudsdkmetastudio.v1.ProductDetailInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListProductsResponse, self).__init__()

        self._count = None
        self._products = None
        self._x_request_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if products is not None:
            self.products = products
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def count(self):
        r"""Gets the count of this ListProductsResponse.

        **参数解释**： 商品信息总数

        :return: The count of this ListProductsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListProductsResponse.

        **参数解释**： 商品信息总数

        :param count: The count of this ListProductsResponse.
        :type count: int
        """
        self._count = count

    @property
    def products(self):
        r"""Gets the products of this ListProductsResponse.

        商品信息列表

        :return: The products of this ListProductsResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ProductDetailInfo`]
        """
        return self._products

    @products.setter
    def products(self, products):
        r"""Sets the products of this ListProductsResponse.

        商品信息列表

        :param products: The products of this ListProductsResponse.
        :type products: list[:class:`huaweicloudsdkmetastudio.v1.ProductDetailInfo`]
        """
        self._products = products

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListProductsResponse.

        :return: The x_request_id of this ListProductsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListProductsResponse.

        :param x_request_id: The x_request_id of this ListProductsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListProductsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
