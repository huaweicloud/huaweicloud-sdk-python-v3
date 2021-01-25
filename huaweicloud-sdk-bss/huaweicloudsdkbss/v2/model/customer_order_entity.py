# coding: utf-8

import pprint
import re

import six





class CustomerOrderEntity:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'customer_id': 'str',
        'status': 'int',
        'order_type': 'int',
        'amount_after_discount': 'float',
        'official_amount': 'float',
        'measure_id': 'int',
        'create_time': 'str',
        'payment_time': 'str',
        'currency': 'str',
        'agent_pay_info': 'AgentPayInfo',
        'amount_info': 'AmountInfomation'
    }

    attribute_map = {
        'order_id': 'order_id',
        'customer_id': 'customer_id',
        'status': 'status',
        'order_type': 'order_type',
        'amount_after_discount': 'amount_after_discount',
        'official_amount': 'official_amount',
        'measure_id': 'measure_id',
        'create_time': 'create_time',
        'payment_time': 'payment_time',
        'currency': 'currency',
        'agent_pay_info': 'agent_pay_info',
        'amount_info': 'amount_info'
    }

    def __init__(self, order_id=None, customer_id=None, status=None, order_type=None, amount_after_discount=None, official_amount=None, measure_id=None, create_time=None, payment_time=None, currency=None, agent_pay_info=None, amount_info=None):
        """CustomerOrderEntity - a model defined in huaweicloud sdk"""
        
        

        self._order_id = None
        self._customer_id = None
        self._status = None
        self._order_type = None
        self._amount_after_discount = None
        self._official_amount = None
        self._measure_id = None
        self._create_time = None
        self._payment_time = None
        self._currency = None
        self._agent_pay_info = None
        self._amount_info = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if customer_id is not None:
            self.customer_id = customer_id
        if status is not None:
            self.status = status
        if order_type is not None:
            self.order_type = order_type
        if amount_after_discount is not None:
            self.amount_after_discount = amount_after_discount
        if official_amount is not None:
            self.official_amount = official_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if create_time is not None:
            self.create_time = create_time
        if payment_time is not None:
            self.payment_time = payment_time
        if currency is not None:
            self.currency = currency
        if agent_pay_info is not None:
            self.agent_pay_info = agent_pay_info
        if amount_info is not None:
            self.amount_info = amount_info

    @property
    def order_id(self):
        """Gets the order_id of this CustomerOrderEntity.

        |参数名称：订单ID。| |参数约束及描述：订单ID。|

        :return: The order_id of this CustomerOrderEntity.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CustomerOrderEntity.

        |参数名称：订单ID。| |参数约束及描述：订单ID。|

        :param order_id: The order_id of this CustomerOrderEntity.
        :type: str
        """
        self._order_id = order_id

    @property
    def customer_id(self):
        """Gets the customer_id of this CustomerOrderEntity.

        |参数名称：客户ID。| |参数约束及描述：客户ID。|

        :return: The customer_id of this CustomerOrderEntity.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CustomerOrderEntity.

        |参数名称：客户ID。| |参数约束及描述：客户ID。|

        :param customer_id: The customer_id of this CustomerOrderEntity.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def status(self):
        """Gets the status of this CustomerOrderEntity.

        |参数名称：订单状态：1：待审核3：处理中4：已取消5：已完成6：待支付9：待确认| |参数的约束及描述：订单状态：1：待审核3：处理中4：已取消5：已完成6：待支付9：待确认|

        :return: The status of this CustomerOrderEntity.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CustomerOrderEntity.

        |参数名称：订单状态：1：待审核3：处理中4：已取消5：已完成6：待支付9：待确认| |参数的约束及描述：订单状态：1：待审核3：处理中4：已取消5：已完成6：待支付9：待确认|

        :param status: The status of this CustomerOrderEntity.
        :type: int
        """
        self._status = status

    @property
    def order_type(self):
        """Gets the order_type of this CustomerOrderEntity.

        |参数名称：订单类型：1：开通2：续订3：变更4：退订10：包周期转按需11：按需转包周期12：赠送13：试用14：转商用15：费用调整| |参数的约束及描述：订单类型：1：开通2：续订3：变更4：退订10：包周期转按需11：按需转包周期12：赠送13：试用14：转商用15：费用调整|

        :return: The order_type of this CustomerOrderEntity.
        :rtype: int
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this CustomerOrderEntity.

        |参数名称：订单类型：1：开通2：续订3：变更4：退订10：包周期转按需11：按需转包周期12：赠送13：试用14：转商用15：费用调整| |参数的约束及描述：订单类型：1：开通2：续订3：变更4：退订10：包周期转按需11：按需转包周期12：赠送13：试用14：转商用15：费用调整|

        :param order_type: The order_type of this CustomerOrderEntity.
        :type: int
        """
        self._order_type = order_type

    @property
    def amount_after_discount(self):
        """Gets the amount_after_discount of this CustomerOrderEntity.

        |参数名称：订单优惠后金额（不含券不含卡的实付价格）| |参数的约束及描述：订单优惠后金额（不含券不含卡的实付价格）|

        :return: The amount_after_discount of this CustomerOrderEntity.
        :rtype: float
        """
        return self._amount_after_discount

    @amount_after_discount.setter
    def amount_after_discount(self, amount_after_discount):
        """Sets the amount_after_discount of this CustomerOrderEntity.

        |参数名称：订单优惠后金额（不含券不含卡的实付价格）| |参数的约束及描述：订单优惠后金额（不含券不含卡的实付价格）|

        :param amount_after_discount: The amount_after_discount of this CustomerOrderEntity.
        :type: float
        """
        self._amount_after_discount = amount_after_discount

    @property
    def official_amount(self):
        """Gets the official_amount of this CustomerOrderEntity.

        |参数名称：订单金额（官网价）。退订订单中，该金额等于amount。| |参数的约束及描述：订单金额（官网价）。退订订单中，该金额等于amount。|

        :return: The official_amount of this CustomerOrderEntity.
        :rtype: float
        """
        return self._official_amount

    @official_amount.setter
    def official_amount(self, official_amount):
        """Sets the official_amount of this CustomerOrderEntity.

        |参数名称：订单金额（官网价）。退订订单中，该金额等于amount。| |参数的约束及描述：订单金额（官网价）。退订订单中，该金额等于amount。|

        :param official_amount: The official_amount of this CustomerOrderEntity.
        :type: float
        """
        self._official_amount = official_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this CustomerOrderEntity.

        |参数名称：订单金额度量单位：1：元| |参数的约束及描述：订单金额度量单位：1：元|

        :return: The measure_id of this CustomerOrderEntity.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this CustomerOrderEntity.

        |参数名称：订单金额度量单位：1：元| |参数的约束及描述：订单金额度量单位：1：元|

        :param measure_id: The measure_id of this CustomerOrderEntity.
        :type: int
        """
        self._measure_id = measure_id

    @property
    def create_time(self):
        """Gets the create_time of this CustomerOrderEntity.

        |参数名称：创建时间 。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数约束及描述：创建时间 。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。|

        :return: The create_time of this CustomerOrderEntity.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CustomerOrderEntity.

        |参数名称：创建时间 。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数约束及描述：创建时间 。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。|

        :param create_time: The create_time of this CustomerOrderEntity.
        :type: str
        """
        self._create_time = create_time

    @property
    def payment_time(self):
        """Gets the payment_time of this CustomerOrderEntity.

        |参数名称：支付时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数约束及描述：支付时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。|

        :return: The payment_time of this CustomerOrderEntity.
        :rtype: str
        """
        return self._payment_time

    @payment_time.setter
    def payment_time(self, payment_time):
        """Sets the payment_time of this CustomerOrderEntity.

        |参数名称：支付时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数约束及描述：支付时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。|

        :param payment_time: The payment_time of this CustomerOrderEntity.
        :type: str
        """
        self._payment_time = payment_time

    @property
    def currency(self):
        """Gets the currency of this CustomerOrderEntity.

        |参数名称：货币编码。| |参数约束及描述：货币编码。最大长度8|

        :return: The currency of this CustomerOrderEntity.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CustomerOrderEntity.

        |参数名称：货币编码。| |参数约束及描述：货币编码。最大长度8|

        :param currency: The currency of this CustomerOrderEntity.
        :type: str
        """
        self._currency = currency

    @property
    def agent_pay_info(self):
        """Gets the agent_pay_info of this CustomerOrderEntity.


        :return: The agent_pay_info of this CustomerOrderEntity.
        :rtype: AgentPayInfo
        """
        return self._agent_pay_info

    @agent_pay_info.setter
    def agent_pay_info(self, agent_pay_info):
        """Sets the agent_pay_info of this CustomerOrderEntity.


        :param agent_pay_info: The agent_pay_info of this CustomerOrderEntity.
        :type: AgentPayInfo
        """
        self._agent_pay_info = agent_pay_info

    @property
    def amount_info(self):
        """Gets the amount_info of this CustomerOrderEntity.


        :return: The amount_info of this CustomerOrderEntity.
        :rtype: AmountInfomation
        """
        return self._amount_info

    @amount_info.setter
    def amount_info(self, amount_info):
        """Sets the amount_info of this CustomerOrderEntity.


        :param amount_info: The amount_info of this CustomerOrderEntity.
        :type: AmountInfomation
        """
        self._amount_info = amount_info

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
        if not isinstance(other, CustomerOrderEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
