# coding: utf-8

import pprint
import re

import six





class MonthlyBillRecord:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bill_cycle': 'str',
        'customer_id': 'str',
        'service_type_code': 'str',
        'resource_type_code': 'str',
        'region_code': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'charging_mode': 'int',
        'consume_time': 'str',
        'trade_time': 'str',
        'provider_type': 'int',
        'trade_id': 'str',
        'bill_type': 'int',
        'status': 'int',
        'official_amount': 'float',
        'official_discount_amount': 'float',
        'erase_amount': 'float',
        'consume_amount': 'float',
        'cash_amount': 'float',
        'credit_amount': 'float',
        'coupon_amount': 'float',
        'flexipurchase_coupon_amount': 'float',
        'stored_value_card_amount': 'float',
        'bonus_amount': 'float',
        'debt_amount': 'float',
        'writeoff_amount': 'float'
    }

    attribute_map = {
        'bill_cycle': 'bill_cycle',
        'customer_id': 'customer_id',
        'service_type_code': 'service_type_code',
        'resource_type_code': 'resource_type_code',
        'region_code': 'region_code',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'charging_mode': 'charging_mode',
        'consume_time': 'consume_time',
        'trade_time': 'trade_time',
        'provider_type': 'provider_type',
        'trade_id': 'trade_id',
        'bill_type': 'bill_type',
        'status': 'status',
        'official_amount': 'official_amount',
        'official_discount_amount': 'official_discount_amount',
        'erase_amount': 'erase_amount',
        'consume_amount': 'consume_amount',
        'cash_amount': 'cash_amount',
        'credit_amount': 'credit_amount',
        'coupon_amount': 'coupon_amount',
        'flexipurchase_coupon_amount': 'flexipurchase_coupon_amount',
        'stored_value_card_amount': 'stored_value_card_amount',
        'bonus_amount': 'bonus_amount',
        'debt_amount': 'debt_amount',
        'writeoff_amount': 'writeoff_amount'
    }

    def __init__(self, bill_cycle=None, customer_id=None, service_type_code=None, resource_type_code=None, region_code=None, enterprise_project_id=None, enterprise_project_name=None, charging_mode=None, consume_time=None, trade_time=None, provider_type=None, trade_id=None, bill_type=None, status=None, official_amount=None, official_discount_amount=None, erase_amount=None, consume_amount=None, cash_amount=None, credit_amount=None, coupon_amount=None, flexipurchase_coupon_amount=None, stored_value_card_amount=None, bonus_amount=None, debt_amount=None, writeoff_amount=None):
        """MonthlyBillRecord - a model defined in huaweicloud sdk"""
        
        

        self._bill_cycle = None
        self._customer_id = None
        self._service_type_code = None
        self._resource_type_code = None
        self._region_code = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._charging_mode = None
        self._consume_time = None
        self._trade_time = None
        self._provider_type = None
        self._trade_id = None
        self._bill_type = None
        self._status = None
        self._official_amount = None
        self._official_discount_amount = None
        self._erase_amount = None
        self._consume_amount = None
        self._cash_amount = None
        self._credit_amount = None
        self._coupon_amount = None
        self._flexipurchase_coupon_amount = None
        self._stored_value_card_amount = None
        self._bonus_amount = None
        self._debt_amount = None
        self._writeoff_amount = None
        self.discriminator = None

        if bill_cycle is not None:
            self.bill_cycle = bill_cycle
        if customer_id is not None:
            self.customer_id = customer_id
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if region_code is not None:
            self.region_code = region_code
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if consume_time is not None:
            self.consume_time = consume_time
        if trade_time is not None:
            self.trade_time = trade_time
        if provider_type is not None:
            self.provider_type = provider_type
        if trade_id is not None:
            self.trade_id = trade_id
        if bill_type is not None:
            self.bill_type = bill_type
        if status is not None:
            self.status = status
        if official_amount is not None:
            self.official_amount = official_amount
        if official_discount_amount is not None:
            self.official_discount_amount = official_discount_amount
        if erase_amount is not None:
            self.erase_amount = erase_amount
        if consume_amount is not None:
            self.consume_amount = consume_amount
        if cash_amount is not None:
            self.cash_amount = cash_amount
        if credit_amount is not None:
            self.credit_amount = credit_amount
        if coupon_amount is not None:
            self.coupon_amount = coupon_amount
        if flexipurchase_coupon_amount is not None:
            self.flexipurchase_coupon_amount = flexipurchase_coupon_amount
        if stored_value_card_amount is not None:
            self.stored_value_card_amount = stored_value_card_amount
        if bonus_amount is not None:
            self.bonus_amount = bonus_amount
        if debt_amount is not None:
            self.debt_amount = debt_amount
        if writeoff_amount is not None:
            self.writeoff_amount = writeoff_amount

    @property
    def bill_cycle(self):
        """Gets the bill_cycle of this MonthlyBillRecord.

        |参数名称：账期，格式固定为YYYY-MM。| |参数约束及描述：账期，格式固定为YYYY-MM。|

        :return: The bill_cycle of this MonthlyBillRecord.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        """Sets the bill_cycle of this MonthlyBillRecord.

        |参数名称：账期，格式固定为YYYY-MM。| |参数约束及描述：账期，格式固定为YYYY-MM。|

        :param bill_cycle: The bill_cycle of this MonthlyBillRecord.
        :type: str
        """
        self._bill_cycle = bill_cycle

    @property
    def customer_id(self):
        """Gets the customer_id of this MonthlyBillRecord.

        |参数名称：消费的客户账号ID。如果是普通客户或者企业子客户查询消费记录，只能查询到客户自己的消费记录，且此处显示的是客户自己的客户ID。如果是企业主查询消费记录，可以查询到企业主以及企业子客户的消费记录，此处为消费的实际客户ID。如果是企业主自己的消费记录，则为企业主ID；如果是某个企业子客户的消费记录，则此处为企业子账号ID。| |参数约束及描述：消费的客户账号ID。如果是普通客户或者企业子客户查询消费记录，只能查询到客户自己的消费记录，且此处显示的是客户自己的客户ID。如果是企业主查询消费记录，可以查询到企业主以及企业子客户的消费记录，此处为消费的实际客户ID。如果是企业主自己的消费记录，则为企业主ID；如果是某个企业子客户的消费记录，则此处为企业子账号ID。|

        :return: The customer_id of this MonthlyBillRecord.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this MonthlyBillRecord.

        |参数名称：消费的客户账号ID。如果是普通客户或者企业子客户查询消费记录，只能查询到客户自己的消费记录，且此处显示的是客户自己的客户ID。如果是企业主查询消费记录，可以查询到企业主以及企业子客户的消费记录，此处为消费的实际客户ID。如果是企业主自己的消费记录，则为企业主ID；如果是某个企业子客户的消费记录，则此处为企业子账号ID。| |参数约束及描述：消费的客户账号ID。如果是普通客户或者企业子客户查询消费记录，只能查询到客户自己的消费记录，且此处显示的是客户自己的客户ID。如果是企业主查询消费记录，可以查询到企业主以及企业子客户的消费记录，此处为消费的实际客户ID。如果是企业主自己的消费记录，则为企业主ID；如果是某个企业子客户的消费记录，则此处为企业子账号ID。|

        :param customer_id: The customer_id of this MonthlyBillRecord.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def service_type_code(self):
        """Gets the service_type_code of this MonthlyBillRecord.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。| |参数约束及描述：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。|

        :return: The service_type_code of this MonthlyBillRecord.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this MonthlyBillRecord.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。| |参数约束及描述：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。|

        :param service_type_code: The service_type_code of this MonthlyBillRecord.
        :type: str
        """
        self._service_type_code = service_type_code

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this MonthlyBillRecord.

        |参数名称：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。| |参数约束及描述：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。|

        :return: The resource_type_code of this MonthlyBillRecord.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this MonthlyBillRecord.

        |参数名称：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。| |参数约束及描述：云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点地区和终端节点对应云服务的“区域”列的值。|

        :param resource_type_code: The resource_type_code of this MonthlyBillRecord.
        :type: str
        """
        self._resource_type_code = resource_type_code

    @property
    def region_code(self):
        """Gets the region_code of this MonthlyBillRecord.

        |参数名称：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型| |参数约束及描述：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型|

        :return: The region_code of this MonthlyBillRecord.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this MonthlyBillRecord.

        |参数名称：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型| |参数约束及描述：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型|

        :param region_code: The region_code of this MonthlyBillRecord.
        :type: str
        """
        self._region_code = region_code

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this MonthlyBillRecord.

        |参数名称：企业项目标识| |参数约束及描述：企业项目标识|

        :return: The enterprise_project_id of this MonthlyBillRecord.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this MonthlyBillRecord.

        |参数名称：企业项目标识| |参数约束及描述：企业项目标识|

        :param enterprise_project_id: The enterprise_project_id of this MonthlyBillRecord.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this MonthlyBillRecord.

        |参数名称：企业项目名称| |参数约束及描述：企业项目名称|

        :return: The enterprise_project_name of this MonthlyBillRecord.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this MonthlyBillRecord.

        |参数名称：企业项目名称| |参数约束及描述：企业项目名称|

        :param enterprise_project_name: The enterprise_project_name of this MonthlyBillRecord.
        :type: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def charging_mode(self):
        """Gets the charging_mode of this MonthlyBillRecord.

        |参数名称：计费模式1、包周期；3、按需；10、预留实例| |参数的约束及描述：计费模式1、包周期；3、按需；10、预留实例|

        :return: The charging_mode of this MonthlyBillRecord.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this MonthlyBillRecord.

        |参数名称：计费模式1、包周期；3、按需；10、预留实例| |参数的约束及描述：计费模式1、包周期；3、按需；10、预留实例|

        :param charging_mode: The charging_mode of this MonthlyBillRecord.
        :type: int
        """
        self._charging_mode = charging_mode

    @property
    def consume_time(self):
        """Gets the consume_time of this MonthlyBillRecord.

        |参数名称：| |参数名称：消费时间，包周期和预留实例订购场景下为订单支付时间，按需场景下为话单生失效时间||参数约束及描述：| |参数名称：消费时间，包周期和预留实例订购场景下为订单支付时间，按需场景下为话单生失效时间|

        :return: The consume_time of this MonthlyBillRecord.
        :rtype: str
        """
        return self._consume_time

    @consume_time.setter
    def consume_time(self, consume_time):
        """Sets the consume_time of this MonthlyBillRecord.

        |参数名称：| |参数名称：消费时间，包周期和预留实例订购场景下为订单支付时间，按需场景下为话单生失效时间||参数约束及描述：| |参数名称：消费时间，包周期和预留实例订购场景下为订单支付时间，按需场景下为话单生失效时间|

        :param consume_time: The consume_time of this MonthlyBillRecord.
        :type: str
        """
        self._consume_time = consume_time

    @property
    def trade_time(self):
        """Gets the trade_time of this MonthlyBillRecord.

        |参数名称：| |参数名称：交易时间| |参数约束及描述：交易时间，某条消费记录对应的扣费时间||参数约束及描述：| |参数名称：交易时间| |参数约束及描述：交易时间，某条消费记录对应的扣费时间|

        :return: The trade_time of this MonthlyBillRecord.
        :rtype: str
        """
        return self._trade_time

    @trade_time.setter
    def trade_time(self, trade_time):
        """Sets the trade_time of this MonthlyBillRecord.

        |参数名称：| |参数名称：交易时间| |参数约束及描述：交易时间，某条消费记录对应的扣费时间||参数约束及描述：| |参数名称：交易时间| |参数约束及描述：交易时间，某条消费记录对应的扣费时间|

        :param trade_time: The trade_time of this MonthlyBillRecord.
        :type: str
        """
        self._trade_time = trade_time

    @property
    def provider_type(self):
        """Gets the provider_type of this MonthlyBillRecord.

        |参数名称：服务商1：华为云2：云市场| |参数的约束及描述：服务商1：华为云2：云市场|

        :return: The provider_type of this MonthlyBillRecord.
        :rtype: int
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this MonthlyBillRecord.

        |参数名称：服务商1：华为云2：云市场| |参数的约束及描述：服务商1：华为云2：云市场|

        :param provider_type: The provider_type of this MonthlyBillRecord.
        :type: int
        """
        self._provider_type = provider_type

    @property
    def trade_id(self):
        """Gets the trade_id of this MonthlyBillRecord.

        |参数名称：订单ID 或 交易ID，扣费维度的唯一标识| |参数约束及描述：订单ID 或 交易ID，扣费维度的唯一标识|

        :return: The trade_id of this MonthlyBillRecord.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """Sets the trade_id of this MonthlyBillRecord.

        |参数名称：订单ID 或 交易ID，扣费维度的唯一标识| |参数约束及描述：订单ID 或 交易ID，扣费维度的唯一标识|

        :param trade_id: The trade_id of this MonthlyBillRecord.
        :type: str
        """
        self._trade_id = trade_id

    @property
    def bill_type(self):
        """Gets the bill_type of this MonthlyBillRecord.

        |参数名称：账单类型1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿12：消费-按时计费13：消费-退订手续费14：消费-服务支持计划月末扣费16：调账-扣费| |参数的约束及描述：账单类型1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿12：消费-按时计费13：消费-退订手续费14：消费-服务支持计划月末扣费16：调账-扣费|

        :return: The bill_type of this MonthlyBillRecord.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this MonthlyBillRecord.

        |参数名称：账单类型1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿12：消费-按时计费13：消费-退订手续费14：消费-服务支持计划月末扣费16：调账-扣费| |参数的约束及描述：账单类型1：消费-新购2：消费-续订3：消费-变更4：退款-退订5：消费-使用8：消费-自动续订9：调账-补偿12：消费-按时计费13：消费-退订手续费14：消费-服务支持计划月末扣费16：调账-扣费|

        :param bill_type: The bill_type of this MonthlyBillRecord.
        :type: int
        """
        self._bill_type = bill_type

    @property
    def status(self):
        """Gets the status of this MonthlyBillRecord.

        |参数名称：支付状态1：已支付2：未结清3：未结算| |参数的约束及描述：支付状态1：已支付2：未结清3：未结算|

        :return: The status of this MonthlyBillRecord.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MonthlyBillRecord.

        |参数名称：支付状态1：已支付2：未结清3：未结算| |参数的约束及描述：支付状态1：已支付2：未结清3：未结算|

        :param status: The status of this MonthlyBillRecord.
        :type: int
        """
        self._status = status

    @property
    def official_amount(self):
        """Gets the official_amount of this MonthlyBillRecord.

        |参数名称：官网价。单位为元说明：official_amount等于official_discount_amount和erase_amount和consume_amount的和。| |参数的约束及描述：官网价。单位为元说明：official_amount等于official_discount_amount和erase_amount和consume_amount的和。|

        :return: The official_amount of this MonthlyBillRecord.
        :rtype: float
        """
        return self._official_amount

    @official_amount.setter
    def official_amount(self, official_amount):
        """Sets the official_amount of this MonthlyBillRecord.

        |参数名称：官网价。单位为元说明：official_amount等于official_discount_amount和erase_amount和consume_amount的和。| |参数的约束及描述：官网价。单位为元说明：official_amount等于official_discount_amount和erase_amount和consume_amount的和。|

        :param official_amount: The official_amount of this MonthlyBillRecord.
        :type: float
        """
        self._official_amount = official_amount

    @property
    def official_discount_amount(self):
        """Gets the official_discount_amount of this MonthlyBillRecord.

        |参数名称：折扣金额。单位为元| |参数的约束及描述：折扣金额。单位为元|

        :return: The official_discount_amount of this MonthlyBillRecord.
        :rtype: float
        """
        return self._official_discount_amount

    @official_discount_amount.setter
    def official_discount_amount(self, official_discount_amount):
        """Sets the official_discount_amount of this MonthlyBillRecord.

        |参数名称：折扣金额。单位为元| |参数的约束及描述：折扣金额。单位为元|

        :param official_discount_amount: The official_discount_amount of this MonthlyBillRecord.
        :type: float
        """
        self._official_discount_amount = official_discount_amount

    @property
    def erase_amount(self):
        """Gets the erase_amount of this MonthlyBillRecord.

        |参数名称：抹零金额。单位为元| |参数的约束及描述：抹零金额。单位为元|

        :return: The erase_amount of this MonthlyBillRecord.
        :rtype: float
        """
        return self._erase_amount

    @erase_amount.setter
    def erase_amount(self, erase_amount):
        """Sets the erase_amount of this MonthlyBillRecord.

        |参数名称：抹零金额。单位为元| |参数的约束及描述：抹零金额。单位为元|

        :param erase_amount: The erase_amount of this MonthlyBillRecord.
        :type: float
        """
        self._erase_amount = erase_amount

    @property
    def consume_amount(self):
        """Gets the consume_amount of this MonthlyBillRecord.

        |参数名称：应付金额，包括现金券和储值卡和代金券金额。单位为元说明：（1）consume_amount的值包含cash_amount，credit_amount，coupon_amount，flexipurchase_coupon_amount，stored_card_amount，bonus_amount，debt_amount，writeoff_amount的和| |参数的约束及描述：应付金额，包括现金券和储值卡和代金券金额。单位为元说明：（1）consume_amount的值包含cash_amount，credit_amount，coupon_amount，flexipurchase_coupon_amount，stored_card_amount，bonus_amount，debt_amount，writeoff_amount的和|

        :return: The consume_amount of this MonthlyBillRecord.
        :rtype: float
        """
        return self._consume_amount

    @consume_amount.setter
    def consume_amount(self, consume_amount):
        """Sets the consume_amount of this MonthlyBillRecord.

        |参数名称：应付金额，包括现金券和储值卡和代金券金额。单位为元说明：（1）consume_amount的值包含cash_amount，credit_amount，coupon_amount，flexipurchase_coupon_amount，stored_card_amount，bonus_amount，debt_amount，writeoff_amount的和| |参数的约束及描述：应付金额，包括现金券和储值卡和代金券金额。单位为元说明：（1）consume_amount的值包含cash_amount，credit_amount，coupon_amount，flexipurchase_coupon_amount，stored_card_amount，bonus_amount，debt_amount，writeoff_amount的和|

        :param consume_amount: The consume_amount of this MonthlyBillRecord.
        :type: float
        """
        self._consume_amount = consume_amount

    @property
    def cash_amount(self):
        """Gets the cash_amount of this MonthlyBillRecord.

        |参数名称：现金支付金额。单位为元| |参数的约束及描述：现金支付金额。单位为元|

        :return: The cash_amount of this MonthlyBillRecord.
        :rtype: float
        """
        return self._cash_amount

    @cash_amount.setter
    def cash_amount(self, cash_amount):
        """Sets the cash_amount of this MonthlyBillRecord.

        |参数名称：现金支付金额。单位为元| |参数的约束及描述：现金支付金额。单位为元|

        :param cash_amount: The cash_amount of this MonthlyBillRecord.
        :type: float
        """
        self._cash_amount = cash_amount

    @property
    def credit_amount(self):
        """Gets the credit_amount of this MonthlyBillRecord.

        |参数名称：信用额度支付金额。单位为元| |参数的约束及描述：信用额度支付金额。单位为元|

        :return: The credit_amount of this MonthlyBillRecord.
        :rtype: float
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        """Sets the credit_amount of this MonthlyBillRecord.

        |参数名称：信用额度支付金额。单位为元| |参数的约束及描述：信用额度支付金额。单位为元|

        :param credit_amount: The credit_amount of this MonthlyBillRecord.
        :type: float
        """
        self._credit_amount = credit_amount

    @property
    def coupon_amount(self):
        """Gets the coupon_amount of this MonthlyBillRecord.

        |参数名称：代金券支付金额。单位为元| |参数的约束及描述：代金券支付金额。单位为元|

        :return: The coupon_amount of this MonthlyBillRecord.
        :rtype: float
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        """Sets the coupon_amount of this MonthlyBillRecord.

        |参数名称：代金券支付金额。单位为元| |参数的约束及描述：代金券支付金额。单位为元|

        :param coupon_amount: The coupon_amount of this MonthlyBillRecord.
        :type: float
        """
        self._coupon_amount = coupon_amount

    @property
    def flexipurchase_coupon_amount(self):
        """Gets the flexipurchase_coupon_amount of this MonthlyBillRecord.

        |参数名称：现金券支付金额。单位为元| |参数的约束及描述：现金券支付金额。单位为元|

        :return: The flexipurchase_coupon_amount of this MonthlyBillRecord.
        :rtype: float
        """
        return self._flexipurchase_coupon_amount

    @flexipurchase_coupon_amount.setter
    def flexipurchase_coupon_amount(self, flexipurchase_coupon_amount):
        """Sets the flexipurchase_coupon_amount of this MonthlyBillRecord.

        |参数名称：现金券支付金额。单位为元| |参数的约束及描述：现金券支付金额。单位为元|

        :param flexipurchase_coupon_amount: The flexipurchase_coupon_amount of this MonthlyBillRecord.
        :type: float
        """
        self._flexipurchase_coupon_amount = flexipurchase_coupon_amount

    @property
    def stored_value_card_amount(self):
        """Gets the stored_value_card_amount of this MonthlyBillRecord.

        |参数名称：储值卡支付金额。单位为元| |参数的约束及描述：储值卡支付金额。单位为元|

        :return: The stored_value_card_amount of this MonthlyBillRecord.
        :rtype: float
        """
        return self._stored_value_card_amount

    @stored_value_card_amount.setter
    def stored_value_card_amount(self, stored_value_card_amount):
        """Sets the stored_value_card_amount of this MonthlyBillRecord.

        |参数名称：储值卡支付金额。单位为元| |参数的约束及描述：储值卡支付金额。单位为元|

        :param stored_value_card_amount: The stored_value_card_amount of this MonthlyBillRecord.
        :type: float
        """
        self._stored_value_card_amount = stored_value_card_amount

    @property
    def bonus_amount(self):
        """Gets the bonus_amount of this MonthlyBillRecord.

        |参数名称：奖励金支付金额（奖励金已经下市，用于现网客户未使用完的奖励金）。单位为元| |参数的约束及描述：奖励金支付金额（奖励金已经下市，用于现网客户未使用完的奖励金）。单位为元|

        :return: The bonus_amount of this MonthlyBillRecord.
        :rtype: float
        """
        return self._bonus_amount

    @bonus_amount.setter
    def bonus_amount(self, bonus_amount):
        """Sets the bonus_amount of this MonthlyBillRecord.

        |参数名称：奖励金支付金额（奖励金已经下市，用于现网客户未使用完的奖励金）。单位为元| |参数的约束及描述：奖励金支付金额（奖励金已经下市，用于现网客户未使用完的奖励金）。单位为元|

        :param bonus_amount: The bonus_amount of this MonthlyBillRecord.
        :type: float
        """
        self._bonus_amount = bonus_amount

    @property
    def debt_amount(self):
        """Gets the debt_amount of this MonthlyBillRecord.

        |参数名称：欠费金额。单位为元| |参数的约束及描述：欠费金额。单位为元|

        :return: The debt_amount of this MonthlyBillRecord.
        :rtype: float
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        """Sets the debt_amount of this MonthlyBillRecord.

        |参数名称：欠费金额。单位为元| |参数的约束及描述：欠费金额。单位为元|

        :param debt_amount: The debt_amount of this MonthlyBillRecord.
        :type: float
        """
        self._debt_amount = debt_amount

    @property
    def writeoff_amount(self):
        """Gets the writeoff_amount of this MonthlyBillRecord.

        |参数名称：欠费核销金额。单位为元| |参数的约束及描述：欠费核销金额。单位为元|

        :return: The writeoff_amount of this MonthlyBillRecord.
        :rtype: float
        """
        return self._writeoff_amount

    @writeoff_amount.setter
    def writeoff_amount(self, writeoff_amount):
        """Sets the writeoff_amount of this MonthlyBillRecord.

        |参数名称：欠费核销金额。单位为元| |参数的约束及描述：欠费核销金额。单位为元|

        :param writeoff_amount: The writeoff_amount of this MonthlyBillRecord.
        :type: float
        """
        self._writeoff_amount = writeoff_amount

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
        if not isinstance(other, MonthlyBillRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
