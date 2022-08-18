# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModSubCustomerBudgetReq:

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
        'budget_amount': 'float',
        'cancel_partner_frozen': 'str',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'budget_amount': 'budget_amount',
        'cancel_partner_frozen': 'cancel_partner_frozen',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, customer_id=None, budget_amount=None, cancel_partner_frozen=None, indirect_partner_id=None):
        """ModSubCustomerBudgetReq

        The model defined in huaweicloud sdk

        :param customer_id: 客户账号ID。您可以调用查询客户列表接口获取customer_id。
        :type customer_id: str
        :param budget_amount: 调整的目标金额。 单位：元。精确至小数点后2位。
        :type budget_amount: float
        :param cancel_partner_frozen: 是否在设置客户预算的同时解除账号冻结： 0：否1：是 默认值为0。
        :type cancel_partner_frozen: str
        :param indirect_partner_id: 云经销商ID。获取方法请参见查询云经销商列表。如果需要查询云经销商的子客户列表，必须携带该字段。除此之外，此参数不做处理。
        :type indirect_partner_id: str
        """
        
        

        self._customer_id = None
        self._budget_amount = None
        self._cancel_partner_frozen = None
        self._indirect_partner_id = None
        self.discriminator = None

        self.customer_id = customer_id
        self.budget_amount = budget_amount
        if cancel_partner_frozen is not None:
            self.cancel_partner_frozen = cancel_partner_frozen
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def customer_id(self):
        """Gets the customer_id of this ModSubCustomerBudgetReq.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :return: The customer_id of this ModSubCustomerBudgetReq.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ModSubCustomerBudgetReq.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :param customer_id: The customer_id of this ModSubCustomerBudgetReq.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def budget_amount(self):
        """Gets the budget_amount of this ModSubCustomerBudgetReq.

        调整的目标金额。 单位：元。精确至小数点后2位。

        :return: The budget_amount of this ModSubCustomerBudgetReq.
        :rtype: float
        """
        return self._budget_amount

    @budget_amount.setter
    def budget_amount(self, budget_amount):
        """Sets the budget_amount of this ModSubCustomerBudgetReq.

        调整的目标金额。 单位：元。精确至小数点后2位。

        :param budget_amount: The budget_amount of this ModSubCustomerBudgetReq.
        :type budget_amount: float
        """
        self._budget_amount = budget_amount

    @property
    def cancel_partner_frozen(self):
        """Gets the cancel_partner_frozen of this ModSubCustomerBudgetReq.

        是否在设置客户预算的同时解除账号冻结： 0：否1：是 默认值为0。

        :return: The cancel_partner_frozen of this ModSubCustomerBudgetReq.
        :rtype: str
        """
        return self._cancel_partner_frozen

    @cancel_partner_frozen.setter
    def cancel_partner_frozen(self, cancel_partner_frozen):
        """Sets the cancel_partner_frozen of this ModSubCustomerBudgetReq.

        是否在设置客户预算的同时解除账号冻结： 0：否1：是 默认值为0。

        :param cancel_partner_frozen: The cancel_partner_frozen of this ModSubCustomerBudgetReq.
        :type cancel_partner_frozen: str
        """
        self._cancel_partner_frozen = cancel_partner_frozen

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ModSubCustomerBudgetReq.

        云经销商ID。获取方法请参见查询云经销商列表。如果需要查询云经销商的子客户列表，必须携带该字段。除此之外，此参数不做处理。

        :return: The indirect_partner_id of this ModSubCustomerBudgetReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ModSubCustomerBudgetReq.

        云经销商ID。获取方法请参见查询云经销商列表。如果需要查询云经销商的子客户列表，必须携带该字段。除此之外，此参数不做处理。

        :param indirect_partner_id: The indirect_partner_id of this ModSubCustomerBudgetReq.
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
        if not isinstance(other, ModSubCustomerBudgetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
