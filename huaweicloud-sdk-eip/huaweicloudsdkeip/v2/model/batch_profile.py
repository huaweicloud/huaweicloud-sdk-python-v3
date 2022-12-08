# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchProfile:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'product_id': 'str',
        'region_id': 'str',
        'order_id': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'product_id': 'product_id',
        'region_id': 'region_id',
        'order_id': 'order_id'
    }

    def __init__(self, user_id=None, product_id=None, region_id=None, order_id=None):
        """BatchProfile

        The model defined in huaweicloud sdk

        :param user_id: 租户id
        :type user_id: str
        :param product_id: 产品id
        :type product_id: str
        :param region_id: 局点id
        :type region_id: str
        :param order_id: 订单id
        :type order_id: str
        """
        
        

        self._user_id = None
        self._product_id = None
        self._region_id = None
        self._order_id = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if product_id is not None:
            self.product_id = product_id
        if region_id is not None:
            self.region_id = region_id
        if order_id is not None:
            self.order_id = order_id

    @property
    def user_id(self):
        """Gets the user_id of this BatchProfile.

        租户id

        :return: The user_id of this BatchProfile.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BatchProfile.

        租户id

        :param user_id: The user_id of this BatchProfile.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def product_id(self):
        """Gets the product_id of this BatchProfile.

        产品id

        :return: The product_id of this BatchProfile.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this BatchProfile.

        产品id

        :param product_id: The product_id of this BatchProfile.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def region_id(self):
        """Gets the region_id of this BatchProfile.

        局点id

        :return: The region_id of this BatchProfile.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this BatchProfile.

        局点id

        :param region_id: The region_id of this BatchProfile.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def order_id(self):
        """Gets the order_id of this BatchProfile.

        订单id

        :return: The order_id of this BatchProfile.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this BatchProfile.

        订单id

        :param order_id: The order_id of this BatchProfile.
        :type order_id: str
        """
        self._order_id = order_id

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
        if not isinstance(other, BatchProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
