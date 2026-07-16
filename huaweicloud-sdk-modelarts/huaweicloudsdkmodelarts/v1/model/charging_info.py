# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChargingInfo:

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
        'is_auto_pay': 'bool',
        'is_auto_renew': 'bool',
        'period_num': 'int',
        'period_type': 'str'
    }

    attribute_map = {
        'charging_mode': 'charging_mode',
        'is_auto_pay': 'is_auto_pay',
        'is_auto_renew': 'is_auto_renew',
        'period_num': 'period_num',
        'period_type': 'period_type'
    }

    def __init__(self, charging_mode=None, is_auto_pay=None, is_auto_renew=None, period_num=None, period_type=None):
        r"""ChargingInfo

        The model defined in huaweicloud sdk

        :param charging_mode: **参数解释**：付费类型。表示服务器的计费模式。 **约束限制**：不涉及。 **取值范围**： - COMMON：同时支持包周期和按需 - POST_PAID：后付费 - PRE_PAID：预付费 **默认取值**：不涉及。
        :type charging_mode: str
        :param is_auto_pay: **参数解释**：是否自动支付。表示是否开启自动支付功能。 **约束限制**：不涉及。 **取值范围**： - true：自动支付 - false：不自动支付 **默认取值**：不涉及。
        :type is_auto_pay: bool
        :param is_auto_renew: **参数解释**：是否自动续订。表示是否开启自动续订功能。 **约束限制**：不涉及。 **取值范围**： - true：自动续订 - false：不自动续订 **默认取值**：不涉及。
        :type is_auto_renew: bool
        :param period_num: **参数解释**：订购周期数量。表示订购周期的数量。 **约束限制**：不涉及。 **取值范围**：1 - 11 **默认取值**：不涉及。
        :type period_num: int
        :param period_type: **参数解释**：订购周期类型。表示订购周期的时间单位。 **约束限制**：不涉及。 **取值范围**： - ABSOLUTE - DAY：天 - HOUR：小时 - MONTH：月 - WEEK：周 - YEAR：年 **默认取值**：不涉及。
        :type period_type: str
        """
        
        

        self._charging_mode = None
        self._is_auto_pay = None
        self._is_auto_renew = None
        self._period_num = None
        self._period_type = None
        self.discriminator = None

        self.charging_mode = charging_mode
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        self.period_num = period_num
        self.period_type = period_type

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ChargingInfo.

        **参数解释**：付费类型。表示服务器的计费模式。 **约束限制**：不涉及。 **取值范围**： - COMMON：同时支持包周期和按需 - POST_PAID：后付费 - PRE_PAID：预付费 **默认取值**：不涉及。

        :return: The charging_mode of this ChargingInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ChargingInfo.

        **参数解释**：付费类型。表示服务器的计费模式。 **约束限制**：不涉及。 **取值范围**： - COMMON：同时支持包周期和按需 - POST_PAID：后付费 - PRE_PAID：预付费 **默认取值**：不涉及。

        :param charging_mode: The charging_mode of this ChargingInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this ChargingInfo.

        **参数解释**：是否自动支付。表示是否开启自动支付功能。 **约束限制**：不涉及。 **取值范围**： - true：自动支付 - false：不自动支付 **默认取值**：不涉及。

        :return: The is_auto_pay of this ChargingInfo.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this ChargingInfo.

        **参数解释**：是否自动支付。表示是否开启自动支付功能。 **约束限制**：不涉及。 **取值范围**： - true：自动支付 - false：不自动支付 **默认取值**：不涉及。

        :param is_auto_pay: The is_auto_pay of this ChargingInfo.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this ChargingInfo.

        **参数解释**：是否自动续订。表示是否开启自动续订功能。 **约束限制**：不涉及。 **取值范围**： - true：自动续订 - false：不自动续订 **默认取值**：不涉及。

        :return: The is_auto_renew of this ChargingInfo.
        :rtype: bool
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this ChargingInfo.

        **参数解释**：是否自动续订。表示是否开启自动续订功能。 **约束限制**：不涉及。 **取值范围**： - true：自动续订 - false：不自动续订 **默认取值**：不涉及。

        :param is_auto_renew: The is_auto_renew of this ChargingInfo.
        :type is_auto_renew: bool
        """
        self._is_auto_renew = is_auto_renew

    @property
    def period_num(self):
        r"""Gets the period_num of this ChargingInfo.

        **参数解释**：订购周期数量。表示订购周期的数量。 **约束限制**：不涉及。 **取值范围**：1 - 11 **默认取值**：不涉及。

        :return: The period_num of this ChargingInfo.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this ChargingInfo.

        **参数解释**：订购周期数量。表示订购周期的数量。 **约束限制**：不涉及。 **取值范围**：1 - 11 **默认取值**：不涉及。

        :param period_num: The period_num of this ChargingInfo.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def period_type(self):
        r"""Gets the period_type of this ChargingInfo.

        **参数解释**：订购周期类型。表示订购周期的时间单位。 **约束限制**：不涉及。 **取值范围**： - ABSOLUTE - DAY：天 - HOUR：小时 - MONTH：月 - WEEK：周 - YEAR：年 **默认取值**：不涉及。

        :return: The period_type of this ChargingInfo.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this ChargingInfo.

        **参数解释**：订购周期类型。表示订购周期的时间单位。 **约束限制**：不涉及。 **取值范围**： - ABSOLUTE - DAY：天 - HOUR：小时 - MONTH：月 - WEEK：周 - YEAR：年 **默认取值**：不涉及。

        :param period_type: The period_type of this ChargingInfo.
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
        if not isinstance(other, ChargingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
