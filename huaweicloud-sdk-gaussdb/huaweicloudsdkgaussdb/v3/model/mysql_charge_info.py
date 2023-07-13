# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlChargeInfo:

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
        """MysqlChargeInfo

        The model defined in huaweicloud sdk

        :param charge_mode: 计费模式。  取值范围：  - prePaid：预付费，即包年/包月。 - postPaid：后付费，即按需付费。
        :type charge_mode: str
        :param period_type: 订购周期类型。  取值范围：  - month：包月。 - year：包年。  说明：“charge_mode”为“prePaid”时生效，且为必选值。
        :type period_type: str
        :param period_num: “charge_mode”为“prePaid”时生效，且为必选值，指定订购的时间。  取值范围：  当“period_type”为“month”时，取值为1~9。 当“period_type”为“year”时，取值为1~3。
        :type period_num: int
        :param is_auto_renew: 创建包周期实例时可指定，表示是否自动续订，续订的周期和原周期相同，且续订时会自动支付。  - true，为自动续订。 - false，为不自动续订，默认该方式。
        :type is_auto_renew: str
        :param is_auto_pay: 创建包周期时可指定，表示是否自动从客户的账户中支付，此字段不影响自动续订的支付方式。  - true，为自动支付，默认该方式。 - false，为手动支付。
        :type is_auto_pay: str
        """
        
        

        self._charge_mode = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self.discriminator = None

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
        """Gets the charge_mode of this MysqlChargeInfo.

        计费模式。  取值范围：  - prePaid：预付费，即包年/包月。 - postPaid：后付费，即按需付费。

        :return: The charge_mode of this MysqlChargeInfo.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this MysqlChargeInfo.

        计费模式。  取值范围：  - prePaid：预付费，即包年/包月。 - postPaid：后付费，即按需付费。

        :param charge_mode: The charge_mode of this MysqlChargeInfo.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def period_type(self):
        """Gets the period_type of this MysqlChargeInfo.

        订购周期类型。  取值范围：  - month：包月。 - year：包年。  说明：“charge_mode”为“prePaid”时生效，且为必选值。

        :return: The period_type of this MysqlChargeInfo.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this MysqlChargeInfo.

        订购周期类型。  取值范围：  - month：包月。 - year：包年。  说明：“charge_mode”为“prePaid”时生效，且为必选值。

        :param period_type: The period_type of this MysqlChargeInfo.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this MysqlChargeInfo.

        “charge_mode”为“prePaid”时生效，且为必选值，指定订购的时间。  取值范围：  当“period_type”为“month”时，取值为1~9。 当“period_type”为“year”时，取值为1~3。

        :return: The period_num of this MysqlChargeInfo.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this MysqlChargeInfo.

        “charge_mode”为“prePaid”时生效，且为必选值，指定订购的时间。  取值范围：  当“period_type”为“month”时，取值为1~9。 当“period_type”为“year”时，取值为1~3。

        :param period_num: The period_num of this MysqlChargeInfo.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this MysqlChargeInfo.

        创建包周期实例时可指定，表示是否自动续订，续订的周期和原周期相同，且续订时会自动支付。  - true，为自动续订。 - false，为不自动续订，默认该方式。

        :return: The is_auto_renew of this MysqlChargeInfo.
        :rtype: str
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this MysqlChargeInfo.

        创建包周期实例时可指定，表示是否自动续订，续订的周期和原周期相同，且续订时会自动支付。  - true，为自动续订。 - false，为不自动续订，默认该方式。

        :param is_auto_renew: The is_auto_renew of this MysqlChargeInfo.
        :type is_auto_renew: str
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this MysqlChargeInfo.

        创建包周期时可指定，表示是否自动从客户的账户中支付，此字段不影响自动续订的支付方式。  - true，为自动支付，默认该方式。 - false，为手动支付。

        :return: The is_auto_pay of this MysqlChargeInfo.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this MysqlChargeInfo.

        创建包周期时可指定，表示是否自动从客户的账户中支付，此字段不影响自动续订的支付方式。  - true，为自动支付，默认该方式。 - false，为手动支付。

        :param is_auto_pay: The is_auto_pay of this MysqlChargeInfo.
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
        if not isinstance(other, MysqlChargeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
