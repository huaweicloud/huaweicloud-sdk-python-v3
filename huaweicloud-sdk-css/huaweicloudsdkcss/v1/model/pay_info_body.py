# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PayInfoBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pay_model': 'int',
        'period': 'int',
        'is_auto_renew': 'int',
        'is_auto_pay': 'int'
    }

    attribute_map = {
        'pay_model': 'payModel',
        'period': 'period',
        'is_auto_renew': 'isAutoRenew',
        'is_auto_pay': 'isAutoPay'
    }

    def __init__(self, pay_model=None, period=None, is_auto_renew=None, is_auto_pay=None):
        """PayInfoBody

        The model defined in huaweicloud sdk

        :param pay_model: 订购周期类型。 - 2: 包月。 - 3: 包年。
        :type pay_model: int
        :param period: 订购周期数。 - 若payModel为2，则有效值为1-9。 - 若payModel为3，则有效值为1-3。
        :type period: int
        :param is_auto_renew: 是否自动续订，为空时表示不自动续订。 - 1: 自动续订。 - 2：不自动续订（默认）。
        :type is_auto_renew: int
        :param is_auto_pay:  是否自动支付。下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。该参数适用于包周期集群。   - 1:是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券)。   - 0: 否（需要客户手动去支付，客户可以选择折扣和优惠券）。默认值为“0”。
        :type is_auto_pay: int
        """
        
        

        self._pay_model = None
        self._period = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self.discriminator = None

        self.pay_model = pay_model
        self.period = period
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def pay_model(self):
        """Gets the pay_model of this PayInfoBody.

        订购周期类型。 - 2: 包月。 - 3: 包年。

        :return: The pay_model of this PayInfoBody.
        :rtype: int
        """
        return self._pay_model

    @pay_model.setter
    def pay_model(self, pay_model):
        """Sets the pay_model of this PayInfoBody.

        订购周期类型。 - 2: 包月。 - 3: 包年。

        :param pay_model: The pay_model of this PayInfoBody.
        :type pay_model: int
        """
        self._pay_model = pay_model

    @property
    def period(self):
        """Gets the period of this PayInfoBody.

        订购周期数。 - 若payModel为2，则有效值为1-9。 - 若payModel为3，则有效值为1-3。

        :return: The period of this PayInfoBody.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this PayInfoBody.

        订购周期数。 - 若payModel为2，则有效值为1-9。 - 若payModel为3，则有效值为1-3。

        :param period: The period of this PayInfoBody.
        :type period: int
        """
        self._period = period

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this PayInfoBody.

        是否自动续订，为空时表示不自动续订。 - 1: 自动续订。 - 2：不自动续订（默认）。

        :return: The is_auto_renew of this PayInfoBody.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this PayInfoBody.

        是否自动续订，为空时表示不自动续订。 - 1: 自动续订。 - 2：不自动续订（默认）。

        :param is_auto_renew: The is_auto_renew of this PayInfoBody.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this PayInfoBody.

         是否自动支付。下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。该参数适用于包周期集群。   - 1:是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券)。   - 0: 否（需要客户手动去支付，客户可以选择折扣和优惠券）。默认值为“0”。

        :return: The is_auto_pay of this PayInfoBody.
        :rtype: int
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this PayInfoBody.

         是否自动支付。下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。该参数适用于包周期集群。   - 1:是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券)。   - 0: 否（需要客户手动去支付，客户可以选择折扣和优惠券）。默认值为“0”。

        :param is_auto_pay: The is_auto_pay of this PayInfoBody.
        :type is_auto_pay: int
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, PayInfoBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
