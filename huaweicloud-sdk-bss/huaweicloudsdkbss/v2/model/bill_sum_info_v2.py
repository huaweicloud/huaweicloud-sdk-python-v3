# coding: utf-8

import pprint
import re

import six





class BillSumInfoV2:


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
        'cloud_service_type': 'str',
        'bill_type': 'str',
        'charge_mode': 'str',
        'amount': 'float',
        'debt_amount': 'float',
        'adjustment_amount': 'float',
        'discount_amount': 'float',
        'measure_id': 'int',
        'account_details': 'list[BalanceTypeDeductSumV2]',
        'resource_type_code': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'cloud_service_type': 'cloud_service_type',
        'bill_type': 'bill_type',
        'charge_mode': 'charge_mode',
        'amount': 'amount',
        'debt_amount': 'debt_amount',
        'adjustment_amount': 'adjustment_amount',
        'discount_amount': 'discount_amount',
        'measure_id': 'measure_id',
        'account_details': 'account_details',
        'resource_type_code': 'resource_type_code'
    }

    def __init__(self, customer_id=None, cloud_service_type=None, bill_type=None, charge_mode=None, amount=None, debt_amount=None, adjustment_amount=None, discount_amount=None, measure_id=None, account_details=None, resource_type_code=None):
        """BillSumInfoV2 - a model defined in huaweicloud sdk"""
        
        

        self._customer_id = None
        self._cloud_service_type = None
        self._bill_type = None
        self._charge_mode = None
        self._amount = None
        self._debt_amount = None
        self._adjustment_amount = None
        self._discount_amount = None
        self._measure_id = None
        self._account_details = None
        self._resource_type_code = None
        self.discriminator = None

        if customer_id is not None:
            self.customer_id = customer_id
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if bill_type is not None:
            self.bill_type = bill_type
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if amount is not None:
            self.amount = amount
        if debt_amount is not None:
            self.debt_amount = debt_amount
        if adjustment_amount is not None:
            self.adjustment_amount = adjustment_amount
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if account_details is not None:
            self.account_details = account_details
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code

    @property
    def customer_id(self):
        """Gets the customer_id of this BillSumInfoV2.

        |参数名称：客户ID。| |参数约束及描述：客户ID。|

        :return: The customer_id of this BillSumInfoV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this BillSumInfoV2.

        |参数名称：客户ID。| |参数约束及描述：客户ID。|

        :param customer_id: The customer_id of this BillSumInfoV2.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this BillSumInfoV2.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型。| |参数约束及描述：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型。|

        :return: The cloud_service_type of this BillSumInfoV2.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this BillSumInfoV2.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型。| |参数约束及描述：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型。|

        :param cloud_service_type: The cloud_service_type of this BillSumInfoV2.
        :type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def bill_type(self):
        """Gets the bill_type of this BillSumInfoV2.

        |参数名称：费用类型。0：消费；1：退订；2：华为核销。| |参数约束及描述：费用类型。0：消费；1：退订；2：华为核销。|

        :return: The bill_type of this BillSumInfoV2.
        :rtype: str
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this BillSumInfoV2.

        |参数名称：费用类型。0：消费；1：退订；2：华为核销。| |参数约束及描述：费用类型。0：消费；1：退订；2：华为核销。|

        :param bill_type: The bill_type of this BillSumInfoV2.
        :type: str
        """
        self._bill_type = bill_type

    @property
    def charge_mode(self):
        """Gets the charge_mode of this BillSumInfoV2.

        |参数名称：消费类型。1：包周期；3: 按需。| |参数约束及描述：消费类型。1：包周期；3: 按需。|

        :return: The charge_mode of this BillSumInfoV2.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this BillSumInfoV2.

        |参数名称：消费类型。1：包周期；3: 按需。| |参数约束及描述：消费类型。1：包周期；3: 按需。|

        :param charge_mode: The charge_mode of this BillSumInfoV2.
        :type: str
        """
        self._charge_mode = charge_mode

    @property
    def amount(self):
        """Gets the amount of this BillSumInfoV2.

        |参数名称：消费的金额，即从客户账户实际扣除的金额。对于billType=1或者2的账单，该金额为负值。| |参数的约束及描述：消费的金额，即从客户账户实际扣除的金额。对于billType=1或者2的账单，该金额为负值。|

        :return: The amount of this BillSumInfoV2.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BillSumInfoV2.

        |参数名称：消费的金额，即从客户账户实际扣除的金额。对于billType=1或者2的账单，该金额为负值。| |参数的约束及描述：消费的金额，即从客户账户实际扣除的金额。对于billType=1或者2的账单，该金额为负值。|

        :param amount: The amount of this BillSumInfoV2.
        :type: float
        """
        self._amount = amount

    @property
    def debt_amount(self):
        """Gets the debt_amount of this BillSumInfoV2.

        |参数名称：欠费金额，指从客户账户扣费的时候，客户账户金额不足，欠费的金额，华为核销或者退订的时候没有该字段。| |参数的约束及描述：欠费金额，指从客户账户扣费的时候，客户账户金额不足，欠费的金额，华为核销或者退订的时候没有该字段。|

        :return: The debt_amount of this BillSumInfoV2.
        :rtype: float
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        """Sets the debt_amount of this BillSumInfoV2.

        |参数名称：欠费金额，指从客户账户扣费的时候，客户账户金额不足，欠费的金额，华为核销或者退订的时候没有该字段。| |参数的约束及描述：欠费金额，指从客户账户扣费的时候，客户账户金额不足，欠费的金额，华为核销或者退订的时候没有该字段。|

        :param debt_amount: The debt_amount of this BillSumInfoV2.
        :type: float
        """
        self._debt_amount = debt_amount

    @property
    def adjustment_amount(self):
        """Gets the adjustment_amount of this BillSumInfoV2.

        |参数名称：核销欠款，华为核销或者退订的时候没有该字段。| |参数的约束及描述：核销欠款，华为核销或者退订的时候没有该字段。|

        :return: The adjustment_amount of this BillSumInfoV2.
        :rtype: float
        """
        return self._adjustment_amount

    @adjustment_amount.setter
    def adjustment_amount(self, adjustment_amount):
        """Sets the adjustment_amount of this BillSumInfoV2.

        |参数名称：核销欠款，华为核销或者退订的时候没有该字段。| |参数的约束及描述：核销欠款，华为核销或者退订的时候没有该字段。|

        :param adjustment_amount: The adjustment_amount of this BillSumInfoV2.
        :type: float
        """
        self._adjustment_amount = adjustment_amount

    @property
    def discount_amount(self):
        """Gets the discount_amount of this BillSumInfoV2.

        |参数名称：折扣金额，华为核销或者退订的时候没有该字段。| |参数的约束及描述：折扣金额，华为核销或者退订的时候没有该字段。|

        :return: The discount_amount of this BillSumInfoV2.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this BillSumInfoV2.

        |参数名称：折扣金额，华为核销或者退订的时候没有该字段。| |参数的约束及描述：折扣金额，华为核销或者退订的时候没有该字段。|

        :param discount_amount: The discount_amount of this BillSumInfoV2.
        :type: float
        """
        self._discount_amount = discount_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this BillSumInfoV2.

        |参数名称：金额单位。1：元| |参数的约束及描述：金额单位。1：元|

        :return: The measure_id of this BillSumInfoV2.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this BillSumInfoV2.

        |参数名称：金额单位。1：元| |参数的约束及描述：金额单位。1：元|

        :param measure_id: The measure_id of this BillSumInfoV2.
        :type: int
        """
        self._measure_id = measure_id

    @property
    def account_details(self):
        """Gets the account_details of this BillSumInfoV2.

        |参数名称：按不同账户消费类型和付费方式区分的支付总金额。具体请参见表 BalanceTypeDeductSum。| |参数约束以及描述：按不同账户消费类型和付费方式区分的支付总金额。具体请参见表 BalanceTypeDeductSum。|

        :return: The account_details of this BillSumInfoV2.
        :rtype: list[BalanceTypeDeductSumV2]
        """
        return self._account_details

    @account_details.setter
    def account_details(self, account_details):
        """Sets the account_details of this BillSumInfoV2.

        |参数名称：按不同账户消费类型和付费方式区分的支付总金额。具体请参见表 BalanceTypeDeductSum。| |参数约束以及描述：按不同账户消费类型和付费方式区分的支付总金额。具体请参见表 BalanceTypeDeductSum。|

        :param account_details: The account_details of this BillSumInfoV2.
        :type: list[BalanceTypeDeductSumV2]
        """
        self._account_details = account_details

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this BillSumInfoV2.

        |参数名称：资源类型编码| |参数约束及描述：资源类型编码|

        :return: The resource_type_code of this BillSumInfoV2.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this BillSumInfoV2.

        |参数名称：资源类型编码| |参数约束及描述：资源类型编码|

        :param resource_type_code: The resource_type_code of this BillSumInfoV2.
        :type: str
        """
        self._resource_type_code = resource_type_code

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
        if not isinstance(other, BillSumInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
