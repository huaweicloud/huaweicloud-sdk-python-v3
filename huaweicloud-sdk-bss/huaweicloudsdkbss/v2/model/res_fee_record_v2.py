# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'cloud_service_type_name': 'str',
        'resource_type_name': 'str',
        'effective_time': 'str',
        'expire_time': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_tag': 'str',
        'product_id': 'str',
        'product_name': 'str',
        'product_spec_desc': 'str',
        'sku_code': 'str',
        'spec_size': 'decimal.Decimal',
        'spec_size_measure_id': 'int',
        'trade_id': 'str',
        'id': 'str',
        'trade_time': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'charge_mode': 'str',
        'order_id': 'str',
        'period_type': 'str',
        'usage_type': 'str',
        'usage': 'decimal.Decimal',
        'usage_measure_id': 'int',
        'free_resource_usage': 'decimal.Decimal',
        'free_resource_measure_id': 'int',
        'ri_usage': 'decimal.Decimal',
        'ri_usage_measure_id': 'int',
        'unit_price': 'decimal.Decimal',
        'unit': 'str',
        'official_amount': 'decimal.Decimal',
        'discount_amount': 'decimal.Decimal',
        'amount': 'decimal.Decimal',
        'cash_amount': 'decimal.Decimal',
        'credit_amount': 'decimal.Decimal',
        'coupon_amount': 'decimal.Decimal',
        'flexipurchase_coupon_amount': 'decimal.Decimal',
        'stored_card_amount': 'decimal.Decimal',
        'bonus_amount': 'decimal.Decimal',
        'debt_amount': 'decimal.Decimal',
        'adjustment_amount': 'decimal.Decimal',
        'measure_id': 'int',
        'formula': 'str',
        'sub_service_type_code': 'str',
        'sub_service_type_name': 'str',
        'sub_resource_type_code': 'str',
        'sub_resource_type_name': 'str',
        'sub_resource_id': 'str',
        'sub_resource_name': 'str',
        'consume_time': 'str',
        'relative_order_id': 'str'
    }

    attribute_map = {
        'bill_date': 'bill_date',
        'bill_type': 'bill_type',
        'customer_id': 'customer_id',
        'region': 'region',
        'region_name': 'region_name',
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'cloud_service_type_name': 'cloud_service_type_name',
        'resource_type_name': 'resource_type_name',
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
        'id': 'id',
        'trade_time': 'trade_time',
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
        'measure_id': 'measure_id',
        'formula': 'formula',
        'sub_service_type_code': 'sub_service_type_code',
        'sub_service_type_name': 'sub_service_type_name',
        'sub_resource_type_code': 'sub_resource_type_code',
        'sub_resource_type_name': 'sub_resource_type_name',
        'sub_resource_id': 'sub_resource_id',
        'sub_resource_name': 'sub_resource_name',
        'consume_time': 'consume_time',
        'relative_order_id': 'relative_order_id'
    }

    def __init__(self, bill_date=None, bill_type=None, customer_id=None, region=None, region_name=None, cloud_service_type=None, resource_type=None, cloud_service_type_name=None, resource_type_name=None, effective_time=None, expire_time=None, resource_id=None, resource_name=None, resource_tag=None, product_id=None, product_name=None, product_spec_desc=None, sku_code=None, spec_size=None, spec_size_measure_id=None, trade_id=None, id=None, trade_time=None, enterprise_project_id=None, enterprise_project_name=None, charge_mode=None, order_id=None, period_type=None, usage_type=None, usage=None, usage_measure_id=None, free_resource_usage=None, free_resource_measure_id=None, ri_usage=None, ri_usage_measure_id=None, unit_price=None, unit=None, official_amount=None, discount_amount=None, amount=None, cash_amount=None, credit_amount=None, coupon_amount=None, flexipurchase_coupon_amount=None, stored_card_amount=None, bonus_amount=None, debt_amount=None, adjustment_amount=None, measure_id=None, formula=None, sub_service_type_code=None, sub_service_type_name=None, sub_resource_type_code=None, sub_resource_type_name=None, sub_resource_id=None, sub_resource_name=None, consume_time=None, relative_order_id=None):
        r"""ResFeeRecordV2

        The model defined in huaweicloud sdk

        :param bill_date: 资源消费记录的日期。 格式：YYYY-MM-DD。按照东八区时间截取。
        :type bill_date: str
        :param bill_type: 账单类型。1：消费-新购 2：消费-续订 3：消费-变更 4：退款-退订 5：消费-使用 8：消费-自动续订 9：调账-补偿 14：消费-服务支持计划月末扣费 16：调账-扣费 18：消费-按月付费 20：退款-变更 23：消费-节省计划抵扣 24：退款-包年/包月转按需 25：消费-抹零补扣 103：消费-按年付费
        :type bill_type: int
        :param customer_id: 消费的客户账号ID。 如果是普通客户或者企业子查询消费记录，只能查询到自身的消费记录，则这个地方显示的是自身的客户ID如果是企业主查询消费记录，可以查询到自身以及企业子的消费记录，这个地方是消费的实际客户ID，如果是企业主自身消费，为企业主ID，如果这条消费记录是某个企业子客户的消费，这个地方的ID是企业子账号ID。
        :type customer_id: str
        :param region: 云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。
        :type region: str
        :param region_name: 云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。
        :type region_name: str
        :param cloud_service_type: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。
        :type cloud_service_type: str
        :param resource_type: 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。
        :type resource_type: str
        :param cloud_service_type_name: 云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。
        :type cloud_service_type_name: str
        :param resource_type_name: 资源类型名称。例如ECS的资源类型名称为“云主机”。
        :type resource_type_name: str
        :param effective_time: 费用对应的资源使用的开始时间，按需有效，包年/包月该字段保留。
        :type effective_time: str
        :param expire_time: 费用对应的资源使用的结束时间，按需有效，包年/包月该字段保留。
        :type expire_time: str
        :param resource_id: 资源ID。
        :type resource_id: str
        :param resource_name: 资源名称。
        :type resource_name: str
        :param resource_tag: 资源标签。
        :type resource_tag: str
        :param product_id: 产品ID。
        :type product_id: str
        :param product_name: 产品名称。
        :type product_name: str
        :param product_spec_desc: 产品的规格描述。
        :type product_spec_desc: str
        :param sku_code: SKU编码，在账单中唯一标识一个资源的规格。
        :type sku_code: str
        :param spec_size: 产品的实例大小，仅线性产品有效。  说明： 线性产品是指订购时需要指定大小的产品。例如硬盘在订购时需选择10G、20G等不同大小规格。
        :type spec_size: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param spec_size_measure_id: 产品实例大小的单位，仅线性产品有该字段。 您可以调用查询度量单位列表接口获取。
        :type spec_size_measure_id: int
        :param trade_id: 订单ID或交易ID，扣费维度的唯一标识。
        :type trade_id: str
        :param id: 唯一标识。 按账期类型统计时不返回唯一标识。
        :type id: str
        :param trade_time: 交易时间。
        :type trade_time: str
        :param enterprise_project_id: 企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目的名称。
        :type enterprise_project_name: str
        :param charge_mode: 计费模式。 1：包年/包月3：按需10：预留实例11：节省计划
        :type charge_mode: str
        :param order_id: 订单ID。  说明： 包年/包月资源的使用记录才有该字段，按需资源则为空。
        :type order_id: str
        :param period_type: 周期类型： 19：年20：月24：天25：小时5：一次性
        :type period_type: str
        :param usage_type: 资源使用量的类型，您可以调用查询使用量类型列表接口获取。
        :type usage_type: str
        :param usage: 资源的使用量。  说明： 查询包周期资源，不返回资源的使用量。
        :type usage: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param usage_measure_id: 资源使用量的度量单位，您可以调用查询度量单位列表接口获取。  说明： 查询包周期资源，不返回资源使用量的度量单位。
        :type usage_measure_id: int
        :param free_resource_usage: 套餐内使用量。
        :type free_resource_usage: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param free_resource_measure_id: 套餐内使用量的度量单位，您可以调用查询度量单位列表接口获取。
        :type free_resource_measure_id: int
        :param ri_usage: 预留实例使用量。
        :type ri_usage: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param ri_usage_measure_id: 预留实例使用量单位。
        :type ri_usage_measure_id: int
        :param unit_price: 产品的单价。 按需产品的单价，只有简单定价，不分档的场景会返回。 包周期产品的单价，只有包周期的如下场景会返回：包周期订购/续订/降配/升配/扩容简单定价，不分档 预留实例的单价，只有如下场景下会返回：订购/续订/降配/升配/扩容/按时计费简单定价，不分档  说明： 当statistic_type入参为1，按账期，查询包周期产品时，不返回单价。
        :type unit_price: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param unit: 产品的单价单位。 线性产品的单价单位为“元/{线性单位}/月”或“元/{线性单位}/小时”等。非线性产品的单价单位为“元/月”或“元/小时”等。  说明： “线性单位”为线性产品（即订购时需要指定大小的产品）的大小的单位，比如硬盘的线性单位为GB，带宽的线性单位为Mbps。当statistic_type入参为1，按账期，查询包周期产品时，不返回单价单位。
        :type unit: str
        :param official_amount: 官网价，华为云商品在官网上未叠加应用商务折扣、促销折扣等优惠的销售价格。
        :type official_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param discount_amount: 优惠金额，用户使用云服务享受折扣优惠如商务折扣、伙伴授予折扣以及促销优惠等减免的金额。
        :type discount_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param amount: 应付金额，用户使用云服务享受折扣优惠后需要支付的费用金额，包括现金券和储值卡和代金券金额，精确到小数点后2位。  说明： amount的值等于cash_amount，credit_amount，coupon_amount，flexipurchase_coupon_amount，stored_card_amount，bonus_amount，debt_amount，adjustment_amount的总和。
        :type amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
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
        :param measure_id: 金额单位。 1：元
        :type measure_id: int
        :param formula: 实付金额计算公式。当前只包含如下场景： 按需非线性定价{使用量}【使用量】/{单位转化率}【单位转换】*{单价}【单价】-{优惠金额}【优惠金额】-{抹零金额}【抹零金额】-{代金券抵扣}【代金券抵扣】 按需线性定价{使用量}【使用量】/{单位转化率}【单位转换】*{线性大小}【规格】*{单价}【单价】-{优惠金额}【优惠金额】-{抹零金额}【抹零金额】-{代金券抵扣}【代金券抵扣】 包年包月新购和续订非线性定价{周期数}【周期数】/{周期转化率}【周期转换】*{单价}【单价】-{优惠金额}【优惠金额】-{代金券抵扣}【代金券抵扣】 包年包月新购和续订线性定价{周期数}【周期数】/{周期转化率}【周期转换】*{线性大小}【规格】*{单价}【单价】-{优惠金额}【优惠金额】-{代金券抵扣}【代金券抵扣】 包年包月（一次性）新购和续订非线性定价{单价}【单价】-{优惠金额}【优惠金额】-{代金券抵扣}【代金券抵扣】 包年包月（一次性）新购和续订线性定价{线性大小}【规格】*{单价}【单价】-{优惠金额}【优惠金额】-{代金券抵扣}【代金券抵扣】  说明： 实付金额计算公式得到的金额值等于amount - coupon_amount的差值。按账期类型查询时不返回计算公式。
        :type formula: str
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
        :param consume_time: |参数名称：消费时间| |参数约束及描述：消费时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ。包周期、预留实例预付为交易时间，按需、预留实例按时计费为话单生失效时间。 说明：当statistic_type&#x3D;3时有效。|
        :type consume_time: str
        :param relative_order_id: |参数名称：客户订单关联的订单ID| |参数约束及描述：客户订单关联的订单ID，包年/包月资源的使用记录该字段才有值，按需资源则为空。当order_id为组合交易订单时，该字段才有值，当查询为普通订单时，此字段返回为空。|
        :type relative_order_id: str
        """
        
        

        self._bill_date = None
        self._bill_type = None
        self._customer_id = None
        self._region = None
        self._region_name = None
        self._cloud_service_type = None
        self._resource_type = None
        self._cloud_service_type_name = None
        self._resource_type_name = None
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
        self._id = None
        self._trade_time = None
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
        self._formula = None
        self._sub_service_type_code = None
        self._sub_service_type_name = None
        self._sub_resource_type_code = None
        self._sub_resource_type_name = None
        self._sub_resource_id = None
        self._sub_resource_name = None
        self._consume_time = None
        self._relative_order_id = None
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
        if cloud_service_type_name is not None:
            self.cloud_service_type_name = cloud_service_type_name
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
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
        if id is not None:
            self.id = id
        if trade_time is not None:
            self.trade_time = trade_time
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
        if formula is not None:
            self.formula = formula
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
        if consume_time is not None:
            self.consume_time = consume_time
        if relative_order_id is not None:
            self.relative_order_id = relative_order_id

    @property
    def bill_date(self):
        r"""Gets the bill_date of this ResFeeRecordV2.

        资源消费记录的日期。 格式：YYYY-MM-DD。按照东八区时间截取。

        :return: The bill_date of this ResFeeRecordV2.
        :rtype: str
        """
        return self._bill_date

    @bill_date.setter
    def bill_date(self, bill_date):
        r"""Sets the bill_date of this ResFeeRecordV2.

        资源消费记录的日期。 格式：YYYY-MM-DD。按照东八区时间截取。

        :param bill_date: The bill_date of this ResFeeRecordV2.
        :type bill_date: str
        """
        self._bill_date = bill_date

    @property
    def bill_type(self):
        r"""Gets the bill_type of this ResFeeRecordV2.

        账单类型。1：消费-新购 2：消费-续订 3：消费-变更 4：退款-退订 5：消费-使用 8：消费-自动续订 9：调账-补偿 14：消费-服务支持计划月末扣费 16：调账-扣费 18：消费-按月付费 20：退款-变更 23：消费-节省计划抵扣 24：退款-包年/包月转按需 25：消费-抹零补扣 103：消费-按年付费

        :return: The bill_type of this ResFeeRecordV2.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        r"""Sets the bill_type of this ResFeeRecordV2.

        账单类型。1：消费-新购 2：消费-续订 3：消费-变更 4：退款-退订 5：消费-使用 8：消费-自动续订 9：调账-补偿 14：消费-服务支持计划月末扣费 16：调账-扣费 18：消费-按月付费 20：退款-变更 23：消费-节省计划抵扣 24：退款-包年/包月转按需 25：消费-抹零补扣 103：消费-按年付费

        :param bill_type: The bill_type of this ResFeeRecordV2.
        :type bill_type: int
        """
        self._bill_type = bill_type

    @property
    def customer_id(self):
        r"""Gets the customer_id of this ResFeeRecordV2.

        消费的客户账号ID。 如果是普通客户或者企业子查询消费记录，只能查询到自身的消费记录，则这个地方显示的是自身的客户ID如果是企业主查询消费记录，可以查询到自身以及企业子的消费记录，这个地方是消费的实际客户ID，如果是企业主自身消费，为企业主ID，如果这条消费记录是某个企业子客户的消费，这个地方的ID是企业子账号ID。

        :return: The customer_id of this ResFeeRecordV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this ResFeeRecordV2.

        消费的客户账号ID。 如果是普通客户或者企业子查询消费记录，只能查询到自身的消费记录，则这个地方显示的是自身的客户ID如果是企业主查询消费记录，可以查询到自身以及企业子的消费记录，这个地方是消费的实际客户ID，如果是企业主自身消费，为企业主ID，如果这条消费记录是某个企业子客户的消费，这个地方的ID是企业子账号ID。

        :param customer_id: The customer_id of this ResFeeRecordV2.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def region(self):
        r"""Gets the region of this ResFeeRecordV2.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :return: The region of this ResFeeRecordV2.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ResFeeRecordV2.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。

        :param region: The region of this ResFeeRecordV2.
        :type region: str
        """
        self._region = region

    @property
    def region_name(self):
        r"""Gets the region_name of this ResFeeRecordV2.

        云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。

        :return: The region_name of this ResFeeRecordV2.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this ResFeeRecordV2.

        云服务区名称，例如：“华北-北京一”。具体请参见地区和终端节点对应云服务的“区域名称”列的值。

        :param region_name: The region_name of this ResFeeRecordV2.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this ResFeeRecordV2.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :return: The cloud_service_type of this ResFeeRecordV2.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this ResFeeRecordV2.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :param cloud_service_type: The cloud_service_type of this ResFeeRecordV2.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ResFeeRecordV2.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :return: The resource_type of this ResFeeRecordV2.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ResFeeRecordV2.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。您可以调用查询资源类型列表接口获取。

        :param resource_type: The resource_type of this ResFeeRecordV2.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def cloud_service_type_name(self):
        r"""Gets the cloud_service_type_name of this ResFeeRecordV2.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :return: The cloud_service_type_name of this ResFeeRecordV2.
        :rtype: str
        """
        return self._cloud_service_type_name

    @cloud_service_type_name.setter
    def cloud_service_type_name(self, cloud_service_type_name):
        r"""Sets the cloud_service_type_name of this ResFeeRecordV2.

        云服务类型名称。例如ECS的云服务类型名称为“弹性云服务器”。

        :param cloud_service_type_name: The cloud_service_type_name of this ResFeeRecordV2.
        :type cloud_service_type_name: str
        """
        self._cloud_service_type_name = cloud_service_type_name

    @property
    def resource_type_name(self):
        r"""Gets the resource_type_name of this ResFeeRecordV2.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :return: The resource_type_name of this ResFeeRecordV2.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        r"""Sets the resource_type_name of this ResFeeRecordV2.

        资源类型名称。例如ECS的资源类型名称为“云主机”。

        :param resource_type_name: The resource_type_name of this ResFeeRecordV2.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def effective_time(self):
        r"""Gets the effective_time of this ResFeeRecordV2.

        费用对应的资源使用的开始时间，按需有效，包年/包月该字段保留。

        :return: The effective_time of this ResFeeRecordV2.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        r"""Sets the effective_time of this ResFeeRecordV2.

        费用对应的资源使用的开始时间，按需有效，包年/包月该字段保留。

        :param effective_time: The effective_time of this ResFeeRecordV2.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ResFeeRecordV2.

        费用对应的资源使用的结束时间，按需有效，包年/包月该字段保留。

        :return: The expire_time of this ResFeeRecordV2.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ResFeeRecordV2.

        费用对应的资源使用的结束时间，按需有效，包年/包月该字段保留。

        :param expire_time: The expire_time of this ResFeeRecordV2.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ResFeeRecordV2.

        资源ID。

        :return: The resource_id of this ResFeeRecordV2.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ResFeeRecordV2.

        资源ID。

        :param resource_id: The resource_id of this ResFeeRecordV2.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ResFeeRecordV2.

        资源名称。

        :return: The resource_name of this ResFeeRecordV2.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ResFeeRecordV2.

        资源名称。

        :param resource_name: The resource_name of this ResFeeRecordV2.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_tag(self):
        r"""Gets the resource_tag of this ResFeeRecordV2.

        资源标签。

        :return: The resource_tag of this ResFeeRecordV2.
        :rtype: str
        """
        return self._resource_tag

    @resource_tag.setter
    def resource_tag(self, resource_tag):
        r"""Sets the resource_tag of this ResFeeRecordV2.

        资源标签。

        :param resource_tag: The resource_tag of this ResFeeRecordV2.
        :type resource_tag: str
        """
        self._resource_tag = resource_tag

    @property
    def product_id(self):
        r"""Gets the product_id of this ResFeeRecordV2.

        产品ID。

        :return: The product_id of this ResFeeRecordV2.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ResFeeRecordV2.

        产品ID。

        :param product_id: The product_id of this ResFeeRecordV2.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_name(self):
        r"""Gets the product_name of this ResFeeRecordV2.

        产品名称。

        :return: The product_name of this ResFeeRecordV2.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this ResFeeRecordV2.

        产品名称。

        :param product_name: The product_name of this ResFeeRecordV2.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def product_spec_desc(self):
        r"""Gets the product_spec_desc of this ResFeeRecordV2.

        产品的规格描述。

        :return: The product_spec_desc of this ResFeeRecordV2.
        :rtype: str
        """
        return self._product_spec_desc

    @product_spec_desc.setter
    def product_spec_desc(self, product_spec_desc):
        r"""Sets the product_spec_desc of this ResFeeRecordV2.

        产品的规格描述。

        :param product_spec_desc: The product_spec_desc of this ResFeeRecordV2.
        :type product_spec_desc: str
        """
        self._product_spec_desc = product_spec_desc

    @property
    def sku_code(self):
        r"""Gets the sku_code of this ResFeeRecordV2.

        SKU编码，在账单中唯一标识一个资源的规格。

        :return: The sku_code of this ResFeeRecordV2.
        :rtype: str
        """
        return self._sku_code

    @sku_code.setter
    def sku_code(self, sku_code):
        r"""Sets the sku_code of this ResFeeRecordV2.

        SKU编码，在账单中唯一标识一个资源的规格。

        :param sku_code: The sku_code of this ResFeeRecordV2.
        :type sku_code: str
        """
        self._sku_code = sku_code

    @property
    def spec_size(self):
        r"""Gets the spec_size of this ResFeeRecordV2.

        产品的实例大小，仅线性产品有效。  说明： 线性产品是指订购时需要指定大小的产品。例如硬盘在订购时需选择10G、20G等不同大小规格。

        :return: The spec_size of this ResFeeRecordV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._spec_size

    @spec_size.setter
    def spec_size(self, spec_size):
        r"""Sets the spec_size of this ResFeeRecordV2.

        产品的实例大小，仅线性产品有效。  说明： 线性产品是指订购时需要指定大小的产品。例如硬盘在订购时需选择10G、20G等不同大小规格。

        :param spec_size: The spec_size of this ResFeeRecordV2.
        :type spec_size: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._spec_size = spec_size

    @property
    def spec_size_measure_id(self):
        r"""Gets the spec_size_measure_id of this ResFeeRecordV2.

        产品实例大小的单位，仅线性产品有该字段。 您可以调用查询度量单位列表接口获取。

        :return: The spec_size_measure_id of this ResFeeRecordV2.
        :rtype: int
        """
        return self._spec_size_measure_id

    @spec_size_measure_id.setter
    def spec_size_measure_id(self, spec_size_measure_id):
        r"""Sets the spec_size_measure_id of this ResFeeRecordV2.

        产品实例大小的单位，仅线性产品有该字段。 您可以调用查询度量单位列表接口获取。

        :param spec_size_measure_id: The spec_size_measure_id of this ResFeeRecordV2.
        :type spec_size_measure_id: int
        """
        self._spec_size_measure_id = spec_size_measure_id

    @property
    def trade_id(self):
        r"""Gets the trade_id of this ResFeeRecordV2.

        订单ID或交易ID，扣费维度的唯一标识。

        :return: The trade_id of this ResFeeRecordV2.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        r"""Sets the trade_id of this ResFeeRecordV2.

        订单ID或交易ID，扣费维度的唯一标识。

        :param trade_id: The trade_id of this ResFeeRecordV2.
        :type trade_id: str
        """
        self._trade_id = trade_id

    @property
    def id(self):
        r"""Gets the id of this ResFeeRecordV2.

        唯一标识。 按账期类型统计时不返回唯一标识。

        :return: The id of this ResFeeRecordV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResFeeRecordV2.

        唯一标识。 按账期类型统计时不返回唯一标识。

        :param id: The id of this ResFeeRecordV2.
        :type id: str
        """
        self._id = id

    @property
    def trade_time(self):
        r"""Gets the trade_time of this ResFeeRecordV2.

        交易时间。

        :return: The trade_time of this ResFeeRecordV2.
        :rtype: str
        """
        return self._trade_time

    @trade_time.setter
    def trade_time(self, trade_time):
        r"""Sets the trade_time of this ResFeeRecordV2.

        交易时间。

        :param trade_time: The trade_time of this ResFeeRecordV2.
        :type trade_time: str
        """
        self._trade_time = trade_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ResFeeRecordV2.

        企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :return: The enterprise_project_id of this ResFeeRecordV2.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ResFeeRecordV2.

        企业项目标识（企业项目ID）。 default项目对应ID：0未归集（表示该云服务不支持企业项目管理能力）项目对应ID：null其余项目对应ID获取方法请参见[如何获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :param enterprise_project_id: The enterprise_project_id of this ResFeeRecordV2.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this ResFeeRecordV2.

        企业项目的名称。

        :return: The enterprise_project_name of this ResFeeRecordV2.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this ResFeeRecordV2.

        企业项目的名称。

        :param enterprise_project_name: The enterprise_project_name of this ResFeeRecordV2.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this ResFeeRecordV2.

        计费模式。 1：包年/包月3：按需10：预留实例11：节省计划

        :return: The charge_mode of this ResFeeRecordV2.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this ResFeeRecordV2.

        计费模式。 1：包年/包月3：按需10：预留实例11：节省计划

        :param charge_mode: The charge_mode of this ResFeeRecordV2.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def order_id(self):
        r"""Gets the order_id of this ResFeeRecordV2.

        订单ID。  说明： 包年/包月资源的使用记录才有该字段，按需资源则为空。

        :return: The order_id of this ResFeeRecordV2.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ResFeeRecordV2.

        订单ID。  说明： 包年/包月资源的使用记录才有该字段，按需资源则为空。

        :param order_id: The order_id of this ResFeeRecordV2.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def period_type(self):
        r"""Gets the period_type of this ResFeeRecordV2.

        周期类型： 19：年20：月24：天25：小时5：一次性

        :return: The period_type of this ResFeeRecordV2.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this ResFeeRecordV2.

        周期类型： 19：年20：月24：天25：小时5：一次性

        :param period_type: The period_type of this ResFeeRecordV2.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def usage_type(self):
        r"""Gets the usage_type of this ResFeeRecordV2.

        资源使用量的类型，您可以调用查询使用量类型列表接口获取。

        :return: The usage_type of this ResFeeRecordV2.
        :rtype: str
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        r"""Sets the usage_type of this ResFeeRecordV2.

        资源使用量的类型，您可以调用查询使用量类型列表接口获取。

        :param usage_type: The usage_type of this ResFeeRecordV2.
        :type usage_type: str
        """
        self._usage_type = usage_type

    @property
    def usage(self):
        r"""Gets the usage of this ResFeeRecordV2.

        资源的使用量。  说明： 查询包周期资源，不返回资源的使用量。

        :return: The usage of this ResFeeRecordV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        r"""Sets the usage of this ResFeeRecordV2.

        资源的使用量。  说明： 查询包周期资源，不返回资源的使用量。

        :param usage: The usage of this ResFeeRecordV2.
        :type usage: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._usage = usage

    @property
    def usage_measure_id(self):
        r"""Gets the usage_measure_id of this ResFeeRecordV2.

        资源使用量的度量单位，您可以调用查询度量单位列表接口获取。  说明： 查询包周期资源，不返回资源使用量的度量单位。

        :return: The usage_measure_id of this ResFeeRecordV2.
        :rtype: int
        """
        return self._usage_measure_id

    @usage_measure_id.setter
    def usage_measure_id(self, usage_measure_id):
        r"""Sets the usage_measure_id of this ResFeeRecordV2.

        资源使用量的度量单位，您可以调用查询度量单位列表接口获取。  说明： 查询包周期资源，不返回资源使用量的度量单位。

        :param usage_measure_id: The usage_measure_id of this ResFeeRecordV2.
        :type usage_measure_id: int
        """
        self._usage_measure_id = usage_measure_id

    @property
    def free_resource_usage(self):
        r"""Gets the free_resource_usage of this ResFeeRecordV2.

        套餐内使用量。

        :return: The free_resource_usage of this ResFeeRecordV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._free_resource_usage

    @free_resource_usage.setter
    def free_resource_usage(self, free_resource_usage):
        r"""Sets the free_resource_usage of this ResFeeRecordV2.

        套餐内使用量。

        :param free_resource_usage: The free_resource_usage of this ResFeeRecordV2.
        :type free_resource_usage: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._free_resource_usage = free_resource_usage

    @property
    def free_resource_measure_id(self):
        r"""Gets the free_resource_measure_id of this ResFeeRecordV2.

        套餐内使用量的度量单位，您可以调用查询度量单位列表接口获取。

        :return: The free_resource_measure_id of this ResFeeRecordV2.
        :rtype: int
        """
        return self._free_resource_measure_id

    @free_resource_measure_id.setter
    def free_resource_measure_id(self, free_resource_measure_id):
        r"""Sets the free_resource_measure_id of this ResFeeRecordV2.

        套餐内使用量的度量单位，您可以调用查询度量单位列表接口获取。

        :param free_resource_measure_id: The free_resource_measure_id of this ResFeeRecordV2.
        :type free_resource_measure_id: int
        """
        self._free_resource_measure_id = free_resource_measure_id

    @property
    def ri_usage(self):
        r"""Gets the ri_usage of this ResFeeRecordV2.

        预留实例使用量。

        :return: The ri_usage of this ResFeeRecordV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._ri_usage

    @ri_usage.setter
    def ri_usage(self, ri_usage):
        r"""Sets the ri_usage of this ResFeeRecordV2.

        预留实例使用量。

        :param ri_usage: The ri_usage of this ResFeeRecordV2.
        :type ri_usage: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._ri_usage = ri_usage

    @property
    def ri_usage_measure_id(self):
        r"""Gets the ri_usage_measure_id of this ResFeeRecordV2.

        预留实例使用量单位。

        :return: The ri_usage_measure_id of this ResFeeRecordV2.
        :rtype: int
        """
        return self._ri_usage_measure_id

    @ri_usage_measure_id.setter
    def ri_usage_measure_id(self, ri_usage_measure_id):
        r"""Sets the ri_usage_measure_id of this ResFeeRecordV2.

        预留实例使用量单位。

        :param ri_usage_measure_id: The ri_usage_measure_id of this ResFeeRecordV2.
        :type ri_usage_measure_id: int
        """
        self._ri_usage_measure_id = ri_usage_measure_id

    @property
    def unit_price(self):
        r"""Gets the unit_price of this ResFeeRecordV2.

        产品的单价。 按需产品的单价，只有简单定价，不分档的场景会返回。 包周期产品的单价，只有包周期的如下场景会返回：包周期订购/续订/降配/升配/扩容简单定价，不分档 预留实例的单价，只有如下场景下会返回：订购/续订/降配/升配/扩容/按时计费简单定价，不分档  说明： 当statistic_type入参为1，按账期，查询包周期产品时，不返回单价。

        :return: The unit_price of this ResFeeRecordV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        r"""Sets the unit_price of this ResFeeRecordV2.

        产品的单价。 按需产品的单价，只有简单定价，不分档的场景会返回。 包周期产品的单价，只有包周期的如下场景会返回：包周期订购/续订/降配/升配/扩容简单定价，不分档 预留实例的单价，只有如下场景下会返回：订购/续订/降配/升配/扩容/按时计费简单定价，不分档  说明： 当statistic_type入参为1，按账期，查询包周期产品时，不返回单价。

        :param unit_price: The unit_price of this ResFeeRecordV2.
        :type unit_price: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._unit_price = unit_price

    @property
    def unit(self):
        r"""Gets the unit of this ResFeeRecordV2.

        产品的单价单位。 线性产品的单价单位为“元/{线性单位}/月”或“元/{线性单位}/小时”等。非线性产品的单价单位为“元/月”或“元/小时”等。  说明： “线性单位”为线性产品（即订购时需要指定大小的产品）的大小的单位，比如硬盘的线性单位为GB，带宽的线性单位为Mbps。当statistic_type入参为1，按账期，查询包周期产品时，不返回单价单位。

        :return: The unit of this ResFeeRecordV2.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ResFeeRecordV2.

        产品的单价单位。 线性产品的单价单位为“元/{线性单位}/月”或“元/{线性单位}/小时”等。非线性产品的单价单位为“元/月”或“元/小时”等。  说明： “线性单位”为线性产品（即订购时需要指定大小的产品）的大小的单位，比如硬盘的线性单位为GB，带宽的线性单位为Mbps。当statistic_type入参为1，按账期，查询包周期产品时，不返回单价单位。

        :param unit: The unit of this ResFeeRecordV2.
        :type unit: str
        """
        self._unit = unit

    @property
    def official_amount(self):
        r"""Gets the official_amount of this ResFeeRecordV2.

        官网价，华为云商品在官网上未叠加应用商务折扣、促销折扣等优惠的销售价格。

        :return: The official_amount of this ResFeeRecordV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._official_amount

    @official_amount.setter
    def official_amount(self, official_amount):
        r"""Sets the official_amount of this ResFeeRecordV2.

        官网价，华为云商品在官网上未叠加应用商务折扣、促销折扣等优惠的销售价格。

        :param official_amount: The official_amount of this ResFeeRecordV2.
        :type official_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._official_amount = official_amount

    @property
    def discount_amount(self):
        r"""Gets the discount_amount of this ResFeeRecordV2.

        优惠金额，用户使用云服务享受折扣优惠如商务折扣、伙伴授予折扣以及促销优惠等减免的金额。

        :return: The discount_amount of this ResFeeRecordV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        r"""Sets the discount_amount of this ResFeeRecordV2.

        优惠金额，用户使用云服务享受折扣优惠如商务折扣、伙伴授予折扣以及促销优惠等减免的金额。

        :param discount_amount: The discount_amount of this ResFeeRecordV2.
        :type discount_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._discount_amount = discount_amount

    @property
    def amount(self):
        r"""Gets the amount of this ResFeeRecordV2.

        应付金额，用户使用云服务享受折扣优惠后需要支付的费用金额，包括现金券和储值卡和代金券金额，精确到小数点后2位。  说明： amount的值等于cash_amount，credit_amount，coupon_amount，flexipurchase_coupon_amount，stored_card_amount，bonus_amount，debt_amount，adjustment_amount的总和。

        :return: The amount of this ResFeeRecordV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this ResFeeRecordV2.

        应付金额，用户使用云服务享受折扣优惠后需要支付的费用金额，包括现金券和储值卡和代金券金额，精确到小数点后2位。  说明： amount的值等于cash_amount，credit_amount，coupon_amount，flexipurchase_coupon_amount，stored_card_amount，bonus_amount，debt_amount，adjustment_amount的总和。

        :param amount: The amount of this ResFeeRecordV2.
        :type amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._amount = amount

    @property
    def cash_amount(self):
        r"""Gets the cash_amount of this ResFeeRecordV2.

        现金支付金额。

        :return: The cash_amount of this ResFeeRecordV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._cash_amount

    @cash_amount.setter
    def cash_amount(self, cash_amount):
        r"""Sets the cash_amount of this ResFeeRecordV2.

        现金支付金额。

        :param cash_amount: The cash_amount of this ResFeeRecordV2.
        :type cash_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._cash_amount = cash_amount

    @property
    def credit_amount(self):
        r"""Gets the credit_amount of this ResFeeRecordV2.

        信用额度支付金额。

        :return: The credit_amount of this ResFeeRecordV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        r"""Sets the credit_amount of this ResFeeRecordV2.

        信用额度支付金额。

        :param credit_amount: The credit_amount of this ResFeeRecordV2.
        :type credit_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._credit_amount = credit_amount

    @property
    def coupon_amount(self):
        r"""Gets the coupon_amount of this ResFeeRecordV2.

        代金券支付金额。

        :return: The coupon_amount of this ResFeeRecordV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        r"""Sets the coupon_amount of this ResFeeRecordV2.

        代金券支付金额。

        :param coupon_amount: The coupon_amount of this ResFeeRecordV2.
        :type coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._coupon_amount = coupon_amount

    @property
    def flexipurchase_coupon_amount(self):
        r"""Gets the flexipurchase_coupon_amount of this ResFeeRecordV2.

        现金券支付金额。

        :return: The flexipurchase_coupon_amount of this ResFeeRecordV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._flexipurchase_coupon_amount

    @flexipurchase_coupon_amount.setter
    def flexipurchase_coupon_amount(self, flexipurchase_coupon_amount):
        r"""Sets the flexipurchase_coupon_amount of this ResFeeRecordV2.

        现金券支付金额。

        :param flexipurchase_coupon_amount: The flexipurchase_coupon_amount of this ResFeeRecordV2.
        :type flexipurchase_coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._flexipurchase_coupon_amount = flexipurchase_coupon_amount

    @property
    def stored_card_amount(self):
        r"""Gets the stored_card_amount of this ResFeeRecordV2.

        储值卡支付金额。

        :return: The stored_card_amount of this ResFeeRecordV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._stored_card_amount

    @stored_card_amount.setter
    def stored_card_amount(self, stored_card_amount):
        r"""Sets the stored_card_amount of this ResFeeRecordV2.

        储值卡支付金额。

        :param stored_card_amount: The stored_card_amount of this ResFeeRecordV2.
        :type stored_card_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._stored_card_amount = stored_card_amount

    @property
    def bonus_amount(self):
        r"""Gets the bonus_amount of this ResFeeRecordV2.

        奖励金支付金额（用于现网客户未使用完的奖励金）。

        :return: The bonus_amount of this ResFeeRecordV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._bonus_amount

    @bonus_amount.setter
    def bonus_amount(self, bonus_amount):
        r"""Sets the bonus_amount of this ResFeeRecordV2.

        奖励金支付金额（用于现网客户未使用完的奖励金）。

        :param bonus_amount: The bonus_amount of this ResFeeRecordV2.
        :type bonus_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._bonus_amount = bonus_amount

    @property
    def debt_amount(self):
        r"""Gets the debt_amount of this ResFeeRecordV2.

        欠费金额。

        :return: The debt_amount of this ResFeeRecordV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        r"""Sets the debt_amount of this ResFeeRecordV2.

        欠费金额。

        :param debt_amount: The debt_amount of this ResFeeRecordV2.
        :type debt_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._debt_amount = debt_amount

    @property
    def adjustment_amount(self):
        r"""Gets the adjustment_amount of this ResFeeRecordV2.

        欠费核销金额。

        :return: The adjustment_amount of this ResFeeRecordV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._adjustment_amount

    @adjustment_amount.setter
    def adjustment_amount(self, adjustment_amount):
        r"""Sets the adjustment_amount of this ResFeeRecordV2.

        欠费核销金额。

        :param adjustment_amount: The adjustment_amount of this ResFeeRecordV2.
        :type adjustment_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._adjustment_amount = adjustment_amount

    @property
    def measure_id(self):
        r"""Gets the measure_id of this ResFeeRecordV2.

        金额单位。 1：元

        :return: The measure_id of this ResFeeRecordV2.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this ResFeeRecordV2.

        金额单位。 1：元

        :param measure_id: The measure_id of this ResFeeRecordV2.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def formula(self):
        r"""Gets the formula of this ResFeeRecordV2.

        实付金额计算公式。当前只包含如下场景： 按需非线性定价{使用量}【使用量】/{单位转化率}【单位转换】*{单价}【单价】-{优惠金额}【优惠金额】-{抹零金额}【抹零金额】-{代金券抵扣}【代金券抵扣】 按需线性定价{使用量}【使用量】/{单位转化率}【单位转换】*{线性大小}【规格】*{单价}【单价】-{优惠金额}【优惠金额】-{抹零金额}【抹零金额】-{代金券抵扣}【代金券抵扣】 包年包月新购和续订非线性定价{周期数}【周期数】/{周期转化率}【周期转换】*{单价}【单价】-{优惠金额}【优惠金额】-{代金券抵扣}【代金券抵扣】 包年包月新购和续订线性定价{周期数}【周期数】/{周期转化率}【周期转换】*{线性大小}【规格】*{单价}【单价】-{优惠金额}【优惠金额】-{代金券抵扣}【代金券抵扣】 包年包月（一次性）新购和续订非线性定价{单价}【单价】-{优惠金额}【优惠金额】-{代金券抵扣}【代金券抵扣】 包年包月（一次性）新购和续订线性定价{线性大小}【规格】*{单价}【单价】-{优惠金额}【优惠金额】-{代金券抵扣}【代金券抵扣】  说明： 实付金额计算公式得到的金额值等于amount - coupon_amount的差值。按账期类型查询时不返回计算公式。

        :return: The formula of this ResFeeRecordV2.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        r"""Sets the formula of this ResFeeRecordV2.

        实付金额计算公式。当前只包含如下场景： 按需非线性定价{使用量}【使用量】/{单位转化率}【单位转换】*{单价}【单价】-{优惠金额}【优惠金额】-{抹零金额}【抹零金额】-{代金券抵扣}【代金券抵扣】 按需线性定价{使用量}【使用量】/{单位转化率}【单位转换】*{线性大小}【规格】*{单价}【单价】-{优惠金额}【优惠金额】-{抹零金额}【抹零金额】-{代金券抵扣}【代金券抵扣】 包年包月新购和续订非线性定价{周期数}【周期数】/{周期转化率}【周期转换】*{单价}【单价】-{优惠金额}【优惠金额】-{代金券抵扣}【代金券抵扣】 包年包月新购和续订线性定价{周期数}【周期数】/{周期转化率}【周期转换】*{线性大小}【规格】*{单价}【单价】-{优惠金额}【优惠金额】-{代金券抵扣}【代金券抵扣】 包年包月（一次性）新购和续订非线性定价{单价}【单价】-{优惠金额}【优惠金额】-{代金券抵扣}【代金券抵扣】 包年包月（一次性）新购和续订线性定价{线性大小}【规格】*{单价}【单价】-{优惠金额}【优惠金额】-{代金券抵扣}【代金券抵扣】  说明： 实付金额计算公式得到的金额值等于amount - coupon_amount的差值。按账期类型查询时不返回计算公式。

        :param formula: The formula of this ResFeeRecordV2.
        :type formula: str
        """
        self._formula = formula

    @property
    def sub_service_type_code(self):
        r"""Gets the sub_service_type_code of this ResFeeRecordV2.

        整机的子云服务的自身的云服务类型编码。

        :return: The sub_service_type_code of this ResFeeRecordV2.
        :rtype: str
        """
        return self._sub_service_type_code

    @sub_service_type_code.setter
    def sub_service_type_code(self, sub_service_type_code):
        r"""Sets the sub_service_type_code of this ResFeeRecordV2.

        整机的子云服务的自身的云服务类型编码。

        :param sub_service_type_code: The sub_service_type_code of this ResFeeRecordV2.
        :type sub_service_type_code: str
        """
        self._sub_service_type_code = sub_service_type_code

    @property
    def sub_service_type_name(self):
        r"""Gets the sub_service_type_name of this ResFeeRecordV2.

        整机的子云服务的自身的云服务类型名称。

        :return: The sub_service_type_name of this ResFeeRecordV2.
        :rtype: str
        """
        return self._sub_service_type_name

    @sub_service_type_name.setter
    def sub_service_type_name(self, sub_service_type_name):
        r"""Sets the sub_service_type_name of this ResFeeRecordV2.

        整机的子云服务的自身的云服务类型名称。

        :param sub_service_type_name: The sub_service_type_name of this ResFeeRecordV2.
        :type sub_service_type_name: str
        """
        self._sub_service_type_name = sub_service_type_name

    @property
    def sub_resource_type_code(self):
        r"""Gets the sub_resource_type_code of this ResFeeRecordV2.

        整机的子云服务的自身的资源类型编码。

        :return: The sub_resource_type_code of this ResFeeRecordV2.
        :rtype: str
        """
        return self._sub_resource_type_code

    @sub_resource_type_code.setter
    def sub_resource_type_code(self, sub_resource_type_code):
        r"""Sets the sub_resource_type_code of this ResFeeRecordV2.

        整机的子云服务的自身的资源类型编码。

        :param sub_resource_type_code: The sub_resource_type_code of this ResFeeRecordV2.
        :type sub_resource_type_code: str
        """
        self._sub_resource_type_code = sub_resource_type_code

    @property
    def sub_resource_type_name(self):
        r"""Gets the sub_resource_type_name of this ResFeeRecordV2.

        整机的子云服务的自身的资源类型名称。

        :return: The sub_resource_type_name of this ResFeeRecordV2.
        :rtype: str
        """
        return self._sub_resource_type_name

    @sub_resource_type_name.setter
    def sub_resource_type_name(self, sub_resource_type_name):
        r"""Sets the sub_resource_type_name of this ResFeeRecordV2.

        整机的子云服务的自身的资源类型名称。

        :param sub_resource_type_name: The sub_resource_type_name of this ResFeeRecordV2.
        :type sub_resource_type_name: str
        """
        self._sub_resource_type_name = sub_resource_type_name

    @property
    def sub_resource_id(self):
        r"""Gets the sub_resource_id of this ResFeeRecordV2.

        整机的子云服务的自身的资源ID，资源标识。（如果为预留实例，则为预留实例标识）

        :return: The sub_resource_id of this ResFeeRecordV2.
        :rtype: str
        """
        return self._sub_resource_id

    @sub_resource_id.setter
    def sub_resource_id(self, sub_resource_id):
        r"""Sets the sub_resource_id of this ResFeeRecordV2.

        整机的子云服务的自身的资源ID，资源标识。（如果为预留实例，则为预留实例标识）

        :param sub_resource_id: The sub_resource_id of this ResFeeRecordV2.
        :type sub_resource_id: str
        """
        self._sub_resource_id = sub_resource_id

    @property
    def sub_resource_name(self):
        r"""Gets the sub_resource_name of this ResFeeRecordV2.

        整机的子云服务的自身的资源名称，资源标识。（如果为预留实例，则为预留实例标识）

        :return: The sub_resource_name of this ResFeeRecordV2.
        :rtype: str
        """
        return self._sub_resource_name

    @sub_resource_name.setter
    def sub_resource_name(self, sub_resource_name):
        r"""Sets the sub_resource_name of this ResFeeRecordV2.

        整机的子云服务的自身的资源名称，资源标识。（如果为预留实例，则为预留实例标识）

        :param sub_resource_name: The sub_resource_name of this ResFeeRecordV2.
        :type sub_resource_name: str
        """
        self._sub_resource_name = sub_resource_name

    @property
    def consume_time(self):
        r"""Gets the consume_time of this ResFeeRecordV2.

        |参数名称：消费时间| |参数约束及描述：消费时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ。包周期、预留实例预付为交易时间，按需、预留实例按时计费为话单生失效时间。 说明：当statistic_type=3时有效。|

        :return: The consume_time of this ResFeeRecordV2.
        :rtype: str
        """
        return self._consume_time

    @consume_time.setter
    def consume_time(self, consume_time):
        r"""Sets the consume_time of this ResFeeRecordV2.

        |参数名称：消费时间| |参数约束及描述：消费时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ。包周期、预留实例预付为交易时间，按需、预留实例按时计费为话单生失效时间。 说明：当statistic_type=3时有效。|

        :param consume_time: The consume_time of this ResFeeRecordV2.
        :type consume_time: str
        """
        self._consume_time = consume_time

    @property
    def relative_order_id(self):
        r"""Gets the relative_order_id of this ResFeeRecordV2.

        |参数名称：客户订单关联的订单ID| |参数约束及描述：客户订单关联的订单ID，包年/包月资源的使用记录该字段才有值，按需资源则为空。当order_id为组合交易订单时，该字段才有值，当查询为普通订单时，此字段返回为空。|

        :return: The relative_order_id of this ResFeeRecordV2.
        :rtype: str
        """
        return self._relative_order_id

    @relative_order_id.setter
    def relative_order_id(self, relative_order_id):
        r"""Sets the relative_order_id of this ResFeeRecordV2.

        |参数名称：客户订单关联的订单ID| |参数约束及描述：客户订单关联的订单ID，包年/包月资源的使用记录该字段才有值，按需资源则为空。当order_id为组合交易订单时，该字段才有值，当查询为普通订单时，此字段返回为空。|

        :param relative_order_id: The relative_order_id of this ResFeeRecordV2.
        :type relative_order_id: str
        """
        self._relative_order_id = relative_order_id

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
        if not isinstance(other, ResFeeRecordV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
