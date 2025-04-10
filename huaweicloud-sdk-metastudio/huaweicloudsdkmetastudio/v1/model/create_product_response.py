# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProductResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, product_id=None, x_request_id=None):
        r"""CreateProductResponse

        The model defined in huaweicloud sdk

        :param product_id: 商品ID
        :type product_id: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateProductResponse, self).__init__()

        self._product_id = None
        self._x_request_id = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def product_id(self):
        r"""Gets the product_id of this CreateProductResponse.

        商品ID

        :return: The product_id of this CreateProductResponse.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this CreateProductResponse.

        商品ID

        :param product_id: The product_id of this CreateProductResponse.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateProductResponse.

        :return: The x_request_id of this CreateProductResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateProductResponse.

        :param x_request_id: The x_request_id of this CreateProductResponse.
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
        if not isinstance(other, CreateProductResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
