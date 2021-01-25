# coding: utf-8

import pprint
import re

import six





class ResFeeRecordV2:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bill_date': 'str',
        'bill_type': 'int',
        'customer_id': 'str',
        'region': 'str',
        'region_name': 'str',
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'effective_time': 'str',
        'expire_time': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_tag': 'str',
        'product_id': 'str',
        'product_name': 'str',
        'product_spec_desc': 'str',
        'sku_code': 'str',
        'spec_size': 'float',
        'spec_size_measure_id': 'int',
        'trade_id': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'charge_mode': 'str',
        'order_id': 'str',
        'period_type': 'str',
        'usage_type': 'str',
        'usage': 'float',
        'usage_measure_id': 'int',
        'free_resource_usage': 'float',
        'free_resource_measure_id': 'int',
        'ri_usage': 'float',
        'ri_usage_measure_id': 'int',
        'unit_price': 'float',
        'unit': 'str',
        'official_amount': 'float',
        'discount_amount': 'float',
        'amount': 'float',
        'cash_amount': 'float',
        'credit_amount': 'float',
        'coupon_amount': 'float',
        'flexipurchase_coupon_amount': 'float',
        'stored_card_amount': 'float',
        'bonus_amount': 'float',
        'debt_amount': 'float',
        'adjustment_amount': 'float',
        'measure_id': 'int'
    }

    attribute_map = {
        'bill_date': 'bill_date',
        'bill_type': 'bill_type',
        'customer_id': 'customer_id',
        'region': 'region',
        'region_name': 'region_name',
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_tag': 'resource_tag',
        'product_id': 'product_id',
        'product_name': 'product_name',
        'product_spec_desc': 'product_spec_desc',
        'sku_code': 'sku_code',
        'spec_size': 'spec_size',
        'spec_size_measure_id': 'spec_size_measure_id',
        'trade_id': 'trade_id',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'charge_mode': 'charge_mode',
        'order_id': 'order_id',
        'period_type': 'period_type',
        'usage_type': 'usage_type',
        'usage': 'usage',
        'usage_measure_id': 'usage_measure_id',
        'free_resource_usage': 'free_resource_usage',
        'free_resource_measure_id': 'free_resource_measure_id',
        'ri_usage': 'ri_usage',
        'ri_usage_measure_id': 'ri_usage_measure_id',
        'unit_price': 'unit_price',
        'unit': 'unit',
        'official_amount': 'official_amount',
        'discount_amount': 'discount_amount',
        'amount': 'amount',
        'cash_amount': 'cash_amount',
        'credit_amount': 'credit_amount',
        'coupon_amount': 'coupon_amount',
        'flexipurchase_coupon_amount': 'flexipurchase_coupon_amount',
        'stored_card_amount': 'stored_card_amount',
        'bonus_amount': 'bonus_amount',
        'debt_amount': 'debt_amount',
        'adjustment_amount': 'adjustment_amount',
        'measure_id': 'measure_id'
    }

    def __init__(self, bill_date=None, bill_type=None, customer_id=None, region=None, region_name=None, cloud_service_type=None, resource_type=None, effective_time=None, expire_time=None, resource_id=None, resource_name=None, resource_tag=None, product_id=None, product_name=None, product_spec_desc=None, sku_code=None, spec_size=None, spec_size_measure_id=None, trade_id=None, enterprise_project_id=None, enterprise_project_name=None, charge_mode=None, order_id=None, period_type=None, usage_type=None, usage=None, usage_measure_id=None, free_resource_usage=None, free_resource_measure_id=None, ri_usage=None, ri_usage_measure_id=None, unit_price=None, unit=None, official_amount=None, discount_amount=None, amount=None, cash_amount=None, credit_amount=None, coupon_amount=None, flexipurchase_coupon_amount=None, stored_card_amount=None, bonus_amount=None, debt_amount=None, adjustment_amount=None, measure_id=None):
        """ResFeeRecordV2 - a model defined in huaweicloud sdk"""
        
        

        self._bill_date = None
        self._bill_type = None
        self._customer_id = None
        self._region = None
        self._region_name = None
        self._cloud_service_type = None
        self._resource_type = None
        self._effective_time = None
        self._expire_time = None
        self._resource_id = None
        self._resource_name = None
        self._resource_tag = None
        self._product_id = None
        self._product_name = None
        self._product_spec_desc = None
        self._sku_code = None
        self._spec_size = None
        self._spec_size_measure_id = None
        self._trade_id = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._charge_mode = None
        self._order_id = None
        self._period_type = None
        self._usage_type = None
        self._usage = None
        self._usage_measure_id = None
        self._free_resource_usage = None
        self._free_resource_measure_id = None
        self._ri_usage = None
        self._ri_usage_measure_id = None
        self._unit_price = None
        self._unit = None
        self._official_amount = None
        self._discount_amount = None
        self._amount = None
        self._cash_amount = None
        self._credit_amount = None
        self._coupon_amount = None
        self._flexipurchase_coupon_amount = None
        self._stored_card_amount = None
        self._bonus_amount = None
        self._debt_amount = None
        self._adjustment_amount = None
        self._measure_id = None
        self.discriminator = None

        if bill_date is not None:
            self.bill_date = bill_date
        if bill_type is not None:
            self.bill_type = bill_type
        if customer_id is not None:
            self.customer_id = customer_id
        if region is not None:
            self.region = region
        if region_name is not None:
            self.region_name = region_name
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if resource_type is not None:
            self.resource_type = resource_type
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_tag is not None:
            self.resource_tag = resource_tag
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if product_spec_desc is not None:
            self.product_spec_desc = product_spec_desc
        if sku_code is not None:
            self.sku_code = sku_code
        if spec_size is not None:
            self.spec_size = spec_size
        if spec_size_measure_id is not None:
            self.spec_size_measure_id = spec_size_measure_id
        if trade_id is not None:
            self.trade_id = trade_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if order_id is not None:
            self.order_id = order_id
        if period_type is not None:
            self.period_type = period_type
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
        if ri_usage is not None:
            self.ri_usage = ri_usage
        if ri_usage_measure_id is not None:
            self.ri_usage_measure_id = ri_usage_measure_id
        if unit_price is not None:
            self.unit_price = unit_price
        if unit is not None:
            self.unit = unit
        if official_amount is not None:
            self.official_amount = official_amount
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if amount is not None:
            self.amount = amount
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
        if measure_id is not None:
            self.measure_id = measure_id

    @property
    def bill_date(self):
        """Gets the bill_date of this ResFeeRecordV2.

        |参数名称：消费记录日期：格式：YYYY-MM-DD。按照东八区截取| |参数约束及描述：消费记录日期：格式：YYYY-MM-DD。按照东八区截取|

        :return: The bill_date of this ResFeeRecordV2.
        :rtype: str
        """
        return self._bill_date

    @bill_date.setter
    def bill_date(self, bill_date):
        """Sets the bill_date of this ResFeeRecordV2.

        |参数名称：消费记录日期：格式：YYYY-MM-DD。按照东八区截取| |参数约束及描述：消费记录日期：格式：YYYY-MM-DD。按照东八区截取|

        :param bill_date: The bill_date of this ResFeeRecordV2.
        :type: str
        """
        self._bill_date = bill_date

    @property
    def bill_type(self):
        """Gets the bill_type of this ResFeeRecordV2.

        |参数名称：账单类型。1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿12：消费-按时计费13：消费-退订手续费14：消费-服务支持计划月末扣费16：调账-扣费| |参数的约束及描述：账单类型。1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿12：消费-按时计费13：消费-退订手续费14：消费-服务支持计划月末扣费 15消费-税金16：调账-扣费17：消费-保底差额 100：退款-退订税金 101：调账-补偿税金 102：调账-扣费税金|

        :return: The bill_type of this ResFeeRecordV2.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this ResFeeRecordV2.

        |参数名称：账单类型。1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿12：消费-按时计费13：消费-退订手续费14：消费-服务支持计划月末扣费16：调账-扣费| |参数的约束及描述：账单类型。1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿12：消费-按时计费13：消费-退订手续费14：消费-服务支持计划月末扣费 15消费-税金16：调账-扣费17：消费-保底差额 100：退款-退订税金 101：调账-补偿税金 102：调账-扣费税金|

        :param bill_type: The bill_type of this ResFeeRecordV2.
        :type: int
        """
        self._bill_type = bill_type

    @property
    def customer_id(self):
        """Gets the customer_id of this ResFeeRecordV2.

        |参数名称：消费的客户账号ID。| |参数约束及描述：如果是查询自己，这个地方是自身的ID; 如果是查询某个企业子客户，这个地方是企业子客户ID如果是查询以及下面的所有子客户，这个地方是消费的实际客户ID; 如果是企业主自身消费，为企业主ID，如果这条消费记录是某个企业子客户的消费，这个地方的ID是企业子账号ID。|

        :return: The customer_id of this ResFeeRecordV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ResFeeRecordV2.

        |参数名称：消费的客户账号ID。| |参数约束及描述：如果是查询自己，这个地方是自身的ID; 如果是查询某个企业子客户，这个地方是企业子客户ID如果是查询以及下面的所有子客户，这个地方是消费的实际客户ID; 如果是企业主自身消费，为企业主ID，如果这条消费记录是某个企业子客户的消费，这个地方的ID是企业子账号ID。|

        :param customer_id: The customer_id of this ResFeeRecordV2.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def region(self):
        """Gets the region of this ResFeeRecordV2.

        |参数名称：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。| |参数约束及描述：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。|

        :return: The region of this ResFeeRecordV2.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ResFeeRecordV2.

        |参数名称：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。| |参数约束及描述：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。|

        :param region: The region of this ResFeeRecordV2.
        :type: str
        """
        self._region = region

    @property
    def region_name(self):
        """Gets the region_name of this ResFeeRecordV2.

        |参数名称：云服务区名称| |参数约束及描述：云服务区名称|

        :return: The region_name of this ResFeeRecordV2.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this ResFeeRecordV2.

        |参数名称：云服务区名称| |参数约束及描述：云服务区名称|

        :param region_name: The region_name of this ResFeeRecordV2.
        :type: str
        """
        self._region_name = region_name

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this ResFeeRecordV2.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。| |参数约束及描述：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。|

        :return: The cloud_service_type of this ResFeeRecordV2.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this ResFeeRecordV2.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。| |参数约束及描述：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。|

        :param cloud_service_type: The cloud_service_type of this ResFeeRecordV2.
        :type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        """Gets the resource_type of this ResFeeRecordV2.

        |参数名称：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。| |参数约束及描述：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。|

        :return: The resource_type of this ResFeeRecordV2.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ResFeeRecordV2.

        |参数名称：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。| |参数约束及描述：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。|

        :param resource_type: The resource_type of this ResFeeRecordV2.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def effective_time(self):
        """Gets the effective_time of this ResFeeRecordV2.

        |参数名称：费用对应的资源使用的开始时间，按需有效，包周期该字段保留。| |参数约束及描述：费用对应的资源使用的开始时间，按需有效，包周期该字段保留。|

        :return: The effective_time of this ResFeeRecordV2.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        """Sets the effective_time of this ResFeeRecordV2.

        |参数名称：费用对应的资源使用的开始时间，按需有效，包周期该字段保留。| |参数约束及描述：费用对应的资源使用的开始时间，按需有效，包周期该字段保留。|

        :param effective_time: The effective_time of this ResFeeRecordV2.
        :type: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        """Gets the expire_time of this ResFeeRecordV2.

        |参数名称：费用对应的资源使用的结束时间，按需有效，包周期该字段保留。| |参数约束及描述：费用对应的资源使用的结束时间，按需有效，包周期该字段保留。|

        :return: The expire_time of this ResFeeRecordV2.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this ResFeeRecordV2.

        |参数名称：费用对应的资源使用的结束时间，按需有效，包周期该字段保留。| |参数约束及描述：费用对应的资源使用的结束时间，按需有效，包周期该字段保留。|

        :param expire_time: The expire_time of this ResFeeRecordV2.
        :type: str
        """
        self._expire_time = expire_time

    @property
    def resource_id(self):
        """Gets the resource_id of this ResFeeRecordV2.

        |参数名称：资源ID。| |参数约束及描述：资源ID。|

        :return: The resource_id of this ResFeeRecordV2.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ResFeeRecordV2.

        |参数名称：资源ID。| |参数约束及描述：资源ID。|

        :param resource_id: The resource_id of this ResFeeRecordV2.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this ResFeeRecordV2.

        |参数名称：资源名称。| |参数约束及描述：资源名称。|

        :return: The resource_name of this ResFeeRecordV2.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ResFeeRecordV2.

        |参数名称：资源名称。| |参数约束及描述：资源名称。|

        :param resource_name: The resource_name of this ResFeeRecordV2.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_tag(self):
        """Gets the resource_tag of this ResFeeRecordV2.

        |参数名称：资源标签。| |参数约束及描述：资源标签。|

        :return: The resource_tag of this ResFeeRecordV2.
        :rtype: str
        """
        return self._resource_tag

    @resource_tag.setter
    def resource_tag(self, resource_tag):
        """Sets the resource_tag of this ResFeeRecordV2.

        |参数名称：资源标签。| |参数约束及描述：资源标签。|

        :param resource_tag: The resource_tag of this ResFeeRecordV2.
        :type: str
        """
        self._resource_tag = resource_tag

    @property
    def product_id(self):
        """Gets the product_id of this ResFeeRecordV2.

        |参数名称：产品ID。| |参数约束及描述：产品ID。|

        :return: The product_id of this ResFeeRecordV2.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ResFeeRecordV2.

        |参数名称：产品ID。| |参数约束及描述：产品ID。|

        :param product_id: The product_id of this ResFeeRecordV2.
        :type: str
        """
        self._product_id = product_id

    @property
    def product_name(self):
        """Gets the product_name of this ResFeeRecordV2.

        |参数名称：产品名称。| |参数约束及描述：产品名称。|

        :return: The product_name of this ResFeeRecordV2.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this ResFeeRecordV2.

        |参数名称：产品名称。| |参数约束及描述：产品名称。|

        :param product_name: The product_name of this ResFeeRecordV2.
        :type: str
        """
        self._product_name = product_name

    @property
    def product_spec_desc(self):
        """Gets the product_spec_desc of this ResFeeRecordV2.

        |参数名称：产品规格描述。| |参数约束及描述：产品规格描述，举例为：普通IO|100.0GB。|

        :return: The product_spec_desc of this ResFeeRecordV2.
        :rtype: str
        """
        return self._product_spec_desc

    @product_spec_desc.setter
    def product_spec_desc(self, product_spec_desc):
        """Sets the product_spec_desc of this ResFeeRecordV2.

        |参数名称：产品规格描述。| |参数约束及描述：产品规格描述，举例为：普通IO|100.0GB。|

        :param product_spec_desc: The product_spec_desc of this ResFeeRecordV2.
        :type: str
        """
        self._product_spec_desc = product_spec_desc

    @property
    def sku_code(self):
        """Gets the sku_code of this ResFeeRecordV2.

        |参数名称：sku编码| |参数约束及描述：sku编码|

        :return: The sku_code of this ResFeeRecordV2.
        :rtype: str
        """
        return self._sku_code

    @sku_code.setter
    def sku_code(self, sku_code):
        """Sets the sku_code of this ResFeeRecordV2.

        |参数名称：sku编码| |参数约束及描述：sku编码|

        :param sku_code: The sku_code of this ResFeeRecordV2.
        :type: str
        """
        self._sku_code = sku_code

    @property
    def spec_size(self):
        """Gets the spec_size of this ResFeeRecordV2.

        |参数名称：线性大小| |参数约束及描述： 线性大小|

        :return: The spec_size of this ResFeeRecordV2.
        :rtype: float
        """
        return self._spec_size

    @spec_size.setter
    def spec_size(self, spec_size):
        """Sets the spec_size of this ResFeeRecordV2.

        |参数名称：线性大小| |参数约束及描述： 线性大小|

        :param spec_size: The spec_size of this ResFeeRecordV2.
        :type: float
        """
        self._spec_size = spec_size

    @property
    def spec_size_measure_id(self):
        """Gets the spec_size_measure_id of this ResFeeRecordV2.

        |参数名称：线性大小单位| |参数的约束及描述：线性大小单位|

        :return: The spec_size_measure_id of this ResFeeRecordV2.
        :rtype: int
        """
        return self._spec_size_measure_id

    @spec_size_measure_id.setter
    def spec_size_measure_id(self, spec_size_measure_id):
        """Sets the spec_size_measure_id of this ResFeeRecordV2.

        |参数名称：线性大小单位| |参数的约束及描述：线性大小单位|

        :param spec_size_measure_id: The spec_size_measure_id of this ResFeeRecordV2.
        :type: int
        """
        self._spec_size_measure_id = spec_size_measure_id

    @property
    def trade_id(self):
        """Gets the trade_id of this ResFeeRecordV2.

        |参数名称：订单ID 或 交易ID，扣费维度的唯一标识| |参数约束及描述：订单ID 或 交易ID，扣费维度的唯一标识|

        :return: The trade_id of this ResFeeRecordV2.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """Sets the trade_id of this ResFeeRecordV2.

        |参数名称：订单ID 或 交易ID，扣费维度的唯一标识| |参数约束及描述：订单ID 或 交易ID，扣费维度的唯一标识|

        :param trade_id: The trade_id of this ResFeeRecordV2.
        :type: str
        """
        self._trade_id = trade_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ResFeeRecordV2.

        |参数名称：企业项目ID。| |参数约束及描述：企业项目ID。|

        :return: The enterprise_project_id of this ResFeeRecordV2.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ResFeeRecordV2.

        |参数名称：企业项目ID。| |参数约束及描述：企业项目ID。|

        :param enterprise_project_id: The enterprise_project_id of this ResFeeRecordV2.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this ResFeeRecordV2.

        |参数名称：企业项目名称。| |参数约束及描述：企业项目名称。|

        :return: The enterprise_project_name of this ResFeeRecordV2.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this ResFeeRecordV2.

        |参数名称：企业项目名称。| |参数约束及描述：企业项目名称。|

        :param enterprise_project_name: The enterprise_project_name of this ResFeeRecordV2.
        :type: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ResFeeRecordV2.

        |参数名称：1 : 包周期；3: 按需。10: 预留实例。| |参数约束及描述：1 : 包周期；3: 按需。10: 预留实例。|

        :return: The charge_mode of this ResFeeRecordV2.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ResFeeRecordV2.

        |参数名称：1 : 包周期；3: 按需。10: 预留实例。| |参数约束及描述：1 : 包周期；3: 按需。10: 预留实例。|

        :param charge_mode: The charge_mode of this ResFeeRecordV2.
        :type: str
        """
        self._charge_mode = charge_mode

    @property
    def order_id(self):
        """Gets the order_id of this ResFeeRecordV2.

        |参数名称：订单ID，包周期资源使用记录才有该字段，按需资源为空。| |参数约束及描述：订单ID，包周期资源使用记录才有该字段，按需资源为空。|

        :return: The order_id of this ResFeeRecordV2.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ResFeeRecordV2.

        |参数名称：订单ID，包周期资源使用记录才有该字段，按需资源为空。| |参数约束及描述：订单ID，包周期资源使用记录才有该字段，按需资源为空。|

        :param order_id: The order_id of this ResFeeRecordV2.
        :type: str
        """
        self._order_id = order_id

    @property
    def period_type(self):
        """Gets the period_type of this ResFeeRecordV2.

        |参数名称：周期类型：19：年；20：月；24：天；25：小时；5：分钟；6：秒。| |参数约束及描述：周期类型：19：年；20：月；24：天；25：小时；5：分钟；6：秒。|

        :return: The period_type of this ResFeeRecordV2.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this ResFeeRecordV2.

        |参数名称：周期类型：19：年；20：月；24：天；25：小时；5：分钟；6：秒。| |参数约束及描述：周期类型：19：年；20：月；24：天；25：小时；5：分钟；6：秒。|

        :param period_type: The period_type of this ResFeeRecordV2.
        :type: str
        """
        self._period_type = period_type

    @property
    def usage_type(self):
        """Gets the usage_type of this ResFeeRecordV2.

        |参数名称：使用量类型| |参数约束及描述：使用量类型|

        :return: The usage_type of this ResFeeRecordV2.
        :rtype: str
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        """Sets the usage_type of this ResFeeRecordV2.

        |参数名称：使用量类型| |参数约束及描述：使用量类型|

        :param usage_type: The usage_type of this ResFeeRecordV2.
        :type: str
        """
        self._usage_type = usage_type

    @property
    def usage(self):
        """Gets the usage of this ResFeeRecordV2.

        |参数名称：使用量。| |参数约束及描述： 使用量。|

        :return: The usage of this ResFeeRecordV2.
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this ResFeeRecordV2.

        |参数名称：使用量。| |参数约束及描述： 使用量。|

        :param usage: The usage of this ResFeeRecordV2.
        :type: float
        """
        self._usage = usage

    @property
    def usage_measure_id(self):
        """Gets the usage_measure_id of this ResFeeRecordV2.

        |参数名称：使用量度量单位| |参数的约束及描述：使用量度量单位|

        :return: The usage_measure_id of this ResFeeRecordV2.
        :rtype: int
        """
        return self._usage_measure_id

    @usage_measure_id.setter
    def usage_measure_id(self, usage_measure_id):
        """Sets the usage_measure_id of this ResFeeRecordV2.

        |参数名称：使用量度量单位| |参数的约束及描述：使用量度量单位|

        :param usage_measure_id: The usage_measure_id of this ResFeeRecordV2.
        :type: int
        """
        self._usage_measure_id = usage_measure_id

    @property
    def free_resource_usage(self):
        """Gets the free_resource_usage of this ResFeeRecordV2.

        |参数名称：套餐内使用量。| |参数约束及描述： 套餐内使用量。|

        :return: The free_resource_usage of this ResFeeRecordV2.
        :rtype: float
        """
        return self._free_resource_usage

    @free_resource_usage.setter
    def free_resource_usage(self, free_resource_usage):
        """Sets the free_resource_usage of this ResFeeRecordV2.

        |参数名称：套餐内使用量。| |参数约束及描述： 套餐内使用量。|

        :param free_resource_usage: The free_resource_usage of this ResFeeRecordV2.
        :type: float
        """
        self._free_resource_usage = free_resource_usage

    @property
    def free_resource_measure_id(self):
        """Gets the free_resource_measure_id of this ResFeeRecordV2.

        |参数名称：套餐内使用量单位，具体枚举参考：usageMeasureId| |参数的约束及描述：套餐内使用量单位，具体枚举参考：usageMeasureId|

        :return: The free_resource_measure_id of this ResFeeRecordV2.
        :rtype: int
        """
        return self._free_resource_measure_id

    @free_resource_measure_id.setter
    def free_resource_measure_id(self, free_resource_measure_id):
        """Sets the free_resource_measure_id of this ResFeeRecordV2.

        |参数名称：套餐内使用量单位，具体枚举参考：usageMeasureId| |参数的约束及描述：套餐内使用量单位，具体枚举参考：usageMeasureId|

        :param free_resource_measure_id: The free_resource_measure_id of this ResFeeRecordV2.
        :type: int
        """
        self._free_resource_measure_id = free_resource_measure_id

    @property
    def ri_usage(self):
        """Gets the ri_usage of this ResFeeRecordV2.

        |参数名称：预留实例使用量。| |参数约束及描述： 预留实例使用量。|

        :return: The ri_usage of this ResFeeRecordV2.
        :rtype: float
        """
        return self._ri_usage

    @ri_usage.setter
    def ri_usage(self, ri_usage):
        """Sets the ri_usage of this ResFeeRecordV2.

        |参数名称：预留实例使用量。| |参数约束及描述： 预留实例使用量。|

        :param ri_usage: The ri_usage of this ResFeeRecordV2.
        :type: float
        """
        self._ri_usage = ri_usage

    @property
    def ri_usage_measure_id(self):
        """Gets the ri_usage_measure_id of this ResFeeRecordV2.

        |参数名称：预留实例使用量单位。| |参数的约束及描述：预留实例使用量单位。|

        :return: The ri_usage_measure_id of this ResFeeRecordV2.
        :rtype: int
        """
        return self._ri_usage_measure_id

    @ri_usage_measure_id.setter
    def ri_usage_measure_id(self, ri_usage_measure_id):
        """Sets the ri_usage_measure_id of this ResFeeRecordV2.

        |参数名称：预留实例使用量单位。| |参数的约束及描述：预留实例使用量单位。|

        :param ri_usage_measure_id: The ri_usage_measure_id of this ResFeeRecordV2.
        :type: int
        """
        self._ri_usage_measure_id = ri_usage_measure_id

    @property
    def unit_price(self):
        """Gets the unit_price of this ResFeeRecordV2.

        |参数名称：单价| |参数约束及描述：单价|

        :return: The unit_price of this ResFeeRecordV2.
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this ResFeeRecordV2.

        |参数名称：单价| |参数约束及描述：单价|

        :param unit_price: The unit_price of this ResFeeRecordV2.
        :type: float
        """
        self._unit_price = unit_price

    @property
    def unit(self):
        """Gets the unit of this ResFeeRecordV2.

        |参数名称：单价单位| |参数约束及描述：单价单位|

        :return: The unit of this ResFeeRecordV2.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ResFeeRecordV2.

        |参数名称：单价单位| |参数约束及描述：单价单位|

        :param unit: The unit of this ResFeeRecordV2.
        :type: str
        """
        self._unit = unit

    @property
    def official_amount(self):
        """Gets the official_amount of this ResFeeRecordV2.

        |参数名称：官网价。| |参数约束及描述： 官网价。|

        :return: The official_amount of this ResFeeRecordV2.
        :rtype: float
        """
        return self._official_amount

    @official_amount.setter
    def official_amount(self, official_amount):
        """Sets the official_amount of this ResFeeRecordV2.

        |参数名称：官网价。| |参数约束及描述： 官网价。|

        :param official_amount: The official_amount of this ResFeeRecordV2.
        :type: float
        """
        self._official_amount = official_amount

    @property
    def discount_amount(self):
        """Gets the discount_amount of this ResFeeRecordV2.

        |参数名称：折扣金额| |参数约束及描述： 折扣金额|

        :return: The discount_amount of this ResFeeRecordV2.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this ResFeeRecordV2.

        |参数名称：折扣金额| |参数约束及描述： 折扣金额|

        :param discount_amount: The discount_amount of this ResFeeRecordV2.
        :type: float
        """
        self._discount_amount = discount_amount

    @property
    def amount(self):
        """Gets the amount of this ResFeeRecordV2.

        |参数名称：消费金额，包括现金券和代金券金额，精确到小数点后2位。| |参数约束及描述： 消费金额，包括现金券和代金券金额，精确到小数点后2位。|

        :return: The amount of this ResFeeRecordV2.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ResFeeRecordV2.

        |参数名称：消费金额，包括现金券和代金券金额，精确到小数点后2位。| |参数约束及描述： 消费金额，包括现金券和代金券金额，精确到小数点后2位。|

        :param amount: The amount of this ResFeeRecordV2.
        :type: float
        """
        self._amount = amount

    @property
    def cash_amount(self):
        """Gets the cash_amount of this ResFeeRecordV2.

        |参数名称：现金支付金额| |参数约束及描述： 现金支付金额|

        :return: The cash_amount of this ResFeeRecordV2.
        :rtype: float
        """
        return self._cash_amount

    @cash_amount.setter
    def cash_amount(self, cash_amount):
        """Sets the cash_amount of this ResFeeRecordV2.

        |参数名称：现金支付金额| |参数约束及描述： 现金支付金额|

        :param cash_amount: The cash_amount of this ResFeeRecordV2.
        :type: float
        """
        self._cash_amount = cash_amount

    @property
    def credit_amount(self):
        """Gets the credit_amount of this ResFeeRecordV2.

        |参数名称：信用额度支付金额。| |参数约束及描述： 信用额度支付金额。|

        :return: The credit_amount of this ResFeeRecordV2.
        :rtype: float
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        """Sets the credit_amount of this ResFeeRecordV2.

        |参数名称：信用额度支付金额。| |参数约束及描述： 信用额度支付金额。|

        :param credit_amount: The credit_amount of this ResFeeRecordV2.
        :type: float
        """
        self._credit_amount = credit_amount

    @property
    def coupon_amount(self):
        """Gets the coupon_amount of this ResFeeRecordV2.

        |参数名称：代金券支付金额。| |参数约束及描述： 代金券支付金额。|

        :return: The coupon_amount of this ResFeeRecordV2.
        :rtype: float
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        """Sets the coupon_amount of this ResFeeRecordV2.

        |参数名称：代金券支付金额。| |参数约束及描述： 代金券支付金额。|

        :param coupon_amount: The coupon_amount of this ResFeeRecordV2.
        :type: float
        """
        self._coupon_amount = coupon_amount

    @property
    def flexipurchase_coupon_amount(self):
        """Gets the flexipurchase_coupon_amount of this ResFeeRecordV2.

        |参数名称：现金券支付金额。| |参数约束及描述： 现金券支付金额。|

        :return: The flexipurchase_coupon_amount of this ResFeeRecordV2.
        :rtype: float
        """
        return self._flexipurchase_coupon_amount

    @flexipurchase_coupon_amount.setter
    def flexipurchase_coupon_amount(self, flexipurchase_coupon_amount):
        """Sets the flexipurchase_coupon_amount of this ResFeeRecordV2.

        |参数名称：现金券支付金额。| |参数约束及描述： 现金券支付金额。|

        :param flexipurchase_coupon_amount: The flexipurchase_coupon_amount of this ResFeeRecordV2.
        :type: float
        """
        self._flexipurchase_coupon_amount = flexipurchase_coupon_amount

    @property
    def stored_card_amount(self):
        """Gets the stored_card_amount of this ResFeeRecordV2.

        |参数名称：储值卡支付金额。| |参数约束及描述： 储值卡支付金额。|

        :return: The stored_card_amount of this ResFeeRecordV2.
        :rtype: float
        """
        return self._stored_card_amount

    @stored_card_amount.setter
    def stored_card_amount(self, stored_card_amount):
        """Sets the stored_card_amount of this ResFeeRecordV2.

        |参数名称：储值卡支付金额。| |参数约束及描述： 储值卡支付金额。|

        :param stored_card_amount: The stored_card_amount of this ResFeeRecordV2.
        :type: float
        """
        self._stored_card_amount = stored_card_amount

    @property
    def bonus_amount(self):
        """Gets the bonus_amount of this ResFeeRecordV2.

        |参数名称：奖励金支付金额（用于现网未清干净的奖励金）。| |参数约束及描述： 奖励金支付金额（用于现网未清干净的奖励金）。|

        :return: The bonus_amount of this ResFeeRecordV2.
        :rtype: float
        """
        return self._bonus_amount

    @bonus_amount.setter
    def bonus_amount(self, bonus_amount):
        """Sets the bonus_amount of this ResFeeRecordV2.

        |参数名称：奖励金支付金额（用于现网未清干净的奖励金）。| |参数约束及描述： 奖励金支付金额（用于现网未清干净的奖励金）。|

        :param bonus_amount: The bonus_amount of this ResFeeRecordV2.
        :type: float
        """
        self._bonus_amount = bonus_amount

    @property
    def debt_amount(self):
        """Gets the debt_amount of this ResFeeRecordV2.

        |参数名称：欠费金额。| |参数约束及描述： 欠费金额。|

        :return: The debt_amount of this ResFeeRecordV2.
        :rtype: float
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        """Sets the debt_amount of this ResFeeRecordV2.

        |参数名称：欠费金额。| |参数约束及描述： 欠费金额。|

        :param debt_amount: The debt_amount of this ResFeeRecordV2.
        :type: float
        """
        self._debt_amount = debt_amount

    @property
    def adjustment_amount(self):
        """Gets the adjustment_amount of this ResFeeRecordV2.

        |参数名称：欠费核销金额。| |参数约束及描述： 欠费核销金额。|

        :return: The adjustment_amount of this ResFeeRecordV2.
        :rtype: float
        """
        return self._adjustment_amount

    @adjustment_amount.setter
    def adjustment_amount(self, adjustment_amount):
        """Sets the adjustment_amount of this ResFeeRecordV2.

        |参数名称：欠费核销金额。| |参数约束及描述： 欠费核销金额。|

        :param adjustment_amount: The adjustment_amount of this ResFeeRecordV2.
        :type: float
        """
        self._adjustment_amount = adjustment_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this ResFeeRecordV2.

        |参数名称：金额单位：1：元| |参数的约束及描述：金额单位：1：元|

        :return: The measure_id of this ResFeeRecordV2.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this ResFeeRecordV2.

        |参数名称：金额单位：1：元| |参数的约束及描述：金额单位：1：元|

        :param measure_id: The measure_id of this ResFeeRecordV2.
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
        if not isinstance(other, ResFeeRecordV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
