# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChargeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charge_mode': 'str',
        'period_type': 'str',
        'period_num': 'int',
        'is_auto_pay': 'bool'
    }

    attribute_map = {
        'charge_mode': 'charge_mode',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, charge_mode=None, period_type=None, period_num=None, is_auto_pay=None):
        """ChargeInfo

        The model defined in huaweicloud sdk

        :param charge_mode: 计费模式。 取值范围： - prePaid：预付费，即包年/包月。（创建集群接口现已支持预付费，创建集群并提交作业接口暂不支持预付费。） - postPaid：后付费，即按需计费。
        :type charge_mode: str
        :param period_type: 周期类型。取值范围： - month：包月。 - year： 包年。 - day：按需计费。
        :type period_type: str
        :param period_num: 周期数，“charge_mode”为“prePaid”时生效，且为必选值，指定订购的时间。取值范围： - 当“period_type”为“month”时，取值为1~9。 - 当“period_type”为“year”时，取值为1~3。
        :type period_num: int
        :param is_auto_pay: 是否自动支付，包周期模式下使用，下单订购后，是否自动从客户的账户中支付，而不需要客户手动去进行支付，默认为手动支付。取值范围： - true：自动支付，会自动选择折扣和优惠券进行优惠，然后自动从客户账户中支付，自动支付失败后会生成订单成功、但订单状态为“待支付”，等待客户手动支付。 - false：手动支付，需要客户手动去支付，客户可以选择折扣和优惠券。
        :type is_auto_pay: bool
        """
        
        

        self._charge_mode = None
        self._period_type = None
        self._period_num = None
        self._is_auto_pay = None
        self.discriminator = None

        self.charge_mode = charge_mode
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ChargeInfo.

        计费模式。 取值范围： - prePaid：预付费，即包年/包月。（创建集群接口现已支持预付费，创建集群并提交作业接口暂不支持预付费。） - postPaid：后付费，即按需计费。

        :return: The charge_mode of this ChargeInfo.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ChargeInfo.

        计费模式。 取值范围： - prePaid：预付费，即包年/包月。（创建集群接口现已支持预付费，创建集群并提交作业接口暂不支持预付费。） - postPaid：后付费，即按需计费。

        :param charge_mode: The charge_mode of this ChargeInfo.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def period_type(self):
        """Gets the period_type of this ChargeInfo.

        周期类型。取值范围： - month：包月。 - year： 包年。 - day：按需计费。

        :return: The period_type of this ChargeInfo.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this ChargeInfo.

        周期类型。取值范围： - month：包月。 - year： 包年。 - day：按需计费。

        :param period_type: The period_type of this ChargeInfo.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this ChargeInfo.

        周期数，“charge_mode”为“prePaid”时生效，且为必选值，指定订购的时间。取值范围： - 当“period_type”为“month”时，取值为1~9。 - 当“period_type”为“year”时，取值为1~3。

        :return: The period_num of this ChargeInfo.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this ChargeInfo.

        周期数，“charge_mode”为“prePaid”时生效，且为必选值，指定订购的时间。取值范围： - 当“period_type”为“month”时，取值为1~9。 - 当“period_type”为“year”时，取值为1~3。

        :param period_num: The period_num of this ChargeInfo.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this ChargeInfo.

        是否自动支付，包周期模式下使用，下单订购后，是否自动从客户的账户中支付，而不需要客户手动去进行支付，默认为手动支付。取值范围： - true：自动支付，会自动选择折扣和优惠券进行优惠，然后自动从客户账户中支付，自动支付失败后会生成订单成功、但订单状态为“待支付”，等待客户手动支付。 - false：手动支付，需要客户手动去支付，客户可以选择折扣和优惠券。

        :return: The is_auto_pay of this ChargeInfo.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this ChargeInfo.

        是否自动支付，包周期模式下使用，下单订购后，是否自动从客户的账户中支付，而不需要客户手动去进行支付，默认为手动支付。取值范围： - true：自动支付，会自动选择折扣和优惠券进行优惠，然后自动从客户账户中支付，自动支付失败后会生成订单成功、但订单状态为“待支付”，等待客户手动支付。 - false：手动支付，需要客户手动去支付，客户可以选择折扣和优惠券。

        :param is_auto_pay: The is_auto_pay of this ChargeInfo.
        :type is_auto_pay: bool
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
        if not isinstance(other, ChargeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
