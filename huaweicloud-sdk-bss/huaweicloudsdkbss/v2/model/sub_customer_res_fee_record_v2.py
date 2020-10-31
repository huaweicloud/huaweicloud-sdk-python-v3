# coding: utf-8

import pprint
import re

import six





class SubCustomerResFeeRecordV2:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'effective_time': 'str',
        'expire_time': 'str',
        'product_id': 'str',
        'product_name': 'str',
        'order_id': 'str',
        'amount': 'float',
        'measure_id': 'int',
        'usage_type': 'str',
        'usage': 'float',
        'usage_measure_id': 'int',
        'free_resource_usage': 'float',
        'free_resource_measure_id': 'int',
        'cloud_service_type': 'str',
        'region': 'str',
        'resource_type': 'str',
        'charge_mode': 'str',
        'resource_tag': 'str',
        'resource_name': 'str',
        'resource_id': 'str',
        'bill_type': 'int',
        'period_type': 'str',
        'product_spec_desc': 'str',
        'ri_usage': 'float',
        'ri_usage_measure_id': 'int',
        'official_amount': 'float',
        'discount_amount': 'float',
        'cash_amount': 'float',
        'credit_amount': 'float',
        'coupon_amount': 'float',
        'flexipurchase_coupon_amount': 'float',
        'stored_card_amount': 'float',
        'bonus_amount': 'float',
        'debt_amount': 'float',
        'adjustment_amount': 'float',
        'spec_size': 'float',
        'spec_size_measure_id': 'int'
    }

    attribute_map = {
        'effective_time': 'effective_time',
        'expire_time': 'expire_time',
        'product_id': 'product_id',
        'product_name': 'product_name',
        'order_id': 'order_id',
        'amount': 'amount',
        'measure_id': 'measure_id',
        'usage_type': 'usage_type',
        'usage': 'usage',
        'usage_measure_id': 'usage_measure_id',
        'free_resource_usage': 'free_resource_usage',
        'free_resource_measure_id': 'free_resource_measure_id',
        'cloud_service_type': 'cloud_service_type',
        'region': 'region',
        'resource_type': 'resource_type',
        'charge_mode': 'charge_mode',
        'resource_tag': 'resource_tag',
        'resource_name': 'resource_name',
        'resource_id': 'resource_id',
        'bill_type': 'bill_type',
        'period_type': 'period_type',
        'product_spec_desc': 'product_spec_desc',
        'ri_usage': 'ri_usage',
        'ri_usage_measure_id': 'ri_usage_measure_id',
        'official_amount': 'official_amount',
        'discount_amount': 'discount_amount',
        'cash_amount': 'cash_amount',
        'credit_amount': 'credit_amount',
        'coupon_amount': 'coupon_amount',
        'flexipurchase_coupon_amount': 'flexipurchase_coupon_amount',
        'stored_card_amount': 'stored_card_amount',
        'bonus_amount': 'bonus_amount',
        'debt_amount': 'debt_amount',
        'adjustment_amount': 'adjustment_amount',
        'spec_size': 'spec_size',
        'spec_size_measure_id': 'spec_size_measure_id'
    }

    def __init__(self, effective_time=None, expire_time=None, product_id=None, product_name=None, order_id=None, amount=None, measure_id=None, usage_type=None, usage=None, usage_measure_id=None, free_resource_usage=None, free_resource_measure_id=None, cloud_service_type=None, region=None, resource_type=None, charge_mode=None, resource_tag=None, resource_name=None, resource_id=None, bill_type=None, period_type=None, product_spec_desc=None, ri_usage=None, ri_usage_measure_id=None, official_amount=None, discount_amount=None, cash_amount=None, credit_amount=None, coupon_amount=None, flexipurchase_coupon_amount=None, stored_card_amount=None, bonus_amount=None, debt_amount=None, adjustment_amount=None, spec_size=None, spec_size_measure_id=None):
        """SubCustomerResFeeRecordV2 - a model defined in huaweicloud sdk"""
        
        

        self._effective_time = None
        self._expire_time = None
        self._product_id = None
        self._product_name = None
        self._order_id = None
        self._amount = None
        self._measure_id = None
        self._usage_type = None
        self._usage = None
        self._usage_measure_id = None
        self._free_resource_usage = None
        self._free_resource_measure_id = None
        self._cloud_service_type = None
        self._region = None
        self._resource_type = None
        self._charge_mode = None
        self._resource_tag = None
        self._resource_name = None
        self._resource_id = None
        self._bill_type = None
        self._period_type = None
        self._product_spec_desc = None
        self._ri_usage = None
        self._ri_usage_measure_id = None
        self._official_amount = None
        self._discount_amount = None
        self._cash_amount = None
        self._credit_amount = None
        self._coupon_amount = None
        self._flexipurchase_coupon_amount = None
        self._stored_card_amount = None
        self._bonus_amount = None
        self._debt_amount = None
        self._adjustment_amount = None
        self._spec_size = None
        self._spec_size_measure_id = None
        self.discriminator = None

        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if order_id is not None:
            self.order_id = order_id
        if amount is not None:
            self.amount = amount
        if measure_id is not None:
            self.measure_id = measure_id
        if usage_type is not None:
            self.usage_type = usage_type
        if usage is not None:
            self.usage = usage
        if usage_measure_id is not None:
            self.usage_measure_id = usage_measure_id
        if free_resource_usage is not None:
            self.free_resource_usage = free_resource_usage
        if free_resource_measure_id is not None:
            self.free_resource_measure_id = free_resource_measure_id
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if region is not None:
            self.region = region
        if resource_type is not None:
            self.resource_type = resource_type
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if resource_tag is not None:
            self.resource_tag = resource_tag
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_id is not None:
            self.resource_id = resource_id
        if bill_type is not None:
            self.bill_type = bill_type
        if period_type is not None:
            self.period_type = period_type
        if product_spec_desc is not None:
            self.product_spec_desc = product_spec_desc
        if ri_usage is not None:
            self.ri_usage = ri_usage
        if ri_usage_measure_id is not None:
            self.ri_usage_measure_id = ri_usage_measure_id
        if official_amount is not None:
            self.official_amount = official_amount
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if cash_amount is not None:
            self.cash_amount = cash_amount
        if credit_amount is not None:
            self.credit_amount = credit_amount
        if coupon_amount is not None:
            self.coupon_amount = coupon_amount
        if flexipurchase_coupon_amount is not None:
            self.flexipurchase_coupon_amount = flexipurchase_coupon_amount
        if stored_card_amount is not None:
            self.stored_card_amount = stored_card_amount
        if bonus_amount is not None:
            self.bonus_amount = bonus_amount
        if debt_amount is not None:
            self.debt_amount = debt_amount
        if adjustment_amount is not None:
            self.adjustment_amount = adjustment_amount
        if spec_size is not None:
            self.spec_size = spec_size
        if spec_size_measure_id is not None:
            self.spec_size_measure_id = spec_size_measure_id

    @property
    def effective_time(self):
        """Gets the effective_time of this SubCustomerResFeeRecordV2.

        |参数名称：费用对应的资源使用的开始时间，按需有效，包周期该字段保留。| |参数约束及描述：费用对应的资源使用的开始时间，按需有效，包周期该字段保留。|

        :return: The effective_time of this SubCustomerResFeeRecordV2.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        """Sets the effective_time of this SubCustomerResFeeRecordV2.

        |参数名称：费用对应的资源使用的开始时间，按需有效，包周期该字段保留。| |参数约束及描述：费用对应的资源使用的开始时间，按需有效，包周期该字段保留。|

        :param effective_time: The effective_time of this SubCustomerResFeeRecordV2.
        :type: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        """Gets the expire_time of this SubCustomerResFeeRecordV2.

        |参数名称：费用对应的资源使用的结束时间，按需有效，包周期该字段保留。| |参数约束及描述：费用对应的资源使用的结束时间，按需有效，包周期该字段保留。|

        :return: The expire_time of this SubCustomerResFeeRecordV2.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this SubCustomerResFeeRecordV2.

        |参数名称：费用对应的资源使用的结束时间，按需有效，包周期该字段保留。| |参数约束及描述：费用对应的资源使用的结束时间，按需有效，包周期该字段保留。|

        :param expire_time: The expire_time of this SubCustomerResFeeRecordV2.
        :type: str
        """
        self._expire_time = expire_time

    @property
    def product_id(self):
        """Gets the product_id of this SubCustomerResFeeRecordV2.

        |参数名称：产品ID。| |参数约束及描述：产品ID。|

        :return: The product_id of this SubCustomerResFeeRecordV2.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this SubCustomerResFeeRecordV2.

        |参数名称：产品ID。| |参数约束及描述：产品ID。|

        :param product_id: The product_id of this SubCustomerResFeeRecordV2.
        :type: str
        """
        self._product_id = product_id

    @property
    def product_name(self):
        """Gets the product_name of this SubCustomerResFeeRecordV2.

        |参数名称：产品名称。| |参数约束及描述：产品名称。|

        :return: The product_name of this SubCustomerResFeeRecordV2.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this SubCustomerResFeeRecordV2.

        |参数名称：产品名称。| |参数约束及描述：产品名称。|

        :param product_name: The product_name of this SubCustomerResFeeRecordV2.
        :type: str
        """
        self._product_name = product_name

    @property
    def order_id(self):
        """Gets the order_id of this SubCustomerResFeeRecordV2.

        |参数名称：订单ID，包周期资源使用记录才有该字段，按需资源为空。| |参数约束及描述：订单ID，包周期资源使用记录才有该字段，按需资源为空。|

        :return: The order_id of this SubCustomerResFeeRecordV2.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this SubCustomerResFeeRecordV2.

        |参数名称：订单ID，包周期资源使用记录才有该字段，按需资源为空。| |参数约束及描述：订单ID，包周期资源使用记录才有该字段，按需资源为空。|

        :param order_id: The order_id of this SubCustomerResFeeRecordV2.
        :type: str
        """
        self._order_id = order_id

    @property
    def amount(self):
        """Gets the amount of this SubCustomerResFeeRecordV2.

        |参数名称：消费金额，包括现金券和代金券金额，精确到小数点后2位。| |参数约束及描述： 消费金额，包括现金券和代金券金额，精确到小数点后2位。|

        :return: The amount of this SubCustomerResFeeRecordV2.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SubCustomerResFeeRecordV2.

        |参数名称：消费金额，包括现金券和代金券金额，精确到小数点后2位。| |参数约束及描述： 消费金额，包括现金券和代金券金额，精确到小数点后2位。|

        :param amount: The amount of this SubCustomerResFeeRecordV2.
        :type: float
        """
        self._amount = amount

    @property
    def measure_id(self):
        """Gets the measure_id of this SubCustomerResFeeRecordV2.

        |参数名称：金额单位：1：元；2：角；3：分。| |参数的约束及描述：金额单位：1：元；2：角；3：分。|

        :return: The measure_id of this SubCustomerResFeeRecordV2.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this SubCustomerResFeeRecordV2.

        |参数名称：金额单位：1：元；2：角；3：分。| |参数的约束及描述：金额单位：1：元；2：角；3：分。|

        :param measure_id: The measure_id of this SubCustomerResFeeRecordV2.
        :type: int
        """
        self._measure_id = measure_id

    @property
    def usage_type(self):
        """Gets the usage_type of this SubCustomerResFeeRecordV2.

        |参数名称：使用量类型| |参数约束及描述：使用量类型|

        :return: The usage_type of this SubCustomerResFeeRecordV2.
        :rtype: str
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        """Sets the usage_type of this SubCustomerResFeeRecordV2.

        |参数名称：使用量类型| |参数约束及描述：使用量类型|

        :param usage_type: The usage_type of this SubCustomerResFeeRecordV2.
        :type: str
        """
        self._usage_type = usage_type

    @property
    def usage(self):
        """Gets the usage of this SubCustomerResFeeRecordV2.

        |参数名称：使用量。| |参数约束及描述： 使用量。|

        :return: The usage of this SubCustomerResFeeRecordV2.
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this SubCustomerResFeeRecordV2.

        |参数名称：使用量。| |参数约束及描述： 使用量。|

        :param usage: The usage of this SubCustomerResFeeRecordV2.
        :type: float
        """
        self._usage = usage

    @property
    def usage_measure_id(self):
        """Gets the usage_measure_id of this SubCustomerResFeeRecordV2.

        |参数名称：使用量度量单位| |参数的约束及描述：使用量度量单位|

        :return: The usage_measure_id of this SubCustomerResFeeRecordV2.
        :rtype: int
        """
        return self._usage_measure_id

    @usage_measure_id.setter
    def usage_measure_id(self, usage_measure_id):
        """Sets the usage_measure_id of this SubCustomerResFeeRecordV2.

        |参数名称：使用量度量单位| |参数的约束及描述：使用量度量单位|

        :param usage_measure_id: The usage_measure_id of this SubCustomerResFeeRecordV2.
        :type: int
        """
        self._usage_measure_id = usage_measure_id

    @property
    def free_resource_usage(self):
        """Gets the free_resource_usage of this SubCustomerResFeeRecordV2.

        |参数名称：套餐内使用量。| |参数约束及描述： 套餐内使用量。|

        :return: The free_resource_usage of this SubCustomerResFeeRecordV2.
        :rtype: float
        """
        return self._free_resource_usage

    @free_resource_usage.setter
    def free_resource_usage(self, free_resource_usage):
        """Sets the free_resource_usage of this SubCustomerResFeeRecordV2.

        |参数名称：套餐内使用量。| |参数约束及描述： 套餐内使用量。|

        :param free_resource_usage: The free_resource_usage of this SubCustomerResFeeRecordV2.
        :type: float
        """
        self._free_resource_usage = free_resource_usage

    @property
    def free_resource_measure_id(self):
        """Gets the free_resource_measure_id of this SubCustomerResFeeRecordV2.

        |参数名称：套餐内使用量单位，具体枚举参考：usage_measure_id| |参数的约束及描述：套餐内使用量单位，具体枚举参考：usage_measure_id|

        :return: The free_resource_measure_id of this SubCustomerResFeeRecordV2.
        :rtype: int
        """
        return self._free_resource_measure_id

    @free_resource_measure_id.setter
    def free_resource_measure_id(self, free_resource_measure_id):
        """Sets the free_resource_measure_id of this SubCustomerResFeeRecordV2.

        |参数名称：套餐内使用量单位，具体枚举参考：usage_measure_id| |参数的约束及描述：套餐内使用量单位，具体枚举参考：usage_measure_id|

        :param free_resource_measure_id: The free_resource_measure_id of this SubCustomerResFeeRecordV2.
        :type: int
        """
        self._free_resource_measure_id = free_resource_measure_id

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this SubCustomerResFeeRecordV2.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。| |参数约束及描述：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。|

        :return: The cloud_service_type of this SubCustomerResFeeRecordV2.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this SubCustomerResFeeRecordV2.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。| |参数约束及描述：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。|

        :param cloud_service_type: The cloud_service_type of this SubCustomerResFeeRecordV2.
        :type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def region(self):
        """Gets the region of this SubCustomerResFeeRecordV2.

        |参数名称：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。| |参数约束及描述：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。|

        :return: The region of this SubCustomerResFeeRecordV2.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this SubCustomerResFeeRecordV2.

        |参数名称：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。| |参数约束及描述：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。|

        :param region: The region of this SubCustomerResFeeRecordV2.
        :type: str
        """
        self._region = region

    @property
    def resource_type(self):
        """Gets the resource_type of this SubCustomerResFeeRecordV2.

        |参数名称：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。| |参数约束及描述：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。|

        :return: The resource_type of this SubCustomerResFeeRecordV2.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this SubCustomerResFeeRecordV2.

        |参数名称：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。| |参数约束及描述：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。|

        :param resource_type: The resource_type of this SubCustomerResFeeRecordV2.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def charge_mode(self):
        """Gets the charge_mode of this SubCustomerResFeeRecordV2.

        |参数名称：1 : 包周期；3: 按需。10: 预留实例。| |参数约束及描述：1 : 包周期；3: 按需。10: 预留实例。|

        :return: The charge_mode of this SubCustomerResFeeRecordV2.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this SubCustomerResFeeRecordV2.

        |参数名称：1 : 包周期；3: 按需。10: 预留实例。| |参数约束及描述：1 : 包周期；3: 按需。10: 预留实例。|

        :param charge_mode: The charge_mode of this SubCustomerResFeeRecordV2.
        :type: str
        """
        self._charge_mode = charge_mode

    @property
    def resource_tag(self):
        """Gets the resource_tag of this SubCustomerResFeeRecordV2.

        |参数名称：资源标签。| |参数约束及描述：资源标签。|

        :return: The resource_tag of this SubCustomerResFeeRecordV2.
        :rtype: str
        """
        return self._resource_tag

    @resource_tag.setter
    def resource_tag(self, resource_tag):
        """Sets the resource_tag of this SubCustomerResFeeRecordV2.

        |参数名称：资源标签。| |参数约束及描述：资源标签。|

        :param resource_tag: The resource_tag of this SubCustomerResFeeRecordV2.
        :type: str
        """
        self._resource_tag = resource_tag

    @property
    def resource_name(self):
        """Gets the resource_name of this SubCustomerResFeeRecordV2.

        |参数名称：资源名称。| |参数约束及描述：资源名称。|

        :return: The resource_name of this SubCustomerResFeeRecordV2.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this SubCustomerResFeeRecordV2.

        |参数名称：资源名称。| |参数约束及描述：资源名称。|

        :param resource_name: The resource_name of this SubCustomerResFeeRecordV2.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_id(self):
        """Gets the resource_id of this SubCustomerResFeeRecordV2.

        |参数名称：资源ID。| |参数约束及描述：资源ID。|

        :return: The resource_id of this SubCustomerResFeeRecordV2.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this SubCustomerResFeeRecordV2.

        |参数名称：资源ID。| |参数约束及描述：资源ID。|

        :param resource_id: The resource_id of this SubCustomerResFeeRecordV2.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def bill_type(self):
        """Gets the bill_type of this SubCustomerResFeeRecordV2.

        |参数名称：账单类型。1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿12：消费-按时计费13：消费-退订手续费14：消费-服务支持计划月末扣费16：调账-扣费| |参数的约束及描述：账单类型。1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿12：消费-按时计费13：消费-退订手续费14：消费-服务支持计划月末扣费16：调账-扣费|

        :return: The bill_type of this SubCustomerResFeeRecordV2.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this SubCustomerResFeeRecordV2.

        |参数名称：账单类型。1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿12：消费-按时计费13：消费-退订手续费14：消费-服务支持计划月末扣费16：调账-扣费| |参数的约束及描述：账单类型。1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿12：消费-按时计费13：消费-退订手续费14：消费-服务支持计划月末扣费16：调账-扣费|

        :param bill_type: The bill_type of this SubCustomerResFeeRecordV2.
        :type: int
        """
        self._bill_type = bill_type

    @property
    def period_type(self):
        """Gets the period_type of this SubCustomerResFeeRecordV2.

        |参数名称：周期类型：19：年；20：月；24：天；25：小时；5：分钟；6：秒。| |参数约束及描述：周期类型：19：年；20：月；24：天；25：小时；5：分钟；6：秒。|

        :return: The period_type of this SubCustomerResFeeRecordV2.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this SubCustomerResFeeRecordV2.

        |参数名称：周期类型：19：年；20：月；24：天；25：小时；5：分钟；6：秒。| |参数约束及描述：周期类型：19：年；20：月；24：天；25：小时；5：分钟；6：秒。|

        :param period_type: The period_type of this SubCustomerResFeeRecordV2.
        :type: str
        """
        self._period_type = period_type

    @property
    def product_spec_desc(self):
        """Gets the product_spec_desc of this SubCustomerResFeeRecordV2.

        |参数名称：产品规格描述。| |参数约束及描述：产品规格描述，举例为：普通IO|100.0GB。|

        :return: The product_spec_desc of this SubCustomerResFeeRecordV2.
        :rtype: str
        """
        return self._product_spec_desc

    @product_spec_desc.setter
    def product_spec_desc(self, product_spec_desc):
        """Sets the product_spec_desc of this SubCustomerResFeeRecordV2.

        |参数名称：产品规格描述。| |参数约束及描述：产品规格描述，举例为：普通IO|100.0GB。|

        :param product_spec_desc: The product_spec_desc of this SubCustomerResFeeRecordV2.
        :type: str
        """
        self._product_spec_desc = product_spec_desc

    @property
    def ri_usage(self):
        """Gets the ri_usage of this SubCustomerResFeeRecordV2.

        |参数名称：预留实例使用量。| |参数约束及描述： 预留实例使用量。|

        :return: The ri_usage of this SubCustomerResFeeRecordV2.
        :rtype: float
        """
        return self._ri_usage

    @ri_usage.setter
    def ri_usage(self, ri_usage):
        """Sets the ri_usage of this SubCustomerResFeeRecordV2.

        |参数名称：预留实例使用量。| |参数约束及描述： 预留实例使用量。|

        :param ri_usage: The ri_usage of this SubCustomerResFeeRecordV2.
        :type: float
        """
        self._ri_usage = ri_usage

    @property
    def ri_usage_measure_id(self):
        """Gets the ri_usage_measure_id of this SubCustomerResFeeRecordV2.

        |参数名称：预留实例使用量单位。| |参数的约束及描述：预留实例使用量单位。|

        :return: The ri_usage_measure_id of this SubCustomerResFeeRecordV2.
        :rtype: int
        """
        return self._ri_usage_measure_id

    @ri_usage_measure_id.setter
    def ri_usage_measure_id(self, ri_usage_measure_id):
        """Sets the ri_usage_measure_id of this SubCustomerResFeeRecordV2.

        |参数名称：预留实例使用量单位。| |参数的约束及描述：预留实例使用量单位。|

        :param ri_usage_measure_id: The ri_usage_measure_id of this SubCustomerResFeeRecordV2.
        :type: int
        """
        self._ri_usage_measure_id = ri_usage_measure_id

    @property
    def official_amount(self):
        """Gets the official_amount of this SubCustomerResFeeRecordV2.

        |参数名称：官网价。| |参数约束及描述： 官网价。|

        :return: The official_amount of this SubCustomerResFeeRecordV2.
        :rtype: float
        """
        return self._official_amount

    @official_amount.setter
    def official_amount(self, official_amount):
        """Sets the official_amount of this SubCustomerResFeeRecordV2.

        |参数名称：官网价。| |参数约束及描述： 官网价。|

        :param official_amount: The official_amount of this SubCustomerResFeeRecordV2.
        :type: float
        """
        self._official_amount = official_amount

    @property
    def discount_amount(self):
        """Gets the discount_amount of this SubCustomerResFeeRecordV2.

        |参数名称：折扣金额| |参数约束及描述： 折扣金额|

        :return: The discount_amount of this SubCustomerResFeeRecordV2.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this SubCustomerResFeeRecordV2.

        |参数名称：折扣金额| |参数约束及描述： 折扣金额|

        :param discount_amount: The discount_amount of this SubCustomerResFeeRecordV2.
        :type: float
        """
        self._discount_amount = discount_amount

    @property
    def cash_amount(self):
        """Gets the cash_amount of this SubCustomerResFeeRecordV2.

        |参数名称：现金支付金额| |参数约束及描述： 现金支付金额|

        :return: The cash_amount of this SubCustomerResFeeRecordV2.
        :rtype: float
        """
        return self._cash_amount

    @cash_amount.setter
    def cash_amount(self, cash_amount):
        """Sets the cash_amount of this SubCustomerResFeeRecordV2.

        |参数名称：现金支付金额| |参数约束及描述： 现金支付金额|

        :param cash_amount: The cash_amount of this SubCustomerResFeeRecordV2.
        :type: float
        """
        self._cash_amount = cash_amount

    @property
    def credit_amount(self):
        """Gets the credit_amount of this SubCustomerResFeeRecordV2.

        |参数名称：信用额度支付金额。| |参数约束及描述： 信用额度支付金额。|

        :return: The credit_amount of this SubCustomerResFeeRecordV2.
        :rtype: float
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        """Sets the credit_amount of this SubCustomerResFeeRecordV2.

        |参数名称：信用额度支付金额。| |参数约束及描述： 信用额度支付金额。|

        :param credit_amount: The credit_amount of this SubCustomerResFeeRecordV2.
        :type: float
        """
        self._credit_amount = credit_amount

    @property
    def coupon_amount(self):
        """Gets the coupon_amount of this SubCustomerResFeeRecordV2.

        |参数名称：代金券支付金额。| |参数约束及描述： 代金券支付金额。|

        :return: The coupon_amount of this SubCustomerResFeeRecordV2.
        :rtype: float
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        """Sets the coupon_amount of this SubCustomerResFeeRecordV2.

        |参数名称：代金券支付金额。| |参数约束及描述： 代金券支付金额。|

        :param coupon_amount: The coupon_amount of this SubCustomerResFeeRecordV2.
        :type: float
        """
        self._coupon_amount = coupon_amount

    @property
    def flexipurchase_coupon_amount(self):
        """Gets the flexipurchase_coupon_amount of this SubCustomerResFeeRecordV2.

        |参数名称：现金券支付金额。| |参数约束及描述： 现金券支付金额。|

        :return: The flexipurchase_coupon_amount of this SubCustomerResFeeRecordV2.
        :rtype: float
        """
        return self._flexipurchase_coupon_amount

    @flexipurchase_coupon_amount.setter
    def flexipurchase_coupon_amount(self, flexipurchase_coupon_amount):
        """Sets the flexipurchase_coupon_amount of this SubCustomerResFeeRecordV2.

        |参数名称：现金券支付金额。| |参数约束及描述： 现金券支付金额。|

        :param flexipurchase_coupon_amount: The flexipurchase_coupon_amount of this SubCustomerResFeeRecordV2.
        :type: float
        """
        self._flexipurchase_coupon_amount = flexipurchase_coupon_amount

    @property
    def stored_card_amount(self):
        """Gets the stored_card_amount of this SubCustomerResFeeRecordV2.

        |参数名称：储值卡支付金额。| |参数约束及描述： 储值卡支付金额。|

        :return: The stored_card_amount of this SubCustomerResFeeRecordV2.
        :rtype: float
        """
        return self._stored_card_amount

    @stored_card_amount.setter
    def stored_card_amount(self, stored_card_amount):
        """Sets the stored_card_amount of this SubCustomerResFeeRecordV2.

        |参数名称：储值卡支付金额。| |参数约束及描述： 储值卡支付金额。|

        :param stored_card_amount: The stored_card_amount of this SubCustomerResFeeRecordV2.
        :type: float
        """
        self._stored_card_amount = stored_card_amount

    @property
    def bonus_amount(self):
        """Gets the bonus_amount of this SubCustomerResFeeRecordV2.

        |参数名称：奖励金支付金额（用于现网未清干净的奖励金）。| |参数约束及描述： 奖励金支付金额（用于现网未清干净的奖励金）。|

        :return: The bonus_amount of this SubCustomerResFeeRecordV2.
        :rtype: float
        """
        return self._bonus_amount

    @bonus_amount.setter
    def bonus_amount(self, bonus_amount):
        """Sets the bonus_amount of this SubCustomerResFeeRecordV2.

        |参数名称：奖励金支付金额（用于现网未清干净的奖励金）。| |参数约束及描述： 奖励金支付金额（用于现网未清干净的奖励金）。|

        :param bonus_amount: The bonus_amount of this SubCustomerResFeeRecordV2.
        :type: float
        """
        self._bonus_amount = bonus_amount

    @property
    def debt_amount(self):
        """Gets the debt_amount of this SubCustomerResFeeRecordV2.

        |参数名称：欠费金额。| |参数约束及描述： 欠费金额。|

        :return: The debt_amount of this SubCustomerResFeeRecordV2.
        :rtype: float
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        """Sets the debt_amount of this SubCustomerResFeeRecordV2.

        |参数名称：欠费金额。| |参数约束及描述： 欠费金额。|

        :param debt_amount: The debt_amount of this SubCustomerResFeeRecordV2.
        :type: float
        """
        self._debt_amount = debt_amount

    @property
    def adjustment_amount(self):
        """Gets the adjustment_amount of this SubCustomerResFeeRecordV2.

        |参数名称：欠费核销金额。| |参数约束及描述： 欠费核销金额。|

        :return: The adjustment_amount of this SubCustomerResFeeRecordV2.
        :rtype: float
        """
        return self._adjustment_amount

    @adjustment_amount.setter
    def adjustment_amount(self, adjustment_amount):
        """Sets the adjustment_amount of this SubCustomerResFeeRecordV2.

        |参数名称：欠费核销金额。| |参数约束及描述： 欠费核销金额。|

        :param adjustment_amount: The adjustment_amount of this SubCustomerResFeeRecordV2.
        :type: float
        """
        self._adjustment_amount = adjustment_amount

    @property
    def spec_size(self):
        """Gets the spec_size of this SubCustomerResFeeRecordV2.

        |参数名称：线性大小| |参数约束及描述： 线性大小|

        :return: The spec_size of this SubCustomerResFeeRecordV2.
        :rtype: float
        """
        return self._spec_size

    @spec_size.setter
    def spec_size(self, spec_size):
        """Sets the spec_size of this SubCustomerResFeeRecordV2.

        |参数名称：线性大小| |参数约束及描述： 线性大小|

        :param spec_size: The spec_size of this SubCustomerResFeeRecordV2.
        :type: float
        """
        self._spec_size = spec_size

    @property
    def spec_size_measure_id(self):
        """Gets the spec_size_measure_id of this SubCustomerResFeeRecordV2.

        |参数名称：线性大小单位| |参数的约束及描述：线性大小单位|

        :return: The spec_size_measure_id of this SubCustomerResFeeRecordV2.
        :rtype: int
        """
        return self._spec_size_measure_id

    @spec_size_measure_id.setter
    def spec_size_measure_id(self, spec_size_measure_id):
        """Sets the spec_size_measure_id of this SubCustomerResFeeRecordV2.

        |参数名称：线性大小单位| |参数的约束及描述：线性大小单位|

        :param spec_size_measure_id: The spec_size_measure_id of this SubCustomerResFeeRecordV2.
        :type: int
        """
        self._spec_size_measure_id = spec_size_measure_id

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
        if not isinstance(other, SubCustomerResFeeRecordV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
