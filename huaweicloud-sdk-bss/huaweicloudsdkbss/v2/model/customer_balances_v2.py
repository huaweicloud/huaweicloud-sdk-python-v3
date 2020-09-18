# coding: utf-8

import pprint
import re

import six





class CustomerBalancesV2:


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
        'debt_amount': 'float',
        'amount': 'float',
        'currency': 'str',
        'measure_id': 'int'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'debt_amount': 'debt_amount',
        'amount': 'amount',
        'currency': 'currency',
        'measure_id': 'measure_id'
    }

    def __init__(self, customer_id=None, debt_amount=None, amount=None, currency=None, measure_id=None):
        """CustomerBalancesV2 - a model defined in huaweicloud sdk"""
        
        

        self._customer_id = None
        self._debt_amount = None
        self._amount = None
        self._currency = None
        self._measure_id = None
        self.discriminator = None

        self.customer_id = customer_id
        if debt_amount is not None:
            self.debt_amount = debt_amount
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if measure_id is not None:
            self.measure_id = measure_id

    @property
    def customer_id(self):
        """Gets the customer_id of this CustomerBalancesV2.

        |参数名称：客户的客户ID。| |参数约束及描述：客户的客户ID。|

        :return: The customer_id of this CustomerBalancesV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CustomerBalancesV2.

        |参数名称：客户的客户ID。| |参数约束及描述：客户的客户ID。|

        :param customer_id: The customer_id of this CustomerBalancesV2.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def debt_amount(self):
        """Gets the debt_amount of this CustomerBalancesV2.

        |参数名称：客户欠款总额度。| |参数约束及描述： 客户欠款总额度。|

        :return: The debt_amount of this CustomerBalancesV2.
        :rtype: float
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        """Sets the debt_amount of this CustomerBalancesV2.

        |参数名称：客户欠款总额度。| |参数约束及描述： 客户欠款总额度。|

        :param debt_amount: The debt_amount of this CustomerBalancesV2.
        :type: float
        """
        self._debt_amount = debt_amount

    @property
    def amount(self):
        """Gets the amount of this CustomerBalancesV2.

        |参数名称：客户可用总额度。| |参数约束及描述： 客户可用总额度。|

        :return: The amount of this CustomerBalancesV2.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CustomerBalancesV2.

        |参数名称：客户可用总额度。| |参数约束及描述： 客户可用总额度。|

        :param amount: The amount of this CustomerBalancesV2.
        :type: float
        """
        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this CustomerBalancesV2.

        |参数名称：币种。| |参数约束及描述：币种。|

        :return: The currency of this CustomerBalancesV2.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CustomerBalancesV2.

        |参数名称：币种。| |参数约束及描述：币种。|

        :param currency: The currency of this CustomerBalancesV2.
        :type: str
        """
        self._currency = currency

    @property
    def measure_id(self):
        """Gets the measure_id of this CustomerBalancesV2.

        |参数名称：度量单位：1：元；2：角；3：分。| |参数的约束及描述：度量单位：1：元；2：角；3：分。|

        :return: The measure_id of this CustomerBalancesV2.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this CustomerBalancesV2.

        |参数名称：度量单位：1：元；2：角；3：分。| |参数的约束及描述：度量单位：1：元；2：角；3：分。|

        :param measure_id: The measure_id of this CustomerBalancesV2.
        :type: int
        """
        self._measure_id = measure_id

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
        if not isinstance(other, CustomerBalancesV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
