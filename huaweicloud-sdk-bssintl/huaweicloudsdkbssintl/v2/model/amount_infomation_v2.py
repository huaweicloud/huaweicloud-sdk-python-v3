# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AmountInfomationV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'discounts': 'list[DiscountItemV2]',
        'flexipurchase_coupon_amount': 'float',
        'coupon_amount': 'float',
        'stored_card_amount': 'float',
        'commission_amount': 'float',
        'consumed_amount': 'float'
    }

    attribute_map = {
        'discounts': 'discounts',
        'flexipurchase_coupon_amount': 'flexipurchase_coupon_amount',
        'coupon_amount': 'coupon_amount',
        'stored_card_amount': 'stored_card_amount',
        'commission_amount': 'commission_amount',
        'consumed_amount': 'consumed_amount'
    }

    def __init__(self, discounts=None, flexipurchase_coupon_amount=None, coupon_amount=None, stored_card_amount=None, commission_amount=None, consumed_amount=None):
        """AmountInfomationV2

        The model defined in huaweicloud sdk

        :param discounts: 费用项。 具体请参见表7。
        :type discounts: list[:class:`huaweicloudsdkbssintl.v2.DiscountItemV2`]
        :param flexipurchase_coupon_amount: 现金券金额，预留。
        :type flexipurchase_coupon_amount: float
        :param coupon_amount: 代金券金额。
        :type coupon_amount: float
        :param stored_card_amount: 储值卡金额，预留。
        :type stored_card_amount: float
        :param commission_amount: 手续费（仅退订订单存在）。
        :type commission_amount: float
        :param consumed_amount: 消费金额（仅退订订单存在）。
        :type consumed_amount: float
        """
        
        

        self._discounts = None
        self._flexipurchase_coupon_amount = None
        self._coupon_amount = None
        self._stored_card_amount = None
        self._commission_amount = None
        self._consumed_amount = None
        self.discriminator = None

        if discounts is not None:
            self.discounts = discounts
        if flexipurchase_coupon_amount is not None:
            self.flexipurchase_coupon_amount = flexipurchase_coupon_amount
        if coupon_amount is not None:
            self.coupon_amount = coupon_amount
        if stored_card_amount is not None:
            self.stored_card_amount = stored_card_amount
        if commission_amount is not None:
            self.commission_amount = commission_amount
        if consumed_amount is not None:
            self.consumed_amount = consumed_amount

    @property
    def discounts(self):
        """Gets the discounts of this AmountInfomationV2.

        费用项。 具体请参见表7。

        :return: The discounts of this AmountInfomationV2.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.DiscountItemV2`]
        """
        return self._discounts

    @discounts.setter
    def discounts(self, discounts):
        """Sets the discounts of this AmountInfomationV2.

        费用项。 具体请参见表7。

        :param discounts: The discounts of this AmountInfomationV2.
        :type discounts: list[:class:`huaweicloudsdkbssintl.v2.DiscountItemV2`]
        """
        self._discounts = discounts

    @property
    def flexipurchase_coupon_amount(self):
        """Gets the flexipurchase_coupon_amount of this AmountInfomationV2.

        现金券金额，预留。

        :return: The flexipurchase_coupon_amount of this AmountInfomationV2.
        :rtype: float
        """
        return self._flexipurchase_coupon_amount

    @flexipurchase_coupon_amount.setter
    def flexipurchase_coupon_amount(self, flexipurchase_coupon_amount):
        """Sets the flexipurchase_coupon_amount of this AmountInfomationV2.

        现金券金额，预留。

        :param flexipurchase_coupon_amount: The flexipurchase_coupon_amount of this AmountInfomationV2.
        :type flexipurchase_coupon_amount: float
        """
        self._flexipurchase_coupon_amount = flexipurchase_coupon_amount

    @property
    def coupon_amount(self):
        """Gets the coupon_amount of this AmountInfomationV2.

        代金券金额。

        :return: The coupon_amount of this AmountInfomationV2.
        :rtype: float
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        """Sets the coupon_amount of this AmountInfomationV2.

        代金券金额。

        :param coupon_amount: The coupon_amount of this AmountInfomationV2.
        :type coupon_amount: float
        """
        self._coupon_amount = coupon_amount

    @property
    def stored_card_amount(self):
        """Gets the stored_card_amount of this AmountInfomationV2.

        储值卡金额，预留。

        :return: The stored_card_amount of this AmountInfomationV2.
        :rtype: float
        """
        return self._stored_card_amount

    @stored_card_amount.setter
    def stored_card_amount(self, stored_card_amount):
        """Sets the stored_card_amount of this AmountInfomationV2.

        储值卡金额，预留。

        :param stored_card_amount: The stored_card_amount of this AmountInfomationV2.
        :type stored_card_amount: float
        """
        self._stored_card_amount = stored_card_amount

    @property
    def commission_amount(self):
        """Gets the commission_amount of this AmountInfomationV2.

        手续费（仅退订订单存在）。

        :return: The commission_amount of this AmountInfomationV2.
        :rtype: float
        """
        return self._commission_amount

    @commission_amount.setter
    def commission_amount(self, commission_amount):
        """Sets the commission_amount of this AmountInfomationV2.

        手续费（仅退订订单存在）。

        :param commission_amount: The commission_amount of this AmountInfomationV2.
        :type commission_amount: float
        """
        self._commission_amount = commission_amount

    @property
    def consumed_amount(self):
        """Gets the consumed_amount of this AmountInfomationV2.

        消费金额（仅退订订单存在）。

        :return: The consumed_amount of this AmountInfomationV2.
        :rtype: float
        """
        return self._consumed_amount

    @consumed_amount.setter
    def consumed_amount(self, consumed_amount):
        """Sets the consumed_amount of this AmountInfomationV2.

        消费金额（仅退订订单存在）。

        :param consumed_amount: The consumed_amount of this AmountInfomationV2.
        :type consumed_amount: float
        """
        self._consumed_amount = consumed_amount

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
        if not isinstance(other, AmountInfomationV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
