# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'is_auto_renew': 'bool',
        'charging_mode': 'str',
        'is_auto_pay': 'bool',
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

    def __init__(self, is_auto_renew=None, charging_mode=None, is_auto_pay=None, period_type=None, period_num=None):
        r"""BssParam

        The model defined in huaweicloud sdk

        :param is_auto_renew: **参数解释**： 是否自动续订。 **约束限制**： 不涉及。 **取值范围**： - true：自动续订。 - false：不自动续订。 **默认取值**： false
        :type is_auto_renew: bool
        :param charging_mode: **参数解释**： 计费模式。 **约束限制**： 不涉及。 **取值范围**： - prePaid：预付费，即包年包月。 - postPaid：后付费，即按需付费。 **默认取值**： postPaid。
        :type charging_mode: str
        :param is_auto_pay: **参数解释**： 下单订购后，是否自动从客户的账户中支付，而不需要客户手动去进行支付。 **约束限制**： 不涉及。 **取值范围**： - true：是（自动支付） - false：否（需要客户手动支付） **默认取值**： false
        :type is_auto_pay: bool
        :param period_type: **参数解释**： 订购周期类型。 **约束限制**： chargingMode为prePaid时生效且为必选值。 **取值范围**： - month：月。 - year：年。 **默认取值**： 不涉及。
        :type period_type: str
        :param period_num: **参数解释**： 订购周期数。 **约束限制**： chargingMode为prePaid时生效且为必选值。 **取值范围**： - periodType&#x3D;month（周期类型为月）时，取值为[1，9]。 - periodType&#x3D;year（周期类型为年）时，取值为[1，3]。 **默认取值**： 不涉及。
        :type period_num: int
        """
        
        

        self._is_auto_renew = None
        self._charging_mode = None
        self._is_auto_pay = None
        self._period_type = None
        self._period_num = None
        self.discriminator = None

        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this BssParam.

        **参数解释**： 是否自动续订。 **约束限制**： 不涉及。 **取值范围**： - true：自动续订。 - false：不自动续订。 **默认取值**： false

        :return: The is_auto_renew of this BssParam.
        :rtype: bool
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this BssParam.

        **参数解释**： 是否自动续订。 **约束限制**： 不涉及。 **取值范围**： - true：自动续订。 - false：不自动续订。 **默认取值**： false

        :param is_auto_renew: The is_auto_renew of this BssParam.
        :type is_auto_renew: bool
        """
        self._is_auto_renew = is_auto_renew

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this BssParam.

        **参数解释**： 计费模式。 **约束限制**： 不涉及。 **取值范围**： - prePaid：预付费，即包年包月。 - postPaid：后付费，即按需付费。 **默认取值**： postPaid。

        :return: The charging_mode of this BssParam.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this BssParam.

        **参数解释**： 计费模式。 **约束限制**： 不涉及。 **取值范围**： - prePaid：预付费，即包年包月。 - postPaid：后付费，即按需付费。 **默认取值**： postPaid。

        :param charging_mode: The charging_mode of this BssParam.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this BssParam.

        **参数解释**： 下单订购后，是否自动从客户的账户中支付，而不需要客户手动去进行支付。 **约束限制**： 不涉及。 **取值范围**： - true：是（自动支付） - false：否（需要客户手动支付） **默认取值**： false

        :return: The is_auto_pay of this BssParam.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this BssParam.

        **参数解释**： 下单订购后，是否自动从客户的账户中支付，而不需要客户手动去进行支付。 **约束限制**： 不涉及。 **取值范围**： - true：是（自动支付） - false：否（需要客户手动支付） **默认取值**： false

        :param is_auto_pay: The is_auto_pay of this BssParam.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def period_type(self):
        r"""Gets the period_type of this BssParam.

        **参数解释**： 订购周期类型。 **约束限制**： chargingMode为prePaid时生效且为必选值。 **取值范围**： - month：月。 - year：年。 **默认取值**： 不涉及。

        :return: The period_type of this BssParam.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this BssParam.

        **参数解释**： 订购周期类型。 **约束限制**： chargingMode为prePaid时生效且为必选值。 **取值范围**： - month：月。 - year：年。 **默认取值**： 不涉及。

        :param period_type: The period_type of this BssParam.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this BssParam.

        **参数解释**： 订购周期数。 **约束限制**： chargingMode为prePaid时生效且为必选值。 **取值范围**： - periodType=month（周期类型为月）时，取值为[1，9]。 - periodType=year（周期类型为年）时，取值为[1，3]。 **默认取值**： 不涉及。

        :return: The period_num of this BssParam.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this BssParam.

        **参数解释**： 订购周期数。 **约束限制**： chargingMode为prePaid时生效且为必选值。 **取值范围**： - periodType=month（周期类型为月）时，取值为[1，9]。 - periodType=year（周期类型为年）时，取值为[1，3]。 **默认取值**： 不涉及。

        :param period_num: The period_num of this BssParam.
        :type period_num: int
        """
        self._period_num = period_num

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
        if not isinstance(other, BssParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
