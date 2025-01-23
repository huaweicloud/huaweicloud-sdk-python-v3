# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradePrepaidOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period_type': 'str',
        'period_num': 'int',
        'resource_package_type': 'list[str]',
        'auto_pay': 'bool'
    }

    attribute_map = {
        'period_type': 'period_type',
        'period_num': 'period_num',
        'resource_package_type': 'resource_package_type',
        'auto_pay': 'auto_pay'
    }

    def __init__(self, period_type=None, period_num=None, resource_package_type=None, auto_pay=None):
        """UpgradePrepaidOption

        The model defined in huaweicloud sdk

        :param period_type: 参数解释：预付费实例的订购周期类型，当前支持月和年。  取值范围：  - month：月。  - year：年。
        :type period_type: str
        :param period_num: 参数解释：预付费实例的订购周期数。  取值范围： - period_type为month时，为[1,9]。 - period_type为year时，为[1,3]。
        :type period_num: int
        :param resource_package_type: 参数解释：购买定向套餐包。
        :type resource_package_type: list[str]
        :param auto_pay: 参数解释：自动支付开关。下单订购后，是否自动从客户的账户中支付。  约束限制：开启自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择关闭自动支付，然后在用户费用中心，选择代金券支付。  取值范围：  - true：开启自动支付。  - false：关闭自动支付。
        :type auto_pay: bool
        """
        
        

        self._period_type = None
        self._period_num = None
        self._resource_package_type = None
        self._auto_pay = None
        self.discriminator = None

        self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        self.resource_package_type = resource_package_type
        if auto_pay is not None:
            self.auto_pay = auto_pay

    @property
    def period_type(self):
        """Gets the period_type of this UpgradePrepaidOption.

        参数解释：预付费实例的订购周期类型，当前支持月和年。  取值范围：  - month：月。  - year：年。

        :return: The period_type of this UpgradePrepaidOption.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this UpgradePrepaidOption.

        参数解释：预付费实例的订购周期类型，当前支持月和年。  取值范围：  - month：月。  - year：年。

        :param period_type: The period_type of this UpgradePrepaidOption.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this UpgradePrepaidOption.

        参数解释：预付费实例的订购周期数。  取值范围： - period_type为month时，为[1,9]。 - period_type为year时，为[1,3]。

        :return: The period_num of this UpgradePrepaidOption.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this UpgradePrepaidOption.

        参数解释：预付费实例的订购周期数。  取值范围： - period_type为month时，为[1,9]。 - period_type为year时，为[1,3]。

        :param period_num: The period_num of this UpgradePrepaidOption.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def resource_package_type(self):
        """Gets the resource_package_type of this UpgradePrepaidOption.

        参数解释：购买定向套餐包。

        :return: The resource_package_type of this UpgradePrepaidOption.
        :rtype: list[str]
        """
        return self._resource_package_type

    @resource_package_type.setter
    def resource_package_type(self, resource_package_type):
        """Sets the resource_package_type of this UpgradePrepaidOption.

        参数解释：购买定向套餐包。

        :param resource_package_type: The resource_package_type of this UpgradePrepaidOption.
        :type resource_package_type: list[str]
        """
        self._resource_package_type = resource_package_type

    @property
    def auto_pay(self):
        """Gets the auto_pay of this UpgradePrepaidOption.

        参数解释：自动支付开关。下单订购后，是否自动从客户的账户中支付。  约束限制：开启自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择关闭自动支付，然后在用户费用中心，选择代金券支付。  取值范围：  - true：开启自动支付。  - false：关闭自动支付。

        :return: The auto_pay of this UpgradePrepaidOption.
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        """Sets the auto_pay of this UpgradePrepaidOption.

        参数解释：自动支付开关。下单订购后，是否自动从客户的账户中支付。  约束限制：开启自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择关闭自动支付，然后在用户费用中心，选择代金券支付。  取值范围：  - true：开启自动支付。  - false：关闭自动支付。

        :param auto_pay: The auto_pay of this UpgradePrepaidOption.
        :type auto_pay: bool
        """
        self._auto_pay = auto_pay

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
        if not isinstance(other, UpgradePrepaidOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
