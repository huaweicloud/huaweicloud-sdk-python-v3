# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProfileResp:

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
        'region_id': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'order_id': 'order_id',
        'product_id': 'product_id',
        'region_id': 'region_id',
        'user_id': 'user_id'
    }

    def __init__(self, order_id=None, product_id=None, region_id=None, user_id=None):
        r"""ProfileResp

        The model defined in huaweicloud sdk

        :param order_id: 订单的id
        :type order_id: str
        :param product_id: 产品的id
        :type product_id: str
        :param region_id: region的id
        :type region_id: str
        :param user_id: 用户的id
        :type user_id: str
        """
        
        

        self._order_id = None
        self._product_id = None
        self._region_id = None
        self._user_id = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if product_id is not None:
            self.product_id = product_id
        if region_id is not None:
            self.region_id = region_id
        if user_id is not None:
            self.user_id = user_id

    @property
    def order_id(self):
        r"""Gets the order_id of this ProfileResp.

        订单的id

        :return: The order_id of this ProfileResp.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ProfileResp.

        订单的id

        :param order_id: The order_id of this ProfileResp.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def product_id(self):
        r"""Gets the product_id of this ProfileResp.

        产品的id

        :return: The product_id of this ProfileResp.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ProfileResp.

        产品的id

        :param product_id: The product_id of this ProfileResp.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ProfileResp.

        region的id

        :return: The region_id of this ProfileResp.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ProfileResp.

        region的id

        :param region_id: The region_id of this ProfileResp.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def user_id(self):
        r"""Gets the user_id of this ProfileResp.

        用户的id

        :return: The user_id of this ProfileResp.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ProfileResp.

        用户的id

        :param user_id: The user_id of this ProfileResp.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, ProfileResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
