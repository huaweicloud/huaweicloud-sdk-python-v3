# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MonthlyBillRes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cycle': 'str',
        'bill_date': 'str',
        'bill_type': 'int',
        'customer_id': 'str',
        'region': 'str',
        'region_name': 'str',
        'cloud_service_type': 'str',
        'resource_type_code': 'str',
        'cloud_service_type_name': 'str',
        'resource_type_name': 'str',
        'res_instance_id': 'str',
        'resource_name': 'str',
        'resource_tag': 'str',
        'sku_code': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'charge_mode': 'int',
        'consume_amount': 'decimal.Decimal',
        'cash_amount': 'decimal.Decimal',
        'credit_amount': 'decimal.Decimal',
        'coupon_amount': 'decimal.Decimal',
        'flexipurchase_coupon_amount': 'decimal.Decimal',
        'stored_card_amount': 'decimal.Decimal',
        'bonus_amount': 'decimal.Decimal',
        'debt_amount': 'decimal.Decimal',
        'adjustment_amount': 'decimal.Decimal',
        'official_amount': 'decimal.Decimal',
        'discount_amount': 'decimal.Decimal',
        'measure_id': 'int',
        'period_type': 'int',
        'root_resource_id': 'str',
        'parent_resource_id': 'str',
        'trade_id': 'str',
        'id': 'str',
        'product_spec_desc': 'str',
        'sub_service_type_code': 'str',
        'sub_service_type_name': 'str',
        'sub_resource_type_code': 'str',
        'sub_resource_type_name': 'str',
        'sub_resource_id': 'str',
        'sub_resource_name': 'str',
        'pre_order_id': 'str',
        'az_code_infos': 'list[AzCodeInfo]',
        'payer_account_id': 'str',
        'effective_time': 'str',
        'expire_time': 'str',
        'consume_time': 'str',
        'be_id': 'str',
        'extend_params': 'ResRelation'
    }

    attribute_map = {
        'cycle': 'cycle',
        'bill_date': 'bill_date',
        'bill_type': 'bill_type',
        'customer_id': 'customer_id',
        'region': 'region',
        'region_name': 'region_name',
        'cloud_service_type': 'cloud_service_type',
        'resource_type_code': 'resource_Type_code',
        'cloud_service_type_name': 'cloud_service_type_name',
        'resource_type_name': 'resource_type_name',
        'res_instance_id': 'res_instance_id',
        'resource_name': 'resource_name',
        'resource_tag': 'resource_tag',
        'sku_code': 'sku_code',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'charge_mode': 'charge_mode',
        'consume_amount': 'consume_amount',
        'cash_amount': 'cash_amount',
        'credit_amount': 'credit_amount',
        'coupon_amount': 'coupon_amount',
        'flexipurchase_coupon_amount': 'flexipurchase_coupon_amount',
        'stored_card_amount': 'stored_card_amount',
        'bonus_amount': 'bonus_amount',
        'debt_amount': 'debt_amount',
        'adjustment_amount': 'adjustment_amount',
        'official_amount': 'official_amount',
        'discount_amount': 'discount_amount',
        'measure_id': 'measure_id',
        'period_type': 'period_type',
        'root_resource_id': 'root_resource_id',
        'parent_resource_id': 'parent_resource_id',
        'trade_id': 'trade_id',
        'id': 'id',
        'product_spec_desc': 'product_spec_desc',
        'sub_service_type_code': 'sub_service_type_code',
        'sub_service_type_name': 'sub_service_type_name',
        'sub_resource_type_code': 'sub_resource_type_code',
        'sub_resource_type_name': 'sub_resource_type_name',
        'sub_resource_id': 'sub_resource_id',
        'sub_resource_name': 'sub_resource_name',
        'pre_order_id': 'pre_order_id',
        'az_code_infos': 'az_code_infos',
        'payer_account_id': 'payer_account_id',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time',
        'consume_time': 'consume_time',
        'be_id': 'be_id',
        'extend_params': 'extend_params'
    }

    def __init__(self, cycle=None, bill_date=None, bill_type=None, customer_id=None, region=None, region_name=None, cloud_service_type=None, resource_type_code=None, cloud_service_type_name=None, resource_type_name=None, res_instance_id=None, resource_name=None, resource_tag=None, sku_code=None, enterprise_project_id=None, enterprise_project_name=None, charge_mode=None, consume_amount=None, cash_amount=None, credit_amount=None, coupon_amount=None, flexipurchase_coupon_amount=None, stored_card_amount=None, bonus_amount=None, debt_amount=None, adjustment_amount=None, official_amount=None, discount_amount=None, measure_id=None, period_type=None, root_resource_id=None, parent_resource_id=None, trade_id=None, id=None, product_spec_desc=None, sub_service_type_code=None, sub_service_type_name=None, sub_resource_type_code=None, sub_resource_type_name=None, sub_resource_id=None, sub_resource_name=None, pre_order_id=None, az_code_infos=None, payer_account_id=None, effective_time=None, expire_time=None, consume_time=None, be_id=None, extend_params=None):
        r"""MonthlyBillRes

        The model defined in huaweicloud sdk

        :param cycle: 资源详单数据所在账期，东八区时间，格式为YYYY-MM。 例如2020-01。
        :type cycle: str
        :param bill_date: 消费日期，东八区时间，格式为YYYY-MM-DD。  说明： 当statistic_type&#x3D;2时该字段才有值，否则返回null。
        :type bill_date: str
        :param bill_type: 账单类型。1：消费-新购 2：消费-续订 3：消费-变更 4：退款-退订 5：消费-使用 8：消费-自动续订 9：调账-补偿 14：消费-服务支持计划月末扣费 16：调账-扣费 18：消费-按月付费 20：退款-变更 23：消费-节省计划抵扣 24：退款-包年/包月转按需 25：消费-抹零补扣 103：消费-按年付费
        :type bill_type: int
        :param customer_id: 消费的客户账号ID。 如果是普通客户或者企业子客户查询消费记录，只能查询到客户自己的消费记录，且此处显示的是客户自己的客户ID。如果是企业主查询消费记录，可以查询到企业主以及企业子客户的消费记录，此处为消费的实际客户ID。如果是企业主自己的消费记录，则为企业主ID；如果是某个企业子客户的消费记录，则此处为企业子账号ID。
        :type customer_id: str
        :param region: 云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。
        :type region: str
        :param region_name: 云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。
        :type region_name: str
        :param cloud_service_type: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。
        :type cloud_service_type: str
        :param resource_type_code: 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。
        :type resource_type_code: str
        :param cloud_service_type_name: 云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。
        :type cloud_service_type_name: str
        :param resource_type_name: 资源类型名称。例如ECS的资源类型名称为“云主机”。
        :type resource_type_name: str
        :param res_instance_id: 资源实例ID。
        :type res_instance_id: str
        :param resource_name: 资源名称。客户在创建资源的时候，可以输入资源名称，有些资源也可以在管理资源时，修改资源名称。
        :type resource_name: str
        :param resource_tag: 资源标签。客户在管理资源的时候，可以设置资源标签。
        :type resource_tag: str
        :param sku_code: SKU编码，在账单中唯一标识一个资源的规格。
        :type sku_code: str
        :param enterprise_project_id: 企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目名称。
        :type enterprise_project_name: str
        :param charge_mode: 计费模式。 1 : 包年/包月3：按需10：预留实例11：节省计划
        :type charge_mode: int
        :param consume_amount: 客户购买云服务类型的消费金额，包含代金券、现金券，精确到小数点后2位。  说明： consume_amount的值等于cash_amount，credit_amount，coupon_amount，flexipurchase_coupon_amount，stored_card_amount，bonus_amount，debt_amount，adjustment_amount的总和。
        :type consume_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param cash_amount: 现金支付金额。
        :type cash_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param credit_amount: 信用额度支付金额。
        :type credit_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param coupon_amount: 代金券支付金额。
        :type coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param flexipurchase_coupon_amount: 现金券支付金额。
        :type flexipurchase_coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param stored_card_amount: 储值卡支付金额。
        :type stored_card_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param bonus_amount: 奖励金支付金额（用于现网客户未使用完的奖励金）。
        :type bonus_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param debt_amount: 欠费金额。
        :type debt_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param adjustment_amount: 欠费核销金额。
        :type adjustment_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param official_amount: 官网价。
        :type official_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param discount_amount: 对应官网价折扣金额。
        :type discount_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param measure_id: 金额单位。 1：元
        :type measure_id: int
        :param period_type: 周期类型： 19：年20：月24：天25：小时5：一次性
        :type period_type: int
        :param root_resource_id: 根资源标识。
        :type root_resource_id: str
        :param parent_resource_id: 父资源标识。
        :type parent_resource_id: str
        :param trade_id: 订单ID 或 交易ID。 账单类型为1，2，3，4，8时为订单ID；其它场景下为： 交易ID(非月末扣费：应收ID；月末扣费：账单ID)。
        :type trade_id: str
        :param id: 唯一标识。 该字段为预留字段。
        :type id: str
        :param product_spec_desc: 产品的规格描述。
        :type product_spec_desc: str
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
        :param pre_order_id: 原订单ID 。
        :type pre_order_id: str
        :param az_code_infos: 可用区信息列表。具体请参见表 AzCodeInfo。
        :type az_code_infos: list[:class:`huaweicloudsdkbss.v2.AzCodeInfo`]
        :param payer_account_id: |参数名称：支付账号ID。| |参数的约束及描述：如果是普通客户或者财务独立企业子客户或者企业主客户查询消费记录，此处为客户自己的客户ID。如果是财务托管企业子查询消费记录，此处为企业主客户ID或自己的客户ID。|
        :type payer_account_id: str
        :param effective_time: |参数名称：费用对应的资源使用的开始时间| |参数的约束及描述：费用对应的资源使用的开始时间，statistic_type&#x3D;3有效，statistic_type&#x3D;1或者2该字段保留。|
        :type effective_time: str
        :param expire_time: |参数名称：费用对应的资源使用的结束时间| |参数的约束及描述：费用对应的资源使用的结束时间，statistic_type&#x3D;3有效，statistic_type&#x3D;1或者2该字段保留。|
        :type expire_time: str
        :param consume_time: |参数名称：消费时间| |参数约束及描述：消费时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ。包周期、预留实例预付为交易时间，按需、预留实例按时计费为话单生失效时间。 说明：当statistic_type&#x3D;3时有效。|
        :type consume_time: str
        :param be_id: |参数名称：华为云运营实体ID。| |参数约束及描述：华为云运营实体ID。|
        :type be_id: str
        :param extend_params: 
        :type extend_params: :class:`huaweicloudsdkbss.v2.ResRelation`
        """
        
        

        self._cycle = None
        self._bill_date = None
        self._bill_type = None
        self._customer_id = None
        self._region = None
        self._region_name = None
        self._cloud_service_type = None
        self._resource_type_code = None
        self._cloud_service_type_name = None
        self._resource_type_name = None
        self._res_instance_id = None
        self._resource_name = None
        self._resource_tag = None
        self._sku_code = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._charge_mode = None
        self._consume_amount = None
        self._cash_amount = None
        self._credit_amount = None
        self._coupon_amount = None
        self._flexipurchase_coupon_amount = None
        self._stored_card_amount = None
        self._bonus_amount = None
        self._debt_amount = None
        self._adjustment_amount = None
        self._official_amount = None
        self._discount_amount = None
        self._measure_id = None
        self._period_type = None
        self._root_resource_id = None
        self._parent_resource_id = None
        self._trade_id = None
        self._id = None
        self._product_spec_desc = None
        self._sub_service_type_code = None
        self._sub_service_type_name = None
        self._sub_resource_type_code = None
        self._sub_resource_type_name = None
        self._sub_resource_id = None
        self._sub_resource_name = None
        self._pre_order_id = None
        self._az_code_infos = None
        self._payer_account_id = None
        self._effective_time = None
        self._expire_time = None
        self._consume_time = None
        self._be_id = None
        self._extend_params = None
        self.discriminator = None

        if cycle is not None:
            self.cycle = cycle
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
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if cloud_service_type_name is not None:
            self.cloud_service_type_name = cloud_service_type_name
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if res_instance_id is not None:
            self.res_instance_id = res_instance_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_tag is not None:
            self.resource_tag = resource_tag
        if sku_code is not None:
            self.sku_code = sku_code
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if charge_mode is not None:
            self.charge_mode = charge_mode
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
        if stored_card_amount is not None:
            self.stored_card_amount = stored_card_amount
        if bonus_amount is not None:
            self.bonus_amount = bonus_amount
        if debt_amount is not None:
            self.debt_amount = debt_amount
        if adjustment_amount is not None:
            self.adjustment_amount = adjustment_amount
        if official_amount is not None:
            self.official_amount = official_amount
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if period_type is not None:
            self.period_type = period_type
        if root_resource_id is not None:
            self.root_resource_id = root_resource_id
        if parent_resource_id is not None:
            self.parent_resource_id = parent_resource_id
        if trade_id is not None:
            self.trade_id = trade_id
        if id is not None:
            self.id = id
        if product_spec_desc is not None:
            self.product_spec_desc = product_spec_desc
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
        if pre_order_id is not None:
            self.pre_order_id = pre_order_id
        if az_code_infos is not None:
            self.az_code_infos = az_code_infos
        if payer_account_id is not None:
            self.payer_account_id = payer_account_id
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time
        if consume_time is not None:
            self.consume_time = consume_time
        if be_id is not None:
            self.be_id = be_id
        if extend_params is not None:
            self.extend_params = extend_params

    @property
    def cycle(self):
        r"""Gets the cycle of this MonthlyBillRes.

        资源详单数据所在账期，东八区时间，格式为YYYY-MM。 例如2020-01。

        :return: The cycle of this MonthlyBillRes.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        r"""Sets the cycle of this MonthlyBillRes.

        资源详单数据所在账期，东八区时间，格式为YYYY-MM。 例如2020-01。

        :param cycle: The cycle of this MonthlyBillRes.
        :type cycle: str
        """
        self._cycle = cycle

    @property
    def bill_date(self):
        r"""Gets the bill_date of this MonthlyBillRes.

        消费日期，东八区时间，格式为YYYY-MM-DD。  说明： 当statistic_type=2时该字段才有值，否则返回null。

        :return: The bill_date of this MonthlyBillRes.
        :rtype: str
        """
        return self._bill_date

    @bill_date.setter
    def bill_date(self, bill_date):
        r"""Sets the bill_date of this MonthlyBillRes.

        消费日期，东八区时间，格式为YYYY-MM-DD。  说明： 当statistic_type=2时该字段才有值，否则返回null。

        :param bill_date: The bill_date of this MonthlyBillRes.
        :type bill_date: str
        """
        self._bill_date = bill_date

    @property
    def bill_type(self):
        r"""Gets the bill_type of this MonthlyBillRes.

        账单类型。1：消费-新购 2：消费-续订 3：消费-变更 4：退款-退订 5：消费-使用 8：消费-自动续订 9：调账-补偿 14：消费-服务支持计划月末扣费 16：调账-扣费 18：消费-按月付费 20：退款-变更 23：消费-节省计划抵扣 24：退款-包年/包月转按需 25：消费-抹零补扣 103：消费-按年付费

        :return: The bill_type of this MonthlyBillRes.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        r"""Sets the bill_type of this MonthlyBillRes.

        账单类型。1：消费-新购 2：消费-续订 3：消费-变更 4：退款-退订 5：消费-使用 8：消费-自动续订 9：调账-补偿 14：消费-服务支持计划月末扣费 16：调账-扣费 18：消费-按月付费 20：退款-变更 23：消费-节省计划抵扣 24：退款-包年/包月转按需 25：消费-抹零补扣 103：消费-按年付费

        :param bill_type: The bill_type of this MonthlyBillRes.
        :type bill_type: int
        """
        self._bill_type = bill_type

    @property
    def customer_id(self):
        r"""Gets the customer_id of this MonthlyBillRes.

        消费的客户账号ID。 如果是普通客户或者企业子客户查询消费记录，只能查询到客户自己的消费记录，且此处显示的是客户自己的客户ID。如果是企业主查询消费记录，可以查询到企业主以及企业子客户的消费记录，此处为消费的实际客户ID。如果是企业主自己的消费记录，则为企业主ID；如果是某个企业子客户的消费记录，则此处为企业子账号ID。

        :return: The customer_id of this MonthlyBillRes.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this MonthlyBillRes.

        消费的客户账号ID。 如果是普通客户或者企业子客户查询消费记录，只能查询到客户自己的消费记录，且此处显示的是客户自己的客户ID。如果是企业主查询消费记录，可以查询到企业主以及企业子客户的消费记录，此处为消费的实际客户ID。如果是企业主自己的消费记录，则为企业主ID；如果是某个企业子客户的消费记录，则此处为企业子账号ID。

        :param customer_id: The customer_id of this MonthlyBillRes.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def region(self):
        r"""Gets the region of this MonthlyBillRes.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :return: The region of this MonthlyBillRes.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this MonthlyBillRes.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :param region: The region of this MonthlyBillRes.
        :type region: str
        """
        self._region = region

    @property
    def region_name(self):
        r"""Gets the region_name of this MonthlyBillRes.

        云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。

        :return: The region_name of this MonthlyBillRes.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this MonthlyBillRes.

        云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。

        :param region_name: The region_name of this MonthlyBillRes.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this MonthlyBillRes.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :return: The cloud_service_type of this MonthlyBillRes.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this MonthlyBillRes.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :param cloud_service_type: The cloud_service_type of this MonthlyBillRes.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type_code(self):
        r"""Gets the resource_type_code of this MonthlyBillRes.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :return: The resource_type_code of this MonthlyBillRes.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        r"""Sets the resource_type_code of this MonthlyBillRes.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :param resource_type_code: The resource_type_code of this MonthlyBillRes.
        :type resource_type_code: str
        """
        self._resource_type_code = resource_type_code

    @property
    def cloud_service_type_name(self):
        r"""Gets the cloud_service_type_name of this MonthlyBillRes.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :return: The cloud_service_type_name of this MonthlyBillRes.
        :rtype: str
        """
        return self._cloud_service_type_name

    @cloud_service_type_name.setter
    def cloud_service_type_name(self, cloud_service_type_name):
        r"""Sets the cloud_service_type_name of this MonthlyBillRes.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :param cloud_service_type_name: The cloud_service_type_name of this MonthlyBillRes.
        :type cloud_service_type_name: str
        """
        self._cloud_service_type_name = cloud_service_type_name

    @property
    def resource_type_name(self):
        r"""Gets the resource_type_name of this MonthlyBillRes.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :return: The resource_type_name of this MonthlyBillRes.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        r"""Sets the resource_type_name of this MonthlyBillRes.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :param resource_type_name: The resource_type_name of this MonthlyBillRes.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def res_instance_id(self):
        r"""Gets the res_instance_id of this MonthlyBillRes.

        资源实例ID。

        :return: The res_instance_id of this MonthlyBillRes.
        :rtype: str
        """
        return self._res_instance_id

    @res_instance_id.setter
    def res_instance_id(self, res_instance_id):
        r"""Sets the res_instance_id of this MonthlyBillRes.

        资源实例ID。

        :param res_instance_id: The res_instance_id of this MonthlyBillRes.
        :type res_instance_id: str
        """
        self._res_instance_id = res_instance_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this MonthlyBillRes.

        资源名称。客户在创建资源的时候，可以输入资源名称，有些资源也可以在管理资源时，修改资源名称。

        :return: The resource_name of this MonthlyBillRes.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this MonthlyBillRes.

        资源名称。客户在创建资源的时候，可以输入资源名称，有些资源也可以在管理资源时，修改资源名称。

        :param resource_name: The resource_name of this MonthlyBillRes.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_tag(self):
        r"""Gets the resource_tag of this MonthlyBillRes.

        资源标签。客户在管理资源的时候，可以设置资源标签。

        :return: The resource_tag of this MonthlyBillRes.
        :rtype: str
        """
        return self._resource_tag

    @resource_tag.setter
    def resource_tag(self, resource_tag):
        r"""Sets the resource_tag of this MonthlyBillRes.

        资源标签。客户在管理资源的时候，可以设置资源标签。

        :param resource_tag: The resource_tag of this MonthlyBillRes.
        :type resource_tag: str
        """
        self._resource_tag = resource_tag

    @property
    def sku_code(self):
        r"""Gets the sku_code of this MonthlyBillRes.

        SKU编码，在账单中唯一标识一个资源的规格。

        :return: The sku_code of this MonthlyBillRes.
        :rtype: str
        """
        return self._sku_code

    @sku_code.setter
    def sku_code(self, sku_code):
        r"""Sets the sku_code of this MonthlyBillRes.

        SKU编码，在账单中唯一标识一个资源的规格。

        :param sku_code: The sku_code of this MonthlyBillRes.
        :type sku_code: str
        """
        self._sku_code = sku_code

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this MonthlyBillRes.

        企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :return: The enterprise_project_id of this MonthlyBillRes.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this MonthlyBillRes.

        企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :param enterprise_project_id: The enterprise_project_id of this MonthlyBillRes.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this MonthlyBillRes.

        企业项目名称。

        :return: The enterprise_project_name of this MonthlyBillRes.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this MonthlyBillRes.

        企业项目名称。

        :param enterprise_project_name: The enterprise_project_name of this MonthlyBillRes.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this MonthlyBillRes.

        计费模式。 1 : 包年/包月3：按需10：预留实例11：节省计划

        :return: The charge_mode of this MonthlyBillRes.
        :rtype: int
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this MonthlyBillRes.

        计费模式。 1 : 包年/包月3：按需10：预留实例11：节省计划

        :param charge_mode: The charge_mode of this MonthlyBillRes.
        :type charge_mode: int
        """
        self._charge_mode = charge_mode

    @property
    def consume_amount(self):
        r"""Gets the consume_amount of this MonthlyBillRes.

        客户购买云服务类型的消费金额，包含代金券、现金券，精确到小数点后2位。  说明： consume_amount的值等于cash_amount，credit_amount，coupon_amount，flexipurchase_coupon_amount，stored_card_amount，bonus_amount，debt_amount，adjustment_amount的总和。

        :return: The consume_amount of this MonthlyBillRes.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._consume_amount

    @consume_amount.setter
    def consume_amount(self, consume_amount):
        r"""Sets the consume_amount of this MonthlyBillRes.

        客户购买云服务类型的消费金额，包含代金券、现金券，精确到小数点后2位。  说明： consume_amount的值等于cash_amount，credit_amount，coupon_amount，flexipurchase_coupon_amount，stored_card_amount，bonus_amount，debt_amount，adjustment_amount的总和。

        :param consume_amount: The consume_amount of this MonthlyBillRes.
        :type consume_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._consume_amount = consume_amount

    @property
    def cash_amount(self):
        r"""Gets the cash_amount of this MonthlyBillRes.

        现金支付金额。

        :return: The cash_amount of this MonthlyBillRes.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._cash_amount

    @cash_amount.setter
    def cash_amount(self, cash_amount):
        r"""Sets the cash_amount of this MonthlyBillRes.

        现金支付金额。

        :param cash_amount: The cash_amount of this MonthlyBillRes.
        :type cash_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._cash_amount = cash_amount

    @property
    def credit_amount(self):
        r"""Gets the credit_amount of this MonthlyBillRes.

        信用额度支付金额。

        :return: The credit_amount of this MonthlyBillRes.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        r"""Sets the credit_amount of this MonthlyBillRes.

        信用额度支付金额。

        :param credit_amount: The credit_amount of this MonthlyBillRes.
        :type credit_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._credit_amount = credit_amount

    @property
    def coupon_amount(self):
        r"""Gets the coupon_amount of this MonthlyBillRes.

        代金券支付金额。

        :return: The coupon_amount of this MonthlyBillRes.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        r"""Sets the coupon_amount of this MonthlyBillRes.

        代金券支付金额。

        :param coupon_amount: The coupon_amount of this MonthlyBillRes.
        :type coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._coupon_amount = coupon_amount

    @property
    def flexipurchase_coupon_amount(self):
        r"""Gets the flexipurchase_coupon_amount of this MonthlyBillRes.

        现金券支付金额。

        :return: The flexipurchase_coupon_amount of this MonthlyBillRes.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._flexipurchase_coupon_amount

    @flexipurchase_coupon_amount.setter
    def flexipurchase_coupon_amount(self, flexipurchase_coupon_amount):
        r"""Sets the flexipurchase_coupon_amount of this MonthlyBillRes.

        现金券支付金额。

        :param flexipurchase_coupon_amount: The flexipurchase_coupon_amount of this MonthlyBillRes.
        :type flexipurchase_coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._flexipurchase_coupon_amount = flexipurchase_coupon_amount

    @property
    def stored_card_amount(self):
        r"""Gets the stored_card_amount of this MonthlyBillRes.

        储值卡支付金额。

        :return: The stored_card_amount of this MonthlyBillRes.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._stored_card_amount

    @stored_card_amount.setter
    def stored_card_amount(self, stored_card_amount):
        r"""Sets the stored_card_amount of this MonthlyBillRes.

        储值卡支付金额。

        :param stored_card_amount: The stored_card_amount of this MonthlyBillRes.
        :type stored_card_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._stored_card_amount = stored_card_amount

    @property
    def bonus_amount(self):
        r"""Gets the bonus_amount of this MonthlyBillRes.

        奖励金支付金额（用于现网客户未使用完的奖励金）。

        :return: The bonus_amount of this MonthlyBillRes.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._bonus_amount

    @bonus_amount.setter
    def bonus_amount(self, bonus_amount):
        r"""Sets the bonus_amount of this MonthlyBillRes.

        奖励金支付金额（用于现网客户未使用完的奖励金）。

        :param bonus_amount: The bonus_amount of this MonthlyBillRes.
        :type bonus_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._bonus_amount = bonus_amount

    @property
    def debt_amount(self):
        r"""Gets the debt_amount of this MonthlyBillRes.

        欠费金额。

        :return: The debt_amount of this MonthlyBillRes.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        r"""Sets the debt_amount of this MonthlyBillRes.

        欠费金额。

        :param debt_amount: The debt_amount of this MonthlyBillRes.
        :type debt_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._debt_amount = debt_amount

    @property
    def adjustment_amount(self):
        r"""Gets the adjustment_amount of this MonthlyBillRes.

        欠费核销金额。

        :return: The adjustment_amount of this MonthlyBillRes.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._adjustment_amount

    @adjustment_amount.setter
    def adjustment_amount(self, adjustment_amount):
        r"""Sets the adjustment_amount of this MonthlyBillRes.

        欠费核销金额。

        :param adjustment_amount: The adjustment_amount of this MonthlyBillRes.
        :type adjustment_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._adjustment_amount = adjustment_amount

    @property
    def official_amount(self):
        r"""Gets the official_amount of this MonthlyBillRes.

        官网价。

        :return: The official_amount of this MonthlyBillRes.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._official_amount

    @official_amount.setter
    def official_amount(self, official_amount):
        r"""Sets the official_amount of this MonthlyBillRes.

        官网价。

        :param official_amount: The official_amount of this MonthlyBillRes.
        :type official_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._official_amount = official_amount

    @property
    def discount_amount(self):
        r"""Gets the discount_amount of this MonthlyBillRes.

        对应官网价折扣金额。

        :return: The discount_amount of this MonthlyBillRes.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        r"""Sets the discount_amount of this MonthlyBillRes.

        对应官网价折扣金额。

        :param discount_amount: The discount_amount of this MonthlyBillRes.
        :type discount_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._discount_amount = discount_amount

    @property
    def measure_id(self):
        r"""Gets the measure_id of this MonthlyBillRes.

        金额单位。 1：元

        :return: The measure_id of this MonthlyBillRes.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this MonthlyBillRes.

        金额单位。 1：元

        :param measure_id: The measure_id of this MonthlyBillRes.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def period_type(self):
        r"""Gets the period_type of this MonthlyBillRes.

        周期类型： 19：年20：月24：天25：小时5：一次性

        :return: The period_type of this MonthlyBillRes.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this MonthlyBillRes.

        周期类型： 19：年20：月24：天25：小时5：一次性

        :param period_type: The period_type of this MonthlyBillRes.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def root_resource_id(self):
        r"""Gets the root_resource_id of this MonthlyBillRes.

        根资源标识。

        :return: The root_resource_id of this MonthlyBillRes.
        :rtype: str
        """
        return self._root_resource_id

    @root_resource_id.setter
    def root_resource_id(self, root_resource_id):
        r"""Sets the root_resource_id of this MonthlyBillRes.

        根资源标识。

        :param root_resource_id: The root_resource_id of this MonthlyBillRes.
        :type root_resource_id: str
        """
        self._root_resource_id = root_resource_id

    @property
    def parent_resource_id(self):
        r"""Gets the parent_resource_id of this MonthlyBillRes.

        父资源标识。

        :return: The parent_resource_id of this MonthlyBillRes.
        :rtype: str
        """
        return self._parent_resource_id

    @parent_resource_id.setter
    def parent_resource_id(self, parent_resource_id):
        r"""Sets the parent_resource_id of this MonthlyBillRes.

        父资源标识。

        :param parent_resource_id: The parent_resource_id of this MonthlyBillRes.
        :type parent_resource_id: str
        """
        self._parent_resource_id = parent_resource_id

    @property
    def trade_id(self):
        r"""Gets the trade_id of this MonthlyBillRes.

        订单ID 或 交易ID。 账单类型为1，2，3，4，8时为订单ID；其它场景下为： 交易ID(非月末扣费：应收ID；月末扣费：账单ID)。

        :return: The trade_id of this MonthlyBillRes.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        r"""Sets the trade_id of this MonthlyBillRes.

        订单ID 或 交易ID。 账单类型为1，2，3，4，8时为订单ID；其它场景下为： 交易ID(非月末扣费：应收ID；月末扣费：账单ID)。

        :param trade_id: The trade_id of this MonthlyBillRes.
        :type trade_id: str
        """
        self._trade_id = trade_id

    @property
    def id(self):
        r"""Gets the id of this MonthlyBillRes.

        唯一标识。 该字段为预留字段。

        :return: The id of this MonthlyBillRes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MonthlyBillRes.

        唯一标识。 该字段为预留字段。

        :param id: The id of this MonthlyBillRes.
        :type id: str
        """
        self._id = id

    @property
    def product_spec_desc(self):
        r"""Gets the product_spec_desc of this MonthlyBillRes.

        产品的规格描述。

        :return: The product_spec_desc of this MonthlyBillRes.
        :rtype: str
        """
        return self._product_spec_desc

    @product_spec_desc.setter
    def product_spec_desc(self, product_spec_desc):
        r"""Sets the product_spec_desc of this MonthlyBillRes.

        产品的规格描述。

        :param product_spec_desc: The product_spec_desc of this MonthlyBillRes.
        :type product_spec_desc: str
        """
        self._product_spec_desc = product_spec_desc

    @property
    def sub_service_type_code(self):
        r"""Gets the sub_service_type_code of this MonthlyBillRes.

        整机的子云服务的自身的云服务类型编码。

        :return: The sub_service_type_code of this MonthlyBillRes.
        :rtype: str
        """
        return self._sub_service_type_code

    @sub_service_type_code.setter
    def sub_service_type_code(self, sub_service_type_code):
        r"""Sets the sub_service_type_code of this MonthlyBillRes.

        整机的子云服务的自身的云服务类型编码。

        :param sub_service_type_code: The sub_service_type_code of this MonthlyBillRes.
        :type sub_service_type_code: str
        """
        self._sub_service_type_code = sub_service_type_code

    @property
    def sub_service_type_name(self):
        r"""Gets the sub_service_type_name of this MonthlyBillRes.

        整机的子云服务的自身的云服务类型名称。

        :return: The sub_service_type_name of this MonthlyBillRes.
        :rtype: str
        """
        return self._sub_service_type_name

    @sub_service_type_name.setter
    def sub_service_type_name(self, sub_service_type_name):
        r"""Sets the sub_service_type_name of this MonthlyBillRes.

        整机的子云服务的自身的云服务类型名称。

        :param sub_service_type_name: The sub_service_type_name of this MonthlyBillRes.
        :type sub_service_type_name: str
        """
        self._sub_service_type_name = sub_service_type_name

    @property
    def sub_resource_type_code(self):
        r"""Gets the sub_resource_type_code of this MonthlyBillRes.

        整机的子云服务的自身的资源类型编码。

        :return: The sub_resource_type_code of this MonthlyBillRes.
        :rtype: str
        """
        return self._sub_resource_type_code

    @sub_resource_type_code.setter
    def sub_resource_type_code(self, sub_resource_type_code):
        r"""Sets the sub_resource_type_code of this MonthlyBillRes.

        整机的子云服务的自身的资源类型编码。

        :param sub_resource_type_code: The sub_resource_type_code of this MonthlyBillRes.
        :type sub_resource_type_code: str
        """
        self._sub_resource_type_code = sub_resource_type_code

    @property
    def sub_resource_type_name(self):
        r"""Gets the sub_resource_type_name of this MonthlyBillRes.

        整机的子云服务的自身的资源类型名称。

        :return: The sub_resource_type_name of this MonthlyBillRes.
        :rtype: str
        """
        return self._sub_resource_type_name

    @sub_resource_type_name.setter
    def sub_resource_type_name(self, sub_resource_type_name):
        r"""Sets the sub_resource_type_name of this MonthlyBillRes.

        整机的子云服务的自身的资源类型名称。

        :param sub_resource_type_name: The sub_resource_type_name of this MonthlyBillRes.
        :type sub_resource_type_name: str
        """
        self._sub_resource_type_name = sub_resource_type_name

    @property
    def sub_resource_id(self):
        r"""Gets the sub_resource_id of this MonthlyBillRes.

        整机的子云服务的自身的资源ID，资源标识。（如果为预留实例，则为预留实例标识）

        :return: The sub_resource_id of this MonthlyBillRes.
        :rtype: str
        """
        return self._sub_resource_id

    @sub_resource_id.setter
    def sub_resource_id(self, sub_resource_id):
        r"""Sets the sub_resource_id of this MonthlyBillRes.

        整机的子云服务的自身的资源ID，资源标识。（如果为预留实例，则为预留实例标识）

        :param sub_resource_id: The sub_resource_id of this MonthlyBillRes.
        :type sub_resource_id: str
        """
        self._sub_resource_id = sub_resource_id

    @property
    def sub_resource_name(self):
        r"""Gets the sub_resource_name of this MonthlyBillRes.

        整机的子云服务的自身的资源名称，资源标识。（如果为预留实例，则为预留实例标识）

        :return: The sub_resource_name of this MonthlyBillRes.
        :rtype: str
        """
        return self._sub_resource_name

    @sub_resource_name.setter
    def sub_resource_name(self, sub_resource_name):
        r"""Sets the sub_resource_name of this MonthlyBillRes.

        整机的子云服务的自身的资源名称，资源标识。（如果为预留实例，则为预留实例标识）

        :param sub_resource_name: The sub_resource_name of this MonthlyBillRes.
        :type sub_resource_name: str
        """
        self._sub_resource_name = sub_resource_name

    @property
    def pre_order_id(self):
        r"""Gets the pre_order_id of this MonthlyBillRes.

        原订单ID 。

        :return: The pre_order_id of this MonthlyBillRes.
        :rtype: str
        """
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, pre_order_id):
        r"""Sets the pre_order_id of this MonthlyBillRes.

        原订单ID 。

        :param pre_order_id: The pre_order_id of this MonthlyBillRes.
        :type pre_order_id: str
        """
        self._pre_order_id = pre_order_id

    @property
    def az_code_infos(self):
        r"""Gets the az_code_infos of this MonthlyBillRes.

        可用区信息列表。具体请参见表 AzCodeInfo。

        :return: The az_code_infos of this MonthlyBillRes.
        :rtype: list[:class:`huaweicloudsdkbss.v2.AzCodeInfo`]
        """
        return self._az_code_infos

    @az_code_infos.setter
    def az_code_infos(self, az_code_infos):
        r"""Sets the az_code_infos of this MonthlyBillRes.

        可用区信息列表。具体请参见表 AzCodeInfo。

        :param az_code_infos: The az_code_infos of this MonthlyBillRes.
        :type az_code_infos: list[:class:`huaweicloudsdkbss.v2.AzCodeInfo`]
        """
        self._az_code_infos = az_code_infos

    @property
    def payer_account_id(self):
        r"""Gets the payer_account_id of this MonthlyBillRes.

        |参数名称：支付账号ID。| |参数的约束及描述：如果是普通客户或者财务独立企业子客户或者企业主客户查询消费记录，此处为客户自己的客户ID。如果是财务托管企业子查询消费记录，此处为企业主客户ID或自己的客户ID。|

        :return: The payer_account_id of this MonthlyBillRes.
        :rtype: str
        """
        return self._payer_account_id

    @payer_account_id.setter
    def payer_account_id(self, payer_account_id):
        r"""Sets the payer_account_id of this MonthlyBillRes.

        |参数名称：支付账号ID。| |参数的约束及描述：如果是普通客户或者财务独立企业子客户或者企业主客户查询消费记录，此处为客户自己的客户ID。如果是财务托管企业子查询消费记录，此处为企业主客户ID或自己的客户ID。|

        :param payer_account_id: The payer_account_id of this MonthlyBillRes.
        :type payer_account_id: str
        """
        self._payer_account_id = payer_account_id

    @property
    def effective_time(self):
        r"""Gets the effective_time of this MonthlyBillRes.

        |参数名称：费用对应的资源使用的开始时间| |参数的约束及描述：费用对应的资源使用的开始时间，statistic_type=3有效，statistic_type=1或者2该字段保留。|

        :return: The effective_time of this MonthlyBillRes.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        r"""Sets the effective_time of this MonthlyBillRes.

        |参数名称：费用对应的资源使用的开始时间| |参数的约束及描述：费用对应的资源使用的开始时间，statistic_type=3有效，statistic_type=1或者2该字段保留。|

        :param effective_time: The effective_time of this MonthlyBillRes.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this MonthlyBillRes.

        |参数名称：费用对应的资源使用的结束时间| |参数的约束及描述：费用对应的资源使用的结束时间，statistic_type=3有效，statistic_type=1或者2该字段保留。|

        :return: The expire_time of this MonthlyBillRes.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this MonthlyBillRes.

        |参数名称：费用对应的资源使用的结束时间| |参数的约束及描述：费用对应的资源使用的结束时间，statistic_type=3有效，statistic_type=1或者2该字段保留。|

        :param expire_time: The expire_time of this MonthlyBillRes.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def consume_time(self):
        r"""Gets the consume_time of this MonthlyBillRes.

        |参数名称：消费时间| |参数约束及描述：消费时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ。包周期、预留实例预付为交易时间，按需、预留实例按时计费为话单生失效时间。 说明：当statistic_type=3时有效。|

        :return: The consume_time of this MonthlyBillRes.
        :rtype: str
        """
        return self._consume_time

    @consume_time.setter
    def consume_time(self, consume_time):
        r"""Sets the consume_time of this MonthlyBillRes.

        |参数名称：消费时间| |参数约束及描述：消费时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ。包周期、预留实例预付为交易时间，按需、预留实例按时计费为话单生失效时间。 说明：当statistic_type=3时有效。|

        :param consume_time: The consume_time of this MonthlyBillRes.
        :type consume_time: str
        """
        self._consume_time = consume_time

    @property
    def be_id(self):
        r"""Gets the be_id of this MonthlyBillRes.

        |参数名称：华为云运营实体ID。| |参数约束及描述：华为云运营实体ID。|

        :return: The be_id of this MonthlyBillRes.
        :rtype: str
        """
        return self._be_id

    @be_id.setter
    def be_id(self, be_id):
        r"""Sets the be_id of this MonthlyBillRes.

        |参数名称：华为云运营实体ID。| |参数约束及描述：华为云运营实体ID。|

        :param be_id: The be_id of this MonthlyBillRes.
        :type be_id: str
        """
        self._be_id = be_id

    @property
    def extend_params(self):
        r"""Gets the extend_params of this MonthlyBillRes.

        :return: The extend_params of this MonthlyBillRes.
        :rtype: :class:`huaweicloudsdkbss.v2.ResRelation`
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        r"""Sets the extend_params of this MonthlyBillRes.

        :param extend_params: The extend_params of this MonthlyBillRes.
        :type extend_params: :class:`huaweicloudsdkbss.v2.ResRelation`
        """
        self._extend_params = extend_params

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
        if not isinstance(other, MonthlyBillRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
