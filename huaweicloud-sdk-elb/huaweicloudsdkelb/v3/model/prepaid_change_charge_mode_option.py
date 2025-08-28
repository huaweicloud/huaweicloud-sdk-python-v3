# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrepaidChangeChargeModeOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'include_publicip': 'bool',
        'publicip_ids': 'list[str]',
        'period_type': 'str',
        'period_num': 'int',
        'auto_renew': 'bool',
        'auto_pay': 'bool'
    }

    attribute_map = {
        'include_publicip': 'include_publicip',
        'publicip_ids': 'publicip_ids',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'auto_renew': 'auto_renew',
        'auto_pay': 'auto_pay'
    }

    def __init__(self, include_publicip=None, publicip_ids=None, period_type=None, period_num=None, auto_renew=None, auto_pay=None):
        r"""PrepaidChangeChargeModeOption

        The model defined in huaweicloud sdk

        :param include_publicip: **参数解释**：是否连同独享按带宽计费的弹性公网IP一起转包周期。 弹性公网IP转包周期之后可以单独解绑、绑定到其他实例和删除EIP。  **约束限制**：只有独享且按带宽计费的弹性公网IP才被允许转包周期。  **取值范围**： - true：连同EIP一起转包周期。 - false：仅转ELB，不转EIP。  **默认取值**：false
        :type include_publicip: bool
        :param publicip_ids: **参数解释**：需要一起按需转包的弹性公网IP的ID。  **约束限制**： - 若include_publicip为false，不能指定该字段。 - 若include_publicip为true，该字段为未指定时，表示所有绑定的v4 eip都需要一起转包周期。 - 若include_publicip为true，该字段列表非空，表示只将指定的v4 eip转包。 - 若include_publicip为true，该字段列表为空，表示不指定任一eip转包，与include_publicip为false等效。  **取值范围**：不涉及  **默认取值**：不涉及
        :type publicip_ids: list[str]
        :param period_type: **参数解释**：订购周期类型。  **约束限制**：不涉及  **取值范围**： - month：月 - year：年  **默认取值**：month
        :type period_type: str
        :param period_num: **参数解释**：订购周期数，取值会随运营策略变化。  **约束限制**：不涉及  **取值范围**： - period_type为month时，为[1,9] - period_type为year时，为[1,3]  **默认取值**：1
        :type period_num: int
        :param auto_renew: **参数解释**：是否自动续订。  **约束限制**：不涉及  **取值范围**： - true：自动续订。 - false：不自动续订。  **默认取值**：false
        :type auto_renew: bool
        :param auto_pay: **参数解释**：下单订购后，是否自动从客户的账户中支付。  **约束限制**：自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择不自动支付，然后在用户费用中心，选择代金券支付。  **取值范围**： - true：自动支付。 - false：不自动支付。  **默认取值**：false
        :type auto_pay: bool
        """
        
        

        self._include_publicip = None
        self._publicip_ids = None
        self._period_type = None
        self._period_num = None
        self._auto_renew = None
        self._auto_pay = None
        self.discriminator = None

        if include_publicip is not None:
            self.include_publicip = include_publicip
        if publicip_ids is not None:
            self.publicip_ids = publicip_ids
        self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if auto_renew is not None:
            self.auto_renew = auto_renew
        if auto_pay is not None:
            self.auto_pay = auto_pay

    @property
    def include_publicip(self):
        r"""Gets the include_publicip of this PrepaidChangeChargeModeOption.

        **参数解释**：是否连同独享按带宽计费的弹性公网IP一起转包周期。 弹性公网IP转包周期之后可以单独解绑、绑定到其他实例和删除EIP。  **约束限制**：只有独享且按带宽计费的弹性公网IP才被允许转包周期。  **取值范围**： - true：连同EIP一起转包周期。 - false：仅转ELB，不转EIP。  **默认取值**：false

        :return: The include_publicip of this PrepaidChangeChargeModeOption.
        :rtype: bool
        """
        return self._include_publicip

    @include_publicip.setter
    def include_publicip(self, include_publicip):
        r"""Sets the include_publicip of this PrepaidChangeChargeModeOption.

        **参数解释**：是否连同独享按带宽计费的弹性公网IP一起转包周期。 弹性公网IP转包周期之后可以单独解绑、绑定到其他实例和删除EIP。  **约束限制**：只有独享且按带宽计费的弹性公网IP才被允许转包周期。  **取值范围**： - true：连同EIP一起转包周期。 - false：仅转ELB，不转EIP。  **默认取值**：false

        :param include_publicip: The include_publicip of this PrepaidChangeChargeModeOption.
        :type include_publicip: bool
        """
        self._include_publicip = include_publicip

    @property
    def publicip_ids(self):
        r"""Gets the publicip_ids of this PrepaidChangeChargeModeOption.

        **参数解释**：需要一起按需转包的弹性公网IP的ID。  **约束限制**： - 若include_publicip为false，不能指定该字段。 - 若include_publicip为true，该字段为未指定时，表示所有绑定的v4 eip都需要一起转包周期。 - 若include_publicip为true，该字段列表非空，表示只将指定的v4 eip转包。 - 若include_publicip为true，该字段列表为空，表示不指定任一eip转包，与include_publicip为false等效。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The publicip_ids of this PrepaidChangeChargeModeOption.
        :rtype: list[str]
        """
        return self._publicip_ids

    @publicip_ids.setter
    def publicip_ids(self, publicip_ids):
        r"""Sets the publicip_ids of this PrepaidChangeChargeModeOption.

        **参数解释**：需要一起按需转包的弹性公网IP的ID。  **约束限制**： - 若include_publicip为false，不能指定该字段。 - 若include_publicip为true，该字段为未指定时，表示所有绑定的v4 eip都需要一起转包周期。 - 若include_publicip为true，该字段列表非空，表示只将指定的v4 eip转包。 - 若include_publicip为true，该字段列表为空，表示不指定任一eip转包，与include_publicip为false等效。  **取值范围**：不涉及  **默认取值**：不涉及

        :param publicip_ids: The publicip_ids of this PrepaidChangeChargeModeOption.
        :type publicip_ids: list[str]
        """
        self._publicip_ids = publicip_ids

    @property
    def period_type(self):
        r"""Gets the period_type of this PrepaidChangeChargeModeOption.

        **参数解释**：订购周期类型。  **约束限制**：不涉及  **取值范围**： - month：月 - year：年  **默认取值**：month

        :return: The period_type of this PrepaidChangeChargeModeOption.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this PrepaidChangeChargeModeOption.

        **参数解释**：订购周期类型。  **约束限制**：不涉及  **取值范围**： - month：月 - year：年  **默认取值**：month

        :param period_type: The period_type of this PrepaidChangeChargeModeOption.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this PrepaidChangeChargeModeOption.

        **参数解释**：订购周期数，取值会随运营策略变化。  **约束限制**：不涉及  **取值范围**： - period_type为month时，为[1,9] - period_type为year时，为[1,3]  **默认取值**：1

        :return: The period_num of this PrepaidChangeChargeModeOption.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this PrepaidChangeChargeModeOption.

        **参数解释**：订购周期数，取值会随运营策略变化。  **约束限制**：不涉及  **取值范围**： - period_type为month时，为[1,9] - period_type为year时，为[1,3]  **默认取值**：1

        :param period_num: The period_num of this PrepaidChangeChargeModeOption.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def auto_renew(self):
        r"""Gets the auto_renew of this PrepaidChangeChargeModeOption.

        **参数解释**：是否自动续订。  **约束限制**：不涉及  **取值范围**： - true：自动续订。 - false：不自动续订。  **默认取值**：false

        :return: The auto_renew of this PrepaidChangeChargeModeOption.
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        r"""Sets the auto_renew of this PrepaidChangeChargeModeOption.

        **参数解释**：是否自动续订。  **约束限制**：不涉及  **取值范围**： - true：自动续订。 - false：不自动续订。  **默认取值**：false

        :param auto_renew: The auto_renew of this PrepaidChangeChargeModeOption.
        :type auto_renew: bool
        """
        self._auto_renew = auto_renew

    @property
    def auto_pay(self):
        r"""Gets the auto_pay of this PrepaidChangeChargeModeOption.

        **参数解释**：下单订购后，是否自动从客户的账户中支付。  **约束限制**：自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择不自动支付，然后在用户费用中心，选择代金券支付。  **取值范围**： - true：自动支付。 - false：不自动支付。  **默认取值**：false

        :return: The auto_pay of this PrepaidChangeChargeModeOption.
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        r"""Sets the auto_pay of this PrepaidChangeChargeModeOption.

        **参数解释**：下单订购后，是否自动从客户的账户中支付。  **约束限制**：自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择不自动支付，然后在用户费用中心，选择代金券支付。  **取值范围**： - true：自动支付。 - false：不自动支付。  **默认取值**：false

        :param auto_pay: The auto_pay of this PrepaidChangeChargeModeOption.
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
        if not isinstance(other, PrepaidChangeChargeModeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
