# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeInstanceChargeMode:

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
        'is_auto_renew': 'bool',
        'is_auto_pay': 'bool'
    }

    attribute_map = {
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, period_type=None, period_num=None, is_auto_renew=None, is_auto_pay=None):
        r"""ChangeInstanceChargeMode

        The model defined in huaweicloud sdk

        :param period_type: **参数说明**：订购设备接入实例的周期类型（包年、包月等）。charge_mode为prePaid时生效，且为必选值。 **取值范围**： - month：包月 - year：包年 
        :type period_type: str
        :param period_num: **参数说明**：订购设备接入实例的周期数。charge_mode为prePaid时生效，且为必选值。 **取值范围**：period_type&#x3D;month（周期类型为月）时，取值为[1，9]；period_type&#x3D;year（周期类型为年）时，取值为[1，3]\&quot; 
        :type period_num: int
        :param is_auto_renew: **参数说明**：创建包年/包月实例时可指定，表示是否自动续订，续订的周期和原周期相同，且续订时会自动支付。 **取值范围**： - true：自动续订 - false：默认值，不自动续订 
        :type is_auto_renew: bool
        :param is_auto_pay: **参数说明**：创建包年/包月实例时可指定，表示是否自动从客户的账户中支付，此字段不影响自动续订的支付方式。 **取值范围**：true - 自动支付，从账户余额自动扣费; false - 默认值，只提交订单不支付。[需要客户参考[\&quot;支付包年/包月产品订单\&quot;](https://support.huaweicloud.com/api-bpconsole/api_order_00016.html#section0)进行支付，或者在华为云官网页面使用进行支付。](tag:hws) 
        :type is_auto_pay: bool
        """
        
        

        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self.discriminator = None

        self.period_type = period_type
        self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def period_type(self):
        r"""Gets the period_type of this ChangeInstanceChargeMode.

        **参数说明**：订购设备接入实例的周期类型（包年、包月等）。charge_mode为prePaid时生效，且为必选值。 **取值范围**： - month：包月 - year：包年 

        :return: The period_type of this ChangeInstanceChargeMode.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this ChangeInstanceChargeMode.

        **参数说明**：订购设备接入实例的周期类型（包年、包月等）。charge_mode为prePaid时生效，且为必选值。 **取值范围**： - month：包月 - year：包年 

        :param period_type: The period_type of this ChangeInstanceChargeMode.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this ChangeInstanceChargeMode.

        **参数说明**：订购设备接入实例的周期数。charge_mode为prePaid时生效，且为必选值。 **取值范围**：period_type=month（周期类型为月）时，取值为[1，9]；period_type=year（周期类型为年）时，取值为[1，3]\" 

        :return: The period_num of this ChangeInstanceChargeMode.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this ChangeInstanceChargeMode.

        **参数说明**：订购设备接入实例的周期数。charge_mode为prePaid时生效，且为必选值。 **取值范围**：period_type=month（周期类型为月）时，取值为[1，9]；period_type=year（周期类型为年）时，取值为[1，3]\" 

        :param period_num: The period_num of this ChangeInstanceChargeMode.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this ChangeInstanceChargeMode.

        **参数说明**：创建包年/包月实例时可指定，表示是否自动续订，续订的周期和原周期相同，且续订时会自动支付。 **取值范围**： - true：自动续订 - false：默认值，不自动续订 

        :return: The is_auto_renew of this ChangeInstanceChargeMode.
        :rtype: bool
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this ChangeInstanceChargeMode.

        **参数说明**：创建包年/包月实例时可指定，表示是否自动续订，续订的周期和原周期相同，且续订时会自动支付。 **取值范围**： - true：自动续订 - false：默认值，不自动续订 

        :param is_auto_renew: The is_auto_renew of this ChangeInstanceChargeMode.
        :type is_auto_renew: bool
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this ChangeInstanceChargeMode.

        **参数说明**：创建包年/包月实例时可指定，表示是否自动从客户的账户中支付，此字段不影响自动续订的支付方式。 **取值范围**：true - 自动支付，从账户余额自动扣费; false - 默认值，只提交订单不支付。[需要客户参考[\"支付包年/包月产品订单\"](https://support.huaweicloud.com/api-bpconsole/api_order_00016.html#section0)进行支付，或者在华为云官网页面使用进行支付。](tag:hws) 

        :return: The is_auto_pay of this ChangeInstanceChargeMode.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this ChangeInstanceChargeMode.

        **参数说明**：创建包年/包月实例时可指定，表示是否自动从客户的账户中支付，此字段不影响自动续订的支付方式。 **取值范围**：true - 自动支付，从账户余额自动扣费; false - 默认值，只提交订单不支付。[需要客户参考[\"支付包年/包月产品订单\"](https://support.huaweicloud.com/api-bpconsole/api_order_00016.html#section0)进行支付，或者在华为云官网页面使用进行支付。](tag:hws) 

        :param is_auto_pay: The is_auto_pay of this ChangeInstanceChargeMode.
        :type is_auto_pay: bool
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
        if not isinstance(other, ChangeInstanceChargeMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
