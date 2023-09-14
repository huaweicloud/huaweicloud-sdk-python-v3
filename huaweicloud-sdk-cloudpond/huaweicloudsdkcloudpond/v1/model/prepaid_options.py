# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrepaidOptions:

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
        'product_id': 'str',
        'pay_mode': 'PayMode'
    }

    attribute_map = {
        'order_id': 'order_id',
        'product_id': 'product_id',
        'pay_mode': 'pay_mode'
    }

    def __init__(self, order_id=None, product_id=None, pay_mode=None):
        """PrepaidOptions

        The model defined in huaweicloud sdk

        :param order_id: 订单ID
        :type order_id: str
        :param product_id: 产品ID
        :type product_id: str
        :param pay_mode: 
        :type pay_mode: :class:`huaweicloudsdkcloudpond.v1.PayMode`
        """
        
        

        self._order_id = None
        self._product_id = None
        self._pay_mode = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if product_id is not None:
            self.product_id = product_id
        if pay_mode is not None:
            self.pay_mode = pay_mode

    @property
    def order_id(self):
        """Gets the order_id of this PrepaidOptions.

        订单ID

        :return: The order_id of this PrepaidOptions.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PrepaidOptions.

        订单ID

        :param order_id: The order_id of this PrepaidOptions.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def product_id(self):
        """Gets the product_id of this PrepaidOptions.

        产品ID

        :return: The product_id of this PrepaidOptions.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this PrepaidOptions.

        产品ID

        :param product_id: The product_id of this PrepaidOptions.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def pay_mode(self):
        """Gets the pay_mode of this PrepaidOptions.

        :return: The pay_mode of this PrepaidOptions.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.PayMode`
        """
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, pay_mode):
        """Sets the pay_mode of this PrepaidOptions.

        :param pay_mode: The pay_mode of this PrepaidOptions.
        :type pay_mode: :class:`huaweicloudsdkcloudpond.v1.PayMode`
        """
        self._pay_mode = pay_mode

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
        if not isinstance(other, PrepaidOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
