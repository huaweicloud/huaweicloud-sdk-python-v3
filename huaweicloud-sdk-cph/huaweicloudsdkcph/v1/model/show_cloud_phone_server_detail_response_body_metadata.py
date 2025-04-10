# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCloudPhoneServerDetailResponseBodyMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charging_mode': 'int',
        'product_id': 'str',
        'order_id': 'str'
    }

    attribute_map = {
        'charging_mode': 'charging_mode',
        'product_id': 'product_id',
        'order_id': 'order_id'
    }

    def __init__(self, charging_mode=None, product_id=None, order_id=None):
        r"""ShowCloudPhoneServerDetailResponseBodyMetadata

        The model defined in huaweicloud sdk

        :param charging_mode: 计费类型。 [- 0：包周期](tag:hws,hws_hk,cmcc)
        :type charging_mode: int
        :param product_id: 产品ID，不超过64个字节。
        :type product_id: str
        :param order_id: 订单ID，不超过64个字节。
        :type order_id: str
        """
        
        

        self._charging_mode = None
        self._product_id = None
        self._order_id = None
        self.discriminator = None

        if charging_mode is not None:
            self.charging_mode = charging_mode
        if product_id is not None:
            self.product_id = product_id
        if order_id is not None:
            self.order_id = order_id

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ShowCloudPhoneServerDetailResponseBodyMetadata.

        计费类型。 [- 0：包周期](tag:hws,hws_hk,cmcc)

        :return: The charging_mode of this ShowCloudPhoneServerDetailResponseBodyMetadata.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ShowCloudPhoneServerDetailResponseBodyMetadata.

        计费类型。 [- 0：包周期](tag:hws,hws_hk,cmcc)

        :param charging_mode: The charging_mode of this ShowCloudPhoneServerDetailResponseBodyMetadata.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def product_id(self):
        r"""Gets the product_id of this ShowCloudPhoneServerDetailResponseBodyMetadata.

        产品ID，不超过64个字节。

        :return: The product_id of this ShowCloudPhoneServerDetailResponseBodyMetadata.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ShowCloudPhoneServerDetailResponseBodyMetadata.

        产品ID，不超过64个字节。

        :param product_id: The product_id of this ShowCloudPhoneServerDetailResponseBodyMetadata.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def order_id(self):
        r"""Gets the order_id of this ShowCloudPhoneServerDetailResponseBodyMetadata.

        订单ID，不超过64个字节。

        :return: The order_id of this ShowCloudPhoneServerDetailResponseBodyMetadata.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ShowCloudPhoneServerDetailResponseBodyMetadata.

        订单ID，不超过64个字节。

        :param order_id: The order_id of this ShowCloudPhoneServerDetailResponseBodyMetadata.
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
        if not isinstance(other, ShowCloudPhoneServerDetailResponseBodyMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
