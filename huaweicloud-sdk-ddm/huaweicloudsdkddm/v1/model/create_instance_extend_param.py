# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceExtendParam:

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
        'is_auto_renew': 'str',
        'is_auto_pay': 'str'
    }

    attribute_map = {
        'charge_mode': 'charge_mode',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, charge_mode=None, period_type=None, period_num=None, is_auto_renew=None, is_auto_pay=None):
        """CreateInstanceExtendParam

        The model defined in huaweicloud sdk

        :param charge_mode: 计费模式，取值范围： - prePaid：预付费，即包年/包月。 - postPaid：后付费，即按需付费。 默认值为postPaid。
        :type charge_mode: str
        :param period_type: 订购周期类型，取值范围： - month：月。 - year：年。 “charge_mode”参数配置为“prePaid”时该参数有效且为必选值。
        :type period_type: str
        :param period_num: 订购周期数，取值范围： - period_type&#x3D;month（周期类型为月）时，取值为[1，9]。 - period_type&#x3D;year（周期类型为年）时，取值为1。 “charge_mode”参数配置为“prePaid”时该参数有效且为必选值。
        :type period_num: int
        :param is_auto_renew: 是否自动续订，取值范围： - “true”：自动续订。 - “false”：不自动续订。 “charge_mode”参数配置为“prePaid”时该参数有效，不传该字段时默认为不自动续订。\&quot;
        :type is_auto_renew: str
        :param is_auto_pay: 下单订购后，是否自动从客户的账户的余额中支付，取值范围： - “true”：是（自动从客户账户的余额中支付）。 - “false”：否（需要客户手动支付）。 “charge_mode”参数配置为“prePaid”时该参数有效，不传该字段时默认为客户手动支付。\&quot;
        :type is_auto_pay: str
        """
        
        

        self._charge_mode = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self.discriminator = None

        if charge_mode is not None:
            self.charge_mode = charge_mode
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def charge_mode(self):
        """Gets the charge_mode of this CreateInstanceExtendParam.

        计费模式，取值范围： - prePaid：预付费，即包年/包月。 - postPaid：后付费，即按需付费。 默认值为postPaid。

        :return: The charge_mode of this CreateInstanceExtendParam.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this CreateInstanceExtendParam.

        计费模式，取值范围： - prePaid：预付费，即包年/包月。 - postPaid：后付费，即按需付费。 默认值为postPaid。

        :param charge_mode: The charge_mode of this CreateInstanceExtendParam.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def period_type(self):
        """Gets the period_type of this CreateInstanceExtendParam.

        订购周期类型，取值范围： - month：月。 - year：年。 “charge_mode”参数配置为“prePaid”时该参数有效且为必选值。

        :return: The period_type of this CreateInstanceExtendParam.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this CreateInstanceExtendParam.

        订购周期类型，取值范围： - month：月。 - year：年。 “charge_mode”参数配置为“prePaid”时该参数有效且为必选值。

        :param period_type: The period_type of this CreateInstanceExtendParam.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this CreateInstanceExtendParam.

        订购周期数，取值范围： - period_type=month（周期类型为月）时，取值为[1，9]。 - period_type=year（周期类型为年）时，取值为1。 “charge_mode”参数配置为“prePaid”时该参数有效且为必选值。

        :return: The period_num of this CreateInstanceExtendParam.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this CreateInstanceExtendParam.

        订购周期数，取值范围： - period_type=month（周期类型为月）时，取值为[1，9]。 - period_type=year（周期类型为年）时，取值为1。 “charge_mode”参数配置为“prePaid”时该参数有效且为必选值。

        :param period_num: The period_num of this CreateInstanceExtendParam.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this CreateInstanceExtendParam.

        是否自动续订，取值范围： - “true”：自动续订。 - “false”：不自动续订。 “charge_mode”参数配置为“prePaid”时该参数有效，不传该字段时默认为不自动续订。\"

        :return: The is_auto_renew of this CreateInstanceExtendParam.
        :rtype: str
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this CreateInstanceExtendParam.

        是否自动续订，取值范围： - “true”：自动续订。 - “false”：不自动续订。 “charge_mode”参数配置为“prePaid”时该参数有效，不传该字段时默认为不自动续订。\"

        :param is_auto_renew: The is_auto_renew of this CreateInstanceExtendParam.
        :type is_auto_renew: str
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this CreateInstanceExtendParam.

        下单订购后，是否自动从客户的账户的余额中支付，取值范围： - “true”：是（自动从客户账户的余额中支付）。 - “false”：否（需要客户手动支付）。 “charge_mode”参数配置为“prePaid”时该参数有效，不传该字段时默认为客户手动支付。\"

        :return: The is_auto_pay of this CreateInstanceExtendParam.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this CreateInstanceExtendParam.

        下单订购后，是否自动从客户的账户的余额中支付，取值范围： - “true”：是（自动从客户账户的余额中支付）。 - “false”：否（需要客户手动支付）。 “charge_mode”参数配置为“prePaid”时该参数有效，不传该字段时默认为客户手动支付。\"

        :param is_auto_pay: The is_auto_pay of this CreateInstanceExtendParam.
        :type is_auto_pay: str
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
        if not isinstance(other, CreateInstanceExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
