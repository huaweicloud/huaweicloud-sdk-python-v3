# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscribePackageProductsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'package_products': 'list[PackageProductRequestDetail]'
    }

    attribute_map = {
        'package_products': 'package_products'
    }

    def __init__(self, package_products=None):
        r"""SubscribePackageProductsRequestBody

        The model defined in huaweicloud sdk

        :param package_products: 套餐包列表。
        :type package_products: list[:class:`huaweicloudsdkcce.v5.PackageProductRequestDetail`]
        """
        
        

        self._package_products = None
        self.discriminator = None

        self.package_products = package_products

    @property
    def package_products(self):
        r"""Gets the package_products of this SubscribePackageProductsRequestBody.

        套餐包列表。

        :return: The package_products of this SubscribePackageProductsRequestBody.
        :rtype: list[:class:`huaweicloudsdkcce.v5.PackageProductRequestDetail`]
        """
        return self._package_products

    @package_products.setter
    def package_products(self, package_products):
        r"""Sets the package_products of this SubscribePackageProductsRequestBody.

        套餐包列表。

        :param package_products: The package_products of this SubscribePackageProductsRequestBody.
        :type package_products: list[:class:`huaweicloudsdkcce.v5.PackageProductRequestDetail`]
        """
        self._package_products = package_products

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubscribePackageProductsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
