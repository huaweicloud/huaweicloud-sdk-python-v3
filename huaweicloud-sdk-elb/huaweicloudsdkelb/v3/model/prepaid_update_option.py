# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrepaidUpdateOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_pay': 'bool',
        'change_mode': 'str',
        'period_num': 'int',
        'period_type': 'str'
    }

    attribute_map = {
        'auto_pay': 'auto_pay',
        'change_mode': 'change_mode',
        'period_num': 'period_num',
        'period_type': 'period_type'
    }

    def __init__(self, auto_pay=None, change_mode=None, period_num=None, period_type=None):
        """PrepaidUpdateOption

        The model defined in huaweicloud sdk

        :param auto_pay: 下单订购后，是否自动从客户的账户中支付； true：自动支付； false：不自动支付（默认）。 自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择不自动支付，然后在用户费用中心，选择代金券支付。
        :type auto_pay: bool
        :param change_mode: 规格变更类型： immediate：即时变更，规格变更立即生效。（默认） delay：续费变更，当前周期结束后变更为目标规格。
        :type change_mode: str
        :param period_num: 订购周期数（默认1），取值会随运营策略变化。（仅在change_mode为delay时生效） period_type为month时，为[1,9]， period_type为year时，为[1,3]
        :type period_num: int
        :param period_type: 订购周期类型，当前支持包月和包年： （仅在change_mode为delay时生效） month：月（默认）； year：年；
        :type period_type: str
        """
        
        

        self._auto_pay = None
        self._change_mode = None
        self._period_num = None
        self._period_type = None
        self.discriminator = None

        if auto_pay is not None:
            self.auto_pay = auto_pay
        if change_mode is not None:
            self.change_mode = change_mode
        if period_num is not None:
            self.period_num = period_num
        if period_type is not None:
            self.period_type = period_type

    @property
    def auto_pay(self):
        """Gets the auto_pay of this PrepaidUpdateOption.

        下单订购后，是否自动从客户的账户中支付； true：自动支付； false：不自动支付（默认）。 自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择不自动支付，然后在用户费用中心，选择代金券支付。

        :return: The auto_pay of this PrepaidUpdateOption.
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        """Sets the auto_pay of this PrepaidUpdateOption.

        下单订购后，是否自动从客户的账户中支付； true：自动支付； false：不自动支付（默认）。 自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择不自动支付，然后在用户费用中心，选择代金券支付。

        :param auto_pay: The auto_pay of this PrepaidUpdateOption.
        :type auto_pay: bool
        """
        self._auto_pay = auto_pay

    @property
    def change_mode(self):
        """Gets the change_mode of this PrepaidUpdateOption.

        规格变更类型： immediate：即时变更，规格变更立即生效。（默认） delay：续费变更，当前周期结束后变更为目标规格。

        :return: The change_mode of this PrepaidUpdateOption.
        :rtype: str
        """
        return self._change_mode

    @change_mode.setter
    def change_mode(self, change_mode):
        """Sets the change_mode of this PrepaidUpdateOption.

        规格变更类型： immediate：即时变更，规格变更立即生效。（默认） delay：续费变更，当前周期结束后变更为目标规格。

        :param change_mode: The change_mode of this PrepaidUpdateOption.
        :type change_mode: str
        """
        self._change_mode = change_mode

    @property
    def period_num(self):
        """Gets the period_num of this PrepaidUpdateOption.

        订购周期数（默认1），取值会随运营策略变化。（仅在change_mode为delay时生效） period_type为month时，为[1,9]， period_type为year时，为[1,3]

        :return: The period_num of this PrepaidUpdateOption.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this PrepaidUpdateOption.

        订购周期数（默认1），取值会随运营策略变化。（仅在change_mode为delay时生效） period_type为month时，为[1,9]， period_type为year时，为[1,3]

        :param period_num: The period_num of this PrepaidUpdateOption.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def period_type(self):
        """Gets the period_type of this PrepaidUpdateOption.

        订购周期类型，当前支持包月和包年： （仅在change_mode为delay时生效） month：月（默认）； year：年；

        :return: The period_type of this PrepaidUpdateOption.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this PrepaidUpdateOption.

        订购周期类型，当前支持包月和包年： （仅在change_mode为delay时生效） month：月（默认）； year：年；

        :param period_type: The period_type of this PrepaidUpdateOption.
        :type period_type: str
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
        if not isinstance(other, PrepaidUpdateOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
