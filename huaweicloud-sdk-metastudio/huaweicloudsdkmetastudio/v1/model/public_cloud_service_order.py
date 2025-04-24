# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicCloudServiceOrder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_auto_pay': 'int',
        'period_type': 'int',
        'period_num': 'int',
        'is_auto_renew': 'int',
        'subscription_num': 'int',
        'resource_spec_code': 'str'
    }

    attribute_map = {
        'is_auto_pay': 'is_auto_pay',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew',
        'subscription_num': 'subscription_num',
        'resource_spec_code': 'resource_spec_code'
    }

    def __init__(self, is_auto_pay=None, period_type=None, period_num=None, is_auto_renew=None, subscription_num=None, resource_spec_code=None):
        r"""PublicCloudServiceOrder

        The model defined in huaweicloud sdk

        :param is_auto_pay: 是否自动支付：下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付；  1：是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券)。 0：否（需要客户手动去支付，客户可以选择折扣和优惠券）。 默认值为“0”。
        :type is_auto_pay: int
        :param period_type: 订购周期类型： 2：月； 3：年； 6：一次性;
        :type period_type: int
        :param period_num: 订购周期数 取值大于0；小于等于0会报错
        :type period_num: int
        :param is_auto_renew: 是否自动续订，为空时表示不自动续订； 1：自动续订 0：不自动续订（默认）
        :type is_auto_renew: int
        :param subscription_num: 订购数量； 取值大于0
        :type subscription_num: int
        :param resource_spec_code: 用户购买云服务产品的资源规格，详见[资源类型](metastudio_02_0042.xml)。
        :type resource_spec_code: str
        """
        
        

        self._is_auto_pay = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._subscription_num = None
        self._resource_spec_code = None
        self.discriminator = None

        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        self.period_type = period_type
        self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        self.subscription_num = subscription_num
        self.resource_spec_code = resource_spec_code

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this PublicCloudServiceOrder.

        是否自动支付：下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付；  1：是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券)。 0：否（需要客户手动去支付，客户可以选择折扣和优惠券）。 默认值为“0”。

        :return: The is_auto_pay of this PublicCloudServiceOrder.
        :rtype: int
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this PublicCloudServiceOrder.

        是否自动支付：下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付；  1：是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券)。 0：否（需要客户手动去支付，客户可以选择折扣和优惠券）。 默认值为“0”。

        :param is_auto_pay: The is_auto_pay of this PublicCloudServiceOrder.
        :type is_auto_pay: int
        """
        self._is_auto_pay = is_auto_pay

    @property
    def period_type(self):
        r"""Gets the period_type of this PublicCloudServiceOrder.

        订购周期类型： 2：月； 3：年； 6：一次性;

        :return: The period_type of this PublicCloudServiceOrder.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this PublicCloudServiceOrder.

        订购周期类型： 2：月； 3：年； 6：一次性;

        :param period_type: The period_type of this PublicCloudServiceOrder.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this PublicCloudServiceOrder.

        订购周期数 取值大于0；小于等于0会报错

        :return: The period_num of this PublicCloudServiceOrder.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this PublicCloudServiceOrder.

        订购周期数 取值大于0；小于等于0会报错

        :param period_num: The period_num of this PublicCloudServiceOrder.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this PublicCloudServiceOrder.

        是否自动续订，为空时表示不自动续订； 1：自动续订 0：不自动续订（默认）

        :return: The is_auto_renew of this PublicCloudServiceOrder.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this PublicCloudServiceOrder.

        是否自动续订，为空时表示不自动续订； 1：自动续订 0：不自动续订（默认）

        :param is_auto_renew: The is_auto_renew of this PublicCloudServiceOrder.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def subscription_num(self):
        r"""Gets the subscription_num of this PublicCloudServiceOrder.

        订购数量； 取值大于0

        :return: The subscription_num of this PublicCloudServiceOrder.
        :rtype: int
        """
        return self._subscription_num

    @subscription_num.setter
    def subscription_num(self, subscription_num):
        r"""Sets the subscription_num of this PublicCloudServiceOrder.

        订购数量； 取值大于0

        :param subscription_num: The subscription_num of this PublicCloudServiceOrder.
        :type subscription_num: int
        """
        self._subscription_num = subscription_num

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this PublicCloudServiceOrder.

        用户购买云服务产品的资源规格，详见[资源类型](metastudio_02_0042.xml)。

        :return: The resource_spec_code of this PublicCloudServiceOrder.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this PublicCloudServiceOrder.

        用户购买云服务产品的资源规格，详见[资源类型](metastudio_02_0042.xml)。

        :param resource_spec_code: The resource_spec_code of this PublicCloudServiceOrder.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

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
        if not isinstance(other, PublicCloudServiceOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
