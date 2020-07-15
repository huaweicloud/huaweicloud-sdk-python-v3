# coding: utf-8

import pprint
import re

import six





class BssParamForCreateVolume:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'charging_mode': 'str',
        'is_auto_pay': 'str',
        'is_auto_renew': 'str',
        'period_num': 'int',
        'period_type': 'str'
    }

    attribute_map = {
        'charging_mode': 'chargingMode',
        'is_auto_pay': 'isAutoPay',
        'is_auto_renew': 'isAutoRenew',
        'period_num': 'periodNum',
        'period_type': 'periodType'
    }

    def __init__(self, charging_mode='postPaid', is_auto_pay='false', is_auto_renew='false', period_num=None, period_type=None):
        """BssParamForCreateVolume - a model defined in huaweicloud sdk"""
        
        

        self._charging_mode = None
        self._is_auto_pay = None
        self._is_auto_renew = None
        self._period_num = None
        self._period_type = None
        self.discriminator = None

        if charging_mode is not None:
            self.charging_mode = charging_mode
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if period_num is not None:
            self.period_num = period_num
        if period_type is not None:
            self.period_type = period_type

    @property
    def charging_mode(self):
        """Gets the charging_mode of this BssParamForCreateVolume.

        功能说明：计费模式。默认值为postPaid。 取值范围： * prePaid：包年包月 * postPaid：按需

        :return: The charging_mode of this BssParamForCreateVolume.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this BssParamForCreateVolume.

        功能说明：计费模式。默认值为postPaid。 取值范围： * prePaid：包年包月 * postPaid：按需

        :param charging_mode: The charging_mode of this BssParamForCreateVolume.
        :type: str
        """
        self._charging_mode = charging_mode

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this BssParamForCreateVolume.

        功能说明：是否立即支付。chargingMode为PrePaid时该参数会生效。默认值为false。 取值范围： * true：立即支付，从帐户余额中自动扣费 * false：不立即支付，创建订单暂不支付 

        :return: The is_auto_pay of this BssParamForCreateVolume.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this BssParamForCreateVolume.

        功能说明：是否立即支付。chargingMode为PrePaid时该参数会生效。默认值为false。 取值范围： * true：立即支付，从帐户余额中自动扣费 * false：不立即支付，创建订单暂不支付 

        :param is_auto_pay: The is_auto_pay of this BssParamForCreateVolume.
        :type: str
        """
        self._is_auto_pay = is_auto_pay

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this BssParamForCreateVolume.

        功能说明：是否自动续订。chargingMode为prePaid时该参数会生效。默认值为false。 取值范围： * true：自动续订，自动续订周期与订购周期相同 * false：不自动续订 

        :return: The is_auto_renew of this BssParamForCreateVolume.
        :rtype: str
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this BssParamForCreateVolume.

        功能说明：是否自动续订。chargingMode为prePaid时该参数会生效。默认值为false。 取值范围： * true：自动续订，自动续订周期与订购周期相同 * false：不自动续订 

        :param is_auto_renew: The is_auto_renew of this BssParamForCreateVolume.
        :type: str
        """
        self._is_auto_renew = is_auto_renew

    @property
    def period_num(self):
        """Gets the period_num of this BssParamForCreateVolume.

        功能说明：订购周期数，chargingMode为prePaid时该参数会生效，并且该参数为为必选。 取值范围： * periodType为month时，为[1-9] * periodType为year时，为[1-1]

        :return: The period_num of this BssParamForCreateVolume.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this BssParamForCreateVolume.

        功能说明：订购周期数，chargingMode为prePaid时该参数会生效，并且该参数为为必选。 取值范围： * periodType为month时，为[1-9] * periodType为year时，为[1-1]

        :param period_num: The period_num of this BssParamForCreateVolume.
        :type: int
        """
        self._period_num = period_num

    @property
    def period_type(self):
        """Gets the period_type of this BssParamForCreateVolume.

        功能说明：订购周期单位。chargingMode为prePaid时该参数会生效，并且该参数为必选。 取值范围： * month：月 * year：年

        :return: The period_type of this BssParamForCreateVolume.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this BssParamForCreateVolume.

        功能说明：订购周期单位。chargingMode为prePaid时该参数会生效，并且该参数为必选。 取值范围： * month：月 * year：年

        :param period_type: The period_type of this BssParamForCreateVolume.
        :type: str
        """
        self._period_type = period_type

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BssParamForCreateVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
