# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrepaidCreateOption:

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
        'auto_renew': 'bool',
        'auto_pay': 'bool'
    }

    attribute_map = {
        'period_type': 'period_type',
        'period_num': 'period_num',
        'auto_renew': 'auto_renew',
        'auto_pay': 'auto_pay'
    }

    def __init__(self, period_type=None, period_num=None, auto_renew=None, auto_pay=None):
        r"""PrepaidCreateOption

        The model defined in huaweicloud sdk

        :param period_type: **参数解释**：预付费实例的订购周期类型，当前支持月和年。  **约束限制**：不涉及  **取值范围**：  - month：月  - year：年 **默认取值**：不涉及
        :type period_type: str
        :param period_num: **参数解释**：预付费实例的订购周期数。  **约束限制**：不涉及  **取值范围**： - period_type为month时，为[1,9]。 - period_type为year时，为[1,3]。  **默认取值**：不涉及
        :type period_num: int
        :param auto_renew: **参数解释**：自动续订开关。  **约束限制**：不涉及  **取值范围**： - true：开启自动续订。 - false：关闭自动续订。  **默认取值**：不涉及
        :type auto_renew: bool
        :param auto_pay: **参数解释**：自动支付开关。下单订购后，是否自动从客户的账户中支付。  **约束限制**：开启自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择关闭自动支付，然后在用户费用中心，选择代金券支付。  **取值范围**：  - true：开启自动支付。  - false：关闭自动支付。  **默认取值**：不涉及
        :type auto_pay: bool
        """
        
        

        self._period_type = None
        self._period_num = None
        self._auto_renew = None
        self._auto_pay = None
        self.discriminator = None

        self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if auto_renew is not None:
            self.auto_renew = auto_renew
        if auto_pay is not None:
            self.auto_pay = auto_pay

    @property
    def period_type(self):
        r"""Gets the period_type of this PrepaidCreateOption.

        **参数解释**：预付费实例的订购周期类型，当前支持月和年。  **约束限制**：不涉及  **取值范围**：  - month：月  - year：年 **默认取值**：不涉及

        :return: The period_type of this PrepaidCreateOption.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this PrepaidCreateOption.

        **参数解释**：预付费实例的订购周期类型，当前支持月和年。  **约束限制**：不涉及  **取值范围**：  - month：月  - year：年 **默认取值**：不涉及

        :param period_type: The period_type of this PrepaidCreateOption.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this PrepaidCreateOption.

        **参数解释**：预付费实例的订购周期数。  **约束限制**：不涉及  **取值范围**： - period_type为month时，为[1,9]。 - period_type为year时，为[1,3]。  **默认取值**：不涉及

        :return: The period_num of this PrepaidCreateOption.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this PrepaidCreateOption.

        **参数解释**：预付费实例的订购周期数。  **约束限制**：不涉及  **取值范围**： - period_type为month时，为[1,9]。 - period_type为year时，为[1,3]。  **默认取值**：不涉及

        :param period_num: The period_num of this PrepaidCreateOption.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def auto_renew(self):
        r"""Gets the auto_renew of this PrepaidCreateOption.

        **参数解释**：自动续订开关。  **约束限制**：不涉及  **取值范围**： - true：开启自动续订。 - false：关闭自动续订。  **默认取值**：不涉及

        :return: The auto_renew of this PrepaidCreateOption.
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        r"""Sets the auto_renew of this PrepaidCreateOption.

        **参数解释**：自动续订开关。  **约束限制**：不涉及  **取值范围**： - true：开启自动续订。 - false：关闭自动续订。  **默认取值**：不涉及

        :param auto_renew: The auto_renew of this PrepaidCreateOption.
        :type auto_renew: bool
        """
        self._auto_renew = auto_renew

    @property
    def auto_pay(self):
        r"""Gets the auto_pay of this PrepaidCreateOption.

        **参数解释**：自动支付开关。下单订购后，是否自动从客户的账户中支付。  **约束限制**：开启自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择关闭自动支付，然后在用户费用中心，选择代金券支付。  **取值范围**：  - true：开启自动支付。  - false：关闭自动支付。  **默认取值**：不涉及

        :return: The auto_pay of this PrepaidCreateOption.
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        r"""Sets the auto_pay of this PrepaidCreateOption.

        **参数解释**：自动支付开关。下单订购后，是否自动从客户的账户中支付。  **约束限制**：开启自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择关闭自动支付，然后在用户费用中心，选择代金券支付。  **取值范围**：  - true：开启自动支付。  - false：关闭自动支付。  **默认取值**：不涉及

        :param auto_pay: The auto_pay of this PrepaidCreateOption.
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
        if not isinstance(other, PrepaidCreateOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
