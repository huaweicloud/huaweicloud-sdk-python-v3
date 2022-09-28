# coding: utf-8

import re
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
        'os_type': 'str',
        'availability_zone': 'str',
        'products': 'list[ProductInfo]'
    }

    attribute_map = {
        'os_type': 'os_type',
        'availability_zone': 'availability_zone',
        'products': 'products'
    }

    def __init__(self, os_type=None, availability_zone=None, products=None):
        """ListProductsResponse

        The model defined in huaweicloud sdk

        :param os_type: 套餐所支持操作系统类型。请求参数有os_type时，才有此参数。
        :type os_type: str
        :param availability_zone: 可用分区。请求参数有availability_zone时，才有此参数。
        :type availability_zone: str
        :param products: 产品列表。
        :type products: list[:class:`huaweicloudsdkworkspace.v2.ProductInfo`]
        """
        
        super(ListProductsResponse, self).__init__()

        self._os_type = None
        self._availability_zone = None
        self._products = None
        self.discriminator = None

        if os_type is not None:
            self.os_type = os_type
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if products is not None:
            self.products = products

    @property
    def os_type(self):
        """Gets the os_type of this ListProductsResponse.

        套餐所支持操作系统类型。请求参数有os_type时，才有此参数。

        :return: The os_type of this ListProductsResponse.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ListProductsResponse.

        套餐所支持操作系统类型。请求参数有os_type时，才有此参数。

        :param os_type: The os_type of this ListProductsResponse.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ListProductsResponse.

        可用分区。请求参数有availability_zone时，才有此参数。

        :return: The availability_zone of this ListProductsResponse.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ListProductsResponse.

        可用分区。请求参数有availability_zone时，才有此参数。

        :param availability_zone: The availability_zone of this ListProductsResponse.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def products(self):
        """Gets the products of this ListProductsResponse.

        产品列表。

        :return: The products of this ListProductsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ProductInfo`]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this ListProductsResponse.

        产品列表。

        :param products: The products of this ListProductsResponse.
        :type products: list[:class:`huaweicloudsdkworkspace.v2.ProductInfo`]
        """
        self._products = products

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
