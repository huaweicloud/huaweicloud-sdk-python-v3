# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeServerChargeModePrepaidOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'include_data_disks': 'bool',
        'include_publicips': 'bool',
        'period_type': 'str',
        'period_num': 'str',
        'auto_pay': 'bool',
        'auto_renew': 'bool'
    }

    attribute_map = {
        'include_data_disks': 'include_data_disks',
        'include_publicips': 'include_publicips',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'auto_pay': 'auto_pay',
        'auto_renew': 'auto_renew'
    }

    def __init__(self, include_data_disks=None, include_publicips=None, period_type=None, period_num=None, auto_pay=None, auto_renew=None):
        """ChangeServerChargeModePrepaidOption

        The model defined in huaweicloud sdk

        :param include_data_disks: 是否连同支持的按需数据盘一起转为包周期。 当参数为true，包括按需非共享的数据盘，不包括共享云硬盘，DSS和DESS硬盘 默认值为false
        :type include_data_disks: bool
        :param include_publicips: 是否连同弹性公网IP一起转为包周期 只有“独享”、“按带宽计费”的弹性公网IP才可以转换为包周期计费模式 默认值为false
        :type include_publicips: bool
        :param period_type: 订购周期类型，取值范围： month-月 year-年
        :type period_type: str
        :param period_num: 订购周期的周期数。 取值范围： period_type&#x3D;month时，取值范围为[1,9]。 period_type&#x3D;year时，取值范围为[1,3]。
        :type period_num: str
        :param auto_pay: 是否自动支付。 true：自动支付，需要确保账户余额充足，如果余额不足则会生成异常订单，只能作废此订单 false：只生成订单不扣费 默认值为false
        :type auto_pay: bool
        :param auto_renew: 是否自动续费。默认值：false
        :type auto_renew: bool
        """
        
        

        self._include_data_disks = None
        self._include_publicips = None
        self._period_type = None
        self._period_num = None
        self._auto_pay = None
        self._auto_renew = None
        self.discriminator = None

        if include_data_disks is not None:
            self.include_data_disks = include_data_disks
        if include_publicips is not None:
            self.include_publicips = include_publicips
        self.period_type = period_type
        self.period_num = period_num
        if auto_pay is not None:
            self.auto_pay = auto_pay
        if auto_renew is not None:
            self.auto_renew = auto_renew

    @property
    def include_data_disks(self):
        """Gets the include_data_disks of this ChangeServerChargeModePrepaidOption.

        是否连同支持的按需数据盘一起转为包周期。 当参数为true，包括按需非共享的数据盘，不包括共享云硬盘，DSS和DESS硬盘 默认值为false

        :return: The include_data_disks of this ChangeServerChargeModePrepaidOption.
        :rtype: bool
        """
        return self._include_data_disks

    @include_data_disks.setter
    def include_data_disks(self, include_data_disks):
        """Sets the include_data_disks of this ChangeServerChargeModePrepaidOption.

        是否连同支持的按需数据盘一起转为包周期。 当参数为true，包括按需非共享的数据盘，不包括共享云硬盘，DSS和DESS硬盘 默认值为false

        :param include_data_disks: The include_data_disks of this ChangeServerChargeModePrepaidOption.
        :type include_data_disks: bool
        """
        self._include_data_disks = include_data_disks

    @property
    def include_publicips(self):
        """Gets the include_publicips of this ChangeServerChargeModePrepaidOption.

        是否连同弹性公网IP一起转为包周期 只有“独享”、“按带宽计费”的弹性公网IP才可以转换为包周期计费模式 默认值为false

        :return: The include_publicips of this ChangeServerChargeModePrepaidOption.
        :rtype: bool
        """
        return self._include_publicips

    @include_publicips.setter
    def include_publicips(self, include_publicips):
        """Sets the include_publicips of this ChangeServerChargeModePrepaidOption.

        是否连同弹性公网IP一起转为包周期 只有“独享”、“按带宽计费”的弹性公网IP才可以转换为包周期计费模式 默认值为false

        :param include_publicips: The include_publicips of this ChangeServerChargeModePrepaidOption.
        :type include_publicips: bool
        """
        self._include_publicips = include_publicips

    @property
    def period_type(self):
        """Gets the period_type of this ChangeServerChargeModePrepaidOption.

        订购周期类型，取值范围： month-月 year-年

        :return: The period_type of this ChangeServerChargeModePrepaidOption.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this ChangeServerChargeModePrepaidOption.

        订购周期类型，取值范围： month-月 year-年

        :param period_type: The period_type of this ChangeServerChargeModePrepaidOption.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this ChangeServerChargeModePrepaidOption.

        订购周期的周期数。 取值范围： period_type=month时，取值范围为[1,9]。 period_type=year时，取值范围为[1,3]。

        :return: The period_num of this ChangeServerChargeModePrepaidOption.
        :rtype: str
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this ChangeServerChargeModePrepaidOption.

        订购周期的周期数。 取值范围： period_type=month时，取值范围为[1,9]。 period_type=year时，取值范围为[1,3]。

        :param period_num: The period_num of this ChangeServerChargeModePrepaidOption.
        :type period_num: str
        """
        self._period_num = period_num

    @property
    def auto_pay(self):
        """Gets the auto_pay of this ChangeServerChargeModePrepaidOption.

        是否自动支付。 true：自动支付，需要确保账户余额充足，如果余额不足则会生成异常订单，只能作废此订单 false：只生成订单不扣费 默认值为false

        :return: The auto_pay of this ChangeServerChargeModePrepaidOption.
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        """Sets the auto_pay of this ChangeServerChargeModePrepaidOption.

        是否自动支付。 true：自动支付，需要确保账户余额充足，如果余额不足则会生成异常订单，只能作废此订单 false：只生成订单不扣费 默认值为false

        :param auto_pay: The auto_pay of this ChangeServerChargeModePrepaidOption.
        :type auto_pay: bool
        """
        self._auto_pay = auto_pay

    @property
    def auto_renew(self):
        """Gets the auto_renew of this ChangeServerChargeModePrepaidOption.

        是否自动续费。默认值：false

        :return: The auto_renew of this ChangeServerChargeModePrepaidOption.
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this ChangeServerChargeModePrepaidOption.

        是否自动续费。默认值：false

        :param auto_renew: The auto_renew of this ChangeServerChargeModePrepaidOption.
        :type auto_renew: bool
        """
        self._auto_renew = auto_renew

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
        if not isinstance(other, ChangeServerChargeModePrepaidOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
