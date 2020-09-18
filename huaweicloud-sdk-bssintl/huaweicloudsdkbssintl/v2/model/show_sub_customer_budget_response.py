# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowSubCustomerBudgetResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'budget_amount': 'float',
        'used_amount': 'float',
        'measure_id': 'int',
        'currency': 'str'
    }

    attribute_map = {
        'budget_amount': 'budget_amount',
        'used_amount': 'used_amount',
        'measure_id': 'measure_id',
        'currency': 'currency'
    }

    def __init__(self, budget_amount=None, used_amount=None, measure_id=None, currency=None):
        """ShowSubCustomerBudgetResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._budget_amount = None
        self._used_amount = None
        self._measure_id = None
        self._currency = None
        self.discriminator = None

        if budget_amount is not None:
            self.budget_amount = budget_amount
        if used_amount is not None:
            self.used_amount = used_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if currency is not None:
            self.currency = currency

    @property
    def budget_amount(self):
        """Gets the budget_amount of this ShowSubCustomerBudgetResponse.

        |参数名称：预算金额。| |参数的约束及描述：预算金额。|

        :return: The budget_amount of this ShowSubCustomerBudgetResponse.
        :rtype: float
        """
        return self._budget_amount

    @budget_amount.setter
    def budget_amount(self, budget_amount):
        """Sets the budget_amount of this ShowSubCustomerBudgetResponse.

        |参数名称：预算金额。| |参数的约束及描述：预算金额。|

        :param budget_amount: The budget_amount of this ShowSubCustomerBudgetResponse.
        :type: float
        """
        self._budget_amount = budget_amount

    @property
    def used_amount(self):
        """Gets the used_amount of this ShowSubCustomerBudgetResponse.

        |参数名称：已经使用的预算。该预算存在一定的时延和误差。| |参数的约束及描述：已经使用的预算。该预算存在一定的时延和误差。|

        :return: The used_amount of this ShowSubCustomerBudgetResponse.
        :rtype: float
        """
        return self._used_amount

    @used_amount.setter
    def used_amount(self, used_amount):
        """Sets the used_amount of this ShowSubCustomerBudgetResponse.

        |参数名称：已经使用的预算。该预算存在一定的时延和误差。| |参数的约束及描述：已经使用的预算。该预算存在一定的时延和误差。|

        :param used_amount: The used_amount of this ShowSubCustomerBudgetResponse.
        :type: float
        """
        self._used_amount = used_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this ShowSubCustomerBudgetResponse.

        |参数名称：金额单位。1：元| |参数的约束及描述：金额单位。1：元|

        :return: The measure_id of this ShowSubCustomerBudgetResponse.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this ShowSubCustomerBudgetResponse.

        |参数名称：金额单位。1：元| |参数的约束及描述：金额单位。1：元|

        :param measure_id: The measure_id of this ShowSubCustomerBudgetResponse.
        :type: int
        """
        self._measure_id = measure_id

    @property
    def currency(self):
        """Gets the currency of this ShowSubCustomerBudgetResponse.

        |参数名称：公司名称币种。CNY：人民币USD：美金| |参数约束及描述：公司名称币种。CNY：人民币USD：美金|

        :return: The currency of this ShowSubCustomerBudgetResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ShowSubCustomerBudgetResponse.

        |参数名称：公司名称币种。CNY：人民币USD：美金| |参数约束及描述：公司名称币种。CNY：人民币USD：美金|

        :param currency: The currency of this ShowSubCustomerBudgetResponse.
        :type: str
        """
        self._currency = currency

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
        if not isinstance(other, ShowSubCustomerBudgetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
