# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProductResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'os_type': 'str',
        'products': 'list[ProductInfo]'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'os_type': 'os_type',
        'products': 'products'
    }

    def __init__(self, availability_zone=None, os_type=None, products=None):
        """ListProductResponse

        The model defined in huaweicloud sdk

        :param availability_zone: 可用分区。将服务创建到指定的可用分区。如果不指定则使用系统随机的可用分区。
        :type availability_zone: str
        :param os_type: 系统类型，当前仅支持Windows。 * &#x60;Linux&#x60; - * &#x60;Windows&#x60; - * &#x60;Other&#x60; -
        :type os_type: str
        :param products: 产品列表
        :type products: list[:class:`huaweicloudsdkworkspaceapp.v1.ProductInfo`]
        """
        
        super(ListProductResponse, self).__init__()

        self._availability_zone = None
        self._os_type = None
        self._products = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        if os_type is not None:
            self.os_type = os_type
        if products is not None:
            self.products = products

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ListProductResponse.

        可用分区。将服务创建到指定的可用分区。如果不指定则使用系统随机的可用分区。

        :return: The availability_zone of this ListProductResponse.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ListProductResponse.

        可用分区。将服务创建到指定的可用分区。如果不指定则使用系统随机的可用分区。

        :param availability_zone: The availability_zone of this ListProductResponse.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def os_type(self):
        """Gets the os_type of this ListProductResponse.

        系统类型，当前仅支持Windows。 * `Linux` - * `Windows` - * `Other` -

        :return: The os_type of this ListProductResponse.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ListProductResponse.

        系统类型，当前仅支持Windows。 * `Linux` - * `Windows` - * `Other` -

        :param os_type: The os_type of this ListProductResponse.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def products(self):
        """Gets the products of this ListProductResponse.

        产品列表

        :return: The products of this ListProductResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.ProductInfo`]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this ListProductResponse.

        产品列表

        :param products: The products of this ListProductResponse.
        :type products: list[:class:`huaweicloudsdkworkspaceapp.v1.ProductInfo`]
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
        if not isinstance(other, ListProductResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
