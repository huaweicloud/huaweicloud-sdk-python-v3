# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCloudPhoneDetailResponseBodyMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'product_id': 'str'
    }

    attribute_map = {
        'order_id': 'order_id',
        'product_id': 'product_id'
    }

    def __init__(self, order_id=None, product_id=None):
        """ShowCloudPhoneDetailResponseBodyMetadata

        The model defined in huaweicloud sdk

        :param order_id: 订单ID，不超过64个字节。
        :type order_id: str
        :param product_id: 产品ID，不超过64个字节。
        :type product_id: str
        """
        
        

        self._order_id = None
        self._product_id = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if product_id is not None:
            self.product_id = product_id

    @property
    def order_id(self):
        """Gets the order_id of this ShowCloudPhoneDetailResponseBodyMetadata.

        订单ID，不超过64个字节。

        :return: The order_id of this ShowCloudPhoneDetailResponseBodyMetadata.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ShowCloudPhoneDetailResponseBodyMetadata.

        订单ID，不超过64个字节。

        :param order_id: The order_id of this ShowCloudPhoneDetailResponseBodyMetadata.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def product_id(self):
        """Gets the product_id of this ShowCloudPhoneDetailResponseBodyMetadata.

        产品ID，不超过64个字节。

        :return: The product_id of this ShowCloudPhoneDetailResponseBodyMetadata.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ShowCloudPhoneDetailResponseBodyMetadata.

        产品ID，不超过64个字节。

        :param product_id: The product_id of this ShowCloudPhoneDetailResponseBodyMetadata.
        :type product_id: str
        """
        self._product_id = product_id

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
        if not isinstance(other, ShowCloudPhoneDetailResponseBodyMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
