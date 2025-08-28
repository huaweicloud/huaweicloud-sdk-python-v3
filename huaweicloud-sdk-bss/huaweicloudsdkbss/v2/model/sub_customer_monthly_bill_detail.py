# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubCustomerMonthlyBillDetail:

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
        'association_type': 'str',
        'service_type_code': 'str',
        'resource_type_code': 'str',
        'service_type_name': 'str',
        'resource_type_name': 'str',
        'charging_mode': 'int',
        'trade_time': 'str',
        'trade_id': 'str',
        'id': 'str',
        'bill_detail_type': 'int',
        'resource_id': 'str',
        'resource_name': 'str',
        'product_spec_desc': 'str',
        'region_code': 'str',
        'product_id': 'str',
        'product_name': 'str',
        'resource_tag': 'str',
        'consume_time': 'str',
        'usage_type': 'str',
        'usage_amount': 'decimal.Decimal',
        'usage_measure_id': 'int',
        'free_resource_usage': 'decimal.Decimal',
        'free_resource_measure_id': 'int',
        'ri_usage': 'decimal.Decimal',
        'ri_usage_measure_id': 'int',
        'official_amount': 'decimal.Decimal',
        'official_discount_amount': 'decimal.Decimal',
        'payment_amount': 'decimal.Decimal',
        'cash_amount': 'decimal.Decimal',
        'credit_amount': 'decimal.Decimal',
        'coupon_amount': 'decimal.Decimal',
        'flexipurchase_coupon_amount': 'decimal.Decimal',
        'stored_value_card_amount': 'decimal.Decimal',
        'debt_amount': 'decimal.Decimal',
        'writeoff_amount': 'decimal.Decimal',
        'period_type': 'int',
        'account_manager_id': 'str',
        'partner_id': 'str',
        'region_name': 'str',
        'sub_service_type_code': 'str',
        'sub_service_type_name': 'str',
        'sub_resource_type_code': 'str',
        'sub_resource_type_name': 'str',
        'sub_resource_id': 'str',
        'sub_resource_name': 'str'
    }

    attribute_map = {
        'bill_cycle': 'bill_cycle',
        'customer_id': 'customer_id',
        'association_type': 'association_type',
        'service_type_code': 'service_type_code',
        'resource_type_code': 'resource_type_code',
        'service_type_name': 'service_type_name',
        'resource_type_name': 'resource_type_name',
        'charging_mode': 'charging_mode',
        'trade_time': 'trade_time',
        'trade_id': 'trade_id',
        'id': 'id',
        'bill_detail_type': 'bill_detail_type',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'product_spec_desc': 'product_spec_desc',
        'region_code': 'region_code',
        'product_id': 'product_id',
        'product_name': 'product_name',
        'resource_tag': 'resource_tag',
        'consume_time': 'consume_time',
        'usage_type': 'usage_type',
        'usage_amount': 'usage_amount',
        'usage_measure_id': 'usage_measure_id',
        'free_resource_usage': 'free_resource_usage',
        'free_resource_measure_id': 'free_resource_measure_id',
        'ri_usage': 'ri_usage',
        'ri_usage_measure_id': 'ri_usage_measure_id',
        'official_amount': 'official_amount',
        'official_discount_amount': 'official_discount_amount',
        'payment_amount': 'payment_amount',
        'cash_amount': 'cash_amount',
        'credit_amount': 'credit_amount',
        'coupon_amount': 'coupon_amount',
        'flexipurchase_coupon_amount': 'flexipurchase_coupon_amount',
        'stored_value_card_amount': 'stored_value_card_amount',
        'debt_amount': 'debt_amount',
        'writeoff_amount': 'writeoff_amount',
        'period_type': 'period_type',
        'account_manager_id': 'account_manager_id',
        'partner_id': 'partner_id',
        'region_name': 'region_name',
        'sub_service_type_code': 'sub_service_type_code',
        'sub_service_type_name': 'sub_service_type_name',
        'sub_resource_type_code': 'sub_resource_type_code',
        'sub_resource_type_name': 'sub_resource_type_name',
        'sub_resource_id': 'sub_resource_id',
        'sub_resource_name': 'sub_resource_name'
    }

    def __init__(self, bill_cycle=None, customer_id=None, association_type=None, service_type_code=None, resource_type_code=None, service_type_name=None, resource_type_name=None, charging_mode=None, trade_time=None, trade_id=None, id=None, bill_detail_type=None, resource_id=None, resource_name=None, product_spec_desc=None, region_code=None, product_id=None, product_name=None, resource_tag=None, consume_time=None, usage_type=None, usage_amount=None, usage_measure_id=None, free_resource_usage=None, free_resource_measure_id=None, ri_usage=None, ri_usage_measure_id=None, official_amount=None, official_discount_amount=None, payment_amount=None, cash_amount=None, credit_amount=None, coupon_amount=None, flexipurchase_coupon_amount=None, stored_value_card_amount=None, debt_amount=None, writeoff_amount=None, period_type=None, account_manager_id=None, partner_id=None, region_name=None, sub_service_type_code=None, sub_service_type_name=None, sub_resource_type_code=None, sub_resource_type_name=None, sub_resource_id=None, sub_resource_name=None):
        r"""SubCustomerMonthlyBillDetail

        The model defined in huaweicloud sdk

        :param bill_cycle: 账期。 格式：YYYY-MM
        :type bill_cycle: str
        :param customer_id: 客户账号ID。
        :type customer_id: str
        :param association_type: 子客户的关联类型： 1：顾问销售2：代售
        :type association_type: str
        :param service_type_code: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。
        :type service_type_code: str
        :param resource_type_code: 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。 ResourceType是CloudServiceType中的一种资源，CloudServiceType由多种ResourceType组合提供。
        :type resource_type_code: str
        :param service_type_name: 云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。
        :type service_type_name: str
        :param resource_type_name: 资源类型名称。例如ECS的资源类型名称为“云主机”。
        :type resource_type_name: str
        :param charging_mode: 计费模式。 1：包周期3：按需10：预留实例11：节省计划
        :type charging_mode: int
        :param trade_time: 交易时间，即某条消费记录对应的扣费时间。 示例：2020-11-17T06:43:38Z
        :type trade_time: str
        :param trade_id: 订单ID或交易ID，扣费维度的唯一标识。 账单类型为1，2，3，4，8时为订单ID。其它场景下为交易ID。非月末扣费：应收ID月末扣费：账单ID
        :type trade_id: str
        :param id: 唯一标识。
        :type id: str
        :param bill_detail_type: 账单类型。1：消费-新购 2：消费-续订 3：消费-变更 4：退款-退订 5：消费-使用 8：消费-自动续订 9：调账-补偿 14：消费-服务支持计划月末扣费 16：调账-扣费 18：消费-按月付费 20：退款-变更 23：消费-节省计划抵扣 24：退款-包年/包月转按需 25：消费-抹零补扣 103：消费-按年付费
        :type bill_detail_type: int
        :param resource_id: 资源ID。
        :type resource_id: str
        :param resource_name: 资源名称。
        :type resource_name: str
        :param product_spec_desc: 产品的规格描述。
        :type product_spec_desc: str
        :param region_code: 云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。
        :type region_code: str
        :param product_id: 产品ID。
        :type product_id: str
        :param product_name: 产品名称。
        :type product_name: str
        :param resource_tag: 资源标签。
        :type resource_tag: str
        :param consume_time: 消费时间。 包周期和预留实例订购场景下为订单支付时间；按需场景下为话单生失效时间。 格式：YYYY-MM-DDThh:mm:ssZ
        :type consume_time: str
        :param usage_type: 资源使用量的类型，您可以调用查询使用量类型列表接口获取。
        :type usage_type: str
        :param usage_amount: 资源的使用量。
        :type usage_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param usage_measure_id: 资源使用量的度量单位，您可以调用查询度量单位列表接口获取。
        :type usage_measure_id: int
        :param free_resource_usage: 套餐内使用量。
        :type free_resource_usage: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param free_resource_measure_id: 套餐内使用量的度量单位，您可以调用查询度量单位列表接口获取。
        :type free_resource_measure_id: int
        :param ri_usage: 预留实例使用量。
        :type ri_usage: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param ri_usage_measure_id: 预留实例使用量单位。
        :type ri_usage_measure_id: int
        :param official_amount: 官网价。
        :type official_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param official_discount_amount: 对应官网价折扣金额。
        :type official_discount_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param payment_amount: 应付金额。
        :type payment_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param cash_amount: 现金支付金额。
        :type cash_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param credit_amount: 信用额度支付金额。
        :type credit_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param coupon_amount: 代金券支付金额。
        :type coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param flexipurchase_coupon_amount: 现金券支付金额。
        :type flexipurchase_coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param stored_value_card_amount: 储值卡支付金额。
        :type stored_value_card_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param debt_amount: 欠费金额。
        :type debt_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param writeoff_amount: 欠费核销金额。
        :type writeoff_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param period_type: 周期类型： 19：年20：月24：天25：小时5：一次性
        :type period_type: int
        :param account_manager_id: 客户经理标识。
        :type account_manager_id: str
        :param partner_id: 关联的经销商ID。
        :type partner_id: str
        :param region_name: 云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。
        :type region_name: str
        :param sub_service_type_code: 整机的子云服务的自身的云服务类型编码。
        :type sub_service_type_code: str
        :param sub_service_type_name: 整机的子云服务的自身的云服务类型名称。
        :type sub_service_type_name: str
        :param sub_resource_type_code: 整机的子云服务的自身的资源类型编码。
        :type sub_resource_type_code: str
        :param sub_resource_type_name: 整机的子云服务的自身的资源类型名称。
        :type sub_resource_type_name: str
        :param sub_resource_id: 整机的子云服务的自身的资源ID，资源标识。（如果为预留实例，则为预留实例标识）
        :type sub_resource_id: str
        :param sub_resource_name: 整机的子云服务的自身的资源名称，资源标识。（如果为预留实例，则为预留实例标识）
        :type sub_resource_name: str
        """
        
        

        self._bill_cycle = None
        self._customer_id = None
        self._association_type = None
        self._service_type_code = None
        self._resource_type_code = None
        self._service_type_name = None
        self._resource_type_name = None
        self._charging_mode = None
        self._trade_time = None
        self._trade_id = None
        self._id = None
        self._bill_detail_type = None
        self._resource_id = None
        self._resource_name = None
        self._product_spec_desc = None
        self._region_code = None
        self._product_id = None
        self._product_name = None
        self._resource_tag = None
        self._consume_time = None
        self._usage_type = None
        self._usage_amount = None
        self._usage_measure_id = None
        self._free_resource_usage = None
        self._free_resource_measure_id = None
        self._ri_usage = None
        self._ri_usage_measure_id = None
        self._official_amount = None
        self._official_discount_amount = None
        self._payment_amount = None
        self._cash_amount = None
        self._credit_amount = None
        self._coupon_amount = None
        self._flexipurchase_coupon_amount = None
        self._stored_value_card_amount = None
        self._debt_amount = None
        self._writeoff_amount = None
        self._period_type = None
        self._account_manager_id = None
        self._partner_id = None
        self._region_name = None
        self._sub_service_type_code = None
        self._sub_service_type_name = None
        self._sub_resource_type_code = None
        self._sub_resource_type_name = None
        self._sub_resource_id = None
        self._sub_resource_name = None
        self.discriminator = None

        if bill_cycle is not None:
            self.bill_cycle = bill_cycle
        if customer_id is not None:
            self.customer_id = customer_id
        if association_type is not None:
            self.association_type = association_type
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if service_type_name is not None:
            self.service_type_name = service_type_name
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if trade_time is not None:
            self.trade_time = trade_time
        if trade_id is not None:
            self.trade_id = trade_id
        if id is not None:
            self.id = id
        if bill_detail_type is not None:
            self.bill_detail_type = bill_detail_type
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if product_spec_desc is not None:
            self.product_spec_desc = product_spec_desc
        if region_code is not None:
            self.region_code = region_code
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if resource_tag is not None:
            self.resource_tag = resource_tag
        if consume_time is not None:
            self.consume_time = consume_time
        if usage_type is not None:
            self.usage_type = usage_type
        if usage_amount is not None:
            self.usage_amount = usage_amount
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
        if official_amount is not None:
            self.official_amount = official_amount
        if official_discount_amount is not None:
            self.official_discount_amount = official_discount_amount
        if payment_amount is not None:
            self.payment_amount = payment_amount
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
        if debt_amount is not None:
            self.debt_amount = debt_amount
        if writeoff_amount is not None:
            self.writeoff_amount = writeoff_amount
        if period_type is not None:
            self.period_type = period_type
        if account_manager_id is not None:
            self.account_manager_id = account_manager_id
        if partner_id is not None:
            self.partner_id = partner_id
        if region_name is not None:
            self.region_name = region_name
        if sub_service_type_code is not None:
            self.sub_service_type_code = sub_service_type_code
        if sub_service_type_name is not None:
            self.sub_service_type_name = sub_service_type_name
        if sub_resource_type_code is not None:
            self.sub_resource_type_code = sub_resource_type_code
        if sub_resource_type_name is not None:
            self.sub_resource_type_name = sub_resource_type_name
        if sub_resource_id is not None:
            self.sub_resource_id = sub_resource_id
        if sub_resource_name is not None:
            self.sub_resource_name = sub_resource_name

    @property
    def bill_cycle(self):
        r"""Gets the bill_cycle of this SubCustomerMonthlyBillDetail.

        账期。 格式：YYYY-MM

        :return: The bill_cycle of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        r"""Sets the bill_cycle of this SubCustomerMonthlyBillDetail.

        账期。 格式：YYYY-MM

        :param bill_cycle: The bill_cycle of this SubCustomerMonthlyBillDetail.
        :type bill_cycle: str
        """
        self._bill_cycle = bill_cycle

    @property
    def customer_id(self):
        r"""Gets the customer_id of this SubCustomerMonthlyBillDetail.

        客户账号ID。

        :return: The customer_id of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this SubCustomerMonthlyBillDetail.

        客户账号ID。

        :param customer_id: The customer_id of this SubCustomerMonthlyBillDetail.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def association_type(self):
        r"""Gets the association_type of this SubCustomerMonthlyBillDetail.

        子客户的关联类型： 1：顾问销售2：代售

        :return: The association_type of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._association_type

    @association_type.setter
    def association_type(self, association_type):
        r"""Sets the association_type of this SubCustomerMonthlyBillDetail.

        子客户的关联类型： 1：顾问销售2：代售

        :param association_type: The association_type of this SubCustomerMonthlyBillDetail.
        :type association_type: str
        """
        self._association_type = association_type

    @property
    def service_type_code(self):
        r"""Gets the service_type_code of this SubCustomerMonthlyBillDetail.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :return: The service_type_code of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        r"""Sets the service_type_code of this SubCustomerMonthlyBillDetail.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :param service_type_code: The service_type_code of this SubCustomerMonthlyBillDetail.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

    @property
    def resource_type_code(self):
        r"""Gets the resource_type_code of this SubCustomerMonthlyBillDetail.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。 ResourceType是CloudServiceType中的一种资源，CloudServiceType由多种ResourceType组合提供。

        :return: The resource_type_code of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        r"""Sets the resource_type_code of this SubCustomerMonthlyBillDetail.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。 ResourceType是CloudServiceType中的一种资源，CloudServiceType由多种ResourceType组合提供。

        :param resource_type_code: The resource_type_code of this SubCustomerMonthlyBillDetail.
        :type resource_type_code: str
        """
        self._resource_type_code = resource_type_code

    @property
    def service_type_name(self):
        r"""Gets the service_type_name of this SubCustomerMonthlyBillDetail.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :return: The service_type_name of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._service_type_name

    @service_type_name.setter
    def service_type_name(self, service_type_name):
        r"""Sets the service_type_name of this SubCustomerMonthlyBillDetail.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :param service_type_name: The service_type_name of this SubCustomerMonthlyBillDetail.
        :type service_type_name: str
        """
        self._service_type_name = service_type_name

    @property
    def resource_type_name(self):
        r"""Gets the resource_type_name of this SubCustomerMonthlyBillDetail.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :return: The resource_type_name of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        r"""Sets the resource_type_name of this SubCustomerMonthlyBillDetail.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :param resource_type_name: The resource_type_name of this SubCustomerMonthlyBillDetail.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this SubCustomerMonthlyBillDetail.

        计费模式。 1：包周期3：按需10：预留实例11：节省计划

        :return: The charging_mode of this SubCustomerMonthlyBillDetail.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this SubCustomerMonthlyBillDetail.

        计费模式。 1：包周期3：按需10：预留实例11：节省计划

        :param charging_mode: The charging_mode of this SubCustomerMonthlyBillDetail.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def trade_time(self):
        r"""Gets the trade_time of this SubCustomerMonthlyBillDetail.

        交易时间，即某条消费记录对应的扣费时间。 示例：2020-11-17T06:43:38Z

        :return: The trade_time of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._trade_time

    @trade_time.setter
    def trade_time(self, trade_time):
        r"""Sets the trade_time of this SubCustomerMonthlyBillDetail.

        交易时间，即某条消费记录对应的扣费时间。 示例：2020-11-17T06:43:38Z

        :param trade_time: The trade_time of this SubCustomerMonthlyBillDetail.
        :type trade_time: str
        """
        self._trade_time = trade_time

    @property
    def trade_id(self):
        r"""Gets the trade_id of this SubCustomerMonthlyBillDetail.

        订单ID或交易ID，扣费维度的唯一标识。 账单类型为1，2，3，4，8时为订单ID。其它场景下为交易ID。非月末扣费：应收ID月末扣费：账单ID

        :return: The trade_id of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        r"""Sets the trade_id of this SubCustomerMonthlyBillDetail.

        订单ID或交易ID，扣费维度的唯一标识。 账单类型为1，2，3，4，8时为订单ID。其它场景下为交易ID。非月末扣费：应收ID月末扣费：账单ID

        :param trade_id: The trade_id of this SubCustomerMonthlyBillDetail.
        :type trade_id: str
        """
        self._trade_id = trade_id

    @property
    def id(self):
        r"""Gets the id of this SubCustomerMonthlyBillDetail.

        唯一标识。

        :return: The id of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SubCustomerMonthlyBillDetail.

        唯一标识。

        :param id: The id of this SubCustomerMonthlyBillDetail.
        :type id: str
        """
        self._id = id

    @property
    def bill_detail_type(self):
        r"""Gets the bill_detail_type of this SubCustomerMonthlyBillDetail.

        账单类型。1：消费-新购 2：消费-续订 3：消费-变更 4：退款-退订 5：消费-使用 8：消费-自动续订 9：调账-补偿 14：消费-服务支持计划月末扣费 16：调账-扣费 18：消费-按月付费 20：退款-变更 23：消费-节省计划抵扣 24：退款-包年/包月转按需 25：消费-抹零补扣 103：消费-按年付费

        :return: The bill_detail_type of this SubCustomerMonthlyBillDetail.
        :rtype: int
        """
        return self._bill_detail_type

    @bill_detail_type.setter
    def bill_detail_type(self, bill_detail_type):
        r"""Sets the bill_detail_type of this SubCustomerMonthlyBillDetail.

        账单类型。1：消费-新购 2：消费-续订 3：消费-变更 4：退款-退订 5：消费-使用 8：消费-自动续订 9：调账-补偿 14：消费-服务支持计划月末扣费 16：调账-扣费 18：消费-按月付费 20：退款-变更 23：消费-节省计划抵扣 24：退款-包年/包月转按需 25：消费-抹零补扣 103：消费-按年付费

        :param bill_detail_type: The bill_detail_type of this SubCustomerMonthlyBillDetail.
        :type bill_detail_type: int
        """
        self._bill_detail_type = bill_detail_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this SubCustomerMonthlyBillDetail.

        资源ID。

        :return: The resource_id of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this SubCustomerMonthlyBillDetail.

        资源ID。

        :param resource_id: The resource_id of this SubCustomerMonthlyBillDetail.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this SubCustomerMonthlyBillDetail.

        资源名称。

        :return: The resource_name of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this SubCustomerMonthlyBillDetail.

        资源名称。

        :param resource_name: The resource_name of this SubCustomerMonthlyBillDetail.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def product_spec_desc(self):
        r"""Gets the product_spec_desc of this SubCustomerMonthlyBillDetail.

        产品的规格描述。

        :return: The product_spec_desc of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._product_spec_desc

    @product_spec_desc.setter
    def product_spec_desc(self, product_spec_desc):
        r"""Sets the product_spec_desc of this SubCustomerMonthlyBillDetail.

        产品的规格描述。

        :param product_spec_desc: The product_spec_desc of this SubCustomerMonthlyBillDetail.
        :type product_spec_desc: str
        """
        self._product_spec_desc = product_spec_desc

    @property
    def region_code(self):
        r"""Gets the region_code of this SubCustomerMonthlyBillDetail.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :return: The region_code of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        r"""Sets the region_code of this SubCustomerMonthlyBillDetail.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :param region_code: The region_code of this SubCustomerMonthlyBillDetail.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def product_id(self):
        r"""Gets the product_id of this SubCustomerMonthlyBillDetail.

        产品ID。

        :return: The product_id of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this SubCustomerMonthlyBillDetail.

        产品ID。

        :param product_id: The product_id of this SubCustomerMonthlyBillDetail.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_name(self):
        r"""Gets the product_name of this SubCustomerMonthlyBillDetail.

        产品名称。

        :return: The product_name of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this SubCustomerMonthlyBillDetail.

        产品名称。

        :param product_name: The product_name of this SubCustomerMonthlyBillDetail.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def resource_tag(self):
        r"""Gets the resource_tag of this SubCustomerMonthlyBillDetail.

        资源标签。

        :return: The resource_tag of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._resource_tag

    @resource_tag.setter
    def resource_tag(self, resource_tag):
        r"""Sets the resource_tag of this SubCustomerMonthlyBillDetail.

        资源标签。

        :param resource_tag: The resource_tag of this SubCustomerMonthlyBillDetail.
        :type resource_tag: str
        """
        self._resource_tag = resource_tag

    @property
    def consume_time(self):
        r"""Gets the consume_time of this SubCustomerMonthlyBillDetail.

        消费时间。 包周期和预留实例订购场景下为订单支付时间；按需场景下为话单生失效时间。 格式：YYYY-MM-DDThh:mm:ssZ

        :return: The consume_time of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._consume_time

    @consume_time.setter
    def consume_time(self, consume_time):
        r"""Sets the consume_time of this SubCustomerMonthlyBillDetail.

        消费时间。 包周期和预留实例订购场景下为订单支付时间；按需场景下为话单生失效时间。 格式：YYYY-MM-DDThh:mm:ssZ

        :param consume_time: The consume_time of this SubCustomerMonthlyBillDetail.
        :type consume_time: str
        """
        self._consume_time = consume_time

    @property
    def usage_type(self):
        r"""Gets the usage_type of this SubCustomerMonthlyBillDetail.

        资源使用量的类型，您可以调用查询使用量类型列表接口获取。

        :return: The usage_type of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        r"""Sets the usage_type of this SubCustomerMonthlyBillDetail.

        资源使用量的类型，您可以调用查询使用量类型列表接口获取。

        :param usage_type: The usage_type of this SubCustomerMonthlyBillDetail.
        :type usage_type: str
        """
        self._usage_type = usage_type

    @property
    def usage_amount(self):
        r"""Gets the usage_amount of this SubCustomerMonthlyBillDetail.

        资源的使用量。

        :return: The usage_amount of this SubCustomerMonthlyBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._usage_amount

    @usage_amount.setter
    def usage_amount(self, usage_amount):
        r"""Sets the usage_amount of this SubCustomerMonthlyBillDetail.

        资源的使用量。

        :param usage_amount: The usage_amount of this SubCustomerMonthlyBillDetail.
        :type usage_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._usage_amount = usage_amount

    @property
    def usage_measure_id(self):
        r"""Gets the usage_measure_id of this SubCustomerMonthlyBillDetail.

        资源使用量的度量单位，您可以调用查询度量单位列表接口获取。

        :return: The usage_measure_id of this SubCustomerMonthlyBillDetail.
        :rtype: int
        """
        return self._usage_measure_id

    @usage_measure_id.setter
    def usage_measure_id(self, usage_measure_id):
        r"""Sets the usage_measure_id of this SubCustomerMonthlyBillDetail.

        资源使用量的度量单位，您可以调用查询度量单位列表接口获取。

        :param usage_measure_id: The usage_measure_id of this SubCustomerMonthlyBillDetail.
        :type usage_measure_id: int
        """
        self._usage_measure_id = usage_measure_id

    @property
    def free_resource_usage(self):
        r"""Gets the free_resource_usage of this SubCustomerMonthlyBillDetail.

        套餐内使用量。

        :return: The free_resource_usage of this SubCustomerMonthlyBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._free_resource_usage

    @free_resource_usage.setter
    def free_resource_usage(self, free_resource_usage):
        r"""Sets the free_resource_usage of this SubCustomerMonthlyBillDetail.

        套餐内使用量。

        :param free_resource_usage: The free_resource_usage of this SubCustomerMonthlyBillDetail.
        :type free_resource_usage: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._free_resource_usage = free_resource_usage

    @property
    def free_resource_measure_id(self):
        r"""Gets the free_resource_measure_id of this SubCustomerMonthlyBillDetail.

        套餐内使用量的度量单位，您可以调用查询度量单位列表接口获取。

        :return: The free_resource_measure_id of this SubCustomerMonthlyBillDetail.
        :rtype: int
        """
        return self._free_resource_measure_id

    @free_resource_measure_id.setter
    def free_resource_measure_id(self, free_resource_measure_id):
        r"""Sets the free_resource_measure_id of this SubCustomerMonthlyBillDetail.

        套餐内使用量的度量单位，您可以调用查询度量单位列表接口获取。

        :param free_resource_measure_id: The free_resource_measure_id of this SubCustomerMonthlyBillDetail.
        :type free_resource_measure_id: int
        """
        self._free_resource_measure_id = free_resource_measure_id

    @property
    def ri_usage(self):
        r"""Gets the ri_usage of this SubCustomerMonthlyBillDetail.

        预留实例使用量。

        :return: The ri_usage of this SubCustomerMonthlyBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._ri_usage

    @ri_usage.setter
    def ri_usage(self, ri_usage):
        r"""Sets the ri_usage of this SubCustomerMonthlyBillDetail.

        预留实例使用量。

        :param ri_usage: The ri_usage of this SubCustomerMonthlyBillDetail.
        :type ri_usage: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._ri_usage = ri_usage

    @property
    def ri_usage_measure_id(self):
        r"""Gets the ri_usage_measure_id of this SubCustomerMonthlyBillDetail.

        预留实例使用量单位。

        :return: The ri_usage_measure_id of this SubCustomerMonthlyBillDetail.
        :rtype: int
        """
        return self._ri_usage_measure_id

    @ri_usage_measure_id.setter
    def ri_usage_measure_id(self, ri_usage_measure_id):
        r"""Sets the ri_usage_measure_id of this SubCustomerMonthlyBillDetail.

        预留实例使用量单位。

        :param ri_usage_measure_id: The ri_usage_measure_id of this SubCustomerMonthlyBillDetail.
        :type ri_usage_measure_id: int
        """
        self._ri_usage_measure_id = ri_usage_measure_id

    @property
    def official_amount(self):
        r"""Gets the official_amount of this SubCustomerMonthlyBillDetail.

        官网价。

        :return: The official_amount of this SubCustomerMonthlyBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._official_amount

    @official_amount.setter
    def official_amount(self, official_amount):
        r"""Sets the official_amount of this SubCustomerMonthlyBillDetail.

        官网价。

        :param official_amount: The official_amount of this SubCustomerMonthlyBillDetail.
        :type official_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._official_amount = official_amount

    @property
    def official_discount_amount(self):
        r"""Gets the official_discount_amount of this SubCustomerMonthlyBillDetail.

        对应官网价折扣金额。

        :return: The official_discount_amount of this SubCustomerMonthlyBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._official_discount_amount

    @official_discount_amount.setter
    def official_discount_amount(self, official_discount_amount):
        r"""Sets the official_discount_amount of this SubCustomerMonthlyBillDetail.

        对应官网价折扣金额。

        :param official_discount_amount: The official_discount_amount of this SubCustomerMonthlyBillDetail.
        :type official_discount_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._official_discount_amount = official_discount_amount

    @property
    def payment_amount(self):
        r"""Gets the payment_amount of this SubCustomerMonthlyBillDetail.

        应付金额。

        :return: The payment_amount of this SubCustomerMonthlyBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, payment_amount):
        r"""Sets the payment_amount of this SubCustomerMonthlyBillDetail.

        应付金额。

        :param payment_amount: The payment_amount of this SubCustomerMonthlyBillDetail.
        :type payment_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._payment_amount = payment_amount

    @property
    def cash_amount(self):
        r"""Gets the cash_amount of this SubCustomerMonthlyBillDetail.

        现金支付金额。

        :return: The cash_amount of this SubCustomerMonthlyBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._cash_amount

    @cash_amount.setter
    def cash_amount(self, cash_amount):
        r"""Sets the cash_amount of this SubCustomerMonthlyBillDetail.

        现金支付金额。

        :param cash_amount: The cash_amount of this SubCustomerMonthlyBillDetail.
        :type cash_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._cash_amount = cash_amount

    @property
    def credit_amount(self):
        r"""Gets the credit_amount of this SubCustomerMonthlyBillDetail.

        信用额度支付金额。

        :return: The credit_amount of this SubCustomerMonthlyBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        r"""Sets the credit_amount of this SubCustomerMonthlyBillDetail.

        信用额度支付金额。

        :param credit_amount: The credit_amount of this SubCustomerMonthlyBillDetail.
        :type credit_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._credit_amount = credit_amount

    @property
    def coupon_amount(self):
        r"""Gets the coupon_amount of this SubCustomerMonthlyBillDetail.

        代金券支付金额。

        :return: The coupon_amount of this SubCustomerMonthlyBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        r"""Sets the coupon_amount of this SubCustomerMonthlyBillDetail.

        代金券支付金额。

        :param coupon_amount: The coupon_amount of this SubCustomerMonthlyBillDetail.
        :type coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._coupon_amount = coupon_amount

    @property
    def flexipurchase_coupon_amount(self):
        r"""Gets the flexipurchase_coupon_amount of this SubCustomerMonthlyBillDetail.

        现金券支付金额。

        :return: The flexipurchase_coupon_amount of this SubCustomerMonthlyBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._flexipurchase_coupon_amount

    @flexipurchase_coupon_amount.setter
    def flexipurchase_coupon_amount(self, flexipurchase_coupon_amount):
        r"""Sets the flexipurchase_coupon_amount of this SubCustomerMonthlyBillDetail.

        现金券支付金额。

        :param flexipurchase_coupon_amount: The flexipurchase_coupon_amount of this SubCustomerMonthlyBillDetail.
        :type flexipurchase_coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._flexipurchase_coupon_amount = flexipurchase_coupon_amount

    @property
    def stored_value_card_amount(self):
        r"""Gets the stored_value_card_amount of this SubCustomerMonthlyBillDetail.

        储值卡支付金额。

        :return: The stored_value_card_amount of this SubCustomerMonthlyBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._stored_value_card_amount

    @stored_value_card_amount.setter
    def stored_value_card_amount(self, stored_value_card_amount):
        r"""Sets the stored_value_card_amount of this SubCustomerMonthlyBillDetail.

        储值卡支付金额。

        :param stored_value_card_amount: The stored_value_card_amount of this SubCustomerMonthlyBillDetail.
        :type stored_value_card_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._stored_value_card_amount = stored_value_card_amount

    @property
    def debt_amount(self):
        r"""Gets the debt_amount of this SubCustomerMonthlyBillDetail.

        欠费金额。

        :return: The debt_amount of this SubCustomerMonthlyBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        r"""Sets the debt_amount of this SubCustomerMonthlyBillDetail.

        欠费金额。

        :param debt_amount: The debt_amount of this SubCustomerMonthlyBillDetail.
        :type debt_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._debt_amount = debt_amount

    @property
    def writeoff_amount(self):
        r"""Gets the writeoff_amount of this SubCustomerMonthlyBillDetail.

        欠费核销金额。

        :return: The writeoff_amount of this SubCustomerMonthlyBillDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._writeoff_amount

    @writeoff_amount.setter
    def writeoff_amount(self, writeoff_amount):
        r"""Sets the writeoff_amount of this SubCustomerMonthlyBillDetail.

        欠费核销金额。

        :param writeoff_amount: The writeoff_amount of this SubCustomerMonthlyBillDetail.
        :type writeoff_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._writeoff_amount = writeoff_amount

    @property
    def period_type(self):
        r"""Gets the period_type of this SubCustomerMonthlyBillDetail.

        周期类型： 19：年20：月24：天25：小时5：一次性

        :return: The period_type of this SubCustomerMonthlyBillDetail.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this SubCustomerMonthlyBillDetail.

        周期类型： 19：年20：月24：天25：小时5：一次性

        :param period_type: The period_type of this SubCustomerMonthlyBillDetail.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def account_manager_id(self):
        r"""Gets the account_manager_id of this SubCustomerMonthlyBillDetail.

        客户经理标识。

        :return: The account_manager_id of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._account_manager_id

    @account_manager_id.setter
    def account_manager_id(self, account_manager_id):
        r"""Sets the account_manager_id of this SubCustomerMonthlyBillDetail.

        客户经理标识。

        :param account_manager_id: The account_manager_id of this SubCustomerMonthlyBillDetail.
        :type account_manager_id: str
        """
        self._account_manager_id = account_manager_id

    @property
    def partner_id(self):
        r"""Gets the partner_id of this SubCustomerMonthlyBillDetail.

        关联的经销商ID。

        :return: The partner_id of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._partner_id

    @partner_id.setter
    def partner_id(self, partner_id):
        r"""Sets the partner_id of this SubCustomerMonthlyBillDetail.

        关联的经销商ID。

        :param partner_id: The partner_id of this SubCustomerMonthlyBillDetail.
        :type partner_id: str
        """
        self._partner_id = partner_id

    @property
    def region_name(self):
        r"""Gets the region_name of this SubCustomerMonthlyBillDetail.

        云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。

        :return: The region_name of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this SubCustomerMonthlyBillDetail.

        云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。

        :param region_name: The region_name of this SubCustomerMonthlyBillDetail.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def sub_service_type_code(self):
        r"""Gets the sub_service_type_code of this SubCustomerMonthlyBillDetail.

        整机的子云服务的自身的云服务类型编码。

        :return: The sub_service_type_code of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._sub_service_type_code

    @sub_service_type_code.setter
    def sub_service_type_code(self, sub_service_type_code):
        r"""Sets the sub_service_type_code of this SubCustomerMonthlyBillDetail.

        整机的子云服务的自身的云服务类型编码。

        :param sub_service_type_code: The sub_service_type_code of this SubCustomerMonthlyBillDetail.
        :type sub_service_type_code: str
        """
        self._sub_service_type_code = sub_service_type_code

    @property
    def sub_service_type_name(self):
        r"""Gets the sub_service_type_name of this SubCustomerMonthlyBillDetail.

        整机的子云服务的自身的云服务类型名称。

        :return: The sub_service_type_name of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._sub_service_type_name

    @sub_service_type_name.setter
    def sub_service_type_name(self, sub_service_type_name):
        r"""Sets the sub_service_type_name of this SubCustomerMonthlyBillDetail.

        整机的子云服务的自身的云服务类型名称。

        :param sub_service_type_name: The sub_service_type_name of this SubCustomerMonthlyBillDetail.
        :type sub_service_type_name: str
        """
        self._sub_service_type_name = sub_service_type_name

    @property
    def sub_resource_type_code(self):
        r"""Gets the sub_resource_type_code of this SubCustomerMonthlyBillDetail.

        整机的子云服务的自身的资源类型编码。

        :return: The sub_resource_type_code of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._sub_resource_type_code

    @sub_resource_type_code.setter
    def sub_resource_type_code(self, sub_resource_type_code):
        r"""Sets the sub_resource_type_code of this SubCustomerMonthlyBillDetail.

        整机的子云服务的自身的资源类型编码。

        :param sub_resource_type_code: The sub_resource_type_code of this SubCustomerMonthlyBillDetail.
        :type sub_resource_type_code: str
        """
        self._sub_resource_type_code = sub_resource_type_code

    @property
    def sub_resource_type_name(self):
        r"""Gets the sub_resource_type_name of this SubCustomerMonthlyBillDetail.

        整机的子云服务的自身的资源类型名称。

        :return: The sub_resource_type_name of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._sub_resource_type_name

    @sub_resource_type_name.setter
    def sub_resource_type_name(self, sub_resource_type_name):
        r"""Sets the sub_resource_type_name of this SubCustomerMonthlyBillDetail.

        整机的子云服务的自身的资源类型名称。

        :param sub_resource_type_name: The sub_resource_type_name of this SubCustomerMonthlyBillDetail.
        :type sub_resource_type_name: str
        """
        self._sub_resource_type_name = sub_resource_type_name

    @property
    def sub_resource_id(self):
        r"""Gets the sub_resource_id of this SubCustomerMonthlyBillDetail.

        整机的子云服务的自身的资源ID，资源标识。（如果为预留实例，则为预留实例标识）

        :return: The sub_resource_id of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._sub_resource_id

    @sub_resource_id.setter
    def sub_resource_id(self, sub_resource_id):
        r"""Sets the sub_resource_id of this SubCustomerMonthlyBillDetail.

        整机的子云服务的自身的资源ID，资源标识。（如果为预留实例，则为预留实例标识）

        :param sub_resource_id: The sub_resource_id of this SubCustomerMonthlyBillDetail.
        :type sub_resource_id: str
        """
        self._sub_resource_id = sub_resource_id

    @property
    def sub_resource_name(self):
        r"""Gets the sub_resource_name of this SubCustomerMonthlyBillDetail.

        整机的子云服务的自身的资源名称，资源标识。（如果为预留实例，则为预留实例标识）

        :return: The sub_resource_name of this SubCustomerMonthlyBillDetail.
        :rtype: str
        """
        return self._sub_resource_name

    @sub_resource_name.setter
    def sub_resource_name(self, sub_resource_name):
        r"""Sets the sub_resource_name of this SubCustomerMonthlyBillDetail.

        整机的子云服务的自身的资源名称，资源标识。（如果为预留实例，则为预留实例标识）

        :param sub_resource_name: The sub_resource_name of this SubCustomerMonthlyBillDetail.
        :type sub_resource_name: str
        """
        self._sub_resource_name = sub_resource_name

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
        if not isinstance(other, SubCustomerMonthlyBillDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
