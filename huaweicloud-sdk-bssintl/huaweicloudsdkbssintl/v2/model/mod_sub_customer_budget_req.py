# coding: utf-8

import pprint
import re

import six





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
        'cancel_partner_frozen': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'budget_amount': 'budget_amount',
        'cancel_partner_frozen': 'cancel_partner_frozen'
    }

    def __init__(self, customer_id=None, budget_amount=None, cancel_partner_frozen=None):
        """ModSubCustomerBudgetReq - a model defined in huaweicloud sdk"""
        
        

        self._customer_id = None
        self._budget_amount = None
        self._cancel_partner_frozen = None
        self.discriminator = None

        self.customer_id = customer_id
        self.budget_amount = budget_amount
        if cancel_partner_frozen is not None:
            self.cancel_partner_frozen = cancel_partner_frozen

    @property
    def customer_id(self):
        """Gets the customer_id of this ModSubCustomerBudgetReq.

        |参数名称：客户ID。| |参数约束及描述：客户ID。|

        :return: The customer_id of this ModSubCustomerBudgetReq.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ModSubCustomerBudgetReq.

        |参数名称：客户ID。| |参数约束及描述：客户ID。|

        :param customer_id: The customer_id of this ModSubCustomerBudgetReq.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def budget_amount(self):
        """Gets the budget_amount of this ModSubCustomerBudgetReq.

        |参数名称：调整的目标金额，可精确至小数点后面2位。| |参数的约束及描述：调整的目标金额，可精确至小数点后面2位。|

        :return: The budget_amount of this ModSubCustomerBudgetReq.
        :rtype: float
        """
        return self._budget_amount

    @budget_amount.setter
    def budget_amount(self, budget_amount):
        """Sets the budget_amount of this ModSubCustomerBudgetReq.

        |参数名称：调整的目标金额，可精确至小数点后面2位。| |参数的约束及描述：调整的目标金额，可精确至小数点后面2位。|

        :param budget_amount: The budget_amount of this ModSubCustomerBudgetReq.
        :type: float
        """
        self._budget_amount = budget_amount

    @property
    def cancel_partner_frozen(self):
        """Gets the cancel_partner_frozen of this ModSubCustomerBudgetReq.

        |参数名称：是否在设置客户预算的同时解除账号冻结：0：否；1：是。默认为否。| |参数约束及描述：是否在设置客户预算的同时解除账号冻结：0：否；1：是。默认为否。|

        :return: The cancel_partner_frozen of this ModSubCustomerBudgetReq.
        :rtype: str
        """
        return self._cancel_partner_frozen

    @cancel_partner_frozen.setter
    def cancel_partner_frozen(self, cancel_partner_frozen):
        """Sets the cancel_partner_frozen of this ModSubCustomerBudgetReq.

        |参数名称：是否在设置客户预算的同时解除账号冻结：0：否；1：是。默认为否。| |参数约束及描述：是否在设置客户预算的同时解除账号冻结：0：否；1：是。默认为否。|

        :param cancel_partner_frozen: The cancel_partner_frozen of this ModSubCustomerBudgetReq.
        :type: str
        """
        self._cancel_partner_frozen = cancel_partner_frozen

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModSubCustomerBudgetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
