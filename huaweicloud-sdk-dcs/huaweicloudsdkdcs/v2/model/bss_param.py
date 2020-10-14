# coding: utf-8

import pprint
import re

import six





class BssParam:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_auto_renew': 'str',
        'charging_mode': 'str',
        'is_auto_pay': 'str',
        'period_type': 'str',
        'period_num': 'int'
    }

    attribute_map = {
        'is_auto_renew': 'is_auto_renew',
        'charging_mode': 'charging_mode',
        'is_auto_pay': 'is_auto_pay',
        'period_type': 'period_type',
        'period_num': 'period_num'
    }

    def __init__(self, is_auto_renew='false', charging_mode='postPaid', is_auto_pay=None, period_type=None, period_num=None):
        """BssParam - a model defined in huaweicloud sdk"""
        
        

        self._is_auto_renew = None
        self._charging_mode = None
        self._is_auto_pay = None
        self._period_type = None
        self._period_num = None
        self.discriminator = None

        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        self.charging_mode = charging_mode
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this BssParam.

        当选择包年包月时，该字段为必选，表示是否自动续订资源。 取值范围： - false：不自动续订； - true：自动续订； 默认值为：false 约束： 如果设置为自动续订，到期后，会自动续订一个月（自动续订时间后续可能会变化），详情可联系客服咨询。 

        :return: The is_auto_renew of this BssParam.
        :rtype: str
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this BssParam.

        当选择包年包月时，该字段为必选，表示是否自动续订资源。 取值范围： - false：不自动续订； - true：自动续订； 默认值为：false 约束： 如果设置为自动续订，到期后，会自动续订一个月（自动续订时间后续可能会变化），详情可联系客服咨询。 

        :param is_auto_renew: The is_auto_renew of this BssParam.
        :type: str
        """
        self._is_auto_renew = is_auto_renew

    @property
    def charging_mode(self):
        """Gets the charging_mode of this BssParam.

        功能说明：付费方式（预付费、按需付费；预付费，即包周期付费）。 取值范围： - prePaid：预付费，即包年包月； - postPaid：后付费，即按需付费； 默认值是postPaid。 后付费的场景下，bss_param参数的其他字段都会被忽略。 

        :return: The charging_mode of this BssParam.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this BssParam.

        功能说明：付费方式（预付费、按需付费；预付费，即包周期付费）。 取值范围： - prePaid：预付费，即包年包月； - postPaid：后付费，即按需付费； 默认值是postPaid。 后付费的场景下，bss_param参数的其他字段都会被忽略。 

        :param charging_mode: The charging_mode of this BssParam.
        :type: str
        """
        self._charging_mode = charging_mode

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this BssParam.

        功能说明：下单订购后，是否自动从客户的账户中支付；默认是“不自动支付” 。  取值范围： - true：是（自动支付，从账户余额自动扣费） - false：否（默认值，只提交订单不支付，需要客户手动去支付）  约束： 自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择不自动支付，然后在用户费用中心，选择代金券支付。  **如果没有设置成自动支付，即设置为false时，在创建实例之后，实例状态为“支付中”，用户必须在“费用中心 > 我的订单”，完成订单支付，否则订单一直在支付中，实例没有创建成功**。 

        :return: The is_auto_pay of this BssParam.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this BssParam.

        功能说明：下单订购后，是否自动从客户的账户中支付；默认是“不自动支付” 。  取值范围： - true：是（自动支付，从账户余额自动扣费） - false：否（默认值，只提交订单不支付，需要客户手动去支付）  约束： 自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择不自动支付，然后在用户费用中心，选择代金券支付。  **如果没有设置成自动支付，即设置为false时，在创建实例之后，实例状态为“支付中”，用户必须在“费用中心 > 我的订单”，完成订单支付，否则订单一直在支付中，实例没有创建成功**。 

        :param is_auto_pay: The is_auto_pay of this BssParam.
        :type: str
        """
        self._is_auto_pay = is_auto_pay

    @property
    def period_type(self):
        """Gets the period_type of this BssParam.

        当选择包年包月时，该字段为必选，表示订购资源的周期类型。  取值范围如下： - month：表示包月 - year：表示包年 

        :return: The period_type of this BssParam.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this BssParam.

        当选择包年包月时，该字段为必选，表示订购资源的周期类型。  取值范围如下： - month：表示包月 - year：表示包年 

        :param period_type: The period_type of this BssParam.
        :type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this BssParam.

        功能说明：订购周期数 取值范围：(后续会随运营策略变化) - period_type为month时，为[1,9]， - period_type为year时，为[1,3]  约束：同period_type约束。 

        :return: The period_num of this BssParam.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this BssParam.

        功能说明：订购周期数 取值范围：(后续会随运营策略变化) - period_type为month时，为[1,9]， - period_type为year时，为[1,3]  约束：同period_type约束。 

        :param period_num: The period_num of this BssParam.
        :type: int
        """
        self._period_num = period_num

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
        if not isinstance(other, BssParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
