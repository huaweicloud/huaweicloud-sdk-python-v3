# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PeriodOrderParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_auto_pay': 'bool',
        'is_auto_renew': 'bool',
        'period_num': 'int',
        'period_type': 'str'
    }

    attribute_map = {
        'is_auto_pay': 'isAutoPay',
        'is_auto_renew': 'isAutoRenew',
        'period_num': 'periodNum',
        'period_type': 'periodType'
    }

    def __init__(self, is_auto_pay=None, is_auto_renew=None, period_num=None, period_type=None):
        r"""PeriodOrderParam

        The model defined in huaweicloud sdk

        :param is_auto_pay: **参数解释**： 是否自动支付订单费用 **约束限制**： 不涉及 **取值范围**： - true：自动支付 - false：手动支付 **默认取值**： false
        :type is_auto_pay: bool
        :param is_auto_renew: **参数解释**： 是否自动续费 **约束限制**： 不涉及 **取值范围**： - true：自动续费 - false：不自动续费 **默认取值**： false
        :type is_auto_renew: bool
        :param period_num: **参数解释**： 包周期时间长度，不同局点、不同产品规格支持的范围可能不同，大部分局点支持：1-9月，1-3年，具体以接口返回为准。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type period_num: int
        :param period_type: **参数解释**： 包周期单位 **约束限制**： 不涉及 **取值范围**： - \&quot;month\&quot;：月 - \&quot;year\&quot;：年 **默认取值**： 不涉及
        :type period_type: str
        """
        
        

        self._is_auto_pay = None
        self._is_auto_renew = None
        self._period_num = None
        self._period_type = None
        self.discriminator = None

        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        self.period_num = period_num
        self.period_type = period_type

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this PeriodOrderParam.

        **参数解释**： 是否自动支付订单费用 **约束限制**： 不涉及 **取值范围**： - true：自动支付 - false：手动支付 **默认取值**： false

        :return: The is_auto_pay of this PeriodOrderParam.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this PeriodOrderParam.

        **参数解释**： 是否自动支付订单费用 **约束限制**： 不涉及 **取值范围**： - true：自动支付 - false：手动支付 **默认取值**： false

        :param is_auto_pay: The is_auto_pay of this PeriodOrderParam.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this PeriodOrderParam.

        **参数解释**： 是否自动续费 **约束限制**： 不涉及 **取值范围**： - true：自动续费 - false：不自动续费 **默认取值**： false

        :return: The is_auto_renew of this PeriodOrderParam.
        :rtype: bool
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this PeriodOrderParam.

        **参数解释**： 是否自动续费 **约束限制**： 不涉及 **取值范围**： - true：自动续费 - false：不自动续费 **默认取值**： false

        :param is_auto_renew: The is_auto_renew of this PeriodOrderParam.
        :type is_auto_renew: bool
        """
        self._is_auto_renew = is_auto_renew

    @property
    def period_num(self):
        r"""Gets the period_num of this PeriodOrderParam.

        **参数解释**： 包周期时间长度，不同局点、不同产品规格支持的范围可能不同，大部分局点支持：1-9月，1-3年，具体以接口返回为准。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The period_num of this PeriodOrderParam.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this PeriodOrderParam.

        **参数解释**： 包周期时间长度，不同局点、不同产品规格支持的范围可能不同，大部分局点支持：1-9月，1-3年，具体以接口返回为准。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param period_num: The period_num of this PeriodOrderParam.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def period_type(self):
        r"""Gets the period_type of this PeriodOrderParam.

        **参数解释**： 包周期单位 **约束限制**： 不涉及 **取值范围**： - \"month\"：月 - \"year\"：年 **默认取值**： 不涉及

        :return: The period_type of this PeriodOrderParam.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this PeriodOrderParam.

        **参数解释**： 包周期单位 **约束限制**： 不涉及 **取值范围**： - \"month\"：月 - \"year\"：年 **默认取值**： 不涉及

        :param period_type: The period_type of this PeriodOrderParam.
        :type period_type: str
        """
        self._period_type = period_type

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
        if not isinstance(other, PeriodOrderParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
