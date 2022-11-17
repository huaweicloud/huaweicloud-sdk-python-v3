# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdjustAccountReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_id': 'str',
        'amount': 'float',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'amount': 'amount',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, customer_id=None, amount=None, indirect_partner_id=None):
        """AdjustAccountReq

        The model defined in huaweicloud sdk

        :param customer_id: 客户账号ID。您可以调用[查询客户列表](https://support.huaweicloud.com/api-bpconsole/mc_00021.html)接口获取customer_id。
        :type customer_id: str
        :param amount: 拨款金额。 单位：元。取值大于0且精确到小数点后2位。 注意该值不能大于“查询伙伴账户余额”接口响应消息表2中参数amount - designated_amount的值。
        :type amount: float
        :param indirect_partner_id: 云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。 云经销商（二级经销商）给子客户拨款时，需携带该参数。除此之外，该参数不做处理。  说明： 该参数存在的情况下，如果结果返回余额不足，表示对应的二级经销商的余额不足。如果该参数不存在，则余额不足表示调用的伙伴自身账号的余额不足。
        :type indirect_partner_id: str
        """
        
        

        self._customer_id = None
        self._amount = None
        self._indirect_partner_id = None
        self.discriminator = None

        self.customer_id = customer_id
        self.amount = amount
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def customer_id(self):
        """Gets the customer_id of this AdjustAccountReq.

        客户账号ID。您可以调用[查询客户列表](https://support.huaweicloud.com/api-bpconsole/mc_00021.html)接口获取customer_id。

        :return: The customer_id of this AdjustAccountReq.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this AdjustAccountReq.

        客户账号ID。您可以调用[查询客户列表](https://support.huaweicloud.com/api-bpconsole/mc_00021.html)接口获取customer_id。

        :param customer_id: The customer_id of this AdjustAccountReq.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def amount(self):
        """Gets the amount of this AdjustAccountReq.

        拨款金额。 单位：元。取值大于0且精确到小数点后2位。 注意该值不能大于“查询伙伴账户余额”接口响应消息表2中参数amount - designated_amount的值。

        :return: The amount of this AdjustAccountReq.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AdjustAccountReq.

        拨款金额。 单位：元。取值大于0且精确到小数点后2位。 注意该值不能大于“查询伙伴账户余额”接口响应消息表2中参数amount - designated_amount的值。

        :param amount: The amount of this AdjustAccountReq.
        :type amount: float
        """
        self._amount = amount

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this AdjustAccountReq.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。 云经销商（二级经销商）给子客户拨款时，需携带该参数。除此之外，该参数不做处理。  说明： 该参数存在的情况下，如果结果返回余额不足，表示对应的二级经销商的余额不足。如果该参数不存在，则余额不足表示调用的伙伴自身账号的余额不足。

        :return: The indirect_partner_id of this AdjustAccountReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this AdjustAccountReq.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。 云经销商（二级经销商）给子客户拨款时，需携带该参数。除此之外，该参数不做处理。  说明： 该参数存在的情况下，如果结果返回余额不足，表示对应的二级经销商的余额不足。如果该参数不存在，则余额不足表示调用的伙伴自身账号的余额不足。

        :param indirect_partner_id: The indirect_partner_id of this AdjustAccountReq.
        :type indirect_partner_id: str
        """
        self._indirect_partner_id = indirect_partner_id

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
        if not isinstance(other, AdjustAccountReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
