# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRefundOrderDetailsRequest:

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
        'customer_id': 'str',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'order_id': 'order_id',
        'customer_id': 'customer_id',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, order_id=None, customer_id=None, indirect_partner_id=None):
        r"""ShowRefundOrderDetailsRequest

        The model defined in huaweicloud sdk

        :param order_id: 退订订单或者降配订单的ID。
        :type order_id: str
        :param customer_id: 客户账号ID，非必填，范围限制:0-64，伙伴查询子客户退款订单的金额详情必须携带该字段。
        :type customer_id: str
        :param indirect_partner_id: 云经销商ID，非必填，范围限制:0-64，如果华为云总经销商（一级经销商）需要查询云经销商的子客户退款订单的金额详情必须携带该字段。除此之外，此参数不做处理。|
        :type indirect_partner_id: str
        """
        
        

        self._order_id = None
        self._customer_id = None
        self._indirect_partner_id = None
        self.discriminator = None

        self.order_id = order_id
        if customer_id is not None:
            self.customer_id = customer_id
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def order_id(self):
        r"""Gets the order_id of this ShowRefundOrderDetailsRequest.

        退订订单或者降配订单的ID。

        :return: The order_id of this ShowRefundOrderDetailsRequest.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ShowRefundOrderDetailsRequest.

        退订订单或者降配订单的ID。

        :param order_id: The order_id of this ShowRefundOrderDetailsRequest.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def customer_id(self):
        r"""Gets the customer_id of this ShowRefundOrderDetailsRequest.

        客户账号ID，非必填，范围限制:0-64，伙伴查询子客户退款订单的金额详情必须携带该字段。

        :return: The customer_id of this ShowRefundOrderDetailsRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this ShowRefundOrderDetailsRequest.

        客户账号ID，非必填，范围限制:0-64，伙伴查询子客户退款订单的金额详情必须携带该字段。

        :param customer_id: The customer_id of this ShowRefundOrderDetailsRequest.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def indirect_partner_id(self):
        r"""Gets the indirect_partner_id of this ShowRefundOrderDetailsRequest.

        云经销商ID，非必填，范围限制:0-64，如果华为云总经销商（一级经销商）需要查询云经销商的子客户退款订单的金额详情必须携带该字段。除此之外，此参数不做处理。|

        :return: The indirect_partner_id of this ShowRefundOrderDetailsRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        r"""Sets the indirect_partner_id of this ShowRefundOrderDetailsRequest.

        云经销商ID，非必填，范围限制:0-64，如果华为云总经销商（一级经销商）需要查询云经销商的子客户退款订单的金额详情必须携带该字段。除此之外，此参数不做处理。|

        :param indirect_partner_id: The indirect_partner_id of this ShowRefundOrderDetailsRequest.
        :type indirect_partner_id: str
        """
        self._indirect_partner_id = indirect_partner_id

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
        if not isinstance(other, ShowRefundOrderDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
